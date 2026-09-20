#!/usr/bin/env python3
from __future__ import annotations
import json, re
from pathlib import Path
from typing import Any, Dict, Iterable, List

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MAP = ROOT / "state" / "CAPABILITY_MAP.json"
TOKEN_RE = re.compile(r"[a-z0-9]+")

def _tokens(value: str) -> set[str]:
    stop = {"a","an","and","the","to","of","for","in","on","with","we","do"}
    return {t for t in TOKEN_RE.findall(value.lower()) if t not in stop and len(t) > 1}

def load_map(path: Path = DEFAULT_MAP) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data.get("capabilities"), list):
        raise ValueError("capability map missing capabilities list")
    return data

def _haystack(cap: Dict[str, Any]) -> str:
    fields: Iterable[Any] = (
        cap.get("id",""), cap.get("name",""), " ".join(cap.get("owners",[])),
        " ".join(cap.get("evidence",[])), cap.get("status",""), cap.get("reuse","")
    )
    return " ".join(str(v) for v in fields)

def find_capabilities(query: str, data: Dict[str, Any] | None = None, limit: int = 5) -> List[Dict[str, Any]]:
    if data is None:
        data = load_map()
    q = _tokens(query)
    if not q:
        return []
    scored = []
    for cap in data["capabilities"]:
        h = _tokens(_haystack(cap))
        overlap = q & h
        if not overlap:
            continue
        phrase_bonus = 2 if query.lower() in _haystack(cap).lower() else 0
        scored.append((len(overlap)+phrase_bonus, cap["id"], cap))
    scored.sort(key=lambda row: (-row[0], row[1]))
    return [row[2] for row in scored[:limit]]

def answer(query: str, data: Dict[str, Any] | None = None) -> Dict[str, Any]:
    matches = find_capabilities(query, data=data)
    if not matches:
        return {"verdict":"POSSIBLE_GAP","query":query,"action":"RECOVER_MORE_BEFORE_INVENTING","matches":[]}
    top = matches[0]
    overlap_statuses = {"HEAVY_OVERLAP","MULTI_SURFACE_SAME_LINEAGE","EXISTS_IN_PARTS_AND_INTEGRATED_IN_FOUNDRY"}
    verdict = "OWNED_OVERLAP" if top.get("status") in overlap_statuses else "OWNED"
    return {"verdict":verdict,"query":query,"action":top.get("reuse"),"matches":matches}

def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description="Answer: what capability do we already own?")
    parser.add_argument("query", nargs="+")
    parser.add_argument("--map", dest="map_path", type=Path, default=DEFAULT_MAP)
    args = parser.parse_args()
    print(json.dumps(answer(" ".join(args.query), load_map(args.map_path)), indent=2))

if __name__ == "__main__":
    main()
