#!/usr/bin/env python3
"""Create a project-specific native KiCad schematic from a known-good template.

KiCad 10 exposes no supported headless API for arbitrary schematic authoring.  This
tool performs the safe subset that is useful for automation: clone native content,
regenerate every UUID consistently, update instance project names, and set existing
title-block fields.  It never invents symbols, pin geometry, or connectivity.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import tempfile
import uuid
from pathlib import Path

UUID_RE = re.compile(r'(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b')


def replace_title_field(text: str, field: str, value: str) -> str:
    escaped = value.replace('\\', '\\\\').replace('"', '\\"')
    pattern = re.compile(rf'(\({re.escape(field)}\s+")[^"]*("\))')
    if not pattern.search(text):
        raise ValueError(f"template has no title-block field {field!r}")
    return pattern.sub(lambda m: m.group(1) + escaped + m.group(2), text, count=1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("template", type=Path, help="known-good native .kicad_sch template")
    parser.add_argument("output", type=Path, help="new .kicad_sch path")
    parser.add_argument("--project-name", required=True)
    parser.add_argument("--title")
    parser.add_argument("--date")
    parser.add_argument("--revision")
    parser.add_argument("--company")
    parser.add_argument("--kicad-cli", type=Path, help="validate by exporting a netlist")
    args = parser.parse_args()

    if args.template.suffix.lower() != ".kicad_sch" or args.output.suffix.lower() != ".kicad_sch":
        parser.error("template and output must use the .kicad_sch extension")
    text = args.template.read_text(encoding="utf-8-sig")
    if not text.lstrip().startswith("(kicad_sch") or "(lib_symbols" not in text:
        raise ValueError("template is not a native, self-contained KiCad schematic")

    replacements: dict[str, str] = {}
    text = UUID_RE.sub(lambda m: replacements.setdefault(m.group(0).lower(), str(uuid.uuid4())), text)
    text = re.sub(r'(\(project\s+")[^"]*(")', lambda m: m.group(1) + args.project_name + m.group(2), text)
    for field, value in (("title", args.title), ("date", args.date), ("rev", args.revision), ("company", args.company)):
        if value is not None:
            text = replace_title_field(text, field, value)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8", newline="\n")

    if args.kicad_cli:
        with tempfile.TemporaryDirectory(prefix="kicad-sch-check-") as temp_dir:
            result = subprocess.run(
                [str(args.kicad_cli), "sch", "export", "netlist", "--output", str(Path(temp_dir) / "check.net"), str(args.output)],
                check=False,
            )
        if result.returncode:
            args.output.unlink(missing_ok=True)
            raise RuntimeError(f"KiCad rejected generated schematic (exit {result.returncode})")

    print(args.output.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
