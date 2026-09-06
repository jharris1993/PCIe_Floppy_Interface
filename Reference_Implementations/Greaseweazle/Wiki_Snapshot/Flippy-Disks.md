Several 8-bit home computers used 5.25" drives with a single read head
but used both sides of the disk to store data, requiring the user to
*flip* the disk to access side B. Double-sided drives
with two heads cannot read both sides in one pass, for two reasons:
1. The second drive head is offset inwards by several tracks, such that
the outer tracks on side B of a flippy disk are inaccessible.
2. The side-B tracks which the double-sided drive *can* read will appear
to be recorded backwards.

The obvious solution is to physically flip the disk, as in the original
system. However if you try this you will receive the error
`Command Failed: GetFluxStatus: No Index`. This is because the index
hole in the disk jacket is in the wrong position for the drive sensor
when the disk is flipped. There are a few possible solutions, which are
also summarised on page 7 of the
[Kryoflux flippy-drive manual][kryoflux_manual]:
1. Punch a second index hole in the disk jacket in the correct flipped
position. This will require removal of the inner disk media from its
jacket.
2. Fake the index pulse signal using Greaseweazle. This requires a drive
which will spin up in the absence of index pulses (many will not).
3. Modify a drive to include a second index sensor (see PDF guides
[here][adafruit] and [here][cowlark]). This allows to select the
correct index sensor based on a switch setting on the modified drive.
4. Obtain a flippy-modded disk drive which can read both sides of a
flippy disk in a single pass.

### Faking the index pulse

First measure the precise rotation speed of your drive by placing a
disk in the drive and running `gw rpm --nr 10`. The
RPM values should be relative constant for every measurement.

Now you can flip the floppy disk in your drive as you would do on
the original hardware and use the following command prefix: `gw read
--fake-index --tracks h=0 ...`. For example, to read a raw single-sided
image of side B:
```
gw read --fake-index 300 --tracks h=0 --drive 0 --raw test.scp
```

### Flippy-modded disk drive

This requires a specially-modified drive as originally specified by
the [Kryoflux project][kryoflux_manual]. You can then read flippy disks
in a single pass, for example (including C64 half tracks):
```
gw read c=0-79:h=0,1:h1.off=-8 test.scp
```

Note that side B will be read backwards in this case. Conversion software
will need to be aware of this.

[adafruit]: https://cdn-learn.adafruit.com/downloads/pdf/flippy-floppy-drive-modification.pdf
[cowlark]: http://cowlark.com/fluxengine/doc/Index_sensor_mod_FDD_1.1.pdf
[kryoflux_manual]: https://www.kryoflux.com/download/kf_525modded_manual.pdf
