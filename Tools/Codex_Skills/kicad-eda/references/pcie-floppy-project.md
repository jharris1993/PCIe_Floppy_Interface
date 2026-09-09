# PCIe floppy-interface project

`Requirements.md` is authoritative. `Design.md` is provisional and identifies open choices.

For hardware work in this repository:

- Preserve programmable geometry, timing, optional signals, FM/MFM operation, transport independence, and the eventual single-board PCIe target.
- Do not assume PC-only Shugart pin use, fixed drive geometry, 5 V tolerance, open-collector behavior, termination, or Windows floppy enumeration details.
- Treat the two 34-pin connectors as distinct compatibility interfaces whose pin use and protection must be verified.
- Keep magnetic-head analog processing out of scope unless requirements change.
- Do not choose an FPGA, PCIe endpoint, DMA model, level translator, connector pinout, or Windows driver architecture without recording the supporting evidence and resolving the applicable open design question.
- Consult applicable `Reference_*` material, but do not elevate it into a requirement or implementation baseline. Record an adopted external baseline in `Dependencies.md`.
