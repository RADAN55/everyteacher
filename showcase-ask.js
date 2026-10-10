/* "That worked? Send it in."

   Submissions come from the moment a teacher has just made something, not
   from a link in a catalog. A page opts in with one attribute:

     <body data-showcase-ask="#out">          watch that container
     <body data-showcase-ask-on="copy">       or: after the first copy

   It asks once, it can be dismissed for good, and it never interrupts —
   it appears underneath the thing the teacher just made. */
(function () {
  "use strict";
  if (window.__elShowcaseAsk) return;
  window.__elShowcaseAsk = true;

  var KEY = "elhub.showcase.asked";
  var MAIL = "richard.spanishteacher@gmail.com";

  function dismissed() {
    try { return localStorage.getItem(KEY) === "no"; } catch (e) { return false; }
  }
  function remember() {
    try { localStorage.setItem(KEY, "no"); } catch (e) {}
  }

  function tool() {
    var t = (document.title || "").split("·")[0].trim();
    return t || "an EL Publishing tool";
  }

  function body() {
    return (
      "Here is something I made with " + tool() + ".\n\n" +
      "What it is:\n" +
      "Subject and grade:\n" +
      "Standard:\n" +
      "What happened when I used it:\n" +
      "Name and school as you want it credited (or say anonymous):\n\n" +
      "I have attached it / pasted it below.\n" +
      "No student names are included.\n"
    );
  }

  var CSS =
    ".sc-ask{margin:22px 0 0;background:var(--paper,#fff);border:1px solid var(--rule,#DCDEE9);" +
    "border-left:4px solid var(--gold,#C9A227);padding:16px 18px 14px;" +
    "font-family:Inter,-apple-system,'Segoe UI',sans-serif}" +
    ".sc-ask h3{font-family:Fraunces,Georgia,serif;font-size:18px;font-weight:600;" +
    "color:var(--navy,#1E2761);margin:0 0 6px;line-height:1.25}" +
    ".sc-ask p{margin:0;font-size:14.3px;line-height:1.5;color:var(--muted,#5D6480)}" +
    ".sc-ask .sc-r{margin-top:12px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}" +
    ".sc-ask a.sc-go{background:var(--gold,#C9A227);color:var(--navy-dk,#141A44);" +
    "font-weight:700;font-size:14px;text-decoration:none;padding:9px 17px;border-radius:999px}" +
    ".sc-ask a.sc-see{font-size:13.5px;font-weight:600;color:var(--navy,#1E2761);" +
    "text-decoration:none;border-bottom:1px solid var(--gold-lt,#EBD9A0)}" +
    ".sc-ask button.sc-no{margin-left:auto;background:none;border:0;cursor:pointer;" +
    "font:inherit;font-size:13px;color:var(--muted,#5D6480);text-decoration:underline}";

  function card() {
    var el = document.createElement("aside");
    el.className = "sc-ask";
    el.innerHTML =
      "<h3>That worked? Put it where other teachers can find it.</h3>" +
      "<p>The Showcase is where Mississippi teachers share what they built with these " +
      "tools. Send yours and I will post it with your name and school, or anonymously — " +
      "whichever you prefer. No student names, ever.</p>" +
      '<div class="sc-r">' +
        '<a class="sc-go" href="mailto:' + MAIL + "?subject=" +
          encodeURIComponent("Showcase: something I made with " + tool()) +
          "&body=" + encodeURIComponent(body()) + '">Send it in</a>' +
        '<a class="sc-see" href="showcase.html">See the Showcase &rarr;</a>' +
        '<button type="button" class="sc-no">Not now</button>' +
      "</div>";
    el.querySelector(".sc-no").addEventListener("click", function () {
      remember();
      el.remove();
    });
    return el;
  }

  function place(after) {
    if (document.querySelector(".sc-ask") || dismissed()) return;
    var s = document.createElement("style");
    s.textContent = CSS;
    document.head.appendChild(s);
    after.parentNode.insertBefore(card(), after.nextSibling);
  }

  function start() {
    if (dismissed()) return;
    var b = document.body;
    var sel = b.getAttribute("data-showcase-ask");
    var on = b.getAttribute("data-showcase-ask-on");

    if (sel) {
      var host = document.querySelector(sel);
      if (host) {
        /* Measure what is already there — these containers often hold an
           empty-state message — and wait for real output to land on top of
           it. Firing on page load would be asking before they made anything. */
        var base = host.textContent.trim().length;
        var seen = function () {
          if (host.textContent.trim().length < base + 200) return;
          obs.disconnect();
          place(host);
        };
        var obs = new MutationObserver(seen);
        obs.observe(host, { childList: true, subtree: true });
      }
    }
    if (on === "copy") {
      document.addEventListener("click", function once(ev) {
        var t = ev.target.closest("[data-copy],.copybtn,[data-act='copy']");
        if (!t) return;
        document.removeEventListener("click", once, true);
        setTimeout(function () {
          var anchor = t.closest("section,article,.card,.panel") || t;
          place(anchor);
        }, 400);
      }, true);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
})();
