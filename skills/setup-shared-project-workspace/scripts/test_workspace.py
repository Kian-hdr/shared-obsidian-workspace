#!/usr/bin/env python3
"""Behavioral regression tests for the generated workspace and tracker."""

from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

SKILL_ROOT = Path(__file__).resolve().parent.parent
SETUP = SKILL_ROOT / "scripts" / "setup_workspace.py"


def snapshot(root: Path) -> dict[str, str]:
    return {
        str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in root.rglob("*")
        if path.is_file()
    }


def read_note(path: Path) -> tuple[dict, str]:
    parts = path.read_text(encoding="utf-8").split("---", 2)
    return yaml.safe_load(parts[1]), parts[2]


def write_note(path: Path, data: dict, body: str) -> None:
    path.write_text("---\n" + yaml.safe_dump(data, sort_keys=False, width=1000000) + "---" + body, encoding="utf-8")


class WorkspaceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="shared-workspace-test-")
        self.root = Path(self.temporary.name) / "Project"
        self.root.mkdir()
        self.setup_project(self.root)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_command(self, command: list[str], expected: int = 0) -> subprocess.CompletedProcess:
        result = subprocess.run(command, text=True, capture_output=True, check=False)
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return result

    def setup_project(self, root: Path, extra: list[str] | None = None, expected: int = 0) -> subprocess.CompletedProcess:
        return self.run_command([
            sys.executable, str(SETUP), str(root), "--purpose", "Test shared project",
            "--actor", "taylor-codex", "--initiated-by", "Taylor", "--agent", "Codex",
        ] + (extra or []), expected)

    def tracker(self, *arguments: str, expected: int = 0) -> subprocess.CompletedProcess:
        return self.run_command([sys.executable, str(self.root / "Coordination" / "project_tracker.py"), *arguments], expected)

    def claim(self, work_id: str = "ARCH-001", target: str = "architecture.md", actor: str = "taylor-codex", owner: str = "Taylor", extra: list[str] | None = None) -> subprocess.CompletedProcess:
        return self.tracker(
            "claim", "--work-id", work_id, "--title", work_id,
            "--actor", actor, "--owner", owner, "--agent", "Codex", "--initiated-by", owner,
            "--target", target, "--objective", "Produce a tested output",
            "--acceptance", "Output exists", "--acceptance", "Validation passes",
            "--next-action", "Implement output", *(extra or []),
        )

    def change(self, work_id: str = "ARCH-001", actor: str = "taylor-codex", extra: list[str] | None = None, expected: int = 0) -> subprocess.CompletedProcess:
        return self.tracker(
            "change", "--work-id", work_id, "--actor", actor, "--summary", "Output updated",
            "--change-kind", "implementation", "--impact", "compatible", "--next-action", "Review output",
            *(extra or []), expected=expected,
        )

    def work_path(self, work_id: str = "ARCH-001") -> Path:
        return self.root / "Coordination" / "Items" / f"WORK-{work_id}.md"

    def test_bootstrap_has_only_lean_fixed_files(self) -> None:
        self.assertTrue((self.root / "AGENTS.md").exists())
        self.assertTrue((self.root / "CLAUDE.md").exists())
        self.assertTrue((self.root / "README.md").exists())
        self.assertFalse((self.root / "AI-README.md").exists())
        self.assertFalse((self.root / "Project Memory.md").exists())
        self.tracker("validate")

    def plan_work(self, work_id="BACKLOG-001", target="future.md", extra=None):
        return self.tracker("plan", "--work-id", work_id, "--title", "Review historical work",
            "--actor", "taylor-codex", "--owner", "Taylor", "--agent", "Codex", "--initiated-by", "Taylor",
            "--suggested-owner", "Morgan", "--target", target,
            "--objective", "Reconcile recorded state", "--acceptance", "Owner verifies current evidence",
            "--source-summary", "Historical: baseline passed; current status unverified",
            "--source-evidence", "legacy.md", "--next-action", "Review source", *(extra or []))

    def start_work(self, work_id="BACKLOG-001", expected=0):
        return self.tracker("start", "--work-id", work_id, "--actor", "morgan-agent-session",
            "--owner", "Morgan", "--agent", "Claude", "--summary", "Reviewed historical context and scope",
            "--evidence", "owner-review.md", "--next-action", "Perform the bounded work", expected=expected)

    def test_backlog_does_not_claim_or_assign_suggested_owner(self):
        self.plan_work()
        data, _ = read_note(self.work_path("BACKLOG-001"))
        self.assertEqual(data["status"], "not_started")
        self.assertEqual(data["owner"], "Unassigned")
        self.assertEqual(data["actor_id"], "")
        self.assertEqual(data["claim_expires"], "")
        self.assertEqual(data["suggested_owner"], "Morgan")
        self.assertEqual(data["acceptance_passed"], 0)
        actor, _ = read_note(self.root / "Coordination/Items/ACTOR-TAYLOR-CODEX.md")
        self.assertNotIn("BACKLOG-001", actor["active_work"])
        self.tracker("validate")

    def test_backlog_allows_overlap_but_start_rejects_active_conflict(self):
        self.claim(target="shared.md")
        self.plan_work(target="shared.md")
        before = snapshot(self.root)
        self.start_work(expected=1)
        self.assertEqual(before, snapshot(self.root))

    def test_start_backlog_records_actor_review_and_preserves_events(self):
        self.plan_work()
        events = {p: p.read_bytes() for p in (self.root / "Coordination/Items").glob("EVENT-*.md")}
        self.start_work()
        data, _ = read_note(self.work_path("BACKLOG-001"))
        self.assertEqual(data["actor_id"], "MORGAN-AGENT-SESSION")
        self.assertEqual(data["revision"], 2)
        self.assertEqual(data["status"], "claimed")
        self.assertEqual(data["source_evidence"], ["legacy.md"])
        self.assertIn("owner-review.md", data["evidence"])
        self.tracker("check", "--actor", "morgan-agent-session", "--work-id", "BACKLOG-001")
        for path, original in events.items():
            self.assertEqual(path.read_bytes(), original)
        self.tracker("validate")

    def test_start_cannot_steal_existing_claim(self):
        self.claim()
        before = snapshot(self.root)
        self.start_work("ARCH-001", expected=1)
        self.assertEqual(before, snapshot(self.root))

    def test_backlog_start_refreshes_reviewed_dependency_baseline(self):
        self.claim()
        self.plan_work(extra=["--depends-on", "ARCH-001"])
        self.change()
        self.start_work()
        data, _ = read_note(self.work_path("BACKLOG-001"))
        self.assertEqual(data["dependency_baseline"], ["ARCH-001@2"])
        self.tracker("validate")

    def test_idempotent_setup(self) -> None:
        before = snapshot(self.root)
        self.setup_project(self.root)
        self.assertEqual(before, snapshot(self.root))

    def test_retrofit_preserves_existing_instructions_and_dossier(self) -> None:
        root = Path(self.temporary.name) / "Legacy"
        root.mkdir()
        (root / "AGENTS.md").write_text("# Existing rules\n\nNever publish.\n", encoding="utf-8")
        (root / "CLAUDE.md").write_text("# Existing Claude settings\n", encoding="utf-8")
        (root / "Legacy.md").write_text("# Existing dossier\n", encoding="utf-8")
        self.setup_project(root, ["--mode", "retrofit"])
        self.assertTrue((root / "AGENTS.md").read_text().startswith("# Existing rules\n\nNever publish."))
        self.assertTrue((root / "CLAUDE.md").read_text().startswith("# Existing Claude settings"))
        self.assertFalse((root / "README.md").exists())

    def test_dry_run_has_no_writes(self) -> None:
        before = snapshot(self.root)
        self.setup_project(self.root, ["--dry-run"])
        self.assertEqual(before, snapshot(self.root))

    def test_audit_has_no_writes(self) -> None:
        before = snapshot(self.root)
        self.run_command([sys.executable, str(SETUP), str(self.root), "--mode", "audit"])
        self.assertEqual(before, snapshot(self.root))

    def test_unsigned_conflict_stops_before_mutation(self) -> None:
        root = Path(self.temporary.name) / "Conflict"
        (root / "Coordination").mkdir(parents=True)
        (root / "Coordination" / "project_tracker.py").write_text("print('mine')\n")
        before = snapshot(root)
        self.setup_project(root, expected=1)
        self.assertEqual(before, snapshot(root))

    def test_modified_generated_file_requires_review(self) -> None:
        path = self.root / "Coordination" / "project_tracker.py"
        path.write_text(path.read_text() + "\n# user customization\n")
        before = snapshot(self.root)
        self.setup_project(self.root, expected=1)
        self.assertEqual(before, snapshot(self.root))

    def test_audit_does_not_execute_project_tracker(self) -> None:
        path = self.root / "Coordination" / "project_tracker.py"
        path.write_text("from pathlib import Path\nPath('UNSAFE-AUDIT').write_text('ran')\n")
        result = self.run_command([sys.executable, str(SETUP), str(self.root), "--mode", "audit"], expected=1)
        self.assertIn("differs from the trusted", result.stdout)
        self.assertFalse((self.root / "UNSAFE-AUDIT").exists())

    def test_claims_allow_distinct_targets(self) -> None:
        self.claim()
        self.claim("DATA-002", "data.md", "jordan-codex", "Jordan")
        self.tracker("validate")

    def test_overlapping_claim_is_rejected(self) -> None:
        self.claim(target="src")
        result = self.tracker(
            "claim", "--work-id", "OTHER", "--title", "Other", "--actor", "jordan-codex",
            "--owner", "Jordan", "--agent", "Codex", "--initiated-by", "Jordan",
            "--target", "src/adapter.py", "--objective", "Test", "--acceptance", "Done",
            "--next-action", "Test", expected=1,
        )
        self.assertIn("Target conflict", result.stderr)

    def test_windows_and_case_aliases_conflict(self) -> None:
        self.claim(target="src/adapter.py")
        result = self.tracker(
            "claim", "--work-id", "OTHER", "--title", "Other", "--actor", "jordan-codex",
            "--owner", "Jordan", "--agent", "Codex", "--initiated-by", "Jordan",
            "--target", "SRC\\adapter.py", "--objective", "Test", "--acceptance", "Done",
            "--next-action", "Test", expected=1,
        )
        self.assertIn("Target conflict", result.stderr)

    def test_dependency_change_requires_acknowledgement(self) -> None:
        self.claim()
        self.claim("CONTROL-002", "control.py", "jordan-codex", "Jordan", ["--depends-on", "ARCH-001"])
        self.change(extra=["--impact", "breaking"])
        self.assertIn("NEEDS SYNC", self.tracker("status").stdout)
        self.change("CONTROL-002", "jordan-codex", expected=1)
        self.tracker("acknowledge", "--actor", "jordan-codex", "--work-id", "CONTROL-002", "--dependency", "ARCH-001", "--summary", "Reviewed the new interface", "--next-action", "Update adapter")
        self.change("CONTROL-002", "jordan-codex")

    def test_unrecorded_change_is_detected_and_recorded(self) -> None:
        self.claim()
        self.tracker("check", "--actor", "taylor-codex", "--work-id", "ARCH-001")
        (self.root / "architecture.md").write_text("new content\n")
        self.tracker("reconcile", expected=1)
        self.tracker("check", "--actor", "taylor-codex", "--work-id", "ARCH-001", expected=1)
        self.change()
        self.tracker("reconcile")

    def test_exact_acceptance_criteria_and_completion_gate(self) -> None:
        self.claim()
        self.change(extra=["--pass-criterion", "2"])
        data, body = read_note(self.work_path())
        self.assertEqual(data["passed_criteria"], [2])
        self.assertIn("- [ ] 1. Output exists", body)
        self.assertIn("- [x] 2. Validation passes", body)
        self.tracker("complete", "--actor", "taylor-codex", "--work-id", "ARCH-001", "--summary", "Complete", "--evidence", "test.log", "--validation", "Tests passed", expected=1)
        self.change(extra=["--pass-criterion", "1", "--evidence", "test.log", "--validation", "Tests passed"])
        self.tracker("complete", "--actor", "taylor-codex", "--work-id", "ARCH-001", "--summary", "Complete", "--evidence", "test.log", "--validation", "Tests passed")
        self.assertEqual(read_note(self.work_path())[0]["status"], "verified")

    def test_handoff_requires_acceptance_and_blocks_old_owner(self) -> None:
        self.claim()
        self.tracker("handoff", "--actor", "taylor-codex", "--work-id", "ARCH-001", "--to-actor", "jordan-codex", "--to-owner", "Jordan", "--to-agent", "Codex", "--last-verified", "Initial claim", "--next-action", "Continue implementation")
        self.change(expected=1)
        self.change(actor="jordan-codex", expected=1)
        self.tracker("accept-handoff", "--actor", "jordan-codex", "--work-id", "ARCH-001", "--summary", "Reviewed handoff", "--next-action", "Continue implementation")
        self.change(actor="jordan-codex")

    def test_stale_claim_is_detected_and_renewed(self) -> None:
        self.claim()
        data, body = read_note(self.work_path())
        data["claim_expires"] = "2000-01-01T00:00:00Z"
        write_note(self.work_path(), data, body)
        self.assertIn("STALE CLAIM", self.tracker("status").stdout)
        self.tracker("check", "--actor", "taylor-codex", "--work-id", "ARCH-001", expected=1)
        self.tracker("heartbeat", "--actor", "taylor-codex", "--work-id", "ARCH-001")
        self.tracker("check", "--actor", "taylor-codex", "--work-id", "ARCH-001")

    def test_late_arriving_older_event_is_not_lost(self) -> None:
        self.tracker("sync", "--actor", "taylor-codex")
        self.tracker("decision", "--decision-key", "late-arrival", "--actor", "taylor-codex", "--owner", "Taylor", "--agent", "Codex", "--initiated-by", "Taylor", "--summary", "Late decision", "--rationale", "Offline event", "--impact", "compatible")
        path = next((self.root / "Coordination" / "Items").glob("DECISION-*-LATE-ARRIVAL-*.md"))
        data, body = read_note(path)
        data["timestamp"] = "2000-01-01T00:00:00Z"
        write_note(path, data, body)
        self.assertIn("Late decision", self.tracker("sync", "--actor", "taylor-codex").stdout)
        self.assertIn("0 new immutable", self.tracker("sync", "--actor", "taylor-codex").stdout)

    def test_existing_events_remain_byte_identical(self) -> None:
        self.claim()
        items = self.root / "Coordination" / "Items"
        before = {path.name: path.read_bytes() for path in items.glob("EVENT-*.md")}
        self.change()
        for name, content in before.items():
            self.assertEqual((items / name).read_bytes(), content)

    def test_correction_supersedes_without_rewriting(self) -> None:
        self.claim()
        event_path = next((self.root / "Coordination" / "Items").glob("EVENT-*.md"))
        before = event_path.read_bytes()
        event_id = read_note(event_path)[0]["event_id"]
        self.change(extra=["--supersedes", event_id])
        self.assertEqual(event_path.read_bytes(), before)
        events = [read_note(path)[0] for path in (self.root / "Coordination" / "Items").glob("EVENT-*.md")]
        self.assertTrue(any(event.get("supersedes") == event_id for event in events))

    def test_same_second_events_have_unique_ids(self) -> None:
        self.claim()
        self.change()
        self.change()
        ids = [read_note(path)[0]["event_id"] for path in (self.root / "Coordination" / "Items").glob("EVENT-*.md")]
        self.assertEqual(len(ids), len(set(ids)))

    def test_actor_identity_collision_is_rejected(self) -> None:
        self.tracker("sync", "--actor", "taylor-codex", "--human", "Not Taylor", "--agent", "Codex", expected=1)

    def test_email_actor_id_is_rejected(self) -> None:
        self.tracker("sync", "--actor", "test@example.com", "--human", "Test", "--agent", "Codex", expected=1)

    def test_dependency_cycle_is_detected(self) -> None:
        self.claim()
        self.claim("CONTROL-002", "control.py", "jordan-codex", "Jordan", ["--depends-on", "ARCH-001"])
        data, body = read_note(self.work_path())
        data["depends_on"] = ["CONTROL-002"]
        data["dependency_baseline"] = ["CONTROL-002@1"]
        write_note(self.work_path(), data, body)
        self.assertIn("Dependency cycle", self.tracker("validate", expected=1).stdout)

    def test_base_yaml_and_view_structure(self) -> None:
        base = yaml.safe_load((self.root / "Coordination" / "Workspace.base").read_text())
        self.assertIn('file.inFolder("Coordination/Items")', base["filters"]["and"])
        names = {view["name"] for view in base["views"]}
        self.assertTrue({"Current work", "Recent activity", "Open handoffs", "Stale claims"}.issubset(names))
        self.assertTrue(all(view["type"] == "table" for view in base["views"]))

    def test_nested_obsidian_path_is_scoped(self) -> None:
        vault = Path(self.temporary.name) / "Vault"
        (vault / ".obsidian").mkdir(parents=True)
        target = vault / "Projects" / "Nested"
        target.mkdir(parents=True)
        self.setup_project(target)
        base = yaml.safe_load((target / "Coordination" / "Workspace.base").read_text())
        self.assertIn('file.inFolder("Projects/Nested/Coordination/Items")', base["filters"]["and"])
        self.assertEqual(read_note(target / "README.md")[0]["type"], "project")

    def test_git_and_hybrid_modes(self) -> None:
        root = Path(self.temporary.name) / "GitProject"
        (root / ".git").mkdir(parents=True)
        self.setup_project(root)
        self.assertIn("Collaboration mode: `git`", (root / "AGENTS.md").read_text())
        self.setup_project(root, ["--collaboration-mode", "hybrid", "--upgrade-managed"])
        self.assertIn("Collaboration mode: `hybrid`", (root / "AGENTS.md").read_text())


if __name__ == "__main__":
    unittest.main(verbosity=2)
