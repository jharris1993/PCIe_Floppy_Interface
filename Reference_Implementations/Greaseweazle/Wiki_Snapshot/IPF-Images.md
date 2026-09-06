
Greaseweazle optionally supports reading IPF image files via the CAPS/SPS
library, which must be installed in your Greaseweazle folder, or in a
standard system location.

On Windows the CAPS/SPS library is installed automatically alongside the
Greaseweazle executable. On other platforms the
library should be downloaded from the [SPS website][sps].

Please note that the library supports *read-only* access to IPF images: it
is not possible to create new IPF image files.

## Windows

Installed automatically. No further steps required.

## macOS

**Intel:**
1. Download version 4.2 for Mac OS X
([ipflib42_macosx-universal.dmg.zip][sps-mac]).
2. Copy the `CAPSImage.framework` folder to `/Library/Frameworks`.

**M1, M2 (ARM64):**
1. Download version 5.1 for Mac OS X on ARM64
([CAPSImg_5.1.3_macOS_ARM64.tar.xz][fsuae-macos]).
2. Copy the `CAPSImg.framework` folder to `/Library/Frameworks`.

When you first attempt to use the library you may see a dialog appear stating
*"CAPSImage.framework" cannot be opened because the developer cannot be
verified*. In this case:
1. Press **Cancel**
2. Run **Setting** -> **Security**. Click on **Allow Anyway**.
3. Run Greaseweazle again. If the dialog reappears, click **Open**.

## Linux

Download version 4.2 for 32-bit ([ipflib42_linux-i686.tar.gz][sps-linux32])
or 64-bit ([ipflib42_linux-x86_64.tar.gz][sps-linux64]) Linux as appropriate.
The file `libcapsimage.so.4.2` should be installed to a standard system-wide
location. For example (as root):
```
cp libcapsimage.so.4.2 /usr/lib
ldconfig
```
Alternatively set environment variable `LD_LIBRARY_PATH` to the location
of the library. For example, if the library is in the current working
directory:
```
export LD_LIBRARY_PATH=`pwd`
```

[sps]: http://softpres.org/download
[sps-w32]: http://softpres.org/_media/files:ipflib42_w32.zip
[sps-mac]: http://softpres.org/_media/files:ipflib42_macosx-universal.dmg.zip
[sps-linux32]: http://softpres.org/_media/files:ipflib42_linux-i686.tar.gz
[sps-linux64]: http://softpres.org/_media/files:ipflib42_linux-x86_64.tar.gz
[fsuae-macos]: https://fs-uae.net/download#macosx
