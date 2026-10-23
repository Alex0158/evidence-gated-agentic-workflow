# Changelog

## Unreleased

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
