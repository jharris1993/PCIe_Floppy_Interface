# Libraries and templates

Prefer project-local libraries for custom or modified symbols, footprints, design blocks, and models. Reference them with `${KIPRJMOD}` so the project remains portable.

Use the standard libraries packaged for the installed stable KiCad release as the global baseline. Do not overlay them with a Git checkout of a moving library branch. If a newer upstream item is required before the next packaged release, copy only the reviewed item into a project-local library and record its exact upstream commit and license.

## Symbols

Build from the exact datasheet. Verify unit structure, hidden power pins, pin number/name, electrical type, orientation, active-low notation, alternate functions, and package applicability. Avoid copying a near-match unless every pin and property is revalidated.

## Footprints

Use the component drawing and its stated land-pattern standard or recommendation. Verify pad numbers, dimensions, pitch, origin, rotation, pin-one indicators, paste/mask rules, courtyard, fabrication outline, assembly clearance, thermal pad and via requirements, and hand/reflow process assumptions. Print or dimension-check critical footprints at 1:1 when physical fit matters.

## 3D models

Treat 3D models as mechanical aids, not footprint evidence. Verify model origin, scale, orientation, body height, connector envelope, and mating clearance independently.

The `kicad-packages3D` repository contains models used by KiCad. The separate `kicad-packages3D-source` repository contains contributor/source assets and generators; it is not required merely to view or export installed models.

## Templates

A reusable template may define page settings, title fields, text variables, library tables, baseline net classes, board setup, layer naming, and release jobs. Do not embed project-specific electrical constraints into a generic template. Keep template versions identifiable and do not silently migrate existing projects.
