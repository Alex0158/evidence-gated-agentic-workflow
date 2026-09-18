import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { runInNewContext } from 'node:vm';

// Exercise the built browser script; this is a routing contract check, not browser QA.
const start = await readFile('dist/start/index.html', 'utf8');
const scripts = [...start.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/g)];
const profileData = scripts.find(([, attributes]) => attributes.includes('data-profile-data'))?.[2];
const routingScript = scripts.find(([, , body]) => body.includes("querySelectorAll('[data-classifier]')"))?.[2];
assert.ok(profileData && routingScript, 'Built classifier data and executable script must exist');
const profiles = JSON.parse(profileData);
const inputNames = new Set([...start.matchAll(/<input\b[^>]*name="([^"]+)"/g)].map((match) => match[1]));

function render(initial) {
  const answers = { ...initial };
  const nodes = new Map();
  const listeners = new Map();
  const root = {
    nextElementSibling: { textContent: profileData },
    querySelector(selector) {
      const input = selector.match(/^input\[name="([^"]+)"\]:checked$/);
      if (input) {
        assert.ok(inputNames.has(input[1]), `Missing rendered input: ${input[1]}`);
        return { value: answers[input[1]] ? 'yes' : 'no' };
      }
      assert.match(selector, /^\[data-(?:mode-name|mode-summary|mode-gates|mode-link|small-edit)\]$/);
      if (!nodes.has(selector)) nodes.set(selector, {});
      return nodes.get(selector);
    },
    addEventListener(event, listener) { listeners.set(event, listener); },
  };
  runInNewContext(routingScript, {
    document: { querySelectorAll: () => [root] },
    localStorage: { setItem() {} },
  }, { timeout: 1000 });
  return { answers, nodes, change: () => listeners.get('change')() };
}

const cases = [
  ['bounded read-only question', {}, 'Fast'],
  ['ordinary implementation', { write: true }, 'Standard'],
  ['local wording/format correction', { write: true, small: true }, 'Fast'],
  ['cross-layer edit despite small size', { write: true, small: true, cross: true }, 'Standard'],
  ['cross-layer investigation', { cross: true }, 'Standard'],
  ['production/publication overrides small edit', { external: true, write: true, small: true }, 'Assured'],
  ['local auth repair overrides small edit', { irreversible: true, write: true, small: true }, 'Assured'],
  ['unclear identity overrides small edit', { identity: true, write: true, small: true }, 'Assured'],
];
for (const [label, answers, expected] of cases) {
  const { nodes } = render(answers);
  assert.equal(nodes.get('[data-mode-name]').textContent, expected, label);
  assert.equal(nodes.get('[data-small-edit]').hidden, !answers.write, `${label}: conditional question`);
  assert.ok(nodes.get('[data-mode-link]').href.endsWith(`?mode=${expected.toLowerCase()}`), `${label}: handoff route`);
}

const transition = render({ write: true, small: true });
transition.answers.identity = true;
transition.change();
assert.equal(transition.nodes.get('[data-mode-name]').textContent, 'Assured', 'New identity uncertainty must escalate');
transition.answers.identity = false;
transition.answers.write = false;
transition.change();
assert.equal(transition.nodes.get('[data-mode-name]').textContent, 'Fast');
assert.equal(transition.nodes.get('[data-small-edit]').hidden, true, 'Stale small-edit answer must not keep the question visible');

const escapeHtml = (text) => text.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;');
for (const profile of profiles) {
  const html = await readFile(`dist/playbooks/${profile.slug}/index.html`, 'utf8');
  for (const gate of profile.minimum) assert.ok(html.includes(escapeHtml(gate)), `${profile.slug}: playbook/classifier gate drift`);
  assert.ok(html.includes('/learn/verification-and-closure/#8-closure-budget'), `${profile.slug}: closure guidance link`);
}

const system = await readFile('dist/system/index.html', 'utf8');
const loopData = system.match(/<script\b[^>]*data-loop-data[^>]*>([\s\S]*?)<\/script>/)?.[1];
assert.ok(loopData, 'Built loop data must exist');
for (const stage of JSON.parse(loopData)) {
  const [route, anchor] = stage.source.split('#');
  assert.ok(route.startsWith('/evidence-gated-agentic-workflow/learn/'), 'Loop guidance must stay in the reference library');
  const html = await readFile(`dist/${route.slice('/evidence-gated-agentic-workflow/'.length)}index.html`, 'utf8');
  if (anchor) assert.ok(html.includes(`id="${decodeURIComponent(anchor)}"`), `${stage.name}: owning-section anchor`);
}

console.log(`Workflow routing passed: ${cases.length} scenarios, 2 state transitions, 3 shared profiles, 13 guidance routes.`);
