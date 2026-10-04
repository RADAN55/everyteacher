/* Newcomer Series: install + offline controls. Loaded only on the Newcomer pages. */
(function(){
"use strict";
if(!("serviceWorker" in navigator)) return;
var base=document.querySelector('script[src$="newcomer-pwa.js"]'); base=base?base.getAttribute("src").replace(/newcomer-pwa\.js$/,""):"";
// manifest + theme
var l=document.createElement("link"); l.rel="manifest"; l.href=base+"newcomer-manifest.webmanifest"; document.head.appendChild(l);
var m=document.createElement("meta"); m.name="theme-color"; m.content="#1E2761"; document.head.appendChild(m);
var a=document.createElement("link"); a.rel="apple-touch-icon"; a.href=base+"icons/el-192.png"; document.head.appendChild(a);
var ac=document.createElement("meta"); ac.name="apple-mobile-web-app-capable"; ac.content="yes"; document.head.appendChild(ac);

var css=".nc-off{position:fixed;left:14px;bottom:14px;z-index:9997;display:flex;gap:8px;flex-wrap:wrap;align-items:center;font:14px Inter,-apple-system,'Segoe UI',sans-serif}"+
".nc-off button{background:#fff;color:#1E2761;border:1.5px solid #1E2761;border-radius:999px;padding:8px 13px;font:600 13px Inter,sans-serif;cursor:pointer;box-shadow:0 4px 14px rgba(30,39,97,.15)}"+
".nc-off button.gold{background:#C9A227;border-color:#C9A227;color:#141A44}.nc-off .st{background:#1E2761;color:#EBD9A0;border-radius:999px;padding:7px 12px;font-size:12.5px}"+
".nc-ios{position:fixed;left:14px;right:14px;bottom:62px;z-index:9997;background:#fff;border:1px solid #DCDEE9;border-top:5px solid #C9A227;padding:12px 14px;font:14px/1.45 Inter,sans-serif;color:#1F2330;max-width:420px;box-shadow:0 10px 30px rgba(30,39,97,.2)}"+
".nc-ios b{color:#1E2761}.nc-ios .x{float:right;border:0;background:transparent;font-size:18px;cursor:pointer}"+
"@media print{.nc-off,.nc-ios{display:none!important}}";
var st=document.createElement("style"); st.textContent=css; document.head.appendChild(st);

var wrap=document.createElement("div"); wrap.className="nc-off"; wrap.setAttribute("aria-label","Offline and install options");
var installBtn=document.createElement("button"); installBtn.className="gold"; installBtn.textContent="Install · Instalar"; installBtn.hidden=true;
var saveBtn=document.createElement("button"); saveBtn.textContent="Save for offline · Guardar sin internet";
var status=document.createElement("span"); status.className="st"; status.hidden=true;
wrap.appendChild(installBtn); wrap.appendChild(saveBtn); wrap.appendChild(status); document.body.appendChild(wrap);

var deferred=null;
window.addEventListener("beforeinstallprompt",function(e){ e.preventDefault(); deferred=e; installBtn.hidden=false; });
installBtn.onclick=function(){ if(!deferred){ iosHelp(); return; } deferred.prompt(); deferred.userChoice.then(function(){ deferred=null; installBtn.hidden=true; }); };
window.addEventListener("appinstalled",function(){ installBtn.hidden=true; say("Installed · Instalado"); });

var isIOS=/iphone|ipad|ipod/i.test(navigator.userAgent) && !window.MSStream;
var standalone=window.matchMedia("(display-mode: standalone)").matches || navigator.standalone;
if(isIOS && !standalone){ installBtn.hidden=false; }
function iosHelp(){
  if(document.querySelector(".nc-ios")) return;
  var d=document.createElement("div"); d.className="nc-ios";
  d.innerHTML='<button class="x" aria-label="Close">×</button><b>Add to your home screen · Agregar a la pantalla de inicio</b><br>Tap the Share button <span aria-hidden="true">⎙</span>, then <b>Add to Home Screen</b>.<br><span style="color:#5D6480">Toca el botón Compartir y luego <b>Agregar a pantalla de inicio</b>.</span>';
  d.querySelector(".x").onclick=function(){ d.remove(); }; document.body.appendChild(d);
}

function say(t){ status.textContent=t; status.hidden=false; clearTimeout(say.h); say.h=setTimeout(function(){ status.hidden=true; },3500); }

navigator.serviceWorker.register(base+"newcomer-sw.js",{scope:base||"./"}).then(function(reg){
  saveBtn.onclick=function(){
    saveBtn.disabled=true; saveBtn.textContent="Saving… · Guardando…";
    var sw=reg.active||reg.waiting||reg.installing;
    if(sw) sw.postMessage({type:"SAVE_ALL"}); else { saveBtn.disabled=false; saveBtn.textContent="Save for offline · Guardar sin internet"; }
  };
  navigator.serviceWorker.addEventListener("message",function(e){
    if(e.data&&e.data.type==="SAVED"){ saveBtn.disabled=false; saveBtn.textContent="Saved offline ✓ · Guardado"; say("Pages + "+e.data.n+" of "+e.data.total+" PDFs saved on this device"); setTimeout(function(){ saveBtn.textContent="Save for offline · Guardar sin internet"; },5000); }
  });
}).catch(function(){ saveBtn.hidden=true; });

function net(){ if(!navigator.onLine) say("Offline · reading saved copy · Sin internet: copia guardada"); }
window.addEventListener("offline",net); window.addEventListener("online",function(){ say("Back online · Conectado"); }); net();
})();
