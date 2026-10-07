# FRIDAY Host Recovery V0 — Candidate

Status: CANDIDATE / NOT ACTIVE

This folder contains a minimal Windows host-recovery kit for the failure class:

`phone -> Codex Remote -> Codex restarts -> owner loses the only remote doorway`

It is intentionally separate from Foundation authority and execution. It does not run Foundation jobs, mutate Harness authority, expose public ports, or assume a particular remote-access provider is installed.

## Design

The recovery plane must survive independently of the work plane.

- Work plane: Codex -> FRIDAY -> Foundation / AIOS / Independent Proof
- Management plane: Windows + private recovery channel(s) -> host-recovery script

Preferred recovery channels are provider-independent at the script layer. The preflight reports whether Windows OpenSSH, Tailscale, and cloudflared are present; deployment of any provider remains an explicit host-side action.

## Commands

Run from PowerShell:

```powershell
.\friday-host-recovery.ps1 status
.\friday-host-recovery.ps1 preflight
.\friday-host-recovery.ps1 recover-codex
.\friday-host-recovery.ps1 recover-remote
```

`recover-codex` is fail-closed unless a verified Codex executable is configured or safely discovered.

`recover-remote` is fail-closed unless the installed `codex` CLI proves that the `remote-control start` subcommand exists.

No force-kill path exists in V0.

## Optional config

Copy `host-recovery.config.example.json` to a local private path and fill only verified values. Do not commit machine-specific secrets or credentials.

The script accepts:

```powershell
-ConfigPath "C:\Users\<user>\Documents\Codex\host-recovery.config.json"
```

## Proof ladder

Do not call this recovery path PROVEN until all applicable gates pass on the actual Windows host:

1. `preflight` reports current services/tools honestly.
2. `status` can distinguish healthy/missing Codex and remote-control state without changing anything.
3. At least one independent private remote channel reaches the laptop while Codex is stopped.
4. `recover-codex` relaunches Codex without force-kill.
5. `recover-remote` restores Codex Remote only when the CLI capability is present.
6. Codex rediscovers `friday-owner-node`.
7. `friday_status` returns the previously recovered trusted state.
8. No Harness authority, Foundation execution, Cloudflare production, or PR #32/#33 state changes.

## Explicit non-goals

- no public SSH exposure;
- no custom privileged HTTP restart endpoint;
- no GitHub self-hosted runner command channel;
- no new orchestrator;
- no automatic Foundation work;
- no credentials in the repository;
- no claim that FRIDAY itself is a durable Windows service yet.

The current FRIDAY MCP gateway is stdio-oriented. Making FRIDAY independently persistent requires a separately reviewed lifecycle adapter; this candidate does not fake that proof.