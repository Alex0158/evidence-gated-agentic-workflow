# AI Development Factory：有邊界的自動開發協作探索

- Stability：**Experimental**
- 研究狀態：**初步試驗回顧已整理；修訂模式與比較驗證待進行**
- 公開整理更新：2026-09-18

## 1. 目標與定位

本文件以 **AI Development Factory** 作為工作模式的探索名稱：人提供目標、約束及決策邊界，由協調 agent 持續編排工作、派發給執行 agent、安排驗證及修復，最後將結果整合成可交付成果。期望提高從已接受 brief 到可驗證整合結果的自動化程度，減少人逐次分派和追蹤工作的負擔。

這是 practitioner framing，不是正式標準或已驗證的產品能力。本 repository 提供設計、觀察及試驗方法，沒有附帶可直接啟動的 factory engine。

「全自動」必須指明作用範圍。在已授權的開發範圍內，自動處理內部步驟；目標取捨、風險承擔、重大語義變更及未授權的外部操作，仍由相應的決策者處理。增加 agent 或延長執行時間不會自行擴張 authority。

## 2. 與既有工作模式的重疊及差異

| 面向 | 共同基礎 | Factory 探索增加的問題 |
| --- | --- | --- |
| 目標與邊界 | objective、non-goals、source of truth、mutation authority | 協調 agent 能否把目標拆成可執行且不偏離意圖的工作？ |
| 開發閉環 | investigate → act → verify → record | 誰安排下一步、追蹤依賴，以及在失敗後選擇修復路徑？ |
| 驗證 | claim 與 evidence 同範圍；需要時獨立 challenge | 如何選擇不同 evidence surface，避免多個 agent 重複同一假設？ |
| 整合 | 一個明確 owner 對最終結果負責 | 如何防止 worker 局部完成，但整體長期未整合？ |
| 恢復 | 保留來源、結果及尚未解決的狀態 | 中斷、context loss 或 worker 消失後，如何知道哪些工作真正完成？ |
| 人的角色 | 保留 outer-loop 決策與後果責任 | 是否真的減少日常介入，還是將實作負擔變成協調負擔？ |

多 task 協作只是一種可能的承載方式。單一 agent 的工具呼叫、短期子任務、持續 task 或 durable queue 各有成本；它們不因都能「派工作」而具備相同的恢復及交付語義。

## 3. 最小概念架構

```text
已接受的目標、約束與停止條件
  → 協調者選擇下一個可整合工作單位
  → 執行者在明確來源與寫入範圍內工作
  → 依 intended claim 驗證結果
  → 通過：整合並回讀；未通過：分類後修復或升級
  → 更新一份目前狀態，決定繼續、收窄或停止
```

- **協調者**負責拆分、依賴與進度，但不能靠 worker 的完成語氣宣告整體成功。
- **執行者**交付 candidate、受影響範圍及實際驗證結果；不能順手改變需求或 shared contract。
- **驗證者**回答指定的風險問題。不同 task 不等於獨立證據；是否需要不同 operator，取決於風險和檢查面。
- **整合 owner**負責確認候選相容、合併後行為及最終 claim；可以與協調者由同一角色承擔。

角色不要求各自建立一個常駐 agent。共享檔案或語義 contract 預設由一個 writer 推進；可以並行的範圍須先證明獨立。工作結果應及時整合，避免完成清單持續增長而使用者仍看不到有用成果。

## 4. 初步試驗的公開觀察

依據是一輪由 maintainer 回顧的內部試驗，以下為經過抽象的 qualitative observations。原始材料不在此公開，讀者無法由本文件獨立重現該試驗。沒有完整 sampling window、dispatch denominator、工時或直接開發對照，因此不作失敗率、速度提升或淨效益的 empirical claim。

| 觀察 | 可保留的意義 | 證據限制 |
| --- | --- | --- |
| 針對另一個失敗面的 verifier，在原有 checks 通過後發現真實一致性缺陷 | 獨立問題設計可以增加驗證價值 | 無法證明派發實作本身優於單一開發者加一次 review |
| 派發目的地的既有工作身分與預期任務不符，候選需重新確認來源及範圍 | dispatch receipt 要能確認誰在處理哪個結果 | 細節只支持 identity failure mode，不支持普遍發生率 |
| 執行 root、實際 runtime 及工具副作用觸發額外修正 | verifier 的環境本身需要具體前提 | 未量度早期 preflight 能節省多少時間 |
| 過廣的來源鎖把正常工作更新視為失效，後來改按 checkpoint 與 ownership 分類 | source identity 與 change impact 要共同判斷 | 縮窄清單也可能漏掉 shared inputs，不能一律少鎖 |
| 保存已有 candidate，再澄清 provenance 並驗證，可以保留有用工作 | 協作失敗不必自動使實作結果報廢 | 不適用於來源、完整性或 ownership 無法安全確定的 candidate |
| 缺少可靠的工作開始／整合時間，無法比較總投入 | 下一輪需要最小成本及 outcome 記錄 | task 壽命、agent 數及文件量不能代替工時與價值 |

操作者對整體試驗的評價偏負面；個別缺陷被攔截的收益仍成立。兩者分別回答「是否找到有用問題」與「這種工作模式整體是否值得」，不能互相抵銷。

## 5. 分析與目前意見

**主要假設：協調成本可能超過工作分派帶來的收益。** 協調者同時承擔拆分、派發、追蹤、環境排查、權責核對、修復安排、整合及記錄。工作拆得越細，每份工作的交接成本越容易成為主要負擔。這是機制推論；工具熟悉度、期限、任務複雜性等替代解釋尚未排除。

值得保留的部分包括：有明確問題的 independent review、精準的 candidate/source identity、共享寫入面的控制、不同失敗類型的處理，以及在可恢復情況下保留有效成果。

優先挑戰的部分包括：把每個內部步驟變成正式工作單、常駐角色過多、為了持續運作而重複沒有新證據的盤點，以及只累積 worker 完成數卻延遲整合。

目前建議將這種模式保留為有條件的探索。先驗證一個小型完整閉環能否改善 outcome，再考慮擴大並行或持續運行。

## 6. 適用、非觸發及代價

**適合試驗：** 有穩定輸入、明確輸出、可隔離寫入面、足夠大的工作單位，以及可描述的整合路徑；或需要另一種 evidence surface 檢驗高影響假設。

**不應僅因此啟用：** 工具有多 agent 功能、有閒置 task、希望看起來更自主，或只是單一串行小修改。需求及共享契約仍快速改動、目標本身未清楚時，應先處理這些前提。

**代價：** context 傳遞、source binding、等待、重工、整合、記錄、工具／模型使用及人的例外處理。更多檢查可能降低某類缺陷，也可能讓協調者成為瓶頸。兩邊都要記，不只列成功的 worker 數。

## 7. Clone 後的最小採用試驗

項目明確選擇試驗後，先沿用已有 [Task Brief](../templates/task-brief.md)及 [Verification Report](../templates/verification-report.md)，只補真正缺少的資訊。以下是一份工作記錄中的欄位示意，不要求新增另一套治理文件：

```text
目標及可整合結果：
Baseline：自己項目的來源、相關依賴及實際執行環境
協調／整合 owner：
執行者可改／不可改的範圍；shared inputs 的 owner：
允許的操作、預算及停止條件：
驗證問題、方法及最高可宣稱結果：
Dispatch identity 與結果回讀：
Candidate → verification → integration 的目前狀態：
失敗、重工、owner intervention 與下一個決策：
```

1. **先保留可比較的簡單模式。** A：主執行者完成工作，需要時加入獨立 review。B：協調者派發一個有界工作單位，取得結果、驗證並整合。對照有獨立 review 與無 review 的差異時，不把其收益混算成 delegation 收益。
2. **選可比較的工作。** 按風險、複雜度、工具熟悉程度及整合範圍分組；記錄差異。少量試驗只能形成方向判斷，不能宣稱一般速度優勢。
3. **派發前證明可執行。** 確認 destination、source、寫入 ownership、實際 runtime、產物位置及驗證工具副作用。前提未變時不為每項 assertion 重做整套 preflight。
4. **失敗先分類。** 分開產品缺陷、錯誤 invocation、未滿足前提、超出來源邊界，以及證據不足。保留仍有效的局部結果，只重開被影響的部分。
5. **中斷後先 reconcile。** 查明是否已產生 candidate 或外部效果，再決定恢復或重新執行；task 結束不自動等於交付成功。沒有 durable state 的 host task 不能直接當成可靠 queue。
6. **到整合結果才評估。** 在同一份記錄寫 outcome、實際缺陷、等待／修復／協調時間、成本及人的介入。記錄 eligible 與 observed 工作，將中斷或未完成項目保留在 denominator 說明中。

可以先做只讀 review delegation，再決定是否值得分派 code-writing。只有在隔離與整合已通過驗證時，才擴大到多 writer；具體 host API、queue 或 CI 設定留在項目自己的 adapter。

## 8. 進度、下一步及停止條件

| 項目 | 現在支持的狀態 | 下一個可改變判斷的結果 |
| --- | --- | --- |
| 概念與現有方法的關係 | 已整理設計及邊界 | 檢查是否有現有模式已能更簡單滿足目標 |
| 初步 trial | 有局部實作／驗證及失敗回顧；整體價值未證明 | 可比較的 integrated outcome 及 operator cost |
| checkpoint／ownership 修正 | 有局部採用的回顧紀錄 | 同時觀察 false invalidation 與錯誤 evidence reuse |
| 自動排程、持續運作及中斷恢復 | 本文件未提供完整可靠性證據或實作 | controlled interruption、resume、duplicate-effect 及整合驗證 |
| 改善生產力 | 未建立 | 有明確範圍、denominator 及反例的比較結果 |
| 成為預設初始化架構 | 尚不推薦 | 個別穩定部分符合採納條件，經 maintainer 明確裁決 |

開始下一輪前，由該項目定出時間、工具／模型成本、整合等待及 owner intervention 的上限。達到上限但沒有決策上新 evidence，或 coordinator 反覆處理同一類 handoff 問題時，收窄工作或退回簡單模式；不靠新增角色維持運作。

身份、權限或 recovery 無法確認時，停止受影響操作。未知只限制某項 claim 時，可保留 unknown 並繼續其他安全工作。必要的恢復及工作保留，不因試驗被停止而失去責任 owner。

## 9. 採納、修訂或放棄

只有當一個具體部分在相關範圍內反覆改善 outcome，且成本、false positive、reopen 與維護責任可接受，才考慮將它提煉到既有方法、template、runbook 或 helper。即使採納某個驗證或 handoff 手法，也不代表整個 factory 模式已獲採納。

若較簡單的模式提供相同品質及更低協調成本，便縮小或放棄相應編排。若獨立驗證仍有價值，保留該部分。若只是缺乏工具成熟度，明確列出會令試驗值得重開的能力，避免永久掛著「快完成」的狀態。

## 10. 公開記錄與參考

本文件保留一般化的協作機制與觀察，未公開來源項目的身份、業務架構、精確事件編號、私人素材或指紋。未公開的資料不能充當讀者可查核的 public citation。未來若有可分享的 synthetic reproduction 或公開 pilot，可補入方法、資料及限制；在此之前維持 qualitative、Experimental 定位。

- [核心原則](../docs/01-core-principles.md)：來源、邊界、不確定性及 repeated failure。
- [風險、授權與決策權](../docs/05-risk-authority-and-decision-rights.md)：自主範圍、unknown delivery 及局部 reopen。
- [驗證、交付與 Closure](../docs/06-verification-delivery-and-closure.md)：不同 evidence surface、handoff 及整合完成。
- [系統演化](../docs/07-system-evolution.md)：控制的效益、成本及 pruning。
- [採用指南](../docs/08-adoption-guide.md)：按項目需要作最小採用。
- [返回探索索引](README.md)。
