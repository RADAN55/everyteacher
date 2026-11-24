#!/usr/bin/env python3
"""Build the hub from tools/catalog.py.

    python3 tools/build.py

Writes, between the <!--B:name--> markers in each file:
    index.html   the welcome band (tools/welcome.py), the Now Showing hero, the four doors, this week, the index panel,
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
import bysubject  # noqa: E402
import featured  # noqa: E402
import welcome  # noqa: E402

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
TOP = [r for r in C if not r["series"]]            # what a door shows: series cards + stand-alone pages
RES = [r for r in C if not r["is_series"]]         # real resources, for counts
N = len(RES)
BY_SERIES = {}
for r in C:
    if r["series"]:
        BY_SERIES.setdefault(r["series"], []).append(r)
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
        core = sorted((r for r in TOP if r["group"] == gid and r["core"]),
                      key=lambda r: catalog.CORE_ORDER[r["href"]])
        rest = len([r for r in RES if r["group"] == gid]) - len([r for r in core if not r["is_series"]]) - sum(len(r["members"]) for r in core)
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


# A short film for the Now Showing screen, keyed by the resource's href.
# The page script shows it only while that resource is the one on screen.
PREMIERE_VIDEO = {
    "el-special-2026-12-world.html": (
        "video/christmas-around-the-world.mp4",
        "video/christmas-around-the-world.jpg",
    ),
}


def now_showing():
    if not fresh:
        return "<!-- nothing released in the last three weeks -->"
    h = fresh[0]
    d = datetime.strptime(h["new"], "%Y-%m-%d").strftime("%b %-d")
    shot = (
        f'<img id="prem-img" src="{e(h["thumb"])}" alt="">' if h["thumb"] else ""
    )
    for r in fresh[:6]:
        if r["href"] in PREMIERE_VIDEO:
            src, poster = PREMIERE_VIDEO[r["href"]]
            on = r is h
            shot += (
                f'<video id="prem-vid" data-for="{e(r["href"])}" src="{e(src)}" '
                f'poster="{e(poster)}" muted playsinline preload="metadata"'
                + ("" if on else " hidden") + "></video>"
            )
            break
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
        <div class="prem-dots" id="prem-dots" role="tablist" aria-label="New releases" hidden></div>
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
  <a id="wk-move" href="monday-moves.html"><span class="wk">Monday Move · <span id="wk-n">this week</span></span><b id="wk-mt">Post and Say the Language Goal</b><span class="es" id="wk-mes"></span><small id="wk-mtag">One EL move for every teacher, every Monday.</small></a>
  <a id="wk-tool" href="tech-radar.html"><span class="wk">Tech tool of the week</span><b id="wk-tt">Read Along in Google Classroom</b><small>From the EL Tech Radar: free, Chromebook-ready, a use for every lane.</small></a>
  <a id="wk-res" href="{e(pick["href"])}"{ext_attr(pick["href"])}><span class="wk">Resource of the week</span><b id="wk-rt">{e(pick["title"])}</b><small id="wk-rd">{e(pick["one"])}</small></a>
</div>'''


def index_panel():
    cards = "".join(
        f'<a href="all.html?g={gid}"><b>{e(label)}</b>'
        f'<span>{len([r for r in RES if r["group"] == gid])} resources · '
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


def featured_block():
    by = {r["href"]: r for r in C}
    for h in [featured.LEAD[0]] + [m[0] for m in featured.MORE]:
        if h not in by:
            sys.exit(f"featured: {h} is not in the catalog.")
    if len(featured.MORE) != 3:
        sys.exit("featured: MORE must hold exactly three.")
    L = by[featured.LEAD[0]]
    lead = (f'<a class="f-lead" href="{e(L["href"])}"{ext_attr(L["href"])}>'
            + (f'<img src="{e(L["thumb"])}" alt="" loading="lazy">' if L["thumb"] else "")
            + f'<div class="f-body"><span class="f-tag">{e(featured.LEAD[2])}</span>'
            f'<b>{e(L["title"])}</b><p>{e(featured.LEAD[1])}</p>'
            f'<small>{e(L["fmt"])} · {e(L["size"])} · free</small></div></a>')
    more = "".join(
        f'<a class="f-card" href="{e(by[h]["href"])}"{ext_attr(h)}>'
        + (f'<img src="{e(by[h]["thumb"])}" alt="" loading="lazy">' if by[h]["thumb"] else "")
        + f'<span><b>{e(by[h]["title"])}</b><p>{e(why)}</p>'
          f'<small>{e(by[h]["fmt"])} · {e(by[h]["size"])}</small></span></a>'
        for h, why in featured.MORE
    )
    return ('<div class="wrap">\n<h2>Featured</h2>\n'
            '<p class="deck">Four worth opening first — picked by hand, not by date.</p>\n'
            f'<div class="feat">{lead}<div class="f-more">{more}</div></div>\n</div>')


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


# --------------------------------------------------------- by-subject.html
def by_subject():
    """The subject × grade-band grid.

    Two checks run before anything is written, and both are fatal. A routing
    page whose routes are wrong is worse than no routing page: a teacher
    follows a dead link once and stops trusting the site. So every resource a
    cell points at has to be in the catalog, and every move a cell cites has
    to match the published series by both number and name.
    """
    by_href = {r["href"]: r for r in C}
    bad_links, bad_moves = [], []

    def check(cell, uses, moves):
        for h in uses:
            if h not in by_href:
                bad_links.append(f"{cell}: {h}")
        for n, name in moves:
            if not 1 <= n <= len(bysubject.MOVE_NAMES):
                bad_moves.append(f"{cell}: move {n} is not in the series")
            elif bysubject.MOVE_NAMES[n - 1] != name:
                bad_moves.append(
                    f"{cell}: move {n} is “{bysubject.MOVE_NAMES[n - 1]}”, "
                    f"not “{name}”")

    for (sid, bid), (_, moves, uses) in bysubject.CELLS.items():
        check(f"{sid}/{bid}", uses, moves)
    for _, items in bysubject.ALWAYS:
        check("always", [h for h, _ in items], [])

    if bad_links or bad_moves:
        sys.exit("by-subject.html: " + "; ".join(bad_links + bad_moves))

    for sid, _, _, _ in bysubject.SUBJECTS:
        for bid, _ in bysubject.BANDS:
            if (sid, bid) not in bysubject.CELLS:
                sys.exit(f"by-subject.html: nothing written for {sid}/{bid}.")

    def chip(h):
        r = by_href[h]
        return (f'<a href="{e(h)}"{ext_attr(h)}>{e(r["title"])}'
                f'<small>{e(r["fmt"])}</small></a>')

    out = []
    for sid, label, light, dark in bysubject.SUBJECTS:
        cards = []
        for bid, band in bysubject.BANDS:
            demand, moves, uses = bysubject.CELLS[(sid, bid)]
            mv = "".join(
                f'<li><a href="{e(bysubject.move_url(n))}" target="_blank" '
                f'rel="noopener"><b>{n}</b> {e(name)}</a></li>'
                for n, name in moves
            )
            cards.append(
                f'<article class="cell" data-band="{bid}">'
                f'<p class="band">{e(band)}</p>'
                f'<p class="demand">{demand}</p>'
                f'<p class="lbl">Two moves</p><ol class="mv">{mv}</ol>'
                f'<p class="lbl">Reach for</p>'
                f'<div class="use">{"".join(chip(h) for h in uses)}</div>'
                f'</article>'
            )
        band_label = dict(bysubject.BANDS)
        rows = []
        for url, name, org, bands, line, note in bysubject.OUTSIDE.get(sid, []):
            if not url.startswith("https://"):
                sys.exit(f"by-subject.html: outside link is not https: {url}")
            chips = "".join(f"<i>{e(band_label[b])}</i>" for b in bands.split())
            flag = f'<em>{e(note)}</em>' if note else ""
            rows.append(
                f'<li data-bands="{e(bands)}">'
                f'<a href="{e(url)}" target="_blank" rel="noopener">{e(name)}</a>'
                f'<span class="org">{e(org)}</span>'
                f'<span class="ln">{e(line)}{flag}</span>'
                f'<span class="bd">{chips}</span></li>'
            )
        outside = (
            f'<div class="out"><p class="lbl">Free, from elsewhere</p>'
            f'<ul>{"".join(rows)}</ul></div>' if rows else ""
        )
        out.append(
            f'<section class="subj" id="s-{sid}" data-subj="{sid}" '
            f'style="--sc:{light};--scd:{dark}">'
            f'<h2>{e(label)}</h2>'
            f'<div class="cells">{"".join(cards)}</div>{outside}</section>'
        )

    always = "".join(
        f'<div class="always"><h3>{e(head)}</h3><div class="use">'
        + "".join(
            f'<a href="{e(h)}"{ext_attr(h)}>{e(by_href[h]["title"])}'
            f'<small>{e(why)}</small></a>' for h, why in items)
        + "</div></div>"
        for head, items in bysubject.ALWAYS
    )

    filters = "".join(
        f'<button type="button" data-f="{bid}">{e(band)}</button>'
        for bid, band in bysubject.BANDS
    )
    keys = "".join(
        f'<button type="button" data-k="{sid}" style="--sc:{light};--scd:{dark}">'
        f'{e(label)}</button>'
        for sid, label, light, dark in bysubject.SUBJECTS
    )

    return (
        # hidden until the script that works it has run: a filter bar that does
        # nothing is worse than no filter bar, and the grid below is all there
        # in the HTML either way
        '<div class="bar" role="group" aria-label="Narrow the grid" hidden>'
        '<div class="fset"><span>Grade</span>'
        '<button type="button" data-f="all" aria-pressed="true">All</button>'
        + filters + '</div>'
        '<div class="fset"><span>Subject</span>'
        '<button type="button" data-k="all" aria-pressed="true">All</button>'
        + keys + '</div></div>'
        + "".join(out)
        + always
        + f'<p class="elsew">{bysubject.NOTE}</p>'
    )


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


def row(r, gid, label, mem=False):
    is_new = r["new"] and 0 <= days_old(r["new"]) <= FRESH_DAYS
    marks = ""
    if r["core"]:
        marks += '<span class="st" title="Start here">★</span>'
    if r["ext"]:
        marks += '<span class="ex" title="Opens on its own site">↗</span>'
    if is_new:
        marks += '<span class="nw">New</span>'
    if r["is_series"]:
        marks += f'<span class="sr" title="A series">{len(r["members"])} inside</span>'
    txt = " ".join([r["title"], r["one"], r["fmt"], r["size"],
                    r["who"], label, r["long"]]).lower()
    return (
        f'<tr data-g="{gid}" data-core="{1 if r["core"] else 0}"'
        f'{" class=mem data-series=" + e(r["series"]) if mem else ""}'
        f' data-t="{e(txt)}"'
        f' data-st="{e(r["title"].lower())}"'
        f' data-sg="{GI[gid]}"'
        f' data-sa="{WHO_SORT[r["aud"]]}{e(r["who"].lower())}"'
        f' data-sf="{e(r["fmt"].lower())}">'
        f'<td class="r"><a href="{e(r["href"])}"{ext_attr(r["href"])}>'
        f'{"↳ " if mem else ""}{e(r["title"])}</a>{marks}'
        f'<span class="o">{e(r["one"])}</span></td>'
        f'<td class="g">{e(label)}</td>'
        f'<td class="a">{e(r["who"])}</td>'
        f'<td class="f">{e(r["fmt"])}</td>'
        f'<td class="z">{e(r["size"])}</td></tr>'
    )


def rows():
    out = []
    by_href = {r["href"]: r for r in C}
    for gid, label, aud, deck, role, sub in GROUPS:
        rs = [r for r in TOP if r["group"] == gid]
        rs.sort(key=lambda r: (not r["core"], not r["is_series"], r["title"].lower()))
        n_res = len([r for r in RES if r["group"] == gid])
        out.append(
            f'<tr class="gh" data-g="{gid}"><td colspan="5"><div class="gh-in">'
            f'<b>{e(label)}</b><i>{n_res} resources</i>'
            f'<span>{e(deck)}</span></div></td></tr>'
        )
        for r in rs:
            out.append(row(r, gid, label))
            for h in r["members"]:
                m = by_href[h]
                out.append(row(m, gid, label, mem=True))
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
t = region(t, "welcome", welcome.build(seen, N, TODAY, ext_attr), p)
t = region(t, "now", now_showing(), p)
t = region(t, "doors", doors(), p)
t = region(t, "play", play_band(), p)
t = region(t, "featured", featured_block(), p)
t = region(t, "game", guess_game(), p)
t = region(t, "week", week(), p)
t = region(t, "qa", qa(), p)
t = region(t, "voices", voices_block(), p)
t = region(t, "index", index_panel(), p)
t = region(t, "titles", titles_script(), p)
if write(p, t):
    changed.append("index.html")

p = ROOT / "by-subject.html"
t = p.read_text(encoding="utf-8")
t = region(t, "matrix", by_subject(), p)
if write(p, t):
    changed.append("by-subject.html")

# any page that quotes the total inline
for name in ("content-teachers.html", "about.html"):
    p = ROOT / name
    t = p.read_text(encoding="utf-8")
    t = region(t, "n", str(N), p).replace("<!--B:n-->\n", "<!--B:n-->").replace("\n<!--/B:n-->", "<!--/B:n-->")
    if write(p, t):
        changed.append(name)

p = ROOT / "all.html"
t = p.read_text(encoding="utf-8")
t = region(t, "intro", (
    f'<p>All {N} free resources on the hub, in one place. Everything opens in a '
    f'browser and prints. Nothing needs an account, a license or a login. Sort by '
    f'any column; the star marks the {sum(1 for r in TOP if r["core"])} to start with. '
    f'Series rows hold their members underneath (↳).</p>'
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
MANIFEST_LINK = '<link rel="manifest" href="manifest.webmanifest">'  # the hub installs as an app; hub-chrome.js adds the rest
CHROME_TAG = '<script src="hub-chrome.js" defer></script>'

# ----------------------------------------------------------- series pages
def series_page(r):
    by_href = {x["href"]: x for x in C}
    cards = []
    for h in r["members"]:
        m = by_href[h]
        shot = f'<img src="{e(m["thumb"])}" alt="" loading="lazy">' if m["thumb"] else '<span class="ph">✦</span>'
        cards.append(
            f'<a class="mc" href="{e(h)}"{ext_attr(h)}><div class="shot">{shot}</div>'
            f'<div class="mb"><b>{e(m["title"])}</b><span>{e(m["one"])}</span>'
            f'<small>{e(m["fmt"])} · {e(m["size"])}{" · opens on its own site" if m["ext"] else ""}</small></div></a>'
        )
    label = GLABEL[r["group"]]
    shelves = getattr(catalog, "SHELVES", {}).get(r["is_series"])
    if shelves:
        card_by = dict(zip(r["members"], cards)); used = set(); parts = []
        for heading, blurb, hrefs in shelves:
            cs = [card_by[h] for h in hrefs if h in card_by]; used.update(hrefs)
            if cs: parts.append(f'<h2 class="shelf">{e(heading)}</h2><p class="lead">{e(blurb)}</p><div class="grid">{"".join(cs)}</div>')
        rest = [card_by[h] for h in r["members"] if h not in used]
        if rest: parts.append(f'<h2 class="shelf">More</h2><div class="grid">{"".join(rest)}</div>')
        grid_html = "".join(parts)
    else:
        grid_html = f'<div class="grid">{"".join(cards)}</div>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_SNIPPET}
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(r["title"])} · EL Publishing</title>
<meta name="description" content="{e(r["long"])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,700;1,9..144,600&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  :root{{--navy:#1E2761;--navy-bg:var(--navy);--navy-dk:#141A44;--navy-dk-bg:var(--navy-dk);--gold:#C9A227;--gold-lt:#EBD9A0;--paper:#fff;--mist:#F4F5FA;--ink:#1F2330;--muted:#5D6480;--rule:#DCDEE9}}
  *{{box-sizing:border-box}}body{{margin:0;background:var(--mist);color:var(--ink);font-family:"Source Sans 3",-apple-system,"Segoe UI",sans-serif;font-size:16px;line-height:1.5}}a{{color:var(--navy)}}
  header{{background:var(--navy-bg);color:#fff;position:relative;overflow:hidden}}header::before{{content:"";position:absolute;inset:0;background:repeating-linear-gradient(112deg,rgba(235,217,160,.09) 0 2px,transparent 2px 24px)}}
  .head-in{{position:relative;max-width:1000px;margin:0 auto;padding:40px 22px 30px}}.brand{{font-size:12px;letter-spacing:.2em;color:var(--gold);font-weight:600;margin:0 0 14px}}.brand a{{color:var(--gold);text-decoration:none}}
  h1{{font-family:Fraunces,Georgia,serif;font-weight:700;letter-spacing:-.02em;font-size:clamp(30px,5.5vw,48px);line-height:1.02;margin:0}}.tag{{margin:14px 0 0;font-size:16px;color:#C9CEEA;max-width:66ch}}
  main{{max-width:1000px;margin:0 auto;padding:22px 22px 44px}}.lead{{color:var(--muted);margin:0 0 16px;max-width:72ch}}
  .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:14px}}
  .mc{{display:flex;flex-direction:column;background:var(--paper);border:1px solid var(--rule);text-decoration:none;color:var(--ink);overflow:hidden;transition:transform .15s,box-shadow .15s}}.mc:hover{{transform:translateY(-2px);box-shadow:0 10px 30px rgba(30,39,97,.12)}}
  .shot{{aspect-ratio:700/509;background:var(--navy-dk-bg);display:grid;place-items:center;overflow:hidden}}.shot img{{width:100%;height:100%;object-fit:cover;display:block}}.shot .ph{{color:var(--gold);font-size:34px}}
  .mb{{padding:12px 14px 14px;display:flex;flex-direction:column;gap:4px}}.mb b{{font-family:Fraunces,Georgia,serif;font-size:19px;line-height:1.2;color:var(--navy)}}.mb span{{font-size:14px}}.mb small{{font-size:12px;color:var(--muted);letter-spacing:.04em;text-transform:uppercase;font-weight:700;margin-top:4px}}
  .back{{display:inline-block;margin-top:22px;font-size:14px;font-weight:600}}
  h2.shelf{{font-family:Fraunces,Georgia,serif;font-size:22px;color:var(--navy);margin:28px 0 4px;padding-top:18px;border-top:2px solid var(--gold)}}h2.shelf:first-of-type{{border-top:0;padding-top:0;margin-top:8px}}
  footer{{background:var(--navy-dk-bg);color:#AEB5DA;padding:26px 0;font-size:14px}}footer .wrap{{max-width:1000px;margin:0 auto;padding:0 22px}}footer b{{display:block;color:#fff;font-family:Fraunces,Georgia,serif;font-size:19px;font-weight:600}}footer a{{color:var(--gold)}}
</style>
{THEME_LINK}
{MANIFEST_LINK}
</head>
<body>
<header><div class="head-in"><p class="brand"><a href="index.html">EL PUBLISHING</a> · {e(label.upper())} · A SERIES</p><h1>{e(r["title"])}</h1><p class="tag">{e(r["one"])}</p></div></header>
<main>
<p class="lead">{e(r["long"])}</p>
{grid_html}
<a class="back" href="all.html?g={e(r["group"])}">← Everything under {e(label)}</a>
</main>
<footer><div class="wrap"><b>Richard A. Daniel, M.Ed.</b>ENL/EL Specialist · Laurel High School · Laurel, Mississippi · <a href="index.html">All EL Publishing resources →</a></div></footer>
<script src="guide.js" defer></script>
{CHROME_TAG}
</body>
</html>
"""

for r in C:
    if r["is_series"]:
        p = ROOT / r["href"]
        if write(p, series_page(r)):
            changed.append(r["href"])

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
NO_CHROME = {"commercial.html", "video-stage.html", "avatar-stage.html", "timer.html",  # a full-screen stage; no bar, no theme toggle
             "storm-reading-sets.html", "storm-writing-sets.html", "storm-listening-sets.html", "storm-speaking-sets.html"}  # Storm Studio engine: own rail, own dark mode; home-button.js links back
for page in sorted(ROOT.glob("*.html")):
    if page.name in NO_CHROME:
        continue
    s = page.read_text(encoding="utf-8")
    before = s
    if "elhub.theme" not in s:
        m = re.search(r"<head[^>]*>", s)
        if m:
            s = s[:m.end()] + "\n" + HEAD_SNIPPET + s[m.end():]
    if 'href="theme.css"' not in s:
        s = insert_at(s, "</head>", THEME_LINK, last=False)
    if 'rel="manifest"' not in s:
        s = insert_at(s, "</head>", MANIFEST_LINK, last=False)
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
    f.name for f in ROOT.glob("*.html") if f.name not in {"index.html", "all.html", "video-stage.html", "avatar-stage.html", "timer.html", "offline.html"}
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
SITECFG = json.loads((ROOT / "tools" / "site.json").read_text(encoding="utf-8")) if (ROOT / "tools" / "site.json").exists() else {}
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
    # what search engines read: a canonical address, structured data naming
    # the resource as a free work by its author, and the Search Console tag
    # once it is set in tools/site.json
    cat = seen.get(page.name)
    ld = {"@context": "https://schema.org", "@type": "WebSite" if page.name == "index.html" else "CreativeWork",
          "name": title.split(" · ")[0], "url": url, "description": desc, "inLanguage": "en",
          "isAccessibleForFree": True,
          "author": {"@type": "Person", "name": "Richard A. Daniel", "jobTitle": "ENL/EL Specialist"},
          "publisher": {"@type": "Organization", "name": "EL Publishing", "url": SITE_URL},
          "audience": {"@type": "EducationalAudience", "educationalRole": "teacher"},
          "about": "English learners, Mississippi K–12"}
    if page.name == "index.html":
        ld["potentialAction"] = {"@type": "SearchAction", "target": SITE_URL + "all.html?q={q}", "query-input": "required name=q"}
    if cat:
        ld["learningResourceType"] = cat["fmt"]
    verify = SITECFG.get("google_site_verification", "")
    tags = "\n".join([
        f'<link rel="canonical" href="{url}">',
        (f'<meta name="google-site-verification" content="{e(verify)}">' if verify and page.name == "index.html" else ""),
        '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>',
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
    tags = "\n".join(t for t in tags.split("\n") if t)
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

core = sum(1 for r in TOP if r["core"])
print(f"{N} resources · {core} starred · {len(fresh)} new · "
      f"{len(pinned)} pinned")
for gid, label, *_ in GROUPS:
    print(f"  {len([r for r in RES if r['group'] == gid]):3}  {label}")
print("wrote: " + (", ".join(changed) if changed else "nothing (already current)"))
