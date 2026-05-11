import { defineConfig, passthroughImageService } from 'astro/config';
import { rehypeFigures } from './src/lib/rehype-figures.mjs';

export default defineConfig({
  site: 'https://simonsorkin.com',
  image: {
    service: passthroughImageService(),
  },
  markdown: {
    rehypePlugins: [rehypeFigures],
  },
});
