import { readFile, readdir } from 'node:fs/promises';
import { extname, join, posix, relative } from 'node:path';

const root = process.cwd();
const dist = join(root, 'dist');
const base = '/evidence-gated-agentic-workflow';
const failures = [];

async function walk(directory) {
  const entries = await readdir(directory, { withFileTypes: true });
  const files = await Promise.all(entries.map(async (entry) => {
    const path = join(directory, entry.name);
    return entry.isDirectory() ? walk(path) : [path];
  }));
  return files.flat();
}

const files = await walk(dist);
const outputFiles = new Set(files.map((file) => relative(dist, file).split('\\').join('/')));
const htmlFiles = [...outputFiles].filter((file) => file.endsWith('.html'));

const requiredOutputs = [
  'index.html',
  'start/index.html',
  'system/index.html',
  'system/evidence/index.html',
  'workbench/index.html',
  'codex/index.html',
  'learn/methodology-positioning/index.html',
  'toolkit/task-brief/index.html',
  'toolkit/codex-agents-example/index.html',
  'cases/remote-timeout/index.html',
  '404.html',
  'robots.txt',
  'sitemap-index.xml',
  'og-card.png',
];

for (const required of requiredOutputs) {
  if (!outputFiles.has(required)) failures.push(`Missing required build output: ${required}`);
}

const notFoundHtml = await readFile(join(dist, '404.html'), 'utf8');
if (!notFoundHtml.includes('name="robots" content="noindex, nofollow"')) failures.push('404.html must be noindex, nofollow');
if (notFoundHtml.includes('rel="canonical"')) failures.push('404.html must not publish a canonical URL');

const sitemapFiles = [...outputFiles].filter((file) => /^sitemap.*\.xml$/.test(file));
const sitemapText = (await Promise.all(sitemapFiles.map((file) => readFile(join(dist, file), 'utf8')))).join('\n');
if (sitemapText.includes('/404')) failures.push('Sitemap must not include the 404 route');

const ogCard = await readFile(join(dist, 'og-card.png'));
if (ogCard.readUInt32BE(16) !== 1200 || ogCard.readUInt32BE(20) !== 630) failures.push('og-card.png must be exactly 1200 x 630');

const idCache = new Map();
async function idsFor(htmlFile) {
  if (!idCache.has(htmlFile)) {
    const html = await readFile(join(dist, htmlFile), 'utf8');
    idCache.set(htmlFile, new Set([...html.matchAll(/\sid=["']([^"']+)["']/g)].map((match) => match[1])));
  }
  return idCache.get(htmlFile);
}

function targetFor(reference, fromFile) {
  const decoded = decodeURI(reference.replace(/&amp;/g, '&'));
  const hashIndex = decoded.indexOf('#');
  const queryIndex = decoded.indexOf('?');
  const cutIndexes = [hashIndex, queryIndex].filter((index) => index >= 0);
  const cutAt = cutIndexes.length ? Math.min(...cutIndexes) : decoded.length;
  const rawPath = decoded.slice(0, cutAt);
  const hash = hashIndex >= 0 ? decoded.slice(hashIndex + 1).split('?')[0] : '';

  let target;
  if (!rawPath) {
    target = fromFile;
  } else if (rawPath === base || rawPath.startsWith(`${base}/`)) {
    target = rawPath.slice(base.length).replace(/^\//, '');
  } else if (rawPath.startsWith('/')) {
    failures.push(`Root-absolute URL escapes configured base in ${fromFile}: ${reference}`);
    return null;
  } else {
    target = posix.normalize(posix.join(posix.dirname(fromFile), rawPath));
  }

  if (target.startsWith('../')) {
    failures.push(`Relative URL escapes build root in ${fromFile}: ${reference}`);
    return null;
  }

  if (!target || target.endsWith('/')) target = `${target}index.html`;
  else if (!extname(target)) target = `${target}/index.html`;

  return { target, hash: decodeURIComponent(hash) };
}

for (const htmlFile of htmlFiles) {
  const html = await readFile(join(dist, htmlFile), 'utf8');
  if (htmlFile !== '404.html') {
    const route = htmlFile === 'index.html' ? '' : htmlFile.replace(/index\.html$/, '');
    const expectedCanonical = `https://alex0158.github.io${base}/${route}`;
    if (!html.includes(`rel="canonical" href="${expectedCanonical}"`)) failures.push(`Missing or incorrect canonical URL in ${htmlFile}`);
  }
  const markup = html.replace(/<script\b[\s\S]*?<\/script>/gi, '').replace(/<style\b[\s\S]*?<\/style>/gi, '');
  const references = [...markup.matchAll(/(?:href|src)=["']([^"']+)["']/g)].map((match) => match[1]);
  for (const reference of references) {
    if (/^(?:https?:|mailto:|tel:|data:|blob:|javascript:|\/\/)/i.test(reference)) continue;
    const pathOnly = reference.split(/[?#]/)[0];
    if (pathOnly.startsWith(`${base}/`) && pathOnly !== `${base}/` && !extname(pathOnly) && !pathOnly.endsWith('/')) {
      failures.push(`Route URL is missing a trailing slash in ${htmlFile}: ${reference}`);
    }
    const resolved = targetFor(reference, htmlFile);
    if (!resolved) continue;
    if (!outputFiles.has(resolved.target)) {
      failures.push(`Broken local reference in ${htmlFile}: ${reference} -> ${resolved.target}`);
      continue;
    }
    if (resolved.hash && resolved.target.endsWith('.html')) {
      const ids = await idsFor(resolved.target);
      if (!ids.has(resolved.hash)) failures.push(`Missing anchor in ${htmlFile}: ${reference}`);
    }
  }
}

const contentManifest = await readFile(join(root, 'src/data/content.ts'), 'utf8');
const expectedSources = [
  ...(await readdir(join(root, 'docs'))).filter((name) => name.endsWith('.md')).map((name) => `docs/${name}`),
  ...(await readdir(join(root, 'templates'))).filter((name) => name.endsWith('.md') && name !== 'README.md').map((name) => `templates/${name}`),
  ...(await readdir(join(root, 'examples'), { withFileTypes: true })).filter((entry) => entry.isDirectory()).map((entry) => `examples/${entry.name}/README.md`),
  'integrations/codex/README.md',
  'integrations/codex/AGENTS.example.md',
];

for (const source of expectedSources) {
  if (!contentManifest.includes(`sourcePath: '${source}'`)) failures.push(`Canonical source is not represented by the site: ${source}`);
}

const leakPatterns = [
  ['absolute macOS user path', /\/Users\/[A-Za-z0-9._-]+\//],
  ['private Codex memory path', /\.codex\/memories\//i],
  ['private rollout path', /rollout_summaries\//i],
  ['private project identifier', /\b(?:JobPortal(?:2|3)?\.0|Muyan|Hanson)\b/i],
  ['GitHub-style access token', /\bgh[pousr]_[A-Za-z0-9]{20,}\b/],
];

for (const file of files.filter((file) => /\.(?:html|css|js|json|xml|txt|svg)$/i.test(file))) {
  const contents = await readFile(file, 'utf8');
  for (const [label, pattern] of leakPatterns) {
    if (pattern.test(contents)) failures.push(`Detected ${label} in ${relative(dist, file)}`);
  }
}

if (failures.length) {
  console.error(`Site validation failed with ${failures.length} issue(s):`);
  failures.forEach((failure) => console.error(`- ${failure}`));
  process.exit(1);
}

console.log(`Site validation passed: ${htmlFiles.length} HTML pages, ${outputFiles.size} build outputs, ${expectedSources.length} canonical sources.`);
