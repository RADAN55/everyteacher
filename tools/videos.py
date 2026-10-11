#!/usr/bin/env python3
"""Six Moves — the PD video series. One classroom move per video, under
three minutes, narrated, with the move shown on a board as it is explained.

Each video is a list of BEATS. A beat is spoken narration plus what the
board shows while it is spoken:
  ("say", text)                         narration only, board unchanged
  ("title", kicker, big)                opening card
  ("board", heading, [lines])           a board that reveals its lines one per beat-line
  ("add", line)                         add a line to the current board
  ("frame", sentence_with___, fill)     a sentence frame; the blank fills on this beat
  ("split", left_head, left, right_head, right)   before / after
  ("end", line)                         closing card
Every beat carries narration as its last element.
tools/make-videos.py turns this into video/moves-N.mp4 and the posters.
"""

VOICE = 1   # af_bella — the same guide as the podcast
SERIES = "Six Moves"
TAG = "One classroom move, under three minutes, for the teacher who teaches content, not English."

VIDEOS = [
# ───────────────────────────── 1 ─────────────────────────────
{"n": 1, "title": "Five Words First", "mins": 3,
 "one": "Pick the five words the lesson falls apart without. Say them, show them, use them ten times.",
 "beats": [
 ("title", "Move one", "Five Words First",
  "Six Moves, from EL Publishing. Move one: five words first. Three minutes."),
 ("say", "Here's the problem. A newcomer sits in your biology class. You start teaching photosynthesis. By the second sentence they're lost — not because they can't do science, but because four of the words in that sentence are new, and nobody said them first."),
 ("board", "Monday's vocabulary list", ["chloroplast", "stomata", "glucose", "carbon dioxide", "oxygen", "transpiration", "autotroph", "pigment", "chlorophyll", "…and twenty-one more"],
  "The usual fix is a vocabulary list. Thirty words on Monday, a quiz on Friday. The English learner learns none of them, because thirty words with no context is noise."),
 ("board", "The five", [],
  "The move is smaller than that. Before the lesson, pick five words. Not twenty. Five. The ones that, if a student doesn't have them, the whole lesson falls apart."),
 ("add", "sunlight ☀", "For photosynthesis, that's probably sunlight."),
 ("add", "energy ⚡", "Energy."),
 ("add", "carbon dioxide", "Carbon dioxide."),
 ("add", "oxygen", "Oxygen."),
 ("add", "glucose 🍬", "And glucose."),
 ("say", "Put them on the board before you start. A picture or a symbol next to each one. Say each word. Have the whole class say it back. That's three minutes, and it's the best three minutes of the period."),
 ("split", "Spanish", ["energía", "dióxido de carbono", "oxígeno", "glucosa"], "English", ["energy", "carbon dioxide", "oxygen", "glucose"],
  "If your English learners speak Spanish, look at those five again. Four of them are cognates. Write the Spanish next to the English. You don't have to speak it. You just have to show the student that the big scary word is a word they already own."),
 ("board", "In the lesson", ["Say the word · point to it", "Use it ten times, the same way", "Students say it in a pair", "It's on the exit ticket"],
  "Then, in the lesson, use the five words on purpose. Say the word and point to it on the board. Use the same word every time — if you said carbon dioxide at the start, don't switch to C O two ten minutes later without saying those are the same. Have students say the word to a partner. Put it on the exit ticket."),
 ("say", "That's the whole move. Five words, a picture each, said out loud before the lesson, used ten times during it. Every level of English learner can get in the door of a lesson that starts this way — and so can the kid in the back who was never going to read the vocabulary list anyway."),
 ("end", "Tomorrow: pick your five.",
  "Tomorrow: pick your five. Write them on the board before the bell. That's it. Six Moves is free, with the rest of the library, at radan55 dot github dot io slash everyteacher."),
]},

# ───────────────────────────── 2 ─────────────────────────────
{"n": 2, "title": "Frames in Four Lanes", "mins": 3,
 "one": "Post four sentence frames, one per level, and let every student join the same discussion.",
 "beats": [
 ("title", "Move two", "Frames in Four Lanes",
  "Six Moves, from EL Publishing. Move two: sentence frames in four lanes."),
 ("say", "You ask the class a good question: why is this a plant cell and not an animal cell? Hands go up. The same four hands. Your English learners know the answer. They don't have the sentence to put it in."),
 ("frame", "This is a ___ cell.", "plant",
  "A sentence frame is the sentence with the content missing. This is a blank cell. The frame carries the grammar, so the student only has to supply the idea. A level-one student says: this is a plant cell. That's a correct spoken answer in academic English, from a student who arrived last month."),
 ("board", "Four lanes", [],
  "Here's the move. Don't post one frame. Post four, one per lane, and let students pick."),
 ("add", "1 · This is a ___ cell.", "Lane one, for a level one or two: one blank, and a word bank next to it."),
 ("add", "2 · It is a plant cell because it has a ___.", "Lane two: a frame with a reason built in. It is a plant cell because it has a blank."),
 ("add", "3 · I think ___ because ___.", "Lane three, for a level three: I think blank because blank. Now they're building the sentence."),
 ("add", "4 · Although ___, the evidence shows ___.", "Lane four, for a level four and for your native speakers: although blank, the evidence shows blank. They would not say that on their own. With the frame, they will."),
 ("say", "Students usually pick the right lane for themselves. When someone picks too low, you nudge: try lane three today."),
 ("board", "Running it", ["Question + four frames on the board", "30 seconds of silence to think", "Partner A talks, partner B says it back", "Switch", "You pick two or three to share"],
  "Running it takes seven or eight minutes. The question and the four frames go on the board. Thirty seconds of silence to think. Partner A talks for a minute; partner B listens and says back one thing they heard. Switch. Then you pick two or three students to share with the class — you pick, so it isn't the same four hands."),
 ("say", "The say-it-back step matters. If a level-one student says a word and their partner has to repeat it, the word was heard. It counted. Nobody got ignored."),
 ("split", "Without frames", ["Four hands", "Newcomer silent", "Level 4: one-word answers"], "With four lanes", ["Everyone speaks twice", "Newcomer: a full sentence", "Level 4: although… the evidence shows…"],
  "Without frames, you get four hands, a silent newcomer, and one-word answers from the students who could do more. With four lanes, everyone speaks academic English twice, the newcomer says a whole sentence, and your level fours are using although and the evidence shows."),
 ("end", "Tomorrow: one question, four frames.",
  "Tomorrow: one question, four frames. There are a hundred and fifty of them sorted by level in the Sentence-Frame Bank on the hub. Free, at radan55 dot github dot io slash everyteacher."),
]},

# ───────────────────────────── 3 ─────────────────────────────
{"n": 3, "title": "Unpack One Sentence", "mins": 3,
 "one": "Take the one textbook sentence that will stop your level threes and take it apart on the board.",
 "beats": [
 ("title", "Move three", "Unpack One Sentence",
  "Six Moves, from EL Publishing. Move three: unpack one sentence."),
 ("say", "Your Progressing students, the level threes and fours, are fine in discussion. Then you assign four pages of the textbook and they come back with nothing. The page didn't beat them. One sentence on it did."),
 ("board", "From the textbook", ["During photosynthesis, energy from sunlight is used by plants to convert carbon dioxide and water into glucose and oxygen."],
  "Here's a real one. During photosynthesis, energy from sunlight is used by plants to convert carbon dioxide and water into glucose and oxygen. One sentence. Five things happening. Passive voice. The subject, plants, buried in the middle."),
 ("board", "Take it apart", [],
  "The move: pick that sentence on purpose, before class, and take it apart on the board with the students. Ask the questions a reader asks."),
 ("add", "Who does it? → plants", "Who does it? Plants. Not energy — energy is used by plants. Plants do it."),
 ("add", "Does what? → convert", "Does what? Convert. Change one thing into another."),
 ("add", "Converts what → into what? → CO₂ + water → glucose + oxygen", "Converts what into what? Carbon dioxide and water, into glucose and oxygen."),
 ("add", "Using what? → energy from sunlight", "Using what? Energy from sunlight. Now every piece has a job."),
 ("board", "Rewrite it in three", ["Plants use energy from sunlight.", "They convert carbon dioxide and water.", "They make glucose and oxygen."],
  "Then rewrite it together as three short sentences. Plants use energy from sunlight. They convert carbon dioxide and water. They make glucose and oxygen. Same science. Three sentences a level two can read and a level four can now see inside of."),
 ("say", "That's three minutes of class. And you didn't just help the English learners — you taught every student in the room how to read a science sentence, which nobody else is teaching them."),
 ("board", "Make it a habit", ["One sentence a day", "Pick it before class", "Who? Does what? To what? Using what?", "Rewrite in short sentences", "Let students do the next one"],
  "Make it a habit. One sentence a day — the one you know will stop them. Pick it before class. Ask the same four questions every time: who, does what, to what, using what. Rewrite it short. After two weeks, hand the next sentence to a pair of students and let them unpack it."),
 ("end", "Tomorrow: find the sentence.",
  "Tomorrow: open next week's reading and find the sentence. Six Moves is part of the PD Library at radan55 dot github dot io slash everyteacher. Free, no login."),
]},

# ───────────────────────────── 4 ─────────────────────────────
{"n": 4, "title": "Word Bank, Frame, Model", "mins": 3,
 "one": "Take the blank off the page. Three things on it before anyone writes a word.",
 "beats": [
 ("title", "Move four", "Word Bank, Frame, Model",
  "Six Moves, from EL Publishing. Move four: word bank, frame, model."),
 ("split", "The prompt", ["Explain how a plant cell is different from an animal cell.", "", "", "", ""], "What comes back", ["", "", "(nothing)", "", ""],
  "You give a writing prompt: explain how a plant cell is different from an animal cell. Your English learners write nothing. Or two sentences. The prompt isn't the problem. The blank page under it is. No vocabulary, no structure, no example — it's the writing equivalent of saying, go talk for five minutes."),
 ("board", "Three things on the page first", [],
  "The move is three things on the page before anyone writes a word."),
 ("add", "① Word bank · cell wall · chloroplast · membrane · nucleus · both · only · unlike", "One: a word bank. The eight or ten words they'll need, right there on the page. Cell wall, chloroplast, membrane, nucleus, both, only, unlike."),
 ("add", "② Frame · Both cells have ___. Only a plant cell has ___. Unlike an animal cell, a plant cell ___.", "Two: a frame, or a structure. Both cells have blank. Only a plant cell has blank. Unlike an animal cell, a plant cell blank. That's a compare paragraph with the grammar already standing up."),
 ("add", "③ Model · a paragraph you wrote — about a different topic", "Three: a model. One paragraph that you wrote, about a different topic — say, a bike and a car — so they can see the shape without copying the content."),
 ("say", "Word bank, frame, model. With those three, a level two writes a paragraph. Without them, nobody does."),
 ("board", "What good looks like, by level", ["Level 1 · labels the diagram, copies 2 frame sentences", "Level 2 · 4–5 sentences from the frames", "Level 3 · a paragraph from the word bank + structure", "Level 4 · paragraph from the model; push connectors"],
  "And know what good looks like at each level, so you can be happy with it. A level one labels the diagram and copies two frame sentences — that's writing, it counts. A level two gives you four or five sentences from the frames. A level three writes the paragraph from the word bank and the structure. A level four writes from the model alone, and you push on connectors: however, as a result, which means."),
 ("board", "A level-two paragraph", ["Both cells have a nucleus.", "Both cells have a membrane.", "Only a plant cell has a cell wall.", "Only a plant cell has chloroplasts.", "Unlike an animal cell, a plant cell makes its own food."],
  "Here is a level-two paragraph. Both cells have a nucleus. Both cells have a membrane. Only a plant cell has a cell wall. Only a plant cell has chloroplasts. Unlike an animal cell, a plant cell makes its own food. Five sentences, correct science, correct English, from a student who wrote nothing in August. That is a win. Say so."),
 ("say", "One more thing. When you mark it, pick one thing. This week it's capital letters. Next week it's because. Fourteen red corrections teach a level two exactly one lesson: don't write."),
 ("end", "Tomorrow: three things on the page.",
  "Tomorrow: take your next prompt and put the three things on the page. The EL Assistants on the hub will draft the word bank and the frames for you. Free, at radan55 dot github dot io slash everyteacher."),
]},

# ───────────────────────────── 5 ─────────────────────────────
{"n": 5, "title": "Check Without Asking", "mins": 3,
 "one": "Everyone says yes to “do you understand?” Ask them to show you instead.",
 "beats": [
 ("title", "Move five", "Check Without Asking",
  "Six Moves, from EL Publishing. Move five: check without asking do you understand."),
 ("say", "You finish explaining. You ask, does everyone understand? Everyone nods. The newcomer nods hardest, because nodding is the one thing they can do perfectly. You move on. Nobody understood."),
 ("board", "Why “do you understand?” fails", ["Yes is the polite answer in every language", "It requires English to answer honestly", "It checks one student at a time, or none"],
  "Do you understand fails for three reasons. Yes is the polite answer in every language. Answering honestly requires English the student may not have. And it checks one student, or none — a nod from thirty people is no information at all."),
 ("board", "Check so they show you", [],
  "The move: check in a way that doesn't require English to answer, and that every student answers at once."),
 ("add", "Point to it on the diagram", "Point to the nucleus on your diagram. Thirty fingers. You can see in two seconds who has it."),
 ("add", "One finger or two", "Is this a plant cell or an animal cell? One finger for plant, two for animal. Hold them up."),
 ("add", "Sort the cards into two piles", "Sort these six cards into plant and animal. A level one can do it without a word."),
 ("add", "Draw it in three boxes", "Draw the process in three boxes. No sentences required."),
 ("add", "Finish my sentence: “The nucleus controls the…”", "Finish my sentence. The nucleus controls the — and they say, cell. That's participation. It builds up."),
 ("say", "Every one of those is answered by every student at the same moment, without a sentence of English, and you get a read on the whole room in ten seconds."),
 ("split", "Instead of…", ["Does everyone understand?", "Any questions?", "Who can tell me what the nucleus does?"], "Ask…", ["Point to the nucleus.", "Thumbs up if the nucleus controls the cell. Thumbs sideways if it stores energy.", "Does the nucleus control the cell, or store energy?"],
  "And when you do ask a question out loud, make the question carry the words. Instead of what does the nucleus do, ask: does the nucleus control the cell, or store energy? Now the student has the words. They say, control the cell. Next week you ask the open question, and they've heard themselves say it before."),
 ("board", "Then", ["Saw it: move on", "Half the room missed it: one more example, different channel", "The newcomer missed it: partner shows, not translates"],
  "Then do something with what you saw. If they have it, move on. If half the room missed it, one more example — in a different channel: a picture, a gesture, the board. If the newcomer missed it, their partner's job is to show them, not translate for them."),
 ("end", "Tomorrow: replace one “do you understand?”",
  "Tomorrow: replace one do you understand with point to it. Six Moves is in the PD Library at radan55 dot github dot io slash everyteacher."),
]},

# ───────────────────────────── 6 ─────────────────────────────
{"n": 6, "title": "Grade the Content", "mins": 3,
 "one": "Two rows on the rubric. Grade the biology fully; note the English, fix one thing.",
 "beats": [
 ("title", "Move six", "Grade the Content, Grow the English",
  "Six Moves, from EL Publishing. Move six: grade the content, grow the English."),
 ("board", "A lab conclusion", ["“The water it was boil at 100 degree. The temperature it no change when we add more heat because the energy go to make the gas.”"],
  "Here is a real kind of lab conclusion from a level-two student. The water it was boil at one hundred degree. The temperature it no change when we add more heat because the energy go to make the gas."),
 ("say", "What grade does that get? In a lot of classrooms, a sixty. Spelling, verbs, articles — it bleeds red. And the student who gets a sixty for that will quit on you by October, and then you've lost the chemistry too."),
 ("split", "The science", ["Water boils at 100 °C ✓", "Temperature stays constant during a phase change ✓", "Energy goes into making gas ✓"], "The English", ["verb forms: was boil → boiled", "it was / it no change", "articles, plural"],
  "Look again. Read it as a chemist. Water boils at one hundred degrees. The temperature stays constant during the phase change. The added energy goes into making the gas. That is a correct explanation of latent heat. Every point. The English is a level two. Those are two different things."),
 ("board", "Two rows on the rubric", [],
  "The move is two rows on the rubric — or at least two questions in your head."),
 ("add", "Row 1 · Content: did they get the science right? → grade this fully", "Row one: content. Did they get the science right? Grade that fully. This conclusion is full credit for science."),
 ("add", "Row 2 · Language: note it, feedback on ONE thing, don't let it sink the grade", "Row two: language. Note it. Give feedback on one thing. Don't let it sink the grade."),
 ("board", "Feedback on one thing", ["This week: past tense · boil → boiled, go → went", "Say it, don't just circle it", "Write the correct sentence above theirs", "Next week: a different one thing"],
  "This week the one thing is past tense. Boil, boiled. Go, went. Say it to the student in person; don't just circle it — a circle says you're wrong, the corrected sentence says here's how it goes. Write the correct sentence above theirs. Next week, a different one thing. The rest will come."),
 ("board", "Accommodation, not modification", ["Accommodation: how they show it — extra time, word bank, dictionary, read aloud, draw instead of write", "Modification: a lower standard — not for ELs unless an IEP says so"],
  "And keep the distinction straight. An accommodation changes how a student shows what they know: extra time, a word bank, a bilingual dictionary, the question read aloud, a drawing instead of a paragraph. The standard stays the same. A modification lowers the standard. English learners get accommodations, not modifications — and the ones your student gets are written in their Language Service Plan. Get a copy."),
 ("say", "A student who gets a ninety-five for the science and a note about the verbs comes back tomorrow and writes more. That's how the English grows: by writing, a lot, without fear, with one thing fixed at a time."),
 ("end", "Tomorrow: two rows.",
  "Tomorrow: two rows on the next thing you grade. That's the sixth move, and the series. All six, with the podcast and the rest of the PD Library, are free at radan55 dot github dot io slash everyteacher. Thanks for watching."),
]},
]
