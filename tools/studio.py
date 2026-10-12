#!/usr/bin/env python3
"""ELPA21 Listening & Speaking Studio — content.

Four units. Each unit has three listening tasks in the ELPA21 formats
(Listen and Match, Short Conversation, Academic Lecture) and two speaking
tasks (Observe and Report / Give the Steps / Classroom Chat / Opinion).

Voices (Kokoro speaker ids): T = teacher/narrator (af_bella), M = narrator
(am_michael), A = student voice 1 (af_sarah), B = student voice 2 (am_adam),
C = adult voice 2 (bm_george).

Everything a student hears is synthesized; the page says so. Scripts are
written to be read twice at a natural pace. Lecture facts are kept to what
is stable and uncontested.
"""

VOICES = {"T": 1, "M": 6, "A": 3, "B": 5, "C": 9}

PIES = [
    {"t": "Pecan pie", "img": "img/pie-pecan.jpg"},
    {"t": "Lemon icebox pie", "img": "img/pie-lemon.jpg"},
    {"t": "Sweet potato pie", "img": "img/pie-sweetpotato.jpg"},
    {"t": "Coconut cream pie", "img": "img/pie-coconut.jpg"},
    {"t": "Buttermilk pie", "img": "img/pie-buttermilk.jpg"},
    {"t": "Chess pie", "img": "img/pie-chess.jpg"},
]

UNITS = [
# ───────────────────────────────── 1 · PIES ─────────────────────────────────
{"id": "pies", "n": 1, "title": "Six Southern pies", "sub": "Food · describing · comparing · a recipe",
 "img": "img/six-pies.jpg", "words": ["ingredient", "crust", "filling", "bake", "slice", "topping", "custard"],
 "listen": [
  {"id": "u1a", "type": "match", "title": "Listen and match", "voice": "T",
   "intro": "I will describe a pie. Choose the pie.", "options": PIES,
   "items": [
    {"say": "This pie is made with nuts. The top is brown and sticky because of the corn syrup.", "ans": 0,
     "why": "Nuts and corn syrup on top: that is pecan pie."},
    {"say": "This pie has a white topping and a yellow filling. The topping is whipped cream, and there is lemon zest on top. The crust is made of graham crackers.", "ans": 1,
     "why": "Lemon zest and a graham-cracker crust: lemon icebox pie."},
    {"say": "This pie is orange. It is made with a vegetable, brown sugar and cinnamon.", "ans": 2,
     "why": "The orange vegetable is the sweet potato."},
    {"say": "The top of this pie is covered with white cream and toasted coconut. The filling is thick and creamy.", "ans": 3,
     "why": "Toasted coconut on cream: coconut cream pie."},
   ]},
  {"id": "u1b", "type": "conv", "title": "Short conversation", "setting": "Two students plan a bake sale.",
   "turns": [
    ("A", "We need two pies for the bake sale on Friday. I was thinking pecan pie. Everybody loves it."),
    ("B", "Pecan is good, but pecans are expensive right now. Buttermilk pie costs almost nothing. It's just buttermilk, sugar, eggs and butter."),
    ("A", "True. But people don't always know what buttermilk pie is. Pecan sells itself."),
    ("B", "Then let's do one of each."),
    ("A", "Deal. I'll buy the pecans tonight. Can you make the buttermilk pie Thursday after school?"),
    ("B", "Sure. It only takes an hour."),
   ],
   "names": {"A": "Maya", "B": "Daniel"},
   "qs": [
    {"q": "What are Maya and Daniel planning for?", "options": ["A birthday party", "A bake sale on Friday", "A science fair", "A family dinner"], "ans": 1,
     "why": "Maya says, “We need two pies for the bake sale on Friday.”"},
    {"q": "Why does Daniel suggest buttermilk pie?", "options": ["It is his favorite.", "It is cheap to make.", "It is the fastest.", "Everybody knows it."], "ans": 1,
     "why": "“Buttermilk pie costs almost nothing.”"},
    {"q": "What do they decide?", "options": ["Two pecan pies", "Two buttermilk pies", "One of each", "No pies"], "ans": 2,
     "why": "Daniel says, “Then let's do one of each,” and Maya says, “Deal.”"},
    {"q": "When will Daniel make his pie?", "options": ["Tonight", "Friday morning", "Thursday after school", "Next week"], "ans": 2,
     "why": "Maya asks him to make it Thursday after school, and he agrees."},
   ]},
  {"id": "u1c", "type": "lecture", "title": "Academic lecture", "voice": "M", "setting": "A food-science teacher explains custard pies.",
   "text": "Three of these pies, buttermilk, chess and sweet potato, are called custard pies. A custard is a mixture of eggs, sugar and milk or cream. When you bake a custard, the proteins in the eggs change shape and link together. That is what turns a liquid into a soft solid. If the oven is too hot, the proteins tighten too much, and the pie cracks or turns watery. So custard pies are usually baked at a moderate temperature, and the center should still move a little, the cooks say it should jiggle, when you take the pie out. It finishes setting as it cools.",
   "qs": [
    {"q": "What is a custard?", "options": ["A kind of crust", "A mixture of eggs, sugar and milk or cream", "A fruit filling", "A type of oven"], "ans": 1,
     "why": "“A custard is a mixture of eggs, sugar and milk or cream.”"},
    {"q": "What turns the liquid into a soft solid?", "options": ["The sugar melts.", "The crust absorbs the liquid.", "Egg proteins link together.", "The milk evaporates."], "ans": 2,
     "why": "The proteins in the eggs change shape and link together."},
    {"q": "What happens if the oven is too hot?", "options": ["The pie cracks or turns watery.", "The pie does not cook.", "The crust stays raw.", "The sugar disappears."], "ans": 0,
     "why": "“The proteins tighten too much, and the pie cracks or turns watery.”"},
    {"q": "How do cooks know the pie is ready to come out?", "options": ["The center is hard.", "The center still moves a little.", "The top is black.", "It smells sweet."], "ans": 1,
     "why": "The center should still jiggle; it finishes setting as it cools."},
   ]},
 ],
 "speak": [
  {"id": "u1s1", "type": "report", "title": "Observe and report", "secs": 45, "img": "img/pie-coconut.jpg",
   "prompt": "Look at the picture. Describe the pie. What do you see? What is it made of? What does it look like?",
   "frames": {"n": "I see ___. It is ___ (white / brown / round).", "e": "I see a ___ pie. It has ___ on top. It looks ___.",
              "p": "I see a ___ pie. It has ___ and ___. It looks ___ because ___.", "c": "Describe the pie, then compare it with one other pie: Unlike the ___, this pie ___."},
   "check": ["I named the pie or two things I see.", "I used a color, shape or texture word.", "I spoke in full sentences."],
   "model": "I see a coconut cream pie. It is round, and the top is white. There is cream on top, and there are small pieces of toasted coconut. The filling looks thick and creamy. Unlike the pecan pie, this pie is not baked with nuts. It looks sweet and soft.", "mvoice": "A"},
  {"id": "u1s2", "type": "opinion", "title": "Opinion", "secs": 60,
   "prompt": "The cafeteria will serve one pie at the Thanksgiving lunch. Which pie should it serve? Give two reasons.",
   "frames": {"n": "I like ___ pie.", "e": "The cafeteria should serve ___ pie because ___.",
              "p": "In my opinion, the cafeteria should serve ___ because ___ and ___. First, ___. Second, ___.", "c": "State your opinion with two reasons, then answer the other side: Some people might say ___; however, ___."},
   "check": ["I said which pie.", "I gave two reasons.", "I used because."],
   "model": "In my opinion, the cafeteria should serve sweet potato pie. First, it is traditional in the South, so many families already know it. Second, it costs less than pecan pie because sweet potatoes are cheap. Some people might say pecan pie is more popular; however, some students are allergic to nuts, so sweet potato pie is safer for everyone.", "mvoice": "B"},
 ]},

# ───────────────────────────────── 2 · SCHOOL ─────────────────────────────────
{"id": "school", "n": 2, "title": "First week at a new school", "sub": "School life · people and places · a schedule",
 "img": "", "words": ["counselor", "schedule", "credit", "semester", "tryouts", "form"],
 "listen": [
  {"id": "u2a", "type": "match", "title": "Listen and match", "voice": "T",
   "intro": "I will describe a place or a person at school. Choose the one I describe.",
   "options": [{"t": "The counselor", "ic": "🧑‍💼"}, {"t": "The nurse's office", "ic": "🩹"}, {"t": "The cafeteria", "ic": "🍽️"}, {"t": "The library", "ic": "📚"}],
   "items": [
    {"say": "This person helps you choose your classes and plan for graduation. You can also talk to this person when you have a problem.", "ans": 0,
     "why": "Choosing classes and planning for graduation is the counselor's job."},
    {"say": "You go here when you do not feel well. There is a bed, a first-aid kit, and someone who can call your family.", "ans": 1,
     "why": "A bed and a first-aid kit: the nurse's office."},
    {"say": "This is where you eat lunch. You can buy food with your lunch number or bring food from home.", "ans": 2,
     "why": "Lunch and a lunch number: the cafeteria."},
    {"say": "You can borrow books here and use a computer. Please speak quietly.", "ans": 3,
     "why": "Books, computers and quiet: the library."},
   ]},
  {"id": "u2b", "type": "conv", "title": "Short conversation", "setting": "A new student talks with the school counselor.",
   "turns": [
    ("B", "Excuse me, Ms. Park. I think there is a mistake on my schedule. I have math in second period and math again in fifth period."),
    ("T", "Let me look. You're right, Luis, that's a mistake. Fifth period should be biology. I'll fix it and print you a new schedule."),
    ("B", "Thank you. Also, I don't have a lunch number yet."),
    ("T", "The cafeteria will give you one today. Just tell them your name. One more thing: did you want to try out for soccer?"),
    ("B", "Yes! When are tryouts?"),
    ("T", "Thursday after school, on the field. You need a physical form signed by a doctor. Bring it to the coach."),
    ("B", "Thursday. I'll bring the form. Thank you, Ms. Park."),
   ],
   "names": {"B": "Luis", "T": "Ms. Park"},
   "qs": [
    {"q": "What is wrong with Luis's schedule?", "options": ["He has no lunch.", "He has two math classes.", "He has no biology teacher.", "It has the wrong name."], "ans": 1,
     "why": "“I have math in second period and math again in fifth period.”"},
    {"q": "What will Ms. Park do?", "options": ["Call his parents", "Move him to another school", "Fix the schedule and print a new one", "Give him a lunch number"], "ans": 2,
     "why": "“I'll fix it and print you a new schedule.”"},
    {"q": "When are soccer tryouts?", "options": ["Today at lunch", "Thursday after school", "Friday morning", "Next week"], "ans": 1,
     "why": "“Thursday after school, on the field.”"},
    {"q": "What does Luis need for tryouts?", "options": ["A new schedule", "A lunch number", "A physical form signed by a doctor", "A library card"], "ans": 2,
     "why": "“You need a physical form signed by a doctor.”"},
   ]},
  {"id": "u2c", "type": "lecture", "title": "Academic lecture", "voice": "T", "setting": "A counselor explains how high-school credits work.",
   "text": "In an American high school, you graduate by earning credits. A credit is what you receive when you pass a class. A class that lasts the whole year is usually worth one credit. A class that lasts one semester, half of the year, is usually worth half a credit. To graduate, you need a certain number of credits in English, math, science and social studies, plus some electives, which are classes you choose. Each state sets its own total, and your counselor knows the number for your school. Credits add up over four years. If you fail a class, you do not lose the credits you already have, but you must earn that credit again, often in summer school or by repeating the class. The counselor checks your credits every year, so ask to see your list.",
   "qs": [
    {"q": "What is a credit?", "options": ["A grade on a test", "What you receive when you pass a class", "A kind of elective", "A letter from the school"], "ans": 1,
     "why": "“A credit is what you receive when you pass a class.”"},
    {"q": "How much is a one-semester class usually worth?", "options": ["One credit", "Two credits", "Half a credit", "No credit"], "ans": 2,
     "why": "A semester class is usually worth half a credit; a year-long class, one."},
    {"q": "What is an elective?", "options": ["A required class", "A class you choose", "A summer class", "A test"], "ans": 1,
     "why": "“Electives, which are classes you choose.”"},
    {"q": "What happens if you fail a class?", "options": ["You lose all your credits.", "You cannot graduate.", "You must earn that credit again.", "Nothing happens."], "ans": 2,
     "why": "You keep the credits you have, but you must earn the missing credit again."},
   ]},
 ],
 "speak": [
  {"id": "u2s1", "type": "steps", "title": "Give the steps", "secs": 45,
   "prompt": "A new student does not know how to get lunch in the cafeteria. Tell the student what to do, step by step. Use first, then, next and finally.",
   "frames": {"n": "First, ___. Then, ___.", "e": "First, get in line. Then, ___. Next, ___. Finally, ___.",
              "p": "First, ___. Then, ___. Next, ___. Finally, ___. Remember to ___.", "c": "Give four or more steps, and add one tip a new student would not know."},
   "check": ["I gave at least three steps.", "I used two sequence words (first, then, next, finally).", "The steps are in order."],
   "model": "First, get in the lunch line with your class. Then, pick up a tray and choose your food. Next, tell the cashier your lunch number. Finally, find a seat and eat. One tip: if you forget your number, tell them your name, and they can look it up.", "mvoice": "A"},
  {"id": "u2s2", "type": "chat", "title": "Classroom chat", "secs": 45,
   "prompt": "Your teacher asks: What is one class you like this year, and why do you like it?",
   "frames": {"n": "I like ___.", "e": "I like ___ class because ___.",
              "p": "My favorite class is ___ because ___. For example, ___.", "c": "Name the class, give two reasons, and say what you want to learn next."},
   "check": ["I named a class.", "I gave a reason with because.", "I added one example or detail."],
   "model": "My favorite class this year is biology, because we do experiments, not only reading. For example, last week we looked at onion cells under a microscope. I also like it because the teacher explains words with pictures. Next, I want to learn about the human body.", "mvoice": "B"},
 ]},

# ───────────────────────────────── 3 · STORMS ─────────────────────────────────
{"id": "storms", "n": 3, "title": "Storms over the Gulf", "sub": "Science · weather · cause and effect",
 "img": "", "words": ["hurricane", "evaporate", "rotation", "category", "warning", "sustained winds"],
 "listen": [
  {"id": "u3a", "type": "match", "title": "Listen and match", "voice": "M",
   "intro": "I will describe a kind of weather. Choose the one I describe.",
   "options": [{"t": "Hurricane", "ic": "🌀"}, {"t": "Tornado", "ic": "🌪️"}, {"t": "Thunderstorm", "ic": "⛈️"}, {"t": "Flood", "ic": "🌊"}],
   "items": [
    {"say": "This storm forms over warm ocean water. Its strong winds spin around a calm center called the eye. It can be hundreds of miles wide.", "ans": 0,
     "why": "Warm ocean water, a calm eye, hundreds of miles wide: a hurricane."},
    {"say": "This is a spinning column of air that reaches from a cloud down to the ground. It is narrow, and it usually lasts only a few minutes.", "ans": 1,
     "why": "A narrow spinning column from cloud to ground: a tornado."},
    {"say": "This brings thunder, lightning and heavy rain. It usually lasts less than an hour.", "ans": 2,
     "why": "Thunder and lightning: a thunderstorm."},
    {"say": "This happens when water covers land that is usually dry. It often follows days of heavy rain.", "ans": 3,
     "why": "Water covering dry land: a flood."},
   ]},
  {"id": "u3b", "type": "conv", "title": "Short conversation", "setting": "Two students divide the work on a science project.",
   "turns": [
    ("A", "Our hurricane project is due Monday. How should we split it up?"),
    ("B", "I can make the slides. Can you make the chart of the five categories?"),
    ("A", "Sure. I'll put the wind speed for each category and one example storm."),
    ("B", "Good idea. Where did you find the wind speeds?"),
    ("A", "On the National Hurricane Center website. I'll send you the link."),
    ("B", "Great. Let's meet Friday at lunch in the library to put it together."),
    ("A", "Friday at lunch. I'll bring my laptop."),
   ],
   "names": {"A": "Ana", "B": "Marcus"},
   "qs": [
    {"q": "When is the project due?", "options": ["Friday", "Monday", "Today", "Next month"], "ans": 1,
     "why": "“Our hurricane project is due Monday.”"},
    {"q": "What will Ana make?", "options": ["The slides", "A chart of the five categories", "A video", "A poster of the eye"], "ans": 1,
     "why": "Marcus asks her to make the chart, and she agrees."},
    {"q": "Where did Ana find the wind speeds?", "options": ["In a textbook", "From the teacher", "On the National Hurricane Center website", "On the news"], "ans": 2,
     "why": "“On the National Hurricane Center website.”"},
    {"q": "When and where will they meet?", "options": ["Monday in class", "Friday at lunch in the library", "Thursday after school", "Saturday at home"], "ans": 1,
     "why": "“Let's meet Friday at lunch in the library.”"},
   ]},
  {"id": "u3c", "type": "lecture", "title": "Academic lecture", "voice": "M", "setting": "An earth-science teacher explains how a hurricane forms.",
   "text": "A hurricane needs one thing above all: warm ocean water. When the surface of the sea is about eighty degrees Fahrenheit or warmer, water evaporates quickly. Warm, wet air rises, cools, and forms clouds and thunderstorms. More air rushes in from the sides to replace the air that rose, and the rotation of the Earth makes this moving air spin. In the Northern Hemisphere, it spins counterclockwise. When the sustained winds reach seventy-four miles per hour, the storm is called a hurricane. Scientists rate hurricanes from category one to category five by wind speed. When a hurricane moves over land, it loses its fuel, the warm water, so it weakens. But it can still bring heavy rain and flooding far from the coast.",
   "qs": [
    {"q": "What does a hurricane need above all?", "options": ["Cold air", "Warm ocean water", "Mountains", "Dry land"], "ans": 1,
     "why": "“A hurricane needs one thing above all: warm ocean water.”"},
    {"q": "What makes the moving air spin?", "options": ["The rotation of the Earth", "The moon", "The clouds", "The heat of the sun"], "ans": 0,
     "why": "“The rotation of the Earth makes this moving air spin.”"},
    {"q": "When is a storm called a hurricane?", "options": ["When it reaches land", "When it rains for a day", "When sustained winds reach 74 miles per hour", "When it has an eye"], "ans": 2,
     "why": "The 74-mile-per-hour line is what makes a storm a hurricane."},
    {"q": "Why does a hurricane weaken over land?", "options": ["The wind stops.", "It loses its fuel, the warm water.", "Buildings block it.", "It gets too cold."], "ans": 1,
     "why": "“It loses its fuel, the warm water, so it weakens.”"},
   ]},
 ],
 "speak": [
  {"id": "u3s1", "type": "steps", "title": "Give the steps", "secs": 45,
   "prompt": "A hurricane warning is on the news. Tell your family what to do at home to get ready, step by step.",
   "frames": {"n": "First, ___. Then, ___.", "e": "First, ___. Then, ___. Next, ___. Finally, ___.",
              "p": "First, we should ___ because ___. Then, ___. Next, ___. Finally, ___.", "c": "Give four steps in order and explain the reason for the most important one."},
   "check": ["I gave at least three steps.", "I used two sequence words.", "I explained one step with because."],
   "model": "First, we should fill bottles with water and charge our phones, because the power may go out. Then, bring the chairs and the trash can inside so the wind does not take them. Next, put important papers in a plastic bag. Finally, listen to the radio and stay away from the windows.", "mvoice": "B"},
  {"id": "u3s2", "type": "opinion", "title": "Opinion", "secs": 60,
   "prompt": "Should schools close when a hurricane warning is issued, even if the storm might not come? Give two reasons.",
   "frames": {"n": "Yes / No. Schools should ___.", "e": "I think schools should ___ because ___.",
              "p": "In my opinion, schools should ___ because ___ and ___.", "c": "Give two reasons, then answer the other side with however."},
   "check": ["I said yes or no clearly.", "I gave two reasons.", "I used because or however."],
   "model": "In my opinion, schools should close when there is a hurricane warning. First, buses and cars are not safe in strong wind and heavy rain. Second, families need time to get ready and to leave if they must. Some people might say we lose a day of learning; however, the school can add a day later, and no one can replace a student who is hurt.", "mvoice": "A"},
 ]},

# ───────────────────────────────── 4 · GOVERNMENT ─────────────────────────────────
{"id": "gov", "n": 4, "title": "Three branches", "sub": "Civics · how government works · an argument",
 "img": "", "words": ["branch", "legislative", "executive", "judicial", "veto", "unconstitutional"],
 "listen": [
  {"id": "u4a", "type": "match", "title": "Listen and match", "voice": "T",
   "intro": "I will describe a part of the United States government. Choose the one I describe.",
   "options": [{"t": "The legislative branch (Congress)", "ic": "🏛️"}, {"t": "The executive branch (the President)", "ic": "🖋️"}, {"t": "The judicial branch (the courts)", "ic": "⚖️"}, {"t": "The Constitution", "ic": "📜"}],
   "items": [
    {"say": "This branch makes the laws. It has two parts: the Senate and the House of Representatives. Together they are called Congress.", "ans": 0,
     "why": "The Senate and the House make laws: the legislative branch."},
    {"say": "This branch carries out the laws. The President leads it, with the help of many departments.", "ans": 1,
     "why": "Carrying out laws, led by the President: the executive branch."},
    {"say": "This branch decides what the laws mean and whether they follow the Constitution. Its highest court is the Supreme Court.", "ans": 2,
     "why": "Courts and the Supreme Court: the judicial branch."},
    {"say": "This document is the plan for the whole government. It begins with the words 'We the People.'", "ans": 3,
     "why": "“We the People” opens the Constitution."},
   ]},
  {"id": "u4b", "type": "conv", "title": "Short conversation", "setting": "A student who was absent talks with his civics teacher.",
   "turns": [
    ("B", "Ms. Rivera, I was absent yesterday. Did I miss anything important?"),
    ("T", "You did, Jamal. We reviewed the three branches, and the test is on Tuesday."),
    ("B", "Tuesday. Is there a way to catch up?"),
    ("T", "Yes. I'm offering tutoring Monday at three-fifteen, here in room two-oh-four. Bring your notes."),
    ("B", "I'll be there. Is the study guide on the class website?"),
    ("T", "It is. Do the practice questions before Monday, and we'll go over the ones you miss."),
    ("B", "Thank you, Ms. Rivera."),
   ],
   "names": {"B": "Jamal", "T": "Ms. Rivera"},
   "qs": [
    {"q": "Why did Jamal miss the review?", "options": ["He was late.", "He was absent.", "He was in another class.", "He forgot."], "ans": 1,
     "why": "“I was absent yesterday.”"},
    {"q": "When is the test?", "options": ["Monday", "Tuesday", "Friday", "Today"], "ans": 1,
     "why": "“The test is on Tuesday.”"},
    {"q": "When and where is tutoring?", "options": ["Monday at 3:15 in room 204", "Tuesday at lunch", "Monday morning in the library", "After the test"], "ans": 0,
     "why": "“Monday at three-fifteen, here in room two-oh-four.”"},
    {"q": "What should Jamal do before Monday?", "options": ["Take the test", "Do the practice questions on the study guide", "Write an essay", "Bring a form"], "ans": 1,
     "why": "“Do the practice questions before Monday.”"},
   ]},
  {"id": "u4c", "type": "lecture", "title": "Academic lecture", "voice": "C", "setting": "A civics teacher explains checks and balances.",
   "text": "The United States Constitution divides the government into three branches so that no one branch has all the power. Each branch can limit, or check, the others. Here is how it works. Congress, the legislative branch, passes a bill. The President, the executive branch, can sign it into law or veto it, which means to refuse it. But Congress can override a veto if two-thirds of both the House and the Senate vote for the bill again. The courts, the judicial branch, can decide that a law is unconstitutional, which means it goes against the Constitution, and then the law cannot be enforced. The President appoints federal judges, but the Senate must approve them. This system is called checks and balances. It is slow on purpose. The people who wrote the Constitution wanted big decisions to need agreement from more than one branch.",
   "qs": [
    {"q": "Why is the government divided into three branches?", "options": ["To make laws faster", "So that no one branch has all the power", "To save money", "Because there are three states"], "ans": 1,
     "why": "“So that no one branch has all the power.”"},
    {"q": "What does veto mean?", "options": ["To sign a law", "To refuse a bill", "To vote twice", "To write a bill"], "ans": 1,
     "why": "“Veto it, which means to refuse it.”"},
    {"q": "How can Congress override a veto?", "options": ["With a letter to the President", "If two-thirds of both houses vote for the bill again", "By asking the Supreme Court", "It cannot."], "ans": 1,
     "why": "Two-thirds of both the House and the Senate must vote for the bill again."},
    {"q": "What can the courts decide about a law?", "options": ["That it is unconstitutional", "That it needs more votes", "That the President must sign it", "That it costs too much"], "ans": 0,
     "why": "The courts can decide a law is unconstitutional, and then it cannot be enforced."},
   ]},
 ],
 "speak": [
  {"id": "u4s1", "type": "chat", "title": "Classroom chat", "secs": 45,
   "prompt": "Your teacher asks: If you could work in one branch of government, which one would you choose, and why?",
   "frames": {"n": "I would choose ___.", "e": "I would choose the ___ branch because ___.",
              "p": "I would choose the ___ branch because ___. In that job, I would ___.", "c": "Choose a branch, give two reasons, and say one problem you would want to work on."},
   "check": ["I named a branch.", "I gave a reason with because.", "I said what I would do in that job."],
   "model": "I would choose the legislative branch, because I like to listen to people and solve problems. In Congress, I would write laws about schools, because I know what students need. For example, I would want every new student to have a counselor who speaks their language.", "mvoice": "A"},
  {"id": "u4s2", "type": "opinion", "title": "Opinion", "secs": 60,
   "prompt": "Some people think the voting age should be lowered from 18 to 16. Do you agree or disagree? Give two reasons.",
   "frames": {"n": "I agree / I disagree.", "e": "I think the voting age should ___ because ___.",
              "p": "In my opinion, the voting age should ___ because ___ and ___.", "c": "Take a side with two reasons, then answer the strongest argument against you."},
   "check": ["I said agree or disagree.", "I gave two reasons.", "I answered the other side with however (Progressing / Challenge)."],
   "model": "I disagree. In my opinion, the voting age should stay at eighteen. First, at eighteen most people have finished high school and have studied government. Second, many laws, like signing a contract, also start at eighteen, so the rules match. Some people might say sixteen-year-olds pay taxes when they work; however, they can still speak at school board meetings and write to their representatives.", "mvoice": "B"},
 ]},
]

SAY = [
    (r"\bELPA21\b", "ELPA twenty-one"), (r"\b74\b", "seventy-four"), (r"—", ", "),
    (r"\bMs\. ", "Miz "), (r"\bU\.S\.", "U S"),
]


def clips():
    """Every audio clip the page needs: (file stem, [(voice, text), ...])."""
    out = []
    for u in UNITS:
        for L in u["listen"]:
            if L["type"] == "match":
                out.append((f"{L['id']}-intro", [(L["voice"], L["intro"])]))
                for i, it in enumerate(L["items"]):
                    out.append((f"{L['id']}-{i+1}", [(L["voice"], it["say"])]))
            elif L["type"] == "conv":
                out.append((L["id"], list(L["turns"])))
            else:
                out.append((L["id"], [(L["voice"], L["text"])]))
        for S in u["speak"]:
            out.append((f"{S['id']}-prompt", [("T", S["prompt"])]))
            out.append((f"{S['id']}-model", [(S["mvoice"], S["model"])]))
    return out


if __name__ == "__main__":
    c = clips()
    print(len(UNITS), "units;", len(c), "clips;",
          sum(len(L["items"]) if L["type"] == "match" else len(L["qs"]) for u in UNITS for L in u["listen"]), "listening items;",
          sum(len(u["speak"]) for u in UNITS), "speaking tasks")
