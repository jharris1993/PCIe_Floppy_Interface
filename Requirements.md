# Requirements

This document defines the current baseline requirements for the floppy-drive interface project. Requirements are normative unless explicitly marked optional or future.

## 1. Functional scope

### R1 — Primary function
The system shall provide a programmable floppy-disk controller and digital Shugart-interface implementation suitable for a broad range of conventional floppy drives and disk formats.

### R2 — Drive compatibility
The system shall support 3.5-inch and 5.25-inch floppy drives using two separate 34-pin signal-interface connectors.

One connector shall support IBM PC/AT-compatible drives using the conventional twisted-cable drive-selection arrangement.

The second connector shall support other approved 34-pin interface variants, including compatible 5.25-inch drives and older full-height units where electrically practical. To the greatest extent practical, interface differences shall be selected by jumpers. Where possible, these jumpers shall provide configuration inputs to the controller or programmable logic, which shall reconfigure the applicable connector signals.

### R3 — Programmable geometry and timing
The controller shall avoid unnecessary fixed assumptions about disk geometry or drive mechanics. Where technically practical, software or firmware shall be able to configure parameters such as:

- cylinders/tracks;
- heads/sides;
- sectors per track;
- step behavior;
- rotational/index behavior;
- sector size;
- data rate;
- FM/MFM encoding;
- hard- or soft-sector operation where supported by the hardware;
- use or non-use of optional drive signals.

### R4 — Basic drive control
The system shall provide the drive-control functions needed for normal floppy operation, including as applicable:

- drive select;
- motor control;
- direction and step;
- track-zero sensing;
- write gate/data;
- read data;
- index;
- write protect;
- head/side selection.

### R5 — Sector-level operation
The initial functional target shall include reliable sector-oriented read and write operation using common FM and MFM formats.

## 2. Architecture

### R6 — Programmable logic
Timing-critical floppy-controller behavior should be implemented in FPGA or comparable programmable logic when that materially improves determinism, flexibility, or future extensibility.

### R7 — Host interface
The final hardware target shall be a single-board internal PCIe device. USB shall not be required as a bridge in the final product.

### R8 — Staged development
The design may use non-PCIe development hardware during early implementation when this reduces development risk. The architecture should avoid choices that unnecessarily prevent later migration to PCIe.

### R9 — Transport abstraction
Host commands and controller operations should be kept reasonably independent of the physical host transport so that early development interfaces can be replaced without redesigning the controller model.

## 3. Flux timing

### R10 — Future transition timing
The design should preserve a practical path to exposing read-transition timing and, potentially, write-transition timing for diagnostic or disk-reconstruction purposes.

### R11 — Secondary priority
Flux-transition capture/replay is a secondary capability. Components shall not be selected solely for full flux-level functionality when doing so materially increases cost or complexity for the primary controller requirements.

## 4. Host software

### R12 — Current 64-bit Windows research
The project shall investigate practical methods for presenting the hardware to current 64-bit Windows as a conventional floppy device where feasible.

### R13 — Drive-letter behavior
Conventional `A:`/`B:` floppy-drive presentation is desirable where supported by the operating system and driver architecture, but shall not be assumed feasible until demonstrated.

### R14 — OS limitations
Any operating-system, driver-signing, enumeration, or compatibility limitations discovered during implementation shall be documented rather than hidden behind emulation assumptions.

## 5. External compatibility

### R15 — Greaseweazle reference
The Greaseweazle project may be used as a technical reference and possible compatibility target for selected functionality. It shall not define the architecture when doing so conflicts with the project's primary programmable-FDC requirements.

### R16 — External baselines
Any external source code or design used as an implementation baseline shall be recorded in `Dependencies.md` with enough information to identify the exact upstream version or commit.

## 6. Engineering constraints

### R17 — Digital drive interface
The controller shall treat the normal Shugart drive connection as a digital interface. Magnetic-head analog processing remains internal to the floppy drive unless a future design explicitly changes this scope.

### R18 — Prototype practicality
Early prototypes may use development boards, adapters, or conventional prototyping methods. High-speed, signal-integrity, voltage, or placement constraints shall take precedence over a preferred prototyping form when necessary.

### R19 — Evidence before commitment
Unverified assumptions about PCIe, Windows driver behavior, legacy floppy support, or external-project compatibility shall be treated as open engineering questions until demonstrated or supported by authoritative documentation.

## 7. Documentation and change control

### R20 — Significant decisions
Significant architectural or compatibility decisions shall be recorded in `DECISIONS/` when the rationale would otherwise be difficult to reconstruct later.

### R21 — Source of truth
When repository documents disagree, the more specific normative requirement or a later approved decision record shall take precedence. Conflicts shall be corrected rather than silently resolved in implementation code.
