# KiCad IPC automation

Use IPC when KiCad 10 is running with Preferences > Plugins > API Server enabled. The official Python package is `kicad-python`, imported as `kipy`.

Run `scripts/Test-KiCadIpc.py` with the isolated interpreter recorded in the installation manifest. Its JSON report separates transport connectivity from document/action handler availability. A successful ping does not imply that schematic or PCB handlers are present. A connection failure is not permission to take over the desktop or rewrite design files blindly.

KiCad 10 requires a running GUI process for IPC, has no general schematic-authoring API, and may return `no handler available` for document and action requests even when ping succeeds. Use the pinned 0.7.1 binding for the KiCad 10 baseline. Treat APIs added for KiCad 11 as unavailable until the project baseline changes.

Do not use screen capture, mouse/keyboard control, or foreground-window automation as an automatic fallback. These methods require explicit user authorization for the current task.

For a supported mutation:

1. Confirm the intended document and selection.
2. Take a Git diff or recoverable copy.
3. Query current objects and units.
4. Apply the smallest change through the API.
5. Save through KiCad.
6. Run CLI ERC/DRC and render/inspect the affected area.

Do not connect to an arbitrary socket or named pipe. The official client discovers the running KiCad server and handles its token.
