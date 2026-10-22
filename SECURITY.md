# Security and privacy

本 repository 是一個公開的通用工作方法與工具底座。提交內容、issue、PR、example、log 或 screenshot 時，都必須避免公開 secrets、個人資料、客戶資料及私人工作 evidence。

## 不要提交

- API keys、tokens、cookies、passwords、private keys 或 credential store；
- .env、browser/session exports 或其他可用憑據；
- 個人 email、電話、地址、account、workspace 或 page IDs；
- customer、supplier、employee、order、payment 或 private business data；
- 個人絕對路徑、private URLs、logs、screenshots 或 raw conversation；
- Memory、rollout/session/thread IDs 或私人審計底稿。

## 回報安全問題

不要在 public issue 或 PR 貼入漏洞細節、credentials、個人資料或 private evidence。本文件不代表此 repository 已啟用 GitHub private vulnerability reporting，也不承諾任何未明示的私人回報功能已可用。提交前請在目前 repository 的 GitHub 安全設定中核實維護者明確提供的私下回報途徑；若沒有已確認的私人途徑，不要把敏感內容送到公開表單或底座作者的其他帳戶。

若你採用本底座，需由自己的 repository owner 設定並核實自己的安全回報途徑。複製來的文件不會把下游問題私下送到此 repository；不要沿用原上游的回報目的地。

若疑似 credential 已進入 Git history，先依該系統的程序 revoke／rotate，再由有權管理者處理 history。只從最新檔案移除內容並不足以消除已暴露的憑據。

## Scope

本 repository 提供 workflow guidance 和本地文件工具，不保證使用者系統的 security、safety 或 regulatory compliance。實際產品與 deployment 仍需由相應 owner 做專業審查及技術控制。

不要把本底座作為提交私有產品設計、工作底稿、客戶資料或原始對話的地方。
