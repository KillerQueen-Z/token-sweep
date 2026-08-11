# Architecture debt signals

## Strong signals

- A policy or invariant is implemented differently in multiple owners.
- A local change routinely requires coordinated edits across unrelated modules or deployables.
- Dependency cycles force partial initialization, global state, or test-order dependence.
- Data ownership is unclear, causing direct cross-component writes or competing schemas.
- Failure, retry, or transaction boundaries do not align with side effects.
- Public contracts leak storage, vendor, or framework details that block change.
- Tests require broad environment assembly because useful seams are missing.

## Weak signals that need more evidence

- Large files, old libraries, a monolith, few interfaces, or nonstandard naming.
- Multiple languages or databases.
- Duplicate-looking code that encodes different policies.
- High abstraction or low abstraction without demonstrated change cost.

## Useful measures

- Change amplification, cycle count, fan-in/fan-out, ownership overlap, build/test blast radius, incident recurrence, deploy coupling, and migration reversibility.
