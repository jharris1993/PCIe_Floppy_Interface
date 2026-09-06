
**NOTE: If you received a pre-assembled adapter then
you can skip straight to [Hardware Setup](Hardware-Setup).**

- [Parts List](#parts-list)
- [Assembly Guidance](#assembly-guidance)
- [Firmware Programming](Firmware-Programming)

## Parts List

You should obtain (or have received) the following parts, in addition
to the Greaseweazle PCB. Note that kits may include
an excess quantity of the "passives" (resistors, capacitors).

Board Reference | Footprint | Value/Type | Quantity
----------|------|-------|---------
C1-C2,C4,C6,C10-C14 | 0603 | 100nF | 9
C3        | 0805 | 4.7uF | 1
C5,C7-C8  | 0805 | 1uF   | 3
C9,C15    | 0805 | 10uF  | 2
 | | | 
R1-R2     | CAY16 | 10k  | 2
R4        | 0603  | 470  | 1
 | | | 
U1        | LQFP64 | STM32F730R8 | 1
U2        | SOT25 | AP2112K-3 | 1
 | | | 
ACT       | 0603 | LED | 1
DEBUG | 6x1 | Pin Header | 1
RESET, WRITE_INHIBIT | 2x1 | Pin Header | 2
FLOPPY DATA | 26x1mm | FFC Connector | 1
USB       | USB-B | | 1
XO1       | 4-SMD | ECS-3225MV-160 | 1

## Assembly Guidance

Please note that the small size and pitch of some components, particularly
U1, means that you will need some soldering proficiency, and
equipment such as the following:
- A workbench with decent lighting
- Moderate magnification (eg. a magnifying bench light)
- Good quality leaded (60/40) solder (eg. Stannol, Kester)
  - **Avoid lead-free solder!**
- Plenty of flux
- Tweezers

Although not a step-by-step guide, I will note some caveats.

1. The kit comes with the STM32 chip placed in a fold of antistatic
material, taped to the PCB. Be warned, the chip will be loose when you
peel the tape!

2. The LED cathode terminal is marked by a green dot under the lens,
which should be oriented towards the STM32 chip.

3. The 10k resistor arrays are tight on their pads. Be careful
that they are correctly aligned.

4. XO1 should be soldered with hot air: The pads are too small for safe
hand soldering.

5. Pin 1 of the floppy connector is towards the USB end of the board. Do
not connect the wrong way round!
