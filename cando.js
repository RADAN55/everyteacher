/* The ELPA21 level descriptors the hub uses everywhere a level is turned into words.
   Plain paraphrases of the ELPA21 proficiency-level descriptors (grades 9–12) as
   Mississippi uses them for the ELPT. Read by read-your-roster.html and
   student-profile.html; edit here, nowhere else.  CAN = what the student can do,
   indexed Level 1–5.  LOOK = what that looks like in a content class. */
window.ELCAN = (function(){
const CAN = {
 L:["understands a few words and set phrases when they come with pictures, gestures or a demonstration",
    "follows one- or two-step directions and simple questions about a familiar topic when you speak slowly and show as you say",
    "follows most of a lesson on a familiar topic and takes simple notes, but loses the thread when the talk is fast, idiomatic or has no visuals",
    "follows a full lesson with few new words, including a discussion with several speakers",
    "understands fast, technical talk — a lecture, a lab briefing, a debate — like any student"],
 S:["answers with one or two words, points, or uses a set phrase to ask for help",
    "asks simple questions and describes with short sentences; needs a frame to go longer",
    "gives an opinion with a reason, retells in order, explains a process in simple sentences",
    "presents and argues a point using academic words, with some errors that do not block meaning",
    "discusses, disagrees, presents and asks precise questions fluently"],
 R:["reads signs, names, numbers and simple words with picture support",
    "reads short, simple sentences about familiar topics; needs written directions read or simplified",
    "reads a page-long text on a familiar topic and answers questions; guesses unknown words from context",
    "reads grade-level text with vocabulary preview or a purpose for reading; finds and cites evidence",
    "reads technical, dense and primary-source text independently"],
 W:["writes name and date, copies from the board, labels pictures and diagrams",
    "writes simple sentences about self and familiar topics; short notes with a frame",
    "writes a paragraph with a topic sentence and details; uses past tense with some errors",
    "writes a multi-paragraph response with evidence and transitions; register and precision still developing",
    "writes research, argument and varied genres with few errors"]
};
const LOOK = {
 L:["Watches what others do before starting. Needs the direction shown, not just said. Silence is processing, not refusal.",
    "Nods, then does the wrong thing — the words were too many. One instruction at a time, checked by asking the student to show you.",
    "Keeps up when there are slides or a diagram; drops off during a ten-minute explanation with none. Notes are thin.",
    "Follows lecture and discussion; may ask you to repeat a technical term or an idiom.",
    "Indistinguishable from classmates in listening."],
 S:["Points, draws or answers in the home language. A bilingual peer or a translation app for understanding unlocks a lot of content.",
    "Will answer a partner before the class. Gives a one-clause answer; 'because…' needs a frame.",
    "Explains to a partner readily; hesitates in whole-class talk. Academic words come slowly and may be replaced with 'thing'.",
    "Presents, argues and asks questions; small grammar slips, correct meaning.",
    "Fully fluent in class talk."],
 R:["Cannot use the textbook, a word problem or a written quiz yet. Labeled diagrams, photos and the real object carry the content.",
    "Reads a short caption, a word problem of one sentence, or a glossary entry with pictures. Grade-level text alone is not readable yet.",
    "Reads the textbook section slowly with the five key words previewed; misses inference, idioms and long sentences.",
    "Reads grade-level text with a purpose; may need help with dense passages, primary sources or figurative language.",
    "Reads anything you assign."],
 W:["Copies. Can label a diagram, fill a table, number steps, draw and caption.",
    "Writes one to three simple sentences with a frame and a word bank; lists; short answers.",
    "Writes a paragraph with an organizer; errors in tense and word form that do not hide the idea.",
    "Writes the essay or the lab report; needs feedback on precision, transitions and formal register.",
    "Writes like any grade-level student; still benefits from writing feedback."]
};
return {CAN:CAN, LOOK:LOOK, DN:{L:"Listening",S:"Speaking",R:"Reading",W:"Writing"}};
})();
