#!/usr/bin/env python3
"""Write podcast.html (players + transcripts) and podcast.xml (RSS) from
tools/podcast.py and the podcast/ep-N.json timings make-podcast.py wrote."""
import json, html, sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import podcast as P

SITE = "https://radan55.github.io/everyteacher/"
e = html.escape
H = P.SERIES["hosts"]

# two questions per episode, for a department meeting or a PLC
TALK = {
 1: ["Pull the four domain scores for one English learner in your class. Which domain is highest, which is lowest, and what does that change about tomorrow?",
     "Where in your lesson does every student produce something in English? If the answer is nowhere, where could it go?"],
 2: ["Name the five words for your next lesson. Which of them are cognates?",
     "Time your longest stretch of uninterrupted teacher talk. What's the three-minute version?"],
 3: ["Write one frame for each of the four lanes for a question you'll ask this week.",
     "Count to five after your next question. What happened?"],
 4: ["Pick the one sentence in next week's reading that will stop a level three. Unpack it on the board in advance.",
     "What would the six-sentence version of that page say?"],
 5: ["Take your next writing prompt and add a word bank, a frame and a model. What changed about who can start?",
     "What is the one thing you'll give feedback on this week — and what will you let go?"],
 6: ["Do you have a copy of the Language Service Plan for each English learner you teach? Who do you ask?",
     "Which of the five people have you not talked to yet this year?"],
}

def mmss(s):
    s = int(round(s)); return f"{s//60}:{s%60:02d}"

def main():
    eps = []
    for ep in P.EPISODES:
        j = ROOT / "podcast" / f"ep-{ep['n']}.json"
        if not j.exists():
            print(f"missing podcast/ep-{ep['n']}.json — run tools/make-podcast.py first"); continue
        d = json.loads(j.read_text(encoding="utf-8")); d["turns"] = ep["turns"]; eps.append(d)
    total = sum(d["duration"] for d in eps)

    # ---------- the page ----------
    cards, trans = [], []
    for d in eps:
        n = d["n"]
        cards.append(f'''<article class="ep" id="ep{n}" data-n="{n}">
  <div class="num">{n}</div>
  <div class="body">
    <h2>{e(d["title"])}</h2>
    <p class="d">{e(d["desc"])}</p>
    <p class="meta"><span>{mmss(d["duration"])}</span><span>{d["bytes"]//1024//1024 or 1} MB</span></p>
    <div class="acts">
      <button type="button" class="play" data-n="{n}" aria-label="Play episode {n}, {e(d["title"])}">▶ Play</button>
      <a class="dl" href="podcast/ep-{n}.mp3" download>Download MP3</a>
      <a class="tr" href="#t{n}">Transcript</a>
    </div>
  </div>
</article>''')
        lines = "".join(
            f'<p class="ln {c["who"]}" data-n="{n}" data-t="{c["t"]}"><b>{e(H[c["who"]][0])}</b><span>{e(c["text"])}</span></p>'
            for c in d["cues"])
        qs = "".join(f"<li>{e(q)}</li>" for q in TALK.get(n, []))
        trans.append(f'''<section class="t" id="t{n}">
  <h3><i>{n}</i>{e(d["title"])} <small>{mmss(d["duration"])}</small></h3>
  <div class="talk"><b>Talk about it</b><ol>{qs}</ol></div>
  <div class="lines">{lines}</div>
</section>''')

    cues_json = json.dumps([{"n": d["n"], "title": d["title"], "src": f"podcast/ep-{d['n']}.mp3",
                             "dur": d["duration"], "cues": [[c["who"], c["t"]] for c in d["cues"]]} for d in eps])
    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Every Teacher · the podcast · EL Publishing</title>
<meta name="description" content="{e(P.SERIES["desc"])}">
<link rel="alternate" type="application/rss+xml" title="Every Teacher" href="{SITE}podcast.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,700;1,9..144,600&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  :root{{--navy:#1E2761;--navy-bg:var(--navy);--navy-dk:#141A44;--navy-dk-bg:var(--navy-dk);--gold:#C9A227;--gold-lt:#EBD9A0;--gold-ink:#7A5F0E;--paper:#fff;--mist:#F4F5FA;--ink:#1F2340;--muted:#5B6078;--rule:#E3E5EF;--wash:#F7F1DC}}
  *{{box-sizing:border-box}}
  body{{margin:0;background:var(--mist);color:var(--ink);font-family:"Source Sans 3",-apple-system,"Segoe UI",sans-serif;font-size:16px;line-height:1.5}}
  a{{color:var(--navy)}}
  header{{background:var(--navy-bg);color:#fff;position:relative;overflow:hidden}}
  header::before{{content:"";position:absolute;inset:0;background:repeating-linear-gradient(112deg,rgba(235,217,160,.09) 0 2px,transparent 2px 24px)}}
  .head-in{{position:relative;max-width:1000px;margin:0 auto;padding:40px 22px 34px;display:grid;grid-template-columns:1fr 220px;gap:30px;align-items:center}}
  .brand{{font-size:12px;letter-spacing:.2em;color:var(--gold);font-weight:600;margin:0 0 14px}}
  .brand a{{color:var(--gold);text-decoration:none}}
  h1{{font-family:Fraunces,Georgia,serif;font-weight:700;letter-spacing:-.02em;font-size:clamp(32px,5.5vw,52px);line-height:1.02;margin:0}}
  h1 em{{font-style:italic;font-weight:600;color:var(--gold)}}
  .tag{{margin:14px 0 0;font-size:16.5px;color:#C9CEEA;max-width:60ch}}
  .tag b{{color:#fff;font-weight:600}}
  .cover{{width:220px;height:220px;border-radius:14px;box-shadow:0 20px 50px rgba(0,0,0,.45);display:block}}
  .hosts{{margin:16px 0 0;font-size:14px;color:#C9CEEA}}
  .hosts b{{color:#fff}}
  .player{{position:sticky;top:0;z-index:6;background:var(--navy-dk-bg);color:#fff;border-bottom:1px solid rgba(255,255,255,.12)}}
  .player[hidden]{{display:none}}
  .p-in{{max-width:1000px;margin:0 auto;padding:10px 22px;display:grid;grid-template-columns:auto 1fr auto;gap:14px;align-items:center}}
  .p-in button{{font:inherit;border:0;cursor:pointer;border-radius:999px}}
  #pp{{width:44px;height:44px;background:var(--gold);color:var(--navy-dk);font-size:18px;font-weight:700}}
  .p-mid{{min-width:0}}
  .p-mid b{{display:block;font-family:Fraunces,Georgia,serif;font-size:15px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
  .p-row{{display:flex;align-items:center;gap:10px;font-size:12px;color:#AEB5DA;font-variant-numeric:tabular-nums}}
  #seek{{flex:1;accent-color:var(--gold);margin:0}}
  .p-end{{display:flex;gap:6px}}
  .p-end button{{background:rgba(255,255,255,.1);color:#fff;font-size:13px;font-weight:600;padding:7px 11px}}
  .p-end button[aria-pressed="true"]{{background:var(--gold);color:var(--navy-dk)}}
  main{{max-width:1000px;margin:0 auto;padding:26px 22px 40px}}
  .lede{{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin:0 0 26px}}
  .box{{background:var(--paper);border:1px solid var(--rule);border-radius:10px;padding:16px 20px;font-size:15px}}
  .box h2{{font-family:Fraunces,Georgia,serif;font-size:19px;color:var(--navy);margin:0 0 6px}}
  .box p{{margin:0 0 8px}} .box p:last-child{{margin:0}}
  .box code{{background:var(--mist);padding:2px 6px;border-radius:4px;font-size:13px;word-break:break-all}}
  .box .cp{{font:inherit;font-size:13px;font-weight:700;border:0;background:var(--gold);color:var(--navy-dk);padding:5px 11px;border-radius:999px;cursor:pointer;margin-left:6px}}
  .eps{{display:grid;gap:12px}}
  .ep{{display:grid;grid-template-columns:64px 1fr;gap:14px;background:var(--paper);border:1px solid var(--rule);border-radius:12px;padding:16px 18px}}
  .ep.now{{border-color:var(--gold);box-shadow:0 0 0 3px var(--wash)}}
  .num{{font-family:Fraunces,Georgia,serif;font-size:40px;font-weight:700;color:var(--gold);line-height:1;padding-top:4px}}
  .ep h2{{font-family:Fraunces,Georgia,serif;font-size:23px;color:var(--navy);margin:0 0 4px;letter-spacing:-.01em}}
  .ep .d{{margin:0 0 8px;font-size:15px}}
  .meta{{margin:0 0 10px;font-size:13px;color:var(--muted);display:flex;gap:12px}}
  .acts{{display:flex;gap:8px;flex-wrap:wrap;align-items:center}}
  .acts .play{{font:inherit;font-size:14px;font-weight:700;border:0;background:var(--navy-bg);color:#fff;padding:8px 16px;border-radius:999px;cursor:pointer}}
  .ep.now .acts .play{{background:var(--gold);color:var(--navy-dk)}}
  .acts a{{font-size:14px;font-weight:600;color:var(--navy);text-decoration:none;border:1px solid var(--rule);padding:7px 13px;border-radius:999px;background:var(--paper)}}
  .acts a:hover{{border-color:var(--gold)}}
  h2.sec{{font-family:Fraunces,Georgia,serif;font-size:26px;color:var(--navy);margin:40px 0 6px}}
  .sub{{color:var(--muted);margin:0 0 16px;font-size:15px}}
  .t{{background:var(--paper);border:1px solid var(--rule);border-radius:12px;padding:18px 22px;margin:0 0 14px}}
  .t h3{{font-family:Fraunces,Georgia,serif;font-size:21px;color:var(--navy);margin:0 0 10px;display:flex;align-items:baseline;gap:10px}}
  .t h3 i{{font-style:normal;color:var(--gold);font-size:26px}}
  .t h3 small{{font-size:13px;color:var(--muted);font-family:"Source Sans 3",sans-serif;font-weight:400}}
  .talk{{background:var(--wash);border-radius:8px;padding:10px 16px 8px;font-size:14.5px;margin:0 0 12px}}
  .talk b{{color:var(--gold-ink);font-size:12px;letter-spacing:.12em;text-transform:uppercase}}
  .talk ol{{margin:4px 0 0;padding-left:20px}}
  .ln{{display:grid;grid-template-columns:72px 1fr;gap:10px;margin:0;padding:6px 8px;border-radius:6px;cursor:pointer;font-size:15.5px}}
  .ln:hover{{background:var(--mist)}}
  .ln.now{{background:var(--wash)}}
  .ln b{{font-size:12px;letter-spacing:.08em;text-transform:uppercase;padding-top:3px}}
  .ln.M b{{color:var(--navy)}} .ln.E b{{color:var(--gold-ink)}}
  footer{{background:var(--navy-dk-bg);color:#AEB5DA;padding:26px 0;font-size:14px}}
  footer .wrap{{max-width:1000px;margin:0 auto;padding:0 22px}}
  footer b{{display:block;color:#fff;font-family:Fraunces,Georgia,serif;font-size:19px;font-weight:600}}
  footer a{{color:var(--gold)}}
  .toast{{position:fixed;bottom:18px;left:50%;transform:translateX(-50%);background:var(--navy-bg);color:#fff;padding:8px 16px;border-radius:999px;font-size:14px;opacity:0;transition:opacity .2s;pointer-events:none}}
  .toast.on{{opacity:1}}
  @media(max-width:760px){{.head-in{{grid-template-columns:1fr}}.cover{{width:150px;height:150px}}.lede{{grid-template-columns:1fr}}.p-end{{display:none}}.p-in{{grid-template-columns:auto 1fr}}.ln{{grid-template-columns:1fr}}.ln b{{padding:0}}}}
  @media print{{header,.player,.acts,footer{{display:none}}.ep,.t{{border:1px solid #bbb;break-inside:avoid}}}}
</style>
</head>
<body>
<header>
  <div class="head-in">
    <div>
      <p class="brand"><a href="index.html">EL PUBLISHING</a> · FOR EVERY CONTENT TEACHER · PODCAST</p>
      <h1>Every Teacher<em>.</em> <span style="font-weight:600;font-size:.62em;display:block;margin-top:6px;color:#C9CEEA">{e(P.SERIES["subtitle"])}</span></h1>
      <p class="tag">Six conversations, five to six minutes each, for the teacher who teaches <b>content, not English</b> and has English learners in the room. What Emerging and Progressing students can do, what to change tomorrow, and what to stop worrying about.</p>
      <p class="hosts"><b>{e(H["M"][0])}</b> teaches {e(H["M"][1])}. <b>{e(H["E"][0])}</b> is the {e(H["E"][1])}. Both voices are synthesized; the scripts are written and edited by Richard A. Daniel, M.Ed.</p>
    </div>
    <img class="cover" src="podcast/cover-600.jpg" width="220" height="220" alt="Every Teacher podcast cover">
  </div>
</header>

<div class="player" id="player" hidden>
  <div class="p-in">
    <button type="button" id="pp" aria-label="Play or pause">▶</button>
    <div class="p-mid"><b id="p-title">—</b>
      <div class="p-row"><span id="p-cur">0:00</span><input type="range" id="seek" min="0" max="1000" value="0" aria-label="Seek"><span id="p-dur">0:00</span></div>
    </div>
    <div class="p-end">
      <button type="button" id="prev" aria-label="Previous episode">‹</button>
      <button type="button" class="spd" data-s="1" aria-pressed="true">1×</button>
      <button type="button" class="spd" data-s="1.25" aria-pressed="false">1.25×</button>
      <button type="button" class="spd" data-s="1.5" aria-pressed="false">1.5×</button>
      <button type="button" id="next" aria-label="Next episode">›</button>
    </div>
  </div>
  <audio id="audio" preload="none"></audio>
</div>

<main>
  <div class="lede">
    <div class="box">
      <h2>How to use it</h2>
      <p>One episode a week at a department meeting is a six-week PD series with no slides to make: play it, then take the two <em>Talk about it</em> questions under the transcript. Or listen in the car; the whole series is {int(total//60)} minutes.</p>
      <p>Every tool the episodes mention is on this hub and free: <a href="cognate-hunt.html">Cognate Hunt</a>, the <a href="sentence-frames.html">Sentence-Frame Bank</a>, the leveled readables, the <a href="parent-letters.html">parent letters</a> and the <a href="lsp-builder.html">LSP Builder</a>.</p>
    </div>
    <div class="box">
      <h2>Subscribe in a podcast app</h2>
      <p>Paste this feed address into Apple Podcasts (Library → Follow a show by URL), Pocket Casts, Overcast or any app that takes an RSS link:</p>
      <p><code id="feed">{SITE}podcast.xml</code><button type="button" class="cp" id="cpfeed">Copy</button></p>
      <p>Or just press play here. Each episode also downloads as an MP3 for a shared drive.</p>
    </div>
  </div>

  <div class="eps" id="eps">
{chr(10).join(cards)}
  </div>

  <h2 class="sec">Transcripts</h2>
  <p class="sub">Click any line to jump the audio to it. The line being spoken is highlighted while an episode plays.</p>
{chr(10).join(trans)}
</main>
<footer><div class="wrap"><b>Richard A. Daniel, M.Ed.</b>ENL/EL Specialist · Laurel High School · Laurel, Mississippi · <a href="index.html">All EL Publishing resources →</a></div></footer>
<div class="toast" id="toast">Copied</div>
<script>
(function(){{
  var EP={cues_json};
  var $=function(s){{return document.querySelector(s)}};
  var audio=$('#audio'),player=$('#player'),pp=$('#pp'),seek=$('#seek'),cur=0,seeking=false;
  function mm(s){{s=Math.max(0,Math.round(s));return Math.floor(s/60)+':'+('0'+s%60).slice(-2)}}
  function load(i,go){{cur=i;var d=EP[i];player.hidden=false;audio.src=d.src;$('#p-title').textContent='Ep. '+d.n+' · '+d.title;$('#p-dur').textContent=mm(d.dur);
    document.querySelectorAll('.ep').forEach(function(x){{x.classList.toggle('now',+x.dataset.n===d.n)}});
    document.querySelectorAll('.ep .play').forEach(function(b){{b.textContent=(+b.dataset.n===d.n)?'▶ Playing':'▶ Play'}});
    if(go){{audio.play().catch(function(){{}})}}
    try{{history.replaceState(null,'','#ep'+d.n)}}catch(e){{}}}}
  function byN(n){{for(var i=0;i<EP.length;i++)if(EP[i].n===n)return i;return 0}}
  document.querySelectorAll('.ep .play').forEach(function(b){{b.addEventListener('click',function(){{var i=byN(+b.dataset.n);
    if(i===cur&&!player.hidden){{audio.paused?audio.play():audio.pause()}}else load(i,true)}})}});
  pp.addEventListener('click',function(){{audio.paused?audio.play():audio.pause()}});
  audio.addEventListener('play',function(){{pp.textContent='❚❚';var b=document.querySelector('.ep.now .play');if(b)b.textContent='❚❚ Pause'}});
  audio.addEventListener('pause',function(){{pp.textContent='▶';var b=document.querySelector('.ep.now .play');if(b)b.textContent='▶ Play'}});
  audio.addEventListener('ended',function(){{if(cur<EP.length-1)load(cur+1,true)}});
  audio.addEventListener('timeupdate',function(){{var d=EP[cur];if(!seeking)seek.value=Math.round(audio.currentTime/d.dur*1000);$('#p-cur').textContent=mm(audio.currentTime);
    var c=d.cues,k=-1;for(var i=0;i<c.length;i++){{if(c[i][1]<=audio.currentTime+.15)k=i}}
    var lines=document.querySelectorAll('.ln[data-n="'+d.n+'"]');
    document.querySelectorAll('.ln.now').forEach(function(x){{if(x.dataset.n!==String(d.n)||x!==lines[k])x.classList.remove('now')}});
    if(k>=0&&lines[k]&&!lines[k].classList.contains('now')){{lines[k].classList.add('now')}}}});
  seek.addEventListener('input',function(){{seeking=true;$('#p-cur').textContent=mm(seek.value/1000*EP[cur].dur)}});
  seek.addEventListener('change',function(){{audio.currentTime=seek.value/1000*EP[cur].dur;seeking=false}});
  $('#prev').addEventListener('click',function(){{load(Math.max(0,cur-1),true)}});
  $('#next').addEventListener('click',function(){{load(Math.min(EP.length-1,cur+1),true)}});
  document.querySelectorAll('.spd').forEach(function(b){{b.addEventListener('click',function(){{audio.playbackRate=+b.dataset.s;document.querySelectorAll('.spd').forEach(function(x){{x.setAttribute('aria-pressed',x===b?'true':'false')}})}})}});
  document.querySelectorAll('.ln').forEach(function(l){{l.addEventListener('click',function(){{var i=byN(+l.dataset.n);if(i!==cur||player.hidden)load(i,false);
    var go=function(){{audio.currentTime=+l.dataset.t;audio.play().catch(function(){{}})}};
    if(audio.readyState>=1)go();else audio.addEventListener('loadedmetadata',go,{{once:true}});audio.load()}})}});
  $('#cpfeed').addEventListener('click',function(){{var t=$('#feed').textContent;(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){{var x=$('#toast');x.classList.add('on');setTimeout(function(){{x.classList.remove('on')}},1200)}},function(){{prompt('Copy:',t)}})}});
  var m=location.hash.match(/^#ep(\\d+)$/);if(m)load(byN(+m[1]),false);
  document.addEventListener('keydown',function(ev){{if(ev.key===' '&&!player.hidden&&!/input|button|a/i.test(document.activeElement.tagName)){{ev.preventDefault();pp.click()}}}});
}})();
</script>
<script data-goatcounter="https://elpublishing.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
<script src="guide.js" defer></script>
<script src="hub-chrome.js" defer></script>
</body>
</html>
'''
    (ROOT / "podcast.html").write_text(page, encoding="utf-8")

    # ---------- the feed ----------
    base = datetime(2026, 10, 12, 12, 0, tzinfo=timezone.utc)   # Monday; one a week
    items = []
    for d in eps:
        n = d["n"]; pub = base + timedelta(days=7 * (n - 1))
        items.append(f'''  <item>
   <title>{e(f"{n}. {d['title']}")}</title>
   <itunes:title>{e(d["title"])}</itunes:title>
   <itunes:episode>{n}</itunes:episode>
   <itunes:episodeType>full</itunes:episodeType>
   <description>{e(d["desc"])}</description>
   <itunes:summary>{e(d["desc"])}</itunes:summary>
   <link>{SITE}podcast.html#ep{n}</link>
   <guid isPermaLink="false">elpublishing-everyteacher-ep{n}</guid>
   <pubDate>{pub.strftime("%a, %d %b %Y %H:%M:%S +0000")}</pubDate>
   <enclosure url="{SITE}podcast/ep-{n}.mp3" length="{d["bytes"]}" type="audio/mpeg"/>
   <itunes:duration>{int(d["duration"])}</itunes:duration>
   <itunes:explicit>false</itunes:explicit>
   <itunes:image href="{SITE}podcast/cover-3000.jpg"/>
  </item>''')
    feed = f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:podcast="https://podcastindex.org/namespace/1.0">
 <channel>
  <title>Every Teacher</title>
  <link>{SITE}podcast.html</link>
  <atom:link href="{SITE}podcast.xml" rel="self" type="application/rss+xml"/>
  <language>en-us</language>
  <copyright>© 2026 Richard A. Daniel · EL Publishing · free for any school to use</copyright>
  <description>{e(P.SERIES["desc"])}</description>
  <itunes:subtitle>{e(P.SERIES["subtitle"])}</itunes:subtitle>
  <itunes:summary>{e(P.SERIES["desc"])}</itunes:summary>
  <itunes:author>EL Publishing</itunes:author>
  <itunes:owner><itunes:name>Richard A. Daniel</itunes:name><itunes:email>{P.SERIES["email"]}</itunes:email></itunes:owner>
  <itunes:image href="{SITE}podcast/cover-3000.jpg"/>
  <image><url>{SITE}podcast/cover-3000.jpg</url><title>Every Teacher</title><link>{SITE}podcast.html</link></image>
  <itunes:category text="Education"><itunes:category text="How To"/></itunes:category>
  <itunes:explicit>false</itunes:explicit>
  <itunes:type>serial</itunes:type>
  <podcast:locked>no</podcast:locked>
{chr(10).join(items)}
 </channel>
</rss>
'''
    (ROOT / "podcast.xml").write_text(feed, encoding="utf-8")
    print(f"wrote podcast.html + podcast.xml — {len(eps)} episodes, {total/60:.0f} min")

if __name__ == "__main__":
    main()
