
Design files for all Greaseweazle boards are linked below:

- [F1 Adapter Board](#f1-adapter-board)
- [F7 v1](#f7-v1)
- [F7 v2](#f7-v2)
- [F7 v3](#f7-v3)
- [F7 Lightning](#f7-lightning)
- [F7 Lightning Plus](#f7-lightning-plus)
- [F7 Slim](#f7-slim)
- [V4](#v4)
- [V4 Slim](#v4-slim)
- [V4.1](#v41)

Test jig for F7 v3, F7 Lightning Plus, V4, V4.1, F1 Plus:
- [Test Jig v2.1](#test-jig-v21)

External links to design files for third-party boards:
- [F1 Plus][f1plusdiy]
- [F7 Plus][f7plusdiy]


## F1 Adapter Board

**DirtyPCBs:** The simplest method, using a [direct purchase
link][dirtypcbs] and costing approximately $25 in total. Once the
design is added to your cart, be sure to increase the *Size* to
*10x10*, or your order will be rejected! You can also choose *Color*,
and optionally increase *Thickness* to *1.6mm* without increasing
purchase cost. Your order will yield 10 PCBs, each containing 4 PC
34-pin adapters and 1 Amstrad 26-pin adapter: 50 in total!

**Custom order (Gerbers):** The Gerber sources for the 10x10cm panel
as in the above DirtyPCBs store link can be downloaded
[here](assets/adapter_rev1/F1_10x10_Gerbers.zip).

**Custom order (KiCad):** The original KiCad PCB design is available in my
[PCB Projects git repository][pcbprojects]. The single-board PC design
is available under *greaseweazle/*, the Amstrad design under *gw-26/*, and
the five-to-a-panel design (as in the DirtyPCBs store link) is under
*panels/GW*. You will need to use KiCad to generate Gerbers.

**Schematic:** You can design your own adapter board based on the
original schematic ([PDF](assets/f1_schematic.pdf)).

## F7 v1

Thanks to George R. Mezzomo for the hardware layouts and collaboration on
schematic design. These designs may be freely reproduced: for example, in
the manufacture of PCBs by your favourite board factory. When making boards
please use the latest version (currently v1.1).

**PCB v1.0:**
- [Schematic](assets/f7_rev1/F7_10_Schematic.pdf) (Note: Incorrect
values for C1,C2,C12,C19,C20,R6)
- [Gerbers](assets/f7_rev1/F7_10_Gerbers.zip)

**PCB v1.1:**
- [Schematic](assets/f7_v1.1/F7_11_Schematic.pdf)
- [Bill of Materials](assets/f7_v1.1/F7_11_Bill_Of_Materials.pdf)
- [Gerbers](assets/f7_v1.1/F7_11_Gerbers.zip)
- Fixes:
  - R1-R4 footprint (0603 rather than 0402)
  - DEBUG header extended to 5x1 to include RST pin
  - USB footprint pin spacing
  - USB connector moved closer to board edge
  - STM32 VBAT connected to VDD
  - Diode orientations marked on PCB
  - Board version added to bottom-side copper
  - Some passive component values fixed in schematic and BoM

## F7 v2

Thanks to George R. Mezzomo for the hardware layout and collaboration on
schematic design. These designs may be freely reproduced: for example, in
the manufacture of PCBs by your favourite board factory.

- [Schematic](assets/f7_v2/F7_v2_Schematic.pdf)
- [Bill of Materials](assets/f7_v2/F7_v2_Bill_Of_Materials.pdf)
- [Gerbers](assets/f7_v2/F7_v2_Gerbers.zip)

## F7 v3

Thanks to George R. Mezzomo for the hardware layout and collaboration on
schematic design. These designs may be freely reproduced: for example, in
the manufacture of PCBs by your favourite board factory.

- [Schematic](assets/f7_v3/F7_v3_Schematic.pdf)
- [Bill of Materials](assets/f7_v3/F7_v3_Bill_Of_Materials.pdf)
- [Gerbers](assets/f7_v3/F7_v3_Gerbers.zip)

## F7 Lightning

Thanks to George R. Mezzomo for the hardware layout and collaboration on
schematic design. These designs may be freely reproduced: for example, in
the manufacture of PCBs by your favourite board factory.

- [Schematic](assets/f7_lightning/F7_Lightning_Schematic.pdf)
- [Bill of Materials](assets/f7_lightning/F7_Lightning_Bill_Of_Materials.pdf)
- [Gerbers](assets/f7_lightning/F7_Lightning_Gerbers.zip)

## F7 Lightning Plus

Thanks to George R. Mezzomo for the hardware layout and collaboration on
schematic design. These designs may be freely reproduced: for example, in
the manufacture of PCBs by your favourite board factory.

- [Assets](assets/f7_lightning_plus/f7_lightning_plus.zip)

## F7 Slim

Thanks to George R. Mezzomo for the hardware layout and collaboration on
schematic design. These designs may be freely reproduced: for example, in
the manufacture of PCBs by your favourite board factory.

- [Schematic](assets/f7_slim/F7_Slim_Schematic.pdf)
- [Bill of Materials](assets/f7_slim/F7_Slim_BoM.pdf)
- [Gerbers](assets/f7_slim/F7_Slim_Gerbers.zip)

## V4

Thanks to George R. Mezzomo for the hardware layout and collaboration on
schematic design. These designs may be freely reproduced: for example, in
the manufacture of PCBs by your favourite board factory.

- [Assets](assets/v4/GW_V4_210511.zip)

## V4 Slim

Thanks to George R. Mezzomo for the hardware layout and collaboration on
schematic design. These designs may be freely reproduced: for example, in
the manufacture of PCBs by your favourite board factory.

- [Assets](assets/v4_slim/v4Slim.zip)

## V4.1

Thanks to George R. Mezzomo for the hardware layout and collaboration on
schematic design. These designs may be freely reproduced: for example, in
the manufacture of PCBs by your favourite board factory.

- [Assets](assets/v4.1/GW_V41_231112.zip)

## Test Jig v2.1

Thanks to George R. Mezzomo for the hardware layout and collaboration on
schematic design. These designs may be freely reproduced: for example, in
the manufacture of PCBs by your favourite board factory.

- [Assets](assets/testjig/greaseweazle-testjig-v2.1.zip)

[f1plusdiy]: https://github.com/solarmon/greaseweazle
[f7plusdiy]: https://github.com/aerobaticant/greaseweazle-F7-Plus
[dirtypcbs]: https://dirtypcbs.com/store/designer/details/keirfraser/6387/greaseweazle-rev-1-panel
[pcbprojects]: https://github.com/keirf/pcb-projects
