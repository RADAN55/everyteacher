#!/usr/bin/env python3
"""Build el-magazine-2026-12.pdf — The Language of Home (December 2026).

Run from the repo root:  python3 tools/make-magazine-2026-12.py
Fonts: static instances are made from tools/fonts/*.ttf into /tmp on the fly.
Art is drawn in code (no stock photos), so the issue is fully original.
"""
import math, random, os, sys, tempfile
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, Color, white, black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import Paragraph, Frame, Spacer, KeepTogether, Table, TableStyle
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
pdfmetrics.registerFont(TTFont("Fr-B", inst(FR, "FrB", wght=700, opsz=72, SOFT=0, WONK=1)))
pdfmetrics.registerFont(TTFont("Fr-S", inst(FR, "FrS", wght=600, opsz=36, SOFT=0, WONK=0)))
pdfmetrics.registerFont(TTFont("Fr-R", inst(FR, "FrR", wght=400, opsz=14, SOFT=0, WONK=0)))
pdfmetrics.registerFont(TTFont("Fr-I", inst(FRI, "FrI", wght=500, opsz=36)))
pdfmetrics.registerFont(TTFont("In-R", inst(IN, "InR", wght=400)))
pdfmetrics.registerFont(TTFont("In-M", inst(IN, "InM", wght=500)))
pdfmetrics.registerFont(TTFont("In-S", inst(IN, "InS", wght=600)))
pdfmetrics.registerFont(TTFont("In-B", inst(IN, "InB", wght=700)))
pdfmetrics.registerFontFamily("In-R", normal="In-R", bold="In-B", italic="Fr-I", boldItalic="In-B")
pdfmetrics.registerFontFamily("Fr-R", normal="Fr-R", bold="Fr-B", italic="Fr-I", boldItalic="Fr-B")

# ---------- palette ----------
NAVY = HexColor("#1E2761"); NAVYDK = HexColor("#141A44"); GOLD = HexColor("#C9A227"); GOLDLT = HexColor("#EBD9A0")
GOLDINK = HexColor("#7A5F0E"); MIST = HexColor("#F4F5FA"); INK = HexColor("#1F2330"); MUTED = HexColor("#5D6480")
RULE = HexColor("#DCDEE9"); RUST = HexColor("#B35A3C"); PINE = HexColor("#3E5F57"); PAPER = white
SLATE = HexColor("#1F2F3F"); EMBER = HexColor("#E8A24A"); NIGHT = HexColor("#0C1030")

M = 46  # margin
CW = W - 2 * M

# ---------- styles ----------
def S(name, font, size, lead, color=INK, **kw):
    return ParagraphStyle(name, fontName=font, fontSize=size, leading=lead, textColor=color, **kw)
body = S("body", "In-R", 10, 13.8)
bodyS = S("bodyS", "In-R", 9.2, 12.4, MUTED)
small = S("small", "In-R", 8.4, 11.2, MUTED)
bodyXS = S("bodyXS", "In-R", 8.6, 11.4, MUTED)
lead = S("lead", "Fr-R", 11.6, 15.6, INK)
h2 = S("h2", "In-B", 9.4, 12.4, NAVY, spaceBefore=7, spaceAfter=2)
h2r = S("h2r", "In-B", 9.4, 12.4, RUST, spaceBefore=7, spaceAfter=2)
h2p = S("h2p", "In-B", 9.4, 12.4, PINE, spaceBefore=7, spaceAfter=2)
kick = S("kick", "In-S", 7.4, 10, GOLDINK)
quote = S("quote", "Fr-I", 13.5, 17.5, NAVY)
num = S("num", "In-R", 10, 13.8, INK, leftIndent=14, firstLineIndent=-14)
bul = S("bul", "In-R", 10, 13.8, INK, leftIndent=11, firstLineIndent=-11, bulletFontName="In-R")
wbody = S("wbody", "In-R", 9.2, 12.6, white)
wsmall = S("wsmall", "In-R", 8.4, 11.2, GOLDLT)
wh = S("wh", "In-B", 9.4, 12.4, GOLDLT, spaceBefore=6, spaceAfter=2)
cap = S("cap", "In-M", 7.6, 10, MUTED)
es = S("es", "In-R", 10, 13.8, INK)

def P(t, st=body): return Paragraph(t, st)
def NL(items, st=num):
    return [Paragraph(f"<b>{i+1}.</b> {t}", st) for i, t in enumerate(items)]
def BL(items, st=bul):
    return [Paragraph("•&nbsp; " + t, st) for t in items]

# ---------- drawing helpers ----------
PAGE_MIN = [H]
def note(y):
    if y > 40: PAGE_MIN[0] = min(PAGE_MIN[0], y)
def rect(c, x, y, w, h, fill, stroke=None, r=0):
    note(y); c.saveState(); c.setFillColor(fill)
    if stroke: c.setStrokeColor(stroke); c.setLineWidth(.6)
    else: c.setStrokeColor(fill)
    if r: c.roundRect(x, y, w, h, r, fill=1, stroke=1 if stroke else 0)
    else: c.rect(x, y, w, h, fill=1, stroke=1 if stroke else 0)
    c.restoreState()

def text(c, x, y, s, font="In-R", size=9, color=INK, align="l", track=0):
    note(y); c.saveState(); c.setFont(font, size); c.setFillColor(color)
    w = c.stringWidth(s, font, size) + track * max(len(s) - 1, 0)
    sx = x if align == "l" else (x - w if align == "r" else x - w / 2)
    t = c.beginText(sx, y); t.setFont(font, size); t.setFillColor(color)
    if track: t.setCharSpace(track)
    t.textOut(s); c.drawText(t)
    c.restoreState()

def col(c, x, y, w, h, flow, pad=0):
    f = Frame(x, y, w, h, leftPadding=pad, rightPadding=pad, topPadding=0, bottomPadding=0, showBoundary=0)
    out = []
    for it in flow:
        if isinstance(it, list): out.extend(it)
        else: out.append(it)
    flow = out; f.addFromList(flow, c)
    if flow:
        print(f"  !! overflow on page {c.getPageNumber()}: {len(flow)} flowables left; first: {str(flow[0])[:70]}")
    note(f._y); return f._y

QUOTES = ["Every language carries a light.", "A first language is not a detour. It is the road.", "The name changed. The door did not.", "Everybody has a December.", "Name it. Compare it. Carry it.", "Although it is cold, we come at seven."]
def endpage(c, quote=True):
    """Finish a page; if the text ends high, add a skyline strip so no page trails off into white."""
    top = PAGE_MIN[0]
    if top > 190:
        h_ = min(top - 18 - 46, 120); y0 = 46
        sky(c, M, y0, CW, h_, stars=50, seed=c.getPageNumber() * 3); skyline(c, M - 2, y0, CW + 4, seed=c.getPageNumber() * 7, scale=.5)
        if quote:
            q = QUOTES[c.getPageNumber() % len(QUOTES)]
            cv = c; cv.saveState(); cv.setFillColor(GOLDLT); cv.setFont("Fr-I", 12); cv.drawRightString(W - M - 14, y0 + h_ - 24, q); cv.restoreState()
    c.showPage(); PAGE_MIN[0] = H

def sky(c, x, y, w, h, stars=90, seed=1):
    c.saveState(); p = c.beginPath(); p.rect(x, y, w, h); c.clipPath(p, stroke=0, fill=0)
    c.linearGradient(x, y + h, x, y, (NIGHT, NAVY, HexColor("#2A3A7A")), (0, .55, 1), extend=True)
    rnd = random.Random(seed); c.setFillColor(white)
    for _ in range(stars):
        sx = x + rnd.random() * w; sy = y + h * (.35 + .65 * rnd.random()); r = rnd.choice([.5, .6, .8, 1.0, 1.3])
        c.setFillColor(Color(1, 1, 1, alpha=rnd.uniform(.35, .95))); c.circle(sx, sy, r, fill=1, stroke=0)
    c.restoreState()

def skyline(c, x, y, w, seed=2, scale=1.0, base=NIGHT):
    """Rooftops with warm windows along the bottom edge of a sky."""
    rnd = random.Random(seed); c.saveState(); cx = x
    while cx < x + w:
        bw = rnd.uniform(34, 78) * scale; bh = rnd.uniform(26, 92) * scale
        c.setFillColor(base); c.rect(cx, y, bw, bh, fill=1, stroke=0)
        roof = rnd.random()
        if roof < .45:  # gable
            p = c.beginPath(); p.moveTo(cx, y + bh); p.lineTo(cx + bw / 2, y + bh + bw * .38); p.lineTo(cx + bw, y + bh); p.close(); c.drawPath(p, fill=1, stroke=0)
        # chimney
        if rnd.random() < .4: c.rect(cx + bw * .68, y + bh, bw * .12, bh * .18 + 6, fill=1, stroke=0)
        # windows
        ww = 5.5 * scale; wh = 7.5 * scale; gx = 9.5 * scale; gy = 12 * scale
        rows = int((bh - 10) // gy); cols = int((bw - 10) // gx)
        for r in range(rows):
            for k in range(cols):
                if rnd.random() < .62:
                    c.setFillColor(rnd.choice([GOLD, EMBER, GOLDLT, GOLD]))
                    c.rect(cx + 6 + k * gx, y + 6 + r * gy, ww, wh, fill=1, stroke=0)
        cx += bw + rnd.uniform(2, 7)
    c.restoreState()

def lantern(c, cx, cy, s=1.0, glow=True):
    c.saveState()
    if glow:
        for i, a in [(2.6, .05), (2.0, .08), (1.5, .12), (1.15, .18)]:
            c.setFillColor(Color(0.91, 0.64, 0.29, alpha=a)); c.circle(cx, cy, 30 * s * i, fill=1, stroke=0)
    c.setFillColor(NAVYDK); c.rect(cx - 9 * s, cy + 30 * s, 18 * s, 4 * s, fill=1, stroke=0)
    c.setStrokeColor(NAVYDK); c.setLineWidth(1.2 * s); c.line(cx, cy + 34 * s, cx, cy + 52 * s)
    c.setFillColor(EMBER); c.roundRect(cx - 18 * s, cy - 28 * s, 36 * s, 58 * s, 7 * s, fill=1, stroke=0)
    c.setFillColor(GOLDLT); c.roundRect(cx - 11 * s, cy - 20 * s, 22 * s, 42 * s, 5 * s, fill=1, stroke=0)
    c.setFillColor(white); c.ellipse(cx - 4 * s, cy - 10 * s, cx + 4 * s, cy + 8 * s, fill=1, stroke=0)
    c.setFillColor(NAVYDK); c.rect(cx - 9 * s, cy - 32 * s, 18 * s, 4 * s, fill=1, stroke=0)
    c.restoreState()

def window(c, x, y, w, h, plant=True):
    c.saveState(); c.setFillColor(NAVYDK); c.rect(x - 6, y - 6, w + 12, h + 12, fill=1, stroke=0)
    c.saveState(); p = c.beginPath(); p.rect(x, y, w, h); c.clipPath(p, stroke=0, fill=0)
    c.linearGradient(x, y, x, y + h, (EMBER, GOLDLT), extend=True); c.restoreState()
    c.setFillColor(NAVYDK); c.rect(x + w / 2 - 2, y, 4, h, fill=1, stroke=0); c.rect(x, y + h * .55, w, 4, fill=1, stroke=0)
    if plant:
        c.setFillColor(HexColor("#2E4A3F"))
        c.ellipse(x + w * .62, y + 6, x + w * .86, y + h * .34, fill=1, stroke=0)
        c.ellipse(x + w * .70, y + 14, x + w * .96, y + h * .46, fill=1, stroke=0)
        c.setFillColor(RUST); c.rect(x + w * .66, y + 2, w * .22, 9, fill=1, stroke=0)
    c.restoreState()

def house(c, cx, cy, s=1.0, body_col=GOLDLT):
    c.saveState(); c.setFillColor(body_col); c.rect(cx - 16 * s, cy - 14 * s, 32 * s, 24 * s, fill=1, stroke=0)
    c.setFillColor(NAVY); p = c.beginPath(); p.moveTo(cx - 20 * s, cy + 10 * s); p.lineTo(cx, cy + 26 * s); p.lineTo(cx + 20 * s, cy + 10 * s); p.close(); c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(EMBER); c.rect(cx - 5 * s, cy - 14 * s, 10 * s, 14 * s, fill=1, stroke=0); c.restoreState()

def chrome(c, section, page, dark=False, label=None):
    """Running head and foot."""
    saved = PAGE_MIN[0]
    fg = GOLDLT if dark else MUTED; strong = white if dark else NAVY
    text(c, M, H - 30, "EL PUBLISHING", "In-B", 7.4, strong, track=1.4)
    text(c, M + 84, H - 30, "·  " + section.upper(), "In-S", 7.2, fg, track=1)
    text(c, W - M, H - 30, "DECEMBER 2026", "In-S", 7.2, fg, "r", track=1)
    c.saveState(); c.setStrokeColor(GOLD if dark else RULE); c.setLineWidth(.7); c.line(M, H - 38, W - M, H - 38); c.restoreState()
    c.saveState(); c.setStrokeColor(GOLD if dark else RULE); c.setLineWidth(.7); c.line(M, 36, W - M, 36); c.restoreState()
    text(c, M, 25, "EL PUBLISHING  ·  THE LANGUAGE OF HOME  ·  DECEMBER 2026", "In-S", 6.6, fg, track=.8)
    if label: text(c, W - M - 30, 25, label.upper(), "In-S", 6.6, fg, "r", track=.8)
    rect(c, W - M - 22, 20, 22, 14, GOLD if dark else NAVY)
    text(c, W - M - 11, 24, f"{page:02d}", "In-B", 7.6, NAVYDK if dark else white, "c")
    PAGE_MIN[0] = saved

def headline(c, y, big, deck=None, kicker=None, color=NAVY, size=27, wrap=None):
    if kicker: text(c, M, y + size + 8, kicker.upper(), "In-S", 7.4, GOLDINK, track=1.4)
    c.saveState(); c.setFillColor(color); c.setFont("Fr-B", size)
    lines = big.split("\n")
    for i, l in enumerate(lines): c.drawString(M - 1, y - i * (size * 1.06), l)
    c.restoreState()
    yy = y - (len(lines) - 1) * size * 1.06 - 14
    if deck:
        para = P(deck, S("dk", "In-R", 9.6, 13, MUTED)); _, dh = para.wrap(CW, 200)
        col(c, M, yy - dh, CW, dh, [para]); yy -= dh + 10
    return yy

def band(c, x, y, w, h, title, body_, fill=NAVY, tcol=GOLDLT, bcol=white):
    rect(c, x, y, w, h, fill, r=3)
    col(c, x + 11, y + 8, w - 22, h - 16, [P(title.upper(), S("bt", "In-B", 7.2, 10, tcol)), Spacer(1, 3), P(body_, S("bb", "In-R", 8.6, 11.4, bcol))])

def labelbox(c, x, y, w, h, title, items, fill=MIST, tcol=NAVY):
    rect(c, x, y, w, h, fill, r=3)
    col(c, x + 10, y + 8, w - 20, h - 16, [P(title.upper(), S("lt", "In-B", 7.2, 10, tcol)), Spacer(1, 3)] + items)

# ---------- daylight (for the visual literacy page) ----------
def daylight_hours(lat_deg, decl_deg=-23.44):
    lat = math.radians(lat_deg); d = math.radians(decl_deg); z = math.radians(90.833)
    cosH = (math.cos(z) - math.sin(lat) * math.sin(d)) / (math.cos(lat) * math.cos(d))
    return 2 * math.degrees(math.acos(max(-1, min(1, cosH)))) / 15

CITIES = [("Laurel, Mississippi", 31.7), ("Guatemala City, Guatemala", 14.6), ("Tegucigalpa, Honduras", 14.1),
          ("San Salvador, El Salvador", 13.7), ("Mexico City, Mexico", 19.4), ("Port-au-Prince, Haiti", 18.5),
          ("Hanoi, Vietnam", 21.0), ("Caracas, Venezuela", 10.5)]

# =====================================================================
c = canvas.Canvas(OUT, pagesize=letter, pageCompression=1)
c.setTitle("The Language of Home · December 2026 · EL Publishing"); c.setAuthor("Richard A. Daniel, M.Ed. · EL Publishing")
c.setSubject("The December 2026 issue of the EL Publishing English Learner Magazine, grades 9–12")

# ---------------- 01 COVER ----------------
sky(c, 0, H * .44, W, H * .56, stars=140, seed=7)
skyline(c, -10, H * .44, W + 20, seed=11, scale=1.25)
lantern(c, W - 120, H * .70, 1.45)
rect(c, 0, 0, W, H * .44, NAVYDK)
# masthead
text(c, M, H - 58, "EL PUBLISHING", "Fr-B", 30, white)
text(c, M, H - 74, "THE ENGLISH LEARNER MAGAZINE", "In-S", 7.6, GOLDLT, track=2)
text(c, W - M, H - 74, "DECEMBER 2026", "In-S", 7.6, GOLDLT, "r", track=2)
c.saveState(); c.setStrokeColor(GOLD); c.setLineWidth(.8); c.line(M, H - 84, W - M, H - 84); c.restoreState()
# title
c.saveState(); c.setFillColor(white); c.setFont("Fr-B", 52); c.drawString(M - 2, H - 150, "The language"); c.drawString(M - 2, H - 204, "of "); c.setFillColor(GOLD); c.drawString(M - 2 + c.stringWidth("of ", "Fr-B", 52), H - 204, "home."); c.restoreState()
col(c, M, H - 262, 330, 52, [P("Every student carries a home language. This issue shows how a classroom can open the door to it, build on it, and send students home with English they can use.", S("ctag", "Fr-R", 12.2, 16, GOLDLT))])
# bottom band content
text(c, M, H * .44 - 40, "THE WINTER ISSUE", "In-B", 7.6, GOLD, track=2)
c.saveState(); c.setFillColor(white); c.setFont("Fr-B", 21); c.drawString(M - 1, H * .44 - 70, "Name it. Compare it. Carry it."); c.restoreState()
col(c, M, H * .44 - 160, 270, 80, [P("A three-move routine that treats a student's first language as a bridge, not a detour. Plus original readings, a listening script, a family interview in two languages, fifteen lessons for the three weeks before break, and a student check with keys.", S("cb", "In-R", 9.6, 13.4, HexColor("#C9CEEA")))])
# inside box
rect(c, W - M - 206, H * .44 - 166, 206, 126, Color(1, 1, 1, alpha=.07), r=4)
text(c, W - M - 184, H * .44 - 60, "INSIDE", "In-B", 7.2, GOLD, track=1.6)
col(c, W - M - 194, H * .44 - 160, 186, 94, [P("The Window on Pine Street · an original reading<br/>The Second Key · original fiction<br/>A family interview, English and Spanish<br/>15 lessons · the December block<br/>Daylight data from eight cities<br/>Student check, rubric, teacher keys", S("ins", "In-R", 8.4, 12.2, white))])
# footer
rect(c, 0, 0, W, 54, GOLD)
text(c, M, 22, "26 PAGES  ·  GRADES 9–12  ·  FREE TO READ, TEACH & SHARE", "In-B", 8, NAVYDK, track=1.2)
text(c, W - M, 22, "radan55.github.io/everyteacher", "In-S", 8, NAVYDK, "r")
endpage(c)

# ---------------- 02 IN THIS ISSUE ----------------
chrome(c, "In this issue", 2, label="Contents")
y = headline(c, H - 96, "The December edit.", "Original readings, a three-move routine for home languages, and three weeks of lessons for grades 9–12. Page numbers match the PDF.", "In this issue")
# art strip
sky(c, M, y - 118, CW, 104, stars=70, seed=3); skyline(c, M - 4, y - 118, CW + 8, seed=5, scale=.55)
text(c, M + 16, y - 42, "THE DECEMBER EDIT", "In-B", 7, GOLD, track=1.6)
c.saveState(); c.setFillColor(white); c.setFont("Fr-B", 21); c.drawString(M + 16, y - 66, "Language. Learning. A way home."); c.restoreState()
toc = [("03", "From the editor", "Every language is a way home"),
       ("04–05", "The teaching feature", "Name it, compare it, carry it: the home-language routine"),
       ("06", "December with care", "Light, observances, and three questions before any holiday lesson"),
       ("07–08", "Reading lab", "The Window on Pine Street + comprehension"),
       ("09–10", "Voice studio", "Listening script + a 60-second tradition talk"),
       ("11–12", "Language workshop", "Used to / now, time connectors + word families"),
       ("13–14", "Literary lens", "The Second Key + evidence analysis"),
       ("15–16", "Writing & visual literacy", "A how-to from home + daylight data from eight cities"),
       ("17–18", "Community pages", "The Home Language Wall + a bilingual family interview"),
       ("19–20", "Plan the month", "90-minute block + fifteen lessons in three weeks"),
       ("21–22", "See the growth", "An original check + classroom rubric"),
       ("23–24", "Teacher desk", "Answer keys + feedback and reteaching"),
       ("25–26", "Keep the work going", "Sources, production notes, the five-day challenge")]
yy = y - 140; colw = CW / 2 - 10
for i, (pg, t, d) in enumerate(toc):
    cx = M + (i % 2) * (colw + 20); ry = yy - (i // 2) * 44
    text(c, cx, ry, pg, "Fr-B", 15, RUST)
    text(c, cx + 54, ry + 1, t, "In-B", 9.4, NAVY)
    col(c, cx + 54, ry - 26, colw - 54, 24, [P(d, bodyXS)])
    c.saveState(); c.setStrokeColor(RULE); c.setLineWidth(.5); c.line(cx, ry - 13, cx + colw, ry - 13); c.restoreState()
uy = yy - 7 * 44 - 10
text(c, M, uy, "HOW TEACHERS USE IT", "In-B", 7.4, GOLDINK, track=1.4)
uw = (CW - 20) / 3
for i, (t, d) in enumerate([("Teach the month", "Pages 19–20 hold a 90-minute block and fifteen lessons that string the readings, the script and the tasks into three weeks."), ("Pull one lab", "Each lab stands alone and shows Emerging and Progressing supports side by side; the Extension is for students who are ready."), ("Check the growth", "Pages 21–24 hold an original check, a classroom rubric, answer keys and guidance for feedback and reteaching.")]):
    bx = M + i * (uw + 10); rect(c, bx, uy - 100, uw, 92, MIST, r=3)
    col(c, bx + 10, uy - 94, uw - 20, 82, [P(t, S("ut", "Fr-B", 13, 15, NAVY, spaceAfter=3)), P(d, bodyXS)])
col(c, M, 48, CW, 30, [P("<b>Independent classroom edition.</b> Original passages, scripts and activities. Students answer in a notebook or on separate paper. Not an official ELPA21 publication.", small)])
endpage(c)

# ---------------- 03 FROM THE EDITOR ----------------
chrome(c, "From the editor", 3, label="Editorial")
y = headline(c, H - 96, "Every language is a way home.", "December is the month students most want to talk about where they come from. This issue gives them the English to do it, and gives you a routine to build on what they already know.", "From the editor")
L = [P("Dear colleagues,", body), Spacer(1, 6),
     P("In November we wrote about belonging as something a classroom designs. This month we take the next step. A student who feels welcome still has to decide, every day, whether the language they grew up with is allowed in the room. Our answer is yes, on purpose, with structure."),
     Spacer(1, 5),
     P("Research on bilingual development has said for decades that skills transfer across languages: a student who can summarize, infer and argue in Spanish, Vietnamese or Haitian Creole is not starting from zero in English. What they need is a bridge. This issue's teaching feature builds one in three moves: <b>name it</b> in any language, <b>compare it</b> across languages, <b>carry it</b> into academic English."),
     Spacer(1, 5),
     P("The readings are original. <i>The Window on Pine Street</i> follows a family's first December in a new town. <i>The Second Key</i> is a short story about a student trusted with a door. The listening script is a radio-style interview. The family page is written in English and Spanish so the conversation can happen at the kitchen table."),
     Spacer(1, 5),
     P("December is short. Fifteen lessons fit between Thanksgiving and winter break, and pages 19–20 lay them out so you can teach the issue in order or pull a single lab."),
     Spacer(1, 8), P("Teach well, and go home on time.", body), Spacer(1, 4), P("<b>Richard A. Daniel, M.Ed.</b><br/>Editor, EL Publishing", bodyS)]
col(c, M, 110, CW * .56 - 10, y - 110, L)
rx = M + CW * .56 + 10; rw = CW * .44 - 10
labelbox(c, rx, y - 150, rw, 150, "What this issue offers", BL(["One routine for every lesson: name it, compare it, carry it.", "Two original readings and one listening script, grades 9–12.", "A family interview in English and Spanish.", "A 90-minute block and fifteen lessons.", "A student check, a rubric and the keys."]))
labelbox(c, rx, y - 290, rw, 128, "How to use the supports", [P("Every lab shows <b>Emerging</b> and <b>Progressing</b> supports side by side, with an <b>Extension</b> for students who are ready. The labels describe the plan for the day, not the student. A student may be Progressing in reading and Emerging in writing; use the support that fits the task.", bodyS)], MIST)
rect(c, rx, 110, rw, y - 300 - 110, NAVY, r=3)
lantern(c, rx + rw / 2, 110 + (y - 300 - 110) / 2 + 10, .95)
col(c, rx + 12, 118, rw - 24, 30, [P("“A first language is not a detour. It is the road.”", S("eq", "Fr-I", 10.5, 13.5, GOLDLT, alignment=TA_CENTER))])
rect(c, M, 48, CW, 44, RUST)
col(c, M + 14, 56, CW - 28, 30, [P("<b>The editorial promise.</b> Rich design. Accessible language. Student work that leaves the classroom and reaches a reader.", S("ep", "In-R", 9.4, 12.6, white))])
endpage(c)

# ---------------- 04 TEACHING FEATURE 1 ----------------
chrome(c, "Teaching feature", 4, label="Feature 1 of 2")
sky(c, 0, H - 232, W, 194, stars=80, seed=21); skyline(c, -6, H - 232, W + 12, seed=23, scale=.6)
text(c, M, H - 70, "TEACHING FEATURE  ·  1 OF 2", "In-B", 7.2, GOLD, track=1.6)
c.saveState(); c.setFillColor(white); c.setFont("Fr-B", 30); c.drawString(M - 1, H - 104, "The home language is the bridge."); c.restoreState()
col(c, M, H - 160, CW * .7, 48, [P("A practical routine for any content lesson: let students name an idea in the language they think in, compare how two languages say it, then carry the idea into academic English they can write and say.", S("fd", "In-R", 10, 13.6, HexColor("#C9CEEA")))])
# three moves
bw = (CW - 20) / 3; by = H - 300
for i, (lab, q, colr) in enumerate([("Name it", "What do we call this where I come from?", SLATE), ("Compare it", "How is it the same? How is it different?", PINE), ("Carry it", "How do I say it in school English?", RUST)]):
    bx = M + i * (bw + 10); rect(c, bx, by, bw, 50, colr, r=3)
    text(c, bx + 10, by + 35, lab.upper(), "In-B", 8, white, track=1.2); col(c, bx + 10, by + 6, bw - 20, 26, [P(q, S("mq", "In-R", 8.2, 10.6, white))])
Lc = [P("1. Make the first language visible", h2),
      P("Begin with the concept, not the English word. Show the image, the problem or the diagram, and ask: <i>What do you call this at home?</i> Students write or say it in any language. A bilingual dictionary, a partner or a phone is fair. The point is that every student starts with something they already own."),
      P("2. Compare on purpose", h2),
      P("Put the home-language word next to the English word. Ask what students notice: a shared root (<i>analizar / analyze</i>), a different word order (<i>la casa blanca / the white house</i>), a sound that is new. Thirty seconds of comparison builds a habit of looking for patterns instead of guessing."),
      P("3. Carry it into school English", h2),
      P("Give a frame that uses the English term in the way the discipline uses it. Students say it, then write it. <i>The data suggest ____ because ____.</i> The home language has done its job; the sentence that reaches the page is in English.")]
col(c, M, 120, CW * .5 - 8, by - 132, Lc)
Rc = [P("A classroom snapshot", h2r),
      P("A biology class is labeling the parts of a cell. The teacher shows the diagram and asks for home-language names first. Three students write <i>núcleo</i>, one writes <i>nhân</i>, one writes the English word and shrugs. The teacher puts <i>núcleo</i> and <i>nucleus</i> side by side and asks what the class notices. A student says both start the same. Another says the Vietnamese word is shorter. The teacher writes the frame: <i>The nucleus controls the cell because ____.</i> Every student says it to a partner before writing it. Total time: four minutes."),
      P("Watch the response, not just the room", h2r),
      P("The routine works when students use the comparison. If the home-language word never comes back in their English sentence, the step was decoration. Ask one student to explain the pattern they found; that is the evidence."),
      P("Try this tomorrow", h2r),
      P("Pick the one term your lesson cannot do without. Run the three moves on that term alone. Keep the frame on the board for the whole period and count how many students use it in their exit ticket.")]
col(c, M + CW * .5 + 8, 120, CW * .5 - 8, by - 132, Rc)
rect(c, M, 50, CW, 56, GOLDLT, r=3)
col(c, M + 14, 58, CW - 28, 42, [P("THE ROUTINE IN ONE LINE", S("r1", "In-B", 7.2, 10, GOLDINK)), Spacer(1, 2), P("Name it in any language. Compare it across languages. Carry it into a complete academic sentence. Four minutes, any subject, every day.", S("r1b", "In-R", 9.4, 12.4, NAVY))])
endpage(c)

# ---------------- 05 TEACHING FEATURE 2 ----------------
chrome(c, "Teaching feature", 5, label="Feature 2 of 2")
y = headline(c, H - 96, "Same routine. Three supports.", "Shared objective: explain a key term using a comparison between two languages and a complete sentence in academic English.", "Teaching feature · 2 of 2")
y -= 6
def support(c, y, kicker, title, body_, frame, h_, colr):
    rect(c, M, y - h_, CW, h_, MIST, r=3); rect(c, M, y - h_, 5, h_, colr)
    col(c, M + 16, y - h_ + 8, CW - 32, h_ - 16, [P(kicker.upper(), S("sk", "In-B", 7.2, 10, colr)), P(title, S("st", "Fr-B", 13.5, 16, NAVY, spaceAfter=3)), P(body_, bodyS), Spacer(1, 3), P(frame, S("fr", "In-M", 8.8, 11.6, colr))])
    return y - h_ - 10
y = support(c, y, "Emerging · more guidance", "Make the pattern visible", "Give the home-language word and the English word already paired on a card. Students circle what is the same and underline what is different, then read the frame aloud twice with a partner before writing it. Allow a drawing beside the sentence.", "“In ____ we say ____. In English we say ____. Both ____.”", 112, SLATE)
y = support(c, y, "Progressing · growing independence", "Find the pattern", "Students write the home-language term themselves, then find a second English word with the same root or a word that sounds similar but means something else (a false friend). They explain the connection in one sentence and use the term in a second, original sentence.", "“____ and ____ share the root ____, which means ____. In this lesson, ____ means ____.”", 112, PINE)
y = support(c, y, "Extension · greater precision", "Teach the pattern", "Students prepare a 60-second explanation of one term for a classmate who speaks a different home language, including a comparison, a common mistake and an example from the lesson. They record it or deliver it live.", "“A common mistake is ____, because in ____ the word ____. The precise meaning here is ____.”", 112, RUST)
labelbox(c, M, y - 120, CW * .55 - 8, 120, "Language for comparison", BL(["This word looks like ____, but it means ____.", "In my language the adjective comes ____ the noun.", "The ending ____ tells me it is a ____ (noun / verb)."]) + [P("Post these three on the wall for the month.", small)])
rect(c, M + CW * .55 + 8, y - 120, CW * .45 - 8, 120, NAVY, r=3)
col(c, M + CW * .55 + 20, y - 112, CW * .45 - 32, 104, [P("TEACHER CHECK", S("tc", "In-B", 7.2, 10, GOLDLT)), Spacer(1, 3), P("If a student explains the pattern in their home language but cannot yet say it in English, the thinking is there. Accept the comparison, supply the frame, and have them repeat it. Do not mark the idea wrong because the English arrived second.", S("tcb", "In-R", 8.6, 11.4, white))])
endpage(c)

# ---------------- 06 DECEMBER WITH CARE ----------------
chrome(c, "December with care", 6, label="Observances")
y = headline(c, H - 96, "Light, without assumptions.", "December holds many observances and many students who celebrate none of them. Use light as the shared thread, and ask three questions before any holiday activity.", "December with care")
items = NL(["<b>Does the task assume a belief?</b> “Write about your Christmas tree” assumes a tree. “Describe a tradition your family keeps in winter, or one you would like to start” does not.",
            "<b>Can a student opt out without being noticed?</b> Offer two prompts of equal weight: a tradition, or a season. Both produce the same language.",
            "<b>Does the activity produce academic language?</b> A list of holiday words is vocabulary without a sentence. Every task in this issue ends in a comparison, an explanation or a claim."])
col(c, M, 300, CW * .55 - 8, y - 300, [P("Three questions first", h2)] + items + [
    P("Two observances worth teaching", h2),
    P("<b>Human Rights Day, December 10.</b> The United Nations adopted the Universal Declaration of Human Rights on this date in 1948. Article 26 concerns education; Article 2 says rights belong to everyone regardless of language. Have students read one article in English and one in a home language, then compare a key word."),
    P("<b>International Migrants Day, December 18.</b> Established by the UN General Assembly in 2000. A fair task: students write a one-paragraph profile of a person who moved, real or fictional, using three time connectors from the Language workshop (page 11).")])
rx = M + CW * .55 + 8; rw = CW * .45 - 8
rect(c, rx, y - 190, rw, 190, NAVY, r=3); lantern(c, rx + rw / 2, y - 70, .8)
col(c, rx + 12, y - 184, rw - 24, 66, [P("THE SHARED THREAD", S("sh", "In-B", 7.2, 10, GOLDLT)), P("Lamps, candles, bonfires, lanterns, the longest night. Light appears in winter traditions on every continent and in no religion in particular. Build the month on it.", S("shb", "In-R", 8.4, 11, white))])
labelbox(c, rx, 300, rw, y - 200 - 300, "A light inquiry (20 minutes)", [
    P("<b>Before:</b> Show four images of light in winter (a candle, a lantern, a bonfire, a window). Students name each in any language.", bodyXS), Spacer(1, 3),
    P("<b>During:</b> Pairs choose one and answer: Who lights it? When? What does it mean to the people who light it? Source: a family member, a book or a reliable site.", bodyXS), Spacer(1, 3),
    P("<b>After:</b> One sentence per pair on the wall: <i>In ____, people light ____ to ____.</i>", bodyXS)])
# bottom strip: a calendar of December light
rect(c, M, 60, CW, 228, MIST, r=3)
text(c, M + 14, 272, "DECEMBER LIGHT, ONE LINE EACH (VERIFY DATES LOCALLY)", "In-B", 7.2, GOLDINK, track=1.2)
rows = [("Dec 4–12", "Hanukkah (2026 dates)", "An eight-night festival; one more candle is lit each evening."),
        ("Dec 10", "Human Rights Day", "Marks the 1948 Universal Declaration of Human Rights."),
        ("Dec 13", "St. Lucia's Day", "Candles and processions in Sweden and other Nordic countries."),
        ("Dec 16–24", "Las Posadas", "Nine nights of processions in Mexico and Central America, with candles and song."),
        ("Dec 18", "International Migrants Day", "A UN observance since 2000."),
        ("Dec 21", "Winter solstice", "The shortest day in the Northern Hemisphere; see the daylight data on page 16."),
        ("Dec 25", "Christmas", "Lights on houses, trees and streets across many countries."),
        ("Dec 26–Jan 1", "Kwanzaa", "Seven nights; a candle is lit for each principle."),
        ("Jan 1", "New Year's Day", "Fireworks and lanterns around the world; Lunar New Year falls later (Feb 6, 2027).")]
ry = 254
for d, n, s_ in rows:
    text(c, M + 14, ry, d, "In-B", 8, RUST); text(c, M + 84, ry, n, "In-S", 8.4, NAVY); text(c, M + 232, ry, s_, "In-R", 8.2, INK); ry -= 21
endpage(c)

# ---------------- 07 READING LAB: TEXT ----------------
chrome(c, "Reading lab", 7, label="Student text")
y = headline(c, H - 96, "The Window on Pine Street", "Original informational narrative · Read to learn how a family's first December in a new town became a tradition for a whole street.", "Reading lab · Student text", size=26)
window(c, M, y - 130, 150, 112)
col(c, M + 170, y - 130, CW - 170, 112, [P("A note before reading", h2), P("Numbers in brackets mark the sections. Read once for the story, then again to answer the questions on page 8. New words: <b>landlord, porch, neighbor, lantern, tradition, gathered, nervous, translate.</b>", bodyS), Spacer(1, 4), P("Reading goal: explain what changed on Pine Street and what caused the change, using details from the text.", S("rg", "In-M", 8.6, 11.4, PINE))])
story_l = [P("<b>[1]</b> The Reyes family moved to Pine Street in October, when the trees were still green. By December the trees were bare and the house was cold in the mornings. Luis, who was fifteen, walked to school past eleven houses and did not know who lived in any of them."),
           P("<b>[2]</b> His mother, Carmen, had a plan. In the town where she grew up, December meant the <i>posadas</i>: nine nights when neighbors walked from house to house with candles, singing, asking for shelter, and being let in for food. “Here, nobody will know the song,” Luis said. “Then we will teach them,” she said."),
           P("<b>[3]</b> The first problem was the landlord. The lease said no open flames on the porch. Luis read the whole lease twice, then wrote an email in English asking whether battery lanterns were allowed. The landlord wrote back the same day: yes. Luis printed the email and put it on the refrigerator."),
           P("<b>[4]</b> The second problem was the neighbors. Carmen wrote an invitation in Spanish. Luis translated it, then changed it. His mother's version said, “We will arrive at your door and sing.” His version said, “We would like to walk to your house with lanterns on December 16, at six. You do not have to do anything. If you open the door, we will sing one song and move on.” He left copies in eleven mailboxes.")]
story_r = [P("<b>[5]</b> On December 16, four doors opened. At the fifth house, a woman named Mrs. Patel stood on the porch with a plate of sweets and asked if she could walk with them. At the seventh, a man named Mr. Boyd said he did not know the song but he had a guitar. By the ninth house there were fourteen people on the sidewalk, and three of them were singing."),
           P("<b>[6]</b> The second year, Mr. Boyd printed the words in English and Spanish. Mrs. Patel added a stop at her house for a lamp-lighting from her own December tradition. A family from Vietnam, new that year, brought paper lanterns. Luis made a map."),
           P("<b>[7]</b> Pine Street now has a December walk every year. The flyer is in four languages. Nobody calls it a <i>posada</i> anymore; they call it the Pine Street Walk. Carmen says this is fine. “The name changed,” she says. “The door did not.”"),
           Spacer(1, 6), P("<b>Quick glossary:</b> <i>posada</i> = shelter, lodging; <i>lease</i> = a rental agreement; <i>mailbox</i> = where letters are delivered; <i>flyer</i> = a one-page notice.", small),
           Spacer(1, 4), P("Original text by EL Publishing. Any resemblance to real streets or people is coincidental.", small)]
cw2 = (CW - 18) / 2
story = S("story", "In-R", 10.4, 14.6, INK, spaceAfter=4)
for q in story_l + story_r:
    if isinstance(q, Paragraph) and q.style.name == "body": q.style = story
col(c, M, 50, cw2, y - 150 - 50, story_l); col(c, M + cw2 + 18, 50, cw2, y - 150 - 50, story_r)
endpage(c)

# ---------------- 08 READING LAB: RESPONSE ----------------
chrome(c, "Reading lab", 8, label="Reading response")
y = headline(c, H - 96, "Notice. Explain. Prove.", "Use section numbers from page 7. Answer in a notebook or on separate paper. Explain your thinking to a partner before writing.", "Reading lab · Response")
A = [P("A / Build understanding", h2)] + NL(["What was Carmen's plan, and why did Luis doubt it?", "What did the lease say? Which section tells you?", "How did Luis solve the first problem? Quote the sentence that shows the solution.", "Which neighbors joined the walk the first year, and what did each one bring?", "Why does the text say the name changed but the door did not?"]) + [
    P("B / Follow the change", h2),
    P("Complete the chain with details from sections [1], [5] and [7]:", bodyS),
    P("<b>Beginning:</b> Luis knew ____ neighbors.<br/><b>First walk:</b> ____ doors opened.<br/><b>Now:</b> the flyer is in ____ languages.", S("ch", "In-R", 9.2, 13.4, INK, leftIndent=10)),
    P("C / Read like a writer", h2)] + NL(["The author tells us Luis read the lease <i>twice</i>. What does this detail show about him?", "Why do you think the author ended with Carmen's words instead of Luis's?"])
B = [P("D / Make an inference", h2)] + NL(["Luis changed his mother's invitation. Explain two changes he made and why each one might matter to a neighbor who does not know the tradition.", "Mrs. Patel added a stop from her own tradition. What does this suggest about how the walk changed over time?"]) + [
    P("E / Turn reading into action", h2),
    P("Choose one. Write 80–120 words.", bodyS),
    BL(["Write the email Luis sent to the landlord. Include a greeting, a clear question and a polite closing.", "Write the flyer for year three in English. Then add one line in a home language and label it."]),
    P("Language support", h2),
    P("<b>Start here:</b> “In section ____, the author says ____. This shows ____.”", bodyS),
    P("<b>Build further:</b> “Luis changed ____ because ____. This matters because ____.”", bodyS),
    P("<b>Stretch:</b> “Although the tradition came from ____, it became ____ when ____.”", bodyS), Spacer(1, 8)]
e1 = col(c, M, 60, cw2, y - 60, A); e2 = col(c, M + cw2 + 18, 60, cw2, y - 60, B)
by = max(min(e1, e2) - 16, 158)
rect(c, M, by - 98, CW * .55 - 8, 98, GOLDLT, r=3)
col(c, M + 12, by - 90, CW * .55 - 32, 82, [P("CHECK BEFORE YOU FINISH", S("cb2", "In-B", 7.2, 10, GOLDINK)), Spacer(1, 3), P("Circle the section number beside every answer. Underline one detail you used. If you wrote an opinion, point to the sentence in the text that supports it. Trade papers with a partner and read one answer aloud.", bodyS)])
rect(c, M + CW * .55 + 8, by - 98, CW * .45 - 8, 98, NAVY, r=3)
col(c, M + CW * .55 + 20, by - 90, CW * .45 - 32, 82, [P("NAME IT · COMPARE IT · CARRY IT", S("nc", "In-B", 7.2, 10, GOLDLT)), Spacer(1, 3), P("Choose the word <b>neighbor</b>. Name it in your home language. Compare: does your word include people on the whole street, or only next door? Carry it: write one sentence about Pine Street using <i>neighbor</i> in the English sense.", S("ncb", "In-R", 8.6, 11.4, white))])
endpage(c)

# ---------------- 09 VOICE STUDIO: LISTENING ----------------
chrome(c, "Voice studio", 9, label="Listening")
y = headline(c, H - 96, "A tradition, told out loud.", "Teacher-read script · Two voices · Original content, not an official test item. Read the script twice; students may take notes during the second reading.", "Voice studio · Listening")
scr = [P("Teacher script", h2),
       P("<b>HOST:</b> Welcome back to <i>Neighborhood Hour</i>. Today we are talking with Amara, a senior who started a December tradition at her school. Amara, what is it?"),
       P("<b>AMARA:</b> It's called the Lantern Hall. On the last Friday before break, students hang paper lanterns in the main hallway. Each lantern has one sentence on it about a tradition from their family, in English and in a home language."),
       P("<b>HOST:</b> How many lanterns did you have the first year?"),
       P("<b>AMARA:</b> Thirty-one. This year we have more than two hundred, in nineteen languages."),
       P("<b>HOST:</b> What was the hardest part?"),
       P("<b>AMARA:</b> Honestly, the rules. The fire marshal said no candles, which we expected. But he also said nothing could hang below seven feet. So we measured every lantern and moved the whole display up. We lost a week."),
       P("<b>HOST:</b> What do students write on the lanterns?"),
       P("<b>AMARA:</b> Anything true. One says, “My grandmother makes tamales on the 24th and we are not allowed to help.” One says, “We don't celebrate anything in December, so we watch movies for three days.” That one is my favorite."),
       P("<b>HOST:</b> Why?"),
       P("<b>AMARA:</b> Because it belongs there too. The point is not the holiday. The point is that everybody has a December."),
       P("<b>HOST:</b> Amara, thank you. The Lantern Hall opens Friday at three.")]
col(c, M, 60, cw2 + 10, y - 60, scr)
qx = M + cw2 + 28; qw = CW - cw2 - 28
Q = [P("Listen 1 / Purpose", h2)] + NL(["What is the main purpose of this interview?", "Where and when does the Lantern Hall happen?", "What two things are written on each lantern?"]) + [
     P("Listen 2 / Details", h2)] + NL(["How many lanterns were there the first year? This year?", "What two rules did the fire marshal give?", "Which lantern is Amara's favorite, and why?"]) + [
     P("After listening / Reasoning", h2)] + NL(["Amara says, “Everybody has a December.” Explain what she means using one detail from the interview.", "The display lost a week. Was that a failure? Give a reason."]) + [
     P("A useful note grid", h2), P("<b>WHO:</b> ____ &nbsp; <b>WHAT:</b> ____<br/><b>NUMBERS:</b> ____ / ____<br/><b>RULES:</b> ____ / ____<br/><b>FAVORITE:</b> ____", S("ng", "In-R", 9, 13.4, INK))]
e1 = col(c, qx, 60, qw, y - 60, Q); by = max(e1 - 14, 150)
rect(c, qx, by - 90, qw, 90, PINE, r=3)
col(c, qx + 12, by - 82, qw - 24, 76, [P("LANGUAGE SUPPORT", S("ls", "In-B", 7.2, 10, GOLDLT)), Spacer(1, 2), P("Emerging: hear the script three times; answer 1–3 with a partner. Progressing: answer all; add one sentence beginning <i>According to Amara, ____.</i> Everyone: speakers pause after each turn so students can write.", S("lsb", "In-R", 8.4, 11, white))])
endpage(c)

# ---------------- 10 VOICE STUDIO: SPEAKING ----------------
chrome(c, "Voice studio", 10, label="Speaking")
y = headline(c, H - 96, "Sixty seconds. One tradition.\nYour voice.", "Partner task: teach a classmate one thing your family does in December, or one thing you would like to start. Plan, rehearse, deliver.", "Voice studio · Speaking", size=25)
y -= 6
for i, (n, t, s_, colr) in enumerate([("1", "PLAN", "Choose and outline.", PINE), ("2", "REHEARSE", "Say it twice to a partner.", RUST), ("3", "DELIVER", "Sixty seconds, then one question.", NAVY)]):
    bx = M + i * (CW / 3); c.saveState(); c.setFillColor(colr); c.circle(bx + 16, y - 10, 13, fill=1, stroke=0); c.restoreState()
    text(c, bx + 16, y - 14, n, "In-B", 11, white, "c"); text(c, bx + 36, y - 7, t, "In-B", 9, NAVY, track=1); text(c, bx + 36, y - 19, s_, "In-R", 8.2, MUTED)
y -= 44
L2 = [P("The prompt", h2), P("“Describe one December tradition, or one you would like to start. Say who does it, when, and what it means. Compare it with something a classmate described.”", lead), Spacer(1, 4),
      P("<b>More guidance:</b> use the planning card. Say one sentence for each line.", bodyS), P("<b>Growing independence:</b> add one detail nobody would guess, and one comparison with a partner's tradition.", bodyS), Spacer(1, 4),
      P("Round 1 / 45–60 seconds", h2), P("Speaker: talk. Listener: write one sentence in the note grid. Swap."),
      P("Round 2 / Improve one move", h2), P("Repeat with one change: a clearer opening, a stronger comparison, or an example. Say the thing you changed before you begin."),
      P("Questions that keep talking going", h2), BL(["Who taught you that?", "What happens if someone cannot be there?", "Is there a version for people who do not celebrate?"])]
col(c, M, 60, cw2, y - 60, L2)
R2 = [P("Planning card", h2), P("<b>WHO:</b> My ____ (family, friends, street) ____.<br/><b>WHEN:</b> On ____ / Every ____.<br/><b>WHAT:</b> We ____ and ____.<br/><b>WHY:</b> It matters because ____.<br/><b>COMPARE:</b> Like ____'s tradition, ours ____. Unlike ____, we ____.", S("pc", "In-R", 9, 13.6, INK, leftIndent=4)),
      P("Feedback that helps", h2), P("Say: “Your clearest part was ____.” Then: “I wanted to know ____.” Name one thing to keep and one thing to add."),
      P("Teacher listening guide", h2), P("Listen for a complete tradition (who, when, what), a comparison word (<i>like, unlike, both, while</i>), and one past-to-present connector from page 11. Note the names of students who use all three; they are ready for the Extension on page 5.")]
e1 = col(c, M + cw2 + 18, 60, cw2, y - 60, R2); by = max(e1 - 14, 150)
rect(c, M + cw2 + 18, by - 86, cw2, 86, PINE, r=3)
col(c, M + cw2 + 30, by - 78, cw2 - 24, 72, [P("SAVE THE GROWTH", S("sg", "In-B", 7.2, 10, GOLDLT)), Spacer(1, 2), P("Record Round 1 on a phone. Record Round 2. Students listen to both and write one sentence: <i>In Round 2, I ____.</i> Keep the clips for a January comparison.", S("sgb", "In-R", 8.4, 11, white))])
endpage(c)

# ---------------- 11 LANGUAGE WORKSHOP: GRAMMAR ----------------
chrome(c, "Language workshop", 11, label="Grammar")
y = headline(c, H - 96, "Then and now.\nThe grammar of change.", "December stories move between the past and the present. Two structures carry most of the work: <i>used to</i> + verb, and time connectors.", "Language workshop · Grammar", size=25)
y -= 2
bw = (CW - 20) / 3
for i, (t, s_, colr) in enumerate([("USED TO", "a past habit that stopped", SLATE), ("NOW / TODAY", "the present habit", PINE), ("WHEN · BEFORE · AFTER · WHILE", "connectors that order events", RUST)]):
    bx = M + i * (bw + 10); rect(c, bx, y - 36, bw, 36, colr, r=3); text(c, bx + 10, y - 16, t, "In-B", 8, white, track=1); text(c, bx + 10, y - 28, s_, "In-R", 8, white)
y -= 48
L3 = [P("Read the difference", h2), P("<b>Used to:</b> Luis <i>used to</i> walk past eleven houses without knowing anyone. (He does not anymore.)"), P("<b>Now:</b> <i>Now</i> he makes the map every year."), P("<b>Connector:</b> <i>Before</i> the first walk, four neighbors said yes. <i>After</i> the ninth house, there were fourteen people."),
      P("A / Choose the structure", h2), NL(["Carmen ____ (celebrate) the posadas in her town. Now she ____ (walk) on Pine Street.", "____ Mr. Boyd joined, nobody played music. Now he prints the words.", "Mrs. Patel added a stop ____ the second year began."]),
      P("B / Combine the ideas", h2), P("Join each pair with a connector. Keep the order of events clear."), NL(["Luis read the lease. He wrote the email.", "The neighbors opened their doors. The group sang one song.", "The family from Vietnam arrived. They brought paper lanterns."]),
      P("C / Apply it to your life", h2), P("Write three sentences about your own December: one with <i>used to</i>, one with <i>now</i>, one with a connector. Underline the structure.")]
col(c, M, 60, cw2, y - 60, L3)
R3 = [P("Teacher mini-lesson / 7 minutes", h2), P("Show the two Pine Street sentences side by side. Ask what changed and which word shows it. Then ask the Spanish speakers how they say <i>used to</i> (the imperfect: <i>caminaba</i>, one word, no helper). Ask the Vietnamese speakers (<font name='In-M'>đã từng</font>, before the verb). Compare: English puts the past habit in a helper phrase before the verb. Name the pattern, then practice it."),
      P("Common mistakes to expect", h2), BL(["<i>use to</i> for <i>used to</i> in writing (the final <i>d</i> is silent in speech).", "<i>I used to walking</i>: after <i>used to</i>, the base verb.", "A connector with no second clause: <i>After the walk.</i> Ask: after the walk, what?"]),
      P("D / Error hunt", h2), P("Find and fix the mistake in each sentence."), NL(["My family use to live in San Pedro Sula.", "When we moved here. We did not know anyone.", "Now I used to take the bus to school."]),
      P("Spanish bridge", h2), P("<b>used to</b> ≈ imperfecto (<i>vivía, hacíamos</i>) · <b>now</b> = ahora · <b>when</b> = cuando · <b>before</b> = antes de · <b>after</b> = después de · <b>while</b> = mientras", S("sb", "In-R", 8.8, 12.4, PINE))]
col(c, M + cw2 + 18, 60, cw2, y - 60, R3)
endpage(c)

# ---------------- 12 LANGUAGE WORKSHOP: VOCABULARY ----------------
chrome(c, "Language workshop", 12, label="Vocabulary")
y = headline(c, H - 96, "Words that travel well.", "Study the word, use it in a meaningful sentence, and compare it with your home language. Spanish is one optional bridge; invite other languages too.", "Language workshop · Vocabulary")
words = [("tradition", "tradición", "something a group does the same way, year after year", "Our ____ is to ____ every December."),
         ("gather", "reunirse", "to come together in one place", "On the 24th, we gather at ____."),
         ("translate", "traducir", "to say or write something in another language", "Luis translated the ____ into English."),
         ("neighbor", "vecino / vecina", "a person who lives near you", "My neighbor ____ when ____."),
         ("invitation", "invitación", "a request to come to an event", "The invitation said ____."),
         ("shelter", "refugio / posada", "a safe place to stay", "The song asks for shelter because ____.")]
cw3 = (CW - 18) / 2
for i, (w_, sp, d, fr) in enumerate(words):
    bx = M + (i % 2) * (cw3 + 18); by = y - 16 - (i // 2) * 92
    rect(c, bx, by - 76, cw3, 80, MIST, r=3)
    text(c, bx + 12, by - 14, w_, "Fr-B", 15, NAVY); text(c, bx + 12 + c.stringWidth(w_, "Fr-B", 15) + 10, by - 14, sp, "Fr-I", 10.5, PINE)
    col(c, bx + 12, by - 70, cw3 - 24, 52, [P(d, bodyS), Spacer(1, 3), P(fr, S("wf", "In-M", 8.6, 11.4, RUST))])
yy = y - 16 - 3 * 92 - 6
L4 = [P("A / Word-family builder", h2), P("Fill the family. The first one is done."), P("<b>tradition</b> → traditional (adj.) → traditionally (adv.)<br/><b>translate</b> → ____ (n.) → ____ (person)<br/><b>invite</b> → ____ (n.) → ____ (adj.: an ____ guest)<br/><b>gather</b> → a ____ (n., the event)", S("wfb", "In-R", 9, 13.4, INK, leftIndent=6)),
      P("B / Meaning detective", h2), NL(["<i>Posada</i> means shelter, but it also names the tradition. Explain how one word can do both jobs.", "Which word on this page has a false friend in your home language? (A word that looks the same but means something else.) Explain it."])]
col(c, M, 60, cw3, yy - 60, L4)
R4 = [P("C / Use it with purpose", h2), P("Write a five-sentence paragraph about Pine Street or your own street using at least four words from this page. Underline them."),
      P("D / Name it, compare it, carry it", h2), P("Choose <b>gather</b>. Name it in your home language. Compare: is your word used for people only, or for things too (gathering wood, gathering data)? Carry it: write one school sentence (<i>The scientist gathered data on ____</i>) and one home sentence."),
      P("Say it", h2), P("Clap the syllables: tra·DI·tion, IN·vi·TA·tion, TRANS·late, NEIGH·bor. Stress falls on the capital syllable. Partners listen for it.", bodyS)]
col(c, M + cw3 + 18, 60, cw3, yy - 60, R4)
endpage(c)

# ---------------- 13 LITERARY LENS: STORY ----------------
chrome(c, "Literary lens", 13, label="Original fiction")
sky(c, 0, H - 250, W, 212, stars=100, seed=31); skyline(c, -6, H - 250, W + 12, seed=37, scale=1.05)
text(c, M, H - 70, "LITERARY LENS  ·  ORIGINAL FICTION", "In-B", 7.2, GOLD, track=1.6)
c.saveState(); c.setFillColor(white); c.setFont("Fr-B", 38); c.drawString(M - 1, H - 112, "The Second Key"); c.restoreState()
col(c, M, H - 160, CW * .75, 40, [P("A short story about a door, a decision, and the sentence a student had been waiting to say.", S("fd2", "Fr-I", 12, 15, GOLDLT))])
st_l = [P("<b>1</b>&nbsp; The key was on a green string. Ms. Okafor set it on the desk in front of Dayana and did not say anything for a moment, which was unusual for Ms. Okafor."),
        P("“The second key to the library,” she said finally. “I have the first. The custodian has a master. This one is for whoever opens the room at seven in the morning so students can study before first period.”"),
        P("Dayana had been in the country for fourteen months. She understood every word. She did not understand why the key was on her desk."),
        P("“You are here every morning anyway,” Ms. Okafor said. “You might as well let the others in.”"),
        P("<b>2</b>&nbsp; The first morning, nobody came. Dayana unlocked the door at 6:58, turned on the lights, and sat in the chair closest to the window with her chemistry book. At 7:40 she locked the door again and went to class. She did not tell anyone."),
        P("The second morning, a boy from her math class knocked, looked surprised that she was the one opening the door, and sat in the far corner without speaking."),
        P("The third morning there were four people. One of them was a freshman who spoke Arabic and almost no English, and he stood in the doorway until Dayana pointed at a chair and said, “Here. Sit. It's okay.” She heard her own voice say it and thought: <i>I sound like Ms. Okafor.</i>"),
        P("<b>3</b>&nbsp; By the second week of December there were eleven students most mornings. Dayana made rules without meaning to. Coats on the back of chairs, not the tables. The freshman, whose name was Yusuf, got the chair by the window because he arrived first. Nobody talked before 7:15, because Dayana did not talk before 7:15.")]
st_r = [P("On the last Wednesday before break, Yusuf came to the desk with a worksheet and put his finger on a word. <i>Although.</i>"),
        P("Dayana knew the word. She had learned it in October, in this room, from a sentence on the board she could still see: <i>Although the experiment failed, the data were useful.</i> She had copied it four times."),
        P("“Although,” she said. “It means… two things are true, and they don't match.” She watched his face. Nothing. She tried again. “In Spanish we say <i>aunque</i>. Do you have a word?”"),
        P("Yusuf thought, then wrote something in Arabic in the margin, and his face changed. “<i>Ma'a anna</i>,” he said. “Yes. I have.”"),
        P("“Okay. So. <i>Although</i> it is cold, we come at seven.” She pointed at the window, at the dark, at the lights on the houses across the street. “Both true.”"),
        P("Yusuf wrote the sentence. Then he wrote one of his own, and it was correct, and he looked at her like she had given him something."),
        P("<b>4</b>&nbsp; Ms. Okafor came in at 7:38, which she never did. She looked at the eleven students and the coats on the chairs and Yusuf's worksheet. She did not ask for the key back."),
        P("“I'm adding a third one in January,” she said. “Think about who should have it.”"),
        P("Dayana thought about it for the whole walk to class. Yusuf arrived first every morning. Yusuf had a word for <i>although</i>. She would tell Ms. Okafor tomorrow, in a complete sentence, and she already knew how it would begin."),
        Spacer(1, 6), P("Read with a pencil. Mark the turning point. The story asks what a key gives a person besides a door.", S("rp", "In-M", 8.4, 11, PINE))]
col(c, M, 50, cw2, H - 262 - 50, st_l); col(c, M + cw2 + 18, 50, cw2, H - 262 - 50, st_r)
endpage(c)

# ---------------- 14 LITERARY LENS: ANALYSIS ----------------
chrome(c, "Literary lens", 14, label="Literary analysis")
y = headline(c, H - 96, "From a key to a sentence.", "Shared literary objective: explain how a character's actions and a recurring object develop a theme.", "Literary lens · Analysis")
A4 = [P("A / Establish what happens", h2)] + NL(["Why does Ms. Okafor give Dayana the second key? Use her words.", "How many students come on the first, second and third mornings? What pattern do you see?", "What rules does Dayana make “without meaning to”? Name two.", "What word does Yusuf not understand, and how does Dayana finally explain it?"]) + [
      P("B / Interpret the craft", h2)] + NL(["The story is divided into four numbered parts. What changes between part 1 and part 4?", "Dayana thinks, <i>I sound like Ms. Okafor.</i> Why is this moment important?", "The window appears in parts 2, 3 and 4. What does it show each time?"]) + [
      P("C / Build a theme", h2), P("Finish the sentence and support it with two details: <b>The story suggests that a key represents ____ because ____.</b>")]
B4 = [P("D / Read the dialogue", h2)] + NL(["Dayana explains <i>although</i> three ways. List them in order. Which one works, and why?", "Ms. Okafor says, “Think about who should have it.” What does she already know?"]) + [
      P("Make the thinking accessible", h2), P("<b>More guidance:</b> place three moments in order: Dayana opens the door alone / Dayana helps Yusuf / Ms. Okafor adds a third key. Write one sentence about what changed.", bodyS), P("<b>Growing independence:</b> write a paragraph connecting the window to the theme. Use <i>although</i> once, correctly.", bodyS),
      P("Discussion bridge", h2), P("Use these frames in a small group."), BL(["“A sentence that shows Dayana changed is ____.”", "“The key matters because ____.”", "“Although ____, ____.”"]),
      P("Extension", h2), P("Write the sentence Dayana says to Ms. Okafor tomorrow. It must begin with <i>Although</i>, name Yusuf, and give one reason.", bodyS)]
col(c, M, 60, cw2, y - 60, A4); e1 = col(c, M + cw2 + 18, 60, cw2, y - 60, B4); by = max(e1 - 14, 160)
rect(c, M + cw2 + 18, by - 100, cw2, 100, NAVY, r=3); house(c, M + cw2 + 48, by - 56, 1.0)
col(c, M + cw2 + 82, by - 92, cw2 - 76, 86, [P("WHAT DO YOU NOTICE?", S("wn", "In-B", 7.2, 10, GOLDLT)), Spacer(1, 3), P("Yusuf's Arabic word opened the English one. Where in your own learning did a home-language word do the same job? Write it down; it belongs on the Home Language Wall (page 17).", S("wnb", "In-R", 8.4, 11, white))])
endpage(c)

# ---------------- 15 WRITING WORKSHOP ----------------
chrome(c, "Writing workshop", 15, label="Procedural writing")
sky(c, 0, H - 232, W, 194, stars=60, seed=41); lantern(c, W - 80, H - 150, 1.0); lantern(c, W - 140, H - 120, .65, glow=False)
text(c, M, H - 70, "WRITING WORKSHOP", "In-B", 7.2, GOLD, track=1.6)
c.saveState(); c.setFillColor(white); c.setFont("Fr-B", 28); c.drawString(M - 1, H - 104, "Write the way home."); c.drawString(M - 1, H - 136, "A how-to from your kitchen."); c.restoreState()
col(c, M, H - 190, CW * .62, 44, [P("A procedural text explains how to do something in order. Students write one for a dish, a game or a routine from home, for a reader who has never seen it.", S("wd", "In-R", 10, 13.6, HexColor("#C9CEEA")))])
yy = H - 250
L5 = [P("The mentor text / abridged", h2), P("<b>How we make champurrado on the 24th</b><br/><i>You will need:</i> masa, water, milk, a tablet of chocolate, piloncillo, cinnamon, a wooden whisk.<br/><i>First,</i> dissolve the masa in cold water. <i>While</i> it rests, heat the milk with the cinnamon. <i>Then</i> add the chocolate and piloncillo and stir until they melt. <i>After that,</i> pour in the masa slowly, whisking the whole time. <i>Finally,</i> keep stirring on low heat until it is thick. Serve it hot, in small cups. <i>Warning:</i> it burns on the bottom if you stop stirring.", S("mt", "In-R", 8.8, 12.2, INK, leftIndent=6)),
      P("Notice the structure", h2), BL(["A title that says what and when.", "A materials list before the steps.", "Order words: <i>first, while, then, after that, finally</i>.", "One warning: what goes wrong."]),
      P("Plan before you draft", h2), P("Choose a dish, a game or a routine. List the materials. Number the steps on scrap paper. Decide where the warning goes.")]
col(c, M, 60, cw2, yy - 60, L5)
R5 = [P("Your writing task", h2), P("Write 120–180 words. Include a title, a materials list, at least five ordered steps with four different order words, and one warning. The reader has never seen this before, so explain the words they will not know in parentheses."),
      P("A frame you can expand", h2), P("<b>Title:</b> How we ____ on ____.<br/><b>You will need:</b> ____, ____, ____.<br/><b>First,</b> ____. <b>Then,</b> ____. <b>While</b> ____, ____. <b>After that,</b> ____. <b>Finally,</b> ____.<br/><b>Warning:</b> ____.", S("fx", "In-R", 9, 13.4, INK, leftIndent=6)),
      P("Revise for the reader", h2), BL(["Circle every order word. Are there at least four different ones?", "Find one word from your home language. Is it explained in parentheses?", "Read the steps to a partner who follows them with their hands. Where did they stop?"]),
      P("Partner conference", h2), P("Reader says: “I could follow steps ____ to ____. I got lost at ____.” Writer fixes the one step.")]
col(c, M + cw2 + 18, 60, cw2, yy - 60, R5)
endpage(c)

# ---------------- 16 VISUAL LITERACY ----------------
chrome(c, "Visual literacy", 16, label="Classroom data")
y = headline(c, H - 96, "A chart needs a careful reader.", "Hours of daylight on December 21, the shortest day in the Northern Hemisphere, in eight cities many Mississippi students know. Values are calculated from latitude, rounded to the nearest five minutes.", "Visual literacy · Real data")
# chart
chx, chy, chw, chh = M, y - 262, CW * .58, 246
rect(c, chx, chy, chw, chh, MIST, r=3)
text(c, chx + 12, chy + chh - 16, "DAYLIGHT ON DECEMBER 21 (HOURS : MINUTES)", "In-B", 7.2, GOLDINK, track=1.2)
data = []
for name, lat in CITIES:
    hrs = daylight_hours(lat); mins = int(round(hrs * 60 / 5) * 5); data.append((name, lat, mins))
mx = max(d[2] for d in data); bar_h = 18; gap = 6; bx0 = chx + 150; bwmax = chw - 150 - 60
for i, (name, lat, mins) in enumerate(data):
    by = chy + chh - 38 - i * (bar_h + gap) - bar_h
    text(c, bx0 - 6, by + 5, name.split(",")[0], "In-S", 8, NAVY, "r")
    text(c, bx0 - 6, by - 3, f"{lat:.1f}°N", "In-R", 6.4, MUTED, "r")
    rect(c, bx0, by, bwmax * mins / mx, bar_h, NAVY if i == 0 else PINE, r=2)
    text(c, bx0 + bwmax * mins / mx + 5, by + 5, f"{mins // 60}:{mins % 60:02d}", "In-B", 8.2, INK)
text(c, chx + 12, chy + 8, "Calculated from latitude with standard sunrise/sunset geometry (sun at −0.833°). Source and method on page 25.", "In-R", 6.6, MUTED)
rx = M + chw + 16; rw = CW - chw - 16
col(c, rx, chy, rw, chh, [P("Read the information", h2)] + NL(["Which city has the least daylight? The most?", "How much more daylight does Caracas have than Laurel? Give hours and minutes.", "What do the cities with the most daylight have in common? Look at the small gray number."]) + [P("Question the data", h2)] + NL(["The chart is for December 21. Would the order change on June 21? Explain.", "The values are rounded to five minutes. Could two cities really be tied?"]))
yy = chy - 16
col(c, M, 60, cw2, yy - 60, [P("Say what the chart supports", h2), P("Finish each sentence with evidence from the chart."), BL(["“A student from ____ will notice that in Mississippi the sun sets ____ in December.”", "“The closer a city is to the equator, the ____.”", "“The difference between ____ and ____ is about ____ minutes, which is ____.”"]), P("Language support", h2), P("<b>Compare:</b> <i>____ has more / less daylight than ____.</i><br/><b>Explain:</b> <i>This is because ____ is closer to / farther from the equator.</i><br/><b>Hedge:</b> <i>The chart suggests ____, but it does not show ____.</i>", S("ls2", "In-R", 9, 13.2, INK))])
col(c, M + cw2 + 18, 60, cw2, yy - 60, [P("Teacher note", h2), P("Students arriving from the tropics often say Mississippi winters feel “dark.” This chart turns a feeling into a measurable difference, which is the move we want in every content class. The gap between Laurel and Caracas on December 21 is well over an hour."), P("Extension / the longest night", h2), P("Have students look up sunrise and sunset for their birthplace on December 21 from a reliable almanac or weather service, calculate the day length, and add it to the chart. Then write a two-sentence comparison using <i>although</i>."), P("Home-language bridge", h2), P("<i>daylight</i> = luz del día · <i>equator</i> = ecuador · <i>latitude</i> = latitud. Ask which word is nearly the same in both languages and which is not.", S("hb", "In-R", 8.8, 12, PINE))])
endpage(c)

# ---------------- 17 COMMUNITY: STUDENT PUBLISHING ----------------
chrome(c, "Student publishing project", 17, label="Publishing")
sky(c, 0, H - 232, W, 194, stars=80, seed=51); skyline(c, -6, H - 232, W + 12, seed=53, scale=.6)
text(c, M, H - 70, "STUDENT PUBLISHING PROJECT", "In-B", 7.2, GOLD, track=1.6)
c.saveState(); c.setFillColor(white); c.setFont("Fr-B", 30); c.drawString(M - 1, H - 104, "Build the Home Language Wall."); c.restoreState()
col(c, M, H - 190, CW * .66, 56, [P("Essential question: what does our school sound like? Students publish a wall of phrases their families use, each with a translation, a pronunciation guide and a sentence about when it is said.", S("pd", "In-R", 10, 13.6, HexColor("#C9CEEA")))])
yy = H - 250
L6 = [P("The product", h2), P("One card per student, 5 × 8 inches, posted in a public hallway before break. Each card has: the phrase in the home language, the English meaning, a pronunciation line in plain letters, and two sentences: <i>We say this when ____. I chose it because ____.</i> Students who speak only English contribute a family phrase in English (every family has them)."),
      P("The process / three sessions", h2),
      P("<b>Session 1 / Collect:</b> students bring one phrase from home (the family page on 18 helps). Pairs check that the meaning is clear to a stranger.", bodyS),
      P("<b>Session 2 / Draft:</b> write the card. Say the pronunciation line to a partner who has never heard the language; revise until they can say it back.", bodyS),
      P("<b>Session 3 / Publish:</b> final cards, one color per language family if you like. Add a map pin for where the phrase comes from.", bodyS),
      P("Design requirements", h2), BL(["Phrase large enough to read from six feet.", "English meaning in a complete sentence, not a single word.", "The student's first name only; no other personal information.", "A small card that says who to ask if you want to learn it."])]
col(c, M, 60, cw2, yy - 60, L6)
R6 = [P("Language requirements", h2), P("Every card uses at least one structure from the Language workshop: <i>used to</i>, <i>now</i>, or a time connector. Example: <i>We used to say this only at home. Now my friends say it too.</i>"),
      P("Assess the thinking", h2), P("Ask each student: What do you notice on the wall? Which phrase is closest to one you know? What surprised you? Score the explanation, not the decoration."),
      P("Name it, compare it, carry it", h2), P("The wall is the routine made public. <b>Name it</b> (the phrase). <b>Compare it</b> (the translation and the moment it is used). <b>Carry it</b> (two sentences in academic English with a grammar target)."),
      P("Make it last", h2), P("Photograph the wall. In January, choose ten phrases and record students saying them for a short audio tour. The hub's Listening & Speaking Studio has the format.")]
e1 = col(c, M + cw2 + 18, 60, cw2, yy - 60, R6); by = max(e1 - 14, 150)
rect(c, M + cw2 + 18, by - 90, cw2, 90, PINE, r=3)
col(c, M + cw2 + 30, by - 82, cw2 - 24, 76, [P("AN AUDIENCE GIVES THE WORK PURPOSE", S("au", "In-B", 7.2, 10, GOLDLT)), Spacer(1, 2), P("Invite the front office, the counselors and one administrator to the wall before break. Students stand by their cards and teach the phrase. Ten minutes; it changes how the building hears them.", S("aub", "In-R", 8.4, 11, white))])
endpage(c)

# ---------------- 18 FAMILY CONNECTION ----------------
chrome(c, "Family connection", 18, label="English + Spanish")
y = headline(c, H - 96, "A conversation, then a card.", "Optional take-home page · Students interview a family member about one December memory. Families may answer in any language; students bring the phrase for the Home Language Wall.", "Family connection · English + Spanish")
rect(c, M, y - 22, cw2, 20, NAVY); text(c, M + 10, y - 16, "ENGLISH", "In-B", 7.6, white, track=1.4)
rect(c, M + cw2 + 18, y - 22, cw2, 20, PINE); text(c, M + cw2 + 28, y - 16, "ESPAÑOL", "In-B", 7.6, white, track=1.4)
EN = [P("Dear families,", body), Spacer(1, 4), P("This month, students are learning how their first language helps them learn English. They are collecting one phrase each family uses, with a short explanation, for a display at school. There are no wrong answers and no required holidays."),
      P("An optional conversation", h2), P("Ask your student to write down your answers, in any language."), NL(["What is something our family says in December that other families might not say?", "When do we say it? Who taught it to you?", "What did you use to do in December when you were my age? What do we do now?", "Is there a tradition you would like us to start?"]),
      P("A simple response", h2), P("Your student will bring home a card that says: <i>We say ____ when ____.</i> If the meaning is not right, please tell them. They will fix it."),
      P("Student reflection", h2), P("One thing I learned from my family: ____.")]
ES = [P("Estimadas familias:", es), Spacer(1, 4), P("Este mes, los estudiantes están aprendiendo cómo su primer idioma les ayuda a aprender inglés. Cada uno recopila una frase que su familia usa, con una breve explicación, para una exhibición en la escuela. No hay respuestas incorrectas ni fiestas obligatorias.", es),
      P("Una conversación opcional", h2p), P("Pida a su estudiante que anote sus respuestas, en cualquier idioma.", es), NL(["¿Qué decimos en nuestra familia en diciembre que otras familias quizá no digan?", "¿Cuándo lo decimos? ¿Quién se lo enseñó a usted?", "¿Qué solía hacer usted en diciembre cuando tenía mi edad? ¿Qué hacemos ahora?", "¿Hay una tradición que le gustaría que empezáramos?"], num),
      P("Una respuesta sencilla", h2p), P("Su estudiante traerá una tarjeta que dice: <i>Decimos ____ cuando ____.</i> Si el significado no está bien, dígaselo. Lo corregirá.", es),
      P("Reflexión del estudiante", h2p), P("Algo que aprendí de mi familia: ____.", es)]
e1 = col(c, M, 60, cw2, y - 30 - 60, EN); e2 = col(c, M + cw2 + 18, 60, cw2, y - 30 - 60, ES); by = max(min(e1, e2) - 16, 150)
rect(c, M, by - 96, CW, 96, MIST, r=3)
text(c, M + 14, by - 16, "THE CARD YOUR STUDENT WILL MAKE  ·  LA TARJETA QUE HARÁ SU ESTUDIANTE", "In-B", 7.2, GOLDINK, track=1.2)
c.saveState(); c.setStrokeColor(RULE); c.setLineWidth(.6)
for i, lab in enumerate(["Phrase / Frase:", "Means / Significa:", "Say it / Se pronuncia:", "We say it when / Lo decimos cuando:"]):
    ly = by - 36 - i * 16; text(c, M + 14, ly, lab, "In-S", 8.2, NAVY); c.line(M + 170, ly - 2, W - M - 14, ly - 2)
c.restoreState()
endpage(c)

# ---------------- 19 TEACHER PLANNER: FULL LESSON ----------------
chrome(c, "Teacher planner", 19, label="90-minute block")
y = headline(c, H - 96, "A complete 90-minute block.", "Shared goal: explain how a tradition changed over time, using one <i>used to / now</i> pair, one time connector and one detail from a text. Built for the EL block; adaptable to any content class.", "Teacher planner · Full lesson")
blocks = [("00–08", "Notice + name", "Show the window art on page 7. Ask: what do you call this where you come from? Collect words on the board in every language. One student explains a pattern they see.", SLATE),
          ("08–20", "Words + model", "Teach <i>used to</i> and <i>now</i> with the Pine Street pair (page 11). Say it, write it, compare it with a home language. Every student says one <i>used to / now</i> pair to a partner.", PINE),
          ("20–40", "Read + mark", "Read <i>The Window on Pine Street</i> aloud; students follow and mark the section numbers. Second read in pairs: find the sentence that shows the change. Answer A1–A3 on page 8.", NAVY),
          ("40–55", "Compare evidence", "Pairs complete the change chain (page 8, B). Share: what used to happen, what happens now, which connector joins them. Teacher writes three class sentences.", RUST),
          ("55–75", "Write + rehearse", "Each student writes a paragraph: a tradition that changed, theirs or Pine Street's. Requirements: one <i>used to / now</i> pair, one connector, one detail from the text or their own experience. Partner reads it aloud; writer revises one sentence.", PINE),
          ("75–85", "Speak", "Volunteers read a paragraph; the class names the pair and the connector they heard. Listeners write one sentence beginning <i>Like ____, my family ____.</i>", SLATE),
          ("85–90", "Exit + next step", "Exit ticket: <i>Although ____, ____.</i> Collect. Tomorrow: the listening script (page 9).", GOLDINK)]
yy = y - 6
for t, n, d, colr in blocks:
    rect(c, M, yy - 56, 52, 52, colr, r=3); text(c, M + 26, yy - 24, t, "In-B", 8.4, white, "c"); text(c, M + 26, yy - 38, "MIN", "In-S", 6, GOLDLT, "c")
    text(c, M + 64, yy - 14, n, "In-B", 9.6, NAVY)
    col(c, M + 64, yy - 56, CW - 64, 38, [P(d, bodyS)])
    yy -= 62
col(c, M, 50, CW, yy - 50, [P("<b>Differentiation inside the block.</b> Emerging: the planning card and the Spanish bridge stay on the desk; paragraph may be four sentences with a drawing. Progressing: paragraph of six or more sentences with two connectors. Extension: add a sentence that begins <i>Unlike ____</i>. <b>Materials:</b> pages 7, 8, 11 printed; the board; a timer. <b>Evidence:</b> the paragraph and the exit ticket.", small)])
endpage(c)

# ---------------- 20 TEACHER PLANNER: 15 LESSONS ----------------
chrome(c, "Teacher planner", 20, label="Three weeks")
y = headline(c, H - 96, "Fifteen lessons. Three weeks.", "Use these fifteen lessons between Thanksgiving and winter break. Adjust to your calendar; the lessons are numbered, not dated.", "Teacher planner · Month map")
cycles = [("WEEK 1 / Then and now", SLATE, [("01", "Name it, compare it, carry it", "Teach the routine (pp. 4–5) on one term from your content."), ("02", "The 90-minute block", "Page 19 in full, or split across two days."), ("03", "Reading response", "Page 8, A–C; language support frames."), ("04", "Grammar: used to / now", "Page 11, A–D; error hunt."), ("05", "Vocabulary + word families", "Page 12; Friday quiz on six words.")]),
          ("WEEK 2 / Voices", PINE, [("06", "Listening: Neighborhood Hour", "Page 9; two readings, note grid."), ("07", "Speaking: sixty seconds", "Page 10, Rounds 1 and 2; record."), ("08", "December with care", "Page 6 light inquiry; Human Rights Day on the 10th."), ("09", "The Second Key, read", "Page 13; mark the turning point."), ("10", "The Second Key, analyze", "Page 14, A–D; the <i>although</i> sentence.")]),
          ("WEEK 3 / Publish", RUST, [("11", "Writing: a how-to from home", "Page 15, plan and draft."), ("12", "Visual literacy: daylight", "Page 16; add your birthplace."), ("13", "Home Language Wall, sessions 1–2", "Page 17; family page (18) came home in week 2."), ("14", "Student check", "Pages 21–22; rubric for the writing."), ("15", "Publish + reflect", "Wall opens; Round 2 recordings; the five-day challenge (p. 26) goes home.")])]
yy = y - 4; cw4 = (CW - 20) / 3
for i, (t, colr, items) in enumerate(cycles):
    bx = M + i * (cw4 + 10); rect(c, bx, yy - 22, cw4, 22, colr, r=3); text(c, bx + 10, yy - 15, t, "In-B", 7.6, white, track=1)
    ly = yy - 30
    for n, h_, d in items:
        text(c, bx, ly - 12, n, "Fr-B", 15, colr); text(c, bx + 24, ly - 10, h_, "In-B", 8.4, NAVY)
        col(c, bx + 24, ly - 50, cw4 - 24, 36, [P(d, S("ld", "In-R", 8.6, 11.4, MUTED))]); ly -= 66
yy = yy - 30 - 5 * 66 - 6
labelbox(c, M, yy - 118, CW, 118, "Suggested ELP connections (not an official alignment)", [P("<b>Domains:</b> reading informational and literary text (pp. 7, 13); listening (p. 9); speaking (p. 10); writing procedural and explanatory text (pp. 15, 19). <b>Language:</b> past-habit and present forms, time connectors, comparison language, academic vocabulary across content areas. <b>Growth evidence:</b> the week-1 paragraph, the week-3 how-to and the student check give three dated samples for a portfolio; keep the Round 1 and Round 2 recordings for speaking. <b>Short weeks:</b> if you have fewer than fifteen days, teach 01, 02, 04, 06, 07, 09, 10, 11, 13 and 15 in that order.", bodyS)])
endpage(c)

# ---------------- 21 STUDENT CHECK ----------------
chrome(c, "Student check", 21, label="Original practice")
y = headline(c, H - 96, "Can you explain what changed?", "Name: ____________________ &nbsp; Date: __________<br/>This classroom check is not an official ELPA21 task or score. Keep the text available.", "Student check · Original practice", size=25)
rect(c, M, y - 92, CW, 86, MIST, r=3)
col(c, M + 12, y - 86, CW - 24, 76, [P("<b>Read:</b> A school posted this notice in November: “Students who arrive before 7:30 must wait outside the front doors.” In December, after three weeks of a student-run study room, the notice changed: “Students may enter the library at 7:00. A student monitor opens the door.” The principal said the change happened because attendance in first period improved and because a teacher trusted a student with a key.", S("ck", "In-R", 9.2, 12.6, INK))])
yy = y - 104
A7 = [P("A / Read and reason", h2)] + NL(["What did the November notice say?", "What changed in December? Quote the new rule.", "Give the two reasons the principal gave.", "The second reason mentions a key. Which story in this issue does it connect to?"]) + [
      P("B / Use language", h2)] + NL(["Write one sentence about the school using <i>used to</i> and <i>now</i>.", "Join these with a connector: <i>Attendance improved. The rule changed.</i>", "Write one sentence that begins with <i>Although</i>."]) + [
      P("C / Explain a choice", h2), P("Choose <b>one</b> word: <i>monitor, trusted, attendance</i>. Name it in your home language, then write one sentence in English that shows you understand it in this context. (2 points)")]
B7 = [P("D / Listen and respond", h2), P("Teacher reads the Amara interview (page 9) once more. Answer:"), NL(["How many languages are on the lanterns this year?", "Why does Amara like the lantern about watching movies?"]),
      P("E / Write", h2), P("In 80–120 words, explain how the study room changed the school. Use: one <i>used to / now</i> pair, one time connector, one detail from the notice and one reason."),
      P("F / Speak (with a partner or recorded)", h2), P("In 45 seconds, describe a tradition or routine that changed. Use a connector. (Rubric, page 22.)"),
      P("Teacher recording", h2), P("Reading A: ____ / 4 &nbsp; Language B: ____ / 3 &nbsp; Word C: ____ / 2<br/>Listening D: ____ / 2 &nbsp; Writing E: rubric ____ &nbsp; Speaking F: rubric ____", S("tr", "In-R", 8.8, 13, INK)), Spacer(1, 4), P("Domain balance: reading, language, listening, writing and speaking appear in that order so that the scores can be read beside ELPA21 domain reports. Not an official score.", small)]
e1 = col(c, M, 60, cw2, yy - 60, A7); e2 = col(c, M + cw2 + 18, 60, cw2, yy - 60, B7); by = min(e1, e2) - 16
if by > 150:
    text(c, M, by - 10, "E / WRITE HERE", "In-B", 7.2, GOLDINK, track=1.2)
    c.saveState(); c.setStrokeColor(RULE); c.setLineWidth(.6); ly = by - 28
    while ly > 56: c.line(M, ly, W - M, ly); ly -= 16
    c.restoreState()
    note(50)
endpage(c)

# ---------------- 22 RUBRIC ----------------
chrome(c, "Teacher desk", 22, label="Classroom rubric")
y = headline(c, H - 96, "Describe growth, then name the next move.", "Use the rubric for the how-to (page 15), the paragraph (page 19) and the check (page 21). These local descriptors do not replace official proficiency levels.", "Teacher desk · Classroom rubric", size=25)
rows = [["CRITERION", "1 / STARTING", "2 / DEVELOPING", "3 / EXTENDING"],
        ["MEANING", "Names the change or tradition.", "Explains what changed and gives one reason.", "Explains the change, the cause and what it shows, with a comparison."],
        ["EVIDENCE", "Refers to the text or experience in general.", "Uses one specific detail, quoted or paraphrased.", "Uses two or more details and connects them."],
        ["STRUCTURE", "Ideas appear in a list.", "Events in order with one connector.", "Clear order with several connectors and a conclusion."],
        ["LANGUAGE", "Uses <i>now</i> or a past form; errors can block meaning.", "Uses <i>used to / now</i> correctly; errors rarely block meaning.", "Uses <i>used to / now</i>, <i>although</i> and precise vocabulary with control."]]
tdata = [[Paragraph(x, S("rc", "In-B" if r == 0 else "In-R", 7.6 if r == 0 else 8.4, 10 if r == 0 else 11, white if r == 0 else INK)) for x in row] for r, row in enumerate(rows)]
t = Table(tdata, colWidths=[78, (CW - 78) / 3, (CW - 78) / 3, (CW - 78) / 3])
t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), NAVY), ("BACKGROUND", (0, 1), (0, -1), MIST), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -1), .5, RULE), ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6), ("LEFTPADDING", (0, 0), (-1, -1), 7)]))
w_, h_ = t.wrap(CW, 300); t.drawOn(c, M, y - 6 - h_)
yy = y - 6 - h_ - 14
col(c, M, 60, cw2, yy - 60, [P("Use the descriptors carefully", h2), P("Mark each criterion separately. A student can have strong meaning and developing English control; record the growth, then set one language target. Score the paragraph and the how-to with the same rubric so December gives you two comparable samples."),
    P("Speaking and listening", h2), P("For speaking, listen for the message first, then the structure. Record the result in the Teacher recording line on page 21.")])
col(c, M + cw2 + 18, 60, cw2, yy - 60, [P("Student self-check", h2), P("<i>My strongest row was ____.</i><br/><i>The support that helped me was ____.</i><br/><i>Next time I will ____.</i>", S("sc", "In-R", 9.2, 13.6, INK)),
    P("Feedback formula", h2), P("Name the move the student made, cite one place it worked, give one next step. “You used <i>used to</i> and <i>now</i> in the first sentence; that showed the change clearly. Next, join two sentences with <i>after</i>.”"),
    P("Reteach signal", h2), P("Three or more students at level 1 on the same row means a ten-minute mini-lesson tomorrow on that row, with the page-11 sentences as the model.", bodyS)])
gy = 50
text(c, M, gy + 112, "DECEMBER GROWTH LOG  ·  ONE ROW PER STUDENT, THREE DATED SAMPLES", "In-B", 7.2, GOLDINK, track=1.2)
gl = [[Paragraph(x, S("gl", "In-B", 7.4, 9.6, white)) for x in ["Student", "Wk 1 paragraph (M/E/S/L)", "Wk 3 how-to (M/E/S/L)", "Check, p. 21", "Next language target"]]] + [[Paragraph("", small)] * 5 for _ in range(4)]
gt = Table(gl, colWidths=[86, (CW - 86) * .25, (CW - 86) * .25, (CW - 86) * .16, (CW - 86) * .34], rowHeights=[18] + [21] * 4)
gt.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), NAVY), ("LINEBELOW", (0, 0), (-1, -1), .5, RULE), ("LEFTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
_, gh = gt.wrap(CW, 200); gt.drawOn(c, M, gy + 104 - gh)
endpage(c)

# ---------------- 23 ANSWER KEY 1 ----------------
chrome(c, "Teacher desk", 23, label="Answer key 1")
y = headline(c, H - 96, "Read for meaning.\nRespond with evidence.", "Accept accurate paraphrases. Open-response samples illustrate reasoning; students do not need to reproduce the wording.", "Teacher desk · Answer key", size=25)
K1 = [P("Page 8 / The Window on Pine Street", h2), NL(["To walk from house to house with lanterns and song, as in the posadas; Luis doubted it because no one here would know the song [2].", "No open flames on the porch [3].", "He asked the landlord by email about battery lanterns; the landlord said yes. Quote: “The landlord wrote back the same day: yes.” [3]", "Mrs. Patel (sweets, and she walked along); Mr. Boyd (a guitar) [5].", "The tradition's name became the Pine Street Walk, but the welcome, the open door, stayed the same [7]."]),
      P("<b>B:</b> eleven neighbors he did not know (0 known) · four doors · four languages.", bodyS),
      P("<b>C1:</b> Careful, responsible, wants to follow the rules. <b>C2:</b> Carmen started the tradition; her line states the theme; it returns the story to the idea of the door.", bodyS),
      P("<b>D1:</b> He gave a date and time, said neighbors did not have to do anything, and promised one song; a stranger needs to know what will happen and that there is no obligation. <b>D2:</b> The walk became shared; it was no longer one family's tradition.", bodyS),
      P("<b>E:</b> Email: greeting, clear question about battery lanterns, polite close. Flyer: date, time, what will happen, a line in a home language with a label.", bodyS)]
K2 = [P("Page 9 / Listening", h2), NL(["To explain a student-made December tradition at a school.", "The main hallway; the last Friday before break (opens at three).", "One sentence about a family tradition, in English and in a home language.", "Thirty-one; more than two hundred.", "No candles; nothing hanging below seven feet.", "The one about watching movies, because it shows everybody has a December, even without a holiday."]),
      P("<b>7:</b> Every student has something true to write about December, celebrated or not; detail: the movie lantern. <b>8:</b> Reasonable either way; strong answers note they solved the problem and kept the display.", bodyS),
      P("Page 11 / Grammar", h2), P("<b>A:</b> 1 used to celebrate / walks; 2 Before; 3 before (or after; accept either with a sensible order). <b>B samples:</b> After Luis read the lease, he wrote the email. When the neighbors opened their doors, the group sang one song. When the family from Vietnam arrived, they brought paper lanterns. <b>D:</b> 1 <i>used to</i>; 2 <i>When we moved here, we did not know anyone.</i> (fragment joined); 3 <i>Now I take the bus</i> (<i>used to</i> cannot describe a present habit).", bodyS),
      P("Page 12 / Vocabulary", h2), P("<b>A:</b> translation / translator · invitation / invited · a gathering. <b>B1:</b> The word for the shelter became the name of the tradition that asks for it (a word can name an object and an event). <b>B2:</b> Any reasoned example; accept a student who finds none and explains why.", bodyS)]
col(c, M, 50, cw2, y - 50, K1); col(c, M + cw2 + 18, 50, cw2, y - 50, K2)
endpage(c)

# ---------------- 24 ANSWER KEY 2 ----------------
chrome(c, "Teacher desk", 24, label="Answer key 2")
y = headline(c, H - 96, "Interpret. Compare.\nDecide what comes next.", "Use the keys to identify the next teaching move, not simply to mark a page complete.", "Teacher desk · Answer key", size=25)
K3 = [P("Page 14 / The Second Key", h2), NL(["Someone must open the room at seven; “You are here every morning anyway.”", "Zero, one, four; the room grows as word spreads.", "Coats on chairs, not tables; the window chair goes to whoever arrives first; no talking before 7:15.", "<i>Although</i>; she gives the Spanish word and asks for his, then uses a sentence about the cold and the lights: both true."]),
      P("<b>B5:</b> From a key she does not understand to a decision about who should have the next one. <b>B6:</b> She has become the person who welcomes others. <b>B7:</b> Dark window / the window seat as a reward / the lit houses as the example that teaches <i>although</i>.", bodyS),
      P("<b>C sample:</b> The story suggests that a key represents trust because Ms. Okafor gives it without instructions and Dayana passes the trust on by choosing Yusuf. <b>D8:</b> definition, comparison with Spanish, a concrete example; the example works because it shows two true things at once. <b>D9:</b> That Dayana will choose well, and probably whom.", bodyS),
      P("Page 16 / Visual literacy", h2), P(f"<b>1:</b> Laurel least ({data[0][2]//60}:{data[0][2]%60:02d}); Caracas most ({data[-1][2]//60}:{data[-1][2]%60:02d}). <b>2:</b> about {(data[-1][2]-data[0][2])//60}:{(data[-1][2]-data[0][2])%60:02d}. <b>3:</b> lower latitude, closer to the equator. <b>4:</b> Yes; in June higher latitudes have longer days, so the order would reverse. <b>5:</b> Rounding can hide small differences; a tie on the chart may not be a true tie.", bodyS)]
K4 = [P("Page 21 / Student check", h2), P("<b>A1:</b> Students arriving before 7:30 must wait outside. <b>A2:</b> “Students may enter the library at 7:00. A student monitor opens the door.” <b>A3:</b> First-period attendance improved; a teacher trusted a student with a key. <b>A4:</b> <i>The Second Key</i>. (4 points)", bodyS),
      P("<b>B5 sample:</b> Students used to wait outside; now they study in the library. <b>B6:</b> After attendance improved, the rule changed (or <i>Because</i>...). <b>B7:</b> Any correct <i>Although</i> sentence with two clauses. (3 points)", bodyS),
      P("<b>C:</b> 1 point for the home-language word, 1 for an English sentence that fits the context. <b>D:</b> nineteen; because it shows everybody has a December. (2 points) <b>E/F:</b> rubric, page 22.", bodyS),
      P("From an error to a next step", h2), P("<b>Evidence missing:</b> return to one paragraph, offer two details, and ask which supports the claim. <b>Connector missing:</b> model one sentence with <i>after</i>, then have the student join two of their own. <b>Home-language word with no English sentence:</b> the comparison happened; supply the frame and have them say it before writing it.", bodyS),
      P("Reading response", h2), P("Reasonable claims with evidence earn credit. The keys show one path, not the only one.", bodyS)]
col(c, M, 50, cw2, y - 50, K3); col(c, M + cw2 + 18, 50, cw2, y - 50, K4)
endpage(c)

# ---------------- 25 SOURCES ----------------
chrome(c, "Sources + issue notes", 25, label="Sources")
y = headline(c, H - 96, "Grounded resources.\nOriginal classroom work.", "A transparent guide to the sources behind the editorial guidance and to the materials created for this issue.", "Sources + issue notes", size=25)
S1 = [P("[1] English language proficiency", h2), P("<b>ELPA21.</b> The ELP Standards and the ELPA21 assessment system. Used for general domain language and purpose; the materials here are classroom practice, not official items. elpa21.org", bodyS),
      P("[2] Home language as an asset", h2), P("<b>Cummins, J. (1979).</b> Linguistic interdependence and the educational development of bilingual children. <i>Review of Educational Research</i>, 49(2). The basis for the claim that skills transfer across languages.", bodyS), P("<b>García, O., &amp; Wei, L. (2014).</b> <i>Translanguaging: Language, Bilingualism and Education.</i> Palgrave Macmillan. Informs the name-it / compare-it / carry-it routine.", bodyS),
      P("[3] Evidence-based practice", h2), P("<b>Baker, S., et al. (2014).</b> <i>Teaching Academic Content and Literacy to English Learners in Elementary and Middle School.</i> IES practice guide (NCEE 2014-4012). Recommendation 1 (academic vocabulary), 2 (oral and written language in content) and 3 (structured writing) shape the labs. ies.ed.gov/ncee/wwc", bodyS)]
S2 = [P("[4] Observances", h2), P("<b>United Nations.</b> Human Rights Day (December 10) and International Migrants Day (December 18): un.org/en/observances. Universal Declaration of Human Rights, 1948, Articles 2 and 26. Other dates on page 6 should be verified locally each year; several follow lunar calendars.", bodyS),
      P("[5] Daylight data, page 16", h2), P("Day length is calculated from latitude for the December solstice (solar declination −23.44°, sun center at −0.833° to include refraction), rounded to five minutes. Latitudes are the city centers. For a specific date and location, use a national weather service or almanac.", bodyS),
      P("Editorial and production notes", h2), P("All readings, scripts, items and art are original to EL Publishing. <i>The Window on Pine Street</i> and <i>The Second Key</i> are fiction; names and places are invented. The art is drawn in code, not photographed, so no real students or homes appear. Design: navy and gold, Fraunces and Inter.", bodyS),
      P("Scope and use", h2), P("Free for classroom use. Teachers may print and copy pages for students. Please keep the EL Publishing credit on copies and do not sell the material.", bodyS)]
col(c, M, 50, cw2, y - 50, S1); col(c, M + cw2 + 18, 50, cw2, y - 50, S2)
rect(c, M, 50, CW, 92, NAVY, r=3)
col(c, M + 14, 58, CW - 28, 78, [P("ON THE HUB THIS MONTH", S("oh", "In-B", 7.2, 10, GOLDLT)), Spacer(1, 3), P("<b>Today in EL</b> · a daily feed of EL articles and three curated picks. <b>Read Your Roster</b> · the ELPA21 level decoder. <b>Teaching the ELPT</b> · the 24-page special issue for the spring test. <b>The Long-Term EL Clinic</b> · twelve weeks on the academic register. <b>Monday Moves</b> · one two-minute move for every classroom teacher, every week. All free at radan55.github.io/everyteacher", S("ohb", "In-R", 9, 12.2, white))])
endpage(c)

# ---------------- 26 BACK COVER / CHALLENGE ----------------
sky(c, 0, 0, W, H, stars=160, seed=61); skyline(c, -10, 0, W + 20, seed=67, scale=.9)
lantern(c, W - 130, H - 190, 1.3)
text(c, M, H - 58, "EL PUBLISHING", "Fr-B", 22, white); text(c, M, H - 74, "DECEMBER 2026  ·  CLOSING CHALLENGE", "In-S", 7.4, GOLD, track=2)
c.saveState(); c.setFillColor(white); c.setFont("Fr-B", 40); c.drawString(M - 1, H - 150, "Carry the light"); c.drawString(M - 1, H - 194, "home."); c.restoreState()
col(c, M, H - 250, CW * .62, 44, [P("A five-day challenge for the last week before break. One move a day; each takes less than ten minutes.", S("bc", "In-R", 11, 15, GOLDLT))])
days = [("MONDAY", "NAME", "Say one school word in your home language to someone who does not speak it. Teach them to say it."),
        ("TUESDAY", "COMPARE", "Find one English word that looks like a word in your language. Decide if it is a true friend or a false one."),
        ("WEDNESDAY", "CARRY", "Use <i>although</i> in a sentence out loud, to a teacher, about something true."),
        ("THURSDAY", "LISTEN", "Ask a family member what they used to do in December. Write one sentence with <i>used to</i> and one with <i>now</i>."),
        ("FRIDAY", "LIGHT", "Put your sentence on the Home Language Wall, or in your notebook, and read it to one person.")]
yy = H - 290
for d, m, s_ in days:
    rect(c, M, yy - 50, CW * .66, 46, Color(1, 1, 1, alpha=.08), r=3)
    text(c, M + 10, yy - 20, d, "In-B", 7.2, GOLD, track=1.4); text(c, M + 10, yy - 36, m, "Fr-B", 12, white)
    col(c, M + 100, yy - 46, CW * .66 - 110, 40, [P(s_, S("dy", "In-R", 8.6, 11.4, white))]); yy -= 54
col(c, M, 140, CW * .62, 60, [P("Every language carries a light.<br/>Every student deserves a place to set it down.", S("close", "Fr-I", 14, 18, GOLDLT))])
text(c, M, 128, "MANY VOICES · ONE STORM", "In-B", 7.6, GOLD, track=2)
text(c, M, 112, "Next issue, January 2027: the ELPT countdown. radan55.github.io/everyteacher", "In-R", 8.4, HexColor("#C9CEEA"))
rect(c, W - M - 22, 20, 22, 14, GOLD); text(c, W - M - 11, 24, "26", "In-B", 7.6, NAVYDK, "c")
c.showPage()
c.save()
print("wrote", OUT)
