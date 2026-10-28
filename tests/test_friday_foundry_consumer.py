import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import time
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('consumer',ROOT/'scripts/friday_foundry_consumer.py')
consumer=importlib.util.module_from_spec(spec);spec.loader.exec_module(consumer)
class ConsumerTests(unittest.TestCase):
    def setUp(self):
        td=tempfile.TemporaryDirectory();self.addCleanup(td.cleanup);self.root=Path(td.name)
        for rel in ('state/CURRENT_PROJECT.json','state/FRIDAY_MAINTENANCE_QUEUE.json','config/friday_automation_policy.json'):
            path=self.root/rel;path.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/rel,path)
        self.request={'request_id':'candidate-001','instruction':consumer.REQUEST}
        self.principal={'subject':'fixture','issuer':'TEST_IDENTITY','verified_at':time.time()}
    def test_identity_is_not_enabled_by_request(self):
        with self.assertRaises(PermissionError):consumer.authorize(self.root,self.principal,self.request)
        result=consumer.authorize(self.root,self.principal,self.request,test_identity=True)
        self.assertFalse(result['activation_permitted'])
        self.assertEqual(result['scope'],'DISPOSABLE_CANDIDATE_ONLY')
    def test_stale_identity_and_inactive_gate_deny(self):
        self.principal['verified_at']-=61
        with self.assertRaises(PermissionError):consumer.authorize(self.root,self.principal,self.request,test_identity=True)
        self.principal['verified_at']=time.time()
        path=self.root/'state/CURRENT_PROJECT.json';data=json.loads(path.read_text());data['work_order']['status']='PAUSED';path.write_text(json.dumps(data))
        with self.assertRaises(PermissionError):consumer.authorize(self.root,self.principal,self.request,test_identity=True)
    def test_queue_source_mismatch_denies_before_job(self):
        path=self.root/'state/FRIDAY_MAINTENANCE_QUEUE.json';data=json.loads(path.read_text())
        for row in data['items']:
            if row['role']=='runtime':row['approved_sha']='f'*40
        path.write_text(json.dumps(data))
        with self.assertRaises(PermissionError):consumer.authorize(self.root,self.principal,self.request,test_identity=True)
