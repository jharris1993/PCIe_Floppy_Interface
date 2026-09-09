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
| KiCad | Schematic capture, PCB layout, libraries, verification, and fabrication output | 10.0.6 | Standard Windows x64 installation with official libraries and API server enabled. The packaged libraries are the selected baseline; do not replace them with moving GitLab `master` branches. |
| kicad-python | Official KiCad IPC Python binding | 0.8.0 | Installed in an isolated Codex tool environment; exact transitive versions are recorded by the installer. Requires a running KiCad 10 instance for IPC. |
| FPGA vendor toolchain | HDL synthesis/place-and-route/programming | TBD | Define after FPGA selection. |
| HDL simulator | Simulation and automated verification | TBD | Define after HDL/toolchain selection. |
| Host compiler/toolchain | Host utilities and driver support | TBD | Record separately per supported OS if needed. |

### KiCad 10.0.6 standard-library baseline

The standard installer contains packed/installed forms of the official library repositories. The release-tag commits corresponding to the selected KiCad version are:

| Library | Upstream | Release/tag | Commit | License | Local installed form |
|---|---|---|---|---|---|
| Schematic symbols | `https://gitlab.com/kicad/libraries/kicad-symbols` | `10.0.6` | `7800d91437ce44e2ed0928f2ad31a287457b8a68` | CC BY-SA 4.0 | 223 packed `.kicad_sym` libraries |
| PCB footprints | `https://gitlab.com/kicad/libraries/kicad-footprints` | `10.0.6` | `819223b66f96508feaeaa305301b5e6bb5c1038b` | CC BY-SA 4.0 | 155 `.pretty` libraries containing 15,450 files |
| 3D models | `https://gitlab.com/kicad/libraries/kicad-packages3D` | `10.0.6` | `e62ed1fc7862da83f789bd562671b5e4b82afcdf` | CC BY-SA 4.0 | 7,251 STEP models |
| Project templates | `https://gitlab.com/kicad/libraries/kicad-templates` | `10.0.6` | `3ed4538b0f965d821df63a5fffc4441e723cfe7f` | CC BY-SA 4.0 | 19 template directories |

The separate `kicad-packages3D-source` repository is not an implementation dependency. It contains editable/generator sources for contributing 3D models and is unnecessary for schematic capture, footprint assignment, PCB layout, 3D viewing, or fabrication exports. Add and pin it only if the project begins maintaining custom generated 3D models from those source formats.

## Rules for adding dependencies

For every implementation dependency, record:

1. canonical upstream location;
2. exact release/tag/commit where practical;
3. purpose in this project;
4. applicable license;
5. local modifications or patches, if any;
6. update procedure or compatibility constraint when relevant.

Do not silently update an implementation baseline. A change that can affect compatibility or behavior should be documented and, when significant, recorded in `Project_Decisions/`.
