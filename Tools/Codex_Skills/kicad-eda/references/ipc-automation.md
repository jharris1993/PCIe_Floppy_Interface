# KiCad 10 IPC automation

Use IPC when KiCad 10 is running with Preferences > Plugins > API Server enabled. The official Python package is `kicad-python`, imported as `kipy`.

Run `scripts/Test-KiCadIpc.py` with the isolated interpreter recorded in the installation manifest. A successful connection reports the KiCad version. A connection failure is not permission to rewrite design files directly.

KiCad 10 API coverage is strongest in PCB Editor. Query the API and current official examples before assuming a schematic or library mutation is supported. For a mutation:

1. Confirm the intended document and selection.
2. Take a Git diff or recoverable copy.
3. Query current objects and units.
4. Apply the smallest change through the API.
5. Save through KiCad.
6. Run CLI ERC/DRC and render/inspect the affected area.

Do not connect to an arbitrary socket or named pipe. The official client discovers the running KiCad server and handles its token.
