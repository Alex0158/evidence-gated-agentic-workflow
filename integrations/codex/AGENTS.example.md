# Project Agent Guide

## Communication

- 預設先給一句結論，再補會改變 decision 或 next step 的 evidence。
- 重要結論區分 Verified、Inferred、Unknown。
- 多步任務在第一次 tool call 前提供簡短進度更新。

## Source of truth

- 開始前識別 owning repository、authoritative docs 與 current runtime/data source。
- Current-state 問題不得只由 Memory 或歷史文件裁決。
- Docs 與 code/runtime 衝突時，回報 mismatch、owner、freshness 與 correction path。

## Boundaries

- 修改前確認 repository、target、operator 與 mutation authority。
- 保留 unrelated dirty changes；只 stage exact files。
- 未明確授權，不做 external publication、production write、delete 或 irreversible action。

## Execution loop

```text
objective → boundary → evidence → smallest reversible action
→ verification → record → closure
```

- 同一路徑重複失敗時停止盲重試，重查 assumption/environment/tool boundary。
- Remote timeout 後先標 outcome unknown 並 reconcile，避免 duplicate mutation。

## Verification

- 變更後先跑最小有意義驗證，再按風險上升到 runtime/true-chain。
- Final 精確列出 executed、passed、not run、blocker、closure level 與 residual risk。
- Task 完成不自動授權修改 global instructions、Memory、Skills 或 Plugins。
