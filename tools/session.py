#!/usr/bin/env python3
"""The session: Emerging and Progressing — a PD session taught by Elena, the
animated presenter (the EL specialist from the podcast, given a face).

Same beat grammar as tools/videos.py, plus:
  ("slide", heading, [lines])  — same as board
  ("two", left_head, left_lines, right_head, right_lines) — same as split
Elena gestures at the board when a card changes, and looks at the viewer
when she is just talking ("say").
"""

VOICE = 1  # af_bella — Elena
TITLE = "Emerging and Progressing"
SUB = "What to do differently for each — a session for content teachers"
PRESENTER = "Elena"

BEATS = [
("title", "A PD session for content teachers", "Emerging and Progressing",
 "Hi, I'm Elena. I'm the EL specialist from the Every Teacher podcast, and this is a ten-minute session for the teacher who teaches content, not English. Biology, algebra, history, PE — if you have English learners in the room, this is for you."),
("say", "We're going to do three things. Get clear on the two words on your roster, Emerging and Progressing. See what a student at each level can actually do in your class. And then — this is the part that matters — walk through what you change for each one. Not two different lessons. One lesson, two different sizes."),

("slide", "The two words", ["ELPT: the state English test, every spring", "Four domains: listening · speaking · reading · writing", "Each scored 1 to 5", "Emerging ≈ levels 1–2", "Progressing ≈ levels 3–4", "Proficient = exits the program"],
 "First, the words. Every spring, every English learner in Mississippi takes the E L P T — the state English test. It gives a score of one to five in four domains: listening, speaking, reading and writing. A student who is mostly at levels one and two is called Emerging. Mostly three and four, Progressing. Level five across the board, and the student is proficient and exits the program."),
("say", "Here's the first thing I want you to do with that. Don't stop at the label. Ask for the four domain scores. A student who is a four in speaking and a two in writing needs something very different from you than a student who is the reverse — and both of them might be labeled Progressing. The EL teacher has the scores. The Language Service Plan has them on page one. Ask."),

("two", "An Emerging student can…", ["Follow a routine they've seen before", "Point, match, sort, copy, label", "Say a word or a memorized phrase", "Answer yes/no or either/or", "Write a sentence from a frame", "Know the content — in their language"],
        "…and can't yet", ["Follow 10 minutes of talk at normal speed", "Read a textbook paragraph", "Write a paragraph on their own", "Answer an open question out loud"],
 "Now, what can an Emerging student do? More than you'd think. They can follow a routine they've seen before. They can point, match, sort, copy and label. They can say a single word or a memorized phrase. They can answer a yes-or-no question, or a question with a choice in it. With a frame, they can write a sentence. And — this is the big one — they very often know the content already, in their own language. What they can't do yet is follow you talking at normal speed for ten minutes, read a paragraph of the textbook, write a paragraph alone, or answer an open question out loud. That's a language gap. It's temporary. It is not a learning problem."),
("two", "A Progressing student can…", ["Sound fluent in the hallway", "Read grade-level text with support", "Write a paragraph with a word bank and a structure", "Explain their thinking out loud", "Give a reason with because"],
        "…and still stalls on", ["The 30-word textbook sentence", "The word problem with the question buried", "Passive voice: energy is stored", "Writing with however, as a result, although", "Dense test language"],
 "A Progressing student is the one most teachers underestimate in the other direction. They sound fluent in the hallway. They joke, they argue, they've got the social English. They can read a grade-level text with support, write a paragraph if you give them a word bank and a structure, explain their thinking out loud, give a reason with because. Where they stall is the dense stuff: the thirty-word textbook sentence, the word problem with the question buried in the middle, the passive voice — energy is stored — the connectors like however and as a result, and the language of test questions. And because they sound fluent, nobody notices. They just look like they aren't trying."),

("slide", "The trap for each", ["Emerging: “They can't do the content.” — They can. They can't do it in English yet.", "Progressing: “They're fluent, so they're fine.” — Social English isn't academic English."],
 "So there's a trap for each one. With an Emerging student, the trap is assuming they can't do the content. They can; they can't do it in English yet. With a Progressing student, the trap is assuming that fluent means fine. Social English is not academic English, and the gap between the two is exactly what your class is for."),

("title", "Part one", "For the Emerging student",
 "Part one. What you change for the Emerging student. Five things. None of them is a different lesson."),
("slide", "For Emerging · five things", [],
 "Here they are."),
("add", "① Five words first — with a picture, said aloud, used ten times", "One. Five words first. Before the lesson, the five words it falls apart without, each with a picture, said out loud by everyone, used ten times. Not thirty words on Monday."),
("add", "② Show everything twice — say it and point, say it and draw, say it and act it out", "Two. Show everything twice. Say it and point. Say it and the diagram is on the slide. Say it and write the key word as you say it. Diffusion — walk across the room and spread your arms. Two channels for every idea."),
("add", "③ Frames with a word bank — “This is a ___ cell.”  [plant · animal]", "Three. Sentence frames with a word bank next to them. This is a blank cell — plant, animal. The frame carries the grammar; the student supplies the idea. A level one can join a discussion they'd otherwise sit out."),
("add", "④ Check by showing — point, one finger or two, sort the cards, draw it", "Four. Check by showing, not by asking. Point to the nucleus. One finger for plant, two for animal. Sort these cards. Draw it in three boxes. A student who can't say it can usually show it."),
("add", "⑤ Home language as a bridge — cognates on the wall, a bilingual glossary, a partner who shows, not translates", "Five. Use the home language as a bridge. Write the Spanish cognate next to the English word — célula, cell. Hand out a bilingual glossary for your course. And give the student a partner whose job is to show, slower, with the picture — not to translate, because if the partner translates, the newcomer never has to listen in English."),
("two", "Emerging · what output looks like", ["Labels on a diagram", "A list of four parts", "Two or three sentences from frames", "A sort, a match, a drawing", "One word said to a partner"],
        "…and what you grade", ["The content — fully", "Did they label the parts right? That's biology.", "Not the English — note it, fix one thing", "Same standard, smaller output"],
 "And what does output look like for an Emerging student? Labels on a diagram. A list of four parts. Two or three sentences from frames. A sort, a match, a drawing. One word said to a partner. That is work. It counts. And you grade the content fully — did they label the parts right? That's biology, and that's full credit. The English you note, and you fix one thing. Same standard as everyone else; smaller output."),

("title", "Part two", "For the Progressing student",
 "Part two. The Progressing student. Also five things, and they're different, because the problem is different. This student doesn't need the door opened. They need to be pushed through the next one."),
("slide", "For Progressing · five things", [],
 "Here's the list."),
("add", "① Unpack one sentence a day — who? does what? to what? using what?", "One. Unpack one sentence a day. Pick the textbook sentence you know will stop them, before class. Who does it, does what, to what, using what. Rewrite it as three short sentences, together. You're teaching them to read science — nobody else is."),
("add", "② Frames that push — “Although ___, the evidence shows ___.”", "Two. Frames that push, not frames that rescue. Although blank, the evidence shows blank. I think blank because blank, however blank. They would not produce that on their own. With the frame, they will — and after a month, without it."),
("add", "③ Teach the tier-two words — analyze · consequence · despite · whereas · therefore", "Three. Teach the words that live in every subject and no textbook glossary: analyze, consequence, despite, whereas, therefore. Tier-two words. Your Progressing students know photosynthesis; they don't know whereas, and whereas is on the test."),
("add", "④ Talk before writing — a minute with a partner, then the paragraph", "Four. Talk before writing. Speaking is ahead of writing for almost every Progressing student. A minute with a partner saying the answer, then two minutes writing it. If they can say it, they can write it."),
("add", "⑤ Five seconds of wait time — and pick who answers", "Five. Wait time. Count to five after a question. The Progressing student spends the first second translating the question. And pick who answers — not the same four hands."),
("two", "Progressing · what output looks like", ["A paragraph, with structure", "Connectors: because · however · as a result", "An explanation of their thinking, out loud", "A claim with evidence"],
        "…and what you grade", ["The content — fully", "The language: one pattern at a time", "Push the next connector, not all of them", "Say it to them, don't just circle it"],
 "Output for a Progressing student is a paragraph with structure, connectors — because, however, as a result — an explanation out loud, a claim with evidence. Grade the content fully. Give language feedback on one pattern at a time: this week it's past tense, next week it's because. Say it to them in person. Don't just circle it."),

("title", "Part three", "One lesson, two sizes",
 "Part three, and this is the whole point. You don't teach two lessons. You teach one, and you size the output."),
("two", "Cell parts · Emerging lane", ["Five words with pictures: nucleus, membrane, cytoplasm, mitochondria, cell", "núcleo · membrana written beside", "Label the diagram with a partner", "Frame: “The ___ controls the cell.”", "Check: point to the nucleus"],
        "Cell parts · Progressing lane", ["Same five words — plus function, structure, whereas", "Unpack: “The membrane, which is selectively permeable, regulates…”", "Frame: “Unlike the ___, the ___ ___, whereas…”", "Talk one minute, then write a paragraph", "Check: explain to a partner why a plant cell needs a wall"],
 "Here's a cell-parts lesson, both lanes. Emerging lane: five words with pictures — nucleus, membrane, cytoplasm, mitochondria, cell — núcleo and membrana written beside them. Label the diagram with a partner. Frame: the blank controls the cell. Check: point to the nucleus. Progressing lane, same lesson: the same five words plus function, structure, and whereas. Unpack the sentence about the selectively permeable membrane. Frame: unlike the blank, the blank blank, whereas. Talk for a minute, then write a paragraph. Check: explain to a partner why a plant cell needs a wall. Same forty minutes. Same cell. Two sizes of English in, two sizes of English out."),
("slide", "Your ten-minute planning routine", ["Five words — which are cognates?", "One frame per lane on the board", "One check that needs no English", "Output size: Emerging = label, list, frame sentence · Progressing = paragraph, explanation", "The accommodations on the student's LSP"],
 "So here's your planning routine, ten minutes before any lesson. Five words — and which are cognates. One frame per lane on the board. One check that needs no English to answer. The size of the output for each lane. And a glance at the accommodations written in each student's Language Service Plan, because those aren't suggestions — and because somebody already wrote down what this student needs."),
("say", "One last thing. Everything I just said is one rule, sized two ways: English in and English out, every day, for every student. For an Emerging student the in is a picture and five words and the out is a label. For a Progressing student the in is an unpacked sentence and the out is a paragraph with however in it. Nobody sits for ninety minutes and produces nothing. That's the job. You already know how to teach biology. This is just teaching it in a way a learner of English can get into."),
("end", "English in. English out. Sized to the level.",
 "Thanks for ten minutes. The tools for all of this — the frame bank, the cognate hunt, the accommodations cards, the LSP builder — are free in the PD Library at radan55 dot github dot io slash everyteacher. Go pick your five words."),
]
