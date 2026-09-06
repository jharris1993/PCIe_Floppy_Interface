
- **Greaseweazle is not detected by my host PC**
  - Test your USB cable with another device. Charging-only micro USB
  cables which
  omit the data wires are very common and will
  not work to connect Greaseweazle (or any other device) to your PC.
  - If the activity LED blinks a repeated pattern, see the
    next question in the FAQ.
  - **F1 only:** Check the resistance between Blue Pill pins **A12**
  and **3.3**. If this is not 1.5k ohms then you should remove Blue
  Pill surface-mounted resistor R10 and manually connect a 1.5k
  resistor between **A12** and **A0**.
  - **F1 only:** Be aware of [STM32 fake chips](STM32-Fakes) which do
      not work properly.
  - **Linux only:** Have you previously installed Kryoflux software? Then
      please [read this](https://github.com/keirf/greaseweazle/discussions/312).

- **Greaseweazle blinks the activity LED and is not detected via USB**
  - Greaseweazle performs a power-on self test and blinks a diagnostic
  code on failure:
    - **1 blink:** Board version straps are unstable.
      Check for bad soldering around those pins (PC13-15).
    - **2 blinks:** Board version straps not recognised. Check you're
      loading the latest firmware.
    - **3 blinks:** Oscillator failed to start up. Check the external
      oscillator.
    - **4 blinks:** Unrecognised or incorrect microcontroller chip.

- **Commands fail with 'Track 0 not found' or 'No Index'**
  - The default drive is **A**, which assumes
  a PC drive (drive-select DS1, pin 12) and a ribbon cable with
  a twist across pins 10-16.
  - A common alternative setup is a PC drive with straight ribbon cable.
  In this case you must select drive **B** (`--drive=b`)
  - Another common setup is an Amiga, Atari ST, or other vintage drive
  which responds to drive-select DS0 (pin 10). In this case you must use
  a straight cable and select drive **0** (`--drive=0`).
  - For further info please
  see the documentation for [Drive Select](Drive-Select).

- **Commands still fail with 'Track 0 not found'**
  - Confirm that your ribbon cable is the correct way round.
    - Look for pin 1 on the Greaseweazle and for pin 1 on the drive.

- **Commands still fail with 'No Index'**
  - Check your drive connections again.
  - Check that you have a disk inserted in your drive.
  - Check whether your drive requires 12-volt power.
    - If so you will need an external power supply to spin the motor.

- **Writes fail with 'Failed to verify Track 0.0'**
  - Check that your disk media is good.
  - Can you read disks okay with your setup? If not, write verification
    cannot possibly succeed.
  - Check the write-enable jumper on your Greaserweazle board.

- **Commands fail with 'ImportError: urllib3 v2.0 only supports OpenSSL 1.1.1+, [...]'**
  - Downgrade Python's urllib3 to v1.x. For example: `python3 -m pip install "urllib3<2"`
