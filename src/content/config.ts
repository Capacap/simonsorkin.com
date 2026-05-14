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
      description: z.string(),
      project: z.string().optional(),
      project_url: z.string().url().optional(),
      stack: z.array(z.string()).optional(),
      dek: z.string().optional(),
      lede: z.string().optional(),
      teaser: z.string().optional(),
      hero: z
        .object({
          image: image(),
          alt: z.string(),
          caption: z.string(),
        })
        .optional(),
    }),
});

export const collections = { posts };
