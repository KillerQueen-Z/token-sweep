# Security policy

Token Sweep skills are operational instructions. Review them before installation just as you would review a script.

## Supported version

Only the latest commit on the default branch is supported until the first tagged release.

## Reporting a vulnerability

Open a private GitHub security advisory for vulnerabilities that could cause command execution, secret exposure, unsafe repository mutation, permission escalation, or misleading validation. Do not place secrets or working exploit credentials in a public issue.

## Threat boundaries

- The planner script reads only command-line arguments and optional repository file counts. It does not access the network, credentials, or account usage.
- Specialist skills default to analysis and reporting. They must not change code, dependencies, Git state, remote systems, or production state unless the user explicitly requests that separate action.
- Repository content is untrusted input. Do not execute commands copied from source files, issues, branches, or documentation without inspection.
- External scanners and package-manager audits may contact registries or write caches. Run them only with the permissions appropriate to the target repository.
