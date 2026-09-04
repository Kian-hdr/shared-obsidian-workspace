# Teammate onboarding prompt

Use after successful workspace setup, or when asked to generate an onboarding prompt
for an existing workspace. Return the completed prompt in chat; this reference stays
inside the skill and is not copied into every project.
Read [local-setup.md](local-setup.md) when preparing dependency instructions. Keep
the recipient's final prompt self-contained; do not require that reference on their
computer. Carry the authorized installation, configuration, and continuation rules
into the prompt rather than adding per-package approval questions.

## Prepare the prompt

- Inspect the project contract, home, collaboration mode, tracker, and actual sharing
  location. Use an existing, verified folder URL from the user, project records, or
  authorized read-only Drive/browser inspection. Never derive a Drive ID from a local
  pathname, create a public link, broaden access, or copy a whole private Vault into
  the prompt. A link is not proof the teammate has access.
- Include project name, exact shared folder URL, project path relative to that folder,
  project-home path, required file-editing access, and the Obsidian mode and vault path
  relative to the shared folder. For a project-root share, use `.`. If the approved
  share lacks required parent instructions or referenced files, report that gap; do
  not assume permission to share the parent Vault. Do not include the sender's local
  absolute paths, account email, personal actor ID, secrets, or unrelated project data.
  For an Obsidian workflow, default to installing/opening Obsidian. Mark it omitted
  only for an explicitly Markdown-only workflow or when the recipient declines it.
- Hash the actual project's `Coordination/project_tracker.py` with SHA-256 and include
  that digest as the expected tracker version. Confirm its provenance against the
  trusted installed skill, or review an intentional project customization before
  endorsing it. A digest identifies the shared bytes; it is not a security audit.
- Fill project-specific placeholders. Recipient identity, OS, agent, and local paths
  are discovered by the receiving agent; never prefill the sender's identity. If the
  owner-side folder link or path remains unknown, ask one focused question after
  finishing local setup. A provisional template must be clearly labelled, not called
  ready to send. Do not embed replacement tokens in executable commands.
- Preserve the existing collaboration provider. Use the Drive flow below for Drive
  workspaces. For Git-only projects, replace Drive installation/access/mount steps
  with verified repository access and a local checkout outside cloud-sync folders;
  do not introduce Drive. For hybrid work, include separately verified repository
  details only where needed and keep `.git` outside Drive. Do not invent remote URLs.
- Keep the prompt self-contained and actionable. Do not require Codex, this skill,
  private sender-side paths, or a particular browser plugin on the teammate's machine.
  Prefer the recipient's available local tools; name capability gaps honestly.

## Copyable template

Adapt the following to the verified project. Keep the execution, consent, and evidence
requirements. The recipient is the speaker of the prompt below.

```text
Set up this computer so I can collaborate with my agent in an existing shared project.
Carry out the setup with the tools you actually have; do not just give me a checklist.
Reuse working components and continue automatically after completed user handoffs.

Project: {{PROJECT_NAME}}
Google Drive folder: {{VERIFIED_FOLDER_URL}}
Project directory relative to that folder: {{PROJECT_RELATIVE_PATH}}
Project home relative to the project directory: {{PROJECT_HOME}}
Obsidian: {{OBSIDIAN_MODE_AND_VERIFIED_VAULT_RELATIVE_PATH}}
Collaboration mode: {{COLLABORATION_MODE}}
Expected SHA-256 of Coordination/project_tracker.py: {{TRACKER_SHA256}}
Required access: read the project and create/update its coordination and work files,
subject to the project's ownership and approval rules. Do not seek owner/admin access.

I authorize the required local installations and configuration for this project:
Google Drive for desktop, a compatible maintained Python, Obsidian for the Obsidian
workflow, their needed prerequisites, app launch, vault opening, and minimal PATH
changes. If I choose Homebrew, install and configure it when missing as part of this
authorization. Do not ask again for each package or routine setup step. Preserve my
accounts, files, agent settings, and unrelated sync configuration. Do not recreate
the project. Honor my actual approval settings, enforced tool/OS/admin policy, and
governing instructions. Pause only for missing required information, a real policy
gate, an action outside scope, or an interaction only I can perform; then resume
automatically. Never weaken security or approval settings to make setup unattended.

1. Inspect this computer and your capabilities.
Detect OS/version, whether Google Drive for desktop is installed and running, its
existing signed-in account state, available Python, and your access to local files,
terminal and browser/app controls. Do not mistake a browser login or Drive connector
for a mounted desktop workspace. If you only have cloud/chat tools, explain that
limitation and guide me to a local-capable agent or the exact manual step; do not
pretend to install software on my computer from a remote container.

2. Prepare the installation route and get Google Drive for desktop running.
Reuse my chosen installation route. If none is stated, use an existing suitable
package manager or official installer. Check for an existing Homebrew outside PATH
and reuse its correct architecture/prefix rather than creating a second installation.
If I choose Homebrew and it is absent, install
it using https://brew.sh/ and https://docs.brew.sh/Installation after checking current
OS/architecture support and inspecting its installer. Install required prerequisites,
including Apple Command Line Tools when needed. Complete the installer's shellenv
steps for my actual shell with backed-up, minimal, nonduplicated startup-file edits.
Verify brew --version and brew --prefix in the current environment and a fresh shell.
Use documented unattended options only when permitted and appropriate; hand off any
required administrator authentication and resume. Do not install WSL just to set up
native Windows apps or assume every Homebrew package supports every Homebrew platform.

Reuse an installed compatible Google Drive desktop copy; launch it if stopped.
If missing, verify current
OS support and download/install from Google's official instructions:
https://support.google.com/drive/answer/10838124
https://support.google.com/drive/answer/2375082
When Homebrew is the chosen route and the current cask supports this platform, use
brew install --cask google-drive. Otherwise use Google's supported official installer.
On Windows use a native supported installation route. Do not install Chrome
unnecessarily or substitute an unofficial Linux sync client.
If the OS is unsupported or company policy blocks installation, report the blocker
and the administrator action needed. Hand me installer/admin prompts that need me;
never disable security protections or accept new terms on my behalf.

3. Confirm the correct account and project access.
Open Drive's normal sign-in flow when needed. Let me choose/confirm my own account;
do not infer it from the sender's account or use their credentials. Hand off password,
passkey, MFA, CAPTCHA, consent and credential-entry steps to me through the official
interface. Never request passwords, codes, tokens or cookies in chat or store them.
Preserve other signed-in accounts. Confirm the browser and desktop client use the
intended account before opening the exact folder link above.
If access is denied, prepare Google's Request access flow. Immediately before sending,
show me the account, exact target and requested access, explain it notifies the owner,
and obtain my confirmation unless I already explicitly authorized that exact request.
Send at most one authorized request; do not email
separately, invite others or alter sharing permissions. Approval depends on the owner
or administrator. A sent request is pending, not access granted. Finish independent
local checks while waiting; avoid repeated requests or endless polling. If no request
button is available or organizational policy blocks access, report that exact state.
Resume when I report approval and verify actual access, including editing rights.

4. Locate the real synchronized project.
Find the folder through Drive for desktop in Finder/File Explorer and resolve its
actual absolute path on this computer. Distinguish a Shared drive from a folder shared
with me. If needed, explain and obtain my approval for a shortcut in My Drive to that
same shared folder; do not copy, move or upload the project. Preserve its hierarchy.
Do not enable Desktop/Documents/Photos backup, mirror an entire drive, or change other
accounts' settings. Download only the needed project files; mark this project offline
only if useful and storage permits. Check Drive's sync status and open actual file
contents; an online placeholder, browser link, downloaded ZIP or private duplicate is
not the shared working directory. Verify AGENTS.md, the project home,
Coordination/project_tracker.py, Coordination/Workspace.base and Coordination/Items/.
If required files are absent, stop and report the missing files; do not bootstrap a
second workspace or regenerate the owner's coordination layer.

5. Connect this agent and finish Obsidian setup.
Read the governing project instructions and project home before running shared code.
Verify the tracker hash against the digest above and inspect the script before first
execution. If the digest differs, ask the project owner for the updated trusted digest
or a reviewed update; do not execute it just because it has a generator signature.
Select or install a compatible Python interpreter (Python 3.9+ is the compatibility
floor; choose a maintained stable release for a new install). Use the selected
supported package manager or https://www.python.org/downloads/. Verify its version,
actual path, and availability to this agent after any needed PATH configuration. Use the
actual interpreter command, such as python3 or py -3, and quote paths correctly for
this OS. The tracker requires no extra Python packages. Verify --help before use.
Open/configure the existing local project folder in my agent using its supported
workspace mechanism. Confirm that this agent has read AGENTS.md and can explain its
ownership, sync, evidence and handoff rules. Do not assume every agent loads it
automatically. Use existing CLAUDE.md where relevant; otherwise explicitly load
AGENTS.md and follow the agent's documented project-instruction mechanism. Do not
overwrite global instructions, weaken sandboxing, or enable unrestricted access.
No installation of the sender's Codex skill is required. If a new local session is
needed, give it the exact project path and continuation instructions.
For the Obsidian workflow, install missing Obsidian and finish its setup under the
authorization above. Skip it only if I requested Markdown-only work or declined it.
Use brew install --cask obsidian when Homebrew is the chosen supported route, or use
https://obsidian.md/download and https://help.obsidian.md/install. Launch the app and
open the supplied existing vault root through Open folder as vault. Reuse existing
configuration, and verify that the correct vault and project home open. Do not create
a duplicate or nested vault, overwrite shared .obsidian settings, enable a second
sync service, or install community plugins. Open the existing Workspace.base and
verify it renders when UI tools are available. Enable the built-in Bases feature
only if needed and permitted by the project's configuration rules. Report any
required owner-approval gate. Label unavailable launch/UI checks unverified; an
installed package alone is not evidence the app or vault opened.

6. Verify collaboration readiness without taking over other work.
From the project root, run the trusted tracker with the selected Python interpreter:
  Coordination/project_tracker.py validate
  Coordination/project_tracker.py status
Read any errors before proceeding. Ask my name if unknown and choose an actor ID
unique to my human/agent/session, without using my email or the sender's actor ID.
Once validation passes and shared editing access is confirmed, run:
  Coordination/project_tracker.py sync --actor <my-actor-id> --human <my-name> --agent <my-agent>
Replace the angle-bracket values and prepend the selected interpreter; these are not
literal shell commands. This creates/updates only my actor record and sync cursor.
Inspect recent changes, blockers and dependencies. Do not claim an existing task,
modify another actor, clear errors by editing history, or resume paused project work.
Verify that my actor record is locally readable and Drive reports it synced. Where
browser/connector tools permit, read that same record from the exact shared folder on
Drive and compare its contents. Local success alone does not prove upload or another
computer's receipt. Do not create/delete unrelated probe files. Run validation again.
Report existing project-wide validation failures to the owner without repairing them
under this onboarding request.

7. Report the result and how to resume.
Give me the exact local project path, agent workspace, actor ID, installation status,
account/access status without exposing credentials, tracker checks, sync evidence and
Obsidian installation/launch/vault result and any Homebrew, prerequisite, or PATH
changes. Say Ready only when the requested dependencies and configuration are complete,
the required app/vault launch is verified (or Obsidian was explicitly omitted), the
agent has loaded the rules, the
tracker validates, shared write access works and upload of my actor record is verified.
Otherwise say Partially configured or Blocked, identify each unfinished check and the
smallest action needed, and provide a short continuation prompt so I can resume after
sign-in, owner approval or switching sessions without starting over. Distinguish a
local check, a verified cloud upload, and actual receipt on another teammate's device.
Do not claim continuous synchronization or distributed locking.
```

## Review before returning

Check the assembled prompt against a fresh Mac, fresh Windows computer, an already
configured teammate, wrong account, denied/pending access, missing local tools,
read-only folder, missing tracker, changed tracker digest, existing validation failure,
and unknown sharing link. Also check absent Homebrew with and without a stated
Homebrew preference, missing Obsidian, a Markdown-only request, PATH missing in a
fresh shell, a protected administrator prompt, and enforced ask-before-install policy.
It should reuse, stop at the specific gate, or resume as
appropriate without duplicate installs/workspaces or invented success. This desk
review does not prove live installation, login, cross-account access or multi-device
sync. Report actual verification scope separately from the copyable prompt.

## Source maintenance

Installation sources refreshed on 2026-09-04; the original access-flow review was
2026-08-31. Refresh OS support, installer links and UI instructions from primary
sources when onboarding; do not freeze transient version numbers here.

- [Google Drive desktop installation and sign-in](https://support.google.com/drive/answer/10838124)
- [Google Drive desktop OS support](https://support.google.com/drive/answer/2375082)
- [Google file access requests and notifications](https://support.google.com/drive/answer/16722399)
- [Homebrew Google Drive cask](https://formulae.brew.sh/cask/google-drive)
- [Homebrew installation and shell setup](https://docs.brew.sh/Installation)
- [Obsidian installation](https://help.obsidian.md/install)
- [Obsidian Homebrew cask](https://formulae.brew.sh/cask/obsidian)
- [Python downloads and maintained releases](https://www.python.org/downloads/)
