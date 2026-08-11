# Performance risk checklist

- Algorithmic complexity at realistic cardinalities and adversarial inputs.
- N+1 queries, missing indexes, wide reads, full scans, chatty calls, and unnecessary serialization.
- Unbounded concurrency, queue growth, lock contention, head-of-line blocking, and missing backpressure.
- Allocation churn, retained objects, large buffers, copies, compression, and garbage-collection pressure.
- Cache hit assumptions, invalidation, stampedes, cold starts, and memory ceilings.
- Retry amplification, timeout layering, fan-out tails, rate limits, and connection-pool exhaustion.
- Batch size, pagination, streaming, checkpointing, and work duplication.
- Benchmark representativeness, warmup, variance, percentiles, environment noise, and correctness checks.
