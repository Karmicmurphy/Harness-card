# Capability Reconciliation — 2026-09-20

## Outcome

The estate already contains most core mechanisms repeatedly proposed as new architecture. The correct next layer is not another framework. It is an evidence-backed capability index plus a small invention gate that asks what is already owned before new architecture is proposed.

## Compared estates

- Temporal Capability Foundry: integrated intent -> typed job -> bounded execution -> evaluation -> learning candidate -> promotion -> activation/rollback lifecycle.
- Untethered AIOS: bounded execution, capability authority, budgets, finite recovery, deterministic rule/reflex work, receipt/trace/certificate lineage.
- Digital Scrapyard: canonical salvage/discovery/rights/proof/recombination skill source.
- Twis Holo Workshop: human-facing product/work surface and local/private interaction layer, not the global trust authority.
- CERT-RIVER / PRISM-RIVER / RiverKernel recovered lineage: prior proof, policy, certification, bounded execution, quarantine and receipt semantics. Historical lineage remains evidence, not current live repository authority.

## Classification

The strongest overlaps are proof/certification, routing/policy, bounded execution/recovery, salvage/discovery, and learning/promotion. These are classified as overlap families. Nothing was deleted or merged.

## Implemented

- `state/CAPABILITY_MAP.json` — machine-readable evidence map.
- `workers/capability_invention.py` — deterministic lookup returning `OWNED`, `OWNED_OVERLAP`, or `POSSIBLE_GAP`.
- `tests/test_capability_invention.py` — regression tests for execution overlap, Artifact Compass lineage, Software Builder continuation, and unknown-gap behavior.

## Boundary

This layer does not execute project work, certify claims, replace Foundry, replace AIOS, or merge repos. It is a pre-build invention gate that answers:

> What do we already own that we do not realize we own?

before creating another core mechanism.
