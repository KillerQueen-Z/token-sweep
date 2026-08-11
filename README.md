# Token Sweep

Turn expiring AI coding quota into durable repository value.

[简体中文](README.zh-CN.md)

Token Sweep is a collection of portable [Agent Skills](https://agentskills.io/) for the moment when your Codex or coding-agent allowance is about to reset. It does not burn tokens with loops or filler. It converts a timebox into evidence-backed code review, test-gap analysis, documentation checks, dependency triage, architecture mapping, or performance investigation.

> Token Sweep cannot read your account's exact remaining quota or guarantee a precise token spend. Give it a timebox and a target; it will stop when the useful work or timebox is exhausted.

## Why this exists

Unused quota has zero future value after a reset. A rushed autonomous rewrite can have negative value. Token Sweep sits between those extremes: spend the remaining reasoning budget on work that leaves a reviewable artifact and does not change production state by default.

The design rules are simple:

- useful output over token consumption;
- report-only by default;
- evidence and confidence for every finding;
- bounded scope and explicit stop conditions;
- code changes only when separately requested;
- never weaken tests or invent work to fill a timebox.

## Included skills

| Skill | Best use |
| --- | --- |
| `spend-tokens-wisely` | Choose and run a portfolio based on time, focus, and risk tolerance |
| `review-repository-deeply` | Find correctness, reliability, security, and maintainability defects |
| `find-test-gaps` | Find consequential behavior that lacks meaningful tests |
| `audit-docs-drift` | Compare docs, examples, config, and APIs with the implementation |
| `map-architecture-debt` | Map boundaries, coupling, ownership, and pragmatic migration paths |
| `audit-dependency-health` | Triage vulnerable, stale, unused, duplicated, or risky dependencies |
| `profile-performance-risks` | Find likely bottlenecks and design measurements before optimizing |

## Install

Install all skills:

```bash
npx skills add KillerQueen-Z/token-sweep
```

Or install a single skill:

```bash
npx skills add KillerQueen-Z/token-sweep --skill spend-tokens-wisely
```

You can also copy one or more directories from `skills/` into a supported personal or project skill directory. Restart the agent if it does not refresh its skill index automatically.

## Use

Invoke the orchestrator with a concrete timebox:

```text
Use $spend-tokens-wisely. I have 45 minutes before my quota resets.
Stay report-only and focus on correctness and tests in this repository.
```

Or invoke a specialist directly:

```text
Use $find-test-gaps on the payment and settlement paths. Return the five
highest-value tests with exact setup, action, and assertions. Do not edit code.
```

Generate a deterministic recommendation without an agent:

```bash
python3 skills/spend-tokens-wisely/scripts/plan_sweep.py \
  --minutes 60 --focus correctness,testing --repo-size medium
```

## Suggested timeboxes

| Time left | Typical sweep |
| --- | --- |
| 10–20 min | Recent-diff review or targeted docs drift |
| 20–45 min | Dependency health or test-gap hunt on one critical path |
| 45–90 min | Deep repository review plus one specialist pass |
| 90+ min | Multi-lane portfolio with deduplication and a final ranked backlog |

## Research basis

The structure follows the official [OpenAI skill authoring guidance](https://learn.chatgpt.com/docs/build-skills) and the open [Agent Skills specification](https://agentskills.io/). The workflows were informed by public patterns in [GitHub's agent-skill documentation](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills), [OpenAI's security skills](https://github.com/openai/plugins/tree/main/plugins/codex-security/skills), [Trail of Bits' security skills](https://github.com/trailofbits/skills), [Cloudflare's security-audit skill](https://github.com/cloudflare/security-audit-skill), and [JUNERDD's review-oriented skills](https://github.com/JUNERDD/skills). Token Sweep's instructions and scripts are original; those projects are references, not bundled dependencies.

Read [research/SOURCES.md](research/SOURCES.md) for the design conclusions and boundaries derived from that survey.

## Safety

Treat every third-party skill as executable operational guidance. Review `SKILL.md`, scripts, network use, and requested permissions before installation. Token Sweep's bundled planner is dependency-free, read-only, and makes no network requests.

See [SECURITY.md](SECURITY.md) for reporting and threat boundaries.

## License

MIT
