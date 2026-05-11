import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const posts = defineCollection({
  loader: glob({
    pattern: '**/post.md',
    base: './src/content/posts',
    generateId: ({ entry }) => entry.replace(/\/post\.md$/, ''),
  }),
  schema: ({ image }) =>
    z.object({
      title: z.string(),
      slug: z.string(),
      date: z.date(),
      read_time: z.number().int().positive(),
      project: z.string().optional(),
      project_url: z.string().url(),
      stack: z.array(z.string()),
      description: z.string(),
      dek: z.string(),
      lede: z.string(),
      teaser: z.string(),
      hero: z.object({
        image: image(),
        alt: z.string(),
        caption: z.string(),
      }),
    }),
});

export const collections = { posts };
