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
  <p>All {N} resources in one sortable table — by name, by who they are for, by format.
    The twenty worth starting with are starred.</p>
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
        {"u": r["href"], "t": r["title"], "o": r["one"],
         "f": f'{r["fmt"]} · {r["size"]}', "g": GLABEL[r["group"]],
         "th": r["thumb"], "pin": r["pin"], "new": r["new"]}
        for r in C
    ]


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
t = region(t, "week", week(), p)
t = region(t, "index", index_panel(), p)
t = region(t, "titles", titles_script(), p)
if write(p, t):
    changed.append("index.html")

p = ROOT / "all.html"
t = p.read_text(encoding="utf-8")
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

core = sum(1 for r in C if r["core"])
print(f"{N} resources · {core} starred · {len(fresh)} new · "
      f"{len(pinned)} pinned")
for gid, label, *_ in GROUPS:
    print(f"  {len([r for r in C if r['group'] == gid]):3}  {label}")
print("wrote: " + (", ".join(changed) if changed else "nothing (already current)"))
