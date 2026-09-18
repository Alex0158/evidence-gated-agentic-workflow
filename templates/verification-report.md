# Verification Report

## Conclusion

`<one sentence with exact closure level>`

## Executed

| Check | Surface | Result | Evidence supports |
| --- | --- | --- | --- |
| `<command/readback/test>` | `<static/targeted/runtime/etc.>` | `<pass/fail>` | `<claim limit>` |

## Not executed

| Check | Why not | Consequence |
| --- | --- | --- |
| `<check>` | `<gate/time/scope>` | `<remaining unknown>` |

## Evidence status

### Reused evidence — only when applicable

首次驗證或簡單 readback 可省略本段；沿用先前結果時，依[來源變更後的影響判斷](../docs/06-verification-delivery-and-closure.md#來源變更後哪些驗證仍可沿用)填寫。不要將沿用結果列為本次 Executed。

- Original evidence, source/environment and claim: `<reference and scope>`
- Current differences and affected inputs: `<diff and semantic dependencies>`
- Retain / revalidate decision: `<reason; new checks belong in Executed above>`
- Remaining uncertainty / owner: `<...>`

### Current assessment

- Verified: `<...>`
- Inferred: `<...>`
- Unknown: `<...>`

## Gate / blocker

`<new authority, identity, environment or external action required>`

## Closure

- Level: `<answered/diagnosed/implemented/integrated/runtime-verified/delivered/closed>`
- Residual risk: `<...>`
- Risk owner / next condition: `<...>`
- Mutating verification/rollback authorization: `<...>`
