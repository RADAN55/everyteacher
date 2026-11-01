/* EL Publishing — the top bar and the light/dark control.
   Styles live in theme.css, which is linked in the head so the colours are
   right before first paint. This file only builds the bar and wires it up.

   The theme is already applied by a small snippet in each page's head; this
   script just keeps the control in sync and remembers the choice. */
(function () {
  "use strict";
  if (window.__elHubBar) return;
  window.__elHubBar = true;

  /* ---- the app ----------------------------------------------------------
     The hub installs as an app (a PWA): a home-screen icon on a phone or a
     Chromebook, its own window, and the pages you have opened kept on the
     device for when the Wi-Fi drops. Everything the app needs lives in
     manifest.webmanifest and hub-sw.js; this block only wires them in, on
     every page, including the full-screen stages that skip the bar below. */
  var APP = { prompt: null, standalone: false, ios: false, base: "" };
  (function app() {
    try {
      var me = document.querySelector('script[src$="hub-chrome.js"]');
      APP.base = me ? me.getAttribute("src").replace(/hub-chrome\.js$/, "") : "";
      var head = document.head;
      function add(tag, attrs) {
        var el = document.createElement(tag);
        for (var k in attrs) el.setAttribute(k, attrs[k]);
        head.appendChild(el); return el;
      }
      if (!document.querySelector('link[rel="manifest"]'))
        add("link", { rel: "manifest", href: APP.base + "manifest.webmanifest" });
      if (!document.querySelector('meta[name="theme-color"]'))
        add("meta", { name: "theme-color", content: "#141A44" });
      if (!document.querySelector('meta[name="apple-mobile-web-app-capable"]'))
        add("meta", { name: "apple-mobile-web-app-capable", content: "yes" });
      if (!document.querySelector('meta[name="apple-mobile-web-app-status-bar-style"]'))
        add("meta", { name: "apple-mobile-web-app-status-bar-style", content: "black-translucent" });
      if (!document.querySelector('meta[name="apple-mobile-web-app-title"]'))
        add("meta", { name: "apple-mobile-web-app-title", content: "EL Hub" });
      if (!document.querySelector('link[rel="apple-touch-icon"]'))
        add("link", { rel: "apple-touch-icon", href: APP.base + "icons/el-180.png" });

      APP.ios = /iphone|ipad|ipod/i.test(navigator.userAgent) && !window.MSStream;
      APP.standalone = (window.matchMedia && window.matchMedia("(display-mode: standalone)").matches) || navigator.standalone === true;
      if (APP.standalone) document.documentElement.setAttribute("data-app", "standalone");

      window.addEventListener("beforeinstallprompt", function (e) {
        e.preventDefault(); APP.prompt = e;
        document.dispatchEvent(new CustomEvent("elhub:installable"));
      });
      window.addEventListener("appinstalled", function () {
        APP.prompt = null;
        document.dispatchEvent(new CustomEvent("elhub:installed"));
      });

      if (!("serviceWorker" in navigator)) return;
      /* A sub-app with its own worker (storm-lens/) keeps it: its scope is
         more specific. Pages served from file:// or a preview have no scope. */
      if (location.protocol !== "https:" && location.hostname !== "localhost") return;
      navigator.serviceWorker.register(APP.base + "hub-sw.js", { scope: APP.base || "./" })
        .then(function (reg) {
          reg.addEventListener("updatefound", function () {
            var nw = reg.installing; if (!nw) return;
            nw.addEventListener("statechange", function () {
              if (nw.state === "installed" && navigator.serviceWorker.controller)
                document.dispatchEvent(new CustomEvent("elhub:update"));
            });
          });
        }).catch(function () {});
    } catch (e) {}
  })();

  /* Some pages take the whole screen on purpose — a simulation, a practice
     session. A bar across the top of those is in the way, so they opt out
     with data-no-hubbar on <html> and keep only the theme. */
  if (document.documentElement.hasAttribute("data-no-hubbar")) return;

  var KEY = "elhub.theme";
  var HOME = "index.html";

  var LINKS = [
    ["Start here", "index.html#start"],
    ["By subject", "by-subject.html"],
    ["PD library", "pd-library.html"],
    ["All resources", "all.html"],
    ["For districts", "leaders.html"],
    ["What's new", "whats-new.html"],
    ["About", "about.html"]
  ];

  /* the mark: four book spines of rising height on a shelf */
  var MARK =
    '<svg viewBox="0 0 64 64" aria-hidden="true" focusable="false">' +
    '<rect x="9" y="34" width="10" height="18" rx="1" fill="#6B74A8"/>' +
    '<rect x="22" y="27" width="10" height="25" rx="1" fill="#C9A227"/>' +
    '<rect x="35" y="20" width="10" height="32" rx="1" fill="#A9B1DA"/>' +
    '<rect x="48" y="13" width="10" height="39" rx="1" fill="#FFFFFF"/>' +
    '<rect x="6" y="52" width="55" height="3.4" rx="1.2" fill="#C9A227"/></svg>';

  var SUN =
    '<svg class="sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4.4"/>' +
    '<path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.2 5.2l1.4 1.4' +
    'M17.4 17.4l1.4 1.4M18.8 5.2l-1.4 1.4M6.6 17.4l-1.4 1.4" ' +
    'stroke-linecap="round"/></svg>';
  var MOON =
    '<svg class="moon" viewBox="0 0 24 24">' +
    '<path d="M20 14.5A8.5 8.5 0 1 1 9.5 4a6.8 6.8 0 0 0 10.5 10.5Z" ' +
    'stroke-linejoin="round"/></svg>';
  var DOWN =
    '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v12m0 0 4.5-4.5M12 15l-4.5-4.5' +
    'M4 17v2.5A1.5 1.5 0 0 0 5.5 21h13a1.5 1.5 0 0 0 1.5-1.5V17" ' +
    'stroke-linejoin="round" stroke-linecap="round"/></svg>';
  var BACK =
    '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7" ' +
    'stroke-linejoin="round" stroke-linecap="round"/></svg>';
  var PLANE =
    '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 3 10.5 13.5M21 3l-6.5 18' +
    '-4-8-8-4Z" stroke-linejoin="round" stroke-linecap="round"/></svg>';

  /* ---- which page are we on? ---------------------------------------- */
  var here = location.pathname.split("/").pop() || HOME;

  /* ---- build ---------------------------------------------------------- */
  /* a div, not a <header>: most pages style their own masthead with
     header{...} and a header::before texture overlay, and the bar would
     inherit both — including an overlay that swallowed its own clicks */
  var bar = document.createElement("div");
  bar.className = "hubbar";
  bar.setAttribute("role", "banner");

  var nav = LINKS.map(function (l) {
    var file = l[1].split("#")[0];
    var cur = file === here || (here === HOME && file === HOME);
    return '<a href="' + l[1] + '"' + (cur ? ' aria-current="page"' : "") +
      ">" + l[0] + "</a>";
  }).join("");

  var canBack = APP.standalone && history.length > 1 && here !== HOME;
  bar.innerHTML =
    '<div class="hubbar-in">' +
      (canBack ? '<button type="button" class="hb-back" id="hbBack" aria-label="Back">' + BACK + "</button>" : "") +
      '<a class="hb-home" href="' + HOME + '" aria-label="EL Publishing, home">' +
        MARK + "<b>EL Publishing</b></a>" +
      '<nav aria-label="Hub">' + nav + "</nav>" +
      '<button type="button" class="hb-install" id="hbInstall" hidden>' + DOWN +
        "<span>Get the app</span></button>" +
      '<button type="button" class="hb-send" id="hbSend">' + PLANE +
        "<span>Send to a teacher</span></button>" +
      '<button type="button" class="hb-theme" id="hbTheme" aria-live="polite">' +
        SUN + MOON + "</button>" +
    "</div>" +
    '<div class="hb-sheet" id="hbSheet" hidden></div>';

  function place() {
    if (document.body.firstChild) document.body.insertBefore(bar, document.body.firstChild);
    else document.body.appendChild(bar);
    offsetStickies();
    wire();
  }

  /* Pages across this hub each pin one thing to the top — a table of
     contents, a filter row. They were written before this bar existed, so
     move them down by its height rather than let the bar sit on them. */
  function offsetStickies() {
    try {
      var h = bar.getBoundingClientRect().height || 50;
      var all = document.querySelectorAll("body *");
      for (var i = 0; i < all.length; i++) {
        var el = all[i];
        if (el === bar || bar.contains(el)) continue;
        var cs = getComputedStyle(el);
        if (cs.position !== "sticky" && cs.position !== "-webkit-sticky") continue;
        if (parseFloat(cs.top) !== 0) continue;
        el.style.top = h + "px";
      }
      document.documentElement.style.scrollPaddingTop = (h + 8) + "px";
    } catch (e) {}
  }

  /* ---- the control ----------------------------------------------------- */
  function current() {
    return document.documentElement.getAttribute("data-theme") === "dark"
      ? "dark" : "light";
  }
  function label(btn) {
    var dark = current() === "dark";
    btn.setAttribute("aria-label", dark ? "Switch to light mode" : "Switch to dark mode");
    btn.setAttribute("title", dark ? "Light mode" : "Dark mode");
  }
  /* ---- send it to someone --------------------------------------------- */
  /* Teachers find this site because another teacher sent it to them. That
     should be one tap, not copy-the-address-bar. */
  function note() {
    var t = (document.title || "EL Publishing").split(" · ")[0];
    /* by file, not by path — this has to keep working if the site moves */
    var f = location.pathname.split("/").pop();
    return (f === "" || f === HOME)
      ? "Free resources for English learners — no login, no account, nothing to buy."
      : "Thought of you: " + t + ". Free, no login.";
  }
  function wireSend() {
    var btn = document.getElementById("hbSend"), sheet = document.getElementById("hbSheet");
    if (!btn || !sheet) return;
    var url = location.href.split("#")[0], msg = note();

    function close() { sheet.hidden = true; btn.setAttribute("aria-expanded", "false"); }
    function open() {
      sheet.innerHTML =
        '<div class="hb-sheet-in">' +
          "<p>" + msg.replace(/</g, "&lt;") + "</p>" +
          '<a href="mailto:?subject=' + encodeURIComponent("Something for your EL students") +
            "&body=" + encodeURIComponent(msg + "\n\n" + url) +
            '">Email it<small>Opens your mail, already written</small></a>' +
          '<a href="sms:?&body=' + encodeURIComponent(msg + " " + url) +
            '">Text it<small>Opens Messages on a phone</small></a>' +
          '<button type="button" id="hbCopy">Copy the link' +
            "<small>Paste it anywhere</small></button>" +
          (navigator.share
            ? '<button type="button" id="hbMore">More ways' +
              "<small>Your device's own share sheet</small></button>" : "") +
        "</div>";
      sheet.hidden = false;
      btn.setAttribute("aria-expanded", "true");
      var more = document.getElementById("hbMore");
      if (more) {
        more.addEventListener("click", function () {
          navigator.share({ title: document.title, text: msg, url: url })
            .catch(function () {});
          close();
        });
      }
      document.getElementById("hbCopy").addEventListener("click", function () {
        var done = function () { this.textContent = "Copied"; }.bind(this);
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(url).then(done, fallback);
        } else { fallback(); }
        var self = this;
        function fallback() {
          var ta = document.createElement("textarea");
          ta.value = url; ta.style.cssText = "position:fixed;opacity:0";
          document.body.appendChild(ta); ta.select();
          try { document.execCommand("copy"); self.textContent = "Copied"; } catch (e) {}
          ta.remove();
        }
      });
    }

    btn.setAttribute("aria-expanded", "false");
    btn.addEventListener("click", function () {
      /* Always show these three first. Handing straight to navigator.share
         looked tidy but hid email behind an OS sheet on every device that
         supports it, which is most of them. */
      sheet.hidden ? open() : close();
    });
    document.addEventListener("click", function (ev) {
      if (!sheet.hidden && !sheet.contains(ev.target) && !btn.contains(ev.target)) close();
    });
    document.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape" && !sheet.hidden) { close(); btn.focus(); }
    });
  }

  /* ---- install it ------------------------------------------------------ */
  /* Chrome and Edge (Chromebooks, Android, Windows) hand us a prompt; we show
     the button once it arrives. iOS has no prompt, so the button opens the
     two-tap instructions instead. Once installed, the button goes away. */
  function wireInstall() {
    var btn = document.getElementById("hbInstall"), sheet = document.getElementById("hbSheet");
    if (!btn || !sheet || APP.standalone) return;
    function show() { btn.hidden = false; }
    function hide() { btn.hidden = true; }
    if (APP.prompt || APP.ios) show();
    document.addEventListener("elhub:installable", show);
    document.addEventListener("elhub:installed", hide);
    btn.addEventListener("click", function () {
      if (APP.prompt) {
        APP.prompt.prompt();
        APP.prompt.userChoice.then(function (r) {
          if (r && r.outcome === "accepted") hide();
          APP.prompt = null;
        }).catch(function () {});
        return;
      }
      /* no prompt: say how, for this device */
      var how = APP.ios
        ? "Tap the <b>Share</b> button <span aria-hidden=\"true\">&#x2BAD;</span> at the bottom of Safari, then <b>Add to Home Screen</b>."
        : "Open the browser menu <b>&#8942;</b> and choose <b>Install app</b> or <b>Add to Home screen</b>.";
      sheet.innerHTML =
        '<div class="hb-sheet-in">' +
          "<p><b>EL Hub</b> on your home screen: its own icon, its own window, and the pages you've opened kept for when the Wi-Fi drops.</p>" +
          '<p class="hb-how">' + how + "</p>" +
          '<p class="hb-how"><i>En tu pantalla de inicio: el mismo sitio, sin internet si hace falta.</i></p>' +
          '<button type="button" id="hbSheetClose">Got it</button>' +
        "</div>";
      sheet.hidden = false;
      document.getElementById("hbSheetClose").addEventListener("click", function () { sheet.hidden = true; });
    });
  }

  /* a newer build of the hub is waiting: one line, one tap */
  function wireUpdate() {
    document.addEventListener("elhub:update", function () {
      if (document.getElementById("hbToast")) return;
      var t = document.createElement("div");
      t.className = "hb-toast"; t.id = "hbToast"; t.setAttribute("role", "status");
      t.innerHTML = "<span>A newer version of the hub is ready.</span><button type=\"button\">Refresh</button>";
      t.querySelector("button").addEventListener("click", function () {
        try {
          navigator.serviceWorker.getRegistration().then(function (reg) {
            if (reg && reg.waiting) reg.waiting.postMessage({ type: "SKIP_WAITING" });
            setTimeout(function () { location.reload(); }, 250);
          });
        } catch (e) { location.reload(); }
      });
      document.body.appendChild(t);
    });
  }

  function wire() {
    wireSend();
    wireInstall();
    wireUpdate();
    var back = document.getElementById("hbBack");
    if (back) back.addEventListener("click", function () { history.back(); });
    var btn = document.getElementById("hbTheme");
    if (!btn) return;
    label(btn);
    btn.addEventListener("click", function () {
      var next = current() === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      try { localStorage.setItem(KEY, next); } catch (e) {}
      label(btn);
    });
    /* follow the system only while the reader has not chosen for themselves */
    try {
      var mq = window.matchMedia("(prefers-color-scheme: dark)");
      var onChange = function (e) {
        var saved = null;
        try { saved = localStorage.getItem(KEY); } catch (err) {}
        if (saved) return;
        document.documentElement.setAttribute("data-theme", e.matches ? "dark" : "light");
        label(btn);
      };
      if (mq.addEventListener) mq.addEventListener("change", onChange);
      else if (mq.addListener) mq.addListener(onChange);
    } catch (e) {}
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", place);
  } else {
    place();
  }
})();
