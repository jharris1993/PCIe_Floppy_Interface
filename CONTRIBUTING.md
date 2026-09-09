# Contributing

Keep changes focused, traceable, and limited to one purpose per commit.

## Requirements and design

- `Requirements.md` is authoritative.
- `Design.md` records the current implementation approach.
- Record significant choices and rationale in `Project_Decisions/`.
- Update affected documentation when requirements, design, interfaces, dependencies, or procedures change.
- Do not silently change requirements or established decisions.

## Dependencies

Record significant tools, libraries, external baselines, versions, sources, and licenses in `Dependencies.md`.

## Hardware

- Use the KiCad version recorded in `Dependencies.md` for maintained schematic and PCB designs.
- Commit native editable sources and all project-specific symbols, footprints, rules, and configuration needed to reproduce the design.
- Run applicable ERC and DRC checks and review all warnings, exclusions, and unconnected items.
- Regenerate and inspect affected fabrication outputs before release.
- Report unverified electrical, mechanical, manufacturing, or hardware assumptions.

Detailed KiCad procedures and automation belong under `Tools/`.

KiCad automation should be headless by default. Desktop capture or GUI control requires explicit user authorization for the task and must not be used merely because CLI or IPC capability is absent.

## Firmware and software

- Provide repeatable tests for affected behavior where practical.
- Document timing, platform, installation, privilege, signing, and compatibility constraints as applicable.
- Keep host-command semantics independent of temporary development transports where practical.

## Before completion

1. Run applicable tests, checks, formatters, simulations, ERC, or DRC.
2. Review the complete diff for unrelated or generated changes.
3. Update affected documentation and dependency records.
4. State what was verified and what remains unverified.
