# 03 — AI / Codex 協作堆疊

## 1. AI 不是單一 chat box

一個可靠 agentic workflow 通常包含多個能力層：

```text
Instructions
→ Context / Memory / Docs
→ Skills / Runbooks
→ Tools / Connectors / MCP / Browser
→ Helpers / Scripts
→ Tests / Evals / Receipts
→ Git / Formal records
→ Human outer-loop verdict
```

各層回答不同問題，不能互相冒充。

## 2. Instructions / AGENTS.md

用途：保存 durable、cross-task 的行為規則與安全邊界。

適合放：

- language、communication、verification defaults；
- repository boundary 與 source-of-truth routing；
- destructive、external、production mutation gates；
- repeated failure modes。

不適合放：

- 易變的 current state；
- persona biography；
- 一次性 task detail；
- 長篇 workflow 教程；
- secrets。

## 3. Context 與 Memory

Context Engineering 的目的不是把所有資料塞進 prompt，而是讓當前 decision 取得最小充分、最新、可追溯的 context。

Memory 適合作：

- routing index；
- durable preference；
- repeated boundary；
- known failure mode。

Memory 不應取代 current code、live data、runtime 或 formal source。

## 4. Skill

Skill 是可觸發、可重跑、帶指令與可能帶 scripts/templates 的 workflow package。

適合做 Skill：

- 任務會重複；
- trigger 可清楚命名；
- 有固定 evidence path、gates 與 output contract；
- 失敗模式可測；
- 比單純 instruction 更需要 procedural guidance。

不適合做 Skill：一次性內容、尚未穩定的 brainstorm，或只需一條 durable rule 的事情。

## 5. Plugin

Plugin 是 distribution/bundling layer，可一起提供 Skills、MCP servers、apps 或其他 capabilities。它不是一個直接「執行」的魔法按鈕。

當多個 workflows 共享同一 domain、依賴、tool surface 與 distribution lifecycle 時，才考慮由 Skills 升成 Plugin。

## 6. Connector / MCP / App

Connector 或 MCP 提供 live system access。可用性至少要分五層：

```text
configured
→ exposed in current task
→ authenticated
→ correct identity/workspace
→ target readable/writeable
```

其中任一層成功都不能代表後續層成功。Read capability 也不能推導 write authority。

Live gate 建議：

1. 檢查 tool 是否在 current surface；
2. 做穩定、read-only smoke；
3. read back exact target；
4. mutation 前重新核對 identity、scope 與 authority；
5. mutation 後取得 receipt/readback。

## 7. Browser / Computer Use

當 target 只存在於 rendered UI、session state、local app 或 human-facing workflow 時使用。Browser 能「看到」不等於 API/data layer 已確認；必要時將 UI、network、backend 與 formal data evidence 分層。

## 8. Helper / Script

Helper 適合把高頻、可判定、低歧義的步驟 machine-check：

- preflight；
- dry-run；
- schema/manifest checks；
- exact packaging；
- count guard；
- post-write reconciliation。

不要把尚未理解的 judgment 直接自動化。

## 9. Tests 與 Evals

- Test 檢查 software behavior 或 contract。
- Eval 檢查 agent routing、output quality、tool use、trigger 與 failure handling。
- Receipt 證明某個 operation 被接受、執行或 read back。

Subagent review 可增加角度，但同模型、同 context 的 subagent 不天然等於 independent verifier。重要 verdict 要有可查 evidence 或不同 failure surface。

## 10. Goal 與 multi-agent

Goal 保存長任務 objective、進度與 completion condition；它不是 scope expansion authority。

Multi-agent 適合可平行、邊界清楚的工作：不同 evidence surfaces、正反 challenge、privacy audit、implementation 與 independent QA。主 agent 仍需 reconciliation，不能因 worker 說完成就宣稱整體完成。

## 11. Human outer loop

AI 內循環：

```text
investigate → implement → verify → repeat
```

Human 外循環：

```text
choose objective
→ define constraints and decision rights
→ judge evidence sufficiency
→ approve high-impact boundary crossings
→ own consequences
→ evolve or prune the system
```

最好的 automation 不是移除所有人，而是把人的注意力移到 evidence、risk、taste、accountability 與 irreversible decisions。
