# 創新工作模式探索

本區收錄新的 AI 協作工作模式、有限試驗的觀察、失敗分析及後續研究方向，讓其他人可以理解、質疑，並按自己項目的需要設計試驗。

**預設 stability：Experimental。** 收錄代表值得研究；不代表已證明有效、已成為推薦流程，或 clone 本 repository 後應自動套用。各文件的最新狀態由其自身的「進度與證據」段落擁有。

## 探索索引

| 工作模式 | 研究問題 | Stability |
| --- | --- | --- |
| [AI Development Factory](ai-development-factory.md) | 協調 agent 能否在明確邊界內，持續編排實作、驗證、修復及整合，同時減少人的日常協調負擔？ | Experimental |

## 與 repository 其他部分的關係

- `docs/`：可裁剪的既有方法與決策原則。
- `templates/`：依任務選用的可複製記錄格式。
- `examples/`：用 fictional 情境示範方法。
- `integrations/`：特定工具的採用 adapter。
- `explorations/`：尚待驗證的工作模式；可以包含失敗、混合結果、被否定的假設及新試驗設計。

探索仍遵循原有的 truth、authority、evidence 及 recovery 邊界。只有經過明確裁決的最小可重用部分，才可能回到既有 docs、template、runbook 或 test；整份探索不會因為一次成功而自動升格。

## Clone 後如何使用

1. 先按[採用指南](../docs/08-adoption-guide.md)識別自己項目的 source of truth、風險、工具能力及最低驗證。
2. 只有當某個探索問題與你的實際瓶頸相關，才讀取對應文件的 trigger、non-trigger、成本及停止條件。
3. 在自己的項目留下簡短的採用決定：試驗哪一部分、保留哪些既有約束、如何衡量結果、何時退回較簡單的模式。
4. 實作與配置留在自己的項目。不要整套複製原試驗的角色、狀態機或文件數量作為初始化架構。

AI agent 讀到本區，不因此取得建立 worker、啟用 queue、擴大權限或自動發布的授權。項目明確選用後，可在已授權的範圍內推進，不需要為每個內部步驟重新請示。

## 每份探索應回答

- 要改善甚麼 outcome，與現有模式重疊及不同之處在哪裡？
- 哪些是設計假設、實際觀察、推論或尚未測試？
- 哪些部分有效、失敗或只完成了局部？有哪些其他解釋？
- 適用與不適用情境、操作成本、失敗／停止／恢復條件是甚麼？
- 如何做一個足以反駁假設的最小試驗？
- 目前進度、下一個決策，以及值得採納、縮小或放棄的條件是甚麼？

這些是寫作問題，不要求每項都新增獨立文件或永久 gate。

## 可公開內容邊界

只保存通用機制、必要分析及明確標示的 synthetic examples。內部經驗須重寫成可獨立理解的公開內容；只改項目名稱並不足夠，還要檢查細節組合能否辨識原項目、人物或系統。

不收錄私人路徑、內部 URL、帳號或 task identifiers、commit／artifact fingerprints、真實產品資料結構、credentials、原始 logs、對話或審計底稿。無法安全抽象的材料留在原有受控位置；公開文件不反向連到私人來源。

若原始證據不能公開，明說證據限制，不提供虛構來源，不將 qualitative experience 寫成可獨立重現的 benchmark。公開數據需要可分享的來源、sampling window、denominator 及限制。

內容裁決與 stability labels 依 [Governance](../GOVERNANCE.md)；隱私處理依 [Security and privacy](../SECURITY.md)。
