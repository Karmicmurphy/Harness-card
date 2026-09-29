import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "authority_spine", ROOT / "scripts" / "check_authority_spine.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class AuthoritySpineTests(unittest.TestCase):
    def test_current_repo_state_agrees(self):
        self.assertEqual(MODULE.validate(ROOT), [])

    def _copy_authority_fixture(self, root: Path):
        (root / "state").mkdir()
        (root / "projects").mkdir()
        (root / "config").mkdir()
        (root / "docs").mkdir()
        for rel in [
            "config/harness.json",
            "docs/FOUNDATION_V0_CURRENT_WORK_PROMPT.md",
            "state/CURRENT_PROJECT.json",
            "state/ACTIVE_WORK_ORDER.json",
            "state/ACTIVE_WORK_ORDER.md",
            "state/ECOSYSTEM_AUTHORITY_INDEX.json",
            "projects/PROJECT_INDEX.md",
        ]:
            src = ROOT / rel
            dst = root / rel
            shutil.copyfile(src, dst)

    def test_detects_active_work_order_drift(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._copy_authority_fixture(root)

            active_path = root / "state/ACTIVE_WORK_ORDER.json"
            active = json.loads(active_path.read_text(encoding="utf-8"))
            active["next_action"] = "stale next action"
            active_path.write_text(json.dumps(active, indent=2) + "\n", encoding="utf-8")

            errors = MODULE.validate(root)
            self.assertTrue(
                any("next_action" in error for error in errors),
                errors,
            )

    def test_detects_ecosystem_pointer_drift(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._copy_authority_fixture(root)

            eco_path = root / "state/ECOSYSTEM_AUTHORITY_INDEX.json"
            eco = json.loads(eco_path.read_text(encoding="utf-8"))
            for item in eco["active_foundation_v0"]["canonical_refs"]:
                if item["role"] == "factory":
                    item["sha"] = "deadbeef"
            eco_path.write_text(json.dumps(eco, indent=2) + "\n", encoding="utf-8")

            errors = MODULE.validate(root)
            self.assertTrue(
                any("factory.sha" in error for error in errors),
                errors,
            )

    def test_detects_project_index_hard_coded_authority_sha(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._copy_authority_fixture(root)

            index_path = root / "projects/PROJECT_INDEX.md"
            text = index_path.read_text(encoding="utf-8")
            marker = "- **Authority refs:** See `state/CURRENT_PROJECT.json`."
            text = text.replace(
                marker,
                marker + " stale-ref `" + ("a" * 40) + "`",
                1,
            )
            index_path.write_text(text, encoding="utf-8")

            errors = MODULE.validate(root)
            self.assertTrue(
                any("hard-code immutable component SHAs" in error for error in errors),
                errors,
            )

    def test_detects_project_index_gate_drift(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._copy_authority_fixture(root)

            current = json.loads((root / "state/CURRENT_PROJECT.json").read_text(encoding="utf-8"))
            gate = current["work_order"]["gate_id"]
            index_path = root / "projects/PROJECT_INDEX.md"
            text = index_path.read_text(encoding="utf-8").replace(f"`{gate}`", "`STALE_GATE`", 1)
            index_path.write_text(text, encoding="utf-8")

            errors = MODULE.validate(root)
            self.assertTrue(
                any("gate_id" in error for error in errors),
                errors,
            )


if __name__ == "__main__":
    unittest.main()
