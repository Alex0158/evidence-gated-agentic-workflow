# Contributing

歡迎提出能令方法更清楚、可執行或可驗證的改進。

## 適合的貢獻

- 修正模糊、矛盾或過度宣稱的規則。
- 提供可重用的 task brief、gate、verification 或 handoff 模板。
- 加入具體 failure mode、stop condition 或 rollback pattern。
- 提供有 claim boundary 的案例；請去除個資、secrets、客戶與內部系統識別資料。
- 用 evidence 說明某個 gate 沒有效果、成本過高或容易被繞過。

## 不適合的貢獻

- 原始對話、私人 Memory、chain-of-thought 或內部審計底稿。
- tokens、cookies、credentials、內部 URLs、個人路徑或帳號識別資料。
- 把單一案例包裝成普遍定律。
- 只增加術語或規則，卻沒有 decision impact、trigger 與驗證方法。

## Pull request 最低內容

1. Problem：現有內容造成什麼實際問題？
2. Evidence：依據是什麼？哪些只是 inference？
3. Change：改了什麼，沒有改什麼？
4. Impact：適用範圍、可能誤觸發與遷移成本。
5. Verification：links、rendering、examples 或 consistency 如何驗證？

提交 contribution 即表示你同意將該 contribution 依本 repository 的 CC BY 4.0 授權發布，並確認你有權提供相關內容。

## 編輯原則

- 先改 current truth，不在正式文件堆疊逐輪歷史。
- 優先修改既有 canonical section；確定無法承接才新增檔案。
- 文字以繁體中文為主，technical terms 可保留 English。
- 不把 practitioner term 說成正式業界標準。
- 所有完成聲明必須與 evidence level 相配。
