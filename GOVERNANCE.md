# Governance

## 適用範圍

本文件管理這個 repository 作為通用底座的維護、內容採納、版本候選及公開發布。它不定義採用者產品的需求、權限或日常工作程序，也不取代項目內的 active binding。

每個使用底座的項目按自己的 owner 路由產品、業務、技術、決策及工作內容。項目 agent 的工作邊界由根 AGENTS.md 承接；項目作業方式與變更規則由項目文件/00-協作與執行/規則與標準/工作規則與標準.md 承接，程序由 00 工作路由及其 Runbook 承接。底座維護者身份不會授予任何採用項目的產品、資料、發布或遠端操作權。

## 現行內容 owner

- [根 README](README.md) 是採用版本、來源身份、初始化、底座升級及 license 範圍的唯一入口。
- AGENTS.md 管本 repository 內 Agent 的工作邊界，不裁決採用項目的產品契約。
- 項目文件/README.md 路由產品、業務、技術、決策及日期化工作內容的 owner。
- 項目文件/00-協作與執行/README.md 管工作程序路由；其中的工作規則與標準及 Runbooks 管項目作業的實際規則和執行方式。
- .workflow/project.json 記錄底座模板 metadata 與 framework baseline；初始化後，項目的 .workflow/instance.json 是該項目的 active binding。Metadata、digest、生成文件或歷史記錄都不會取代內容 owner 的確認。
- CONTRIBUTING.md 管本底座的貢獻與必要驗證；.github/workflows/framework-checks.yml 是工具及 CI 實際命令的 owner。
- SECURITY.md 管本 repository 的公開資料邊界及安全回報指引。採用者需為自己的 repository 配置適用的安全入口。

既有 docs/、templates/、examples/、explorations/ 及 integrations/ 內容保留其參考、案例或探索身份。它們不與 AGENTS.md、README 或項目文件/00 中的現行 owner 平行裁決。舊 metadata 或 reference 文件不會因較早或較晚的日期而自動取得優先權；遇到矛盾時，按上面的問題 owner 核實，不以檔案排序或時間戳解決。

## 底座維護決策

審查底座變更時，依次確認：

1. 問題是否由現行 owner 或可核 evidence 支持；分開已知、推論與未知。
2. 最小改動是否能改善清晰度、路由、可執行性或驗證，而不建立重複 owner。
3. 變更是否保留 authority、privacy、security、license、attribution 及可恢復性邊界。
4. 適用與不適用情境、 operator cost、相容性及必要遷移是否清楚。
5. 若是版本發布，該候選 commit、CHANGELOG、framework version、CI 和公開發布 receipt 是否彼此一致。

小型修正可直接提出。新增 control、程序、profile 或術語主張，應說明實際問題、owner、source、trigger、non-trigger、成本及驗證。Breaking workflow change 說明 migration。沒有 evidence 支持的有效性主張，只能標為設計選擇或 inference，不可包裝成已證明的成效或正式認證。

## 內容身份

- **Reference**：按需閱讀的非 active source；內容可供理解，不會自動成為現行規則或本次採納決定。要納入 active 工作流程，須由相應 owner 審查並明確採納。
- **Experimental**：仍在探索；不因收錄而成為預設架構或 mandatory control。
- **Example**：說明概念，不代表唯一實作，也不構成產品 evidence。
- **Deprecated**：保留遷移背景，不再推薦作為現行入口。

任何文件被標為參考，不代表其原有安全或權限條件已由另一文件承接。要變更操作語義，需在新的 active owner 明確承接後，再將舊內容保留為非裁決性參考。舊文檔不要求隨每次現行規則更新而同步改寫。

## 公開版本與外部動作

本地分支、候選版號及 CHANGELOG 草稿不等於 public tag、Release、遠端 CI 或外部採用。版本發布須以實際授權的遠端動作與可回查 receipt 證明。推送、合併、打 tag、建立 Release 和部署均是各自獨立的外部操作；此文件本身不構成授權。

現行 0.3.0-rc.1 是本地整合候選，尚未發布。任何候選需按適用驗收核對檔案來源、舊入口路由、工具、全庫 Markdown links/anchors、公開內容與授權。未執行的檢查明確記為 NOT_RUN；本地 checker PASS 不代表 GitHub matrix 通過或產品已驗收。

## 下游項目的邊界

新項目 clone 後會取得本 repository 的協作文件及 GitHub templates。項目 owner 在首次推送或開啟協作功能前，應將 .github/、SECURITY.md、CONTRIBUTING.md 和其他本地說明改為自己的入口或標明不適用。底座不會自動清理它們，也不會自動升級或覆寫產品內容、active instance 或本地決策。

採用者專案可以是 private，並須使用自己核實的 remote、回報目的地、權限和授權。通用底座不收納專案私有需求或資料；將專案經驗提升到上游前，須先去識別、證明可重用並由底座 owner 明確採納。
