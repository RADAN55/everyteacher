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
 ('https://radan55.github.io/stormphonicslab/', "Storm Phonics Lab", "elteacher", "Program", "187 + 120 lessons",
  "A plain guide, a coach who teaches the daily lesson, and a learn-to-read program for teens.", True),
 ('https://radan55.github.io/stormelresourcelist-/', "Bilingual Resources, K-12", "classroom", "Directory", "229 entries",
  "Find what exists in a student's home language for English, math, history and science.", True),
 ('https://radan55.github.io/Stormsentencelab/', "Storm Sentence Lab", "students", "Interactive", "40 run-ons · EN/ES",
  "Find the seam, pick the fix, stop writing run-ons — with a coach lab for the teacher.", True),
 ("elpa21-listening-2/", "ELPA21 Listening Practice · Set 2", "students", "Interactive", "51 items",
  "Seven more listening lessons: new words, scenes, talks, debates and lectures.", True),
 ("elpa21-listening/", "ELPA21 Listening Practice · Set 1", "students", "Interactive", "51 items",
  "Students hear a direction, conversation, debate, presentation or lesson, then tap the picture, card or answer that matches.", True),
 ("https://radan55.github.io/Stormattention/", "Your Attention Is for Sale", "students", "Lesson", "90 min · EN/ES",
  "A read-aloud lesson where students feel the tricks apps use on them, then take their attention back.", True),
 ("newcomer-guide.html", "Your Guide to School in the U.S.", "students", "PDF guide", "5 languages",
  "How an American school works, for a family that arrived this week.", True),
 ("first-100-words.html", "My First 100 Words at School", "students", "Interactive", "100 words",
  "The hundred words of a first month, tap to hear, printable as flashcards.", True),
 ("storm-lens/", "Storm Lens: Point. Name. Say.", "students", "Camera app", "334 words",
  "Point a Chromebook at the room and the room becomes the vocabulary list.", True),
 ("grammar-calisthenics/", "Storm Grammar Calisthenics", "students", "Daily coach", "180 routines",
  "Verb jumps, error hunts, rapid fire, dictation sprints — a bilingual coach, fifteen minutes a day.", True),
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
 ("picture-dictionary.html", "The Picture Dictionary · Issue 1", "students", "Picture dictionary", "12 spreads · 144 words",
  "Point at the thing, hear the word, say it, spell it, use it. Twelve places, drawn as spreads.", True),
 ("picture-dictionary-2.html", "The Picture Dictionary · Issue 2", "students", "Picture dictionary", "12 spreads · 144 words",
  "Food, the living room, the road, the bank, the clock, the family, the gym, the screen, the farm: twelve new spreads.", False),
 ("picture-dictionary-3.html", "The Picture Dictionary · Issue 3", "students", "Picture dictionary", "12 spreads · 144 words",
  "The lab, shapes, colors, the yard, a whole day of verbs, opposites, animals, safety, the park, the arts: twelve more spreads.", False),
 ("grammar-map.html", "The Grammar Map", "students", "Lessons + practice", "14 stations · 112 items",
  "Grammar you can see: a sentence X-ray, four lines, fourteen taught stations, a stamp at each.", True),
 ("writing-studio.html", "The Writing Studio", "students", "Lessons", "8 lessons at the board",
  "Mr. Castillo teaches the shape of a 4 or 5: claim, reasons, transitions, the email, the edit, the clock.", True),
 ("elpa-question-types-guide.html", "ELPA Question Types: Test Prep Guide", "students", "Guide", "18 question types · PDF",
  "What each question is really asking, the words that signal it, three moves, and a worked example with every choice explained.", True),
 ("write-about-it.html", "Write About It", "students", "Lessons", "5 lessons at the board",
  "Ms. Bell teaches the six-step routine on four given topics (describe, explain how, tell a time, opinion) and then any topic you bring.", True),
 ("listening-speaking-studio.html", "ELPA21 Listening & Speaking Studio", "students", "Practice", "48 items · 8 speaking tasks",
  "Hear it twice, choose, check; then record your answer and compare it with a model.", True),
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

 ("today-in-el.html", "Today in EL: the Daily Feed", "classroom", "Daily feed", "3 picks · 13 sources",
  "Updated every morning: three picks with a take and a move to try, plus thirty days of EL pedagogy and articles worth your time.", True),
 ("front-office-kit.html", "The Front Office Kit", "classroom", "Office kit", "14 languages · 20 phrases",
  "For the registrar: enroll a family that speaks no English — today, legally, kindly — with the board, the survey and the clock.", True),
 ("family-conference-kit.html", "The Family Conference Kit", "classroom", "Conference kit", "EN/ES · 15 minutes",
  "A bilingual parent conference for an EL: interpreter checklist, the script with audio, the report card explained, a take-home summary.", True),
 ("grade-it-fair.html", "Grade It Fair", "classroom", "Grading tool", "Rubric · quiz · score",
  "Paste a rubric or a quiz; get the version that grades the content, with the English handled separately, in four lanes.", True),
 ("straight-answers.html", "Straight Answers", "classroom", "FAQ", "40 questions",
  "The forty questions content teachers actually ask about ELs, answered in a hundred words, with the rule and the tool.", True),
 ("read-your-roster.html", "Read Your Roster: the ELPA21 Level Decoder", "classroom", "Decoder", "4 domains · whole class",
  "Your roster says Level 2. Here is what that student can do in your class, what is fair to grade, and what MAAP allows.", True),
 ("spanish-course/", "Spanish for Teachers: the 6-Module Course", "classroom", "Course", "6 modules · 45–60 min each",
  "Self-paced from names and greetings to the family call: audio phrases, self-checking practice, quizzes, cheat sheets, a printable workbook and a certificate.", True),
 ("spanish-for-teachers.html", "Spanish for Teachers: a 90-Minute Workshop", "classroom", "Workshop", "90 min · 72 phrases",
  "A teacher-led workshop for colleagues who speak no Spanish: names, directions, encouragement, the call home.", True),
 ("using-spanish-content-classroom.html", "Using Spanish in the Content Classroom", "classroom", "PDF guide", "40 pages",
  "Research-based moves for math, science, social studies and ELA teachers who speak no Spanish: cognates, talk-then-write, fair assessment.", True),
 ("using-spanish-handouts.html", "Teacher Handout Folder: Using Spanish", "classroom", "PDF handouts", "10 pages",
  "Ten one-page handouts from the guide: cognate lists by subject, the phrase bank, frames by level, newcomer week one, a family call script.", True),
 ("read-the-question-first.html", "Read the Question First", "classroom", "Poster", "3 steps",
  "Spot the key words, say what you need to find, read and prove it — in two languages.", True),
 ("content-teachers.html", "For Content Teachers", "classroom", "Start here", "3 questions",
  "Three questions every content teacher asks, each answered with a free tool.", True),
 ("book-study-50-strategies.html", "Fifty Strategies, One Semester", "classroom", "Book study", "8 sessions · 45 min",
  "A PLC book study of Herrell & Jordan's 50 Strategies, built for the teacher who teaches biology, not English.", True),
 ("session.html", "The Session: Emerging and Progressing", "classroom", "Video PD", "8 minutes · taught",
  "Elena, an animated presenter, teaches what to change for each level.", False),
 ("pd-library.html", "The PD Library", "classroom", "PD library", "7 videos · 61 pieces",
  "A taught session, the Six Moves videos, and 54 more pieces of PD by grade and level.", False),
 ("podcast.html", "Every Teacher: the Podcast", "classroom", "Podcast", "6 episodes",
  "Six five-minute conversations on strengthening English in a content class.", False),
 ("cognate-hunt.html", "Cognate Hunt", "classroom", "Tool", "373 pairs",
  "Paste any reading; the words your Spanish speakers already know light up.", False),
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
 ("literacy-lab/", "The Teacher Literacy Lab", "classroom", "Interactive lab", "144 sentences · 12 sessions",
  "Paste a reading or upload a PDF: vocabulary with Spanish, hard sentences, a handout.", True),
 ("monday-moves.html", "Monday Moves", "classroom", "Staff cards", "37 moves",
  "One move, every room, five minutes: a weekly language move for any content class.", True),
 ("adolescent-literacy-brochure.html", "Improving Adolescent Literacy, in Plain English", "classroom", "Brochure", "Trifold · PDF",
  "The federal reading guide's five moves, on one folded sheet any teacher can use.", False),
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
 ("el-magazine-2026-12.html", "The Language of Home · December 2026", "classroom", "Magazine", "Dec 2026 · 26 pages",
  "The December issue: the home language as a bridge, fifteen lessons, teacher keys.", True),
 ("el-magazine-2026-11.html", "The Language of Belonging · November 2026", "classroom", "Magazine", "Nov 2026 · 26 pages",
  "The November issue: belonging through contribution, 15 lessons, teacher keys.", False),
 ("https://radan55.github.io/elpa21speaking01/october/", "The Field Atlas", "classroom", "Magazine", "Oct 2026",
  "Sixteen plates for the teacher who never planned to teach language.", False),
 ("https://radan55.github.io/everyteacherisalanguageteacher/", "Every Teacher Is a Language Teacher", "classroom", "PD module", "45–60 min",
  "Self-paced PD that fits a department meeting. Six sections, no facilitator.", False),

 ("ltel-clinic.html", "The Long-Term EL Clinic", "elteacher", "Clinic", "12 weeks · tracker",
  "Six years an EL and stuck at Writing 2: a roster finder, a 30-minute diagnostic, twelve weeks on the academic register.", True),
 ("teaching-the-elpt.html", "Teaching the ELPT · Special Issue", "elteacher", "Magazine", "Winter 2026–27 · 24 pages",
  "A page-turning issue: four domain features, daily routines with a live timer, sixteen test moves, coaches who read aloud.", True),
 ("https://radan55.github.io/RichardDaniel/language-functions/", "36-Week Language Functions", "elteacher", "Scope & sequence", "36 weeks · K–12",
  "Twelve language functions across four grade bands and four proficiency tiers.", True),
 ("https://radan55.github.io/RichardDaniel/curriculum-36/", "36-Week EL Curriculum: Emerging + Progressing", "elteacher", "Curriculum map", "36 weeks · 9–12",
  "The year week by week in two lanes, built back from the ELPT window.", True),
 ("six-pies-elpa21.html", "Six Southern Pies: an ELPA21 Task Set", "elteacher", "Task set", "4 domains · 4 lanes",
  "One infographic, all four ELPA21 domains, every task in four lanes.", False),
 ("sample-lesson.html", "One Text. Four Lanes. Five Ways to Prove It.", "elteacher", "Sample lesson", "90 minutes",
  "One 90-minute block taken apart, decision by decision.", True),
 ("newcomer-week1.html", "Newcomer Week 1 Kit", "elteacher", "Kit", "5 days",
  "The week a student arrives, hour by hour, ending in an exit ticket.", True),
 ("lsp-builder.html", "LSP Builder", "elteacher", "Generator", "Mississippi LSP",
  "Drafts itself from the levels; a checklist shows what a Mississippi LSP still needs.", True),
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

 ("counselor-desk.html", "The Counselor's EL Desk", "district", "Counselor desk", "5 decisions · worksheets",
  "Foreign transcripts, placement by level, diplomas and tests, and the seventeen-year-old Level 1 — with printable worksheets.", True),
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
 ("parent-letters.html", "EL Parent Notification Letters", "district", "Templates", "6 letters · 6 languages",
  "The six letters ESSA requires, fillable, in English plus five family languages.", False),
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
NEW = {"el-magazine-2026-12.html": "2026-11-20", "today-in-el.html": "2026-11-19", "front-office-kit.html": "2026-11-18", "counselor-desk.html": "2026-11-18", "ltel-clinic.html": "2026-11-18", "family-conference-kit.html": "2026-11-18", "grade-it-fair.html": "2026-11-18", "straight-answers.html": "2026-11-18", "read-your-roster.html": "2026-11-17", 'https://radan55.github.io/stormphonicslab/': "2026-11-15", 'https://radan55.github.io/stormelresourcelist-/': "2026-11-15", 'https://radan55.github.io/Stormsentencelab/': "2026-11-15", "literacy-lab/": "2026-11-14", "adolescent-literacy-brochure.html": "2026-11-08", "monday-moves.html": "2026-11-08", "teaching-the-elpt.html": "2026-11-07", "elpa21-listening-2/": "2026-11-04", "elpa21-listening/": "2026-11-04", "el-magazine-2026-11.html": "2026-10-31", "https://radan55.github.io/Stormattention/": "2026-10-27", "spanish-course/": "2026-10-25", "spanish-for-teachers.html": "2026-10-25", "using-spanish-handouts.html": "2026-10-25", "using-spanish-content-classroom.html": "2026-10-25", "read-the-question-first.html": "2026-10-25", "elpa-question-types-guide.html": "2026-10-14", "write-about-it.html": "2026-10-14", "picture-dictionary-3.html": "2026-10-13", "book-study-50-strategies.html": "2026-10-13", "picture-dictionary-2.html": "2026-10-13", "picture-dictionary.html": "2026-10-13", "grammar-map.html": "2026-10-13", "writing-studio.html": "2026-10-12", "listening-speaking-studio.html": "2026-10-12", "grammar-calisthenics/": "2026-10-12", "six-pies-elpa21.html": "2026-10-11", "session.html": "2026-10-11", "pd-library.html": "2026-10-11", "podcast.html": "2026-10-11", "cognate-hunt.html": "2026-10-10", "by-subject.html": "2026-10-10", "sheltered.html": "2026-10-09", "el-evaluate.html": "2026-10-09"}
PIN = {"el-magazine-2026-12.html": "2026-12-25", "today-in-el.html": "2026-12-24", "front-office-kit.html": "2026-12-23", "counselor-desk.html": "2026-12-23", "ltel-clinic.html": "2026-12-23", "family-conference-kit.html": "2026-12-23", "grade-it-fair.html": "2026-12-23", "straight-answers.html": "2026-12-23", "read-your-roster.html": "2026-12-20", 'https://radan55.github.io/stormphonicslab/': "2026-12-13", 'https://radan55.github.io/stormelresourcelist-/': "2026-12-06", 'https://radan55.github.io/Stormsentencelab/': "2026-12-06", "literacy-lab/": "2026-12-05", "adolescent-literacy-brochure.html": "2026-11-22", "monday-moves.html": "2026-11-29", "teaching-the-elpt.html": "2026-12-12", "elpa21-listening-2/": "2026-11-25", "elpa21-listening/": "2026-11-25", "el-magazine-2026-11.html": "2026-12-05", "https://radan55.github.io/Stormattention/": "2026-11-17", "spanish-course/": "2026-11-29", "spanish-for-teachers.html": "2026-11-22", "using-spanish-handouts.html": "2026-11-15", "using-spanish-content-classroom.html": "2026-11-15", "read-the-question-first.html": "2026-11-08", "grammar-calisthenics/": "2026-11-02", "el-evaluate.html": "2026-11-20"}

# ------------------------------------------------------------------ series
# A series is one card on the home page that opens a landing page listing its
# members. Members stay in the catalog (search, the Hub Guide, the full index
# and sitemap all still find them) but no longer get their own card on a door.
#   id, title, group, fmt, size, one, long, [member hrefs]
SERIES = [
 ("newcomer", "The Newcomer Series", "elteacher", "Series", "3 kits + 2 for families",
  "The student arrived this week: intake, the first week hour by hour, the K–5 kit, and what goes home.",
  "Everything for the week a student arrives: Newcomer Intake (type the student once; the profile, plan and letter fill themselves), the Newcomer Week 1 Kit (the first week hour by hour, ending in an exit ticket), the Elementary Newcomer Kit for K–5, and the two things that go home — Your Guide to School in the U.S. in five languages and My First 100 Words at School. The front office's part is in the Front Office Kit.",
  ["newcomer-intake.html", "newcomer-week1.html", "newcomer-k5.html"]),
 ("elpt-teacher", "Teaching the ELPT", "elteacher", "Series", "issue + task sets",
  "The spring test from the teacher's side: the special issue, the task practice with keys, the Six Pies set.",
  "The ELPT from the EL teacher's desk: the page-turning special issue with daily routines and sixteen test moves, the teacher edition of the ELPA21 task practice (read-aloud scripts, keys, look-fors, four lanes), and Six Southern Pies, one infographic that runs every task type across all four domains.",
  ["teaching-the-elpt.html", "elpa21-practice-teacher.pdf", "six-pies-elpa21.html"]),
 ("spanish", "Spanish for Teachers", "classroom", "Series", "6 pieces",
  "For the teacher who speaks no Spanish: a 90-minute workshop, a six-module course, the research guide, handouts, phrases, cognates.",
  "Six pieces for the content teacher who speaks no Spanish: the 90-minute teacher-led workshop, the self-paced six-module course with audio, Using Spanish in the Content Classroom (the research-based guide for math, science, social studies and ELA), the Teacher Handout Folder (ten one-page handouts), Spoken Spanish & Spoken English (what you will hear and a reply for each), and Cognate Hunt (paste any reading; the words your Spanish speakers already know light up).",
  ["spanish-for-teachers.html", "spanish-course/", "using-spanish-content-classroom.html", "using-spanish-handouts.html", "spoken-spanish-english.html", "cognate-hunt.html"]),
 ("magazines", "Magazines & Bulletins", "classroom", "Series", "monthly",
  "The teacher magazine, the Field Atlas, the Language Bridge bulletin, Field Notes and the Tech Radar, in one rack.",
  "The hub's periodicals for teachers, in one rack: the EL Publishing teacher magazine (December 2026: The Language of Home; November 2026: The Language of Belonging; October 2026: The Field Atlas), The Language Bridge one-page bulletin, What's New in Teaching English Learners (Field Notes, with evidence ratings) and the monthly EL Tech Radar. For the day-by-day version, read Today in EL.",
  ["el-magazine-2026-12.html", "el-magazine-2026-11.html", "https://radan55.github.io/elpa21speaking01/october/", "language-bridge-2026-09.html", "field-notes.html", "tech-radar.html"]),
 ("pd", "The PD Library", "classroom", "Series", "60+ pieces",
  "Every piece of professional learning on the hub: the self-paced module, the taught session, the podcast, the book study, the literacy guide.",
  "Every piece of professional learning on the hub: Every Teacher Is a Language Teacher (self-paced, six sections, fits a department meeting), The Session with Elena (Emerging and Progressing, taught), the Every Teacher podcast, Fifty Strategies, One Semester (a PLC book study), Improving Adolescent Literacy in plain English, and the PD Library index of 54 more pieces by grade and level.",
  ["pd-library.html", "https://radan55.github.io/everyteacherisalanguageteacher/", "session.html", "podcast.html", "book-study-50-strategies.html", "adolescent-literacy-brochure.html"]),
 ("elpt-practice", "The ELPT Practice Center", "students", "Series", "4 domains · 7 tools",
  "Practice for every domain of the spring English test: listening sets, speaking, reading, the full form, the question-types guide.",
  "Every ELPT practice tool for students in one place, by domain: Listening Practice Sets 1 and 2, the Listening & Speaking Studio (hear it twice, record, compare), the ELPA21 Reading Studio under mock-test conditions, English On Your Own (a full form with every task type, speaking checked by the browser), the student Task Practice packet, and the ELPA Question Types guide.",
  ["elpa21-listening/", "elpa21-listening-2/", "listening-speaking-studio.html", "https://radan55.github.io/elpa21-reading-studio/", "english-on-your-own.html", "elpa21-practice-student.pdf", "elpa-question-types-guide.html"]),
 ("grammar", "Grammar & Writing", "students", "Series", "7 tools",
  "Run-ons, sentence features, the grammar map, calisthenics, grammar songs, and two writing coaches.",
  "The sentence and the paragraph, seven ways: Storm Sentence Lab (stop writing run-ons), Sentence Lab (sixteen grammar features in real school scenes), The Grammar Map (grammar you can see), Storm Grammar Calisthenics (a bilingual coach, fifteen minutes a day), Grammar Beats (grammar as radio songs), The Writing Studio (Mr. Castillo teaches the shape of a 4 or 5) and Write About It (Ms. Bell's six-step routine).",
  ["https://radan55.github.io/Stormsentencelab/", "sentence-lab.html", "grammar-map.html", "grammar-calisthenics/", "https://radan55.github.io/el-publishing-grammar-songs/", "writing-studio.html", "write-about-it.html"]),
 ("vocab", "Picture Dictionary & Vocabulary", "students", "Series", "3 issues + camera",
  "Point at the thing, hear the word: three picture-dictionary issues and Storm Lens, the camera that names the room.",
  "Vocabulary you can see and hear: The Picture Dictionary Issues 1–3 (twelve spreads each, Spanish, word and sentence audio, four activities per spread) and Storm Lens, which points a Chromebook at the room and turns it into the vocabulary list.",
  ["picture-dictionary.html", "picture-dictionary-2.html", "picture-dictionary-3.html", "storm-lens/"]),
 ("storm", "Storm Lessons & Readers", "students", "Series", "4 titles",
  "Full-period interactive lessons and readers for the 9–12 block: attention, tamales, a school day, a student magazine.",
  "Full-period interactive lessons and readers for the 9–12 EL block: Your Attention Is for Sale, How Tamales Are Made (the feature article behind the sample lesson), School Life • Language Lab (twenty-five four-skill activities inside an ordinary school day) and Many Voices, the magazine written for multilingual high-school students.",
  ["https://radan55.github.io/Stormattention/", "https://radan55.github.io/tamales02/", "https://radan55.github.io/elpa21speaking01/", "https://radan55.github.io/elstudentmagazine01/"]),
]
SERIES_HREF = {sid: f"series-{sid}.html" for sid, *_ in SERIES}

# The cards that earn a place on the home page, in the order each door shows them.
CORE = [
 # 1 · the EL teacher's desk — "your first month, in order"
 "series-newcomer.html", "student-profile.html", "lsp-builder.html",
 "https://radan55.github.io/RichardDaniel/curriculum-36/", "https://radan55.github.io/stormphonicslab/",
 "series-elpt-teacher.html", "ltel-clinic.html",
 # 2 · every classroom teacher
 "read-your-roster.html", "straight-answers.html", "monday-moves.html", "grade-it-fair.html",
 "el-bridge.html", "literacy-lab/", "series-spanish.html", "sheltered.html", "today-in-el.html",
 # 3 · students & families
 "series-elpt-practice.html", "series-grammar.html", "series-vocab.html", "series-storm.html",
 "newcomer-guide.html", "first-100-words.html", "elpt-family-guide.html", "graduation-roadmap.html",
 # 4 · district & compliance
 "leaders.html", "el-audit.html", "el-compliance-calendar.html", "parent-letters.html",
 "title3-planner.html", "policy-brief.html", "counselor-desk.html",
]
CORE_ORDER = {h: i for i, h in enumerate(CORE)}

GROUP_AUD = {g[0]: g[2] for g in GROUPS}


def load():
    """Build the catalog, carrying over the long descriptions and thumbnails.
    Series cards come first in their group; members carry "series": id."""
    import json, pathlib
    here = pathlib.Path(__file__).resolve().parent
    extra = json.loads((here / "catalog-long.json").read_text(encoding="utf-8"))
    member_of = {}
    for sid, *_, members in SERIES:
        for h in members:
            member_of[h] = sid
    out = []
    for sid, title, group, fmt, size, one, long, members in SERIES:
        href = SERIES_HREF[sid]
        e = extra.get(href, {})
        out.append({
            "href": href, "title": title, "group": group, "aud": GROUP_AUD[group],
            "fmt": fmt, "size": size, "one": one, "core": href in CORE,
            "long": long, "thumb": e.get("thumb", ""), "who": e.get("who", ""),
            "new": NEW.get(href, ""), "pin": PIN.get(href, ""), "ext": False,
            "series": "", "is_series": sid, "members": list(members),
        })
    for href, title, group, fmt, size, one, core in R:
        e = extra.get(href, {})
        out.append({
            "href": href, "title": title, "group": group, "aud": GROUP_AUD[group],
            "fmt": fmt, "size": size, "one": one, "core": href in CORE,
            "long": e.get("long", one), "thumb": e.get("thumb", ""),
            "who": e.get("who", ""),
            "new": NEW.get(href, ""), "pin": PIN.get(href, ""),
            "ext": href.startswith("http"),
            "series": member_of.get(href, ""), "is_series": "", "members": [],
        })
    hrefs = {r["href"] for r in out}
    for h in member_of:
        if h not in hrefs:
            raise SystemExit(f"catalog: series member {h} is not in the catalog")
    for h in CORE:
        if h not in hrefs:
            raise SystemExit(f"catalog: CORE entry {h} is not in the catalog")
    return out


if __name__ == "__main__":
    import json
    print(json.dumps(load(), indent=1, ensure_ascii=False))
