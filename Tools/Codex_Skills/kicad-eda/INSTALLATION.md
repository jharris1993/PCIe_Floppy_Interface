# Local installation record

The maintained skill source is this directory. The normal installed copy is:

`%USERPROFILE%\.codex\skills\kicad-eda`

The optional official IPC client environment is:

`%USERPROFILE%\.codex\tools\kicad-eda-python`

The installer records exact package versions in `installed-packages.txt` inside that environment and verifies the installed skill against this source.
The reproducible package set is also committed as `requirements-ipc.txt`.

To uninstall, remove only the installed skill directory and IPC environment shown above, then restart Codex. Project files and this maintained source are unaffected. KiCad itself is not modified by this skill installation.
