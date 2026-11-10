#!/usr/bin/env python3
"""Regression contract: preserve real owner intent and prove the safe release routing guide.

This test checks durable instructions/CI wiring, NOT free-form FRIDAY execution,
owner authentication, provider credentials, deployed app behavior, or model weights.
"""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
VISION = "docs/FRIDAY_OWNER_VISION_AND_LEARNING_LOOP_2026-10-23.md"


def content(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class FridayOwnerVisionContractTests(unittest.TestCase):
    def test_vision_is_loaded_but_never_promoted_to_authority(self):
        agent = content("AGENTS.md")
        vision = content(VISION)
        for marker in ("FRIDAY owner-vision and capability routing", VISION,
                       "smallest sufficient", "correlated runner receipt"):
            self.assertIn(marker, agent)
        for marker in ("state/CURRENT_PROJECT.json", "config/friday_automation_policy.json",
                       "human-owned capability machine", "NOT autonomous task execution",
                       "owner/credential/spend/production/irreversible authority gate"):
            self.assertIn(marker, vision)

    def test_machine_keeps_user_authority_and_realistic_action_menu(self):
        policy = json.loads(content("config/friday_automation_policy.json"))
        current = json.loads(content("state/CURRENT_PROJECT.json"))
        self.assertEqual(policy["mode"], "AUTOMATE_UNTIL_OWNER_GATE")
        self.assertIn("broaden permissions or authorization scope", policy["owner_gate_actions"])
        self.assertIn("destructive or irreversible mutation", policy["owner_gate_actions"])
        self.assertIn("claim PROVEN_LIVE from tests, builds, deploy metadata, or mockups alone", policy["never_automatic"])
        work = current["work_order"]
        self.assertEqual(work["gate_id"], "FRIDAY_POST_003_LESSON_RETRIEVAL_REUSE_REVIEW")
        self.assertEqual(work["status"], "ACTIVE")
        historical = json.loads(content("state/receipts/FRIDAY_COMMISSIONING_SUCCESSOR_2026-11-07.json"))
        next_release = json.loads(content("state/receipts/FRIDAY_COMMISSIONING_003_RELEASE_2026-11-09.json"))
        self.assertEqual(work["hosted_fixture"], next_release["hosted_fixture"])
        self.assertEqual(work["hosted_fixture"], {
            "request_id": "request-commissioning-003",
            "recipe": "aios-path-containment-fixture-v1",
            "owner_github_id": 141688225,
            "manifest_sha256": "46e0cb9446779bdcf65dc442897a4775de17dfa04a756af2d8bcd39579550961",
            "workflow_sha": "6e37d786b5f73ea8de03f95ed99ec21cf09113b8",
        })
        # A past approval is an immutable historical record, not current authority.
        self.assertEqual(historical["hosted_fixture"]["request_id"], "request-commissioning-002")
        self.assertEqual(historical["reviewed_control_tree"], "ce2a9ece7e35720afe705140dcbd9be42bf0bcf8")
        self.assertEqual(next_release["state"], "PREPARED_NOT_ACTIVATED")
        self.assertRegex(work["hosted_fixture"]["workflow_sha"], r"^[0-9a-f]{40}$")
        self.assertEqual([x["request_id"] for x in work["previous_hosted_fixtures"]],
                         ["request-first-001", "request-commissioning-002", "request-commissioning-003"])
        self.assertTrue(all(not x["rerun_authorized"] for x in work["previous_hosted_fixtures"]))
        closed = work["previous_hosted_fixtures"][-1]
        self.assertEqual(closed["run_id"], 42802809287)
        self.assertEqual(closed["status"], "CERTIFIED_DELIVERED_READONLY_CLOSED")
        self.assertFalse(closed["rerun_authorized"])
        self.assertFalse(closed["activation_performed"])
        self.assertIn("WINDOWS_LOCAL_INVENTORY_DEFERRED_OWNER_REPORTS_PC_SLEEPING", work["blockers"])
        self.assertIn("no Windows inventory", current["next_action"])
        receipt = json.loads(content("state/receipts/FRIDAY_COMMISSIONING_003_CLOSEOUT_2026-11-10.json"))
        self.assertEqual(receipt["github"]["run_id"], closed["run_id"])
        self.assertEqual(receipt["job"]["certificate_id"], closed["certificate_id"])
        self.assertFalse(receipt["job"]["activation_performed"])
        self.assertFalse(receipt["shutdown"]["workshop_submit_enabled"])
        self.assertFalse(receipt["lesson_archive"]["automatic_reuse_proven"])
        self.assertEqual(receipt["lesson_archive"]["authority_grants"], [])

        operator = content("scripts/friday_operator.py")
        self.assertIn("Choose from the fixed local action menu, never from free-form text.", operator)

    def test_registered_harness_skill_leads_and_no_new_agent(self):
        routes = json.loads(content("config/skill_registry.json"))["skills"]
        self.assertIn("chat-software-harness", routes)
        self.assertIn("friday-provider-release", routes)
        self.assertIn("owner-interruption-minimizer", routes)
        self.assertIn("capability-downshift", routes)
        chat = content("skills/chat-software-harness/SKILL.md")
        for expected in (VISION, "cheapest sufficient verified capability",
                         "not new model weights", "correlated operator/runtime receipt"):
            self.assertIn(expected, chat)

    def test_provider_cannot_false_block_working_autobuild(self):
        skill = content("skills/friday-provider-release/SKILL.md")
        for marker in ("Multi-actor provider truth gate", "Cloudflare-native automatic Builds",
                       "provider build history keyed to exact Git commit",
                       "CLOUDFLARE_API_TOKEN", "PARTIAL_UNKNOWN",
                       "a single tool or actor", "local phone records"):
            self.assertIn(marker, skill)

    def test_spine_executes_the_contract_regression(self):
        workflow = content(".github/workflows/friday-control-plane.yml")
        self.assertIn("python tests/test_friday_owner_vision_contract.py", workflow)
        self.assertIn("tests/test_friday_owner_vision_contract.py", workflow)
        self.assertIn(VISION, workflow)


if __name__ == "__main__":
    unittest.main()
