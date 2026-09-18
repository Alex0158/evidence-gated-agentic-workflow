# Public Release Gate

## Release mode

選擇本次模式；只填適用分支及共用 checks，其他項目標明 N/A 及原因。

- [ ] A — 首次建立公開 repository（可包含從私人來源抽取的通用內容）
- [ ] B — 更新既有公開 repository

兩種模式均須去除私人來源及未授權內容。既有 repo 加入新的抽取內容仍使用 B，不因此重建 repository 或改寫 history。

## Scope and ownership

- Audience/purpose: `<...>`
- Exact public allowlist: `<files>`
- Explicit exclusions: `<private evidence/history/assets>`
- Owner and publication authority: `<...>`
- License/attribution: `<...>`

## A — First public repository only

- [ ] Built in a new directory with clean Git history
- [ ] New/empty destination remote verified; no unrelated history imported
- [ ] Main protection/ruleset configured after bootstrap under the approved repository policy

## B — Existing public repository only

- [ ] Existing remote, branch, visibility and intended baseline verified
- [ ] Exact diff reviewed; unrelated work and existing history preserved
- [ ] Applicable branch rules, CI and deployment effects identified

## Shared content boundary

- [ ] No private Git metadata, unreviewed hidden files, logs, exports, attachments or symlink targets
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
- [ ] Push targets the approved remote/branch without force push or unrelated changes
- [ ] Remote visibility verified
- [ ] Local and remote HEAD SHA match

## Public closure

- [ ] README/license render checked in GitHub UI
- [ ] Anonymous/incognito access verified
- [ ] No links depend on private systems
- [ ] Clean clone passes the same QA
