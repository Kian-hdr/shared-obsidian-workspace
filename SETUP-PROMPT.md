# Set this up with your own agent

Copy the entire block below into your own agent's chat. **No placeholders need
editing.** Your agent will ask for your vault or shared-project location if it
cannot determine it. Use an agent that can work with local files and a terminal
on your computer; a browser-only chat may need to hand off the local steps.

This prompt supports setting up your own workspace and joining an existing one.
It does not contain a private vault invitation or grant access to someone else's files.
No particular storage provider or online account is required. Your agent will use
your own local folder, repository, or existing sharing method.
It authorizes required local installs and configuration. If you choose Homebrew,
the agent will install and configure it when missing. Your agent's approval settings
and operating system controls still apply.

```text
Set up my computer and the correct Obsidian or Markdown project so I can work with
my AI agent and collaborate with other people using this toolkit:
https://github.com/Kian-hdr/shared-obsidian-workspace

Carry out the setup with the tools you have. Reuse working components and continue
through in-scope steps without repeatedly asking for permission. I authorize the
necessary local installations and configuration: Obsidian for an Obsidian workspace,
a compatible maintained Python, this skill, and only the clients/prerequisites needed
by my actual access method, plus minimal shell/PATH setup. If I choose
Homebrew, install and configure it too when missing. Reuse my preferred installation
route; otherwise use an existing suitable package manager or an official installer.
Do not ask me to approve each already-authorized package or routine setup step.
Honor my actual approval settings and enforced tool, OS, and administrator policies.
Pause only for missing required information, a real enforced gate, an action outside
scope, or an interaction only I can perform. Resume automatically afterward. Preserve
existing files, accounts, agent settings, and the sharing provider. Do not claim you
configured my computer from a remote container or browser-only chat.

1. Identify the target and my role.
Inspect the current workspace and available local tools, without scanning unrelated
private folders. Determine my OS, my intended project/vault roots, and whether I am
setting up my own project or joining an existing one. Establish whether I use a
local-only directory, Git, a shared folder with a known provider, or a hybrid workflow.
Do not assume any storage provider, account, domain, or sender's machine path. The
GitHub namespace above identifies the toolkit source, not my identity or vault.
If the target or role is unclear, ask for my local project path or the actual access
locator and which situation applies. Do not demand a cloud URL for local-only work.
Ask my name only if unknown. If I want a new vault, agree its name and location
before creating it. Never treat the toolkit repository as my working vault.

2. Get and inspect the toolkit.
Reuse a clean existing checkout or download this exact public repository to a
local tools directory outside my synchronized vault. Do not reset a modified copy.
Record the commit or source version you use. Read README.md, AGENTS.md, docs/SETUP.md,
docs/COLLABORATION.md, and skills/setup-shared-project-workspace/SKILL.md. Also read
that skill's references/retrofit-policy.md, references/local-setup.md,
references/storage-access.md, and
references/teammate-onboarding.md.
Inspect scripts before execution. Follow their actual help and use correctly
quoted paths and the appropriate interpreter for my OS. Never execute placeholders.

3. Prepare this computer.
Follow references/local-setup.md to install missing dependencies and finish their
configuration. Reuse existing Python and Obsidian. Python 3.9+ is the compatibility
floor; choose a maintained stable release for a new install. Normal setup needs no
third-party Python packages. If I chose Homebrew and it is missing, install it from
its official source, handle required prerequisites, apply its shellenv instructions
to the correct shell without duplicating entries, and verify brew in a fresh shell.
Unless I requested Markdown-only work or declined Obsidian, install missing Obsidian
through the chosen supported route. Verify current package
and OS compatibility instead of assuming every Homebrew package runs on every OS.
Use documented unattended options when appropriate and permitted. Hand off required
password, administrator, MFA, and consent interactions through their normal UI,
then resume. Do not weaken security or approval settings to suppress those gates.
If my agent supports skills, install the complete skill folder, including assets,
scripts, references, metadata, and license, in its supported local skill location.
Back up and compare an existing installation rather than blindly replacing it.
If skills are unsupported, read SKILL.md directly and use the bundled scripts.
Joining an already configured project does not require installing this skill.

4. Locate the real project and establish access.
Read the governing vault/project instructions, existing home, and coordination state.
Follow only the selected access method in references/storage-access.md. Use my own
account if one is required, and resolve my actual local paths. For a shared folder,
verify its provider/server and access. For Git, reuse or obtain the authorized project
checkout, preserve local work, and identify the intended branch and enclosing Git root.
For hybrid work, map each target to its authority. For local-only work, use my chosen
directory with no remote account, storage client, sharing URL, or upload requirement.
Install a client only if that actual workflow needs it, under the authorization above.
Some methods use an existing app or OS facility instead. Do not introduce another
service or treat a downloaded project copy as a live synchronized workspace.
Hand password, passkey, MFA, consent, and administrator prompts to me through their
normal interfaces. If access is denied, prepare the exact next step; ask before
sending an access request or changing permissions, then resume after access is granted.
Finish independent local checks while an external step is pending.

5. Set up or join, according to the actual state.
For my own unconfigured project, back up affected files, merge the toolkit's general
AGENTS.md guidance into the vault instructions, and preserve stricter existing rules.
Audit, preview, and apply a compatible bootstrap or retrofit using the bundled skill.
Reuse the existing project home inside the project; keep its stored path relative. Use
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
Unless I requested Markdown-only setup or declined Obsidian, finish installing and launching Obsidian,
then open the correct existing vault or my chosen new vault. Verify the app launch
and vault opening when UI tools are available. Do not create a nested duplicate,
overwrite .obsidian settings, install community plugins, or add a second sync service.
Inspect Coordination/Workspace.base visually when UI tools are available; otherwise
label the visual check unverified. If a new agent session is necessary, give me the
exact local path and a continuation prompt so the setup can resume.

7. Validate and establish my own context.
Run workspace validation and inspect tracker status. Investigate errors without
deleting records to make checks pass. After validation and editing access are
confirmed, use the tracker to sync my own actor identity and review recent changes,
blockers, and dependencies. Do not claim a task just to prove setup works.
Verify the actor record locally and rerun validation after creation/update. Check that
shared file references resolve inside my project and that the dashboard matches my
vault layout. For shared folders, verify propagation through the actual provider/server.
For Git, report local changes, commit, push, and remote receipt separately; commit or
push only when authorized. For local-only work, remote propagation is not applicable.
For hybrid work, check each relevant authority. Tracker sync refreshes local context;
it does not upload files, perform Git operations, or provide distributed locking.
Another contributor's actual receipt is a separate check.

8. Report and hand off.
Give me the exact project and vault paths, toolkit version, skill location or direct
script fallback, actor ID, installed dependencies, PATH changes, Obsidian launch and
vault-opening results, what was reused or changed, validation results, and next
action. Distinguish locally configured, shared collaboration ready, partially
configured, and blocked. Call shared collaboration ready only when required local
installs/configuration are complete, the Obsidian app and correct vault opened (or
I explicitly omitted Obsidian), the agent has loaded the rules, validation passes,
shared editing access and propagation through the chosen method are verified. Do not imply
a local-only project is already shared.
List any unverified UI or other-device checks and the smallest step needed to finish.
Do not call the requested setup complete while a required installation, configuration,
app launch, or validation step remains unfinished.

If you bootstrapped or retrofitted my project, also give me the skill's teammate
onboarding prompt in chat using verified project details and the selected access
method. For shared work, ask only for missing essential access information, not a
specific provider's URL. For local-only setup, say no remote is configured and do not
block completion on a sharing URL. Do not invent accounts/locators or call an unfilled
shared invitation ready. Keep my private paths and project details
out of the public toolkit. Do not send messages, publish, buy anything, change
accounts or sharing permissions, or destructively remove files without my explicit
authorization for that action.
```
