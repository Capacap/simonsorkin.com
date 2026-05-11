/**
 * Wrap markdown image+caption pairs in <figure>/<figcaption>.
 *
 * The source convention is plain markdown (no MDX, no custom directives):
 *
 *     ![alt](image.png)
 *     *caption*
 *
 * Two rendered shapes are accepted:
 *   - One <p> containing <img> followed by <em> (image+caption on adjacent
 *     lines in the source). This is what remark produces.
 *   - Two consecutive <p>s — first contains only <img>, second contains
 *     only <em> (image and caption separated by a blank line).
 */
export function rehypeFigures() {
  return (tree) => {
    if (!tree || !Array.isArray(tree.children)) return;
    const out = [];
    let i = 0;
    while (i < tree.children.length) {
      const cur = tree.children[i];
      const nxt = tree.children[i + 1];

      const single = singleParagraphFigure(cur);
      if (single) {
        out.push(single);
        i += 1;
        continue;
      }

      const imgInFirst = soleChild(cur, 'p', 'img');
      const emInSecond = soleChild(nxt, 'p', 'em');
      if (imgInFirst && emInSecond) {
        out.push(makeFigure(imgInFirst, emInSecond.children));
        i += 2;
        continue;
      }

      out.push(cur);
      i += 1;
    }
    tree.children = out;
  };
}

function singleParagraphFigure(node) {
  if (!node || node.type !== 'element' || node.tagName !== 'p') return null;
  const real = stripWhitespace(node.children || []);
  if (real.length !== 2) return null;
  const [a, b] = real;
  if (a.type !== 'element' || a.tagName !== 'img') return null;
  if (b.type !== 'element' || b.tagName !== 'em') return null;
  return makeFigure(a, b.children);
}

function makeFigure(img, captionChildren) {
  return {
    type: 'element',
    tagName: 'figure',
    properties: {},
    children: [
      { ...img },
      {
        type: 'element',
        tagName: 'figcaption',
        properties: {},
        children: captionChildren,
      },
    ],
  };
}

function soleChild(node, wrapperTag, innerTag) {
  if (!node || node.type !== 'element' || node.tagName !== wrapperTag) return null;
  const real = stripWhitespace(node.children || []);
  if (real.length !== 1) return null;
  const inner = real[0];
  if (inner.type !== 'element' || inner.tagName !== innerTag) return null;
  return inner;
}

function stripWhitespace(arr) {
  return arr.filter((c) => !(c.type === 'text' && /^\s*$/.test(c.value)));
}
