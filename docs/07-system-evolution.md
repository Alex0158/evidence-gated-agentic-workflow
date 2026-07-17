# 07 — 把重複成功演化成系統

## 1. Double-loop learning

第一層 loop 修任務：

```text
problem → action → verification → result
```

第二層 loop 修系統：

```text
repeated success/failure
→ identify rule/routing/tool gap
→ choose smallest durable landing point
→ verify trigger and non-trigger
→ observe effectiveness
→ keep, revise, or prune
```

## 2. Landing-point ladder

| Pattern | 最小落點 |
| --- | --- |
| 一次性但值得追溯 | decision note / issue / record |
| 穩定 current truth | authoritative docs |
| 重複 procedural workflow | runbook / Skill |
| 可機械判定的高頻步驟 | helper / script / CI gate |
| software behavior regression | test |
| agent routing/quality regression | eval |
| 多個能力需一起 distribution | Plugin |
| 高量 recurring orchestration | persistent state/queue，最後才考慮 |

不要一發現 pattern 就直接做 Plugin 或自動化。

## 3. Skill lifecycle

### 建立前

- 是否至少重複出現？
- trigger 能否用一句話判定？
- owner、source、tool、authority 與 output contract 是否清楚？
- failure modes 是否穩定？
- instruction 或現有 Skill 是否已可承接？

### 建立時

- 使用 progressive disclosure；
- 核心 `SKILL.md` 保持 routing、gates 與最低流程；
- 長 reference、scripts、templates 分離；
- 寫 positive、negative、boundary eval；
- 明確說明何時不能使用。

### 建立後

- 驗證 trigger hit 與 false trigger；
- 驗證 output/side effects；
- 追蹤 bypass、reopen、manual override 與 operator cost；
- 重複或低價值時合併／移除。

## 4. Control effectiveness > control density

規則存在不等於 gate 有跑；gate 有跑不等於攔截了錯誤；攔截錯誤也不一定值得成本。

推薦觀測：

- eligible opportunities；
- gate invoked / bypassed；
- actual error intercepted；
- false closure / reopen；
- manual override；
- routing accuracy；
- time-to-verified；
- operator cost；
- false positive / unnecessary escalation。

分開 actual outcome 與 counterfactual avoided loss；後者只能標為 inference。

## 5. Shadow observation pilot

在自動化更多 gate 前，可用 `4–6 週` 或 `30–50 tasks` 作 pilot heuristic；這不是統計充分性保證。

先定義：

- sampling frame、included task types、exclusions；
- missing/censored cases；
- 每個 stratum 的 `observed / eligible`；
- behavior 是 spontaneous、existing-rule-induced、observer-induced 還是 unknown；
- passive observation 與 active intervention 分段；
- rule/protocol version 與 effective time。

Baseline 期不要立 performance target，也不要用 metrics 評價人或 agent，避免 Goodhart effect 與 observer effect。

## 6. Context/policy inventory

定期盤點 Instructions、Memory、Skills、runbooks、docs 與 gates：

- owner；
- freshness；
- duplicate/conflict；
- retrieval path；
- actual usage；
- bypass/reopen；
- removal condition。

目的不是建立更大知識庫，而是降低 context debt 與 policy entropy。

## 7. Traceability pilot

對 1–2 個高頻 workflow 建立一條 evidence chain：

```text
objective/spec
→ decision/authority
→ change
→ test/runtime evidence
→ artifact/deployment
→ handoff/adoption
→ closure
```

先證明這條 chain 有用，再考慮 machine-readable task envelope、state machine 或 persistent queue。

## 8. Pruning gate

每季問：

1. 哪些 gate 真正攔截高代價錯誤？
2. 哪些只是重複另一層 authority？
3. 哪些從未 trigger，或 trigger 後沒有 decision impact？
4. 哪些造成過度升級、context bloat 或 delegation bottleneck？
5. 能否用一個 mechanical check 取代三段文字？

成熟不是規則累積，而是少量、可執行、可觀測、可刪除的 control plane。

## 9. 推薦演化順序

1. shadow observation；
2. control-effectiveness baseline；
3. context/policy inventory；
4. end-to-end traceability pilot；
5. canonical task envelope；
6. machine-checkable gates/receipts；
7. persistent state/queue；
8. 持續 pruning。

不要以最大 autonomy 為 KPI。更好的目標是：在不犧牲 truth、authority、verification 與 accountability 的前提下，把人的注意力移到最高價值的 outer-loop decisions。
