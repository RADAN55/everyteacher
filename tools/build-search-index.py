#!/usr/bin/env python3
"""Build search-index.json for the EL Publishing Hub.
Run through tools/build.py, which calls this last.
Indexes every top-level .html page by heading section so the home-page search
can find text inside pages, not only catalog cards."""
import re, json, html, glob, os

# index.html and all.html are the catalog itself — the typeahead already searches
# the catalog, so indexing them would bury page text under 57 duplicate blurbs.
SKIP = {"search.html", "index.html", "all.html"}
out = []
def clean(s):
    s = re.sub(r"<script.*?</script>|<style.*?</style>", " ", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()

for f in sorted(glob.glob("*.html")):
    if f in SKIP: continue
    src = open(f, encoding="utf-8").read()
    title = clean(re.search(r"<title>(.*?)</title>", src, re.S).group(1) if re.search(r"<title>", src) else f)
    title = title.replace(" · EL Publishing", "").strip()
    body = src[src.find("<body"):] if "<body" in src else src
    body = re.sub(r"<script.*?</script>|<style.*?</style>|<nav.*?</nav>|<footer.*?</footer>", " ", body, flags=re.S)
    # split on h1-h3; keep the id of the heading or of a nearby <section id=...>
    parts = re.split(r"(<(?:h[123]|section)\b[^>]*>)", body)
    cur_id, cur_head, buf = "", title, []
    def flush():
        txt = clean(" ".join(buf))
        if len(txt) > 40:
            out.append({"u": f + (("#" + cur_id) if cur_id else ""), "p": title, "h": cur_head if cur_head != title else "", "t": txt[:600]})
    for i, chunk in enumerate(parts):
        m = re.match(r"<(h[123]|section)\b([^>]*)>", chunk)
        if m:
            idm = re.search(r'id="([^"]+)"', m.group(2))
            if m.group(1) == "section":
                if idm: cur_id = idm.group(1)
                continue
            flush(); buf = []
            if idm: cur_id = idm.group(1)
            # heading text is the start of the next chunk up to the closing tag
            nxt = parts[i + 1] if i + 1 < len(parts) else ""
            hm = re.match(r"(.*?)</h[123]>", nxt, re.S)
            cur_head = clean(hm.group(1)) if hm else cur_head
            if hm: parts[i + 1] = nxt[hm.end():]
        else:
            buf.append(chunk)
    flush()

json.dump(out, open("search-index.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(f"indexed {len(out)} sections from {len(set(e['p'] for e in out))} pages -> search-index.json ({os.path.getsize('search-index.json')//1024} KB)")
