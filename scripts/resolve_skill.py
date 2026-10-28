#!/usr/bin/env python3
"""Resolve Harness skill names to one canonical source.

This deliberately does not execute a skill. It removes ambiguity about which
repo/path/version an agent must load before applying a routed procedure.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REGISTRY=ROOT/"config"/"skill_registry.json"

def load_registry():
    data=json.loads(REGISTRY.read_text(encoding="utf-8"))
    if data.get("schema_version")!="1.0.0":
        raise ValueError("unsupported skill registry schema")
    return data

def resolve(name: str):
    data=load_registry()
    item=(data.get("skills") or {}).get(name)
    if not item:
        raise KeyError(f"unknown skill: {name}")
    source=(data.get("sources") or {}).get(item["source"])
    if not source:
        raise ValueError(f"missing source for skill: {name}")
    root=source.get("root","").strip("/")
    rel=item["path"].lstrip("/")
    full_path=f"{root}/{rel}" if root else rel
    return {
        "name":name,
        "kind":item["kind"],
        "repo":source["repo"],
        "ref":source["ref"],
        "authority_sha":source.get("authority_sha"),
        "path":full_path,
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("skill")
    args=p.parse_args()
    print(json.dumps(resolve(args.skill),indent=2,sort_keys=True))

if __name__=="__main__":
    main()


def discover_verified_lessons(warehouse, conditions):
    """Discover data-only proof lessons; never import executable code or grants."""
    import hashlib
    pointer = resolve('proof-gate')
    if pointer['repo'] != 'Karmicmurphy/digital-scrapyard-autopilot':
        raise ValueError('proof skill source changed')
    results = []
    for path in sorted(Path(warehouse).glob('*.json')):
        if path.is_symlink():
            raise ValueError('lesson must not be a symlink')
        row = json.loads(path.read_text())
        payload = row.get('lesson', {})
        actual = hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
        if row.get('digest') != actual:
            raise ValueError('lesson integrity mismatch')
        if (payload.get('conditions') == conditions and payload.get('status') == 'PROVEN_IN_TEST'
                and payload.get('action') == 'VERIFY_FINAL_BYTES_BEFORE_REUSE'
                and payload.get('authority_grants') == []):
            results.append({**payload, 'skill': pointer['name']})
    return results
