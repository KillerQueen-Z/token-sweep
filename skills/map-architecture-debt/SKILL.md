---
name: map-architecture-debt
description: Build an evidence-backed map of architectural debt, coupling, unclear boundaries, ownership friction, change amplification, and pragmatic migration options. Use for architecture review, technical-debt mapping, modularity analysis, service-boundary evaluation, modernization planning, or a high-reasoning repository sweep that should not rewrite the system.
---

# Map Architecture Debt

Distinguish costly structural debt from unfamiliar or unfashionable design. Optimize recommendations for incremental delivery.

## Model the current system

1. Read repository instructions, manifests, entrypoints, deployment config, schemas, and representative tests.
2. Map components, responsibilities, dependency direction, runtime calls, data ownership, state stores, and external boundaries.
3. Trace two or three representative change journeys from request to affected modules, tests, configuration, and deployment.

Read [references/debt-signals.md](references/debt-signals.md) before naming debt.

## Establish evidence of cost

Look for repeated cross-boundary edits, cycles, duplicated policy, ambiguous ownership, leaking abstractions, shared mutable state, version-lock coupling, fragile initialization, and inconsistent failure semantics. Use history or issue evidence when available, but do not require it when code provides decisive evidence.

Do not call something debt solely because it is a monolith, uses an older pattern, has large files, or differs from personal preference. State the maintenance or reliability cost and who pays it.

## Develop options

For each material debt item, provide:

- keep-as-is conditions;
- a smallest containment step;
- a staged structural option;
- migration hazards and rollback points;
- a measurable success signal.

Prefer seams, ownership clarification, contract tests, and dependency inversion over broad rewrites. Avoid speculative microservice extraction.

## Report

Use [assets/architecture-debt-report.md](assets/architecture-debt-report.md). Include a compact component/data-flow diagram when it materially improves understanding. Rank by recurring cost, risk, confidence, and migration effort.

Do not refactor code unless the user explicitly requests implementation.
