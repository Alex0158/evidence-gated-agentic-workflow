# Handoff

> **內容身份：** Reference — 舊 handoff 欄位格式，不新增平行 handoff 狀態表。
> **適用範圍：** 版本交付依 Runbook 與 REL；一般任務交接沿用原 Task。
> **現行 owner：** [版本交付 Runbook](../項目文件/00-協作與執行/Runbooks/版本交付.md) · [交付紀錄範本](../文件模板/交付紀錄範本.md) · [工作任務範本](../文件模板/工作任務範本.md)

## Objective

`<target outcome>`

## Baseline → target

- Baseline: `<current state>`
- Target: `<intended state>`

## Artifact and provenance

- Version/commit/checksum: `<...>`
- Source/artifact binding: `<...>`
- Changed: `<...>`
- Unchanged/non-goals: `<...>`

## Decision rights

- Operator: `<...>`
- Approver: `<...>`
- Verification/evidence-return owner: `<...>`
- Closure owner: `<...>`

## Prerequisites and boundary

- Environment/account/target: `<...>`
- Required authority: `<...>`
- Stop conditions: `<...>`

## Steps

1. `<exact action>`
2. `<readback>`
3. `<return evidence>`

## Verification

若交接需要沿用先前驗證，附上 [Verification Report 的 Reused evidence](verification-report.md#reused-evidence--only-when-applicable) 或等價記錄，說明原 source／claim、本次差異及保留／重驗理由；首次驗證可省略。

- Expected evidence: `<...>`
- Success condition: `<...>`
- Known risks: `<...>`

## Rollback/remediation

`<exact path, owner and trigger>`

## Lifecycle state

- [ ] Artifact ready
- [ ] Delivered
- [ ] Executed/adopted
- [ ] Evidence returned
- [ ] Verified
- [ ] Closed
