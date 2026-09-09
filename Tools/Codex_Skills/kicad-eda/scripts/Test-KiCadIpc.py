#!/usr/bin/env python3
"""Verify that the official kicad-python client can reach a running KiCad."""

import json
import sys


def main() -> int:
    try:
        from kipy import KiCad
    except ImportError as exc:
        print(json.dumps({"connected": False, "error": f"kicad-python is not installed: {exc}"}))
        return 2

    try:
        client = KiCad()
        print(json.dumps({"connected": True, "version": str(client.get_version())}))
        return 0
    except BaseException as exc:  # The official example treats connection errors broadly.
        print(json.dumps({"connected": False, "error": str(exc)}))
        return 1


if __name__ == "__main__":
    sys.exit(main())
