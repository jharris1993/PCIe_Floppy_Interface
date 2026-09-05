# Pico 2 drive interface — tentative electrical design

Status: discussion proposal, 2026-09-01. Not a fabrication release or a hardware-verified circuit. This supplements the existing requirements; it does not select the final controller architecture. Pico GPIO numbers remain deliberately unassigned.

## Drawings

- `interface-cells.svg` / `.png`: reusable output, input, and configurable-direction circuits.
- `connector-map.svg` / `.png`: channel allocation, connector selection, and power connections.
- `draw_schematic.py`: editable drawing source; generates SVG and PNG using Python and Pillow. This is an electrical concept drawing, not a KiCad netlist; no electrical-rule check has been performed.

## Proposed circuit

Use discrete AO3400A N-channel MOSFETs as inverting open-drain outputs, and SN74LVC14A Schmitt-trigger inverters powered from the Pico's 3.3 V supply as receivers. All cable-side signals stay in the drive's 5 V domain. The Pico only sees 3.3 V logic. Both paths invert, so GPIO high means cable signal asserted low.

The MOSFET gate connects to its GPIO through 100 ohms, with 10 kilohms gate-to-source. Source is grounded; drain connects directly to the signal. A high GPIO asserts the signal. A low or high-impedance GPIO releases it. The pull-down is on the MOSFET side of any jumper. Do not infer suitability of an arbitrary substitute from gate threshold voltage: specify on-resistance at a gate voltage no greater than the actual GPIO high voltage. AO3400A specifies a maximum 48 milliohms at VGS = 2.5 V, at its stated 25 C test condition [S1]. Its switching figures use different gate drive/load conditions from this circuit; they are not a guaranteed board-level timing result.

Receiver: signal -> 100 ohms -> SN74LVC14A input; output -> 100 ohms -> GPIO. The receiver is powered at 3.3 V and accepts inputs up to 5.5 V. At 3.3 V +/- 0.3 V, the datasheet specifies a maximum propagation delay of 6.4 ns over -40 to +85 C, under its test conditions [S2]. Cable assertion produces a rising edge at the GPIO. Configure PIO accordingly, and sample READ DATA and INDEX with known relative timing.

For a role-changing signal, fit both paths and a 3-pin direction header. The centre contact connects to GPIO; one outer contact goes to the transmitter gate resistor, the other to the receiver output resistor. Fit one shunt only, or none for disabled. In receive mode the MOSFET gate pull-down holds the transmitter off. This provides configuration-time direction selection using one GPIO. It does not provide simultaneous transmit/readback. A genuinely bidirectional open-drain protocol would instead require independent TX and RX GPIOs, with the TX released during reception; a push-pull variant requires its own electrical review.

## Connector and channel allocation

Two 34-pin connectors are retained. For this inexpensive proposal, only one connector's signal bank is connected at a time. Seventeen 3-pin port-select headers route the 17 even-numbered signal positions to J1 (PC twisted cable) or J2 (approved alternate interface). Set the entire bank consistently with power off. Ground contacts are shared. This avoids connecting two terminator packs or incompatible signal outputs in parallel. Simultaneous operation on both connectors is not implemented by this proposal and remains an open requirement interpretation.

| Cable pin | PC controller-end interpretation | Alternate interface interpretation | Cell |
|---|---|---|---|
| 2 | Density control, if supported | Drive-specific; unresolved | Configurable |
| 4 | Reserved; disable | Drive-specific; unresolved | Configurable |
| 6 | Reserved; disable | DS4 on SA455/465 | Configurable |
| 8 | INDEX | INDEX / sector pulse where supported | RX |
| 10 | MOTOR A | DS1 on SA455/465 | TX |
| 12 | SELECT B | DS2 on SA455/465 | TX |
| 14 | SELECT A | DS3 on SA455/465 | TX |
| 16 | MOTOR B | MOTOR ON on SA455/465 | TX |
| 18 | DIRECTION | DIRECTION | TX |
| 20 | STEP | STEP | TX |
| 22 | WRITE DATA | WRITE DATA | TX |
| 24 | WRITE GATE | WRITE GATE | TX |
| 26 | TRACK ZERO | TRACK ZERO | RX |
| 28 | WRITE PROTECT | WRITE PROTECT | RX |
| 30 | READ DATA | READ DATA | RX |
| 32 | SIDE SELECT | SIDE SELECT, if supported | TX |
| 34 | DISK CHANGE, if supported | READY or drive-specific status | Configurable |

Signal names describe functions, not mandatory polarities or universal assignments. Check the exact approved drive manual before enabling pins 2, 4, 6, or 34. Conventional odd-numbered contacts are ground; nonstandard use of those positions needs a different adapter. J1 names are at the controller end of the twisted cable; do not apply the cable twist twice in firmware. The alternate map is an example, not approval of every SA455-family or full-height drive.

Total: nine fixed TX, four fixed RX, four configurable channels = seventeen GPIOs. Full population uses thirteen MOSFETs and eight receiver gates (two hex packages). Assign the receiver gates in cable-pin order 2, 4, 6, 8, 26, 28, 30, 34. SN74LVC14A 14-pin packages use A/Y pairs 1/2, 3/4, 5/6, 9/8, 11/10, 13/12; VCC = 14, GND = 7. Ground unused gate inputs and leave their outputs unconnected. Initial build may omit optional transmitter/receiver parts for unused channels. Additional jumper-sense GPIOs are optional and are not included in seventeen.

## Pull-ups and termination

For drive-to-controller lines, provision a removable 1 kilohm pull-up to +5V_IF near the receiver. Fit it for an open-collector output only after checking existing pull-ups and the drive's sink-current rating. At 5 V it draws approximately 5 mA. This is an initial short-cable value, not a universal floppy termination specification. Provide a footprint accepting an alternate value, including 150 ohms / 0.5 W only where the drive output specification permits that load.

For controller-to-drive lines, normally use the drive's existing input termination. Optional local pull-up footprints are DNP unless required by the selected drive; a local bias resistor does not replace specified far-end cable termination. Some older Shugart drives specify 150-ohm input termination and low-level currents up to 40 mA [S3]. At 5.25 V and a 150-ohm -5% resistor, the resistor alone draws about 36.8 mA. Include receiver input current and wiring/ground resistance in the final budget. A nominal 150-ohm resistor dissipates about 0.167 W when low at 5 V.

The selected MOSFET has ample static sink capability for one such load. A conventional LVC open-drain gate is not automatically suitable for this load. SN74LS06 is another plausible driver, but its specified VOL can reach 0.7 V at 40 mA [S4], whereas the cited old drive input specification calls for at most 0.4 V [S3]. The MOSFET avoids relying on typical TTL output saturation voltage. Do not install substantial series resistance in the drain/cable path: 33 ohms at 33 mA would add approximately 1.1 V to the low level.

## Timing assessment

For 250 kbit/s MFM, data-bit time is 4 us and legal transition intervals are 4, 6, or 8 us. Individual cable pulses are much narrower; their required width comes from the drive manual. A proof-of-concept should target clean edges on the order of 100 ns or better where practical and verify the actual read/write pulse widths at the cable connector.

Illustrative lumped-RC estimate: t(10-90%) = 2.2 R C. With an assumed total line capacitance of 100 pF, 1 kilohm gives 220 ns and 150 ohms gives 33 ns. A 10-kilohm pull-up would give 2.2 us. These are estimates, not simulations: actual cable, receiver, MOSFET drain capacitance (voltage-dependent), connector, and probe capacitance must be included. The gate also has a charging delay: AO3400A lists typical Ciss = 630 pF at its test point; 100 ohms alone gives a 63 ns RC time constant, before GPIO impedance and Miller effects. Do not reuse its fast datasheet switching figures as measurements of this circuit. Tune gate resistance/pulse programming based on scope measurements, or use a lower-charge, suitably specified MOSFET or gate buffer if necessary.

The receiver delay is comfortably below floppy bit periods. The output path is a credible DD prototype, but its pulse distortion and cable settling remain to be measured. PIO must generate edges and pulse widths; firmware should not bit-bang WRITE DATA under interrupts. Do not add debounce or large filter capacitors to READ DATA, WRITE DATA, or INDEX.

## Power and startup

Power the Pico through its USB connector for the prototype. Power receiver VCC from Pico 3V3(OUT). Obtain regulated +5V_IF from the same supply domain as the drive's 5 V electronics; drive power remains on the drive's separate power connector. Add any required 12 V there, according to the drive manual. Do not connect external +5V_IF to Pico VBUS or 3V3. All grounds are common; route motor power return separately from the interface return until the supply connection.

Fit 100 nF ceramic at each receiver IC and about 4.7 uF bulk on each local rail. Keep cable/ground connections short and retain the ribbon's ground conductors. No hot-plug or surge-protection qualification is claimed. The design assumes an internal, correctly wired 5 V drive interface; external/long-cable or odd-pin variants need explicit protection review.

Fit a removable WRITE ARM link in series with the WRITE GATE GPIO path, ahead of the gate resistor. Default is removed. Its MOSFET pull-down remains connected. This inhibits writes during bring-up even if firmware misconfigures the GPIO. On startup, set all TX data latches low before switching GPIOs to output, disable internal pull-ups on TX pins, and only arm writes after drive configuration. A hardware watchdog/write timeout is not implemented by this tentative circuit.

## Verification before drive testing

1. Confirm exact drive connector directions, termination, voltage limits, and pulse requirements.
2. Confirm the GPIO map suits the intended PIO programs and that jumpers match firmware configuration.
3. Test each TX into the expected pull-up load; measure VOL, pulse width, release time, and ringing, including worst simultaneous control states.
4. Test RX with realistic open-collector pulses; measure threshold crossing, polarity, and timing at the GPIO.
5. Check power-up/reset and disconnected-Pico behavior, with WRITE ARM removed. Check both selected/unselected connector banks.
6. Read known-good DD disks, then write expendable media and verify on an independent controller.

Completed for this proposal: datasheet review, DC/RC estimates, generated-drawing inspection. Not completed: SPICE simulation, EDA/ERC, PCB layout, oscilloscope measurements, or hardware read/write testing.

## Sources

- **S1:** [Alpha & Omega AO3400A datasheet](https://www.aosmd.com/sites/default/files/res/datasheets/AO3400A.pdf), Rev 3.1, July 2023, pp. 1-2: package, RDS(on), capacitance and switching conditions.
- **S2:** [TI SN74LVC14A datasheet](https://www.ti.com/lit/ds/symlink/sn74lvc14a.pdf), SCAS285AC, April 2022, sections 5, 6.4, 6.7, 6.9: pinout, voltage limits, thresholds, timing.
- **S3:** [Shugart SA455/465 manufacturer service manual, reproduced by ManualsLib](https://www.manualslib.com/manual/4220043/Shugart-Minifloppy-Sa455.html?page=18), sections 2.2.1-2.2.2, viewer pages 18-19: input current, low level, and 150-ohm termination. This is an illustrative legacy load; the actual proof-of-concept drive remains unspecified.
- **S4:** [TI SN74LS06 datasheet](https://www.ti.com/lit/ds/symlink/sn74ls06.pdf), SDLS020F, July 2016, section 6.5: VOL at specified sink currents.
- [Pico 2 datasheet](https://datasheets.raspberrypi.com/pico/pico-2-datasheet.pdf), release 5, July 2026, sections 3.1 and 5: board I/O and power connections.

Hardware drawings are under the repository's CERN-OHL-S-2.0 license. Drawing generator is under GPL-3.0-or-later.
