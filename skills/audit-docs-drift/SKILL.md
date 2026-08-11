---
name: audit-docs-drift
description: Compare repository documentation, examples, configuration references, API descriptions, and operational instructions with the current implementation to find actionable drift. Use for stale README or docs audits, docs-versus-code checks, broken setup instructions, outdated examples, release-readiness documentation review, or a low-risk productive quota sweep.
---

# Audit Docs Drift

Treat documentation as an executable contract. Report exact mismatches and safe replacements.

## Define authoritative sources

1. Read repository instructions and identify generated versus hand-written docs.
2. Inventory user-visible claims: install commands, config keys, defaults, endpoints, schemas, examples, supported versions, architecture statements, and operational procedures.
3. Map each claim to implementation, tests, schemas, manifests, CLI help, or deployment configuration.

Read [references/drift-checklist.md](references/drift-checklist.md) for claim categories.

## Verify claims

Prefer static evidence first. Run documented commands only when they are safe, local, and do not require secrets or external mutation. Never deploy, publish, migrate, or write production data to test documentation.

Classify each mismatch:

- `incorrect`: following the docs produces wrong behavior or failure;
- `stale`: an old name, path, version, output, or workflow remains;
- `missing`: a necessary public contract or operational step is undocumented;
- `ambiguous`: wording supports materially different interpretations;
- `cosmetic`: no behavioral consequence; omit unless requested.

Check for generated-source ownership before recommending edits. Fix the source template or schema, not generated output.

## Report

Use [assets/docs-drift-report.md](assets/docs-drift-report.md). Quote only the shortest identifying fragment. Cite the documentation and authoritative code locations, state user impact, and provide replacement wording or a concrete doc change.

Do not edit docs unless the user explicitly requests fixes.
