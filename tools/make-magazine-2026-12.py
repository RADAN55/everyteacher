#!/usr/bin/env python3
"""Build el-magazine-2026-12.pdf — The Language of Home (December 2026).

Newsstand edition: full-bleed illustrated openers, cover lines, contents spread,
bylines and standfirsts, raised initials, pull quotes, multi-column body text,
section tabs on the page edge, and a house ad on the back cover.

Run from the repo root:  python3 tools/make-magazine-2026-12.py
All art is drawn in code (no stock photos), so the issue is fully original.
"""
import math, random, os, tempfile
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, Color, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import Paragraph, Frame, Spacer, Table, TableStyle, KeepTogether
from fontTools.ttLib import TTFont as FTFont
from fontTools.varLib import instancer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "el-magazine-2026-12.pdf")
W, H = letter

# ---------- fonts ----------
FD = tempfile.mkdtemp(prefix="mag12fonts")
def inst(src, name, **loc):
    f = FTFont(src); f.flavor = None
    axes = {a.axisTag: a.defaultValue for a in f["fvar"].axes}; axes.update(loc)
    p = os.path.join(FD, name + ".ttf")
    instancer.instantiateVariableFont(f, axes).save(p); return p
FR = os.path.join(ROOT, "tools/fonts/Fraunces.ttf"); IN = os.path.join(ROOT, "tools/fonts/Inter.ttf")
FRI = os.path.join(ROOT, "fonts/fraunces-italic.woff2")
pdfmetrics.registerFont(TTFont("Fr-X", inst(FR, "FrX", wght=800, opsz=144, SOFT=0, WONK=1)))
pdfmetrics.registerFont(TTFont("Fr-B", inst(FR, "FrB", wght=700, opsz=72, SOFT=0, WONK=1)))
pdfmetrics.registerFont(TTFont("Fr-S", inst(FR, "FrS", wght=600, opsz=36, SOFT=0, WONK=0)))
pdfmetrics.registerFont(TTFont("Fr-R", inst(FR, "FrR", wght=400, opsz=14, SOFT=0, WONK=0)))
pdfmetrics.registerFont(TTFont("Fr-I", inst(FRI, "FrI", wght=500, opsz=36)))
pdfmetrics.registerFont(TTFont("Fr-IX", inst(FRI, "FrIX", wght=700, opsz=144)))
pdfmetrics.registerFont(TTFont("In-R", inst(IN, "InR", wght=400)))
pdfmetrics.registerFont(TTFont("In-M", inst(IN, "InM", wght=500)))
pdfmetrics.registerFont(TTFont("In-S", inst(IN, "InS", wght=600)))
pdfmetrics.registerFont(TTFont("In-B", inst(IN, "InB", wght=700)))
pdfmetrics.registerFont(TTFont("In-X", inst(IN, "InX", wght=800)))
pdfmetrics.registerFontFamily("In-R", normal="In-R", bold="In-B", italic="Fr-I", boldItalic="In-B")
pdfmetrics.registerFontFamily("Fr-R", normal="Fr-R", bold="Fr-B", italic="Fr-I", boldItalic="Fr-B")

# ---------- palette ----------
NAVY = HexColor("#1E2761"); NAVYDK = HexColor("#141A44"); NIGHT = HexColor("#0B0F2C"); GOLD = HexColor("#C9A227"); GOLDLT = HexColor("#EBD9A0")
GOLDINK = HexColor("#7A5F0E"); MIST = HexColor("#F4F5FA"); INK = HexColor("#1F2330"); MUTED = HexColor("#5D6480")
RULE = HexColor("#DCDEE9"); RUST = HexColor("#B35A3C"); PINE = HexColor("#3E5F57")
SLATE = HexColor("#1F2F3F"); EMBER = HexColor("#E8A24A"); CREAM = HexColor("#FBF7EC"); PLUM = HexColor("#4A2E5C"); SKY2 = HexColor("#2E3F86")

M = 44; CW = W - 2 * M; GUT = 14
C3 = (CW - 2 * GUT) / 3; C2 = (CW - GUT) / 2

# ---------- styles ----------
def S(name, font, size, lead, color=INK, **kw):
    return ParagraphStyle(name, fontName=font, fontSize=size, leading=lead, textColor=color, **kw)
body = S("body", "In-R", 9.3, 12.9, INK, spaceAfter=5)
bodyS = S("bodyS", "In-R", 8.7, 11.8, MUTED, spaceAfter=4)
small = S("small", "In-R", 7.8, 10.4, MUTED)
h2 = S("h2", "In-X", 8.2, 11, NAVY, spaceBefore=6, spaceAfter=3, keepWithNext=1)
h2r = S("h2r", "In-X", 8.2, 11, RUST, spaceBefore=6, spaceAfter=3, keepWithNext=1)
h2p = S("h2p", "In-X", 8.2, 11, PINE, spaceBefore=6, spaceAfter=3, keepWithNext=1)
num = S("num", "In-R", 9.3, 12.9, INK, leftIndent=13, firstLineIndent=-13, spaceAfter=2)
bul = S("bul", "In-R", 9.3, 12.9, INK, leftIndent=10, firstLineIndent=-10, spaceAfter=2)
wbody = S("wbody", "In-R", 9, 12.4, white, spaceAfter=4)
std = S("std", "Fr-R", 12.5, 17, INK)
wstd = S("wstd", "Fr-R", 12.5, 17, GOLDLT)
story = S("story", "In-R", 10, 14.2, INK, spaceAfter=5)

def P(t, st=body): return Paragraph(t, st)
def NL(items, st=num): return [Paragraph(f"<b>{i+1}.</b> {t}", st) for i, t in enumerate(items)]
def BL(items, st=bul): return [Paragraph("•&nbsp; " + t, st) for t in items]
def cap(t, st=body):
    """Raised initial, magazine style. Works on plain text or text starting with a <b>…</b> tag."""
    st2 = ParagraphStyle(st.name + "cap", parent=st, spaceAfter=st.spaceAfter + 9)
    if t.startswith("<b>"):
        end = t.index("</b>") + 4; rest = t[end:].replace("&nbsp;", " ").lstrip()
        return Paragraph(t[:end] + f'&nbsp; <font name="Fr-X" size="21" color="#B35A3C">{rest[0]}</font>{rest[1:]}', st2)
    return Paragraph(f'<font name="Fr-X" size="21" color="#B35A3C">{t[0]}</font>{t[1:]}', st2)

# ---------- drawing primitives ----------
PAGE_MIN = [H]; LAST_ENDS = []
def note(y):
    if 40 < y: PAGE_MIN[0] = min(PAGE_MIN[0], y)
def rect(c, x, y, w, h, fill, stroke=None, r=0, sw=.6):
    note(y); c.saveState(); c.setFillColor(fill)
    if stroke: c.setStrokeColor(stroke); c.setLineWidth(sw)
    if r: c.roundRect(x, y, w, h, r, fill=1, stroke=1 if stroke else 0)
    else: c.rect(x, y, w, h, fill=1, stroke=1 if stroke else 0)
    c.restoreState()
def text(c, x, y, s, font="In-R", size=9, color=INK, align="l", track=0):
    note(y); c.saveState()
    w = c.stringWidth(s, font, size) + track * max(len(s) - 1, 0)
    sx = x if align == "l" else (x - w if align == "r" else x - w / 2)
    t = c.beginText(sx, y); t.setFont(font, size); t.setFillColor(color)
    if track: t.setCharSpace(track)
    t.textOut(s); c.drawText(t); c.restoreState(); return w
def fade(c, x, y, w, h, rgb=(.04, .06, .17), a_bottom=.9, a_top=0.0, steps=28):
    """Vertical fade drawn as translucent strips (shadings ignore alpha)."""
    c.saveState()
    for i in range(steps):
        a = a_bottom + (a_top - a_bottom) * (i / (steps - 1))
        c.setFillColor(Color(*rgb, alpha=max(0, a))); c.rect(x, y + h * i / steps, w, h / steps + .5, fill=1, stroke=0)
    c.restoreState()
def hline(c, x1, x2, y, col=RULE, w=.6):
    c.saveState(); c.setStrokeColor(col); c.setLineWidth(w); c.line(x1, y, x2, y); c.restoreState()
def vline(c, x, y1, y2, col=RULE, w=.6):
    c.saveState(); c.setStrokeColor(col); c.setLineWidth(w); c.line(x, y1, x, y2); c.restoreState()
def flatten(flow):
    out = []
    for it in flow:
        if isinstance(it, list): out.extend(it)
        else: out.append(it)
    return out
def place(f, flow, c):
    """Like Frame.addFromList, but a heading never ends a frame on its own."""
    while flow:
        it = flow[0]
        if isinstance(it, Paragraph) and getattr(it.style, "keepWithNext", 0) and len(flow) > 1:
            avail = f._y - f._y1p; _, h1 = it.wrap(f._aW, avail); nxt = flow[1]
            try: _, h2_ = nxt.wrap(f._aW, avail)
            except Exception: h2_ = 24
            if h1 + min(h2_, 28) + it.getSpaceBefore() > avail: return
        if f.add(it, c, trySplit=0):
            flow.pop(0); continue
        avail = f._y - f._y1p
        try: S = it.split(f._aW, avail) if avail > 14 else []
        except Exception: S = []
        if S and f.add(S[0], c, trySplit=0):
            flow[0:1] = S[1:]
        return
def col(c, x, y, w, h, flow, pad=0):
    f = Frame(x, y, w, h, leftPadding=pad, rightPadding=pad, topPadding=0, bottomPadding=0, showBoundary=0)
    flow = flatten(flow); place(f, flow, c)
    if flow: print(f"  !! overflow p{c.getPageNumber()}: {len(flow)} left: {str(flow[0])[:60]!r}")
    note(f._y); return f._y
def columns(c, flow, n, top, bottom, x=M, w=CW, rules=True):
    flow = flatten(flow); cw = (w - (n - 1) * GUT) / n; ends = []
    for i in range(n):
        f = Frame(x + i * (cw + GUT), bottom, cw, top - bottom, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, showBoundary=0)
        place(f, flow, c); ends.append(f._y)
        if rules and i < n - 1 and flow: vline(c, x + (i + 1) * (cw + GUT) - GUT / 2, bottom, top, RULE)
    if flow: print(f"  !! overflow p{c.getPageNumber()} (columns): {len(flow)} left: {str(flow[0])[:60]!r}")
    e = min(ends); note(e); LAST_ENDS[:] = ends; return e

# ---------- scenes (all vector) ----------
def glow(c, cx, cy, r, col=(0.91, 0.64, 0.29), steps=6, a=.16):
    c.saveState()
    for i in range(steps, 0, -1):
        c.setFillColor(Color(*col, alpha=a / steps)); c.circle(cx, cy, r * i / steps * 1.6, fill=1, stroke=0)
    c.restoreState()
def sky(c, x, y, w, h, stars=90, seed=1, moon=False, cols=(NIGHT, NAVY, SKY2)):
    c.saveState(); p = c.beginPath(); p.rect(x, y, w, h); c.clipPath(p, stroke=0, fill=0)
    c.linearGradient(x, y + h, x, y, cols, (0, .55, 1), extend=True)
    rnd = random.Random(seed)
    for _ in range(stars):
        sx = x + rnd.random() * w; sy = y + h * (.3 + .7 * rnd.random()); r = rnd.choice([.5, .6, .8, 1.0, 1.3])
        c.setFillColor(Color(1, 1, 1, alpha=rnd.uniform(.3, .95))); c.circle(sx, sy, r, fill=1, stroke=0)
    if moon:
        mx, my = x + w * .78, y + h * .8; glow(c, mx, my, 26, (.9, .9, 1), a=.25)
        c.setFillColor(HexColor("#F3EFD8")); c.circle(mx, my, 13, fill=1, stroke=0)
        c.setFillColor(cols[1]); c.circle(mx + 7, my + 4, 11, fill=1, stroke=0)
    c.restoreState()
def trees(c, x, y, w, seed=3, col=NIGHT, scale=1.0):
    rnd = random.Random(seed); c.saveState(); c.setFillColor(col); cx = x
    while cx < x + w:
        r = rnd.uniform(14, 30) * scale; hgt = rnd.uniform(18, 40) * scale
        c.rect(cx - 2 * scale, y, 4 * scale, hgt, fill=1, stroke=0)
        for k in range(3):
            c.circle(cx + rnd.uniform(-r * .5, r * .5), y + hgt + rnd.uniform(0, r * .8), r * rnd.uniform(.6, 1), fill=1, stroke=0)
        cx += rnd.uniform(r * 1.6, r * 3.2)
    c.restoreState()
def housefront(c, x, y, w, h, col=NAVYDK, lit=True, door=True, porch=False, seed=0):
    rnd = random.Random(seed); c.saveState(); c.setFillColor(col); c.rect(x, y, w, h, fill=1, stroke=0)
    p = c.beginPath(); p.moveTo(x - 6, y + h); p.lineTo(x + w / 2, y + h + w * .36); p.lineTo(x + w + 6, y + h); p.close(); c.drawPath(p, fill=1, stroke=0)
    if rnd.random() < .5: c.rect(x + w * .7, y + h, w * .1, w * .2, fill=1, stroke=0)
    ww, wh = w * .2, h * .3
    for k in range(2):
        wx = x + w * (.14 + .52 * k); wy = y + h * .5
        if lit and rnd.random() < .85:
            c.setFillColor(rnd.choice([GOLD, EMBER, GOLDLT])); c.rect(wx, wy, ww, wh, fill=1, stroke=0)
            c.setFillColor(col); c.rect(wx + ww / 2 - .8, wy, 1.6, wh, fill=1, stroke=0); c.rect(wx, wy + wh / 2 - .8, ww, 1.6, fill=1, stroke=0)
        else:
            c.setFillColor(HexColor("#26306E")); c.rect(wx, wy, ww, wh, fill=1, stroke=0)
    if door:
        c.setFillColor(EMBER if lit else HexColor("#26306E")); c.roundRect(x + w * .42, y, w * .16, h * .36, 2, fill=1, stroke=0)
    if porch:
        c.setFillColor(col); c.rect(x - 4, y + h * .40, w + 8, 3, fill=1, stroke=0)
        for px in (x - 2, x + w + 1): c.rect(px, y, 2.2, h * .4, fill=1, stroke=0)
    c.restoreState()
def street(c, x, y, w, h, seed=5, moon=True, big=True):
    sky(c, x, y, w, h, stars=int(w / 5), seed=seed, moon=moon)
    gy = y + h * .18
    rnd = random.Random(seed + 1); cx = x - 10
    while cx < x + w:
        bw = rnd.uniform(26, 48); bh = rnd.uniform(22, 44); c.saveState(); c.setFillColor(HexColor("#171D4F")); c.rect(cx, gy + 8, bw, bh, fill=1, stroke=0)
        p = c.beginPath(); p.moveTo(cx, gy + 8 + bh); p.lineTo(cx + bw / 2, gy + 8 + bh + bw * .3); p.lineTo(cx + bw, gy + 8 + bh); p.close(); c.drawPath(p, fill=1, stroke=0); c.restoreState(); cx += bw + rnd.uniform(4, 14)
    trees(c, x, gy + 4, w, seed=seed + 2, col=HexColor("#10153A"), scale=.9)
    c.saveState(); p = c.beginPath(); p.rect(x, y, w, gy - y + 6); c.clipPath(p, stroke=0, fill=0)
    c.linearGradient(x, gy + 6, x, y, (HexColor("#10153A"), HexColor("#2A2A3A")), extend=True); c.restoreState()
    rnd = random.Random(seed + 3); cx = x + 10; i = 0
    while cx < x + w - 40:
        bw = rnd.uniform(70, 110) if big else rnd.uniform(50, 80); bh = bw * rnd.uniform(.55, .75)
        housefront(c, cx, gy, bw, bh, col=rnd.choice([NAVYDK, HexColor("#1A2254"), HexColor("#121842")]), porch=(i % 2 == 0), seed=seed + i)
        if i % 2 == 0:
            glow(c, cx + bw * .5, gy + bh * .42, 10, a=.22); c.saveState(); c.setFillColor(GOLDLT); c.circle(cx + bw * .5, gy + bh * .42, 2.6, fill=1, stroke=0); c.restoreState()
        c.saveState(); c.setFillColor(Color(.91, .64, .29, alpha=.10)); c.ellipse(cx + bw * .2, gy - 14, cx + bw * .8, gy + 4, fill=1, stroke=0); c.restoreState()
        cx += bw + rnd.uniform(14, 30); i += 1
def street_hi(c, x, y, w, h, seed=31):
    """Street scene for openers: houses sit above the title band."""
    c.saveState(); c.setFillColor(NIGHT); c.rect(x, y, w, h, fill=1, stroke=0); c.restoreState()
    street(c, x, y + 90, w, h - 90, seed=seed, moon=True, big=True)
def lantern(c, cx, cy, s=1.0, col=EMBER, glow_=True):
    c.saveState()
    if glow_: glow(c, cx, cy, 26 * s, a=.2)
    c.setStrokeColor(NAVYDK); c.setLineWidth(1.1 * s); c.line(cx, cy + 30 * s, cx, cy + 48 * s)
    c.setFillColor(NAVYDK); c.rect(cx - 8 * s, cy + 27 * s, 16 * s, 3.5 * s, fill=1, stroke=0); c.rect(cx - 8 * s, cy - 31 * s, 16 * s, 3.5 * s, fill=1, stroke=0)
    c.setFillColor(col); c.roundRect(cx - 17 * s, cy - 28 * s, 34 * s, 56 * s, 8 * s, fill=1, stroke=0)
    c.setFillColor(GOLDLT); c.roundRect(cx - 10 * s, cy - 20 * s, 20 * s, 40 * s, 5 * s, fill=1, stroke=0)
    c.setFillColor(white); c.ellipse(cx - 3.5 * s, cy - 10 * s, cx + 3.5 * s, cy + 8 * s, fill=1, stroke=0)
    c.restoreState()
def paper_lantern(c, cx, cy, r, col):
    c.saveState(); glow(c, cx, cy, r * 1.1, a=.18); c.setFillColor(col); c.ellipse(cx - r, cy - r * .8, cx + r, cy + r * .8, fill=1, stroke=0)
    c.setFillColor(Color(1, 1, 1, alpha=.22)); c.ellipse(cx - r * .55, cy - r * .5, cx + r * .55, cy + r * .5, fill=1, stroke=0)
    c.setFillColor(NAVYDK); c.rect(cx - r * .25, cy + r * .78, r * .5, 3, fill=1, stroke=0); c.rect(cx - r * .25, cy - r * .82, r * .5, 3, fill=1, stroke=0)
    c.setStrokeColor(Color(1, 1, 1, alpha=.25)); c.setLineWidth(.6)
    for k in (-.5, 0, .5): c.ellipse(cx - r * (1 - abs(k) * .3), cy - r * .8 + r * .8 * k, cx + r * (1 - abs(k) * .3), cy - r * .8 + r * .8 * k + 1, fill=0, stroke=1)
    c.restoreState()
def figure(c, cx, y, h=40, col=NIGHT, lantern_=True):
    c.saveState(); c.setFillColor(col); c.circle(cx, y + h * .86, h * .12, fill=1, stroke=0)
    p = c.beginPath(); p.moveTo(cx - h * .16, y); p.lineTo(cx - h * .13, y + h * .72); p.lineTo(cx + h * .13, y + h * .72); p.lineTo(cx + h * .16, y); p.close(); c.drawPath(p, fill=1, stroke=0)
    if lantern_:
        c.setStrokeColor(col); c.setLineWidth(1.4); c.line(cx + h * .12, y + h * .6, cx + h * .36, y + h * .5)
        glow(c, cx + h * .38, y + h * .36, h * .22, a=.3); c.setFillColor(EMBER); c.roundRect(cx + h * .3, y + h * .28, h * .16, h * .2, 2, fill=1, stroke=0)
    c.restoreState()
def bridge(c, x, y, w, h, seed=9):
    sky(c, x, y, w, h, stars=120, seed=seed, moon=True)
    wy = y + h * .34
    c.saveState(); p = c.beginPath(); p.rect(x, y, w, wy - y); c.clipPath(p, stroke=0, fill=0)
    c.linearGradient(x, wy, x, y, (HexColor("#1B2461"), HexColor("#0B0F2C")), extend=True); c.restoreState()
    c.saveState(); c.setFillColor(NIGHT); c.rect(x, wy + 26, w, 10, fill=1, stroke=0)
    n = 4; aw = w / n
    for i in range(n):
        ax = x + i * aw; p = c.beginPath(); p.moveTo(ax, wy - 10); p.lineTo(ax, wy + 26); p.lineTo(ax + aw, wy + 26); p.lineTo(ax + aw, wy - 10); p.lineTo(ax + aw - 8, wy - 10)
        p.arcTo(ax + 8, wy - 50, ax + aw - 8, wy + 20, startAng=0, extent=180); p.close(); c.setFillColor(NIGHT); c.drawPath(p, fill=1, stroke=0)
        lx = ax + aw / 2; c.rect(lx - 1, wy + 36, 2, 26, fill=1, stroke=0); glow(c, lx, wy + 66, 10, a=.3); c.setFillColor(GOLDLT); c.circle(lx, wy + 66, 3, fill=1, stroke=0)
        c.setFillColor(Color(.91, .64, .29, alpha=.18))
        for k in range(5): c.rect(lx - 6 + k, wy - 8 - k * 9, 12 - k * 1.5, 3, fill=1, stroke=0)
    c.restoreState()
    trees(c, x, wy + 36, w * .22, seed=seed + 4, col=NIGHT, scale=1.1); trees(c, x + w * .8, wy + 36, w * .2, seed=seed + 5, col=NIGHT, scale=1.1)
def hall_of_lanterns(c, x, y, w, h, seed=13):
    c.saveState(); p = c.beginPath(); p.rect(x, y, w, h); c.clipPath(p, stroke=0, fill=0)
    c.linearGradient(x, y + h, x, y, (NIGHT, NAVYDK, HexColor("#1E2761")), extend=True)
    rnd = random.Random(seed)
    for row in range(3):
        ry = y + h * (.82 - row * .22); c.setStrokeColor(Color(1, 1, 1, alpha=.25)); c.setLineWidth(.8)
        p = c.beginPath(); p.moveTo(x, ry + 10); p.curveTo(x + w * .3, ry - 6, x + w * .7, ry - 6, x + w, ry + 10); c.drawPath(p, stroke=1, fill=0)
        n = 7 + row
        for i in range(n):
            lx = x + w * (i + .5) / n; ly = ry - 14 - rnd.uniform(0, 8) + (abs(lx - x - w / 2) / (w / 2)) ** 2 * 10
            paper_lantern(c, lx, ly, rnd.uniform(9, 15) - row * 1.5, rnd.choice([EMBER, GOLD, RUST, GOLDLT, HexColor("#D96B4F")]))
    c.restoreState()
def key_scene(c, x, y, w, h):
    sky(c, x, y, w, h, stars=70, seed=23, cols=(NIGHT, NAVYDK, HexColor("#243070")))
    wx, wy, ww, wh = x + w * .06, y + h * .22, w * .26, h * .62
    c.saveState(); c.setFillColor(NIGHT); c.rect(wx - 8, wy - 8, ww + 16, wh + 16, fill=1, stroke=0)
    p = c.beginPath(); p.rect(wx, wy, ww, wh); c.clipPath(p, stroke=0, fill=0); c.linearGradient(wx, wy, wx, wy + wh, (EMBER, GOLDLT), extend=True); c.restoreState()
    c.saveState(); c.setFillColor(NIGHT); c.rect(wx + ww / 2 - 2, wy, 4, wh, fill=1, stroke=0); c.rect(wx, wy + wh * .55, ww, 4, fill=1, stroke=0)
    c.setFillColor(HexColor("#5A3A1E")); c.circle(wx + ww * .3, wy + wh * .36, 7, fill=1, stroke=0); c.rect(wx + ww * .2, wy + wh * .08, 20, 22, fill=1, stroke=0)
    c.setFillColor(HexColor("#3B2A14")); c.rect(wx + ww * .1, wy + wh * .06, ww * .8, 4, fill=1, stroke=0); c.restoreState()
    kx, ky = x + w * .78, y + h * .5; s = h / 150
    c.saveState(); c.setStrokeColor(PINE); c.setLineWidth(2.2 * s); p = c.beginPath(); p.moveTo(kx - 10 * s, ky + 52 * s); p.curveTo(kx - 60 * s, ky + 90 * s, kx + 40 * s, ky + 110 * s, kx + 4 * s, ky + 52 * s); c.drawPath(p, stroke=1, fill=0)
    glow(c, kx, ky, 40 * s, (.79, .64, .15), a=.22)
    c.setFillColor(GOLD); c.circle(kx, ky + 36 * s, 22 * s, fill=1, stroke=0); c.setFillColor(NAVYDK); c.circle(kx, ky + 36 * s, 10 * s, fill=1, stroke=0)
    c.setFillColor(GOLD); c.rect(kx - 6 * s, ky - 60 * s, 12 * s, 80 * s, fill=1, stroke=0)
    for dy, dw in [(-60, 16), (-46, 12), (-34, 18)]: c.rect(kx + 6 * s, ky + dy * s, dw * s, 7 * s, fill=1, stroke=0)
    c.setFillColor(GOLDLT); c.rect(kx - 6 * s, ky - 60 * s, 3 * s, 80 * s, fill=1, stroke=0); c.restoreState()
def kitchen(c, x, y, w, h):
    c.saveState(); p = c.beginPath(); p.rect(x, y, w, h); c.clipPath(p, stroke=0, fill=0)
    c.linearGradient(x, y + h, x, y, (HexColor("#3A2314"), HexColor("#6B3F22")), extend=True)
    sky(c, x + w * .58, y + h * .42, w * .3, h * .48, stars=30, seed=41, moon=True)
    c.setFillColor(HexColor("#2A180C")); c.rect(x + w * .58 - 6, y + h * .42 - 6, w * .3 + 12, 6, fill=1, stroke=0); c.rect(x + w * .58 - 6, y + h * .42, 6, h * .48 + 6, fill=1, stroke=0); c.rect(x + w * .88, y + h * .42, 6, h * .48 + 6, fill=1, stroke=0); c.rect(x + w * .58 + w * .15 - 2, y + h * .42, 4, h * .48, fill=1, stroke=0)
    c.setFillColor(HexColor("#8A5A34")); c.rect(x, y, w, h * .36, fill=1, stroke=0); c.setFillColor(HexColor("#A56D3E")); c.rect(x, y + h * .34, w, 6, fill=1, stroke=0)
    px, py = x + w * .3, y + h * .38; glow(c, px, py + 30, 30, a=.1)
    c.setFillColor(HexColor("#2B2B33")); c.roundRect(px - 48, py, 96, 54, 10, fill=1, stroke=0); c.setFillColor(HexColor("#3A3A44")); c.rect(px - 52, py + 48, 104, 7, fill=1, stroke=0)
    c.setFillColor(HexColor("#5C3A1E")); c.ellipse(px - 44, py + 44, px + 44, py + 54, fill=1, stroke=0)
    c.setStrokeColor(HexColor("#D9B37A")); c.setLineWidth(3); c.line(px + 20, py + 50, px + 70, py + 120); c.setLineWidth(1.2)
    for k in range(-3, 4): c.line(px + 20 + k * 2, py + 52, px + 8 + k * 5, py + 30)
    for cx in (x + w * .62, x + w * .75):
        cy = y + h * .36; c.setFillColor(HexColor("#E7DCC8")); c.roundRect(cx - 14, cy, 28, 24, 4, fill=1, stroke=0); c.setStrokeColor(HexColor("#E7DCC8")); c.setLineWidth(3); c.ellipse(cx + 12, cy + 6, cx + 22, cy + 18, fill=0, stroke=1)
        c.setStrokeColor(Color(1, 1, 1, alpha=.35)); c.setLineWidth(1.2)
        for k in range(2):
            p = c.beginPath(); p.moveTo(cx - 6 + k * 10, cy + 28); p.curveTo(cx - 12 + k * 10, cy + 40, cx + k * 10, cy + 46, cx - 6 + k * 10, cy + 58); c.drawPath(p, stroke=1, fill=0)
    c.setFillColor(HexColor("#8E4B21"))
    for k in range(3): c.saveState(); c.translate(x + w * .5 + k * 9, y + h * .2); c.rotate(25); c.roundRect(-3, -22, 6, 44, 3, fill=1, stroke=0); c.restoreState()
    c.restoreState()
def wall_of_cards(c, x, y, w, h, seed=17):
    rect(c, x, y, w, h, HexColor("#2A2F5E")); rnd = random.Random(seed)
    cols_ = [NAVY, PINE, RUST, GOLD, PLUM, SLATE, EMBER]
    cw, ch = 54, 36; n = int(w // (cw + 10)); rows = int(h // (ch + 12))
    for r in range(rows):
        for k in range(n):
            cx = x + 12 + k * (cw + 10) + rnd.uniform(-3, 3); cy = y + h - 14 - (r + 1) * (ch + 12) + rnd.uniform(-2, 2)
            c.saveState(); c.translate(cx + cw / 2, cy + ch / 2); c.rotate(rnd.uniform(-4, 4)); c.setFillColor(Color(0, 0, 0, alpha=.12)); c.rect(-cw / 2 + 2, -ch / 2 - 2, cw, ch, fill=1, stroke=0)
            c.setFillColor(white); c.rect(-cw / 2, -ch / 2, cw, ch, fill=1, stroke=0); c.setFillColor(rnd.choice(cols_)); c.rect(-cw / 2, ch / 2 - 6, cw, 6, fill=1, stroke=0)
            c.setFillColor(HexColor("#B9B5C9"))
            for j in range(3): c.rect(-cw / 2 + 6, ch / 2 - 14 - j * 7, cw * rnd.uniform(.4, .8), 2.2, fill=1, stroke=0)
            c.setFillColor(GOLD); c.circle(cw / 2 - 7, -ch / 2 + 7, 3, fill=1, stroke=0); c.restoreState()
def sun_arc(c, x, y, w, h):
    rect(c, x, y, w, h, MIST, r=4); c.saveState(); p = c.beginPath(); p.rect(x, y, w, h); c.clipPath(p, stroke=0, fill=0)
    base = y + h * .3; c.setStrokeColor(RULE); c.setLineWidth(.8); c.line(x, base, x + w, base)
    for lat, colr, label in [(10.5, GOLD, "Caracas"), (31.7, NAVY, "Laurel")]:
        hrs = daylight_hours(lat); half = hrs / 24 * w * .92; top = h * .6 * (hrs / 12)
        c.setStrokeColor(colr); c.setLineWidth(2.2); p = c.beginPath(); p.moveTo(x + w / 2 - half, base); p.curveTo(x + w / 2 - half * .5, base + top * 1.3, x + w / 2 + half * .5, base + top * 1.3, x + w / 2 + half, base); c.drawPath(p, stroke=1, fill=0)
    c.setFillColor(GOLD); c.circle(x + w / 2, base + h * .6 * .9 * .9, 5, fill=1, stroke=0)
    text(c, x + 8, y + h * .12, "sunrise", "In-R", 6.5, MUTED); text(c, x + w - 8, y + h * .12, "sunset", "In-R", 6.5, MUTED, "r")
    c.restoreState()

# ---------- daylight ----------
def daylight_hours(lat_deg, decl_deg=-23.44):
    lat = math.radians(lat_deg); d = math.radians(decl_deg); z = math.radians(90.833)
    cosH = (math.cos(z) - math.sin(lat) * math.sin(d)) / (math.cos(lat) * math.cos(d))
    return 2 * math.degrees(math.acos(max(-1, min(1, cosH)))) / 15
CITIES = [("Laurel, Mississippi", 31.7), ("Guatemala City, Guatemala", 14.6), ("Tegucigalpa, Honduras", 14.1), ("San Salvador, El Salvador", 13.7), ("Mexico City, Mexico", 19.4), ("Port-au-Prince, Haiti", 18.5), ("Hanoi, Vietnam", 21.0), ("Caracas, Venezuela", 10.5)]
DATA = [(n, lat, int(round(daylight_hours(lat) * 60 / 5) * 5)) for n, lat in CITIES]

# ---------- page furniture ----------
SECTIONS = {"features": (RUST, "FEATURES"), "labs": (PINE, "THE LABS"), "community": (PLUM, "COMMUNITY"), "planner": (NAVY, "TEACHER DESK"), "front": (GOLDINK, "UP FRONT")}
def tab(c, page, section):
    colr, lab = SECTIONS[section]; right = page % 2 == 1
    x = W - 14 if right else 0
    c.saveState(); c.setFillColor(colr); c.rect(x, H - 250, 14, 150, fill=1, stroke=0)
    c.translate(x + 11, H - 175); c.rotate(90)
    tw_ = c.stringWidth(lab, "In-B", 6.6) + 1.6 * (len(lab) - 1)
    t = c.beginText(-tw_ / 2, 0); t.setCharSpace(1.6); t.setFont("In-B", 6.6); t.setFillColor(white); t.textOut(lab); c.drawText(t); c.restoreState()
def folio(c, page, section, dark=False):
    saved = PAGE_MIN[0]; fg = GOLDLT if dark else MUTED; strong = white if dark else NAVY
    right = page % 2 == 1
    hline(c, M, W - M, 30, GOLD if dark else RULE, .6)
    if right:
        text(c, M, 19, "EL PUBLISHING  ·  THE LANGUAGE OF HOME", "In-S", 6.4, fg, track=.9)
        text(c, W - M - 20, 19, "DECEMBER 2026", "In-S", 6.4, fg, "r", track=.9); text(c, W - M, 19, str(page), "In-X", 9.5, strong, "r")
    else:
        text(c, M, 19, str(page), "In-X", 9.5, strong); text(c, M + 20, 19, "DECEMBER 2026", "In-S", 6.4, fg, track=.9)
        text(c, W - M, 19, "EL PUBLISHING  ·  THE LANGUAGE OF HOME", "In-S", 6.4, fg, "r", track=.9)
    tab(c, page, section); PAGE_MIN[0] = saved
def runhead(c, section_label, kicker=None):
    text(c, M, H - 34, section_label.upper(), "In-B", 6.8, GOLDINK, track=1.6)
    if kicker: text(c, W - M, H - 34, kicker.upper(), "In-S", 6.8, MUTED, "r", track=1.2)
    hline(c, M, W - M, H - 40, RULE)
def display(c, x, y, lines, size=34, color=NAVY, font="Fr-B", lead=1.02):
    c.saveState(); c.setFillColor(color); c.setFont(font, size)
    for i, l in enumerate(lines): c.drawString(x - 1, y - i * size * lead, l)
    c.restoreState(); return y - (len(lines) - 1) * size * lead
def byline(c, x, y, who="By the EL Publishing desk", color=MUTED):
    text(c, x, y, who.upper(), "In-B", 6.8, color, track=1.4)
def standfirst(c, x, y, w, t, st=std):
    para = Paragraph(t, st); _, hh = para.wrap(w, 300); col(c, x, y - hh, w, hh, [para]); return y - hh
def pull(c, x, y, w, t, color=RUST, size=15):
    st = S("pq", "Fr-I", size, size * 1.22, color); para = Paragraph(t, st); _, hh = para.wrap(w, 300)
    hline(c, x, x + w, y, color, 1.4); col(c, x, y - 10 - hh, w, hh, [para]); hline(c, x, x + w, y - 18 - hh, color, .6); return y - 24 - hh
def box(c, x, y, w, h, title, flow, fill=MIST, tcol=NAVY, bar=None):
    rect(c, x, y, w, h, fill, r=3)
    if bar: rect(c, x, y, 4, h, bar)
    col(c, x + 11, y + 8, w - 22, h - 16, [P(title.upper(), S("bt", "In-X", 6.8, 9.6, tcol)), Spacer(1, 4)] + list(flow))
def dark_box(c, x, y, w, h, title, flow, fill=NAVY, tcol=GOLDLT):
    rect(c, x, y, w, h, fill, r=3)
    col(c, x + 11, y + 8, w - 22, h - 16, [P(title.upper(), S("dbt", "In-X", 6.8, 9.6, tcol)), Spacer(1, 4)] + list(flow))
def opener(c, scene, kicker, lines, standfirst_, size=40, h_=300, byline_=True):
    scene(c, 0, H - h_, W, h_)
    fade(c, 0, H - h_, W, h_ * .68, a_bottom=.94, a_top=0)
    text(c, M, H - 34, kicker.upper(), "In-B", 7, GOLD, track=1.8)
    sf = Paragraph(standfirst_, wstd); _, sh = sf.wrap(CW * .8, 300)
    base = H - h_ + 16 + (12 if byline_ else 0) + sh + 12
    ye = display(c, M, base + (len(lines) - 1) * size * 1.0, lines, size=size, color=white)
    col(c, M, base - 12 - sh, CW * .8, sh, [sf])
    if byline_: byline(c, M, H - h_ + 12, color=GOLDLT)
    PAGE_MIN[0] = H; return H - h_ - 16
def endpage(c, page, section, dark=False):
    folio(c, page, section, dark); c.showPage(); PAGE_MIN[0] = H

# =====================================================================
c = canvas.Canvas(OUT, pagesize=letter, pageCompression=1)
c.setTitle("The Language of Home · December 2026 · EL Publishing"); c.setAuthor("Richard A. Daniel, M.Ed. · EL Publishing")
c.setSubject("The December 2026 issue of the EL Publishing English Learner Magazine, grades 9–12")

# ---------------- 01 COVER ----------------
rect(c, 0, 0, W, H, NIGHT)
street(c, 0, 210, W, H - 210, seed=7, moon=True, big=True)
fade(c, 0, H - 260, W, 260, a_bottom=0, a_top=.78); fade(c, 0, 210, W, 110, a_bottom=.96, a_top=0)
lantern(c, W - 120, 470, 1.5)
text(c, M, H - 86, "EL PUBLISHING", "Fr-X", 54, white)
text(c, M + 2, H - 102, "THE ENGLISH LEARNER MAGAZINE", "In-B", 7.6, GOLD, track=3)
text(c, W - M, H - 102, "DECEMBER 2026  ·  NO. 4", "In-B", 7.6, GOLD, "r", track=2)
hline(c, M, W - M, H - 112, GOLD, .9)
cl = [("15 LESSONS", "for the three weeks before break"), ("THE SECOND KEY", "original fiction about a door and a word"), ("USED TO / NOW", "the grammar of change, in seven minutes"), ("DAYLIGHT", "real data from eight cities students call home")]
yy = H - 140
for a, b in cl:
    text(c, M, yy, a, "In-X", 10.5, GOLDLT, track=1); text(c, M, yy - 12, b, "In-R", 8.6, white); yy -= 36
c.saveState(); c.setFillColor(GOLD); c.circle(W - M - 44, H - 180, 44, fill=1, stroke=0); c.restoreState()
text(c, W - M - 44, H - 176, "FREE", "Fr-X", 21, NAVYDK, "c"); text(c, W - M - 44, H - 190, "TO READ, TEACH", "In-B", 5.6, NAVYDK, "c", track=.8); text(c, W - M - 44, H - 198, "& SHARE", "In-B", 5.6, NAVYDK, "c", track=.8)
display(c, M, 214, ["The language", "of"], size=60, color=white, lead=1.0)
c.saveState(); c.setFillColor(GOLD); c.setFont("Fr-IX", 60); c.drawString(M - 1 + c.stringWidth("of ", "Fr-B", 60), 214 - 60, "home."); c.restoreState()
col(c, M, 78, 340, 58, [P("Every student carries a first language. The winter issue shows how a classroom opens the door to it, builds on it, and sends students home with English they can use.", S("ctag", "Fr-R", 12.4, 16, GOLDLT))])
text(c, M, 58, "PLUS", "In-X", 7.6, GOLD, track=2); text(c, M + 32, 58, "The Window on Pine Street  ·  A family interview in English & Spanish  ·  The Home Language Wall", "In-M", 7.6, white)
bx, by = W - M - 112, 66; rect(c, bx, by, 112, 50, white)
rnd = random.Random(12); xx = bx + 8
while xx < bx + 104:
    bw = rnd.choice([1, 1, 1.5, 2, 3]); rect(c, xx, by + 14, bw, 30, NIGHT); xx += bw + rnd.choice([1, 1.5, 2])
text(c, bx + 56, by + 5, "RADAN55.GITHUB.IO/EVERYTEACHER", "In-M", 5.2, NIGHT, "c")
text(c, M, 34, "GRADES 9–12  ·  26 PAGES  ·  ISSUE NO. 4  ·  MANY VOICES · ONE STORM", "In-B", 7, GOLDLT, track=1.4)
c.showPage(); PAGE_MIN[0] = H

# ---------------- 02 CONTENTS ----------------
runhead(c, "Contents", "December 2026 · No. 4")
display(c, M, H - 92, ["Inside."], size=46, color=NAVY)
text(c, M + 150, H - 92, "Four features, six labs, two community pages and the teacher desk.", "Fr-R", 12, MUTED)
feat = [("04", "The home language is the bridge", "A three-move routine for any content lesson.", bridge), ("07", "The Window on Pine Street", "A family's first December became a whole street's tradition.", lambda c, x, y, w, h: street(c, x, y, w, h, seed=31, big=False)), ("13", "The Second Key", "Original fiction: a door, a decision, a word.", key_scene), ("17", "The Home Language Wall", "Student publishing with a real audience.", wall_of_cards)]
tw = (CW - 3 * 10) / 4; ty = H - 118
for i, (pg, t, d, scn) in enumerate(feat):
    tx = M + i * (tw + 10); c.saveState(); p = c.beginPath(); p.rect(tx, ty - 96, tw, 96); c.clipPath(p, stroke=0, fill=0); scn(c, tx, ty - 96, tw, 96); c.restoreState()
    rect(c, tx, ty - 96, 30, 18, GOLD); text(c, tx + 15, ty - 91, pg, "In-X", 9, NAVYDK, "c")
    col(c, tx, ty - 156, tw, 56, [P(t, S("ft", "Fr-B", 11, 12.5, NAVY, spaceAfter=2)), P(d, S("ftd", "In-R", 7.4, 9.6, MUTED))])
yy = ty - 180
def toclist(c, x, y, w, title, items):
    text(c, x, y, title, "In-X", 7, GOLDINK, track=1.6); hline(c, x, x + w, y - 6, GOLD, .8); ly = y - 24
    for pg, t, d in items:
        text(c, x, ly, pg, "In-X", 13, RUST); text(c, x + 40, ly + 1, t, "In-B", 9.2, NAVY)
        col(c, x + 40, ly - 26, w - 40, 24, [P(d, S("tocd", "In-R", 7.8, 10, MUTED))]); hline(c, x, x + w, ly - 16, RULE); ly -= 40
    return ly
feats = [("03", "From the editor", "Every language is a way home"), ("04", "Feature · The bridge", "Name it, compare it, carry it, with three supports"), ("06", "December with care", "Light, observances, and three questions first"), ("07", "Reading lab", "The Window on Pine Street + response"), ("09", "Voice studio", "Neighborhood Hour listening script + a 60-second talk"), ("11", "Language workshop", "Used to / now, time connectors, words that travel"), ("13", "Literary lens", "The Second Key + analysis")]
regs = [("15", "Writing workshop", "A how-to from your kitchen"), ("16", "Data", "Daylight on December 21 in eight cities"), ("17", "Community", "The Home Language Wall + a family interview"), ("19", "Teacher desk", "90-minute block + fifteen lessons"), ("21", "Check & rubric", "Can you explain what changed? + growth log"), ("23", "Answer keys", "Two pages, with the next teaching move"), ("25", "Sources · Back page", "What we read, and the five-day challenge")]
toclist(c, M, yy, C2, "FEATURES & LABS", feats); toclist(c, M + C2 + GUT, yy, C2, "REGULARS & TEACHER DESK", regs)
rect(c, M, 44, CW, 40, NAVY, r=3)
col(c, M + 12, 50, CW - 24, 30, [P("<b>Independent classroom edition.</b> Original passages, scripts, activities and art. Students answer in a notebook or on separate paper. Emerging and Progressing are planning labels, not fixed descriptions of ability. Not an official ELPA21 publication.", S("ice", "In-R", 7.8, 10.2, white))])
endpage(c, 2, "front")

# ---------------- 03 EDITOR ----------------
runhead(c, "From the editor", "Richard A. Daniel, M.Ed.")
display(c, M, H - 96, ["Every language", "is a way home."], size=36, color=NAVY)
sy = standfirst(c, M, H - 182, CW * .66, "December is the month students most want to talk about where they come from. This issue gives them the English to do it, and gives you a routine to build on what they already know.")
L = [cap("In November we wrote about belonging as something a classroom designs. This month we take the next step. A student who feels welcome still has to decide, every day, whether the language they grew up with is allowed in the room. Our answer is yes, on purpose, with structure."),
     P("Research on bilingual development has said for decades that skills transfer across languages: a student who can summarize, infer and argue in Spanish, Vietnamese or Haitian Creole is not starting from zero in English. What they need is a bridge. This issue's teaching feature builds one in three moves: <b>name it</b> in any language, <b>compare it</b> across languages, <b>carry it</b> into academic English."),
     P("The readings are original. <i>The Window on Pine Street</i> follows a family's first December in a new town. <i>The Second Key</i> is a short story about a student trusted with a door. The listening script is a radio-style interview. The family page is written in English and Spanish so the conversation can happen at the kitchen table."),
     P("December is short. Fifteen lessons fit between Thanksgiving and winter break, and pages 19–20 lay them out so you can teach the issue in order or pull a single lab."),
     P("Teach well, and go home on time."), Spacer(1, 6), P("<b>Richard A. Daniel, M.Ed.</b><br/>Editor, EL Publishing · ENL/EL Specialist, Laurel High School", bodyS)]
columns(c, L, 2, H - 244, 236, x=M, w=CW * .66 - GUT)
rx = M + CW * .66; rw = CW * .34
rect(c, rx, H - 244 - 180, rw, 180, NAVY, r=3); lantern(c, rx + rw / 2, H - 244 - 86, .9)
col(c, rx + 12, H - 244 - 172, rw - 24, 30, [P("“A first language is not a detour. It is the road.”", S("eq", "Fr-I", 11, 14, GOLDLT, alignment=TA_CENTER))])
box(c, rx, 236, rw, H - 244 - 190 - 236, "In this issue", BL(["One routine: name it, compare it, carry it.", "Two original readings, one listening script.", "A family interview in English and Spanish.", "A check, a rubric and the keys."], S("bulS", "In-R", 8.2, 11, INK, leftIndent=9, firstLineIndent=-9, spaceAfter=1)))
rect(c, M, 44, CW, 176, CREAM, r=3)
text(c, M + 14, 202, "THE MASTHEAD", "In-X", 7, GOLDINK, track=1.6)
mast = [("Editor & writer", "Richard A. Daniel, M.Ed."), ("Design", "EL Publishing · navy and gold · Fraunces and Inter"), ("Art", "Drawn in code for this issue; no stock photos, no real students or homes"), ("Readings", "The Window on Pine Street · The Second Key · Neighborhood Hour (all original)"), ("Published", "Monthly, free, at radan55.github.io/everyteacher"), ("Previous issues", "No. 3 The Language of Belonging (Nov) · No. 2 The Field Atlas (Oct) · No. 1 Every Teacher (Sept)"), ("Write to us", "richard.spanishteacher@gmail.com")]
ly = 186
for a, b in mast:
    text(c, M + 14, ly, a.upper(), "In-B", 6.6, NAVY, track=1); text(c, M + 110, ly, b, "In-R", 8.2, INK); ly -= 18
col(c, M + 14, 50, CW - 28, 24, [P("<b>How to use the supports.</b> Every lab shows Emerging and Progressing supports side by side, with an Extension for students who are ready. The labels describe the plan for the day, not the student.", S("hu", "In-R", 7.8, 10.2, MUTED))])
endpage(c, 3, "front")

# ---------------- 04 FEATURE: THE BRIDGE ----------------
yt = opener(c, bridge, "Teaching feature", ["The home language", "is the bridge."], "A practical routine for any content lesson: let students name an idea in the language they think in, compare how two languages say it, then carry the idea into academic English they can write and say.", size=38, h_=330)
bw = (CW - 20) / 3
for i, (lab, q, colr) in enumerate([("Name it", "What do we call this where I come from?", SLATE), ("Compare it", "How is it the same? How is it different?", PINE), ("Carry it", "How do I say it in school English?", RUST)]):
    bx = M + i * (bw + 10); rect(c, bx, yt - 48, bw, 44, colr, r=3)
    text(c, bx + 10, yt - 18, lab.upper(), "In-X", 8, white, track=1.2); col(c, bx + 10, yt - 46, bw - 20, 24, [P(q, S("mq", "In-R", 8.2, 10.6, white))])
F = [P("1. Make the first language visible", h2r), cap("Begin with the concept, not the English word. Show the image, the problem or the diagram, and ask: <i>What do you call this at home?</i> Students write or say it in any language. A bilingual dictionary, a partner or a phone is fair. The point is that every student starts with something they already own."),
     P("2. Compare on purpose", h2r), P("Put the home-language word next to the English word. Ask what students notice: a shared root (<i>analizar / analyze</i>), a different word order (<i>la casa blanca / the white house</i>), a sound that is new. Thirty seconds of comparison builds a habit of looking for patterns instead of guessing."),
     P("3. Carry it into school English", h2r), P("Give a frame that uses the English term in the way the discipline uses it. Students say it, then write it. <i>The data suggest ____ because ____.</i> The home language has done its job; the sentence that reaches the page is in English."),
     P("A classroom snapshot", h2r), P("A biology class is labeling the parts of a cell. The teacher shows the diagram and asks for home-language names first. Three students write <i>núcleo</i>, one writes <i>nhân</i>, one writes the English word and shrugs. The teacher puts <i>núcleo</i> and <i>nucleus</i> side by side and asks what the class notices. A student says both start the same. Another says the Vietnamese word is shorter. The teacher writes the frame: <i>The nucleus controls the cell because ____.</i> Every student says it to a partner before writing it. Total time: four minutes."),
     P("Watch the response, not just the room", h2r), P("The routine works when students use the comparison. If the home-language word never comes back in their English sentence, the step was decoration. Ask one student to explain the pattern they found; that is the evidence."),
     P("Try this tomorrow", h2r), P("Pick the one term your lesson cannot do without. Run the three moves on that term alone. Keep the frame on the board for the whole period and count how many students use it in their exit ticket.")]
e = columns(c, F, 3, yt - 62, 44); e3 = LAST_ENDS[2]
if e3 > 170: pull(c, M + 2 * (C3 + GUT), e3 - 24, C3, "“The home language has done its job; the sentence that reaches the page is in English.”", RUST, 13)
endpage(c, 4, "features")

# ---------------- 05 FEATURE: THREE SUPPORTS ----------------
runhead(c, "Teaching feature · 2 of 2", "The routine, differentiated")
display(c, M, H - 92, ["Same routine.", "Three supports."], size=34, color=NAVY)
sy = standfirst(c, M, H - 176, CW * .62, "Shared objective: explain a key term using a comparison between two languages and a complete sentence in academic English.")
pull(c, M + CW * .66, H - 92, CW * .34, "“Accept the comparison, supply the frame, and have them repeat it. The idea arrived first; the English arrives second.”", RUST, 13)
y = H - 230
def support(c, y, kicker, title, body_, frame, h_, colr):
    rect(c, M, y - h_, CW, h_, MIST, r=3); rect(c, M, y - h_, 5, h_, colr)
    col(c, M + 16, y - h_ + 8, CW * .58, h_ - 16, [P(kicker.upper(), S("sk", "In-X", 6.8, 9.6, colr)), P(title, S("st", "Fr-B", 14, 16.5, NAVY, spaceAfter=3)), P(body_, bodyS)])
    col(c, M + CW * .62, y - h_ + 14, CW * .36, h_ - 24, [P("THE FRAME", S("fk", "In-X", 6.6, 9, colr)), Spacer(1, 3), P(frame, S("fr", "Fr-I", 11, 14, colr))])
    return y - h_ - 10
y = support(c, y, "Emerging · more guidance", "Make the pattern visible", "Give the home-language word and the English word already paired on a card. Students circle what is the same and underline what is different, then read the frame aloud twice with a partner before writing it. Allow a drawing beside the sentence.", "“In ____ we say ____. In English we say ____. Both ____.”", 104, SLATE)
y = support(c, y, "Progressing · growing independence", "Find the pattern", "Students write the home-language term themselves, then find a second English word with the same root or a word that sounds similar but means something else (a false friend). They explain the connection in one sentence and use the term in a second, original sentence.", "“____ and ____ share the root ____, which means ____. In this lesson, ____ means ____.”", 104, PINE)
y = support(c, y, "Extension · greater precision", "Teach the pattern", "Students prepare a 60-second explanation of one term for a classmate who speaks a different home language, including a comparison, a common mistake and an example from the lesson. They record it or deliver it live.", "“A common mistake is ____, because in ____ the word ____. The precise meaning here is ____.”", 104, RUST)
box(c, M, 44, C2, y - 44, "Language for comparison · post these for the month", BL(["This word looks like ____, but it means ____.", "In my language the adjective comes ____ the noun.", "The ending ____ tells me it is a ____ (noun / verb)."]))
dark_box(c, M + C2 + GUT, 44, C2, y - 44, "Teacher check", [P("If a student explains the pattern in their home language but cannot yet say it in English, the thinking is there. Accept the comparison, supply the frame, and have them repeat it. Do not mark the idea wrong because the English arrived second.", wbody)])
endpage(c, 5, "features")

# ---------------- 06 DECEMBER WITH CARE ----------------
runhead(c, "December with care", "Observances")
display(c, M, H - 92, ["Light, without", "assumptions."], size=34, color=NAVY)
sy = standfirst(c, M, H - 176, CW * .62, "December holds many observances and many students who celebrate none of them. Use light as the shared thread, and ask three questions before any holiday activity.")
rect(c, M + CW * .66, H - 92 - 150, CW * .34, 160, NAVY, r=3); lantern(c, M + CW * .83, H - 140, .7)
col(c, M + CW * .66 + 10, H - 92 - 146, CW * .34 - 20, 60, [P("THE SHARED THREAD", S("sh", "In-X", 6.6, 9, GOLDLT)), P("Lamps, candles, bonfires, lanterns, the longest night. Light appears in winter traditions on every continent and in no religion in particular.", S("shb", "In-R", 7.8, 10.2, white))])
D = [P("Three questions first", h2)] + NL(["<b>Does the task assume a belief?</b> “Write about your Christmas tree” assumes a tree. “Describe a tradition your family keeps in winter, or one you would like to start” does not.", "<b>Can a student opt out without being noticed?</b> Offer two prompts of equal weight: a tradition, or a season. Both produce the same language.", "<b>Does the activity produce academic language?</b> A list of holiday words is vocabulary without a sentence. Every task in this issue ends in a comparison, an explanation or a claim."]) + [
     P("Two observances worth teaching", h2), P("<b>Human Rights Day, December 10.</b> The United Nations adopted the Universal Declaration of Human Rights on this date in 1948. Article 26 concerns education; Article 2 says rights belong to everyone regardless of language. Have students read one article in English and one in a home language, then compare a key word."),
     P("<b>International Migrants Day, December 18.</b> Established by the UN General Assembly in 2000. A fair task: students write a one-paragraph profile of a person who moved, real or fictional, using three time connectors from the Language workshop (page 11)."),
     P("A light inquiry · 20 minutes", h2), P("<b>Before:</b> show four images of light in winter (a candle, a lantern, a bonfire, a window). Students name each in any language. <b>During:</b> pairs choose one and answer: Who lights it? When? What does it mean to the people who light it? Source: a family member, a book or a reliable site. <b>After:</b> one sentence per pair on the wall: <i>In ____, people light ____ to ____.</i>")]
columns(c, D, 2, H - 250, 262, x=M, w=CW)
rect(c, M, 44, CW, 208, CREAM, r=3)
text(c, M + 14, 236, "DECEMBER LIGHT  ·  ONE LINE EACH  ·  VERIFY DATES LOCALLY; SEVERAL FOLLOW LUNAR CALENDARS", "In-X", 6.8, GOLDINK, track=1.2)
rows = [("Dec 4–12", "Hanukkah (2026 dates)", "An eight-night festival; one more candle is lit each evening."), ("Dec 10", "Human Rights Day", "Marks the 1948 Universal Declaration of Human Rights."), ("Dec 13", "St. Lucia's Day", "Candles and processions in Sweden and other Nordic countries."), ("Dec 16–24", "Las Posadas", "Nine nights of processions in Mexico and Central America, with candles and song."), ("Dec 18", "International Migrants Day", "A UN observance since 2000."), ("Dec 21", "Winter solstice", "The shortest day in the Northern Hemisphere; see the daylight data on page 16."), ("Dec 25", "Christmas", "Lights on houses, trees and streets across many countries."), ("Dec 26–Jan 1", "Kwanzaa", "Seven nights; a candle is lit for each principle."), ("Jan 1", "New Year's Day", "Fireworks and lanterns around the world; Lunar New Year falls later (Feb 6, 2027).")]
ry = 218
for d, n, s_ in rows:
    text(c, M + 14, ry, d, "In-B", 8, RUST); text(c, M + 84, ry, n, "In-S", 8.4, NAVY); text(c, M + 232, ry, s_, "In-R", 8.2, INK); hline(c, M + 14, W - M - 14, ry - 5, HexColor("#EADFC4")); ry -= 19
endpage(c, 6, "front")

# ---------------- 07 READING LAB: TEXT ----------------
yt = opener(c, street_hi, "Reading lab · Original informational narrative", ["The Window on", "Pine Street"], "How a family's first December in a new town became a tradition for a whole street.", size=40, h_=270)
text(c, M, yt - 10, "BEFORE YOU READ", "In-X", 6.8, GOLDINK, track=1.4)
col(c, M, yt - 56, CW, 42, [P("Numbers in brackets mark the sections. Read once for the story, then again to answer the questions on page 8. New words: <b>landlord, porch, neighbor, lantern, tradition, gathered, nervous, translate.</b> Reading goal: explain what changed on Pine Street and what caused the change, using details from the text.", bodyS)])
ST = [cap("<b>[1]</b>&nbsp; The Reyes family moved to Pine Street in October, when the trees were still green. By December the trees were bare and the house was cold in the mornings. Luis, who was fifteen, walked to school past eleven houses and did not know who lived in any of them.", story),
      P("<b>[2]</b>&nbsp; His mother, Carmen, had a plan. In the town where she grew up, December meant the <i>posadas</i>: nine nights when neighbors walked from house to house with candles, singing, asking for shelter, and being let in for food. “Here, nobody will know the song,” Luis said. “Then we will teach them,” she said.", story),
      P("<b>[3]</b>&nbsp; The first problem was the landlord. The lease said no open flames on the porch. Luis read the whole lease twice, then wrote an email in English asking whether battery lanterns were allowed. The landlord wrote back the same day: yes. Luis printed the email and put it on the refrigerator.", story),
      P("<b>[4]</b>&nbsp; The second problem was the neighbors. Carmen wrote an invitation in Spanish. Luis translated it, then changed it. His mother's version said, “We will arrive at your door and sing.” His version said, “We would like to walk to your house with lanterns on December 16, at six. You do not have to do anything. If you open the door, we will sing one song and move on.” He left copies in eleven mailboxes.", story),
      P("<b>[5]</b>&nbsp; On December 16, four doors opened. At the fifth house, a woman named Mrs. Patel stood on the porch with a plate of sweets and asked if she could walk with them. At the seventh, a man named Mr. Boyd said he did not know the song but he had a guitar. By the ninth house there were fourteen people on the sidewalk, and three of them were singing.", story),
      P("<b>[6]</b>&nbsp; The second year, Mr. Boyd printed the words in English and Spanish. Mrs. Patel added a stop at her house for a lamp-lighting from her own December tradition. A family from Vietnam, new that year, brought paper lanterns. Luis made a map.", story),
      P("<b>[7]</b>&nbsp; Pine Street now has a December walk every year. The flyer is in four languages. Nobody calls it a <i>posada</i> anymore; they call it the Pine Street Walk. Carmen says this is fine. “The name changed,” she says. “The door did not.”", story),
      Spacer(1, 4), P("<b>Quick glossary:</b> <i>posada</i> = shelter, lodging; <i>lease</i> = a rental agreement; <i>mailbox</i> = where letters are delivered; <i>flyer</i> = a one-page notice. Original text by EL Publishing; any resemblance to real streets or people is coincidental.", small)]
e = columns(c, ST, 2, yt - 66, 44)
if e > 150:
    sky(c, M, 44, CW, e - 60, stars=40, seed=33)
    for i in range(7): figure(c, M + 40 + i * 70, 50, h=42 + (i % 3) * 4, col=NIGHT)
    text(c, W - M - 12, e - 78, "“The name changed. The door did not.”", "Fr-I", 12, GOLDLT, "r")
endpage(c, 7, "labs")

# ---------------- 08 READING RESPONSE ----------------
runhead(c, "Reading lab · Response", "Pages 7–8")
display(c, M, H - 92, ["Notice. Explain. Prove."], size=32, color=NAVY)
sy = standfirst(c, M, H - 132, CW, "Use section numbers from page 7. Answer in a notebook or on separate paper. Explain your thinking to a partner before writing.")
A = [P("A / Build understanding", h2)] + NL(["What was Carmen's plan, and why did Luis doubt it?", "What did the lease say? Which section tells you?", "How did Luis solve the first problem? Quote the sentence that shows the solution.", "Which neighbors joined the walk the first year, and what did each one bring?", "Why does the text say the name changed but the door did not?"]) + [
     P("B / Follow the change", h2), P("Complete the chain with details from sections [1], [5] and [7]:", bodyS), P("<b>Beginning:</b> Luis knew ____ neighbors.<br/><b>First walk:</b> ____ doors opened.<br/><b>Now:</b> the flyer is in ____ languages.", S("ch", "In-R", 9.3, 13.4, INK, leftIndent=10, spaceAfter=4)),
     P("C / Read like a writer", h2)] + NL(["The author tells us Luis read the lease <i>twice</i>. What does this detail show about him?", "Why do you think the author ended with Carmen's words instead of Luis's?"]) + [
     P("D / Make an inference", h2)] + NL(["Luis changed his mother's invitation. Explain two changes he made and why each one might matter to a neighbor who does not know the tradition.", "Mrs. Patel added a stop from her own tradition. What does this suggest about how the walk changed over time?"]) + [
     P("E / Turn reading into action", h2), P("Choose one. Write 80–120 words.", bodyS), BL(["Write the email Luis sent to the landlord. Include a greeting, a clear question and a polite closing.", "Write the flyer for year three in English. Then add one line in a home language and label it."]),
     P("Language support", h2), P("<b>Start here:</b> “In section ____, the author says ____. This shows ____.”<br/><b>Build further:</b> “Luis changed ____ because ____. This matters because ____.”<br/><b>Stretch:</b> “Although the tradition came from ____, it became ____ when ____.”", S("ls", "In-R", 8.8, 12.4, INK))]
e = columns(c, A, 2, sy - 16, 150)
by = max(min(e - 14, H - 160), 150)
box(c, M, by - 100, C2, 100, "Check before you finish", [P("Circle the section number beside every answer. Underline one detail you used. If you wrote an opinion, point to the sentence in the text that supports it. Trade papers with a partner and read one answer aloud.", bodyS)], GOLDLT, GOLDINK)
dark_box(c, M + C2 + GUT, by - 100, C2, 100, "Name it · Compare it · Carry it", [P("Choose the word <b>neighbor</b>. Name it in your home language. Compare: does your word include people on the whole street, or only next door? Carry it: write one sentence about Pine Street using <i>neighbor</i> in the English sense.", S("ncb", "In-R", 8.6, 11.4, white))])
endpage(c, 8, "labs")

# ---------------- 09 VOICE STUDIO: LISTENING ----------------
yt = opener(c, hall_of_lanterns, "Voice studio · Listening", ["A tradition,", "told out loud."], "Teacher-read script in two voices. Read it twice; students may take notes during the second reading. Original content, not an official test item.", size=38, h_=270)
scr = [P("Teacher script · Neighborhood Hour", h2p),
       P("<b>HOST:</b> Welcome back to <i>Neighborhood Hour</i>. Today we are talking with Amara, a senior who started a December tradition at her school. Amara, what is it?"),
       P("<b>AMARA:</b> It's called the Lantern Hall. On the last Friday before break, students hang paper lanterns in the main hallway. Each lantern has one sentence on it about a tradition from their family, in English and in a home language."),
       P("<b>HOST:</b> How many lanterns did you have the first year?"), P("<b>AMARA:</b> Thirty-one. This year we have more than two hundred, in nineteen languages."),
       P("<b>HOST:</b> What was the hardest part?"), P("<b>AMARA:</b> Honestly, the rules. The fire marshal said no candles, which we expected. But he also said nothing could hang below seven feet. So we measured every lantern and moved the whole display up. We lost a week."),
       P("<b>HOST:</b> What do students write on the lanterns?"), P("<b>AMARA:</b> Anything true. One says, “My grandmother makes tamales on the 24th and we are not allowed to help.” One says, “We don't celebrate anything in December, so we watch movies for three days.” That one is my favorite."),
       P("<b>HOST:</b> Why?"), P("<b>AMARA:</b> Because it belongs there too. The point is not the holiday. The point is that everybody has a December."),
       P("<b>HOST:</b> Amara, thank you. The Lantern Hall opens Friday at three.")]
Q = [P("Listen 1 / Purpose", h2)] + NL(["What is the main purpose of this interview?", "Where and when does the Lantern Hall happen?", "What two things are written on each lantern?"]) + [P("Listen 2 / Details", h2)] + NL(["How many lanterns were there the first year? This year?", "What two rules did the fire marshal give?", "Which lantern is Amara's favorite, and why?"]) + [P("After listening / Reasoning", h2)] + NL(["Amara says, “Everybody has a December.” Explain what she means using one detail from the interview.", "The display lost a week. Was that a failure? Give a reason."]) + [P("A useful note grid", h2), P("<b>WHO:</b> ____ &nbsp; <b>WHAT:</b> ____<br/><b>NUMBERS:</b> ____ / ____<br/><b>RULES:</b> ____ / ____<br/><b>FAVORITE:</b> ____", S("ng", "In-R", 9, 13.4, INK))]
col(c, M, 44, C2 + 10, yt - 54, scr); e2 = col(c, M + C2 + 10 + GUT, 44, C2 - 10, yt - 54, Q); vline(c, M + C2 + 10 + GUT / 2, 44, yt - 10, RULE)
by = max(min(e2 - 14, yt - 60), 140)
dark_box(c, M + C2 + 10 + GUT, by - 92, C2 - 10, 92, "Language support", [P("Emerging: hear the script three times; answer 1–3 with a partner. Progressing: answer all; add one sentence beginning <i>According to Amara, ____.</i> Everyone: speakers pause after each turn so students can write.", S("lsb", "In-R", 8.4, 11, white))], PINE)
endpage(c, 9, "labs")

# ---------------- 10 VOICE STUDIO: SPEAKING ----------------
runhead(c, "Voice studio · Speaking", "Partner task")
display(c, M, H - 92, ["Sixty seconds.", "One tradition. Your voice."], size=30, color=NAVY)
sy = standfirst(c, M, H - 168, CW, "Partner task: teach a classmate one thing your family does in December, or one thing you would like to start. Plan, rehearse, deliver.")
y = sy - 22
for i, (n, t, s_, colr) in enumerate([("1", "PLAN", "Choose and outline.", PINE), ("2", "REHEARSE", "Say it twice to a partner.", RUST), ("3", "DELIVER", "Sixty seconds, then one question.", NAVY)]):
    bx = M + i * (CW / 3); c.saveState(); c.setFillColor(colr); c.circle(bx + 16, y - 10, 13, fill=1, stroke=0); c.restoreState()
    text(c, bx + 16, y - 14, n, "In-X", 11, white, "c"); text(c, bx + 36, y - 7, t, "In-X", 8.6, NAVY, track=1); text(c, bx + 36, y - 19, s_, "In-R", 8.2, MUTED)
y -= 40
L2 = [P("The prompt", h2), P("“Describe one December tradition, or one you would like to start. Say who does it, when, and what it means. Compare it with something a classmate described.”", S("pr", "Fr-I", 11.5, 15, NAVY, spaceAfter=6)),
      P("<b>More guidance:</b> use the planning card. Say one sentence for each line.", bodyS), P("<b>Growing independence:</b> add one detail nobody would guess, and one comparison with a partner's tradition.", bodyS),
      P("Round 1 / 45–60 seconds", h2), P("Speaker: talk. Listener: write one sentence in the note grid. Swap."), P("Round 2 / Improve one move", h2), P("Repeat with one change: a clearer opening, a stronger comparison, or an example. Say the thing you changed before you begin."),
      P("Questions that keep talking going", h2), BL(["Who taught you that?", "What happens if someone cannot be there?", "Is there a version for people who do not celebrate?"]),
      P("Planning card", h2), P("<b>WHO:</b> My ____ (family, friends, street) ____.<br/><b>WHEN:</b> On ____ / Every ____.<br/><b>WHAT:</b> We ____ and ____.<br/><b>WHY:</b> It matters because ____.<br/><b>COMPARE:</b> Like ____'s tradition, ours ____. Unlike ____, we ____.", S("pc", "In-R", 9, 13.6, INK, leftIndent=4)),
      P("Feedback that helps", h2), P("Say: “Your clearest part was ____.” Then: “I wanted to know ____.” Name one thing to keep and one thing to add."),
      P("Teacher listening guide", h2), P("Listen for a complete tradition (who, when, what), a comparison word (<i>like, unlike, both, while</i>), and one past-to-present connector from page 11. Note the names of students who use all three; they are ready for the Extension on page 5.")]
e = columns(c, L2, 2, y, 150)
by = max(min(e - 14, y), 150)
dark_box(c, M, by - 80, CW, 80, "Save the growth", [P("Record Round 1 on a phone. Record Round 2. Students listen to both and write one sentence: <i>In Round 2, I ____.</i> Keep the clips for a January comparison; the Round 2 recording is a dated speaking sample.", wbody)], PINE)
endpage(c, 10, "labs")

# ---------------- 11 GRAMMAR ----------------
runhead(c, "Language workshop · Grammar", "Used to / now · time connectors")
display(c, M, H - 92, ["Then and now.", "The grammar of change."], size=30, color=NAVY)
sy = standfirst(c, M, H - 168, CW, "December stories move between the past and the present. Two structures carry most of the work: <i>used to</i> + verb, and time connectors.")
y = sy - 22; bw = (CW - 20) / 3
for i, (t, s_, colr) in enumerate([("USED TO", "a past habit that stopped", SLATE), ("NOW / TODAY", "the present habit", PINE), ("WHEN · BEFORE · AFTER · WHILE", "connectors that order events", RUST)]):
    bx = M + i * (bw + 10); rect(c, bx, y - 36, bw, 36, colr, r=3); text(c, bx + 10, y - 16, t, "In-X", 7.8, white, track=1); text(c, bx + 10, y - 28, s_, "In-R", 8, white)
y -= 48
G = [P("Read the difference", h2), P("<b>Used to:</b> Luis <i>used to</i> walk past eleven houses without knowing anyone. (He does not anymore.)<br/><b>Now:</b> <i>Now</i> he makes the map every year.<br/><b>Connector:</b> <i>Before</i> the first walk, four neighbors said yes. <i>After</i> the ninth house, there were fourteen people."),
     P("A / Choose the structure", h2), NL(["Carmen ____ (celebrate) the posadas in her town. Now she ____ (walk) on Pine Street.", "____ Mr. Boyd joined, nobody played music. Now he prints the words.", "Mrs. Patel added a stop ____ the second year began."]),
     P("B / Combine the ideas", h2), P("Join each pair with a connector. Keep the order of events clear."), NL(["Luis read the lease. He wrote the email.", "The neighbors opened their doors. The group sang one song.", "The family from Vietnam arrived. They brought paper lanterns."]),
     P("C / Apply it to your life", h2), P("Write three sentences about your own December: one with <i>used to</i>, one with <i>now</i>, one with a connector. Underline the structure."),
     P("Teacher mini-lesson / 7 minutes", h2r), P("Show the two Pine Street sentences side by side. Ask what changed and which word shows it. Then ask the Spanish speakers how they say <i>used to</i> (the imperfect: <i>caminaba</i>, one word, no helper). Ask the Vietnamese speakers (<font name='In-M'>đã từng</font>, before the verb). Compare: English puts the past habit in a helper phrase before the verb. Name the pattern, then practice it."),
     P("Common mistakes to expect", h2r), BL(["<i>use to</i> for <i>used to</i> in writing (the final <i>d</i> is silent in speech).", "<i>I used to walking</i>: after <i>used to</i>, the base verb.", "A connector with no second clause: <i>After the walk.</i> Ask: after the walk, what?"]),
     P("D / Error hunt", h2), P("Find and fix the mistake in each sentence."), NL(["My family use to live in San Pedro Sula.", "When we moved here. We did not know anyone.", "Now I used to take the bus to school."]),
     P("Spanish bridge", h2p), P("<b>used to</b> ≈ imperfecto (<i>vivía, hacíamos</i>) · <b>now</b> = ahora · <b>when</b> = cuando · <b>before</b> = antes de · <b>after</b> = después de · <b>while</b> = mientras", S("sb", "In-R", 8.8, 12.4, PINE))]
columns(c, G, 2, y, 44)
endpage(c, 11, "labs")

# ---------------- 12 VOCABULARY ----------------
runhead(c, "Language workshop · Vocabulary", "Six words that travel")
display(c, M, H - 92, ["Words that travel well."], size=32, color=NAVY)
sy = standfirst(c, M, H - 132, CW, "Study the word, use it in a meaningful sentence, and compare it with your home language. Spanish is one optional bridge; invite other languages too.")
words = [("tradition", "tradición", "something a group does the same way, year after year", "Our ____ is to ____ every December."), ("gather", "reunirse", "to come together in one place", "On the 24th, we gather at ____."), ("translate", "traducir", "to say or write something in another language", "Luis translated the ____ into English."), ("neighbor", "vecino / vecina", "a person who lives near you", "My neighbor ____ when ____."), ("invitation", "invitación", "a request to come to an event", "The invitation said ____."), ("shelter", "refugio / posada", "a safe place to stay", "The song asks for shelter because ____.")]
y = sy - 26
for i, (w_, sp, d, fr) in enumerate(words):
    bx = M + (i % 3) * (C3 + GUT); by = y - (i // 3) * 92
    rect(c, bx, by - 82, C3, 82, MIST, r=3); rect(c, bx, by - 82, C3, 3, GOLD)
    text(c, bx + 10, by - 20, w_, "Fr-B", 15, NAVY); text(c, bx + 10, by - 32, sp, "Fr-I", 10, PINE)
    col(c, bx + 10, by - 78, C3 - 20, 42, [P(d, S("wd", "In-R", 8.2, 10.6, MUTED, spaceAfter=3)), P(fr, S("wf", "In-M", 8.2, 10.6, RUST))])
yy = y - 2 * 92 - 10
V = [P("A / Word-family builder", h2), P("Fill the family. The first one is done."), P("<b>tradition</b> → traditional (adj.) → traditionally (adv.)<br/><b>translate</b> → ____ (n.) → ____ (person)<br/><b>invite</b> → ____ (n.) → ____ (adj.: an ____ guest)<br/><b>gather</b> → a ____ (n., the event)", S("wfb", "In-R", 9, 13.4, INK, leftIndent=6, spaceAfter=5)),
     P("B / Meaning detective", h2), NL(["<i>Posada</i> means shelter, but it also names the tradition. Explain how one word can do both jobs.", "Which word on this page has a false friend in your home language? (A word that looks the same but means something else.) Explain it."]),
     P("C / Use it with purpose", h2), P("Write a five-sentence paragraph about Pine Street or your own street using at least four words from this page. Underline them."),
     P("D / Name it, compare it, carry it", h2), P("Choose <b>gather</b>. Name it in your home language. Compare: is your word used for people only, or for things too (gathering wood, gathering data)? Carry it: write one school sentence (<i>The scientist gathered data on ____</i>) and one home sentence."),
     P("Say it", h2), P("Clap the syllables: tra·DI·tion, IN·vi·TA·tion, TRANS·late, NEIGH·bor. Stress falls on the capital syllable. Partners listen for it.", bodyS)]
columns(c, V, 2, yy, 44)
endpage(c, 12, "labs")

# ---------------- 13 THE SECOND KEY ----------------
yt = opener(c, key_scene, "Literary lens · Original fiction", ["The Second Key"], "A short story about a door, a decision, and the sentence a student had been waiting to say.", size=46, h_=250)
st_l = [cap("<b>1</b>&nbsp; The key was on a green string. Ms. Okafor set it on the desk in front of Dayana and did not say anything for a moment, which was unusual for Ms. Okafor.", story),
        P("“The second key to the library,” she said finally. “I have the first. The custodian has a master. This one is for whoever opens the room at seven in the morning so students can study before first period.”", story),
        P("Dayana had been in the country for fourteen months. She understood every word. She did not understand why the key was on her desk.", story),
        P("“You are here every morning anyway,” Ms. Okafor said. “You might as well let the others in.”", story),
        P("<b>2</b>&nbsp; The first morning, nobody came. Dayana unlocked the door at 6:58, turned on the lights, and sat in the chair closest to the window with her chemistry book. At 7:40 she locked the door again and went to class. She did not tell anyone.", story),
        P("The second morning, a boy from her math class knocked, looked surprised that she was the one opening the door, and sat in the far corner without speaking.", story),
        P("The third morning there were four people. One of them was a freshman who spoke Arabic and almost no English, and he stood in the doorway until Dayana pointed at a chair and said, “Here. Sit. It's okay.” She heard her own voice say it and thought: <i>I sound like Ms. Okafor.</i>", story),
        P("<b>3</b>&nbsp; By the second week of December there were eleven students most mornings. Dayana made rules without meaning to. Coats on the back of chairs, not the tables. The freshman, whose name was Yusuf, got the chair by the window because he arrived first. Nobody talked before 7:15, because Dayana did not talk before 7:15.", story),
        P("On the last Wednesday before break, Yusuf came to the desk with a worksheet and put his finger on a word. <i>Although.</i>", story),
        P("Dayana knew the word. She had learned it in October, in this room, from a sentence on the board she could still see: <i>Although the experiment failed, the data were useful.</i> She had copied it four times.", story),
        P("“Although,” she said. “It means… two things are true, and they don't match.” She watched his face. Nothing. She tried again. “In Spanish we say <i>aunque</i>. Do you have a word?”", story),
        P("Yusuf thought, then wrote something in Arabic in the margin, and his face changed. “<i>Ma'a anna</i>,” he said. “Yes. I have.”", story),
        P("“Okay. So. <i>Although</i> it is cold, we come at seven.” She pointed at the window, at the dark, at the lights on the houses across the street. “Both true.”", story),
        P("Yusuf wrote the sentence. Then he wrote one of his own, and it was correct, and he looked at her like she had given him something.", story),
        P("<b>4</b>&nbsp; Ms. Okafor came in at 7:38, which she never did. She looked at the eleven students and the coats on the chairs and Yusuf's worksheet. She did not ask for the key back.", story),
        P("“I'm adding a third one in January,” she said. “Think about who should have it.”", story),
        P("Dayana thought about it for the whole walk to class. Yusuf arrived first every morning. Yusuf had a word for <i>although</i>. She would tell Ms. Okafor tomorrow, in a complete sentence, and she already knew how it would begin.", story),
        Spacer(1, 4), P("Read with a pencil. Mark the turning point. The story asks what a key gives a person besides a door.", S("rp", "In-M", 8.2, 11, PINE))]
for q in st_l:
    if isinstance(q, Paragraph) and q.style.name == "story": q.style = S("story13", "In-R", 8.9, 12.3, INK, spaceAfter=3)
columns(c, st_l, 3, yt - 8, 44)
endpage(c, 13, "features")

# ---------------- 14 ANALYSIS ----------------
runhead(c, "Literary lens · Analysis", "The Second Key")
display(c, M, H - 92, ["From a key to a sentence."], size=32, color=NAVY)
sy = standfirst(c, M, H - 132, CW * .62, "Shared literary objective: explain how a character's actions and a recurring object develop a theme.")
pull(c, M + CW * .66, H - 92, CW * .34, "“Yusuf's Arabic word opened the English one.”", NAVY, 14)
A4 = [P("A / Establish what happens", h2)] + NL(["Why does Ms. Okafor give Dayana the second key? Use her words.", "How many students come on the first, second and third mornings? What pattern do you see?", "What rules does Dayana make “without meaning to”? Name two.", "What word does Yusuf not understand, and how does Dayana finally explain it?"]) + [
      P("B / Interpret the craft", h2)] + NL(["The story is divided into four numbered parts. What changes between part 1 and part 4?", "Dayana thinks, <i>I sound like Ms. Okafor.</i> Why is this moment important?", "The window appears in parts 2, 3 and 4. What does it show each time?"]) + [
      P("C / Build a theme", h2), P("Finish the sentence and support it with two details: <b>The story suggests that a key represents ____ because ____.</b>"),
      P("D / Read the dialogue", h2)] + NL(["Dayana explains <i>although</i> three ways. List them in order. Which one works, and why?", "Ms. Okafor says, “Think about who should have it.” What does she already know?"]) + [
      P("Make the thinking accessible", h2), P("<b>More guidance:</b> place three moments in order: Dayana opens the door alone / Dayana helps Yusuf / Ms. Okafor adds a third key. Write one sentence about what changed.", bodyS), P("<b>Growing independence:</b> write a paragraph connecting the window to the theme. Use <i>although</i> once, correctly.", bodyS),
      P("Discussion bridge", h2), BL(["“A sentence that shows Dayana changed is ____.”", "“The key matters because ____.”", "“Although ____, ____.”"]),
      P("Extension", h2), P("Write the sentence Dayana says to Ms. Okafor tomorrow. It must begin with <i>Although</i>, name Yusuf, and give one reason.", bodyS)]
e = columns(c, A4, 2, sy - 16, 150)
by = max(min(e - 14, sy - 16), 150)
dark_box(c, M, by - 90, CW, 90, "What do you notice?", [P("Where in your own learning did a home-language word do the same job Yusuf's did? Write it down; it belongs on the Home Language Wall (page 17). Then write one sentence that begins with <i>Although</i> about something true this week.", wbody)])
endpage(c, 14, "features")

# ---------------- 15 WRITING WORKSHOP ----------------
yt = opener(c, kitchen, "Writing workshop · Procedural text", ["Write the way home."], "A procedural text explains how to do something in order. Students write one for a dish, a game or a routine from home, for a reader who has never seen it.", size=40, h_=290)
Wk = [P("The mentor text / abridged", h2), P("<b>How we make champurrado on the 24th</b><br/><i>You will need:</i> masa, water, milk, a tablet of chocolate, piloncillo, cinnamon, a wooden whisk.<br/><i>First,</i> dissolve the masa in cold water. <i>While</i> it rests, heat the milk with the cinnamon. <i>Then</i> add the chocolate and piloncillo and stir until they melt. <i>After that,</i> pour in the masa slowly, whisking the whole time. <i>Finally,</i> keep stirring on low heat until it is thick. Serve it hot, in small cups. <i>Warning:</i> it burns on the bottom if you stop stirring.", S("mt", "In-R", 8.8, 12.2, INK, leftIndent=6, spaceAfter=5)),
      P("Notice the structure", h2), BL(["A title that says what and when.", "A materials list before the steps.", "Order words: <i>first, while, then, after that, finally</i>.", "One warning: what goes wrong."]),
      P("Plan before you draft", h2), P("Choose a dish, a game or a routine. List the materials. Number the steps on scrap paper. Decide where the warning goes."),
      P("Your writing task", h2r), P("Write 120–180 words. Include a title, a materials list, at least five ordered steps with four different order words, and one warning. The reader has never seen this before, so explain the words they will not know in parentheses."),
      P("A frame you can expand", h2), P("<b>Title:</b> How we ____ on ____.<br/><b>You will need:</b> ____, ____, ____.<br/><b>First,</b> ____. <b>Then,</b> ____. <b>While</b> ____, ____. <b>After that,</b> ____. <b>Finally,</b> ____.<br/><b>Warning:</b> ____.", S("fx", "In-R", 9, 13.4, INK, leftIndent=6, spaceAfter=5)),
      P("Revise for the reader", h2), BL(["Circle every order word. Are there at least four different ones?", "Find one word from your home language. Is it explained in parentheses?", "Read the steps to a partner who follows them with their hands. Where did they stop?"]),
      P("Partner conference", h2), P("Reader says: “I could follow steps ____ to ____. I got lost at ____.” Writer fixes the one step.")]
columns(c, Wk, 2, yt - 8, 44)
endpage(c, 15, "labs")

# ---------------- 16 VISUAL LITERACY ----------------
runhead(c, "Visual literacy · Real data", "Daylight on December 21")
display(c, M, H - 92, ["A chart needs", "a careful reader."], size=32, color=NAVY)
sy = standfirst(c, M, H - 168, CW * .6, "Hours of daylight on December 21, the shortest day in the Northern Hemisphere, in eight cities many Mississippi students know. Values are calculated from latitude, rounded to the nearest five minutes.")
sun_arc(c, M + CW * .64, H - 92 - 100, CW * .36, 104)
text(c, M + CW * .64, H - 92 - 112, "The sun's path on Dec 21: Caracas (gold) vs Laurel (navy)", "In-R", 6.8, MUTED)
chx, chy, chw, chh = M, sy - 16 - 236, CW * .6, 236
rect(c, chx, chy, chw, chh, MIST, r=3)
text(c, chx + 12, chy + chh - 16, "DAYLIGHT ON DECEMBER 21 (HOURS : MINUTES)", "In-X", 6.8, GOLDINK, track=1.2)
mx = max(d[2] for d in DATA); bar_h = 17; gap = 6; bx0 = chx + 120; bwmax = chw - 120 - 56
for i, (name, lat, mins) in enumerate(DATA):
    by = chy + chh - 36 - i * (bar_h + gap) - bar_h
    text(c, bx0 - 6, by + 5, name.split(",")[0], "In-S", 7.8, NAVY, "r"); text(c, bx0 - 6, by - 2, f"{lat:.1f}°N", "In-R", 6, MUTED, "r")
    rect(c, bx0, by, bwmax * mins / mx, bar_h, NAVY if i == 0 else PINE, r=2); text(c, bx0 + bwmax * mins / mx + 5, by + 5, f"{mins // 60}:{mins % 60:02d}", "In-B", 8, INK)
text(c, chx + 12, chy + 8, "Calculated from latitude with standard sunrise/sunset geometry (sun at −0.833°). Method on page 25.", "In-R", 6.4, MUTED)
rx = M + CW * .64; rw = CW * .36
col(c, rx, chy, rw, H - 92 - 120 - chy, [P("Read the information", h2)] + NL(["Which city has the least daylight? The most?", "How much more daylight does Caracas have than Laurel? Give hours and minutes.", "What do the cities with the most daylight have in common? Look at the small gray number."]) + [P("Question the data", h2)] + NL(["The chart is for December 21. Would the order change on June 21? Explain.", "The values are rounded to five minutes. Could two cities really be tied?"]))
VL = [P("Say what the chart supports", h2), P("Finish each sentence with evidence from the chart."), BL(["“A student from ____ will notice that in Mississippi the sun sets ____ in December.”", "“The closer a city is to the equator, the ____.”", "“The difference between ____ and ____ is about ____ minutes, which is ____.”"]),
      P("Language support", h2), P("<b>Compare:</b> <i>____ has more / less daylight than ____.</i><br/><b>Explain:</b> <i>This is because ____ is closer to / farther from the equator.</i><br/><b>Hedge:</b> <i>The chart suggests ____, but it does not show ____.</i>", S("ls2", "In-R", 8.8, 12.6, INK)),
      P("Teacher note", h2r), P("Students arriving from the tropics often say Mississippi winters feel “dark.” This chart turns a feeling into a measurable difference, which is the move we want in every content class. The gap between Laurel and Caracas on December 21 is well over an hour."),
      P("Extension / the longest night", h2), P("Have students look up sunrise and sunset for their birthplace on December 21 from a reliable almanac or weather service, calculate the day length, and add it to the chart. Then write a two-sentence comparison using <i>although</i>."),
      P("Home-language bridge", h2p), P("<i>daylight</i> = luz del día · <i>equator</i> = ecuador · <i>latitude</i> = latitud. Ask which word is nearly the same in both languages and which is not.", S("hb", "In-R", 8.8, 12, PINE))]
columns(c, VL, 2, chy - 14, 44)
endpage(c, 16, "labs")

# ---------------- 17 HOME LANGUAGE WALL ----------------
yt = opener(c, wall_of_cards, "Student publishing project", ["Build the Home", "Language Wall."], "Essential question: what does our school sound like? Students publish a wall of phrases their families use, each with a translation, a pronunciation guide and a sentence about when it is said.", size=38, h_=300)
PUB = [P("The product", h2), P("One card per student, 5 × 8 inches, posted in a public hallway before break. Each card has: the phrase in the home language, the English meaning, a pronunciation line in plain letters, and two sentences: <i>We say this when ____. I chose it because ____.</i> Students who speak only English contribute a family phrase in English (every family has them)."),
       P("The process / three sessions", h2), P("<b>Session 1 / Collect:</b> students bring one phrase from home (the family page on 18 helps). Pairs check that the meaning is clear to a stranger.", bodyS), P("<b>Session 2 / Draft:</b> write the card. Say the pronunciation line to a partner who has never heard the language; revise until they can say it back.", bodyS), P("<b>Session 3 / Publish:</b> final cards, one color per language family if you like. Add a map pin for where the phrase comes from.", bodyS),
       P("Design requirements", h2), BL(["Phrase large enough to read from six feet.", "English meaning in a complete sentence, not a single word.", "The student's first name only; no other personal information.", "A small card that says who to ask if you want to learn it."]),
       P("Language requirements", h2r), P("Every card uses at least one structure from the Language workshop: <i>used to</i>, <i>now</i>, or a time connector. Example: <i>We used to say this only at home. Now my friends say it too.</i>"),
       P("Assess the thinking", h2r), P("Ask each student: What do you notice on the wall? Which phrase is closest to one you know? What surprised you? Score the explanation, not the decoration."),
       P("Name it, compare it, carry it", h2r), P("The wall is the routine made public. <b>Name it</b> (the phrase). <b>Compare it</b> (the translation and the moment it is used). <b>Carry it</b> (two sentences in academic English with a grammar target)."),
       P("Make it last", h2r), P("Photograph the wall. In January, choose ten phrases and record students saying them for a short audio tour; the hub's Listening & Speaking Studio has the format.")]
e = columns(c, PUB, 2, yt - 8, 140)
by = max(min(e - 14, yt - 8), 140)
dark_box(c, M, by - 84, CW, 84, "An audience gives the work purpose", [P("Invite the front office, the counselors and one administrator to the wall before break. Students stand by their cards and teach the phrase. Ten minutes; it changes how the building hears them.", wbody)], PLUM)
endpage(c, 17, "community")

# ---------------- 18 FAMILY PAGE ----------------
runhead(c, "Family connection · English + Spanish", "Optional take-home page")
display(c, M, H - 92, ["A conversation,", "then a card."], size=32, color=NAVY)
sy = standfirst(c, M, H - 168, CW, "Students interview a family member about one December memory. Families may answer in any language; students bring the phrase for the Home Language Wall.")
y = sy - 24
rect(c, M, y - 20, C2, 20, NAVY); text(c, M + 10, y - 14, "ENGLISH", "In-X", 7.4, white, track=1.4)
rect(c, M + C2 + GUT, y - 20, C2, 20, PINE); text(c, M + C2 + GUT + 10, y - 14, "ESPAÑOL", "In-X", 7.4, white, track=1.4)
EN = [P("Dear families,"), P("This month, students are learning how their first language helps them learn English. They are collecting one phrase each family uses, with a short explanation, for a display at school. There are no wrong answers and no required holidays."),
      P("An optional conversation", h2), P("Ask your student to write down your answers, in any language."), NL(["What is something our family says in December that other families might not say?", "When do we say it? Who taught it to you?", "What did you use to do in December when you were my age? What do we do now?", "Is there a tradition you would like us to start?"]),
      P("A simple response", h2), P("Your student will bring home a card that says: <i>We say ____ when ____.</i> If the meaning is not right, please tell them. They will fix it."), P("Student reflection", h2), P("One thing I learned from my family: ____.")]
ES = [P("Estimadas familias:"), P("Este mes, los estudiantes están aprendiendo cómo su primer idioma les ayuda a aprender inglés. Cada uno recopila una frase que su familia usa, con una breve explicación, para una exhibición en la escuela. No hay respuestas incorrectas ni fiestas obligatorias."),
      P("Una conversación opcional", h2p), P("Pida a su estudiante que anote sus respuestas, en cualquier idioma."), NL(["¿Qué decimos en nuestra familia en diciembre que otras familias quizá no digan?", "¿Cuándo lo decimos? ¿Quién se lo enseñó a usted?", "¿Qué solía hacer usted en diciembre cuando tenía mi edad? ¿Qué hacemos ahora?", "¿Hay una tradición que le gustaría que empezáramos?"]),
      P("Una respuesta sencilla", h2p), P("Su estudiante traerá una tarjeta que dice: <i>Decimos ____ cuando ____.</i> Si el significado no está bien, dígaselo. Lo corregirá."), P("Reflexión del estudiante", h2p), P("Algo que aprendí de mi familia: ____.")]
e1 = col(c, M, 160, C2, y - 28 - 160, EN); e2 = col(c, M + C2 + GUT, 160, C2, y - 28 - 160, ES)
by = max(min(e1, e2) - 16, 150)
rect(c, M, by - 100, CW, 100, CREAM, r=3)
text(c, M + 14, by - 16, "THE CARD YOUR STUDENT WILL MAKE  ·  LA TARJETA QUE HARÁ SU ESTUDIANTE", "In-X", 6.8, GOLDINK, track=1.2)
for i, lab in enumerate(["Phrase / Frase:", "Means / Significa:", "Say it / Se pronuncia:", "We say it when / Lo decimos cuando:"]):
    ly = by - 38 - i * 17; text(c, M + 14, ly, lab, "In-S", 8.2, NAVY); hline(c, M + 180, W - M - 14, ly - 2, HexColor("#C9BE9A"))
endpage(c, 18, "community")

# ---------------- 19 90-MINUTE BLOCK ----------------
runhead(c, "Teacher desk · Full lesson", "90 minutes")
display(c, M, H - 92, ["A complete 90-minute block."], size=30, color=NAVY)
sy = standfirst(c, M, H - 132, CW, "Shared goal: explain how a tradition changed over time, using one <i>used to / now</i> pair, one time connector and one detail from a text. Built for the EL block; adaptable to any content class.")
blocks = [("00–08", "Notice + name", "Show the street art on page 7. Ask: what do you call this where you come from? Collect words on the board in every language. One student explains a pattern they see.", SLATE), ("08–20", "Words + model", "Teach <i>used to</i> and <i>now</i> with the Pine Street pair (page 11). Say it, write it, compare it with a home language. Every student says one <i>used to / now</i> pair to a partner.", PINE), ("20–40", "Read + mark", "Read <i>The Window on Pine Street</i> aloud; students follow and mark the section numbers. Second read in pairs: find the sentence that shows the change. Answer A1–A3 on page 8.", NAVY), ("40–55", "Compare evidence", "Pairs complete the change chain (page 8, B). Share: what used to happen, what happens now, which connector joins them. Teacher writes three class sentences.", RUST), ("55–75", "Write + rehearse", "Each student writes a paragraph: a tradition that changed, theirs or Pine Street's. Requirements: one <i>used to / now</i> pair, one connector, one detail from the text or their own experience. Partner reads it aloud; writer revises one sentence.", PINE), ("75–85", "Speak", "Volunteers read a paragraph; the class names the pair and the connector they heard. Listeners write one sentence beginning <i>Like ____, my family ____.</i>", SLATE), ("85–90", "Exit + next step", "Exit ticket: <i>Although ____, ____.</i> Collect. Tomorrow: the listening script (page 9).", GOLDINK)]
yy = sy - 16
for t, n, d, colr in blocks:
    rect(c, M, yy - 58, 54, 54, colr, r=3); text(c, M + 27, yy - 26, t, "In-X", 8.6, white, "c"); text(c, M + 27, yy - 40, "MIN", "In-S", 6, GOLDLT, "c")
    text(c, M + 66, yy - 14, n, "In-X", 10.5, NAVY); col(c, M + 66, yy - 58, CW - 66, 40, [P(d, bodyS)]); hline(c, M + 66, W - M, yy - 62, RULE); yy -= 66
box(c, M, 44, CW, yy - 52, "Differentiation inside the block", [P("<b>Emerging:</b> the planning card and the Spanish bridge stay on the desk; paragraph may be four sentences with a drawing. <b>Progressing:</b> paragraph of six or more sentences with two connectors. <b>Extension:</b> add a sentence that begins <i>Unlike ____</i>. <b>Materials:</b> pages 7, 8, 11 printed; the board; a timer. <b>Evidence:</b> the paragraph and the exit ticket.", bodyS)])
endpage(c, 19, "planner")

# ---------------- 20 FIFTEEN LESSONS ----------------
runhead(c, "Teacher desk · Month map", "Fifteen lessons")
display(c, M, H - 92, ["Fifteen lessons. Three weeks."], size=30, color=NAVY)
sy = standfirst(c, M, H - 132, CW, "Use these between Thanksgiving and winter break. Adjust to your calendar; the lessons are numbered, not dated.")
cycles = [("WEEK 1 / Then and now", SLATE, [("01", "Name it, compare it, carry it", "Teach the routine (pp. 4–5) on one term from your content."), ("02", "The 90-minute block", "Page 19 in full, or split across two days."), ("03", "Reading response", "Page 8, A–C; language support frames."), ("04", "Grammar: used to / now", "Page 11, A–D; error hunt."), ("05", "Vocabulary + word families", "Page 12; Friday quiz on six words.")]),
          ("WEEK 2 / Voices", PINE, [("06", "Listening: Neighborhood Hour", "Page 9; two readings, note grid."), ("07", "Speaking: sixty seconds", "Page 10, Rounds 1 and 2; record."), ("08", "December with care", "Page 6 light inquiry; Human Rights Day on the 10th."), ("09", "The Second Key, read", "Page 13; mark the turning point."), ("10", "The Second Key, analyze", "Page 14, A–D; the <i>although</i> sentence.")]),
          ("WEEK 3 / Publish", RUST, [("11", "Writing: a how-to from home", "Page 15, plan and draft."), ("12", "Visual literacy: daylight", "Page 16; add your birthplace."), ("13", "Home Language Wall, sessions 1–2", "Page 17; family page (18) came home in week 2."), ("14", "Student check", "Pages 21–22; rubric for the writing."), ("15", "Publish + reflect", "Wall opens; Round 2 recordings; the five-day challenge (p. 26) goes home.")])]
yy = sy - 26
for i, (t, colr, items) in enumerate(cycles):
    bx = M + i * (C3 + GUT); rect(c, bx, yy - 22, C3, 22, colr, r=3); text(c, bx + 10, yy - 15, t, "In-X", 7.4, white, track=1); ly = yy - 30
    for n, h_, d in items:
        text(c, bx, ly - 13, n, "In-X", 14, colr); text(c, bx + 28, ly - 11, h_, "In-B", 8.4, NAVY)
        col(c, bx + 28, ly - 52, C3 - 28, 38, [P(d, S("ld", "In-R", 8.4, 11.2, MUTED))]); hline(c, bx, bx + C3, ly - 56, RULE); ly -= 68
yy = yy - 30 - 5 * 68 - 4
box(c, M, 44, CW, yy - 52, "Suggested ELP connections (not an official alignment)", [P("<b>Domains:</b> reading informational and literary text (pp. 7, 13); listening (p. 9); speaking (p. 10); writing procedural and explanatory text (pp. 15, 19). <b>Language:</b> past-habit and present forms, time connectors, comparison language, academic vocabulary across content areas. <b>Growth evidence:</b> the week-1 paragraph, the week-3 how-to and the student check give three dated samples for a portfolio; keep the Round 1 and Round 2 recordings for speaking. <b>Short weeks:</b> if you have fewer than fifteen days, teach 01, 02, 04, 06, 07, 09, 10, 11, 13 and 15 in that order.", bodyS)])
endpage(c, 20, "planner")

# ---------------- 21 STUDENT CHECK ----------------
runhead(c, "Student check · Original practice", "Not an official ELPA21 task")
display(c, M, H - 92, ["Can you explain what changed?"], size=30, color=NAVY)
text(c, M, H - 118, "Name: ______________________________      Date: ______________      Keep the text available.", "In-R", 9, MUTED)
rect(c, M, H - 214, CW, 84, MIST, r=3)
col(c, M + 12, H - 208, CW - 24, 74, [P("<b>Read:</b> A school posted this notice in November: “Students who arrive before 7:30 must wait outside the front doors.” In December, after three weeks of a student-run study room, the notice changed: “Students may enter the library at 7:00. A student monitor opens the door.” The principal said the change happened because attendance in first period improved and because a teacher trusted a student with a key.", S("ck", "In-R", 9.2, 12.6, INK))])
CK = [P("A / Read and reason", h2)] + NL(["What did the November notice say?", "What changed in December? Quote the new rule.", "Give the two reasons the principal gave.", "The second reason mentions a key. Which story in this issue does it connect to?"]) + [
      P("B / Use language", h2)] + NL(["Write one sentence about the school using <i>used to</i> and <i>now</i>.", "Join these with a connector: <i>Attendance improved. The rule changed.</i>", "Write one sentence that begins with <i>Although</i>."]) + [
      P("C / Explain a choice", h2), P("Choose <b>one</b> word: <i>monitor, trusted, attendance</i>. Name it in your home language, then write one sentence in English that shows you understand it in this context. (2 points)"),
      P("D / Listen and respond", h2), P("Teacher reads the Amara interview (page 9) once more. Answer:"), NL(["How many languages are on the lanterns this year?", "Why does Amara like the lantern about watching movies?"]),
      P("E / Write", h2), P("In 80–120 words, explain how the study room changed the school. Use: one <i>used to / now</i> pair, one time connector, one detail from the notice and one reason."),
      P("F / Speak (with a partner or recorded)", h2), P("In 45 seconds, describe a tradition or routine that changed. Use a connector. (Rubric, page 22.)"),
      P("Teacher recording", h2), P("Reading A: ____ / 4 &nbsp; Language B: ____ / 3 &nbsp; Word C: ____ / 2<br/>Listening D: ____ / 2 &nbsp; Writing E: rubric ____ &nbsp; Speaking F: rubric ____", S("tr", "In-R", 8.8, 13, INK)), P("Domain balance: reading, language, listening, writing and speaking appear in that order so the scores can be read beside ELPA21 domain reports. Not an official score.", small)]
e = columns(c, CK, 2, H - 230, 150)
by = min(e, H - 230) - 16
if by > 120:
    text(c, M, by - 10, "E / WRITE HERE", "In-X", 6.8, GOLDINK, track=1.2); ly = by - 28
    while ly > 46: hline(c, M, W - M, ly, RULE); ly -= 16
    note(44)
endpage(c, 21, "planner")

# ---------------- 22 RUBRIC ----------------
runhead(c, "Teacher desk · Classroom rubric", "Rubric + growth log")
display(c, M, H - 92, ["Describe growth, then", "name the next move."], size=30, color=NAVY)
sy = standfirst(c, M, H - 166, CW, "Use the rubric for the how-to (page 15), the paragraph (page 19) and the check (page 21). These local descriptors do not replace official proficiency levels.")
rows = [["CRITERION", "1 / STARTING", "2 / DEVELOPING", "3 / EXTENDING"], ["MEANING", "Names the change or tradition.", "Explains what changed and gives one reason.", "Explains the change, the cause and what it shows, with a comparison."], ["EVIDENCE", "Refers to the text or experience in general.", "Uses one specific detail, quoted or paraphrased.", "Uses two or more details and connects them."], ["STRUCTURE", "Ideas appear in a list.", "Events in order with one connector.", "Clear order with several connectors and a conclusion."], ["LANGUAGE", "Uses <i>now</i> or a past form; errors can block meaning.", "Uses <i>used to / now</i> correctly; errors rarely block meaning.", "Uses <i>used to / now</i>, <i>although</i> and precise vocabulary with control."]]
tdata = [[Paragraph(x, S("rc", "In-X" if r == 0 else "In-R", 7.2 if r == 0 else 8.4, 9.6 if r == 0 else 11, white if r == 0 else INK)) for x in row] for r, row in enumerate(rows)]
t = Table(tdata, colWidths=[78, (CW - 78) / 3, (CW - 78) / 3, (CW - 78) / 3])
t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), NAVY), ("BACKGROUND", (0, 1), (0, -1), MIST), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -1), .5, RULE), ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6), ("LEFTPADDING", (0, 0), (-1, -1), 7)]))
_, th = t.wrap(CW, 300); t.drawOn(c, M, sy - 18 - th); yy = sy - 18 - th - 14
RB = [P("Use the descriptors carefully", h2), P("Mark each criterion separately. A student can have strong meaning and developing English control; record the growth, then set one language target. Score the paragraph and the how-to with the same rubric so December gives you two comparable samples."),
      P("Speaking and listening", h2), P("For speaking, listen for the message first, then the structure. Record the result in the Teacher recording line on page 21."),
      P("Student self-check", h2), P("<i>My strongest row was ____.</i><br/><i>The support that helped me was ____.</i><br/><i>Next time I will ____.</i>", S("sc", "In-R", 9.2, 13.6, INK, spaceAfter=5)),
      P("Feedback formula", h2), P("Name the move the student made, cite one place it worked, give one next step. “You used <i>used to</i> and <i>now</i> in the first sentence; that showed the change clearly. Next, join two sentences with <i>after</i>.”"),
      P("Reteach signal", h2), P("Three or more students at level 1 on the same row means a ten-minute mini-lesson tomorrow on that row, with the page-11 sentences as the model.", bodyS)]
columns(c, RB, 2, yy, 170)
text(c, M, 156, "DECEMBER GROWTH LOG  ·  ONE ROW PER STUDENT, THREE DATED SAMPLES", "In-X", 6.8, GOLDINK, track=1.2)
gl = [[Paragraph(x, S("gl", "In-X", 7, 9.4, white)) for x in ["Student", "Wk 1 paragraph (M/E/S/L)", "Wk 3 how-to (M/E/S/L)", "Check, p. 21", "Next language target"]]] + [[Paragraph("", small)] * 5 for _ in range(4)]
gt = Table(gl, colWidths=[86, (CW - 86) * .25, (CW - 86) * .25, (CW - 86) * .16, (CW - 86) * .34], rowHeights=[18] + [21] * 4)
gt.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), NAVY), ("LINEBELOW", (0, 0), (-1, -1), .5, RULE), ("LEFTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
_, gh = gt.wrap(CW, 200); gt.drawOn(c, M, 148 - gh); note(44)
endpage(c, 22, "planner")

# ---------------- 23 ANSWER KEY 1 ----------------
runhead(c, "Teacher desk · Answer key 1", "Pages 8–12")
display(c, M, H - 92, ["Read for meaning.", "Respond with evidence."], size=28, color=NAVY)
sy = standfirst(c, M, H - 160, CW, "Accept accurate paraphrases. Open-response samples illustrate reasoning; students do not need to reproduce the wording.")
numS = S("numS", "In-R", 8.6, 11.8, INK, leftIndent=12, firstLineIndent=-12, spaceAfter=2)
K1 = [P("Page 8 / The Window on Pine Street", h2), NL(["To walk from house to house with lanterns and song, as in the posadas; Luis doubted it because no one here would know the song [2].", "No open flames on the porch [3].", "He asked the landlord by email about battery lanterns; the landlord said yes. Quote: “The landlord wrote back the same day: yes.” [3]", "Mrs. Patel (sweets, and she walked along); Mr. Boyd (a guitar) [5].", "The tradition's name became the Pine Street Walk, but the welcome, the open door, stayed the same [7]."], numS),
      P("<b>B:</b> eleven neighbors he did not know (0 known) · four doors · four languages.", bodyS), P("<b>C1:</b> Careful, responsible, wants to follow the rules. <b>C2:</b> Carmen started the tradition; her line states the theme; it returns the story to the idea of the door.", bodyS),
      P("<b>D1:</b> He gave a date and time, said neighbors did not have to do anything, and promised one song; a stranger needs to know what will happen and that there is no obligation. <b>D2:</b> The walk became shared; it was no longer one family's tradition.", bodyS), P("<b>E:</b> Email: greeting, clear question about battery lanterns, polite close. Flyer: date, time, what will happen, a line in a home language with a label.", bodyS),
      P("Page 9 / Listening", h2), NL(["To explain a student-made December tradition at a school.", "The main hallway; the last Friday before break (opens at three).", "One sentence about a family tradition, in English and in a home language.", "Thirty-one; more than two hundred.", "No candles; nothing hanging below seven feet.", "The one about watching movies, because it shows everybody has a December, even without a holiday."], numS),
      P("<b>7:</b> Every student has something true to write about December, celebrated or not; detail: the movie lantern. <b>8:</b> Reasonable either way; strong answers note they solved the problem and kept the display.", bodyS),
      P("Page 11 / Grammar", h2), P("<b>A:</b> 1 used to celebrate / walks; 2 Before; 3 before (or after; accept either with a sensible order). <b>B samples:</b> After Luis read the lease, he wrote the email. When the neighbors opened their doors, the group sang one song. When the family from Vietnam arrived, they brought paper lanterns. <b>D:</b> 1 <i>used to</i>; 2 <i>When we moved here, we did not know anyone.</i> (fragment joined); 3 <i>Now I take the bus</i> (<i>used to</i> cannot describe a present habit).", bodyS),
      P("Page 12 / Vocabulary", h2), P("<b>A:</b> translation / translator · invitation / invited · a gathering. <b>B1:</b> The word for the shelter became the name of the tradition that asks for it (a word can name an object and an event). <b>B2:</b> Any reasoned example; accept a student who finds none and explains why.", bodyS)]
e = columns(c, K1, 3, sy - 16, 44); e3 = LAST_ENDS[2]
if e3 > 200: dark_box(c, M + 2 * (C3 + GUT), e3 - 20 - 200, C3, 200, "How to use these keys", [P("Mark for the move, not the wording. A paraphrase that names the right section and the right detail earns full credit. When a student is wrong, ask which section they used; the error is usually a reading-location problem, not a language problem.", wbody), Spacer(1, 6), P("Score reading A1–A5 out of 5, listening 1–6 out of 6. Open responses: use the rubric on page 22.", S("kb", "In-R", 8.4, 11.2, GOLDLT))])
endpage(c, 23, "planner")

# ---------------- 24 ANSWER KEY 2 ----------------
runhead(c, "Teacher desk · Answer key 2", "Pages 14–21")
display(c, M, H - 92, ["Interpret. Compare.", "Decide what comes next."], size=28, color=NAVY)
sy = standfirst(c, M, H - 160, CW, "Use the keys to identify the next teaching move, not simply to mark a page complete.")
K2 = [P("Page 14 / The Second Key", h2), NL(["Someone must open the room at seven; “You are here every morning anyway.”", "Zero, one, four; the room grows as word spreads.", "Coats on chairs, not tables; the window chair goes to whoever arrives first; no talking before 7:15.", "<i>Although</i>; she gives the Spanish word and asks for his, then uses a sentence about the cold and the lights: both true."], numS),
      P("<b>B5:</b> From a key she does not understand to a decision about who should have the next one. <b>B6:</b> She has become the person who welcomes others. <b>B7:</b> Dark window / the window seat as a reward / the lit houses as the example that teaches <i>although</i>.", bodyS),
      P("<b>C sample:</b> The story suggests that a key represents trust because Ms. Okafor gives it without instructions and Dayana passes the trust on by choosing Yusuf. <b>D8:</b> definition, comparison with Spanish, a concrete example; the example works because it shows two true things at once. <b>D9:</b> That Dayana will choose well, and probably whom.", bodyS),
      P("Page 16 / Visual literacy", h2), P(f"<b>1:</b> Laurel least ({DATA[0][2]//60}:{DATA[0][2]%60:02d}); Caracas most ({DATA[-1][2]//60}:{DATA[-1][2]%60:02d}). <b>2:</b> about {(DATA[-1][2]-DATA[0][2])//60}:{(DATA[-1][2]-DATA[0][2])%60:02d}. <b>3:</b> lower latitude, closer to the equator. <b>4:</b> Yes; in June higher latitudes have longer days, so the order would reverse. <b>5:</b> Rounding can hide small differences; a tie on the chart may not be a true tie.", bodyS),
      P("Page 21 / Student check", h2), P("<b>A1:</b> Students arriving before 7:30 must wait outside. <b>A2:</b> “Students may enter the library at 7:00. A student monitor opens the door.” <b>A3:</b> First-period attendance improved; a teacher trusted a student with a key. <b>A4:</b> <i>The Second Key</i>. (4 points)", bodyS),
      P("<b>B5 sample:</b> Students used to wait outside; now they study in the library. <b>B6:</b> After attendance improved, the rule changed (or <i>Because</i>...). <b>B7:</b> Any correct <i>Although</i> sentence with two clauses. (3 points)", bodyS),
      P("<b>C:</b> 1 point for the home-language word, 1 for an English sentence that fits the context. <b>D:</b> nineteen; because it shows everybody has a December. (2 points) <b>E/F:</b> rubric, page 22.", bodyS),
      P("From an error to a next step", h2r), P("<b>Evidence missing:</b> return to one paragraph, offer two details, and ask which supports the claim. <b>Connector missing:</b> model one sentence with <i>after</i>, then have the student join two of their own. <b>Home-language word with no English sentence:</b> the comparison happened; supply the frame and have them say it before writing it.", bodyS),
      P("Reading response", h2), P("Reasonable claims with evidence earn credit. The keys show one path, not the only one.", bodyS)]
e = columns(c, K2, 3, sy - 16, 44); e3 = LAST_ENDS[2]
if e3 > 200: dark_box(c, M + 2 * (C3 + GUT), e3 - 20 - 150, C3, 150, "The next move, in one line", [P("<b>Most errors in A:</b> reread with section numbers tomorrow.<br/><b>Most errors in B:</b> reteach <i>used to / now</i> with the page-11 pair.<br/><b>Weak C:</b> run the three moves on one word, aloud.<br/><b>Weak E:</b> model one paragraph on the board; students revise theirs with one connector.", wbody)], PINE)
endpage(c, 24, "planner")

# ---------------- 25 SOURCES ----------------
runhead(c, "Sources + issue notes", "What we read")
display(c, M, H - 92, ["Grounded resources.", "Original classroom work."], size=28, color=NAVY)
sy = standfirst(c, M, H - 160, CW, "A transparent guide to the sources behind the editorial guidance and to the materials created for this issue.")
SR = [P("[1] English language proficiency", h2), P("<b>ELPA21.</b> The ELP Standards and the ELPA21 assessment system. Used for general domain language and purpose; the materials here are classroom practice, not official items. elpa21.org", bodyS),
      P("[2] Home language as an asset", h2), P("<b>Cummins, J. (1979).</b> Linguistic interdependence and the educational development of bilingual children. <i>Review of Educational Research</i>, 49(2). The basis for the claim that skills transfer across languages.", bodyS), P("<b>García, O., &amp; Wei, L. (2014).</b> <i>Translanguaging: Language, Bilingualism and Education.</i> Palgrave Macmillan. Informs the name-it / compare-it / carry-it routine.", bodyS),
      P("[3] Evidence-based practice", h2), P("<b>Baker, S., et al. (2014).</b> <i>Teaching Academic Content and Literacy to English Learners in Elementary and Middle School.</i> IES practice guide (NCEE 2014-4012). Recommendation 1 (academic vocabulary), 2 (oral and written language in content) and 3 (structured writing) shape the labs. ies.ed.gov/ncee/wwc", bodyS),
      P("[4] Observances", h2), P("<b>United Nations.</b> Human Rights Day (December 10) and International Migrants Day (December 18): un.org/en/observances. Universal Declaration of Human Rights, 1948, Articles 2 and 26. Other dates on page 6 should be verified locally each year; several follow lunar calendars.", bodyS),
      P("[5] Daylight data, page 16", h2), P("Day length is calculated from latitude for the December solstice (solar declination −23.44°, sun center at −0.833° to include refraction), rounded to five minutes. Latitudes are the city centers. For a specific date and location, use a national weather service or almanac.", bodyS),
      P("Editorial and production notes", h2), P("All readings, scripts, items and art are original to EL Publishing. <i>The Window on Pine Street</i> and <i>The Second Key</i> are fiction; names and places are invented. The art is drawn in code, not photographed, so no real students or homes appear. Design: navy and gold, Fraunces and Inter.", bodyS),
      P("Scope and use", h2), P("Free for classroom use. Teachers may print and copy pages for students. Please keep the EL Publishing credit on copies and do not sell the material.", bodyS)]
e = columns(c, SR, 2, sy - 16, 150)
by = max(min(e - 14, sy - 16), 150)
rect(c, M, by - 100, CW, 100, NAVY, r=3)
col(c, M + 14, by - 92, CW - 28, 86, [P("ON THE HUB THIS MONTH", S("oh", "In-X", 6.8, 9.6, GOLDLT)), Spacer(1, 4), P("<b>Today in EL</b> · a daily feed of EL articles and three curated picks. <b>Read Your Roster</b> · the ELPA21 level decoder. <b>Teaching the ELPT</b> · the 24-page special issue for the spring test. <b>The Long-Term EL Clinic</b> · twelve weeks on the academic register. <b>Monday Moves</b> · one two-minute move for every classroom teacher, every week. All free at radan55.github.io/everyteacher", S("ohb", "In-R", 9, 12.4, white))])
endpage(c, 25, "planner")

# ---------------- 26 BACK COVER ----------------
street(c, 0, 0, W, H, seed=61, moon=False, big=False)
fade(c, 0, 0, W, H, a_bottom=.92, a_top=.5)
text(c, M, H - 64, "EL PUBLISHING", "Fr-X", 26, white); text(c, M, H - 80, "DECEMBER 2026  ·  THE CLOSING CHALLENGE", "In-B", 7.4, GOLD, track=2)
display(c, M, H - 150, ["Carry the light", "home."], size=46, color=white)
col(c, M, H - 258, CW * .62, 48, [P("A five-day challenge for the last week before break. One move a day; each takes less than ten minutes.", S("bc", "Fr-R", 12, 16, GOLDLT))])
days = [("MONDAY", "NAME", "Say one school word in your home language to someone who does not speak it. Teach them to say it."), ("TUESDAY", "COMPARE", "Find one English word that looks like a word in your language. Decide if it is a true friend or a false one."), ("WEDNESDAY", "CARRY", "Use <i>although</i> in a sentence out loud, to a teacher, about something true."), ("THURSDAY", "LISTEN", "Ask a family member what they used to do in December. Write one sentence with <i>used to</i> and one with <i>now</i>."), ("FRIDAY", "LIGHT", "Put your sentence on the Home Language Wall, or in your notebook, and read it to one person.")]
yy = H - 284
for d, m_, s_ in days:
    rect(c, M, yy - 50, CW * .66, 46, Color(1, 1, 1, alpha=.08), r=3)
    text(c, M + 10, yy - 20, d, "In-X", 7, GOLD, track=1.4); text(c, M + 10, yy - 37, m_, "Fr-B", 13, white)
    col(c, M + 100, yy - 46, CW * .66 - 110, 40, [P(s_, S("dy", "In-R", 8.6, 11.4, white))]); yy -= 54
lantern(c, W - 110, H - 220, 1.4)
col(c, M, 118, CW * .62, 60, [P("Every language carries a light.<br/>Every student deserves a place to set it down.", S("close", "Fr-I", 14, 18, GOLDLT))])
text(c, M, 96, "MANY VOICES · ONE STORM", "In-X", 7.6, GOLD, track=2)
text(c, M, 80, "Next issue, January 2027: the ELPT countdown.", "In-R", 8.4, HexColor("#C9CEEA"))
rect(c, W - M - 190, 46, 190, 150, GOLD, r=4)
text(c, W - M - 95, 176, "THE HUB", "In-X", 8, NAVYDK, "c", track=2)
col(c, W - M - 180, 56, 170, 112, [P("<b>97 free resources</b> for teachers of English learners: Today in EL, Read Your Roster, Teaching the ELPT, Monday Moves, the Newcomer Guide in five languages, and every issue of this magazine.", S("ad", "In-R", 8.6, 11.4, NAVYDK, spaceAfter=6)), P("radan55.github.io/everyteacher", S("adu", "In-X", 8.6, 11, NAVYDK))])
c.showPage()
c.save()
print("wrote", OUT)
