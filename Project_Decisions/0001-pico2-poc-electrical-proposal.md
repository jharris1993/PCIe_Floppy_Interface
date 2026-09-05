# Pico 2 proof-of-concept electrical interface

Date: 2026-09-01

Status: proposed for discussion; not an approved final architecture or fabrication baseline.

## Context

The user requested an inexpensive proof of concept supplementing the original requirements, assumed a Pico 2 with an unspecified GPIO allocation, and requested a tentative drive-interface schematic. PCIe is outside this prototype discussion.

## Proposal

Use open-drain MOSFET transmitters, 3.3 V Schmitt-trigger receivers with 5 V-tolerant inputs, and hardware direction selection for variant connector signals. Preserve two connector options with one selected at a time. Detailed circuits and assumptions are in [Hardware/Pico2_POC/README.md](../Hardware/Pico2_POC/README.md).

## Rationale and alternatives

Some legacy drives specify approximately 40 mA low-level interface loads. A suitably specified MOSFET avoids the low-voltage margin problem of assuming every open-drain logic IC can sink that load. Direction-selected circuits fit the existing seventeen-signal premise. True bidirectional operation would use distinct drive and sense paths and needs an explicit protocol requirement. Separate buffered ports would be preferable if both connectors must be electrically active concurrently.

## Consequences and unresolved items

Pico GPIO mapping, drive variants, pulse requirements, cable loading, and power sequencing remain to be validated. AO3400A is a candidate whose GPIO-driven switching must be measured. No hardware or simulation verification is claimed. This proposal does not supersede Requirements.md or commit the final design away from programmable logic.
