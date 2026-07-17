# Codex Adapter

這份 adapter 將本 repository 的 vendor-neutral workflow 映射到 Codex concepts。它不列出任何個人的 installed plugins、auth state、local paths 或 current capability inventory。

## Capability mapping

| Workflow need | Codex surface | 正確邊界 |
| --- | --- | --- |
| Durable operating rules | `AGENTS.md` / scoped instructions | 放穩定規則；current state 仍需 live verify |
| Cross-task routing | Memory | 找 source 的 index，不取代 current truth |
| Reusable procedure | Skill | workflow instructions；不等於 underlying capability 已可用 |
| Bundled distribution | Plugin | 可帶 Skills/MCP/Apps；不等於已 authenticated |
| Live external access | Connector / MCP / App | configured ≠ exposed ≠ authenticated ≠ correct target ≠ authorized |
| UI/session operation | Browser / computer use | rendered UI evidence 不自動證明 backend/data state |
| Long-running objective | Goal | 保存 objective/status；不擴張原始 authority |
| Parallel work | Subagents | worker result 要由 parent reconcile；不天然是 independent verifier |
| Local automation | scripts/helpers | 適合機械 gate；仍受 repo與 mutation boundary 約束 |
| Quality control | tests/evals | tests 驗 software；evals 驗 agent behavior/routing |

## Recommended interaction contract

### User task envelope

高品質請求不必很長，但應盡量提供：

```text
Objective
Current symptom/evidence
In scope / out of scope
Read/write/publish/deploy/delete authority
Desired closure level
Any hard stop or no-delete rule
```

缺資料時，Codex 應先做安全、read-only、會產生新 evidence 的工作，而不是把所有 troubleshooting 退回給使用者。

### Commentary

中途更新應短而可掃描：

- 現在確認了什麼；
- 接下來做哪一個 evidence-producing step；
- 只有真正影響方向的 assumption/blocker。

Commentary 不應假裝 final；也不應讓使用者長時間不知道 agent 是否仍在工作。

### Final

先給 outcome，再給：

- exact changed artifacts；
- verification run/pass/not run；
- closure level；
- residual risk 或唯一 blocker；
- 可點擊的 local/remote link。

## Capability smoke gate

問「某 connector 是否能用」時，依序證明：

1. current task 看得到 tool；
2. read-only stable probe 成功；
3. 正確 identity/workspace；
4. exact target 可讀；
5. 若要 write，tool capability 與 user authority 都存在；
6. write 後有 receipt/readback。

不要只因 CLI 顯示 configured 或一次 probe 成功，就聲稱 intermittent issue 已被官方修復或整個 workflow 已可靠。

## Skill lifecycle in Codex

1. 先找 existing Skill/Plugin，遵守 reuse-before-create。
2. 完整讀取 `SKILL.md` 與它指定的必要 references。
3. 依 trigger 使用，不自行擴大 scope。
4. Skill 造成 action/pause 時向使用者說明。
5. 重複 workflow 穩定後才建立或更新 Skill。
6. 以 positive/negative/boundary cases 驗證 trigger 與 failure handling。

## Multi-agent pattern

適合平行：

- 不同 repository/data/evidence surfaces；
- implementation、privacy review、QA 分離；
- taxonomy claim challenge；
- adversarial verification。

Parent agent 必須：

- 給清楚 input/output boundary；
- 防止多 agent 同改一檔；
- reconcile contradictions；
- 自己檢查共享 worktree；
- 只在整體 evidence 足夠時宣稱完成。

## Control-plane mutation

修改 global instructions、Memory、Skills、Plugins、MCP config、automations 或 hooks 會改變未來行為，不應只是因本次 workaround 有效就自動持久化。先取得 explicit authority，選最小 landing point，驗證後再版本化。

## Starter instruction file

可使用 [`AGENTS.example.md`](AGENTS.example.md) 作為 project-level 起點；`.example.md` 本身不會自動生效。

1. 複製內容到目標 repository root，並命名為 `AGENTS.md`。
2. 依該 repository 的 owner、source of truth、commands 與 risk boundary 裁剪；長 workflow 放進 docs 或 Skills。
3. 開啟新的 Codex task，要求它 read back applicable instructions 與 repository boundary，再用一個 read-only task 驗證載入。
