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
   ["cognate-hunt.html", "https://radan55.github.io/mselablueprintinfo01/", "sentence-frames.html"]),
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
   ["cognate-hunt.html", "el-bridge.html", "sentence-frames.html"]),
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


# ------------------------------------------------------------------ outside
# Free resources from elsewhere, by subject. Every URL here was opened and read
# on 2026-10-10 before it was written down; nothing is listed from memory.
# `bands` says where it fits. `note` is the honest catch, if there is one —
# "free account to download", say — and is shown, not hidden.
#
#   (url, name, organization, bands, one line, note)
OUTSIDE = {
 "ela": [
  ("https://www.colorincolorado.org/teaching-ells/ell-strategies-best-practices",
   "ELL Strategies & Best Practices", "Colorín Colorado", "k2 g35 g68 g912",
   "Articles and classroom videos on language objectives, background knowledge and checking understanding.", ""),
  ("https://readingrockets.org/strategies",
   "Classroom Strategy Library", "Reading Rockets", "k2 g35 g68",
   "Named reading and writing strategies, each with the steps and a printable.", ""),
  ("https://pz.harvard.edu/thinking-routines",
   "Thinking Routines", "Project Zero, Harvard", "k2 g35 g68 g912",
   "Short discussion routines — See-Think-Wonder and dozens more — with printable handouts, several in Spanish.", ""),
  ("https://wida.wisc.edu/teach/can-do/descriptors",
   "Can Do Descriptors", "WIDA", "k2 g35 g68 g912",
   "What a student at each level can do when they recount, explain, argue and discuss — by grade band.", ""),
  ("https://www.serpinstitute.org/wordgen-weekly/sample",
   "WordGen Weekly", "SERP Institute", "g68",
   "A week of five short academic-vocabulary activities, teacher edition and word cards as PDFs.", ""),
  ("https://achievethecore.org/category/411/ela-literacy-lessons",
   "ELA / Literacy Lessons", "Achieve the Core", "k2 g35 g68 g912",
   "Downloadable lessons, text sets and mini-assessments with the files attached.", ""),
 ],
 "math": [
  ("https://ul.stanford.edu/sites/default/files/resource/2021-11/Principles%20for%20the%20Design%20of%20Mathematics%20Curricula_1.pdf",
   "Mathematical Language Routines", "Understanding Language, Stanford", "g35 g68 g912",
   "The eight routines — Three Reads, Stronger and Clearer, Collect and Display — with numbered steps. PDF.", ""),
  ("https://www.erikson.edu/early-math-collaborative/idea/exploring-3-reads-math-protocol-word-problems/",
   "Three Reads for Word Problems", "Erikson Early Math Collaborative", "k2 g35",
   "The word-problem routine walked through with early-grade classroom examples.", ""),
  ("https://steinhardt.nyu.edu/metrocenter/resources/glossaries",
   "Bilingual Math Glossaries", "NYU Steinhardt", "g35 g68 g912",
   "Printable English-to-home-language math term lists, elementary through Algebra 2, in dozens of languages.", ""),
  ("https://www.youcubed.org/tasks/",
   "Tasks", "YouCubed, Stanford", "k2 g35 g68 g912",
   "Visual low-floor, high-ceiling tasks filterable by grade, each with a student handout.", ""),
  ("https://www.openmiddle.com/",
   "Open Middle", "Open Middle", "k2 g35 g68 g912",
   "Problems with one answer and many ways in, by grade and course, also in Spanish.", ""),
  ("https://insidemathematics.org/classroom-videos/number-talks",
   "Number Talks on video", "Inside Mathematics", "k2 g35 g68",
   "Seven full classroom number talks, grades 1–7, one taught in Spanish.", ""),
  ("https://www.colorincolorado.org/teaching-ells/content-instruction-ells/math-instruction-ells",
   "Math Instruction for ELLs", "Colorín Colorado", "k2 g35 g68 g912",
   "Articles, videos and booklists on the language of math problems.", ""),
 ],
 "sci": [
  ("https://stemteachingtools.org/brief/27",
   "Engaging English Learners in the Science Practices", "STEM Teaching Tools, U. of Washington", "k2 g35 g68 g912",
   "A two-page brief of concrete moves — sentence stems, pictorial input charts, bilingual journals. Also in Spanish.", ""),
  ("https://stemteachingtools.org/brief/48",
   "Guiding Classroom Science Talk", "STEM Teaching Tools, U. of Washington", "k2 g35 g68 g912",
   "How to run science conversations, with talk cards and partner-talk supports.", ""),
  ("https://phet.colorado.edu/en/simulations/browse",
   "Interactive Simulations", "PhET, U. of Colorado", "g35 g68 g912",
   "Physics, chemistry, biology and earth science simulations that run in a browser, each in Spanish and many languages.", ""),
  ("https://thewonderofscience.com/phenomenal",
   "NGSS Phenomena", "The Wonder of Science", "k2 g35 g68 g912",
   "Short phenomenon videos and images sorted by standard — meaning before vocabulary.", ""),
  ("https://steinhardt.nyu.edu/metrocenter/resources/glossaries",
   "Bilingual Science Glossaries", "NYU Steinhardt", "g35 g68 g912",
   "Printable term lists for elementary, middle, Earth Science, Biology, Chemistry and Physics, in dozens of languages.", ""),
  ("https://www.nextgenscience.org/sites/default/files/%284%29%20Case%20Study%20ELL%206-14-13.pdf",
   "English Language Learners and the NGSS", "NGSS Appendix D, Case Study 4", "k2 g35 g68 g912",
   "A classroom vignette and five strategy sets: literacy, language, discourse, home language, home culture. PDF.", ""),
  ("https://www.colorincolorado.org/teaching-ells/content-instruction-ells/science-instruction-ells",
   "Science Instruction for ELLs", "Colorín Colorado", "k2 g35 g68 g912",
   "Articles and videos on labs, vocabulary and science writing with ELs.", ""),
 ],
 "soc": [
  ("https://www.loc.gov/programs/teachers/getting-started-with-primary-sources/guides/",
   "Primary Source Analysis Tool", "Library of Congress", "g35 g68 g912",
   "The Observe–Reflect–Question tool plus guides for photos, maps, cartoons, newspapers and oral histories.", ""),
  ("https://www.loc.gov/programs/teachers/classroom-materials/primary-source-sets/",
   "Primary Source Sets", "Library of Congress", "g35 g68 g912",
   "Topic sets — Civil Rights, immigration, the Dust Bowl — of images, maps and papers with a teacher guide.", ""),
  ("https://www.archives.gov/education/lessons/worksheets",
   "Document Analysis Worksheets", "National Archives", "k2 g35 g68 g912",
   "Two tiers of analysis sheets for every document type; the novice tier is written for English learners, with Spanish versions.", ""),
  ("https://vision.icivics.org/how-to-use/spanish-el-ml",
   "Spanish & EL/ML Supports", "iCivics", "g35 g68 g912",
   "Civics games playable in Spanish, bilingual glossaries and Constitution videos.",
   "free account for some downloads"),
  ("https://steinhardt.nyu.edu/metrocenter/resources/glossaries",
   "Bilingual Social Studies Glossaries", "NYU Steinhardt", "g35 g68",
   "Printable elementary and middle-school term lists in dozens of languages, for word walls and testing.", ""),
  ("https://inquirygroup.org/history-lessons",
   "Reading Like a Historian", "Digital Inquiry Group", "g68 g912",
   "Document-based U.S. and world history lessons with sourcing routines; many with Spanish student materials.",
   "free account to download"),
  ("https://www.colorincolorado.org/teaching-ells/content-instruction-ells/social-studies-instruction-ells",
   "Social Studies Instruction for ELLs", "Colorín Colorado", "k2 g35 g68 g912",
   "Lesson-planning tips, a primary-sources article and classroom videos.", ""),
 ],
}
