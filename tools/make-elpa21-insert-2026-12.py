#!/usr/bin/env python3
"""Build elpa21-insert-2026-12.pdf — the December classroom ELPA21 insert.

An 8-page pull-out for the December 2026 issue (The Language of Home): ELPA21-style
practice in all four domains for grades 9-12, a two-page teacher key with listening
scripts, and a take-home family interview in English and Spanish.

Designed for a black-and-white printer: black ink, light grey tints, no floods.
Run from the repo root:  python3 tools/make-elpa21-insert-2026-12.py
"""
import os, tempfile
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, Flowable, KeepTogether)
from fontTools.ttLib import TTFont as FTFont
from fontTools.varLib import instancer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "elpa21-insert-2026-12.pdf")
W, H = letter
M = 46

FD = tempfile.mkdtemp(prefix="insfonts")
def inst(src, name, **loc):
    f = FTFont(src); f.flavor = None
    axes = {a.axisTag: a.defaultValue for a in f["fvar"].axes}; axes.update(loc)
    p = os.path.join(FD, name + ".ttf")
    g = instancer.instantiateVariableFont(f, axes)
    for rec in g["name"].names:                      # ReportLab keys embedded fonts by name: make each instance unique
        if rec.nameID in (1, 3, 4, 6, 16): rec.string = "ELP" + name
    g.save(p); return p
FR = os.path.join(ROOT, "tools/fonts/Fraunces.ttf"); IN = os.path.join(ROOT, "tools/fonts/Inter.ttf")
FRI = os.path.join(ROOT, "fonts/fraunces-italic.woff2")
for nm, src, loc in [("Fr-X", FR, dict(wght=800, opsz=144, SOFT=0, WONK=0)), ("Fr-B", FR, dict(wght=700, opsz=36, SOFT=0, WONK=0)),
                     ("Fr-R", FR, dict(wght=400, opsz=14, SOFT=0, WONK=0)), ("Fr-I", FRI, dict(wght=500, opsz=36)),
                     ("In-R", IN, dict(wght=400)), ("In-S", IN, dict(wght=600)), ("In-B", IN, dict(wght=700)), ("In-X", IN, dict(wght=800))]:
    pdfmetrics.registerFont(TTFont(nm, inst(src, nm.replace("-", ""), **loc)))
pdfmetrics.registerFontFamily("In-R", normal="In-R", bold="In-B", italic="Fr-I", boldItalic="In-B")
pdfmetrics.registerFontFamily("Fr-R", normal="Fr-R", bold="Fr-B", italic="Fr-I", boldItalic="Fr-B")

INK = black; GREY = HexColor("#555555"); TINT = HexColor("#EDEDED"); RULE = HexColor("#9A9A9A"); MID = HexColor("#BDBDBD")

def S(name, font, size, lead, color=INK, **kw):
    return ParagraphStyle(name, fontName=font, fontSize=size, leading=lead, textColor=color, **kw)
body = S("body", "In-R", 10.6, 14.6, spaceAfter=5)
read = S("read", "Fr-R", 10.5, 14.3, spaceAfter=4)
small = S("small", "In-R", 8.8, 11.6, GREY)
q = S("q", "In-S", 10.5, 14, leftIndent=18, firstLineIndent=-18, spaceBefore=6, spaceAfter=2.5, keepWithNext=1)
opt = S("opt", "In-R", 10.3, 13.6, leftIndent=34, firstLineIndent=-16, spaceAfter=1)
optc = S("optc", "In-R", 10.3, 13.6, leftIndent=16, firstLineIndent=-16)
h1 = S("h1", "Fr-B", 21, 24, spaceAfter=2)
kick = S("kick", "In-X", 8.6, 11, GREY, spaceAfter=3)
h2 = S("h2", "In-X", 9.6, 12.5, spaceBefore=9, spaceAfter=4, keepWithNext=1)
dirs = S("dirs", "In-R", 10.2, 14, spaceAfter=6)
es = S("es", "Fr-I", 10.6, 14.4, GREY)
keyS = S("key", "In-R", 9.3, 12.6, spaceAfter=3)
keyH = S("keyH", "In-X", 8.8, 11.5, spaceBefore=7, spaceAfter=3, keepWithNext=1)
script = S("script", "Fr-R", 9.8, 13.4, leftIndent=8, spaceAfter=4)

def P(t, st=body): return Paragraph(t, st)

def tr(t):
    """Letter-space a small-caps label."""
    return t.upper()

class Lines(Flowable):
    def __init__(self, n, gap=21, width=None): super().__init__(); self.n, self.gap, self.w = n, gap, width
    def wrap(self, aw, ah): self.aw = self.w or aw; return self.aw, self.n * self.gap + 2
    def draw(self):
        c = self.canv; c.setStrokeColor(RULE); c.setLineWidth(.6)
        for i in range(self.n): c.line(0, self.n * self.gap - (i + 1) * self.gap + 2, self.aw, self.n * self.gap - (i + 1) * self.gap + 2)

class Band(Flowable):
    """Section header: black rule, domain name, task type, time."""
    def __init__(self, domain, task, mins): super().__init__(); self.d, self.t, self.m = domain, task, mins
    def wrap(self, aw, ah): self.aw = aw; return aw, 44
    def draw(self):
        c = self.canv; c.setFillColor(INK); c.rect(0, 40, self.aw, 3, stroke=0, fill=1)
        c.setFont("Fr-X", 25); c.drawString(0, 12, self.d)
        c.setFont("In-X", 8.4); c.setFillColor(GREY); c.drawRightString(self.aw, 26, tr(self.t))
        c.setFont("In-S", 8.8); c.drawRightString(self.aw, 13, self.m)
        c.setStrokeColor(RULE); c.setLineWidth(.6); c.line(0, 3, self.aw, 3)

class House(Flowable):
    """Line drawing for Compare Pictures. Variant 'A' or 'B'."""
    def __init__(self, v, w=250, h=178): super().__init__(); self.v, self.w, self.h = v, w, h
    def wrap(self, aw, ah): return self.w, self.h
    def draw(self):
        c = self.canv; A = self.v == "A"; w, h = self.w, self.h
        c.setLineWidth(1.1); c.setStrokeColor(INK); c.rect(0, 0, w, h, stroke=1, fill=0)
        c.setFillColor(TINT); c.rect(0, 0, w, 30, stroke=0, fill=1); c.line(0, 30, w, 30)          # ground
        hx, hy, hw, hh = 78, 30, 124, 70
        c.setFillColor(white); c.rect(hx, hy, hw, hh, stroke=1, fill=1)                            # house
        p = c.beginPath(); p.moveTo(hx - 10, hy + hh); p.lineTo(hx + hw / 2, hy + hh + 42); p.lineTo(hx + hw + 10, hy + hh); p.close()
        c.setFillColor(MID); c.drawPath(p, stroke=1, fill=1)
        c.setFillColor(white); c.rect(hx + 88, hy + hh + 14, 14, 26, stroke=1, fill=1)             # chimney
        if A:                                                                                     # smoke
            c.setLineWidth(.9)
            for i, r in enumerate((4, 5.5, 7)): c.circle(hx + 97 + i * 5, hy + hh + 48 + i * 10, r, stroke=1, fill=0)
            c.setLineWidth(1.1)
        dx = hx + 52
        if A: c.setFillColor(MID); c.rect(dx, hy, 20, 38, stroke=1, fill=1); c.setFillColor(INK); c.circle(dx + 15.5, hy + 19, 1.4, stroke=0, fill=1)
        else:                                                                                     # open door
            c.setFillColor(INK); c.rect(dx, hy, 20, 38, stroke=1, fill=1)
            c.setFillColor(MID); pp = c.beginPath(); pp.moveTo(dx, hy); pp.lineTo(dx - 12, hy - 5); pp.lineTo(dx - 12, hy + 34); pp.lineTo(dx, hy + 38); pp.close(); c.drawPath(pp, stroke=1, fill=1)
        wins = [(hx + 14, hy + 30), (hx + 88, hy + 30)] + ([] if A else [(hx + 51, hy + 76)])
        for (x, y) in wins:
            ww, wh = (22, 22) if y < hy + 60 else (22, 18)
            c.setFillColor(white); c.rect(x, y, ww, wh, stroke=1, fill=1); c.line(x + ww / 2, y, x + ww / 2, y + wh); c.line(x, y + wh / 2, x + ww, y + wh / 2)
        if A:                                                                                     # tree, left
            c.setFillColor(MID); c.rect(34, 30, 7, 18, stroke=1, fill=1)
            for i, s in enumerate((30, 23, 16)):
                t = c.beginPath(); y0 = 46 + i * 17; t.moveTo(37.5 - s, y0); t.lineTo(37.5, y0 + 26); t.lineTo(37.5 + s, y0); t.close()
                c.setFillColor(white); c.drawPath(t, stroke=1, fill=1)
        else:                                                                                     # mailbox, left
            c.setFillColor(MID); c.rect(36, 30, 4, 30, stroke=1, fill=1); c.setFillColor(white); c.roundRect(24, 58, 28, 16, 5, stroke=1, fill=1)
            c.line(52, 70, 52, 82); c.setFillColor(INK); c.rect(52, 76, 8, 6, stroke=0, fill=1)
        if A:                                                                                     # moon + snow
            c.setFillColor(MID); c.circle(218, 146, 13, stroke=1, fill=1); c.setFillColor(white); c.setStrokeColor(white); c.circle(224, 150, 12, stroke=1, fill=1); c.setStrokeColor(INK)
            c.setFillColor(INK)
            for (x, y) in [(20, 150), (48, 128), (70, 160), (110, 164), (150, 150), (180, 126), (232, 104), (212, 78), (16, 104), (60, 96), (236, 52), (190, 160), (132, 150), (22, 64)]:
                c.circle(x, y, 1.5, stroke=0, fill=1)
        else:                                                                                     # sun
            c.setFillColor(white); c.circle(216, 146, 12, stroke=1, fill=1)
            import math
            for k in range(8):
                a = k * math.pi / 4; c.line(216 + 16 * math.cos(a), 146 + 16 * math.sin(a), 216 + 23 * math.cos(a), 146 + 23 * math.sin(a))
        c.setFillColor(INK); c.setFont("In-X", 10); c.drawString(8, h - 16, "PICTURE " + self.v)

class Chart(Flowable):
    """Bar chart: approximate hours of daylight in Laurel, Mississippi."""
    DATA = [("December", 10.1), ("March", 12.0), ("June", 14.2), ("September", 12.2)]
    def __init__(self, w=300, h=170): super().__init__(); self.w, self.h = w, h
    def wrap(self, aw, ah): return self.w, self.h
    def draw(self):
        c = self.canv; x0, y0, pw, ph = 38, 30, self.w - 48, self.h - 56
        c.setFont("In-B", 9.4); c.setFillColor(INK); c.drawString(0, self.h - 11, "Hours of daylight on the 21st of the month, Laurel, Mississippi (approximate)")
        c.setLineWidth(.5); c.setStrokeColor(RULE); c.setFont("In-R", 8.2)
        for v in (0, 4, 8, 12, 16):
            y = y0 + ph * v / 16; c.line(x0, y, x0 + pw, y); c.setFillColor(GREY); c.drawRightString(x0 - 5, y - 3, str(v))
        c.setStrokeColor(INK); c.setLineWidth(1); c.line(x0, y0, x0 + pw, y0)
        bw = pw / 4 * .5
        for i, (m, v) in enumerate(self.DATA):
            x = x0 + pw / 4 * i + pw / 8 - bw / 2; bh = ph * v / 16
            c.setFillColor(MID); c.rect(x, y0, bw, bh, stroke=1, fill=1)
            c.setFillColor(INK); c.setFont("In-B", 9.6); c.drawCentredString(x + bw / 2, y0 + bh + 4, f"{v:.1f}")
            c.setFont("In-R", 9); c.drawCentredString(x + bw / 2, y0 - 12, m)
        c.saveState(); c.translate(9, y0 + ph / 2); c.rotate(90); c.setFont("In-R", 8.4); c.setFillColor(GREY); c.drawCentredString(0, 0, "hours"); c.restoreState()

def mc(n, stem, options):
    out = [P(f"<b>{n}.</b>&nbsp; {stem}", q)]
    cells = [P(f"<font name='In-B'>{chr(65 + i)}</font>&nbsp;&nbsp; {o}", optc) for i, o in enumerate(options)]
    longest = max(len(o) for o in options)
    cols = 4 if (longest <= 12 and len(options) == 4) else 2 if (longest <= 44 and len(options) == 4) else 1
    if cols == 1:
        out += [P(f"<font name='In-B'>{chr(65 + i)}</font>&nbsp;&nbsp; {o}", opt) for i, o in enumerate(options)]
    else:
        rows = [cells] if cols == 4 else [[cells[0], cells[1]], [cells[2], cells[3]]]
        t = Table(rows, colWidths=[(W - 2 * M - 18) / cols] * cols, hAlign="RIGHT")
        t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5), ("VALIGN", (0, 0), (-1, -1), "TOP")]))
        out.append(t)
    return KeepTogether(out)

def box(flowables, pad=8, tint=True, width=None):
    t = Table([[flowables]], colWidths=[width or (W - 2 * M)])
    t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), .8, INK), ("BACKGROUND", (0, 0), (-1, -1), TINT if tint else white),
                           ("LEFTPADDING", (0, 0), (-1, -1), pad + 2), ("RIGHTPADDING", (0, 0), (-1, -1), pad + 2),
                           ("TOPPADDING", (0, 0), (-1, -1), pad), ("BOTTOMPADDING", (0, 0), (-1, -1), pad)]))
    return t

def page_deco(c, doc):
    c.saveState(); n = doc.page
    c.setFont("In-X", 7.6); c.setFillColor(GREY)
    c.drawString(M, H - 30, "EL PUBLISHING  ·  THE DECEMBER ELPA21 INSERT  ·  GRADES 9–12")
    label = "TEACHER KEY · DO NOT COPY FOR STUDENTS" if n in (6, 7) else "Name ______________________________   Date ____________"
    c.setFont("In-B" if n in (6, 7) else "In-R", 8.2 if n in (6, 7) else 9); c.drawRightString(W - M, H - 30, label)
    c.setStrokeColor(RULE); c.setLineWidth(.5); c.line(M, 36, W - M, 36)
    c.setFont("In-R", 7.6); c.drawString(M, 24, "ELPA21-style classroom practice written by EL Publishing. These are not released test items.  ·  radan55.github.io/everyteacher")
    c.setFont("In-B", 9); c.setFillColor(INK); c.drawRightString(W - M, 24, f"{n} / 8")
    c.restoreState()

doc = BaseDocTemplate(OUT, pagesize=letter, leftMargin=M, rightMargin=M, topMargin=46, bottomMargin=44,
                      title="The December ELPA21 Insert · Grades 9–12", author="Richard A. Daniel, M.Ed. · EL Publishing",
                      subject="ELPA21-style classroom practice in four domains, themed to The Language of Home (December 2026)")
doc.addPageTemplates(PageTemplate(id="p", frames=[Frame(M, 44, W - 2 * M, H - 44 - 46, leftPadding=0, rightPadding=0, topPadding=4, bottomPadding=0)], onPage=page_deco))
F = []

# ---------------- page 1: cover + plan + Reading A ----------------
F += [P("SPECIAL CLASSROOM INSERT · DECEMBER 2026 · PULL OUT AND COPY", kick),
      P("The December ELPA21 Insert", S("cov", "Fr-X", 34, 36, spaceAfter=4)),
      P("Four domains in five short sessions before winter break, on the theme of this month's issue: <i>the language of home.</i>", S("dek", "Fr-R", 13.2, 18, spaceAfter=10))]
plan = [[P("<b>SESSION</b>", small), P("<b>DOMAIN</b>", small), P("<b>TASK TYPE</b>", small), P("<b>PAGE</b>", small), P("<b>MIN</b>", small)],
        ["1", "Reading", "Short paragraph · Informational passage", "1–2", "20"],
        ["2", "Listening", "Listen for information · Conversation · Lecture", "3", "15"],
        ["3", "Writing", "Editing · Reply to a classmate · Build a claim", "4", "25"],
        ["4", "Speaking", "Compare pictures · A visual and a claim", "5", "15"],
        ["5", "Home", "Family interview, then report back", "8", "10"]]
plan = [r if i == 0 else [P(x, S("pl", "In-R", 9.6, 12.4)) for x in r] for i, r in enumerate(plan)]
t = Table(plan, colWidths=[52, 70, 290, 50, 58])
t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, 0), .9, INK), ("LINEBELOW", (0, 1), (-1, -1), .4, RULE), ("BACKGROUND", (0, 0), (-1, 0), TINT),
                       ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4), ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
F += [t, Spacer(1, 12), Band("Reading", "Part A · Short paragraph", "about 6 minutes"),
      P("Read the paragraph. Then choose the best answer to each question.", dirs),
      box([P("Marisol's grandmother keeps a small notebook on the kitchen shelf. Every December, she writes down one thing each person "
             "in the family learned that year. Some entries are serious, like passing a driving test. Others are funny, like the year "
             "Marisol's brother learned not to microwave an egg. On the last night of the year, the family reads the whole list aloud. "
             "Marisol used to think the notebook was old-fashioned. Now she is the one who reminds everyone to add to it.", S("rb", "Fr-R", 11.6, 16.4))]),
      mc(1, "What is the notebook used for?", ["planning the family's December meals", "recording what each family member learned", "keeping the grandmother's recipes", "listing the gifts each person wants"]),
      mc(2, "Which word could replace <u>old-fashioned</u> in the paragraph?", ["expensive", "outdated", "private", "confusing"]),
      mc(3, "What does the last sentence show about Marisol?", ["She has changed her opinion of the tradition.", "She wants to write a book about her family.", "She is tired of reading the list aloud.", "She is older than her brother."]),
      PageBreak()]

# ---------------- page 2: Reading B ----------------
F += [Band("Reading", "Part B · Informational passage", "about 14 minutes"),
      P("Read the passage. Then answer questions 4–8.", dirs),
      P("The Shortest Day", S("rt", "Fr-B", 15, 18, spaceAfter=5)),
      P("<b>1</b>&nbsp;&nbsp;On or near December 21, people in the Northern Hemisphere experience the winter solstice, the day with the fewest hours "
        "of daylight in the year. In Laurel, Mississippi, the sun is up for only about ten hours that day. In June, it is up for more than fourteen.", read),
      P("<b>2</b>&nbsp;&nbsp;The cause is not distance. Many people believe Earth is farther from the sun in winter, but Earth is actually closest "
        "to the sun in early January. The real cause is tilt. Earth's axis leans about 23.5 degrees. In December, the northern half of the planet "
        "leans away from the sun, so sunlight strikes it at a lower angle and for fewer hours.", read),
      P("<b>3</b>&nbsp;&nbsp;Less daylight changes daily life. Streetlights turn on earlier. Some students leave for school and return home in near "
        "darkness. Sleep researchers say that morning light helps set the body's internal clock, so dark mornings can make it harder to feel alert.", read),
      P("<b>4</b>&nbsp;&nbsp;For thousands of years, communities have answered the dark with light. Families light candles, hang lanterns, or gather "
        "around a fire. After the solstice, each day is slightly longer than the one before. The darkest day is also the turning point.", read),
      mc(4, "What is the main idea of the passage?", ["Earth is closest to the sun in early January.", "The winter solstice is caused by Earth's tilt, and it affects how people live.", "Students should not travel to school in the dark.", "Families in every country celebrate the same winter traditions."]),
      mc(5, "According to the passage, why are December days short in the Northern Hemisphere?", ["Earth is farthest from the sun.", "The northern half of Earth leans away from the sun.", "The sun produces less light in winter.", "Earth spins faster in December."]),
      mc(6, "Which <b>two</b> effects of less daylight does the passage mention? Choose <b>two</b>. (2 points)", ["Streetlights turn on earlier.", "School starts later in the morning.", "Some students travel to and from school in near darkness.", "The weather becomes warmer."]),
      mc(7, "Which sentence from the passage corrects a common mistake?", ["“In June, it is up for more than fourteen.”", "“Many people believe Earth is farther from the sun in winter, but Earth is actually closest to the sun in early January.”", "“Streetlights turn on earlier.”", "“Families light candles, hang lanterns, or gather around a fire.”"]),
      P("<b>8.</b>&nbsp; Explain the last sentence of the passage. Use one detail from the passage. (2 points)", q),
      Lines(3, 17), PageBreak()]

# ---------------- page 3: Listening ----------------
F += [Band("Listening", "Three recordings · your teacher reads each one twice", "about 15 minutes"),
      P("Listen carefully. You may take notes in the box. Then choose the best answer. You will not see the words your teacher reads.", dirs),
      box([P("MY NOTES", S("nl", "In-X", 8, 10, GREY)), Spacer(1, 22)], tint=False, pad=4),
      P("RECORDING 1 · A SCHOOL ANNOUNCEMENT", h2),
      mc(1, "When do semester exams begin?", ["Monday, December 14", "Tuesday, December 15", "Thursday, December 17", "Friday, December 18"]),
      mc(2, "What time will school dismiss on exam days?", ["11:30", "12:30", "2:30", "3:00"]),
      mc(3, "What happens to a student who does not return a library book?", ["The student pays a fine.", "The student cannot take exams.", "No report card until the book is returned.", "The student loses the library card."]),
      P("RECORDING 2 · A CONVERSATION BETWEEN TWO STUDENTS", h2),
      mc(4, "Why will Amira sleep on the couch during the break?", ["Her room is being painted.", "She is giving her room to her aunt.", "Her cousins asked for her room.", "She likes the couch better."]),
      mc(5, "What is Amira most worried about?", ["cooking for nine people", "finding a place to study", "the long drive to Houston", "missing a semester exam"]),
      mc(6, "What do Amira and Deshawn agree to do?", ["study at Amira's apartment on Monday", "meet at the public library Monday at ten", "meet at the school library on Tuesday", "finish the lab report before break"]),
      P("RECORDING 3 · A SCIENCE TEACHER EXPLAINS", h2),
      mc(7, "What is the teacher mainly explaining?", ["why winter mornings are cold", "why you can see your breath in cold air", "how clouds move across the sky", "why smoke rises"]),
      mc(8, "According to the teacher, what is water vapor?", ["water in the form of a gas", "tiny drops of liquid water", "a kind of smoke", "very cold air"]),
      mc(9, "What is condensation?", ["a liquid changing into a gas", "a gas changing into a liquid", "a liquid changing into ice", "air becoming warmer"]),
      mc(10, "Which other example of the same process does the teacher give?", ["ice melting in a glass", "steam rising from soup", "a cold glass getting wet on the outside", "snow falling at night"]),
      PageBreak()]

# ---------------- page 4: Writing ----------------
F += [Band("Writing", "Editing · Reply to a classmate · Build a claim", "about 25 minutes"),
      P("PART A · CHOOSE THE WORDS THAT MAKE THE SENTENCE CORRECT", h2)]
ed = [("My family ______ tamales every December.", ["make", "makes", "making", "are make"]),
      ("Last winter, we ______ to my uncle's house in Jackson.", ["drive", "drove", "driven", "are driving"]),
      ("The kitchen was crowded ______ everyone wanted to help.", ["but", "because", "or", "so that"]),
      ("Which sentence is written correctly?", ["Me and my sister decorates the door.", "My sister and I decorate the door.", "My sister and me decorate the door.", "My sister and I decorates the door."])]
rows = []
for i, (stem, os_) in enumerate(ed):
    rows.append([P(f"<b>{i + 1}.</b>&nbsp; {stem}", S("eq", "In-S", 10.2, 13.4)),
                 P("&nbsp;&nbsp; ".join(f"<font name='In-B'>{chr(65 + j)}</font> {o}" for j, o in enumerate(os_)) if i < 3 else
                   "<br/>".join(f"<font name='In-B'>{chr(65 + j)}</font>&nbsp; {o}" for j, o in enumerate(os_)), S("eo", "In-R", 10, 13.6))])
t = Table(rows, colWidths=[262, 258]); t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -2), .4, RULE), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4), ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
F += [t, P("PART B · REPLY TO A CLASSMATE", h2),
      box([P("<b>From:</b> Tomás &nbsp;&nbsp; <b>Subject:</b> Winter traditions project", S("em", "In-R", 9.6, 13)),
           P("Hi! For our class project, I'm collecting traditions that families keep in winter. Does your family, or a family you know, have one? "
             "What do people do? Why do you think it matters to them? Thanks! — Tomás", S("em2", "Fr-R", 11, 15))], pad=6),
      Spacer(1, 4), P("Write a reply to Tomás. Answer <b>all three</b> of his questions. Write at least five sentences.", dirs), Lines(5, 19),
      P("PART C · BUILD A CLAIM", h2),
      P("<b>Question:</b> Should teachers give homework over winter break?", S("cq", "In-R", 10.6, 14, spaceAfter=3)),
      P("<b>Note 1:</b> Practice helps students remember skills after time away from school. &nbsp; <b>Note 2:</b> Students and families need time to rest and be together.", S("cn", "In-R", 9.8, 13.2, spaceAfter=4)),
      P("Write a paragraph. State your claim, give one reason, support it with one of the notes or your own experience, and end with a closing sentence.", dirs),
      P("<i>You may begin:</i> &nbsp;I believe teachers (should / should not) ______ because ______. For example, ______. That is why ______.", S("fr", "In-R", 9.6, 13, GREY, spaceAfter=3)),
      Lines(5, 19), PageBreak()]

# ---------------- page 5: Speaking ----------------
F += [Band("Speaking", "Compare pictures · A visual and a claim", "about 15 minutes · work with a partner"),
      P("PART A · COMPARE PICTURES", h2),
      P("Look at Picture A and Picture B. Tell your partner what is <b>the same</b> and what is <b>different</b>. Speak for 45 seconds. Name at least four differences.", dirs)]
pics = Table([[House("A"), House("B")]], colWidths=[260, 260]); pics.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("ALIGN", (1, 0), (1, 0), "RIGHT")]))
F += [pics, Spacer(1, 5),
      P("<i>You may say:</i> &nbsp;Both pictures show ______. &nbsp;In Picture A ______, but in Picture B ______. &nbsp;Another difference is ______. &nbsp;Picture A has ______, while Picture B has ______.", S("fr2", "In-R", 9.8, 13.6, GREY, spaceAfter=2)),
      P("PART B · A VISUAL AND A CLAIM", h2),
      P("Study the chart. Then read the two claims. For each claim, tell your partner whether the chart <b>supports</b> it or <b>does not support</b> it. Use numbers from the chart.", dirs)]
claims = [P("<b>Jamal says:</b> “Laurel gets about four more hours of daylight in June than in December.”", S("cl", "Fr-R", 11, 15, spaceAfter=8)),
          P("<b>Rosa says:</b> “March has the least daylight of the four months.”", S("cl2", "Fr-R", 11, 15, spaceAfter=10)),
          P("<i>You may say:</i> The chart (supports / does not support) the claim because ______ has ______ hours and ______ has ______ hours.", S("fr3", "In-R", 9.6, 13.2, GREY))]
t = Table([[Chart(), claims]], colWidths=[312, 208]); t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (1, 0), (1, 0), 14)]))
F += [t, Spacer(1, 6), P("PARTNER CHECK · CIRCLE ONE NUMBER IN EACH ROW", h2)]
rub = [["My partner…", "Not yet", "Some", "Yes"], ["answered every part of the task", "1", "2", "3"], ["used details from the pictures or numbers from the chart", "1", "2", "3"],
       ["spoke in complete sentences", "1", "2", "3"], ["was easy to understand", "1", "2", "3"]]
t = Table([[P(c_, S("rb2", "In-B" if i == 0 else "In-R", 9.6, 12.4)) for c_ in r] for i, r in enumerate(rub)], colWidths=[340, 60, 60, 60])
t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), .5, RULE), ("BACKGROUND", (0, 0), (-1, 0), TINT), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
F += [t, PageBreak()]

# ---------------- pages 6-7: teacher key ----------------
F += [Band("Teacher key", "Answers · scoring · listening scripts", "pages 6–7"),
      P("READING · PAGES 1–2", keyH),
      P("<b>1</b> B &nbsp;·&nbsp; <b>2</b> B &nbsp;·&nbsp; <b>3</b> A &nbsp;·&nbsp; <b>4</b> B &nbsp;·&nbsp; <b>5</b> B &nbsp;·&nbsp; <b>6</b> A and C (1 point each) &nbsp;·&nbsp; <b>7</b> B", keyS),
      P("<b>8</b> (2 points) A full answer explains that the solstice is the day with the least daylight <i>and</i> that the days begin to get longer after it, so the worst point is also where improvement starts. "
        "1 point for one of the two ideas. Sample: “The solstice has the fewest hours of daylight, but after it each day is slightly longer, so things start to get brighter.”", keyS),
      P("<b>Reading total: 10 points.</b> Language focus: cause and effect (<i>so, because</i>), correcting a misconception (<i>many people believe… but actually</i>).", keyS),
      P("LISTENING · PAGE 3", keyH),
      P("<b>1</b> B &nbsp;·&nbsp; <b>2</b> B &nbsp;·&nbsp; <b>3</b> C &nbsp;·&nbsp; <b>4</b> B &nbsp;·&nbsp; <b>5</b> B &nbsp;·&nbsp; <b>6</b> B &nbsp;·&nbsp; <b>7</b> B &nbsp;·&nbsp; <b>8</b> A &nbsp;·&nbsp; <b>9</b> B &nbsp;·&nbsp; <b>10</b> C &nbsp;&nbsp; <b>Listening total: 10 points.</b>", keyS),
      P("Read each script twice at a natural pace, with a short pause between readings. Give students a moment to read the questions first. For Recording 2, change your voice or ask a student to read one part.", keyS),
      P("Script 1 · School announcement", S("sh", "In-B", 9.4, 12.4, spaceBefore=4, spaceAfter=2)),
      P("Good morning, students. This is a reminder about the week before winter break. Semester exams begin on Tuesday, December 15, and end on Friday, December 18. "
        "On exam days, school will dismiss at 12:30, and buses will run at that time. The library will stay open until 3:00 for students who want a quiet place to study. "
        "Please return all library books by Thursday. Students with overdue books will not receive their report cards until the books are returned. Have a great day.", script),
      P("Script 2 · Conversation", S("sh2", "In-B", 9.4, 12.4, spaceBefore=4, spaceAfter=2)),
      P("<b>Deshawn:</b> Amira, are you going anywhere over the break?<br/>"
        "<b>Amira:</b> No, we're staying here. My aunt and my cousins are driving in from Houston, so there will be nine people in our apartment.<br/>"
        "<b>Deshawn:</b> Nine! Where is everybody going to sleep?<br/>"
        "<b>Amira:</b> That's the problem. I'm giving my room to my aunt, so I'll be on the couch. I don't mind, really. The hard part is studying. I have a chemistry project due the first day back.<br/>"
        "<b>Deshawn:</b> You could work at the public library. It's open every day except the 24th and 25th.<br/>"
        "<b>Amira:</b> That's a good idea. Want to meet there on Monday? You still owe me help with the lab report.<br/>"
        "<b>Deshawn:</b> Deal. Ten o'clock?<br/><b>Amira:</b> Ten o'clock.", script),
      P("Script 3 · A science teacher explains", S("sh3", "In-B", 9.4, 12.4, spaceBefore=4, spaceAfter=2)),
      P("Today's question: why can you see your breath on a cold morning? The air you breathe out is warm, and it carries water in the form of a gas called water vapor. "
        "You can't see water vapor. But when that warm, wet air meets the cold air outside, it cools quickly. Cold air cannot hold as much water vapor as warm air, so some of the vapor "
        "changes into tiny drops of liquid water. That change is called condensation. Those tiny drops are what you see. It is the same process that forms clouds, and it is the same reason "
        "a cold glass gets wet on the outside in summer. So the cloud in front of your face is not smoke, and it is not a gas. It is liquid water.", script),
      PageBreak(),
      Band("Teacher key", "Writing · speaking · using the scores", "continued"),
      P("WRITING · PAGE 4", keyH),
      P("<b>Part A:</b> 1 B (makes) &nbsp;·&nbsp; 2 B (drove) &nbsp;·&nbsp; 3 B (because) &nbsp;·&nbsp; 4 B. &nbsp; 1 point each.", keyS),
      P("<b>Part B, reply to a classmate (0–3).</b> 3: answers all three questions (a tradition, what people do, why it matters) in connected sentences; errors do not block meaning. "
        "2: answers two questions, or all three in very short or list-like sentences. 1: on topic, but only one question answered or meaning is often unclear. 0: blank, copied, or off topic.", keyS),
      P("<b>Part C, build a claim (0–3).</b> 3: clear claim, a reason, support from a note or experience, and a closing sentence. 2: claim and reason, but support or closing is missing. "
        "1: an opinion with no reason, or a reason with no clear claim. 0: blank, copied, or off topic. Either side of the question can earn full credit.", keyS),
      P("<b>Writing total: 10 points.</b> Sample claim: “I believe teachers should not give homework over winter break because students need rest. For example, my family travels to see relatives, "
        "and there is no quiet place to work. That is why a short reading list is better than a packet.”", keyS),
      P("SPEAKING · PAGE 5", keyH),
      P("<b>Part A, differences between the pictures:</b> moon in A, sun in B · snow falling in A, none in B · a tree in A, a mailbox in B · smoke from the chimney in A, none in B · "
        "the door is closed in A and open in B · two windows in A, three in B. <b>The same:</b> one house, a chimney, the same roof, the ground in front.", keyS),
      P("<b>Part B:</b> Jamal's claim is <b>supported</b>: 14.2 hours in June minus 10.1 hours in December is 4.1 hours, about four. Rosa's claim is <b>not supported</b>: "
        "March has 12.0 hours, and December has the least, 10.1.", keyS),
      P("<b>Scoring (0–3 for each part).</b> 3: completes the task with relevant detail in connected sentences; easy to understand. 2: completes most of the task; some short or halting answers. "
        "1: a few words or phrases on topic. 0: no response or not in English. Listen to four or five students each session; the partner check covers the rest.", keyS),
      P("The chart values are rounded estimates for Laurel's latitude, for classroom use.", small),
      P("USING THE SCORES", keyH),
      P("These tasks follow ELPA21 task types, but the points are classroom points, not ELPA21 scale scores or proficiency levels. Use them to choose the next three weeks of practice:", keyS)]
use = [["If the weak spot is…", "Try this in January", "On the hub"],
       ["Reading 6, 7 or 8 (evidence)", "Underline the sentence that proves each answer before choosing.", "Storm Reading Sets"],
       ["Listening 7–10 (academic talk)", "Two-column notes: term on the left, meaning on the right.", "Storm Listening Sets"],
       ["Writing B or C below 2", "Colour-code the parts of the task, then check each one off.", "Storm Writing Sets · Sentence-Frame Bank"],
       ["Speaking: short answers", "Thirty seconds of talk with a frame before any written answer.", "Storm Speaking Sets"]]
t = Table([[P(c_, S("u", "In-B" if i == 0 else "In-R", 9, 12)) for c_ in r] for i, r in enumerate(use)], colWidths=[150, 232, 138])
t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), .5, RULE), ("BACKGROUND", (0, 0), (-1, 0), TINT), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
F += [t, Spacer(1, 6),
      P("<b>Four lanes.</b> Newcomer: Reading A and Listening 1 only, with a partner who shares the home language; the speaking frames may be answered in single words. "
        "Emerging: all tasks, with the frames. Progressing: all tasks, frames covered. Challenge: after Reading B, write the claim a person might make from paragraph 3 and one piece of evidence the passage does <i>not</i> give.", keyS),
      PageBreak()]

# ---------------- page 8: take-home ----------------
F += [Band("Home", "Family interview · Entrevista familiar", "10 minutes at home · report back in class"),
      P("Ask an adult at home these six questions, in <b>any language</b>. Write short notes in any language. In class, you will report in English.", dirs),
      P("Hazle estas seis preguntas a un adulto en casa, en <b>cualquier idioma</b>. Escribe notas breves en cualquier idioma. En clase, vas a contarlo en inglés.", es), Spacer(1, 6)]
iv = [("What did you do in winter when you were my age?", "¿Qué hacías en invierno cuando tenías mi edad?"),
      ("What food reminds you of home?", "¿Qué comida te recuerda a tu hogar?"),
      ("What is one tradition you want our family to keep?", "¿Qué tradición quieres que nuestra familia conserve?"),
      ("What is a saying or proverb you heard as a child?", "¿Qué dicho o refrán escuchabas de niño o de niña?"),
      ("What was hard about school for you? What was good?", "¿Qué fue difícil para ti en la escuela? ¿Qué fue bueno?"),
      ("What do you hope I learn this year?", "¿Qué esperas que yo aprenda este año?")]
rows = [[P(f"<b>{i + 1}.</b>&nbsp; {a}<br/><font name='Fr-I' color='#555555'>{b}</font>", S("iq", "In-R", 10.2, 14)), Lines(2, 19)] for i, (a, b) in enumerate(iv)]
t = Table(rows, colWidths=[250, 270]); t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -1), .4, RULE), ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7), ("LEFTPADDING", (0, 0), (0, -1), 0)]))
F += [t, Spacer(1, 10), P("REPORT BACK · SPEAK FOR 45 SECONDS", h2),
      box([P("I interviewed my ______. &nbsp;When (he / she / they) was my age, ______. &nbsp;A food that reminds (him / her / them) of home is ______ because ______. "
             "&nbsp;One tradition (he / she / they) wants us to keep is ______. &nbsp;Something I did not know before is ______.", S("rf", "Fr-R", 11.4, 17))], pad=9),
      Spacer(1, 10),
      P("<b>To the family:</b> This interview is practice for your student's English test in the spring. Your home language helps. Please answer in the language you know best.", S("fam", "In-R", 9.8, 13.6)),
      P("<b>A la familia:</b> Esta entrevista es práctica para el examen de inglés de su estudiante en la primavera. El idioma del hogar ayuda. Por favor, responda en el idioma que mejor domina.", S("fam2", "Fr-I", 10.2, 14, GREY, spaceBefore=3))]

doc.build(F)
print("wrote", OUT)
