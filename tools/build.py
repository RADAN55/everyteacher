#!/usr/bin/env python3
"""Build the hub from tools/catalog.py.

    python3 tools/build.py

Writes, between the <!--B:name--> markers in each file:
    index.html   the Now Showing hero, the four doors, this week, the index panel,
                 and the catalog the search box reads
    all.html     the group buttons and all 57 table rows
    guide.js     the Hub Guide's catalog
    featured.json  what is new and what is pinned, for the personal site

Every number on the hub — the resource count above all — comes from the catalog,
written into the HTML itself. Nothing is left for a browser to calculate, because
search engines, link previews and social cards do not run scripts.
"""
import html as H
import json
import pathlib
import re
import sys
from datetime import date, datetime

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import catalog  # noqa: E402
import questions  # noqa: E402
import voices  # noqa: E402
import play  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
FRESH_DAYS = 21
TODAY = date.today()


def e(s):
    return H.escape(str(s), quote=True)


def region(text, name, body, path):
    """Replace everything between <!--B:name--> and <!--/B:name-->."""
    pat = re.compile(r"(<!--B:%s-->)(.*?)(<!--/B:%s-->)" % (name, name), re.S)
    if not pat.search(text):
        sys.exit(f"{path.name}: no <!--B:{name}--> region found.")
    return pat.sub(lambda m: m.group(1) + "\n" + body.rstrip() + "\n" + m.group(3), text)


def ext_attr(href):
    return ' target="_blank" rel="noopener"' if href.startswith("http") else ""


def days_old(iso):
    try:
        return (TODAY - datetime.strptime(iso, "%Y-%m-%d").date()).days
    except ValueError:
        return 10**6


# ---------------------------------------------------------------- the catalog
C = catalog.load()
N = len(C)
GROUPS = catalog.GROUPS
GI = {g[0]: i for i, g in enumerate(GROUPS)}
GLABEL = {g[0]: g[1] for g in GROUPS}
GDECK = {g[0]: g[3] for g in GROUPS}

seen = {}
for r in C:
    if r["href"] in seen:
        sys.exit(f"catalog: {r['href']} is listed twice.")
    seen[r["href"]] = r
if N < 20:
    sys.exit(f"catalog: only {N} resources — refusing to write that.")

fresh = sorted(
    (r for r in C if r["new"] and 0 <= days_old(r["new"]) <= FRESH_DAYS),
    key=lambda r: r["new"], reverse=True,
)
pinned = [r for r in C if r["pin"] and days_old(r["pin"]) <= 0]


# ------------------------------------------------------------------ index.html
def doors():
    out = []
    for i, (gid, label, aud, deck, role, sub) in enumerate(GROUPS, 1):
        core = [r for r in C if r["group"] == gid and r["core"]]
        rest = len([r for r in C if r["group"] == gid]) - len(core)
        steps = "".join(
            f'<li><a href="{e(r["href"])}"{ext_attr(r["href"])}>{e(r["title"])}</a>'
            f'<span>{e(r["one"])}</span></li>' for r in core
        )
        out.append(
            f'<div class="door">'
            f'<div class="door-h"><span class="door-n">{i}</span>'
            f'<div><b>{e(role)}</b><small>{e(sub)}</small></div></div>'
            f'<ol>{steps}</ol>'
            f'<a class="rest" href="all.html?g={gid}">{e(label)} · '
            f'{rest} more →</a></div>'
        )
    return '<div class="doors">' + "".join(out) + "</div>"


def now_showing():
    if not fresh:
        return "<!-- nothing released in the last three weeks -->"
    h = fresh[0]
    d = datetime.strptime(h["new"], "%Y-%m-%d").strftime("%b %-d")
    shot = (
        f'<img id="prem-img" src="{e(h["thumb"])}" alt="">' if h["thumb"] else ""
    )
    rail = ""
    if len(fresh) > 1:
        items = "".join(
            f'<a href="{e(r["href"])}"{ext_attr(r["href"])}>'
            f'<span class="nb">NEW · '
            f'{datetime.strptime(r["new"], "%Y-%m-%d").strftime("%b %-d")}</span>'
            + (f'<img src="{e(r["thumb"])}" alt="">' if r["thumb"]
               else '<span class="ph">✦</span>')
            + f'<span><b>{e(r["title"])}</b>'
              f'<small>{e(r["fmt"])} · {e(r["size"])}</small></span></a>'
            for r in fresh[1:4]
        )
        rail = (f'<div class="prem-rail" id="prem-rail"><p class="rk">Also new</p>'
                f'<div class="rr" id="prem-rr">{items}</div></div>')
    else:
        rail = ('<div class="prem-rail" id="prem-rail" hidden>'
                '<p class="rk">Also new</p><div class="rr" id="prem-rr"></div></div>')
    verb = h["title"].split(":")[0]
    return f'''<section class="premiere" id="premiere" aria-label="Now showing">
  <div class="beam"></div>
  <div class="prem-in">
    <p class="prem-k"><i></i>Now showing <small id="prem-date">· released {d}</small></p>
    <div class="prem-grid">
      <div>
        <h2 class="prem-t" id="prem-title">{e(h["title"])}</h2>
        <p class="prem-kind" id="prem-kind">{e(h["fmt"])} · {e(h["size"])}</p>
        <p class="prem-p" id="prem-p">{e(h["one"])}</p>
        <div class="prem-cta"><a class="go" id="prem-go" href="{e(h["href"])}"{ext_attr(h["href"])}>▶ &nbsp;Open {e(verb)}</a><a class="alt" href="whats-new.html">What's new on the hub →</a></div>
      </div>
      <a class="prem-shot" id="prem-shot" href="{e(h["href"])}"{ext_attr(h["href"])} aria-label="Open the featured resource">{shot}<i></i><i></i><i></i><i></i><div class="vig"></div><span class="rec"><b></b>NEW</span></a>
    </div>
    {rail}
  </div>
</section>'''


def week():
    """The resource of the week, written in so the card is never blank.
    index.html re-picks it at load, because the rotation is weekly."""
    pick = pinned[0] if pinned else C[0]
    return f'''<div class="week" aria-label="This week">
  <a id="wk-move" href="https://radan55.github.io/mselablueprintinfo01/monday-moves.html" target="_blank" rel="noopener"><span class="wk">Monday Move · <span id="wk-n">this week</span></span><b id="wk-mt">Post and Say the Language Goal</b><span class="es" id="wk-mes"></span><small id="wk-mtag">One EL move for every teacher, every Monday.</small></a>
  <a id="wk-tool" href="tech-radar.html"><span class="wk">Tech tool of the week</span><b id="wk-tt">Read Along in Google Classroom</b><small>From the EL Tech Radar: free, Chromebook-ready, a use for every lane.</small></a>
  <a id="wk-res" href="{e(pick["href"])}"{ext_attr(pick["href"])}><span class="wk">Resource of the week</span><b id="wk-rt">{e(pick["title"])}</b><small id="wk-rd">{e(pick["one"])}</small></a>
</div>'''


def index_panel():
    cards = "".join(
        f'<a href="all.html?g={gid}"><b>{e(label)}</b>'
        f'<span>{len([r for r in C if r["group"] == gid])} resources · '
        f'{e(deck.split(".")[0].lower()[:1] + deck.split(".")[0][1:])}</span></a>'
        for gid, label, aud, deck, role, sub in GROUPS
    )
    return f'''<div class="wrap">
  <h2>The full index</h2>
  <p>All {N} of them in one sortable table — by name, by who they are for, by format.
    The twenty worth starting with are starred. Still free, still no login.</p>
  <div class="idx-g">{cards}</div>
  <a class="idx-all" href="all.html">Open the full index · {N} resources →</a>
  <div class="idx-s">
    <div><b>{N}</b>live resources</div>
    <div><b>187</b>leveled readables</div>
    <div><b>36</b>week curriculum, 9–12</div>
    <div><b>6</b>languages in the Newcomer Guide</div>
    <div><b>$0</b>every resource is free</div>
  </div>
</div>'''


def small_catalog():
    return [
        # "k" is the long description, carried so the home page's search finds a
        # resource by any phrase the full index would find it by.
        {"u": r["href"], "t": r["title"], "o": r["one"],
         "f": f'{r["fmt"]} · {r["size"]}', "g": GLABEL[r["group"]],
         "k": r["long"], "th": r["thumb"], "pin": r["pin"], "new": r["new"]}
        for r in C
    ]


SHOWN = 6  # questions visible before "show all"


def qa():
    counts = {}
    for who, *_ in questions.Q:
        counts[who] = counts.get(who, 0) + 1
    tabs = (f'<button type="button" data-w="all" aria-pressed="true">All'
            f'<i>{len(questions.Q)}</i></button>')
    for key, label in questions.WHO:
        if counts.get(key):
            tabs += (f'<button type="button" data-w="{key}" aria-pressed="false">'
                     f'{e(label)}<i>{counts[key]}</i></button>')
    cards = []
    for i, (who, q, a, links) in enumerate(questions.Q):
        ls = "".join(
            f'<a href="{e(h)}"{ext_attr(h)}>{e(lab)} →</a>' for lab, h in links)
        cards.append(
            f'<article class="qc{"" if i < SHOWN else " over"}" data-w="{who}">'
            f'<h3>{e(q)}</h3><p>{e(a)}</p><div class="ql">{ls}</div></article>'
        )
    return f'''<div class="wrap">
  <h2>Questions people actually ask</h2>
  <p class="deck">Real questions from real teachers, answered plainly — each with the resource that goes deeper.</p>
  <div class="qtabs" role="group" aria-label="Filter the questions">{tabs}</div>
  <div class="qgrid" id="qgrid">{"".join(cards)}</div>
  <p class="qmore"><button type="button" id="qmore">Show all {len(questions.Q)} questions ↓</button></p>
  <p class="qnone" id="qnone" hidden>No questions in that group yet.</p>
</div>'''


def voices_block():
    items = "".join(
        f'<figure class="voice">'
        f'<a href="voices/{e(img)}" target="_blank" rel="noopener">'
        f'<img src="voices/t-{e(img)}" alt="{e(alt)}" loading="lazy" decoding="async">'
        f'</a><blockquote>{e(quote)}</blockquote>'
        f'<figcaption><b>{e(who)}</b>{e(where)}</figcaption></figure>'
        for img, quote, who, where, alt in voices.V
    )
    return f'''<div class="wrap">
  <h2>In their own handwriting</h2>
  <p class="deck">The notes I kept. From students, from administrators, from a
    school that once gave me a painted tire. Open any one to see the original.</p>
  <div class="vgrid">{items}</div>
</div>'''


def play_band():
    cards = "".join(
        f'<a class="pcard" href="{e(h)}"{ext_attr(h)}>'
        f'<b>{e(name)}</b><i>{e(hook)}</i><span>{e(sub)}</span></a>'
        for h, name, hook, sub in play.PLAY
    )
    return f'''<div class="wrap">
  <p class="freeline">{e(play.FREE)}</p>
  <p class="usage" id="usage" hidden></p>
  <p class="playk">Try one right now</p>
  <div class="pgrid">{cards}</div>
</div>'''


def guess_game():
    """A level-guessing round built from the real Can-Do checklist, so the
    statements are the ones students actually score themselves against."""
    src = (ROOT / "can-do-checklist.html").read_text(encoding="utf-8")
    items = []
    for dm in re.finditer(r'd:"([LRSW])",en:"([^"]+)"[^\[]*lv:\[', src):
        dom, name = dm.group(1), dm.group(2)
        i = dm.end() - 1
        depth, j = 0, i
        while j < len(src):
            if src[j] == "[":
                depth += 1
            elif src[j] == "]":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        for lv, chunk in enumerate(re.findall(r"\[(.*?)\]", src[i:j + 1], re.S), 1):
            for s in re.findall(r'"([^"]+)"', chunk):
                en = s.split("|")[0].strip()
                if en.lower().startswith("i can"):
                    items.append({"t": en, "lv": lv, "d": name})
    if len(items) < 30:
        return "<!-- not enough can-do statements to build the round -->"
    return ('<div class="wrap">\n'
            '<h2>Guess the level</h2>\n'
            '<p class="deck">Here is something a student says they can do. '
            'Which ELPA21 level is that? Eight of them, about a minute. '
            'Every statement is lifted straight from the Can-Do checklist your '
            'students score themselves against.</p>\n'
            '<div class="game" id="game"></div>\n'
            '<script>window.HUB_CANDO=' + json.dumps(items, ensure_ascii=False) +
            ';</script>\n</div>')


def titles_script():
    small = small_catalog()
    return ("<script>\n/* The catalog the search box and the weekly picks read. "
            "Generated by tools/build.py — edit tools/catalog.py instead. */\n"
            "window.HUB_CATALOG=" + json.dumps(small, ensure_ascii=False) +
            ";\n</script>")


# -------------------------------------------------------------------- all.html
def gbtns():
    btns = "".join(
        f'<button type="button" data-g="{gid}" aria-pressed="false">{e(label)}</button>'
        for gid, label, *_ in GROUPS
    )
    gmap = {gid: label for gid, label, *_ in GROUPS}
    return (btns + "\n<script>window.HUB_GROUPS=" +
            json.dumps(gmap, ensure_ascii=False) + ";</script>")


WHO_SORT = {"students": "1", "teachers": "2", "admin": "3"}


def rows():
    out = []
    for gid, label, aud, deck, role, sub in GROUPS:
        rs = [r for r in C if r["group"] == gid]
        rs.sort(key=lambda r: (not r["core"], r["title"].lower()))
        out.append(
            f'<tr class="gh" data-g="{gid}"><td colspan="5"><div class="gh-in">'
            f'<b>{e(label)}</b><i>{len(rs)} resources</i>'
            f'<span>{e(deck)}</span></div></td></tr>'
        )
        for r in rs:
            is_new = r["new"] and 0 <= days_old(r["new"]) <= FRESH_DAYS
            marks = ""
            if r["core"]:
                marks += '<span class="st" title="Start here">★</span>'
            if r["ext"]:
                marks += '<span class="ex" title="Opens on its own site">↗</span>'
            if is_new:
                marks += '<span class="nw">New</span>'
            txt = " ".join([r["title"], r["one"], r["fmt"], r["size"],
                            r["who"], label, r["long"]]).lower()
            out.append(
                f'<tr data-g="{gid}" data-core="{1 if r["core"] else 0}"'
                f' data-t="{e(txt)}"'
                f' data-st="{e(r["title"].lower())}"'
                f' data-sg="{GI[gid]}"'
                f' data-sa="{WHO_SORT[r["aud"]]}{e(r["who"].lower())}"'
                f' data-sf="{e(r["fmt"].lower())}">'
                f'<td class="r"><a href="{e(r["href"])}"{ext_attr(r["href"])}>'
                f'{e(r["title"])}</a>{marks}'
                f'<span class="o">{e(r["one"])}</span></td>'
                f'<td class="g">{e(label)}</td>'
                f'<td class="a">{e(r["who"])}</td>'
                f'<td class="f">{e(r["fmt"])}</td>'
                f'<td class="z">{e(r["size"])}</td></tr>'
            )
    return "\n".join(out)


# -------------------------------------------------------------------- guide.js
def guide_catalog():
    items = [
        {"href": r["href"], "title": r["title"], "aud": r["who"],
         "kind": f'{r["fmt"]} · {r["size"]}', "desc": r["long"],
         "section": GLABEL[r["group"]]}
        for r in C
    ]
    return "var CATALOG = " + json.dumps(items, ensure_ascii=False) + ";"


# ------------------------------------------------------------------------ write
def write(path, text):
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    if old != text:
        path.write_text(text, encoding="utf-8")
        return True
    return False


changed = []

p = ROOT / "index.html"
t = p.read_text(encoding="utf-8")
t = region(t, "now", now_showing(), p)
t = region(t, "doors", doors(), p)
t = region(t, "play", play_band(), p)
t = region(t, "game", guess_game(), p)
t = region(t, "week", week(), p)
t = region(t, "qa", qa(), p)
t = region(t, "voices", voices_block(), p)
t = region(t, "index", index_panel(), p)
t = region(t, "titles", titles_script(), p)
if write(p, t):
    changed.append("index.html")

p = ROOT / "all.html"
t = p.read_text(encoding="utf-8")
t = region(t, "intro", (
    f'<p>All {N} free resources on the hub, in one place. Everything opens in a '
    f'browser and prints. Nothing needs an account, a license or a login. Sort by '
    f'any column; the star marks the {sum(1 for r in C if r["core"])} to start with.</p>'
), p)
t = region(t, "gbtns", gbtns(), p)
t = region(t, "rows", rows(), p)
if write(p, t):
    changed.append("all.html")

p = ROOT / "guide.js"
t = p.read_text(encoding="utf-8")
new_line = guide_catalog()
t2 = re.sub(r"^var CATALOG = \[.*?\];$", lambda m: new_line, t, count=1, flags=re.M)
if t2 == t and new_line not in t:
    sys.exit("guide.js: could not find the CATALOG line.")
if write(p, t2):
    changed.append("guide.js")

# The catalog as data. The personal site reads this instead of scraping the hub's
# HTML, so a change to the home page's markup can never break it again.
p = ROOT / "catalog.json"
if write(p, json.dumps(small_catalog(), ensure_ascii=False, indent=1) + "\n"):
    changed.append("catalog.json")
old = ROOT / "featured.json"
if old.exists():
    old.unlink()
    changed.append("featured.json (removed)")

# ------------------------------------------------- the bar and the theme ----
# Every page gets three things, in this order: a snippet that applies the saved
# theme before the first paint, the stylesheet that defines it, and the script
# that builds the bar. Inserted here rather than by hand so a new page cannot
# be forgotten, and skipped where they are already present.
HEAD_SNIPPET = (
    '<script>/* set the theme before first paint, so nothing flashes white */'
    'try{var _t=localStorage.getItem("elhub.theme");'
    'document.documentElement.setAttribute("data-theme",'
    '_t||(matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light"))}'
    'catch(e){}</script>'
)
THEME_LINK = '<link rel="stylesheet" href="theme.css">'
CHROME_TAG = '<script src="hub-chrome.js" defer></script>'

def insert_at(s, tag, payload, last):
    """Put payload before the document's own closing tag.

    Some pages build an HTML export inside a template literal, so </head> and
    </body> appear more than once. A template lives inside the body, so the
    document's own </head> is the FIRST and its own </body> is the LAST. Get
    that backwards and the tag lands in the export instead of the page — and a
    literal </script> inside an inline script ends it early, which is how this
    went wrong the first time.
    """
    i = s.rfind(tag) if last else s.find(tag)
    return s if i < 0 else s[:i] + payload + "\n" + s[i:]


wired = 0
for page in sorted(ROOT.glob("*.html")):
    s = page.read_text(encoding="utf-8")
    before = s
    if "elhub.theme" not in s:
        m = re.search(r"<head[^>]*>", s)
        if m:
            s = s[:m.end()] + "\n" + HEAD_SNIPPET + s[m.end():]
    if 'href="theme.css"' not in s:
        s = insert_at(s, "</head>", THEME_LINK, last=False)
    if "hub-chrome.js" not in s:
        s = insert_at(s, "</body>", CHROME_TAG, last=True)
    if s != before:
        page.write_text(s, encoding="utf-8")
        wired += 1
if wired:
    changed.append(f"top bar + theme on {wired} pages")

# A sitemap, because the home page is a front door now and no longer lists all
# 57 titles for a crawler to follow. all.html is listed first after the root.
SITE = "https://radan55.github.io/everyteacher/"
pages = ["", "all.html"] + sorted(
    f.name for f in ROOT.glob("*.html") if f.name not in {"index.html", "all.html"}
)
pages += sorted({r["href"] for r in C
                 if not r["ext"] and r["href"].endswith("/")})
prio = {"": "1.0", "all.html": "0.9"}
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in pages:
    sm.append(f"<url><loc>{SITE}{u}</loc>"
              f"<lastmod>{TODAY.isoformat()}</lastmod>"
              f"<priority>{prio.get(u, '0.7')}</priority></url>")
sm.append("</urlset>")
if write(ROOT / "sitemap.xml", "\n".join(sm) + "\n"):
    changed.append(f"sitemap.xml ({len(pages)} urls)")
if write(ROOT / "robots.txt",
         f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n"):
    changed.append("robots.txt")

# the deep "inside the pages" index, rebuilt last so it sees today's HTML
import subprocess  # noqa: E402

idx = subprocess.run(
    [sys.executable, "-I", str(ROOT / "tools" / "build-search-index.py")],
    cwd=ROOT, capture_output=True, text=True,
)
sys.stdout.write(idx.stdout)
if idx.returncode:
    sys.stderr.write(idx.stderr)
    sys.exit("search index failed — the rest of the build is written.")

# ------------------------------------------------------- link previews ------
# The card someone sees when a link is pasted into a group or a text. It is how
# most people meet this site, so every page with a card gets the tags for it,
# rewritten each build so a page can never keep a stale picture.
SITE_URL = "https://radan55.github.io/everyteacher/"
cards = 0
for page in sorted(ROOT.glob("*.html")):
    img = ROOT / "share" / (page.stem + ".png")
    if not img.exists():
        continue
    s = page.read_text(encoding="utf-8")
    m = re.search(r"<title>(.*?)</title>", s, re.S)
    title = re.sub(r"\s+", " ", m.group(1)).strip() if m else "EL Publishing"
    m = re.search(r'<meta name="description" content="([^"]*)"', s)
    desc = m.group(1) if m else ""
    url = SITE_URL + ("" if page.name == "index.html" else page.name)
    tags = "\n".join([
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="EL Publishing">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:title" content="{e(title)}">',
        f'<meta property="og:description" content="{e(desc)}">',
        f'<meta property="og:image" content="{SITE_URL}share/{img.name}">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">',
    ])
    marked = "<!--B:og-->\n" + tags + "\n<!--/B:og-->"
    if "<!--B:og-->" in s:
        s = re.sub(r"<!--B:og-->.*?<!--/B:og-->", lambda mo: marked, s, flags=re.S)
    else:
        s = re.sub(r'\s*<meta (?:property="og:|name="twitter:)[^>]*>', "", s)
        s = insert_at(s, "</head>", marked, last=False)
    if write(page, s):
        cards += 1
if cards:
    changed.append(f"link previews on {cards} pages")

core = sum(1 for r in C if r["core"])
print(f"{N} resources · {core} starred · {len(fresh)} new · "
      f"{len(pinned)} pinned")
for gid, label, *_ in GROUPS:
    print(f"  {len([r for r in C if r['group'] == gid]):3}  {label}")
print("wrote: " + (", ".join(changed) if changed else "nothing (already current)"))
