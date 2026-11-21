/* Step-by-step mode: one screen per step, a checklist that catches anything missing, and printing. */
const STEPS=[
[1,"Lesson","Pick your subject, your grade, and the standard for this lesson.","What are you teaching?","std"],
[2,"Students","Tap + once for each student. Go by what you see and hear in class. You do not need test scores.","Who are your English learners?","who"],
[3,"Five things","This is your plan. Each step says what to do and why it helps.","Do these five things","five"],
[4,"Lesson ideas","Activities that fit this standard, each with a tip for students who are new to English. Tap the ones you want.","Lesson ideas","ideas"],
[5,"Lesson parts","Set your class length and choose one activity for each part of the lesson. The planner shows what to do for each group of students.","Your lesson, part by part","parts"],
[6,"Words and frames","Choose the words to teach, and see a sentence starter for every level, in English and Spanish.","Words and sentence frames","words"],
[7,"Seating","Who is in the room, where to seat them, and tips for teaching this subject to English learners.","Seating and tips","seat"],
[8,"Daily text","A short practice reading that changes every school day, in three versions from easy to hard.","Daily text","text"],
[9,"More texts","Real texts and free sites for finding or making a reading on your topic.","More texts","more"],
[10,"Questions","Discussion questions that go from simple to deep, and an end-of-class question for each group of students.","Questions and exit ticket","check"],
[11,"Choice board","Nine ways for students to show what they learned. A dot marks the ones that need little English.","Student choice board","choice"],
[12,"Supports","A support, or accommodation, changes how a student gets the lesson or shows learning. Tap each one you will give, then log the lesson to keep a record.","Supports you will give","supports"],
[13,"All together","Everything in one plan: the five things first, then every extra you added. Check the list, then print it, copy it, or save it.","Put it all together","review"],
[14,"Teach","Show the objectives on the board, or run the lesson on screen with a timer for each part.","Teach the lesson","teach"],
[15,"Class tools","Quick helpers during class: call on a seat, make groups, spin a word.","Class tools","tools"]];
const ST={};STEPS.forEach(x=>ST[x[4]]=x[0]);
const STEPOF={over:ST.seat,lang:ST.words,act:ST.ideas,text:ST.text,check:ST.check,track:ST.supports,teach:ST.teach};
const CARDSTEP={allcard:ST.review,ideacard:ST.ideas,partcard:ST.parts,wordcard:ST.words,framecard:ST.words,whocard:ST.seat,seatcard:ST.seat,tipcard:ST.seat,txcard:ST.text,excard:ST.more,sitecard:ST.more,quizcard:ST.check,cbcard:ST.choice,acccard:ST.supports,reviewcard:ST.review,teachcard:ST.teach,toolcard:ST.tools,c2:ST.parts,c4:ST.words};
let NUDGE=0,NEW2=false;
function steps(){return S.mode!=="classic";}
function stepCur(){const n=+S.step;return n>=1&&n<=STEPS.length?n:1;}
function simple(){return steps()&&stepCur()<=3;}
function stepSeen(n){return Array.isArray(S.seen)&&S.seen.includes(n);}
function reviewItems(){const d=std(),g=groups(),t=txState(),io=ideasOn(),r=TX[txIndex()],ex=exOn().length+sitesOn().length;return[
 {n:"Standard and objectives",ok:true,yes:d.c+" · "+objs()[S.obj],s:ST.std},
 {n:"English learners counted",ok:g.n>0,yes:g.n+" student"+(g.n===1?"":"s")+" counted",no:"No students counted yet. The supports cannot match your class.",s:ST.who},
 {n:"Words and sentence frames",ok:true,yes:vocab().length+" key words; frames for "+F[fn()].label.toLowerCase()+(bi()?", in English and Spanish":""),s:ST.words},
 {n:"Lesson ideas",ok:io.length>0,yes:io.map(x=>x.title).join("; "),no:"None chosen yet.",s:ST.ideas,fix:"ideas"},
 {n:"Daily text",ok:!!t.on,yes:r[1],no:"Not in your plan.",s:ST.text,fix:"tx"},
 {n:"More texts",ok:ex>0,opt:true,yes:ex+" chosen",no:"Optional. None chosen.",s:ST.more},
 {n:"Discussion questions",ok:!!S.qz,yes:"In your plan",no:"Not added.",s:ST.check,fix:"qz"},
 {n:"Exit ticket",ok:!!S.et,yes:"In your plan: "+etSet()[0],no:"Not added.",s:ST.check,fix:"et"},
 {n:"Student choice board",ok:!!S.cb,opt:true,yes:"In your plan",no:"Optional. Not added.",s:ST.choice,fix:"cb"},
 {n:"Supports",ok:S.acc.length>0,yes:S.acc.length+" marked for this lesson",no:"None marked. Mark the ones you will give.",s:ST.supports}];}
function stepMissing(){return reviewItems().filter(x=>!x.ok&&!x.opt);}
function stepDone(n){const g=groups(),k=STEPS[n-1][4];return k==="std"?true:k==="who"?g.n>0:k==="ideas"?ideasOn().length>0:k==="text"?!!txState().on:k==="more"?exOn().length+sitesOn().length>0:k==="check"?!!(S.qz||S.et):k==="choice"?!!S.cb:k==="supports"?S.acc.length>0:k==="review"?stepSeen(n)&&!stepMissing().length:k==="teach"?LOG.some(e=>e.d===today()&&e.c===S.c):stepSeen(n)&&stepCur()!==n;}
function goStep(n,quiet){n=Math.max(1,Math.min(STEPS.length,n));S.step=n;if(!Array.isArray(S.seen))S.seen=[];if(!S.seen.includes(n))S.seen.push(n);NUDGE=0;NEW2=false;const ts=$("toast");if(ts)ts.classList.remove("on");all();if(!quiet){const t=$("steptop");if(n===1)window.scrollTo(0,0);else if(t)t.scrollIntoView();const h=$("steph");if(h){try{h.focus({preventScroll:true});}catch(e){}}}}
function stepSync(){const on=steps(),n=stepCur(),sm=on&&n<=3,b=document.body;b.classList.toggle("steps",on);b.classList.toggle("simple",sm);b.classList.toggle("guided",on);if(on)b.dataset.step=n;else delete b.dataset.step;if(sm)b.dataset.q=n;else delete b.dataset.q;
 for(const id in CARDSTEP){const el=$(id);if(el)el.dataset.step=CARDSTEP[id];}
 const top=$("steptop"),bar=$("bbar"),sp=$("simple"),s=STEPS[n-1];
 if(top){top.innerHTML=on?`<nav class="srow" id="srow" aria-label="Steps">${STEPS.map(x=>`${x[0]===4?'<span class="sdiv">Extras</span>':""}<button class="${x[0]===n?"cur":""} ${stepDone(x[0])?"done":""}" data-stepgo="${x[0]}" ${x[0]===n?'aria-current="step"':""}><i>${stepDone(x[0])&&x[0]!==n?"✓":x[0]}</i>${x[1]}</button>`).join("")}</nav><div class="sprog"><i style="width:${n/STEPS.length*100}%"></i></div><div class="shead"><p class="skick">Step ${n} of ${STEPS.length}${n>3?" · extra":""}</p><h2 id="steph" tabindex="-1">${s[3]}</h2><p>${s[2]}</p></div>`:"";
  const row=$("srow");if(row){const c=row.querySelector(".cur");if(c)row.scrollLeft=c.offsetLeft-row.clientWidth/2+c.offsetWidth/2;}}
 if(sp)sp.innerHTML=sm?simpleHTML():"";
 if(bar)bar.innerHTML=on?`<button data-stepgo="${n-1}" ${n===1?"disabled":""}>‹ Back</button><span>${n} of ${STEPS.length}</span><button class="nx" id="stepnext">${n===2?"Show my plan ›":n<STEPS.length?"Next: "+STEPS[n][1]+" ›":"Back to print"}</button>`
  :`<button data-go="choices">Choices</button><button data-go="plan">My plan</button><button id="bcopy">Copy</button><button id="teachgo3">Teach</button>`;}
function reviewCard(){if(!steps())return "";const it=reviewItems(),miss=it.filter(x=>!x.ok&&!x.opt).length;
 return `<div class="card" id="reviewcard"><h3>${miss?miss+" thing"+(miss>1?"s are":" is")+" not in your plan yet":"Everything is in your plan"}</h3><p class="hint">${miss?"Add what you want, or print without it.":"Print it, copy it, or save it."}</p>
 <ul class="rv">${it.map(x=>`<li class="${x.ok?"ok":x.opt?"opt":"no"}"><span class="rvi" aria-hidden="true">${x.ok?"✓":x.opt?"+":"!"}</span><div><b>${x.n}</b><small>${esc(x.ok?x.yes:x.no)}</small></div>${x.ok?`<button class="lnk" data-stepgo="${x.s}">Change</button>`:x.fix?`<button class="btn" data-fix="${x.fix}">Add it</button>`:`<button class="btn" data-stepgo="${x.s}">Go to step ${x.s}</button>`}</li>`).join("")}</ul>
 ${it.some(x=>!x.ok&&x.fix)?'<div class="row"><button class="btn" id="fixall">Put every extra in</button></div>':""}
 <h4 class="acat">Print, copy, or save the complete plan</h4><div class="row"><button class="btn gold big2" id="rprint">Print the complete plan</button><button class="btn" id="rcopy">Copy the complete plan</button><button class="btn ghost" id="rsave">Save this plan</button></div>
 <p class="hint" id="rmsg">${printHint("For the one-page version, go back to step 3.")}</p><textarea id="rbox" class="cbox" rows="8" readonly aria-label="Plan text"></textarea>
 <h4 class="acat">Saved plans on this device</h4><div class="saved">${PL.length?PL.map((p,i)=>`<div><span>${esc(p.c)} · ${esc(glabel(p.g))}</span><span><button data-load="${i}">Open</button><button data-del="${i}">Delete</button></span></div>`).join(""):'<p class="hint" style="margin:0">No saved plans yet.</p>'}</div>
 <div class="row"><button class="btn ghost" id="new2">${NEW2?"Tap again to clear this plan":"New plan, same class"}</button><button class="btn ghost" id="ezhelp">How it works</button><button class="lnk" id="modeclassic">Use the one-page view</button></div></div>`;}
function allText(){const d=std(),q=qText().split("\n"),p=planText().split("\n").slice(2).filter(x=>!/^Standard: /.test(x));const cut=q.findIndex(x=>/^What to accept:/.test(x));
 return [`COMPLETE PLAN FOR ENGLISH LEARNERS: ${d.k} (${subjName()}, ${glabel(S.g)}, ${S.min} minutes)`,""].concat(q.slice(2,4),["","PART 1. THE FIVE THINGS TO DO:",""],q.slice(5,cut<0?q.length:cut),["PART 2. THE DETAILS AND YOUR EXTRAS:",""],p,[""],cut<0?[]:q.slice(cut,cut+3)).join("\n");}
function textHTML(txt){const L=txt.split("\n"),o=[];let ul=false;const close=()=>{if(ul){o.push("</ul>");ul=false;}};
 L.forEach((raw,i)=>{const t=raw.trim();if(!t){close();return;}if(i===0){o.push(`<h4 class="alt">${esc(t.replace(/^[A-Z ]+: /,""))}</h4>`);return;}
  if(/^PART \d/.test(t)){close();o.push(`<h4 class="alp">${esc(t.replace(/:$/,""))}</h4>`);return;}
  if(!raw.startsWith(" ")&&/:$/.test(t)&&t.length<90){close();o.push(`<h5>${esc(t.replace(/:$/,""))}</h5>`);return;}
  const m=t.replace(/^- /,"").match(/^([^:]{2,70}:)\s+(.*)$/),body=m?`<b>${esc(m[1])}</b> ${esc(m[2])}`:esc(t.replace(/^- /,""));
  if(t.startsWith("- ")){if(!ul){o.push("<ul>");ul=true;}o.push(`<li>${body}</li>`);}else if(raw.startsWith("   ")&&ul){o.push(`<li class="sub">${body}</li>`);}else{close();o.push(`<p${raw.startsWith(" ")?' class="sub"':""}>${body}</p>`);}});
 close();return o.join("");}
function allCard(){if(!steps())return "";return `<div class="card" id="allcard"><h3>Your complete plan</h3><p class="hint noprint">This is exactly what prints. Part 1 is the five things. Part 2 holds the details and every extra you added.</p><div class="allp">${textHTML(allText())}</div></div>`;}
function fixOne(k){if(k==="ideas"){const p=ideaPick();S.ideas=[p[0][0]+p[0][1],p[1][0]+p[1][1]];}else if(k==="cb")S.cb=true;else if(k==="tx")txState().on=true;else if(k==="qz")S.qz=true;else if(k==="et")S.et=true;}
/* printing: the printer window when the page is open on its own; a PDF file when the page is shown inside another app's frame */
function pdfClean(s){return String(s).replace(/[‘’]/g,"'").replace(/[“”]/g,'"').replace(/[–—−]/g,"-").replace(/…/g,"...").replace(/[‹›✓↗]/g,"").replace(/[^\x09\x0A\x20-\x7E\xA0-\xFF]/g,"");}
const PDFLIB=["https://cdn.jsdelivr.net/npm/jspdf@4.2.1/dist/jspdf.umd.min.js","https://unpkg.com/jspdf@4.2.1/dist/jspdf.umd.min.js"];
function loadPdfLib(){const has=()=>window.jspdf&&window.jspdf.jsPDF;return new Promise((ok,no)=>{if(has())return ok();let k=0;const next=()=>{if(k>=PDFLIB.length)return no(new Error("pdf library"));const el=document.createElement("script");el.src=PDFLIB[k++];el.onload=()=>has()?ok():next();el.onerror=next;document.head.appendChild(el);};next();});}
function planPdf(txt,sub){const doc=new window.jspdf.jsPDF({unit:"pt",format:"letter"}),W=doc.internal.pageSize.getWidth(),H=doc.internal.pageSize.getHeight(),M=54,LH=13.5;let y=M;
 const need=h=>{if(y+h>H-M){doc.addPage();y=M;}},font=(b,z)=>{doc.setFont("helvetica",b?"bold":"normal");doc.setFontSize(z);};
 const para=(label,text,ind)=>{const x=M+ind,w=W-M-x;font(true,10.5);const lw=label?doc.getTextWidth(label+" "):0;font(false,10.5);let lines=[];
  if(label&&lw<w*0.6){const first=doc.splitTextToSize(text||" ",w-lw);lines=[first[0]||""];const rest=first.slice(1).join(" ");if(rest)lines=lines.concat(doc.splitTextToSize(rest,w));need(LH);font(true,10.5);doc.text(label,x,y);font(false,10.5);doc.text(lines[0],x+lw,y);y+=LH;lines.slice(1).forEach(l=>{need(LH);doc.text(l,x,y);y+=LH;});}
  else{if(label){need(LH);font(true,10.5);doc.splitTextToSize(label,w).forEach(l=>{need(LH);doc.text(l,x,y);y+=LH;});font(false,10.5);}doc.splitTextToSize(text||"",w).forEach(l=>{need(LH);doc.text(l,x,y);y+=LH;});}};
 const L=pdfClean(txt||planText()).split("\n");
 font(true,16);doc.splitTextToSize(L[0].replace(/^(EL LESSON PLAN|QUICK PLAN FOR ENGLISH LEARNERS|COMPLETE PLAN FOR ENGLISH LEARNERS): /,"").replace(/^./,c=>c.toUpperCase()),W-2*M).forEach(l=>{doc.text(l,M,y+4);y+=20;});font(false,9);doc.text((sub||(txt?"Quick plan for English learners":"EL lesson plan"))+" · printed "+nice(today()),M,y);y+=8;doc.setLineWidth(1);doc.line(M,y,W-M,y);y+=16;
 for(let i=1;i<L.length;i++){const raw=L[i];if(!raw.trim()){y+=5;continue;}const ind=raw.startsWith("   ")?24:raw.startsWith(" ")?12:0;let t=raw.trim();const bullet=t.startsWith("- ");if(bullet)t=t.slice(2);
  if(!ind&&/^PART \d/.test(t)){need(LH*4);y+=10;font(true,13);doc.text(t.replace(/:$/,""),M,y);y+=6;doc.setLineWidth(1.5);doc.line(M,y,W-M,y);y+=LH+2;continue;}
  if(!ind&&/:$/.test(t)&&t.length<90){need(LH*2.2);y+=4;font(true,11.5);doc.text(t.replace(/:$/,""),M,y);y+=4;doc.setLineWidth(.5);doc.line(M,y,W-M,y);y+=LH;continue;}
  const m=t.match(/^([^:]{2,70}:)\s+(.*)$/);if(bullet){need(LH);font(false,10.5);doc.text("•",M+ind,y);}
  if(m)para(m[1],m[2],ind+(bullet?10:0));else para("",t,ind+(bullet?10:0));}
 const n=doc.getNumberOfPages();for(let p=1;p<=n;p++){doc.setPage(p);font(false,8.5);doc.text(pdfClean("EL Lesson Planner · "+std().c+" · page "+p+" of "+n),M,H-30);}
 return doc.output("blob");}
function pdfName(tag){return "EL-"+(tag||"Lesson-Plan")+"-"+std().c.replace(/[^A-Za-z0-9]+/g,"-").replace(/^-|-$/g,"")+"-"+today()+".pdf";}
function printHint(extra){return (window.self!==window.top?"Print saves a PDF of the plan for you to open and print.":"Print opens your printer window. Choose Save as PDF there to keep a copy.")+(extra?" "+extra:"");}
function printFallback(msg,mid){toast(msg);const m=$(mid||"rmsg");if(m)m.textContent=msg+" Tap Copy the plan, paste it into a document, and print from there.";}
async function printPlan(b,txt,tag,cls,sub,mid){if(window.self===window.top){try{document.body.classList.remove("printquick","printall");if(cls)document.body.classList.add(cls);window.print();return;}catch(e){}}
 const lab=b.textContent;b.disabled=true;b.textContent="Making your PDF…";
 try{const dl=window.claude&&typeof window.claude.use==="function"?await window.claude.use("downloads"):null;if(!dl){printFallback("Printing is not available in this view.",mid);return;}
  await loadPdfLib();await dl.save({filename:pdfName(tag),data:planPdf(txt,sub)});toast("PDF saved. Open it and print.");const m=$(mid||"rmsg");if(m)m.textContent="Your PDF was saved. Open it and print.";}
 catch(err){const c=err&&err.code;if(c==="declined")toast("No file was saved.");else if(c==="rate_limited")toast("A save window is already open. Answer it, then try again.");else printFallback("The PDF could not be made here.",mid);}
 finally{b.disabled=false;b.textContent=lab;}}
function copyPlanTo(box){const tx=planText(),no=()=>{const x=$(box);if(x){x.style.display="block";x.value=tx;x.focus();x.select();toast("Select the text and copy it.");}};try{navigator.clipboard.writeText(tx).then(()=>toast("Plan copied. Paste it into any document."),no);}catch(err){no();}}
document.addEventListener("click",e=>{const b=e.target.closest("button");if(!b)return;const d=b.dataset;if(b.id!=="new2"&&NEW2){NEW2=false;}
 if(d.stepgo){goStep(+d.stepgo);}
 else if(b.id==="stepnext"){const n=stepCur();if(n===STEPS.length){goStep(ST.review);return;}if(n===ST.who&&!groups().n){if(NUDGE!==n){NUDGE=n;toast("Tap + for each English learner. If you cannot tell yet, tap Next again and the plan will cover every level.");return;}S.lv=[1,1,1,1,0];S.guess=true;}goStep(n+1);}
 else if(d.fix){fixOne(d.fix);keep();}
 else if(b.id==="fixall"){reviewItems().filter(x=>!x.ok&&x.fix).forEach(x=>fixOne(x.fix));keep();toast("Every extra is in. The supports are yours to mark in step "+ST.supports+".");}
 else if(b.id==="rprint"||(b.id==="print2"&&steps())){printPlan(b,allText(),"Complete-Plan","printall","Complete plan for English learners");}
 else if(b.id==="print2"){printPlan(b);}
 else if(b.id==="rcopy"){const tx=allText(),no=()=>{const x=$("rbox");if(x){x.style.display="block";x.value=tx;x.focus();x.select();toast("Select the text and copy it.");}};try{navigator.clipboard.writeText(tx).then(()=>toast("Complete plan copied. Paste it into any document."),no);}catch(err){no();}}
 else if(b.id==="rsave"){const c=JSON.parse(JSON.stringify(S));if(c.tx&&c.tx.on&&c.tx.pin<0)c.tx.pin=txIndex();PL.unshift(c);PL=PL.slice(0,20);persist();keep();toast("Plan saved on this device.");}
 else if(b.id==="new2"){if(!NEW2){NEW2=true;keep();}else{NEW2=false;const k=JSON.parse(JSON.stringify(DEF));["s","g","lv","langs","newc","min","doms","bi","cls","hideqs","mode","guess","m3"].forEach(x=>k[x]=S[x]);k.c="";S=k;TOFF=0;goStep(1);toast("New plan started for the same class. Choose a standard.");}}
 else if(b.id==="modeclassic"){S.mode="classic";all();window.scrollTo(0,0);}
 else if(b.id==="modesteps"){S.mode="steps";goStep(stepCur());}
 else if(b.id==="qagain"){const k=JSON.parse(JSON.stringify(DEF));["s","g","lv","langs","newc","min","doms","bi","cls","hideqs","mode","guess","m3"].forEach(x=>k[x]=S[x]);k.c="";S=k;TOFF=0;goStep(1);toast("New lesson, same class. Choose a standard.");}
});

window.addEventListener("afterprint",()=>document.body.classList.remove("printquick","printall"));
