#!/usr/bin/env python3
"""Featured — the hand-picked few on the home page.

Not the newest (that is Now Showing) and not the pinned resource of the
week; this is the editor's shelf: one lead and three beside it, chosen
because they are the best thing on the hub for a visitor who has five
minutes. Change them whenever something better earns the spot.

Every href is checked against the catalog by tools/build.py.

  LEAD   (href, why, tag)  — the big card, with its thumbnail
  MORE   [(href, why), …]  — three beside it
"""

LEAD = ("lsp-builder.html",
        "Enter four ELPT levels and the Language Service Plan drafts itself — services, "
        "accommodations, a measurable goal for every domain — then checks its own dates "
        "and prints only what matters.",
        "Rebuilt this week")

MORE = [
    ("cognate-hunt.html",
     "Paste tomorrow's reading. The words your Spanish speakers already own light up; the false friends go red."),
    ("by-subject.html",
     "Your subject, your grade band: the language demand, two moves, what to reach for — and 27 free resources from elsewhere."),
    ("sheltered.html",
     "Twelve minutes as an English learner. Sit the lesson once in a language you don't speak, then again with supports."),
]
