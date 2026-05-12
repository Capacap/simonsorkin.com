import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export const GET: APIRoute = async ({ site }) => {
  const base = (site?.toString() ?? 'https://simonsorkin.com/').replace(/\/$/, '');
  const posts = await getCollection('posts');

  const urls = [
    { loc: `${base}/`, lastmod: null as string | null },
    ...posts.map((p) => ({
      loc: `${base}/posts/${p.id}`,
      lastmod: p.data.date.toISOString().slice(0, 10),
    })),
  ];

  const body =
    '<?xml version="1.0" encoding="UTF-8"?>\n' +
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    urls
      .map(
        (u) =>
          `  <url>\n    <loc>${u.loc}</loc>` +
          (u.lastmod ? `\n    <lastmod>${u.lastmod}</lastmod>` : '') +
          `\n  </url>`,
      )
      .join('\n') +
    '\n</urlset>\n';

  return new Response(body, {
    headers: { 'Content-Type': 'application/xml; charset=utf-8' },
  });
};
