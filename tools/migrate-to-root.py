#!/usr/bin/env python3
"""Move the hub from radan55.github.io/everyteacher/ to radan55.github.io/.

    python3 tools/migrate-to-root.py --stage      # build it, change nothing live
    python3 tools/migrate-to-root.py --apply      # rewrite this repo in place

Staging writes the new site to ../rootsite/ and the redirect stubs the old
repo will need to ../oldstubs/, so both can be read before anything moves.

Nothing anyone has ever shared should break: every page of the old site is
left behind as a redirect to its new address.
"""
import argparse, pathlib, re, shutil, sys

OLD = "radan55.github.io/everyteacher/"
NEW = "radan55.github.io/"
ROOT = pathlib.Path(__file__).resolve().parent.parent
TEXT = {".html", ".js", ".json", ".xml", ".txt", ".css", ".md", ".webmanifest", ".py"}

STUB = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>Moved · EL Publishing</title>
<link rel="canonical" href="https://{new}{path}">
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url=https://{new}{path}">
<style>body{{font-family:Inter,-apple-system,"Segoe UI",sans-serif;background:#F4F5FA;
color:#1F2330;margin:0;display:grid;place-items:center;min-height:100vh;padding:24px;
text-align:center;line-height:1.6}}a{{color:#1E2761}}</style>
</head><body><div>
<p>EL Publishing has moved to <b>radan55.github.io</b>.</p>
<p><a href="https://{new}{path}">Continue to this page &rarr;</a></p>
</div></body></html>
"""


def rewrite(text):
    return text.replace(OLD, NEW)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", action="store_true")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    if not (a.stage or a.apply):
        sys.exit("choose --stage or --apply")

    site = ROOT.parent / "rootsite"
    stubs = ROOT.parent / "oldstubs"
    if a.stage:
        for d in (site, stubs):
            if d.exists():
                shutil.rmtree(d)
        shutil.copytree(ROOT, site, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    target = site if a.stage else ROOT
    n_files = n_links = 0
    for f in sorted(target.rglob("*")):
        if not f.is_file() or f.suffix.lower() not in TEXT:
            continue
        if ".git" in f.parts:
            continue
        t = f.read_text(encoding="utf-8", errors="ignore")
        if OLD not in t:
            continue
        n_links += t.count(OLD)
        f.write_text(rewrite(t), encoding="utf-8")
        n_files += 1

    # a redirect for every page of the old site, so shared links survive
    n_stubs = 0
    if a.stage:
        stubs.mkdir(parents=True, exist_ok=True)
        for f in sorted(ROOT.rglob("*.html")):
            if ".git" in f.parts:
                continue
            rel = f.relative_to(ROOT).as_posix()
            out = stubs / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(STUB.format(new=NEW, path=rel.replace("index.html", "")),
                           encoding="utf-8")
            n_stubs += 1
        # non-HTML the old site served directly
        for f in sorted(ROOT.glob("*.pdf")):
            shutil.copy2(f, stubs / f.name)

    print(f"{'staged' if a.stage else 'applied'}: "
          f"{n_links} absolute links rewritten across {n_files} files"
          + (f", {n_stubs} redirect stubs written" if a.stage else ""))
    if a.stage:
        print(f"  new site  -> {site}")
        print(f"  old stubs -> {stubs}")


if __name__ == "__main__":
    main()
