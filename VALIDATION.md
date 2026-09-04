# Publication validation

Checked on 2026-09-04 before initial publication.

## Passed locally

- All 31 bundled regression tests on macOS with Python 3.9.6 and PyYAML 6.0.3.
- Documentation smoke test in a disposable Obsidian-shaped project: unconfigured
  audit, no-write preview, retrofit, workspace validation, and repeat-run idempotence.
- Preservation of the copyable `AGENTS.md`, existing home note, and research note
  during that retrofit.
- Relative Markdown link checks and YAML syntax checks across the distribution.
- Byte-for-byte comparison of runtime scripts and dashboard assets with the installed skill.
- Targeted distribution scan for private local paths, project identifiers, and common
  credential patterns. This is a publication check, not a comprehensive security audit.

## Scope

The packaged runtime scripts and dashboard are copied from the existing
`setup-shared-project-workspace` skill. Personal names in test fixtures and the record
schema example were replaced with generic identities. The installed source skill
was not modified. The repository adds general vault instructions, distribution
documentation, an MIT license, development requirements, and CI configuration.

## Limits

Local tests do not establish cross-device locking, provider upload, another person's
access, or real-time synchronization. Obsidian dashboard rendering and Windows
PowerShell instructions were not manually exercised during this publication pass.

The GitHub Actions workflow runs the bundled Python tests on Linux, macOS, and Windows
with Python 3.9 and 3.13. Consult the actual workflow run for its current result;
the existence of the workflow file is not evidence that those jobs passed.

## Local setup instruction update, 2026-09-04

The setup prompt, teammate prompt, skill entrypoint, and supporting documentation
now authorize required local dependencies and configuration, including missing
Homebrew when chosen, Obsidian installation/launch, and opening the correct vault.
An independent scenario review covered a fresh machine, installation preferences,
missing PATH entries, Markdown-only use, unsupported platforms, and enforced
approval/authentication gates. The skill validator and documentation link/format
checks passed. Runtime scripts and dashboard assets were unchanged.

The revised skill guidance was also synchronized to the maintainer's installed
skill after preserving its previous instruction files. No fresh-machine installer,
administrator/authentication flow, or recipient app launch was executed for this update.
