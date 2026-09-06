
<img align="right" width="40%" src="https://raw.githubusercontent.com/wiki/keirf/greaseweazle/assets/bit-shift.png">

When writing to a disk, some or all tracks can have **write precompensation**
applied. This technique compensates for the tendency for consecutive flux
transitions to interact and cause them to spread apart. The effect is
particularly noticeable on inner tracks where the bit density is highest.

The precomp specifier is presented by **--precomp=** and can
contain any of the following elements:
- **type=\<t\>**: Precomp type (**mfm**, **fm**, **gcr**): Default **mfm**
- **\<c\>=\<p\>**: Precompensate all cylinders >= **c** by **p** nanoseconds.

For example:
- `40=125`: Apply 125ns MFM precompensation to cylinders 40 and higher
