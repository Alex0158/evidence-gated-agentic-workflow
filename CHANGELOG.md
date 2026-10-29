# Changelog

## Unreleased

## 0.3.0-rc.4 — Pre-release

此版本的公開狀態及發布時間以對應 GitHub Release 的實際狀態、`published_at` 與可回查 receipt 核實。

### 固定版本與新項目採用

- 固定採用版本、首次 clone、Release／attestation 核對及共用採用腳本同步為 RC4，包含本輪 AGENTS、工作標準、九份 Runbook 及模板更新。
- Framework metadata 更新為 `0.3.0-rc.4`；初始化後 active instance 沿用這個版本，設計基線及設計來源 digest 保持原義及原值。
- 新項目保留同版 AGENTS／工作標準／九份 Runbook，初始化只生成三份核心 draft、active binding 及 receipts；文件存在不代表規格已確認或產品已實作。
- 舊版本 tag、Release 及歷史紀錄保留；既有項目由 owner 比較採納，不重新初始化或覆寫 instance／產品內容。

### 入口、Loop 與交付例外交叉核對

- 根 AGENTS 明示按需閱讀仍須遵守適用標準與程序；缺 native runner 的 NOT_RUN 限於需要它的該項檢查，其他已完成核查依實際方法及 claim 判定。
- 底座採用／實體初始化先回根 README 的唯一狀態路由，再交接產品啟動；工作路由及啟動程序不另定採用步驟。
- 開發中的目標失敗可在既有授權及安全前提內返回 TDD／最小修正，不強制另繞缺陷流程或因沒有 recovery procedure 自動 blocked；資料／外部狀態恢復、破壞性操作及新風險決策仍核相應 gates。
- 驗證前提及 NOT_RUN 分支按所選方法判定必要 runner，與根 AGENTS、工作標準及已完成的人工／source 核查路徑一致。
- 交接／部署前明判本階段必要檢查與 gates；未滿足時停止相依交付並保留實際成果。Unknown dispatch 不自動授予重試、成功聲明或恢復權；恢復／補償須有涵蓋當前未知狀態的有效明確授權及安全程序。
- 採納／遷移：無 binding、schema 或初始化變更，毋須重新初始化；下游由 owner 比較採納，在下一個適用入口／回跳／交付點使用澄清條件，保留既有紀錄、失敗及未驗範圍。

### 任務捕捉與查重交叉核對

- 重要發現可在允許位置先保留待查重／待登記紀錄，模板不再把完整查重及正式主源作無條件前提；可確認同案時，即使根因未知也沿用原項。
- 暫存與正式登記分清，對帳後將獨有 evidence 連入／引用主源並 readback，再轉指主源，停止第二份同維度狀態而保留原捕捉。
- 登記已派送但結果未知時保留對帳責任，不因其後權限失效或不可 readback 改判未寫入；調查成果完成與後續承接的 closure 依各自目標判定。
- 同步調查、任務範本及工作標準；既有紀錄不批量合併、刪除或重開，進行中的工作在下一次捕捉／對帳／Exit 套用澄清條件，毋須重新初始化。

### 任務登記與分流

- 新增共用 Runbook，串起後續處置、查重、最小捕捉、分類、優先級／責任、Route、跟進及關閉／重開；同一狀態維度沿用 primary tracker，不另造平行台帳。
- 調查允許重要發現途中先登記，Exit 明判更新既有、新增待處理、本次已處理或無後續。Task 保存接手摘要並引用原分析，未知、建議、需求確認及實作授權分開。
- 工作任務範本改為首次最小登記、下一步前提及 closure 分階段補足；補分類、來源／查重、優先級／排程、下一責任、處置及延期／重開依據，不要求未查明問題先有完整規格或根因。
- 同步工作標準、九份 Runbook 的導航及 default checker；登記須有實體 readback，寫入不可用時交安全 handoff，不聲稱已入 tracker 或已被接手。
- 採納／遷移：無 binding、schema 或初始化變更，毋須重新初始化；既有任務沿用主源，只補下一步及處置所缺資訊，不批量重寫／關閉舊項。下游由 owner 比較採納；更新 checker 時一併帶入新 Runbook、Route 及範本，進行中的調查在重要發現或下一次 Exit 使用新判斷。

### Loop 與例外交叉核對

- 將 TDD 內循環限於 caller 選定的小步／AC，完成後先返回主流程驗證／review；本輪必要相關測試通過且無本輪新 FAIL，才進 Refactor 或完成。
- 缺陷修復在改碼前核對業務鏈路、共用影響、方案及回歸；只有仍需修正且已授權的範圍進修正分支，non-defect／無需修正的風險接受分開退出或交接。
- 區分目標接口缺失／受控逾時契約失敗與無關前提錯誤；「已實作」替代路徑限接手前目標改動或有效緊急決定，本輪未先測則記方法偏差，不事後自動豁免或補造 Red。
- 已完成調查的 decision gap 直接送 SDD 確認分支，不在兩程序無新 evidence 往返。既有授權、原失敗及 revision evidence 保留；採納後從下一個適用小步使用澄清條件，毋須重新初始化或改歷史紀錄。

### SDD 與完整開發 Loop

- 新增《規格驅動開發》共用 Runbook，處理沿用／補缺、規格確認及變更、本輪開工條件、影響與重新驗證；規格內容仍回原產品／業務／技術 owner。
- 開發主 Loop 串接業務／共用影響、SDD、必要設計與小步安排、TDD、整體驗證、review／回寫及下一輪；補齊實作偏差、預期歧義、環境失敗、阻塞與完成的回跳條件。
- 修復沿用清楚既有契約走短路徑，缺漏／衝突／變更才展開 SDD；TDD、調查與驗證入口同步契約釐清及變更路由。規格就緒不授權實作，規格變更不抹去原失敗，也不把舊 PASS 改掛新 revision。
- 同步工作標準、現行 Runbook 導航與 default checker 必需檔案；無行為變更不強造 spec，已授權隔離 PoC 及獨立工作保持原授權邊界。
- 採納／遷移：無 binding、schema 或初始化變更，毋須重新初始化；進行中的工作從下一個適用小步核規格與 evidence，既有內容足夠時直接引用。下游由 owner 比較採納；更新 checker 時一併帶入新 Runbook、Route 及標準，不回退工作樹補造事前規格／確認。此要求不宣稱既有項目已實際執行完整 SDD。

### 共用 TDD 子程序

- 新增《測試驅動開發》Runbook，為適用的程式行為變更及缺陷修復提供 Red → Green → Refactor、各階段判斷、例外與返回原流程的程序；避免兩個主流程重複維護或遺漏測試先行要求。
- 開發與變更、修復缺陷直接 Route 到同一子程序；工作標準定適用條件與例外，工作路由、README 及 default 文件檢查清單同步納入新 Runbook。
- 人工／等價失敗證據及事後補測保留其真實身份，不稱為 test-first TDD；局部 Green 不取代共用 consumers／業務鏈路回歸、required checks 或 acceptance。不新增授權、全量套件、逐輪 commit 或固定 coverage 門檻。
- 採納／遷移：新增方法要求，不改 schema、binding 或初始化；進行中的工作在下一個尚未實作的適用行為小步採用，已完成實作保留先後順序並補必要回歸，不回退工作樹補造 Red。既有下游由 owner 比較採納，default checker 新增新檔為必要 artifact；更新 checker 時一併帶入 Runbook 及路由，毋須重新初始化。

### 業務脈絡與方案取捨

- 調查涉及功能、業務鏈路、共用模組或處置建議時，先定位業務結果及其他受影響 consumers，再按整體項目目標、成本、相容性與風險比較方案；不以局部修補或最低行數代替整體判斷。
- Evidence 支持調整既定規則、功能或產品定位時，Agent 須主動提出 proposal，由有權決策者確認；未確認前保留 current contract，不新增實作或外部操作權。
- 同步工作標準、開發 Runbook 與決策範本；按實際影響展開，既有分析可核實後引用，無須全庫掃描或為小改動新增完整紀錄。
- 採納／遷移：無 schema、工具或初始化變更，毋須重新初始化；進行中的調查在下次推薦方案前補足會改變判斷的影響與取捨，已完成紀錄保留原 baseline。既有下游項目由其 owner 比較採納，不自動覆寫本地規則。

## 0.3.0-rc.3 — Pre-release

此版本的公開狀態及發布時間以對應 GitHub Release 的實際狀態、`published_at` 與可回查 receipt 核實。

### 首次使用與相容性

- README 將首次使用入口、RC3 同版開場提示及完整採用程序連在一起，按下載版本的文件即可開始。
- 新採用者不需切到 `main` 或依賴私人對話；既有 RC1／RC2 項目毋須重新初始化，採納新指引仍由項目 owner 決定。
- 核心文件架構、AGENTS／Runbooks、模板、native 工具、schema、授權邊界及 licenses 不變；metadata 僅更新底座版本，設計基線及設計 digest 保留。

### 發布界線

- 版號或 merge 不代表 Release 已公開；公開狀態仍須按實際 GitHub Release 驗證。RC1／RC2 的歷史 tag、Release 與記錄保留。
- 沿用既有工具／環境前提及驗證限制；文件檢查不代表產品 build、runtime、deployment 或 acceptance。

## 0.3.0-rc.2 — Pre-release

此版本的公開狀態及發布時間以對應 GitHub Release 的實際狀態、`published_at` 與可回查 receipt 核實。

### 啟動與採用

- 新 Agent 可先從 README 辨認新目錄、既有未初始化 checkout、已初始化項目、partial 狀態或底座維護工作，再沿唯一採用程序前進。
- 既有 checkout 可在原根目錄初始化；保留項目 origin，只調整可確認的上游 remote，遇來源、branch 或初始化狀態衝突時停止並保留資料。
- 採用程序明確以 sh 執行，修正從 zsh 貼入時初始化狀態 glob 無匹配的問題。
- 初始化後明示 workspace 根目錄、active binding、三份核心草稿及啟動 Runbook；AGENTS 只引用 README 的採用路由。
- 固定版本指引以 RC2 為預設，明確核對 Release attestation、annotated tag object 及其指向的 commit，不依賴先前對話或其他版本的 SHA。

### 相容性與保留範圍

- 核心文件架構、Runbooks、模板、native 工具、schema、授權邊界及 licenses 不變；設計基線仍為 v1.0-rev15，設計 digest 不變。
- RC1 tag 與 Release 保持原樣。既有 RC1 項目毋須重新初始化；文件指引更新須按項目 owner 比較採納，不覆寫產品內容或 active binding。
- 維持既有環境與 evidence 限制；文件檢查不代表產品 build、runtime、deployment 或 acceptance。

## 0.3.0-rc.1 — Pre-release

此版本的公開狀態及發布時間以對應 GitHub Release 的實際狀態、`published_at` 與可回查 receipt 核實。

### Integration candidate

- Integrate the revision 15 project starter into the existing repository while retaining its public history and older reference material.
- Establish one adoption entry with three initialization drafts, five on-demand document types, candidate source verification, and separate upstream and project remotes.
- Clarify base-repository maintenance governance, downstream project boundaries, public safety, and the license scope for the new tools.
- Report retained files truthfully when on-demand document writing or readback fails, with a nonzero exit and explicit reconciliation guidance.

### Teaching frontend retirement

- 撤除教學前端及 assets、Astro／TypeScript／npm 設定、網站專用 validation／routing scripts、Pages deployment workflow 與前端專用授權／dependency notices。
- 保留 current canonical 方法、模板、examples、Codex adapter 與 Experimental explorations；同步 README、governance、contribution、security 及 adapter 的入口與驗證要求。
- Migration：`npm ci`、`npm run dev/build/preview` 及網站互動工具不再適用；改用 repository 中的 Markdown 與模板。後續文件變更驗證 links／anchors、claim boundaries 及 public privacy，而不是網站 build。
- 教學前端暫不維護，是否重建留待另行決定。此變更不代表既有 hosted website 已下架；歷史網站 source 及授權仍由 Git history 保存。

### Workflow guidance updates

- 新增 `explorations/`，保存可公開、通用的創新工作模式研究，預設標為 Experimental。
- 首份探索整理 AI Development Factory 的設計、一般化試驗觀察、限制、進度、比較試驗及停止條件。
- 更新 clone／初始化採用指引及 governance；既有工作模式的預設權限與 gates 不變。
- 補充既有驗證／handoff 指引：以通用例子區分 source identity、ownership 與 change impact，說明何時可沿用 evidence 或局部重驗。
- 統一既有指引診斷、extraction／proposal 入口及 evidence-reuse 模板；明確保留項目 required checks，模板可合併使用。
- 修正採用週次與風險要求、首次公開與既有 repo 發佈的適用範圍。

## 0.2.0 — 2026-07-17

- 加入以 Astro 產生的多頁互動教學／參考網站，部署至 GitHub Pages。
- 加入 13-stage system explorer、Fast／Standard／Assured classifier、claim–evidence matcher、Codex capability ladder 與 local-only task workbench。
- 原始 Markdown 保持 canonical source；模板頁直接提供 raw preview、copy 與 download。
- 加入 responsive、keyboard navigation、reduced motion、print styles、SEO、sitemap、custom 404 與 command palette。
- 加入 build-time route／asset／source-coverage／private-path validation 及 GitHub Actions deployment。
- 明確拆分內容的 CC BY 4.0 與網站程式碼的 MIT dual license。

## 0.1.0 — 2026-07-17

- 發布去識別化 public edition。
- 建立核心原則、operating loop、AI collaboration stack 與 methodology map。
- 建立 authority、verification、handoff、workflow evolution 與 adoption guides。
- 加入可直接複製的 task、investigation、implementation、risk、connector、verification、handoff 與 workflow-extraction templates。
