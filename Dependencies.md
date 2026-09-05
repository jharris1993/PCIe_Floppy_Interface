# Dependencies and External References

This file records external projects, specifications, tools, and implementation baselines that materially affect the project.

Do not record an external project merely because it was consulted during discussion. Add it when the repository depends on it, implements compatibility with it, or uses it as a significant engineering baseline.

## Source-code baselines

No source-code baselines have been selected.

## Hardware / protocol specifications

Add authoritative specifications here when selected, for example:

| Specification | Purpose | Revision | Source | Notes |
|---|---|---|---|---|
| PCI Express Base Specification | PCIe endpoint/interface design | TBD | PCI-SIG | Record the actual revision used. |
| Floppy/Shugart interface references | Drive electrical and signal behavior | TBD | TBD | Prefer original manufacturer documentation where available. |

## Development tools

Tool versions should be pinned when reproducibility depends on them.

| Tool | Purpose | Required version | Notes |
|---|---|---|---|
| FPGA vendor toolchain | HDL synthesis/place-and-route/programming | TBD | Define after FPGA selection. |
| HDL simulator | Simulation and automated verification | TBD | Define after HDL/toolchain selection. |
| Host compiler/toolchain | Host utilities and driver support | TBD | Record separately per supported OS if needed. |

## Rules for adding dependencies

For every implementation dependency, record:

1. canonical upstream location;
2. exact release/tag/commit where practical;
3. purpose in this project;
4. applicable license;
5. local modifications or patches, if any;
6. update procedure or compatibility constraint when relevant.

Do not silently update an implementation baseline. A change that can affect compatibility or behavior should be documented and, when significant, recorded in `Project_Decisions/`.
