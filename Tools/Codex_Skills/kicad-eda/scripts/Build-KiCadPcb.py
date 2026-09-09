#!/usr/bin/env python3
"""Build an explicitly placed and routed KiCad PCB from a JSON specification.

Run with KiCad's bundled Python.  The specification is intentionally mechanical:
it assigns pads and draws supplied tracks; it is not an autorouter or netlist
inference engine.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pcbnew


def mm_point(value: list[float]) -> "pcbnew.VECTOR2I":
    if len(value) != 2:
        raise ValueError(f"point must contain two numbers: {value!r}")
    return pcbnew.VECTOR2I_MM(float(value[0]), float(value[1]))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--footprint-root", type=Path, required=True)
    args = parser.parse_args()
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    board = pcbnew.BOARD()

    settings = board.GetDesignSettings()
    rules = spec.get("rules_mm", {})
    if "min_clearance" in rules:
        settings.m_MinClearance = pcbnew.FromMM(float(rules["min_clearance"]))
    if "min_track_width" in rules:
        settings.m_TrackMinWidth = pcbnew.FromMM(float(rules["min_track_width"]))
    if "min_via_diameter" in rules:
        settings.m_ViasMinSize = pcbnew.FromMM(float(rules["min_via_diameter"]))
    if "min_via_drill" in rules:
        settings.m_MinThroughDrill = pcbnew.FromMM(float(rules["min_via_drill"]))

    nets: dict[str, object] = {}
    for name in spec.get("nets", []):
        if name in nets:
            raise ValueError(f"duplicate net {name!r}")
        item = pcbnew.NETINFO_ITEM(board, name)
        board.Add(item)
        nets[name] = item

    footprints: dict[str, object] = {}
    for item in spec.get("footprints", []):
        reference = item["reference"]
        if reference in footprints:
            raise ValueError(f"duplicate reference {reference!r}")
        library, name = item["library_id"].split(":", 1)
        footprint = pcbnew.FootprintLoad(str(args.footprint_root / f"{library}.pretty"), name)
        if footprint is None:
            raise FileNotFoundError(f"footprint not found: {item['library_id']}")
        footprint.SetReference(reference)
        footprint.SetValue(item.get("value", ""))
        footprint.SetPosition(mm_point(item["at_mm"]))
        footprint.SetOrientationDegrees(float(item.get("rotation_deg", 0)))
        board.Add(footprint)
        footprints[reference] = footprint
        for pad_number, net_name in item.get("pads", {}).items():
            pad = footprint.FindPadByNumber(str(pad_number))
            if pad is None:
                raise ValueError(f"{reference} has no pad {pad_number}")
            if net_name not in nets:
                raise ValueError(f"{reference} pad {pad_number} names unknown net {net_name!r}")
            pad.SetNet(nets[net_name])

    layers = {"F.Cu": pcbnew.F_Cu, "B.Cu": pcbnew.B_Cu}
    for item in spec.get("tracks", []):
        net_name = item["net"]
        points = [mm_point(point) for point in item["points_mm"]]
        if net_name not in nets or len(points) < 2:
            raise ValueError(f"invalid track for net {net_name!r}")
        layer = layers[item.get("layer", "F.Cu")]
        for start, end in zip(points, points[1:]):
            track = pcbnew.PCB_TRACK(board)
            track.SetStart(start)
            track.SetEnd(end)
            track.SetLayer(layer)
            track.SetWidth(pcbnew.FromMM(float(item.get("width_mm", 0.25))))
            track.SetNet(nets[net_name])
            board.Add(track)

    for item in spec.get("vias", []):
        net_name = item["net"]
        if net_name not in nets:
            raise ValueError(f"via names unknown net {net_name!r}")
        via = pcbnew.PCB_VIA(board)
        via.SetPosition(mm_point(item["at_mm"]))
        via.SetWidth(pcbnew.FromMM(float(item.get("diameter_mm", 0.6))))
        via.SetDrill(pcbnew.FromMM(float(item.get("drill_mm", 0.3))))
        via.SetNet(nets[net_name])
        board.Add(via)

    outline = [mm_point(point) for point in spec["outline_mm"]]
    if len(outline) < 3:
        raise ValueError("outline_mm must contain at least three points")
    if outline[0] != outline[-1]:
        outline.append(outline[0])
    for start, end in zip(outline, outline[1:]):
        edge = pcbnew.PCB_SHAPE(board)
        edge.SetShape(pcbnew.SHAPE_T_SEGMENT)
        edge.SetLayer(pcbnew.Edge_Cuts)
        edge.SetStart(start)
        edge.SetEnd(end)
        edge.SetWidth(pcbnew.FromMM(0.05))
        board.Add(edge)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    pcbnew.SaveBoard(str(args.output), board)
    print(args.output.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
