#!/usr/bin/env python3
"""Report KiCad IPC transport and safe capability probes as JSON."""

import json
import sys


def main() -> int:
    try:
        from kipy import KiCad
        from kipy.proto.common.types import DocumentType
    except ImportError as exc:
        print(json.dumps({"connected": False, "error": f"kicad-python is not installed: {exc}"}))
        return 2

    try:
        client = KiCad()
        report = {
            "connected": True,
            "version": str(client.get_version()),
            "api_version": str(client.get_api_version()),
            "client_methods": sorted(name for name in dir(client) if not name.startswith("_")),
            "probes": {},
            "limitations": [
                "KiCad 10 requires a running GUI process for IPC",
                "KiCad 10 does not expose general schematic authoring over IPC",
            ],
        }
        for label, document_type in (
            ("open_pcb_documents", DocumentType.DOCTYPE_PCB),
            ("open_schematic_documents", DocumentType.DOCTYPE_SCHEMATIC),
        ):
            try:
                report["probes"][label] = {
                    "available": True,
                    "documents": [str(item) for item in client.get_open_documents(document_type)],
                }
            except BaseException as exc:
                report["probes"][label] = {"available": False, "error": str(exc)}
        print(json.dumps(report, indent=2, sort_keys=True))
        return 0
    except BaseException as exc:  # The official example treats connection errors broadly.
        print(json.dumps({"connected": False, "error": str(exc)}))
        return 1


if __name__ == "__main__":
    sys.exit(main())
