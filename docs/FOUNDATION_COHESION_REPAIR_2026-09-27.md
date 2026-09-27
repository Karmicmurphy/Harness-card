# Foundation cohesion repair — 2026-09-27

Bounded outcome: make the existing machine resumable without contradictory instructions.
Overall machine state: **PARTIALLY_PROVEN**. The phone round trip is not implemented/proven by this repair.

## Diagnosis

The components were not all missing. Their advancement was recorded on different surfaces, while old work orders kept sending subsequent sessions backwards. The prior guard compared JSON fields but checked only two Markdown headings. It could not detect a stale Windows-only task or an old instruction to rebuild Independent Proof.

On inspected Harness main `a15b9f8d377e0d616ffafc078cfc4213f714b309`, the existing guard actually failed: ecosystem factory SHA `cf51b485...` disagreed with canonical current-project SHA `e0e14e6...`. The canonical evidence field also contained a compound string outside its own configured enum. The active Markdown still listed missing correlation, while newer Foundry evidence already demonstrated it. The build prompt still directed agents into Cog 3. The work order combined runtime integration and local inventory into one stop condition.

This is a continuity and integration failure, not evidence that the engine should be replaced.

## Current components

| Component | Approved ref / SHA | Observed on 2026-09-27 | Meaning |
|---|---|---|---|
| Harness | main | a15b9f8d377e0d616ffafc078cfc4213f714b309 | Existing authority check fails before this repair |
| Foundry | software-builder-v0 / e0e14e689b1d3a3bda1356276975b4b34f1b615e | Same | Keep approved engine |
| AIOS | main / 8a954439af2b15b00f7c961d83552772b382fd1f | Same | Keep bounded runtime |
| Salvage | main / a059a27ef2bd662827a51da44dd8efb8863d634c | Same | Source recovery tooling, not another runtime |
| Workshop | living-workshop-main-build / 1785ed1405e769a17ec22066dc1e27a40dbf153b | 9822e988dd125f55b13be3891eb0a39975a26191 | Three later commits concern music and Pages publication; no automatic Foundation promotion |
| Foundry dispatcher | main | cc27cd6ee8e18326663b6f6b88c55a3426252dac | PR #30 already merged a narrow dispatcher pinned to approved Foundry; no full branch migration needed |

GitHub connector reads verified branch trees, default-branch workflow, PR metadata, run steps and logs. Plain shell access could not clone private Foundry. That access limitation is not evidence that the repository is absent or broken.

## Recovered working mechanism

Existing workflow: `.github/workflows/foundation-bounded-job.yml` on Foundry main.
Existing runner: `scripts/run_bounded_phone_foundation_job.py` at approved Foundry SHA.
Existing job: `aios-path-containment`, an isolated deterministic repair fixture.

Verified [run 36248023448](https://github.com/Karmicmurphy/temporal-capability-foundry/actions/runs/36248023448), job `108420731824`, emitted:

- `job:phone-36248023448-aios-path-containment`
- `CERTIFIED_AWAITING_HUMAN_REVIEW`
- Independent Proof verdict `CERTIFIED`
- correlated job identity `true`
- activation performed `false`
- scope `EXACT_PATCH_FIXTURE_ONLY`

The workflow checked out `e0e14e6...` and rejected an unknown fixture before execution. This was a PR-triggered remote fixture proof, not a phone request, arbitrary coding proof or deployed Workshop proof. Its receipt must not be relabeled as any of those.

Foundry PR #31 already holds a compiled coding-engine candidate. PR test run `36305666502` is successful. It remains open/unmerged; retain it for bounded review instead of rewriting it.

## Recommendation disposition

| Recommendation family | Decision and reason |
|---|---|
| One authoritative project and continuation | FIX NOW: CURRENT_PROJECT owns current work; derive work-order JSON, Markdown, current build prompt and ecosystem ref projection |
| Cross-file stale state checks | FIX NOW: compare full generated content, enum validity, exact refs, blockers and dates; add regressions |
| Observe cross-repo advancement | IMPLEMENT read-only branch/pin observer; emit drift or UNKNOWN, never auto-promote; daily workflow becomes active only after merge |
| Separate observed, approved and candidate refs | KEEP: existing approved refs retained; observations and open PRs are not authority |
| One execution identity and proof receipt | REUSE existing job_id and remote fixture runner; avoid another receipt/proof engine |
| Phone-first access | KEEP as target; existing Pages shell plus a narrow Pages Functions boundary |
| Separate Worker + D1 + new orchestration | DEFER: superseded by narrower Pages direction; no need to create infrastructure for state repair |
| Windows as mandatory always-on host | REMOVE as remote-path prerequisite; retain historical NOT_RUN field-trial truth and optional local/private role |
| Authenticate through Cloudflare Access | REQUIRED for live proof; HTTP 302 to Access verified, authenticated app unavailable here |
| Merge Workshop deploy PR #23 blindly | DO NOT: still open; deployment-specific delta must be reviewed against existing Pages setup |
| Natural-language coding | REVIEW existing Foundry PR #31 after bounded phone round trip; fixture proof is not general coding proof |
| Free compute cluster, quantum, model relay | PARK until one bounded user path returns a result |
| FRIDAY/PersonalJarvis revival | KEEP shelved; source availability does not reverse owner rejection |
| Broad estate re-inventory | PARK; use existing indexed evidence or a named source delta |
| CSV-to-Foundry bridge | PARK as separate source-intake work; prior local access blocker does not establish current connector failure |
| Spatial app primary map, three lenses, orientation completion, real typecheck | KEEP as separate product repairs; source working tree is unavailable here, so no invented implementation |
| Spatial useEffect/pattern badges/edge styling and scaffolding cleanup | VERIFY against preserved actual source before repair; old recommendations alone do not prove current defects |
| Spatial nested Git roots and deletion entries | PRESERVE first; transcript reports preservation and 416 recoverable committed blobs, not permission to restore or delete blindly |
| Off-device backup | REMAINS UNVERIFIED; historical same-disk preservation is not independent backup; do not copy private contents to public repositories |
| Local machine diagnostics/restart | Separate device task; cannot diagnose or change the owner's PC from this Linux checkout |

## What changed

`scripts/foundation_state.py` uses Python's standard library. `sync` regenerates derived files but never changes CURRENT_PROJECT or advances an approved SHA. `status` prints the single work order. `check` verifies projections. `observe` performs GitHub GET requests, checks the named branch and the pinned commit, and reports MATCH, RECONCILIATION_REQUIRED or UNKNOWN. It does not inspect deployments or infer live runtime health.

The original authority guard now validates these projections. The CI guard runs the new regression suite. A separate read-only scheduled/manual workflow preserves observations even on failure; it has no write permission. Private repos may require an existing cross-repo read token. Missing access is explicitly UNKNOWN, never a clean result. It does not create or rotate credentials.

Existing pins, candidate shelves, history and unrelated ecosystem entries are preserved. The compound evidence string is retained in `evidence_detail`, with the configured `PARTIALLY_PROVEN` enum used for current evidence. Spatial is explicitly separate. The resume prompt no longer sends the next session back to already-proven Cog 3.

## Evidence and limits

- Reproduced original authority failure before editing.
- Authority guard passes after synchronized state repair.
- 22 unit regressions pass, including stale Markdown/prompt, invalid enum, missing pin, missing projection, branch advancement, private-repo denial and no automatic promotion.
- Existing self-improvement regression is run in an isolated copy to avoid incidental generated-file changes.
- External Pages GET/HEAD boundary returns 302 to Cloudflare Access. Deployed source SHA, authenticated UI and cloud configuration remain unverified.
- No new deployment, source-yard scan, Windows action, model call, paid service, credential rotation, runtime promotion or live job dispatch is part of this repair.

## One next gate

`PAGES_BOUNDED_JOB_ROUND_TRIP` — owner authenticates in existing Workshop, starts the approved fixture, and receives the correlated Independent Proof receipt on the phone. The observed Pages branch currently has only the AI chat function, so dispatch and receipt routes remain missing code, not merely an account setting. Reload/status recovery, authentication denial, bounded input and duplicate-dispatch behavior must be proven before activation. Account configuration and live-device proof follow implementation; logging in alone will not complete the missing integration.

Resume from `state/ACTIVE_WORK_ORDER.md`. Do not turn this report into a second live work order.
