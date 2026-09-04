# Retrofit policy

Retrofitting must preserve the target project's existing authority and history.

## Inspect first

Read the target's governing instructions and inventory root-level Markdown, existing
status or work logs, coordination folders, `.obsidian`, `.git`, and linked external
systems. Select one existing project home in this order: an explicit path, `README.md`,
a root note matching the directory name, then a root note with `type: project`.

## Managed sections

The setup script owns only content between its explicit markers in `AGENTS.md` and
`CLAUDE.md`. On repeat runs it replaces that section in place. It appends the section to
an existing file when no marker exists and never rewrites the surrounding content.

Generated `Workspace.base` and `project_tracker.py` include generator signatures. A
changed generated file or managed instruction section is treated as drift. Review the
diff, then use `--upgrade-managed` only when replacement is authorized. Preserve an
unsigned conflicting file and stop rather than treating it as generated content.

Audit runs the trusted tracker bundled with the skill against the target root. It does
not execute the target project's tracker. It also reports drift in the installed tracker.

## Legacy material

Do not automatically import, rewrite, split, archive, or delete old logs, memory notes,
decision notes, task systems, or historical status documents. Link them as legacy
sources only after their authority and mapping are clear. A plan, checklist, or old log
is not current state without reconciliation.

When the user authorizes reconciliation, use `project_tracker.py plan` to record
source-linked follow-ups without taking claims on other contributors' targets.
`--owner` identifies the recording human; `--suggested-owner` is advisory only.
Preserve original status and date in `--source-summary`, with `--source-evidence`.
The real owner later uses `start` after reviewing that evidence and dependencies.
Do not import historical percentages as passed criteria for a new follow-up.

## Idempotence

A second setup run with the same inputs must not duplicate managed sections, create a
second project home, or create a second workspace-setup decision. Audit and validation
must distinguish a valid installed workspace from a partially configured one.

## Collaboration mode

- `shared-folder`: use target hashes and reconciliation records for non-Git files.
- `git`: store branch and commit evidence; Git controls exact diffs.
- `hybrid`: use both and record which system controls each target.

Automatic mode selects Git only when the target itself contains `.git`; otherwise it
selects shared-folder. Select hybrid explicitly when documentation and implementation
have different homes.
