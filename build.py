"""Static blog generator.

Reads posts from posts/<slug>/post.md with YAML front-matter, renders each
into site/post-<slug>.html and a combined site/index.html. Copies any images
referenced by the body markdown into site/assets/.

Run: `uv run python build.py`. Output is always written relative to this
file, not the cwd.
"""

from __future__ import annotations

import re
import shutil
import sys
from dataclasses import dataclass
from datetime import date as date_cls
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader


REPO_ROOT = Path(__file__).resolve().parent
POSTS_DIR = REPO_ROOT / "posts"
TEMPLATES_DIR = REPO_ROOT / "templates"
OUTPUT_DIR = REPO_ROOT / "site"
ASSETS_OUTPUT_DIR = OUTPUT_DIR / "assets"

REQUIRED_FIELDS = {
    "title", "slug", "date", "read_time",
    "project_url", "stack", "description",
    "dek", "lede", "teaser", "hero",
}
HERO_REQUIRED = {"image", "alt", "caption"}

MD_EXTENSIONS = ["fenced_code", "attr_list"]

FIGURE_RE = re.compile(
    r'<p>\s*<img alt="([^"]*)" src="([^"]+)"\s*/?>\s*'
    r'(?:</p>\s*<p>\s*)?'
    r'<em>(.*?)</em>\s*</p>',
    re.DOTALL,
)
BODY_IMG_RE = re.compile(r'!\[[^\]]*\]\(([^)\s]+)\)')


def die(msg: str) -> None:
    print(f"build.py: {msg}", file=sys.stderr)
    sys.exit(1)


def render_md_block(text: str) -> str:
    """Render markdown as block content (preserves paragraph structure)."""
    return markdown.markdown(text.strip(), extensions=MD_EXTENSIONS, output_format="html5")


def render_md_inline(text: str) -> str:
    """Render markdown then strip the wrapping <p>...</p>, for single-paragraph fields."""
    html = render_md_block(text)
    if html.startswith("<p>") and html.endswith("</p>"):
        return html[3:-4]
    return html


def wrap_figures(html: str, slug_assets_prefix: str) -> str:
    """Merge ``<p><img/></p>`` + ``<p><em>caption</em></p>`` pairs into figures.

    Rewrites the src to point at the deployed assets path while doing so.
    """
    def replace(m: re.Match[str]) -> str:
        alt, src, caption = m.group(1), m.group(2), m.group(3)
        return (
            f'<figure>\n'
            f'      <img src="{slug_assets_prefix}{src}" alt="{alt}">\n'
            f'      <figcaption>{caption}</figcaption>\n'
            f'    </figure>'
        )
    return FIGURE_RE.sub(replace, html)


def rewrite_image_paths(html: str, slug_assets_prefix: str) -> str:
    """Rewrite any remaining bare <img src="x.png"> to point at the assets dir.

    The figure wrapper already handles paired image+caption; this catches images
    that aren't paired with a caption.
    """
    def replace(m: re.Match[str]) -> str:
        return f'<img src="{slug_assets_prefix}{m.group(1)}"'
    return re.sub(r'<img src="([^"/]+)"', replace, html)


def indent_body(html: str, indent: str = "    ") -> str:
    """Indent top-level block lines and separate them with blank lines.

    Lines starting at column 0 are treated as top-level blocks: indented and
    separated by a blank line. Continuation lines (already indented, e.g. the
    inner lines of a wrapped figure) pass through unchanged.
    """
    lines = html.rstrip("\n").split("\n")
    out: list[str] = []
    for line in lines:
        if line and not line[0].isspace():
            if out and out[-1].strip():
                out.append("")
            out.append(indent + line)
        else:
            out.append(line)
    return "\n".join(out)


def project_url_display(url: str) -> str:
    """Strip the protocol prefix for display, matching the existing site."""
    return re.sub(r'^https?://', '', url)


def format_date_display(d: date_cls) -> str:
    """Render dates as 'April 28, 2026' (matches the existing hand-rendered HTML)."""
    return f"{d.strftime('%B')} {d.day}, {d.year}"


@dataclass
class Post:
    slug: str
    title: str
    date: date_cls
    date_iso: str
    date_display: str
    read_time: int
    project: str | None
    project_url: str
    project_url_display: str
    stack: list[str]
    description: str
    dek_html: str
    lede_html: str
    teaser_html: str
    body_html: str
    hero_image: str
    hero_alt: str
    hero_caption_html: str
    images: list[str]
    post_dir: Path


def load_post(post_dir: Path) -> Post:
    md_path = post_dir / "post.md"
    raw = md_path.read_text(encoding="utf-8")

    if not raw.startswith("---\n"):
        die(f"{md_path}: file must start with '---' front-matter delimiter")
    parts = raw.split("---\n", 2)
    if len(parts) < 3:
        die(f"{md_path}: front-matter block is not closed by '---'")
    _, fm_text, body_md = parts

    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError as e:
        die(f"{md_path}: invalid YAML in front-matter: {e}")

    missing = REQUIRED_FIELDS - set(fm)
    if missing:
        die(f"{md_path}: missing required front-matter fields: {sorted(missing)}")

    date_val = fm["date"]
    if not isinstance(date_val, date_cls):
        die(f"{md_path}: 'date' must be an ISO date (YYYY-MM-DD), got {date_val!r}")

    slug = fm["slug"]
    if slug != post_dir.name:
        die(f"{md_path}: front-matter slug '{slug}' does not match directory name '{post_dir.name}'")

    hero = fm["hero"]
    if not isinstance(hero, dict):
        die(f"{md_path}: 'hero' must be a mapping with image/alt/caption")
    hero_missing = HERO_REQUIRED - set(hero)
    if hero_missing:
        die(f"{md_path}: hero missing required fields: {sorted(hero_missing)}")

    images = list(dict.fromkeys(BODY_IMG_RE.findall(body_md)))
    if hero["image"] not in images:
        images.append(hero["image"])
    for img in images:
        if not (post_dir / img).exists():
            die(f"{md_path}: references missing image '{img}'")

    # The deployed assets path is currently flat: assets/<filename>.
    assets_prefix = "assets/"
    body_html = render_md_block(body_md)
    body_html = wrap_figures(body_html, assets_prefix)
    body_html = rewrite_image_paths(body_html, assets_prefix)
    body_html = indent_body(body_html)

    teaser_html = render_md_block(fm["teaser"])
    teaser_html = indent_body(teaser_html)

    return Post(
        slug=slug,
        title=fm["title"],
        date=date_val,
        date_iso=date_val.isoformat(),
        date_display=format_date_display(date_val),
        read_time=int(fm["read_time"]),
        project=fm.get("project"),
        project_url=fm["project_url"],
        project_url_display=project_url_display(fm["project_url"]),
        stack=list(fm["stack"]),
        description=fm["description"],
        dek_html=render_md_inline(fm["dek"]),
        lede_html=render_md_inline(fm["lede"]),
        teaser_html=teaser_html,
        body_html=body_html,
        hero_image=f"{assets_prefix}{hero['image']}",
        hero_alt=hero["alt"],
        hero_caption_html=render_md_inline(hero["caption"]),
        images=images,
        post_dir=post_dir,
    )


def build() -> None:
    if not POSTS_DIR.exists():
        die(f"posts directory not found: {POSTS_DIR}")

    posts: list[Post] = []
    for post_dir in sorted(POSTS_DIR.iterdir()):
        if not post_dir.is_dir():
            continue
        if not (post_dir / "post.md").exists():
            continue
        posts.append(load_post(post_dir))

    if not posts:
        die(f"no posts found under {POSTS_DIR}")

    posts.sort(key=lambda p: p.date, reverse=True)

    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)
    ASSETS_OUTPUT_DIR.mkdir()

    for post in posts:
        for img in post.images:
            src = post.post_dir / img
            dst = ASSETS_OUTPUT_DIR / img
            if dst.exists():
                die(f"asset collision: two posts ship an image named '{img}'")
            shutil.copy2(src, dst)

    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=False,
        trim_blocks=False,
        lstrip_blocks=False,
        keep_trailing_newline=True,
    )

    post_tmpl = env.get_template("post.html.j2")
    for post in posts:
        html = post_tmpl.render(post=post)
        (OUTPUT_DIR / f"post-{post.slug}.html").write_text(html, encoding="utf-8")

    index_tmpl = env.get_template("index.html.j2")
    html = index_tmpl.render(posts=posts)
    (OUTPUT_DIR / "index.html").write_text(html, encoding="utf-8")

    print(f"built {len(posts)} post{'s' if len(posts) != 1 else ''} -> {OUTPUT_DIR.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    build()
