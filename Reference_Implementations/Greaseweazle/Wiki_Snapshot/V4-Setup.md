
This page describes hardware setup of the **Greaseweazle V4**. You should
also read the [**Software Installation**](Software-Installation) page to set up
the control software on your host PC, and peruse the **Usage** pages listed in
the wiki sidebar.

To set up your V4 board you will need the following additional items:
- [Floppy drive](#floppy-drive)
- [Floppy data cable](#floppy-data-cable)
- [Floppy power](#floppy-power)
- [USB cable](#usb-cable)

See the following advanced notes on setup:
- [Jumper configuration](#jumper-configuration)
- [Drive terminations](#drive-terminations)
- [External LEDs](#external-leds)

## IMPORTANT NOTE

To avoid damage to your drive or Greaseweazle, please set up your
hardware in the following order:
1. Connect your drive to Greaseweazle before connecting to USB
or external power supply.
2. Connect Greaseweazle to USB power.
3. Switch on drive power, if drive is not powered via Greaseweazle.
4. Disconnection order is the opposite of connection order.

## Additional Items

### Floppy drive

You can connect your V4 to any floppy drive implementing a Shugart
interface: Old PC 3.5-inch and 5.25-inch drives are a good choice, or
an Amstrad 3-inch drive for Amstrad CPC and Spectrum +3 disks.  Note
that, broadly speaking, the drive need not be the exact same model as
in the system to which the disks belong: a PC 3.5-inch drive can read
and write Amiga and ST disks, for example.

An 8-inch drive can be connected via a suitable interface board such
as [FDADAP](http://www.dbit.com/fdadap.html).

Please also note that GCR formats (as used by Apple II, Mac, and
Commodore 64) can be problematic with some floppy drives due
to the non-standard bitcell timings. Unfortunately finding a compatible
drive can be a matter of trial and error.

### Floppy data cable

Your drive connects to Greaseweazle using a standard 34-pin ribbon
cable. If your cable will not plug into the V4, note that some cables
have a blocked pin at each end: pin 5 at the Greaseweazle, and pin 3
at the drive connector.  You can fix this by drilling out the cable's
blocked pin 5, or by carefully cutting and removing pin 5 from the
Greaseweazle connector, or by rooting around for a 34-pin cable without
blocked pins.

By default the V4 boards acts like an IBM-PC controller addressing **Drive A**:
This assumes a PC floppy drive and a ribbon cable with a 'twist' on pins
10-16.

A common alternative setup is a PC drive with straight ribbon cable.
In this case you must select drive **B** (`--drive=b`)

Another common setup is an Amiga, Atari ST, or other vintage drive
which responds to drive-select DS0 (pin 10). In this case you must use
a straight cable and select drive **0** (`--drive=0`).

For further info please
see the documentation for [Drive Select](Drive-Select).

### Floppy power

3.5-inch drives typically require only 5v power and can *usually* be
supplied directly from the power header on the Greaseweazle
board. Older 5.25- and 3-inch drives typically are more power hungry
and require 12v power too: These you must connect to a separate power
source.

If you have problems accessing your drive and you believe your Greaseweazle
is correctly set up, it can be because the drive requires more power than
it can obtain via USB. In this case try connecting your drive to its own
power supply.

For a suitable drive power supply for 3.5- and 5.25-inch drives, search for
*"Molex power supply"*. These usually feature 5V and 12V supply at 2A, and
a full-size Molex power connector; They connect directly to a
5.25" drive, or to a 3.5" drive via a Molex-to-floppy adapter cable.

### USB cable

V4 requires a USB-A to -B cable (commonly known as a "USB printer cable")
to connect to your host PC (Linux, Mac, Windows, etc).
Greaseweazle appears as a serial or modem device, depending on your OS.

## Jumper configuration

Greaseweazle V4 has a 6x2 jumper block through which a number of features
can be accessed:

**WRT.ENA**: From factory these pins are jumpered to allow your Greaseweazle
to write to disk. Remove this jumper to physically disable write support and
provide an extra layer of safety when preserving precious vintage media.

**Firmware Update Mode:** Your V4 will automatically enter firmware-update
mode when requested. However this mode can also be manually forced by placing
a jumper across the TXO-RXI pins.

## Drive terminations

The standard floppy bus is *open collector* with *termination*
(pull-up resistors) at the far receiving end.

The terminations on older 5.25- and 8-inch drives can be as strong as
150 ohms. It is also important that only *one* drive in a bussed setup
has 150-ohm terminations: Greaseweazle V4 cannot drive into multiple
strong pull-ups in parallel.

The strong termination in older drives is usually *optional*
because only the last drive on a ribbon cable is expected
to terminate. The terminating resistors on intermediate drives are
traditionally either disabled by a jumper, or removed entirely.
This correctly terminates the signal lines and also prevents overloading
the drive controller's outputs with excessive pull-up current.
However, if termination is missing entirely then the
drive input signals will float (usually at around 2 volts) with unpredictable
results!

1. If using 3.5-inch and 3-inch drives, this is not a concern. Their
terminations are weaker and cannot be disabled.
2. If using a 5.25- or 8-inch drive on its own, make sure that the
termination resistors are present and enabled.
3. If using a 5.25- or 8-inch drive in a multi-drive setup, you probably
do not need the termination resistors.

Note that an unterminated setup will work with other flux boards such
as Kryoflux and Supercard Pro, which actively drive their outputs both
high and low. Greaseweazle by contrast has standard open-collector
outputs which rely on termination resistors to pull signals high.

## External LEDs

If casing your V4, you may want to use external LEDs in place of the
on-board ones. This can be achieved as follows:
* Power LED:  Connect +ve lead to jumper pin 5V via a suitable resistor.
Connect -ve lead to any jumper pin marked GND.
* Activity LED: Connect +ve lead to jumper pin 5V via a suitable resistor.
Connect -ve lead to jumper pin TXO.
