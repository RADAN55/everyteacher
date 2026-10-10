#!/usr/bin/env python3
"""The catalog — the single source of truth for every resource on the hub.

Add a resource HERE and nowhere else, then run tools/build.py. That writes
the home page, the full index, the Hub Guide's list, the counts and
featured.json. Nothing about a resource is typed twice.

Fields
  href   where it lives (relative on this hub, absolute if it lives elsewhere)
  title  as it reads on its own page
  group  students | classroom | elteacher | district  (the four doors)
  fmt    what kind of thing it is, two words at most
  size   one concrete quantity — pages, items, minutes, languages
  one    ONE line, under about twelve words. This is what people read.
  long   the full paragraph. Search and the Hub Guide use it; no page shows it whole.
  thumb  screenshot in thumbs/, or "" if there isn't one
  core   True for the twenty that earn a place on the home page
  new    release date YYYY-MM-DD — hero on the home page for 21 days
  pin    YYYY-MM-DD — resource of the week until that date
"""

# id, index label, audience filter, what the group holds,
# the role it answers to on the home page, and that role's one line
GROUPS = [
    ("elteacher", "The EL teacher's desk", "teachers",
     "The year, the plans and the paperwork the EL teacher is responsible for.",
     "New EL teacher", "Your first month, in order"),
    ("classroom", "Every classroom teacher", "teachers",
     "For the teacher who teaches biology, not English. Enough to change tomorrow.",
     "Content teacher with ELs", "You teach biology, not English — this is enough"),
    ("students", "Students & families", "students",
     "Built to be handed straight to a student or sent home to a family.",
     "Family or student", "Nuevo en la escuela — empieza aquí"),
    ("district", "District & compliance", "admin",
     "For EL coordinators, Title III directors, principals and superintendents.",
     "District leader", "Superintendent, federal programs, EL coordinator"),
]

# href, title, group, fmt, size, one-liner, core
R = [
 ("newcomer-guide.html", "Your Guide to School in the U.S.", "students", "PDF guide", "5 languages",
  "How an American school works, for a family that arrived this week.", True),
 ("first-100-words.html", "My First 100 Words at School", "students", "Interactive", "100 words",
  "The hundred words of a first month, tap to hear, printable as flashcards.", True),
 ("storm-lens/", "Storm Lens: Point. Name. Say.", "students", "Camera app", "334 words",
  "Point a Chromebook at the room and the room becomes the vocabulary list.", True),
 ("english-on-your-own.html", "English On Your Own", "students", "Practice", "22 task types",
  "ELPA21 practice a student can do alone — speaking checked by the browser.", True),
 ("graduation-roadmap.html", "Graduation Roadmap for Newcomers", "students", "Planner", "4 diploma paths",
  "Credits, state tests and a four-year plan, filled in with a counselor.", True),
 ("elpt-family-guide.html", "The English Test, Explained for Families", "students", "Explainer", "5 languages",
  "What the ELPT measures, what the levels mean, how a student exits.", False),
 ("can-do-checklist.html", "My English Can-Do Checklist", "students", "Self-check", "80 statements",
  "Eighty “I can” statements a student scores three times a year.", False),
 ("sentence-lab.html", "Sentence Lab: English Grammar in Real Life", "students", "PDF packet", "25 pages",
  "Sixteen grammar features in real school scenes, two lanes on every page.", False),
 ("elpa21-practice-student.pdf", "ELPA21 Task Practice · Student", "students", "PDF packet", "16 pages",
  "Practice written in the exact format of the test, all four domains.", False),
 ("https://radan55.github.io/elpa21-reading-studio/", "ELPA21 Reading Studio", "students", "Practice", "122 items",
  "ELPT-style reading practice under mock-test conditions, six grade bands.", False),
 ("https://radan55.github.io/elpa21speaking01/", "School Life • Language Lab", "students", "Practice", "25 activities",
  "Twenty-five four-skill activities set inside an ordinary school day.", False),
 ("https://radan55.github.io/el-publishing-grammar-songs/", "Grammar Beats", "students", "Music", "3 song lessons",
  "Grammar as radio songs, each with a lesson built to the beat.", False),
 ("https://radan55.github.io/tamales02/", "How Tamales Are Made", "students", "Lesson", "1 text",
  "The feature article behind the sample lesson, with five activities.", False),
 ("https://radan55.github.io/elstudentmagazine01/", "Many Voices", "students", "Magazine", "Issue 1",
  "A magazine written for multilingual high-school students.", False),

 ("content-teachers.html", "For Content Teachers", "classroom", "Start here", "3 questions",
  "Three questions every content teacher asks, each answered with a free tool.", True),
 ("by-subject.html", "By Subject & Grade", "classroom", "Grid", "16 squares",
  "Your subject, your grade band: the language demand, two moves, what to use.", False),
 ("sheltered.html", "Sheltered: 12 Minutes as an English Learner", "classroom", "Simulation", "12 minutes",
  "Sit a real lesson in a language you don't speak. Then sit it again with supports.", True),
 ("el-assistants.html", "EL Assistants for Content Teachers", "classroom", "AI prompts", "4 assistants",
  "Four prompts to paste: scaffold a lesson, level a text, fix a quiz, write home.", True),
 ("el-bridge.html", "EL Bridge Mississippi", "classroom", "Builder", "K–12 + EOC",
  "A Mississippi standard in; a four-lane lesson, leveled text or MAAP items out.", True),
 ("https://radan55.github.io/el-field-guide/", "The EL Field Guide", "classroom", "Field guide", "Web guide",
  "The whole obligation in plain language, for staff who never trained for it.", True),
 ("sentence-frames.html", "Sentence-Frame Bank", "classroom", "Bank", "150 frames",
  "150 frames by function and level, each with a Spanish gloss. Copy into a slide.", False),
 ("spoken-spanish-english.html", "Spoken Spanish & Spoken English", "classroom", "PDF guide", "23 pages",
  "What you will hear from a Spanish speaker, and a useful reply for each.", False),
 ("accommodations-cards.html", "EL Accommodations Quick Cards", "classroom", "Quick cards", "18 cards",
  "How to do it tomorrow, whether MAAP allows it, and the wording for the LSP.", False),
 ("sub-para.html", "Substitute Card & Para Guide", "classroom", "Printable", "2 pages",
  "One page for the substitute, one for the paraprofessional. No student names.", False),
 ("coteaching-plan.html", "Co-Teaching Lesson Plan", "classroom", "Planner", "1 page",
  "Content and language objectives on one page, with six co-teaching models.", False),
 ("newcomer-k5.html", "Elementary Newcomer Kit (K–5)", "classroom", "Kit", "K–2 and 3–5",
  "The first ten days with a young newcomer, and the printables for tomorrow.", False),
 ("showcase.html", "Showcase: Built by Teachers", "classroom", "Gallery", "Open submissions",
  "What other Mississippi teachers made with these tools and chose to share.", False),
 ("tech-radar.html", "Six New Tech Tools for English Learners", "classroom", "Radar", "Updated weekly",
  "What is new and free this month, with a classroom use for each lane.", False),
 ("language-bridge-2026-09.html", "The Language Bridge", "classroom", "Bulletin", "Sept 2026",
  "The monthly one-page bulletin for content teachers: five findings, five moves.", False),
 ("https://radan55.github.io/elpa21speaking01/october/", "The Field Atlas", "classroom", "Magazine", "Oct 2026",
  "Sixteen plates for the teacher who never planned to teach language.", False),
 ("https://radan55.github.io/everyteacherisalanguageteacher/", "Every Teacher Is a Language Teacher", "classroom", "PD module", "45–60 min",
  "Self-paced PD that fits a department meeting. Six sections, no facilitator.", False),

 ("https://radan55.github.io/RichardDaniel/language-functions/", "36-Week Language Functions", "elteacher", "Scope & sequence", "36 weeks · K–12",
  "Twelve language functions across four grade bands and four proficiency tiers.", True),
 ("https://radan55.github.io/RichardDaniel/curriculum-36/", "36-Week EL Curriculum: Emerging + Progressing", "elteacher", "Curriculum map", "36 weeks · 9–12",
  "The year week by week in two lanes, built back from the ELPT window.", True),
 ("sample-lesson.html", "One Text. Four Lanes. Five Ways to Prove It.", "elteacher", "Sample lesson", "90 minutes",
  "One 90-minute block taken apart, decision by decision.", True),
 ("newcomer-week1.html", "Newcomer Week 1 Kit", "elteacher", "Kit", "5 days",
  "The week a student arrives, hour by hour, ending in an exit ticket.", True),
 ("lsp-builder.html", "LSP Builder", "elteacher", "Generator", "Mississippi LSP",
  "Enter the ELPT levels and the Language Service Plan drafts itself.", True),
 ("newcomer-intake.html", "Newcomer Intake", "elteacher", "Generator", "3 documents",
  "Type the student once; the profile, the plan and the letter fill themselves.", False),
 ("student-profile.html", "EL Student Profile", "elteacher", "Generator", "1 page",
  "The one page a substitute or a new content teacher needs about a student.", False),
 ("field-notes.html", "What's New in Teaching English Learners", "elteacher", "Research brief", "Oct 2026",
  "Eight ideas shaping the year, each tagged by how strong the evidence is.", False),
 ("elpa21-practice-teacher.pdf", "ELPA21 Task Practice · Teacher", "elteacher", "PDF packet", "Teacher edition",
  "Read-aloud scripts, keys, look-fors, and a four-lane version of every task.", False),
 ("https://radan55.github.io/mselablueprintinfo01/", "The Blueprint / El Plano", "elteacher", "Curriculum", "K–12 · EN/ES",
  "The Mississippi ELA blueprints grade by grade, in English and Spanish.", False),
 ("https://radan55.github.io/msellibrary/", "The Mississippi EL Library", "elteacher", "Library", "5 volumes",
  "Five volumes: the shelf an EL teacher in this state should have open.", False),
 ("https://radan55.github.io/elvocabularycurriculumengine/", "The Vocabulary Engine", "elteacher", "PDF", "5-day cycle",
  "A five-day instructional cycle for academic vocabulary, with handouts.", False),
 ("https://radan55.github.io/hispanicheritagemonth2026/", "Hispanic Heritage: 30 People", "elteacher", "Unit", "30 profiles",
  "Thirty bilingual biography profiles with discussion prompts and projects.", False),
 ("https://radan55.github.io/ms-el-command-center/", "MS EL Command Center", "elteacher", "Reference app", "Mississippi",
  "The reference desk: identification timelines, procedures, §15 accountability.", False),

 ("leaders.html", "For District Leaders", "district", "Start here", "3 questions",
  "Are we compliant, are they growing, what does it cost — and the tools for each.", True),
 ("el-evaluate.html", "Evaluate Your Own EL Program", "district", "Course", "6 sessions",
  "The consulting firm's method, written out so your own team can run it.", True),
 ("el-audit.html", "EL Program Self-Audit", "district", "Self-audit", "33 items · 1 hour",
  "Thirty-three legal items scored live, with a corrective-action plan.", True),
 ("el-outcomes.html", "EL Outcomes Dashboard", "district", "Dashboard", "5 charts",
  "Counts in; the annual program evaluation Castañeda asks for out.", True),
 ("el-compliance-calendar.html", "EL Program Compliance Calendar", "district", "Checklist", "45 items",
  "Forty-five obligations placed in the month they actually come due.", True),
 ("title3-planner.html", "Title III Funding Planner", "district", "Fiscal planner", "ESSA §3115",
  "The split, the 2 percent cap, the supplanting test, the FY27 contingency.", False),
 ("parent-letters.html", "EL Parent Notification Letters", "district", "Templates", "6 letters",
  "The six letters ESSA requires, fillable, English and Spanish side by side.", False),
 ("board-brief.html", "Board Brief & Deck", "district", "Template", "1 page + .pptx",
  "A dozen numbers become a one-page brief and an eight-slide deck.", False),
 ("el-data-dashboard.html", "EL Data Dashboard", "district", "Excel template", "8 tables",
  "Paste the ELPT roster; get the eight tables a board and Title III ask for.", False),
 ("policy-brief.html", "Mississippi EL Policy Brief", "district", "Monthly brief", "Oct 2026",
  "One page a month: what changed, what it means here, what to do by when.", False),
 ("case-studies.html", "EL Case Studies", "district", "Cases", "3 cases",
  "Three composite districts, with the tool and the cost named at every step.", False),
 ("district-kit.html", "District Partnership Kit", "district", "Kit", "90 days",
  "Ninety days of resource building for a district with no EL coordinator — free, a few districts a year.", False),
 ("fact-check.html", "Mississippi Fact-Check", "district", "Review record", "24 claims",
  "Every Mississippi claim on this hub, with its source and its status.", False),
 ("https://radan55.github.io/elpublishing-magazineeditionone/#compliance", "Making Them Count", "district", "Book", "Issue One",
  "Teaching English learners in Mississippi's overlooked districts.", False),
]

# release dates and pins — the only dated fields, and the only ones that expire
NEW = {"sheltered.html": "2026-10-09", "el-evaluate.html": "2026-10-09"}
PIN = {"el-evaluate.html": "2026-11-20"}

GROUP_AUD = {g[0]: g[2] for g in GROUPS}


def load():
    """Build the catalog, carrying over the long descriptions and thumbnails."""
    import json, pathlib
    here = pathlib.Path(__file__).resolve().parent
    extra = json.loads((here / "catalog-long.json").read_text(encoding="utf-8"))
    out = []
    for href, title, group, fmt, size, one, core in R:
        e = extra.get(href, {})
        out.append({
            "href": href, "title": title, "group": group, "aud": GROUP_AUD[group],
            "fmt": fmt, "size": size, "one": one, "core": core,
            "long": e.get("long", one), "thumb": e.get("thumb", ""),
            "who": e.get("who", ""),
            "new": NEW.get(href, ""), "pin": PIN.get(href, ""),
            "ext": href.startswith("http"),
        })
    return out


if __name__ == "__main__":
    import json
    print(json.dumps(load(), indent=1, ensure_ascii=False))
