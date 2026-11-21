#!/usr/bin/env python3
"""Build el-lesson-planner.html — the EL Lesson Planner.

    python3 tools/make-planner.py

The planner is one self-contained page. Its parts live in tools/planner/ so
each can be edited on its own; this script joins them and adds the hub's head
(theme, share card, canonical) and the hub's top bar.

  head.html   the page shell and all the styles
  bank.js     454 Mississippi standards (codes exact, wording shortened)
  texts.js    40 daily informational texts at three levels, and the Daily Text step
  es.js       Spanish for the sentence frames and the daily texts
  ideas.js    lesson ideas matched to each standard
  dyn.js      questions, exit tickets, choice board, class tools, teach mode, tabs
  sites.js    outside text builders (Diffit and others)
  ex.js       example texts for ELA standards
  easy.js     help screen, glossary, toast
  steps.js    the fifteen steps, the complete plan, printing
  simple.js   steps 1 to 3: the plain-language quick plan
  app.js      state, the plan itself, rendering

Nothing in the page calls an AI, and nothing a teacher taps leaves the browser.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "planner"
ORDER = ["bank.js", "texts.js", "es.js", "ideas.js", "dyn.js", "sites.js", "ex.js",
         "easy.js", "steps.js", "simple.js", "app.js"]

URL = "https://radan55.github.io/everyteacher/el-lesson-planner.html"
TITLE = "EL Lesson Planner · know what to do for your English learners in one minute · EL Publishing"
DESC = ("For the teacher who teaches biology, algebra or history and has English learners on the roster. "
        "Pick a Mississippi standard, tap in your students by what you see and hear, and get five things to do, "
        "each with the reason it helps. Then add extras one step at a time: lesson ideas, a daily leveled text in "
        "English and Spanish, questions, an exit ticket, a choice board, supports, and a teach mode with a timer. "
        "Print one complete plan. No typing, no account, no AI, and nothing leaves the browser.")

THEME = ('<script>/* set the theme before first paint, so nothing flashes white */try{var _t=localStorage.getItem("elhub.theme");'
         'document.documentElement.setAttribute("data-theme",_t||(matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light"))}catch(e){}</script>\n')


def swap(text, old, new):
    if text.count(old) != 1:
        raise SystemExit(f"make-planner: expected exactly one {old[:50]!r}, found {text.count(old)}")
    return text.replace(old, new)


def main():
    head = (SRC / "head.html").read_text(encoding="utf-8")
    head = swap(head, "<head>\n", "<head>\n" + THEME)
    head = swap(head, "<title>EL Lesson Planner</title>",
                f"<title>{TITLE}</title>\n"
                f'<meta name="description" content="{DESC}">\n'
                '<meta property="og:type" content="website">\n'
                '<meta property="og:site_name" content="EL Publishing">\n'
                f'<meta property="og:url" content="{URL}">\n'
                f'<meta property="og:title" content="{TITLE}">\n'
                f'<meta property="og:description" content="{DESC}">\n'
                '<meta property="og:image" content="https://radan55.github.io/everyteacher/share/el-lesson-planner.png">\n'
                '<meta property="og:image:width" content="1200">\n'
                '<meta property="og:image:height" content="630">\n'
                '<meta name="twitter:card" content="summary_large_image">\n'
                '<link rel="stylesheet" href="theme.css">\n'
                '<link rel="manifest" href="manifest.webmanifest">\n'
                f'<link rel="canonical" href="{URL}">')
    head = swap(head, '<span class="wm">EL <i>Publishing</i></span>',
                '<a class="wm" href="index.html">EL <i>Publishing</i></a>')
    body = "".join((SRC / f).read_text(encoding="utf-8") for f in ORDER)
    page = (head + body + "</script>\n"
            '<script src="guide.js" defer></script>\n<script src="hub-chrome.js" defer></script>\n'
            "</body>\n</html>\n")
    (ROOT / "el-lesson-planner.html").write_text(page, encoding="utf-8")
    print(f"el-lesson-planner.html · {len(page):,} bytes")


if __name__ == "__main__":
    main()
