[CmdletBinding()]
param(
    [string]$KiCadRoot = 'C:\Program Files\KiCad\10.0'
)

$ErrorActionPreference = 'Stop'
$skillRoot = Split-Path -Parent $PSScriptRoot
$scripts = Join-Path $skillRoot 'scripts'
$fixtures = Join-Path $PSScriptRoot 'fixtures'
$python = Join-Path $KiCadRoot 'bin\python.exe'
$cli = Join-Path $KiCadRoot 'bin\kicad-cli.exe'
$footprints = Join-Path $KiCadRoot 'share\kicad\footprints'
foreach ($path in @($python, $cli, $footprints)) {
    if (-not (Test-Path -LiteralPath $path)) { throw "Required KiCad path not found: $path" }
}

$tempRoot = Join-Path ([IO.Path]::GetTempPath()) ("kicad-eda-regression-" + [guid]::NewGuid())
New-Item -ItemType Directory -Path $tempRoot | Out-Null
try {
    $sch = Join-Path $tempRoot 'clone.kicad_sch'
    & $python (Join-Path $scripts 'Build-KiCadSchematic.py') (Join-Path $fixtures 'empty-native.kicad_sch') $sch --project-name regression --title 'Generated regression fixture' --kicad-cli $cli
    if ($LASTEXITCODE -ne 0) { throw 'Native schematic scaffold test failed.' }

    $pcb = Join-Path $tempRoot 'routed.kicad_pcb'
    & $python (Join-Path $scripts 'Build-KiCadPcb.py') (Join-Path $fixtures 'routed-board.json') $pcb --footprint-root $footprints
    if ($LASTEXITCODE -ne 0) { throw 'PCB generation test failed.' }
    & $cli pcb drc --format json --severity-all --exit-code-violations --output (Join-Path $tempRoot 'drc.json') $pcb
    if ($LASTEXITCODE -ne 0) { throw 'Generated PCB failed DRC.' }

    & $python (Join-Path $scripts 'Build-KiCadPcb.py') (Join-Path $fixtures 'invalid-duplicate-net.json') (Join-Path $tempRoot 'invalid.kicad_pcb') --footprint-root $footprints 2>$null
    if ($LASTEXITCODE -eq 0) { throw 'Invalid duplicate-net fixture unexpectedly succeeded.' }

    & $python (Join-Path $scripts 'Build-KiCadSchematic.py') (Join-Path $fixtures 'empty-native.kicad_sch') (Join-Path $tempRoot 'invalid.sch') --project-name regression 2>$null
    if ($LASTEXITCODE -eq 0) { throw 'Invalid schematic output extension unexpectedly succeeded.' }

    [pscustomobject]@{
        passed = $true
        kicadVersion = (& $cli version 2>$null).Trim()
        tests = @('native schematic clone and validation', 'declarative routed PCB and DRC', 'invalid duplicate net rejection', 'invalid schematic extension rejection')
    } | ConvertTo-Json -Depth 3
}
finally {
    Remove-Item -LiteralPath $tempRoot -Recurse -Force -ErrorAction SilentlyContinue
}
