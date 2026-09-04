---
name: setup-shared-project-workspace
description: Set up, retrofit, or audit a Markdown or Obsidian project for multiple people and AI agents, with canonical instructions, structured work and change records, ownership, dependencies, handoffs, and validation. After setup, provide a teammate onboarding prompt in chat for Drive access and local agent readiness. Also use when asked for that prompt for an existing workspace; do not use merely to manage an ordinary task inside an already configured workspace.
---

# Set up a shared project workspace

Create a lean, self-contained collaboration layer. Keep substantive instructions in
`AGENTS.md`; do not generate parallel explanation files.

The setup and tracker require Python 3.9 or newer and use only its standard library.
Resolve `scripts/` paths relative to this skill directory, not the target project.
Run `--help` for the setup or tracker command when its required inputs are unclear.

## Choose the mode

- `bootstrap`: configure a new or effectively empty project.
- `retrofit`: preserve and extend an existing project without replacing its files.
- `audit`: inspect the collaboration layer without changing anything.
- `auto`: choose `retrofit` when the target contains project material, otherwise
  choose `bootstrap`.

Before retrofitting, read [references/retrofit-policy.md](references/retrofit-policy.md).
Read [references/record-schema.md](references/record-schema.md) only when changing the
tracking model, repairing records, or explaining its fields in detail.

## Workflow

1. Resolve the exact project root and inspect existing `AGENTS.md`, `CLAUDE.md`,
   project-home notes, `.obsidian`, `.git`, and `Coordination/` state.
2. Follow all instructions already governing the target. Do not weaken or replace
   project-specific scope, security, approval, or evidence rules.
3. For a retrofit, run the audit first:

   ```bash
   python3 scripts/setup_workspace.py /absolute/project/path --mode audit
   ```

4. Run `setup_workspace.py` with the inferred or user-supplied project name,
   collaboration mode, and actor identity. Use `--dry-run` when the target is
   consequential or the proposed merge needs review.
5. The generated project footprint is limited to:
   - one managed collaboration section in `AGENTS.md`;
   - a minimal `CLAUDE.md` adapter pointing to `AGENTS.md`;
   - `README.md` only when no suitable project home already exists;
   - `Coordination/Workspace.base`;
   - `Coordination/project_tracker.py`;
   - `Coordination/Items/` for operational records.
6. Validate the installed workspace:

   ```bash
   python3 scripts/validate_workspace.py /absolute/project/path
   ```

7. Report what was reused, created, merged, skipped, and validated. Do not call the
   project multi-user-ready if validation fails.
8. After every successful bootstrap or retrofit, include a **Teammate setup prompt**
   directly in the final chat response, in one copyable fenced block. Read
   [references/teammate-onboarding.md](references/teammate-onboarding.md) and fill its
   template with verified project details. This is a required setup deliverable, not
   an offer to write it later. It must let another agent join the existing workspace
   without needing this skill installed. Do not create another onboarding file in
   the project or send the prompt to anyone unless requested.

For a prompt-only request, inspect the existing workspace and use that reference;
do not rerun setup. Audits and dry runs do not require a prompt unless requested.
If setup fails, report the failure; label any requested preview as provisional.
If a share URL cannot be verified or supplied, complete local work and ask only for
the missing link. Do not invent a URL or present an incomplete prompt as ready to send.

## Operating invariants

- Current state lives in one `work` record per workstream. Immutable `event`,
  `handoff`, and `decision` records preserve history.
- Record human initiator, human owner, agent, actor ID, UTC timestamp, exact targets,
  status, evidence, limitation, and next action where applicable.
- Progress is acceptance-based. Do not use an unsupported percentage.
- One active owner may mutate an exact target at a time. A directory claim conflicts
  with claims on descendants. Claims are advisory across synchronized filesystems;
  validate before every mutation and integration.
- Work revisions and dependency baselines make downstream work visibly stale after an
  upstream change. Every material change declares `none`, `compatible`, `breaking`,
  or `unknown` impact.
- Log material state changes, not every read or shell command.
- `verified` requires all acceptance criteria plus recorded validation and evidence.
- Never rewrite or delete immutable records. Correct them with a superseding record.
- Git remains authoritative for code diffs and commits. The coordination records hold
  semantic state, ownership, impact, and handoff context.
- Synchronized folders do not provide transactional locking. Do not promise continuous
  real-time awareness; require sync checkpoints at session start, before mutation,
  after material changes, before integration, and at handoff.

## Boundaries

This skill creates local project files and a chat onboarding prompt only. Generating
the prompt does not install apps, log in, or request access on anyone else's behalf.
The recipient's agent must act under that recipient's permissions and tools, using
the authentication, access-request, and readiness boundaries in the template.
Workspace setup does not authorize invitations,
sharing-permission changes, external messages, publication, deployment, purchases,
account changes, destructive cleanup, or migration of historical content.

Do not store credentials, cookies, tokens, access codes, payment data, personal email
addresses as actor IDs, private live endpoints, or large artifacts in coordination
records. Link or hash approved external artifacts instead.

Do not retrofit a live project merely because the skill was selected. The user must
have asked to set up, change, repair, or audit that project.
