#!/usr/bin/env python3
"""Write spanish-for-teachers.html and spanish-for-teachers-packet.pdf from tools/workshop.py.

    python3 tools/make-workshop.py          # page + PDF
    python3 tools/make-workshop.py --page   # page only
"""
import html, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import workshop as W  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE = ROOT / "spanish-for-teachers.html"
PDF = ROOT / "spanish-for-teachers-packet.pdf"
BANNER = "img/spanish-for-teachers-banner.jpg"
E = html.escape

TITLE = "Spanish for Teachers"
DESC = ("A free 90-minute workshop any teacher can lead for colleagues who speak no Spanish: five "
        "pronunciation rules, students' names said right, the directions a class hears every day, "
        "encouragement, the fifteen things students say to a teacher, and a two-minute good-news call "
        "home — with a Spanish voice on every phrase, round timers, a projector mode and a printable packet.")

BLOCKS = [  # the agenda, in order; rounds slot in by id
 ("welcome", "Welcome and the five rules", 10),
 ("greet", None, None), ("room", None, None), ("encourage", None, None), ("hear", None, None), ("call", None, None),
 ("cognates", "The cognate shortcut", 5),
 ("close", "Pocket card and close", 10),
]
RID = {r["id"]: r for r in W.ROUNDS}


def agenda():
    out, t = [], 0
    for bid, title, mins in BLOCKS:
        if bid in RID:
            r = RID[bid]; title = f"Round {r['n']} · {r['title']}"; mins = r["minutes"]
        out.append((bid, title, mins, t)); t += mins
    assert t == 90, t
    return out


WELCOME_SCRIPT = [
 "Open with the honest sentence: ‘Ninety minutes will not make anyone bilingual. It will give you about seventy phrases, five rules that make Spanish readable, and a call-home script. That is enough to change how a student feels in your room on Monday.’",
 "Ask who in the room already has a Spanish-speaking student. Nearly every hand goes up. That is the audience.",
 "Put the five rules on the screen one at a time. Play the example words. Everyone repeats. Spend most of the time on rule 2 — stress — because it is the one that fixes names.",
 "Set the ground rule for the room: nobody says ‘I can't.’ You say casi (almost) and try again.",
]
CLOSE_SCRIPT = [
 "Everyone fills in the pocket card: five phrases I will say this week, one student I will greet by name, one family I will call. Fold it; it fits behind a badge.",
 "Exit ticket, three lines: one phrase I can say now, one I will practice, one thing I want next. Collect them — they are the agenda for the ten-minute follow-ups.",
 "Announce the follow-up: ten minutes a week for six weeks, same room, same page. Week 1 is greet at the door. Put it on the calendar before people leave.",
 "Last word, together: Piénsalo en español. Escríbelo en inglés. Then hasta mañana.",
]


def rule_say(i, ex):
    import re
    if i == 4:
        return "¿Lo dije bien?"
    return re.sub(r"\s*\([^)]*\)", "", ex).replace(" · ", ". ")


def phrase_rows(r):
    rows = []
    for es, say, en, note in r["phrases"]:
        rows.append(f'<tr><td class="es" data-h="Spanish"><button class="say" type="button" data-say="{E(es)}" aria-label="Play">▶</button>{E(es)}</td>'
                    f'<td class="sy" data-h="Say it">{E(say)}</td><td data-h="English"><b>{E(en)}</b>{("<i> · " + E(note) + "</i>") if note else ""}</td></tr>')
    return "\n".join(rows)


def round_section(r):
    extra = ""
    if r.get("extra"):
        extra = f'<div class="callout gold"><b>{E(r["extra"][0])}</b><p>{E(r["extra"][1])}</p></div>'
    script = "".join(f"<li>{E(s)}</li>" for s in r["script"])
    return f'''
<section class="part round" id="round-{r["id"]}">
  <p class="pk">Round {r["n"]} · {r["minutes"]} minutes</p>
  <h2 class="sec">{E(r["title"])}</h2>
  <p class="deck">{E(r["goal"])}</p>
  <table><thead><tr><th>Spanish</th><th>Say it</th><th>English</th></tr></thead><tbody>
{phrase_rows(r)}
  </tbody></table>
  {extra}
  <div class="duo">
    <div class="callout"><b>Practice · {E(r["practice"][0])}</b><p>{E(r["practice"][1])}</p></div>
    <div class="facil"><b>If you are leading</b><ol>{script}</ol></div>
  </div>
</section>'''


def page():
    ag = agenda()
    rules = "".join(
        f'<div class="rule"><span class="num">{i+1}</span><b class="t">{E(t)}</b><p>{E(body)}</p><p class="ex"><button class="say" type="button" data-say="{E(rule_say(i, ex))}" aria-label="Play">▶</button>{E(ex)}</p></div>'
        for i, (t, body, ex) in enumerate(W.RULES))
    names = "".join(f'<li><button class="say" type="button" data-say="{E(n)}" aria-label="Play">▶</button><b>{E(n)}</b> <span>{E(s)}</span></li>' for n, s in W.NAMES)
    agenda_html = "".join(
        f'<li><span class="at">{t:02d}:00</span><span class="min">{m} min</span><b>{E(title)}</b></li>' for bid, title, m, t in ag)
    prep = "".join(f"<li>{E(p)}</li>" for p in W.PREP)
    rounds = "".join(round_section(r) for r in W.ROUNDS)
    cog = "".join(f'<li><button class="say" type="button" data-say="{E(a)}" aria-label="Play">▶</button><b>{E(a)}</b> <span>{E(b)}</span></li>' for a, b in W.COGNATES)
    pat = "".join(f'<div><b>{E(a)}</b><p>{E(b)}</p></div>' for a, b in W.PATTERNS)
    false = "".join(f'<li><b>{E(a)}</b> = {E(b)} <i>({E(c)})</i></li>' for a, b, c in W.FALSE)
    follow = "".join(f'<li><b>{E(w)}</b><span class="t">{E(t)}</span><p>{E(d)}</p></li>' for w, t, d in W.FOLLOWUP)

    # data for the runner and projector
    blocks_js = []
    for bid, title, m, t in ag:
        if bid in RID:
            r = RID[bid]
            blocks_js.append(dict(id=bid, title=title, min=m, at=t, script=r["script"],
                                  practice=r["practice"], phrases=[list(p) for p in r["phrases"]], goal=r["goal"]))
        elif bid == "welcome":
            blocks_js.append(dict(id=bid, title=title, min=m, at=t, script=WELCOME_SCRIPT, practice=None,
                                  phrases=[[__import__("re").sub(r"\s*\([^)]*\)", "", r_[2]), "", r_[0], ""] for r_ in W.RULES[:4]] + [["¿Lo dije bien?", "loh DEE-heh byen", "Did I say it right? — the ground rule: nobody says ‘I can't’", ""]], goal="Five rules that make Spanish readable, and the ground rule for the room."))
        elif bid == "cognates":
            blocks_js.append(dict(id=bid, title=title, min=m, at=t, practice=None, goal="The words your Spanish speakers already know.",
                                  script=["Put the twenty cognates up. Ask the room to read them out loud with the five vowel rule. They can.",
                                          "Show the five endings. Ask each table to find three more cognates in a textbook on the table — one minute.",
                                          "Read the false friends. The one everyone remembers is the last one."],
                                  phrases=[[a, "", b, ""] for a, b in W.COGNATES]))
        else:
            blocks_js.append(dict(id=bid, title=title, min=m, at=t, script=CLOSE_SCRIPT, practice=None,
                                  phrases=[["Piénsalo en español. Escríbelo en inglés.", "PYEN-sah-loh en es-pah-NYOL · es-KREE-beh-loh en een-GLES", "Think it in Spanish. Write it in English.", ""],
                                           ["Hasta mañana", "AHS-tah mah-NYAH-nah", "See you tomorrow", ""]],
                                  goal="Five phrases on a card, a three-line exit ticket, and the first follow-up on the calendar."))
    data = json.dumps(blocks_js, ensure_ascii=False)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<script>/* set the theme before first paint, so nothing flashes white */try{{var _t=localStorage.getItem("elhub.theme");document.documentElement.setAttribute("data-theme",_t||(matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light"))}}catch(e){{}}</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE} · A Free 90-Minute Teacher-Led Workshop · EL Publishing</title>
<meta name="description" content="{E(DESC)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,700;1,9..144,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root{{--navy:#1E2761;--navy-bg:var(--navy);--wash-grey-5:#FAFBFD;--ink-red-6:#8A6A0E;--navy-dk-bg:var(--navy-dk);--navy-dk:#141A44;--gold:#C9A227;--gold-lt:#EBD9A0;--paper:#fff;--mist:#F4F5FA;--ink:#1F2330;--muted:#5D6480;--rule:#DCDEE9;--teal:#0B6670;--teal-lt:#E6F2F3;--cream:#FFF5D6;--red:#C8373E;--coral:#E8503A}}
  *{{box-sizing:border-box}}
  html{{scroll-behavior:smooth}}
  body{{margin:0;background:var(--mist);color:var(--ink);font-family:Inter,-apple-system,"Segoe UI",sans-serif;font-size:16.5px;line-height:1.6}}
  .wrap{{max-width:960px;margin:0 auto;padding:0 22px}}
  a{{color:var(--navy)}}
  header{{background:var(--navy-bg);color:#fff;position:relative;overflow:hidden}}
  header::before{{content:"";position:absolute;inset:0;background:repeating-linear-gradient(112deg,rgba(235,217,160,.09) 0 2px,transparent 2px 24px)}}
  .head-in{{position:relative;max-width:960px;margin:0 auto;padding:40px 22px 34px;display:grid;grid-template-columns:1.25fr 1fr;gap:28px;align-items:center}}
  @media (max-width:720px){{.head-in{{grid-template-columns:1fr}}.head-in .cover{{order:-1}}}}
  .brand{{font-size:12px;letter-spacing:.2em;color:var(--gold);font-weight:600;margin:0 0 14px}}
  .brand a{{color:var(--gold);text-decoration:none}}
  h1{{font-family:Fraunces,Georgia,serif;font-weight:700;letter-spacing:-.02em;font-size:clamp(34px,7vw,58px);line-height:1;margin:0}}
  h1 em{{font-style:italic;font-weight:600;color:var(--gold)}}
  .tag{{margin:14px 0 0;font-size:17px;color:#C9CEEA;max-width:62ch}}
  .chips{{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}}
  .chips span{{border:1px solid rgba(235,217,160,.5);color:var(--gold-lt);font-size:12px;letter-spacing:.12em;text-transform:uppercase;padding:4px 11px;border-radius:999px;font-weight:600}}
  .hbtns{{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}}
  .btn{{display:inline-block;background:var(--gold);color:var(--navy-dk);font-weight:700;text-decoration:none;padding:9px 18px;border-radius:999px;font-size:14px;border:0;cursor:pointer;font-family:inherit}}
  .btn.ghost{{background:transparent;border:1.5px solid var(--gold-lt);color:var(--gold-lt)}}
  main .btn.ghost{{border-color:var(--navy);color:var(--navy)}}
  .cover img{{width:100%;height:auto;display:block;border-radius:10px;box-shadow:0 18px 40px rgba(0,0,0,.35)}}

  .toc{{position:sticky;top:0;z-index:5;background:var(--paper);border-bottom:1px solid var(--rule);box-shadow:0 2px 10px rgba(30,39,97,.06)}}
  .toc .wrap{{display:flex;gap:4px;overflow-x:auto;padding-top:8px;padding-bottom:8px;scrollbar-width:none}}
  .toc .wrap::-webkit-scrollbar{{display:none}}
  .toc a{{flex:0 0 auto;font-size:13px;font-weight:600;text-decoration:none;color:var(--navy);padding:6px 12px;border-radius:999px;white-space:nowrap}}
  .toc a:hover{{background:var(--mist)}}
  .toc a.on{{background:var(--navy-bg);color:#fff}}

  main{{padding:28px 0 40px}}
  .part{{margin:40px 0 0;scroll-margin-top:60px}}
  .part .pk{{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--gold-ink);font-weight:700;margin:0 0 4px}}
  h2.sec{{font-family:Fraunces,Georgia,serif;font-weight:700;font-size:30px;color:var(--navy);margin:0 0 6px;letter-spacing:-.01em;line-height:1.12}}
  .deck{{margin:0 0 16px;color:var(--muted);font-size:16px}}
  h3{{font-family:Fraunces,Georgia,serif;font-weight:700;font-size:22px;color:var(--navy);margin:28px 0 6px;letter-spacing:-.01em;line-height:1.15}}

  .callout{{background:var(--teal-lt);border:1px solid #CBE2E4;border-left:6px solid var(--teal);padding:14px 18px;margin:14px 0 0;border-radius:4px}}
  .callout b{{display:block;color:var(--teal);font-size:12.5px;letter-spacing:.12em;text-transform:uppercase;margin-bottom:4px}}
  .callout p{{margin:0}}
  .callout.gold{{background:var(--cream);border-color:#EBD9A0;border-left-color:var(--gold)}}
  .callout.gold b{{color:var(--ink-red-6)}}
  .facil{{background:var(--paper);border:1px solid var(--rule);border-left:6px solid var(--navy);padding:14px 18px;margin:14px 0 0;border-radius:4px}}
  .facil b{{display:block;color:var(--navy);font-size:12.5px;letter-spacing:.12em;text-transform:uppercase;margin-bottom:4px}}
  .facil ol{{margin:0;padding-left:20px;font-size:15px}}
  .facil li+li{{margin-top:6px}}
  .duo{{display:grid;grid-template-columns:1fr 1fr;gap:14px}}
  @media (max-width:720px){{.duo{{grid-template-columns:1fr}}}}

  .stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin:18px 0 0}}
  .stats div{{background:var(--paper);border:1px solid var(--rule);padding:14px 16px}}
  .stats b{{display:block;font-family:Fraunces,Georgia,serif;font-size:32px;color:var(--navy);line-height:1}}
  .stats span{{font-size:13px;color:var(--muted)}}
  ul.prep{{margin:14px 0 0;padding-left:22px;font-size:15.5px}}
  ul.prep li+li{{margin-top:6px}}

  ol.agenda{{list-style:none;margin:16px 0 0;padding:0;border:1px solid var(--rule);background:var(--paper)}}
  ol.agenda li{{display:grid;grid-template-columns:64px 70px 1fr;gap:12px;align-items:center;padding:10px 16px;border-top:1px solid var(--rule);font-size:15.5px}}
  ol.agenda li:first-child{{border-top:0}}
  ol.agenda .at{{font-family:Fraunces,Georgia,serif;font-weight:700;color:var(--gold-ink);font-size:18px}}
  ol.agenda .min{{font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:600}}
  ol.agenda b{{color:var(--navy)}}

  .rules{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px;margin:16px 0 0}}
  .rule{{background:var(--paper);border:1px solid var(--rule);border-top:6px solid var(--gold);padding:16px 18px;position:relative}}
  .rule .num{{font-family:Fraunces,Georgia,serif;font-weight:700;font-size:40px;line-height:1;color:var(--navy);display:block}}
  .rule b.t{{display:block;color:var(--navy);font-family:Fraunces,Georgia,serif;font-size:20px;line-height:1.15;margin:6px 0 4px}}
  .rule p{{margin:0;font-size:15px}}
  .rule p.ex{{margin-top:8px;color:var(--teal);font-weight:600;font-size:14.5px}}

  ul.names,ul.cog{{list-style:none;margin:14px 0 0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:8px}}
  ul.names li,ul.cog li{{background:var(--paper);border:1px solid var(--rule);padding:8px 12px;font-size:15px;display:flex;gap:8px;align-items:center}}
  ul.names b,ul.cog b{{color:var(--navy)}}
  ul.names span,ul.cog span{{color:var(--teal);font-size:13.5px;margin-left:auto;text-align:right}}

  button.say{{width:28px;height:28px;border-radius:50%;border:0;background:var(--navy);color:#fff;font-size:11px;cursor:pointer;margin-right:8px;flex:0 0 auto;vertical-align:middle;font-family:inherit}}
  button.say:hover{{background:var(--teal)}}
  button.say.on{{background:var(--coral)}}

  table{{width:100%;border-collapse:collapse;margin:14px 0 0;background:var(--paper);font-size:15px;border:1px solid var(--rule)}}
  th{{background:var(--teal);color:#fff;text-align:left;padding:10px 12px;font-size:13px;letter-spacing:.06em;text-transform:uppercase;font-weight:600}}
  td{{padding:9px 12px;border-top:1px solid var(--rule);vertical-align:top}}
  tr:nth-child(even) td{{background:var(--wash-grey-5)}}
  td.es{{font-weight:600;color:var(--navy);white-space:nowrap}}
  td.sy{{color:var(--teal);font-size:14px}}
  td b{{color:var(--navy)}}
  td i{{color:var(--muted);font-style:normal;font-size:13.5px}}
  @media (max-width:640px){{
    table,thead,tbody,tr,th,td{{display:block}}
    thead{{display:none}}
    tr{{border-top:3px solid var(--teal);margin-top:10px}}
    td{{border-top:1px solid var(--rule);padding:8px 12px}}
    td.es{{white-space:normal}}
    td::before{{content:attr(data-h);display:block;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--teal);font-weight:700;margin-bottom:2px}}
  }}

  .pats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:10px;margin:14px 0 0}}
  .pats div{{background:var(--paper);border:1px solid var(--rule);border-top:4px solid var(--teal);padding:12px 14px}}
  .pats b{{display:block;color:var(--navy);font-family:Fraunces,Georgia,serif;font-size:19px}}
  .pats p{{margin:4px 0 0;font-size:14px;color:var(--muted)}}
  ul.false{{margin:10px 0 0;padding-left:20px;font-size:15px;columns:2;column-gap:28px}}
  @media (max-width:560px){{ul.false{{columns:1}}}}
  ul.false b{{color:var(--red)}}
  ul.false i{{color:var(--muted)}}

  ol.follow{{list-style:none;margin:16px 0 0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:10px}}
  ol.follow li{{background:var(--paper);border:1px solid var(--rule);border-top:5px solid var(--gold);padding:12px 14px}}
  ol.follow b{{display:block;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-ink)}}
  ol.follow .t{{display:block;font-family:Fraunces,Georgia,serif;font-size:19px;color:var(--navy);margin:2px 0 4px}}
  ol.follow p{{margin:0;font-size:14.5px}}

  .pdfbox{{display:flex;flex-wrap:wrap;gap:14px;align-items:center;justify-content:space-between;background:var(--paper);border:1px solid var(--rule);border-left:6px solid var(--navy);padding:16px 20px;margin:16px 0 0}}
  .pdfbox p{{margin:0;font-size:15px}}
  .pdfbox b{{color:var(--navy)}}
  .related{{margin:34px 0 0;border-top:1px solid var(--rule);padding-top:18px}}
  .related h4{{margin:0 0 8px;font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}}
  .related a{{display:inline-block;margin:4px 8px 4px 0;font-size:14.5px}}
  .fine{{font-size:13.5px;color:var(--muted);margin:14px 0 0}}
  footer{{background:var(--navy-dk-bg);color:#C9CEEA;font-size:14px;padding:26px 0}}
  footer a{{color:var(--gold-lt)}}
  footer b{{color:#fff;display:block;font-size:15px}}

  /* the runner */
  .runner{{background:var(--paper);border:1px solid var(--rule);border-top:6px solid var(--coral);padding:18px 20px;margin:16px 0 0}}
  .run-top{{display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between}}
  .clock{{font-family:Fraunces,Georgia,serif;font-weight:700;font-size:44px;line-height:1;color:var(--navy);font-variant-numeric:tabular-nums}}
  .clock small{{display:block;font-family:Inter,sans-serif;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);font-weight:600;margin-top:4px}}
  .clock.over{{color:var(--red)}}
  .run-ctl{{display:flex;flex-wrap:wrap;gap:8px}}
  .run-ctl .btn{{font-size:13.5px}}
  .run-ctl .btn.sec{{background:var(--navy);color:#fff}}
  .run-body{{margin-top:16px;border-top:1px solid var(--rule);padding-top:14px}}
  .run-body .pk{{margin:0}}
  .run-body h3{{margin:2px 0 4px}}
  .run-body .goal{{color:var(--muted);margin:0 0 10px;font-size:15px}}
  .run-body ol{{margin:0;padding-left:20px;font-size:15.5px}}
  .run-body li+li{{margin-top:7px}}
  .run-steps{{display:flex;flex-wrap:wrap;gap:6px;margin-top:14px}}
  .run-steps button{{border:1px solid var(--rule);background:var(--mist);color:var(--navy);font-weight:600;font-size:12.5px;padding:5px 10px;border-radius:999px;cursor:pointer;font-family:inherit}}
  .run-steps button.on{{background:var(--navy);color:#fff;border-color:var(--navy)}}
  .run-steps button.done{{opacity:.55;text-decoration:line-through}}
  .audio-line{{font-size:13.5px;color:var(--muted);margin:10px 0 0;display:flex;gap:10px;align-items:center;flex-wrap:wrap}}
  .audio-line select{{font:inherit;font-size:13px;padding:3px 6px;border:1px solid var(--rule);border-radius:4px;background:var(--paper);color:var(--ink)}}

  /* projector */
  .proj{{position:fixed;inset:0;background:#141A44;color:#fff;z-index:50;display:none;flex-direction:column;padding:4vh 5vw}}
  .proj.on{{display:flex}}
  .proj .pt{{display:flex;justify-content:space-between;align-items:center;font-size:clamp(14px,1.8vw,20px);color:#C9CEEA;letter-spacing:.08em;text-transform:uppercase;font-weight:600}}
  .proj .pt button{{background:transparent;border:1.5px solid #C9CEEA;color:#fff;font:inherit;padding:6px 14px;border-radius:999px;cursor:pointer}}
  .proj .pc{{flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;gap:2vh}}
  .proj .es{{font-family:Fraunces,Georgia,serif;font-weight:700;font-size:clamp(34px,7.5vw,104px);line-height:1.05;color:#fff}}
  .proj .sy{{font-size:clamp(18px,3vw,40px);color:var(--gold-lt);font-weight:600}}
  .proj .en{{font-size:clamp(18px,3vw,40px);color:#C9CEEA}}
  .proj .en i{{display:block;font-size:.65em;color:#8E96C4;font-style:normal;margin-top:.4em}}
  .proj .pb{{display:flex;gap:14px;justify-content:center;align-items:center;flex-wrap:wrap;margin-top:2vh}}
  .proj .pb button{{font:inherit;font-weight:700;font-size:clamp(14px,1.6vw,20px);padding:12px 26px;border-radius:999px;border:0;cursor:pointer;background:var(--gold);color:#141A44}}
  .proj .pb button.g{{background:transparent;border:1.5px solid #C9CEEA;color:#fff}}
  .proj .cnt{{color:#8E96C4;font-size:clamp(13px,1.5vw,18px)}}

  @media print{{
    body{{background:var(--paper);font-size:12.5px}}
    header{{background:var(--navy-bg)!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
    .toc,.hbtns,.pdfbox,.related,footer,.runner,button.say,#elp-guide-btn,.elp-guide,.proj{{display:none!important}}
    th{{background:var(--teal)!important;color:#fff!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
    table,.callout,.rule,.facil{{break-inside:avoid}}
  }}
</style>
<link rel="stylesheet" href="theme.css">

<!--B:og-->
<!--/B:og-->
</head>
<body>
<header>
  <div class="head-in">
    <div>
      <p class="brand"><a href="index.html">EL PUBLISHING</a> · PROFESSIONAL LEARNING</p>
      <h1>Spanish for Teachers — <em>a 90-minute workshop any teacher can lead.</em></h1>
      <p class="tag">Five pronunciation rules, your students’ names said right, the directions a class hears every day, encouragement, the fifteen things students say to a teacher, and a two-minute good-news call home. For teachers who speak no Spanish, led by a colleague who may not either: every phrase plays in a Spanish voice, every round has a timer, and the packet prints. <b>Free. No trainer needed.</b></p>
      <div class="chips"><span>90 minutes</span><span>5 rounds</span><span>70+ phrases</span><span>Audio on every line</span><span>Projector mode</span><span>Printable packet</span></div>
      <div class="hbtns"><a class="btn" href="#run">Run the workshop</a><a class="btn ghost" href="spanish-for-teachers-packet.pdf" download>Download the packet (PDF)</a></div>
    </div>
    <div class="cover"><img src="{BANNER}" alt="Spanish for Teachers — a free 90-minute teacher-led workshop" width="1280" height="720"></div>
  </div>
</header>
<nav class="toc" aria-label="Sections"><div class="wrap">
  <a href="#start">Start here</a><a href="#agenda">Agenda</a><a href="#run">Run it</a><a href="#rules">Five rules</a><a href="#round-greet">Round 1</a><a href="#round-room">Round 2</a><a href="#round-encourage">Round 3</a><a href="#round-hear">Round 4</a><a href="#round-call">Round 5</a><a href="#cognates">Cognates</a><a href="#after">After</a><a href="#packet">Packet</a>
</div></nav>
<main class="wrap">

<section class="part" id="start">
  <p class="pk">Start here</p>
  <h2 class="sec">What ninety minutes can and cannot do</h2>
  <p>It cannot make a faculty bilingual, and this workshop does not pretend to. What it does is narrower and more useful: a teacher who speaks no Spanish walks out able to say a student’s name the way the student says it, greet the class, give the directions every class needs, encourage, recognize the fifteen things a student is most likely to say, and make a two-minute good-news call home from a script. Those are the moments where a Spanish-speaking student decides whether this room is for them.</p>
  <p>It is built to be run by whoever is willing: the EL specialist, a department chair, a teacher who took Spanish in high school, or one who never did. The page plays every phrase in a Spanish voice, the timers run each round, and the facilitator notes under every table say what to do next. A Spanish-speaking colleague or student in the room is a gift, not a requirement.</p>
  <div class="stats"><div><b>90</b><span>minutes, timed by round</span></div><div><b>5</b><span>rounds, each with a practice</span></div><div><b>72</b><span>phrases, with audio and a say-it key</span></div><div><b>0</b><span>Spanish required to lead it</span></div></div>
  <h3>Before people arrive</h3>
  <ul class="prep">{prep}</ul>
  <div class="callout gold"><b>Where it comes from</b><p>The phrases are the ones in the <a href="using-spanish-handouts.html">Teacher Handout Folder</a> and the <a href="using-spanish-content-classroom.html">Using Spanish in the Content Classroom</a> guide, cut to what can be learned in a sitting. The one sentence the whole workshop turns on — <i>Piénsalo en español. Escríbelo en inglés.</i> — is the guide’s Talk → Plan → Write move in six words.</p></div>
</section>

<section class="part" id="agenda">
  <p class="pk">The agenda</p>
  <h2 class="sec">Eight blocks, ninety minutes</h2>
  <p class="deck">Times are from the start. The runner below keeps you on it.</p>
  <ol class="agenda">{agenda_html}</ol>
</section>

<section class="part" id="run">
  <p class="pk">Run it</p>
  <h2 class="sec">The workshop runner</h2>
  <p class="deck">Press start when the room is ready. Each block counts down and turns red when it runs over; <b>Projector</b> puts the block’s phrases on the screen one at a time, big, with a play button and arrow keys.</p>
  <div class="runner" id="runner">
    <div class="run-top">
      <div class="clock" id="clk">10:00<small id="clk-sub">Block 1 of 8 · 00:00 elapsed</small></div>
      <div class="run-ctl">
        <button class="btn" id="b-start" type="button">▶ Start</button>
        <button class="btn sec" id="b-proj" type="button">Projector</button>
        <button class="btn ghost" id="b-prev" type="button">‹ Back</button>
        <button class="btn ghost" id="b-next" type="button">Next ›</button>
      </div>
    </div>
    <div class="run-steps" id="steps"></div>
    <div class="run-body" id="run-body"></div>
    <p class="audio-line"><span id="au-status">Audio: tap any ▶ to test the Spanish voice on this device.</span><label>Voice <select id="voice"></select></label></p>
  </div>
</section>

<section class="part" id="rules">
  <p class="pk">Block 1 · 10 minutes</p>
  <h2 class="sec">Five rules that make Spanish readable</h2>
  <p class="deck">Spanish is spelled the way it sounds. Learn these five and you can read any phrase in this workshop out loud without ever having heard it.</p>
  <div class="rules">{rules}</div>
  <h3>The name card</h3>
  <p>Say the name the way the student says it. If you are not sure, ask — <i>¿Cómo se pronuncia tu nombre?</i> — and say it back. Capitals mark the stressed syllable.</p>
  <ul class="names">{names}</ul>
  <div class="facil"><b>If you are leading</b><ol>{"".join(f"<li>{E(s)}</li>" for s in WELCOME_SCRIPT)}</ol></div>
</section>

{rounds}

<section class="part" id="cognates">
  <p class="pk">Block 7 · 5 minutes</p>
  <h2 class="sec">The cognate shortcut</h2>
  <p class="deck">Roughly three in four academic words in English have a Spanish twin. Your Spanish speakers already own these; you just have to point.</p>
  <ul class="cog">{cog}</ul>
  <h3>Five endings that convert</h3>
  <div class="pats">{pat}</div>
  <h3>Nine false friends</h3>
  <ul class="false">{false}</ul>
</section>

<section class="part" id="after">
  <p class="pk">Block 8 and after</p>
  <h2 class="sec">Pocket card, exit ticket, six Tuesdays</h2>
  <p class="deck">The workshop is the easy part. The pocket card goes behind a badge; the ten-minute follow-ups keep the phrases alive for six weeks.</p>
  <div class="facil"><b>Closing the room</b><ol>{"".join(f"<li>{E(s)}</li>" for s in CLOSE_SCRIPT)}</ol></div>
  <h3>Six ten-minute follow-ups</h3>
  <ol class="follow">{follow}</ol>
</section>

<section class="part" id="packet">
  <p class="pk">The packet</p>
  <h2 class="sec">Everything on paper</h2>
  <div class="pdfbox"><p><b>Spanish for Teachers — facilitator packet (PDF).</b> The agenda and facilitator script, the five rules and name card, every phrase table with its say-it key, the cut-apart cards for Round 3, the family-call script, the cognate page, a fold-over pocket card, the exit ticket and the six-week plan. Print the script for yourself and the last pages for every teacher.</p><a class="btn" href="spanish-for-teachers-packet.pdf" download>Download the packet</a></div>
  <div class="related"><h4>Goes with</h4>
    <a href="using-spanish-handouts.html">Teacher Handout Folder →</a>
    <a href="using-spanish-content-classroom.html">Using Spanish in the Content Classroom →</a>
    <a href="spoken-spanish-english.html">Spoken Spanish &amp; Spoken English →</a>
    <a href="sheltered.html">Sheltered: 12 minutes as an EL →</a>
    <a href="cognate-hunt.html">Cognate Hunt →</a>
  </div>
  <p class="fine">Spanish reflects widely understood Latin American usage; words vary by country, so welcome your students’ versions. The Spanish voice is your browser’s own speech synthesis and is labeled as such; on a device with no Spanish voice installed, the say-it column is the guide. Free to copy and share for professional learning.</p>
</section>
</main>
<footer>
  <div class="wrap">
    <b>Richard A. Daniel, M.Ed.</b>
    ENL/EL Specialist · Laurel High School · Laurel, Mississippi · <a href="index.html">All EL Publishing resources →</a>
  </div>
</footer>

<div class="proj" id="proj" role="dialog" aria-label="Projector">
  <div class="pt"><span id="p-title">Round 1</span><button type="button" id="p-close">Close · Esc</button></div>
  <div class="pc"><div class="es" id="p-es"></div><div class="sy" id="p-sy"></div><div class="en" id="p-en"></div>
    <div class="pb"><button type="button" class="g" id="p-prev">‹ Back</button><button type="button" id="p-play">▶ Play</button><button type="button" class="g" id="p-next">Next ›</button></div>
    <div class="cnt" id="p-cnt"></div></div>
</div>

<script>
window.SFT = {data};
(function(){{
  // ---- Spanish voice ----
  var synth = window.speechSynthesis, voices = [], chosen = null, unlocked = false;
  var sel = document.getElementById('voice'), st = document.getElementById('au-status');
  function pick(){{
    if(!synth) return;
    voices = synth.getVoices().filter(function(v){{ return /^es/i.test(v.lang); }});
    var pref = ['es-MX','es-US','es-419','es-ES'];
    voices.sort(function(a,b){{
      var ia = pref.indexOf(a.lang.replace('_','-')), ib = pref.indexOf(b.lang.replace('_','-'));
      ia = ia<0?9:ia; ib = ib<0?9:ib;
      if(ia!==ib) return ia-ib;
      return (b.localService?1:0)-(a.localService?1:0);
    }});
    sel.innerHTML = '';
    if(!voices.length){{ sel.innerHTML='<option>No Spanish voice on this device</option>'; chosen=null;
      st.textContent='Audio: this device has no Spanish voice installed — use the say-it column, or open the page on a phone or Chromebook.'; return; }}
    voices.forEach(function(v,i){{ var o=document.createElement('option'); o.value=i; o.textContent=v.name+' ('+v.lang+')'; sel.appendChild(o); }});
    var saved = null; try{{ saved = localStorage.getItem('sft.voice'); }}catch(e){{}}
    var idx = 0; if(saved){{ voices.forEach(function(v,i){{ if(v.name===saved) idx=i; }}); }}
    sel.value = idx; chosen = voices[idx];
    st.textContent = 'Audio: Spanish voice ready ('+chosen.name+'). Synthesized speech — a model, not a native speaker.';
  }}
  if(synth){{ pick(); synth.onvoiceschanged = pick; setTimeout(pick, 600); }}
  else {{ st.textContent='Audio: this browser cannot speak. Use the say-it column.'; }}
  sel.addEventListener('change', function(){{ chosen = voices[+sel.value]; try{{ localStorage.setItem('sft.voice', chosen.name); }}catch(e){{}} }});
  var lastBtn = null;
  window.sftSay = function(text, btn){{
    if(!synth) return;
    synth.cancel();
    if(lastBtn) lastBtn.classList.remove('on');
    var u = new SpeechSynthesisUtterance(text);
    u.lang = chosen ? chosen.lang : 'es-MX'; if(chosen) u.voice = chosen; u.rate = 0.85; u.pitch = 1;
    if(btn){{ btn.classList.add('on'); lastBtn = btn; u.onend = u.onerror = function(){{ btn.classList.remove('on'); }}; }}
    synth.speak(u); unlocked = true;
    if(!voices.length) st.textContent='Audio: no Spanish voice found; the browser may read it with an English accent. The say-it column is the guide.';
  }};
  document.addEventListener('click', function(ev){{
    var b = ev.target.closest('button.say'); if(!b) return;
    sftSay(b.getAttribute('data-say'), b);
  }});

  // ---- runner ----
  var B = window.SFT, cur = 0, running = false, blockStart = null, blockUsed = 0, total = 0, tick = null;
  var clk = document.getElementById('clk'), sub = document.getElementById('clk-sub'), body = document.getElementById('run-body'), steps = document.getElementById('steps');
  function mmss(s){{ s=Math.max(0,Math.round(s)); return (s<600?'0':'')+Math.floor(s/60)+':'+('0'+s%60).slice(-2); }}
  function render(){{
    var b = B[cur];
    steps.innerHTML = B.map(function(x,i){{ return '<button type="button" data-i="'+i+'" class="'+(i===cur?'on':'')+(i<cur?' done':'')+'">'+(i+1)+' · '+x.title.replace(/^Round \\d+ · /,'')+'</button>'; }}).join('');
    var pr = b.practice ? '<div class="callout"><b>Practice · '+esc(b.practice[0])+'</b><p>'+esc(b.practice[1])+'</p></div>' : '';
    body.innerHTML = '<p class="pk">Block '+(cur+1)+' of '+B.length+' · '+b.min+' minutes · starts at '+mmss(b.at*60).replace(/^0/,'')+'</p><h3>'+esc(b.title)+'</h3><p class="goal">'+esc(b.goal)+'</p><ol>'+b.script.map(function(s){{return '<li>'+esc(s)+'</li>';}}).join('')+'</ol>'+pr;
    paint();
  }}
  function esc(s){{ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;'); }}
  function used(){{ return blockUsed + (running && blockStart ? (Date.now()-blockStart)/1000 : 0); }}
  function paint(){{
    var b = B[cur], left = b.min*60 - used();
    clk.firstChild.nodeValue = (left<0?'-':'')+mmss(Math.abs(left));
    clk.classList.toggle('over', left<0);
    sub.textContent = 'Block '+(cur+1)+' of '+B.length+' · '+mmss(total+used())+' elapsed of 90:00';
  }}
  function go(i){{ if(i<0||i>=B.length) return; total += used(); blockUsed = 0; blockStart = running?Date.now():null; cur = i; render(); }}
  document.getElementById('b-start').addEventListener('click', function(){{
    if(!running){{ running = true; blockStart = Date.now(); this.textContent='❚❚ Pause'; tick = setInterval(paint, 500); }}
    else {{ running = false; blockUsed = used(); blockStart = null; this.textContent='▶ Resume'; clearInterval(tick); }}
    paint();
  }});
  document.getElementById('b-next').addEventListener('click', function(){{ go(cur+1); }});
  document.getElementById('b-prev').addEventListener('click', function(){{ go(cur-1); }});
  steps.addEventListener('click', function(ev){{ var b=ev.target.closest('button'); if(b) go(+b.getAttribute('data-i')); }});
  render();

  // ---- projector ----
  var P = document.getElementById('proj'), pi = 0;
  var pes=document.getElementById('p-es'), psy=document.getElementById('p-sy'), pen=document.getElementById('p-en'), pcnt=document.getElementById('p-cnt'), ptitle=document.getElementById('p-title');
  function pshow(){{
    var list = B[cur].phrases, p = list[pi];
    ptitle.textContent = B[cur].title; pes.textContent = p[0]; psy.textContent = p[1];
    pen.innerHTML = esc(p[2]) + (p[3] ? '<i>'+esc(p[3])+'</i>' : ''); pcnt.textContent = (pi+1)+' / '+list.length;
  }}
  function popen(){{ pi = 0; P.classList.add('on'); pshow(); if(P.requestFullscreen) P.requestFullscreen().catch(function(){{}}); }}
  function pclose(){{ P.classList.remove('on'); if(document.fullscreenElement && document.exitFullscreen) document.exitFullscreen().catch(function(){{}}); synth && synth.cancel(); }}
  function pnext(d){{ var n = B[cur].phrases.length; pi = (pi + d + n) % n; pshow(); }}
  document.getElementById('b-proj').addEventListener('click', popen);
  document.getElementById('p-close').addEventListener('click', pclose);
  document.getElementById('p-next').addEventListener('click', function(){{ pnext(1); }});
  document.getElementById('p-prev').addEventListener('click', function(){{ pnext(-1); }});
  document.getElementById('p-play').addEventListener('click', function(){{ sftSay(B[cur].phrases[pi][0]); }});
  document.addEventListener('keydown', function(ev){{
    if(!P.classList.contains('on')) return;
    if(ev.key==='Escape') pclose(); else if(ev.key==='ArrowRight'||ev.key===' ') {{ ev.preventDefault(); pnext(1); }}
    else if(ev.key==='ArrowLeft') pnext(-1); else if(ev.key==='Enter'||ev.key==='p') sftSay(B[cur].phrases[pi][0]);
  }});

  // ---- toc ----
  var links=[].slice.call(document.querySelectorAll('.toc a'));
  var parts=links.map(function(a){{return document.querySelector(a.getAttribute('href'))}}).filter(Boolean);
  function upd(){{ var y=window.scrollY+90, c=parts[0]; parts.forEach(function(p){{ if(p.offsetTop<=y) c=p; }}); links.forEach(function(a){{ a.classList.toggle('on', a.getAttribute('href')==='#'+c.id); }}); }}
  window.addEventListener('scroll',upd,{{passive:true}}); upd();
}})();
</script>
<script src="guide.js" defer></script>
<script data-goatcounter="https://elpublishing.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
<script src="hub-chrome.js" defer></script>
</body>
</html>
'''


# ---------------- the packet ----------------
def pdf_html():
    ag = agenda()
    def tbl(r):
        rows = "".join(f'<tr><td class="es">{E(es)}</td><td class="sy">{E(say)}</td><td>{E(en)}{(" <i>· " + E(n) + "</i>") if n else ""}</td></tr>' for es, say, en, n in r["phrases"])
        return f'<table><thead><tr><th>Spanish</th><th>Say it</th><th>English</th></tr></thead><tbody>{rows}</tbody></table>'
    def scriptbox(title, mins, lines, practice=None, extra=None):
        pr = f'<div class="pr"><b>Practice · {E(practice[0])}</b>{E(practice[1])}</div>' if practice else ""
        ex = f'<div class="pr gold"><b>{E(extra[0])}</b>{E(extra[1])}</div>' if extra else ""
        return f'<div class="blk"><div class="bh"><span>{mins} min</span><h2>{E(title)}</h2></div><ol>{"".join(f"<li>{E(s)}</li>" for s in lines)}</ol>{pr}{ex}</div>'

    # facilitator script pages
    script_pages = []
    for bid, title, m, t in ag:
        if bid in RID:
            r = RID[bid]; script_pages.append(scriptbox(title, m, r["script"], r["practice"], r.get("extra")))
        elif bid == "welcome": script_pages.append(scriptbox(title, m, WELCOME_SCRIPT))
        elif bid == "cognates": script_pages.append(scriptbox(title, m, ["Put the twenty cognates up. Ask the room to read them out loud with the five vowel rule. They can.", "Show the five endings. Ask each table to find three more cognates in a textbook on the table — one minute.", "Read the false friends. The one everyone remembers is the last one."]))
        else: script_pages.append(scriptbox(title, m, CLOSE_SCRIPT))

    agenda_rows = "".join(f'<tr><td class="at">{t:02d}:00</td><td>{m} min</td><td><b>{E(title)}</b></td></tr>' for bid, title, m, t in ag)
    rules = "".join(f'<div class="rule"><span class="n">{i+1}</span><div><b>{E(t)}</b><p>{E(b)}</p><p class="ex">{E(ex)}</p></div></div>' for i, (t, b, ex) in enumerate(W.RULES))
    names = "".join(f'<li><b>{E(n)}</b> <span>{E(s)}</span></li>' for n, s in W.NAMES)
    phrase_pages = "".join(f'<section class="page"><p class="k">Round {r["n"]} · {r["minutes"]} minutes</p><h1>{E(r["title"])}</h1><p class="goal">{E(r["goal"])}</p>{tbl(r)}{("<div class=pr><b>" + E(r["extra"][0]) + "</b>" + E(r["extra"][1]) + "</div>") if r.get("extra") else ""}<div class="pr"><b>Practice · {E(r["practice"][0])}</b>{E(r["practice"][1])}</div><p class="foot">Spanish for Teachers · EL Publishing · radan55.github.io/everyteacher</p></section>' for r in W.ROUNDS)
    cards = "".join(f'<div class="card"><b>{E(es)}</b><span>{E(say)}</span><i>{E(en)}</i></div>' for es, say, en, n in RID["encourage"]["phrases"])
    cog = "".join(f'<li><b>{E(a)}</b> {E(b)}</li>' for a, b in W.COGNATES)
    pat = "".join(f'<li><b>{E(a)}</b> — {E(b)}</li>' for a, b in W.PATTERNS)
    false = "".join(f'<li><b>{E(a)}</b> = {E(b)} <i>({E(c)})</i></li>' for a, b, c in W.FALSE)
    follow = "".join(f'<tr><td><b>{E(w)}</b></td><td><b>{E(t)}</b></td><td>{E(d)}</td></tr>' for w, t, d in W.FOLLOWUP)
    prep = "".join(f"<li>{E(p)}</li>" for p in W.PREP)
    banner_b64 = __import__("base64").b64encode((ROOT / BANNER).read_bytes()).decode()

    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Spanish for Teachers — Facilitator Packet</title>
<style>
@page{{size:letter;margin:0.6in 0.65in 0.7in}}
body{{font-family:Inter,"Segoe UI",Arial,sans-serif;color:#1F2330;font-size:10.5pt;line-height:1.42;margin:0}}
h1{{font-family:Fraunces,Georgia,serif;color:#1E2761;font-size:22pt;margin:0 0 4pt;line-height:1.1}}
h2{{font-family:Fraunces,Georgia,serif;color:#1E2761;font-size:14pt;margin:0}}
.page{{page-break-after:always;position:relative;min-height:9.2in}}
.page:last-child{{page-break-after:auto}}
.k{{font-size:8.5pt;letter-spacing:.18em;text-transform:uppercase;color:#7A5F0E;font-weight:700;margin:0 0 2pt}}
.goal{{color:#5D6480;margin:0 0 8pt;font-size:10.5pt}}
.foot{{position:absolute;bottom:0;left:0;font-size:8pt;color:#8E96C4;margin:0}}
.cover{{background:#1E2761;color:#fff;margin:-0.6in -0.65in -0.7in;padding:0.6in 0.65in;min-height:11in;box-sizing:border-box;page-break-after:always}}
.cover img{{width:100%;border-radius:8pt;display:block}}
.cover h1{{color:#fff;font-size:30pt;margin:22pt 0 6pt}}
.cover p{{color:#C9CEEA;font-size:11.5pt;max-width:60ch}}
.cover .sub{{color:#EBD9A0;font-size:13pt;font-weight:600}}
.cover .by{{position:absolute;bottom:.55in;color:#C9CEEA;font-size:9.5pt}}
.cover .by b{{color:#fff;display:block}}
table{{width:100%;border-collapse:collapse;font-size:9.6pt;margin:6pt 0 0}}
th{{background:#0B6670;color:#fff;text-align:left;padding:4pt 6pt;font-size:8pt;letter-spacing:.08em;text-transform:uppercase}}
td{{padding:3.6pt 6pt;border-bottom:1px solid #DCDEE9;vertical-align:top}}
td.es{{font-weight:700;color:#1E2761;white-space:nowrap}}
td.sy{{color:#0B6670;font-size:9pt}}
td.at{{font-family:Fraunces,Georgia,serif;font-weight:700;color:#7A5F0E;font-size:12pt;white-space:nowrap}}
td i{{color:#5D6480;font-style:normal;font-size:8.8pt}}
.pr{{background:#E6F2F3;border-left:4pt solid #0B6670;padding:6pt 9pt;margin:8pt 0 0;font-size:9.6pt;page-break-inside:avoid}}
.pr b{{display:block;color:#0B6670;font-size:8pt;letter-spacing:.12em;text-transform:uppercase;margin-bottom:2pt}}
.pr.gold{{background:#FFF5D6;border-left-color:#C9A227}}.pr.gold b{{color:#8A6A0E}}
.blk{{border:1px solid #DCDEE9;border-top:4pt solid #C9A227;padding:8pt 11pt;margin:0 0 9pt;page-break-inside:avoid}}
.bh{{display:flex;gap:10pt;align-items:baseline}}
.bh span{{font-family:Fraunces,Georgia,serif;font-weight:700;color:#7A5F0E;font-size:12pt;white-space:nowrap}}
.blk ol{{margin:4pt 0 0;padding-left:16pt;font-size:9.8pt}}
.blk li+li{{margin-top:3pt}}
.rule{{display:flex;gap:10pt;border:1px solid #DCDEE9;border-left:4pt solid #C9A227;padding:7pt 10pt;margin:0 0 7pt;page-break-inside:avoid}}
.rule .n{{font-family:Fraunces,Georgia,serif;font-weight:700;font-size:24pt;color:#1E2761;line-height:1}}
.rule b{{color:#1E2761;font-size:11.5pt}}.rule p{{margin:2pt 0 0;font-size:9.8pt}}.rule p.ex{{color:#0B6670;font-weight:600}}
ul.names{{list-style:none;margin:6pt 0 0;padding:0;columns:3;column-gap:14pt;font-size:10pt}}
ul.names li{{display:flex;justify-content:space-between;border-bottom:1px solid #DCDEE9;padding:2.5pt 0;break-inside:avoid}}
ul.names b{{color:#1E2761}}ul.names span{{color:#0B6670;font-size:9pt}}
ul.prep{{margin:6pt 0 0;padding-left:16pt;font-size:10pt}}ul.prep li+li{{margin-top:3pt}}
.cards{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8pt;margin-top:8pt}}
.card{{border:1.5pt dashed #8E96C4;padding:10pt 10pt;text-align:center;min-height:1.05in;display:flex;flex-direction:column;justify-content:center;page-break-inside:avoid}}
.card b{{font-family:Fraunces,Georgia,serif;color:#1E2761;font-size:13.5pt;line-height:1.1}}
.card span{{color:#0B6670;font-size:9pt;margin-top:3pt}}
.card i{{color:#5D6480;font-size:9.5pt;margin-top:4pt;font-style:normal}}
ul.cog{{columns:4;list-style:none;margin:6pt 0 0;padding:0;font-size:9.8pt}}ul.cog li{{border-bottom:1px solid #DCDEE9;padding:2pt 0;break-inside:avoid}}ul.cog b{{color:#1E2761;display:block}}
ul.two{{columns:2;margin:4pt 0 0;padding-left:16pt;font-size:9.8pt}}ul.two b{{color:#1E2761}}ul.two i{{color:#5D6480}}
h3{{font-family:Fraunces,Georgia,serif;color:#1E2761;font-size:12.5pt;margin:12pt 0 2pt}}
.pocket{{border:1.5pt solid #1E2761;display:grid;grid-template-columns:1fr 1fr;margin-top:8pt}}
.pocket>div{{padding:12pt 14pt;min-height:3.4in}}
.pocket>div:first-child{{border-right:1.5pt dashed #8E96C4}}
.pocket h4{{margin:0 0 6pt;font-family:Fraunces,Georgia,serif;color:#1E2761;font-size:13pt}}
.pocket .ln{{border-bottom:1px solid #8E96C4;height:18pt}}
.pocket small{{color:#5D6480;font-size:8.5pt}}
.exit{{border:1.5pt solid #0B6670;padding:12pt 14pt;margin-top:12pt}}
.exit h4{{margin:0 0 6pt;font-family:Fraunces,Georgia,serif;color:#0B6670;font-size:13pt}}
.exit .ln{{border-bottom:1px solid #8E96C4;height:20pt}}
.exit p{{margin:6pt 0 0;font-size:10pt;color:#1E2761;font-weight:600}}
.fine{{font-size:8.5pt;color:#5D6480;margin-top:10pt}}
</style></head><body>

<section class="cover">
  <img src="data:image/jpeg;base64,{banner_b64}" alt="">
  <h1>Spanish for Teachers</h1>
  <p class="sub">A free 90-minute teacher-led workshop · Facilitator packet</p>
  <p>Everything needed to run the workshop without a trainer: the agenda and facilitator script, the five pronunciation rules and the name card, every phrase with a say-it key, cut-apart cards, the family-call script, the cognate page, a pocket card, the exit ticket and the six-week follow-up plan. The audio, timers and projector mode are on the web page: <b style="color:#EBD9A0">radan55.github.io/everyteacher/spanish-for-teachers.html</b></p>
  <div class="by"><b>Richard A. Daniel, M.Ed.</b>ENL/EL Specialist · Laurel High School · Laurel, Mississippi · EL Publishing · Free to copy for professional learning</div>
</section>

<section class="page">
  <p class="k">Before people arrive</p><h1>The agenda and the setup</h1>
  <table><thead><tr><th>Start</th><th>Length</th><th>Block</th></tr></thead><tbody>{agenda_rows}</tbody></table>
  <h3>Setup</h3><ul class="prep">{prep}</ul>
  <div class="pr gold"><b>What to say in the first minute</b>Ninety minutes will not make anyone bilingual. It will give you about seventy phrases, five rules that make Spanish readable, and a call-home script. That is enough to change how a student feels in your room on Monday.</div>
  <p class="foot">Spanish for Teachers · EL Publishing · radan55.github.io/everyteacher</p>
</section>

{"".join(f'<section class="page"><p class="k">Facilitator script</p><h1>Blocks {i*2+1} – {i*2+2}</h1>{script_pages[i*2]}{script_pages[i*2+1]}<p class="foot">Spanish for Teachers · EL Publishing · radan55.github.io/everyteacher</p></section>' for i in range(4))}

<section class="page">
  <p class="k">Block 1 · 10 minutes</p><h1>Five rules that make Spanish readable</h1>
  <p class="goal">Spanish is spelled the way it sounds. Learn these five and you can read any phrase in this packet out loud without ever having heard it.</p>
  {rules}
  <h3>The name card — capitals mark the stressed syllable</h3>
  <ul class="names">{names}</ul>
  <p class="fine">Not sure? Ask: <b>¿Cómo se pronuncia tu nombre?</b> (KOH-moh seh proh-NOON-syah too NOHM-breh) — and say it back.</p>
  <p class="foot">Spanish for Teachers · EL Publishing · radan55.github.io/everyteacher</p>
</section>

{phrase_pages}

<section class="page">
  <p class="k">Round 3 · cut apart, one set per table</p><h1>The encouragement deck</h1>
  <div class="cards">{cards}</div>
  <p class="foot">Spanish for Teachers · EL Publishing · radan55.github.io/everyteacher</p>
</section>

<section class="page">
  <p class="k">Block 7 · 5 minutes</p><h1>The cognate shortcut</h1>
  <p class="goal">Roughly three in four academic words in English have a Spanish twin. Your Spanish speakers already own these; you just have to point.</p>
  <ul class="cog">{cog}</ul>
  <h3>Five endings that convert</h3><ul class="two">{pat}</ul>
  <h3>Nine false friends</h3><ul class="two">{false}</ul>
  <h3>Six ten-minute follow-ups</h3>
  <table><thead><tr><th>When</th><th>Focus</th><th>What happens</th></tr></thead><tbody>{follow}</tbody></table>
  <p class="foot">Spanish for Teachers · EL Publishing · radan55.github.io/everyteacher</p>
</section>

<section class="page">
  <p class="k">Block 8 · one per teacher</p><h1>Pocket card and exit ticket</h1>
  <p class="goal">Fold the card on the dashed line. It fits behind a badge.</p>
  <div class="pocket">
    <div><h4>Five phrases I will say this week</h4><div class="ln"></div><div class="ln"></div><div class="ln"></div><div class="ln"></div><div class="ln"></div><br><small>One student I will greet by name:</small><div class="ln"></div><small>One family I will call with good news:</small><div class="ln"></div></div>
    <div><h4>Keep these handy</h4><p style="margin:0;font-size:9.6pt;line-height:1.5"><b>Hola · Buenos días · Mucho gusto</b><br>¿Cómo te llamas? · KOH-moh teh YAH-mahs<br><b>Siéntense · Escuchen · Miren · Escriban</b><br>Levanta la mano · leh-VAHN-tah lah MAH-noh<br><b>Muy bien · Casi · Inténtalo · Sigue así</b><br>¿Necesitas ayuda? · neh-seh-SEE-tahs ah-YOO-dah<br><b>Piénsalo en español. Escríbelo en inglés.</b><br>PYEN-sah-loh en es-pah-NYOL · es-KREE-beh-loh en een-GLES<br><b>Listen for:</b> No entiendo · ¿Qué página? · ¿Me ayuda?<br><b>Call home:</b> Buenas tardes. Soy la maestra / el maestro de ___ de ___. Llamo con buenas noticias.</p><br><small>Five vowels: a=ah e=eh i=ee o=oh u=oo · h silent · j = h · ñ = ny · ll = y</small></div>
  </div>
  <div class="exit"><h4>Exit ticket</h4>
    <p>One phrase I can say now:</p><div class="ln"></div>
    <p>One phrase I will practice this week:</p><div class="ln"></div>
    <p>One thing I want next (a phrase, a situation, a student):</p><div class="ln"></div>
  </div>
  <p class="fine">Spanish reflects widely understood Latin American usage; words vary by country — welcome your students’ versions. Free to copy and share for professional learning. EL Publishing · Richard A. Daniel, M.Ed.</p>
</section>
</body></html>'''


def main():
    PAGE.write_text(page(), encoding="utf-8")
    print("wrote", PAGE.name, PAGE.stat().st_size)
    if "--page" in sys.argv:
        return
    tmp = ROOT / "tools" / "_packet.html"
    tmp.write_text(pdf_html(), encoding="utf-8")
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        pg.goto(tmp.resolve().as_uri(), wait_until="load")
        pg.pdf(path=str(PDF), prefer_css_page_size=True, print_background=True)
        b.close()
    tmp.unlink()
    print("wrote", PDF.name, PDF.stat().st_size)


if __name__ == "__main__":
    main()
