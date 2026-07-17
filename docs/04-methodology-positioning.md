# 04 — 方法論定位

## 1. Prompt、Context、Harness、Loop 不是線性世代

把它們說成「Prompt Engineering → Harness Engineering → Loop Engineering」的正式發展階段會過度簡化。較準確的是四個相互重疊的 control surfaces／分析視角；下表只隔離各自主要回答的問題，不代表它們有乾淨、互斥的邊界：

| Layer | 核心問題 | 典型資產 |
| --- | --- | --- |
| Prompt Engineering | 這一次如何清楚表達 intent？ | instruction、example、output schema |
| Context Engineering | 模型此刻應看到什麼？ | scoped docs、Memory routing、live data、history compression |
| Harness Engineering | agent 在什麼環境中可靠地工作？ | files、tools、permissions、sandbox、tests、observability、recovery |
| Loop Engineering | 如何讓工作以 feedback 收斂並演化？ | investigate/act/verify、state、queue、retry/reconcile、human verdict |

Prompt 內容通常也是 context 的一部分，context/tool routing 常由 harness 承載，而 loop 又透過 harness 執行。一個 workflow 可以同時使用四者；差異在主要控制面，不在「已經進化到哪一代」。

## 2. 這套系統的位置

> **Harness-centric、Loop-aware、human-orchestrated、bounded-autonomy agentic workflow。**

- **Harness-centric**：可靠性主要來自 source routing、tools、permissions、tests、receipts 與 formal records，而非單次 prompt 技巧。
- **Loop-aware**：工作有明確 feedback、reopen、record、handoff 與 improvement paths。
- **Human-orchestrated**：objective、priority 與 high-impact verdict 仍由人負責。
- **Bounded autonomy**：AI 在已授權、可逆、scope-clear 的內循環主動推進；高風險 crossing 保留 human gate。

只有當 discovery、queue、state transition、multi-loop dispatch、recovery 與 unattended execution 成為持久日常，才適合進一步稱為 always-on orchestration 或 agentic software factory。

## 3. 與 TDD 的關係

推薦的 defect 子循環是：

```text
Evidence → Red or equivalent failure proof
→ Green → behavior-preserving Refactor → Record
```

因此本 repository 用 **TDD-compatible / TDD-shaped evidence-first repair** 作為保守的 project shorthand，但不自動等於 strict TDD：

- failing automated test 不一定永遠先於 production code；
- docs、research、data repair 與一次性 operations 不應硬套 TDD；
- 無法自動化 Red 時，允許使用可重現 log、runtime readback 或 contract mismatch，但要標明。

只有在 implementation 前穩定建立 failing automated tests，才應聲稱採用 test-first TDD practice。

## 4. 與 Spec-Driven Development 的關係

高風險或 cross-layer 工作要求先定義 intent、constraints、affected surfaces、failure modes、success、non-goals、verification 與 rollback。本 repository 用 **spec-governed / spec-gated，SDD-like** 作為 project shorthand。

它不是 strict SDD，因為：

- 小任務不一定先寫完整 spec；
- current behavior 有時仍由 code/runtime 裁決；
- spec 不一定自動生成全部 plan、code 與 tests；
- docs 與 code 衝突時，需要先辨認 owning authority，不能假設文件天然正確。

本 repository 只會在具備 spec → plan → task → code → test → runtime 的可查 traceability，以及 spec change 驅動 revalidation 的穩定 gate 時，使用「完整 SDD」標籤。這是本框架選擇的 assurance bar，不是對所有 SDD 實作的普遍定義。

## 5. Source of Truth

這是整套方法的基礎公理。本 repository 用以下 project-defined 描述性名稱表達它：

> **Federated Source-of-Truth Governance** 或 **authority-aware knowledge architecture**。

不同問題由不同 authority 裁決，而且要考慮 event time。它直接防止：

- Memory 冒充 current truth；
- config 冒充 live capability；
- source 冒充 artifact/runtime；
- draft/history 冒充 formal；
- local success 冒充 external closure。

## 6. 其他概念映射

下表是 structural mapping，不是 adoption certification。`Established family` 表示它對應已有廣泛文獻的概念家族；`Project description` 表示本 repository 為自身 pattern 採用的描述性短語；兩者都不證明某個 control 已被 benchmark 或持續有效執行。

| 概念 | Status | 在本 workflow 的形式與邊界 |
| --- | --- | --- |
| Evidence-Driven Engineering | Project description | Verified/Inferred/Unknown、provenance、falsifier、claim limit；不冒充 formal assurance |
| Progressive Assurance | Established family mapping | 風險越高，驗證梯度與 gate 越強；未主張特定 assurance standard |
| Requirements Engineering | Established family mapping | objective、constraint、success、non-goals、affected surfaces |
| Contract-aware Development | Project description | UI/API/data/config/runtime 等跨層 contract 一起看；未必有 consumer-driven contract tests |
| Human-in-the-loop | Established family mapping | high-impact approval、evidence sufficiency、accountability 保留給人；不自動保證安全 |
| Least authority | Established family mapping | 權限綁 target、operator、mutation class、lifetime 與 preconditions；workflow ledger 不等於 IAM enforcement |
| Docs-as-code / Living Documentation | Established family mapping | behavior 改變後同步 formal current truth，並由 Git 管理；仍需 freshness control |
| Double-loop Learning / Kaizen | Established family mapping | 不只修結果，也修 rule、routing、Skill、helper、test/eval |
| Risk-Driven Development | Project description | blast radius 決定流程強度；不是正式 maturity model |
| Reversible Engineering | Project description | smallest action、dry-run、copy-on-write、rollback/remediation |
| Provenance-aware Delivery | Project description | source、build、artifact、runtime、adoption 分層 |
| Socio-technical Systems Thinking | Established family mapping | operator、approver、verifier、owner 與 tool/account boundary 分開 |

## 7. 相似但不要過度命名

| 名詞 | 相似處 | 保守邊界 |
| --- | --- | --- |
| ATDD / BDD | 有 acceptance、true-chain、positive/negative/boundary cases | 未必 acceptance-test-first，也未必使用 Given/When/Then |
| Assurance Case | claim、evidence、provenance 與反證相連 | 未必有正式 claim-argument-evidence notation |
| Cybernetics | evidence、decision、action、feedback、reopen 形成控制循環 | 是結構類比，不是數學控制模型 |
| SRE | runtime evidence、rollback、partial failure、recovery | 未必有完整 SLI/SLO/error-budget regime |
| GitOps | Git、version diff、artifact binding | live state 未必 declaratively reconciled from Git |
| Event Sourcing | event-time authority、receipts、reconciliation | 未必可由 append-only event log 重建全部 state |
| Eval-Driven Development | 有 agent routing/trigger/failure evals | 未必所有 workflow 都 eval-first 並持續量化 |

## 8. Outer loop ownership

這套方法的成熟度不以「人完全退出」衡量，而以責任 topology 衡量：

- agent 負責在 boundary 內高速調查、執行、驗證與重試；
- human 負責 objective、constraints、risk appetite、evidence verdict 與 consequence；
- harness 負責讓兩者之間的 handoff 可觀測、可恢復、可審核。

這比追求最大 autonomy 更實用，也更適合 production、formal data、customer 或 irreversible workflows。

## 9. 參考來源

這些來源用於界定術語，不代表任何單一 framework 對本 workflow 的完整背書：

1. OpenAI — [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)
2. Anthropic — [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
3. Anthropic — [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
4. Anthropic — [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
5. GitHub — [Spec Kit](https://github.github.com/spec-kit/)
6. GitHub — [Spec-driven development with AI](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)
7. Addy Osmani — [Loop Engineering](https://addyosmani.com/blog/loop-engineering/)
8. Addy Osmani — [Own the Outer Loop](https://addyosmani.com/blog/own-the-outer-loop/)

`Loop Engineering` 與 `outer loop` 在此採 practitioner framing，不宣稱為正式標準或唯一命名。
