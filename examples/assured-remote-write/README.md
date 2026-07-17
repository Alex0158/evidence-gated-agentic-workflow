# Example — Assured remote write

## Task

在 fictional inventory service 為 exact SKU 建立一次 replenishment request。Remote API 可能 timeout。

## Brief

- Objective：只建立一筆 request，不能 duplicate。
- Profile：Assured。
- Target：`SKU-DEMO-001` in `sandbox-warehouse`。
- Authority：one-shot create；不授權 delete、retry with new key 或 production target。
- Preconditions：identity readback、existing-request query、preview，以及已核實 scope/TTL/request-match semantics 的 service-side idempotency key。
- Closure target：Remote verified。

## Preflight

1. Read back workspace = `sandbox-warehouse`。
2. Query stable business key，沒有 existing open request。
3. Preview quantity/target。
4. Reserve grant `G-001`。
5. Dispatch with idempotency key `demo-request-001`。

## Ambiguous response

API 在 response 前 timeout。此時狀態是：

```text
outcome unknown
```

不是 confirmed failure，因此不使用新 key 重送。

## Reconciliation

1. 以 business key 查詢，early read 為空；因 system 有 eventual consistency，仍是 unknown。
2. 等已知 consistency window 後以原 operation/idempotency reference 查詢。
3. Server 返回一筆 request 與 matching receipt。
4. Read back SKU、quantity、workspace 均正確。

## Final state

- Confirmed success；只有一筆 request。
- One-shot grant 已 consumed。
- 沒有 second mutation。
- Receipt 與 readback 支持 Remote verified。

若 consistency window 後仍無 authoritative result，正確 closure 應是 `outcome unknown; verification owner assigned`，而不是冒險重送。
