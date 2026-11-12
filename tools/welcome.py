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
.wl-me .ph{display:block;width:min(100%,360px);padding:10px;border:2px solid #C9A227;border-radius:26px;box-sizing:border-box}
.wl-me img{position:relative;display:block;width:100%;height:auto;aspect-ratio:4/5;object-fit:cover;object-position:50% 20%;border-radius:20px;box-shadow:0 24px 50px rgba(6,10,30,.45)}
.wl-me p{margin:0;font-size:15px;line-height:1.55;color:#D5D9EE;max-width:420px}
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
/* the card runs the full height of the left column and ends with the photo
   */
.wl-in{align-items:stretch}
.wl-picks:not([hidden]){flex:1 1 auto}
.wl-picks li{flex:1 1 auto;display:flex}
.wl-picks li a{flex:1 1 auto}
.wl-picks a{flex-direction:column;align-items:stretch;gap:12px;padding:12px}
.wl-th{display:block;width:100%;flex:1 1 80px;min-height:80px;height:0;object-fit:cover;object-position:50% 0;border-radius:10px;border:1px solid #E3E6F2;background:#E9ECF6}
.wl-row{display:flex;gap:14px;align-items:center;padding:0 4px 2px}
a.wl-play{display:inline-flex;align-items:center;gap:12px;align-self:flex-start;min-height:52px;padding:0 24px 0 8px;border-radius:999px;background:#C9A227;color:#1E2761;font-weight:700;font-size:16px;text-decoration:none;box-shadow:0 10px 26px rgba(201,162,39,.25);transition:transform .2s,box-shadow .2s}
a.wl-play:hover{transform:translateY(-2px);box-shadow:0 14px 32px rgba(201,162,39,.35);color:#1E2761}
a.wl-play i{width:38px;height:38px;border-radius:50%;background:#1E2761;display:flex;align-items:center;justify-content:center}
a.wl-play i::before{content:"";border-left:12px solid #C9A227;border-top:8px solid transparent;border-bottom:8px solid transparent;margin-left:3px}
.wl-dlg{width:min(1100px,94vw);max-width:none;padding:0;border:2px solid #C9A227;border-radius:20px;background:#141A44;box-shadow:0 40px 120px rgba(0,0,0,.6)}
.wl-dlg::backdrop{background:rgba(8,12,36,.82)}
.wl-dlg video{display:block;width:100%;height:auto;aspect-ratio:16/9;background:#141A44}
.wl-dlg .x{position:absolute;top:10px;right:10px;z-index:2;width:44px;height:44px;border-radius:50%;border:0;background:rgba(20,26,68,.85);color:#fff;font-size:26px;line-height:1;cursor:pointer}
.wl-dlg .x:focus-visible{outline:3px solid #C9A227}
/* ---- finishing touches ---- */
/* paper grain: a whisper of texture so the navy reads as printed, not flat */
.welcome::after{content:"";position:absolute;inset:0;pointer-events:none;opacity:.07;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
/* the brand's opening quotation mark, set huge and faint behind the welcome */
.wl-glyph{position:absolute;left:-18px;top:-96px;font-family:Fraunces,Georgia,serif;font-style:italic;font-weight:700;font-size:440px;line-height:1;color:#C9A227;opacity:.07;pointer-events:none;user-select:none}
.wl-say,.wl-card{position:relative}
/* kicker led in by a gold hairline */
.wl-k{display:flex;align-items:center;gap:14px}
.wl-k::before{content:"";width:40px;height:1px;background:#C9A227}
/* each new welcome gets a gold rule that draws in beneath it */
.wl-word b{display:inline-block;position:relative;align-self:flex-start;padding-bottom:10px}
.wl-word b::after{content:"";position:absolute;left:0;bottom:0;height:3px;width:72px;background:#C9A227;border-radius:2px;transform-origin:0 50%;animation:wl-draw .7s .25s cubic-bezier(.2,.7,.2,1) both}
.wl-word[dir="rtl"] b::after{left:auto;right:0;transform-origin:100% 50%}
@keyframes wl-draw{from{transform:scaleX(0)}to{transform:scaleX(1)}}
/* figures that sit level and don't jitter as the count changes */
.wl-count b{font-variant-numeric:lining-nums tabular-nums;letter-spacing:-.02em}
/* registration marks at two corners of the portrait frame, like a proof sheet */
.wl-me .ph{position:relative}
.wl-me .ph::before,.wl-me .ph::after{content:"";position:absolute;width:22px;height:22px;pointer-events:none}
.wl-me .ph::before{left:-12px;top:-12px;border-left:1px solid #C9A227;border-top:1px solid #C9A227}
.wl-me .ph::after{right:-12px;bottom:-12px;border-right:1px solid #C9A227;border-bottom:1px solid #C9A227}
.wl-me .ph img{transition:filter .5s}
.wl-me .ph:hover img{filter:saturate(1.08) contrast(1.03)}
/* small-caps credit line under the name */
.wl-me p b{letter-spacing:-.005em}
/* the card: a fine inner rule and livelier picks */
.wl-card{box-shadow:0 30px 60px rgba(8,12,36,.35),inset 0 0 0 1px rgba(30,39,97,.06)}
.wl-role{transition:background .2s,color .2s,border-color .2s,transform .15s}
.wl-role:hover{border-color:#1E2761}
.wl-role:active{transform:scale(.98)}
.wl-n{transition:background .25s,color .25s}
.wl-picks a:hover .wl-n{background:#C9A227;color:#1E2761}
.wl-ar{transition:transform .25s}
.wl-picks a:hover .wl-ar{transform:translateX(4px)}
.wl-picks a:focus-visible,.wl-role:focus-visible,.wl-chip:focus-visible,a.wl-play:focus-visible{outline:3px solid #C9A227;outline-offset:3px}
/* the page opens in sequence instead of all at once */
@keyframes wl-in{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}
.wl-say>*{animation:wl-in .8s cubic-bezier(.2,.7,.2,1) both}
.wl-say>:nth-child(2){animation-delay:.06s}.wl-say>:nth-child(3){animation-delay:.12s}
.wl-say>:nth-child(4){animation-delay:.18s}.wl-say>:nth-child(5){animation-delay:.24s}
.wl-say>:nth-child(6){animation-delay:.30s}.wl-say>:nth-child(7){animation-delay:.36s}
.wl-say>:nth-child(n+8){animation-delay:.42s}
.wl-card{animation:wl-in .9s .2s cubic-bezier(.2,.7,.2,1) both}
/* a fleuron rule closing the section */
.wl-orn{position:relative;max-width:1060px;margin:44px auto 0;padding:0 26px;display:flex;align-items:center;gap:18px;color:#C9A227}
.wl-orn::before,.wl-orn::after{content:"";flex:1;height:1px;background:linear-gradient(90deg,transparent,rgba(201,162,39,.55))}
.wl-orn::after{background:linear-gradient(90deg,rgba(201,162,39,.55),transparent)}
.wl-orn i{width:8px;height:8px;transform:rotate(45deg);border:1px solid #C9A227}
.wl-orn b{font:600 12px Inter,system-ui,sans-serif;letter-spacing:4px;text-transform:uppercase;color:#C9CEE8}
@media(max-width:700px){.wl-glyph{font-size:300px;top:-70px}}
@media(prefers-reduced-motion:reduce){.wl-say>*,.wl-card,.wl-word b::after{animation:none}}
@media(prefers-reduced-motion:reduce){.wl-word b{animation:none}}
/* ==== luxe layer ==== */
.welcome{--foil:linear-gradient(100deg,#8A6D12 0%,#C9A227 18%,#FFF1BF 34%,#E2B93B 46%,#9C7A15 62%,#F3D77A 80%,#C9A227 100%)}
.welcome::before{display:none}
/* gold foil lettering with a slow travelling sheen */
@keyframes wl-sheen{from{background-position:0% 50%}to{background-position:250% 50%}}
.wl-h1 em,.wl-count b,.wl-k{background:var(--foil);background-size:250% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:wl-sheen 7s linear infinite}
.wl-k::before{background:#C9A227}
.wl-glyph{color:transparent;-webkit-text-stroke:1.5px rgba(201,162,39,.35);opacity:1}
/* gold-foil frame around the portrait */
.wl-me .ph{border:2px solid transparent;background:linear-gradient(#1E2761,#1E2761) padding-box,var(--foil) border-box;background-size:100% 100%,250% 100%;animation:wl-sheen 9s linear infinite;box-shadow:0 0 0 1px rgba(201,162,39,.15),0 30px 70px rgba(4,8,28,.55),0 0 60px rgba(201,162,39,.12)}
.wl-me .ph img{box-shadow:inset 0 0 0 1px rgba(255,255,255,.08)}
/* foil play button with a light that sweeps across it */
a.wl-play{position:relative;overflow:hidden;background:var(--foil);background-size:250% 100%;animation:wl-sheen 7s linear infinite;box-shadow:0 12px 30px rgba(201,162,39,.35),inset 0 1px 0 rgba(255,255,255,.5)}
a.wl-play::after{content:"";position:absolute;top:0;bottom:0;width:60px;left:-80px;background:linear-gradient(100deg,transparent,rgba(255,255,255,.65),transparent);transform:skewX(-20deg);animation:wl-sweep 3.6s 1.2s ease-in-out infinite}
@keyframes wl-sweep{0%{left:-80px}45%,100%{left:110%}}
/* a slow gold orbit behind the card */
.wl-orbit{position:absolute;right:-260px;top:-240px;width:900px;height:900px;pointer-events:none;animation:wl-turn 140s linear infinite;opacity:.9}
@keyframes wl-turn{to{transform:rotate(360deg)}}
/* soft gold light that follows the cursor */
.wl-spot{position:absolute;inset:0;pointer-events:none;background:radial-gradient(520px circle at var(--mx,70%) var(--my,30%),rgba(201,162,39,.13),transparent 62%);transition:background .08s}
/* letters of each welcome cascade in */
.wl-word b .ch{display:inline-block;animation:wl-ch .55s cubic-bezier(.2,.8,.2,1) both}
.wl-word b .ch{font-size:inherit;color:inherit;margin:0;line-height:inherit}
.wl-h1 em .swap{background:var(--foil);background-size:250% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:wl-sheen 7s linear infinite;padding-right:.08em}
.wl-word b{white-space:nowrap;font-size:clamp(44px,7.4vw,84px)}
@keyframes wl-ch{from{opacity:0;transform:translateY(.45em) rotate(4deg);filter:blur(6px)}to{opacity:1;transform:none;filter:none}}
.wl-word b{animation:none}
/* depth: the card and portrait lean toward the cursor */
.wl-card,.wl-me .ph{transform-style:preserve-3d;transition:transform .35s cubic-bezier(.2,.7,.2,1),box-shadow .35s}
.wl-card{box-shadow:0 40px 90px rgba(4,8,28,.5),0 0 0 1px rgba(201,162,39,.25),inset 0 0 0 1px rgba(30,39,97,.06)}
.wl-card::before{content:"";position:absolute;inset:-1px;border-radius:21px;padding:1px;background:var(--foil);background-size:250% 100%;animation:wl-sheen 9s linear infinite;-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none;opacity:.7}
.wl-in>.wl-say,.wl-in>.wl-card{z-index:1}
@media(prefers-reduced-motion:reduce){.wl-h1 em,.wl-h1 em .swap,.wl-count b,.wl-k,.wl-me .ph,a.wl-play,a.wl-play::after,.wl-orbit,.wl-card::before,.wl-word b .ch{animation:none}}

"""

JS = """
(function(){try{
  var W=__WORDS__,i=0,t=null,box=document.getElementById('wl-word'),
      chips=[].slice.call(document.querySelectorAll('.wl-chip')),
      calm=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function show(n){i=n;var w=W[n];box.innerHTML='';box.dir=w[3];
    var b=document.createElement('b');b.lang=w[2];if(calm||w[3]==='rtl'){b.textContent=w[0]}else{Array.from(w[0]).forEach(function(c,k){var sp=document.createElement('span');sp.className='ch';sp.style.animationDelay=(k*0.045)+'s';sp.textContent=c===' '?'\u00a0':c;b.appendChild(sp)})}
    var s=document.createElement('span');s.dir='ltr';s.textContent='\\u201cWelcome\\u201d in '+w[1];
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
  if(!calm&&window.matchMedia('(pointer:fine)').matches){
    var sec=document.getElementById('welcome');
    sec.addEventListener('pointermove',function(ev){var r=sec.getBoundingClientRect();
      sec.style.setProperty('--mx',(ev.clientX-r.left)+'px');sec.style.setProperty('--my',(ev.clientY-r.top)+'px')});
    [].slice.call(document.querySelectorAll('.wl-card,.wl-me .ph')).forEach(function(el){
      var max=el.classList.contains('wl-card')?3:6;
      el.addEventListener('pointermove',function(ev){var r=el.getBoundingClientRect(),x=(ev.clientX-r.left)/r.width-.5,y=(ev.clientY-r.top)/r.height-.5;
        el.style.transform='perspective(1200px) rotateY('+(x*max)+'deg) rotateX('+(-y*max)+'deg)'});
      el.addEventListener('pointerleave',function(){el.style.transform=''})});
  }
  var pl=document.getElementById('wl-play'),dl=document.getElementById('wl-dlg'),vd=document.getElementById('wl-vid');
  if(pl&&dl&&dl.showModal){
    pl.addEventListener('click',function(ev){ev.preventDefault();dl.showModal();try{vd.currentTime=0;var pr=vd.play();if(pr&&pr.catch)pr.catch(function(){})}catch(e){}});
    document.getElementById('wl-x').addEventListener('click',function(){dl.close()});
    dl.addEventListener('click',function(ev){if(ev.target===dl)dl.close()});
    dl.addEventListener('close',function(){try{vd.pause()}catch(e){}});
  }
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
                + (f'<img class="wl-th" src="{e(r["thumb"])}" alt="" loading="lazy" decoding="async">' if r["thumb"] else "")
                + f'<span class="wl-row"><span class="wl-n">0{j}</span>'
                f'<span class="wl-tx"><b>{e(r["title"])}</b><small>{e(r["one"])}</small></span>'
                f'<span class="wl-ar" aria-hidden="true">→</span></span></a></li>'
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
<div class="wl-spot" aria-hidden="true"></div>
<svg class="wl-orbit" viewBox="0 0 900 900" aria-hidden="true"><g fill="none" stroke="#C9A227"><circle cx="450" cy="450" r="300" stroke-opacity=".28"/><circle cx="450" cy="450" r="360" stroke-opacity=".22" stroke-dasharray="1 9"/><circle cx="450" cy="450" r="430" stroke-opacity=".12"/></g><g fill="#C9A227"><circle cx="750" cy="450" r="4" fill-opacity=".8"/><circle cx="450" cy="90" r="3" fill-opacity=".55"/><circle cx="146" cy="560" r="2.5" fill-opacity=".5"/><circle cx="560" cy="858" r="3" fill-opacity=".4"/></g></svg>
<div class="wl-in">
  <span class="wl-glyph" aria-hidden="true">“</span>
  <div class="wl-say">
    <p class="wl-k">Many Voices · One Storm</p>
    <div class="wl-word" id="wl-word" aria-live="polite"><b lang="en">Welcome</b><span>“Welcome” in English</span></div>
    <div class="wl-chips" role="group" aria-label="Languages">{chips}</div>
    <h1 class="wl-h1">Every teacher is a <em><span class="swap" id="swapWord">language</span> teacher.</em></h1>
    <a class="wl-play" id="wl-play" href="video/hub-tour.mp4"><i aria-hidden="true"></i>Watch the 1-minute tour</a>
    <div class="wl-count"><b id="wl-days">{days}</b><span>days until the ELPT window opens<br>({opens}) · <a href="teaching-the-elpt.html">get your students ready</a></span></div>
    <div class="wl-me"><p><b>Richard A. Daniel, M.Ed.</b>ENL/EL Specialist, Laurel High School · 31 years in Mississippi, Alabama and Georgia classrooms · NBCT ENL candidate</p>
      <span class="ph"><img src="img/richard-daniel-portrait-level.jpg" alt="Richard A. Daniel" width="880" height="1100" decoding="async"></span></div>
  </div>
  <div class="wl-card">
    <h2>Who’s visiting today?</h2>
    <p>Pick one and the hub hands you the three tools to start with.</p>
    <div class="wl-roles" role="group" aria-label="Choose your role">{"".join(tabs)}</div>
    {"".join(panels)}
    <a class="wl-all" href="all.html">Browse all {n_total} free resources</a>
  </div>
</div>
<div class="wl-orn" aria-hidden="true"><i></i><b>Free for every teacher</b><i></i></div>
<dialog class="wl-dlg" id="wl-dlg" aria-label="One-minute tour of the EL Publishing Hub"><button type="button" class="x" id="wl-x" aria-label="Close the tour">×</button><video id="wl-vid" controls playsinline preload="none" poster="video/hub-tour-poster.jpg" width="1920" height="1080"><source src="video/hub-tour.mp4" type="video/mp4"></video></dialog>
<script>{js}</script>
</section>"""
