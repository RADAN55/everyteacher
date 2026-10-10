#!/usr/bin/env python3
"""By subject and grade — what the language demand is, and what to reach for.

This is a routing page, not new pedagogy. Every cell names the language demand
at that point, two moves drawn from the Monday Moves series, and the hub
resources that genuinely apply. Where the hub has nothing for a cell, it says
so instead of pointing at something that nearly fits.

Each `use` entry is checked against the catalog by tools/build.py, so a cell
can never point at a resource that does not exist. Each move number is
checked against MOVE_NAMES, so a cell can never cite a move that is not in
the series or name it wrongly.

  demand  one sentence: what the language, not the content, asks of a
          student. Light inline markup (<i>) is allowed here and is
          written out as-is, so it stays prose and not a table cell.
  moves   (number, name) from the Monday Moves series — his, not invented here
  use     hrefs from the catalog that apply at this subject and band

The color is the whole point of the page, so each subject carries two: the
one used on paper-white, and a lifted version for dark mode. Nothing here is
colored for decoration — the color IS the subject.
"""

# id, label, color on white, color on dark
SUBJECTS = [
    ("ela", "English / ELA", "#1E6F8E", "#7CC5DF"),
    ("math", "Mathematics", "#7A3E9D", "#C49BE0"),
    ("sci", "Science", "#1F6F3A", "#7FCB97"),
    ("soc", "Social Studies", "#A6571C", "#E0A66B"),
]
BANDS = [("k2", "K–2"), ("g35", "3–5"), ("g68", "6–8"), ("g912", "9–12")]

NOTE = ("Electives, CTE, art, music and PE sit closest to the K–2 column whatever "
        "the grade: the doing carries the meaning, and the language rides along with "
        "it. Special education shares this grid — a disability and a language still "
        "need separating, and the Student Profile is where that gets written down.")

# (subject, band): demand, moves, use
CELLS = {
 ("ela", "k2"): (
   "Everything at once — letters, sounds, words and a story — in a language the "
   "child is still assembling.",
   [(2, "Preview Three Words"), (16, "Read Aloud, Think Aloud")],
   ["newcomer-k5.html", "first-100-words.html"]),
 ("ela", "g35"): (
   "The shift from learning to read to reading to learn, with vocabulary growing "
   "faster than anyone can teach it one word at a time.",
   [(12, "Teach the Word Parts"), (10, "Go on a Cognate Hunt")],
   ["https://radan55.github.io/mselablueprintinfo01/", "sentence-frames.html"]),
 ("ela", "g68"): (
   "Claim, evidence, explanation — and the sentence that holds all three together.",
   [(22, "From Sentence to Paragraph"), (23, "Grow the Sentence")],
   ["sentence-lab.html", "sentence-frames.html",
    "https://radan55.github.io/elpa21-reading-studio/"]),
 ("ela", "g912"): (
   "Analysis in writing, on demand, in a second language — and the exam language "
   "wrapped around it.",
   [(26, "The Language of Test Questions"), (14, "Annotate with a Purpose")],
   ["https://radan55.github.io/RichardDaniel/curriculum-36/", "sentence-lab.html",
    "elpa21-practice-student.pdf"]),

 ("math", "k2"): (
   "Number sense arrives before the English for it. Counting, comparing and "
   "position words are the language, not the math.",
   [(3, "Hand Over a Sentence Frame"), (5, "Check Without Asking “Do You Understand?”")],
   ["newcomer-k5.html", "first-100-words.html"]),
 ("math", "g35"): (
   "The word problem, not the arithmetic. A student who can divide may not know "
   "what <i>each</i> or <i>altogether</i> is asking for.",
   [(13, "Read the Question First"), (15, "Match the Organizer to the Thinking")],
   ["sentence-frames.html", "el-assistants.html"]),
 ("math", "g68"): (
   "Explaining the reasoning in words, which is a language task bolted onto a "
   "math task and graded as one.",
   [(4, "Talk Before Writing"), (19, "Structure the Partner Talk")],
   ["el-bridge.html", "coteaching-plan.html"]),
 ("math", "g912"): (
   "Algebra's own vocabulary, plus the MAAP question stems that decide whether a "
   "student who knows the content can show it.",
   [(26, "The Language of Test Questions"), (8, "Test-Ready All Year")],
   ["el-bridge.html", "accommodations-cards.html"]),

 ("sci", "k2"): (
   "Observation words. What a child can point at, they can often say before they "
   "can read it.",
   [(11, "Word Walls That Work"), (2, "Preview Three Words")],
   ["newcomer-k5.html", "first-100-words.html"]),
 ("sci", "g35"): (
   "Process language — <i>first</i>, <i>then</i>, <i>because</i>, <i>so</i> — carrying a sequence the student "
   "can already see happening.",
   [(15, "Match the Organizer to the Thinking"), (3, "Hand Over a Sentence Frame")],
   ["sentence-frames.html", "el-assistants.html"]),
 ("sci", "g68"): (
   "Cause and effect in writing, and a vocabulary load heavier than any other "
   "subject at this age.",
   [(12, "Teach the Word Parts"), (10, "Go on a Cognate Hunt")],
   ["el-bridge.html", "sentence-frames.html"]),
 ("sci", "g912"): (
   "Biology I's terminology and the claim-evidence-reasoning paragraph, both at "
   "once, both assessed.",
   [(22, "From Sentence to Paragraph"), (7, "Grade the Content, Grow the English")],
   ["el-bridge.html", "sample-lesson.html", "accommodations-cards.html"]),

 ("soc", "k2"): (
   "Community and time words — <i>yesterday</i>, <i>neighbor</i>, <i>rule</i> — that assume a shared "
   "childhood the student may not have had here.",
   [(32, "Culture as Content"), (17, "Build Background in Two Minutes")],
   ["newcomer-k5.html", "newcomer-guide.html"]),
 ("soc", "g35"): (
   "Background knowledge, not vocabulary. A reading about a prairie is hard if you "
   "have never seen one, however good your English.",
   [(17, "Build Background in Two Minutes"), (32, "Culture as Content")],
   ["el-assistants.html", "https://radan55.github.io/hispanicheritagemonth2026/"]),
 ("soc", "g68"): (
   "Dense text with long sentences and an assumed American frame of reference.",
   [(6, "Make the Text Reachable"), (14, "Annotate with a Purpose")],
   ["el-bridge.html", "sentence-frames.html"]),
 ("soc", "g912"): (
   "Argument from sources — reading several, taking a position, defending it in "
   "academic English.",
   [(20, "Teach the Conversation Moves"), (22, "From Sentence to Paragraph")],
   ["el-bridge.html", "sentence-lab.html",
    "https://radan55.github.io/RichardDaniel/curriculum-36/"]),
}

# every band, whatever the subject
ALWAYS = [
    ("Any subject, any grade", [
        ("sheltered.html", "Sit twelve minutes as an EL before changing anything"),
        ("can-do-checklist.html", "What a level actually means, in student words"),
        ("accommodations-cards.html", "What you may change, and what MAAP allows"),
        ("student-profile.html", "The one page about the student for your folder"),
    ]),
]

MOVES_HOME = "https://radan55.github.io/mselablueprintinfo01/monday-moves.html"

# The thirty-six Monday Moves, in order, as the page itself names them. Cells
# cite these by number; build.py checks the name it was given against this list
# rather than trusting what was typed into a cell.
MOVE_NAMES = [
    "Post and Say the Language Goal", "Preview Three Words",
    "Hand Over a Sentence Frame", "Talk Before Writing",
    "Check Without Asking “Do You Understand?”", "Make the Text Reachable",
    "Grade the Content, Grow the English", "Test-Ready All Year",
    "Families and Wins", "Go on a Cognate Hunt", "Word Walls That Work",
    "Teach the Word Parts", "Read the Question First",
    "Annotate with a Purpose", "Match the Organizer to the Thinking",
    "Read Aloud, Think Aloud", "Build Background in Two Minutes",
    "Look at the Work Together", "Structure the Partner Talk",
    "Teach the Conversation Moves", "Share the Air",
    "From Sentence to Paragraph", "Grow the Sentence", "Feedback That Sticks",
    "ELPA21 Season: What It Measures", "The Language of Test Questions",
    "Stamina and Calm", "Review with Games",
    "Use the Home Language as a Tool", "Technology That Helps",
    "When a Newcomer Arrives in Spring", "Culture as Content",
    "State Test Week", "Projects and Presentations", "Celebrate the Growth",
    "Hand Off and Reflect",
]

# The series is published in four parts, and those section anchors are the only
# link targets the page is known to carry. A move link lands in its own part —
# which is honest — rather than at a per-card anchor that may not exist.
PARTS = [
    (1, 9, "mq-1", "The Five Moves"),
    (10, 18, "mq-2", "Reading and Words"),
    (19, 27, "mq-3", "Talk, Writing, and Test Season"),
    (28, 36, "mq-4", "Finishing Strong"),
]


def move_url(n):
    for lo, hi, anchor, _ in PARTS:
        if lo <= n <= hi:
            return f"{MOVES_HOME}#{anchor}"
    raise ValueError(f"move {n} is outside the series")
