# PCB layout

## Inputs and constraints

Do not begin detailed placement or routing until the board outline, mounting holes, connectors, keepouts, layer stackup, fabrication limits, net classes, current requirements, and impedance requirements are known or explicitly provisional.

## Placement

- Place mechanical and externally constrained items first.
- Group circuits by function while preserving signal flow and return-current continuity.
- Place decoupling capacitors at the relevant power pins with short power and ground paths. Treat the complete current loop, not only trace length, as the constraint.
- Separate noisy switching, clocks, sensitive analog/flux inputs, and external cable interfaces according to their coupling risks.
- Reserve access for test points, programming, probes, assembly, rework, and connector mating.

## Stackup and routing

- Use a continuous reference plane for fast signals where practical. Do not route a critical signal across a plane split or void without an intentional return path.
- Derive widths, clearances, vias, differential geometry, and impedance from the selected stackup and fabricator capabilities.
- Apply PCIe constraints only after the endpoint, connector/topology, generation, stackup, and reference-clock architecture are selected.
- Size power paths from current, allowable rise/drop, copper weight, cooling, and transient requirements.
- Review every layer transition, return via, connector escape, zone neck-down, thermal relief, and copper-to-edge clearance.

## Verification

Update the PCB from the schematic and check parity. Refill zones before final DRC. Inspect copper and mask per layer, silkscreen readability, courtyard/assembly clearance, holes and slots, board outline closure, and 3D/mechanical fit. DRC exclusions require a specific documented rationale.

For reproducible headless construction, `Build-KiCadPcb.py` accepts a declarative JSON specification for the outline, standard-library footprints, pad-to-net assignments, and explicit routed segments. It deliberately does not autoroute or infer electrical connectivity. Run it with KiCad's bundled Python so the `pcbnew` module matches the saved board format.
