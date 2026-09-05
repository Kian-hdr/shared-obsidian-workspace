# Publication validation

## Portability refactor 1.2.0, 2026-09-05

All **45 regression tests** passed locally on macOS with Python 3.9.6 and
PyYAML 6.0.3. The additional cases cover:

- Copying a workspace to a different local root and checking the recipient's files.
- Normalizing absolute in-project targets to relative paths and detecting overlapping
  absolute/relative claims, including a claim on the whole project.
- Rejecting external, home-relative, and parent-traversal targets without writes.
- Diagnosing legacy machine-specific work, event hashes, and project-home pointers
  without silently rewriting records.
- Reusing `Home.md`, requiring an in-project home, and using portable separators.
- Detecting an enclosing Git repository for nested projects.
- Detecting a changed vault layout and validating a reviewed dashboard update.
- Safely serializing dashboard folders containing Unicode, apostrophes, colons, and
  quotation marks. Characters invalid in Windows filenames use serialization tests.

The source and all four pre-refactor commits were inspected for personal account
addresses, private sharing links, and author-machine paths. None were found. The
actual portability defects were Drive-specific onboarding defaults and runtime
acceptance of machine-specific paths. The GitHub source URL and MIT copyright
attribution remain public project identifiers, not account or vault configuration.

The setup and teammate prompts now distinguish local-only, Git, shared-folder, and
hybrid access. Independent review checked that local-only needs no remote/account,
recipients use their own paths and identities, dependencies follow the selected
workflow, and authorized local installation still includes missing Obsidian and
Homebrew when chosen. Skill validation and documentation link, format, YAML, and
targeted private-reference checks passed.

Consult the [workflow runs](https://github.com/Kian-hdr/shared-obsidian-workspace/actions/workflows/test.yml)
for Linux, macOS, and Windows results on Python 3.9 and 3.13. A workflow definition
alone does not establish a passing run.

These tests do not prove fresh-machine installation, protected authentication,
Obsidian UI rendering, another person's access, or actual multi-device synchronization.
Existing installed skills and project-local trackers need a reviewed upgrade.
Legacy absolute-path records require explicit mapping and migration; the toolkit
does not automatically migrate them or clear their diagnostics by superseding them.

## Historical initial publication, 2026-09-04

### Passed locally

- All 31 bundled regression tests on macOS with Python 3.9.6 and PyYAML 6.0.3.
- Documentation smoke test in a disposable Obsidian-shaped project: unconfigured
  audit, no-write preview, retrofit, workspace validation, and repeat-run idempotence.
- Preservation of the copyable `AGENTS.md`, existing home note, and research note
  during that retrofit.
- Relative Markdown link checks and YAML syntax checks across the distribution.
- Byte-for-byte comparison of runtime scripts and dashboard assets with the installed skill.
- Targeted distribution scan for private local paths, project identifiers, and common
  credential patterns. This is a publication check, not a comprehensive security audit.

### Scope at initial publication

The packaged runtime scripts and dashboard are copied from the existing
`setup-shared-project-workspace` skill. Personal names in test fixtures and the record
schema example were replaced with generic identities. The installed source skill
was not modified. The repository adds general vault instructions, distribution
documentation, an MIT license, development requirements, and CI configuration.

### Limits at initial publication

Local tests do not establish cross-device locking, provider upload, another person's
access, or real-time synchronization. Obsidian dashboard rendering and Windows
PowerShell instructions were not manually exercised during this publication pass.

The GitHub Actions workflow runs the bundled Python tests on Linux, macOS, and Windows
with Python 3.9 and 3.13. Consult the actual workflow run for its current result;
the existence of the workflow file is not evidence that those jobs passed.

## Historical local setup instruction update, 2026-09-04

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
