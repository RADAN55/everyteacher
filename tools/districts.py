#!/usr/bin/env python3
"""For districts — what a district can take and use, at no cost.

The point of this section is that the work is already built and already free.
It is not a services menu. Nothing here is sold, quoted, or scoped, and no
card should ever read like an engagement.

One source for both places it appears: the foot of leaders.html, and a shorter
version on the home page. Change it here and run tools/build.py.

  head   what the district can do
  body   two or three sentences, naming the thing and its size
  links  (label, href) — the free tool that does it
"""

HEADING = "Free for your district"

LEAD = ("Everything on this hub is free, and it stays free. No license, no account, "
        "no invoice, and no call with me first. A district can review its own "
        "program, train its own staff and send its own parent notices without "
        "paying anyone — including me. Take what you need and put your own name "
        "on it.")

NOTE = ("<b>If what your teachers need isn't here, say so.</b> Tell me and I will "
        "build it — also free, and published here so the next district gets it too. "
        "And if you are rebuilding an EL program and want to think it through out "
        "loud, write to me in confidence: what you send stays between us.")

MAIL = ("mailto:richard.spanishteacher@gmail.com"
        "?subject=A%20conversation%20about%20EL%20program%20work")

D = [
 ("Review your own program",
  "Thirty-three legal items scored in about an hour, and a six-session course that "
  "walks your team through the evaluation a consulting firm would charge for. Your "
  "people run it, on your numbers, and nothing leaves the browser.",
  [("EL Program Self-Audit", "el-audit.html"),
   ("Evaluate your own program", "el-evaluate.html")]),

 ("Train your staff without a trainer",
  "Sheltered puts a whole faculty through twelve minutes as an English learner in "
  "about twenty-five. The PD module runs 45–60 minutes in a browser. Neither needs "
  "a facilitator, a purchase order, or me in the room.",
  [("Sheltered", "sheltered.html"),
   ("The PD module", "https://radan55.github.io/everyteacherisalanguageteacher/")]),

 ("Send the paperwork that has to be right",
  "The six parent notices ESSA requires, English and Spanish side by side. Language "
  "Service Plans that draft themselves from the ELPT levels. Forty-five obligations "
  "placed in the month they actually come due.",
  [("EL Parent Notification Letters", "parent-letters.html"),
   ("EL Program Compliance Calendar", "el-compliance-calendar.html")]),

 ("Put it on your own letterhead",
  "Adapt the wording for your state, your grade bands, your district's name. Print "
  "it, copy it, hand it to your faculty, post it on your own site. You do not need "
  "permission and you do not owe me attribution.",
  [("All 57 resources", "all.html"),
   ("Start with the three questions", "leaders.html")]),
]
