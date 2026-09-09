# KiCad automation tooling

## Status

Accepted for development tooling on 2026-09-09.

## Context

The project needs repeatable creation, inspection, verification, and release of KiCad schematics and PCB layouts. KiCad 10.0.6 is installed with its standard libraries and API server enabled. Automation must remain removable and must not silently replace project requirements or electrical engineering review.

## Decision

Use KiCad 10.0.6 as the pinned EDA baseline. Use the official `kicad-cli` interface for deterministic ERC, DRC, BOM, plot, and fabrication exports. Use the official `kicad-python` IPC binding, isolated in a dedicated environment, for supported interaction with a running KiCad session.

Use the symbol, footprint, 3D-model, and template libraries packaged with the KiCad 10.0.6 Windows installer. Their corresponding `10.0.6` release-tag commits are recorded in `Dependencies.md`. Do not overlay or replace them with moving `master` branches. The separate 3D-model source repository is not installed unless the project later needs to develop generated 3D models.

Maintain the Codex skill and wrapper scripts in `Tools/Codex_Skills/kicad-eda` and install a copy in the personal Codex skills directory. Do not adopt an unlicensed community KiCad parser or MCP server as a project dependency.

## Alternatives considered

- Direct S-expression editing remains a last-resort method because malformed UUID, embedded-library, or connectivity changes can produce plausible but incorrect files.
- A community KiCad skill/tool repository was evaluated for structural editing, but its repository did not contain a license file and it depended on a forked parser. It was not adopted.
- A third-party MCP server was not needed because KiCad provides official CLI and IPC interfaces.

## Consequences

The installed Codex capability is removable without uninstalling KiCad or changing project files. KiCad 10 must be running for IPC operations; CLI verification and exports remain available without IPC. Electrical correctness, footprint accuracy, manufacturability, and hardware behavior still require engineering evidence and appropriate review/testing.
