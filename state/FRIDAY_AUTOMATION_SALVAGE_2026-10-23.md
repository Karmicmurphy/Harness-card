# FRIDAY maintenance radar & Artifact Compass salvage — October 23, 2026

**Goal:** Give the existing scheduled FRIDAY operator a memory of investigated exact repository revisions, so she does not repeatedly compare the same source while neglecting other problems. This is an operating improvement, not a new autonomous coding service.

## What's operationally missing

The Harness daily operator normally selects the first remote `RECONCILIATION_REQUIRED` and repeats it on subsequent runs even when the same exact approved-vs-observed commit has already been safely inspected. The prior receipt retains only the last action, not a ranked, idempotent list of the four components. Private source access remains UNKNOWN in the narrow Actions context. No permission to promote refs follows from CI.

## Smallest mechanism salvaged from existing machine

- **KEEP:** The existing `FRIDAY_BOUNDED_OPERATOR_LOOP` scheduler, `scripts/friday_operator.py`, `foundation_state.py`, the Authority Spine Guard and sanitized self-improvement worker.
- **KEEP:** The existing AIOS [Artifact Compass](https://github.com/Karmicmurphy/Untethered-AIOS/blob/main/skills/artifact-compass/SKILL.md) and [Deep Salvage](https://github.com/Karmicmurphy/Untethered-AIOS/blob/main/skills/deep-salvage/SKILL.md), plus the authorized [Scrapyard salvage suite](https://github.com/Karmicmurphy/digital-scrapyard-autopilot/tree/main/skills/salvage-suite). Routes resolve through `config/skill_registry.json`, not by cloning an unreviewed framework.
- **TEST:** `scripts/friday_diagnostics.py` writes the SHA-scoped `state/FRIDAY_MAINTENANCE_QUEUE.json` as generated data. For each approved component: exact-ref `MATCH`, `UNKNOWN_READ_ACCESS`, `UNTRIAGED_READ_ONLY`, `READ_PROOF_FAILED` with a three-attempt limit, or `TRIAGED_REVIEW_REQUIRED` after an exact verified comparison. It never silently repins or merges.
- **TEST:** The next scheduled run selects the next untriaged revision; an already-reviewed exact source remains reviewed until the observed source changes. Compare failures are bounded rather than repeated forever. Authorized skill routes and proof gates accompany each result. The refreshed owner view displays pending/review/unknown counts.
- **DEFER:** Automatically rewriting arbitrary repo source; accepting general owner intent; deploying; modifying secrets; gaining private repo read scopes; installing models and new orchestration; the phone and Cloudflare Preview. These require separate scope, permission or execution proof.

## Reverse-engineering / static analysis candidates (research-only, no installation)

The aim is learning techniques for **your own legally held code, open-license repositories, or authorized binaries**. Reverse-engineering tools are not interchangeable with static checks for source code:

| Mechanism | Official source and rights | Stack role | Current decision |
|---|---|---|---|
| Static source pattern search and reusable guardrails | [Semgrep OSS](https://github.com/semgrep/semgrep), LGPL-2.1 (check exact engine/rules licences) | Candidate isolated source-quality scan | **TEST later** only if native Python tests and simple GitHub CI cannot detect the target bug; zero automatic remediation until proof |
| Open static-analysis alternative | [Opengrep](https://github.com/opengrep/opengrep), LGPL-2.1 | Alternative source scanner | **DEFER** until a concrete competing bug-detection bakeoff; do not run both by default |
| Binary reverse-engineering/disassembly | [Ghidra](https://github.com/NationalSecurityAgency/ghidra), Apache-2.0 plus contained component notices | Authorized binary analysis, *not* essential to source repair | **DEFER**; significant Java/resource burden and not relevant to the current Foundry→AIOS missing admission/recovery proof |
| CLI binary analysis and disassembly | [Rizin](https://github.com/rizinorg/rizin), LGPL/GPL component licences | Binary/executable investigation only | **DEFER**; review file-level licence on any future extraction |
| GitHub code scanning | [CodeQL CLI usage and repository eligibility](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-cli) | Optional source semantic/static analysis | **DEFER**; review private-repo licensing before proposing any execution |

These are findings, not adopted dependencies. No copied third-party code, untrusted binary execution, network-connected reverse-engineering service, recurring billing or extra workflow is authorized by this research.

## Proof checklist

1. Canonical authority and existing Harness tests pass on candidate.
2. One fresh exact ref is compared, receives an independently proven receipt, and becomes review-queued without promotion.
3. Next run cannot waste time on that **same** SHA, and proceeds to the next ref.
4. Changed observed SHA reopens exactly that role.
5. Missing/unknown private GitHub access stays UNKNOWN, and failed compare stops after three attempts with a durable record.
6. Malformed queue or forged comparison fails closed; history and generated owner status do not claim general autonomous code repair.
7. A real scheduled main-branch run writes queue and status before claiming operational behavior.

**Do not merge this card alone as proof of unattended repair.** It must be paired with its source PR regression checks and a main-branch run. Phone/Preview remain parked.
