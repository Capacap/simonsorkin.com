import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export const GET: APIRoute = async ({ site }) => {
  const posts = await getCollection('posts');
  posts.sort((a, b) => b.data.date.getTime() - a.data.date.getTime());

  const base = (site?.toString() ?? 'https://simonsorkin.com/').replace(/\/$/, '');

  const preamble = [
    '# Simon Sorkin — Writing',
    '',
    'Technical writeups by Simon Sorkin (Capacap), AI Engineer in Stockholm.',
    `Site: ${base}`,
    '',
  ].join('\n');

  const sections = posts.map((p) => {
    const date = p.data.date.toISOString().slice(0, 10);
    const headerLines = [
      `# ${p.data.title}`,
      '',
      `Source: ${base}/posts/${p.id}`,
      `Date: ${date}`,
    ];
    if (p.data.project_url) headerLines.push(`Project: ${p.data.project_url}`);
    if (p.data.stack && p.data.stack.length > 0) {
      headerLines.push(`Stack: ${p.data.stack.join(', ')}`);
    }
    headerLines.push('', p.data.lede ?? p.data.description, '');
    return headerLines.join('\n') + (p.body ?? '');
  });

  const body = preamble + '\n---\n\n' + sections.join('\n\n---\n\n');

  return new Response(body, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
};
