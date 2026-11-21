/* Dynamic tools: plan meter, discussion questions and exit tickets, student choice board, class tools, teach mode.
   All text is filled in from the chosen standard with ideaFill(): {k} topic, {w1} {w2} {w3} key words. */
const DQ=[
["Remember",["What do you remember about {k}?","Which key words go with {k}?","What did we see or read today about {k}?"]],
["Understand",["How would you explain {k} in your own words?","What is one example of {k}?","How is the word {w1} connected to {k}?"]],
["Analyze",["Why is it important to understand {k}?","What would change if one part of {k} were different?","What is the difference between the words {w1} and {w2}?"]],
["Connect",["Where do you see {k} in your own life or community?","What question about {k} do you still want to answer?","What is the most important thing to understand about {k}, and why?"]]];
const ETF={
explain:["Draw something about {k}. Label your drawing with two key words.","Explain {k} in two sentences. Use because.","Explain {k} in a short paragraph. Use the words {w1} and {w2}."],
compare:["Circle same or different. Then finish the sentence: __ and __ are __.","Write one way two parts of {k} are alike and one way they are different. Use both and but.","Compare two parts of {k} in a paragraph. Use however or while."],
sequence:["Put three pictures or steps of {k} in order. Number them 1, 2, and 3.","Write three steps of {k}. Use first, next, and finally.","Describe the order of {k} in a paragraph and explain why the order matters."],
cause:["Finish the sentence: __ happens because __.","Write one cause and one effect in {k}. Use because or so.","Explain a cause and its effects in {k} in a paragraph. Use as a result."],
argue:["Do you agree? Circle yes or no. Then finish the sentence: I think __.","Write one claim about {k} and one reason. Use because.","Write a claim about {k}, support it with evidence, and answer one objection."],
describe:["Draw and label one thing about {k}.","Describe {k} in two sentences. Use the word {w1}.","Describe the most important features of {k} in a paragraph with precise words."],
summarize:["Finish the sentence: Today's lesson is about __.","Write the main idea of today's lesson and one key detail.","Summarize today's lesson on {k} in three or four sentences in your own words."],
solve:["Solve one problem. Circle your answer.","Solve one problem about {k} and write one sentence about your first step.","Solve one problem about {k} two ways, or explain how you checked your answer."]};
const ETG=[
["Three, two, one",["Write or draw one new word you learned today.","Write two things you learned about {k} and one question you still have.","Write three things you learned, two connections, and one question about {k}."]],
["Rate yourself",["Show a thumb: up, sideways, or down. Point to the part that was hard.","Rate your understanding of {k} from 1 to 4 and tell why in one sentence.","Rate your understanding of {k} from 1 to 4 and write what you would study next."]],
["Use the words",["Say or write one sentence with the word {w1}.","Use the words {w1} and {w2} in two sentences about today's lesson.","Use the words {w1}, {w2}, and {w3} in a short paragraph about {k}."]]];
/* choice board: [way of working, friendly for Levels 1-2, three tasks] */
const CBM=[
["Draw",1,["Draw a picture of {k} and label it with {w1}, {w2}, and {w3}.","Make a comic with four boxes that shows {k}.","Draw a diagram of {k} and add three labels."]],
["Write",0,["Write three sentences about {k}. Use the words {w1} and {w2}.","Write a note to a friend that explains {k}.","Write two questions about {k} and answer one of them."]],
["Say",0,["Tell a partner about {k} for one minute. Use the word {w1}.","Record yourself explaining {k} in 30 seconds.","Ask three classmates one question about {k} and report what they said."]],
["Make",1,["Build a model of {k} with paper or objects.","Make a poster that teaches {k}.","Make three flash cards with pictures for {w1}, {w2}, and {w3}."]],
["Act",1,["Act out {w1}, {w2}, and {w3} for a partner to guess.","Make up hand motions for {w1}, {w2}, and {w3} and teach them to a partner.","With a partner, act out one example of {k}."]],
["Connect",1,["Explain {k} to someone at home in your home language. Write one thing that person said.","Find {w1}, {w2}, or {w3} in your home language. Is the word similar to English?","Find an example of {k} in your home or neighborhood and draw it."]],
["Find",0,["Find {k} in a book, a video, or the news. Tell where you found it.","Find two pictures that show {k} and explain why you chose them.","Choose the three most important words about {k} and tell why."]],
["Quiz",0,["Write three quiz questions about {k} and quiz a partner.","Make a matching game with {w1}, {w2}, {w3} and their meanings.","Write one true sentence and one false sentence about {k}. Can a partner tell which is which?"]]];
const WTASK=["Draw it.","Act it out.","Use it in a sentence.","Say it in your home language.","Give an example.","Tell what it is not.","Use it in a question.","Whisper it, then say it loudly."];
function dqList(){const h=ideaHash(S.c),o=S.qo||0;return DQ.map((d,i)=>[d[0],ideaFill(d[1][(h+i+o)%3])]);}
function etSet(){const o=(S.eo||0)%4;if(o===0)return[F[fn()].label,ETF[fn()].map(ideaFill)];return[ETG[o-1][0],ETG[o-1][1].map(ideaFill)];}
function cbCells(){const h=ideaHash(S.c),o=S.cbo||0,c=CBM.map((m,i)=>({m:m[0],low:m[1],t:ideaFill(m[2][(h+i+o)%3])})),r=(h+o*3)%8,a=c.slice(r).concat(c.slice(0,r));a.splice(4,0,{m:"Your choice",low:1,t:ideaFill("Show what you know about {k} in your own way.")});return a;}
function dynPlan(){const L=[];if(S.qz){L.push("","Discussion questions:");dqList().forEach(q=>L.push(` - ${q[0]}: ${q[1]}`));}
 if(S.et){const e=etSet();L.push("",`Exit ticket (${e[0]}):`);["Levels 1-2","Levels 3-4","Level 5"].forEach((n,i)=>L.push(` - ${n}: ${e[1][i]}`));}
 if(S.cb){L.push("","Student choice board (choose three in a row):");cbCells().forEach((c,i)=>L.push(` ${i+1}. ${c.m}: ${c.t}`));}return L;}
function quizCard(){const q=dqList(),e=etSet(),g=groups(),gs=["em","pr","l5"],gn=["Levels 1-2","Levels 3-4","Level 5"];
 return `<div class="card ${S.qz||S.et?"":"none"}" id="quizcard"><h3>Questions and exit ticket</h3><p class="hint">Written for this standard. Tap to get a different set, then add what you want to your plan.</p>
 <div class="${S.qz?"":"skipprint"}"><h4 class="acat">Discussion questions, from simple to deep</h4><ol class="dq">${q.map(x=>`<li><span class="g all">${x[0]}</span>${esc(x[1])}</li>`).join("")}</ol>
 <div class="row noprint noshow"><button class="btn ghost" id="qzmore">Different questions</button><button class="btn ghost" id="qzon" aria-pressed="${!!S.qz}">${S.qz?"In my plan ✓":"Add to my plan"}</button></div></div>
 <div class="${S.et?"":"skipprint"}"><h4 class="acat">Exit ticket: ${esc(e[0])}</h4><div class="etl">${e[1].map((x,i)=>`<p class="${g[gs[i]]?"":"dim"}"><span class="g ${gs[i]}">${gn[i]}</span>${esc(x)}</p>`).join("")}</div>
 <div class="row noprint noshow"><button class="btn ghost" id="etmore">Different exit ticket</button><button class="btn ghost" id="eton" aria-pressed="${!!S.et}">${S.et?"In my plan ✓":"Add to my plan"}</button></div></div></div>`;}
function choiceCard(){const c=cbCells();return `<div class="card ${S.cb?"":"none"}" id="cbcard"><h3>Student choice board</h3><p class="hint">Nine ways for students to show what they know about ${esc(std().k)}. Students choose three in a row. A dot marks tasks that need little English.</p>
 <div class="cb">${c.map((x,i)=>`<div class="cbc ${i===4?"mid":""}"><b>${x.m}${x.low?'<i title="Needs little English" aria-label="Needs little English"></i>':""}</b><span>${esc(x.t)}</span></div>`).join("")}</div>
 <div class="row noprint noshow"><button class="btn" id="cbmore">Shuffle the board</button><button class="btn ghost" id="cbon" aria-pressed="${!!S.cb}">${S.cb?"In my plan ✓":"Add to my plan"}</button></div></div>`;}
/* plan meter */
function meterItems(){const g=groups();return[["Students counted",g.n>0,"levels"],["Lesson ideas chosen",ideasOn().length>0,"ideacard"],["Daily text in plan",!!txState().on,"txcard"],["Questions or exit ticket",!!(S.qz||S.et),"quizcard"],["Choice board",!!S.cb,"cbcard"],["Accommodations marked",S.acc.length>0,"acccard"],["Lesson logged today",LOG.some(e=>e.d===today()&&e.c===S.c),"acccard"]];}
function meterCard(){const it=meterItems(),n=it.filter(x=>x[1]).length,p=n/it.length,C=2*Math.PI*26;
 return `<div class="card noprint noshow" id="meter"><div class="mrow"><svg viewBox="0 0 64 64" width="72" height="72" role="img" aria-label="${n} of ${it.length} parts of the plan are ready"><circle cx="32" cy="32" r="26" fill="none" stroke="var(--soft)" stroke-width="7"/><circle cx="32" cy="32" r="26" fill="none" stroke="${p===1?"var(--l5)":"var(--gold)"}" stroke-width="7" stroke-linecap="round" stroke-dasharray="${(C*p).toFixed(1)} ${C.toFixed(1)}" transform="rotate(-90 32 32)" class="ring"/><text x="32" y="37" text-anchor="middle" font-size="16" font-weight="700" fill="currentColor">${n}/${it.length}</text></svg>
 <div><h3>${p===1?"Your plan is complete":"Build your plan"}</h3><p class="hint" style="margin:0">Tap a step to jump to it.</p></div></div>
 <div class="chips" style="margin-top:8px">${it.map(x=>`<button class="chip sq ${x[1]?"done":""}" data-go="${x[2]}">${x[1]?"✓ ":""}${x[0]}</button>`).join("")}</div></div>`;}
/* class tools (nothing here is saved except the class size; seats are numbers, never names) */
const TL={pick:null,used:[],groups:null,gs:3,word:null};let TLI=null;
function toolsCard(){const n=S.cls||24,v=vocab().length?vocab():std().v;
 return `<div class="card noprint noshow" id="toolcard"><h3>Class tools</h3><p class="hint">Quick helpers for the lesson. They use seat numbers, never names.</p>
 <div class="tgrid"><div class="tool"><h4 class="acat">Students in the room</h4><div class="stp"><button data-cls="-1" aria-label="One fewer student">−</button><output id="clsn">${n}</output><button data-cls="1" aria-label="One more student">+</button></div>
 <h4 class="acat">Call on a seat</h4><div class="big" id="seatnum" aria-live="polite">${TL.pick||"?"}</div><button class="btn" id="seatgo">Pick a seat</button><p class="hint" style="margin:6px 0 0">${TL.used.length} of ${n} called. No repeats until everyone has had a turn.</p></div>
 <div class="tool"><h4 class="acat">Make groups</h4><div class="chips">${[2,3,4,5].map(k=>`<button class="chip ${TL.gs===k?"on":""}" data-gs="${k}" aria-pressed="${TL.gs===k}">Groups of ${k}</button>`).join("")}</div><button class="btn" id="grpgo" style="margin-top:8px">Mix the groups</button>
 ${TL.groups?`<div class="grps">${TL.groups.map((g,i)=>`<div><b>Group ${i+1}</b><span>Seats ${g.join(", ")}</span></div>`).join("")}</div>`:'<p class="hint" style="margin:6px 0 0">Seat numbers are mixed at random.</p>'}</div>
 <div class="tool"><h4 class="acat">Word spinner</h4><div class="big sm" id="wordout" aria-live="polite">${TL.word?esc(TL.word[0]):"?"}</div><p class="wt" id="wordtask">${TL.word?esc(TL.word[1]):"Spin for a key word and a quick task."}</p><button class="btn" id="wordgo">Spin</button><p class="hint" style="margin:6px 0 0">Key words: ${v.map(esc).join(", ")}</p></div></div></div>`;}
function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
function still(){try{return window.matchMedia("(prefers-reduced-motion:reduce)").matches;}catch(e){return false;}}
function spinInto(id,vals,done){clearInterval(TLI);if(still()||vals.length<2){done();return;}let k=0;TLI=setInterval(()=>{const el=$(id);if(el)el.textContent=vals[Math.floor(Math.random()*vals.length)];if(++k>=12){clearInterval(TLI);done();}},70);}
/* teach mode: run the lesson part by part with a countdown */
const TM={on:false,i:0,left:0,run:false,done:false,t:null};
function tmFmt(s){const m=Math.floor(Math.abs(s)/60),x=Math.abs(s)%60;return m+":"+String(x).padStart(2,"0");}
function tmBeep(){try{const A=window.AudioContext||window.webkitAudioContext,c=new A(),o=c.createOscillator(),g=c.createGain();o.connect(g);g.connect(c.destination);o.frequency.value=880;g.gain.setValueAtTime(.2,c.currentTime);g.gain.exponentialRampToValueAtTime(.001,c.currentTime+.6);o.start();o.stop(c.currentTime+.6);}catch(e){}}
function tmSet(i){TM.i=i;TM.left=minutes()[i]*60;TM.run=false;TM.done=false;clearInterval(TM.t);}
function tmTick(){if(!TM.run)return;TM.left--;const c=$("tclock"),b=$("tbar"),tot=minutes()[TM.i]*60;if(c)c.textContent=tmFmt(Math.max(TM.left,0));if(b)b.style.width=Math.max(0,Math.min(100,(1-TM.left/tot)*100))+"%";if(TM.left<=0){TM.run=false;TM.done=true;clearInterval(TM.t);tmBeep();tmRender();}}
function tmRender(){let el=$("teach");if(!TM.on){if(el)el.remove();document.body.classList.remove("teaching");return;}if(!el){el=document.createElement("div");el.id="teach";el.className="teach noprint";el.setAttribute("role","dialog");el.setAttribute("aria-label","Teach mode");document.body.appendChild(el);}document.body.classList.add("teaching");
 const d=std(),g=groups(),mins=minutes(),end=TM.i>=PH.length;
 if(end){el.innerHTML=`<div class="tin"><div class="ttop"><span>${esc(d.c)} · ${esc(d.k)}</span><button class="tx2" id="tclose" aria-label="Close teach mode">Close ✕</button></div><h2>Lesson complete</h2><p class="tact">${S.min} minutes, ${PH.length} parts.</p><div class="tbtn"><button class="btn gold" id="tlog">Log this lesson</button><button class="btn ghost" data-tgo="0">Start again</button></div></div>`;return;}
 const p=PH[TM.i],a=p.acts[S.act[TM.i]],tot=mins[TM.i]*60;
 el.innerHTML=`<div class="tin"><div class="ttop"><span>${esc(d.c)} · ${esc(d.k)}</span><button class="tx2" id="tclose" aria-label="Close teach mode">Close ✕</button></div>
 <div class="tdots">${PH.map((x,i)=>`<button class="${i===TM.i?"cur":i<TM.i?"past":""}" data-tgo="${i}" aria-label="Go to ${x.n}">${i+1}</button>`).join("")}</div>
 <p class="tpart">Part ${TM.i+1} of ${PH.length} · ${mins[TM.i]} min</p><h2>${p.n}</h2><p class="tact">${a[0]}</p>
 <div class="tclock ${TM.done?"over":""}" id="tclock" aria-live="off">${tmFmt(Math.max(TM.left,0))}</div><div class="tbarw"><i id="tbar" style="width:${Math.max(0,Math.min(100,(1-TM.left/tot)*100))}%"></i></div>
 ${TM.done?'<p class="tdone" role="status">Time. Move to the next part when you are ready.</p>':""}
 <div class="tbtn"><button class="btn ghost" data-tgo="${TM.i-1}" ${TM.i===0?"disabled":""}>‹ Back</button><button class="btn gold" id="tplay">${TM.run?"Pause":TM.done?"Restart the timer":"Start"}</button><button class="btn ghost" id="tplus">+1 min</button><button class="btn ghost" data-tgo="${TM.i+1}">${TM.i===PH.length-1?"Finish":"Next ›"}</button></div>
 <ul class="tlist"><li><span class="g act">${a[0]}</span>${a[1]}</li>${p.all.map(x=>`<li><span class="g all">Everyone</span>${x}</li>`).join("")}${g.em?p.em.map(x=>`<li><span class="g em">Levels 1-2</span>${x}</li>`).join(""):""}${g.pr?p.pr.map(x=>`<li><span class="g pr">Levels 3-4</span>${x}</li>`).join(""):""}${g.l5?p.l5.map(x=>`<li><span class="g l5">Level 5</span>${x}</li>`).join(""):""}</ul>
 <p class="tobj"><b>Language objective:</b> ${esc(langObj())}</p></div>`;}
document.addEventListener("click",e=>{const b=e.target.closest("button");if(!b)return;const d=b.dataset;
 if(b.id==="qzmore"){S.qo=((S.qo||0)+1)%3;keep();}
 else if(b.id==="qzon"){S.qz=!S.qz;keep();}
 else if(b.id==="etmore"){S.eo=((S.eo||0)+1)%4;keep();}
 else if(b.id==="eton"){S.et=!S.et;keep();}
 else if(b.id==="cbmore"){S.cbo=((S.cbo||0)+1)%24;keep();}
 else if(b.id==="cbon"){S.cb=!S.cb;keep();}
 else if(d.tab){S.tab=d.tab;renderPlan();const n=$("tabs");if(n&&(d.top||n.getBoundingClientRect().top<0))n.scrollIntoView();}
 else if(d.go){if(steps()){const st=d.go==="levels"?ST.who:d.go==="choices"?ST.std:d.go==="plan"?ST.review:CARDSTEP[d.go];if(st&&st!==stepCur())goStep(st,true);}else if(PANEOF[d.go]&&tabCur()!=="all"&&tabCur()!==PANEOF[d.go]){S.tab=PANEOF[d.go];renderPlan();}const t=$(d.go);if(t){try{t.scrollIntoView({behavior:still()?"auto":"smooth",block:"start"});}catch(err){t.scrollIntoView();}}}
 else if(d.cls){S.cls=Math.max(2,Math.min(45,(S.cls||24)+(+d.cls)));TL.used=[];TL.pick=null;TL.groups=null;keep();}
 else if(b.id==="seatgo"){const n=S.cls||24;if(TL.used.length>=n)TL.used=[];const left=[];for(let i=1;i<=n;i++)if(!TL.used.includes(i))left.push(i);const pick=left[Math.floor(Math.random()*left.length)];b.disabled=true;spinInto("seatnum",left,()=>{TL.pick=pick;TL.used.push(pick);keep();});}
 else if(d.gs){TL.gs=+d.gs;TL.groups=null;keep();}
 else if(b.id==="grpgo"){const n=S.cls||24,a=shuffle(Array.from({length:n},(x,i)=>i+1)),G=[];for(let i=0;i<n;i+=TL.gs)G.push(a.slice(i,i+TL.gs));if(G.length>1&&G[G.length-1].length===1){G[G.length-2].push(G.pop()[0]);}TL.groups=G.map(g=>g.sort((x,y)=>x-y));keep();}
 else if(b.id==="wordgo"){const v=vocab().length?vocab():std().v,w=v[Math.floor(Math.random()*v.length)],t=WTASK[Math.floor(Math.random()*WTASK.length)];b.disabled=true;spinInto("wordout",v,()=>{TL.word=[w,t];keep();});}
 else if(b.id==="teachgo"||b.id==="teachgo2"||b.id==="teachgo3"){TM.on=true;tmSet(0);tmRender();}
 else if(b.id==="tclose"){TM.on=false;TM.run=false;clearInterval(TM.t);tmRender();}
 else if(d.tgo!==undefined&&d.tgo!==""){const i=+d.tgo;if(i<0)return;if(i>=PH.length){TM.i=PH.length;TM.run=false;clearInterval(TM.t);}else tmSet(i);tmRender();}
 else if(b.id==="tplay"){if(TM.run){TM.run=false;clearInterval(TM.t);}else{if(TM.done||TM.left<=0){TM.left=minutes()[TM.i]*60;TM.done=false;}TM.run=true;clearInterval(TM.t);TM.t=setInterval(tmTick,1000);}tmRender();}
 else if(b.id==="tplus"){TM.left=Math.max(TM.left,0)+60;TM.done=false;tmRender();}
 else if(b.id==="tlog"){LOG.unshift({d:today(),c:S.c,k:std().k,lv:S.lv.slice(),acc:S.acc.slice()});LOG=LOG.slice(0,200);TM.on=false;tmRender();keep();}
});
document.addEventListener("keydown",e=>{if(e.key==="Escape"&&TM.on){TM.on=false;TM.run=false;clearInterval(TM.t);tmRender();}});
/* sections: the plan is organized into tabs; "All" shows every section on one page */
const TABS=[["over","Overview","Who is in the room, where to seat students, and tips for this subject."],["lang","Language","The words to teach on purpose and the sentence frames to post."],["act","Activities","Lesson ideas, the lesson part by part, and a student choice board."],["text","Daily text","Today's informational text at three levels, with key words and questions."],["check","Check","Discussion questions and an exit ticket for this standard."],["teach","Teach","Run the lesson with a timer, and use quick class tools."],["track","Track","The accommodations you provide and your lesson log."],["all","All","Every section on one page."]];
const PANEOF={excard:"text",sitecard:"text",meter:"over",ideacard:"act",cbcard:"act",txcard:"text",quizcard:"check",toolcard:"teach",acccard:"track"};
function tabCur(){return TABS.some(t=>t[0]===S.tab)?S.tab:"over";}
function tabHas(k){const g=groups();return k==="over"?g.n>0:k==="act"?(ideasOn().length>0||!!S.cb):k==="text"?!!txState().on:k==="check"?!!(S.qz||S.et):k==="teach"?LOG.some(e=>e.d===today()&&e.c===S.c):k==="track"?S.acc.length>0:false;}
function tabNav(){const c=tabCur();return `<nav class="tabs noprint noshow" id="tabs" aria-label="Sections of the plan">${TABS.map(t=>`<button class="tab ${t[0]===c?"cur":""} ${tabHas(t[0])?"has":""}" data-tab="${t[0]}" ${t[0]===c?'aria-current="page"':""}>${t[1]}</button>`).join("")}</nav>`;}
function pane(k,html){const t=TABS.find(x=>x[0]===k),c=tabCur();return `<section class="pane ${c===k||c==="all"||steps()?"cur":""}" id="pane-${k}" aria-label="${t[1]}"><header class="ph"><h2>${t[1]}</h2><p>${t[2]}</p></header>${html}${c===k&&!steps()?paneNav(k):""}</section>`;}
function paneNav(k){const T=TABS.filter(t=>t[0]!=="all"),i=T.findIndex(t=>t[0]===k),p=T[i-1],n=T[i+1];return `<div class="pnav noprint noshow">${p?`<button class="btn ghost" data-tab="${p[0]}" data-top="1">‹ ${p[1]}</button>`:"<span></span>"}${n?`<button class="btn" data-tab="${n[0]}" data-top="1">Next: ${n[1]} ›</button>`:`<button class="btn gold" data-go="plan">Finish: copy or print ›</button>`}</div>`;}
function teachCard(){const m=minutes();return `<div class="card noprint noshow" id="teachcard"><h3>Teach mode</h3><p class="hint">A full-screen view that runs the ${S.min}-minute lesson part by part, with a countdown and the supports for the levels in your room.</p>
 <ol class="tparts">${PH.map((p,i)=>`<li><b>${p.n}</b><span>${p.acts[S.act[i]][0]}</span><i>${m[i]} min</i></li>`).join("")}</ol><div class="row"><button class="btn gold" id="teachgo2">Start teach mode</button></div></div>`;}
