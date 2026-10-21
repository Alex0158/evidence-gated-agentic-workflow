# Connector / MCP / App Capability Gate

> **內容身份：** Reference — 舊 Connector 能力診斷欄位，不是新增 template ID。
> **適用範圍：** 只在相關外部工具任務按需參考；不要求每次工作填完整 ladder。
> **現行 owner：** [工具能力與身份](../項目文件/00-協作與執行/規則與標準/工作規則與標準.md#工具能力與身份) · [項目工程入口](../項目文件/00-協作與執行/項目工程入口.md) · [調查 Runbook](../項目文件/00-協作與執行/Runbooks/調查與分析.md)

## Intended operation

- Mode: `<capability check / read / write / publish>`
- Target system: `<generic system>`
- Exact target: `<workspace/project/record placeholder>`

## Capability ladder

- [ ] Configured/installed
- [ ] Exposed in current task
- [ ] Authenticated
- [ ] Correct identity/workspace
- [ ] Exact target readable
- [ ] Required write capability available
- [ ] Mutation explicitly authorized

## Read-only smoke

- Stable probe: `<search/fetch/status>`
- Expected result: `<...>`
- Actual result: `<...>`

## Mutation preflight

- Identity rechecked: `<evidence>`
- Scope/authority: `<grant>`
- Dry-run/preview/count guard: `<result>`
- Retry safety/reconciliation: `<if service semantics are verified: idempotency key + scope/TTL/request-match; otherwise stable business identity + authoritative readback>`
- Stop condition: `<...>`

## Post-write

- Operation receipt: `<...>`
- Readback: `<...>`
- Outcome: `<confirmed success / failure / partial-mixed / unknown>`
- Cleanup/remediation: `<...>`
