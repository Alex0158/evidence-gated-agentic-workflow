# 02 — 端到端 Operating Loop

## Stage 0：Objective

先定義要改變的 outcome，不從工具或 solution 開始。

- 真正使用者／業務結果是什麼？
- 表面症狀和底層問題是否相同？
- binding constraint 是技術、資料、權限、流程、時間還是認知？
- success、non-goals 與 closure target 是什麼？

最低產物：一句 objective、成功條件、不做什麼。

## Stage 1：Boundary 與 authority

確認 workspace、repository、data source、account、environment 與 owner。把權限拆成 read、edit、write、publish、deploy、delete，不使用模糊的「已授權」。

最低產物：in scope、out of scope、mutation class、stop condition。

## Stage 2：Task classification

任務類別決定 evidence 與 gate：

- quick answer；
- current-state investigation；
- diagnose only；
- change/build；
- formal data operation；
- release/runtime/customer delivery；
- destructive cleanup；
- business decision；
- learning/teaching；
- workflow/tooling evolution。

同時選擇 Fast、Standard 或 Assured。

## Stage 3：Evidence map

只收集會改變 implementation 或 risk 的 evidence：

1. current code、live data、actual runtime；
2. authoritative current docs/spec；
3. tests、logs、tool output、artifact metadata；
4. active issue、decision record；
5. history/Memory 只作 routing 或 historical interpretation。

每個重要結論記錄 Verified、Inferred、Unknown，以及可能推翻它的 falsifier。

## Stage 4：Challenge

Standard/Assured 任務問：

1. 什麼 evidence 會證明目前假設錯？
2. 最可能的 regression、data loss、security 或 external impact 是什麼？
3. 是否把相似但不同的 mechanism 混在一起？
4. 最小方案、保守方案與擴大方案的 trade-off？
5. non-goals？
6. 最低有意義驗證？

Challenge 的目的不是增加篇幅，而是避免修錯層、優化錯目標或擴大 blast radius。

## Stage 5：Decision 與 governance gate

決定是否：

- 直接做；
- 更新既有 issue；
- 建立 tracking issue/spec/decision note；
- 建立 release/handoff record；
- 只分析、不修改。

高風險 behavior、auth、permissions、data lifecycle、deployment 或 cross-layer contract，應在實作前留下 intent、affected surfaces、failure modes、minimum verification 與 rollback/remediation。

## Stage 6：Smallest reversible path

設計：

```text
precondition → smallest useful action → verification
→ stop/rollback → next-entry condition
```

不要順手做無關重構、broad cleanup、shared-layer 修改或沒有證據支持的 extra fix。

Defect/contract 變更可使用：

```text
Evidence → Red or equivalent failure proof
→ Green → behavior-preserving Refactor → Record
```

若無法建立 automated failing test，說明使用了哪種等價失敗證據。

## Stage 7：Execution

偏好 exact target、exact files、controlled helper、dry-run、minimal mutation 與 incremental verification。

Remote write 遇 timeout/disconnect 時，不自動判 failure：

```text
confirmed success / confirmed failure / partial-mixed / outcome unknown
```

`outcome unknown` 不可直接用新 request 重試。先用 stable business identity、receipt、count、query 做 authoritative reconciliation；只有 target service 的 idempotency semantics 已核實時，才依其 contract 沿用原 key 嘗試 duplicate suppression。

## Stage 8：Verification

按需要逐層上升：

1. static/readback；
2. targeted tests；
3. full suite；
4. runtime smoke；
5. true-chain；
6. artifact freshness；
7. external/user closure。

驗證本身若會 mutate production、寄信、建測試資料或 rollback，也需要自己的 authority。

## Stage 9：Record

把結果放回 owning truth layer：

- product behavior → product docs/spec；
- active defect → issue；
- test method → test/eval assets；
- runtime/delivery diff → release record；
- formal business data → authoritative data source；
- reusable workflow → runbook/Skill/helper；
- temporary experiment → sandbox/history，不冒充 current truth。

## Stage 10：Delivery 與 handoff

區分：

```text
artifact ready → delivered → executed/adopted
→ evidence returned → verified → closed
```

Handoff 必須 self-contained：baseline、target、changed、operator、steps、verification、rollback、known risks。

## Stage 11：Workflow evolution

任務後問：

- 這是一次例外還是重複 pattern？
- 下一次最可能在哪裡再次失敗？
- 最小正確 landing point 是 docs、Skill、helper、test、eval 還是 decision note？
- 如何驗證它會 trigger 且不誤觸發？

不要把每次成功都制度化。只有重複、穩定、可命名、可驗證的 pattern 才 promotion。

## Stage 12：Closure

Closure checklist：

- objective 已達成；
- action receipt 與 verification evidence 存在；
- claim 沒有超過 evidence；
- current truth 已同步；
- downstream adoption 已證實，或明確標為 pending；
- residual risk 有 owner 與 next condition；
- 未授權或 out-of-scope 內容沒有被順手改動。

若缺其中一項，使用精確狀態，例如 `implemented but not runtime-verified`、`delivered but adoption pending`，而不是模糊的「大致完成」。
