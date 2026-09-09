# Verification and fabrication release

Use `scripts/Invoke-KiCad.ps1`. Its `doctor` action discovers KiCad 10 and reports the environment and headless-authoring boundaries. Individual actions produce ERC, DRC, BOM, schematic PDF/SVG, PCB top/bottom renders, Gerbers, drills, position data, or STEP. `verify` runs ERC/DRC and review renders; `release` runs the verification gates and then creates the manufacturing set.

On the maintained Windows Codex host, launch the wrapper and `tests/Run-Regression.ps1` outside the sandbox under the normal user using a narrowly scoped execution approval. Both scripts refuse the `CodexSandboxOffline` identity before invoking KiCad. Do not use Administrator elevation. This prevents misleading per-user registry warnings and keeps KiCad CLI, configuration, and any running API server in the same user context.

## Gate order

1. Confirm source files and exact KiCad version.
2. Run ERC with violations producing a failing exit code.
3. Run DRC with schematic parity and violations producing a failing exit code. Refill zones only on a recoverable working copy because it can modify the board when saved.
4. Export and inspect the BOM for exact MPNs, quantities, DNP state, and footprints.
5. Export schematic PDF/SVG and PCB top/bottom renders without taking over the desktop; inspect every sheet and relevant board view.
6. Generate Gerbers using saved board plot parameters, plus Excellon PTH/NPTH drills, drill maps/reports, CSV position data, and STEP.
7. Inspect output filenames, layer completeness, drill counts, outline, apertures, origins, units, polarity, and archive contents against the selected fabricator's requirements.

Generated output is not proof of manufacturability. Do not release while unresolved ERC/DRC errors, unreviewed exclusions, missing fabrication constraints, unknown stackup, or unverified footprints remain.
