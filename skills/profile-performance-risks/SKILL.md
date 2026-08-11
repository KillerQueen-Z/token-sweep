---
name: profile-performance-risks
description: Investigate likely latency, throughput, memory, I/O, database, concurrency, and scaling risks and design measurements before optimization. Use for performance reviews, bottleneck hypotheses, profiling plans, slow-path analysis, capacity risks, benchmark design, or productive high-reasoning quota use without speculative code changes.
---

# Profile Performance Risks

Separate measured bottlenecks from code-based hypotheses. Do not optimize without an observable target.

## Define the performance contract

Record the workload, user-visible metric, scale, environment, percentile or throughput target, and known baseline. If unavailable, state assumptions and make measurement the first recommendation.

Read [references/performance-checklist.md](references/performance-checklist.md).

## Model the path

1. Trace one scoped request, job, render, or data pipeline end to end.
2. Identify CPU work, allocations, serialization, network hops, queries, filesystem I/O, locks, queues, caches, retries, batching, and fan-out.
3. Estimate algorithmic growth and multiplicative effects such as N+1 queries, nested scans, repeated parsing, or retry storms.
4. Locate existing metrics, traces, benchmarks, load tests, and production constraints.

## Gather evidence

Run existing benchmarks or focused local measurements when safe. Preserve comparable inputs and environment metadata. Avoid production load, paid services, destructive datasets, and installing profilers without authorization.

Classify observations:

- `measured bottleneck`: reproduced with relevant workload and metric;
- `strong hypothesis`: direct path evidence and plausible magnitude, awaiting measurement;
- `weak hypothesis`: possible but insufficiently bounded; keep out of ranked findings.

For every optimization idea, state the predicted metric movement, measurement method, correctness risk, and rollback signal.

## Report

Use [assets/performance-risk-report.md](assets/performance-risk-report.md). Prioritize measurement gaps and high-leverage bottlenecks. Include a reproducible benchmark or profiling plan, not just generic advice.

Do not implement optimizations unless the user explicitly requests changes.
