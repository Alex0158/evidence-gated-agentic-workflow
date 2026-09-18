# 06 — 驗證、交付與 Closure

## 1. Progressive verification ladder

驗證不是單一 `tests passed`。按風險與 claim 逐層上升：

### Level 1 — Static / readback

- exact diff、schema、route、config shape；
- record/page/file 回讀；
- link、syntax、manifest structure。

支持「變更存在／結構正確」，不支持 runtime 或 business success。

### Level 2 — Targeted

- 本次範圍的 unit/integration/focused check；
- positive、negative、boundary case。

支持指定 contract，不代表 full regression coverage。

### Level 3 — Full suite

只有實際執行完整 suite 才能寫「full suite passed」。仍需說明 suite 沒覆蓋的 runtime、data 或 external surfaces。

### Level 4 — Runtime smoke

- 真實 process/container/service；
- live config/data connection；
- browser/API path；
- exact identity/environment。

### Level 5 — True-chain

包含真 UI operation、真 core API/data flow、跨角色或 state transition，以及閉環 assertion。HTTP 200、stub 或 mock-only smoke 不等於 true-chain。

### Level 6 — Artifact freshness

把 source、build、artifact 與 runtime binding 分開：

- source commit / dirty state；
- build command/result；
- artifact timestamp/checksum/manifest；
- deployed runtime 實際使用哪個 artifact/config。

### Level 7 — External/user closure

- artifact 已交付；
- operator 已執行；
- evidence 已返回；
- target state 已驗證；
- rollback/remediation 可用；
- residual risk 有 owner。

## 2. Claim–evidence fit

驗證報告必須寫：

1. 執行了什麼；
2. 通過了什麼；
3. 沒執行什麼；
4. 哪個 gate/blocker 阻止更高層驗證；
5. 現有 evidence 最多支持什麼 claim；
6. residual risk 與 owner。

推薦使用精確狀態：

- `implemented, static-verified`；
- `targeted tests passed, full suite not run`；
- `packaged, runtime binding unverified`；
- `delivered, adoption pending`；
- `remote outcome unknown, reconciliation pending`；
- `verified and closed`。

## 3. Maker、checker 與 verdict

AI 可以同時實作和自檢，但高風險 work 應增加不同 failure surface：

- static scanner；
- test/runtime evidence；
- separate reviewer/subagent；
- human verdict；
- external readback。

「另一個 agent 說 OK」只是一項 review signal。Independent verification 的重點是證據來源與失敗模式是否真的不同。

## 4. Verification 也可能有副作用

以下不是 read-only：

- production 寄測試郵件；
- 建立或修改測試資料；
- 模擬 payment/order；
- restart/deploy；
- rollback；
- public smoke that sends notifications。

它們需要獨立 mutation authority、cleanup/remediation 與 receipt。沒有授權時，誠實停在較低 closure level。

## 5. Delivery lifecycle

```mermaid
stateDiagram-v2
    [*] --> Ready
    Ready --> Delivered
    Delivered --> Adopted
    Adopted --> EvidenceReturned
    EvidenceReturned --> Verified
    Verified --> Closed
    Delivered --> Blocked
    Adopted --> Unknown
    Unknown --> EvidenceReturned: reconcile
    Blocked --> Delivered: unblock
```

- **Ready**：artifact 本地完成。
- **Delivered**：已到 downstream owner/target。
- **Adopted**：已執行或採用。
- **Evidence returned**：有 receipt、readback、logs、screenshots 或 live data。
- **Verified**：evidence 足以支持 intended claim。
- **Closed**：formal truth、risk owner 與 handoff 都已收口。

## 6. Self-contained handoff

每個 handoff 最少包含：

- objective 與 target outcome；
- baseline → target；
- exact changed artifacts；
- operator、approver、verifier；
- prerequisites 與 environment/account boundary；
- exact steps；
- expected evidence；
- rollback/remediation；
- non-goals、known risks、stop condition。

不要要求接手者回頭閱讀整條 chat 才能執行。

### 來源變更後，哪些驗證仍可沿用？

Source identity 回答「驗證了哪份內容」；change impact 回答「哪些結論仍然成立」。Commit 或 hash 是識別依據；它們有變，不能單獨裁決所有 evidence 失效。同樣，功能檔案沒變也不能證明所有相關前提不變。

當交接、並行修改或後續變更需要沿用既有驗證時，先對照原 claim、實際 diff 及相關輸入，包括需求／acceptance criteria、shared contract、dependency、runtime、config、data 與 generated inputs。Ownership 說明誰可以改；是否需要重驗仍由改動對 claim 的影響判斷。獲准修改不代表舊驗證繼續有效。

以下是 fictional example：一份 Task 文件同時記錄驗收條件及工作進度。

| 變更 | 判斷 | 最小處理 |
| --- | --- | --- |
| 只新增進度文字，驗收條件及執行前提不變 | 文件版本變了，原產品驗證的前提未變 | 回讀 diff、記錄理由；可保留原產品結論，文件本身的檢查另行更新 |
| 同一文件改了驗收條件 | 即使沒有 code diff，原驗證也未必回答新要求 | 重開受影響 claim，依新條件補驗證 |
| 功能檔案沒變，但 shared schema、dependency 或 runtime 改了 | 檔案路徑分開不代表語義獨立 | 檢查相依影響，重跑必要 checks；範圍不清時不能直接沿用 |
| 無法確認誰改了哪些相關輸入 | 來源或 ownership 不足以支持交接 | 暫停受影響的交接／驗證，保留 candidate 並釐清；不因此丟棄成果 |

修正正在驗證的相關 source 或前提時，要重新識別候選並處理受影響 checks，不能把不同版本的結果混成同一次通過。若沿用舊 evidence，在原有 verification report 記下適用範圍、差異及保留理由；不要把歷史結果寫成新執行。

局部重驗判斷不會自行取消目標項目已明確要求的 release／CI checks；要更改這些要求，仍須回到其 owning rule 與決策者。

這是既有 [Decision lock 與 reopen](05-risk-authority-and-decision-rights.md#7-decision-lock-與-reopen) 的具體用法。一般單人小改動仍使用最小 diff／check；只在交接或 evidence reuse 有需要時補充輸入與 ownership 說明，不要求所有任務建立全庫 manifest 或永久鎖定表。

## 7. Git 不等於 closure

Git commit/push 能證明內容被版本化與送到 remote，但不能自動證明：

- correct branch 已 deployment；
- artifact 是 fresh；
- runtime 使用新版本；
- formal data 已更新；
- user/customer 已採用；
- public links 對匿名使用者可用。

每個下游狀態都要自己的 evidence。

## 8. Closure budget

開始前選 closure target，避免無限延長：

| Target | 含義 |
| --- | --- |
| Answered | 問題已由足夠 evidence 回答 |
| Diagnosed | root cause/likely cause 與未驗證邊界清楚 |
| Implemented | change 已完成並通過最低本地驗證 |
| Integrated | owning surfaces 與 contracts 已同步 |
| Runtime-verified | 指定 live path 已驗證 |
| Delivered | downstream 已收到完整 handoff |
| Externally closed | adoption、readback、risk 全部收口 |

不是每個任務都需要最高層；但必須誠實命名目前在哪一層。

風險 profile 決定檢查深度與必要邊界，closure target 決定本次要交付到哪裡。Assured 的本機 auth 修復仍可停在已約定的有界驗證結果；只有任務需要且取得相應授權，才進行 deployment 或 external closure。
