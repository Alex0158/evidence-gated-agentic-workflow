# Investigation

> **內容身份：** Reference — 舊 investigation 欄位格式，不新增預設調查表。
> **適用範圍：** 調查程序由現行 Runbook 承接；結論留既有 Task／調查摘要。
> **現行 owner：** [調查與分析 Runbook](../項目文件/00-協作與執行/Runbooks/調查與分析.md) · [工作任務範本](../文件模板/工作任務範本.md)

## Question

`<要回答的 current-state 或 root-cause 問題>`

## Boundaries

- Read-only surfaces: `<targets>`
- Explicitly excluded mutations: `<writes/restarts/deploys/etc.>`
- Owning authority: `<source>`

## Hypotheses

| Hypothesis | Supporting evidence | Falsifier | Status |
| --- | --- | --- | --- |
| `<H1>` | `<evidence>` | `<what disproves it>` | Unknown |

## Evidence plan

1. `<lowest-cost, highest-decision-impact check>`
2. `<cross-layer check if needed>`
3. `<live proof if current state matters>`

## Findings

- Verified: `<directly proven>`
- Inferred: `<reasoned, not directly proven>`
- Unknown/unavailable: `<gap and why>`

## Root cause / current conclusion

`<one sentence; match claim to evidence>`

## Next safe action

`<recommendation; do not implement unless authorized>`
