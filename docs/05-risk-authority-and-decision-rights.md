# 05 — 風險、授權與決策權

## 1. 風險適應，而非一律保守

合理 autonomy 取決於 blast radius、recoverability 與 evidence quality：

| 情況 | 預設行為 |
| --- | --- |
| read-only、diagnostic、local、可逆 | 主動執行並回報 evidence |
| low-risk write、target 明確 | 最小修改後 readback/targeted verify |
| production/customer/formal data | 預設先確認 identity、scope、authority、recovery |
| auth/permissions/data lifecycle/deployment | Challenge + spec/decision gate + cross-layer verification |
| destructive/permanent | exact targets + necessity + recoverability + informed consent |
| external send/publication/payment/account change | 明確授權，必要時由人完成 identity/2FA gate |

## 2. Authority 不是 yes/no

最低 authorization contract：

| Field | 問題 |
| --- | --- |
| Target | 哪個 repo、workspace、data source、account、environment？ |
| Operator | 誰執行？誰 approve？誰負責 verification？ |
| Mutation class | read、edit、write、publish、deploy、delete 哪一種？ |
| Lifetime | one-shot、current task/session、project-durable？ |
| Preconditions | identity、dry-run、count guard、backup、test、review？ |
| Revalidation trigger | 新 target、tool、format、permission surface、risk escalation？ |
| Recovery | cancel、rollback、compensation、manual remediation 由誰授權？ |

「允許 edit」不代表允許 push；「允許 push」不代表允許 public publication；「允許原 action」也不自動授權 production verification 或 rollback mutation。

## 3. 新訊息與 mid-task steering

收到新指示時先分類：

- **Replace**：新 objective 取代舊任務；freeze 尚未 dispatch 的 mutation。
- **Add**：新增要求但保留原 objective；重算 scope、risk 與 plan。
- **Constraint**：收窄 authority 或新增 non-goal；立即套用到未執行工作。
- **Question/status**：回答後繼續原任務，不把它誤認為取消。

若 authority、target 或 risk 有實質改變，重新跑 precondition；不要沿用過期 grant。

## 4. Destructive gate

任何 delete、overwrite、reset、clean、archive 或平台「近似刪除」先過兩道 gate。

### Necessity

- exact targets 是什麼？
- 是否直接服務本任務 objective？
- 有無 rename、quarantine、copy-on-write、ignore、disable 等非破壞替代？
- target 是否為本任務建立且 ownership 清楚？

### Impact / recoverability

- tracked、untracked、ignored、modified？
- 是否跨 repository/workspace 或使用 glob/tree？
- 是否含 data、media、backup、archive 或其他人的工作？
- exact recovery source 在哪裡？恢復是否已驗證？
- 平台 semantics 是 permanent delete、trash、archive 還是 soft delete？

只要 target、ownership、scope、expansion 或 recovery 有不確定，就保留並詢問。

## 5. Remote mutation 與 outcome unknown

Remote write dispatch 前保存 grant snapshot 與 operation identity；之後保存 operation receipt。若 target service 已核實支援 idempotency，才使用 idempotency key，並記錄其 scope、TTL、request-match 與 replay semantics。

遇 timeout/disconnect：

1. 不直接判失敗。
2. 若 service 支援已驗證的 idempotency，不用新 key 重送；沿用原 key 也只代表依該 service contract 嘗試 duplicate suppression，不保證 exactly-once。
3. 先 readback/reconcile。
4. batch 逐 item 記 success/failure/unknown。
5. eventual consistency 的 early negative read 仍可能是 unknown。
6. 沒有 idempotency support 時，以 stable business identity、server receipt 與 authoritative readback reconcile，不盲目重送。
7. 無法判定就停止，保留 evidence 與 next verification owner。

One-shot authority 在 dispatch 時視為 consumed；結果未知不等於 grant 自動恢復。

本章的 authorization ledger 是 workflow decision record；除非它已 machine-bound 到實際 execution control，否則不構成 IAM、capability 或 runtime policy enforcement。每個 Grant ID 都應指向可查的 authoritative approval source。

## 6. Decision rights matrix

建議最少分五種角色：

| Role | 責任 |
| --- | --- |
| Objective owner | 決定要解決什麼與 priority |
| Operator | 在既定 boundary 執行 |
| Approver | 授權高風險 crossing |
| Verifier | 判斷 evidence 是否支持 claim |
| Closure owner | 確認 adoption、residual risk 與正式收口 |

一人可兼多角，但角色不能因 tool 便利而消失。

## 7. Decision lock 與 reopen

複雜工作可以鎖定已驗證方向，避免每輪重開全部策略。每個重要 decision 記：

```text
ID / statement / scope / assumptions / depends-on
/ invalidates / state / reopen trigger
```

子決策失敗通常只 reopen 該子層；若推翻 shared assumption，所有依賴項轉成 `needs revalidation`。只有新 evidence、objective/constraint 改變或 owner 明確解鎖，才重開上層 invariant。

## 8. Stop conditions

以下情況應停止並尋求新 authority 或 evidence：

- target identity 不清；
- wrong account/workspace 風險；
- destructive impact/recovery 不明；
- external/public/production mutation 未授權；
- repeated failure 沒產生新 evidence；
- remote outcome unknown 且無安全 reconciliation path；
- evidence 只能支持比預期更小的 claim，而 owner 不接受縮小 scope。
