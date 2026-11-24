#!/usr/bin/env python3
"""Build the interactive edition of Christmas Around the World.

Reads the content straight out of tools/make-special-2026-12-world.py (the PDF
generator), so the web edition and the print edition say the same thing, and
writes el-special-2026-12-world-interactive.html from
tools/special-interactive.template.html.

  python3 tools/make-special-2026-12-world-interactive.py [--standalone DIR]
"""
import ast, json, pathlib, re, sys
from datetime import date

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
SRC = (HERE / "make-special-2026-12-world.py").read_text(encoding="utf-8")
TREE = ast.parse(SRC)

class Names(dict):
    def __missing__(self, k): return k

WANT = {"STOPS", "GREET", "DAYS", "WEEK", "COLOR", "SUBJ", "MOVES", "TL", "ed", "iv"}
V = {}
for n in TREE.body:
    if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name) and n.targets[0].id in WANT:
        V[n.targets[0].id] = eval(compile(ast.Expression(n.value), "x", "eval"), {"__builtins__": {}}, Names())
MC = {}
for n in ast.walk(TREE):
    if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in ("mc", "mc3"):
        MC.setdefault(n.lineno, []).append([ast.literal_eval(a) for a in n.args])
RUNS = []  # consecutive mc() calls, in page order, split where the numbering restarts
for ln in sorted(MC):
    for num, stem, opts in MC[ln]:
        if not RUNS or num == 1: RUNS.append([])
        RUNS[-1].append((stem, opts))
ELEM, READ, LISTEN, MATH, SCI, HIST = RUNS
assert [len(x) for x in RUNS] == [3, 7, 10, 12, 12, 9], [len(x) for x in RUNS]

COL = {"CRAN": "#9B2335", "GOLDINK": "#7A5F0E", "PINE": "#1F4D3A", "NAVY": "#1E2761", "INK": "#1F2330"}
DOM = {"Listening": "#1F4D3A", "Speaking": "#9B2335", "Reading": "#1E2761", "Writing": "#7A5F0E", "All four": "#1F2330"}
MEDAL = {"Las Posadas": 0, "The parol": 1, "Tamales at midnight": 2, "Las patinatas": 3, "The fanal": 4,
         "The twelve dishes": 5, "The crown of candles": 6, "Genna": 7}
WORDLANG = {"Las Posadas": "es-MX", "Tamales at midnight": "es-MX", "Las patinatas": "es-MX", "The crown of candles": "sv-SE"}
# a speaker only where the greeting is written in the language's own alphabet
CODE = {"Spanish": "es", "Portuguese": "pt", "French": "fr", "Tagalog": "fil", "Vietnamese": "vi", "German": "de",
        "Italian": "it", "Swedish": "sv", "Swahili": "sw"}
MON = {"Nov": 11, "Dec": 12}

def strings(a, b):
    out = []
    for line in SRC.split("\n")[a - 1:b]:
        out += [m.encode().decode("unicode_escape").encode("latin-1").decode("utf-8") if "\\" in m else m
                for m in re.findall(r'"((?:[^"\\]|\\.)*)"', line)]
    return out

def find(start):
    """The full string literal that begins with `start` (adjacent literals joined)."""
    for n in ast.walk(TREE):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and n.value.startswith(start):
            return n.value
    raise KeyError(start)

def clean(t):
    t = re.sub(r"<font[^>]*>|</font>", "", t).replace("<br/>", "<br>").replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", t).strip()

def items(run, key, why=None):
    out = []
    for i, (stem, opts) in enumerate(run):
        k = key[i]
        a = [ord(c) - 65 for c in k] if len(k) > 1 else ord(k) - 65
        it = {"s": clean(stem.replace(" (2 points)", "")), "o": [clean(o) for o in opts], "a": a}
        if why and why[i]: it["x"] = why[i]
        out.append(it)
    return out

stops = [{"place": p, "name": n, "date": d, "color": COL.get(c, "#1E2761"), "text": clean(t), "words": clean(w),
          "move": clean(m), "young": clean(y), "img": f"img/special-2026-12-world/medal-{MEDAL[n]}.jpg",
          "lang": WORDLANG.get(n, "en-US")} for p, n, d, c, t, w, m, y in V["STOPS"]]
days = []
for n, dt, dom, practice, young, coach, light in V["DAYS"]:
    mon, dd = dt.split(" · ")[1].split()
    days.append({"n": n, "date": dt, "iso": date(2026, MON[mon], int(dd)).isoformat(), "dom": dom, "color": DOM.get(dom, "#1F2330"),
                 "practice": clean(practice), "young": clean(young), "coach": clean(coach), "light": clean(light)})

rec1 = clean(find("Good afternoon, students."))
rec2 = [(m.group(1), clean(m.group(2))) for m in re.finditer(r"<b>(\w+):</b>\s*(.*?)(?=<br/>|$)", find("<b>Mateo:</b> Linh, what should"))]
rec3 = clean(find("Here is a question students ask every year"))
flood = [clean(re.sub(r"^<b>\d</b>", "", find(f"<b>{i}</b>&nbsp;&nbsp;"))) for i in (1, 2, 3, 4)]
parol = clean(find("In the Philippines, the Christmas season is easy to see."))
ellis = clean(find("Between 1892 and 1954"))
assert len(rec2) == 8 and all(flood) and "Ellis Island" in ellis

MATH_WHY = ["12 × 9 = 108.", "Count 16 through 24: nine nights.", "7 × 6 = 42.", "2½ × 3 = 7½.", "3 ÷ 12 = ¼ cup each; ¼ × 100 = 25.",
            "25% of 18 is 4.50; 18 − 4.50 = 13.50.", "2h + 4 = 14, so h = 5.", "360 ÷ 7 is about 51.4.", "Start with 20, add 15 each day.",
            "15 is the number made each day.", "15d + 20 ≥ 200, so d ≥ 12.", "a + s = 60 and 8a + 5s = 390 give s = 30."]
HIST_WHY = ["December 6 is the earliest date.", "From the 13th to the 25th is 12 days.", "January 6 and January 7.", None, None, None, None, None, "1882 comes before 1892, 1924 and 1965."]

quiz = [
 {"id": "elem", "tab": "Elementary", "sub": "Grades K–5 · 3 items", "title": "Read and answer: the parol", "points": 3,
  "note": "Grades 3–5 read it themselves; K–2 listen while the teacher reads.",
  "blocks": [{"pass": [parol], "items": items(ELEM, "AAB")},
             {"write": {"id": "elem-lantern", "task": "What would you put on your own lantern? Write one sentence.",
                        "frame": "My lantern has ______ and ______ .", "rubric": "Classroom credit for one complete sentence that names two things."}}]},
 {"id": "read", "tab": "Reading", "sub": "ELPA21 · 8 points", "title": "ELPA21 practice · Reading", "points": 8,
  "note": "Grades 6–12 · about 15 minutes · the two-point written item is in the printed insert",
  "blocks": [{"h": "Part A · Short paragraph", "dir": "Read the paragraph. Then choose the best answer to each question.", "pass": [parol], "items": items(READ[:3], "BAC")},
             {"h": "Part B · The Book Flood", "dir": "Read the passage. Then answer the questions. One question asks for two answers.", "pass": flood,
              "items": items(READ[3:], ["B", "C", "AC", "A"])}]},
 {"id": "listen", "tab": "Listening", "sub": "ELPA21 · 10 points", "title": "ELPA21 practice · Listening", "points": 10,
  "note": "Grades 6–12 · three recordings · play each one twice",
  "blocks": [{"h": "Recording 1 · A school announcement", "rec": [("", rec1)], "items": items(LISTEN[:3], "BCB")},
             {"h": "Recording 2 · A conversation between two students", "rec": rec2, "items": items(LISTEN[3:6], "ABC")},
             {"h": "Recording 3 · A social studies teacher explains", "rec": [("", rec3)], "items": items(LISTEN[6:], "ACCA")}]},
 {"id": "speak", "tab": "Speaking", "sub": "ELPA21 · a visual and a claim", "title": "ELPA21 practice · Speaking", "points": 2,
  "note": "Grades 6–12 · decide, then say your answer to a partner in a full sentence",
  "blocks": [{"h": "Part B · A visual and a claim", "dir": "Study the timeline. Then read the two claims. Decide whether the timeline supports each one. Use dates from the timeline.", "timeline": True,
              "claims": [{"who": "Ana", "t": "Las Posadas lasts longer than any other celebration on the timeline.", "a": 0,
                          "x": "Las Posadas runs from December 16 to 24, nine nights, and every other celebration on the timeline is a single day."},
                         {"who": "Ben", "t": "All of these celebrations happen in December.", "a": 1,
                          "x": "Three Kings Day is on January 6 and Genna is on January 7."}]}]},
 {"id": "write", "tab": "Writing", "sub": "ELPA21 · edit, reply, claim", "title": "ELPA21 practice · Writing", "points": 4,
  "note": "Grades 6–12 · Part A is checked here; your teacher scores Parts B and C",
  "blocks": [{"h": "Part A · Choose the words that make the sentence correct", "items": items(V["ed"], "ABBB")},
             {"h": "Part B · Reply to a classmate", "write": {"id": "w-reply", "min": 5,
               "box": "<b>From:</b> Linh &nbsp; <b>Subject:</b> Our “December Around the World” display<br>Hi! I'm finishing the class display. Which tradition did you find most interesting? What happens in it? How is it similar to, or different from, something your family does? Thanks! — Linh",
               "task": "Write a reply to Linh. Answer <b>all three</b> of her questions. Write at least five sentences.",
               "frame": "You may begin: The tradition I found most interesting is ______. In it, ______. It is similar to ______ because ______.",
               "rubric": clean(find("<b>Part B, reply to a classmate (0–3).</b>")).replace("<b>Part B, reply to a classmate (0–3).</b> ", "")}},
             {"h": "Part C · Build a claim", "write": {"id": "w-claim", "min": 4,
               "box": "<b>Question:</b> Should schools teach about traditions from many countries?<br><b>Note 1:</b> Learning about classmates' traditions can help students understand one another.<br><b>Note 2:</b> Class time is limited, and there is a lot to learn before the spring tests.",
               "task": "Write a paragraph. State your claim, give one reason, support it with one of the notes or your own experience, and end with a closing sentence.",
               "frame": "You may begin: I believe schools (should / should not) ______ because ______. For example, ______. That is why ______.",
               "rubric": clean(find("<b>Part C, build a claim (0–3).</b>")).replace("<b>Part C, build a claim (0–3).</b> ", "")}}]},
 {"id": "math", "tab": "Math", "sub": "State test prep · 12 items", "title": "State test prep · Mathematics", "points": 12,
  "note": "Three grade bands · every answer shows the working",
  "blocks": [{"h": "Grades 3–5", "items": items(MATH[:4], "CCCC", MATH_WHY[:4])},
             {"h": "Grades 6–8", "items": items(MATH[4:8], "BBBB", MATH_WHY[4:8])},
             {"h": "Algebra I", "dir": "For questions 9–11: " + find("An art club has 20 paper lanterns"), "items": items(MATH[8:], "BBCC", MATH_WHY[8:])}]},
 {"id": "sci", "tab": "Science", "sub": "State test prep · 12 items", "title": "State test prep · Science", "points": 12,
  "note": "Grade 5, grade 8 and Biology",
  "blocks": [{"h": "Grade 5", "items": items(SCI[:4], "BBBB")}, {"h": "Grade 8", "items": items(SCI[4:8], "BBBC")},
             {"h": "Biology", "items": items(SCI[8:], "BBBC")}]},
 {"id": "hist", "tab": "History", "sub": "State test prep · 9 items", "title": "State test prep · Social studies and U.S. History", "points": 9,
  "note": "Timeline skills, then a U.S. History passage",
  "blocks": [{"h": "Social studies skills", "dir": "Use the timeline of winter celebrations to answer questions 1–3.", "timeline": True, "items": items(HIST[:3], "BBC", HIST_WHY[:3])},
             {"h": "U.S. History · Traditions travel with people", "dir": "Read the passage. Then answer questions 4–9.", "pass": [ellis], "items": items(HIST[3:], "BABBAB", HIST_WHY[3:])}]},
]

missing = []

DATA = {
 "stops": stops,
 "greet": [{"lang": l, "text": t, "code": CODE.get(l, "")} for l, t in V["GREET"]],
 "weeks": V["WEEK"], "days": days, "color": V["COLOR"],
 "events": [[6, "Dec 6", "St. Nicholas Day", "Germany"], [13, "Dec 13", "St. Lucia Day", "Sweden"], [25, "Dec 25", "Christmas Day", "many countries"],
            [37, "Jan 6", "Three Kings Day", "Spain, Latin America"], [38, "Jan 7", "Genna", "Ethiopia"]],
 "quiz": quiz,
 "family": V["iv"],
 "familyFrame": "I interviewed my ______. The most important celebration in our family is ______. It happens ______ and lasts ______. We always ______. When (he / she / they) was my age, ______. Something I did not know before is ______.",
 "familyNote": "<b>To the family:</b> This interview is practice for your student's English test in the spring. Your home language helps. Please answer in the language you know best.<br><span lang='es'><b>A la familia:</b> Esta entrevista es práctica para el examen de inglés de su estudiante en la primavera. El idioma del hogar ayuda. Por favor, responda en el idioma que mejor domina.</span>",
 "subj": [[s[0], COL.get(s[1], "#1E2761"), s[2], clean(s[3]), clean(s[4])] for s in V["SUBJ"]],
 "moves": [[clean(x) for x in m] for m in V["MOVES"]],
 "tl": V["TL"],
}

def build(out, hub, edition, pdf, colorpdf, canon, share):
    t = (HERE / "special-interactive.template.html").read_text(encoding="utf-8")
    for k, v in {"__DATA__": json.dumps(DATA, ensure_ascii=False).replace("</", "<\\/"), "__HUB__": hub, "__EDITION__": edition,
                 "__PDF__": pdf, "__COLORPDF__": colorpdf, "__CANON__": canon, "__SHARE__": share}.items():
        t = t.replace(k, v)
    out.write_text(t, encoding="utf-8")
    print("wrote", out, f"{len(t) // 1024} KB")

if __name__ == "__main__":
    if missing: print("NOTE family questions not found verbatim in the print edition:", missing)
    H = "https://radan55.github.io/everyteacher/"
    if "--standalone" in sys.argv:
        d = pathlib.Path(sys.argv[sys.argv.index("--standalone") + 1])
        S = "https://radan55.github.io/stormdecemberspecialedition/"
        build(d / "interactive.html", H, "index.html", "el-special-2026-12-world.pdf", "el-special-2026-12-world-coloring.pdf",
              S + "interactive.html", S + "share/el-special-2026-12-world-interactive.png")
    else:
        build(ROOT / "el-special-2026-12-world-interactive.html", "index.html", "el-special-2026-12-world.html", "el-special-2026-12-world.pdf",
              "el-special-2026-12-world-coloring.pdf", H + "el-special-2026-12-world-interactive.html", H + "share/el-special-2026-12-world-interactive.png")
