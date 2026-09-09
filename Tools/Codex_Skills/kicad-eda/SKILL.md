---
name: kicad-eda
description: Create, edit, inspect, verify, and release KiCad schematics, symbol and footprint libraries, PCB layouts, BOMs, plots, and fabrication outputs. Use for .kicad_pro, .kicad_sch, .kicad_pcb, .kicad_sym, .kicad_mod, ERC, DRC, placement, routing, stackups, Gerbers, drills, or KiCad IPC work. Do not use for unrelated electronics prose that does not involve a KiCad artifact.
---

# KiCad EDA

Produce electrically justified, mechanically consistent, reviewable KiCad artifacts. Treat a project as the unit of work: keep its project, schematic, board, project-local libraries, rules, and release configuration together.

## Before changing a design

- Read repository instructions and the applicable requirements, design, dependency, and decision documents. Requirements govern when documents disagree.
- Identify unresolved electrical, mechanical, fabrication, component-availability, and interface assumptions. Do not convert an assumption into a design choice silently.
- Inspect the whole KiCad project and determine its saved KiCad version. Work on a Git-backed branch or other recoverable copy before a format upgrade or substantial edit.
- Prefer official KiCad 10 CLI and IPC APIs. Do not install or execute third-party plugins, libraries, scripts, or models without checking provenance, license, version, and authorization.

## Route the task

- For schematic creation, connectivity, annotation, power flags, hierarchy, and BOM fields, read [references/schematic-design.md](references/schematic-design.md).
- For placement, stackup, constraints, routing, planes, return paths, and mechanical layout, read [references/pcb-layout.md](references/pcb-layout.md).
- For symbols, footprints, 3D models, design blocks, and templates, read [references/libraries-and-templates.md](references/libraries-and-templates.md).
- For ERC, DRC, plots, BOMs, Gerbers, drills, position files, STEP, and release gates, read [references/release-workflow.md](references/release-workflow.md).
- For a running KiCad session or API-based PCB manipulation, read [references/ipc-automation.md](references/ipc-automation.md).
- In this repository, also read [references/pcie-floppy-project.md](references/pcie-floppy-project.md).

## Editing methods

Choose the least fragile method that supplies the needed capability:

1. Prefer headless, file-based work: native KiCad sources, KiCad's bundled `pcbnew` Python for PCB construction, and `kicad-cli` for checks and exports.
2. Use the official `kicad-python` IPC binding only for operations its capability probe confirms against a running KiCad session. KiCad 10 IPC does not provide general schematic authoring.
3. Invoke [scripts/Invoke-KiCad.ps1](scripts/Invoke-KiCad.ps1) for deterministic checks and exports. Use [scripts/Build-KiCadPcb.py](scripts/Build-KiCadPcb.py) for declarative PCB construction and [scripts/Build-KiCadSchematic.py](scripts/Build-KiCadSchematic.py) for native schematic scaffolding or checked transformations.
4. Edit native KiCad S-expressions only when the format and operation are understood. Preserve or regenerate UUIDs deliberately, keep embedded library data consistent, make narrow edits, and validate connectivity plus rendered output.

Do not capture or control the user's desktop, launch KiCad's GUI, or use GUI keystroke/mouse automation unless the user explicitly authorizes that method for the current task. A headless limitation is a capability boundary to report, not implicit permission to take over the desktop.

Never claim that a syntactically valid file is an electrically correct design. Never infer pin numbers, footprints, voltage limits, polarity, stackup, impedance, or manufacturer ordering data from a similar-looking part.

## Completion gates

- Schematic work: verify annotation, connectivity, pin mapping, required fields, and ERC; render every affected sheet and visually inspect it.
- PCB work: verify schematic parity, board outline, stackup/rules, placement constraints, routing, zones, and DRC; inspect relevant copper, mask, silkscreen, fabrication, and 3D views.
- Release work: generate outputs from a clean verified source, inspect the output manifest, and keep generated files separate from source unless repository policy says otherwise.
- Report the exact KiCad/tool versions, checks run, violations or exclusions, generated outputs, and anything not verified. Hardware behavior remains unverified without hardware testing or authoritative evidence.
