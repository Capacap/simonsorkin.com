# simonsorkin.com

Source for [simonsorkin.com](https://simonsorkin.com).

Built with [Astro](https://astro.build/).

## Develop

```sh
npm install
npm run dev
```

## Build

```sh
npm run build
```

Output goes to `dist/`.

## Layout

- `src/content/posts/<slug>/post.md` — post sources with YAML front-matter and inline images
- `src/content/config.ts` — content collection schema
- `src/layouts/Base.astro` — site shell and bio header
- `src/pages/` — routes (`/` and `/posts/<slug>`)
- `src/styles/global.css` — single global stylesheet
- `src/lib/rehype-figures.mjs` — pairs `![](img.png)` + `*caption*` into `<figure>`
