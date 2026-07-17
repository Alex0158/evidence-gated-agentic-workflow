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
| [Workflow extraction](workflow-extraction.md) | 把重複做法沉澱為 durable asset |
| [Public release](public-release.md) | documentation/public repository 發布 gate |

建議組合：

- Fast：Task brief + Verification report。
- Standard：Task brief + Investigation/Implementation + Verification report。
- Assured：Task brief + High-risk + Authorization + Receipt + Verification + Handoff。
