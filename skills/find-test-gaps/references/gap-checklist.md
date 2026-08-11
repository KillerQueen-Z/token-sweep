# Test-gap checklist

## Boundaries

- Empty, zero, maximum, malformed, duplicate, expired, and mixed-version inputs.
- Authentication, authorization, tenant, filesystem, network, database, and queue boundaries.

## State and time

- Retry, replay, idempotency, cancellation, timeout, clock skew, and expiration.
- Partial success, rollback, crash recovery, and cleanup.
- Concurrent updates, ordering, stale reads, and double submission.

## Contracts

- Serialization, migrations, backward compatibility, feature flags, configuration defaults, and public error shapes.
- External provider failure modes and unexpected but valid responses.

## Test quality

- Assert observable behavior, not internal call choreography unless choreography is the contract.
- Prefer deterministic fakes at external boundaries.
- Ensure the test fails for the intended defect and is stable under harmless refactors.
