param(
    [Parameter(Position = 0)]
    [ValidateSet('status','preflight','recover-codex','recover-remote')]
    [string]$Action = 'status',

    [string]$ConfigPath = ''
)

$ErrorActionPreference = 'Stop'

function Write-Json($value) {
    $value | ConvertTo-Json -Depth 8
}

function Get-OptionalConfig {
    param([string]$Path)
    if ([string]::IsNullOrWhiteSpace($Path)) { return $null }
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw "CONFIG_NOT_FOUND: $Path"
    }
    $raw = Get-Content -LiteralPath $Path -Raw
    if ([string]::IsNullOrWhiteSpace($raw)) {
        throw "CONFIG_EMPTY: $Path"
    }
    return $raw | ConvertFrom-Json
}

function Test-Command([string]$Name) {
    return [bool](Get-Command $Name -ErrorAction SilentlyContinue)
}

function Get-ServiceState([string]$Name) {
    try {
        $svc = Get-Service -Name $Name -ErrorAction Stop
        return [ordered]@{
            installed = $true
            status = [string]$svc.Status
            start_type = try { (Get-CimInstance Win32_Service -Filter "Name='$Name'").StartMode } catch { 'UNKNOWN' }
        }
    }
    catch {
        return [ordered]@{ installed = $false; status = 'NOT_INSTALLED'; start_type = 'UNKNOWN' }
    }
}

function Get-CodexProcesses {
    $names = @('Codex','codex')
    $items = @()
    foreach ($name in $names) {
        try {
            $items += Get-Process -Name $name -ErrorAction Stop | ForEach-Object {
                [ordered]@{ name = $_.ProcessName; id = $_.Id; responding = $_.Responding }
            }
        } catch {}
    }
    return @($items | Sort-Object id -Unique)
}

function Test-CodexRemoteControlCapability {
    if (-not (Test-Command 'codex')) {
        return [ordered]@{ available = $false; reason = 'CODEX_CLI_NOT_FOUND' }
    }
    try {
        $output = & codex remote-control --help 2>&1 | Out-String
        $hasStart = $output -match '(?im)^\s*start\b|\bstart\b'
        return [ordered]@{
            available = [bool]$hasStart
            reason = if ($hasStart) { 'REMOTE_CONTROL_START_ADVERTISED' } else { 'REMOTE_CONTROL_START_NOT_ADVERTISED' }
        }
    }
    catch {
        return [ordered]@{ available = $false; reason = 'REMOTE_CONTROL_HELP_FAILED' }
    }
}

function Get-Preflight {
    $tailscale = if (Test-Command 'tailscale') {
        [ordered]@{ installed = $true; command = (Get-Command tailscale).Source }
    } else { [ordered]@{ installed = $false; command = $null } }

    $cloudflared = if (Test-Command 'cloudflared') {
        [ordered]@{ installed = $true; command = (Get-Command cloudflared).Source }
    } else { [ordered]@{ installed = $false; command = $null } }

    $codexCli = if (Test-Command 'codex') {
        [ordered]@{ installed = $true; command = (Get-Command codex).Source }
    } else { [ordered]@{ installed = $false; command = $null } }

    return [ordered]@{
        computer = $env:COMPUTERNAME
        user = $env:USERNAME
        openssh_sshd = Get-ServiceState 'sshd'
        tailscale = $tailscale
        tailscale_service = Get-ServiceState 'Tailscale'
        cloudflared = $cloudflared
        cloudflared_service = Get-ServiceState 'cloudflared'
        codex_cli = $codexCli
        codex_processes = @(Get-CodexProcesses)
        codex_remote_control = Get-CodexRemoteControlCapability
        public_port_changes_performed = $false
        foundation_execution_performed = $false
    }
}

function Resolve-CodexExecutable($config) {
    if ($config -and $config.CodexExecutable) {
        $candidate = [Environment]::ExpandEnvironmentVariables([string]$config.CodexExecutable)
        if (Test-Path -LiteralPath $candidate -PathType Leaf) {
            return $candidate
        }
        throw "CONFIGURED_CODEX_EXECUTABLE_NOT_FOUND: $candidate"
    }

    $known = @(
        "$env:LOCALAPPDATA\Programs\Codex\Codex.exe",
        "$env:LOCALAPPDATA\Codex\Codex.exe"
    )
    foreach ($candidate in $known) {
        if (Test-Path -LiteralPath $candidate -PathType Leaf) { return $candidate }
    }

    return $null
}

$config = Get-OptionalConfig -Path $ConfigPath

switch ($Action) {
    'preflight' {
        Write-Json ([ordered]@{ action='preflight'; verdict='READ_ONLY'; evidence=(Get-Preflight) })
        exit 0
    }

    'status' {
        $preflight = Get-Preflight
        $codexRunning = @($preflight.codex_processes).Count -gt 0
        Write-Json ([ordered]@{
            action = 'status'
            codex_running = $codexRunning
            codex_processes = $preflight.codex_processes
            remote_control_capability = $preflight.codex_remote_control
            sshd = $preflight.openssh_sshd
            tailscale = $preflight.tailscale
            tailscale_service = $preflight.tailscale_service
            cloudflared = $preflight.cloudflared
            cloudflared_service = $preflight.cloudflared_service
            changes_performed = $false
            foundation_execution_performed = $false
        })
        exit 0
    }

    'recover-codex' {
        $running = @(Get-CodexProcesses)
        if ($running.Count -gt 0) {
            Write-Json ([ordered]@{
                action='recover-codex'; verdict='NO_ACTION_HEALTHY'; codex_processes=$running; changes_performed=$false
            })
            exit 0
        }

        $exe = Resolve-CodexExecutable $config
        if (-not $exe) {
            Write-Json ([ordered]@{
                action='recover-codex'; verdict='BLOCKED'; blocker='CODEX_EXECUTABLE_NOT_VERIFIED'; changes_performed=$false
            })
            exit 2
        }

        $args = @()
        if ($config -and $config.CodexArguments) { $args = @($config.CodexArguments) }
        Start-Process -FilePath $exe -ArgumentList $args
        Start-Sleep -Seconds 3
        $after = @(Get-CodexProcesses)
        $ok = $after.Count -gt 0
        Write-Json ([ordered]@{
            action='recover-codex'; verdict= if ($ok) {'STARTED'} else {'START_ATTEMPT_UNPROVEN'}; executable=$exe; codex_processes=$after; force_kill_used=$false; foundation_execution_performed=$false
        })
        if ($ok) { exit 0 } else { exit 3 }
    }

    'recover-remote' {
        $capability = Get-CodexRemoteControlCapability
        if (-not $capability.available) {
            Write-Json ([ordered]@{
                action='recover-remote'; verdict='BLOCKED'; blocker=$capability.reason; changes_performed=$false
            })
            exit 2
        }

        $output = & codex remote-control start 2>&1 | Out-String
        $exitCode = $LASTEXITCODE
        Write-Json ([ordered]@{
            action='recover-remote'; verdict= if ($exitCode -eq 0) {'START_COMMAND_SUCCEEDED'} else {'START_COMMAND_FAILED'}; exit_code=$exitCode; output=$output.Trim(); force_kill_used=$false; foundation_execution_performed=$false
        })
        exit $exitCode
    }
}
