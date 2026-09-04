# Set this up with your own agent

Copy the entire block below into your own agent's chat. **No placeholders need
editing.** Your agent will ask for your vault or shared-project location if it
cannot determine it. Use an agent that can work with local files and a terminal
on your computer; a browser-only chat may need to hand off the local steps.

This prompt supports setting up your own workspace and joining an existing one.
It does not contain a private vault invitation or grant access to someone else's files.

```text
Set up my computer and the correct Obsidian or Markdown project so I can work with
my AI agent and collaborate with other people using this toolkit:
https://github.com/Kian-hdr/shared-obsidian-workspace

Carry out the setup with the tools you have. Reuse working components and continue
through reversible, in-scope steps without repeatedly asking for permission. I
authorize necessary local setup, including installing a compatible Python runtime,
this skill, and Obsidian if needed for the vault I choose. Preserve my existing
files, accounts, agent settings, and sharing provider. Do not claim you configured
my computer if you can only operate in a remote container or browser-only chat.

1. Identify the target and my role.
Inspect the current workspace and available local tools, without scanning unrelated
private folders. Determine my OS and whether I am setting up my own project or
joining someone else's existing shared project. If the target or role is unclear,
ask for my vault/project path or shared-folder link and which situation applies.
Ask my name only if unknown. If I want a new vault, agree its name and location
before creating it. Never treat the toolkit repository as my working vault.

2. Get and inspect the toolkit.
Reuse a clean existing checkout or download this exact public repository to a
local tools directory outside my synchronized vault. Do not reset a modified copy.
Record the commit or source version you use. Read README.md, AGENTS.md, docs/SETUP.md,
docs/COLLABORATION.md, and skills/setup-shared-project-workspace/SKILL.md. Also read
that skill's references/retrofit-policy.md and references/teammate-onboarding.md.
Inspect scripts before execution. Follow their actual help and use correctly
quoted paths and the appropriate interpreter for my OS. Never execute placeholders.

3. Prepare this computer.
Reuse existing Python and Obsidian. The setup and tracker require Python 3.9+
and no third-party Python packages; test dependencies are not needed for normal use.
Verify current compatibility and use official sources for any necessary installs.
If my agent supports skills, install the complete skill folder, including assets,
scripts, references, metadata, and license, in its supported local skill location.
Back up and compare an existing installation rather than blindly replacing it.
If skills are unsupported, read SKILL.md directly and use the bundled scripts.
Joining an already configured project does not require installing this skill.

4. Locate the real project and establish access.
Read the governing vault and project instructions, existing home note, and current
coordination state. For a shared project, resolve the actual locally synchronized
folder and confirm its required files are readable and I have the necessary access.
Use the onboarding reference for the existing sharing provider. If its desktop
client is missing, explain the required installation and obtain my approval before
installing it. Do not introduce a new sharing service or duplicate the shared vault.
Hand password, passkey, MFA, consent, and administrator prompts to me through their
normal interfaces. If access is denied, prepare the exact next step; ask before
sending an access request or changing permissions, then resume after access is granted.
Finish independent local checks while an external step is pending.

5. Set up or join, according to the actual state.
For my own unconfigured project, back up affected files, merge the toolkit's general
AGENTS.md guidance into the vault instructions, and preserve stricter existing rules.
Remove the template-repository-specific sentence from the copied guidance. Audit,
preview, and then apply a compatible bootstrap or retrofit using the bundled skill.
Reuse the existing project home, passing Home.md explicitly when appropriate. Use
my identity and a unique actor ID without my email address. Preserve the recorded
collaboration mode, or infer it from the actual storage/code workflow if none exists.
Review the preview yourself and proceed with compatible local
changes. Pause only for a real conflict, missing required input, or consequential choice.

For an already configured project, reuse its instructions and coordination layer.
Do not bootstrap again, upgrade its tracker, merge new shared instructions, repair
history, take another actor's identity, claim existing work, or resume paused work
under this onboarding request. Verify the tracker against the owner's trusted
SHA-256 digest or reviewed provenance. A generated-file signature alone is not
sufficient. If it differs, request the owner's reviewed version or updated digest
before running it. Missing project files are a blocker, not permission to recreate them.

6. Connect my agent and Obsidian.
Open the real project in my agent and explicitly load its governing AGENTS.md.
Verify that the agent understands target ownership, checkpoints, evidence, and
handoffs. Do not assume automatic instruction discovery or weaken global permissions.
Open the existing vault in Obsidian if available; do not create a nested duplicate,
overwrite .obsidian settings, install community plugins, or add a second sync service.
Inspect Coordination/Workspace.base visually when UI tools are available; otherwise
label the visual check unverified. If a new agent session is necessary, give me the
exact local path and a continuation prompt so the setup can resume.

7. Validate and establish my own context.
Run workspace validation and inspect tracker status. Investigate errors without
deleting records to make checks pass. After validation and editing access are
confirmed, use the tracker to sync my own actor identity and review recent changes,
blockers, and dependencies. Do not claim a task just to prove setup works.
Verify the actor record locally and, for a synchronized project, its provider upload
when tools permit. Run validation again after my actor record is created or updated.
Tracker sync only refreshes local context; it does not upload
files or provide distributed locking. Another computer's receipt is a separate check.

8. Report and hand off.
Give me the exact project and vault paths, toolkit version, skill location or direct
script fallback, actor ID, what was reused or changed, validation results, and next
action. Distinguish locally configured, shared collaboration ready, partially
configured, and blocked. Call shared collaboration ready only when the agent has
loaded the rules, validation passes, shared editing access works, and my actor
record's upload is verified. Do not imply a local-only project is already shared.
List any unverified UI or other-device checks and the smallest step needed to finish.

If you bootstrapped or retrofitted my project, also give me the skill's teammate
onboarding prompt in chat using verified project details. Ask for an approved
sharing URL only if needed to finish that invitation; do not invent a URL or call
an unfilled invitation ready to send. Keep my private paths and project details
out of the public toolkit. Do not send messages, publish, buy anything, change
accounts or sharing permissions, or destructively remove files without my explicit
authorization for that action.
```
