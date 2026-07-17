# 08 — 採用指南

## 1. 不要一次搬完整套

這個 framework 的價值在 decision quality，不在 process density。推薦由三個最小習慣開始：

1. 每個 non-trivial task 先寫 objective + boundary。
2. 所有重要結論標 Verified / Inferred / Unknown。
3. 完成前寫「跑了什麼、沒跑什麼、claim 到哪一層」。

## 2. 第一週：建立最小閉環

- 使用 `templates/task-brief.md`。
- 只選 Fast 或 Standard，暫不新增複雜 gate。
- 任務完成後回寫 owning truth source。
- 追蹤一次 false closure 或 wrong-boundary incident。

成功條件：團隊能區分「做了」與「已驗證完成」。

## 3. 第二週：風險分流

- 定義哪些 mutation 必須 Assured。
- 建立 destructive/publication/production gate。
- 寫清 decision rights：operator、approver、verifier、closure owner。
- 為 outcome unknown 設 reconciliation rule。

成功條件：低風險工作不被拖慢，高風險 crossing 不靠臨場猜測。

## 4. 第三週：AI collaboration stack

- 盤點 instructions、docs、Memory、Skills、connectors、helpers、tests/evals。
- 找出 duplicate、stale 與 conflicting authority。
- 將一個重複 workflow 變成 runbook 或 Skill。
- 將一個可機械判定的 gate 變成 helper/test。

成功條件：AI 能在較少 prompt 重複下找到正確 source 與 tool。

## 5. 第四週：量 effectiveness

開始記：

- gate eligible / invoked / bypassed；
- false closure / reopen；
- time-to-verified；
- operator cost；
- workflow routing errors。

先收 baseline，不設定懲罰性 KPI。刪除沒有 decision impact 的規則。

## 6. 個人使用版

最低工具組：

- 一份 task brief；
- repository-level instructions；
- authoritative docs map；
- verification report；
- 一個 workflow improvement log。

不要先建立大型知識庫或多 agent orchestration。

## 7. 小團隊使用版

增加：

- decision-rights matrix；
- PR/issue templates；
- definition of done 分層；
- release/handoff record；
- privacy/secret/publication gate；
- 1–2 條 end-to-end traceability pilots。

## 8. 高風險組織版

再增加：

- machine-readable authority/receipt；
- policy version/effective time；
- 已驗證的 idempotency semantics／無 idempotency 時的 authoritative reconciliation；
- maker/checker separation；
- immutable audit evidence；
- SLO/error-budget 或 assurance regime；
- persistent orchestration，但只在 volume 與 recovery path 已證明時。

## 9. 常見失敗模式

### 把所有工作升級成 Assured

後果：速度下降、規則被繞過。修正：Fast/Standard/Assured 明確分流。

### 把更多 docs 當成 Context Engineering

後果：context debt、conflict、stale retrieval。修正：按 owner、freshness、question relevance 選最小充分 context。

### 把 connector configured 當 connected

後果：錯帳號、錯 workspace 或 write failure。修正：current-surface read-only smoke + exact target readback。

### 把 Skill 數量當 maturity

後果：trigger collision、重複流程、maintenance burden。修正：reuse-before-create + usage/effectiveness review。

### 把 push/deploy 當 closure

後果：artifact/runtime/adoption gap。修正：用 delivery lifecycle 精確命名狀態。

### 把 subagents 當獨立真相

後果：同一錯誤被多次複述。修正：讓 reviewer 使用不同 evidence surface，最後由主 agent/human reconcile。

### 把所有 unknown 變成 blocker

後果：失去推進能力。修正：區分可編碼 uncertainty、claim-limiting uncertainty 與 authority/identity hard stop。

## 10. 最小 definition of done

```text
Objective achieved
AND exact scope respected
AND action receipt exists
AND minimum verification passed
AND claim fits evidence
AND current truth updated
AND residual risk owned
```

如果其中一項不成立，不必說失敗；只需用正確狀態交付。
