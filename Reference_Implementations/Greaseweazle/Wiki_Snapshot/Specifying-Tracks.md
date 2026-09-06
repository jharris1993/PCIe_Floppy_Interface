
The read, write and erase commands can all act on a specified set of
disk tracks. The format specifier is presented by **--tracks=** and can
contain any of the following elements:
- **c=\<set\>**: Set of cylinders to access
- **h=\<set\>**: Set of heads (sides) to access
- **step=[0-9]**: Number of physical head steps between cylinders (default 1)
- **hswap**: Physical drive heads are swapped
- **h[01].off=[+-][0-9]**: Physical cylinders of the specified head are offset by the specified amount (used for flippy-modded 5.25" drives only!)

**\<set\>** is a comma-separated list of integers and integer ranges.

For example:
- `c=0-7,9-12:h=0-1`: Accesses both sides of cylinders 0-7 and 9-12.
- `c=0-39:h=0:step=2`: Read a single-sided 40-cyl disk in an 80-cyl drive.
- `c=0-79:h=0:hswap`: Treat physical side 1 as a second single-sided image on a double-sided disk.
- `c=0-79:h=0,1:h1.off=-8`: Read both sides of a C64 flippy disk, including half tracks, in one pass.
