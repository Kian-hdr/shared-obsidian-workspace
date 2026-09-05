# Select the project's actual access method

Read only the section for the workflow established from the user's request and
project records. The toolkit does not supply an account, shared vault, storage
subscription, or required provider. A tracker mode is not evidence of a configured
remote. Discover accounts and paths on the recipient's computer, not the author's.

| Workflow | Required access information | Local prerequisites | Propagation evidence |
| --- | --- | --- | --- |
| Local-only | Recipient's chosen directory | Python; Obsidian if wanted | Local records and validation; no remote required |
| Git | Authorized remote and intended checkout/branch | Git and access appropriate to that remote | Local edits, commits, pushes, and remote receipt reported separately |
| Shared/synchronized folder | Actual service or network share, approved locator, relative project/vault paths | Only that method's supported client, app, or OS facility | Actual provider/server propagation; not tracker `sync` alone |
| Hybrid | Explicit mapping of files/repositories to authorities | Requirements for those authorities only | Evidence for each relevant target |

## Local-only

Use the selected existing directory or create the requested new one. No online
account, cloud client, sharing URL, or upload is needed. File-mode tracking uses
`shared-folder` even when the directory has no sync service; label it local-only in
the project context and final report. Sharing can be configured later under a
separate request. A copy sent to another person is independent until a shared
workflow is established; do not advertise coordinated ownership across such copies.

## Git

Use the project's actual authorized remote, which can differ from the public toolkit
repository. Preserve local work; do not reset an existing checkout or pick a new
branch arbitrarily. The recipient uses their own Git/provider identity. A public
readable remote does not prove push access. Do not create commits or push solely to
pass onboarding unless those actions are authorized.

Keep the Git checkout outside a folder managed by another sync provider. For a
project within a larger repository, identify that enclosing Git root and keep
project-relative coordination targets. Local tracker `sync` only refreshes actor
context. It does not fetch, commit, push, or prove remote propagation.

## Shared folders and services

Resolve the actual service first. Examples include an existing Obsidian Sync vault,
a supported cloud desktop client, a network share, or an already configured local
synchronization tool. These are possible workflows, not automatic installations or
claims of equivalent behavior. Check the chosen method's current official support,
access model, and compatibility with the user's OS before setup.

Preserve the user's accounts and existing provider configuration. Ask for a choice
only when multiple plausible targets/accounts remain and choosing could affect the
wrong data. A shared URL does not specify the recipient's login or local mount path.
Use the actual available path and approved relative layout. An online placeholder
or downloaded ZIP is not proof of an editable synchronized directory.

Use [local-setup.md](local-setup.md) for authorized installations. Some methods need
no additional desktop client. Do not buy a subscription, enable another sync service,
mirror all folders, or change sharing permissions implicitly. If a required service
is unsupported or blocked by policy, identify the gap instead of substituting one.

### Google Drive, only when it is the selected provider

Google Drive is optional and has no connection to the toolkit author's account.
For an existing Drive workspace, inspect the recipient's own desktop client and
chosen account. Use the current [installation/sign-in guide](https://support.google.com/drive/answer/10838124)
and [OS requirements](https://support.google.com/drive/answer/2375082). When Homebrew
is selected and the current [cask](https://formulae.brew.sh/cask/google-drive) supports
the platform, `brew install --cask google-drive` is the installation route.

Distinguish a Shared drive from a folder shared with the recipient. Resolve the
actual folder through the desktop client; do not derive a Drive ID from a local
pathname or reuse a sender's account-specific mount path. If a project shortcut is
required, follow the recipient's authorization and policy without moving/copying the
project. Do not enable unrelated Desktop/Documents/Photos backup.

Use the recipient's normal sign-in interface. Credentials, MFA, and consent remain
with that person. If access is denied, prepare an exact request and send it only if
authorized. A pending request is not granted access. Verify shared write access and
the relevant record's upload; another device's receipt remains a separate check.

## Hybrid and incomplete access information

Identify which system governs each target. Do not synchronize a `.git` directory
through a second storage provider to create a hybrid workflow. A shared document
folder and a separate code checkout can have different local roots on each computer.

If essential shared access details are missing, finish independent local work and
request only those details. Accept the locator appropriate to the method; do not
require a Google account or a folder URL for a Git, network-share, or local-only task.
Keep private project locators in the user's private handoff, never this public toolkit.
