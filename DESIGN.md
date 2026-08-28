# Design

This document describes the current architectural direction. It is not a substitute for `REQUIREMENTS.md`; implementation choices may change as long as the requirements remain satisfied or are deliberately revised.

## 1. Architectural concept

The system is divided into four primary layers:

```text
Host software / OS integration
            │
      Host command layer
            │
   PCIe interface / transport
            │
 FPGA controller and timing logic
            │
   Shugart-compatible drive I/O
            │
        Floppy drive
```

Early prototypes may replace PCIe with a simpler development transport while preserving the command/controller separation.

## 2. FPGA / programmable logic

The programmable-logic portion is expected to handle timing-critical functions such as:

- drive-control signal generation and sampling;
- step timing;
- index timing and measurement;
- read-data sampling;
- write-data generation;
- FM/MFM encode/decode support;
- data separation or equivalent timing recovery;
- configurable controller parameters;
- buffering and host-facing command execution.

The exact partition between FPGA logic and embedded/host software remains open until a development platform is selected.

## 3. Shugart interface

The drive-side interface should be designed for broad Shugart-derived compatibility rather than only the IBM-PC subset.

The electrical design must explicitly account for:

- signal direction;
- open-collector/open-drain behavior where applicable;
- pull-up requirements;
- voltage levels;
- termination;
- connector pinout variants;
- optional or historically reused signals;
- protection against incompatible external drive wiring.

Signal capabilities that are not required for a particular drive should be software- or hardware-disableable where practical.

## 4. Data handling

The first implementation should prioritize conventional sector operation using FM and MFM encoding.

The architecture should avoid unnecessarily discarding low-level timing information. If practical without substantial complexity, the read path should retain enough timing information to support later diagnostics or transition-level capture.

Full Greaseweazle-style flux capture/replay is not a first-stage requirement.

## 5. Host interface

The final host interface is PCIe.

A likely structure is:

```text
Host driver/software
       │
 command / descriptor interface
       │
 PCIe endpoint + DMA or mapped buffers
       │
 controller command engine
       │
 floppy timing/data engine
```

The exact PCIe endpoint architecture, DMA strategy, BAR layout, interrupt model, and driver interface remain open design decisions.

## 6. Host command model

Commands should express controller operations independently of the physical development transport where reasonable. Candidate operations include:

- query capabilities;
- select/configure drive;
- motor on/off;
- seek/step;
- read sector/track;
- write sector/track;
- read status;
- configure timing/format parameters;
- diagnostic timing operations.

Transport-independent command semantics will make it easier to develop against UART/USB/JTAG or another temporary interface before PCIe is available.

## 7. Windows integration

Windows integration is a research item, not an assumed solved problem.

The project should evaluate at least two host-facing models:

1. presentation as a conventional floppy/controller device where current Windows permits it; and
2. a project-specific device interface with user-mode software when conventional floppy enumeration is impractical.

The architecture should not depend on `A:`/`B:` drive-letter presentation until driver feasibility is demonstrated.

## 8. Development sequence

### Stage 1 — Controller proof of concept
Use a practical programmable-logic development platform to validate drive control, seeking, index handling, read/write timing, FM/MFM processing, and sector-level operation.

### Stage 2 — Command and host software
Define a stable host/controller command boundary and develop diagnostic/test software.

### Stage 3 — PCIe proof of concept
Move the host interface to PCIe using a development board or validated endpoint solution.

### Stage 4 — OS integration
Develop and validate the selected Windows/Linux driver and host integration strategy.

### Stage 5 — Custom hardware
Integrate the proven logic, electrical interface, PCIe endpoint, power, connectors, and protection circuitry onto the final board.

## 9. Open design questions

The following are intentionally unresolved and should be decided through analysis or prototypes rather than assumed:

- FPGA family and development board.
- PCIe endpoint implementation.
- DMA versus programmed-I/O balance.
- FPGA/firmware/software partitioning.
- Exact command protocol.
- Windows device/driver architecture.
- Level shifting and line-interface implementation.
- Extent of 8-inch-drive support.
- Extent of Greaseweazle compatibility.
- Depth and representation of optional flux-timing data.
