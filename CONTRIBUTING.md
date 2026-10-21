# Contributing

本文件和本 repository 的 issue／PR templates 專為維護 Evidence-Gated Agentic Workflow 通用底座而設。若你把它們帶到自己的產品 repository，請先由該項目的 owner 調整 .github/、回報入口、貢獻程序及 license 說明；不要把產品問題導向此上游。

## 適合的底座貢獻

- 修正錯誤、過時、矛盾或超出 evidence 的公開內容。
- 改善底座的閱讀入口、owner 路由、工具契約或可重用模板。
- 說明一個可重現的 failure mode、適用邊界、成本或停止條件。
- 提供去識別的通用案例，並清楚標示 inference、unknown 及驗證限制。

Workflow proposal 表單是底座維護專用，用來評估通用控制或程序，不是採用者產品缺陷的必填表。已確認的內容錯誤可直接提出修正，毋須等同一錯誤重複發生。

## 不可提交到這個公開 repository

- credentials、tokens、cookies、private keys 或未遮蔽的 .env；
- 個人、客戶、供應商、員工、帳戶或 workspace 識別資料；
- private URLs、個人絕對路徑、日誌、截圖、raw conversation、Memory 或 session／audit 底稿；
- 未去識別的產品需求、內部系統細節或私人驗證證據。

上游公開禁入規則適用於整個本 repository，包括 examples、tests、issues 和 PR。不要把「例子」或「維護者專用」當成提交私人資料的例外。

## 審查內容

請說明問題、公開 source 或可重現 evidence、改動範圍、適用及不適用情境、可能成本和剩餘未知。修改底座規則時，指出新文字應由哪個 active owner 維護；避免在舊 docs、templates 或 metadata 中建立第二套裁決規則。

PR template 提供底座審查項目。只有與該改動相關的檢查才適用於其驗證欄位；公開資料禁入規則始終適用。單一成功案例不能證明整套 workflow 有效，也不能把 local check、test、runtime 或 GitHub status 擴大解讀成未實際驗證的結果。

## 驗證 owner 與發布 QA

[.github/workflows/framework-checks.yml](.github/workflows/framework-checks.yml) 是本底座工具及 CI 命令的實際 owner；依該 workflow 和被它呼叫的腳本核對精確命令與範圍，不在本文件複製一份容易過時的命令清單。workflow 只在它明確配置的上游 repository 條件下執行。下游或 fork 上顯示 skipped 的 job 不是測試成功，也不證明其工具或產品通過。

每次公開發布仍須額外完成一次涵蓋整個 repository tracked Markdown 的 links／anchors QA，並進行公開 privacy、claim 和 license 審查。scripts/check_docs.py 的 default 與 --project-docs 檢查範圍由其程式和工程入口定義；它不是全庫 Markdown QA。不得以這些腳本的 PASS 代替發布所需的全庫檢查。

任何未執行的檢查均標為 NOT_RUN，並說明對發布或結論的影響。此候選的 GitHub Actions matrix 尚未執行。

## 授權與署名

對本 repository 提交文字、圖表、文件模板或其他方法論模板，即確認你有權提供，並同意依原 [CC BY 4.0 license](LICENSE) 授權。對 scripts/**、tests/** 或 .github/workflows/** 提交的程式內容，依 [MIT License](LICENSE-CODE) 授權。提交前請確認來源及第三方材料沒有超出其 license 條件。

這些條款只說明本通用底座的內容範圍，不替下游項目選擇產品內容或程式碼 license。
