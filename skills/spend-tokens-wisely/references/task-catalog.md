# Task catalog

Choose lanes by expected value and evidence availability, not by their ability to consume context.

| Lane | Minimum useful time | Good scope | Durable output |
| --- | ---: | --- | --- |
| Recent-diff review | 10 min | Current diff or last commit | Verified review findings |
| Docs drift | 15 min | README, examples, config, API docs | Exact stale claims and replacements |
| Dependency health | 20 min | One ecosystem or deployable | Ranked upgrade/removal plan |
| Test gaps | 25 min | One critical journey | Executable test specifications |
| Deep repository review | 40 min | Small repo or critical subsystem | Cross-cutting defect backlog |
| Performance risks | 40 min | One request/job/data path | Measurement plan and bottleneck hypotheses |
| Architecture debt | 45 min | One subsystem or small repo | Boundary map and staged migration options |

## Portfolio heuristics

- Under 20 minutes: choose one narrow lane with existing evidence.
- 20–45 minutes: choose one specialist lane; add a short diff review only if it does not duplicate scope.
- 45–90 minutes: run a general review and one specialist lane.
- Above 90 minutes: run up to three independent lanes, then reserve at least 15% of the time for deduplication and synthesis.
- Large repositories: narrow to one critical subsystem unless the timebox is at least 90 minutes.

## Stop conditions

Stop when one of these is true:

- the timebox is exhausted;
- all high-confidence paths in scope have been checked;
- further work requires unavailable production data, credentials, or user intent;
- the next action would mutate code or external state without authorization;
- new observations duplicate an existing root cause.
