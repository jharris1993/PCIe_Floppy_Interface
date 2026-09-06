
Installation steps depend on your host OS:
- [Windows](#windows)
- [macOS](#macos)
- [Linux](#linux)

## Windows

Greaseweazle is packaged as a Windows executable, hence there are no
extra application components to download or install. Simply
[download](Download-Host-Tools) the Greaseweazle host software, unzip,
and run it in place from a CMD window.

Greaseweazle uses Microsoft's **usbser.sys** device driver. The steps
to install the driver depend on your Windows OS version.

**Windows 10 & 11:** The correct driver is automatically installed.

**Windows 8.1:** The driver must be manually installed as follows:
1. Download and install [**Zadig**][zadig]
2. Connect Greaseweazle via USB
3. Start Zadig
4. Select "*List all devices*" from the Options pull-down menu
5. Select "*Greaseweazle*" in the dropdown list
6. Select "*USB Serial (CDC)*" as the driver
7. Select "*Install driver*" or "*Replace driver*"

From now on Greaseweazle will automatically appear as a **COM** device
(typically **COM3**). To test correct connection to Greaseweazle hardware:
```
gw info
```

After installing the Greaseweazle command-line tools, you may be interested
in a Windows GUI wrapper. There are two available, maintained by third parties:
- [FluxMyFluffyFloppy][fmffgui] (Frank Bopple)
- [GreaseweazleGUI][ggui] (Don Mankin)

## macOS

Greaseweazle tools are installed as a Python 3 package from the command line.

To install Python 3 and Xcode tools:
```
xcode-select --install
brew install python
```

If available, the easiest way to install Greaseweazle is using pipx:
```
brew install pipx
pipx ensurepath
pipx install git+https://github.com/keirf/greaseweazle@latest
```

If pipx is unavailable, you can instead install into your system Python
environment:
```
python3 -m pip install git+https://github.com/keirf/greaseweazle@latest
```

When you connect Greaseweazle it will automatically appear as a
**/dev/cu.usbmodem** device.

To test correct connection to Greaseweazle hardware:
```
gw info
```

## Linux

Greaseweazle tools are installed as a Python 3 package from the command line.

To install Python 3 and C compiler on Ubuntu and other Debian-derived Linux:
```
sudo apt install gcc python3-pip python3-dev
```

If available, the easiest way to install Greaseweazle is using pipx:
```
sudo apt install pipx
pipx ensurepath
pipx install git+https://github.com/keirf/greaseweazle@latest
```

If pipx is unavailable, you can instead install into your system Python
environment:
```
python3 -m pip install git+https://github.com/keirf/greaseweazle@latest
```

To make the Greaseweazle device accessible as a normal user, and to
avoid conflicts with ModemManager under Ubuntu Linux, you need
to add some udev rules (included in the
[release download](Download-Host-Tools)) before connecting the Greaseweazle:
```
sudo cp scripts/49-greaseweazle.rules /etc/udev/rules.d/.
```

When you connect Greaseweazle it will automatically appear as a
**/dev/ttyACM** device (typically **/dev/ttyACM0**). To test correct
connection to Greaseweazle hardware:
```
gw info
```

If you install the Ubuntu udev rules, Greaseweazle should also appear
as **/dev/greaseweazle** (this is a symlink to the correct ttyACM device).

[fmffgui]: https://github.com/FrankieTheFluff/FluxMyFluffyFloppy
[ggui]: https://desertsagesolutions.com/greaseweazlegui
[bitarray]: https://www.lfd.uci.edu/~gohlke/pythonlibs/#bitarray
[zadig]: https://zadig.akeo.ie/
