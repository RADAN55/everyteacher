#!/usr/bin/env python3
"""Render the share cards — the picture that appears when someone pastes a link.

    python3 tools/make-cards.py

One 1200x630 card per page, written to share/. A teacher posting a link in a
Facebook group is the main way anyone finds this site, so the card has to say
what the thing is and that it costs nothing, in the half second before someone
scrolls past.

Cards are drawn as HTML and photographed with the same browser the site runs
in, so they use the real brand faces rather than an approximation.
"""
import base64, json, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import catalog  # noqa: E402

OUT = ROOT / "share"
FONTS = ROOT / "tools" / "fonts"
NAVY, GOLD, MIST = "#141A44", "#C9A227", "#C9CEEA"


def b64(p):
    return base64.b64encode(p.read_bytes()).decode()


MARK = ('<svg viewBox="0 0 64 64" class="mk">'
        '<rect x="9" y="34" width="10" height="18" rx="1" fill="#6B74A8"/>'
        '<rect x="22" y="27" width="10" height="25" rx="1" fill="#C9A227"/>'
        '<rect x="35" y="20" width="10" height="32" rx="1" fill="#A9B1DA"/>'
        '<rect x="48" y="13" width="10" height="39" rx="1" fill="#FFFFFF"/>'
        '<rect x="6" y="52" width="55" height="3.4" rx="1.2" fill="#C9A227"/></svg>')


def card_html(title, sub, kicker, thumb_b64):
    size = 72 if len(title) < 28 else 60 if len(title) < 46 else 50 if len(title) < 70 else 42
    shot = (f'<div class="shot"><img src="data:image/jpeg;base64,{thumb_b64}"></div>'
            if thumb_b64 else "")
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Fr;src:url(data:font/ttf;base64,{b64(FONTS/'Fraunces.ttf')})}}
@font-face{{font-family:In;src:url(data:font/ttf;base64,{b64(FONTS/'Inter.ttf')})}}
*{{margin:0;box-sizing:border-box}}
body{{width:1200px;height:630px;background:{NAVY};overflow:hidden;position:relative;
  font-family:In,sans-serif;display:flex}}
body::before{{content:"";position:absolute;inset:0;
  background:repeating-linear-gradient(112deg,rgba(235,217,160,.09) 0 2px,transparent 2px 26px)}}
.l{{position:relative;flex:1;padding:54px 50px 48px 64px;display:flex;flex-direction:column}}
.top{{display:flex;align-items:center;gap:14px}}
.mk{{width:52px;height:52px;flex:none}}
.top b{{font-family:Fr;font-size:27px;font-weight:600;color:#fff;letter-spacing:.01em}}
.kick{{margin-top:auto;font-size:17px;letter-spacing:.26em;text-transform:uppercase;
  color:{GOLD};font-weight:700}}
h1{{font-family:Fr;font-weight:700;font-size:{size}px;line-height:1.02;color:#fff;
  letter-spacing:-.025em;margin:16px 0 0;max-width:19ch}}
p{{font-size:25px;line-height:1.38;color:{MIST};margin:20px 0 0;max-width:30ch}}
.foot{{margin-top:auto;padding-top:22px;border-top:2px solid {GOLD};
  display:flex;justify-content:space-between;align-items:baseline;font-size:19px}}
.foot b{{color:{GOLD};font-weight:700}}
.foot span{{color:#AEB5DA}}
.shot{{position:relative;width:420px;flex:none;padding:54px 50px 48px 0;
  display:flex;align-items:center}}
.shot img{{width:100%;border:3px solid {GOLD};box-shadow:0 24px 60px rgba(0,0,0,.55);
  display:block}}
</style></head><body>
<div class="l">
  <div class="top">{MARK}<b>EL Publishing</b></div>
  <p class="kick">{kicker}</p>
  <h1>{title}</h1>
  <p>{sub}</p>
  <div class="foot"><b>Free — no login, no account</b><span>radan55.github.io/everyteacher</span></div>
</div>{shot}</body></html>"""


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def main():
    OUT.mkdir(exist_ok=True)
    jobs = []

    jobs.append(("index", "Free resources for English learners",
                 "Curriculum, practice, compliance and the paperwork — built in a "
                 "Mississippi high school, free to anyone who wants it.",
                 f"{len(catalog.load())} resources", "thumbs/storm-lens.jpg"))
    jobs.append(("all", "Every resource, in one index",
                 "Sortable by name, audience and format. The twenty worth starting "
                 "with are starred.", "The full index", ""))
    jobs.append(("leaders", "For district leaders",
                 "Are we compliant? Are our ELs growing? What does it cost? Three "
                 "questions, with the free tools for each.", "District office", ""))
    jobs.append(("whats-new", "What's new on the hub",
                 "New resources, bulletins and tools — something lands most weeks.",
                 "Updated weekly", ""))
    jobs.append(("about", "About EL Publishing",
                 "Who builds this, how it is checked, and what it costs. (Nothing.)",
                 "Accuracy · access · privacy", ""))

    for r in catalog.load():
        if r["ext"] or not r["href"].endswith(".html"):
            continue
        jobs.append((r["href"][:-5], r["title"], r["one"],
                     f'{r["fmt"]} · {r["size"]}', r["thumb"]))

    spec = []
    for name, title, sub, kicker, thumb in jobs:
        tb = ""
        if thumb and (ROOT / thumb).exists():
            tb = b64(ROOT / thumb)
        spec.append({"out": str(OUT / f"{name}.png"),
                     "html": card_html(esc(title), esc(sub), esc(kicker), tb)})

    tmp = ROOT / "tools" / ".cards.json"
    tmp.write_text(json.dumps(spec), encoding="utf-8")
    js = ROOT / "tools" / "shoot-cards.mjs"
    # playwright lives in the scratch sandbox, not here
    env = dict(**__import__("os").environ)
    node_path = pathlib.Path(
        "/tmp/claude-0/-home-claude/8b8003a1-aa3b-52bd-bcbf-19614c79fc15/"
        "scratchpad/node_modules")
    if node_path.exists():
        env["NODE_PATH"] = str(node_path)
    r = subprocess.run(["node", str(js), str(tmp)],
                       capture_output=True, text=True, env=env)
    sys.stdout.write(r.stdout)
    if r.returncode:
        sys.stderr.write(r.stderr)
        sys.exit("card rendering failed")
    tmp.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
