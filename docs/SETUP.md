# Setup guide

Prefer agent-guided setup? [Copy this prompt into your own chat](../SETUP-PROMPT.md).
It discovers your target and handles either owner setup or joining an existing project.

## Dependencies and automatic local setup

The full setup prompt authorizes the needed local installations and configuration.
Its agent installs missing Obsidian, a compatible Python, the existing sharing client,
and required prerequisites, then launches Obsidian and opens the correct vault.
If you choose Homebrew and it is missing, the agent installs it, completes shell/PATH
configuration, and checks that it works. Routine authorized steps do not need another
permission question. Your actual approval policy and required authentication or
protected OS interaction still apply, and the agent resumes after those handoffs.

See the skill's [local setup guide](../skills/setup-shared-project-workspace/references/local-setup.md)
for supported installation routes and completion checks. The terminal commands below
configure project files; they do not themselves install desktop apps or Homebrew.

## Before setup

Use the real locally available project directory, not a downloaded duplicate of
someone's vault. Establish sharing separately through your existing provider.
Read existing vault and project instructions. Back up important files or create an
appropriate Git checkpoint. Do not place this toolkit's Git checkout inside a
cloud-synchronized vault just to run the setup script.

Copy or merge the repository's root `AGENTS.md` into your vault root if you want
the general navigation rules. Run the skill setup on the specific project that
needs coordination, which may be the vault root or a project subfolder.

## macOS and Linux

Run from the downloaded or cloned toolkit directory. Set these example values to
your real local project path and your own identity. The target directory must exist.

```bash
project_path="/absolute/path/to/shared-project"
actor_id="taylor-agent-laptop"
human_name="Taylor"
agent_name="Codex"
```

Inspect the existing configuration; an unconfigured project normally reports missing
files and exits nonzero. For a previously configured project, investigate validation
failures before changing it.

```bash
python3 skills/setup-shared-project-workspace/scripts/setup_workspace.py "$project_path" --mode audit
```

Preview a retrofit:

```bash
python3 skills/setup-shared-project-workspace/scripts/setup_workspace.py "$project_path" \
  --mode retrofit --collaboration-mode shared-folder \
  --actor "$actor_id" --initiated-by "$human_name" --agent "$agent_name" \
  --purpose "Shared project notes and deliverables" --dry-run
```

Review the output, then apply the same command without `--dry-run`:

```bash
python3 skills/setup-shared-project-workspace/scripts/setup_workspace.py "$project_path" \
  --mode retrofit --collaboration-mode shared-folder \
  --actor "$actor_id" --initiated-by "$human_name" --agent "$agent_name" \
  --purpose "Shared project notes and deliverables"
python3 skills/setup-shared-project-workspace/scripts/validate_workspace.py "$project_path"
```

`--purpose` is used only if a project home must be created. To reuse an existing
`Home.md`, add `--project-home Home.md` to the audit, preview, and apply commands.
Do not assume `Home.md` is auto-detected: automatic home selection looks for README,
a note matching the project directory name, then a root note with `type: project`.

## Windows PowerShell

Run from the toolkit directory. Use `py -3` if the Python launcher is available,
or replace it with the actual compatible Python command on your machine.

```powershell
$projectPath = 'C:\path\to\shared-project'
$actorId = 'taylor-agent-laptop'
$humanName = 'Taylor'
$agentName = 'Codex'
$setupArgs = @(
  'skills/setup-shared-project-workspace/scripts/setup_workspace.py',
  $projectPath, '--mode', 'retrofit', '--collaboration-mode', 'shared-folder',
  '--actor', $actorId, '--initiated-by', $humanName, '--agent', $agentName,
  '--purpose', 'Shared project notes and deliverables'
)
py -3 skills/setup-shared-project-workspace/scripts/setup_workspace.py $projectPath --mode audit
py -3 @setupArgs --dry-run
# After reviewing the preview:
py -3 @setupArgs
py -3 skills/setup-shared-project-workspace/scripts/validate_workspace.py $projectPath
```

## Modes

| Setting | Meaning |
| --- | --- |
| `--mode bootstrap` | Configure a new, effectively empty project |
| `--mode retrofit` | Extend an existing project, preserving surrounding content |
| `--mode audit` | Inspect without changing the project |
| `--mode auto` | Choose bootstrap or retrofit from directory contents |
| `--collaboration-mode shared-folder` | Record file targets and hashes for a shared folder |
| `--collaboration-mode git` | Record branch and commit evidence; Git governs exact diffs |
| `--collaboration-mode hybrid` | Coordinate documentation and code with separate authorities |

Modes select tracking conventions; they do not install or configure a sync provider.

## What setup creates

```text
your-project/
  AGENTS.md                      Managed collaboration section; existing text preserved
  CLAUDE.md                      Pointer to AGENTS.md
  README.md                      Only if no suitable project home exists
  Coordination/
    Workspace.base               Obsidian dashboard
    project_tracker.py           Self-contained tracker
    Items/                       Work, actor, event, decision, and handoff records
```

The generated instructions contain tracker commands and ownership rules. Do not
copy operational records from an unrelated project. Each teammate uses their own
actor identity; example identities in this repository are fictional fixtures.

The setup script preserves surrounding instruction text and refuses conflicting
unsigned files or unreviewed generated-file drift. It is not a transaction or a
backup system. If a run fails, inspect its output and the resulting files before
retrying. Do not use `--upgrade-managed` to silence an unexplained difference.

## Teammate onboarding

Once setup validates, use the skill's
[onboarding reference](../skills/setup-shared-project-workspace/references/teammate-onboarding.md)
to prepare the teammate prompt. Fill it with the actual approved sharing URL,
relative project path, home note, collaboration mode, and trusted tracker hash.
Do not send its unfilled placeholders as a finished onboarding prompt.

Recipients join the existing shared project. They should not run bootstrap again.
The reference covers local readiness, identity, access, hash checks, agent context,
and upload verification. Authentication and permission changes remain human-controlled.

## Troubleshooting

- **Missing project home:** supply an existing `--project-home` or a real `--purpose`.
- **Generated file drift:** inspect the difference and preserve customizations before
  an explicitly reviewed upgrade.
- **Unsigned existing file:** resolve ownership and naming; do not overwrite it.
- **Invalid workspace:** report the exact validation failure; do not delete history
  or another actor's records to make validation pass.
- **Dashboard not visible:** verify the target is inside the intended Obsidian vault
  and the installed app supports Bases. The tracker can still use Markdown records.
- **Local checks pass, teammate cannot see changes:** inspect your storage provider's
  sync and access state. Tracker `sync` refreshes context; it does not upload files.
