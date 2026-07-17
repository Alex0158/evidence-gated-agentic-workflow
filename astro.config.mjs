import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://alex0158.github.io',
  base: '/evidence-gated-agentic-workflow',
  trailingSlash: 'always',
  devToolbar: { enabled: false },
  integrations: [sitemap()],
  markdown: {
    shikiConfig: {
      theme: 'github-dark-default',
      wrap: true,
    },
  },
});
