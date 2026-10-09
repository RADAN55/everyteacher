/* Storm Lens service worker — offline after first load (page, fonts, models) */
const C="storm-lens-v6";
self.addEventListener("install",e=>{ self.skipWaiting(); e.waitUntil(caches.open(C).then(c=>c.addAll(["./","./index.html"]).catch(()=>{}))); });
self.addEventListener("activate",e=>{ e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==C).map(k=>caches.delete(k))))); self.clients.claim(); });
self.addEventListener("fetch",e=>{ const u=e.request.url; if(e.request.method!=="GET") return;
  const cacheable=/cdn\.jsdelivr\.net|unpkg\.com|tfhub\.dev|storage\.googleapis\.com|fonts\.(googleapis|gstatic)\.com/.test(u)||u.startsWith(self.registration.scope);
  if(!cacheable) return;
  e.respondWith(caches.match(e.request).then(hit=>hit||fetch(e.request).then(r=>{ if(r&&r.ok){ const cp=r.clone(); caches.open(C).then(c=>c.put(e.request,cp)); } return r; }).catch(()=>hit))); });
