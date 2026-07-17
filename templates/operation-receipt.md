# Operation Receipt

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
