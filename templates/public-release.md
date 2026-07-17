# Public Release Gate

## Scope and ownership

- Audience/purpose: `<...>`
- Exact public allowlist: `<files>`
- Explicit exclusions: `<private evidence/history/assets>`
- Owner and publication authority: `<...>`
- License/attribution: `<...>`

## Clean export

- [ ] Built in a new directory with clean Git history
- [ ] No private `.git`, hidden files, logs, exports, attachments or symlinks
- [ ] Examples use synthetic placeholders only
- [ ] README states scope, non-goals, status and license

## Privacy / secrets

- [ ] No local absolute paths
- [ ] No credentials, env values, cookies or auth state
- [ ] No personal/customer/supplier/order/account/workspace identifiers
- [ ] No raw conversations, Memory, session/rollout IDs or audit notes
- [ ] Automated scan and manual contextual review passed
- [ ] Any discovered credential was revoked/rotated before history cleanup

## Content QA

- [ ] Markdown syntax/lint passed
- [ ] Relative links and anchors passed
- [ ] Mermaid renders on GitHub
- [ ] External links reviewed
- [ ] License and third-party attribution reviewed
- [ ] Claim boundaries and practitioner/project-defined terms are explicit

## Git and remote

- [ ] Exact files staged; cached diff reviewed
- [ ] Commit contains only public allowlist
- [ ] Correct GitHub identity and owner verified live
- [ ] Remote is new/empty; no force push or unrelated history
- [ ] Remote visibility verified
- [ ] Local and remote HEAD SHA match

## Public closure

- [ ] README/license render checked in GitHub UI
- [ ] Anonymous/incognito access verified
- [ ] No links depend on private systems
- [ ] Main protection/ruleset configured after bootstrap
- [ ] Clean clone passes the same QA
