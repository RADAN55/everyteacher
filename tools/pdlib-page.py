#!/usr/bin/env python3
"""Write pd-library.html from tools/pdlib.py."""
import html, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import pdlib as L

e = html.escape

def check():
    ids = [i[0] for i in L.ITEMS]
    assert len(ids) == len(set(ids)), "duplicate item id"
    for it in L.ITEMS:
        href = it[2]
        if not href.startswith("http"):
            f = href.split("#")[0].rstrip("/")
            p = ROOT / (f + ("/index.html" if (ROOT / f).is_dir() else ""))
            assert p.exists(), f"missing page: {href}"
        assert it[8] in L.SHELF_NAME, it[0]
        assert it[4] in L.KINDS, it[0]
    for t, who, items in L.PATHS:
        for i in items:
            assert i in ids, f"path {t}: unknown item {i}"

def main():
    check()
    by = {k: [] for k, _, _ in L.SHELVES}
    for it in L.ITEMS:
        by[it[8]].append(it)
    total_min = sum(i[5] for i in L.ITEMS)
    n_out = sum(1 for i in L.ITEMS if i[2].startswith("http") and "radan55" not in i[2])

    def card(it):
        id_, title, href, src, kind, mins, grades, levels, shelf, why, then = it
        ext = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
        gl = " ".join(f'<i>{e(dict(L.GRADES)[g])}</i>' for g in grades.split())
        ll = " ".join(f'<i class="lv{l}">{e(dict(L.LEVELS)[l].split(" ·")[0])}</i>' for l in levels.split())
        return f'''<article class="it" id="it-{id_}" data-id="{id_}" data-g="{grades}" data-l="{levels}" data-k="{kind}" data-m="{mins}" data-s="{shelf}" data-t="{e((title+' '+src+' '+why+' '+then).lower())}">
  <div class="top"><span class="kind k-{kind}">{kind}</span><span class="min">{mins} min</span><label class="done"><input type="checkbox" data-done="{id_}" aria-label="Mark done: {e(title)}"> Done</label></div>
  <h3><a href="{e(href)}"{ext}>{e(title)}</a></h3>
  <p class="src">{e(src)}</p>
  <p class="why">{e(why)}</p>
  <p class="then"><b>Then, in your room:</b> {e(then)}</p>
  <p class="tags">{gl}<span class="sep"></span>{ll}</p>
</article>'''

    shelves = "".join(
        f'<section class="shelf" id="s-{k}" data-s="{k}"><h2>{e(n)}</h2><p class="sd">{e(d)}</p><div class="grid">'
        + "".join(card(it) for it in by[k]) + '</div></section>'
        for k, n, d in L.SHELVES)

    items_by_id = {i[0]: i for i in L.ITEMS}
    paths = "".join(
        f'''<article class="path"><h3>{e(t)}</h3><p>{e(who)} <b>{sum(items_by_id[i][5] for i in ids)} min.</b></p><ol>'''
        + "".join(f'<li><a href="#it-{i}" data-jump="{i}">{e(items_by_id[i][1])}</a> <small>{items_by_id[i][5]} min</small></li>' for i in ids)
        + '</ol></article>'
        for t, who, ids in L.PATHS)

    meta = json.dumps({i[0]: {"t": i[1], "m": i[5]} for i in L.ITEMS})

    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The PD Library · English learners for content teachers, K–12 · EL Publishing</title>
<meta name="description" content="A professional-learning library for the biology, algebra and history teacher with English learners: {len(L.ITEMS)} pieces of PD on eight shelves, filterable by grade band K–12 and language level (Emerging, Progressing, Proficient), each under 60 minutes with a thing to do in your own classroom afterward. Seven guided paths, a done-list and a printable PD log.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,700;1,9..144,600&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  :root{{--navy:#1E2761;--navy-bg:var(--navy);--navy-dk:#141A44;--navy-dk-bg:var(--navy-dk);--gold:#C9A227;--gold-lt:#EBD9A0;--gold-ink:#7A5F0E;--paper:#fff;--mist:#F4F5FA;--ink:#1F2340;--muted:#5B6078;--rule:#E3E5EF;--wash:#F7F1DC;--teal:#17606F;--teal-lt:#E3F1F4;--ok:#2E7D4F;--ok-lt:#E6F3EA}}
  *{{box-sizing:border-box}}
  body{{margin:0;background:var(--mist);color:var(--ink);font-family:"Source Sans 3",-apple-system,"Segoe UI",sans-serif;font-size:16px;line-height:1.5}}
  a{{color:var(--navy)}}
  header{{background:var(--navy-bg);color:#fff;position:relative;overflow:hidden}}
  header::before{{content:"";position:absolute;inset:0;background:repeating-linear-gradient(112deg,rgba(235,217,160,.09) 0 2px,transparent 2px 24px)}}
  .head-in{{position:relative;max-width:1100px;margin:0 auto;padding:40px 22px 30px}}
  .brand{{font-size:12px;letter-spacing:.2em;color:var(--gold);font-weight:600;margin:0 0 14px}}
  .brand a{{color:var(--gold);text-decoration:none}}
  h1{{font-family:Fraunces,Georgia,serif;font-weight:700;letter-spacing:-.02em;font-size:clamp(30px,5.5vw,50px);line-height:1.02;margin:0}}
  h1 em{{font-style:italic;font-weight:600;color:var(--gold)}}
  .tag{{margin:14px 0 0;font-size:16.5px;color:#C9CEEA;max-width:66ch}}
  .tag b{{color:#fff;font-weight:600}}
  .stats{{display:flex;gap:26px;flex-wrap:wrap;margin:20px 0 0}}
  .stats div{{font-size:13px;color:#AEB5DA}} .stats b{{display:block;font-family:Fraunces,Georgia,serif;font-size:26px;color:var(--gold);line-height:1}}
  .bar{{position:sticky;top:0;z-index:5;background:var(--paper);border-bottom:1px solid var(--rule)}}
  .bar-in{{max-width:1100px;margin:0 auto;padding:10px 22px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}}
  .srch{{display:flex;align-items:center;gap:8px;border:1px solid var(--rule);border-radius:999px;padding:6px 12px;flex:1 1 220px}}
  .srch input{{border:0;font:inherit;font-size:14px;outline:none;flex:1;min-width:0;background:transparent;color:inherit}}
  .grp{{display:flex;gap:4px;flex-wrap:wrap;align-items:center}}
  .grp span{{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-right:2px}}
  .grp button{{font:inherit;font-size:13px;font-weight:600;border:1px solid var(--rule);background:var(--paper);color:var(--navy);padding:5px 11px;border-radius:999px;cursor:pointer}}
  .grp button[aria-pressed="true"]{{background:var(--navy-bg);color:#fff;border-color:var(--navy)}}
  .grp.lv button[aria-pressed="true"]{{background:var(--gold);color:var(--navy-dk);border-color:var(--gold)}}
  .cnt{{font-size:13px;color:var(--muted);margin-left:auto}}
  main{{max-width:1100px;margin:0 auto;padding:22px 22px 40px}}
  .paths{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px;margin:0 0 30px}}
  .path{{background:var(--paper);border:1px solid var(--rule);border-radius:12px;padding:14px 18px}}
  .path h3{{font-family:Fraunces,Georgia,serif;font-size:19px;color:var(--navy);margin:0 0 4px}}
  .path p{{font-size:14px;color:var(--muted);margin:0 0 8px}} .path p b{{color:var(--gold-ink)}}
  .path ol{{margin:0;padding-left:20px;font-size:14px}} .path li{{margin:2px 0}} .path small{{color:var(--muted)}}
  h2.sec{{font-family:Fraunces,Georgia,serif;font-size:24px;color:var(--navy);margin:0 0 4px}}
  .sub{{color:var(--muted);margin:0 0 14px;font-size:15px}}
  .shelf{{margin:0 0 30px}}
  .shelf h2{{font-family:Fraunces,Georgia,serif;font-size:24px;color:var(--navy);margin:0;padding-top:10px;border-top:3px solid var(--gold);display:inline-block}}
  .shelf .sd{{font-size:15px;color:var(--muted);margin:4px 0 12px}}
  .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}}
  .it{{background:var(--paper);border:1px solid var(--rule);border-radius:12px;padding:14px 16px 12px;display:flex;flex-direction:column;gap:4px}}
  .it.isdone{{background:var(--ok-lt);border-color:#BFE0CA}}
  .it .top{{display:flex;align-items:center;gap:8px;font-size:12px}}
  .kind{{font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:2px 8px;border-radius:5px;background:var(--mist);color:var(--navy)}}
  .k-Listen{{background:var(--wash);color:var(--gold-ink)}} .k-Do{{background:var(--teal-lt);color:var(--teal)}} .k-Watch{{background:#EEE9FA;color:#5B3FA8}} .k-Print{{background:var(--mist)}} .k-Plan{{background:#FCEBE4;color:#9A4C2E}}
  .min{{color:var(--muted)}}
  .done{{margin-left:auto;color:var(--muted);cursor:pointer;display:flex;align-items:center;gap:4px}} .done input{{accent-color:var(--ok)}}
  .it h3{{font-family:Fraunces,Georgia,serif;font-size:18px;line-height:1.2;margin:4px 0 0}}
  .it h3 a{{text-decoration:none}} .it h3 a:hover{{text-decoration:underline}}
  .src{{font-size:12.5px;color:var(--muted);margin:0}}
  .why{{font-size:14.5px;margin:4px 0 0}}
  .then{{font-size:13.5px;margin:4px 0 0;padding:8px 10px;background:var(--mist);border-radius:6px;border-left:3px solid var(--gold)}}
  .then b{{color:var(--gold-ink);font-size:11px;letter-spacing:.1em;text-transform:uppercase;display:block;margin-bottom:2px}}
  .tags{{margin:6px 0 0;display:flex;flex-wrap:wrap;gap:4px;align-items:center}}
  .tags i{{font-style:normal;font-size:11.5px;padding:1px 7px;border-radius:999px;border:1px solid var(--rule);color:var(--muted)}}
  .tags .sep{{width:6px}}
  .tags .lve{{border-color:#E3C66A;color:var(--gold-ink)}} .tags .lvp{{border-color:#9FC4CC;color:var(--teal)}} .tags .lvm{{border-color:#BFE0CA;color:var(--ok)}}
  .hide{{display:none!important}}
  .log{{background:var(--paper);border:1px solid var(--rule);border-radius:12px;padding:16px 20px;margin:0 0 30px;display:flex;gap:16px;align-items:center;flex-wrap:wrap}}
  .log b{{font-family:Fraunces,Georgia,serif;font-size:22px;color:var(--navy)}}
  .log .n{{font-size:14px;color:var(--muted)}}
  .act{{font:inherit;font-size:13.5px;font-weight:700;border:0;background:var(--gold);color:var(--navy-dk);padding:8px 14px;border-radius:999px;cursor:pointer}}
  .act.q{{background:var(--paper);border:1px solid var(--rule);color:var(--navy)}}
  .note{{font-size:13px;color:var(--muted);margin:0}}
  footer{{background:var(--navy-dk-bg);color:#AEB5DA;padding:26px 0;font-size:14px}}
  footer .wrap{{max-width:1100px;margin:0 auto;padding:0 22px}}
  footer b{{display:block;color:#fff;font-family:Fraunces,Georgia,serif;font-size:19px;font-weight:600}}
  footer a{{color:var(--gold)}}
  #printlog{{display:none}}
  @media(max-width:760px){{.cnt{{margin-left:0;flex-basis:100%}}}}
  @media print{{header,.bar,main>*:not(#printlog),footer{{display:none!important}}body{{background:#fff}}#printlog{{display:block;font-size:12.5pt}}#printlog h1{{font-size:22pt;color:#000}}#printlog table{{width:100%;border-collapse:collapse;margin-top:12px}}#printlog th,#printlog td{{border-bottom:1px solid #999;text-align:left;padding:6px 4px;vertical-align:top}}#printlog .sig{{margin-top:40px;display:grid;grid-template-columns:1fr 1fr;gap:30px}}#printlog .sig div{{border-top:1px solid #000;padding-top:4px;font-size:10.5pt}}}}
</style>
</head>
<body>
<header>
  <div class="head-in">
    <p class="brand"><a href="index.html">EL PUBLISHING</a> · FOR EVERY CONTENT TEACHER · PD LIBRARY · K–12</p>
    <h1>The PD <em>library.</em></h1>
    <p class="tag">Professional learning for the teacher who teaches <b>content, not English</b> and has English learners in the room. Eight shelves, every grade band, every language level, nothing over an hour — and every piece ends with <b>the thing to do in your own classroom</b>, because that is the PD. Tick what you finish; print the log for your district's records.</p>
    <div class="stats"><div><b>{len(L.ITEMS)}</b>pieces of PD</div><div><b>8</b>shelves</div><div><b>{len(L.PATHS)}</b>guided paths</div><div><b>{total_min//60}h</b>in all, {n_out} from outside EL Publishing</div><div><b>$0</b>no login, nothing to join</div></div>
  </div>
</header>
<nav class="bar" aria-label="Filter the library"><div class="bar-in">
  <label class="srch"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg><input type="search" id="q" placeholder="Search the library… (frames, newcomer, grading)" aria-label="Search the library"></label>
  <div class="grp" id="gr"><span>Grade</span>{"".join(f'<button type="button" data-g="{g}" aria-pressed="true">{e(n)}</button>' for g,n in L.GRADES)}</div>
  <div class="grp lv" id="lv"><span>Level</span>{"".join(f'<button type="button" data-l="{l}" aria-pressed="true">{e(n.split(" ·")[0])}</button>' for l,n in L.LEVELS)}</div>
  <div class="grp" id="kd"><span>Kind</span>{"".join(f'<button type="button" data-k="{k}" aria-pressed="true">{k}</button>' for k in L.KINDS)}</div>
  <div class="grp" id="tm"><span>Time</span><button type="button" data-m="15" aria-pressed="false">≤ 15 min</button><button type="button" data-hide-done="1" aria-pressed="false">Hide done</button></div>
  <p class="cnt" id="cnt"></p>
</div></nav>
<main>
  <div class="log" id="log">
    <div><b><span id="done-n">0</span> done · <span id="done-m">0</span> min</b><div class="n">Your done-list lives in this browser only. Nothing is sent anywhere.</div></div>
    <button type="button" class="act" id="printbtn">🖨 Print my PD log</button>
    <button type="button" class="act q" id="clearbtn">Clear</button>
    <p class="note">The log is a record for you and your district's PD documentation; whether it earns credit is your district's call.</p>
  </div>

  <h2 class="sec">Guided paths</h2>
  <p class="sub">Don't know where to start? Pick the sentence that sounds like you. Each path is in order.</p>
  <div class="paths">{paths}</div>

  <h2 class="sec">The shelves</h2>
  <p class="sub">Filter by your grade band and your students' levels above. Everything stays filtered as you scroll.</p>
{shelves}
  <section id="printlog" aria-hidden="true">
    <h1>Professional learning log · English learners for content teachers</h1>
    <p>Name: ______________________________ &nbsp; School: ______________________________ &nbsp; Printed: <span id="pl-date"></span></p>
    <p>Source: The PD Library, EL Publishing — radan55.github.io/everyteacher/pd-library.html. Each item is self-paced; times are the publisher's estimates.</p>
    <table><thead><tr><th>Completed</th><th>Title</th><th>Shelf</th><th>Minutes</th></tr></thead><tbody id="pl-rows"></tbody>
    <tfoot><tr><th colspan="3">Total</th><th id="pl-total"></th></tr></tfoot></table>
    <div class="sig"><div>Teacher signature · date</div><div>Administrator · date</div></div>
  </section>
</main>
<footer><div class="wrap"><b>Richard A. Daniel, M.Ed.</b>ENL/EL Specialist · Laurel High School · Laurel, Mississippi · <a href="index.html">All EL Publishing resources →</a></div></footer>
<script>
(function(){{
  var META={meta};
  var SHELF={json.dumps(L.SHELF_NAME)};
  var KEY='elhub.pdlog';
  var log={{}};try{{log=JSON.parse(localStorage.getItem(KEY)||'{{}}')||{{}}}}catch(e){{}}
  function save(){{try{{localStorage.setItem(KEY,JSON.stringify(log))}}catch(e){{}}}}
  var items=[].slice.call(document.querySelectorAll('.it'));
  var G=new Set(['k2','g35','g68','g912']),LV=new Set(['e','p','m']),K=new Set({json.dumps(L.KINDS)}),MAXM=0,HIDE=false;
  var q=document.getElementById('q');
  function run(){{var s=q.value.trim().toLowerCase(),n=0;
    items.forEach(function(it){{var g=it.dataset.g.split(' '),l=it.dataset.l.split(' ');
      var ok=g.some(function(x){{return G.has(x)}})&&l.some(function(x){{return LV.has(x)}})&&K.has(it.dataset.k)&&(!MAXM||+it.dataset.m<=MAXM)&&(!s||it.dataset.t.indexOf(s)>=0)&&!(HIDE&&log[it.dataset.id]);
      it.classList.toggle('hide',!ok);if(ok)n++}});
    document.querySelectorAll('.shelf').forEach(function(sh){{sh.classList.toggle('hide',!sh.querySelector('.it:not(.hide)'))}});
    document.getElementById('cnt').textContent=n+' of '+items.length+' shown';}}
  function tog(id,set,attr){{document.getElementById(id).addEventListener('click',function(e){{var b=e.target.closest('button');if(!b||!(attr in b.dataset))return;
    var on=b.getAttribute('aria-pressed')!=='true';b.setAttribute('aria-pressed',on);on?set.add(b.dataset[attr]):set.delete(b.dataset[attr]);run()}})}}
  tog('gr',G,'g');tog('lv',LV,'l');tog('kd',K,'k');
  document.getElementById('tm').addEventListener('click',function(e){{var b=e.target.closest('button');if(!b)return;var on=b.getAttribute('aria-pressed')!=='true';b.setAttribute('aria-pressed',on);
    if(b.dataset.m)MAXM=on?+b.dataset.m:0;else HIDE=on;run()}});
  q.addEventListener('input',run);
  // done-list
  function paint(){{var n=0,m=0;items.forEach(function(it){{var id=it.dataset.id,d=!!log[id];it.classList.toggle('isdone',d);it.querySelector('[data-done]').checked=d;if(d){{n++;m+=META[id].m}}}});
    document.getElementById('done-n').textContent=n;document.getElementById('done-m').textContent=m}}
  document.addEventListener('change',function(e){{var c=e.target.closest('[data-done]');if(!c)return;var id=c.dataset.done;if(c.checked)log[id]=new Date().toISOString().slice(0,10);else delete log[id];save();paint();if(HIDE)run()}});
  document.getElementById('clearbtn').addEventListener('click',function(){{if(!confirm('Clear your done-list?'))return;log={{}};save();paint();run()}});
  document.getElementById('printbtn').addEventListener('click',function(){{var rows=Object.keys(log).sort(function(a,b){{return log[a]<log[b]?-1:1}}),tot=0;
    document.getElementById('pl-rows').innerHTML=rows.map(function(id){{var it=document.getElementById('it-'+id);tot+=META[id].m;
      return '<tr><td>'+log[id]+'</td><td>'+META[id].t.replace(/&/g,'&amp;').replace(/</g,'&lt;')+'</td><td>'+(SHELF[it?it.dataset.s:'']||'')+'</td><td>'+META[id].m+'</td></tr>'}}).join('')||'<tr><td colspan="4">Nothing marked done yet.</td></tr>';
    document.getElementById('pl-total').textContent=tot+' min';document.getElementById('pl-date').textContent=new Date().toLocaleDateString('en-US',{{year:'numeric',month:'long',day:'numeric'}});
    window.print()}});
  document.querySelectorAll('[data-jump]').forEach(function(a){{a.addEventListener('click',function(){{var it=document.getElementById('it-'+a.dataset.jump);if(it&&it.classList.contains('hide')){{q.value='';G=new Set(['k2','g35','g68','g912']);LV=new Set(['e','p','m']);K=new Set({json.dumps(L.KINDS)});MAXM=0;HIDE=false;document.querySelectorAll('.bar button').forEach(function(b){{b.setAttribute('aria-pressed',!(b.dataset.m||b.dataset.hideDone))}});run()}}}})}});
  paint();run();
}})();
</script>
<script data-goatcounter="https://elpublishing.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
<script src="guide.js" defer></script>
<script src="hub-chrome.js" defer></script>
</body>
</html>
'''
    (ROOT / "pd-library.html").write_text(page, encoding="utf-8")
    print(f"wrote pd-library.html — {len(L.ITEMS)} items, {len(L.PATHS)} paths, {total_min} min")

if __name__ == "__main__":
    main()
