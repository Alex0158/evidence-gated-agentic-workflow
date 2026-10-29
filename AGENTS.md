# Agent 工作入口

## 適用範圍與權威

本檔適用於本 repository；執行前還要讀取目前 harness 注入的 instructions，以及工作目錄內適用的巢狀 AGENTS.md。不要由檔案先後或一般 Markdown 位置推定規則優先級。若正式產品來源、既有授權與指令互相衝突，先分類並保留 evidence；只有依賴該衝突的動作停止。

本檔提供 Agent 的工作邊界，不取代產品契約、工程 binding 或操作程序。依問題查閱[項目文件來源目錄](項目文件/README.md)，依任務查閱[工作路由](項目文件/00-協作與執行/README.md)，實際 repo、工具與 environment 入口由[項目工程入口](項目文件/00-協作與執行/項目工程入口.md)指向唯一 binding。每次只讀任務需要的 canonical owners，不要求全庫預讀。

原 `docs/`、`templates/`、`examples/`、`integrations/` 與 `explorations/` 的身份依[底座治理](GOVERNANCE.md)及各檔入口判讀；它們提供方法參考、歷史案例或探索，不是另一套預設工作規範。需要使用時沿其現行 owner 引用，不以舊範例覆寫本檔、重建模板台帳或取得額外授權。底座維護／公開發布另依[貢獻程序](CONTRIBUTING.md)與[安全政策](SECURITY.md)的適用要求，不將它們套成所有下游產品的工作流程。

## 開始工作

先自行確定目標、允許動作、active repo／source、current 與 intended、主要 owner、影響面、完成層及阻塞未知。由[項目文件來源目錄](項目文件/README.md)找正式內容來源，由[工作路由](項目文件/00-協作與執行/README.md)選 Runbook；依任務觸發條件查閱並遵守適用的[工作規則與標準](項目文件/00-協作與執行/規則與標準/工作規則與標準.md)及程序，按需閱讀不免除適用要求。不要以模板、generated view、舊紀錄、檔名或較新 timestamp 代替 current contract 或確認事件。

底座採用及新目錄／既有 checkout／已初始化／partial 狀態的入口，統一依[README 採用狀態路由](README.md#採用前先辨認工作狀態)；README 是唯一採用程序 owner。

小而可逆、已有授權的工作可直接推進。Runbook 只教如何執行，不授予產品、風險、發布或外部承諾權。新方向、scope、權限／資料政策、相容性、風險接受或外部承諾超出現有授權時，保留為 proposal，提出具體決策點；不把文件存在或工程 maintainer 身份當成批准。

## 來源與狀態邊界

- 正式產品及業務語義由項目文件中的 designated owner 定義；技術 representation 由明確的 MD 或 native owner 承接。
- 單次分析、工作進度、驗證與交付結果留在日期化紀錄，不回寫成永久標準。
- 文件的 draft／current／superseded 是內容生命週期；不是已批准、已實作、已部署或用戶已接受。
- 需要 native runner 的該項檢查，必要 runner 未設定或不可用時記 NOT_RUN 並說明原因；其他已實際完成且有 evidence 的核查，依[結果與狀態](項目文件/00-協作與執行/規則與標準/工作規則與標準.md#結果與狀態)按實際方法及 claim 各自判定。不能發明命令或把靜態文件檢查稱為產品驗證。
- Source、build、test execution、runtime、deployment、user-visible behavior 與 acceptance 是不同 evidence 層；只報告實際證明的層次。

## 保護範圍

不在通用 base 中加入項目私有需求、真實客戶資料、secrets、個人絕對路徑或特定客戶角色／流程。Secrets 只使用經授權的 secure retrieval reference，不寫進文檔、命令輸出或 commit。

不要自動覆寫或刪除既有文件，不做 reset／clean，不把實驗初始化當成重建權。破壞性操作的必要性、影響／可恢復性與 exact-target 重核依[工作規則與標準](項目文件/00-協作與執行/規則與標準/工作規則與標準.md#破壞性操作)；外部 remote、公開、部署、資料變更及不可逆操作只在明確授權與項目 gate 都成立時執行。local validation 不授權 push 或宣稱 remote 已發布。

通用 base、項目 private overlay 和 upstream promotion 分開。項目差異留在本地項目 owner；要提升為通用內容，先去除私有資料、確認改動確實是可重用的方法，再由有權 owner 明確採納。新 branch、PR、文件更新或 maintainer 身份都不會自動批准 promotion。
