# Research notes

Snapshot: 2026-08-11.

## Sources

- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills) — skill anatomy, progressive disclosure, discovery, and optional scripts/references/assets.
- [OpenAI: Save workflows as skills](https://learn.chatgpt.com/use-cases/reusable-codex-skills) — repeatable workflow framing.
- [OpenAI: Code review](https://learn.chatgpt.com/docs/code-review) — review as a first-class Codex workflow.
- [Agent Skills specification](https://agentskills.io/) — portable `SKILL.md` format.
- [GitHub: About agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) — cross-agent compatibility and project/personal install locations.
- [skills CLI](https://www.skills.sh/docs/cli) — repository and single-skill installation syntax.
- [OpenAI plugins: Codex Security](https://github.com/openai/plugins/tree/main/plugins/codex-security/skills) — phased discovery, validation, and finding handoff.
- [Cloudflare security-audit-skill](https://github.com/cloudflare/security-audit-skill) — multi-phase audits with independently verified findings.
- [Trail of Bits skills](https://github.com/trailofbits/skills) — specialist security and program-analysis workflows.
- [JUNERDD skills](https://github.com/JUNERDD/skills) — bounded deep reviews, report lineage, regression review, and code-slimming workflows.

## Conclusions used in this repository

1. A reusable skill needs a clear trigger and a bounded workflow, not a long generic prompt.
2. Expensive analysis is most valuable when it produces evidence, reproducible commands, test cases, or a ranked backlog.
3. Report-only should be the default near a reset. Broad autonomous edits are difficult to review when time is short.
4. Multiple independent passes help only when their scopes differ. Repeating the same review wastes context and creates duplicate findings.
5. Security findings need validation and careful handling. Token Sweep routes dedicated security work to an installed security workflow instead of pretending a lightweight generic checklist is equivalent.
6. Skills are a supply-chain surface. Bundled scripts should be small, inspectable, dependency-free where practical, and never read secrets unnecessarily.
7. Exact account quota is product state, not something a portable skill should assume it can inspect. Timeboxes and user-supplied intensity are more reliable controls.

## Deliberate non-goals

- Infinite loops, filler generation, or prompts whose only metric is tokens consumed.
- Exact token metering or reset-time detection.
- Unattended production changes, deployments, merges, or credential rotation.
- Repackaging third-party skills without their licenses and provenance.
- Claiming a checklist review is a professional security audit.
