
## Sector Image Types

Supported for read and write, with automatic verification:
- ADF (Commodore Amiga, 880k and 1760k; Acorn ADFS)
- ADS, ADM, ADL (Acorn ADFS)
- DSD, SSD (Acorn DFS)
- [DSK, EDSK](#edsk-imd-td0) (Amstrad CPC; Also used by Spectrum +3, SAM Coupé, and others)
  - Automatically disambiguated from raw-sector DSK by header signature
- D64 (Commodore 64 1541 GCR)
- D71 (Commodore 64 1571 GCR)
- D81 (Commodore 64 1581 MFM)
- HDM, XDF (PC-98)
- [IMD](#edsk-imd-td0) (IBM Sectors)
- [IMG, IMA, DSK](#img-ima-dsk) (Generic suffixes for IBM FM/MFM Raw Sector)
- MGT (Sinclair ZX Spectrum DISCiPLE/+D, SAM Coupé)
- MSA, ST (Atari ST)
- SF7 (Sega SF-7000)

#### IMG, IMA, DSK

These formats store the payload data of all sectors back-to-back, in
logical order, with no separators and no metadata.

The sectors appear in increasing logical order of Track #, Head #,
Sector #. Physical layout attributes such as sector interleave are
not represented in these image files.

For example on a double-sided, 80-track, 9-sectors format, the order
of sectors in the file will be:

- T0 H0 S1, T0 H0 S2, ..., T0 H0 S9
- T0 H1 S1, T0 H1 S2, ..., T0 H1 S9 
- ...
- T79 H1 S1, ..., T79 H1 S9

Since these image types do not describe the physical disk and track
layout, they can only be handled by Greaseweazle in concert with a
specified `--format`.

#### EDSK, IMD, TD0

These formats contain an image header and additional metadata which
describes the physical layout and identificatoon of sectors within
each track. This will include attributes such as: Track #, Head #,
Sector #, and checksum.

Thus, unlike the headerless image types described above, these formats
can represent physical attributes such as sector interleave and skew,
and some simple copy protections (bad checksum, unusual sector ids,
and so on).

Greaseweazle can import these image types without need of a specified
`--format`, because they are sufficiently self-describing.

## Import-Only Image Types

Supported only for importing existing images. Can be written to disk
with automatic verification:
- D88, DCP, DIM, FDI, NFD (PC-98)
- IPF (Universal 'Golden Image' Format)
- [TD0](#edsk-imd-td0) (IBM Sectors)

## Raw Image Types

Universal raw image types supported for read and write, no automatic
verification:
- HFE (Raw Bitcells, 1 revolution per track)
- [Kryoflux](#kryoflux) (Raw Flux, multiple revolutions per track)
- SCP (Raw Flux, multiple revolutions per track)

These can be used or analysed in several ways:
- WinUAE, FS-UAE (Universal Amiga Emulator): Directly support SCP files
- [Disk-Utilities][du]: A command-line analyser and transcoder
- [HxC Software][hs]: A GUI visualiser, analyser and transcoder

Import-only (existing image to disk):
- A2R (Applesauce 3.x Raw Flux)

#### Exporting raw flux

Please note that by default `gw read` will re-generate flux when you
specify `--format`. To export
raw flux directly from the disk you *must* specify both `--raw` and
`--format`, or neither. For example:
```
gw read --format=ibm.720 not_raw_flux.scp
gw read --format=ibm.720 --raw really_raw_flux.scp
```

If you specify a `--format` but not `--raw`, the file will store
digitally regenerated "perfect" flux data, and bad sectors will be
filled with `==[BAD SECTOR]==` data. This is probably not what you
want when saving raw flux data!

#### Kryoflux

Kryoflux stream files are supported for both import and export. This
files are stored one per track in the form `name<track>.<side>.raw`. For
example: name00.0.raw, name00.1.raw, ..., name79.1.raw.

To specify a set of Kryoflux stream files to Greaseweazle, simply pass
the name of any one individual file. For example:
```
gw read --tracks=c=0-39 name00.0.raw
```

[du]: https://github.com/keirf/Disk-Utilities/blob/master/README.md
[hs]: https://hxc2001.com/download/floppy_drive_emulator/HxCFloppyEmulator_soft.zip
