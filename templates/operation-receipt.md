# Operation Receipt

> **內容身份：** Reference — 舊 provider receipt 欄位提示，不新增通用 operation ledger。
> **適用範圍：** 只在有外部操作時按需參考；未知結果規則回工作標準，receipt／逐項結果留在原 Task、REL 或服務紀錄。
> **現行 owner：** [外部操作、授權時點與未知結果](../項目文件/00-協作與執行/規則與標準/工作規則與標準.md#外部操作授權時點與未知結果) · [工作任務範本](../文件模板/工作任務範本.md) · [交付紀錄範本](../文件模板/交付紀錄範本.md)

## Dispatch

- Operation ID: `<stable ID>`
- Grant ID/snapshot: `<...>`
- Target: `<...>`
- Mutation: `<...>`
- Idempotency support: `<verified service contract / unsupported / unknown>`
- Idempotency key and semantics: `<if supported: key + scope/TTL/request-match/replay behavior>`
- Stable business identity: `<fallback reconciliation identity>`
- Dispatched at: `<...>`

## Immediate response

- Tool/service response: `<minimal non-sensitive summary>`
- Receipt/reference: `<...>`
- Connection outcome: `<normal/timeout/disconnect>`

## Reconciliation

- Authoritative readback method: `<...>`
- Consistency window: `<if known>`
- Per-item result: `<success/failure/unknown>`
- Retry/replay: `<if supported, same key and contract result; otherwise no blind retry>`

## Final operation state

- [ ] Confirmed success
- [ ] Confirmed failure
- [ ] Partial-mixed
- [ ] Outcome unknown

Evidence: `<...>`

只有在 target service 的 contract 已核實時，idempotency key 才能降低 duplicate risk；它不能 undo mutation，也不保證 exactly-once delivery。

## Next authority

- New mutation allowed: `<yes/no; grant>`
- Verification owner: `<...>`
- Compensation/remediation: `<...>`
