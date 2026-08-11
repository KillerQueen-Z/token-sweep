# Deep review checklist

Use only sections relevant to the target.

## Correctness and contracts

- Boundary values, null/empty states, unit conversions, parsing, serialization, and schema evolution.
- Authorization before effects; validation before persistence or external calls.
- Public API, CLI, configuration, and database contract compatibility.
- Partial success, duplicate delivery, retry, cancellation, and timeout behavior.

## State and concurrency

- Atomicity across reads, writes, queues, caches, and external side effects.
- Lock scope, lost updates, stale reads, races, deadlocks, and ordering assumptions.
- Idempotency keys, deduplication, replay safety, and cleanup on every exit.

## Failure and operations

- Error propagation, fallback correctness, retry bounds, backoff, and circuit breaking.
- Resource lifetime, leaked handles, unbounded work, and shutdown behavior.
- Logs and metrics that preserve diagnosis without exposing secrets.

## Security and data

- Trust-boundary transitions, injection, path traversal, SSRF, unsafe deserialization, and confused-deputy paths.
- Secret handling, sensitive-data minimization, tenant isolation, and permission scope.
- Dependency and build-script behavior when directly relevant.

## Finding threshold

Exclude preferences, speculative future scale problems, unreachable paths, lint-only concerns, and claims already disproved by tests or guards.
