#!/usr/bin/env python3
"""The PD Library — professional learning for content teachers with English
learners, every grade band and every language level.

Each item: (id, title, href, source, kind, minutes, grades, levels, shelf, why, then)
  kind    Watch · Listen · Do · Read · Print · Plan
  grades  any of k2 g35 g68 g912
  levels  e = Emerging (ELPT 1–2) · p = Progressing (3–4) · m = Proficient / monitored
  shelf   key into SHELVES
  why     one line a teacher reads before clicking
  then    the thing to do in your own classroom afterward (the PD is the doing)

Outside links are the ones already verified for by-subject.html; nothing here
is listed unseen. tools/pdlib-page.py writes pd-library.html from this file.
"""

SHELVES = [
 ("start",  "Start here",                  "Who English learners are, what the levels mean, what the law expects of a content teacher."),
 ("input",  "Make it understandable",      "Same content, more handholds: words before the lesson, cognates, chunked talk, visuals."),
 ("talk",   "Get them talking",            "Structured partner talk, frames by level, wait time, questions a level-one can answer."),
 ("read",   "Reading in the content area", "Previewing the page, unpacking a sentence, leveled texts, read-alouds that model."),
 ("write",  "Writing that happens",        "Word bank, frame, model; quick writes; feedback on one thing; what each level's writing looks like."),
 ("assess", "Assess and grade fairly",     "Accommodations versus modifications, grading the content, the Language Service Plan, state tests."),
 ("newcomer","Newcomers and families",     "The first week, the first month, and the family on the other end of the letter."),
 ("tech",   "Tools and AI",                "What is worth your planning period, and what is not."),
]

SHELF_NAME = {k: n for k, n, _ in SHELVES}
GRADES = [("k2", "K–2"), ("g35", "3–5"), ("g68", "6–8"), ("g912", "9–12")]
LEVELS = [("e", "Emerging · ELPT 1–2"), ("p", "Progressing · 3–4"), ("m", "Proficient / monitored")]
KINDS = ["Watch", "Listen", "Do", "Read", "Print", "Plan"]

ALL = "k2 g35 g68 g912"
EPM = "e p m"

ITEMS = [
 ("session", "The session · Emerging and Progressing", "pd-library.html#session", "EL Publishing · video, with Elena", "Watch", 10, ALL, "e p", "start",
  "A ten-minute PD session taught by an animated presenter: what each level can do, the five things you change for each, one lesson in two sizes.",
  "Run the ten-minute planning routine from the end of the session on tomorrow's lesson."),
 # ── the video series (players at the top of the page) ────────────────
 ("v1", "Six Moves 1 · Five Words First", "pd-library.html#v1", "EL Publishing · video", "Watch", 3, ALL, "e p", "input",
  "Pick the five words the lesson falls apart without. Say them, show them, use them ten times.",
  "Pick your five for tomorrow and write them on the board before the bell."),
 ("v2", "Six Moves 2 · Frames in Four Lanes", "pd-library.html#v2", "EL Publishing · video", "Watch", 3, ALL, EPM, "talk",
  "Post four sentence frames, one per level, and let every student join the same discussion.",
  "One question, four frames, partner talk with say-it-back."),
 ("v3", "Six Moves 3 · Unpack One Sentence", "pd-library.html#v3", "EL Publishing · video", "Watch", 3, "g35 g68 g912", "p m", "read",
  "Take the textbook sentence that will stop your level threes and take it apart on the board.",
  "Find the sentence in next week's reading. Who? Does what? To what? Using what?"),
 ("v4", "Six Moves 4 · Word Bank, Frame, Model", "pd-library.html#v4", "EL Publishing · video", "Watch", 3, ALL, EPM, "write",
  "Take the blank off the page: three things on it before anyone writes a word.",
  "Add a word bank, a frame and a model to your next prompt."),
 ("v5", "Six Moves 5 · Check Without Asking", "pd-library.html#v5", "EL Publishing · video", "Watch", 3, ALL, "e p", "input",
  "Everyone says yes to “do you understand?” Ask them to show you instead.",
  "Replace one “do you understand?” with “point to it.”"),
 ("v6", "Six Moves 6 · Grade the Content", "pd-library.html#v6", "EL Publishing · video", "Watch", 3, ALL, EPM, "assess",
  "Two rows on the rubric: grade the science fully, note the English, fix one thing.",
  "Two rows on the next thing you grade."),

 # ── start here ─────────────────────────────────────────────────────────
 ("sheltered", "Sheltered: 12 Minutes as an English Learner", "sheltered.html", "EL Publishing", "Do", 25, ALL, EPM, "start",
  "Sit a real content lesson in a language you don't speak, twice. Faster than being told.",
  "Write down the one support that changed round two. Use it tomorrow."),
 ("pod1", "Podcast 1 · Who is in your room", "podcast.html#ep1", "EL Publishing", "Listen", 6, ALL, EPM, "start",
  "Emerging, Progressing, Proficient — what each student can already do in your class, and the one daily habit.",
  "Pull the four domain scores for one of your English learners. Which domain is lowest?"),
 ("etlt", "Every Teacher Is a Language Teacher", "https://radan55.github.io/everyteacherisalanguageteacher/", "EL Publishing", "Do", 50, ALL, EPM, "start",
  "A self-paced module with tracks for general education, special education and administrators.",
  "Finish the track for your role and keep the one-page summary it produces."),
 ("fieldguide", "The EL Field Guide", "https://radan55.github.io/el-field-guide/", "EL Publishing", "Read", 20, ALL, EPM, "start",
  "The whole landscape in one web guide: levels, law, what works, what to stop doing.",
  "Mark the three pages you'll come back to."),
 ("wida", "Can Do Descriptors", "https://wida.wisc.edu/teach/can-do/descriptors", "WIDA", "Read", 15, ALL, EPM, "start",
  "What a student at each level can do when they recount, explain, argue and discuss — by grade band.",
  "Find your grade band and read the row for your lowest-level student. Plan one task they can do."),
 ("fieldnotes", "What's New in Teaching English Learners", "field-notes.html", "EL Publishing", "Read", 15, ALL, EPM, "start",
  "Eight ideas shaping the year, each tagged by how strong the evidence is, sources attached.",
  "Pick the one idea with the strongest evidence you aren't using yet."),
 ("coteach", "Co-Teaching Lesson Plan", "coteaching-plan.html", "EL Publishing", "Plan", 15, ALL, EPM, "start",
  "One page that gives the content teacher and the EL teacher each a job in the same lesson.",
  "Plan one lesson with your EL teacher on it. Teach it together."),
 ("subpara", "Substitute Card & Para Guide", "sub-para.html", "EL Publishing", "Print", 5, ALL, "e p", "start",
  "What a substitute or paraprofessional needs to know about your English learners, on two pages.",
  "Fill it in and leave it in your sub folder."),
 ("moves", "Monday Moves", "https://radan55.github.io/mselablueprintinfo01/monday-moves.html", "EL Publishing", "Read", 5, ALL, EPM, "start",
  "One EL move for every teacher, every Monday — 36 of them across the year.",
  "Try this week's move once before Friday."),

 # ── make it understandable ────────────────────────────────────────────
 ("pod2", "Podcast 2 · Make it understandable, not easier", "podcast.html#ep2", "EL Publishing", "Listen", 6, ALL, "e p", "input",
  "Five words before the lesson, cognates on the board, chunk the talk, show everything twice.",
  "Pick the five words for your next lesson. Put a picture next to each."),
 ("bysubject", "By Subject & Grade", "by-subject.html", "EL Publishing", "Plan", 10, ALL, EPM, "input",
  "Your subject, your grade band: what the language is asking, two moves that work, what to reach for.",
  "Open your square. Do one of the two moves this week."),
 ("cognate", "Cognate Hunt", "cognate-hunt.html", "EL Publishing", "Do", 5, ALL, "e p", "input",
  "Paste tomorrow's reading; the words your Spanish speakers already own light up.",
  "Paste tomorrow's reading. Write the cognates on the board before you teach."),
 ("stormlens", "Storm Lens", "storm-lens/", "EL Publishing", "Do", 10, ALL, "e", "input",
  "Point a Chromebook at the room and the room becomes the word list — try it as the teacher first.",
  "Scan your own classroom. Hand the word wall it makes to a newcomer."),
 ("vocab", "The Vocabulary Engine", "https://radan55.github.io/elvocabularycurriculumengine/", "EL Publishing", "Plan", 15, "g35 g68 g912", "e p", "input",
  "A five-day cycle for academic vocabulary that fits any subject.",
  "Run one five-day cycle on your next unit's words."),
 ("colorin", "ELL Strategies & Best Practices", "https://www.colorincolorado.org/teaching-ells/ell-strategies-best-practices", "Colorín Colorado", "Watch", 20, ALL, EPM, "input",
  "Articles and classroom videos on language objectives, background knowledge and checking understanding.",
  "Watch one classroom video. Name the move. Steal it."),
 ("stemtt", "Engaging English Learners in the Science Practices", "https://stemteachingtools.org/brief/27", "STEM Teaching Tools, U. of Washington", "Read", 10, ALL, "e p", "input",
  "A two-page brief of concrete moves — sentence stems, pictorial input charts, bilingual journals.",
  "Add one pictorial input chart to your next lab."),
 ("ngssd", "English Language Learners and the NGSS", "https://www.nextgenscience.org/sites/default/files/%284%29%20Case%20Study%20ELL%206-14-13.pdf", "NGSS Appendix D", "Read", 20, ALL, "e p", "input",
  "A classroom vignette and five strategy sets: literacy, language, discourse, home language, home culture.",
  "Choose one of the five sets and plan it into a lesson."),
 ("glossaries", "Bilingual Glossaries", "https://steinhardt.nyu.edu/metrocenter/resources/glossaries", "NYU Steinhardt", "Print", 5, "g35 g68 g912", "e p", "input",
  "Printable English-to-home-language term lists for math, science and social studies, in dozens of languages.",
  "Print the glossary for your course in your students' languages. Put it in their binders."),

 # ── get them talking ──────────────────────────────────────────────────
 ("pod3", "Podcast 3 · Get them talking", "podcast.html#ep3", "EL Publishing", "Listen", 6, ALL, EPM, "talk",
  "Frames in four lanes, the ten-minute partner-talk routine, five seconds of wait time.",
  "Count to five after your next question. Notice what happens."),
 ("frames", "Sentence-Frame Bank", "sentence-frames.html", "EL Publishing", "Print", 10, ALL, EPM, "talk",
  "150 frames by language function and level 1–5, with Spanish glosses. Pick, copy, print.",
  "Post two frames for your next discussion — one for level 1–2, one for level 3–4."),
 ("spoken", "Spoken Spanish & Spoken English", "spoken-spanish-english.html", "EL Publishing", "Read", 20, ALL, "e p", "talk",
  "Why a Spanish speaker says what they say in English — the sounds and structures that transfer and the ones that don't.",
  "Stop correcting the one pattern that is transfer, not error."),
 ("mlr", "Mathematical Language Routines", "https://ul.stanford.edu/sites/default/files/resource/2021-11/Principles%20for%20the%20Design%20of%20Mathematics%20Curricula_1.pdf", "Understanding Language, Stanford", "Read", 25, "g35 g68 g912", EPM, "talk",
  "The eight routines — Three Reads, Stronger and Clearer, Collect and Display — with numbered steps.",
  "Run Stronger and Clearer Each Time on one problem this week."),
 ("pz", "Thinking Routines", "https://pz.harvard.edu/thinking-routines", "Project Zero, Harvard", "Do", 10, ALL, EPM, "talk",
  "Short discussion routines — See-Think-Wonder and dozens more — with printable handouts, several in Spanish.",
  "Open a lesson with See-Think-Wonder on a single image."),
 ("scitalk", "Guiding Classroom Science Talk", "https://stemteachingtools.org/brief/48", "STEM Teaching Tools, U. of Washington", "Read", 10, ALL, EPM, "talk",
  "How to run science conversations, with talk cards and partner-talk supports.",
  "Print the talk cards. Use them in one lab debrief."),
 ("langfn", "36-Week Language Functions", "https://radan55.github.io/RichardDaniel/language-functions/", "EL Publishing", "Plan", 15, ALL, EPM, "talk",
  "A K–12 scope and sequence of what students should be able to do with language each week — describe, compare, explain, argue.",
  "Find this week's function. Ask one question that requires it."),

 # ── reading ───────────────────────────────────────────────────────────
 ("pod4", "Podcast 4 · Reading the textbook", "podcast.html#ep4", "EL Publishing", "Listen", 6, "g35 g68 g912", EPM, "read",
  "Preview the page, give a reading job, unpack one sentence, hand a level-one the leveled version.",
  "Pick the one sentence in next week's reading that will stop a level three. Unpack it on the board."),
 ("library", "The Mississippi EL Library", "https://radan55.github.io/msellibrary/", "EL Publishing", "Do", 15, ALL, EPM, "read",
  "187 leveled readables in five volumes — the same topic at three levels, so everyone joins the same discussion.",
  "Find a readable near your next topic. Give the three levels to three students."),
 ("sample", "One Text. Four Lanes. Five Ways to Prove It.", "sample-lesson.html", "EL Publishing", "Read", 20, "g68 g912", EPM, "read",
  "A full 90-minute lesson that keeps one text and changes the path to it for four lanes of students.",
  "Take your next text and write the four lanes for it in the margin."),
 ("rrockets", "Classroom Strategy Library", "https://readingrockets.org/strategies", "Reading Rockets", "Read", 15, "k2 g35 g68", EPM, "read",
  "Named reading and writing strategies, each with the steps and a printable.",
  "Choose one before-reading strategy and one during-reading strategy. Run both this week."),
 ("loc", "Primary Source Analysis Tool", "https://www.loc.gov/programs/teachers/getting-started-with-primary-sources/guides/", "Library of Congress", "Print", 10, "g35 g68 g912", EPM, "read",
  "Observe–Reflect–Question: a reading routine that works on a photograph before it works on a paragraph.",
  "Start your next history lesson with a photo and the three questions."),
 ("archives", "Document Analysis Worksheets", "https://www.archives.gov/education/lessons/worksheets", "National Archives", "Print", 10, ALL, "e p", "read",
  "Two tiers of analysis sheets; the novice tier is written for English learners, with Spanish versions.",
  "Give the novice sheet to your level 1–2 students and the standard sheet to everyone else, same document."),
 ("phet", "Interactive Simulations", "https://phet.colorado.edu/en/simulations/browse", "PhET, U. of Colorado", "Do", 15, "g35 g68 g912", "e p", "read",
  "Science simulations that run in a browser, each in Spanish — meaning before the reading, not after.",
  "Open the simulation before the textbook page on the same topic."),

 # ── writing ───────────────────────────────────────────────────────────
 ("pod5", "Podcast 5 · Writing that actually happens", "podcast.html#ep5", "EL Publishing", "Listen", 6, ALL, EPM, "write",
  "Take the blank off the page: word bank, frame, model. Two-minute quick writes. Feedback on one thing.",
  "Add a word bank, a frame and a model to your next writing prompt."),
 ("sentencelab", "Sentence Lab: English Grammar in Real Life", "sentence-lab.html", "EL Publishing", "Print", 15, "g68 g912", "e p", "write",
  "Sixteen grammar features in real school scenes, a Newcomer lane and a Progressing lane on every page.",
  "Hand the page that matches the one thing you're giving feedback on this week."),
 ("assistants", "EL Assistants for Content Teachers", "el-assistants.html", "EL Publishing", "Do", 15, ALL, EPM, "write",
  "Paste what you already teach and get it back in four lanes — frames, word banks and models included.",
  "Run tomorrow's writing task through the assistant. Keep the level-two version."),
 ("wordgen", "WordGen Weekly", "https://www.serpinstitute.org/wordgen-weekly/sample", "SERP Institute", "Print", 15, "g68", "p m", "write",
  "A week of five short academic-vocabulary activities ending in a written argument.",
  "Run one week of it in advisory or at the start of class."),

 # ── assess and grade ──────────────────────────────────────────────────
 ("pod6", "Podcast 6 · Grade the biology, and get help", "podcast.html#ep6", "EL Publishing", "Listen", 6, ALL, EPM, "assess",
  "Accommodation versus modification, two rows on the rubric, the LSP you're supposed to have, the five people who help.",
  "Get a copy of the Language Service Plan for each English learner you teach."),
 ("accom", "EL Accommodations Quick Cards", "accommodations-cards.html", "EL Publishing", "Print", 10, ALL, EPM, "assess",
  "Eighteen cards: the accommodation, when it applies, how it looks in class and on the state test.",
  "Match each card to a student on your roster. Tape the ones you need inside your plan book."),
 ("cando", "My English Can-Do Checklist", "can-do-checklist.html", "EL Publishing", "Do", 10, ALL, EPM, "assess",
  "Eighty 'I can' statements a student scores three times a year — the plainest picture of a level there is.",
  "Have one English learner score it. Compare their answers with the ELPT domains."),
 ("eoyo", "English On Your Own", "english-on-your-own.html", "EL Publishing", "Do", 10, "g912", "p", "assess",
  "ELPA21 practice in all twenty-two task types. Take three tasks yourself to see what the test actually asks.",
  "Do the speaking task. Then look at what your class talk does and doesn't practice."),
 ("elptguide", "The English Test, Explained for Families", "elpt-family-guide.html", "EL Publishing", "Read", 5, ALL, EPM, "assess",
  "What the ELPT measures, what the levels mean, how a student exits — written for families, useful for you.",
  "Read it once so you can answer the question a parent will ask you."),
 ("profile", "EL Student Profile", "student-profile.html", "EL Publishing", "Print", 10, ALL, EPM, "assess",
  "One page per student: levels, languages, accommodations, what works. The thing to hand the next teacher.",
  "Make one for the student you worry about most."),

 # ── newcomers and families ────────────────────────────────────────────
 ("k5kit", "Elementary Newcomer Kit (K–5)", "newcomer-k5.html", "EL Publishing", "Print", 15, "k2 g35", "e", "newcomer",
  "The first weeks for a K–2 or 3–5 newcomer: routines, survival language, what to send home.",
  "Print the first-week pages before the student arrives, not after."),
 ("week1", "Newcomer Week 1 Kit", "newcomer-week1.html", "EL Publishing", "Print", 15, "g68 g912", "e", "newcomer",
  "Five days for a secondary newcomer: the schedule, the people, the building, the first hundred words.",
  "Run day one as written. Adjust from day two."),
 ("first100", "My First 100 Words at School", "first-100-words.html", "EL Publishing", "Do", 10, ALL, "e", "newcomer",
  "The hundred words of a first month, tap to hear, printable as flashcards, five languages.",
  "Hand a newcomer the flashcards for 'In the classroom' on day one."),
 ("nguide", "Your Guide to School in the U.S.", "newcomer-guide.html", "EL Publishing", "Print", 10, ALL, "e p", "newcomer",
  "How an American school works, for a family that arrived this week — English beside five languages.",
  "Send it home in the family's language with the first parent letter."),
 ("letters", "EL Parent Notification Letters", "parent-letters.html", "EL Publishing", "Print", 10, ALL, EPM, "newcomer",
  "The six letters every program sends, in English plus five family languages. Know what your families received.",
  "Read the initial-placement letter so you know what the family was promised."),
 ("roadmap", "Graduation Roadmap for Newcomers", "graduation-roadmap.html", "EL Publishing", "Plan", 15, "g912", "e p", "newcomer",
  "Credits, state tests and a four-year plan for a student who arrived at sixteen.",
  "Sit with the counselor and fill it in for one newcomer."),
 ("heritage", "Hispanic Heritage: 30 People", "https://radan55.github.io/hispanicheritagemonth2026/", "EL Publishing", "Plan", 15, "g35 g68 g912", EPM, "newcomer",
  "Thirty profiles that put your students' world on the wall — and a leveled reading in every one.",
  "Put one profile a week on the board, whatever month it is."),
 ("icivics", "Spanish & EL/ML Supports", "https://vision.icivics.org/how-to-use/spanish-el-ml", "iCivics", "Do", 10, "g35 g68 g912", "e p", "newcomer",
  "Civics games playable in Spanish, bilingual glossaries and Constitution videos.",
  "Let a newcomer play one game in Spanish, then the same game in English."),

 # ── tools and AI ──────────────────────────────────────────────────────
 ("radar", "EL Tech Radar", "tech-radar.html", "EL Publishing", "Read", 10, ALL, EPM, "tech",
  "Six tools verified this month, free and Chromebook-ready, a use named for every lane, and a watch list.",
  "Try the one tool marked for your lane this week."),
 ("bridge", "EL Bridge Mississippi", "el-bridge.html", "EL Publishing", "Do", 15, ALL, EPM, "tech",
  "Give it a Mississippi standard; it builds the lesson, a leveled text or MAAP-style items. Runs on whatever AI you already have.",
  "Build one leveled text for next week. Read it before you use it."),
 ("openmiddle", "Open Middle", "https://www.openmiddle.com/", "Open Middle", "Do", 10, ALL, EPM, "tech",
  "Problems with one answer and many ways in, by grade and course, also in Spanish.",
  "Put one Open Middle problem on the board as the warm-up."),
 ("ntalks", "Number Talks on video", "https://insidemathematics.org/classroom-videos/number-talks", "Inside Mathematics", "Watch", 15, "k2 g35 g68", EPM, "tech",
  "Seven full classroom number talks, grades 1–7, one taught in Spanish.",
  "Watch the Spanish one. Notice how much you understood from the gestures and the board."),
]

# Curated sequences. (title, who it is for, total minutes label, [item ids])
PATHS = [
 ("Six moves in twenty minutes", "The video series, start to finish. Watch one a day for a week, or all six at a department meeting.", ["v1", "v2", "v3", "v4", "v5", "v6"]),
 ("Your first ninety minutes", "You have an English learner for the first time and no training.", ["session", "sheltered", "v1", "v2", "bysubject", "frames", "accom"]),
 ("A six-week department PLC", "One podcast episode and one tool a week; discuss with the two questions under each transcript.", ["pod1", "pod2", "pod3", "pod4", "pod5", "pod6"]),
 ("A newcomer arrives Monday", "Level one, this week.", ["k5kit", "week1", "first100", "nguide", "stormlens", "cognate", "subpara"]),
 ("Elementary, K–5", "Routines, read-alouds, frames and the family.", ["pod1", "k5kit", "rrockets", "pz", "frames", "cando", "nguide"]),
 ("Secondary, 6–12", "The textbook, the lab, the essay and the state test.", ["sheltered", "pod4", "sample", "mlr", "sentencelab", "eoyo", "roadmap"]),
 ("They sound fluent and still stall", "Progressing students, levels 3–4: academic language, not social language.", ["session", "pod1", "pod4", "pod5", "mlr", "wordgen", "frames", "eoyo"]),
 ("Exited, monitored — and slipping", "Former English learners in the four-year window.", ["pod6", "accom", "cando", "profile", "letters"]),
]
