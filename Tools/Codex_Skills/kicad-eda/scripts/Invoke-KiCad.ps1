[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [ValidateSet('doctor', 'erc', 'drc', 'bom', 'schematic-pdf', 'gerbers', 'drill', 'positions', 'step', 'release')]
    [string]$Action,

    [Parameter(Position = 1)]
    [string]$InputFile,

    [string]$SchematicFile,
    [string]$BoardFile,
    [string]$OutputDirectory = 'build\kicad'
)

$ErrorActionPreference = 'Stop'

function Find-KiCadCli {
    if ($env:KICAD_CLI -and (Test-Path -LiteralPath $env:KICAD_CLI)) {
        return (Resolve-Path -LiteralPath $env:KICAD_CLI).Path
    }

    $command = Get-Command kicad-cli -ErrorAction SilentlyContinue
    if ($command) { return $command.Source }

    $candidates = Get-ChildItem -Path 'C:\Program Files\KiCad\*\bin\kicad-cli.exe' -ErrorAction SilentlyContinue |
        Sort-Object { [version]$_.Directory.Parent.Name } -Descending
    if ($candidates) { return $candidates[0].FullName }

    throw 'kicad-cli was not found. Install KiCad or set KICAD_CLI to its full path.'
}

function Resolve-Input([string]$Path, [string]$Extension) {
    if (-not $Path) { throw "An input $Extension file is required for action '$Action'." }
    $resolved = (Resolve-Path -LiteralPath $Path).Path
    if ([IO.Path]::GetExtension($resolved) -ne $Extension) {
        throw "Expected a $Extension file, received '$resolved'."
    }
    return $resolved
}

function Invoke-Cli([string[]]$Arguments) {
    & $script:KiCadCli @Arguments
    $code = $LASTEXITCODE
    if ($code -ne 0) { throw "kicad-cli exited with code $code." }
}

$script:KiCadCli = Find-KiCadCli
$versionText = (& $script:KiCadCli version 2>$null).Trim()
if (-not $versionText) { throw 'Unable to determine the KiCad version.' }
$major = [int]($versionText.Split('.')[0])
if ($major -lt 10) { throw "KiCad 10 or newer is required; found $versionText." }

if ($Action -eq 'doctor') {
    [pscustomobject]@{
        KiCadCli = $script:KiCadCli
        Version = $versionText
        Symbols = Test-Path -LiteralPath "C:\Program Files\KiCad\${major}.0\share\kicad\symbols"
        Footprints = Test-Path -LiteralPath "C:\Program Files\KiCad\${major}.0\share\kicad\footprints"
        Models3D = Test-Path -LiteralPath "C:\Program Files\KiCad\${major}.0\share\kicad\3dmodels"
        ApiEnabled = if ($major -eq 10) {
            $cfg = Join-Path $env:APPDATA 'kicad\10.0\kicad_common.json'
            if (Test-Path -LiteralPath $cfg) {
                (Get-Content -Raw -LiteralPath $cfg | ConvertFrom-Json).api.enable_server
            } else { $false }
        } else { $null }
    } | ConvertTo-Json
    exit 0
}

$out = if ([IO.Path]::IsPathRooted($OutputDirectory)) {
    [IO.Path]::GetFullPath($OutputDirectory)
} else {
    [IO.Path]::GetFullPath((Join-Path (Get-Location) $OutputDirectory))
}
New-Item -ItemType Directory -Force -Path $out | Out-Null

switch ($Action) {
    'erc' {
        $sch = Resolve-Input $InputFile '.kicad_sch'
        Invoke-Cli @('sch', 'erc', '--format', 'json', '--severity-all', '--exit-code-violations', '--output', (Join-Path $out 'erc.json'), $sch)
    }
    'drc' {
        $pcb = Resolve-Input $InputFile '.kicad_pcb'
        Invoke-Cli @('pcb', 'drc', '--format', 'json', '--severity-all', '--schematic-parity', '--exit-code-violations', '--output', (Join-Path $out 'drc.json'), $pcb)
    }
    'bom' {
        $sch = Resolve-Input $InputFile '.kicad_sch'
        Invoke-Cli @('sch', 'export', 'bom', '--exclude-dnp', '--fields', 'Reference,Value,Footprint,Manufacturer,MPN,QUANTITY,DNP', '--labels', 'References,Value,Footprint,Manufacturer,MPN,Quantity,DNP', '--group-by', 'Value,Footprint,Manufacturer,MPN', '--output', (Join-Path $out 'bom.csv'), $sch)
    }
    'schematic-pdf' {
        $sch = Resolve-Input $InputFile '.kicad_sch'
        Invoke-Cli @('sch', 'export', 'pdf', '--black-and-white', '--output', (Join-Path $out 'schematic.pdf'), $sch)
    }
    'gerbers' {
        $pcb = Resolve-Input $InputFile '.kicad_pcb'
        $gerberOut = Join-Path $out 'gerbers'
        New-Item -ItemType Directory -Force -Path $gerberOut | Out-Null
        Invoke-Cli @('pcb', 'export', 'gerbers', '--board-plot-params', '--check-zones', '--output', $gerberOut, $pcb)
    }
    'drill' {
        $pcb = Resolve-Input $InputFile '.kicad_pcb'
        $drillOut = Join-Path $out 'drill'
        New-Item -ItemType Directory -Force -Path $drillOut | Out-Null
        Invoke-Cli @('pcb', 'export', 'drill', '--format', 'excellon', '--excellon-units', 'mm', '--excellon-separate-th', '--generate-map', '--map-format', 'pdf', '--generate-report', '--report-path', (Join-Path $drillOut 'drill-report.txt'), '--output', $drillOut, $pcb)
    }
    'positions' {
        $pcb = Resolve-Input $InputFile '.kicad_pcb'
        Invoke-Cli @('pcb', 'export', 'pos', '--format', 'csv', '--units', 'mm', '--side', 'both', '--exclude-dnp', '--output', (Join-Path $out 'positions.csv'), $pcb)
    }
    'step' {
        $pcb = Resolve-Input $InputFile '.kicad_pcb'
        Invoke-Cli @('pcb', 'export', 'step', '--force', '--no-dnp', '--subst-models', '--output', (Join-Path $out 'board.step'), $pcb)
    }
    'release' {
        $sch = Resolve-Input $SchematicFile '.kicad_sch'
        $pcb = Resolve-Input $BoardFile '.kicad_pcb'
        $scriptPath = $MyInvocation.MyCommand.Path
        foreach ($item in @(@('erc', $sch), @('drc', $pcb), @('bom', $sch), @('schematic-pdf', $sch), @('gerbers', $pcb), @('drill', $pcb), @('positions', $pcb), @('step', $pcb))) {
            & $scriptPath $item[0] $item[1] -OutputDirectory $out
            if ($LASTEXITCODE -ne 0) { throw "Release stopped during $($item[0])." }
        }
        $files = Get-ChildItem -LiteralPath $out -File -Recurse | Sort-Object FullName
        $manifest = [ordered]@{
            generatedAtUtc = (Get-Date).ToUniversalTime().ToString('o')
            kicadVersion = $versionText
            schematic = $sch
            board = $pcb
            files = @($files | ForEach-Object {
                [ordered]@{
                    path = [IO.Path]::GetRelativePath($out, $_.FullName)
                    bytes = $_.Length
                    sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName).Hash.ToLowerInvariant()
                }
            })
        }
        $manifest | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $out 'manifest.json') -Encoding utf8
    }
}

Write-Host "Completed '$Action' with KiCad $versionText. Output: $out"
