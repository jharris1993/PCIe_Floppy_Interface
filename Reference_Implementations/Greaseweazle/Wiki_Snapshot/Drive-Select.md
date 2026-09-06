Greaseweazle supports Shugart and IBM/PC multi-drive setups<sup>1</sup>.

The **read** and **write** commands both accept option `--drive N`
where **N** is one of **A**, **B**, **0**, **1**, or **2**. Note that **N**
is not case sensitive: **a** and **b** are also accepted.

The default is **A** (IBM/PC Drive A) requiring an IBM/PC drive and
a "cable with a twist" (see the explanation below). If your drive fails
with a *Track 0 not found* error, you may have:
- A Shugart drive, strapped for DS0 (pin 10): Connect with straight ribbon and use `--drive 0`
- A PC drive being used with a straight cable: Use `--drive b`

**Note:** Greaseweazle F1 does not support multiple drives and any specified non-default
drive letter will be ignored.

### A,B: IBM/PC

<img align="right" src="https://raw.githubusercontent.com/wiki/keirf/greaseweazle/assets/ibmpc_ribbon.jpg">

In IBM/PC mode the Greaseweazle header acts the same as on a PC
motherboard: Two drives may be connected, each with an independent motor-enable
line. All PC drives are strapped for drive-select DS1 (pin 12),
and a cable twist is used to differentiate between drives **A** and **B**:
- **A**: Drive connected via a cable with twist on pins 10-16
- **B**: Drive connected via a straight ribbon cable

A two-drive cable will have connector(s) before and after a twist,
as shown.

### 0,1,2: Shugart

Up to three drives may be connected, with drive-select lines DS0-DS1 on
pins 10, 12 and 14 respectively. All drives share a common motor-select
signal on pin 16. Drives are addressed by drive identifiers **0**, **1**,
and **2**.

### Summary

The diagrams below summarise the use of pins 10-16 on the respective buses.
Click for full-size.

<a href="https://raw.githubusercontent.com/wiki/keirf/greaseweazle/assets/ibmpc_sel.jpg"><img width="40%" src="https://raw.githubusercontent.com/wiki/keirf/greaseweazle/assets/ibmpc_sel.jpg"></a>
<a href="https://raw.githubusercontent.com/wiki/keirf/greaseweazle/assets/shugart_sel.jpg"><img width="40%" src="https://raw.githubusercontent.com/wiki/keirf/greaseweazle/assets/shugart_sel.jpg"></a>

1. Except Greaseweazle F1 (basic Blue Pill model).
