# Headless KiCad 10 automation boundary

Date: 2026-09-09

## Context

The initial KiCad automation workflow used GUI conversion and, when automation failed, desktop capture/control. That occupied the user's foreground desktop and obscured whether a failure came from the Codex sandbox, KiCad IPC transport, or an unsupported API operation. KiCad 10 IPC requires a running GUI process, is focused on PCB Editor, and does not expose general schematic authoring. A successful IPC ping therefore is not evidence that document handlers are available.

## Decision

- Headless file and CLI workflows are the default.
- Desktop capture, mouse/keyboard automation, and launching KiCad's GUI require explicit user authorization for the current task.
- Native `.kicad_sch` sources are maintained directly. The scaffold tool only clones a known-good native schematic, regenerates UUIDs, updates instance project names, and changes existing title-block fields; it does not claim arbitrary symbol placement.
- Declarative PCB construction uses the `pcbnew` module bundled with the selected KiCad installation. Placement, pad-to-net assignments, and routes remain explicit inputs; the tool does not autoroute.
- `kicad-cli` is the verification and export authority for ERC, DRC, netlist/BOM, schematic renders, PCB renders, and fabrication outputs.
- The KiCad 10 IPC client is pinned to `kicad-python` 0.7.1. IPC diagnostics distinguish transport connectivity from handler capability.
- Maintained source, dependency pins, tests, and fixtures are committed under `Tools/Codex_Skills/kicad-eda`. Personal skill copies, virtual environments, registry data, IPC sockets, and temporary renders are not committed.

## Consequences

The workflow is reproducible and reversible through Git without taking control of the desktop. KiCad 10 still cannot provide a supported fully general headless schematic editor; circuit-specific native-format changes require careful format work followed by ERC, exported connectivity/BOM checks, and visual inspection. The sandbox may emit nonfatal Windows registry warnings from `kicad-cli`; commands that need the real per-user KiCad state or IPC transport may require narrowly scoped execution outside the sandbox.

The regression suite covers native schematic cloning and CLI parsing, declarative PCB generation with a routed net and clean DRC, and rejection of an invalid duplicate-net specification. More complex fixtures should be added when their corresponding generator features are introduced.
