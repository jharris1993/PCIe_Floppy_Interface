# Local installation record

The maintained skill source is this directory. The normal installed copy is:

`%USERPROFILE%\.codex\skills\kicad-eda`

The optional official IPC client environment is:

`%USERPROFILE%\.codex\tools\kicad-eda-python`

The installer records exact package versions in `installed-packages.txt` inside that environment and verifies the installed skill against this source.
The reproducible package set is also committed as `requirements-ipc.txt`.

KiCad's bundled Python at `C:\Program Files\KiCad\10.0\bin\python.exe` supplies the matching `pcbnew` module for headless board construction. It is part of KiCad and is not copied into the Codex environment.

Approve KiCad CLI work outside the Codex sandbox using the exact installed `kicad-cli.exe` path. Scripts that invoke it must run as the normal Windows user; they intentionally stop when executed as `CodexSandboxOffline`. Outside-sandbox execution does not require Administrator elevation.

The maintained repository copy is authoritative. Reinstall by copying this directory to the personal skills directory and recreating the isolated environment from `requirements-ipc.txt`. The local copy and environment are deployment artifacts, not repository content.

To uninstall, remove only the installed skill directory and IPC environment shown above, then restart Codex. Project files and this maintained source are unaffected. KiCad itself is not modified by this skill installation.
