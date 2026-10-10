#!/usr/bin/env python3
"""For districts — the ways a district can start a conversation.

One source for both places it appears: the full version at the foot of
leaders.html, where district leaders actually are, and a compact version on the
home page. Change it here and run tools/build.py.

Written as what a district needs, not as what I am looking for. Nothing here
says available, seeking, opportunities or hire, and nothing should.

  head   the card's heading
  body   two or three sentences
  links  (label, href) — relative on this hub wherever possible
"""

LEAD = ("Everything on this hub is free and stays free. But some of what a district "
        "needs is not a file — it is time, a second set of eyes, or a decision about "
        "who does this work next year. If that is where you are, write to me directly.")

NOTE = ("<b>In confidence.</b> Write to my personal address. What you send stays "
        "between us — no list, no follow-up sequence, and no one else on the thread.")

MAIL = ("mailto:richard.spanishteacher@gmail.com"
        "?subject=A%20conversation%20about%20EL%20program%20work")

D = [
 ("Build something that doesn't exist yet",
  "A resource your teachers need, written for your grade bands, your levels and your "
  "devices — and published so it keeps working long after the project is finished.",
  [("District Partnership Kit", "district-kit.html")]),

 ("Professional learning",
  "A faculty session, a department meeting, or a self-paced module your staff runs "
  "without me in the room. Sheltered puts a whole faculty through twelve minutes as "
  "an English learner, and it changes the conversation that follows.",
  [("Sheltered", "sheltered.html"),
   ("The PD module", "https://radan55.github.io/everyteacherisalanguageteacher/")]),

 ("A second set of eyes",
  "The self-audit and the six-session evaluation course are free, and most districts "
  "can run them without help. If you would rather think it through with someone who "
  "has read the same regulations, ask.",
  [("EL Program Self-Audit", "el-audit.html"),
   ("Evaluate your own program", "el-evaluate.html")]),

 ("The longer conversation",
  "Some districts are not looking for a resource at all. They are building or "
  "rebuilding an EL program and working out the shape of the role that ought to run "
  "it. I am glad to think that through with you, in confidence, wherever it leads.",
  [("Write to me", MAIL)]),
]
