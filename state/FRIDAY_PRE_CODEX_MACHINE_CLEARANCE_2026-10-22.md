# FRIDAY pre-Codex machine clearance — 2026-10-22

> **2026-10-22/23 SUPPLEMENT:** The previously unproven *bounded* cross-repo Foundation integration has now passed a Harness-governed CI fixture at Foundry PR #35. See [exact verified receipt](FRIDAY_GOVERNED_INTEGRATION_PROOF_2026-10-22.md) and [Actions run 39879548240](https://github.com/Karmicmurphy/temporal-capability-foundry/actions/runs/39879548240). The general-purpose FRIDAY runtime, owner-intent execution path, durable dispatcher, and local machine integration **remain unproven**; candidate is unmerged. Historical "next proof" wording below is retained as a dated snapshot.

> **Evidence-backed recovery receipt, not a second source of authority.** The live state always comes from [CURRENT_PROJECT.json](CURRENT_PROJECT.json), [FRIDAY_MACHINE_STATUS.md](FRIDAY_MACHINE_STATUS.md), and [FRIDAY_OPERATOR_LAST_RUN.json](FRIDAY_OPERATOR_LAST_RUN.json), plus fresh GitHub/provider evidence. This file is a dated snapshot, not a command to promote refs, turn on services, or reactivate old gates.

## Codex first-session readiness audit (2026-10-22 local / 2026-10-23 UTC)

**Decision: SAFE for READ-ONLY / DISPOSABLE candidate verification. NOT approved for bulk merges, canonical repins, live dispatch or autonomous operation.** GitHub source and CI were checked; the owner's actual Codex cloud environment, connected private-repository permissions, session history, subscription/usage, and local Windows/host availability **cannot be verified from the available GitHub connection**.

- **First source of truth:** [Harness Card main/current project](https://github.com/Karmicmurphy/Harness-card/blob/main/state/CURRENT_PROJECT.json), `AGENTS.md`, `OPERATING_CONTRACT.md`, current machine status/receipt, plus [governed proof](FRIDAY_GOVERNED_INTEGRATION_PROOF_2026-10-22.md). Do not use old Codex chat prompts, historic laptop paths or unmerged candidates as authority.
- **Codex handoff repaired:** [Untethered AIOS PR #2](https://github.com/Karmicmurphy/Untethered-AIOS/pull/2), merged at `824048c2cef65225d9a6d56eac7847da3e6a662e`, replaces old active Windows-first `CODEX_START_HERE.md`. CI passed [all four Windows/Linux tests](https://github.com/Karmicmurphy/Untethered-AIOS/actions/runs/39884651404). The actual executable AIOS kernel at approved `8a954439af2b15b00f7c961d83552772b382fd1f` was not modified by these two newer documentation/regression commits.
- **Working implementation scope for a later Codex session:** private `Karmicmurphy/temporal-capability-foundry`, base `software-builder-v0` at `319c4945c6b9bb180385cdf0935633e2f1915d61`. Open [draft PR #35](https://github.com/Karmicmurphy/temporal-capability-foundry/pull/35), candidate head `8d85c6af6f36f10964dbf9298ffafc0d1e9a3a5e`; **both integration proof and full unit CI green**, no merge. Compare [unmerged PR #34](https://github.com/Karmicmurphy/temporal-capability-foundry/pull/34) and [#31](https://github.com/Karmicmurphy/temporal-capability-foundry/pull/31) read-only. Do **not** mistakenly start in the Foundry `main` branch, which diverges substantially from the builder branch. Do not merge Foundry PR #21 wholesale.
- **First Codex task:** confirm repository and exact branch/commit, inspect Harness-approved vs observed refs, reproduce/independently inspect existing passing receipts, assess PR #35 limitations and #31/#34 minimal reusable scope, and return ONE smallest test-only candidate step. Stop before new changes unless subsequently scoped. This is a reconnaissance / risk audit, not an order for advanced unbounded implementation.
- **Access gate:** GitHub access in this Chat does **not** prove a Codex Cloud environment can read private Foundry. Confirm the environment is created/published and the intended GitHub account grants this repo. If unavailable, Codex should report `BLOCKED_BY_CODEX_ENVIRONMENT_OR_GITHUB_ACCESS` without asking for secrets in chat or rewriting the machine.
- **Parked:** Android-to-FRIDAY and Cloudflare Preview integration. Using Codex from a phone or cloud browser is a separate access workflow, not permission to reactivate either implementation.
- **Owner approval still needed only for:** extra GitHub scopes; secrets/identity; protected production changes; new paid usage; consequential real-world dispatch; destructive changes; or uncertain canonical authority promotion. Read-only audits and bounded tests on isolated workspaces may proceed under existing Harness policy.

**Do not call Codex READY_FOR_AUTONOMOUS_EXECUTION from this receipt.** Entry and review readiness are proven in source/CI, but user-specific Codex availability and end-to-end autonomous runtime remain UNKNOWN/UNPROVEN.

## Owner outcome and scope

Clear avoidable GitHub/repository, continuity, discovery, salvage, test-reporting and Codex-entry mess **before** delegation. Keep **Android-to-FRIDAY/phone work and Cloudflare Pages Preview integration** parked. Local-only/private Workshop state remains UNKNOWN; do not recover it from a historical path. No new warehouse, framework, scheduler, provider, paid API, permission grant or live dispatch.

## Verified repairs already merged

| Repository | Change | Evidence |
|---|---|---|
| Harness-card | Correct expected UNKNOWN/drift monitoring findings without suppressing malformed reports; retain observer receipts | [PR #40](https://github.com/Karmicmurphy/Harness-card/pull/40), [observer CI](https://github.com/Karmicmurphy/Harness-card/actions/runs/39862496340) |
| Harness-card | Preserve repeated monitoring error as sanitized incident/learning | [PR #41](https://github.com/Karmicmurphy/Harness-card/pull/41), [learning run](https://github.com/Karmicmurphy/Harness-card/actions/runs/39862948450) |
| Harness-card | Keep Night Shift valid observation states from being mislabeled failed executions | [PR #42](https://github.com/Karmicmurphy/Harness-card/pull/42), [spine CI](https://github.com/Karmicmurphy/Harness-card/actions/runs/39872789403) |
| Harness-card | Remove already-proven first-operator-run blocker; synchronize canonical work order and generated projections | [PR #43](https://github.com/Karmicmurphy/Harness-card/pull/43), [guard](https://github.com/Karmicmurphy/Harness-card/actions/runs/39873049502) |
| Harness-card | Repair generated-status commit collisions by revalidating on current main and rejecting unexpected intervening source changes | [PR #44](https://github.com/Karmicmurphy/Harness-card/pull/44), [main-branch spine](https://github.com/Karmicmurphy/Harness-card/actions/runs/39873723953) |
| Harness-card | Fix ROUTING.md hard-coded retired Pages gate; enforce live canonical selection with regression | [PR #45](https://github.com/Karmicmurphy/Harness-card/pull/45), [guard](https://github.com/Karmicmurphy/Harness-card/actions/runs/39875265068) |
| Untethered-AIOS | Replace wrong create-a-new-repo / mandatory Windows-first bootstrap entry with existing five-repo, cloud-first, canonical Harness pointers | [PR #1](https://github.com/Karmicmurphy/Untethered-AIOS/pull/1), [four-platform green CI](https://github.com/Karmicmurphy/Untethered-AIOS/actions/runs/39875305672) |

## Source and approved-versus-observed reconciliation

All entries below were queried from GitHub on October 22. **Branches may move. Re-read them before any action.** These are observations, not new authority pins.

| Role | Canonical branch | Approved commit | Observed branch head | Comparison | Classification |
|---|---|---|---|---|---|
| Governance | `Harness-card/main` | moving governance branch; no SHA pin | live head via GitHub | authority guard passed | KEEP |
| Factory | `temporal-capability-foundry/software-builder-v0` | `e0e14e689b1d3a3bda1356276975b4b34f1b615e` | `319c4945c6b9bb180385cdf0935633e2f1915d61` | +4 commits; fixed phone correlation and candidate workflow changes | REVIEW (not promote) |
| Runtime | `Untethered-AIOS/main` | `8a954439af2b15b00f7c961d83552772b382fd1f` | `df26e5ee0770b629a4b68a2a0c6af0896b5a03c3` | +1 commit, **README.md and docs/CODEX_HANDOFF.md only** | KEEP prior runtime pin; note documentation-only divergence |
| Warehouse | `digital-scrapyard-autopilot/main` | `a059a27ef2bd662827a51da44dd8efb8863d634c` | `a904f29213b5a5bcf1b39f1392bca740c46a6093` | +1 commit, separate CSS-guide intake record only | REVIEW/DEFER |
| Cockpit | `Ollie_Twis_Holo_workshop/living-workshop-main-build` | `1785ed1405e769a17ec22066dc1e27a40dbf153b` | `9822e988dd125f55b13be3891eb0a39975a26191` | +3 commits, music rig/UI/Pages workflow; already triaged by bounded operator | REVIEW/DEFER |

No approved SHA was repinned. **Observed ahead is not equivalent to reviewed/approved.** AIOS has a newly documented main head, but the executable kernel at the previously approved commit was unchanged by this documentation-only PR.

## Test and execution evidence

- **FRIDAY bounded operator:** [main-branch run 39873723953](https://github.com/Karmicmurphy/Harness-card/actions/runs/39873723953) passed and persisted a receipt; it inspected Workshop divergence, not a general autonomous model or live external job. Read the latest operator JSON before relying on this dated run.
- **Foundry:** [workflow 37027102094, attempt 2](https://github.com/Karmicmurphy/temporal-capability-foundry/actions/runs/37027102094) rerun on 2026-10-22, **success**, checked head `319c4945c6b9bb180385cdf0935633e2f1915d61`.
- **Digital Scrapyard:** [workflow 36491300167, attempt 2](https://github.com/Karmicmurphy/digital-scrapyard-autopilot/actions/runs/36491300167) rerun on 2026-10-22, **success**, checked head `a904f29213b5a5bcf1b39f1392bca740c46a6093`.
- **AIOS:** [workflow 39875305672](https://github.com/Karmicmurphy/Untethered-AIOS/actions/runs/39875305672) passed all four combinations of Windows/Ubuntu and Python 3.10/3.12 on the documented successor; these are GitHub tests/demos, not user's physical machine proof.
- Workshop Preview is not retested as part of this pre-Codex scope; earlier provider metadata and blocked bindings remain historical and **parked**.

## Artifact Compass / Salvage / Rights Gate pass

Reuse these existing mechanisms (no code copied or dependencies installed):

| Mechanism | Canonical evidence / source path | Stack location and decision |
|---|---|---|
| Authority, bounded decision, receipts, recovery and closeout | `Harness-card/AGENTS.md`, `OPERATING_CONTRACT.md`, `ROUTING.md`, `scripts/friday_operator.py`, `state/ESTATE_CAPABILITY_MAP_V1.json` | Governance — **KEEP**; do not add a second operating harness |
| Ten-pass discovery, mechanism extraction, reality/rights/cost checks | `Untethered-AIOS/skills/artifact-compass/SKILL.md`, `skills/deep-salvage/SKILL.md` | Discovery/decision — **KEEP** as scoped skills, not a search marathon |
| Rights Gate, Proof Gate, Recombination Forge, Project Context Harvester, Salvage Suite and adaptive pass rule | `digital-scrapyard-autopilot/skills/salvage-suite/` | Salvage/rights/proof — **KEEP/REUSE** methods only; preserve source/rights limits |
| Inventory, provenance, hash-based recovered source receipts | `digital-scrapyard-autopilot/warehouse/intake/personal-jarvis-2026-09-21/warehouse_manifest.json`, `SALVAGE_MAP.md`, `PROVENANCE.md`, `SOURCE_FILE_INDEX.md` | Existing warehouse — **KEEP** with no duplicate repository or wholesale Jarvis import |
| Typed source identity, job compilation, evaluation and non-destructive learning | `temporal-capability-foundry/registry/`, `state/SALVAGE_INTAKE_V1_RECEIPT.md` and proven Foundry tests | Factory — **KEEP**; integrate only behind present authority/proof contracts |

**Salvage decision:** no third-party library or full agent system passes the cost/necessity gate for this cleanup. No new paid model, local-service deployment, huge framework, new database, rehomed warehouse or unlicensed code reuse. Follow established `KEEP / CUT / TEST / REJECT / DEFER` disposition.

## Candidate pull requests: avoid accidental mass merges

- [Foundry #34](https://github.com/Karmicmurphy/temporal-capability-foundry/pull/34) — **TEST**: deterministic FRIDAY native/startup candidate; focused tests and PR CI passed, but host, general language execution and local/private Workshop integration are unproven. Inspect its diff/permissions/test coverage before selecting the smallest reusable slice. Do not claim or merge a live local service.
- [Foundry #31](https://github.com/Karmicmurphy/temporal-capability-foundry/pull/31) — **TEST/REVIEW**: older trusted coding engine candidate with green past CI, based on older branch state; requires rebase/reproof, not a blind merge.
- [Foundry #23](https://github.com/Karmicmurphy/temporal-capability-foundry/pull/23) — **QUARANTINE**: old Estate Librarian candidate; one unit CI passed but its dedicated proof workflow failed. Existing estate/warehouse maps already cover discovery; do not merge another librarian without a concrete unmet proof.
- [Harness #25](https://github.com/Karmicmurphy/Harness-card/pull/25) — **REVIEW/DEFER**: historical owner-language PR; some goals now live in the Harness and routing. Its old base is not a reason to promote it.
- [Workshop #26](https://github.com/Karmicmurphy/Ollie_Twis_Holo_workshop/pull/26) — **DEFER**: authenticated Pages/phone path; explicitly parked.
- [Scrapyard #19](https://github.com/Karmicmurphy/digital-scrapyard-autopilot/pull/19) — **DEFER**: separate payment/business repair candidate, not Foundation's current machine problem.

## Known limits (not secretly fixed)

1. Two private repo refs remain `UNKNOWN` to the narrow GitHub Actions read token. The broader connected GitHub read independently found the repos and branch diffs; the nightly runner permission has **not** been broadened.
2. Cloudflare observer read credentials and protected Preview bindings remain unconfigured for the parked provider lane. **Do not** copy Production secrets or resurface this as the main priority.
3. The local Windows Workshop is unavailable for fresh proof; do not claim to have run it.
4. General free-form FRIDAY runtime / live local machine integration remains **NOT PROVEN**. Tests, operator receipts and successful GitHub jobs are bounded evidence only.
5. Candidate PRs and historic estate maps do not override the current Harness authority, and newer branch heads are not approved merely because their tests pass.

## Next bounded machine move / Codex handoff

**Do not start with cloud dashboards, phone activation or a replacement architecture.** Begin in the existing `Harness-card` governed workflow, then inspect `Untethered-AIOS` and the Foundry candidates. Read `state/CURRENT_PROJECT.json`, the generated active work order, latest FRIDAY operator receipt and the existing skills above. Confirm head SHAs and test outcomes afresh.

**The one unresolved engineering proof:** can an existing governed FRIDAY operator consume one permitted job, select/reuse the current Foundry/AIOS machinery, exercise it in a disposable credential-free checkout, independently verify a correlated receipt, and safely stop **without** needing the Windows host, phone or Cloudflare? Use #34/#31 as *unmerged evidence*, not mandatory dependencies. Produce a candidate branch, negative-path tests (bad authorization, changed SHA, missing receipt, unexpected write), and an exact evidence receipt. If these tools require an unavailable real-host boundary, report **BLOCKED**; don't invent proof or ask the owner to reconfigure unrelated systems.

**Stop:** one green bounded proof plus explicit no-production/no-owner-exception attestations, or the first exact technical/authority blocker. Merge or promote only after normal Harness scope and review gates. This handoff is a useful map, not itself proof of an autonomous FRIDAY.
