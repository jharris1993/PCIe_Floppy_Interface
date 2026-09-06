**The following is a getting started guide contributed by Yann Serra**

Greaseweazle is a hardware and software solution that lets you archive
or regenerate old floppy disks. Reading them is useful for recovering
old data or forgotten programs that you can use in your favourite
emulators. And writing them is useful for collectors who need real boot,
game or application floppy disks to run authentic machines from the 70s,
80s and 90s.

To start, you obviously need a Greaseweazle board, since the gw software
provided here runs with it only. See [where to purchase a Greaseweazle
board](https://github.com/keirf/greaseweazle/wiki/Purchase-a-Greaseweazle).

Then, you need some floppy drives.

### Compatible with any standard floppy drive

The Greaseweazle board is compatible with any Shugart or IBM standard
floppy drive, that includes any 3.5 and 5.25-inch drive with a 34-pin
connector, or a 3-inch "Amstrad" drive with a 26-pin connector (actually
just a shorten 34-pin connector: same signals on same pins, just the
no-signal pins are missing), or a 8-inch drive with a 50-pin connector
(extended 34 pin connector with irrelevant signals). You need an extra
adaptor to connect 26-pin or 50-pin drives to the Greaseweazle’s 34-pin
connector.

Commodore (excluding Amiga) and Apple drives (including Macintosh),
which use a proprietary connection, are not supported. But you can
read/write Commodore 8-bit and Apple II/Mac floppy disks with most
regular 34 pin drives.

**Important Note:** GCR formats (as used by Apple II, Mac, and
Commodore 64) can be problematic with some floppy drives due
to the non-standard bitcell timings. Unfortunately finding a compatible
drive can be a matter of trial and error.

### Two IBM drives, or four Shugart drives supported on the same cable

The Greaseweazle solution supports two IBM drives or three Shugart
drives on the same cable.

If the drives are of "IBM" standard (any drive coming from a
MS-Dos/Windows machine), then you use a ribbon cable with a twist: the
drive on the edge will be drive A, and the drive in the middle connector
will be drive B.

If your drives are Shugart standard from any computer before mid-90's
(Amiga, Atari, Acorn…), then you use a flat ribbon cable, and tells
which drive is unit \# 0, 1, 2 or 3 by moving their configuration jumpers
accordingly (located near their rear, where it’s written
“DS0/DS1/DS2/DS3”).

See [here](https://github.com/keirf/greaseweazle/wiki/Drive-Select) for
a more in-depth explanation of how to connect them.

### Three levels of access for reading or writing any floppy disk

Depending on the disk image you wish to create (from a floppy disk) or
restore (to a floppy disk), the Greaseweazle solution can access three
levels of information on a floppy disk: the user content in the sectors,
the formatted tracks, or the flux of polarised information on the
surface.

**Sectors:** a floppy disk is made up of tracks, themselves subdivided
into sectors, which contain the data directly accessible to users. It is
this data that makes up the content of disk images in block mode (.img,
.st, .dsk, .adf...).

**Formatted tracks:** for each floppy disk format, the tracks contain a
particular number of sectors, of a particular size, with a particular
identification in some headers, and gaps of a certain size between all
these elements. In some case, there are also intentional identification
errors as a form of copy-protection. All these details are stored in
'meta' images (.edsk, .imd...) that can tell which floppy disk format
they contain. It matters, for instance, in case of Amstrad or CP/M
computers that use several formatting variants.

**Flux:** Information is encoded in the form of magnetic pulses on the
surface of floppy disks. Disk images such as .scp or .hfe store these
pulses regardless of the encoding used, thereby preserving an exact copy
of an original floppy disk, even with its intentional encoding errors
that constituted the most advanced copy protections.

### How to use it, level \#1: the simplest/new-comer way

After [having
downloaded](https://github.com/keirf/greaseweazle/wiki/Download-Host-Tools)
and
[installed](https://github.com/keirf/greaseweazle/wiki/Software-Installation)
the gw command line (it's just Python3 code, so it works on every modern
system, including Raspberry Pis), you backup a physical disk to an image
file with :

```
gw read --format=<profile.of.your.floppy.disk> <name_of_your_image.suffix> --drive=<ID>
```

For example:

```
gw read --format=amiga.amigados MyAmigaDisk.adf --drive=A
```
…will backup the physical Amiga disk you inserted into the drive, that
is located at the end of your twisted cable, to a file named
“MyAmigaDisk.adf”, in the current directory.

In some circumstances, you can omit the --format and the --drive
options. For instances, the drive A being the default choice, and .adf
disk images being most often a backup of an Amiga 880KB disk format, you
can type here:  

```
gw read MyAmigaDisk.adf
```

To generate some content to a physical disk from a disk image, you just
replace the “read” argument with “write”, like this:

```
gw write --format=amiga.amigados MyAmigaDisk.adf --drive=A
```

In the above commands, what you tell after the “--format=” option is
just the name of a predefined profile matching one of the many software
formats that computer brands defined for their disks systems. Thanks to
this profile, the gw command can check the content is read or written
without error.

You should also take care about the suffix you put as the extension of
your image name (“.adf”, for instance), as it defines the preferred disk
image format for the floppy disk you are working with.

Here are some tables that would help you to find which predefined
profile you should use for the floppy disk format you want to backup to
disk image or to recreate from a disk image. And also, the preferred
suffix your disk image should have according to the profile.

| **3.5-inch disks**  | **profile**          | **sides** | **cyls** | **RPM** | **kbit/s** | **sct/trk** | **byt/sct** | **encoding** | **size (KB)** | **suffix**   |
|---------------------|----------------------|-----------|----------|---------|------------|-------------|-------------|--------------|---------------|--------------|
| Acorn BBC           | acorn.adfs.320       | 1         | 80       | 300     | 250        | 16          | 256         | MFM          | 320           | .adm         |
|                     | acorn.adfs.640       | 2         | 80       | 300     | 250        | 16          | 256         | MFM          | 640           | .adl         |
| Archimedes          | acorn.adfs.800       | 2         | 80       | 300     | 250        | 5           | 1024        | MFM          | 800           | .adf         |
| RiscPC              | acorn.adfs.1600      | 2         | 80       | 300     | 500        | 10          | 1024        | MFM-HD       | 1600          | .adf         |
| Amiga               | amiga.amigados       | 2         | 80       | 300     | 250        | 11          | 512         | AMFM         | 880           | .adf         |
|                     | amiga.amigados\_hd   | 2         | 80       | 300     | 500        | 22          | 512         | AMFM-HD      | 1760          | .adf         |
| Atari ST            | atarist.360          | 1         | 80       | 300     | 250        | 9           | 512         | MFM          | 360           | .st, .msa    |
|                     | atarist.400          | 1         | 80       | 300     | 250        | 10          | 512         | MFM          | 400           | .st, .msa    |
|                     | atarist.440          | 1         | 80       | 300     | 261        | 11          | 512         | MFM          | 440           | .st, .msa    |
|                     | atarist.720          | 2         | 80       | 300     | 250        | 9           | 512         | MFM          | 720           | .st, .msa    |
|                     | atarist.800          | 2         | 80       | 300     | 250        | 10          | 512         | MFM          | 800           | .st, .msa    |
|                     | atarist.880          | 2         | 80       | 300     | 261        | 11          | 512         | MFM          | 880           | .st, .msa    |
| C64/C128            | commodore.1581       | 2         | 80       | 300     | 250        | 10          | 512         | MFM          | 800           | .d81         |
| IBM PC              | ibm.720              | 2         | 80       | 300     | 250        | 9           | 512         | MFM          | 720           | ..img        |
| (Sam Coupé)         | ibm.800              | 2         | 80       | 300     | 250        | 10          | 512         | MFM          | 800           | .img, (.mgt) |
| (Macintosh HD)      | ibm.1440             | 2         | 80       | 300     | 500        | 18          | 512         | MFM-HD       | 1440          | .img, (.dsk) |
|                     | ibm.1680             | 2         | 80       | 300     | 500        | 21          | 512         | MFM-HD       | 1680          | .img         |
|                     | ibm.dmf              | 2         | 80       | 300     | 500        | 21          | 512         | MFM-HD       | 1680          | .img         |
|                     | ibm.2880             | 2         | 80       | 300     | 1000       | 36          | 512         | MFM-ED       | 2880          | .img         |
| Macintosh 68K       | mac.400              | 1         | 80       | VAR     | 375        | 12-8        | 512         | GCR          | 400           | .dsk         |
|                     | mac.800              | 2         | 80       | VAR     | 375        | 12-8        | 512         | GCR          | 800           | .dsk         |
| MSX                 | msx.1dd              | 1         | 80       | 300     | 250        | 9           | 512         | MFM          | 360           | .dsk         |
|                     | msx.2dd              | 2         | 80       | 300     | 250        | 9           | 512         | MFM          | 720           | .dsk         |
| Nec PC98            | pc98.2hs             | 2         | 81       | 300     | 500        | 9           | 1024        | MFM-HD       | 1458          | .hdm, .xdf   |
| Piano               | akai.800             | 2         | 80       | 300     | 250        | 5           | 1024        | MFM          | 800           | .img         |
|                     | akai.1600            | 2         | 80       | 300     | 500        | 10          | 1024        | MFM-HD       | 1600          | .img         |
|                     | ensoniq.mirage       | 1         | 80       | 300     | 250        | 5+1         | 1K+512      | MFM          | 440           | .img         |
|                     | ensoniq.800          | 2         | 80       | 300     | 250        | 10          | 512         | MFM          | 800           | .img         |
|                     | ensoniq.1600         | 2         | 80       | 300     | 500        | 20          | 512         | MFM-HD       | 1600          | .img         |
|                     | gem.1600             | 2         | 80       | 300     | 500        | 20          | 512         | MFM-HD       | 1600          | .img         |
|                     | sci.prophet          | 2         | 80       | 300     | 250        | 5           | 1024        | MFM          | 800           | .img         |
| ZX Spectrum         | zx.trdos.640         | 2         | 80       | 300     | 250        | 16          | 256         | MFM          | 640           | .mgt, .dsk   |
|                     | zx.quorum.800        | 2         | 80       | 300     | 250        | 5           | 1024        | MFM          | 800           | .mgt, .dsk   |
| MicroWare OS-9      | mm1.os9.80ds.hd32spt | 2         | 80       | 300     | 500        | 32          | 256         | MFM-HD       | 1280          | .img         |
|                     | mm1.os9.80ds.hd36spt | 2         | 80       | 300     | 500        | 36          | 256         | MFM-HD       | 1440          | .img         |
|                     |                      |           |          |         |            |             |             |              |               |              |
| **5.25-inch disks** | **profile**          | **sides** | **cyls** | **RPM** | **kbit/s** | **sct/trk** | **byt/sct** | **encoding** | **size (KB)** | **suffix**   |
| Acorn Atom          | acorn.dfs.ss         | 1         | 40       | 300     | 125        | 10          | 256         | FM           | 100           | .ssd         |
|                     | acorn.dfs.ds         | 2         | 40       | 300     | 125        | 10          | 256         | FM           | 200           | .dsd         |
| BBC                 | acorn.adfs.160       | 1         | 40       | 300     | 250        | 16          | 256         | MFM          | 160           | .ads         |
|                     | acorn.adfs.320       | 1         | 80       | 300     | 250        | 16          | 256         | MFM          | 320           | .adm         |
|                     | acorn.adfs.640       | 2         | 80       | 300     | 250        | 16          | 256         | MFM          | 640           | .adl         |
| Atari 800           | atari.90             | 1         | 40       | 288     | 125        | 18          | 128         | FM           | 90            | .img         |
| Vic20/C64           | commodore.1541       | 1         | 35       | 300     | VAR        | 21-17       | 256         | GCR          | 170           | .d64         |
| /C128               | commodore.1571       | 2         | 35       | 300     | VAR        | 21-17       | 256         | GCR          | 340           | .d71         |
| Dragon 32/64        | dragon.40ss          | 1         | 40       | 300     | 250        | 18          | 256         | MFM          | 180           | .img         |
|                     | dragon.40ds          | 2         | 40       | 300     | 250        | 18          | 256         | MFM          | 360           | .img         |
|                     | dragon.80ss          | 1         | 80       | 300     | 250        | 18          | 256         | MFM          | 360           | .img         |
|                     | dragon.80ds          | 2         | 80       | 300     | 250        | 18          | 256         | MFM          | 720           | .img         |
| IBM PC              | ibm.160              | 1         | 40       | 300     | 250        | 8           | 512         | MFM          | 160           | .img, .ima   |
|                     | ibm.180              | 1         | 40       | 300     | 250        | 9           | 512         | MFM          | 180           | .img, .ima   |
|                     | ibm.320              | 2         | 40       | 300     | 250        | 8           | 512         | MFM          | 320           | .img, .ima   |
|                     | ibm.360              | 2         | 40       | 300     | 250        | 9           | 512         | MFM          | 360           | .img, .ima   |
|                     | ibm.1200             | 2         | 80       | 360     | 500        | 15          | 512         | MFM-HD       | 1200          | .img         |
| Luxor ABC           | luxor.80             | 1         | 40       | 300     | 250        | 8           | 256         | FM           | 80            | .img         |
|                     | luxor.160            | 1         | 40       | 300     | 250        | 16          | 256         | MFM          | 160           | .img         |
|                     | luxor.320            | 2         | 40       | 300     | 250        | 16          | 256         | MFM          | 320           | .img         |
|                     | luxor.640            | 2         | 80       | 300     | 250        | 16          | 256         | MFM          | 640           | .img         |
| MSX                 | msx.1d               | 1         | 40       | 300     | 250        | 9           | 512         | MFM          | 180           | .dsk         |
|                     | msx.2d               | 2         | 40       | 300     | 250        | 9           | 512         | MFM          | 360           | .dsk         |
| Nec PC88/PC98       | pc98.2d              | 2         | 40       | 300     | 250        | 8           | 512         | MFM          | 320           | .hdm, .xdf   |
|                     | pc98.2dd             | 2         | 77       | 360     | 250        | 8           | 512         | MFM          | 616           | .hdm, .xdf   |
|                     | pc98.n88basic.hd     | 2         | 77       | 360     | 500        | 26          | 256         | MFM-HD       | 998           | .hdm, .xdf   |
|                     | pc98.2hd             | 2         | 77       | 360     | 500        | 8           | 1024        | MFM-HD       | 1232          | .hdm, .xd    |
| CP/M - Osborne 1    | occ1.sd              | 1         | 40       | 300     | 125        | 10          | 256         | FM           | 100           | .img         |
|                     | occ1.dd              | 1         | 40       | 300     | 250        | 5           | 1024        | MFM          | 200           | .img         |
| Olivetti M20        | olivetti.m20         | 2         | 35       | 300     | 250        | 16          | 256         | MFM          | 278           | .img         |
| Tandy CoCo          | coco.decb            | 1         | 35       | 300     | 250        | 18          | 256         | MFM          | 157.5         | .img         |
|                     | coco.decb.40t        | 1         | 40       | 300     | 250        | 18          | 256         | MFM          | 180           | .img         |
|                     | coco.os9.40ss        | 1         | 40       | 300     | 250        | 18          | 256         | MFM          | 180           | .img         |
|                     | coco.os9.40ds        | 2         | 40       | 300     | 250        | 18          | 256         | MFM          | 360           | .img         |
|                     | coco.os9.80ss        | 1         | 80       | 300     | 250        | 18          | 256         | MFM          | 360           | .img         |
|                     | coco.os9.80ds        | 2         | 80       | 300     | 250        | 18          | 256         | MFM          | 720           | .img         |
| TSC Flex            | tsc.flex.ssdd        | 1         | 80       | 300     | 250        | 18          | 256         | MFM          | 358           | .img         |
|                     | tsc.flex.dsdd        | 2         | 80       | 300     | 250        | 18          | 256         | MFM          | 715           | .img         |
|                     |                      |           |          |         |            |             |             |              |               |              |
| **8-inch disks**    | **profile**          | **sides** | **cyls** | **RPM** | **kbit/s** | **sct/trk** | **byt/sct** | **encoding** | **size (KB)** | **suffix**   |
| DEC RX              | dec.rx01             | 1         | 77       | 360     | 250        | 26          | 128         | FM           | 250.25        | .img         |
| (PDP-11/VAX)        | dec.rx02             | 1         | 77       | 360     | 250        | 26          | 256         | M2FM         | 500,5         | .img         |
| Luxor ABC           | luxor.1000.data      | 2         | 77       | 360     | 500        | 26          | 256         | MFM          | 1000          | .img         |
|                     | luxor.1000.program   | 2         | 77       | 360     | 500/250    | 26          | 256/128     | MFM/FM       | 1000          | .img         |
|                     | luxor.1000.abcnet    | 1         | 77       | 360     | 500/250    | 26          | 256/128     | MFM/FM       | 1000          | .img         |
|                     |                      |           |          |         |            |             |             |              |               |              |
| **3-inch disks**    | **profile**          | **sides** | **cyls** | **RPM** | **kbit/s** | **sct/trk** | **byt/sct** | **encoding** | **size (KB)** | **suffix**   |
| Sega SC-3000        | sega.sf7000          | 1         | 40       | 300     | 250        | 16          | 256         | MFM          | 160           | .sf7         |

The gw command does an honest job at supporting dozens of disk formats
and image formats, but it doesn’t directly support all of them yet. This
list keeps evolving. To know all the possible disk format profiles and
disk image suffixes supported by your latest version of the gw command,
just type:  

```
gw read --help
```

Don't despair if you don’t see the profile of your floppy disk in the
list. Predefined profiles are just shortcuts for working with specific
formats. Right now, Greaseweazle offers other ways of saving and
recreating all your floppy disks.

### Level \#2: Troubleshooting common errors

Here are the few common errors many beginners encounter and how you can
resolve them:

**<span class="underline">Error “No Index”:</span>**

**Symptom:** The gw command has asked the drive to start its motor, but
the drive never confirms that the floppy disk is actually spinning.

**Probable cause:** you have not specified the correct drive unit in the
command line.

**Solution:** add "--drive=" to the command line and specify the correct
ID. This could be:

--drive=a when you are using the PC drive at the end of the cable, on a
cable with a twist.

--drive=b: when you are using the PC drive in the middle of the cable,
on a cable with a twist.

--drive=0, or 1, or 2: on a flat cable (without any twist), when you are
using the drive whose plastic jumpers (on the rear) configure the DS0,
DS1 or DS2 unit respectively.

Special case: when you connect a PC drive (without plastic jumpers) to a
flat cable, it always has unit DS1 (--drive=1).

**Other possible causes:** there is no power supply for the drive, you
plug the ribbon cable upside-down, you forgot to insert a floppy disk
into the drive.

**<span class="underline">Error “Track 0 not found”:</span>**

**Symptom:** the drive has been selected, but something is missing to
tell that it has managed to position its head on track 0.

**Probable cause:** the drive doesn't have enough power to operate
normally.

**Solution:** the power source needs to be changed. Either:

\- if the drive is powered by the Greaseweazle board, plug the
Greaseweazle board into another USB port.

\- if the drive is powered by an external power source (power supply,
self-powered USB hub, etc.), unplug the other devices connected to this
power source.

\- If the error persists, supply your drive with a more efficient power
source.

**Other possible causes:** When several drives are attached on the
ribbon cable, this error can also be caused by a wrong drive selection.
Check the solution given for the “No Index” error in this case.

**<span class="underline">Errors “Flux Overflow” or “Flux
Underflow”</span>**

**Symptom:** The data from the Greaseweazle board is not arriving at the
right speed.

**Probable cause:** there is interference in the USB connection.

**Solution:** plug the Greaseweazle card into another USB port on your
computer. If no USB port solves the problem, change your USB cable.

**<span class="underline">Errors: “Verify Failure”, “Failed to verify
Track”</span>**

**Symptom:** When writing, something is preventing a certain area on the
surface of your diskette from storing information correctly.

**Probable cause:** there is mould on the surface of your floppy disk.

**Solution:** gently clean the surface of your floppy disk with a
microfibre cloth soaked in 70% Isopropyl alcohol. Unfortunately, the
result is not guaranteed. If the errors keep recurring on other
diskettes, clean the heads of your drive too.

For more troubleshooting, see [this
page](https://github.com/keirf/greaseweazle/wiki/Troubleshooting-FAQ).

### Level \#3: more disk formats with meta-profiles and meta-disk images

The gw command also provides 'metaprofiles' which, without necessarily
referring to a particular type of formatting, capture all the sectors
present on a floppy disk, whatever their number, size, numbering scheme
or formatting bytes used. These metaprofiles are called:

**- ibm.scan**: all FM or MFM encoded floppy disks,

**- raw.125**: all single-density floppy disks,

**- raw.250**: all double-density floppy disks,

**- raw.500**: all high-density floppy disks.

They are accompanied by 'meta-images' which store not only the contents
of the sectors, but also their number, size, etc. These 'meta-images'
are:

**- .edsk**: this is the disk image format favoured by British Z80
machine emulators (Sinclair, Amstrad, Sam Coupé and all MGT floppy disk
systems).

**- .imd**: a format invented in the MS-DOS era to allow a PC to save
any type of floppy disk readable by its floppy disk controller as an
image.

To use these meta-profiles and meta-images, you must manually specify
the geometry of the floppy disk using the "**--tracks=**" option,
followed by various arguments:

**- c=**: the range of cylinders to be read. This means the tracks
accessible by the drive head, the first being numbered "0" and the last
being the 39th or 79th depending on the 40 or 80 track formats. For
example: "c=0-79".

**- h=**: the drive heads to be used, to indicate whether only one side
is to be accessed ("h=0"), both sides of the diskette ("h=0-1"), or only
the second side of the diskette ("h=1").

See [here](https://github.com/keirf/greaseweazle/wiki/Specifying-Tracks)
for a more in-depth explanation of how to use the --tracks option.

For example, to backup a 180 KB Amstrad CPC floppy disk, which has a
single side with 40 tracks, to a "MyCPCdisk.edsk" image, using a drive
with ID "0" (Amstrad floppy disks are 3-inch, 3-inch drives being of the
Shugart type, they necessarily have ID "0", "1" or "2"), you would do :

```
gw read --format=ibm.scan MyCPCdisk.edsk --drive=0 --tracks=c=0-39:h=0
```

Writing a floppy disk from a meta-image is much simpler. All the
geometry of the floppy disk being already indicated in the meta-image,
you indicate neither the profile nor the quantity of tracks in the
command line:

```
gw write MyCPCdisk.edsk --drive=0
```

Note that emulators that use .edsk images prefer the ".dsk" suffix. When
reading a floppy disk with the gw command, you should always use the
".edsk" suffix to avoid confusion with plain ".dsk" images. But remember
to rename your ".edsk" images to ".dsk" before using them with an
emulator.

However, you can use such an image with the suffix ".dsk" to write a
floppy disk; the command will detect its type automatically when reading
it.

### Level \#4: manage 5.25-inch 48-TPI disks with your 5.25-inch 96-TPI drive

With 5.25-inch disks, there are two sizes for the floppy drive’s head:
48 TPI and 96 TPI.

When they are written by a 48 TPI floppy drive, floppy disks contain
around 40 'thick' tracks (from 35 to 42, depending on the format).

When they are written by a 96 TPI floppy drive, they contain around 80
'thin' tracks (sometimes up to 82).

<!---
<img src="media/image1.jpg" style="width:5.54444in;height:3.03212in" alt="Une image contenant capture d’écran, jaune, Graphique, texte Description générée automatiquement" />
--->

The good news is that you can absolutely read a 48 TPI floppy disk from
a 96 TPI floppy drive when you ask your drive to read one track every
two tracks. You tell this in the command line with the "**--tracks=**"
option and its "**step=2**" argument applied to the interval of tracks
you want to read.

For instance, let’s say you want to read a 2-side, 40-track Dragon 32/64
floppy disk, using a 5.25-inch Teac FD-55GFR floppy drive, which is a
96-TPI drive. You would do:

```
gw read --format= dragon.40ds MyDragonDisk.img --tracks=c=0-39:step=2
```

Side note: a 48 TPI floppy disk is in all cases also a “double density”
disk (DD), while a 96 TPI drive is most often also a “high density”
floppy drive (HD). This has nothing to do with track thickness, but is
related to the amount of current the floppy drive head uses to
read/write a floppy disk made of iron oxide (double density) or cobalt
(high density). To force an HD floppy drive to adapt to a DD floppy
disk, it may be useful to add the **--dd L** option to the command line.

Writing a 48 TPI floppy disk with a 96 TPI floppy drive is a bit more
complicated than just replace “read” by “write”. This floppy drive
writes tracks that are twice too thin compared to real 48 TPI tracks. If
your floppy disk has been previously written with a 48 TPI floppy drive,
then half of the old “thick” tracks will remain in between the new
"thin" tracks you are writing. At the end, the 48 TPI drive in your old
computer will read at the same time your newly written thin track + half
of an old thick track. It will fail.

<!---
<img src="media/image2.jpg" style="width:5.73333in;height:3.73264in" alt="Une image contenant texte, capture d’écran, jaune, arc-en-ciel Description générée automatiquement" />
--->

A solution - not guaranteed! - would be to completely erase your floppy
disk before writing on it, by passing a magnet over its entire surface.
This will leave no trace of the old thick tracks between the new thin
tracks.

But the most reliable solution is to only write 48 floppy disks with 48
TPI floppy drives.

### Level \#5: work at the magnetic flux level to read/write any disk (even copy-protected)

In the examples above, the gw command automates a complex process of
backing up the useful contents of an uncopy-protected floppy disk to a
disk image compatible with your emulator. Or it does the opposite: it
automates the writing of a physical floppy disk from a disk image that
contains the data useful to an emulator. But that's not necessarily what
you want to do.

The Greaseweazle solution also allows you to archive the complete
magnetic flux on the surface of your floppy disk. This is useful when
you want to keep an archive of an original floppy disk, possibly
copy-protected, so that you can recreate a strictly identical copy
later. It is also useful for capturing a floppy disk whose formatting is
not directly supported by the gw command.

It works like a photocopy of the surface of your disk. It works with any
disk format, you don't even need to tell which format your disk is, just
put the right suffix at the end of your archive name. The supported
archive formats are:

-   **.scp :** A long detailed digitized flux in very high definition,
    better for archiving purposes of special disk formats. But expect
    dozens of MegaBytes for the size of the archive of a simple double
    density disk. This archive format was invented for the older
    archiving solution SuperCard Pro.

-   **.ctr :** The same as above. This archive format was invented for
    the older archiving solution Kryoflux.

-   **.raw :** The same as above, but with one separate file per track.
    This archive format was invented for the older archiving solution
    Kryoflux.

-   **.hfe :** a digitized flux at the exact resolution of the bitcells,
    the smallest bits of useful data on a floppy disk. Expect around
    twice the size of your original disk for the archive (2 MB for the
    archive of an Amiga disk, for instance). This archive format was
    invented for the HxC floppy drive emulator.

However, when you work at the flux level, you need to **manually tell**
gw the speed of the recording it is supposed to read. The speed of the
recording is the rotation speed in RPM for .scp, .ctr and .raw archives,
or a bitrate in kbit/s for .hfe archives. And, as before, you must also
tell the number of tracks to read.

**RPM (for .scp, .ctr and .raw archives):** the Rotations Per Minute
your disk was initially recorded with. Most of the drives spin at 300
RPM, except:  
- the latest 5.25-inch and all the 8-inch drives, who spin at 360 RPM.

\- the Atari 810 and 1050 drives, who spin at 288 RPM.

So, here's the scenario you might encounter: you want to archive an
Acorn BBC floppy disk that was written on a 300 RPM drive with your last
generation 5.25-inch 1200 KB drive, which runs at 360 RPM. The data will
be read too quickly. Specifying the original RPM number, with the option
“--adjust-speed”, will correct this problem.

Here are some examples:  
  
- To archive an Atari 800XL 5.25-inch disk, that has one side formatted
and 40 “thick” tracks (48 TPI), originally written at 288 RPM, into a
“MyAtari800Disk.scp” file, using a 5.25-inch Teac FD-55GFR drive, that
is a 96 TPI drive spinning at 360 RPM, you will do:

```
gw read MyAtari800Disk.scp --tracks="c=0-39:h=0:step=2" --adjust-speed=288rpm
```

\- To archive an IBM PC-XT “360 KB” 5.25-inch disk, that has two sides
and 40 “thick” tracks (48 TPI) originally written at 300 RPM, into a
“MyIBMdisk.scp” file, using the same 96 TPI/360 RPM drive, you will do:

```
gw read MyIBMdisk.scp --tracks="c=0-39:step=2" --adjust-speed=300rpm
```

\- To archive a MSX 3.5-inch disk, that has one side formatted, into a
“MyMSXdisk.scp” file, using any 3.5-inch drive, disk and drive being
both in 80 tracks and 300 RPM:

```
gw read MyMSXdisk.scp --tracks="c=0-79:h=0”
```

\- To archive any Amiga disk, being double density (880 KB) or high
density (1760 KB), being copy-protected or not, into a “MyAmigaDisk.scp”
file, using any 3.5-inch drive:

```
gw read MyAmigaDisk.scp
```

Side note: When you do not specify a format, the gw command does not
check that the flux it is reading is error-free. This is desirable for
capturing protections that are based on malformed data. But there is a
risk that you will also capture random errors. To avoid this pitfall, it
is possible to combine format checking with saving the content in flux
mode, using the --format and --raw options together, as follows:

```
gw read --format=amiga.amigados MyAmigaDisk.scp --raw
```

**Bitrate** **(for .hfe archives only):** for disks encoded in FM/MFM,
there are four possible bitrates, depending on the 'density' of your
floppy disk:

\- 125 kbit/s for 'single density' floppy disks (aka SD: early
computers)

\- 250 kbit/s for 'double density' floppy disks (aka DD: most computers
created during the 80’s)

\- 500 kbit/s for "high density" floppy disks (aka HD: IBM PC-AT and
every other computer launched after it)

\- 1000 kbit/s for "Extra high density" floppy disks (aka ED, mainly
latest IBM PS/2 and NeXT’s computers)  
You specify this by adding “::bitrate=” right after the suffix of your
.hfe archive name.

Here are some examples:

To archive an Atari ST 3.5-inch disk, that has two sides formatted at
double density, into a “MyAtariSTdisk.hfe” file suitable for a HxC drive
emulator, using any 3.5-inch drive:

```  
gw read MyAtariSTdisk.hfe::bitrate=250
```

To archive an Amstrad CPC 3-inch disk, that has only one side formatted
at double density and 40 tracks, into a “MyAmstradCPCdisk.hfe” suitable
for a HxC drive emulator, using an original Amstrad 3-inch floppy drive
that has unit ID 0 and that also reads/writes 40 ‘thick’ tracks:  

```
gw read MyAmstradCPCdisk.hfe::bitrate=250 --tracks="c=0-39:h=0” --drive=0
```

The good news is all the speed and tracks information is stored into
these archives. So, you don’t have to tell it again when you write the
.scp or .hfe file back to the disk. For instance:  

```
gw write MyAmstradCPCdisk.hfe
gw write MyMSXdisk.scp
```

### Level \#6: Working with 8-inch floppy drives and the TG-43 option

When working with 8-inch floppy drives, you may encounter issues with writing and reading disks reliably, especially on tracks 43 and higher. This is where the `--gen-tg43` option becomes essential.

#### Understanding TG-43 (Track Greater than 43)

The TG-43 signal is a control signal that tells the floppy drive to reduce the write current when accessing tracks 43 and above on 8-inch floppy disks. This is necessary because:

1. **Higher linear velocity**: As you move toward the outer tracks of a spinning disk, the linear velocity increases even though the rotational speed remains constant.

2. **Read amplifier saturation**: The faster-moving magnetic medium on outer tracks produces stronger read signals that can saturate the read amplifier circuitry, leading to data corruption and read/write errors.

3. **Write current reduction**: The TG-43 signal reduces the write head's output current for tracks ≥43, preventing read amplifier saturation and ensuring reliable data storage.

#### Using the --gen-tg43 option

When writing to 8-inch floppy disks use the `--gen-tg43` option:

```
gw write --gen-tg43 --format=dec.rx02 MyDisk.img
```

This enables pin 2 (TG-43) on the floppy drive interface, which signals the drive to reduce write current for tracks 43 and above.

#### Drive compatibility and filtering

Some drives have additional filtering capabilities:

- **Track 60+ filtering**: Some 8-inch drives include hardware filters that help reduce read errors on tracks 60 and above caused by overly strong magnetic signals.

- **Controller differences**: Not all floppy disk controllers implement TG-43 properly:
  - Many PC floppy controllers don't support TG-43 for 8-inch drives
  - DEC RX02 controllers may not implement TG-43 correctly
  - In these cases you need to enable --gen-tg43 to help the read circuitry handle disks that were written with excessive current (without TG-43), as the stronger magnetic patterns can saturate the read amplifier 

The TG-43 feature is essential for reliable 8-inch floppy disk operations and is one of the key differences between 8-inch and smaller floppy disk technologies.

### Level \#7: yes, you can read any disk, except (probably) "flippy" 5.25-inch disks

In most cases, Commodore, Apple and Atari 800 5.25-inch floppy disks
that were recorded on both sides, by physically flipping the disk, will
not be supported.

The problem is not in the Greaseweazle solution, but in the 5.25-inch
floppy drive you use, that is physically incompatible with “flippy
disks”. It relies on the “index hole” to evaluate the speed of the disk
before any read/write operation. But when you flip a disk upside down,
the index hole is no more in front of the optical probe.

That said, it has been reported that some rare 5.25-inch drives support
reading floppy disks without using index hole, thanks to a special
configuration of their plastic jumpers. On the Panasonic JU-475-4, for
instance, you achieve this mode of operation by removing the jumper from
the GX position and move it on the EX position.

If your drive has this kind of feature, then you must manually tell the
gw command what is the rotation speed (in RPM) of your drive with the
option “--fake-index”. For instance, if you want to read the flipped
side of a C64 floppy disk with a JU-475-4, which is a 96 TPI and 360 RPM
drive, you would insert it upside down into your drive and type:

```
gw read --format=commodore.1541 MyC64sideB.d64 --tracks=”c=0-35:h=0:step=2” --fake-index=360rpm
```

Note that --fake-index is related here to the rotation speed of the
drive you are using. It is not the rotation speed used by the original
computer to write the floppy disk you are reading. For instance, let’s
take one complex example: you want to dump the flipped side of a
35-track Apple II floppy disk, written in 300 RPM and 48 TPI, into a
“MyApple2SideB.scp” archive, using a 96 TPI and 360 RPM drive. You would
insert the disk upside down into your drive and type:

```
gw read MyApple2SideB.scp --tracks=”c=0-35:h=0:step=2” --adjust-speed=300rpm --fake-index=360rpm
```

For more information about flippy disks, see [this
page](https://github.com/keirf/greaseweazle/wiki/Flippy-Disks).

### Level \#8: Restore floppy disks from even more image disks

Beyond .edsk, .imd, .scp, .ctr, .raw and .hfe, other self-descriptive
disk images exist. The gw command cannot create them for some reason
(legal, lack of documentation, time missing…), but it can read them to
write their content back to a physical floppy disk. The supported
formats are:  
  
**.a2r :** archive of flux, dedicated to Apple II floppy disks,

**.d88, .dcp, .dim, .fdi** : meta-image dedicated to Japanese Nec
88xx/98xx and X68000 floppy disks,

**.tdo** : similar to .imd.

**.ipf** : similar to .hfe + metadata. Please note that support of .ipf
disk images is optional. To install its library on your system, read
[this page](https://github.com/keirf/greaseweazle/wiki/IPF-Images).

Then, to generate an Amiga physical floppy disk from a MyAmigaGame.ipf
file, for instance, you would do:

```
gw write MyAmigaGame.ipf
```

### Level \#9: complete your Greaseweazle experience with other tools

You still can’t find in the gw command the support for the disk images
of your choice? Then use .scp, .hfe; .edsk or .imd images with
Greaseweazle and install third-party tools that will make the bridge between
theses disk images and other ones. Here are some extra tools, compatible
with Windows, macOS and Linux, that you could use to expand your
Greaseweazle experience:

**[Disk Utilities](https://github.com/keirf/disk-utilities):** helpful
to convert a .scp or an old .dfi flux archive of a protected floppy disk
into an .ipf image easier to write with a Greaseweazle or to use with an
emulator.

[**HxC Floppy
Emulator**](https://github.com/jfdelnero/HxCFloppyEmulator/releases/tag/HxCFloppyEmulator_V2_15_1_2):
to convert many exotic disk images (Apple II .po or .do, Atari ST .stx;
Atari 800 .atr, NorthStar .nsi, Dragon 32/64 .vdk, Thomson MO/TO .fd,
TRS-80 .jv3 or .jv1, and a dozen of audio keyboard proprietary images,
among others) to .hfe or .scp archives writable with the gw command.

It can also convert .scp or .hfe archives created with gw command to
.po, .do, .stx, .nsi, .vdk, .fd, or .jv3 images usable with emulators.

This software exists in command line and GUI versions. The GUI version
also offers a graphic disk analyser to visually detect errors on flux
archives created with Greaseweazle.

**[SamDisk](https://simonowen.com/samdisk/):** to convert even more
exotic disk images (Amstrad .dsc and .cfi, C64 CMD FD-2000/4000 .d2m or
.d4m, HP LIF .lif, Jupiter Ace Sam Coupé .sad or .sbt, Sega System 24
.s24, TRS-80 .dmk, ZX Spectrum .mbd, .opd,.scl or .udi, among others) to
.edsk meta-images writable with the gw command.

It can also help to convert .edsk images created with the gw command to
.d2m, .d4m, .lif, .sad, .mbd, and .opd images compatible with some
emulators.

**a8rawconv ([FTP
link](http://ftp.pigwa.net/stuff/emulators_and_utils/8-bit/a8rawconv/))**:
to convert .scp archives of Atari 800 disks created by the gw command to
.atr, .atx, or .xfd images compatibles with emulators. Or the opposite:
to convert .atr, .atx and .xfd images into a .scp archive writable to
floppy disk with the gw command.

[Fluxengine](https://github.com/davidgiven/fluxengine/releases): This is
an alternative command to gw, which supports other floppy disk formats,
like Apple II AppleDos or ProDos, Victor 9000, among others.

### Level \#10: create your own profile to support a specific disk format

All the profiles used with the --format option are described in the
[diskdefs.cfg](https://github.com/keirf/greaseweazle/blob/master/src/greaseweazle/data/diskdefs.cfg)
configuration file that is installed with the gw command. If you feel
that you are familiar with the characteristics of a certain floppy disk
formatting which is not directly supported by any profile of the gw
command, you can write its specifications as a new profile into a
configuration file following the pattern in diskdefs.cfg.

Then, to read a floppy disk with a custom profile that you named, for
instance, my.disk.format and that you saved in a configuration file
named, for instance, MyFormats.cfg, you would type:  

```
gw read --diskdefs=MyFormats.cfg --format=my.disk.format MyDisk.img
```
