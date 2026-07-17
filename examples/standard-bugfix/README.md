# Example — Standard bugfix

## Task

Sample API 對空白 display name 回傳成功，但 contract 要求 validation error。

## Brief

- Objective：空白 display name 被拒絕，合法名稱維持原行為。
- Owner：`sample-api` repository。
- Profile：Standard。
- Non-goals：不重構整個 validation framework。
- Closure target：Implemented + targeted verified。

## Evidence / Red

新增 failing unit test：

```text
given display name = whitespace
when update profile
then return validation error
```

測試在修改前失敗，現有合法名稱 test 通過。

## Action / Green

在 owning validator 加入 trimmed-empty check；沒有修改 shared dependency 或 unrelated endpoint。

## Verification

- New failing test：修改前 fail，修改後 pass。
- Existing validator unit tests：pass。
- Targeted API integration test：pass。
- Full repository suite：not run，因本例只示範 targeted closure。
- Runtime deployment：not performed。

## Record and claim

```text
Implemented and targeted-verified.
Full-suite regression and deployed runtime remain unverified.
```

這是 TDD-shaped，而且本例確實 test-first；仍不由單一例子推論整個團隊採用 strict TDD。
