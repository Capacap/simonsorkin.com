import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export const GET: APIRoute = async ({ site }) => {
  const posts = await getCollection('posts');
  posts.sort((a, b) => b.data.date.getTime() - a.data.date.getTime());

  const base = (site?.toString() ?? 'https://simonsorkin.com/').replace(/\/$/, '');

  const lines = [
    '# Simon Sorkin',
    '',
    '> AI Engineer in Stockholm. Technical writeups on AI engineering, image processing, and computer vision projects.',
    '',
    'Simon Sorkin (Capacap) is an AI Engineer in Stockholm, open to full-time roles. This site collects writing on his projects.',
    '',
    '## Posts',
    '',
    ...posts.map((p) => `- [${p.data.title}](${base}/posts/${p.id}): ${p.data.description}`),
    '',
    '## Optional',
    '',
    `- [Full content as markdown](${base}/llms-full.txt): all posts concatenated`,
    '',
  ];

  return new Response(lines.join('\n'), {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
};
