"""Candidate-only queue admission. No scheduler activation or canonical repin."""
from __future__ import annotations
import hashlib
import json
import re
import time
from pathlib import Path

REQUEST = "Repair only the isolated AIOS path-containment test fixture."
RECIPE = "aios-path-containment-fixture-v1"

def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

def authorize(root: Path, principal: dict, request: dict, *, test_identity=False):
    if set(request) != {'request_id', 'instruction'} or request['instruction'] != REQUEST:
        raise ValueError('instruction outside bounded maintenance recipe')
    if not isinstance(request['request_id'], str) or not re.fullmatch(r'[a-zA-Z0-9_-]{8,80}', request['request_id']):
        raise ValueError('invalid idempotency identity')
    if (not principal.get('subject') or principal.get('issuer') not in
            ({'github', 'TEST_IDENTITY'} if test_identity else {'github'})
            or not 0 <= time.time() - principal.get('verified_at', 0) <= 60):
        raise PermissionError('fresh provider-verified owner identity required')
    authority = json.loads((root/'state/CURRENT_PROJECT.json').read_text())
    policy = json.loads((root/'config/friday_automation_policy.json').read_text())
    queue = json.loads((root/'state/FRIDAY_MAINTENANCE_QUEUE.json').read_text())
    work = authority.get('work_order', {})
    if (authority.get('authority', {}).get('governance') != {'repo':'Karmicmurphy/Harness-card','branch':'main'}
            or work.get('gate_id') != 'FRIDAY_BOUNDED_OPERATOR_LOOP' or work.get('status') != 'ACTIVE'
            or policy.get('mode') != 'AUTOMATE_UNTIL_OWNER_GATE'
            or 'run deterministic tests, validators, benchmarks, and candidate CI' not in policy.get('automatic_actions', [])):
        raise PermissionError('Harness does not authorize candidate maintenance tests')
    runtime = authority['authority']['runtime']
    if queue.get('scope') != 'APPROVED_REFS_READ_ONLY':
        raise PermissionError('unexpected maintenance queue scope')
    rows = [r for r in queue.get('items', []) if r.get('role') == 'runtime']
    if len(rows) != 1:
        raise PermissionError('runtime queue identity missing or duplicated')
    row = rows[0]
    if (row.get('repo') != runtime['repo'] or row.get('approved_sha') != runtime['sha']
            or row.get('owner_gate') != 'NO_AUTO_REPIN_OR_MERGE'
            or row.get('state') not in {'TRIAGED_REVIEW_REQUIRED', 'UNTRIAGED_READ_ONLY'}
            or 'proof-gate' not in row.get('skill_routes', [])):
        raise PermissionError('queue is not eligible for isolated candidate proof')
    # A diagnostic row never authorizes repairing its live repository. This is
    # an explicitly requested disposable candidate test under existing policy.
    binding = {'authority': authority, 'policy': policy, 'queue_row': row}
    return {'request_id': request['request_id'], 'instruction': REQUEST, 'recipe': RECIPE,
            'subject': principal['subject'], 'issuer': principal['issuer'],
            'authority_digest': digest(binding), 'runtime': runtime,
            'queue_identity': digest(row), 'scope': 'DISPOSABLE_CANDIDATE_ONLY',
            'activation_permitted': False}
