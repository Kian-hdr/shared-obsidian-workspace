# Shared Obsidian Workspace

A copyable `AGENTS.md` and a complete agent skill for organizing a Markdown or
Obsidian workspace shared by multiple people and AI agents.

The instructions cover navigation, ownership, evidence, synchronization checkpoints,
and handoffs. The optional Python tracker adds work records, target claims, dependency
tracking, and an Obsidian Bases dashboard.

Use your own folder, repository, storage provider, and account. Local-only work needs
no online account. The public GitHub address below is the software source; it does
not connect you to the maintainer's vault or Google Drive.

This is a coordination toolkit, not a sync service or an Obsidian plugin. File claims
are advisory; they cannot prevent simultaneous offline edits on different computers.

## Let your agent set it up

**[Copy the setup prompt into your own chat](SETUP-PROMPT.md).** No placeholders
need editing. The prompt guides a local agent through finding your vault, installing
the toolkit, preserving existing instructions, setting up or joining the correct
project, and checking the result. It directs the agent to install missing Obsidian,
Python, and only the dependencies of your selected access method. If you choose Homebrew, it installs
and configures Homebrew too. It continues under your setup authorization, respecting
your agent's approval settings and any required authentication or OS interaction.

## Get it

- [Download the repository ZIP](https://github.com/Kian-hdr/shared-obsidian-workspace/archive/refs/heads/main.zip).
- [Open the copyable AGENTS.md](AGENTS.md).
- [Open the complete skill folder](skills/setup-shared-project-workspace).

Or clone it outside your synchronized vault:

```bash
git clone https://github.com/Kian-hdr/shared-obsidian-workspace.git
cd shared-obsidian-workspace
```

## Choose how much you need

| Option | What to copy | Result |
| --- | --- | --- |
| Instructions only | Root `AGENTS.md` | Navigation and shared-work rules; no tracker installed |
| Full agent skill | Entire `skills/setup-shared-project-workspace/` folder | Agent-guided bootstrap, retrofit, audit, and teammate onboarding |
| Direct setup | Run the bundled Python setup script | Same workspace files, without requiring a skill-aware agent |

### Instructions only

Copy [AGENTS.md](AGENTS.md) into your vault root. If that file already exists, merge
the relevant sections rather than replacing your existing rules. Keep any stricter
privacy, approval, and project-specific requirements. The instructions discover the
recipient's environment rather than assuming the source author's account or paths.

Tell your agent to read the file explicitly. Automatic discovery differs by agent.
The file alone does not install the tracker or configure sharing.

### Full skill

Copy the **whole** `skills/setup-shared-project-workspace` folder, preserving its
structure. `SKILL.md` references bundled scripts, assets, and reference documents.

For an existing Codex setup using `~/.codex/skills/`, place the folder at:

```text
~/.codex/skills/setup-shared-project-workspace/
```

Keep a backup and review differences if a skill with that name is already installed.
Start a new agent session if needed, and confirm the skill is discoverable. Other
agents can read its `SKILL.md` directly and use the scripts without automatic discovery.

Then use the same [setup prompt](SETUP-PROMPT.md). It is the single starting prompt
for both downloaded toolkits and installed skills, and discovers your actual project.

### Direct setup

See [the setup guide](docs/SETUP.md) for copyable terminal commands, Windows guidance,
existing-vault preservation, generated files, and validation.

Setup and the tracker require **Python 3.9+** and only its standard library.
Obsidian is installed by the full setup prompt for Obsidian workflows; an explicitly
Markdown-only workflow can omit it. The notes are ordinary Markdown. Viewing `Workspace.base`
requires an Obsidian installation that supports Bases. Python tests additionally
require PyYAML, which is a development dependency only.

## How teammates work together

1. The owner configures the actual shared project once.
2. Teammates obtain authorized access through that project's actual access method.
3. Each agent reads `AGENTS.md`, reviews current records, and uses a unique actor ID.
4. Contributors claim separate targets and check ownership before each mutation.
5. Material changes include evidence, dependency impact, and a next action.
6. The next contributor accepts a handoff and refreshes their context before editing.

Teammates do **not** need this skill installed once the project contains the generated
tracker and instructions. They need access to those project files and a compatible
Python runtime. Downloading this public repository does not grant access to anyone's
private vault, and downloading a copy of a vault does not create a synchronized workspace.

See [the collaboration guide](docs/COLLABORATION.md) for everyday use and conflict handling.

## Choose your own access method

| Your workflow | What setup needs |
| --- | --- |
| Local-only | Your chosen folder; no cloud account, client, link, or upload |
| Git | Your project's remote and checkout, using your own access |
| Shared folder | Your actual service/network share and its approved locator |
| Hybrid | A clear mapping of notes, code, and other targets to their authorities |

Google Drive is one optional provider, not a requirement. The
[access guide](skills/setup-shared-project-workspace/references/storage-access.md)
keeps provider-specific instructions separate from the generic setup. The toolkit
does not supply storage, subscriptions, accounts, or access to someone else's files.

Shared file targets and project-home references use project-relative paths so each
person can keep the project under a different local root. Keep the agreed vault
layout, or review and regenerate dashboard scope after moving a nested project.
See [updating an existing workspace](docs/SETUP.md#updating-an-existing-workspace)
before upgrading an older tracker or transferred copy.

## Repository contents

```text
AGENTS.md                         Copyable vault instructions
SETUP-PROMPT.md                   Paste into your own agent's chat to get started
docs/SETUP.md                     Owner setup and validation
docs/COLLABORATION.md             Teammate workflow and boundaries
skills/setup-shared-project-workspace/
  SKILL.md                       Agent workflow
  agents/openai.yaml             Skill display metadata
  assets/                        Tracker and Obsidian dashboard template
  scripts/                       Setup, validation, and regression tests
  references/                    Retrofit policy, record schema, onboarding prompt
LICENSE                          MIT license
```

## Validation and development

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python skills/setup-shared-project-workspace/scripts/test_workspace.py
```

On Windows, use `.venv\Scripts\python.exe` instead of `.venv/bin/python`.
The regression suite uses disposable temporary projects. It checks setup preservation,
ownership conflicts, stale dependencies, validation, and handoffs. It does not prove
cloud upload, another computer's receipt, or the Obsidian dashboard's visual behavior.

See [VALIDATION.md](VALIDATION.md) for the publication checks and their limits.

## License

[MIT](LICENSE). You may copy, adapt, and redistribute the toolkit under that license.
Keep its copyright and permission notice with copies or substantial portions.
