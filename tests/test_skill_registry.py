import json
import unittest
from pathlib import Path
import importlib.util

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("resolve_skill",ROOT/"scripts"/"resolve_skill.py")
MODULE=importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)

class SkillRegistryTests(unittest.TestCase):
    def test_every_skill_resolves(self):
        data=json.loads((ROOT/"config"/"skill_registry.json").read_text())
        for name in data["skills"]:
            resolved=MODULE.resolve(name)
            self.assertEqual(resolved["name"],name)
            self.assertTrue(resolved["repo"])
            self.assertTrue(resolved["path"])
            self.assertIn(resolved["kind"],{"PROCEDURAL","PROCEDURAL_CONDITIONAL","EXECUTABLE","MAPPED_NOT_IMPLEMENTED"})

    def test_external_suite_is_pinned_to_authority_sha(self):
        data=json.loads((ROOT/"config"/"skill_registry.json").read_text())
        src=data["sources"]["salvage_suite"]
        self.assertEqual(src["authority_sha"],"a059a27ef2bd662827a51da44dd8efb8863d634c")

    def test_unknown_skill_fails(self):
        with self.assertRaises(KeyError):
            MODULE.resolve("does-not-exist")

if __name__=="__main__":
    unittest.main()
