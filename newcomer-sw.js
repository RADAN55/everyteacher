/* Newcomer Series service worker — EL Publishing Hub.
   Precaches the Newcomer pages, their translations and fonts; caches PDFs when opened or when the visitor taps "Save for offline". */
const VERSION = "newcomer-v1-"+"20261004";
const CORE = [
"./",
"index.html",
"newcomer-guide.html",
"first-100-words.html",
"elpt-family-guide.html",
"graduation-roadmap.html",
"can-do-checklist.html",
"newcomer-week1.html",
"newcomer-k5.html",
"guide.js",
"newcomer-pwa.js",
"newcomer-manifest.webmanifest",
"icons/el-192.png",
"icons/el-512.png",
"newcomer/i18n/ar.json",
"newcomer/i18n/cando-ar.json",
"newcomer/i18n/cando-es.json",
"newcomer/i18n/cando-ht.json",
"newcomer/i18n/cando-vi.json",
"newcomer/i18n/cando-zh.json",
"newcomer/i18n/elpt-ar.json",
"newcomer/i18n/elpt-es.json",
"newcomer/i18n/elpt-ht.json",
"newcomer/i18n/elpt-vi.json",
"newcomer/i18n/elpt-zh.json",
"newcomer/i18n/es.json",
"newcomer/i18n/ht.json",
"newcomer/i18n/roadmap-ar.json",
"newcomer/i18n/roadmap-es.json",
"newcomer/i18n/roadmap-ht.json",
"newcomer/i18n/roadmap-vi.json",
"newcomer/i18n/roadmap-zh.json",
"newcomer/i18n/vi.json",
"newcomer/i18n/words-ar.json",
"newcomer/i18n/words-es.json",
"newcomer/i18n/words-ht.json",
"newcomer/i18n/words-vi.json",
"newcomer/i18n/words-zh.json",
"newcomer/i18n/zh.json",
"newcomer/fonts/NotoSansArabic-Bold.ttf",
"newcomer/fonts/NotoSansArabic-Regular.ttf",
"thumbs/newcomer-guide.jpg",
"thumbs/first-100-words.jpg",
"thumbs/elpt-family-guide.jpg",
"thumbs/graduation-roadmap.jpg",
"thumbs/can-do-checklist.jpg"
];
const PDFS = ["newcomer/Newcomer-Guide-US-Schools-ar.pdf", "newcomer/Newcomer-Guide-US-Schools-es.pdf", "newcomer/Newcomer-Guide-US-Schools-ht.pdf", "newcomer/Newcomer-Guide-US-Schools-vi.pdf", "newcomer/Newcomer-Guide-US-Schools-zh.pdf"];
self.addEventListener("install", e => { e.waitUntil(caches.open(VERSION).then(c => c.addAll(CORE)).then(() => self.skipWaiting())); });
self.addEventListener("activate", e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k.startsWith("newcomer-v") && k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener("message", e => {
  if (e.data && e.data.type === "SAVE_ALL") {
    e.waitUntil(caches.open(VERSION).then(async c => { let n = 0; for (const u of PDFS) { try { const r = await fetch(u, {cache: "no-cache"}); if (r.ok) { await c.put(u, r); n++; } } catch (_) {} } const cs = await self.clients.matchAll(); cs.forEach(cl => cl.postMessage({type: "SAVED", n, total: PDFS.length})); }));
  }
});
self.addEventListener("fetch", e => {
  const req = e.request; if (req.method !== "GET") return;
  const url = new URL(req.url); if (url.origin !== location.origin) return;
  const p = url.pathname;
  const isAsset = /\.(pdf|ttf|woff2?|png|jpe?g|svg|json)$/i.test(p);
  if (isAsset) { // cache-first, fill cache on first use
    e.respondWith(caches.match(req).then(hit => hit || fetch(req).then(r => { if (r.ok) { const cp = r.clone(); caches.open(VERSION).then(c => c.put(req, cp)); } return r; })));
    return;
  }
  if (req.mode === "navigate" || /\.(html|js|webmanifest)$/i.test(p) || p.endsWith("/")) { // network-first, cache fallback
    e.respondWith(fetch(req).then(r => { if (r.ok) { const cp = r.clone(); caches.open(VERSION).then(c => c.put(req, cp)); } return r; }).catch(() => caches.match(req).then(hit => hit || caches.match("newcomer-guide.html"))));
  }
});
