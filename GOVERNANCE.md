# Governance

## Project scope

本 repository 維護一套 vendor-neutral 的 AI collaboration reference model、playbooks 與 templates。它不收集或發布原始私人工作證據，也不提供 compliance/safety certification。

## Decision principles

Maintainer 依以下順序裁決內容變更：

1. claim 是否與 evidence/source 相配；
2. 是否讓 workflow 更可執行、可驗證或可裁剪；
3. 是否維持 truth、authority、verification、closure 的邊界；
4. 是否增加不必要的 governance cost 或 context debt；
5. 是否含 privacy、security、license 或 attribution 風險。

## Stability labels

- **Reference**：推薦作為框架的一部分，但應按情境裁剪。
- **Experimental**：尚需實務驗證，不應作 mandatory control。
- **Example**：教學用途，不代表唯一實作。
- **Deprecated**：保留遷移資訊，不再推薦。

## Claim discipline

外部術語需標明是 established concept、practitioner framing 或 project-defined term。Empirical claim 必須提供 population、sampling window、denominator 與 limitations；否則只能作 framework choice 或 inference。

Control effectiveness 分四級，不可跳級：

```text
rule documented → gate executed → error intercepted → outcome improved
```

## Change process

- 小型文字修正可直接以 pull request 處理。
- Workflow 提案先依[既有指引診斷](docs/07-system-evolution.md#先診斷既有指引)分清內容、入口、執行或新情境問題；已確認的錯誤不必等重複發生才修正。
- 新 control、task profile 或 terminology claim 應附 problem、source、trigger、non-trigger、cost 與 verification。
- Breaking workflow change 應更新 CHANGELOG，並說明 migration。
- Privacy/security incident 不應在 public issue 貼出 sensitive detail；依 SECURITY.md 處理。

## Content source of truth

- `docs/`、`templates/`、`examples/` 與 `integrations/` 中已收錄的 Markdown 裁決完整方法論正文與可複製 source。
- `explorations/` 的 Markdown 擁有各探索的設計、觀察、限制及目前研究狀態；預設為 `Experimental`，不會因收錄而成為 mandatory control 或預設初始化架構。
- 網站 components、navigation metadata 與 interactive synthesis 負責教學與操作，不得暗中重定義 canonical claim、gate 或 evidence boundary。
- 需要結構化視覺資料時，應保留對應 source path，並以 build-time consistency checks 防止遺漏或漂移。
- 若 UI 與 canonical Markdown 衝突，先視為 release blocker；修正兩者並重新驗證後才可發布。

## Experimental workflow intake

- 內部試驗以通用機制及最少必要觀察重寫；不得複製私人 case、原始證據、項目架構或指向私人材料的連結。
- 分開 design、observation、inference、unknown 及下一輪驗證。原始材料未公開時，明說不能獨立重現，不把 qualitative 經驗稱為 benchmark。
- 失敗及混合結果可以保留；實驗進度由單一 owning document 更新，索引只路由。
- 採納時選最小可重用部分，依既有 change process 裁決；探索中的角色、流程、queue 或狀態機不會整套自動進入既有方法。
