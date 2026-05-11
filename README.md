# simonsorkin.com

Source for [simonsorkin.com](https://simonsorkin.com).

## Build

```sh
uv sync
uv run python build.py
```

Output goes to `site/`. Open `site/index.html` in a browser to preview.

## Layout

- `posts/<slug>/post.md` — post sources with YAML front-matter and inline images
- `templates/` — Jinja2 templates for the index and post pages
- `build.py` — generator entry point
