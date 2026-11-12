"""The welcome band on the home page, between the header and Now Showing.

"Welcome" cycling through the hub's languages, a who's-visiting picker that
hands each visitor three tools, and the ELPT countdown. Titles and one-liners
come from the catalog, so the band never drifts from the cards. Edit the role
lists below to change what each visitor is handed; build.py writes the band
into index.html between <!--B:welcome--> markers.
"""
import html as H
import json
import sys
from datetime import date

ROLES = [
    ("content", "Content teacher", ["using-spanish-content-classroom.html", "sheltered.html", "el-bridge.html"]),
    ("el", "EL teacher", ["teaching-the-elpt.html", "grammar-calisthenics/", "elpa21-listening/"]),
    ("leader", "District leader", ["el-evaluate.html", "el-audit.html", "title3-planner.html"]),
    ("student", "Student", ["storm-lens/", "english-on-your-own.html", "picture-dictionary.html"]),
]
WORDS = [
    ("Welcome", "English", "en", "ltr"),
    ("Bienvenidos", "Spanish", "es", "ltr"),
    ("Chào mừng", "Vietnamese", "vi", "ltr"),
    ("أهلاً وسهلاً", "Arabic", "ar", "rtl"),
    ("Byenveni", "Haitian Creole", "ht", "ltr"),
    ("欢迎", "Chinese", "zh", "ltr"),
    ("Bem-vindos", "Portuguese", "pt", "ltr"),
]
ELPT_OPENS = date(2027, 3, 1)  # el-compliance-calendar.html: 2027 window Mar 1 – Apr 16

CSS = """
.welcome{background:#1E2761;color:#fff;padding:52px 0;position:relative;overflow:hidden}
.welcome::before{content:"";position:absolute;right:-120px;top:-120px;width:420px;height:420px;border-radius:50%;border:1px solid rgba(201,162,39,.28);box-shadow:0 0 0 60px rgba(201,162,39,.04),0 0 0 120px rgba(201,162,39,.03);pointer-events:none}
.wl-h1{margin:6px 0 0;font-family:Fraunces,Georgia,serif;font-weight:600;font-size:clamp(30px,4vw,42px);line-height:1.12;color:#fff;letter-spacing:-.01em}
.wl-h1 em{font-style:italic;color:#C9A227}
.wl-in{max-width:1060px;margin:0 auto;padding:0 26px;display:flex;flex-wrap:wrap;gap:40px;align-items:flex-start;position:relative}
.wl-say{flex:1 1 380px;min-width:0;display:flex;flex-direction:column;gap:16px}
.wl-k{margin:0;font-size:13px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#C9A227}
.wl-word{min-height:128px;display:flex;flex-direction:column;justify-content:flex-end}
.wl-word b{font-family:Fraunces,Georgia,serif;font-size:clamp(52px,8vw,88px);line-height:1.05;font-weight:700;color:#fff;animation:wl-rise .6s ease-out both}
.wl-word span{font-size:15px;color:#C9CEE8;margin-top:6px}
@keyframes wl-rise{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
.wl-chips{display:flex;flex-wrap:wrap;gap:8px}
.wl-chip{min-width:44px;min-height:44px;padding:0 14px;border-radius:999px;font:600 14px Inter,system-ui,sans-serif;cursor:pointer;background:transparent;color:#E4E7F5;border:1px solid rgba(255,255,255,.35)}
.wl-chip[aria-pressed="true"]{background:#C9A227;color:#1E2761;border-color:#C9A227}
.wl-count{display:inline-flex;align-items:center;gap:14px;margin-top:6px;padding:12px 18px;border:1px solid rgba(201,162,39,.5);border-radius:14px;align-self:flex-start}
.wl-count b{font-family:Fraunces,Georgia,serif;font-size:34px;color:#C9A227;line-height:1}
.wl-count span{font-size:14px;color:#E4E7F5;line-height:1.4}
.wl-count a{color:#F0DDA6}
.wl-me{display:flex;flex-direction:column;gap:22px;margin-top:14px;padding-top:26px;border-top:1px solid rgba(235,217,160,.28)}
.wl-me .ph{position:relative;width:min(100%,340px)}
.wl-me .ph::before{content:"";position:absolute;inset:16px -16px -16px 16px;border:2px solid #C9A227;border-radius:20px}
.wl-me img{position:relative;display:block;width:100%;height:auto;aspect-ratio:4/5;object-fit:cover;object-position:50% 20%;border-radius:20px;box-shadow:0 24px 50px rgba(6,10,30,.45)}
.wl-me p{margin:10px 0 0;font-size:15px;line-height:1.55;color:#D5D9EE;max-width:420px}
.wl-me b{display:block;font-family:Fraunces,Georgia,serif;font-size:24px;color:#fff;margin-bottom:4px}
.wl-card{flex:1 1 480px;min-width:0;background:#fff;color:#1E2761;border-radius:20px;padding:26px;display:flex;flex-direction:column;gap:16px;box-shadow:0 30px 60px rgba(8,12,36,.35)}
.wl-card h2{margin:0;font-size:26px;color:#1E2761}
.wl-card p{margin:0;font-size:15px;color:#4A5280}
.wl-roles{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.wl-role{min-height:48px;padding:0 14px;border-radius:12px;font:600 15px Inter,system-ui,sans-serif;cursor:pointer;text-align:left;background:#fff;color:#1E2761;border:2px solid #D5D9EA}
.wl-role[aria-pressed="true"]{background:#1E2761;color:#fff;border-color:#1E2761}
.wl-picks{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px}
.wl-picks[hidden]{display:none}
.wl-picks a{display:flex;gap:14px;align-items:center;text-decoration:none;color:#1E2761;padding:14px 16px;border:1px solid #E3E6F2;border-radius:14px;background:#F7F8FC;transition:transform .2s,box-shadow .2s}
.wl-picks a:hover{transform:translateY(-2px);box-shadow:0 12px 26px rgba(10,14,40,.18)}
.wl-n{flex:0 0 44px;height:44px;border-radius:12px;background:#1E2761;color:#C9A227;font:700 17px Fraunces,Georgia,serif;display:flex;align-items:center;justify-content:center}
.wl-tx{flex:1 1 auto;min-width:0;display:flex;flex-direction:column;gap:2px}
.wl-tx b{font-size:16px}
.wl-tx small{font-size:14px;color:#4A5280;line-height:1.45}
.wl-ar{color:#8A6D12;font-weight:700}
a.wl-all{align-self:flex-start;display:inline-flex;align-items:center;min-height:44px;padding:0 22px;border-radius:999px;background:#1E2761;color:#fff;font-weight:600;text-decoration:none}
@media(max-width:520px){.wl-roles{grid-template-columns:1fr}}
@media(prefers-reduced-motion:reduce){.wl-word b{animation:none}}
"""

JS = """
(function(){try{
  var W=__WORDS__,i=0,t=null,box=document.getElementById('wl-word'),
      chips=[].slice.call(document.querySelectorAll('.wl-chip')),
      calm=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function show(n){i=n;var w=W[n];box.innerHTML='';box.dir=w[3];
    var b=document.createElement('b');b.lang=w[2];b.textContent=w[0];
    var s=document.createElement('span');s.textContent='\\u201cWelcome\\u201d in '+w[1];
    box.appendChild(b);box.appendChild(s);
    chips.forEach(function(c,k){c.setAttribute('aria-pressed',k===n?'true':'false')})}
  function go(){if(t)clearInterval(t);if(!calm)t=setInterval(function(){show((i+1)%W.length)},2600)}
  chips.forEach(function(c){c.addEventListener('click',function(){show(+c.getAttribute('data-i'));go()})});
  go();
  var roles=[].slice.call(document.querySelectorAll('.wl-role')),
      lists=[].slice.call(document.querySelectorAll('.wl-picks'));
  function pick(r){
    roles.forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-r')===r?'true':'false')});
    lists.forEach(function(l){l.hidden=l.getAttribute('data-r')!==r});
    try{localStorage.setItem('elhub.role',r)}catch(e){}}
  roles.forEach(function(b){b.addEventListener('click',function(){pick(b.getAttribute('data-r'))})});
  try{var saved=localStorage.getItem('elhub.role');
    if(saved&&document.querySelector('.wl-picks[data-r="'+saved+'"]'))pick(saved)}catch(e){}
  var d=Math.ceil((new Date(__Y__,__M__,__D__)-new Date())/864e5),el=document.getElementById('wl-days');
  if(el)el.textContent=Math.max(0,d);
}catch(e){}})();
"""


def e(s):
    return H.escape(str(s), quote=True)


def build(seen, n_total, today, ext_attr):
    chips = "".join(
        f'<button type="button" class="wl-chip" data-i="{i}" '
        f'aria-pressed="{"true" if i == 0 else "false"}" '
        f'aria-label="Show welcome in {e(name)}">{e(lang.upper())}</button>'
        for i, (_, name, lang, _d) in enumerate(WORDS)
    )
    tabs, panels = [], []
    for k, (rid, label, hrefs) in enumerate(ROLES):
        on = k == 0
        tabs.append(
            f'<button type="button" class="wl-role" data-r="{rid}" '
            f'aria-pressed="{"true" if on else "false"}">{e(label)}</button>'
        )
        items = []
        for j, h in enumerate(hrefs, 1):
            r = seen.get(h)
            if not r:
                sys.exit(f"welcome.py: {h} is not in the catalog.")
            items.append(
                f'<li><a href="{e(r["href"])}"{ext_attr(r["href"])}>'
                f'<span class="wl-n">0{j}</span>'
                f'<span class="wl-tx"><b>{e(r["title"])}</b><small>{e(r["one"])}</small></span>'
                f'<span class="wl-ar" aria-hidden="true">→</span></a></li>'
            )
        panels.append(
            f'<ol class="wl-picks" data-r="{rid}"{"" if on else " hidden"}>{"".join(items)}</ol>'
        )
    days = max(0, (ELPT_OPENS - today).days)
    js = (JS.replace("__WORDS__", json.dumps([list(w) for w in WORDS], ensure_ascii=False))
            .replace("__Y__", str(ELPT_OPENS.year))
            .replace("__M__", str(ELPT_OPENS.month - 1))
            .replace("__D__", str(ELPT_OPENS.day)))
    opens = ELPT_OPENS.strftime("%B %-d, %Y")
    return f"""<section class="welcome" id="welcome" aria-label="Welcome">
<style>{CSS}</style>
<div class="wl-in">
  <div class="wl-say">
    <p class="wl-k">Many Voices · One Storm</p>
    <div class="wl-word" id="wl-word" aria-live="polite"><b lang="en">Welcome</b><span>“Welcome” in English</span></div>
    <div class="wl-chips" role="group" aria-label="Languages">{chips}</div>
    <h1 class="wl-h1">Every teacher is a <em><span class="swap" id="swapWord">language</span> teacher.</em></h1>
    <div class="wl-count"><b id="wl-days">{days}</b><span>days until the ELPT window opens<br>({opens}) · <a href="teaching-the-elpt.html">get your students ready</a></span></div>
    <div class="wl-me"><span class="ph"><img src="img/richard-daniel-portrait.jpg" alt="Richard A. Daniel" width="440" height="550" decoding="async"></span>
      <p><b>Richard A. Daniel, M.Ed.</b>ENL/EL Specialist, Laurel High School · 31 years in Mississippi, Alabama and Georgia classrooms · NBCT ENL candidate</p></div>
  </div>
  <div class="wl-card">
    <h2>Who’s visiting today?</h2>
    <p>Pick one and the hub hands you the three tools to start with.</p>
    <div class="wl-roles" role="group" aria-label="Choose your role">{"".join(tabs)}</div>
    {"".join(panels)}
    <a class="wl-all" href="all.html">Browse all {n_total} free resources</a>
  </div>
</div>
<script>{js}</script>
</section>"""
