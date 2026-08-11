# Dependency health checklist

- Known vulnerabilities, reachability, affected configuration, patched versions, and compensating controls.
- End-of-life runtimes, archived packages, stalled releases, ownership transfer, and suspicious maintainer changes.
- Direct dependencies with no verified imports or runtime/build use.
- Multiple libraries serving the same purpose or multiple incompatible versions with material cost.
- Lockfile/manifests mismatch, floating versions, unpinned actions/images, integrity hashes, and install scripts.
- License compatibility, notices, source-availability duties, and distribution model. Flag for legal review; do not provide legal conclusions.
- Native extensions, privileged hooks, broad transitive trees, and packages that process untrusted data.
- Upgrade sequencing, breaking APIs, schema/data migrations, and test coverage at dependency boundaries.
