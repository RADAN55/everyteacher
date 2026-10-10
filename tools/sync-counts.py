#!/usr/bin/env python3
"""Write the true resource count into the hub's source files.

The home page also recounts at runtime, but that only helps a real browser.
Search engines, link previews, social cards and anything that reads the HTML
without running scripts see whatever is literally in the file — so the number
has to be correct in the source too.

Run from the repo root after adding or removing a catalog card:
    python3 tools/sync-counts.py
"""
import re, sys, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
idx = root / "index.html"
guide = root / "guide.js"

html = idx.read_text(encoding="utf-8")

# Count catalog cards the same way the runtime counter does:
# an <a class="card"> inside a <section>'s .cards grid.
sections = re.findall(r'<section\b[^>]*>.*?</section>', html, re.S)
n = 0
for s in sections:
    for grid in re.findall(r'<div class="cards">.*?</section>', s, re.S):
        n += len(re.findall(r'<a class="card"', grid))

if n < 10:
    sys.exit(f"Refusing to write an implausible count ({n}). Check the markup.")

before = html
html = re.sub(r'(<span id="nRes">)\d+(</span>)', rf'\g<1>{n}\g<2>', html)
html = re.sub(r'(placeholder="Search )\d+( resources)', rf'\g<1>{n}\g<2>', html)
if html != before:
    idx.write_text(html, encoding="utf-8")

g = guide.read_text(encoding="utf-8")
gb = g
# The greeting uses CATALOG.length at runtime; keep any literal fallbacks honest.
g = re.sub(r'(I know all )\d+( resources)', rf'\g<1>{n}\g<2>', g)
g = re.sub(r'(Conozco los )\d+( recursos)', rf'\g<1>{n}\g<2>', g)
if g != gb:
    guide.write_text(g, encoding="utf-8")

print(f"resource count = {n}  (index.html deck + search placeholder, guide.js literals)")
