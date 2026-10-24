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
        self.assertEqual(current["work_order"]["gate_id"], "FRIDAY_BOUNDED_OPERATOR_LOOP")
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
