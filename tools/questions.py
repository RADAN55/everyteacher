#!/usr/bin/env python3
"""The questions people actually ask, and the answers.

Ported from the personal site and retargeted at this hub: every link that can
point at a resource here points at a relative path, so the answers stay correct
when the catalog moves. Add one here and run tools/build.py.

  who    teachers | coordinators | students | families
  q      the question, in the words someone would type it
  a      the answer. Say the thing, then say where to go — not the reverse.
  links  (label, href) pairs. Keep it to two.
"""

WHO = [
    ("teachers", "Teachers"),
    ("coordinators", "Coordinators & admin"),
    ("students", "Students"),
    ("families", "Families · Familias"),
]

Q = [
 ("teachers",
  "I have an English learner in my class and I don't teach English. Where do I start?",
  "Post a language goal next to your content objective, give one sentence frame, and "
  "let the student talk before writing. Those three moves cost about two minutes a "
  "lesson and change what the student can produce. If you only do one thing this week, "
  "sit the twelve-minute simulation first — it is faster than being told.",
  [("Sheltered: 12 minutes as an EL", "sheltered.html"),
   ("The EL Field Guide", "https://radan55.github.io/el-field-guide/")]),

 ("teachers",
  "What do ELPA21 levels 1–5 actually mean for my classroom?",
  "Levels 1–2 need visuals, frames and the home language as a bridge. Levels 3–4 can "
  "handle grade-level text once the vocabulary is pre-taught. A student at Level 4 in "
  "all four domains exits the program. The Can-Do checklist is the plainest version of "
  "this — eighty statements a student scores themselves.",
  [("My English Can-Do Checklist", "can-do-checklist.html"),
   ("The ELPT, explained", "elpt-family-guide.html")]),

 ("teachers",
  "Can I grade an English learner the same way as everyone else?",
  "Grade the content, and grade it against the accommodations written in the student's "
  "Language Service Plan. Read-aloud, extra time, a word-to-word glossary — if it is on "
  "the plan it is not optional. Give language feedback separately, on one pattern at a "
  "time, so the grade still tells the truth about your subject.",
  [("EL Accommodations Quick Cards", "accommodations-cards.html"),
   ("LSP Builder", "lsp-builder.html")]),

 ("teachers",
  "Where can I get a 45-minute PD on English learners for my department?",
  "Two that need no facilitator. \"Every Teacher Is a Language Teacher\" is a self-paced "
  "module with sections for general-education, special-education and administrative "
  "staff. Sheltered runs a whole faculty through twelve minutes as an EL and lands "
  "harder — budget twenty-five minutes for the room.",
  [("Every Teacher Is a Language Teacher",
    "https://radan55.github.io/everyteacherisalanguageteacher/"),
   ("Sheltered", "sheltered.html")]),

 ("teachers",
  "I need tomorrow's lesson scaffolded and I have one planning period.",
  "Paste what you already teach into the EL Assistants and get it back in four lanes, "
  "or give EL Bridge a Mississippi standard and let it build the lesson, a leveled text "
  "or MAAP-style items. Both run on whichever AI you already have, and neither asks for "
  "a student name.",
  [("EL Assistants", "el-assistants.html"), ("EL Bridge Mississippi", "el-bridge.html")]),

 ("teachers",
  "Which tech tools are worth my time right now?",
  "Six verified this month, all free and Chromebook-ready, with a classroom use named "
  "for each lane and a watch list for what is not ready. One more is added every "
  "Tuesday, so it is worth a look at the start of a unit rather than once a year.",
  [("EL Tech Radar", "tech-radar.html")]),

 ("teachers",
  "What's actually new in EL teaching this year — and what's just a trend?",
  "Eight ideas shaping the year, each tagged by how strong the evidence behind it is, "
  "with the sources attached: Science of Reading \"yes AND,\" what does and does not "
  "transfer across languages, Key Language Uses, time-boxed newcomer programs, "
  "co-teaching, teacher-in-the-loop AI, and Mississippi's four-domain exit rule.",
  [("Field Notes", "field-notes.html")]),

 ("coordinators",
  "What has to be in a student's folder to survive an MDE monitoring visit?",
  "Home Language Survey, the screener and every annual ELPT score, a current Language "
  "Service Plan with measurable goals in all four domains, parent notification letters "
  "in a language the family reads, and four years of monitoring after exit. The "
  "self-audit walks all thirty-three items and prints what is missing.",
  [("EL Program Self-Audit", "el-audit.html"),
   ("EL Program Compliance Calendar", "el-compliance-calendar.html")]),

 ("coordinators",
  "How does EL progress count in the Mississippi accountability model?",
  "The §15 EL Progress component is worth 5 percent of the model and is computed from "
  "the ELPT overall scale score against a five-year trajectory to proficiency. A "
  "student can gain a level and still miss their target, which is why growth has to be "
  "read against years in program rather than against last year alone.",
  [("EL Outcomes Dashboard", "el-outcomes.html"),
   ("Evaluate Your Own EL Program", "el-evaluate.html")]),

 ("coordinators",
  "How do I know whether our EL program is actually working?",
  "Ask it as six questions, in order, and answer each one from your own data: who is in "
  "the program, are they learning English, are they getting the same education as "
  "everyone else, and what is causing the gap. That is the method a consulting firm "
  "sells. It is written out here so your own team can run it.",
  [("Evaluate Your Own EL Program", "el-evaluate.html"),
   ("For district leaders", "leaders.html")]),

 ("coordinators",
  "Is there a ready-made year plan for a combined Emerging + Progressing block?",
  "One theme calendar, two language lanes: eight units mapped week by week with grammar "
  "ladders, ELP and MS CCRS codes, writing products, ELPA21 mirror tasks, a 90-minute "
  "block template and an assessment calendar built back from the ELPT window.",
  [("36-Week EL Curriculum",
    "https://radan55.github.io/RichardDaniel/curriculum-36/"),
   ("36-Week Language Functions",
    "https://radan55.github.io/RichardDaniel/language-functions/")]),

 ("students",
  "How can I practice for the English test on my own?",
  "English On Your Own is built to the real ELPA21 blueprint for grades 9–12 — all "
  "twenty-two task types plus a sixty-item practice form that gives you a level for "
  "each skill. It records your speaking and checks what you actually said. Directions "
  "come in six languages. No account, no teacher needed.",
  [("English On Your Own", "english-on-your-own.html"),
   ("ELPA21 Reading Studio", "https://radan55.github.io/elpa21-reading-studio/")]),

 ("students",
  "I just arrived. What do I need to know about school here?",
  "Start with the guide — how school works, enrolling, a school day, grades and "
  "graduation, your rights, and a sixty-word glossary, with English beside Spanish, "
  "Vietnamese, Arabic, Chinese or Haitian Creole. Then point your Chromebook camera at "
  "the room and learn the words that are already around you.",
  [("Your Guide to School in the U.S.", "newcomer-guide.html"),
   ("Storm Lens", "storm-lens/")]),

 ("students",
  "Is there something to read that was written for students like me?",
  "Many Voices is a magazine for multilingual high-school students. The Mississippi EL "
  "Library has 187 leveled readables across five volumes. And Sentence Lab puts sixteen "
  "grammar features in real school scenes, with a Newcomer lane and a Progressing lane "
  "on every page.",
  [("Many Voices", "https://radan55.github.io/elstudentmagazine01/"),
   ("Sentence Lab", "sentence-lab.html")]),

 ("families",
  "¿Mi hijo tiene que salir de sus clases regulares para recibir apoyo de inglés? / "
  "Does my child have to leave regular classes for English support?",
  "No. Los servicios de inglés se suman a las clases regulares; nunca reemplazan "
  "matemáticas, ciencias ni historia. Usted puede pedir el plan de servicios de su hijo "
  "en cualquier momento. — No. English services are added to regular classes; they never "
  "replace math, science or history. You may ask for your child's service plan at any "
  "time.",
  [("El examen de inglés, explicado", "elpt-family-guide.html"),
   ("Guía de la escuela en EE. UU.", "newcomer-guide.html")]),

 ("families",
  "¿Cómo puedo ayudar en casa si no hablo inglés? / "
  "How can I help at home if I don't speak English?",
  "Lea con su hijo en español, hable de la escuela en español y pídale que le explique "
  "lo que aprendió. Un español fuerte acelera el inglés. — Read with your child in your "
  "language, talk about school in your language, and ask them to explain what they "
  "learned. A strong first language speeds English up; it does not slow it down.",
  [("Camino a la graduación", "graduation-roadmap.html"),
   ("Mis primeras 100 palabras", "first-100-words.html")]),
]
