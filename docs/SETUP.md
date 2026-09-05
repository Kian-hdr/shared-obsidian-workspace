# Setup guide

Prefer agent-guided setup? [Copy this prompt into your own chat](../SETUP-PROMPT.md).
It discovers your target and handles either owner setup or joining an existing project.

## Dependencies and automatic local setup

The full setup prompt authorizes the needed local installations and configuration.
Its agent installs missing Obsidian, a compatible Python, and only the client or
prerequisites required by your selected access method, then opens the correct vault.
If you choose Homebrew and it is missing, the agent installs it, completes shell/PATH
configuration, and checks that it works. Routine authorized steps do not need another
permission question. Your actual approval policy and required authentication or
protected OS interaction still apply, and the agent resumes after those handoffs.

See the skill's [local setup guide](../skills/setup-shared-project-workspace/references/local-setup.md)
for supported installation routes and completion checks. The terminal commands below
configure project files; they do not themselves install desktop apps or Homebrew.

## Before setup

Identify your own project/vault paths and actual workflow using the
[access guide](../skills/setup-shared-project-workspace/references/storage-access.md).
For local-only work, use your chosen directory without configuring remote access.
For shared work, use the real authorized folder/checkout, not an unrelated downloaded
duplicate. A software repository URL does not identify your cloud account or vault.
Read existing vault and project instructions. Back up important files or create an
appropriate Git checkpoint. Do not place this toolkit's Git checkout inside a
cloud-synchronized vault just to run the setup script.

Copy or merge the repository's root `AGENTS.md` into your vault root if you want
the general navigation rules. Run the skill setup on the specific project that
needs coordination, which may be the vault root or a project subfolder.

## macOS and Linux

Run from the downloaded or cloned toolkit directory. These prompts collect your
own local project path and identity. The target directory must exist.

```bash
printf 'Local project path: '
read -r project_path
printf 'Your unique actor ID (no email address): '
read -r actor_id
printf 'Your name: '
read -r human_name
printf 'Your agent name: '
read -r agent_name
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
  --mode retrofit --collaboration-mode auto \
  --actor "$actor_id" --initiated-by "$human_name" --agent "$agent_name" \
  --purpose "Shared project notes and deliverables" --dry-run
```

Review the output, then apply the same command without `--dry-run`:

```bash
python3 skills/setup-shared-project-workspace/scripts/setup_workspace.py "$project_path" \
  --mode retrofit --collaboration-mode auto \
  --actor "$actor_id" --initiated-by "$human_name" --agent "$agent_name" \
  --purpose "Shared project notes and deliverables"
python3 skills/setup-shared-project-workspace/scripts/validate_workspace.py "$project_path"
```

`--purpose` is used only if a project home must be created. To reuse an existing
home note, supply `--project-home` with its project-relative path. Automatic discovery
also recognizes `Home.md`. Keep the home inside the project so the same link works
for teammates with different local roots. An external private home is not a portable
project entrypoint; use an existing in-project index linking only approved sources.

## Windows PowerShell

Run from the toolkit directory. Use `py -3` if the Python launcher is available,
or replace it with the actual compatible Python command on your machine.

```powershell
$projectPath = Read-Host 'Local project path'
$actorId = Read-Host 'Your unique actor ID (no email address)'
$humanName = Read-Host 'Your name'
$agentName = Read-Host 'Your agent name'
$setupArgs = @(
  'skills/setup-shared-project-workspace/scripts/setup_workspace.py',
  $projectPath, '--mode', 'retrofit', '--collaboration-mode', 'auto',
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
`shared-folder` also handles a local-only directory: label its access method local-only
and do not claim it is synchronized. Use `git` for a project in a Git checkout and
`hybrid` only for an actual mix of authorities. The commands above use `auto`, which
detects an enclosing Git checkout and otherwise uses file-mode tracking. Override it
only to match an explicit workflow.

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
to prepare the teammate prompt. Fill it with the actual access method and appropriate
locator, relative project/vault paths, home note, tracker mode, and trusted tracker hash.
No locator or account is required for a local-only workspace. A Git project needs its
own remote/checkout details rather than a cloud-folder URL.
Do not send its unfilled placeholders as a finished onboarding prompt.

Recipients join the existing shared project. They should not run bootstrap again.
The reference covers local readiness, identity, access, hash checks, agent context,
and workflow-specific propagation checks. Authentication and permission changes
remain human-controlled. Each recipient discovers their own account and local paths.

## Updating an existing workspace

Download the current toolkit or refresh a clean checkout, then update the installed
skill if you use one. Existing downloaded copies, agent sessions, and project-local
trackers do not change automatically when this public repository changes.

Read the target instructions and audit with the current toolkit before any upgrade.
Back up the affected files and review generated-file differences. Use
`--upgrade-managed` only for the changes you intend; it is not a migration of work
records and should not overwrite unexplained customizations. Revalidate afterward.

Use project-relative file targets for new claims. If an older workspace contains
absolute or outside-project file targets, identify the affected records and owners
before editing. Do not silently rewrite immutable history, remove another actor's
claims, or assume an old machine path still points to the same file. Resolve or
replace active work through the project's authorized coordination process.
The toolkit has no automatic record migration. Adding a superseding record alone
does not clear diagnostics for absolute paths retained in historical records.

When copying a nested project, preserve the agreed vault-relative layout where
possible. If it becomes a standalone vault, review the dashboard's scope with the
current setup tool and apply the intended generated-file update. A recipient's
home-directory name may differ; the shared project's internal layout is what matters.

If an agent still requests an unexpected account or provider, inspect the exact
prompt, installed skill, target `AGENTS.md`, and toolkit version it read. A stale or
project-customized copy has its own instructions. Do not try logging in as the
toolkit author to resolve a portability problem.

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
