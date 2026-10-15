#!/usr/bin/env python3
"""Write About It — a teacher at the board teaches EL students to write on a given topic.

Four given topics (describe, explain how, tell about a time, give an opinion), each taught start to
finish with the same six-step routine, then one lesson that works for ANY topic the student types in.
Beat grammar is the same as the Writing Studio (say / head / write / clear / pick / ask / task);
the task beat carries one extra field: the labels for the five plan boxes.
All lines are original. Nothing here quotes a test, a rubric or a book.
"""
TEACHER = "Ms. Bell"
VOICE = 1          # af_bella
TITLE = "Write About It"
SUB = "A teacher at the board teaches you to write on any topic"

FB = {
  "ok": ["Good. That line does its job.", "Yes. Keep that habit.", "That works. A reader can follow that."],
  "fix": ["Close. Look at the note under your line and fix one thing.", "Not yet. Check the note, then try again.", "Almost. One more pass."],
}

STEPS = "Read it. Brainstorm it. Plan it. Open it. Build it. Close it and check it."

def L(n, T):
    """Build one topic lesson from a topic dict."""
    id_ = f"t{n}"
    b = []
    b.append(("say", T["intro"]))
    b.append(("head", f"Lesson {n} · {T['title']}", f"Lesson {n}. {T['title']}."))
    b.append(("write", "Topic: " + T["prompt"], "Here is the topic, just as it could appear on a test. " + T["prompt"] + " Before I write one word, I read it twice."))
    b.append(("write", "① READ IT  " + T["read_board"], T["read_say"]))
    b.append(("pick", T["read_q"], T["read_opts"], T["read_ans"], T["read_why"]))
    b.append(("write", "② BRAINSTORM IT  " + T["brain_board"], T["brain_say"]))
    b.append(("pick", T["brain_q"], T["brain_opts"], T["brain_ans"], T["brain_why"]))
    b.append(("write", "③ PLAN IT  " + T["plan_board"], T["plan_say"]))
    b.append(("write", "④ OPEN IT  " + T["open"], T["open_say"]))
    b.append(("ask", T["open_ask"], T["open_prompt"], T["open_checks"] + [("starts_upper", None, "Start with a capital letter."), ("ends_punct", None, "End with a period."), ("min_words", 8, "A full sentence, at least eight words.")], T["open_model"],
              "That opening tells the reader the topic right away.", "Look at the note under your line. A good opening names the topic in the first sentence."))
    b.append(("say", "Now the middle. This is where most of the points are earned, so I build it slowly."))
    for line, say in T["body"]:
        b.append(("write", "⑤ " + line if line is T["body"][0][0] else line, say))
    b.append(("ask", T["detail_ask"], T["detail_prompt"], T["detail_checks"] + [("ends_punct", None, "End with punctuation.")], T["detail_model"],
              "Yes. A reader can picture, or follow, that sentence.", "Look at the note under your line and fix the first thing it names."))
    b.append(("write", "⑥ CLOSE IT  " + T["close"], T["close_say"]))
    b.append(("pick", T["edit_q"], T["edit_opts"], T["edit_ans"], T["edit_why"]))
    b.append(("say", "That is the routine: " + STEPS + " Six steps, in that order, every time. Now you do the whole thing, on the clock. I will give you the same topic, or you can choose another from the list."))
    b.append(("clear", "Board wiped. Your turn."))
    model = T["open_line"] + " " + " ".join(x[0] for x in T["body"]) + " " + T["close_line"]
    b.append(("task", "Your topic. " + T["prompt"] + " Read it, brainstorm, plan in the five boxes, then write. Go.", "Topic: " + T["prompt"], 15, T["rubric"], model,
              "Here is a five. " + model + " " + T["why5"], T["plan_labels"]))
    b.append(("say", T["outro"]))
    return {"id": id_, "n": n, "title": T["title"], "sub": T["sub"], "mins": 20, "goal": T["goal"], "beats": b}

# ───────────────────────── Lesson 1 · describe a place ─────────────────────────
T1 = dict(
 title="Describe a place", sub="Use your senses to show a place", goal="I can describe a place with exact details from three senses and explain why it matters.",
 intro="Welcome to the board. I'm Ms. Bell. In this lesson, we are going to write about a topic together, from the first look at the prompt to the last period. I will write first, slowly, and say what I'm thinking. Then you write your own lines, and at the end you write a whole answer on the clock. The six steps we use will work on any topic you meet, on a test or in class.",
 prompt="Describe a place that is important to you. Tell what you see, hear, and feel there, and explain why it matters.",
 read_board="**Describe** · a **place** · what you **see, hear, feel** · **why** it matters",
 read_say="Step one. Read it. I read the prompt twice and mark the task words. Describe is the job. Place is the topic. See, hear, and feel mean the prompt wants my senses. And why it matters means I must give a reason. Four marks. Four things my answer must do.",
 read_q="Which one is NOT something this prompt asks you to do?", read_opts=["Describe a place", "Use what you see, hear, and feel", "Tell a story about a trip you took"], read_ans=2,
 read_why="The prompt asks for a place, your senses, and a reason. It does not ask for a story about a trip. Staying on the topic is the first thing a reader checks.",
 brain_board="place: my grandmother's kitchen · see: yellow walls, big blue pot · smell: fresh tortillas · hear: radio, spoon on the pot · feel: warm, safe · why: my family comes together",
 brain_say="Step two. Brainstorm it. I write notes fast, without full sentences. My place is my grandmother's kitchen. I see yellow walls and a big blue pot. I smell fresh tortillas. I hear the radio and a spoon on the pot. I feel warm and safe. And why it matters: my family comes together there. Messy notes are fine. Nobody grades the notes.",
 brain_q="Which note does NOT belong to the kitchen?", brain_opts=["smell: fresh tortillas", "sound: cars on the highway", "feel: warm and safe"], brain_ans=1,
 brain_why="Cars on the highway do not belong in my grandmother's kitchen. When I brainstorm, I keep every note tied to my one place.",
 plan_board="1 Opening: place + why · 2 What I see and smell · 3 What I hear and feel · 4 Closing: why it matters",
 plan_say="Step three. Plan it. Four parts: an opening with the place and the reason, one part for what I see and smell, one part for what I hear and feel, and a closing that returns to why it matters. A plan takes one minute and saves ten.",
 open="My grandmother's kitchen is the place that matters most to me because it is where my family comes together.",
 open_say="Step four. Open it. My first sentence names the place and gives the reason, both at once. Now the reader knows exactly where we are going. I use words from the prompt: place, matters.",
 open_ask="Your turn. Write your opening: name your place and say why it matters. Type it in the notebook.", open_prompt="Your opening: name your place and say why it matters.",
 open_checks=[("has_any", ["place", "matters", "important", "because"], "Use words from the prompt: place, matters, important, because.")],
 open_model="The soccer field behind my house is the place that matters most to me because I feel free there.",
 body=[("When I walk in, I see yellow walls and a big blue pot on the stove. The smell of fresh tortillas fills the whole room.",
        "Step five. Build it. The first body part: what I see and smell. Notice the exact words. Not a nice kitchen, but yellow walls and a big blue pot. Exact words make the reader see it. "
        "When I walk in, I see yellow walls and a big blue pot on the stove. The smell of fresh tortillas fills the whole room."),
       ("Then, I hear the radio playing old songs and my grandmother's spoon tapping the pot. Her voice is soft, and I feel warm and safe.",
        "The second body part: what I hear and feel. Notice then, a small word that moves the reader along. "
        "Then, I hear the radio playing old songs and my grandmother's spoon tapping the pot. Her voice is soft, and I feel warm and safe.")],
 detail_ask="Your turn. Write one sentence about what you see or hear in your place. Use one exact detail, not a weak word like nice or good.",
 detail_prompt="One sentence: what you see or hear. No nice, good, or thing.",
 detail_checks=[("has_any", ["see", "saw", "hear", "smell", "feel", "look"], "Use a sense word: see, hear, smell, feel."), ("not_regex", r"\b(nice|good|thing|things)\b", "Replace nice, good, or thing with an exact word."), ("starts_upper", None, "Start with a capital letter."), ("min_words", 7, "At least seven words.")],
 detail_model="I see tall green grass and white lines, and I hear my friends shouting my name.",
 close="This kitchen matters because it makes me feel that I belong. No matter where I go, I will carry its smell and its warmth with me.",
 close_say="Step six. Close it. My last sentences return to why it matters, which is the question the prompt asked. A good closing says the answer one more time in new words, and then stops. This kitchen matters because it makes me feel that I belong. No matter where I go, I will carry its smell and its warmth with me.",
 edit_q="Now check it. Which sentence is correct?", edit_opts=["i see a big blue pot on the stove", "I see a big blue pot on the stove.", "I seen a big blue pot on the stove."], edit_ans=1,
 edit_why="The second one. It starts with a capital letter, it ends with a period, and it uses see, not seen. I check capitals, verbs, punctuation, and spelling, every time, after I write.",
 open_line="The place that matters most to me is my grandmother's kitchen because it is where my family comes together.",
 close_line="This kitchen matters because it makes me feel that I belong. No matter where I go, I will carry its smell and its warmth with me.",
 rubric=["My first sentence names a place and says why it matters.", "I used at least three senses or exact details: see, hear, smell, feel.", "I used exact words instead of nice, good, or thing.", "Every sentence starts with a capital letter and ends with punctuation.", "My last sentences return to why the place matters."],
 plan_labels=["Place + why", "What I see", "What I hear", "How I feel", "Closing"],
 why5="Why is it a five? The first sentence names the place and the reason. It uses three senses with exact details. It never says nice or good. And the last sentences answer the question the prompt asked, why it matters.",
 outro="You just described a place with the six steps. Next lesson, a different kind of topic: explaining how to do something. The routine stays the same.")

# ───────────────────────── Lesson 2 · explain how ─────────────────────────
T2 = dict(
 title="Explain how to do something", sub="Clear steps for a new person", goal="I can explain a process in clear steps with First, Next, Then, Finally for a reader who is new to it.",
 intro="Welcome back. This is a different kind of topic: explaining how to do something. But the routine is the same six steps, and you will see that the steps work again. This time the secret is the reader. Your reader has never done this before, so every step has to be clear.",
 prompt="Choose something you know how to do. Explain how to do it, step by step, so a new person could do it too.",
 read_board="**Explain how** · something you **know** · **step by step** · for a **new person**",
 read_say="Step one. Read it. Explain how is the job. Something you know is the topic, and I choose it. Step by step tells me the shape: steps, in order. And a new person is my reader. Four marks.",
 read_q="Who is your reader?", read_opts=["Someone who already knows how to do it", "A new person who has never done it", "Only your best friend"], read_ans=1,
 read_why="A new person. That means no skipped steps. If I forget to say crack the egg, a new person is lost.",
 brain_board="topic: how to make scrambled eggs · need: eggs, pan, fork, butter, salt · steps: crack, beat, melt butter, pour, stir, serve · careful: the pan is hot",
 brain_say="Step two. Brainstorm it. My topic is scrambled eggs. First, what you need: eggs, a pan, a fork, butter, salt. Then the steps in order: crack, beat, melt the butter, pour, stir, serve. And one warning: the pan is hot.",
 brain_q="Which note does NOT belong in how to make scrambled eggs?", brain_opts=["steps: crack, beat, stir", "need: eggs, pan, butter", "my favorite soccer team"], brain_ans=2,
 brain_why="My favorite soccer team. It is a fine thing to know, but it does not help a new person make eggs. In a how-to, every note helps the reader do the job.",
 plan_board="1 Opening: what + why it is easy · 2 What you need · 3 Steps: First, Next, Then · 4 A warning or tip · 5 Closing",
 plan_say="Step three. Plan it. An opening that says what and why it is easy. What you need. The steps with First, Next, Then. A warning. And a closing. Notice that the steps are the biggest part, because the steps are what the reader came for.",
 open="Scrambled eggs are easy to make, and anyone can learn how in five minutes.",
 open_say="Step four. Open it. One sentence that says what I will teach, and gives the reader a reason to keep reading: it is easy, and it takes five minutes.",
 open_ask="Your turn. Write your opening: say what you will teach and one reason it is easy or useful.", open_prompt="Your opening: what you will teach, and why it is easy or useful.",
 open_checks=[("has_any", ["how to", "easy", "learn", "simple", "useful", "can", "will"], "Say what you will teach: how to, easy, learn, simple, useful.")],
 open_model="Making a paper airplane is simple, and you only need one sheet of paper.",
 body=[("First, gather what you need: two eggs, a pan, a fork, a little butter, and a pinch of salt.",
        "Step five. Build it. The first body part: what you need. First, with a comma, tells the reader this is the start. First, gather what you need: two eggs, a pan, a fork, a little butter, and a pinch of salt."),
       ("Next, crack the eggs into a bowl and beat them with the fork. Then, melt the butter in the pan on low heat. After that, pour in the eggs and stir slowly until they are soft and yellow.",
        "The steps. Watch the signal words: Next, Then, After that. Each one has a comma. And each step starts with a command verb: crack, beat, melt, pour, stir. Next, crack the eggs into a bowl and beat them with the fork. Then, melt the butter in the pan on low heat. After that, pour in the eggs and stir slowly until they are soft and yellow."),
       ("Be careful: the pan is hot, so never touch it without a towel.",
        "And the warning. A good teacher thinks about what could go wrong. Be careful: the pan is hot, so never touch it without a towel.")],
 detail_ask="Your turn. Write one step. Start with First, Next, Then, or Finally, add a comma, and use a command verb like crack, stir, or fold.",
 detail_prompt="One step: a signal word, a comma, and a command verb.",
 detail_checks=[("has_regex", r"^(First|Next|Then|After that|Finally),", "Start with First, Next, Then, After that, or Finally, and put a comma after it."), ("min_words", 6, "At least six words.")],
 detail_model="Next, fold the paper in half so the edges match.",
 close="Finally, put the eggs on a plate and enjoy them while they are warm. Now you know how to make breakfast for yourself.",
 close_say="Step six. Close it. A how-to ends with the finish line: the last step and the result. Finally, put the eggs on a plate and enjoy them while they are warm. Now you know how to make breakfast for yourself.",
 edit_q="Now check it. Which step is written best for a new person?", edit_opts=["Then you stir the eggs it is easy.", "Then, stir the eggs slowly until they are soft.", "Then stirring eggs slow."], edit_ans=1,
 edit_why="The second one. It has a signal word and a comma, a command verb, and it tells how: slowly, and until what. The first one runs two ideas together. The third one has no real verb.",
 open_line="Scrambled eggs are easy to make, and anyone can learn how in five minutes.",
 close_line="Finally, put the eggs on a plate and enjoy them while they are warm. Now you know how to make breakfast for yourself.",
 rubric=["My first sentence says what I will teach.", "I listed what the reader needs.", "My steps are in order, with First, Next, Then, Finally and a comma after each.", "Each step starts with a command verb.", "I gave one warning or tip, and a closing."],
 plan_labels=["What + why easy", "What you need", "Steps", "Warning / tip", "Closing"],
 why5="Why is it a five? The first sentence says what and why it is easy. The things needed come before the steps. The steps are in order with signal words and commas, and each one starts with a command verb. There is a warning, and a closing.",
 outro="You just explained a process with the six steps. Next lesson: telling about a time. That one needs the past tense.")

# ───────────────────────── Lesson 3 · a time you learned ─────────────────────────
T3 = dict(
 title="Tell about a time", sub="A short story in the past tense", goal="I can tell a short true story with a beginning, a middle, and an end, in the past tense, and say what I learned.",
 intro="Welcome back. Today's topic asks for a story: a time that really happened to you. A story has its own shape, and it has its own grammar trap, the past tense. We will use the same six steps, and I will show you where the past tense matters.",
 prompt="Write about a time you learned something important. Tell what happened and what you learned.",
 read_board="**Write about** · a **time** · what **happened** · what you **learned**",
 read_say="Step one. Read it. Write about a time. A time is something that already happened, so I will write in the past. What happened is the story. What you learned is the lesson, and the prompt asks for it, so I must not forget it.",
 read_q="Which verb form will most of your sentences use?", read_opts=["I learn", "I learned", "I will learn"], read_ans=1,
 read_why="I learned. A time that already happened is told in the past: learned, walked, felt, said. If the verbs are in the past, the reader hears a story.",
 brain_board="time: my first day at a new school · beginning: scared, no friends · middle: a boy shared his lunch · end: I learned to say hello first",
 brain_say="Step two. Brainstorm it. My time is my first day at a new school. Beginning: I was scared and had no friends. Middle: a boy sat with me and shared his lunch. End: I learned that I can say hello first.",
 brain_q="Which note is the MIDDLE of the story, the thing that happened?", brain_opts=["beginning: scared, no friends", "middle: a boy shared his lunch", "end: I learned to say hello first"], brain_ans=1,
 brain_why="A boy shared his lunch. The beginning sets up the problem, the middle is what happens, and the end is what I learned.",
 plan_board="1 Opening: when + what I learned · 2 Beginning: the problem · 3 Middle: what happened (Then, Suddenly) · 4 End: what I learned",
 plan_say="Step three. Plan it. An opening that says when it happened. A beginning with the problem. A middle with what happened, using Then and Suddenly. And an end with what I learned.",
 open="Last September, on my first day at a new school, I learned that one small hello can change everything.",
 open_say="Step four. Open it. I begin with when it happened: last September. Then I hint at what I learned. A reader who sees a time word and a hint wants to read on.",
 open_ask="Your turn. Write your opening: say when it happened and hint at what you learned.", open_prompt="Your opening: when it happened + a hint of what you learned.",
 open_checks=[("has_regex", r"\b(last|ago|year|day|week|month|once|when|summer|winter|spring|fall|september|october|november|december|january|february|march|april|may|june|july|august|morning|night)\b", "Say when it happened: last year, two years ago, one day.")],
 open_model="Two years ago, when I moved to a new country, I learned that being brave is a choice.",
 body=[("At first, I was scared. I walked into the cafeteria and could not find one person I knew. My hands were shaking, and I sat alone.",
        "Step five. Build it. The beginning, the problem. Listen to the verbs: was, walked, could not find, shaking, sat. All past. At first, I was scared. I walked into the cafeteria and could not find one person I knew. My hands were shaking, and I sat alone."),
       ("Then, a boy with a red backpack sat down next to me and shared his lunch. He smiled and said, \"Hi, I am Marcos.\" Suddenly, my fear felt smaller.",
        "The middle, what happened. Then and Suddenly move the story forward. And notice the exact details: a red backpack, a smile, his name. Then, a boy with a red backpack sat down next to me and shared his lunch. He smiled and said, Hi, I am Marcos. Suddenly, my fear felt smaller.")],
 detail_ask="Your turn. Write one sentence about what happened. Use a time word like then or suddenly and a past-tense verb like walked, saw, felt, or said.",
 detail_prompt="One sentence: a time word + a past-tense verb.",
 detail_checks=[("has_any", ["then", "suddenly", "after that", "next", "finally", "first", "later", "at first"], "Use a time word: then, suddenly, after that, later."), ("has_regex", r"\b\w+ed\b|\b(was|were|saw|felt|said|went|came|took|gave|made|ran|sat|began|knew|told|found|got|had)\b", "Use a past-tense verb: walked, saw, felt, said, went."), ("min_words", 7, "At least seven words.")],
 detail_model="Then, I opened my notebook and said hello to the girl next to me.",
 close="That day I learned that I do not have to wait for friendship; I can start it. Now, when a new student arrives, I am the first to say hello.",
 close_say="Step six. Close it. The prompt asked what I learned, so my ending says it directly. That day I learned that I do not have to wait for friendship; I can start it. Now, when a new student arrives, I am the first to say hello. See how the last line shows the lesson in action.",
 edit_q="Now check it. Which sentence keeps the story in the past?", edit_opts=["Then, he sits next to me and shared his lunch.", "Then, he sat next to me and shared his lunch.", "Then, he sit next to me and share his lunch."], edit_ans=1,
 edit_why="The second one. Sat and shared are both past. The first one jumps from sits to shared. When I check, I read only the verbs, and I ask: is every one the same time?",
 open_line="Last September, on my first day at a new school, I learned that one small hello can change everything.",
 close_line="That day I learned that I do not have to wait for friendship; I can start it. Now, when a new student arrives, I am the first to say hello.",
 rubric=["My first sentence says when it happened.", "My story has a beginning, a middle, and an end.", "Most verbs are in the past tense, and I checked each one.", "I used time words: at first, then, suddenly, after that.", "I said clearly what I learned."],
 plan_labels=["When + hint", "Beginning", "Middle", "End", "What I learned"],
 why5="Why is it a five? The first sentence tells when. There is a clear beginning, middle, and end. The verbs stay in the past. Time words move the story along, and the ending says directly what was learned.",
 outro="That was a story with the six steps. Next lesson: an opinion, where you must give reasons and examples.")

# ───────────────────────── Lesson 4 · opinion ─────────────────────────
T4 = dict(
 title="Give your opinion", sub="A claim, two reasons, and the other side", goal="I can state an opinion that answers the question and support it with two reasons, examples, and a nod to the other side.",
 intro="Welcome back. Now the topic that appears most often: an opinion question. Should students do this, should schools do that. The six steps stay the same. What changes is the shape of the middle: reasons, and an example for each reason.",
 prompt="Should students have homework on weekends? Explain your opinion with reasons and examples.",
 read_board="**Should** students have homework on weekends? · my **opinion** · **reasons** · **examples**",
 read_say="Step one. Read it. Should is the signal for an opinion: yes or no. Explain with reasons and examples tells me what to build. So my answer needs a claim, reasons, and an example for each one.",
 read_q="What does the word should ask you for?", read_opts=["A story about your weekend", "Your opinion: yes or no, and why", "A list of weekend games"], read_ans=1,
 read_why="Your opinion, yes or no, and why. A should question is never answered with a story. It is answered with a claim and reasons.",
 brain_board="opinion: NO homework on weekends · reason 1: students need rest (example: tired on Monday) · reason 2: family time (example: cooking together) · other side: practice helps, but 20 minutes is enough",
 brain_say="Step two. Brainstorm it. My opinion: no homework on weekends. Reason one: students need rest. My example: I come to class tired on Monday. Reason two: family time. My example: my family cooks together on Sunday. And the other side: some teachers say practice helps, and that is fair, so twenty minutes is enough.",
 brain_q="Which note is the example for the reason rest?", brain_opts=["I come to Monday class tired when I work all weekend.", "Some teachers give long projects.", "Families eat dinner together."], brain_ans=0,
 brain_why="I come to Monday class tired. It is a real situation that shows the reason. An example is a small picture of the reason.",
 plan_board="1 Opening: my claim · 2 Reason 1 + example · 3 Reason 2 + example · 4 The other side · 5 Closing",
 plan_say="Step three. Plan it. The claim. Reason one with its example. Reason two with its example. A sentence about the other side. And a closing. Five parts, five boxes.",
 open="In my opinion, students should not have homework on weekends.",
 open_say="Step four. Open it. One sentence that answers the question with the words of the prompt: students, homework, weekends. The reader knows my side right away.",
 open_ask="Your turn. Write your claim: yes or no, in one sentence that uses the words homework and weekends.", open_prompt="Your claim: yes or no, with homework and weekends.",
 open_checks=[("has_any", ["homework"], "Use the word homework from the prompt."), ("has_any", ["weekend"], "Use the word weekends from the prompt."), ("has_any", ["should", "opinion", "think", "believe"], "Give an opinion: should, I think, I believe, in my opinion.")],
 open_model="I believe students should have a little homework on weekends.",
 body=[("First, students need rest. For example, when I work all weekend, I come to class tired on Monday and cannot focus.",
        "Step five. Build it. Reason one, with First and a comma, and then For example. The example is a real situation, not a general idea. First, students need rest. For example, when I work all weekend, I come to class tired on Monday and cannot focus."),
       ("Second, weekends are for family. As a result, students who spend Saturday with their families feel happier and ready to learn.",
        "Reason two. Second, with a comma. And As a result shows what the reason causes. Second, weekends are for family. As a result, students who spend Saturday with their families feel happier and ready to learn."),
       ("However, some teachers say practice helps, and that is true. A short reading assignment of twenty minutes is enough.",
        "And the other side. However tells the reader I heard the other opinion. I agree with a part of it, and still hold my claim. However, some teachers say practice helps, and that is true. A short reading assignment of twenty minutes is enough.")],
 detail_ask="Your turn. Write one reason. Start with First or Second and a comma, then add an example that starts with For example.",
 detail_prompt="One reason + an example: First or Second, then For example.",
 detail_checks=[("has_regex", r"^(First|Second|Also|In addition|Another reason)", "Start with First, Second, Also, or In addition."), ("has_any", ["for example", "for instance", "such as"], "Add an example: For example, For instance, such as."), ("min_words", 12, "At least twelve words, a reason and an example.")],
 detail_model="Second, weekends are for family. For example, my family cooks together on Sunday.",
 close="In conclusion, students need weekends to rest and to be with their families. Short, smart assignments during the week are better for everyone.",
 close_say="Step six. Close it. In conclusion, with a comma, and then the claim again in new words. In conclusion, students need weekends to rest and to be with their families. Short, smart assignments during the week are better for everyone.",
 edit_q="Now check it. Which sentence has correct punctuation?", edit_opts=["First students need rest", "First, students need rest.", "First students, need rest."], edit_ans=1,
 edit_why="The second one. A comma goes right after First, and a period ends the sentence. The comma after a transition is one of the easiest points to win.",
 open_line="In my opinion, students should not have homework on weekends.",
 close_line="In conclusion, students need weekends to rest and to be with their families. Short, smart assignments during the week are better for everyone.",
 rubric=["My first sentence answers the question and uses the prompt's words.", "I gave two reasons, each with an example or a result.", "I used transitions: First, Second, However, In conclusion, with commas.", "I wrote one sentence about the other side.", "I checked capitals, verbs, and punctuation."],
 plan_labels=["Claim", "Reason 1 + example", "Reason 2 + example", "Other side", "Conclusion"],
 why5="Why is it a five? The first sentence answers the question in the prompt's words. There are two reasons, and each one has an example or a result. The transitions have commas. One sentence admits the other side. And the conclusion says the claim again.",
 outro="That is a full opinion answer. One lesson left, and it is the most useful one: how to use these six steps on any topic you meet.")

# ───────────────────────── Lesson 5 · any topic ─────────────────────────
A = []
A.append(("say", "Welcome to the last lesson. You have used the six steps on four kinds of topics. Now I want you to be able to do it alone, on any topic, even one I have never seen. So this time, you bring the topic. Type one you really have to write about, or one you invent, and we will move through the steps together."))
A.append(("head", "Lesson 5 · Any topic", "Lesson five. Any topic."))
A.append(("write", "① READ IT: the first word is the job\n**Describe** → senses and exact details\n**Explain how** → steps in order\n**Tell about a time** → past tense: beginning, middle, end\n**Should / opinion** → claim + two reasons + examples\n**Compare** → alike and different", "Step one is always the same: find the job word. Describe means senses and exact details. Explain how means steps in order. Tell about a time means past tense, with a beginning, a middle, and an end. Should or opinion means a claim, two reasons, and examples. And compare means how things are alike and how they are different. The job word tells you the shape of your answer."))
A.append(("pick", "The prompt says: Explain how to get ready for a test. What will your answer need?", ["Steps with First, Next, Then", "A story in the past tense", "A claim and two reasons"], 0, "Steps with First, Next, Then. Explain how means steps in order, for a reader who is new."))
A.append(("pick", "The prompt says: Should schools give a longer lunch? What goes in your first sentence?", ["A story about lunch", "Your opinion: yes or no", "A list of steps"], 1, "Your opinion, yes or no. A should question needs a claim in the first sentence."))
A.append(("ask", "Now it is your turn to bring the topic. Type the prompt you have to write about, or make one up that begins with Describe, Explain how, Tell about, or Should.", "Type your topic as a prompt.", [("min_words", 4, "A prompt has at least four words."), ("has_regex", r"^(describe|explain|tell|write|should|compare|what|why|how|choose|is|do|are)", "Begin with a job word: Describe, Explain, Tell, Write, Should, Compare, Why, How.")], "Describe a person who helps you.", "Good. That is your topic. Everything we do now is about this one prompt.", "Begin with a job word the prompt uses: Describe, Explain, Tell, Write, Should, or Compare."))
A.append(("write", "② BRAINSTORM IT\nwrite 4 to 6 notes, fast\nwords and phrases, not sentences\nno grading!", "Step two. Brainstorm it. Write four to six notes about your topic, fast. Words and phrases, not full sentences. Nobody grades the notes."))
A.append(("ask", "Write your notes in the notebook, with a comma between each one.", "Brainstorm: four or more notes, separated by commas.", [("min_words", 6, "Write at least six words of notes."), ("has_regex", r",", "Separate your notes with commas.")], "my grandfather, teaches me guitar, very patient, Sunday afternoons, I feel proud", "Good notes. That is plenty to build from.", "Write your notes with commas between them, for example: my grandfather, teaches me guitar, very patient."))
A.append(("write", "③ PLAN IT\n1 Opening: the topic\n2 Part one\n3 Part two\n4 Closing", "Step three. Plan it. Number your parts. At least three: an opening, one or two body parts, and a closing. The job word decides what goes in the parts."))
A.append(("ask", "Write your plan in the notebook: number your parts, one through four, each with a few words.", "Plan: number your parts 1, 2, 3, 4.", [("has_regex", r"1.*2", "Number your parts: 1 ... 2 ..."), ("min_words", 8, "A few words for each part, at least eight in all.")], "1 who he is 2 what he teaches me 3 how I feel 4 why he matters", "That plan will keep you on the topic.", "Number your parts one, two, three, four, each with a few words."))
A.append(("write", "④ OPEN IT\none sentence: name the topic\nuse words from the prompt\nno Hello. No My name is.", "Step four. Open it. One sentence that names the topic and uses words from the prompt. Do not begin with hello, and do not begin with my name is."))
A.append(("ask", "Write your opening sentence for your own topic.", "Your opening: name the topic, use the prompt's words.", [("min_words", 8, "A full sentence, at least eight words."), ("starts_upper", None, "Start with a capital letter."), ("ends_punct", None, "End with a period."), ("not_regex", r"^(hello|hi|my name is)", "Do not begin with hello or my name is. Go straight to the topic.")], "My grandfather is the person who helps me most because he teaches me patience.", "That opening gets right to the topic.", "Look at the note under your line. Name the topic in the first sentence."))
A.append(("write", "⑤ BUILD IT\ntransition + point + detail or example\nFirst, … For example, …\nThen, … Suddenly, …", "Step five. Build it. Each body sentence has a signal word to start, a point, and a detail or an example. First, with a comma, then your point, then for example."))
A.append(("ask", "Write one body sentence about your topic. Start with a signal word and a comma, such as First, Then, Also, or For example, and give a detail.", "One body sentence: signal word + comma + detail.", [("has_regex", r"^(First|Second|Next|Then|Also|For example|In addition|One|Another|At first|Suddenly|After that)\b", "Start with a signal word: First, Then, Also, For example."), ("has_regex", r"^\w+( \w+)?,", "Put a comma right after the signal word."), ("min_words", 8, "At least eight words.")], "For example, every Sunday he sits with me for an hour and shows me one new chord.", "Yes. A reader can picture that.", "Start with a signal word and a comma, then give one clear detail."))
A.append(("write", "⑥ CLOSE IT\nreturn to the prompt\nsay the answer again in new words", "Step six. Close it. Return to the prompt and say your answer again in new words. Then stop."))
A.append(("ask", "Write a closing sentence for your topic.", "A closing: say the answer again, in new words.", [("min_words", 8, "At least eight words."), ("has_any", ["conclusion", "finally", "that is why", "because", "matters", "learned", "now", "so"], "A closing often uses: In conclusion, Finally, That is why, Now."), ("ends_punct", None, "End with a period.")], "That is why my grandfather matters to me: he teaches me music and patience.", "Good. That ends the answer.", "Use a closing signal like In conclusion, Finally, or That is why, and return to the topic."))
A.append(("clear", "Board wiped. Now, the check at the end."))
A.append(("write", "CHECK IT: C U P S\n**C** apitals\n**U** sage: verbs, same time\n**P** unctuation: , after First. End marks.\n**S** pelling", "Last, check it. Think of the word C U P S. C: capitals at the start of every sentence and for names. U: usage. Read only the verbs and ask, is every one the right time? P: punctuation. A comma after First, Next, Then, and an end mark on every sentence. S: spelling. Check the words from the prompt first, because they are on the page."))
A.append(("pick", "Which sentence passes the C U P S check?", ["then we play a song together", "Then, we play a song together.", "Then, we played a song together, and then he play it."], 1, "The second one. A capital letter starts it, a period ends it, and the verb is correct. The third one mixes played and play."))
A.append(("say", "Here is the whole routine in one line. Read it. Brainstorm it. Plan it. Open it. Build it. Close it and check it. Now do it once on the clock, with your own topic, or with one from the list."))
A.append(("task", "Your own topic. Choose a prompt from the list, or use the one you typed. Plan in the five boxes first. Go.", "Topic: choose a prompt from the list, or write about the one you typed.", 15,
 ["My first sentence names the topic and uses the prompt's words.", "My answer has the shape the job word asks for: senses, steps, a story, or reasons.", "I used signal words with commas: First, Then, For example, In conclusion.", "I used exact words instead of nice, good, or thing.", "I checked C U P S: capitals, usage, punctuation, spelling."],
 "The person who helps me most is my grandfather because he teaches me patience. First, he teaches me guitar. For example, every Sunday he sits with me for an hour and shows me one new chord. Then, he waits while I try. He never gets angry, even when I make the same mistake ten times. As a result, I feel brave enough to keep trying. That is why my grandfather matters to me: he teaches me music, and he teaches me patience.",
 "Here is a five, for the prompt: describe a person who helps you. The person who helps me most is my grandfather because he teaches me patience. First, he teaches me guitar. For example, every Sunday he sits with me for an hour and shows me one new chord. Then, he waits while I try. He never gets angry, even when I make the same mistake ten times. As a result, I feel brave enough to keep trying. That is why my grandfather matters to me: he teaches me music, and he teaches me patience. Why is it a five? The first sentence names the topic and the reason. The signal words have commas. The example is exact, a real Sunday and a real chord. And the closing returns to the prompt.",
 ["Opening", "Part one", "Part two", "Detail / example", "Closing"]))
A.append(("say", "That is the whole Write About It lesson. Six steps, any topic. Come back to lesson five every week with a new prompt, and bring your plan boxes to the test. I'll see you at the board."))

LESSONS = [L(1, T1), L(2, T2), L(3, T3), L(4, T4),
           {"id": "t5", "n": 5, "title": "Any topic", "sub": "Bring your own prompt", "mins": 22, "goal": "I can use the six steps on any prompt I am given, including one I choose myself.", "beats": A}]

PROMPTS = [
 "Describe a place that is important to you. Tell what you see, hear, and feel there, and explain why it matters.",
 "Choose something you know how to do. Explain how to do it, step by step, so a new person could do it too.",
 "Write about a time you learned something important. Tell what happened and what you learned.",
 "Should students have homework on weekends? Explain your opinion with reasons and examples.",
 "Describe a person who helps you. Explain how this person helps.",
 "Explain how to get ready for a big test.",
 "Write about a time you helped someone. Tell what happened and how you felt.",
 "Should schools give students a longer lunch? Explain your opinion with reasons and examples.",
 "Compare living in a small town and living in a big city. Tell how they are alike and different.",
]

SAY = [(r"—", ", "), (r"\bC U P S\b", "C, U, P, S"), (r"\bCUPS\b", "C, U, P, S"), (r"[①②③④⑤⑥]", ""), (r"\*\*|~~|_", ""), (r"\s*/\s*", ". "), (r"→", ", becomes, "), (r"\bELPA21\b", "ELPA twenty-one"), (r"\bEL\b", "E L"),
       (r"\bsept\b", "September")]


def clips():
    out = []
    for Ls in LESSONS:
        for i, b in enumerate(Ls["beats"]):
            k = b[0]; st = f"{Ls['id']}-{i:02d}"
            if k == "say": out.append((st, b[1]))
            elif k in ("head", "write"): out.append((st, b[2]))
            elif k == "clear": out.append((st, b[1]))
            elif k == "pick": out.append((st, b[1])); out.append((st + "w", b[4]))
            elif k == "ask": out.append((st, b[1])); out.append((st + "o", b[5])); out.append((st + "f", b[6]))
            elif k == "task": out.append((st, b[1])); out.append((st + "m", b[6]))
    for i, t in enumerate(FB["ok"]): out.append((f"fb-ok-{i}", t))
    for i, t in enumerate(FB["fix"]): out.append((f"fb-fix-{i}", t))
    return out


if __name__ == "__main__":
    c = clips(); print(len(LESSONS), "lessons;", len(c), "clips;", sum(len(t.split()) for _, t in c), "words")
