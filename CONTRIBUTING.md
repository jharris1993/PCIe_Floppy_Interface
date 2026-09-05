# Contributing

This repository contains hardware, HDL/firmware, host software, drivers, and documentation. Keep changes focused, traceable, and documented.

## General practice

- Keep commits focused and use descriptive messages.
- Do not mix unrelated cleanup with functional changes.
- Update documentation when requirements, architecture, interfaces, dependencies, build procedures, or externally visible behavior change.

## Requirements and design

- `Requirements.md` is the authoritative current project requirements specification.
- `Design.md` describes the current design used to implement the requirements but is not authoritative.
- Do not weaken requirements to simplify implementation. Propose requirement changes explicitly for review.

## Engineering decisions

Use `Project_Decisions/` as a non-authoritative engineering notebook for significant choices whose rationale may matter later, including major changes to:

- FPGA or PCIe architecture;
- host driver model;
- electrical interfaces;
- command protocols;
- compatibility targets;
- external baselines.

Record the decision, context, alternatives, rationale, consequences, and relevant commit or issue references.

When a project choice changes a requirement or the current design, update `Requirements.md` or `Design.md`, as applicable. A notebook entry does not override `Requirements.md`.

## Dependencies

- Record significant implementation dependencies and baselines in `Dependencies.md`.
- Verify license compatibility before incorporating external code.

## Hardware

Maintain applicable schematic and PCB sources, BOM/part information, substitutions, electrical assumptions, pinouts, and release fabrication outputs.

Do not compromise documented signal-integrity, timing, voltage, or safety constraints for prototype convenience.

## Firmware and HDL

- Provide repeatable verification for timing-sensitive logic where practical.
- Document non-obvious timing assumptions and clock-domain crossings.

## Software and drivers

Document applicable OS support and significant installation, privilege, signing, or kernel requirements.

## Completion

Before considering a change complete:

- verify affected functionality;
- update relevant documentation;
- identify remaining unverified assumptions or hardware-dependent behavior.
