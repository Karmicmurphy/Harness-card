import importlib.util
from pathlib import Path
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'inspect_preview_sync.py'
spec = importlib.util.spec_from_file_location('inspect_preview_sync', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

CURRENT = {"candidates": {"pages_bounded_fixture_promotion": {
    "repo": "Karmicmurphy/Ollie_Twis_Holo_workshop",
    "branch": "reviewed-branch", "sha": "a" * 40}}}
PROJECT = {"source": {"config": {"owner": "Karmicmurphy", "repo_name": "Ollie_Twis_Holo_workshop"}},
           "deployment_configs": {"preview": {"env_vars": {
               "FOUNDATION_OWNER_SUB": {"type": "secret_text", "value": "DO_NOT_LEAK"},
               "FOUNDATION_GITHUB_TOKEN": {"type": "secret_text", "value": "DO_NOT_LEAK"}}}}}
DEPLOYMENTS = [{"environment": "preview", "id": "approved-deployment",
                "latest_stage": {"status": "success"},
                "deployment_trigger": {"metadata": {"branch": "reviewed-branch", "commit_hash": "a" * 40}}}]

class SyncInspectTests(unittest.TestCase):
    def test_approved_preview_ready_without_claiming_runtime_proof(self):
        report = module.inspect(PROJECT, DEPLOYMENTS, CURRENT)
        self.assertEqual(report['state'], 'CONFIG_READY_RUNTIME_UNPROVEN')
        self.assertEqual(report['runtime_authenticated_phone_proof'], 'NOT_CHECKED')
        self.assertNotIn('DO_NOT_LEAK', str(report))

    def test_missing_token_blocks_even_if_deploy_passed(self):
        p = {**PROJECT, 'deployment_configs': {'preview': {'env_vars': {'FOUNDATION_OWNER_SUB': {}}}}}
        r = module.inspect(p, DEPLOYMENTS, CURRENT)
        self.assertEqual(r['state'], 'CONFIG_BLOCKED')
        self.assertEqual(r['required_binding_names_missing'], ['FOUNDATION_GITHUB_TOKEN'])

    def test_different_branch_does_not_count_as_approved(self):
        r = module.inspect(PROJECT, [{**DEPLOYMENTS[0], 'deployment_trigger':
             {'metadata': {'branch': 'unreviewed', 'commit_hash': 'a' * 40}}}], CURRENT)
        self.assertEqual(r['state'], 'CONFIG_BLOCKED')

    def test_missing_credentials_must_never_mean_green(self):
        r = module.run(CURRENT, None, None)
        self.assertEqual(r['state'], 'UNKNOWN')
        self.assertEqual(r['changes_performed'], False)

    def test_cli_emits_actionable_preview_findings_without_false_failure(self):
        from unittest.mock import patch
        import json
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "state").mkdir()
            (root / "state" / "CURRENT_PROJECT.json").write_text(json.dumps(CURRENT), encoding="utf-8")
            with patch.object(module, "ROOT", root):
                for state in ("UNKNOWN", "CONFIG_BLOCKED", "CONFIG_READY_RUNTIME_UNPROVEN"):
                    with self.subTest(state=state), patch.object(module, "run", return_value={"state": state}):
                        self.assertEqual(module.main(), 0)
                with patch.object(module, "run", return_value={"state": "UNRECOGNIZED"}):
                    self.assertEqual(module.main(), 2)

    def test_provider_failure_does_not_claim_blocked_or_ready(self):
        def failed(*_):
            raise ValueError('provider unavailable')
        r = module.run(CURRENT, 'account', 'token', get=failed)
        self.assertEqual(r['state'], 'UNKNOWN')
        self.assertNotIn('token', str(r))

if __name__ == '__main__':
    unittest.main()
