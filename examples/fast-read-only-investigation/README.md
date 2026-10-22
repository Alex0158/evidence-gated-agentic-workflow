# Example — Fast read-only investigation

> **內容身份：** Example — fictional read-only case; no real connector or product evidence。
> **適用範圍：** 只示範能力判讀；Fast profile 與 closure target 不成為普遍要求。
> **現行 owner：** [工具能力與身份](../../項目文件/00-協作與執行/規則與標準/工作規則與標準.md#工具能力與身份) · [調查 Runbook](../../項目文件/00-協作與執行/Runbooks/調查與分析.md)

## Task

「確認 sample knowledge connector 現在能否讀到 `Demo Handbook`。」

## Brief

- Objective：證明 current task 的 exact target 是否可讀。
- Scope：read-only；不修改 connector config、auth 或 target content。
- Source of truth：current tool exposure + live search/fetch result。
- Profile：Fast。
- Closure target：Answered。

## Evidence

1. Settings 顯示 connector configured：只能證明 config 存在。
2. Current task tool list 有 search/fetch：證明 surface exposed。
3. Search `Demo Handbook` 成功：證明 auth 與至少一個 search path 當下可用。
4. Fetch exact item 成功，title/ID 匹配：證明 target readable。

## Conclusion

```text
Verified: Demo Handbook 在本次 task 由正確 tool 成功 search + fetch。
Not claimed: write authority、其他 items、長期穩定性或官方已修復任何 intermittent issue。
```

## Why this closes

Claim 是 exact target 當下 read capability，evidence 同粒度。沒有為了「更完整」執行 write smoke。
