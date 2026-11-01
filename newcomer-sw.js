/* Retired Oct 31, 2026: the Newcomer pages are served by hub-sw.js, the worker
   for the whole hub. This stub clears the old cache and steps aside. */
self.addEventListener("install", e => self.skipWaiting());
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k.startsWith("newcomer-v")).map(k => caches.delete(k))))
    .then(() => self.registration.unregister())
    .then(() => self.clients.matchAll({type: "window"}))
    .then(cs => cs.forEach(c => c.navigate(c.url))));
});
