/* EL Publishing — the top bar and the light/dark control.
   Styles live in theme.css, which is linked in the head so the colours are
   right before first paint. This file only builds the bar and wires it up.

   The theme is already applied by a small snippet in each page's head; this
   script just keeps the control in sync and remembers the choice. */
(function () {
  "use strict";
  if (window.__elHubBar) return;
  window.__elHubBar = true;

  /* Some pages take the whole screen on purpose — a simulation, a practice
     session. A bar across the top of those is in the way, so they opt out
     with data-no-hubbar on <html> and keep only the theme. */
  if (document.documentElement.hasAttribute("data-no-hubbar")) return;

  var KEY = "elhub.theme";
  var HOME = "index.html";

  var LINKS = [
    ["Start here", "index.html#start"],
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

  bar.innerHTML =
    '<div class="hubbar-in">' +
      '<a class="hb-home" href="' + HOME + '" aria-label="EL Publishing, home">' +
        MARK + "<b>EL Publishing</b></a>" +
      '<nav aria-label="Hub">' + nav + "</nav>" +
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
            "&body=" + encodeURIComponent(msg + "\n\n" + url) + '">Email it</a>' +
          '<a href="sms:?&body=' + encodeURIComponent(msg + " " + url) + '">Text it</a>' +
          '<button type="button" id="hbCopy">Copy the link</button>' +
        "</div>";
      sheet.hidden = false;
      btn.setAttribute("aria-expanded", "true");
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
      /* a phone has a better share sheet than anything built here */
      if (navigator.share) {
        navigator.share({ title: document.title, text: msg, url: url }).catch(function () {});
        return;
      }
      sheet.hidden ? open() : close();
    });
    document.addEventListener("click", function (ev) {
      if (!sheet.hidden && !sheet.contains(ev.target) && !btn.contains(ev.target)) close();
    });
    document.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape" && !sheet.hidden) { close(); btn.focus(); }
    });
  }

  function wire() {
    wireSend();
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
