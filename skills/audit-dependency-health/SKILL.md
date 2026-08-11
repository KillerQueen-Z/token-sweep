---
name: audit-dependency-health
description: Audit repository dependencies for known vulnerabilities, staleness, maintenance risk, unnecessary or duplicate packages, license concerns, lockfile integrity, and upgrade blast radius. Use for dependency health checks, supply-chain triage, upgrade planning, package cleanup, end-of-cycle maintenance sweeps, or high-value quota use without changing dependencies by default.
---

# Audit Dependency Health

Produce a prioritized plan grounded in manifests, lockfiles, actual usage, and current authoritative advisories.

## Inventory

1. Read repository instructions and identify every package ecosystem, manifest, lockfile, workspace, container base image, vendored module, and runtime/build boundary.
2. Separate direct, transitive, development, optional, bundled, and runtime dependencies.
3. Search actual imports, commands, plugins, generated code, and build configuration before calling a dependency unused.

Read [references/dependency-checklist.md](references/dependency-checklist.md).

## Gather evidence

Use local package-manager inspection first. Current versions, advisories, release status, and licenses are time-sensitive; verify them with authoritative registries, vendor advisories, or repository releases when internet access is available. Clearly date external evidence.

Do not install packages or rewrite lockfiles merely to inspect them. Networked audit commands may contact registries and write caches; use them only when allowed. Never expose registry credentials.

## Classify and rank

Classify each item as vulnerable, unsupported, stale, duplicated, unused, over-privileged, license-sensitive, integrity concern, or upgrade blocker. Confirm reachability and exposure before escalating a vulnerability. Distinguish an available update from a required update.

Rank by exploitability or operational impact, confidence, upgrade urgency, and blast radius. Include compatible target versions, breaking changes, test gates, and rollback strategy when known.

## Report

Use [assets/dependency-health-report.md](assets/dependency-health-report.md). Include exact manifests and resolved versions, source/date for time-sensitive facts, and a staged action plan.

Do not modify manifests, lockfiles, containers, or remote registries unless the user explicitly requests implementation.
