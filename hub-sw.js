/* EL Publishing Hub — service worker (whole hub).
   One worker for the whole site, registered by hub-chrome.js on every page
   and by newcomer-pwa.js on the Newcomer pages (it used to have a worker of
   its own at the same scope; two workers at one scope replace each other, so
   the Newcomer precache and its "Save for offline" message live here now).

   Strategy
   - Pages, scripts, styles, JSON: network first, fall back to the cache, and
     for a page that was never cached, to offline.html. The hub changes often
     (Now Showing, resource of the week), so a page is never served stale
     while the network is up.
   - Fonts, images, PDFs, audio: cache first, filled on first use.
   - Sub-apps with their own worker (storm-lens/) keep it: a more specific
     scope wins, so this worker never sees those requests.

   Bump VERSION on any change to the shell list; the activate step drops old
   caches, including the retired newcomer-v* ones. */
const VERSION = "elhub-v1-20261031b";

const SHELL = [
  "./",
  "index.html",
  "all.html",
  "by-subject.html",
  "whats-new.html",
  "pd-library.html",
  "leaders.html",
  "about.html",
  "offline.html",
  "theme.css",
  "hub-chrome.js",
  "guide.js",
  "catalog.json",
  "search-index.json",
  "manifest.webmanifest",
  "brand/mark.svg",
  "icons/el-32.png",
  "icons/el-180.png",
  "icons/el-192.png",
  "icons/el-512.png",
  "icons/el-maskable-512.png",
  "fonts/fraunces.woff2",
  "fonts/fraunces-italic.woff2",
  /* Newcomer Series — installable offline since Oct 2026 */
  "newcomer-guide.html",
  "first-100-words.html",
  "elpt-family-guide.html",
  "graduation-roadmap.html",
  "can-do-checklist.html",
  "newcomer-week1.html",
  "newcomer-k5.html",
  "newcomer-pwa.js",
  "newcomer/i18n/ar.json", "newcomer/i18n/es.json", "newcomer/i18n/ht.json",
  "newcomer/i18n/vi.json", "newcomer/i18n/zh.json",
  "newcomer/i18n/cando-ar.json", "newcomer/i18n/cando-es.json", "newcomer/i18n/cando-ht.json",
  "newcomer/i18n/cando-vi.json", "newcomer/i18n/cando-zh.json",
  "newcomer/i18n/elpt-ar.json", "newcomer/i18n/elpt-es.json", "newcomer/i18n/elpt-ht.json",
  "newcomer/i18n/elpt-vi.json", "newcomer/i18n/elpt-zh.json",
  "newcomer/i18n/roadmap-ar.json", "newcomer/i18n/roadmap-es.json", "newcomer/i18n/roadmap-ht.json",
  "newcomer/i18n/roadmap-vi.json", "newcomer/i18n/roadmap-zh.json",
  "newcomer/i18n/words-ar.json", "newcomer/i18n/words-es.json", "newcomer/i18n/words-ht.json",
  "newcomer/i18n/words-vi.json", "newcomer/i18n/words-zh.json",
  "newcomer/fonts/NotoSansArabic-Bold.ttf",
  "newcomer/fonts/NotoSansArabic-Regular.ttf"
];

/* Pulled in only when the visitor taps "Save for offline" on a Newcomer page. */
const NEWCOMER_PDFS = [
  "newcomer/Newcomer-Guide-US-Schools-ar.pdf",
  "newcomer/Newcomer-Guide-US-Schools-es.pdf",
  "newcomer/Newcomer-Guide-US-Schools-ht.pdf",
  "newcomer/Newcomer-Guide-US-Schools-vi.pdf",
  "newcomer/Newcomer-Guide-US-Schools-zh.pdf"
];

self.addEventListener("install", e => {
  e.waitUntil(
    caches.open(VERSION).then(async c => {
      /* one missing file must not sink the whole install */
      await Promise.all(SHELL.map(u => c.add(u).catch(() => null)));
    }).then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", e => {
  e.waitUntil(
    caches.keys()
      .then(ks => Promise.all(
        ks.filter(k => (k.startsWith("elhub-v") || k.startsWith("newcomer-v")) && k !== VERSION)
          .map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("message", e => {
  const d = e.data || {};
  if (d.type === "SKIP_WAITING") { self.skipWaiting(); return; }
  if (d.type === "SAVE_ALL") {
    e.waitUntil(caches.open(VERSION).then(async c => {
      let n = 0;
      for (const u of NEWCOMER_PDFS) {
        try { const r = await fetch(u, { cache: "no-cache" }); if (r.ok) { await c.put(u, r); n++; } } catch (_) {}
      }
      const cs = await self.clients.matchAll();
      cs.forEach(cl => cl.postMessage({ type: "SAVED", n, total: NEWCOMER_PDFS.length }));
    }));
  }
});

const ASSET = /\.(pdf|ttf|otf|woff2?|png|jpe?g|gif|webp|svg|ico|mp3|m4a|ogg|wav|mp4|webm)$/i;
const DOC = /\.(html?|js|css|json|xml|webmanifest|txt)$/i;

self.addEventListener("fetch", e => {
  const req = e.request;
  if (req.method !== "GET") return;
  let url;
  try { url = new URL(req.url); } catch (_) { return; }
  if (url.origin !== location.origin) return;           /* fonts.googleapis, CDNs: let the browser handle them */
  const p = url.pathname;

  if (ASSET.test(p)) {
    e.respondWith(
      caches.match(req).then(hit => hit || fetch(req).then(r => {
        if (r.ok) { const cp = r.clone(); caches.open(VERSION).then(c => c.put(req, cp)); }
        return r;
      }))
    );
    return;
  }

  if (req.mode === "navigate" || DOC.test(p) || p.endsWith("/")) {
    e.respondWith(
      fetch(req).then(r => {
        if (r.ok) { const cp = r.clone(); caches.open(VERSION).then(c => c.put(req, cp)); }
        return r;
      }).catch(() => caches.match(req, { ignoreSearch: true }).then(hit => {
        if (hit) return hit;
        if (req.mode === "navigate") return caches.match("offline.html");
        return Response.error();
      }))
    );
  }
});
