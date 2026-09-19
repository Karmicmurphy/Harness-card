# Skill Sources

Harness Card routes skills; it should not silently fork or duplicate them.

## Current canonical source

Primary reusable skill suite currently lives in:

`Karmicmurphy/digital-scrapyard-autopilot/skills/salvage-suite/`

Known reusable skills include:
- intent-recovery-compass
- rabbit-hole-governor
- project-context-harvester
- project-closeout-gate
- artifact-compass
- artifact-salvage
- deep-sea-salvage
- rights-gate
- cost-complexity-challenge
- recombination-forge
- thought-economy
- proof-gate
- owner-interruption-minimizer
- capability-downshift
- market-want-board
- scrap-built-tiny-house-salvage

## Harness-local canonical skills

These skills are canonical in Harness Card because they define harness behavior rather than project/product behavior:

- `chat-software-harness`
  - canonical path: `skills/chat-software-harness/SKILL.md`
  - purpose: make ordinary interactive Chat the default software command center; orchestrate authority recovery, salvage-first execution, proof, state writeback, and bounded delegation
  - source policy: do not duplicate Artifact Compass, Artifact Salvage, Proof Gate, or other canonical salvage-suite skills inside it; route to them

## Source-of-truth rule

Before copying any skill into Harness Card:
1. verify the current canonical file and version;
2. decide whether Harness Card should reference it, vendor a pinned copy, or replace it with a better standard form;
3. never maintain two unlabeled competing canonical copies;
4. if vendored later, record source repo/path/SHA and update policy.

## Automatic routing

See root `ROUTING.md`.

## Future standardization

Portable skill packaging may later be added under `skills/` when it improves interoperability with Codex, ChatGPT, AIOS, MCP-aware agents, or other runtimes. Do not migrate merely for fashion; migrate when the new packaging produces a tested continuity or execution benefit.
