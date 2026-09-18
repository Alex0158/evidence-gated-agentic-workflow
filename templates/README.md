# Templates

這些模板全部使用 placeholders；請按 risk profile 裁剪，不需要每次填滿所有欄位。

| Template | 用途 |
| --- | --- |
| [Task brief](task-brief.md) | 所有 non-trivial task 的最小 envelope |
| [Investigation](investigation.md) | read-only current-state / root-cause 排查 |
| [Implementation](implementation.md) | 一般 change/build 閉環 |
| [High-risk change](high-risk-change.md) | Assured challenge/spec gate |
| [Connector capability gate](connector-capability-gate.md) | Connector/MCP/App live capability 與 mutation gate |
| [Authorization ledger](authorization-ledger.md) | target、operator、mutation、lifetime 與 revalidation |
| [Operation receipt](operation-receipt.md) | remote/async mutation 與 outcome reconciliation |
| [Verification report](verification-report.md) | 限制完成聲明與 residual risk |
| [Handoff](handoff.md) | self-contained delivery/adoption closure |
| [Workflow extraction](workflow-extraction.md) | 先診斷既有指引，再決定修正、保留案例或新增候選 |
| [Public release](public-release.md) | 區分首次建立公開 repo 與既有公開 repo 更新 |

建議組合：

以下是所需資訊的組合，可合併在現有 task／PR／交付回覆；簡單任務不要求另建檔案。只有 handoff、recovery 或重用需要時才持久化更多資料，並保留可找回的必要證據。

- Fast：Task brief + Verification report。
- Standard：Task brief + Investigation/Implementation + Verification report。
- Assured：Task brief + High-risk + Authorization + Receipt + Verification + Handoff。
