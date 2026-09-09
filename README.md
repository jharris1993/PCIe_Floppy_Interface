# Floppy Drive Interface

A hardware/software project to develop a programmable floppy-disk controller and Shugart-interface platform, ultimately implemented as an internal PCIe card.

## Project goals

The primary goal is broad compatibility with floppy drives and disk formats that use conventional Shugart-derived interfaces, including 3.5-inch and 5.25-inch drives and, where practical, 8-inch drives.

The design should support programmable controller behavior rather than being restricted to the assumptions of a conventional PC floppy-disk controller. Future support for flux-transition timing is desirable, but it is secondary to the core controller/interface function and must not materially increase initial cost or complexity.

## Development approach

Development is intentionally staged:

1. Validate floppy-drive control and data handling using a practical FPGA or programmable-logic development platform.
2. Implement and test controller functions including drive selection, motor control, seeking, index handling, read/write operation, and FM/MFM data handling.
3. Develop the host-side software and investigate practical integration with current 64-bit Windows.
4. Migrate the validated design to PCIe.
5. Produce a custom single-board implementation when the architecture is sufficiently mature.

## Repository documentation

- [`Requirements.md`](Requirements.md) — authoritative current project requirements.
- [`Design.md`](Design.md) — current, non-authoritative project design.
- [`Dependencies.md`](Dependencies.md) — external projects, specifications, tools, and pinned baselines.
- [`AGENTS.md`](AGENTS.md) — instructions for Codex and other repository-aware coding agents.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — repository working practices and change discipline.
- [`Project_Decisions/`](Project_Decisions/) — non-authoritative engineering notebook of significant project choices and rationale.
- [`Documents/`](Documents/) — project-created supporting documentation.
- [`Reference_Documentation/`](Reference_Documentation/) — external technical documents and research.
- [`Reference_Illustrations/`](Reference_Illustrations/) — external explanatory illustrations.
- [`Reference_Implementations/`](Reference_Implementations/) — external implementations available for design reference.
- [`Tools/`](Tools/) — project development, verification, and automation tooling.

## Repository structure

```text
project-root/
├── .gitattributes
├── AGENTS.md
├── CONTRIBUTING.md
├── Dependencies.md
├── Design.md
├── Documents/
├── Drivers/
├── Firmware/
├── Hardware/
├── LICENSE.md
├── Licenses/
├── Project_Decisions/
├── README.md
├── Reference_Documentation/
│   ├── Documents/
│   ├── Pinouts/
│   ├── Research/
│   ├── Schematics/
│   ├── Specifications/
│   ├── README.md
│   └── Sources.md
├── Reference_Illustrations/
├── Reference_Implementations/
│   └── Greaseweazle/
├── Requirements.md
├── Software/
└── Tools/
```

Detailed organization should be defined close to the material it describes.

## Project status

Architecture and baseline documentation are under development. Hardware, firmware, host software, and driver implementation should not be assumed complete unless explicitly documented.

## License

This project is governed by the license conditions specified in [`LICENSE.md`](LICENSE.md).
