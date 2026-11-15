/* EL Publishing: a small floating Home button for the pages that have no
   top bar (full-screen stages, practice apps in their own folders). It finds
   the hub from its own src, so a page in a subfolder links to ../index.html.
   Skipped when the page is embedded in another page, and in print. */
(function () {
  "use strict";
  if (window.__elHomeBtn) return;
  window.__elHomeBtn = true;
  try { if (window.top !== window.self) return; } catch (e) { return; }
  function go() {
    if (document.querySelector(".hubbar") || document.getElementById("elHomeBtn")) return;
    var me = document.querySelector('script[src$="home-button.js"]');
    var base = me ? me.getAttribute("src").replace(/home-button\.js$/, "") : "";
    var css = document.createElement("style");
    css.textContent =
      "#elHomeBtn{position:fixed;left:12px;bottom:calc(12px + env(safe-area-inset-bottom,0px));z-index:2147483000;" +
      "display:inline-flex;align-items:center;gap:6px;height:44px;padding:0 16px 0 12px;border-radius:999px;" +
      "background:#141A44;color:#fff;border:1.5px solid #C9A227;box-shadow:0 4px 14px rgba(0,0,0,.35);" +
      "font:600 15px/1 Inter,-apple-system,'Segoe UI',Arial,sans-serif;text-decoration:none;opacity:.92}" +
      "#elHomeBtn:hover,#elHomeBtn:focus-visible{opacity:1;background:#C9A227;color:#141A44;outline:none}" +
      "#elHomeBtn svg{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:2}" +
      "@media print{#elHomeBtn{display:none}}";
    document.head.appendChild(css);
    var a = document.createElement("a");
    a.id = "elHomeBtn";
    a.href = base + "index.html";
    a.setAttribute("aria-label", "Home, EL Publishing hub");
    a.innerHTML =
      '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3.5 11 12 3.5 20.5 11' +
      'M5.5 9.5V20h4.8v-5.6h3.4V20h4.8V9.5" stroke-linejoin="round" stroke-linecap="round"/></svg>' +
      "<span>Home</span>";
    document.body.appendChild(a);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", go);
  else go();
})();
