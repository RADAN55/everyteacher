#!/usr/bin/env python3
"""The Writing Studio — eight lessons taught at the board by Mr. Castillo.

Beat grammar (each lesson is a list of beats; the page plays them in order):

  ("say", text)                      teacher talks; nothing changes on the board
  ("head", title, say)               a heading goes on the board
  ("write", line, say)               a line goes on the board while he talks
                                     **yellow chalk**  _underline_  ~~strike~~
  ("clear", say)                     he wipes the board
  ("pick", say, [options], ans, why_say)
                                     a choice on the board; the class answers
  ("ask", say, board_prompt, checks, model, ok_say, fix_say)
                                     the student writes one line in the notebook;
                                     checks = [(kind, arg, note), ...] where kind is
                                     min_words | has_any | has_regex | not_regex |
                                     starts_upper | ends_punct
  ("task", say, board_prompt, minutes, rubric, model, model_say)
                                     the timed You-do: plan, write, self-score, then
                                     hear a level-5 model and why it is a 5

Everything he says is synthesized; the page says so. The lessons teach the
features a top ELPA21 writing response shows — a claim that answers the
prompt, reasons with evidence, organizing transitions, controlled sentences
and clean mechanics — without quoting any scoring document.
"""

TEACHER = "Mr. Castillo"
VOICE = 5          # am_adam
TITLE = "The Writing Studio"
SUB = "Write for a 4 or a 5 — eight lessons at the board"

TRANS = ["first", "second", "third", "finally", "however", "in addition", "also", "for example", "for instance",
         "as a result", "therefore", "in contrast", "on the other hand", "unlike", "while", "whereas", "both",
         "in conclusion", "because", "so", "then", "next", "although", "even though"]

FB = {
  "ok": ["Good. That is exactly what a scorer wants to see.", "Yes. That line does its job.", "That works. Keep that habit."],
  "fix": ["Close. Look at the board and fix one thing.", "Not yet. Check the note under your line.", "Almost. One more pass."],
}

LESSONS = [
# ───────────────────────────── 1 ─────────────────────────────
{"id": "w1", "n": 1, "title": "What a 5 looks like", "sub": "The shape of a top answer", "mins": 9,
 "goal": "I can name the five parts of a top-scoring answer and find them in a sample.",
 "beats": [
 ("say", "Welcome to the Writing Studio. I'm Mr. Castillo. For the next eight lessons, we are going to the board together, and when we finish, you will know exactly what a writing answer needs to score a four or a five on the English language proficiency test. Not more words. The right parts. Let's start by looking at one."),
 ("head", "Lesson 1 · What a 5 looks like", "Lesson one. What a five looks like."),
 ("write", "Prompt: **Should students be allowed to use phones in class?** Explain your opinion with reasons.", "Here is a prompt like the ones on the test. Should students be allowed to use phones in class? Explain your opinion with reasons. Read it twice. The prompt tells you the job: an opinion, with reasons."),
 ("say", "Now I'm going to write an answer that would score a five, and I'm going to write it slowly, one part at a time, so you can see the parts."),
 ("write", "① In my opinion, students should not use phones during class, except when the teacher asks for them.", "Part one. The claim. In my opinion, students should not use phones during class, except when the teacher asks for them. Notice: it answers the question in one sentence, and it uses the words from the prompt. Students. Phones. Class."),
 ("write", "② First, phones take attention away from the lesson. For example, when a message arrives, a student reads it instead of the board.", "Part two. The first reason, with an example. First, phones take attention away from the lesson. For example, when a message arrives, a student reads it instead of the board. Reason, then example. The example is a picture a scorer can see."),
 ("write", "③ Second, phones make cheating easy. As a result, teachers cannot trust the grades.", "Part three. A second reason, with a result. Second, phones make cheating easy. As a result, teachers cannot trust the grades. Two reasons is the minimum for a four or a five. One reason is a three."),
 ("write", "④ However, some teachers use phones for research, and that is a good use.", "Part four. The other side. However, some teachers use phones for research, and that is a good use. This one sentence tells the scorer you can see more than one side. That is a five-level move."),
 ("write", "⑤ In conclusion, phones should stay in the backpack unless the teacher says otherwise.", "Part five. The conclusion. In conclusion, phones should stay in the backpack unless the teacher says otherwise. It repeats the claim in new words. Done."),
 ("say", "Count them with me. Claim. Reason one with an example. Reason two with a result. The other side. Conclusion. Five parts. Every lesson from here teaches one of those parts. Now you find them."),
 ("pick", "Which sentence is the claim, the sentence that answers the question?", ["First, phones take attention away from the lesson.", "In my opinion, students should not use phones during class.", "However, some teachers use phones for research."], 1,
  "The claim is: In my opinion, students should not use phones during class. It answers the question directly. The other two are a reason and the other side."),
 ("pick", "Which words tell the scorer that the writer is organized?", ["phones, class, teacher", "First, Second, However, In conclusion", "opinion, reasons, explain"], 1,
  "First, second, however, in conclusion. Those are transitions. They are the signs on the road. A scorer sees them in two seconds, before reading a single idea."),
 ("pick", "Which sentence shows the writer can see the other side?", ["However, some teachers use phones for research, and that is a good use.", "Second, phones make cheating easy.", "In conclusion, phones should stay in the backpack."], 0,
  "However, some teachers use phones for research. That is the other side. A three says only my side. A five can say the other side and still hold the claim."),
 ("clear", "Let me wipe the board. Your turn to write one line."),
 ("head", "Your line · the claim", "Your line. Just the claim."),
 ("ask", "New prompt. Should the school day start later? Write only the claim: one sentence that answers the question and uses the words from the prompt. Type it in your notebook.",
  "Prompt: Should the school day start later? Write the claim only.",
  [("has_any", ["school day", "start later", "start"], "Use the words from the prompt: school day, start later."),
   ("has_any", ["should", "opinion", "think", "believe"], "A claim gives an opinion: should, I think, in my opinion."),
   ("starts_upper", None, "Start with a capital letter."), ("ends_punct", None, "End with a period."), ("min_words", 6, "A full sentence, at least six words.")],
  "In my opinion, the school day should start later because teenagers need more sleep.",
  "That is a claim. It answers the question, it uses the prompt's words, and it is one clean sentence.",
  "Look at the note under your line. A claim answers the question in one sentence and borrows the words of the prompt."),
 ("say", "One more thing before we go. A five is not long. The answer on the board was five sentences. Five parts, five sentences, and a scorer can find every part. That is the shape. Lesson two: the claim, and how to build it from any prompt."),
 ]},

# ───────────────────────────── 2 ─────────────────────────────
{"id": "w2", "n": 2, "title": "The claim", "sub": "Turn the prompt into your first sentence", "mins": 8,
 "goal": "I can turn any prompt into a one-sentence claim that answers it.",
 "beats": [
 ("say", "Lesson two. The claim. Here is a secret from scorers: the first sentence decides the mood of the whole read. If the first sentence answers the question, the scorer relaxes. If it doesn't, the scorer starts hunting. We don't want the scorer hunting."),
 ("head", "Lesson 2 · The claim", "To the board."),
 ("write", "A claim = **the prompt's words** + **your answer** + (**because** + one reason)", "A claim has a recipe. The prompt's words, plus your answer, plus, if you want, because and one reason. Let me show you with three prompts."),
 ("write", "Prompt: Is it better to study alone or with a group?", "Prompt one. Is it better to study alone or with a group?"),
 ("write", "Claim: It is better to study **with a group** because students can explain ideas to each other.", "Claim: It is better to study with a group because students can explain ideas to each other. See the prompt's words? It is better to study. Then my answer: with a group. Then because, and a reason."),
 ("write", "Prompt: Describe a person who has influenced you.", "Prompt two is different. Describe a person who has influenced you. No yes or no. Still, the claim names the answer."),
 ("write", "Claim: The person who has influenced me most is **my grandmother**, who taught me to finish what I start.", "The person who has influenced me most is my grandmother, who taught me to finish what I start. Prompt words, then the answer, then a detail that promises what the paragraph will be about."),
 ("write", "Prompt: Write an email to your principal asking for a longer lunch period.", "Prompt three. An email. Write an email to your principal asking for a longer lunch period. In an email the claim is the purpose sentence."),
 ("write", "Claim: I am writing to ask you to make the lunch period **ten minutes longer**.", "I am writing to ask you to make the lunch period ten minutes longer. Prompt words, answer, and a specific number. Specific beats general every time."),
 ("say", "Now watch what a weak claim looks like, so you can hear the difference."),
 ("write", "~~Phones are a big topic today and many people have different opinions about them.~~", "Phones are a big topic today and many people have different opinions about them. True, and useless. It does not answer anything. A scorer reads that and starts hunting. Cross it out."),
 ("write", "~~I will talk about studying.~~", "I will talk about studying. That announces; it does not answer. Cross it out."),
 ("pick", "Which one is a claim?", ["There are many ways to study and each person is different.", "Studying with a group is better because partners catch each other's mistakes.", "In this essay I will explain my opinion about studying."], 1,
  "Studying with a group is better because partners catch each other's mistakes. Prompt words, answer, because. The other two announce or wander."),
 ("clear", "Board wiped. Three prompts are coming. Write only the claim for each."),
 ("head", "Your lines · three claims", "Three claims."),
 ("ask", "Prompt: Should students have homework every night? Write the claim.",
  "Prompt: Should students have homework every night? → your claim",
  [("has_any", ["homework"], "Use the prompt's word: homework."), ("has_any", ["should", "think", "opinion", "believe"], "Give your answer: should or should not."),
   ("starts_upper", None, "Capital letter first."), ("ends_punct", None, "Period at the end."), ("min_words", 6, "A full sentence.")],
  "In my opinion, students should not have homework every night because they need time to rest and work.",
  "That answers the question. Prompt words, your answer. Good.", "Check the note. Use the word homework, and say should or should not."),
 ("ask", "Prompt: Describe a place that is important to you. Write the claim.",
  "Prompt: Describe a place that is important to you. → your claim",
  [("has_any", ["place", "important"], "Borrow the prompt's words: place, important."), ("starts_upper", None, "Capital letter first."), ("ends_punct", None, "End punctuation."), ("min_words", 6, "A full sentence.")],
  "The place that is important to me is my uncle's garage, where I learned to fix engines.",
  "You named the place and promised a detail. That is a claim for a describing prompt.", "Name the place in the sentence, and borrow the words place and important."),
 ("ask", "Prompt: Write an email to your coach explaining why you missed practice. Write the purpose sentence.",
  "Prompt: email to your coach, why you missed practice → your purpose sentence",
  [("has_any", ["writing", "missed", "practice", "sorry", "apologize"], "An email starts with its purpose: I am writing to..., or I missed practice because..."), ("starts_upper", None, "Capital letter first."), ("ends_punct", None, "End punctuation."), ("min_words", 6, "A full sentence.")],
  "I am writing to explain why I missed practice on Tuesday.",
  "That is a purpose sentence. The coach knows why you wrote in the first line.", "Start with the purpose: I am writing to explain why I missed practice."),
 ("say", "Three prompts, three claims, each one sentence. From now on, every time you see a prompt, the first thing your pen does is the claim. Lesson three: reasons, and the evidence that makes them count."),
 ]},

# ───────────────────────────── 3 ─────────────────────────────
{"id": "w3", "n": 3, "title": "Reasons and evidence", "sub": "Because, for example, and the specific noun", "mins": 9,
 "goal": "I can support a claim with two reasons, each with an example or a result.",
 "beats": [
 ("say", "Lesson three. Reasons and evidence. A claim alone is a three. A claim with two reasons is a four. A claim with two reasons that each carry an example or a result, that is a five. The difference is one word: for example."),
 ("head", "Lesson 3 · Reasons and evidence", "To the board."),
 ("write", "Reason = **because** + why    Evidence = **for example** / **as a result** + a picture", "A reason answers why. Evidence makes it a picture. Because gives the reason. For example or as a result gives the picture."),
 ("write", "Claim: Schools should serve breakfast to every student.", "Claim. Schools should serve breakfast to every student."),
 ("write", "Reason 1: First, students learn better when they are not hungry.", "Reason one. First, students learn better when they are not hungry. Good reason. But a scorer can't see it yet."),
 ("write", "Evidence: **For example**, in my first-period class, students who eat breakfast finish the warm-up; the ones who skip it put their heads down.", "Evidence. For example, in my first-period class, students who eat breakfast finish the warm-up; the ones who skip it put their heads down. Now the scorer can see a room. That is the picture."),
 ("write", "Reason 2: Second, free breakfast is fair, because not every family can afford it.", "Reason two. Second, free breakfast is fair, because not every family can afford it."),
 ("write", "Evidence: **As a result**, every student starts the day the same way.", "Evidence. As a result, every student starts the day the same way. Reason, then result. Two reasons, two pictures."),
 ("say", "Now the most important word in this lesson. Specific. General words are a three. Specific words are a five. Listen."),
 ("write", "~~Students do things on their phones.~~  →  Students **watch videos and text friends** on their phones.", "Students do things on their phones. Things. What things? Change it: students watch videos and text friends on their phones. Specific nouns. The scorer sees it."),
 ("write", "~~Breakfast is good for you.~~  →  Breakfast gives you **energy for the first two classes**.", "Breakfast is good for you. Good how? Breakfast gives you energy for the first two classes. Specific."),
 ("pick", "Which evidence is specific enough for a five?", ["Many students have problems in the morning.", "A lot of things happen when students are hungry.", "In my math class, three students fell asleep before 9 a.m. because they had not eaten."], 2,
  "In my math class, three students fell asleep before nine a.m. because they had not eaten. A class, a number, a time, a cause. The other two say things and problems, which are not pictures."),
 ("clear", "Board wiped. Your turn. I give the claim; you give a reason with evidence."),
 ("head", "Your lines · reason + evidence", "Reason plus evidence."),
 ("ask", "Claim: Students should learn a second language in high school. Write one reason that starts with First, and uses because.",
  "Claim: Students should learn a second language. → First, ... because ...",
  [("has_regex", r"^\s*first\b", "Start with First,"), ("has_any", ["because"], "Give the why with because."), ("ends_punct", None, "End punctuation."), ("min_words", 7, "A full reason, at least seven words.")],
  "First, students should learn a second language because many jobs need workers who can talk to customers in two languages.",
  "A reason with a because. Now the picture.", "Start with First, and give the why with because."),
 ("ask", "Now the evidence for that reason. Start with For example, and use a specific noun: a place, a job, a number, a person.",
  "Evidence → For example, ... (a specific place, job, number or person)",
  [("has_regex", r"^\s*for (example|instance)\b", "Start with For example,"), ("min_words", 8, "Make it a picture: at least eight words."), ("ends_punct", None, "End punctuation."),
   ("not_regex", r"\b(things|stuff|many ways|a lot of)\b", "Replace things, stuff, many ways with a specific noun.")],
  "For example, the hospital in our town hires nurses who speak Spanish and English, and it pays them more.",
  "A hospital, nurses, two languages, more pay. That is evidence a scorer can see.", "For example, then a specific place, job, number or person. No things, no stuff."),
 ("ask", "One more. Write a second reason that starts with Second, and ends with a result: use As a result.",
  "Reason 2 → Second, ... As a result, ...",
  [("has_regex", r"^\s*second\b", "Start with Second,"), ("has_any", ["as a result", "so ", "therefore"], "Finish with the result: As a result, ..."), ("min_words", 10, "Two ideas, at least ten words."), ("ends_punct", None, "End punctuation.")],
  "Second, learning a language teaches students how English works. As a result, their English grammar improves too.",
  "Reason and result. Your paragraph now has the body of a five.", "Second, then the reason. Then As a result, and what happens."),
 ("say", "Claim, reason, picture, reason, picture. That is the body. Lesson four puts the signs on the road: the transitions that make a scorer say organized."),
 ]},

# ───────────────────────────── 4 ─────────────────────────────
{"id": "w4", "n": 4, "title": "Transitions", "sub": "The signs on the road, and the comma that follows them", "mins": 8,
 "goal": "I can organize a response with transitions and punctuate them correctly.",
 "beats": [
 ("say", "Lesson four. Transitions. Here is how a scorer reads your answer: eyes first, then brain. Before reading a single idea, the eyes look for the signs. First. Second. However. In conclusion. If the signs are there, the answer looks organized before it is read. Let's put the signs on the board."),
 ("head", "Lesson 4 · Transitions", "To the board."),
 ("write", "To order: **First, Second, Third, Finally,**", "To put things in order: First, second, third, finally. Comma after each one."),
 ("write", "To add: **In addition, Also, Another reason is**", "To add an idea: In addition. Also. Another reason is."),
 ("write", "To show the other side: **However, On the other hand, Although**", "To show the other side: However. On the other hand. Although."),
 ("write", "To show a result: **As a result, Therefore, So**", "To show a result: As a result. Therefore. So."),
 ("write", "To give a picture: **For example, For instance**", "To give the picture: For example. For instance."),
 ("write", "To finish: **In conclusion, To sum up**", "To finish: In conclusion. To sum up."),
 ("say", "Now the rule that costs more points than any other on this list. The comma. When the transition starts the sentence, a comma follows it. First, comma. However, comma. As a result, comma. Watch."),
 ("write", "~~However students need phones for emergencies.~~ → **However,** students need phones for emergencies.", "However students need phones for emergencies. No comma. The scorer's pen twitches. Fix it: However, comma, students need phones for emergencies."),
 ("write", "~~In conclusion phones should stay away.~~ → **In conclusion,** phones should stay in the backpack.", "In conclusion phones should stay away. Fix it: In conclusion, comma. And while we are here, stay away is vague. Stay in the backpack is a picture."),
 ("say", "One more trap. Although is not however. However stands alone with a comma. Although needs the rest of the sentence."),
 ("write", "**However,** phones are useful for research.   /   **Although** phones are useful for research, they distract most students.", "However, phones are useful for research. Full stop before it, comma after it. Although phones are useful for research, comma, they distract most students. Although opens a door; the sentence has to walk through it."),
 ("pick", "Which sentence is punctuated correctly?", ["As a result students pay more attention.", "As a result, students pay more attention.", "As a result students, pay more attention."], 1,
  "As a result, comma, students pay more attention. The comma comes right after the transition, not in the middle of the sentence."),
 ("pick", "Which one uses although correctly?", ["Although, phones are useful.", "Although phones are useful, they distract students.", "Phones are useful. Although."], 1,
  "Although phones are useful, they distract students. Although opens the sentence, and the sentence finishes the thought."),
 ("clear", "Board wiped. You write two sentences with the signs."),
 ("head", "Your lines · with the signs", "With the signs."),
 ("ask", "Claim: Our school should have a longer lunch. Write reason one. Start with First, with the comma, and give the reason.",
  "First, ... (comma after First)",
  [("has_regex", r"^\s*first,", "First, with a comma right after it."), ("min_words", 7, "A full reason."), ("ends_punct", None, "End punctuation.")],
  "First, students need time to eat without rushing, so they can concentrate in the afternoon.",
  "First, comma. The sign is on the road.", "Start with First, and put the comma right after it."),
 ("ask", "Now the other side. Start with However, with the comma, and say one thing the other side would say.",
  "However, ... (the other side)",
  [("has_regex", r"^\s*however,", "However, with a comma right after it."), ("min_words", 7, "A full sentence."), ("ends_punct", None, "End punctuation.")],
  "However, a longer lunch means the school day ends later, and some students have jobs.",
  "That is the other side, with the comma in the right place. A five-level move.", "However, comma, then what the other side would say."),
 ("say", "Signs on the road, commas after the signs. Lesson five: the compare-and-contrast prompt, where the signs do most of the work."),
 ]},

# ───────────────────────────── 5 ─────────────────────────────
{"id": "w5", "n": 5, "title": "Compare and contrast", "sub": "Both, unlike, while, and a two-paragraph shape", "mins": 9,
 "goal": "I can compare two things with both / unlike / while and organize the answer in two paragraphs.",
 "beats": [
 ("say", "Lesson five. Compare and contrast. The test loves this prompt: compare two things, say how they are alike and how they are different. Students lose points in one way: they describe one thing, then the other, and never compare. The fix is four words."),
 ("head", "Lesson 5 · Compare and contrast", "To the board."),
 ("write", "Alike: **Both** A and B ...   /   A ..., **and** B **also** ...", "To say alike: Both A and B. Or: A does this, and B also does it."),
 ("write", "Different: **Unlike** A, B ...   /   **While** A ..., B ...   /   A ...; **however,** B ...", "To say different: Unlike A, B. While A does this, B does that. Or A does this; however, B does that."),
 ("write", "Prompt: Compare learning online and learning in a classroom.", "Prompt. Compare learning online and learning in a classroom. Watch the shape: paragraph one, alike. Paragraph two, different. Then a sentence that picks."),
 ("write", "¶1  **Both** online classes and classroom classes teach the same material, and **both** give homework. **In addition,** students in both can ask the teacher questions.", "Paragraph one. Both online classes and classroom classes teach the same material, and both give homework. In addition, students in both can ask the teacher questions. Alike, alike, alike. The word both does the comparing for you."),
 ("write", "¶2  **However,** they are different in one important way. **Unlike** a classroom, an online class has no one watching, so students must manage their own time. **While** a classroom teacher sees a confused face, an online teacher only sees a blank screen.", "Paragraph two. However, they are different in one important way. Unlike a classroom, an online class has no one watching, so students must manage their own time. While a classroom teacher sees a confused face, an online teacher only sees a blank screen. Unlike. While. Each sentence holds both things at once. That is comparing."),
 ("write", "Closing: **For these reasons,** a classroom is better for most students, **although** online classes work for students who manage their time well.", "Closing. For these reasons, a classroom is better for most students, although online classes work for students who manage their time well. A pick, and the other side in the same sentence."),
 ("say", "Now listen to the mistake that costs the most. Here is a paragraph that describes but never compares."),
 ("write", "~~Online classes are on a computer. You can do them at home. Classroom classes are at school. There is a teacher. They are different.~~", "Online classes are on a computer. You can do them at home. Classroom classes are at school. There is a teacher. They are different. Five sentences, zero comparing. Not one sentence holds both things. Cross it out."),
 ("pick", "Which sentence actually compares?", ["Online classes are at home.", "Unlike a classroom, an online class has no one watching the students.", "Classroom classes have a teacher in the room."], 1,
  "Unlike a classroom, an online class has no one watching. Both things are in one sentence. That is the test."),
 ("clear", "Board wiped. Your turn. Two things to compare: texting and talking on the phone."),
 ("head", "Your lines · both / unlike", "Both, unlike."),
 ("ask", "Write one sentence that says how texting and talking on the phone are alike. Use both.",
  "Alike → Both texting and talking on the phone ...",
  [("has_regex", r"\bboth\b", "Use the word both."), ("min_words", 7, "A full sentence."), ("ends_punct", None, "End punctuation."), ("starts_upper", None, "Capital letter first.")],
  "Both texting and talking on the phone let people share news in seconds.",
  "Both, and one sentence holds the two things. That is comparing.", "Use both, and put the two things in the same sentence."),
 ("ask", "Now one sentence about how they are different. Use unlike or while.",
  "Different → Unlike ..., ... / While ..., ...",
  [("has_regex", r"\b(unlike|while|whereas)\b", "Use unlike or while."), ("min_words", 8, "A full sentence with both things in it."), ("ends_punct", None, "End punctuation."), ("starts_upper", None, "Capital letter first.")],
  "Unlike a text, a phone call lets you hear if the other person is upset.",
  "Unlike, and both things in one sentence. Good.", "Start with Unlike or While, and keep both things in the sentence."),
 ("say", "Both. Unlike. While. Four words that turn describing into comparing. Lesson six: the email, where the test checks whether you can change your voice."),
 ]},

# ───────────────────────────── 6 ─────────────────────────────
{"id": "w6", "n": 6, "title": "The email", "sub": "Greeting, purpose, request, closing, and the right voice", "mins": 8,
 "goal": "I can write a short formal email with a greeting, a purpose sentence, a specific request and a closing.",
 "beats": [
 ("say", "Lesson six. The email. The test asks for an email or a letter to check one thing: can you change your voice for the reader? The way you text a friend is not the way you write to a principal. The shape is four parts, and the voice is the fifth."),
 ("head", "Lesson 6 · The email", "To the board."),
 ("write", "① Greeting: **Dear Mr. Lopez,** / **Dear Principal Lopez,**", "Part one, the greeting. Dear Mr. Lopez, comma. Or Dear Principal Lopez. Not Hey. Not Hi there."),
 ("write", "② Purpose: **I am writing to ask** ... / **I am writing because** ...", "Part two, the purpose sentence. I am writing to ask. I am writing because. The reader knows why you wrote before the end of line one."),
 ("write", "③ Request + reason: **Could you please** ... ? **This would help because** ...", "Part three, the request, polite and specific, with a reason. Could you please. This would help because."),
 ("write", "④ Closing: **Thank you for your time.** / **Sincerely,** + your name", "Part four, the closing. Thank you for your time. Sincerely, comma, your name."),
 ("write", "Prompt: Write an email to your principal asking for a quiet room to study during lunch.", "Here is the prompt. Write an email to your principal asking for a quiet room to study during lunch. Watch me build it."),
 ("write", "Dear Principal Lopez,\nI am writing to ask for a quiet room where students can study during lunch.", "Dear Principal Lopez, comma. I am writing to ask for a quiet room where students can study during lunch. Greeting, purpose."),
 ("write", "Could you please open the library from 11:30 to 12:15? This would help because many students have no quiet place at home, and the cafeteria is too loud to read.", "Could you please open the library from eleven thirty to twelve fifteen? Specific. This would help because many students have no quiet place at home, and the cafeteria is too loud to read. Request, reason, picture."),
 ("write", "Thank you for your time.\nSincerely,\nAna Torres", "Thank you for your time. Sincerely, Ana Torres. Done. Six lines. A five."),
 ("say", "Now the voice. Listen to the same request in the wrong voice."),
 ("write", "~~hey can u open the library at lunch its so loud in the cafeteria thx~~", "Hey can u open the library at lunch its so loud in the cafeteria thx. Every word is understandable, and it fails, because the voice is wrong for the reader. No capitals, u for you, no greeting, no closing. The test is checking exactly this."),
 ("pick", "Which purpose sentence fits an email to a teacher?", ["yo i need help with the test", "I am writing to ask if you could explain the homework from Tuesday.", "Help me with homework."], 1,
  "I am writing to ask if you could explain the homework from Tuesday. Formal, polite, specific."),
 ("pick", "Which closing fits a formal email?", ["later", "Sincerely, Marcus Reed", "bye bye!!"], 1,
  "Sincerely, comma, Marcus Reed. The name goes on its own line."),
 ("clear", "Board wiped. You write the email, one part at a time."),
 ("head", "Your lines · an email to your coach", "An email to your coach."),
 ("ask", "Prompt: Email your coach to ask if practice can move from 3:00 to 4:00 because of your bus. Write the greeting and the purpose sentence together.",
  "Dear Coach ___, + I am writing to ...",
  [("has_regex", r"^\s*dear\b", "Start with Dear Coach ...,"), ("has_any", ["i am writing", "i'm writing"], "Then the purpose: I am writing to ask ..."), ("has_any", ["practice"], "Say what it is about: practice."), ("min_words", 10, "Greeting plus a full purpose sentence.")],
  "Dear Coach Daniels, I am writing to ask if practice could move from 3:00 to 4:00 on Tuesdays.",
  "Greeting, purpose, specific times. The coach knows the ask in line one.", "Dear Coach, comma, then I am writing to ask, then the practice time."),
 ("ask", "Now the request with its reason. Use Could you please, and This would help because.",
  "Could you please ...? This would help because ...",
  [("has_any", ["could you please", "would you please"], "Ask politely: Could you please ...?"), ("has_any", ["because"], "Give the reason: This would help because ..."), ("min_words", 12, "Request plus reason, at least twelve words."), ("not_regex", r"\bu\b|\bthx\b|\bpls\b", "No texting spelling: write you, thanks, please.")],
  "Could you please start practice at 4:00? This would help because my bus does not arrive until 3:40, and I miss the warm-up every day.",
  "Polite request, a reason, a picture of the problem. That is the body of a five.", "Could you please, then the question. This would help because, then the reason."),
 ("say", "Greeting, purpose, request with reason, closing, and the right voice. Lesson seven is the one that saves the most points: editing like a scorer."),
 ]},

# ───────────────────────────── 7 ─────────────────────────────
{"id": "w7", "n": 7, "title": "Edit like a scorer", "sub": "The five errors that cost the most, and how to catch them", "mins": 9,
 "goal": "I can find and fix the five most common errors in my own writing in two minutes.",
 "beats": [
 ("say", "Lesson seven. Editing. A scorer does not count your mistakes one by one. A scorer asks: does the language get in the way? Five errors get in the way more than any others. Learn to see them, and you fix most of your lost points in two minutes at the end."),
 ("head", "Lesson 7 · Edit like a scorer", "To the board."),
 ("write", "1 · Subject–verb:  ~~Students needs~~ → Students **need**   /   ~~She go~~ → She **goes**", "Error one. Subject and verb. Students needs. Students is plural, so: students need. She go. She is one person, so: she goes. The S moves. One S per pair."),
 ("write", "2 · Run-on:  ~~Phones are useful they are distracting.~~ → Phones are useful**. However,** they are distracting.", "Error two. The run-on. Phones are useful they are distracting. Two sentences glued together. Fix: a period, then a transition. Phones are useful. However, they are distracting."),
 ("write", "3 · Capitals and periods:  ~~in my opinion students should rest~~ → **I**n my opinion, students should rest**.**", "Error three. Capitals and periods. In my opinion students should rest, with no capital and no period. Fix: capital I, comma after the transition, period at the end. Small, but a scorer sees it in every line."),
 ("write", "4 · Tense:  ~~Yesterday I go to the library and study.~~ → Yesterday I **went** to the library and **studied**.", "Error four. Tense. Yesterday I go to the library and study. Yesterday is the past. Went. Studied. When you write a time word, check every verb after it."),
 ("write", "5 · Articles and plurals:  ~~I have idea.~~ → I have **an** idea.   ~~many student~~ → many student**s**", "Error five. Articles and plurals. I have idea. I have an idea. Many student. Many students. If there is a number or many, add the S."),
 ("say", "Now the method. Read your answer backwards, one sentence at a time, last sentence first. Backwards stops your brain from reading what you meant and makes it read what you wrote. For each sentence, ask the five questions: verb matches subject? one idea per sentence? capital and period? tense matches the time word? articles and S? Let's hunt."),
 ("pick", "Find the error: ~~The teachers gives homework every night.~~", ["Run-on", "Subject–verb", "Tense"], 1,
  "Subject verb. Teachers is plural, so teachers give, no S on the verb."),
 ("pick", "Find the error: ~~I like math it is easy for me.~~", ["Run-on", "Articles", "Capital"], 0,
  "Run-on. Two ideas, no stop. I like math. It is easy for me. Or: I like math because it is easy for me."),
 ("pick", "Find the error: ~~Last year we move to Laurel.~~", ["Subject–verb", "Tense", "Plural"], 1,
  "Tense. Last year is the past. Last year we moved to Laurel."),
 ("clear", "Board wiped. Three broken sentences. Fix each one; type the whole corrected sentence."),
 ("head", "Your lines · fix the sentence", "Fix the sentence."),
 ("ask", "Fix it: my brother play soccer every saturday", "Fix: my brother play soccer every saturday",
  [("has_regex", r"\bplays\b", "One brother: plays, with an S."), ("has_regex", r"\bSaturday\b", "Days of the week take a capital: Saturday."), ("starts_upper", None, "Capital M on My."), ("ends_punct", None, "Period at the end.")],
  "My brother plays soccer every Saturday.",
  "Capital, plays with an S, capital Saturday, period. Four fixes in one line.", "Check: capital M, plays with S, capital S on Saturday, a period."),
 ("ask", "Fix it: Phones are useful they help students find information", "Fix: Phones are useful they help students find information",
  [("has_regex", r"useful[.;]|useful\s+because|useful,\s*(and|so)\b", "Stop the run-on: a period after useful, or because, or a comma with and."), ("ends_punct", None, "Period at the end."), ("min_words", 8, "Keep the whole sentence.")],
  "Phones are useful because they help students find information.",
  "The run-on is gone. Period or because: both work.", "Put a period after useful and start a new sentence, or join them with because."),
 ("ask", "Fix it: Yesterday the student go to the office and ask for a new schedule", "Fix: Yesterday the student go to the office and ask for a new schedule",
  [("has_regex", r"\bwent\b", "Yesterday: went."), ("has_regex", r"\basked\b", "Yesterday: asked."), ("ends_punct", None, "Period at the end."), ("starts_upper", None, "Capital first letter.")],
  "Yesterday the student went to the office and asked for a new schedule.",
  "Went, asked. Both verbs follow the time word. That is the habit.", "Yesterday means the past: went, asked. Check both verbs."),
 ("say", "Backwards, one sentence at a time, five questions. Two minutes at the end of every answer. Lesson eight puts it all together on the clock."),
 ]},

# ───────────────────────────── 8 ─────────────────────────────
{"id": "w8", "n": 8, "title": "The timed response", "sub": "Plan 2, write 10, check 2", "mins": 16,
 "goal": "I can plan, write and check a full response in fourteen minutes.",
 "beats": [
 ("say", "Lesson eight. The timed response. Everything from the seven lessons, on the clock. The test gives you limited time, and most students spend all of it writing. A five spends two minutes planning, ten writing, and two checking. Let me show you the plan, because the plan is where the five is decided."),
 ("head", "Lesson 8 · The timed response", "To the board."),
 ("write", "**Plan · 2 min**: claim · reason 1 + example · reason 2 + result · other side · conclusion", "Two minutes. Five words on your paper, one per part. Claim. Reason one and an example. Reason two and a result. The other side. Conclusion. You are not writing sentences yet. You are writing a map."),
 ("write", "**Write · 10 min**: one part per sentence or two · a sign at the start of each", "Ten minutes. One part per sentence or two. A transition at the start of each part. First. Second. However. In conclusion. If you have the map, you never stop to think what comes next."),
 ("write", "**Check · 2 min**: backwards · verb? one idea? capital + period? tense? S?", "Two minutes. Backwards, one sentence at a time. Verb matches? One idea? Capital and period? Tense? Articles and S?"),
 ("write", "Prompt: **Should every student do community service to graduate?** Explain your opinion with reasons.", "Here is the prompt. Should every student do community service to graduate? Explain your opinion with reasons. Watch my two-minute plan."),
 ("write", "Plan: yes · learn skills (ex: hospital volunteers) · helps town (result: parks) · but: jobs/time · yes, 20 hours", "My plan, in twenty seconds. Yes. Reason: learn skills, example, hospital volunteers. Reason: helps the town, result, parks. Other side: some students have jobs and no time. Conclusion: yes, twenty hours. That is the whole map."),
 ("say", "Now your turn, on the clock. I will give you a new prompt. Plan for two minutes in the plan box: five short notes. Then write for ten. Then check for two. The board will keep the time. When you finish, score yourself, and then I'll read you a five and tell you why it is a five."),
 ("clear", "Board wiped. Here is your prompt."),
 ("task", "Your prompt. Should students be required to take a physical education class every year? Explain your opinion with reasons. Plan first. Go.",
  "Prompt: Should students be required to take a physical education class every year? Explain your opinion with reasons.",
  14,
  ["My first sentence answers the question and uses the prompt's words.", "I gave two reasons, each with an example or a result.", "I used transitions: First, Second, However, In conclusion.", "I wrote one sentence about the other side.", "I checked backwards: verbs, run-ons, capitals and periods, tense, S."],
  "In my opinion, students should be required to take a physical education class every year. First, teenagers need to move. For example, in my school, students sit in class for six hours, and PE is the only time many of them run. Second, PE teaches habits that last. As a result, students who learn to exercise at fifteen are more likely to exercise at thirty. However, some students want that period for an extra science or art class, and their choice matters too. In conclusion, every student should take PE each year, but schools should let students choose the activity.",
  "Here is a five. In my opinion, students should be required to take a physical education class every year. First, teenagers need to move. For example, in my school, students sit in class for six hours, and PE is the only time many of them run. Second, PE teaches habits that last. As a result, students who learn to exercise at fifteen are more likely to exercise at thirty. However, some students want that period for an extra science or art class, and their choice matters too. In conclusion, every student should take PE each year, but schools should let students choose the activity. Why is that a five? The claim answers the question with the prompt's words. Two reasons, one with an example you can see, one with a result. Four transitions, each with its comma. The other side in one sentence. A conclusion that repeats the claim in new words and adds something. And not one run-on, not one missing S. Seven sentences. That is the shape. Now you have it."),
 ("say", "That is the Writing Studio. Eight lessons, one shape. Come back to lesson eight with a new prompt every week, and bring your plan box with you to the test. I'll see you at the board."),
 ]},
]

PROMPTS = [   # extra prompts for lesson 8 practice
 "Should schools require uniforms? Explain your opinion with reasons.",
 "Is it better to have a part-time job in high school or to focus only on school? Explain.",
 "Compare living in a small town and living in a big city.",
 "Write an email to your teacher asking to retake a test. Explain why.",
 "Should the school year be longer? Explain your opinion with reasons.",
 "Describe a skill everyone should learn before they finish high school, and explain why.",
]

SAY = [(r"—", ", "), (r"\bPE\b", "P E"), (r"\bELPA21\b", "ELPA twenty-one"), (r"¶", "paragraph "), (r"[①②③④⑤]", ""), (r"\*\*|~~|_", ""),
       (r"\s*/\s*", ". "), (r"→", ", becomes, ")]


def clips():
    """(stem, text) for every line the teacher speaks."""
    out = []
    for L in LESSONS:
        for i, b in enumerate(L["beats"]):
            k = b[0]; st = f"{L['id']}-{i:02d}"
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
