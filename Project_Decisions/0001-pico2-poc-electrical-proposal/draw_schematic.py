# SPDX-License-Identifier: GPL-3.0-or-later
"""Render the tentative electrical concept to editable SVG and preview PNG.
Requires Pillow. Coordinates and net names are shared between both formats.
"""
from pathlib import Path
from html import escape
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent
INK, WIRE, MUTED, ACCENT = '#182737', '#145c46', '#516477', '#235e91'

class Sheet:
    def __init__(self, title, subtitle, height=1400):
        self.w, self.h = 1600, height
        self.im = Image.new('RGB', (self.w, self.h), 'white')
        self.d = ImageDraw.Draw(self.im)
        self.svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}">', '<rect width="100%" height="100%" fill="white"/>']
        self.text(45, 25, title, 32, ACCENT)
        self.text(45, 72, subtitle, 18, MUTED)
        self.line((45, 110), (1555, 110), color=ACCENT)

    def text(self, x, y, s, size=20, color=INK):
        font = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', size)
        self.d.text((x, y), s, fill=color, font=font)
        self.svg.append(f'<text x="{x}" y="{y+size}" fill="{color}" font-family="Consolas,monospace" font-size="{size}">{escape(s)}</text>')

    def line(self, *points, color=WIRE, width=2):
        self.d.line(points, fill=color, width=width)
        p = ' '.join(f'{x},{y}' for x,y in points)
        self.svg.append(f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="{width}"/>')

    def rect(self, x, y, w, h, color=MUTED):
        self.line((x,y),(x+w,y),(x+w,y+h),(x,y+h),(x,y), color=color)

    def dot(self, x, y, open=False):
        self.d.ellipse((x-4,y-4,x+4,y+4),fill='white' if open else WIRE,outline=WIRE,width=2)
        self.svg.append(f'<circle cx="{x}" cy="{y}" r="4" fill="{"white" if open else WIRE}" stroke="{WIRE}" stroke-width="2"/>')

    def ground(self,x,y):
        self.line((x,y),(x,y+12))
        for i,w in enumerate((18,12,6)):
            self.line((x-w,y+12+i*6),(x+w,y+12+i*6))

    def resistor(self,x,y,label,vertical=False):
        if vertical:
            self.line((x,y),(x,y+12)); self.rect(x-8,y+12,16,36,WIRE); self.line((x,y+48),(x,y+60)); self.text(x+16,y+17,label,18)
        else:
            self.line((x,y),(x+12,y)); self.rect(x+12,y-8,56,16,WIRE); self.line((x+68,y),(x+80,y)); self.text(x+8,y-36,label,18)

    def fet(self,x,y):
        # Gate terminal at x-70,y; drain at x+20,y-90; source at x+20,y+70.
        self.line((x-70,y),(x-25,y)); self.line((x-25,y-30),(x-25,y+30))
        for a,b in ((-32,-12),(-8,8),(12,32)): self.line((x-12,y+a),(x-12,y+b))
        self.line((x-12,y-27),(x+20,y-27),(x+20,y-90))
        self.line((x-12,y+27),(x+20,y+27),(x+20,y+70))
        self.line((x+20,y),(x-12,y)); self.line((x-5,y-5),(x-12,y),(x-5,y+5))
        self.text(x+36,y-38,'Q: AO3400A',18)
        self.text(x+36,y-12,'1=G  2=S  3=D',16,MUTED)
        self.text(x-47,y-53,'G',16); self.text(x+28,y-78,'D',16); self.text(x+28,y+42,'S',16)
        self.ground(x+20,y+70)

    def inv(self,x,y):
        # Input at x,y; output at x+108,y.
        self.line((x,y),(x+20,y)); self.line((x+20,y-30),(x+20,y+30),(x+85,y),(x+20,y-30))
        self.dot(x+91,y,True); self.line((x+95,y),(x+108,y))
        self.line((x+35,y+10),(x+35,y-9),(x+46,y-9),(x+46,y+10),(x+55,y+10),color=INK)
        self.text(x-4,y-68,'SN74LVC14A',18); self.text(x+8,y+38,'VCC = 3.3 V',16,MUTED)

    def save(self,name):
        self.text(45,self.h-44,'TENTATIVE | 2026-09-01 | GPIO numbers TBD | See README for limits and sources',18,MUTED)
        self.svg.append('</svg>')
        (OUT/f'{name}.svg').write_text('\n'.join(self.svg),encoding='utf-8')
        self.im.save(OUT/f'{name}.png')

s=Sheet('Pico 2 / floppy drive interface — circuit cells','3.3 V controller domain | 5 V cable domain | One cell per signal; names are symbolic')
s.text(45,130,'A. OUTPUT — GPIO high pulls the cable signal low',24,ACCENT)
s.text(75,220,'GPIO_TX',20)
s.line((170,255),(260,255)); s.resistor(260,255,'100R'); s.line((340,255),(470,255))
s.dot(385,255); s.resistor(385,275,'10k',True); s.line((385,255),(385,275)); s.ground(385,335)
s.fet(540,255); s.line((560,165),(1040,165)); s.text(760,132,'LINE_TX_n -> port selector',20)
s.text(1090,160,'At the selected DRIVE:',18,MUTED)
s.line((1040,165),(1040,205)); s.resistor(1040,205,'R_TERM',True); s.line((1040,265),(1040,285)); s.text(930,300,'+5 V drive supply',18)
s.text(1090,207,'Use its specified pull-up.',18)
s.text(1090,238,'150R is a legacy example.',18)
s.text(75,375,'GPIO low / high-Z = release. Pull-down keeps Q off during reset.',18)
s.text(75,405,'WRITE GATE only: add removable WRITE ARM link before the 100R gate resistor.',18)
s.line((45,453),(1555,453),color=MUTED)

s.text(45,472,'B. INPUT — asserted cable signal becomes GPIO high',24,ACCENT)
s.text(75,590,'LINE_RX_n',20); s.line((190,620),(520,620)); s.dot(350,620)
s.text(270,510,'+5V_IF',18); s.resistor(350,545,'1k initial',True); s.line((350,530),(350,545)); s.line((350,605),(350,620))
s.resistor(520,620,'100R'); s.line((600,620),(720,620)); s.inv(720,620)
s.line((828,620),(940,620)); s.resistor(940,620,'100R'); s.line((1020,620),(1260,620)); s.text(1290,605,'GPIO_RX',20)
s.text(75,710,'Pull-up is removable. Select its value from the drive sink rating and cable load.',18)
s.text(75,740,'Receiver supply: Pico 3V3(OUT). 100 nF at each IC. Inputs tolerate 5.5 V.',18)
s.line((45,792),(1555,792),color=MUTED)

s.text(45,810,'C. CONFIGURABLE DIRECTION — one GPIO, set by a hardware jumper',24,ACCENT)
s.text(65,940,'GPIO_FLEX',20); s.line((180,975),(320,975)); s.dot(320,975,True)
s.dot(360,925,True); s.dot(360,1025,True); s.line((320,975),(355,930),width=3)
s.text(230,863,'JP_DIR',18); s.text(370,889,'TX',18); s.text(370,1035,'RX',18)
s.line((360,925),(530,925)); s.resistor(530,925,'100R'); s.line((610,925),(720,925))
s.dot(655,925); s.line((655,925),(655,950)); s.resistor(655,950,'10k',True); s.ground(655,1010)
s.fet(790,925); s.line((810,835),(1015,835),(1015,900),(1270,900)); s.text(1280,878,'LINE_FLEX_n',18)
s.line((1015,900),(1015,1130)); s.dot(1015,900)
s.text(1130,954,'Cable pull-up as in A/B;',18); s.text(1130,982,'fit only as required.',18)
# Receiver drawn left-to-right with named net connected to shared cable node.
s.line((1015,1130),(1015,1195),(440,1195),(440,1110),(500,1110)); s.resistor(500,1110,'100R')
s.line((580,1110),(700,1110)); s.inv(700,1110); s.line((808,1110),(845,1110)); s.resistor(845,1110,'100R')
s.line((925,1110),(955,1110),(955,1060),(410,1060),(410,1025),(360,1025))
s.text(75,1230,'One shunt: TX or RX. No shunt: GPIO disconnected; Q stays off.',18)
s.text(75,1260,'This selects direction between configurations. For live open-drain bidirectionality,',18)
s.text(75,1290,'use separate TX and RX GPIOs instead; never tie the receiver output to the Q gate.',18)
s.save('interface-cells')

s=Sheet('Pico 2 / floppy drive interface — connector plan','Two physical connectors | One active port at a time | Illustrative PC + SA455/465 signal roles',1450)
s.text(45,130,'D. PORT SELECTION — repeat for even pin p = 2, 4, ... 34',24,ACCENT)
s.text(65,216,'Cell LINE_p',20); s.line((220,240),(400,240)); s.dot(400,240,True)
s.dot(470,200,True); s.dot(470,280,True); s.line((400,240),(466,202),width=3)
s.line((470,200),(740,200)); s.line((470,280),(740,280))
s.text(755,182,'J1 pin p — PC twisted cable',20); s.text(755,262,'J2 pin p — alternate drive',20)
s.text(380,152,'JP_PORT[p]',18); s.text(70,326,'Set all 17 shunts to the same port. Grounds remain common. Change only with power off.',18)

rows=[('2','Density / optional','Drive-specific','FLEX'),('4','Reserved: disable','Drive-specific','FLEX'),('6','Reserved: disable','DS4','FLEX'),('8','INDEX','INDEX / SECTOR','RX'),('10','MOTOR A','DS1','TX'),('12','SELECT B','DS2','TX'),('14','SELECT A','DS3','TX'),('16','MOTOR B','MOTOR ON','TX'),('18','DIRECTION','DIRECTION','TX'),('20','STEP','STEP','TX'),('22','WRITE DATA','WRITE DATA','TX'),('24','WRITE GATE','WRITE GATE','TX + ARM'),('26','TRACK ZERO','TRACK ZERO','RX'),('28','WRITE PROTECT','WRITE PROTECT','RX'),('30','READ DATA','READ DATA','RX'),('32','SIDE SELECT','SIDE SELECT','TX'),('34','DISK CHANGE','READY / variant','FLEX')]
s.text(65,380,'PIN',20,ACCENT); s.text(200,380,'J1: PC (controller end)',20,ACCENT); s.text(740,380,'J2: example alternate',20,ACCENT); s.text(1300,380,'CELL',20,ACCENT)
for i,row in enumerate(rows):
    y=425+i*32
    for x,t in zip((65,200,740,1300),row): s.text(x,y,t,19)
    s.line((60,y+29),(1530,y+29),color='#dee5eb',width=1)
s.text(65,982,'All conventional odd contacts: GND. Approve each actual drive pinout before connection.',18)
s.text(65,1012,'9 TX + 4 RX + 4 FLEX = 17 GPIOs. Full fit: 13 MOSFETs + 2 hex receiver ICs.',18)
s.line((45,1055),(1555,1055),color=MUTED)
s.text(45,1072,'E. POWER / DEFAULTS',24,ACCENT)
s.text(65,1120,'USB -> Pico 2          Pico 3V3(OUT) -> receiver VCC (pin 14); GND -> pin 7',19)
s.text(65,1154,'Drive regulated 5 V -> +5V_IF pull-ups; drive motor power uses its own connector.',19)
s.text(65,1188,'Do not connect external +5V_IF to Pico VBUS or 3V3. Connect all signal grounds.',19)
s.text(65,1222,'Per IC: 100 nF bypass. Per local rail: 4.7 uF bulk. Ground unused receiver inputs.',19)
s.text(65,1256,'TX GPIOs start LOW. WRITE ARM starts OPEN. FLEX jumpers must match firmware.',19)
s.text(65,1290,'TX pull-ups: normally at drive. RX pull-ups: removable 1k starting value; see notes.',19)
s.text(65,1334,'Unverified: final GPIO map, approved drives, cable loading, pulse widths, power sequencing.',18,MUTED)
s.save('connector-map')
print('Wrote interface-cells and connector-map SVG/PNG.')
