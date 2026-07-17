# Authorization Ledger

這是 workflow decision record；除非已明確 machine-bound 到實際 execution control，否則不是 IAM、capability 或 runtime enforcement。每個 Grant ID 都必須指向 authoritative approval source。

| Grant ID | Target | Operator | Mutation class | Lifetime | Preconditions | Revalidate when | State |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `<G-001>` | `<target>` | `<operator>` | `<read/write/etc.>` | `<one-shot/task>` | `<checks>` | `<trigger>` | `<active/reserved/consumed/revoked/expired>` |

## Grant source

- Authoritative approval source/approver: `<message/record/reference>`
- Effective from: `<time/event>`
- Superseded by: `<if any>`
- Non-precedent waiver: `<yes/no>`

## In-flight policy

- Cancellation authority: `<...>`
- Compensation/rollback authority: `<...>`
- Verification owner after revoke/expiry: `<...>`

## Notes

- One-shot grant becomes reserved/consumed at dispatch; unknown outcome does not restore it.
- New target, tool, format, permission surface or risk level requires revalidation.
- Original action authority does not automatically authorize mutating verification or rollback.
