import { dirname, relative, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('../', import.meta.url));
const base = '/evidence-gated-agentic-workflow';
const sourceRoutes = {
  'docs/01-core-principles.md': 'learn/core-principles/',
  'docs/02-operating-loop.md': 'learn/operating-loop/',
  'docs/03-ai-collaboration-stack.md': 'learn/ai-collaboration-stack/',
  'docs/04-methodology-positioning.md': 'learn/methodology-positioning/',
  'docs/05-risk-authority-and-decision-rights.md': 'learn/risk-and-authority/',
  'docs/06-verification-delivery-and-closure.md': 'learn/verification-and-closure/',
  'docs/07-system-evolution.md': 'learn/system-evolution/',
  'docs/08-adoption-guide.md': 'learn/adoption-guide/',
  'explorations/README.md': 'explorations/',
  'explorations/ai-development-factory.md': 'explorations/ai-development-factory/',
};

// Native MDAST adapter: keep clone links portable, changing only rendered URLs.
function resolveLink(node, ctx) {
  if (!ctx.fileURL || typeof node.url !== 'string') return;
  const match = node.url.match(/^([^?#]+\.md)([?#].*)?$/i);
  if (!match || /^(?:[a-z][a-z\d+.-]*:|\/)/i.test(node.url)) return;
  const target = relative(root, resolve(dirname(fileURLToPath(ctx.fileURL)), decodeURIComponent(match[1]))).split('\\').join('/');
  if (target.startsWith('../')) return;
  const route = sourceRoutes[target] ?? (target.startsWith('templates/') && target !== 'templates/README.md'
    ? `toolkit/${target.slice('templates/'.length, -3)}/` : undefined);
  const suffix = match[2] ?? '';
  ctx.setProperty(node, 'url', route ? `${base}/${route}${suffix}`
    : `https://github.com/Alex0158/evidence-gated-agentic-workflow/blob/main/${target.split('/').map(encodeURIComponent).join('/')}${suffix}`);
}

export default { name: 'public-source-links', link: resolveLink, definition: resolveLink };
