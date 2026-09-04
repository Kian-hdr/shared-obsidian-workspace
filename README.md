# Shared Obsidian Workspace

A copyable `AGENTS.md` and a complete agent skill for organizing a Markdown or
Obsidian workspace shared by multiple people and AI agents.

The instructions cover navigation, ownership, evidence, synchronization checkpoints,
and handoffs. The optional Python tracker adds work records, target claims, dependency
tracking, and an Obsidian Bases dashboard.

**This is a coordination toolkit, not a sync service or an Obsidian plugin.** Use your
existing sharing provider. File claims are advisory; they cannot prevent simultaneous
offline edits on different computers.

## Let your agent set it up

**[Copy the setup prompt into your own chat](SETUP-PROMPT.md).** No placeholders
need editing. The prompt guides a local agent through finding your vault, installing
the toolkit, preserving existing instructions, setting up or joining the correct
project, and checking the result. It installs and configures missing Obsidian, Python,
and the existing sharing client's dependencies. If you choose Homebrew, it installs
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
privacy, approval, and project-specific requirements. Remove the sentence about this
template repository when adapting it to your own vault.

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

Give your local agent this prompt, replacing the project path:

```text
Use the setup-shared-project-workspace skill to configure my computer and the existing
project at <absolute project path> for collaboration by multiple people and AI agents.
I authorize required local installs and configuration, including missing Obsidian,
Python, the existing sharing client, prerequisites, and minimal PATH changes. If I
choose Homebrew, install and configure it when missing. Follow references/local-setup.md.
Continue without repeated permission requests for authorized steps; honor my actual
approval settings and hand off only required authentication or OS interactions.
Read its governing instructions and current coordination state first. Audit it,
preview the retrofit, preserve existing files and rules, and apply compatible local
setup changes. Reuse the existing sharing provider. Ask for identity information
only if it cannot be determined. Validate the result and give me the skill's
teammate onboarding prompt. If the approved shared-folder URL is missing, finish
local setup and ask me for that URL before calling the onboarding prompt ready.
Do not change sharing permissions, send invitations, or resume existing project work.
```

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
2. Teammates obtain authorized access through the existing sharing provider.
3. Each agent reads `AGENTS.md`, reviews current records, and uses a unique actor ID.
4. Contributors claim separate targets and check ownership before each mutation.
5. Material changes include evidence, dependency impact, and a next action.
6. The next contributor accepts a handoff and refreshes their context before editing.

Teammates do **not** need this skill installed once the project contains the generated
tracker and instructions. They need access to those project files and a compatible
Python runtime. Downloading this public repository does not grant access to anyone's
private vault, and downloading a copy of a vault does not create a synchronized workspace.

See [the collaboration guide](docs/COLLABORATION.md) for everyday use and conflict handling.

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
