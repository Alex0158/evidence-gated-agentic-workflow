import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import { satteri } from '@astrojs/markdown-satteri';
import sourceLinks from './scripts/remark-source-links.mjs';

export default defineConfig({
  site: 'https://alex0158.github.io',
  base: '/evidence-gated-agentic-workflow',
  trailingSlash: 'always',
  devToolbar: { enabled: false },
  integrations: [sitemap()],
  markdown: {
    processor: satteri({ mdastPlugins: [sourceLinks] }),
    shikiConfig: {
      theme: 'github-dark-default',
      wrap: true,
    },
  },
});
