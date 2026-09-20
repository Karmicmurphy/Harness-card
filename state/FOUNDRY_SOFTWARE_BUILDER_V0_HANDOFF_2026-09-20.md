# Foundry Software Builder V0 — Resume Pointer

Date: 2026-09-20

Project authority remains in `Karmicmurphy/temporal-capability-foundry`.

Candidate branch: `software-builder-v0`

Draft PR: #21

Current durable authority:
- `state/SOFTWARE_BUILDER_V0_AUTHORITY.json`
- `state/SOFTWARE_BUILDER_V0_RECEIPT.md`

Real repository proof:
- `Karmicmurphy/digital-scrapyard-autopilot`
- branch `software-builder-v0-proof`
- draft PR #19
- final proof workflow run `35504537852`: PASS

Terminal state for V0:
**BLOCKED BY a callable capable coding-engine runtime that can be attached to the Software Builder process in the current execution environment.**

Do not redesign the worker.

Resume at:
1. recover Foundry authority file;
2. attach one real capable coding engine to the existing `SubprocessCodingEngine` or contract-compatible adapter;
3. run one bounded real-repository task through `SoftwareBuilder.run()` itself;
4. persist the worker-generated receipt into Foundry evidence/evaluation;
5. only then wire the smallest AIOS scheduler/capability adapter.
