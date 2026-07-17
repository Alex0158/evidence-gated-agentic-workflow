# Security and privacy

這是一個 documentation repository，但內容仍可能出現 credentials、個人資料、內部路徑或客戶識別資訊。

## 不要提交

- API keys、tokens、cookies、passwords、private keys；
- `.env`、credential store、browser/session exports；
- 個人 email、電話、地址、account/workspace/page IDs；
- customer、supplier、employee、order、payment 或 private business data；
- local absolute paths、private URLs、logs、screenshots 或 raw conversation history；
- Memory、rollout/session/thread IDs 或私人審計底稿。

## 回報方式

若發現敏感內容，請不要建立含原文的 public issue。請使用 GitHub repository 的 private vulnerability reporting 功能聯絡 maintainer，並只提供定位所需的最少資料。

若疑似 credential 已進 Git history，應先 revoke/rotate，再處理 history。只從最新 commit 刪除並不足夠。

## Scope

本 project 提供 workflow guidance，不保證使用者系統的 security、safety 或 regulatory compliance。實際 deployment 仍需相應專業審查與技術控制。
