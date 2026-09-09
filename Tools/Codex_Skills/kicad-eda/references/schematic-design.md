# Schematic design

## Required inputs

Establish the intended function, interfaces, supply rails, tolerances, environmental conditions, safety constraints, programmable behavior, and test strategy. Obtain authoritative datasheets for every active or pin-sensitive component. Mark missing values as unresolved.

## Structure

- Partition sheets by function and signal flow. Keep sheet interfaces explicit and stable.
- Use descriptive net names. Distinguish rails whose nominal voltage is the same but whose filtering, sequencing, or current path differs.
- Show connector pin numbers, polarity, active-low notation, direction, voltage domain, and off-board protection clearly.
- Put decoupling, bias, termination, protection, clock, reset, and programming circuitry next to the device or interface they serve.
- Use net labels to clarify structure, not to conceal an unreadable connection graph.

## Components and BOM data

Verify symbol pin numbers and electrical types against the exact package/datasheet. Assign an exact footprint before PCB work. Populate manufacturer, manufacturer part number, description, tolerance/rating, and procurement fields required by the project. Record substitutions explicitly; do not treat a parametric match as approved.

## Verification

Run annotation and ERC. Resolve warnings by correcting the circuit; use exclusions or no-connect markers only when their intent is documented. Export a netlist/BOM and check that references, values, footprints, and part numbers agree with the schematic. Render all changed sheets and inspect junctions, labels, overlapping text, bus entries, power symbols, and page boundaries.

## KiCad 10 headless boundary

KiCad 10 has no supported headless schematic-authoring API. Create or transform native `.kicad_sch` files only from a known native source whose embedded symbols and instance data are preserved. `Build-KiCadSchematic.py` can create a project-specific native scaffold from such a template, regenerate UUIDs, update the root instance path, and set title-block metadata. It does not add arbitrary symbols or infer pin geometry. Circuit-specific composition must be followed by CLI ERC, netlist/BOM export, PDF rendering, and visual inspection.
