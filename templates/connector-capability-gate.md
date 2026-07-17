# Connector / MCP / App Capability Gate

## Intended operation

- Mode: `<capability check / read / write / publish>`
- Target system: `<generic system>`
- Exact target: `<workspace/project/record placeholder>`

## Capability ladder

- [ ] Configured/installed
- [ ] Exposed in current task
- [ ] Authenticated
- [ ] Correct identity/workspace
- [ ] Exact target readable
- [ ] Required write capability available
- [ ] Mutation explicitly authorized

## Read-only smoke

- Stable probe: `<search/fetch/status>`
- Expected result: `<...>`
- Actual result: `<...>`

## Mutation preflight

- Identity rechecked: `<evidence>`
- Scope/authority: `<grant>`
- Dry-run/preview/count guard: `<result>`
- Retry safety/reconciliation: `<if service semantics are verified: idempotency key + scope/TTL/request-match; otherwise stable business identity + authoritative readback>`
- Stop condition: `<...>`

## Post-write

- Operation receipt: `<...>`
- Readback: `<...>`
- Outcome: `<confirmed success / failure / partial-mixed / unknown>`
- Cleanup/remediation: `<...>`
