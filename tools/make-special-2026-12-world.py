#!/usr/bin/env python3
"""Build el-special-2026-12-world.pdf — Christmas Around the World (Special December Edition, 2026).

A K-12 special edition for teachers of English learners: an eight-stop world tour of December
traditions (customs only: what people make, cook, carry and light), a 15-school-day countdown
calendar with practice for grades K-5 and 6-12, four coloring pages, two elementary practice pages,
and an eight-page black-and-white ELPA21 practice insert for grades 6-12 with a teacher key.

Run from the repo root:  python3 tools/make-special-2026-12-world.py
All art is drawn in code. Each font instance gets a unique internal name so every weight embeds.
"""
import math, os, random, tempfile
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, Color, white, black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, Flowable, KeepTogether, NextPageTemplate)
from fontTools.ttLib import TTFont as FTFont
from fontTools.varLib import instancer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "el-special-2026-12-world.pdf")
W, H = letter
M = 48; CW = W - 2 * M

# ---------------- fonts ----------------
FD = tempfile.mkdtemp(prefix="wfonts")
def inst(src, name, **loc):
    f = FTFont(src); f.flavor = None
    axes = {a.axisTag: a.defaultValue for a in f["fvar"].axes}; axes.update(loc)
    g = instancer.instantiateVariableFont(f, axes)
    for rec in g["name"].names:
        if rec.nameID in (1, 3, 4, 6, 16): rec.string = "ELW" + name
    p = os.path.join(FD, name + ".ttf"); g.save(p); return p
FR = os.path.join(ROOT, "tools/fonts/Fraunces.ttf"); IN = os.path.join(ROOT, "tools/fonts/Inter.ttf")
FRI = os.path.join(ROOT, "fonts/fraunces-italic.woff2")
for nm, src, loc in [("Fr-X", FR, dict(wght=800, opsz=144, SOFT=0, WONK=0)), ("Fr-B", FR, dict(wght=700, opsz=48, SOFT=0, WONK=0)),
                     ("Fr-S", FR, dict(wght=600, opsz=24, SOFT=0, WONK=0)), ("Fr-R", FR, dict(wght=400, opsz=14, SOFT=0, WONK=0)),
                     ("Fr-I", FRI, dict(wght=500, opsz=36)), ("Fr-IX", FRI, dict(wght=700, opsz=144)),
                     ("In-R", IN, dict(wght=400)), ("In-M", IN, dict(wght=500)), ("In-S", IN, dict(wght=600)),
                     ("In-B", IN, dict(wght=700)), ("In-X", IN, dict(wght=800))]:
    pdfmetrics.registerFont(TTFont(nm, inst(src, nm.replace("-", ""), **loc)))
pdfmetrics.registerFontFamily("In-R", normal="In-R", bold="In-B", italic="Fr-I", boldItalic="In-B")
pdfmetrics.registerFontFamily("Fr-R", normal="Fr-R", bold="Fr-B", italic="Fr-I", boldItalic="Fr-B")

# ---------------- palette ----------------
NAVY = HexColor("#1E2761"); NAVYDK = HexColor("#141A44"); NIGHT = HexColor("#0B0F2C"); GOLD = HexColor("#C9A227"); GOLDLT = HexColor("#EBD9A0")
GOLDINK = HexColor("#7A5F0E"); CREAM = HexColor("#FBF7EC"); PAPER = HexColor("#FFFDF7"); INK = HexColor("#1F2330"); MUTED = HexColor("#555B73")
RULE = HexColor("#D9D3C0"); PINE = HexColor("#2F5D50"); CRAN = HexColor("#9B2D3A"); WASH = HexColor("#F3ECD6"); PINEDK = HexColor("#1C4037"); SNOW = HexColor("#FFFFFF")
GREY = HexColor("#555555"); TINT = HexColor("#EDEDED"); GRULE = HexColor("#9A9A9A"); MID = HexColor("#BDBDBD")
DOM = {"Listening": PINE, "Speaking": CRAN, "Reading": NAVY, "Writing": GOLDINK, "All four": INK}

def S(name, font, size, lead, color=INK, **kw):
    return ParagraphStyle(name, fontName=font, fontSize=size, leading=lead, textColor=color, **kw)
body = S("body", "In-R", 10, 14.2, spaceAfter=6)
lede = S("lede", "Fr-R", 13, 18.5, INK, spaceAfter=8)
h2 = S("h2", "Fr-B", 15, 18, NAVY, spaceBefore=8, spaceAfter=4, keepWithNext=1)
kick = S("kick", "In-X", 8, 10.5, GOLDINK, spaceAfter=3)
small = S("small", "In-R", 8.4, 11.4, MUTED)
bul = S("bul", "In-R", 10, 14.2, leftIndent=12, firstLineIndent=-12, spaceAfter=3)
def P(t, st=body): return Paragraph(t, st)
def BL(items, st=bul): return [Paragraph("•&nbsp; " + t, st) for t in items]

def tracked(c, x, y, t, font, size, color, track=1.2, align="l"):
    c.setFont(font, size); c.setFillColor(color)
    w = pdfmetrics.stringWidth(t, font, size) + track * (len(t) - 1)
    if align == "r": x -= w
    elif align == "c": x -= w / 2
    to = c.beginText(x, y); to.setFont(font, size); to.setCharSpace(track); to.textOut(t); to.setCharSpace(0); c.drawText(to)

# ---------------- art ----------------
def star_path(c, cx, cy, R, r, n=5, rot=90):
    p = c.beginPath()
    for i in range(n * 2):
        a = math.radians(rot + i * 180 / n); rad = R if i % 2 == 0 else r
        (p.moveTo if i == 0 else p.lineTo)(cx + rad * math.cos(a), cy + rad * math.sin(a))
    p.close(); return p

def parol(c, cx, cy, R, line=GOLD, fill=None, glow=True, tails=True, lw=1.6):
    """A Philippine star lantern: five-point star in a ring, with two tassels."""
    if glow:
        for i in range(7, 0, -1):
            c.setFillColor(Color(0.79, 0.64, 0.15, alpha=0.035 * (8 - i) / 2 + 0.01)); c.circle(cx, cy, R * (1 + i * 0.16), stroke=0, fill=1)
    c.setStrokeColor(line); c.setLineWidth(lw)
    if fill: c.setFillColor(fill)
    c.circle(cx, cy, R, stroke=1, fill=0)
    c.drawPath(star_path(c, cx, cy, R * .96, R * .40), stroke=1, fill=1 if fill else 0)
    for i in range(5):                                  # ribs
        a = math.radians(90 + i * 72); c.setLineWidth(lw * .55); c.line(cx, cy, cx + R * .96 * math.cos(a), cy + R * .96 * math.sin(a))
    c.setLineWidth(lw)
    if tails:
        for s in (-1, 1):
            a = math.radians(270 + s * 36); x, y = cx + R * math.cos(a), cy + R * math.sin(a)
            c.line(x, y, x, y - R * .28)
            for k in range(5): c.setLineWidth(lw * .6); c.line(x + (k - 2) * R * .035, y - R * .28, x + (k - 2) * R * .06, y - R * .62)
            c.setLineWidth(lw)

def icon(c, kind, cx, cy, s, lw=1.4, line=black, fill=None, detail=False):
    """Line-art tradition icons. s is roughly half the icon's height. fill=None leaves shapes open for coloring."""
    c.saveState(); c.setStrokeColor(line); c.setLineWidth(lw); c.setLineJoin(1); c.setLineCap(1)
    f = 1 if fill else 0
    if fill: c.setFillColor(fill)
    if kind == "parol":
        c.circle(cx, cy + s * .12, s * .78, stroke=1, fill=0)
        c.drawPath(star_path(c, cx, cy + s * .12, s * .75, s * .31), stroke=1, fill=f)
        if detail:
            c.circle(cx, cy + s * .12, s * .88, stroke=1, fill=0); c.circle(cx, cy + s * .12, s * .17, stroke=1, fill=0)
            for i in range(5):
                a = math.radians(90 + i * 72); c.line(cx + s * .17 * math.cos(a), cy + s * .12 + s * .17 * math.sin(a), cx + s * .75 * math.cos(a), cy + s * .12 + s * .75 * math.sin(a))
            for i in range(10):
                a = math.radians(18 + i * 36); c.circle(cx + s * .83 * math.cos(a), cy + s * .12 + s * .83 * math.sin(a), s * .022, stroke=1, fill=0)
        for sg in (-1, 1):
            a = math.radians(270 + sg * 34); x, y = cx + s * .78 * math.cos(a), cy + s * .12 + s * .78 * math.sin(a)
            c.line(x, y, x, y - s * .12); c.circle(x, y - s * .15, s * .035, stroke=1, fill=0)
            for k in range(5): c.line(x + (k - 2) * s * .02, y - s * .19, x + (k - 2) * s * .045, y - s * .42)
        c.line(cx, cy + s * .9, cx, cy + s * 1.02)
    elif kind == "pinata":
        r = s * .30
        for i in range(7):                                   # seven cones
            a = math.radians(90 + i * 360 / 7); b1 = a - .33; b2 = a + .33
            tip = (cx + s * .88 * math.cos(a), cy + s * .88 * math.sin(a))
            pth = c.beginPath(); pth.moveTo(cx + r * math.cos(b1), cy + r * math.sin(b1)); pth.lineTo(*tip); pth.lineTo(cx + r * math.cos(b2), cy + r * math.sin(b2)); pth.close()
            c.drawPath(pth, stroke=1, fill=f)
            if detail:
                for t in (.45, .68):
                    c.line(cx + (r + (s * .88 - r) * t) * math.cos(a) - s * .12 * (1 - t) * math.sin(a), cy + (r + (s * .88 - r) * t) * math.sin(a) + s * .12 * (1 - t) * math.cos(a),
                           cx + (r + (s * .88 - r) * t) * math.cos(a) + s * .12 * (1 - t) * math.sin(a), cy + (r + (s * .88 - r) * t) * math.sin(a) - s * .12 * (1 - t) * math.cos(a))
            if i != 0:
                for k in (-1, 0, 1): c.line(tip[0], tip[1], tip[0] + k * s * .05 + s * .04 * math.cos(a), tip[1] - s * .16 + s * .02 * k)
        c.circle(cx, cy, r, stroke=1, fill=f)
        if detail: c.circle(cx, cy, r * .55, stroke=1, fill=0)
        c.line(cx, cy + s * .88, cx, cy + s * 1.02)
    elif kind == "fanal":
        w, h = s * 1.05, s * .82; x0, y0 = cx - w / 2, cy - s * .78
        c.rect(x0 - s * .08, y0 - s * .08, w + s * .16, s * .08, stroke=1, fill=f)                  # base
        c.rect(x0, y0, w, h, stroke=1, fill=f)
        pth = c.beginPath(); pth.moveTo(x0 - s * .1, y0 + h); pth.lineTo(cx, y0 + h + s * .62); pth.lineTo(x0 + w + s * .1, y0 + h); pth.close(); c.drawPath(pth, stroke=1, fill=f)
        dw = s * .24; c.rect(cx - dw / 2, y0, dw, s * .36, stroke=1, fill=0); c.circle(cx, y0 + s * .36, dw / 2, stroke=1, fill=0)
        for wx in (x0 + s * .1, x0 + w - s * .1 - s * .22):
            for wy in (y0 + s * .12, y0 + s * .48):
                c.rect(wx, wy, s * .22, s * .22, stroke=1, fill=0); c.line(wx + s * .11, wy, wx + s * .11, wy + s * .22); c.line(wx, wy + s * .11, wx + s * .22, wy + s * .11)
        c.circle(cx, y0 + h + s * .24, s * .09, stroke=1, fill=0)
        c.drawPath(star_path(c, cx, y0 + h + s * .78, s * .14, s * .06), stroke=1, fill=f)
        if detail:
            for k in range(1, 5):
                yy = y0 + h + s * .62 * k / 5; half = (w / 2 + s * .1) * (1 - k / 5); c.line(cx - half, yy, cx + half, yy)
    elif kind == "skate":
        x0, y0 = cx - s * .62, cy - s * .42
        pth = c.beginPath(); pth.moveTo(x0, y0); pth.lineTo(x0 + s * 1.3, y0); pth.curveTo(x0 + s * 1.36, y0 + s * .3, x0 + s * 1.1, y0 + s * .42, x0 + s * .78, y0 + s * .5)
        pth.lineTo(x0 + s * .62, y0 + s * 1.3); pth.lineTo(x0 + s * .08, y0 + s * 1.3); pth.lineTo(x0, y0); pth.close(); c.drawPath(pth, stroke=1, fill=f)
        c.rect(x0 - s * .02, y0 - s * .1, s * 1.34, s * .1, stroke=1, fill=f)
        for wx in (x0 + s * .22, x0 + s * 1.06):
            c.circle(wx, y0 - s * .28, s * .19, stroke=1, fill=f); c.circle(wx, y0 - s * .28, s * .06, stroke=1, fill=0)
        c.circle(x0 + s * 1.38, y0 - s * .04, s * .09, stroke=1, fill=f)                           # toe stop
        for k in range(4):
            yy = y0 + s * (.62 + k * .16); c.line(x0 + s * .34, yy, x0 + s * .66 - k * s * .012, yy + s * .05)
        c.line(x0 + s * .06, y0 + s * 1.3, x0 + s * .64, y0 + s * 1.3)
        if detail:
            c.line(x0 + s * .08, y0 + s * 1.12, x0 + s * .64, y0 + s * 1.12)
            c.drawPath(star_path(c, x0 + s * .2, y0 + s * .32, s * .13, s * .055), stroke=1, fill=0)
    elif kind == "crown":
        c.ellipse(cx - s * .8, cy - s * .55, cx + s * .8, cy - s * .15, stroke=1, fill=f)
        for k in range(5):
            x = cx + (k - 2) * s * .32; yb = cy - s * .22 + abs(k - 2) * s * .03
            c.rect(x - s * .06, yb, s * .12, s * .62, stroke=1, fill=f)
            pth = c.beginPath(); pth.moveTo(x, yb + s * .62); pth.curveTo(x - s * .12, yb + s * .78, x - s * .04, yb + s * .92, x, yb + s * 1.0); pth.curveTo(x + s * .04, yb + s * .92, x + s * .12, yb + s * .78, x, yb + s * .62)
            c.drawPath(pth, stroke=1, fill=f)
        for k in range(6):
            x = cx + (k - 2.5) * s * .28; c.ellipse(x - s * .1, cy - s * .5, x + s * .1, cy - s * .36, stroke=1, fill=0)
    elif kind == "books":
        ws = [(1.3, 0), (1.12, .06), (1.22, -.04)]
        for k, (wd, off) in enumerate(ws):
            x0 = cx - s * wd / 2 + s * off - s * .12; y0 = cy - s * .7 + k * s * .3
            c.rect(x0, y0, s * wd, s * .28, stroke=1, fill=f); c.line(x0 + s * .14, y0, x0 + s * .14, y0 + s * .28); c.line(x0 + s * wd - s * .1, y0 + s * .06, x0 + s * wd - s * .1, y0 + s * .22)
        mx, my = cx + s * .5, cy + s * .22
        c.rect(mx - s * .2, my, s * .4, s * .36, stroke=1, fill=f); c.ellipse(mx + s * .16, my + s * .08, mx + s * .36, my + s * .28, stroke=1, fill=0)
        for k in (-1, 1):
            pth = c.beginPath(); pth.moveTo(mx + k * s * .07, my + s * .42); pth.curveTo(mx + k * s * .07 + s * .08, my + s * .52, mx + k * s * .07 - s * .08, my + s * .6, mx + k * s * .07, my + s * .7); c.drawPath(pth, stroke=1, fill=0)
    elif kind == "tamal":
        c.ellipse(cx - s * .95, cy - s * .62, cx + s * .95, cy - s * .2, stroke=1, fill=f)
        c.roundRect(cx - s * .6, cy - s * .36, s * 1.2, s * .5, s * .16, stroke=1, fill=f)
        for k in (-1, 1):
            x = cx + k * s * .38; c.line(x, cy - s * .36, x, cy + s * .14); c.line(x - s * .03, cy + s * .14, x - s * .1, cy + s * .26); c.line(x + s * .03, cy + s * .14, x + s * .1, cy + s * .26)
        for k in (-1, 0, 1):
            x = cx + k * s * .22; pth = c.beginPath(); pth.moveTo(x, cy + s * .32); pth.curveTo(x + s * .1, cy + s * .46, x - s * .1, cy + s * .58, x, cy + s * .74); c.drawPath(pth, stroke=1, fill=0)
    elif kind == "bowl":
        pth = c.beginPath(); pth.moveTo(cx - s * .75, cy - s * .05); pth.curveTo(cx - s * .7, cy - s * .75, cx + s * .7, cy - s * .75, cx + s * .75, cy - s * .05); pth.close(); c.drawPath(pth, stroke=1, fill=f)
        c.ellipse(cx - s * .75, cy - s * .17, cx + s * .75, cy + s * .07, stroke=1, fill=f)
        c.rect(cx - s * .28, cy - s * .72, s * .56, s * .08, stroke=1, fill=f)
        c.line(cx + s * .3, cy - s * .02, cx + s * .78, cy + s * .42)
        c.drawPath(star_path(c, cx - s * .1, cy + s * .62, s * .26, s * .11), stroke=1, fill=f)
    elif kind == "genna":
        for sg in (-1, 1):                                   # two crossed sticks with curved ends
            pth = c.beginPath(); pth.moveTo(cx + sg * s * .62, cy + s * .82); pth.lineTo(cx - sg * s * .34, cy - s * .5)
            pth.curveTo(cx - sg * s * .46, cy - s * .7, cx - sg * s * .74, cy - s * .66, cx - sg * s * .78, cy - s * .42); c.drawPath(pth, stroke=1, fill=0)
        c.circle(cx, cy - s * .62, s * .16, stroke=1, fill=f)
    c.restoreState()

MEDALS = [("pinata", "MEXICO", "Las Posadas", CRAN), ("parol", "THE PHILIPPINES", "The parol", GOLDINK), ("tamal", "GUATEMALA", "Tamales at midnight", PINE), ("skate", "VENEZUELA", "Las patinatas", NAVY),
          ("fanal", "HAITI", "The fanal", GOLDINK), ("bowl", "UKRAINE", "The twelve dishes", NAVY), ("crown", "SWEDEN", "The crown of candles", CRAN), ("genna", "ETHIOPIA", "Genna", PINE)]

def cover(c, doc):
    c.saveState(); random.seed(7)
    c.setFillColor(CREAM); c.rect(0, 0, W, H, stroke=0, fill=1)
    c.setFillColor(PINEDK); c.rect(0, H - 128, W, 128, stroke=0, fill=1); c.setFillColor(GOLD); c.rect(0, H - 132, W, 4, stroke=0, fill=1)
    for _ in range(46):
        c.setFillColor(Color(1, 1, 1, alpha=random.uniform(.18, .5))); c.circle(random.uniform(0, W), random.uniform(H - 124, H - 4), random.choice((.7, 1, 1.4)), stroke=0, fill=1)
    c.setFillColor(white); c.setFont("Fr-X", 42); c.drawString(M, H - 78, "EL PUBLISHING")
    tracked(c, M, H - 100, "THE ENGLISH LEARNER MAGAZINE", "In-S", 7.8, GOLDLT, 2.4)
    tracked(c, W - M, H - 100, "SPECIAL DECEMBER EDITION  ·  2026", "In-S", 7.8, GOLDLT, 2.2, "r")
    c.setFillColor(GOLD); c.roundRect(W - M - 104, H - 76, 104, 30, 15, stroke=0, fill=1); tracked(c, W - M - 52, H - 66, "GRADES K–12", "In-X", 8.6, NAVYDK, 1.6, "c")
    c.setFillColor(NAVY); c.setFont("Fr-X", 64); c.drawString(M, H - 208, "Christmas around")
    c.drawString(M, H - 272, "the"); x = M + pdfmetrics.stringWidth("the", "Fr-X", 64) + 18
    c.setFillColor(CRAN); c.setFont("Fr-IX", 70); c.drawString(x, H - 272, "world.")
    c.setFillColor(GOLD); c.rect(M, H - 292, 72, 4, stroke=0, fill=1)
    c.setFillColor(INK); c.setFont("Fr-R", 13.4)
    for i, ln in enumerate(["Eight traditions, a 15-day countdown, coloring pages, and practice for the state tests.", "What people make, cook, carry and light in December, for every grade."]):
        c.drawString(M, H - 318 - i * 18.5, ln)
    gw = CW / 4; y0 = H - 440
    for i, (kind, place, name, col) in enumerate(MEDALS):
        cx = M + gw * (i % 4) + gw / 2; cy = y0 - (i // 4) * 158
        c.setFillColor(SNOW); c.setStrokeColor(col); c.setLineWidth(2.4); c.circle(cx, cy, 48, stroke=1, fill=1)
        c.setLineWidth(.7); c.circle(cx, cy, 53, stroke=1, fill=0)
        icon(c, kind, cx, cy - (2 if kind in ("parol", "pinata") else -4 if kind in ("fanal", "skate") else 0), 30 if kind not in ("tamal", "bowl", "crown", "books", "genna") else 28, lw=1.3, line=NAVYDK, fill=HexColor("#F6E7B4"))
        tracked(c, cx, cy - 70, place, "In-X", 7.2, col, 1.4, "c"); c.setFillColor(NAVY); c.setFont("Fr-S", 10.6); c.drawCentredString(cx, cy - 84, name)
    c.setStrokeColor(RULE); c.setLineWidth(.8); c.line(M, 58, W - M, 58)
    tracked(c, M, 40, "FOR EVERY TEACHER IN THE BUILDING  ·  36 PAGES  ·  FREE", "In-S", 6.8, MUTED, 1.4)
    tracked(c, W - M, 40, "MANY VOICES · ONE STORM", "In-S", 6.8, GOLDINK, 1.4, "r")
    c.restoreState()

def back(c, doc):
    c.saveState(); random.seed(5)
    c.setFillColor(PINEDK); c.rect(0, 0, W, H, stroke=0, fill=1)
    for _ in range(90):
        c.setFillColor(Color(1, 1, 1, alpha=random.uniform(.15, .5))); c.circle(random.uniform(0, W), random.uniform(0, H), random.choice((.6, .9, 1.3)), stroke=0, fill=1)
    parol(c, W / 2, H - 230, 78, line=HexColor("#E9C25A"), lw=2)
    c.setStrokeColor(Color(.92, .76, .35, alpha=.7)); c.setLineWidth(1); c.line(W / 2, H - 152, W / 2, H)
    c.setFillColor(white); c.setFont("Fr-X", 34); c.drawCentredString(W / 2, 360, "Every language carries")
    c.setFillColor(GOLD); c.setFont("Fr-IX", 38); c.drawCentredString(W / 2, 318, "a light.")
    c.setFillColor(GOLDLT); c.setFont("Fr-R", 12.5)
    c.drawCentredString(W / 2, 282, "More than 110 free resources for teachers of English learners,")
    c.drawCentredString(W / 2, 265, "with no account and no cost.")
    c.setFillColor(GOLD); c.roundRect(W / 2 - 150, 196, 300, 40, 4, stroke=0, fill=1)
    c.setFillColor(NAVYDK); c.setFont("In-B", 13); c.drawCentredString(W / 2, 211, "radan55.github.io/everyteacher")
    tracked(c, W / 2, 120, "EL PUBLISHING", "Fr-B", 15, white, 1.5, "c")
    tracked(c, W / 2, 102, "MANY VOICES  ·  ONE STORM", "In-S", 7.6, GOLD, 2.4, "c")
    c.setFont("In-R", 8.4); c.setFillColor(HexColor("#D5E2DC"))
    c.drawCentredString(W / 2, 74, "Edited by Richard A. Daniel, M.Ed.  ·  Special December Edition, 2026  ·  Grades K–12")
    c.drawCentredString(W / 2, 60, "Original text and art. Not an official ELPA21 publication.")
    c.restoreState()

def ed_page(label):
    def deco(c, doc):
        c.saveState(); c.setFillColor(CREAM); c.rect(0, 0, W, H, stroke=0, fill=1)
        c.setFillColor(PINEDK); c.rect(0, H - 30, W, 30, stroke=0, fill=1); c.setFillColor(GOLD); c.rect(0, H - 32.5, W, 2.5, stroke=0, fill=1)
        tracked(c, M, H - 19.5, "CHRISTMAS AROUND THE WORLD", "In-S", 7, GOLDLT, 1.8)
        tracked(c, W - M, H - 19.5, label.upper(), "In-S", 7, white, 1.8, "r")
        c.setStrokeColor(RULE); c.setLineWidth(.6); c.line(M, 40, W - M, 40)
        tracked(c, M, 27, "EL PUBLISHING  ·  SPECIAL DECEMBER EDITION 2026  ·  GRADES K–12", "In-S", 6.6, MUTED, 1.4)
        c.setFont("Fr-B", 11); c.setFillColor(NAVY); c.drawRightString(W - M, 25, str(doc.page))
        c.restoreState()
    return deco

def ins_page(c, doc):
    c.saveState(); n = doc.page - INS0 + 1
    c.setFont("In-X", 7.4); c.setFillColor(GREY); c.drawString(M, H - 30, "EL PUBLISHING  ·  ELPA21 PRACTICE INSERT  ·  GRADES 6–12")
    key = n in (6, 7)
    c.setFont("In-B" if key else "In-R", 8 if key else 8.8)
    c.drawRightString(W - M, H - 30, "TEACHER KEY · DO NOT COPY FOR STUDENTS" if key else "Name ________________________   Date __________")
    c.setStrokeColor(GRULE); c.setLineWidth(.5); c.line(M, 36, W - M, 36)
    c.setFont("In-R", 7.4); c.drawString(M, 24, "ELPA21-style classroom practice by EL Publishing. Not released test items.  ·  radan55.github.io/everyteacher")
    c.setFont("In-B", 9); c.setFillColor(black); c.drawRightString(W - M, 24, f"Insert {n} / 8   ·   {doc.page}")
    c.restoreState()

def plain_page(label):
    def deco(c, doc):
        c.saveState(); c.setFont("In-X", 7.4); c.setFillColor(GREY); c.drawString(M, H - 30, "EL PUBLISHING  ·  CHRISTMAS AROUND THE WORLD  ·  " + label.upper())
        c.setFont("In-R", 8.8); c.drawRightString(W - M, H - 30, "Name ________________________   Date __________")
        c.setStrokeColor(GRULE); c.setLineWidth(.5); c.line(M, 36, W - M, 36)
        c.setFont("In-R", 7.4); c.drawString(M, 24, "Free to copy for classroom use.  ·  radan55.github.io/everyteacher")
        c.setFont("In-B", 9); c.setFillColor(black); c.drawRightString(W - M, 24, str(doc.page)); c.restoreState()
    return deco

class Art(Flowable):
    """A tradition icon as a flowable (small, for practice pages; large, for coloring pages)."""
    def __init__(self, kind, s, lw=1.4, detail=False, pad=6): super().__init__(); self.k, self.s, self.lw, self.d, self.pad = kind, s, lw, detail, pad
    def wrap(self, aw, ah): self.aw = aw; return aw, self.s * 2.2 + self.pad
    def draw(self): icon(self.canv, self.k, self.aw / 2, self.s * 1.05 + self.pad / 2, self.s, lw=self.lw, detail=self.d)

class Outline(Flowable):
    """Big hollow lettering to color in."""
    def __init__(self, text, size=62): super().__init__(); self.t, self.s = text, size
    def wrap(self, aw, ah): self.aw = aw; return aw, self.s * 1.05
    def draw(self):
        c = self.canv; w = pdfmetrics.stringWidth(self.t, "Fr-X", self.s)
        to = c.beginText((self.aw - w) / 2, self.s * .22); to.setFont("Fr-X", self.s); to.setTextRenderMode(1); c.setLineWidth(1.3); c.setStrokeColor(black); to.textOut(self.t); to.setTextRenderMode(0); c.drawText(to)

class Trace(Flowable):
    """Pale lettering on a baseline for tracing."""
    def __init__(self, text, size=30, width=None): super().__init__(); self.t, self.s, self.w = text, size, width
    def wrap(self, aw, ah): self.aw = self.w or aw; return self.aw, self.s * 1.45
    def draw(self):
        c = self.canv; c.setStrokeColor(GRULE); c.setLineWidth(.7); c.line(0, self.s * .3, self.aw, self.s * .3)
        c.setDash(2, 3); c.line(0, self.s * .3 + self.s * .52, self.aw, self.s * .3 + self.s * .52); c.setDash()
        c.setFillColor(HexColor("#B8B8B8")); c.setFont("In-M", self.s); c.drawString(4, self.s * .3, self.t)

# ---------------- flowables ----------------
class Title(Flowable):
    def __init__(self, kicker, title, gold=None, size=40): super().__init__(); self.k, self.t, self.g, self.s = kicker, title, gold, size
    def wrap(self, aw, ah): self.aw = aw; return aw, self.s + 34
    def draw(self):
        c = self.canv; tracked(c, 0, self.s + 22, self.k.upper(), "In-X", 8.2, GOLDINK, 2)
        c.setFillColor(NAVY); c.setFont("Fr-X", self.s); c.drawString(0, 12, self.t)
        if self.g:
            x = pdfmetrics.stringWidth(self.t, "Fr-X", self.s) + self.s * .27; c.setFillColor(CRAN); c.setFont("Fr-IX", self.s); c.drawString(x, 12, self.g)
        c.setFillColor(GOLD); c.rect(0, 0, 64, 3.5, stroke=0, fill=1)

class Lines(Flowable):
    def __init__(self, n, gap=19): super().__init__(); self.n, self.gap = n, gap
    def wrap(self, aw, ah): self.aw = aw; return aw, self.n * self.gap + 2
    def draw(self):
        c = self.canv; c.setStrokeColor(GRULE); c.setLineWidth(.6)
        for i in range(self.n): c.line(0, (self.n - 1 - i) * self.gap + 2, self.aw, (self.n - 1 - i) * self.gap + 2)

class Band(Flowable):
    def __init__(self, domain, task, mins): super().__init__(); self.d, self.t, self.m = domain, task, mins
    def wrap(self, aw, ah): self.aw = aw; return aw, 44
    def draw(self):
        c = self.canv; c.setFillColor(black); c.rect(0, 40, self.aw, 3, stroke=0, fill=1)
        c.setFont("Fr-X", 25); c.drawString(0, 12, self.d)
        c.setFont("In-X", 8.2); c.setFillColor(GREY); c.drawRightString(self.aw, 26, self.t.upper())
        c.setFont("In-S", 8.6); c.drawRightString(self.aw, 13, self.m)
        c.setStrokeColor(GRULE); c.setLineWidth(.6); c.line(0, 3, self.aw, 3)

class DayTag(Flowable):
    """Countdown number, date and domain chip for a calendar row."""
    def __init__(self, n, date, dom): super().__init__(); self.n, self.date, self.dom = n, date, dom
    def wrap(self, aw, ah): return 78, 80
    def draw(self):
        c = self.canv; col = DOM[self.dom]
        c.setFillColor(col); c.setFont("Fr-X", 44); c.drawString(0, 36, str(self.n))
        tracked(c, 0, 22, self.date.upper(), "In-B", 7.4, INK, 1)
        w = pdfmetrics.stringWidth(self.dom.upper(), "In-X", 6.6) + 6.6 * .8 * len(self.dom) * .15 + 12
        c.roundRect(0, 2, w, 13, 6.5, stroke=0, fill=1); tracked(c, 6, 5.6, self.dom.upper(), "In-X", 6.6, white, .9)

class Lantern(Flowable):
    """Line drawing for Compare Pictures. Variant A or B (six differences)."""
    def __init__(self, v, w=250, h=146): super().__init__(); self.v, self.w, self.h = v, w, h
    def wrap(self, aw, ah): return self.w, self.h
    def draw(self):
        c = self.canv; A = self.v == "A"; w, h = self.w, self.h
        c.setStrokeColor(black); c.setLineWidth(1.1); c.rect(0, 0, w, h, stroke=1, fill=0)
        cx, cy, R = w / 2, h / 2 + 10, 40
        c.line(cx, cy + R, cx, h)                                                     # hanging string
        if not A: c.setFillColor(black); c.circle(cx, cy + R + 10, 3.2, stroke=0, fill=1)   # bead on string (B)
        n = 5 if A else 6
        if A: c.circle(cx, cy, R, stroke=1, fill=0)                                    # ring only in A
        c.setFillColor(TINT if A else white); c.drawPath(star_path(c, cx, cy, R * .96, R * (.40 if A else .52), n), stroke=1, fill=1)
        c.setFillColor(MID if A else white); c.circle(cx, cy, 9, stroke=1, fill=1)      # centre: shaded in A
        tails = (-1, 1) if A else (-1, 0, 1)
        for s in tails:
            a = math.radians(270 + s * 34); x, y = cx + R * math.cos(a), cy + R * math.sin(a)
            c.line(x, y, x, y - 9)
            for k in range(5): c.line(x + (k - 2) * 2, y - 9, x + (k - 2) * 3.2, y - 24)
        c.setFillColor(black)
        if A:                                                                        # small stars around A
            for (x, y) in [(28, 112), (212, 100), (34, 46), (220, 42)]: c.drawPath(star_path(c, x, y, 5, 2.2), stroke=0, fill=1)
        c.setFont("In-X", 10); c.drawString(8, h - 16, "LANTERN " + self.v)

class Timeline(Flowable):
    EV = [(6, "Dec 6", "St. Nicholas Day", "Germany", False, "l"), (13, "Dec 13", "St. Lucia Day", "Sweden", False, "c"), (25, "Dec 25", "Christmas Day", "many countries", False, "c"),
          (37, "Jan 6", "Three Kings Day", "Spain, Latin America", True, "r"), (38, "Jan 7", "Genna", "Ethiopia", False, "l")]
    def __init__(self, w): super().__init__(); self.w = w
    def wrap(self, aw, ah): return self.w, 162
    def draw(self):
        c = self.canv; x0, x1, y = 16, self.w - 16, 76; sc = (x1 - x0) / 34.0
        X = lambda d: x0 + (d - 5) * sc
        c.setFont("In-B", 9.4); c.setFillColor(black); c.drawString(0, 151, "Winter celebrations on a timeline, December 5 to January 8")
        c.setStrokeColor(black); c.setLineWidth(1.2); c.line(x0, y, x1, y)
        c.setFillColor(MID); c.rect(X(16), y - 6, X(24) - X(16), 12, stroke=1, fill=1)
        mx = (X(16) + X(24)) / 2; c.setFillColor(black); c.setFont("In-B", 8.6); c.drawCentredString(mx, y + 36, "Las Posadas")
        c.setFont("In-R", 8); c.drawCentredString(mx, y + 25, "Dec 16–24 · Mexico"); c.setLineWidth(.6); c.line(mx, y + 7, mx, y + 22)
        for d, date, name, place, up, al in self.EV:
            x = X(d); c.setLineWidth(1); c.setFillColor(white); c.circle(x, y, 4.2, stroke=1, fill=1)
            yy = (y + 52) if up else (y - 30); c.setLineWidth(.6); c.line(x, y + 5 if up else y - 5, x, yy + (-3 if up else 11))
            fn = {"l": c.drawString, "c": c.drawCentredString, "r": c.drawRightString}[al]; dx = {"l": -12 if d == 6 else 2, "c": 0, "r": -2}[al]
            c.setFillColor(black); c.setFont("In-B", 8.6); fn(x + dx, yy + (10 if up else 0), name)
            c.setFont("In-R", 8); fn(x + dx, yy + (0 if up else -10), f"{date} · {place}")

def mc(n, stem, options):
    out = [P(f"<b>{n}.</b>&nbsp; {stem}", q)]
    cells = [P(f"<font name='In-B'>{chr(65 + i)}</font>&nbsp;&nbsp; {o}", optc) for i, o in enumerate(options)]
    longest = max(len(o) for o in options)
    cols = 4 if longest <= 12 else 2 if longest <= 44 else 1
    if cols == 1: out += [P(f"<font name='In-B'>{chr(65 + i)}</font>&nbsp;&nbsp; {o}", opt) for i, o in enumerate(options)]
    else:
        rows = [cells] if cols == 4 else [[cells[0], cells[1]], [cells[2], cells[3]]]
        t = Table(rows, colWidths=[(CW - 18) / cols] * cols, hAlign="RIGHT")
        t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5), ("VALIGN", (0, 0), (-1, -1), "TOP")]))
        out.append(t)
    return KeepTogether(out)

def box(fl, pad=8, bg=TINT, line=black, width=None, lw=.8):
    t = Table([[fl]], colWidths=[width or CW])
    t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), lw, line), ("BACKGROUND", (0, 0), (-1, -1), bg), ("LEFTPADDING", (0, 0), (-1, -1), pad + 2), ("RIGHTPADDING", (0, 0), (-1, -1), pad + 2),
                           ("TOPPADDING", (0, 0), (-1, -1), pad), ("BOTTOMPADDING", (0, 0), (-1, -1), pad)]))
    return t

def cols(parts, widths, gap=16, valign="TOP"):
    t = Table([parts], colWidths=widths)
    st = [("VALIGN", (0, 0), (-1, -1), valign), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), gap), ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (-1, 0), (-1, 0), 0)]
    t.setStyle(TableStyle(st)); return t

# insert styles
q = S("q", "In-S", 10.5, 14, black, leftIndent=18, firstLineIndent=-18, spaceBefore=5.5, spaceAfter=2.5, keepWithNext=1)
opt = S("opt", "In-R", 10.3, 13.6, black, leftIndent=34, firstLineIndent=-16, spaceAfter=1)
optc = S("optc", "In-R", 10.3, 13.6, black, leftIndent=16, firstLineIndent=-16)
read = S("read", "Fr-R", 10.6, 14.5, black, spaceAfter=4)
dirs = S("dirs", "In-R", 10.2, 14, black, spaceAfter=6)
ih2 = S("ih2", "In-X", 9.4, 12.4, black, spaceBefore=9, spaceAfter=4, keepWithNext=1)
keyS = S("key", "In-R", 9.2, 12.5, black, spaceAfter=3)
keyH = S("keyH", "In-X", 8.8, 11.5, black, spaceBefore=7, spaceAfter=3, keepWithNext=1)
script = S("script", "Fr-R", 9.7, 13.2, black, leftIndent=8, spaceAfter=4)
ismall = S("ismall", "In-R", 8.6, 11.4, GREY)

# ---------------- document ----------------
doc = BaseDocTemplate(OUT, pagesize=letter, leftMargin=M, rightMargin=M, topMargin=48, bottomMargin=48,
                      title="Christmas Around the World · Special December Edition 2026 · EL Publishing", author="Richard A. Daniel, M.Ed. · EL Publishing",
                      subject="A special edition for teachers of English learners: world tour, 15-day countdown calendar, ELPA21 practice insert")
full = Frame(0, 0, W, H, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
def edf(): return Frame(M, 48, CW, H - 48 - 50, leftPadding=0, rightPadding=0, topPadding=6, bottomPadding=0)
TEMPL = {"cover": PageTemplate(id="cover", frames=[full], onPage=cover), "back": PageTemplate(id="back", frames=[Frame(0, 0, W, H)], onPage=back),
         "ins": PageTemplate(id="ins", frames=[Frame(M, 44, CW, H - 44 - 46, leftPadding=0, rightPadding=0, topPadding=4, bottomPadding=0)], onPage=ins_page)}
LABELS = ["Contents", "Every grade", "The world tour", "Say it", "One lesson, any grade", "The countdown", "Coaching notes", "ELA standards", "ELA for every classroom", "Every subject", "Every teacher", "A note for the last day"]
for l in ("Coloring page", "Elementary practice", "State test prep"):
    TEMPL[l] = PageTemplate(id=l, frames=[Frame(M, 44, CW, H - 44 - 46, leftPadding=0, rightPadding=0, topPadding=4, bottomPadding=0)], onPage=plain_page(l))
for l in LABELS: TEMPL[l] = PageTemplate(id=l, frames=[edf()], onPage=ed_page(l))
doc.addPageTemplates(list(TEMPL.values()))
INS0 = 19      # first page of the insert
F = [NextPageTemplate("Contents"), Spacer(1, 1), PageBreak()]

# ---------- p2 contents + editor ----------
toc = [("03", "Every grade, K to 12", "What to use with each grade band"), ("04", "The world tour", "Eight December traditions to read, with the words to teach"),
       ("06", "Say it", "A December greeting in fourteen languages"), ("07", "One lesson, any grade", "The same routine from kindergarten to grade 12"),
       ("08", "The countdown", "15 school days of practice for K–5 and 6–12, with coaching notes"), ("12", "Coaching notes", "What to listen for in each domain, and what to say next"),
       ("13", "Coloring pages", "Four traditions to color, trace and talk about"), ("17", "Elementary practice", "Listen and circle for K–2; read, answer and write for 3–5"),
       ("19", "ELPA21 practice insert", "Eight pages for grades 6–12, with a teacher key"), ("27", "ELA standards and activities", "For the general education classroom teacher"),
       ("29", "Every subject, every teacher", "One activity per subject, and five moves for any room"), ("31", "State test prep", "Math, science and history practice, with a key"),
       ("35", "A note for the last day", "For the teacher, before the building empties")]
rows = [[P(a, S("tn", "Fr-X", 17, 19, GOLDINK)), [P(b, S("tt", "Fr-B", 12.2, 15, NAVY)), P(c_, S("ts", "In-R", 8.6, 11.4, MUTED))]] for a, b, c_ in toc]
tt = Table(rows, colWidths=[38, 222]); tt.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -2), .5, RULE), ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5), ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
letter_ = [P("FROM THE EDITOR", kick), P("The world is already in your room.", S("eh", "Fr-B", 19, 22.5, NAVY, spaceAfter=8)),
           P("In December a classroom of English learners holds more geography than the textbook. One student is counting the nights until Las Posadas. Another knows how many tamales it takes to feed twenty cousins. "
             "A third can tell you exactly which street in her home city has the best lights.", body),
           P("This special edition treats that knowledge as curriculum. Each stop on the tour is a short, true text about a tradition: what people make, cook, carry and light. "
             "It comes with the words worth teaching and one classroom move for older students and one for younger ones.", body),
           P("The edition now runs from kindergarten to grade 12. There are coloring pages and listen-and-circle practice for the youngest learners, a reading page for grades 3–5, "
             "and an ELPA21-style insert for grades 6–12, all on the same eight traditions.", body),
           P("It is also for the whole building. There are ELA standards and activities for the classroom teacher, one activity for every subject from math to music, and five moves any teacher can use tomorrow.", body),
           P("The countdown calendar turns the fifteen school days before break into fifteen small practices. December is long, and teachers are tired, so every day also carries one line that is only for you.", body),
           Spacer(1, 6), P("Richard A. Daniel, M.Ed.", S("sig", "Fr-I", 13, 16, NAVY)), P("ENL / EL Specialist · Editor", small)]
F += [Title("In this edition", "Christmas around the", "world.", 34), Spacer(1, 14), cols([[P("CONTENTS", kick), tt], letter_], [276, CW - 276], gap=28), NextPageTemplate("Every grade"), PageBreak()]

# ---------- p3 every grade ----------
BANDS = [("K–2", CRAN, "10–20 minutes", "Coloring pages 13–16 · Listen and circle, page 17 · the greeting wall",
          "Listen and point. Name and color. Say one sentence with a frame. Trace one sentence.", "“This is a ___.” · “I see ___.” · “My light is ___.”"),
         ("3–5", GOLDINK, "20–30 minutes", "Read, answer and write, page 18 · coloring pages as speaking prompts · tour stops read aloud",
          "Read a short text and answer. Put three events in order. Write two or three sentences.", "“First ___. Then ___. Last ___.” · “I like ___ best because ___.”"),
         ("6–8", PINE, "30–45 minutes", "The tour stops as texts · ELPA21 insert, pages 19–26 (read the directions aloud the first time)",
          "Listen for details. Compare two traditions. Reply to a classmate. Support an answer with a date.", "“Both ___, but ___.” · “The timeline shows ___.”"),
         ("9–12", NAVY, "45–90 minutes", "The full lesson on page 7 · ELPA21 insert, pages 19–26 · family interview, page 26",
          "Explain a cause. Build a claim with a reason and support. Report an interview in connected sentences.", "“___ because ___.” · “I believe ___. For example, ___.”")]
rows = [[P(h, S("bh", "In-B", 8.6, 11, white)) for h in ("Grades", "Time", "Use these pages", "Students will", "Frames")]]
for g, col, tm, pages_, will, fr in BANDS:
    rows.append([P(g, S("bg", "Fr-X", 21, 23, col)), P(tm, S("bt", "In-S", 9, 12.4)), P(pages_, S("bp", "In-R", 9, 12.6)), P(will, S("bw", "In-R", 9, 12.6)), P(fr, S("bf", "Fr-I", 9.6, 13, MUTED))])
t = Table(rows, colWidths=[56, 62, 150, 142, CW - 410])
t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), PINEDK), ("ROWBACKGROUNDS", (0, 1), (-1, -1), [PAPER, WASH]), ("LINEBELOW", (0, 1), (-1, -1), .4, RULE), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
F += [Title("How to use this edition", "Every grade,", "K to 12.", 36), Spacer(1, 8),
      P("The eight traditions are the same for every student. What changes is how much language each grade band is asked to take in and produce. Find your band, then turn to the pages listed.", S("lede3", "Fr-R", 12.4, 17.4, INK, spaceAfter=8)),
      t, P("Three things that stay the same in every grade", h2),
      *BL(["<b>Traditions, not beliefs.</b> Every page is about what people do: the lantern, the food, the skates, the songs. Students describe customs; nobody is asked what a family believes.",
           "<b>Home language first.</b> A child who can name the dish in Spanish, Vietnamese or Haitian Creole already has the idea. English is added to it, not put in its place.",
           "<b>Every student produces language every day.</b> One spoken sentence in kindergarten; one paragraph in grade 12."]),
      Spacer(1, 6),
      box([P("KEY FOR THE ELEMENTARY PRACTICE PAGES", S("ek", "In-X", 7.6, 10, GOLDINK, spaceAfter=4)),
           P("<b>Page 17, Listen and circle (K–2).</b> Read each line twice. 1. “Circle the star lantern.” (the star in a ring) &nbsp; 2. “Circle the thing with wheels.” (the skate) &nbsp; "
             "3. “Circle the little paper house.” (the house) &nbsp; 4. “Circle the thing you can read.” (the books)", S("ek2", "In-R", 9.2, 12.8, spaceAfter=4)),
           P("<b>Page 18, Read, answer and write (3–5).</b> 1 A &nbsp;·&nbsp; 2 A &nbsp;·&nbsp; 3 B &nbsp;·&nbsp; In order: neighbors walk from house to house (1), they sing and ask to come in (2), the last house opens the door (3). "
             "Written answers: accept any complete sentence on topic.", S("ek3", "In-R", 9.2, 12.8))], pad=10, bg=WASH, line=RULE),
      NextPageTemplate("The world tour"), PageBreak()]

# ---------- p4-5 world tour ----------
STOPS = [
 ("Mexico and Central America", "Las Posadas", "December 16–24", CRAN,
  "For nine nights, neighbors walk from house to house carrying candles and singing. At each door they ask for <i>posada</i>, a place to stay, and are turned away, until the last house opens and everyone is welcomed in. "
  "Then comes the piñata, traditionally a star with seven points, and cups of hot fruit punch called <i>ponche</i>.",
  "posada (a place to stay) · piñata · ponche · villancico (carol)", "<b>Sequence.</b> Retell the night in four sentences with <i>first, then, until, finally</i>.", "Count the seven points on the piñata page. “First we walk. Then we sing.”"),
 ("The Philippines", "The parol", "September to January", GOLDINK,
  "Star-shaped lanterns called <i>parols</i> hang in windows and along streets, traditionally made of bamboo sticks and thin paper. The season is long here: carols can be heard as early as September. "
  "On December 24, families share a late-night meal called <i>Noche Buena</i>.",
  "parol (star lantern) · Noche Buena · Maligayang Pasko", "<b>Describe.</b> Read the text aloud; students draw the lantern from what they hear, then label it.", "Color the parol. Point to the star, the circle and the tassels."),
 ("Guatemala", "Tamales at midnight", "December 24", PINE,
  "On December 24, many families in Guatemala spend the day making tamales together, dozens at a time, each one wrapped in a leaf and steamed. At midnight the neighborhood fills with fireworks, "
  "and everyone eats tamales with a cup of hot fruit punch.",
  "tamal · ponche (fruit punch) · cohetes (firecrackers) · medianoche (midnight)", "<b>Explain a process.</b> “First they ___. Next they ___.” How does a family make a hundred of anything?", "“We make ___ at my house.” Draw a food your family makes together."),
 ("Venezuela", "Las patinatas", "December 16–24", NAVY,
  "In Caracas, a December tradition sends whole neighborhoods out on roller skates early in the morning. Some streets are closed to cars so that skaters can travel safely, and afterward families share <i>hallacas</i>, "
  "corn dough filled with meat and wrapped in plantain leaves.",
  "patinata (skating party) · aguinaldo (carol) · hallaca", "<b>Ask questions.</b> Pairs write three questions for a skater, then trade and answer.", "Color the skate. “The skate has ___ wheels.” Act out: fast, slow, stop."),
 ("Haiti", "The fanal", "December 24", GOLDINK,
  "Haitian children and craftspeople build <i>fanals</i>: paper lanterns shaped like little houses, cut with tiny windows and lit from inside. They glow on porches and in windows on the night of December 24, "
  "when many families stay up for a late meal called the <i>réveillon</i>.",
  "fanal (paper lantern) · réveillon (late-night meal) · Jwaye Nwèl", "<b>Compare.</b> A fanal and a parol are both paper lanterns. List two similarities and two differences.", "Count the windows on the fanal page. “The house has a door and ___ windows.”"),
 ("Ethiopia", "Genna", "January 7", PINE,
  "Ethiopia keeps its own calendar, with thirteen months, so its Christmas, called <i>Genna</i>, falls on January 7. Many people dress in white and gather early in the morning. "
  "Later in the day some play a game with sticks and a ball, also called genna, that looks like field hockey, and families eat together from one large plate.",
  "Genna · injera (flatbread) · Melkam Genna (Happy Christmas)", "<b>Explain a cause.</b> “Ethiopia celebrates on January 7 because ___.” Use the insert's listening script.", "Find January 7 on the class calendar. “It is after ___.”"),
 ("Ukraine", "The twelve dishes", "December 24", NAVY,
  "The family waits for the first star in the evening sky before sitting down to twelve dishes. The first is <i>kutia</i>, wheat sweetened with honey and poppy seeds. A sheaf of wheat called a <i>didukh</i> stands in the room, "
  "and children go from house to house singing carols called <i>koliadky</i>.",
  "kutia · didukh (sheaf of wheat) · koliadky (carols)", "<b>Sequence and number.</b> The class sets its own table of twelve dishes from students' homes, one sentence each.", "Count to twelve with paper plates. Each child draws one food and names it."),
 ("Sweden", "The crown of candles", "December 13", CRAN,
  "On one of the darkest mornings of the year, a girl chosen as Lucia wears a white gown, a red sash and a crown of candles, and leads a line of singers through the school or town. Families serve saffron buns called <i>lussekatter</i>. "
  "The custom comes from the old idea that this was the longest night of winter.",
  "Lucia · lussekatt (saffron bun) · God Jul (Merry Christmas)", "<b>Describe from a picture.</b> Describe what Lucia wears to a partner who cannot see the picture.", "“She has a ___ on her head.” Count the candles. Name the colors: white, red."),
]
def stop(place, name, date, col, text, words, move, young):
    left = [P(place.upper(), S("sp", "In-X", 7.4, 9.6, col)), P(name, S("sn", "Fr-B", 14.6, 17, NAVY, spaceAfter=1)), P(date, S("sd", "Fr-I", 10, 12.4, MUTED, spaceAfter=4)), P(text, S("st", "In-R", 9.2, 12.9))]
    lab = lambda t_: P(t_, S("sw", "In-X", 6.8, 9, GOLDINK, spaceAfter=1.5)); tx = lambda t_, sa=5: P(t_, S("sw2" + str(sa), "In-R", 8.6, 11.8, INK, spaceAfter=sa))
    right = [lab("WORDS TO TEACH"), tx(words), lab("GRADES 6–12"), tx(move), lab("GRADES K–5"), tx(young, 0)]
    t = Table([[left, right]], colWidths=[CW * .56, CW * .44])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BACKGROUND", (0, 0), (0, 0), PAPER), ("BACKGROUND", (1, 0), (1, 0), WASH), ("BOX", (0, 0), (-1, -1), .6, RULE), ("LINEBEFORE", (0, 0), (0, 0), 4, col),
                           ("LEFTPADDING", (0, 0), (0, 0), 14), ("LEFTPADDING", (1, 0), (1, 0), 11), ("RIGHTPADDING", (0, 0), (-1, -1), 11), ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    return t
F += [Title("Eight stops", "The world", "tour.", 34), Spacer(1, 4),
      P("Each stop is a text you can read aloud, project or hand out. Customs vary from family to family and town to town, so invite students to correct and add to what is printed here.", S("wl", "Fr-R", 10.8, 15, INK, spaceAfter=6))]
for i, s_ in enumerate(STOPS):
    F += [stop(*s_), Spacer(1, 6)]
    if i == 3: F += [PageBreak(), Title("Eight stops, continued", "The world", "tour.", 30), Spacer(1, 8)]
F += [NextPageTemplate("Say it"), PageBreak()]

# ---------- p6 say it ----------
GREET = [("Spanish", "Feliz Navidad"), ("Haitian Creole", "Jwaye Nwèl"), ("Portuguese", "Feliz Natal"), ("French", "Joyeux Noël"), ("Tagalog", "Maligayang Pasko"), ("Vietnamese", "Chúc mừng Giáng sinh"),
         ("German", "Frohe Weihnachten"), ("Italian", "Buon Natale"), ("Swedish", "God Jul"), ("Swahili", "Heri ya Krismasi"), ("Ukrainian", "Z Rizdvom!"), ("Amharic", "Melkam Genna"),
         ("Arabic", "Eid Milad Majid"), ("Mandarin Chinese", "Shèngdàn kuàilè")]
cells = [[P(l.upper(), S("gl", "In-X", 7, 9.5, GOLDINK, spaceAfter=2)), P(g, S("gg", "Fr-B", 14.5, 18, NAVY))] for l, g in GREET]
rows = [cells[i:i + 2] for i in range(0, len(cells), 2)]
t = Table(rows, colWidths=[CW / 2, CW / 2]); t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), .5, RULE), ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("VALIGN", (0, 0), (-1, -1), "TOP")]))
F += [Title("The greeting wall", "Say", "it.", 40), Spacer(1, 8),
      P("A greeting in a student's language, said badly by a teacher who tried, is one of the cheapest ways to build trust. Post these, then let students correct your pronunciation. That correction is a speaking task.", lede),
      t, Spacer(1, 10),
      box([P("THREE NOTES", S("tn2", "In-X", 7.6, 10, GOLDINK, spaceAfter=4)),
           *BL(["Ukrainian, Amharic, Arabic and Mandarin are written here in Latin letters. Ask a student or family member to write the greeting in its own script for your wall.",
                "With younger grades, teach two greetings a day. Children say the greeting, then say whose language it is: “That is how Linh's family says it.”",
                "Add a blank row to your wall and ask every student: <i>What do people say to each other at a happy time in your family?</i>"], S("gb", "In-R", 9.4, 13.2, leftIndent=12, firstLineIndent=-12, spaceAfter=3))], pad=10, bg=WASH, line=RULE),
      NextPageTemplate("One lesson, any grade"), PageBreak()]

# ---------- p7 the block ----------
blk = [["Min", "Stage", "What happens", "Domain"],
       ["0–10", "Open the map", "Project the cover. Students choose one of the eight circles and say one thing they know or notice about it, in any language. Chart what they say.", "Speaking"],
       ["10–25", "Listen", "Read one stop aloud twice. First time: listen. Second time: students note three facts. Pairs compare notes.", "Listening"],
       ["25–45", "Read", "Hand out the same stop. Students underline the sentence that answers each of your three questions. Teach four words from “Words to teach.”", "Reading"],
       ["45–60", "Talk", "Use the stop's “In class” move. Every student speaks to a partner before anyone speaks to the room.", "Speaking"],
       ["60–80", "Write", "One paragraph: what happens, when, and how it is like or unlike something the student knows. Frames by lane, below.", "Writing"],
       ["80–90", "Close", "Three students read one sentence aloud. Exit line: “Something I did not know before is ___.”", "All four"]]
t = Table([[P(c_, S("bk", "In-B" if i == 0 or j < 2 else "In-R", 9.2, 12.6, white if i == 0 else (DOM.get(c_, INK) if j == 3 else INK))) for j, c_ in enumerate(r)] for i, r in enumerate(blk)], colWidths=[44, 84, CW - 198, 70])
t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), PINEDK), ("ROWBACKGROUNDS", (0, 1), (-1, -1), [PAPER, WASH]), ("LINEBELOW", (0, 1), (-1, -1), .4, RULE), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 4.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5)]))
def lane(name, col, text): return [P(name.upper(), S("ln", "In-X", 7.6, 10, col, spaceAfter=3)), P(text, S("lb", "In-R", 9.3, 13))]
lanes = Table([[lane("Newcomer · K–2", CRAN, "Draws or colors the tradition and labels it from a word bank. Says or copies: “This is ___. People ___.”"),
                lane("Emerging · 3–5", GOLDINK, "“In ___, people ___ on ___. First they ___. Then they ___.” Three sentences, with the four taught words."),
                lane("Progressing", PINE, "“This tradition is similar to ___ because both ___. One difference is that ___, while ___.” A full paragraph."),
                lane("Challenge", NAVY, "Explains why the tradition exists and what it shows about what the community values, with one detail from the text as evidence.")]], colWidths=[CW / 4] * 4)
lanes.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BOX", (0, 0), (-1, -1), .6, RULE), ("INNERGRID", (0, 0), (-1, -1), .6, RULE), ("BACKGROUND", (0, 0), (-1, -1), PAPER), ("TOPPADDING", (0, 0), (-1, -1), 9), ("BOTTOMPADDING", (0, 0), (-1, -1), 9), ("LEFTPADDING", (0, 0), (-1, -1), 9), ("RIGHTPADDING", (0, 0), (-1, -1), 9)]))
bt = Table([[P(x, S("btm", "In-B" if i == 0 else "In-R", 9, 12.2, white if i == 0 else INK, alignment=1)) for x in r] for i, r in enumerate([["", "K–2", "3–5", "6–8", "9–12"], ["Whole lesson", "20 min", "30 min", "45 min", "90 min"], ["Stages to use", "Open · Listen · Talk", "Open · Listen · Read · Talk", "All six, shortened", "All six, as written"]])], colWidths=[92, (CW - 92) / 4, (CW - 92) / 4, (CW - 92) / 4, (CW - 92) / 4])
bt.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), PINEDK), ("BACKGROUND", (0, 1), (-1, -1), PAPER), ("GRID", (0, 0), (-1, -1), .5, RULE), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
F += [Title("The same routine, K to 12", "One lesson, any", "grade.", 34), Spacer(1, 6),
      P("Pick one stop on the tour. The lesson runs the same way every time, so by the third stop students know the routine and all of their attention goes to the language. The times below are for grades 9–12; the small table shows how to shorten it.", S("lede4", "Fr-R", 11.6, 16.2, INK, spaceAfter=7)), t, Spacer(1, 7), bt,
      P("The writing task in four lanes", h2), lanes, Spacer(1, 10),
      box([P("<b>Shorter periods.</b> In a 50-minute class, run Open, Listen and Read on day one, and Talk, Write and Close on day two. "
             "<b>Content teachers.</b> A social studies, art or music teacher can use any stop as a bell-ringer text: read, three questions, one sentence.", S("sh", "In-R", 9.5, 13.4))], pad=10, bg=WASH, line=RULE),
      NextPageTemplate("The countdown"), PageBreak()]

# ---------- p8-11 the countdown ----------
DAYS = [
 (15, "Mon · Nov 30", "Listening", "Read the Philippines stop aloud twice. Students draw a parol from what they hear, then label three parts.", "Color the parol (page 13) while you read. Children point to the star, the circle and the tassels.", "Read at natural speed. Lengthen the pause between sentences, not the words.", "The first day back is for finding your footing. Theirs and yours."),
 (14, "Tue · Dec 1", "Speaking", "“A light in my house.” Forty-five seconds to a partner about a light that matters at home.", "Draw a light at home, then tell a partner: “My light is ___.”", "Count seconds of student talk, not teacher talk. Every student speaks before you do.", "A sentence spoken in a new language is an act of courage. You will hear thirty of them today."),
 (13, "Wed · Dec 2", "Reading", "Insert, Reading Part A: the parol paragraph, questions 1–3.", "Grades 3–5: page 18, the reading and questions 1–3. K–2: trace and read <i>star</i> and <i>light</i> on page 17.", "Before choosing a letter, students underline the sentence that proves it. Evidence first.", "Nobody remembers the worksheet. They remember who noticed them."),
 (12, "Thu · Dec 3", "Writing", "Insert, Writing Part A, then four sentences retelling Las Posadas with <i>first, then, until, finally</i>.", "Trace the sentence on a coloring page. Grades 3–5 add one sentence of their own.", "Mark only the verbs today. One target is feedback. Ten is noise.", "Mark less. Mean more."),
 (11, "Fri · Dec 4", "All four", "Gallery walk: post four stops. Pairs read one, tell another pair, and write the most surprising fact.", "Picture walk: post the four coloring pages. Partners name what they see and one color they will use.", "Stand at one poster for the whole rotation. You hear more language standing still.", "It is Friday. Something worked this week. Name it before you leave the building."),
 (10, "Mon · Dec 7", "Listening", "Insert, Listening: Recordings 1 and 2, questions 1–6.", "Page 17, Listen and circle, items 1–4. Read each line twice.", "Give thirty seconds to look at the questions or pictures before you read. Predicting is a listening skill.", "In Guatemala a whole family folds tamales at one table. Nobody learns alone. Pair them up."),
 (9, "Tue · Dec 8", "Speaking", "Insert, Speaking Part A: compare the two lanterns, then the partner check.", "Compare two finished coloring pages: “Mine is ___. Yours is ___.”", "Listen for <i>both, while</i> and <i>but</i>. Write what you hear on the board with the student's name.", "Your students are translating their whole lives in real time. Be impressed out loud."),
 (8, "Wed · Dec 9", "Reading", "Insert, Reading Part B: “The Book Flood,” questions 4–8.", "Book flood: each child chooses a class book for a friend and says why. “I pick this for ___ because ___.”", "Let pairs talk through the last question before anyone writes. Talk is the rehearsal for writing.", "In Iceland the best gift is a book and a quiet night. You are in the business of giving both."),
 (7, "Thu · Dec 10", "Writing", "Insert, Writing Part B: reply to Linh's email.", "A card for a classmate: “Dear ___, I like your ___.” Draw, write, deliver.", "Students number the questions in the task, then number their answers to match.", "Five honest sentences are worth more than a page that was copied."),
 (6, "Fri · Dec 11", "All four", "Twelve dishes: the class sets a table of twelve foods from students' homes. One sentence and one label each.", "Each child draws one food from home on a paper plate, names it, and adds it to the class table.", "Accept the dish's name in the home language. Ask for an English description, not an English name.", "There is room at the table for every language in the room. Set the places."),
 (5, "Mon · Dec 14", "Listening", "Insert, Listening: Recording 3, questions 7–10, with two-column notes.", "Listen and draw: describe the fanal. “Draw a little house. It has a door, four windows and a star on top.”", "Model the first two steps only. Then stop talking and let them finish.", "Some of your students will celebrate on another day. Every one of them belongs in your room today."),
 (4, "Tue · Dec 15", "Speaking", "Insert, Speaking Part B: the timeline and the two claims.", "Calendar talk: find today, then December 24. “It is ___ days away. It is after ___.”", "Require a date or a number in every answer. “The timeline shows” is a habit the test rewards.", "A second language grows slowly, then suddenly. You are in the slow part. Keep going."),
 (3, "Wed · Dec 16", "Reading", "Students choose any stop and write two questions for a partner: one answered in the text, one that takes thinking.", "Grades 3–5: page 18, put Las Posadas in order. K–2: match three word cards to the coloring pages.", "Collect what they write. It shows who understood, and it is tomorrow's warm-up.", "Tonight Las Posadas begins: nine nights of knocking until a door opens. You open one every morning."),
 (2, "Thu · Dec 17", "Writing", "Insert, Writing Part C: build a claim about teaching traditions from many countries.", "Finish and illustrate: “My favorite tradition is ___ because ___.”", "Score the claim, the reason and the support separately. Tell each student which one to fix.", "You taught a child to disagree politely in a second language. That is not a small thing."),
 (1, "Fri · Dec 18", "All four", "Family interview report-back (page 26): forty-five seconds each. The class listens for one thing they did not know.", "Show and tell: a drawing of a family celebration, and two sentences about it.", "Put the pen down. Today only listen, and thank each speaker by name.", "Go home. Rest is part of the work. They will need you whole in January."),
]
# at a glance
gl = [[P(d, S("gh", "In-X", 7.6, 10, white, alignment=1)) for d in ("MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY")]]
short = {15: "Draw or color the parol", 14: "A light in my house", 13: "Parol reading", 12: "Retell or trace", 11: "Gallery or picture walk", 10: "Listen and answer", 9: "Compare lanterns",
         8: "The book flood", 7: "Reply or card", 6: "Twelve dishes", 5: "Listen, note or draw", 4: "Timeline and calendar", 3: "Questions and order", 2: "Claim or favorite", 1: "Report from home"}
for wk in range(3):
    row = []
    for n, date, dom, *_ in DAYS[wk * 5:wk * 5 + 5]:
        col = DOM[dom].hexval()[2:]
        row.append([P(f"<font name='Fr-X' size='26' color='#{col}'>{n}</font>", S("gn", "Fr-X", 26, 28)), P(date.split("· ")[1].upper(), S("gd", "In-B", 7.4, 10, MUTED, spaceAfter=3)),
                    P(dom.upper(), S("gdm", "In-X", 7.2, 9.6, DOM[dom], spaceAfter=2)), P(short[n], S("gs", "In-R", 8.8, 11.6))])
    gl.append(row)
t = Table(gl, colWidths=[CW / 5] * 5, rowHeights=[20, 92, 92, 92])
t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), PINEDK), ("BACKGROUND", (0, 1), (-1, -1), PAPER), ("GRID", (0, 0), (-1, -1), .6, RULE), ("VALIGN", (0, 1), (-1, -1), "TOP"), ("VALIGN", (0, 0), (-1, 0), "MIDDLE"),
                       ("TOPPADDING", (0, 1), (-1, -1), 7), ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 6)]))
legend = Table([[P(f"<font color='#{DOM[d].hexval()[2:]}'>■</font>&nbsp; <b>{d}</b>&nbsp; {x}", S("lg", "In-R", 9, 12.4)) for d, x in (("Listening", "Mondays"), ("Speaking", "Tuesdays"), ("Reading", "Wednesdays"), ("Writing", "Thursdays"), ("All four", "Fridays"))]], colWidths=[CW / 5] * 5)
legend.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0)]))
F += [Title("15 school days to winter break", "The", "countdown.", 40), Spacer(1, 8),
      P("One domain a day, ten to fifteen minutes, from the Monday after Thanksgiving to the last Friday before break. Each day has a <b>practice</b> for grades 6–12 and one for K–5, a <b>coaching note</b> for you, and a <b>note for the day</b> that is only yours.", S("lede5", "Fr-R", 12.2, 17, INK, spaceAfter=8)),
      t, Spacer(1, 8), legend, Spacer(1, 10),
      box([P("HOW TO USE IT", S("hu", "In-X", 7.6, 10, GOLDINK, spaceAfter=4)),
           *BL(["The dates follow a calendar with school in session November 30 to December 18, 2026. If your break starts earlier, begin at the number that matches your days left and keep the order.",
                "Every day has a practice for <b>grades 6–12</b> and one for <b>grades K–5</b>. “Insert” means the ELPA21 practice insert on pages 19–26; the K–5 practices use the coloring pages (13–16) and the elementary pages (17–18).",
                "Short on time? Keep the Monday-to-Thursday domain days and drop the Fridays.",
                "The three pages that follow give every day in full. Copy them for a co-teacher, a paraprofessional or a substitute."], S("hb", "In-R", 9.4, 13.2, leftIndent=12, firstLineIndent=-12, spaceAfter=3))], pad=10, bg=WASH, line=RULE),
      PageBreak()]
WEEK = [("Week one", "Light", "Lanterns, candles and porch lights: how people answer the dark."), ("Week two", "The table", "What families cook, burn, read and carry into the season."),
        ("Week three", "Home", "Different dates, different customs, and the report from home.")]
def dayrow(n, date, dom, practice, young, coach, light):
    L = lambda t_, col=MUTED: P(t_, S("dl" + col.hexval(), "In-X", 6.6, 8.6, col, spaceAfter=1))
    T = lambda t_, sa=3: P(t_, S("dp" + str(sa), "In-R", 8.7, 11.5, INK, spaceAfter=sa))
    mid = [L("GRADES 6–12", DOM[dom]), T(practice), L("GRADES K–5", DOM[dom]), T(young), L("COACHING NOTE"), T(coach, 0)]
    right = [P("A NOTE FOR THE DAY", S("dl3", "In-X", 6.6, 8.6, GOLDINK, spaceAfter=3)), P(light, S("dn", "Fr-I", 10.6, 14, NAVY))]
    t = Table([[DayTag(n, date, dom), mid, right]], colWidths=[90, CW - 90 - 156, 156])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BACKGROUND", (0, 0), (1, 0), PAPER), ("BACKGROUND", (2, 0), (2, 0), WASH), ("BOX", (0, 0), (-1, -1), .6, RULE), ("LINEBEFORE", (0, 0), (0, 0), 4, DOM[dom]),
                           ("LEFTPADDING", (0, 0), (0, 0), 14), ("LEFTPADDING", (1, 0), (2, 0), 11), ("RIGHTPADDING", (0, 0), (-1, -1), 9), ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
    return t
for wk, (kk, name, sub) in enumerate(WEEK):
    F += [Title(f"The countdown · {kk}", name + ".", None, 26), Spacer(1, 2), P(sub, S("ws", "Fr-R", 11, 14, MUTED, spaceAfter=5))]
    for d in DAYS[wk * 5:wk * 5 + 5]: F += [dayrow(*d), Spacer(1, 4)]
    F += [PageBreak()]
F[-1:] = [NextPageTemplate("Coaching notes"), PageBreak()]

# ---------- p12 coaching notes ----------
CO = [("Listening", "Did the student catch the detail, or only the topic? Ask “What exactly did you hear?”", "“Tell me one word you heard that you did not know.” Then teach that word and read the sentence again.", "Repeating the script slower and louder. Read it the same way twice, then check."),
      ("Speaking", "Connected sentences. One long turn tells you more than five one-word answers.", "“Say more about that.” Then wait five full seconds. Count them.", "Finishing the student's sentence. The pause is where the language is being built."),
      ("Reading", "Can the student point to the sentence that proves the answer?", "“Show me where it says that.” A finger on the line is an answer.", "Pre-teaching every hard word. Teach four; let the text teach the rest."),
      ("Writing", "Does the writing answer every part of the task? Count the parts with the student.", "“You answered two of the three questions. Which one is missing?”", "Correcting every error in red. Choose one pattern, show it once, and have the student fix the others.")]
rows = [[P(h, S("ch", "In-B", 8.6, 11, white)) for h in ("Domain", "Listen for", "Say next", "Avoid")]]
for d, a, b, c_ in CO:
    rows.append([P(d, S("cd", "Fr-B", 12.5, 15, DOM[d])), P(a, S("cc", "In-R", 9.3, 13)), P(b, S("cc2", "In-R", 9.3, 13)), P(c_, S("cc3", "In-R", 9.3, 13))])
t = Table(rows, colWidths=[78, (CW - 78) / 3, (CW - 78) / 3, (CW - 78) / 3])
t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), PINEDK), ("ROWBACKGROUNDS", (0, 1), (-1, -1), [PAPER, WASH]), ("LINEBELOW", (0, 1), (-1, -1), .4, RULE), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
F += [Title("For the adult in the room", "Coaching", "notes.", 40), Spacer(1, 8),
      P("Whether you are coaching a colleague, a paraprofessional or yourself, the question in December is the same: what did the student just show me, and what do I say next?", lede), t,
      P("Five habits for the fifteen days", h2),
      *BL(["<b>Two students, not twenty.</b> Each day, choose two students to listen to closely. In three weeks you will have real notes on every one.",
           "<b>Write down exact words.</b> “<i>In my house we doing tamales</i>” is data. “She struggles with verbs” is an opinion.",
           "<b>Name the growth out loud.</b> “In September you answered in one word. Today you gave me a reason.” Say it where others can hear.",
           "<b>Let the home language work.</b> A minute of planning in Spanish or Vietnamese produces better English than a minute of silence.",
           "<b>End every practice with one sentence from every student.</b> Spoken or written. No student leaves December having only listened."]),
      Spacer(1, 6),
      box([P("FOR CONTENT TEACHERS", S("fc", "In-X", 7.6, 10, GOLDINK, spaceAfter=4)),
           P("You do not need the whole calendar. Take one row a week. A social studies teacher can use the insert's listening script on calendars; a math teacher can use the timeline; "
             "an art teacher can use the coloring pages; an English teacher can use “The Book Flood.” The coaching note on each day applies to any subject.", S("fb", "In-R", 9.5, 13.4))], pad=10, bg=WASH, line=RULE),
      NextPageTemplate("Coloring page"), PageBreak()]

# ---------- p13-16 coloring pages ----------
COLOR = [("parol", "parol", "A star lantern · the Philippines", "This is a star."), ("pinata", "piñata", "A star with seven points · Mexico", "I see seven points."),
         ("fanal", "fanal", "A paper house lantern · Haiti", "It is a little house."), ("skate", "skate", "Skating in December · Venezuela", "The skate has wheels.")]
for i, (kind, word, sub, sent) in enumerate(COLOR):
    F += [P("COLOR · TRACE · TELL", S("ck", "In-X", 9, 12, GREY, alignment=1, spaceAfter=2)), Outline(word, 66),
          P(sub, S("cs", "Fr-I", 14, 18, black, alignment=1, spaceAfter=4)), Art(kind, 168, lw=2.6, detail=True, pad=10), Spacer(1, 4),
          P("TRACE", S("ct", "In-X", 8, 10, GREY, spaceAfter=2)), Trace(sent, 34), Spacer(1, 8), P("WRITE OR TELL", S("ct2", "In-X", 8, 10, GREY, spaceAfter=0)),
          cols([P("I see ____________________ .", S("cw", "In-M", 15, 28, black)), P("My colors are ______________ .", S("cw2", "In-M", 15, 28, black))], [CW * .5, CW * .5], gap=20),
          NextPageTemplate("Coloring page" if i < 3 else "Elementary practice"), PageBreak()]

# ---------- p17-18 elementary practice ----------
def iconrow(n, kinds):
    cells = [P(f"<b>{n}</b>", S("irn", "Fr-X", 26, 28, black))] + [Art(k, 30, lw=1.6) for k in kinds]
    t = Table([cells], colWidths=[40] + [(CW - 40) / 3] * 3)
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("BOX", (0, 0), (-1, -1), .8, black), ("LINEAFTER", (0, 0), (0, 0), .8, black), ("INNERGRID", (1, 0), (-1, 0), .5, GRULE), ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3), ("LEFTPADDING", (0, 0), (0, 0), 12)]))
    return t
F += [Band("Listen and circle", "Grades K–2 · your teacher reads each line twice", "about 10 minutes"),
      P("Listen to your teacher. Circle the picture.", S("ed", "In-M", 14, 19, black, spaceAfter=6)),
      iconrow(1, ["books", "parol", "skate"]), Spacer(1, 5), iconrow(2, ["tamal", "fanal", "skate"]), Spacer(1, 5), iconrow(3, ["pinata", "books", "fanal"]), Spacer(1, 5), iconrow(4, ["parol", "books", "tamal"]),
      P("TRACE AND SAY", ih2), cols([Trace("star", 34), Trace("light", 34), Trace("book", 34), Trace("home", 34)], [CW / 4] * 4, gap=14),
      P("DRAW AND TELL · A LIGHT IN MY HOME", ih2), box([Spacer(1, 96)], bg=white, pad=4), Spacer(1, 6),
      P("My light is ______________________________ .", S("ef", "In-M", 15, 22, black)), PageBreak(),
      Band("Read, answer, write", "Grades 3–5", "about 20 minutes"),
      P("Read the paragraph. Then answer the questions.", S("ed2", "In-R", 11.4, 15, black, spaceAfter=6)),
      box([P("The Star Lantern", S("et", "Fr-B", 14, 17, black, spaceAfter=4)),
           P("In the Philippines, many families hang a star lantern in the window in December. The lantern is called a parol. It is made from bamboo sticks and thin paper. "
             "A small light inside makes it glow. Many families build their parol together.", S("er", "Fr-R", 13, 19, black))], pad=9)]
def mc3(n, stem, options):
    return KeepTogether([P(f"<b>{n}.</b>&nbsp; {stem}", S("q3", "In-S", 11.6, 15.4, black, spaceBefore=8, spaceAfter=3)),
                         cols([P(f"<font name='In-B'>{chr(65 + i)}</font>&nbsp;&nbsp; {o}", S("o3", "In-R", 11.4, 15, black)) for i, o in enumerate(options)], [(CW - 20) / 3] * 3, gap=8)])
F += [mc3(1, "What is a parol?", ["a star lantern", "a kind of bread", "a game"]), mc3(2, "What is a parol made from?", ["bamboo and paper", "glass and metal", "wood and cloth"]),
      mc3(3, "What makes the parol glow?", ["the sun", "a small light inside", "bright paint"]),
      P("<b>4.</b>&nbsp; What would you put on your own lantern? Write one sentence.", S("q4", "In-S", 11.6, 15.4, black, spaceBefore=9, spaceAfter=2)),
      P("My lantern has ______________________ and ______________________ .", S("f4", "In-M", 12.6, 24, black)),
      P("PUT IT IN ORDER · LAS POSADAS", ih2), P("Write 1, 2 and 3 to show the order.", S("ed3", "In-R", 11, 14.6, black, spaceAfter=5))]
od = Table([[P("____", S("ob", "In-B", 13, 18, black)), P(x, S("ox", "In-R", 12, 18, black))] for x in ("The last house opens the door.", "Neighbors walk from house to house.", "They sing and ask to come in.")], colWidths=[48, CW - 48])
od.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), .4, GRULE), ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5), ("LEFTPADDING", (0, 0), (0, -1), 0)]))
tl = Table([[Art(k, 22, lw=1.3) for k in ("parol", "pinata", "fanal", "skate")], [P(w_, S("tw", "In-B", 10.4, 13, black, alignment=1)) for w_ in ("parol", "piñata", "fanal", "skate")]], colWidths=[CW / 4] * 4)
tl.setStyle(TableStyle([("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
F += [od, P("TELL A PARTNER", ih2), tl, P("Which one do you like best? Why? &nbsp;&nbsp;<i>I like the ______ best because ______.</i>", S("tp", "In-R", 11.4, 16, black, spaceBefore=3)),
      NextPageTemplate("ins"), PageBreak()]

# ================= INSERT (8 pages, black and white) =================
plan = [["Part", "Domain", "Task type", "Insert page", "Calendar day"], ["1", "Reading", "Short paragraph · Informational passage", "1–2", "13, 8"], ["2", "Listening", "Announcement · Conversation · Explanation", "3", "10, 5"],
        ["3", "Writing", "Editing · Reply to a classmate · Build a claim", "4", "12, 7, 2"], ["4", "Speaking", "Compare pictures · A visual and a claim", "5", "9, 4"], ["5", "Home", "Family interview, then report back", "8", "1"]]
t = Table([[P(x, S("pl", "In-B" if i == 0 else "In-R", 9.2, 12, black)) for x in r] for i, r in enumerate(plan)], colWidths=[40, 70, 270, 68, 68])
t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, 0), .9, black), ("LINEBELOW", (0, 1), (-1, -1), .4, GRULE), ("BACKGROUND", (0, 0), (-1, 0), TINT), ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5)]))
F += [P("PULL OUT AND COPY · GRADES 6–12 · PRINTS IN BLACK AND WHITE", S("ik", "In-X", 8.2, 11, GREY, spaceAfter=3)),
      P("ELPA21 Practice Insert", S("icov", "Fr-X", 32, 34, black, spaceAfter=3)),
      P("Four domains on one theme: <i>how the world keeps December.</i> Use it with the countdown calendar or on its own.", S("idek", "Fr-R", 12.6, 17, black, spaceAfter=9)),
      t, Spacer(1, 10), Band("Reading", "Part A · Short paragraph", "about 6 minutes"),
      P("Read the paragraph. Then choose the best answer to each question.", dirs),
      box([P("In the Philippines, the Christmas season is easy to see. Star-shaped lanterns called parols hang in windows, on streetlights and outside stores. A traditional parol is made from bamboo sticks and thin paper. "
             "A candle or a small bulb inside makes it glow. Some families buy their lanterns, but many still build one together each year. The city of San Fernando is famous for giant lanterns that are about twenty feet across.", S("rb", "Fr-R", 11.4, 16, black))]),
      mc(1, "What is a parol?", ["a kind of Christmas food", "a star-shaped lantern", "a city in the Philippines", "a song sung in December"]),
      mc(2, "What is a traditional parol made from?", ["bamboo and paper", "glass and metal", "plastic and wire", "wood and cloth"]),
      mc(3, "Which detail shows that making parols is still a family activity?", ["Parols hang outside stores.", "A small bulb makes the lantern glow.", "Many families still build one together each year.", "San Fernando has giant lanterns."]),
      PageBreak(),
      Band("Reading", "Part B · Informational passage", "about 14 minutes"), P("Read the passage. Then answer questions 4–8.", dirs),
      P("The Book Flood", S("rt", "Fr-B", 15, 18, black, spaceAfter=5)),
      P("<b>1</b>&nbsp;&nbsp;In Iceland, the most common Christmas gift is a book. The tradition has a name, <i>Jólabókaflóð</i>, which means “Christmas book flood.” Most of the country's new books are published in the weeks before the holiday, "
        "so bookstores suddenly fill with new titles.", read),
      P("<b>2</b>&nbsp;&nbsp;The tradition began during the Second World War. Many goods from other countries were hard to get, and people could not buy the gifts they wanted. Paper, however, was easier to find. "
        "Books became the gift that almost everyone could give.", read),
      P("<b>3</b>&nbsp;&nbsp;In 1944, publishers began sending a catalog of new books to every home in the country. Families still read it each autumn and mark the titles they hope to receive.", read),
      P("<b>4</b>&nbsp;&nbsp;Gifts are opened on the evening of December 24. Afterward, many people go to bed early with their new book and read late into the night, often with a cup of hot chocolate. "
        "In a country where winter nights are very long, a good story is a practical gift.", read),
      mc(4, "What is the main idea of the passage?", ["Iceland has very long winter nights.", "Giving books at Christmas is an Icelandic tradition with a history.", "Paper was easy to find during the Second World War.", "Bookstores in Iceland are busy all year."]),
      mc(5, "According to the passage, why did books become a common gift?", ["Books were cheaper than toys.", "Schools required students to read.", "Other goods were hard to get, but paper was easier to find.", "Publishers gave books away for free."]),
      mc(6, "Which <b>two</b> things happen on December 24, according to the passage? Choose <b>two</b>. (2 points)", ["Families open their gifts in the evening.", "Publishers mail a catalog to every home.", "Many people read their new book late into the night.", "Bookstores close for the winter."]),
      mc(7, "Why is the tradition called a <u>flood</u>?", ["Many new books arrive at the same time.", "Iceland has a lot of rain in winter.", "The books are about rivers and the sea.", "People read near the water."]),
      P("<b>8.</b>&nbsp; Explain why the author calls a story “a practical gift.” Use one detail from the passage. (2 points)", q), Lines(3, 17), PageBreak(),

      Band("Listening", "Three recordings · your teacher reads each one twice", "about 15 minutes"),
      P("Listen carefully. You may take notes in the box. Then choose the best answer. You will not see the words your teacher reads.", dirs),
      box([P("MY NOTES", S("nl", "In-X", 8, 10, GREY)), Spacer(1, 14)], bg=white, pad=4),
      P("RECORDING 1 · A SCHOOL ANNOUNCEMENT", ih2),
      mc(1, "When is Winter Around the World Night?", ["Monday, December 7", "Thursday, December 10", "Friday, December 11", "Thursday, December 17"]),
      mc(2, "Where should students sign up?", ["in the cafeteria", "in the library", "in room 114", "in the main office"]),
      mc(3, "What may students bring?", ["only food from a restaurant", "a dish or a decoration from a tradition", "a gift for a teacher", "a costume for a play"]),
      P("RECORDING 2 · A CONVERSATION BETWEEN TWO STUDENTS", ih2),
      mc(4, "What are Linh and Mateo making?", ["a poster for a class display", "a lantern for a contest", "a video about Vietnam", "a meal for their families"]),
      mc(5, "Why does Linh's family go downtown on Christmas Eve?", ["to visit their cousins", "to see the lights and take pictures", "to buy gifts for friends", "to walk in a posada"]),
      mc(6, "What do the two students decide?", ["to make two separate posters", "to write only about Mexico", "to build the poster around the idea of light", "to ask the teacher for a new topic"]),
      P("RECORDING 3 · A SOCIAL STUDIES TEACHER EXPLAINS", ih2),
      mc(7, "What is the teacher mainly explaining?", ["why Ethiopia's Christmas is on January 7", "how field hockey is played", "why calendars have twelve months", "what people eat in Ethiopia"]),
      mc(8, "How many months are in Ethiopia's calendar?", ["7", "12", "13", "25"]),
      mc(9, "What is Genna?", ["a city in Ethiopia", "a kind of white clothing", "the Ethiopian name for Christmas", "a calendar"]),
      mc(10, "According to the teacher, what do many people do on that day?", ["dress in white and gather early", "roller-skate through the city", "give each other books", "eat twelve dishes"]),
      PageBreak(),

      Band("Writing", "Editing · Reply to a classmate · Build a claim", "about 25 minutes"),
      P("PART A · CHOOSE THE WORDS THAT MAKE THE SENTENCE CORRECT", ih2)]
ed = [("In Mexico, families ______ from house to house during Las Posadas.", ["walk", "walks", "walking", "is walk"]),
      ("Last year, my class ______ paper lanterns.", ["make", "made", "making", "are made"]),
      ("In Ukraine, the family waits ______ the first star appears.", ["but", "until", "or", "so"]),
      ("Which sentence is written correctly?", ["There is twelve dishes on the table.", "There are twelve dishes on the table.", "There are twelve dish on the table.", "They is twelve dishes on the table."])]
rows = []
for i, (stem, os_) in enumerate(ed):
    rows.append([P(f"<b>{i + 1}.</b>&nbsp; {stem}", S("eq", "In-S", 10.2, 13.4, black)),
                 P(("&nbsp;&nbsp; " if i < 3 else "<br/>").join(f"<font name='In-B'>{chr(65 + j)}</font>&nbsp;{o}" for j, o in enumerate(os_)), S("eo", "In-R", 10, 13.6, black))])
t = Table(rows, colWidths=[270, CW - 270]); t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -2), .4, GRULE), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4), ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
F += [t, P("PART B · REPLY TO A CLASSMATE", ih2),
      box([P("<b>From:</b> Linh &nbsp;&nbsp; <b>Subject:</b> Our “December Around the World” display", S("em", "In-R", 9.6, 13, black)),
           P("Hi! I'm finishing the class display. Which tradition did you find most interesting? What happens in it? How is it similar to, or different from, something your family does? Thanks! — Linh", S("em2", "Fr-R", 11, 15, black))], pad=6),
      Spacer(1, 4), P("Write a reply to Linh. Answer <b>all three</b> of her questions. Write at least five sentences.", dirs), Lines(5, 19),
      P("PART C · BUILD A CLAIM", ih2),
      P("<b>Question:</b> Should schools teach about traditions from many countries?", S("cq", "In-R", 10.6, 14, black, spaceAfter=3)),
      P("<b>Note 1:</b> Learning about classmates' traditions can help students understand one another. &nbsp; <b>Note 2:</b> Class time is limited, and there is a lot to learn before the spring tests.", S("cn", "In-R", 9.8, 13.2, black, spaceAfter=4)),
      P("Write a paragraph. State your claim, give one reason, support it with one of the notes or your own experience, and end with a closing sentence.", dirs),
      P("<i>You may begin:</i> &nbsp;I believe schools (should / should not) ______ because ______. For example, ______. That is why ______.", S("fr", "In-R", 9.6, 13, GREY, spaceAfter=3)),
      Lines(5, 19), PageBreak(),

      Band("Speaking", "Compare pictures · A visual and a claim", "about 15 minutes · work with a partner"),
      P("PART A · COMPARE PICTURES", ih2),
      P("Look at Lantern A and Lantern B. Tell your partner what is <b>the same</b> and what is <b>different</b>. Speak for 45 seconds. Name at least four differences.", dirs)]
pics = Table([[Lantern("A"), Lantern("B")]], colWidths=[CW / 2, CW / 2]); pics.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("ALIGN", (1, 0), (1, 0), "RIGHT")]))
F += [pics, Spacer(1, 5),
      P("<i>You may say:</i> &nbsp;Both lanterns have ______. &nbsp;Lantern A has ______, but Lantern B has ______. &nbsp;Another difference is ______. &nbsp;Lantern A ______, while Lantern B ______.", S("fr2", "In-R", 9.8, 13.6, GREY, spaceAfter=2)),
      P("PART B · A VISUAL AND A CLAIM", ih2),
      P("Study the timeline. Then read the two claims. For each claim, tell your partner whether the timeline <b>supports</b> it or <b>does not support</b> it. Use dates from the timeline.", dirs),
      Timeline(CW),
      cols([P("<b>Ana says:</b> “Las Posadas lasts longer than any other celebration on the timeline.”", S("cl", "Fr-R", 11, 15, black)), P("<b>Ben says:</b> “All of these celebrations happen in December.”", S("cl2", "Fr-R", 11, 15, black))], [CW / 2, CW / 2], gap=14),
      Spacer(1, 4), P("<i>You may say:</i> The timeline (supports / does not support) the claim because ______ is on ______ and ______ is on ______.", S("fr3", "In-R", 9.6, 13.2, GREY)),
      P("PARTNER CHECK · CIRCLE ONE NUMBER IN EACH ROW", ih2)]
rub = [["My partner…", "Not yet", "Some", "Yes"], ["answered every part of the task", "1", "2", "3"], ["used details from the pictures or dates from the timeline", "1", "2", "3"], ["spoke in complete sentences and was easy to understand", "1", "2", "3"]]
t = Table([[P(c_, S("rb2", "In-B" if i == 0 else "In-R", 9.4, 12, black)) for c_ in r] for i, r in enumerate(rub)], colWidths=[CW - 180, 60, 60, 60])
t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), .5, GRULE), ("BACKGROUND", (0, 0), (-1, 0), TINT), ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
F += [t, PageBreak(),

      Band("Teacher key", "Answers · scoring · listening scripts", "insert pages 6–7"),
      P("READING · INSERT PAGES 1–2", keyH),
      P("<b>1</b> B &nbsp;·&nbsp; <b>2</b> A &nbsp;·&nbsp; <b>3</b> C &nbsp;·&nbsp; <b>4</b> B &nbsp;·&nbsp; <b>5</b> C &nbsp;·&nbsp; <b>6</b> A and C (1 point each) &nbsp;·&nbsp; <b>7</b> A", keyS),
      P("<b>8</b> (2 points) A full answer says that a book is useful, not only enjoyable, <i>and</i> connects that to a detail: winter nights in Iceland are very long, or people read late into the night on December 24. "
        "1 point for either idea alone. Sample: “A story is practical because the nights are very long, so people need something to do indoors.”", keyS),
      P("<b>Reading total: 10 points.</b> Language focus: cause (<i>because, so</i>), contrast (<i>however, but</i>), and a word used in a new way (<i>flood</i>).", keyS),
      P("LISTENING · INSERT PAGE 3", keyH),
      P("<b>1</b> B &nbsp;·&nbsp; <b>2</b> C &nbsp;·&nbsp; <b>3</b> B &nbsp;·&nbsp; <b>4</b> A &nbsp;·&nbsp; <b>5</b> B &nbsp;·&nbsp; <b>6</b> C &nbsp;·&nbsp; <b>7</b> A &nbsp;·&nbsp; <b>8</b> C &nbsp;·&nbsp; <b>9</b> C &nbsp;·&nbsp; <b>10</b> A &nbsp;&nbsp; <b>Listening total: 10 points.</b>", keyS),
      P("Read each script twice at a natural pace, with a short pause between readings. Give students a moment to read the questions first. For Recording 2, change your voice or ask a student to read one part.", keyS),
      P("Script 1 · School announcement", S("sh1", "In-B", 9.4, 12.4, black, spaceBefore=4, spaceAfter=2)),
      P("Good afternoon, students. The International Club invites you to Winter Around the World Night on Thursday, December 10, from 6:00 to 7:30 in the cafeteria. "
        "You may bring a dish or a decoration from a tradition your family keeps at this time of year. Any tradition is welcome. To take part, sign up with Ms. Okafor in room 114 by Monday. "
        "Families are invited, and Spanish interpreters will be there to help. We hope to see you.", script),
      P("Script 2 · Conversation", S("sh2", "In-B", 9.4, 12.4, black, spaceBefore=4, spaceAfter=2)),
      P("<b>Mateo:</b> Linh, what should we put on our poster for the class display?<br/>"
        "<b>Linh:</b> You could write about Las Posadas. Your family does that, right?<br/>"
        "<b>Mateo:</b> Every year. Nine nights, and my little cousins always break the piñata. What about your family?<br/>"
        "<b>Linh:</b> We don't do much at home. But in Ho Chi Minh City, everybody goes downtown on the night of December 24 to see the lights and take pictures. The streets are completely full.<br/>"
        "<b>Mateo:</b> So both of our families go out at night, and there are lights in both places.<br/>"
        "<b>Linh:</b> That's true. Candles in your neighborhood, and electric lights in my city.<br/>"
        "<b>Mateo:</b> Then let's build the whole poster around light. Your photos on one side, my family's candles on the other.<br/>"
        "<b>Linh:</b> I like that. I'll bring the photos tomorrow.", script),
      P("Script 3 · A social studies teacher explains", S("sh3", "In-B", 9.4, 12.4, black, spaceBefore=4, spaceAfter=2)),
      P("Here is a question students ask every year: why do people in Ethiopia celebrate Christmas on January 7? The answer is the calendar. Most of the world uses the same calendar, with twelve months. "
        "Ethiopia keeps its own. The Ethiopian calendar has thirteen months: twelve months of thirty days each, and one very short month at the end of the year. Because the two calendars count the days differently, "
        "the holiday falls on the day we call January 7. In Ethiopia it is called Genna. Many people dress in white clothing and gather very early in the morning, before the sun comes up. "
        "Later in the day, some people play a game with sticks and a ball. It looks like field hockey, and it is also called genna. So the date is different, but the idea is the same: people gather, they dress in a special way, and they celebrate together.", script),
      PageBreak(),
      Band("Teacher key", "Writing · speaking · using the scores", "continued"),
      P("WRITING · INSERT PAGE 4", keyH),
      P("<b>Part A:</b> 1 A (walk) &nbsp;·&nbsp; 2 B (made) &nbsp;·&nbsp; 3 B (until) &nbsp;·&nbsp; 4 B. &nbsp; 1 point each.", keyS),
      P("<b>Part B, reply to a classmate (0–3).</b> 3: answers all three questions (which tradition, what happens, how it compares) in connected sentences; errors do not block meaning. "
        "2: answers two questions, or all three in very short or list-like sentences. 1: on topic, but only one question is answered or meaning is often unclear. 0: blank, copied, or off topic. "
        "A student may compare the tradition with any family custom at any time of year.", keyS),
      P("<b>Part C, build a claim (0–3).</b> 3: clear claim, a reason, support from a note or experience, and a closing sentence. 2: claim and reason, but support or closing is missing. "
        "1: an opinion with no reason, or a reason with no clear claim. 0: blank, copied, or off topic. Either side of the question can earn full credit.", keyS),
      P("<b>Writing total: 10 points.</b> Sample claim: “I believe schools should teach about traditions from many countries because it helps students understand each other. For example, I did not know why my classmate "
        "celebrates in January until we read about it. That is why a short lesson is worth the time.”", keyS),
      P("SPEAKING · INSERT PAGE 5", keyH),
      P("<b>Part A, differences:</b> A has five points, B has six · A has a ring around the star, B has none · A's star is shaded, B's is white · the centre circle is dark in A and white in B · "
        "A has two tassels, B has three · B has a bead on the string · A has small stars around it. <b>The same:</b> both are star lanterns that hang from a string and have tassels.", keyS),
      P("<b>Part B:</b> Ana's claim is <b>supported</b>: Las Posadas runs from December 16 to 24, nine nights, and every other celebration on the timeline is a single day. "
        "Ben's claim is <b>not supported</b>: Three Kings Day is on January 6 and Genna is on January 7.", keyS),
      P("<b>Scoring (0–3 for each part).</b> 3: completes the task with relevant detail in connected sentences; easy to understand. 2: completes most of the task; some short or halting answers. "
        "1: a few words or phrases on topic. 0: no response, or not in English. Listen to four or five students each session; the partner check covers the rest.", keyS),
      P("USING THE SCORES", keyH),
      P("These tasks follow ELPA21 task types, but the points are classroom points, not ELPA21 scale scores or proficiency levels. Use them to plan January:", keyS)]
use = [["If the weak spot is…", "Try this in January", "On the hub"], ["Reading 6, 7 or 8 (evidence, word meaning)", "Underline the sentence that proves each answer before choosing.", "Storm Reading Sets"],
       ["Listening 7–10 (academic talk)", "Two-column notes: term on the left, meaning on the right.", "Storm Listening Sets"], ["Writing B or C below 2", "Number the parts of the task, then number the answers to match.", "Storm Writing Sets · Sentence-Frame Bank"],
       ["Speaking: short answers", "Thirty seconds of talk with a frame before any written answer.", "Storm Speaking Sets"]]
t = Table([[P(c_, S("u", "In-B" if i == 0 else "In-R", 9, 12, black)) for c_ in r] for i, r in enumerate(use)], colWidths=[156, CW - 156 - 140, 140])
t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), .5, GRULE), ("BACKGROUND", (0, 0), (-1, 0), TINT), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
F += [t, Spacer(1, 6),
      P("<b>Grades 6–8.</b> Read the directions aloud the first time and allow five more minutes for each reading part. <b>Four lanes.</b> Newcomer: Reading A and Listening Recording 1 only, with a partner who shares the home language. Emerging: all tasks, with the frames. "
        "Progressing: all tasks, frames covered. Challenge: after “The Book Flood,” write one question the passage does <i>not</i> answer and say where you would look for the answer.", keyS),
      P("Facts in the passages and scripts were written from general reference knowledge for classroom practice. The school, the students and the event in the listening scripts are invented.", ismall),
      PageBreak(),
      Band("Home", "Family interview · Entrevista familiar", "10 minutes at home · report back in class"),
      P("Ask an adult at home these six questions, in <b>any language</b>. Write short notes in any language. In class, you will report in English. Your family may talk about any celebration that matters to them.", dirs),
      P("Hazle estas seis preguntas a un adulto en casa, en <b>cualquier idioma</b>. Escribe notas breves en cualquier idioma. En clase, vas a contarlo en inglés. Tu familia puede hablar de cualquier celebración que sea importante para ustedes.", S("es", "Fr-I", 10.4, 14.2, GREY)), Spacer(1, 6)]
iv = [("What celebration is most important in our family?", "¿Cuál es la celebración más importante de nuestra familia?"), ("When is it, and how long does it last?", "¿Cuándo es y cuánto dura?"),
      ("What do we eat or make for it?", "¿Qué comemos o preparamos para esa celebración?"), ("How did you celebrate when you were my age?", "¿Cómo la celebrabas cuando tenías mi edad?"),
      ("Is there a song, a saying or a greeting that goes with it?", "¿Hay una canción, un dicho o un saludo que la acompañe?"), ("What do you want me to remember about it?", "¿Qué quieres que yo recuerde de ella?")]
rows = [[P(f"<b>{i + 1}.</b>&nbsp; {a}<br/><font name='Fr-I' color='#555555'>{b}</font>", S("iq", "In-R", 10.2, 14, black)), Lines(2, 19)] for i, (a, b) in enumerate(iv)]
t = Table(rows, colWidths=[258, CW - 258]); t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -1), .4, GRULE), ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7), ("LEFTPADDING", (0, 0), (0, -1), 0)]))
F += [t, Spacer(1, 8), P("REPORT BACK · SPEAK FOR 45 SECONDS", ih2),
      box([P("I interviewed my ______. &nbsp;The most important celebration in our family is ______. &nbsp;It happens ______ and lasts ______. &nbsp;We always ______. "
             "&nbsp;When (he / she / they) was my age, ______. &nbsp;Something I did not know before is ______.", S("rf", "Fr-R", 11.2, 16.6, black))], pad=9),
      Spacer(1, 8),
      P("<b>To the family:</b> This interview is practice for your student's English test in the spring. Your home language helps. Please answer in the language you know best.", S("fam", "In-R", 9.6, 13.2, black)),
      P("<b>A la familia:</b> Esta entrevista es práctica para el examen de inglés de su estudiante en la primavera. El idioma del hogar ayuda. Por favor, responda en el idioma que mejor domina.", S("fam2", "Fr-I", 10, 13.8, GREY, spaceBefore=3)),
      NextPageTemplate("ELA standards"), PageBreak()]

# ---------- p27 ELA standards, K-12 ----------
XW = [("Read a tour stop or a practice passage and prove each answer from the text", "Cite evidence from the text", "RI", "1", "13, 8, 3"),
      ("Name the main idea of “The Book Flood,” “The Star Lantern” or a stop", "Determine the main or central idea", "RI", "2", "11, 8"),
      ("Work out <i>flood</i>, <i>practical</i> and the taught words from context", "Determine word meanings", "RI · L", "4", "13, 8"),
      ("Listen to a read-aloud or the three recordings and answer", "Understand information presented orally", "SL", "2", "15, 10, 5"),
      ("Compare the lanterns; gallery and picture walks; partner talk", "Take part in collaborative conversations", "SL", "1", "11, 9"),
      ("Judge the timeline claims; show and tell; report the family interview", "Present with relevant details", "SL", "4", "14, 6, 4, 1"),
      ("Build a claim; “My favorite tradition is ___ because ___”", "Write opinion and argument", "W", "1", "2"),
      ("Reply to Linh; the tradition paragraph; “My lantern has ___”", "Write to inform and explain", "W", "2", "7"),
      ("Retell Las Posadas in order; put three events in order", "Sequence events with time words", "W", "3", "12, 3"),
      ("Editing items; trace and write a sentence; one feedback target a day", "Use standard English grammar", "L", "1", "12"),
      ("Interview an adult at home and report what you learned", "Take part in short research", "W", "7", "1")]
rows = [[P(h, S("xh", "In-B", 8.4, 10.8, white)) for h in ("In this edition", "ELA standard", "Strand", "Number", "Calendar days")]]
for a, b, st, n, d in XW:
    rows.append([P(a, S("xa", "In-R", 9, 12.2)), P(b, S("xb", "In-S", 9, 12.2, NAVY)), P(st, S("xc", "In-B", 9.4, 12.2, PINE)), P(n, S("xc2", "In-X", 11, 12.2, CRAN)), P(d, S("xd", "In-R", 9, 12.2, MUTED))])
t = Table(rows, colWidths=[214, 150, 50, 48, CW - 462])
t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), PINEDK), ("ROWBACKGROUNDS", (0, 1), (-1, -1), [PAPER, WASH]), ("LINEBELOW", (0, 1), (-1, -1), .4, RULE), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5), ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 5)]))
code = Table([[P(x, S("cd0", "In-B" if i == 0 else "In-R", 9, 12.2, white if i == 0 else INK, alignment=1)) for x in r] for i, r in enumerate([["The standard", "Kindergarten", "Grade 3", "Grade 7", "Grades 9–10", "Grades 11–12"], ["Cite evidence (RI, 1)", "RI.K.1", "RI.3.1", "RI.7.1", "RI.9-10.1", "RI.11-12.1"], ["Write opinion or argument (W, 1)", "W.K.1", "W.3.1", "W.7.1", "W.9-10.1", "W.11-12.1"]])], colWidths=[160] + [(CW - 160) / 5] * 5)
code.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), NAVY), ("BACKGROUND", (0, 1), (-1, -1), PAPER), ("GRID", (0, 0), (-1, -1), .5, RULE), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
F += [Title("For the lesson plan", "ELA standards,", "K to 12.", 30), Spacer(1, 4),
      P("Every activity in this edition is also English language arts. This page matches each one to the Mississippi College- and Career-Readiness Standards for ELA, so a classroom teacher can use the edition as core instruction and an EL teacher can show the alignment in a lesson plan.", S("xl", "Fr-R", 11.4, 15.8, INK, spaceAfter=7)),
      t, Spacer(1, 8),
      P("<b>How to read the code.</b> The strand and the number are the same in every grade; only the grade in the middle changes.", S("xr", "In-R", 9.6, 13.4, spaceAfter=4)), code, Spacer(1, 6),
      box([P("ENGLISH LANGUAGE PROFICIENCY STANDARDS", S("xk2", "In-X", 7.6, 10, GOLDINK, spaceAfter=4)),
           P("The same tasks practice ELP Standards 1, 2, 3, 4 and 8, the standards behind the ELPT. In a plan, pair one ELA standard with one language target, for example: <b>RI.7.1</b>, cite evidence from “The Book Flood”; "
             "language target: explain a cause with <i>because</i> and <i>so</i>. Read the full wording for your grade in the state document before you file a plan.", S("xp2", "In-R", 9.2, 12.8))], pad=8, bg=WASH, line=RULE),
      NextPageTemplate("ELA for every classroom"), PageBreak()]

# ---------- p28 ELA activities for the general education classroom ----------
ACT = [("Prove it", "Reading · RI, 1", "Grades 2–12", "Read one tour stop. Ask three questions that can only be answered from the text. Students underline the proving sentence before they answer.",
        "Read the stop aloud first. Let them point to the sentence, then say it."),
       ("The gist in ten words", "Reading · RI, 2", "Grades 3–12", "After reading, each pair writes the main idea in ten words or fewer. Post them; the class votes on the clearest and says why.",
        "Give a word bank of six words from the text. Accept a spoken gist."),
       ("One word, two jobs", "Language · L, 4 and 5", "Grades 3–12", "<i>Flood</i> usually means water. In “The Book Flood” it means something else. Students find two more everyday words that change meaning in school reading.",
        "Start with words English borrowed from their languages: <i>piñata, tamal, fiesta</i>. They are the experts."),
       ("Same and different", "Writing · W, 2", "Grades 2–12", "Compare two traditions, such as the parol and the fanal, in a Venn diagram, then write a paragraph with <i>both, but</i> and <i>while</i>.",
        "The diagram can be labeled drawings. Provide the frame: “Both ___, but ___.”"),
       ("The night the door opened", "Writing · W, 3", "Grades 3–12", "Write a short story about one night of a tradition from the tour, or a true story about a celebration in your own family. Use time words to keep the events in order.",
        "Plan it out loud, or in the home language, before writing. Three sentences is a story."),
       ("Bring it here", "Writing · W, 1", "Grades 4–12", "Which tradition from the tour should our town try? State a claim, give two reasons, and support each with a detail from the text.",
        "“I believe ___ because ___. For example, ___.” One reason is enough at first."),
       ("Why light?", "Speaking · SL, 1", "Grades 5–12", "A circle discussion: why do so many December traditions use lanterns, candles and fireworks? Students must build on the last speaker before adding a new idea.",
        "Post stems: “I agree with ___ because ___.” Let them rehearse one sentence with a partner first."),
       ("A ninth stop", "Research · W, 7 · SL, 4", "Grades 4–12", "Research a December tradition that is not in this edition, using two sources, and present it in two minutes with one picture.",
        "Interviewing a family member counts as a source. Presenting with a partner is allowed.")]
def act(title, strand, grades, text, el):
    return box([P(f"{strand.upper()} &nbsp;·&nbsp; {grades.upper()}", S("ak", "In-X", 6.8, 9, GOLDINK, spaceAfter=2)), P(title, S("at", "Fr-B", 13.4, 16, NAVY, spaceAfter=3)), P(text, S("ab", "In-R", 9, 12.4, INK, spaceAfter=4)),
                P("<font name='In-B' color='#2F5D50'>For your English learners:</font> " + el, S("ae", "In-R", 8.8, 12.2, INK))], pad=7, bg=PAPER, line=RULE, width=(CW - 12) / 2, lw=.6)
grid = Table([[act(*ACT[k]), act(*ACT[k + 1])] for k in range(0, 8, 2)], colWidths=[(CW - 12) / 2 + 12, (CW - 12) / 2])
grid.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
F += [Title("For the general education teacher", "ELA for every", "classroom.", 30), Spacer(1, 4),
      P("You do not need an EL class to use this edition. These eight activities are whole-class English language arts, built on the tour stops and practice passages. Each one names its standard and the one change that lets an English learner do the same work. The texts are the tour stops (pages 4–5), “The Star Lantern” (page 18) and “The Book Flood” (page 20).", S("al", "Fr-R", 11.2, 15.4, INK, spaceAfter=7)),
      grid,
      NextPageTemplate("Every subject"), PageBreak()]

# ---------- p29 every subject ----------
SUBJ = [("Math", NAVY, "Count the calendar", "Las Posadas runs December 16 to 24: how many nights? Ethiopia's calendar has twelve months of thirty days and one short month: how many days are left for it? Older grades: a piñata star has seven points, so what is the angle between them?", "nights, altogether, are left, divided by, each"),
        ("Science", PINE, "What makes a lantern glow?", "Test paper, foil, wax paper and cardboard with a flashlight. Sort them: light passes through, some light passes through, no light passes through. Which would you use for a parol, and why?", "transparent, translucent, opaque, because"),
        ("Social studies", CRAN, "Map the tour", "Find the eight places on a world map. Which is farthest north? Which is closest to us? Older grades: Sweden's December mornings are dark and the Philippines' are not. What does the map tell you about why?", "north of, south of, closer to, farther from"),
        ("Art", GOLDINK, "Design a lantern", "Fold and cut a paper star or a paper house. Plan the pattern first, so that both halves match. Display the lanterns in a window with a one-sentence label by each artist.", "symmetry, pattern, fold, cut, both sides"),
        ("Music", NAVY, "Clap the season", "Play one instrumental recording of a December song from two countries on the tour. Students clap the beat, then say which is faster and which instruments they hear.", "beat, faster, slower, I hear a ___"),
        ("Physical education", PINE, "Sticks and skates", "Genna is played with curved sticks and a ball, like field hockey. Run a stick-and-ball relay. Or teach the balance drills skaters use: glide, stop, turn.", "pass, stop, turn, to your left, your turn"),
        ("Career and technical", CRAN, "A hundred tamales", "A recipe makes twelve tamales. A family needs one hundred. How many batches, how much of each ingredient, and what does it cost? Culinary classes can cook the plan.", "batch, multiply, per, enough, we need"),
        ("Technology and business", GOLDINK, "Build the timeline", "Enter the dates from the timeline on page 23 into a spreadsheet or a slide. Sort them, then add one more celebration from your own family or town.", "sort, earliest, latest, add a row"),
        ("Library", NAVY, "A book flood", "In Iceland the favorite gift is a book. Hold a class book swap: each student recommends one book to one classmate, on a card that says why.", "I recommend ___ because ___"),
        ("World languages and homeroom", PINE, "The greeting wall", "Post the fourteen greetings from page 6. Students add one more from a language spoken at home or in the community, and teach the class to say it.", "How do you say ___? In ___, we say ___.")]
def subj(name, col, title, text, lang):
    t = Table([[[P(name.upper(), S("sj", "In-X", 7, 9.2, col, spaceAfter=1.5)), P(title, S("sjt", "Fr-B", 12.6, 15, NAVY, spaceAfter=3)), P(text, S("sjb", "In-R", 8.7, 11.9, INK, spaceAfter=3)),
                 P("<font name='In-B' color='#7A5F0E'>Language to teach:</font> <i>" + lang + "</i>", S("sjl", "In-R", 8.6, 11.6, INK))]]], colWidths=[(CW - 12) / 2])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), PAPER), ("BOX", (0, 0), (-1, -1), .6, RULE), ("LINEBEFORE", (0, 0), (0, 0), 4, col), ("LEFTPADDING", (0, 0), (-1, -1), 12), ("RIGHTPADDING", (0, 0), (-1, -1), 9), ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7)]))
    return t
grid = Table([[subj(*SUBJ[k]), subj(*SUBJ[k + 1])] for k in range(0, 10, 2)], colWidths=[(CW - 12) / 2 + 12, (CW - 12) / 2])
grid.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
F += [Title("For every teacher in the building", "Every", "subject.", 32), Spacer(1, 4),
      P("One activity for each subject area, built on the same eight traditions. Each takes a single class period or less, and each names the handful of words an English learner needs to take part.", S("sl", "Fr-R", 11.4, 15.6, INK, spaceAfter=7)),
      grid, NextPageTemplate("Every teacher"), PageBreak()]

# ---------- p30 every teacher: five moves ----------
MOVES = [("Show it before you say it", "A picture, an object or a gesture comes first; the word comes second.", "Hold up the coloring page of the fanal, then say “paper lantern.”"),
         ("Teach four words, not forty", "Choose the four words the lesson cannot work without. Post them with a picture and leave them up.", "Each tour stop lists its four under “Words to teach.”"),
         ("Give the start of the sentence", "A frame gets a student talking. The thinking is still theirs.", "“Both ___, but ___.” “I think ___ because ___.”"),
         ("Talk first, write second", "Thirty seconds with a partner, in any language, before pencils move.", "The calendar's Tuesday practices are all partner talk."),
         ("Wait five seconds", "After a question, count to five in your head. A student working in two languages needs the time.", "Use it on every question you ask this month.")]
rows = []
for i, (h, t_, ex) in enumerate(MOVES):
    rows.append([P(str(i + 1), S("mn", "Fr-X", 30, 32, CRAN)), [P(h, S("mh", "Fr-B", 13.6, 16.5, NAVY, spaceAfter=2)), P(t_, S("mb", "In-R", 9.6, 13.2))], [P("IN DECEMBER", S("mk", "In-X", 6.8, 9, GOLDINK, spaceAfter=2)), P(ex, S("me", "Fr-I", 10.6, 14, NAVY))]])
mv = Table(rows, colWidths=[42, CW - 42 - 196, 196])
mv.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BACKGROUND", (0, 0), (1, -1), PAPER), ("BACKGROUND", (2, 0), (2, -1), WASH), ("BOX", (0, 0), (-1, -1), .6, RULE), ("LINEBELOW", (0, 0), (-1, -2), .5, RULE),
                        ("TOPPADDING", (0, 0), (-1, -1), 9), ("BOTTOMPADDING", (0, 0), (-1, -1), 9), ("LEFTPADDING", (0, 0), (0, -1), 12), ("LEFTPADDING", (2, 0), (2, -1), 11), ("RIGHTPADDING", (0, 0), (-1, -1), 10)]))
half = (CW - 14) / 2
F += [Title("Any room, any subject", "Every teacher: five", "moves.", 32), Spacer(1, 4),
      P("You do not have to be a language teacher to teach a student who is learning English. These five moves cost no planning time, work in every subject from kindergarten to grade 12, and help every other student in the room too.", S("ml", "Fr-R", 11.4, 15.6, INK, spaceAfter=8)),
      mv, Spacer(1, 10),
      cols([box([P("IF YOU HAVE TEN MINUTES", S("mt", "In-X", 7.6, 10, GOLDINK, spaceAfter=4)),
                 P("Use any tour stop as a bell-ringer. Read it aloud once. Ask three questions that the text answers. Every student says or writes one sentence that starts “Something I did not know before is ___.”", S("mp", "In-R", 9.4, 13))], pad=9, bg=WASH, line=RULE, width=half),
            box([P("THREE THINGS TO STOP DOING", S("mt2", "In-X", 7.6, 10, CRAN, spaceAfter=4)),
                 *BL(["Speaking louder. Slow down the pauses instead.", "Calling on a new student with no warning. Tell them the question first.", "Taking off content points for grammar. Grade the idea; note the language."], S("mb2", "In-R", 9.2, 12.6, leftIndent=11, firstLineIndent=-11, spaceAfter=2))], pad=9, bg=PAPER, line=RULE, width=half)],
           [half + 14, half], gap=14),
      Spacer(1, 8),
      P("<b>Ask your EL teacher</b> for each student's proficiency level in listening, speaking, reading and writing. A student can be strong in one and new in another, and that tells you which of the five moves matters most.", S("ma", "In-R", 9.6, 13.4)),
      NextPageTemplate("State test prep"), PageBreak()]

# ---------- p31-34 state test prep: math, science, history, key ----------
sub = lambda t_: P(t_, S("tsub", "In-X", 9.4, 12.4, black, spaceBefore=6, spaceAfter=1, keepWithNext=1))
F += [Band("Math", "State test practice · grades 3–5, 6–8 and Algebra I", "about 10 minutes for each band"),
      P("Choose the best answer. Show your work in the margin.", dirs),
      sub("GRADES 3–5"),
      mc(1, "A family makes 12 tamales in each batch. They make 9 batches. How many tamales do they make?", ["21", "96", "108", "129"]),
      mc(2, "Las Posadas runs from December 16 through December 24. How many nights is that?", ["7", "8", "9", "10"]),
      mc(3, "One star lantern uses 7 bamboo sticks. How many sticks are needed for 6 lanterns?", ["13", "36", "42", "49"]),
      mc(4, "One pot of fruit punch uses 2½ cups of fruit. How many cups of fruit are needed for 3 pots?", ["5½", "6", "7½", "8½"]),
      sub("GRADES 6–8"),
      mc(5, "3 cups of corn flour make 12 tamales. At the same rate, how many cups make 100 tamales?", ["20", "25", "33", "36"]),
      mc(6, "A book costs $18.00. It is on sale for 25% off. What is the sale price?", ["$4.50", "$13.50", "$14.50", "$22.50"]),
      mc(7, "Skates cost $4 plus $2 an hour. Lena paid $14. Which equation and answer are correct?", ["4h + 2 = 14; 3 hours", "2h + 4 = 14; 5 hours", "2h + 4 = 14; 7 hours", "6h = 14; 2 hours"]),
      mc(8, "A piñata's 7 points are equally spaced around 360°. About how many degrees apart are they?", ["45°", "51°", "60°", "72°"]),
      sub("ALGEBRA I"),
      P("An art club has 20 paper lanterns and makes 15 more each day.", S("stim", "Fr-R", 11, 15, black, spaceBefore=3)),
      mc(9, "Which function gives the number of lanterns, <i>L</i>, after <i>d</i> days?", ["L(d) = 20d + 15", "L(d) = 15d + 20", "L(d) = 35d", "L(d) = 15(d + 20)"]),
      mc(10, "In that function, what does the number 15 represent?", ["the lanterns the club started with", "the lanterns made each day", "the number of days", "the total number of lanterns"]),
      mc(11, "What is the least number of days the club needs to have at least 200 lanterns?", ["9", "10", "12", "14"]),
      mc(12, "A winter festival sold 60 tickets for $390. Adult tickets cost $8 and student tickets cost $5. How many student tickets were sold?", ["20", "25", "30", "35"]),
      PageBreak(),
      Band("Science", "State test practice · grade 5, grade 8 and Biology", "choose the best answer · about 10 minutes for each band"),
      sub("GRADE 5"),
      mc(1, "Wax paper lets some light pass through, but you cannot see clearly through it. Wax paper is", ["transparent", "translucent", "opaque", "reflective"]),
      mc(2, "When the water in a pot of tamales boils, the liquid water changes into", ["a solid", "a gas", "a mixture", "a mineral"]),
      mc(3, "The noon sun is lower in December than in June. In December, a flagpole's noon shadow is", ["shorter", "longer", "the same length", "gone"]),
      mc(4, "Which tool best separates pieces of fruit from the liquid in fruit punch?", ["a magnet", "a strainer", "a thermometer", "a balance"]),
      sub("GRADE 8"),
      mc(5, "Why does the Northern Hemisphere have fewer hours of daylight in December?", ["Earth is farther from the sun.", "Earth's axis is tilted away from the sun.", "The sun gives off less light.", "The moon blocks some sunlight."]),
      mc(6, "A candle heats the air inside a lantern. The warm air rises and cooler air moves in. This is", ["conduction", "convection", "radiation", "insulation"]),
      mc(7, "Paper on a lantern looks red in white light because the paper", ["absorbs red light only", "reflects red light and absorbs other colors", "bends all light equally", "produces its own red light"]),
      mc(8, "Which of these is a chemical change?", ["wax melting", "paper being folded", "a candle wick burning", "sugar dissolving in water"]),
      sub("BIOLOGY"),
      mc(9, "Corn stores energy as starch. That energy was first captured from sunlight during", ["cellular respiration", "photosynthesis", "fermentation", "mitosis"]),
      mc(10, "Yeast makes bread dough rise by releasing carbon dioxide. This process is", ["photosynthesis", "fermentation", "osmosis", "transcription"]),
      mc(11, "A student tests whether candle color affects burn time. What is the independent variable?", ["the burn time", "the color of the candle", "the size of the room", "the length of the wick"]),
      mc(12, "Which structure in a plant cell captures light energy?", ["mitochondrion", "ribosome", "chloroplast", "nucleus"]),
      PageBreak(),
      Band("History", "State test practice · social studies skills and U.S. History", "about 20 minutes"),
      sub("GRADES 3–8 · READ A TIMELINE"),
      P("Use the timeline of winter celebrations on page 23 to answer questions 1–3.", dirs),
      mc(1, "Which celebration comes first on the timeline?", ["St. Lucia Day", "St. Nicholas Day", "Genna", "Las Posadas"]),
      mc(2, "How many days are there from December 13 to December 25?", ["10", "12", "13", "38"]),
      mc(3, "Which two celebrations on the timeline take place in January?", ["Las Posadas and Genna", "St. Lucia Day and Christmas Day", "Three Kings Day and Genna", "St. Nicholas Day and Three Kings Day"]),
      sub("U.S. HISTORY · TRADITIONS TRAVEL WITH PEOPLE"),
      P("Read the passage. Then answer questions 4–9.", dirs),
      box([P("Between 1892 and 1954, about twelve million immigrants entered the United States through Ellis Island in New York Harbor. Many came for jobs in the country's growing factories and cities. "
             "They brought the foods, songs and celebrations of their home countries and kept them in their new neighborhoods. Over time, many of those traditions became part of American life.", S("hp", "Fr-R", 11, 15.4, black))], pad=8),
      mc(4, "Which statement is best supported by the passage?", ["Most immigrants returned home within a year.", "Immigrants' traditions became part of American communities.", "Ellis Island was located on the West Coast.", "Immigration ended in 1892."]),
      mc(5, "According to the passage, why did many immigrants come to the United States?", ["to find jobs in factories and cities", "to buy farmland in the South", "to attend universities", "to serve in the military"]),
      mc(6, "Which law, passed in 1882, was the first to bar immigrants of one nationality from entering the United States?", ["the Homestead Act", "the Chinese Exclusion Act", "the Social Security Act", "the Civil Rights Act"]),
      mc(7, "The Immigration Act of 1924 limited immigration mainly by", ["closing Ellis Island", "setting quotas based on national origin", "requiring every immigrant to speak English", "ending immigration from Canada"]),
      mc(8, "The Immigration and Nationality Act of 1965 changed immigration policy mainly by", ["ending the national-origins quota system", "building new immigration stations", "stopping all immigration for ten years", "creating Ellis Island"]),
      mc(9, "Which of these events happened first?", ["Ellis Island opened", "the Chinese Exclusion Act", "the Immigration Act of 1924", "the Immigration and Nationality Act"]),
      PageBreak(),
      Band("Test prep key", "Answers · the language of the test", "for teachers of math, science and history"),
      P("MATH", keyH),
      P("<b>1</b> C (12 × 9 = 108) &nbsp;·&nbsp; <b>2</b> C (16 through 24 is 9 nights) &nbsp;·&nbsp; <b>3</b> C (7 × 6 = 42) &nbsp;·&nbsp; <b>4</b> C (2½ × 3 = 7½) &nbsp;·&nbsp; <b>5</b> B (3 ÷ 12 = ¼ cup each; ¼ × 100 = 25) &nbsp;·&nbsp; "
        "<b>6</b> B (25% of 18 is 4.50; 18 − 4.50 = 13.50) &nbsp;·&nbsp; <b>7</b> B (2h + 4 = 14, so h = 5) &nbsp;·&nbsp; <b>8</b> B (360 ÷ 7 ≈ 51.4) &nbsp;·&nbsp; <b>9</b> B &nbsp;·&nbsp; <b>10</b> B &nbsp;·&nbsp; "
        "<b>11</b> C (15d + 20 ≥ 200, so d ≥ 12) &nbsp;·&nbsp; <b>12</b> C (a + s = 60 and 8a + 5s = 390 give s = 30)", keyS),
      P("SCIENCE", keyH),
      P("<b>1</b> B &nbsp;·&nbsp; <b>2</b> B &nbsp;·&nbsp; <b>3</b> B &nbsp;·&nbsp; <b>4</b> B &nbsp;·&nbsp; <b>5</b> B &nbsp;·&nbsp; <b>6</b> B &nbsp;·&nbsp; <b>7</b> B &nbsp;·&nbsp; <b>8</b> C &nbsp;·&nbsp; <b>9</b> B &nbsp;·&nbsp; <b>10</b> B &nbsp;·&nbsp; <b>11</b> B &nbsp;·&nbsp; <b>12</b> C", keyS),
      P("HISTORY", keyH),
      P("<b>1</b> B (December 6) &nbsp;·&nbsp; <b>2</b> B (12 days) &nbsp;·&nbsp; <b>3</b> C &nbsp;·&nbsp; <b>4</b> B &nbsp;·&nbsp; <b>5</b> A &nbsp;·&nbsp; <b>6</b> B &nbsp;·&nbsp; <b>7</b> B &nbsp;·&nbsp; <b>8</b> A &nbsp;·&nbsp; <b>9</b> B (1882)", keyS),
      P("WHICH TEST THIS PRACTICES", keyH),
      P("Mississippi tests mathematics in grades 3–8 and Algebra I, science in grades 5 and 8 and Biology, and U.S. History in high school. These pages follow that pattern. "
        "They are original classroom items written for this edition. They are not released state items, and the scores are not state scores.", keyS),
      P("THE LANGUAGE OF THE TEST", keyH),
      P("English learners often know the content and lose the point to the wording of the question. Teach these ten phrases in every subject, and post them.", keyS)]
TL = [("which statement is best supported", "which one can you prove from the text or data"), ("most likely", "the one that probably happens; not certain, but the best choice"), ("according to the passage", "the answer is written in the text; go back and find it"),
      ("at the same rate", "the pattern does not change; use the same ratio"), ("at least", "that number or more"), ("about how many", "estimate; the answer may be rounded"),
      ("represents", "stands for; what the number or letter means"), ("independent variable", "the one thing the scientist changes on purpose"), ("compared with", "look at two things and find the difference"), ("happened first", "the earliest date; check each one")]
t = Table([[P(h, S("tlh", "In-B", 8.8, 11, black)) for h in ("On the test", "What it is asking")]] + [[P(a, S("tla", "In-S", 9.2, 12.2, black)), P(b, S("tlb", "In-R", 9.2, 12.2, black))] for a, b in TL], colWidths=[190, CW - 190])
t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), .5, GRULE), ("BACKGROUND", (0, 0), (-1, 0), TINT), ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5)]))
F += [t, Spacer(1, 8),
      P("<b>For English learners on any practice page.</b> Read the question aloud once. Let students underline what the question asks before they look at the choices. Allow a word-to-word bilingual dictionary if the student's language plan lists it. "
        "After scoring, ask one student to explain a wrong choice: saying why an answer is wrong is the best speaking practice a test can give.", keyS),
      NextPageTemplate("A note for the last day"), PageBreak()]

# ---------- a note for the last day ----------
note = ["It is the last Friday. The room is loud, somebody brought food, and half the class is already somewhere else in their heads. Before the bell, look at them once.",
        "In August, one of these students did not know how to ask for the bathroom. Today that student stood up and told the class what her grandmother cooks in December, and why.",
        "Nobody will hand you a certificate for that. The spring test will count some of it. The rest will show up years from now, in a job interview or a parent conference "
        "or a phone call made without help, and you will not be there to see it.",
        "It happened anyway. You were the adult who waited five seconds longer than was comfortable. You wrote down their exact words. You said their names correctly, or kept trying until you did.",
        "The world's December traditions have one thing in common. In the darkest weeks, people make a light, and they do not keep it to themselves.",
        "You have done that for fifteen days, and for all the days before them. Now go home. Read something that is not a lesson plan. Sleep.",
        "They will be back in January, a little taller, with new words they learned without you. Be ready for them."]
F += [Spacer(1, 20), P("FOR THE TEACHER, BEFORE THE BUILDING EMPTIES", S("nk", "In-X", 8.2, 11, GOLDINK, alignment=1, spaceAfter=10)),
      P("A note for the last day", S("nt", "Fr-X", 36, 40, NAVY, alignment=1, spaceAfter=22))]
nb = [P(note[0], S("n0", "Fr-R", 14, 21, INK, spaceAfter=11))] + [P(x, S("nn", "Fr-R", 12.2, 19, INK, spaceAfter=10)) for x in note[1:]] + [Spacer(1, 6), P("EL Publishing · December 2026", S("ns", "Fr-I", 11.5, 15, GOLDINK))]
tb = Table([[nb]], colWidths=[CW - 110]); tb.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, 0), 2.5, GOLD), ("TOPPADDING", (0, 0), (-1, -1), 20), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
tb.hAlign = "CENTER"
F += [tb, NextPageTemplate("back"), PageBreak(), Spacer(1, 1)]

doc.build(F)
print("wrote", OUT)
