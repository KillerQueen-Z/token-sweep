---
name: spend-tokens-wisely
description: Convert soon-to-reset or otherwise unused AI coding quota into a bounded portfolio of useful repository analysis. Use when the user says their tokens, quota, credits, allowance, or usage window will reset or expire; asks to use spare capacity productively; wants a last-call repository sweep; or asks which high-value audits to run within a time budget.
---

# Spend Tokens Wisely

Turn a user-supplied timebox into durable findings. Optimize for value, not raw token count.

## Establish the sweep contract

Infer these fields from the request and repository. Ask only when a missing value would materially change the work.

- `timebox`: default to 30 minutes when unspecified.
- `focus`: correctness, testing, docs, architecture, dependencies, performance, or balanced.
- `scope`: recent diff, named subsystem, or whole repository.
- `risk`: default to `report-only`; use `safe-fixes` only when explicitly requested.
- `output`: default to a Markdown report in the response. Write a file only when requested or when the repository already defines a report location.

Do not claim access to account quota or reset metadata. Do not promise exact token consumption.

## Build the portfolio

Run `scripts/plan_sweep.py` when Python is available, or use [references/task-catalog.md](references/task-catalog.md) directly. Prefer the smallest set of non-overlapping lanes that fits the timebox.

Use these skills when installed:

- `$review-repository-deeply` for correctness and cross-cutting risk.
- `$find-test-gaps` for missing behavioral coverage.
- `$audit-docs-drift` for stale public contracts and examples.
- `$map-architecture-debt` for coupling and migration opportunities.
- `$audit-dependency-health` for supply-chain and maintenance health.
- `$profile-performance-risks` for measurement-led performance work.

Route a dedicated security audit to an installed security-audit workflow. Do not substitute a shallow checklist for specialist security validation.

## Execute safely

1. Inspect repository instructions, Git status, language, build system, and test entrypoints.
2. Freeze the scope and record it in the report.
3. Gather evidence before making claims. Prefer reachable execution paths, test results, call sites, history, and documented contracts.
4. Keep lanes independent. Deduplicate findings by root cause and impacted path.
5. Rank by expected value: impact × likelihood × confidence ÷ remediation cost.
6. Stop a lane when marginal value falls below another available lane. Do not generate filler to occupy the timebox.
7. Preserve the worktree, index, branch, remote state, dependencies, and production systems unless the user separately authorizes changes.

If subagents are available, use them only when the user requested parallel agents or the active environment instructions explicitly allow delegation. Give each agent a distinct lane and the same frozen scope. Never use parallel copies of the same prompt merely to spend quota.

## Produce one synthesis

Use [assets/sweep-report.md](assets/sweep-report.md). Include:

- contract, scope, and validation performed;
- ranked findings with evidence and confidence;
- discarded hypotheses and coverage gaps;
- recommended next actions sized as small, medium, or large;
- exact commands or prompts needed to continue.

Separate verified findings from hypotheses. If nothing consequential is found, say so and list what was checked.

## Fix mode

Enter fix mode only when explicitly authorized. Implement the smallest confirmed changes, run proportionate tests, and report remaining risks. Do not deploy, merge, push, publish, rotate credentials, or modify external systems without separate authorization.
