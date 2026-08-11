---
name: find-test-gaps
description: Discover consequential behavior that lacks meaningful automated coverage and design concrete, high-value tests. Use when asked for test-gap analysis, missing tests, coverage improvement, regression prevention, edge-case discovery, test strategy, or a productive quota sweep focused on correctness without editing code by default.
---

# Find Test Gaps

Optimize for defects prevented, not lines covered.

## Establish the coverage model

1. Read repository instructions and locate test commands, frameworks, fixtures, helpers, and CI gates.
2. Inventory existing tests by behavior and boundary rather than filename.
3. Map the scoped runtime path from input through side effects and terminal outcome.
4. Identify high-cost failures: money, authorization, data loss, availability, compatibility, irreversible effects, and silent corruption.

Read [references/gap-checklist.md](references/gap-checklist.md) before ranking gaps.

## Generate and challenge candidates

Look for untested branches at trust boundaries, state transitions, retries, partial failures, concurrency edges, time behavior, schema evolution, and cleanup paths. Search existing tests and helpers before declaring a gap.

Reject candidates that only increase coverage numbers, duplicate an existing behavioral assertion, depend on unstable implementation details, or cannot express a meaningful oracle.

## Rank gaps

Score each candidate by:

- failure impact;
- likelihood and historical plausibility;
- absence of equivalent coverage;
- ability to create a deterministic oracle;
- implementation and maintenance cost.

Prefer a small ranked set. For each gap, specify setup, action, assertions, test layer, fixtures/mocks, and the defect class it prevents.

When useful and already supported by the repository, run focused coverage or mutation tooling. Do not install tools, update snapshots, or weaken assertions without explicit authorization.

## Report

Use [assets/test-gap-report.md](assets/test-gap-report.md). Cite the production path and nearest existing tests. Separate confirmed gaps from questions about intended behavior. Include an execution order that delivers the most risk reduction first.

Do not create tests unless the user explicitly requests implementation.
