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
