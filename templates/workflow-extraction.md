# Workflow Extraction

## Problem / observed pattern

- Trigger/context: `<when it appears>`
- Independent occurrences: `<count/scope if proposing a reusable control; no private data>`
- Current handling: `<...>`
- Observed failure or cost: `<...>`

## Existing guidance diagnosis

依[系統演化指引](../docs/07-system-evolution.md#先診斷既有指引)先判斷要修哪一層。已確認的內容錯誤不必等再次發生；無法核實的歷史保留 Unknown。

- Existing guidance / owning section: `<source, or none found within stated search scope>`
- Event-time rule and retrieval/execution evidence: `<version, evidence, or Unknown>`
- Current guidance already corrected: `<yes/no/Unknown; relevant difference>`
- Diagnosis: `<missing/ambiguous/conflicting/over-broad rule; routing/execution/tool gap; new context; Unknown>`

## Candidate disposition

`<correct existing guidance / improve routing or execution / add example / retain case / propose new control>`

Smallest change and reason: `<...>`

## Landing-point decision

- [ ] Current docs
- [ ] Runbook
- [ ] Skill
- [ ] Helper/script
- [ ] Software test
- [ ] Agent eval
- [ ] Plugin/bundle
- [ ] Do not institutionalize yet

Why this is the smallest correct layer: `<...>`

## Trigger contract

- Positive cases: `<should trigger>`
- Negative cases: `<must not trigger>`
- Boundary cases: `<requires judgment>`

## Evidence and effectiveness

- Baseline: `<if available>`
- Expected intercept: `<actual failure to prevent>`
- Operator cost: `<...>`
- Measurement: `<eligible/invoked/bypassed/reopen/etc.>`

## Promotion / pruning condition

- Promote when: `<stable evidence>`
- Revise/remove when: `<false trigger, no impact, duplication, stale>`
