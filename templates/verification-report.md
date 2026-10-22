# Verification Report

> **內容身份：** Reference — 舊 verification-report 欄位格式，不新增 run result owner。
> **適用範圍：** 本次驗證程序由 Runbook 承接，結果由 VR／native run 記錄；舊 closure labels 不作 active enum。
> **現行 owner：** [驗證功能 Runbook](../項目文件/00-協作與執行/Runbooks/驗證功能.md) · [驗證紀錄範本](../文件模板/驗證紀錄範本.md) · [交付紀錄範本](../文件模板/交付紀錄範本.md)

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
