This project is cross-compiled on an x86 Ubuntu Linux system. However
other similar Linux-base systems (or a Linux virtual environment on
another OS) can likely be made to work quite easily.

To install the prerequisites:
```
sudo apt install git gcc-arm-none-eabi python3-pip srecord stm32flash zip
python3 -m pip install --user bitarray crcmod pyserial requests
```

To build the firmware, producing a distribution folder and zip
archive:
```
git clone https://github.com/keirf/greaseweazle-firmware.git
cd greaseweazle-firmware
make dist
```

If you wish to build firmware incrementally, for example for development
testing, then you can build all targets as follows (you can modify or
remove the `-j8` parameter to adjust build parallelism):
```
make -j8
```

You will now find HEX files for flashing at:
```
out/<mcu>/<level>/greaseweazle/target.hex
<mcu> := at32f4 | stm32f1 | stm32f7
<level> := debug | prod
```

You can flash the relevant HEX to your Greaseweazle via
serial or ST-Link. The `flash` and `ocd` build targets may be
useful for automatically doing this on Linux, via
serial adapter or OpenOCD/ST-Link.

If you require debug logging over the serial line at 3Mbaud then
use the HEX file within the relevant `debug` folder.

For example, to build and automatically flash the F7 firmware with
debug logging to an attached Greaseweazle via ST-Link and OpenOCD:
```
make -j8 ocd target=stm32f7/debug
```
