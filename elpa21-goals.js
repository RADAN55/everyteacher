/* ELPA21 goal bank — for the LSP Builder.

   Four domains × five levels × four goals. Each goal is tied to one of the ten
   ELP Standards (std) and written to be measured: a behavior, the condition it
   happens under, and how progress is shown (ev). The level descriptions follow
   the ELPA21 achievement levels: 1 words and phrases with support · 2 short
   sentences on familiar topics · 3 expanded sentences, errors do not impede ·
   4 grade-appropriate with support · 5 independent, minimal errors.

   Edit freely. Keep each goal one sentence; keep "by the spring ELPT" or a
   date in it so it stays a target and not a wish.

   Evidence (ev) is written to be realistic for a teacher with a full load:
   it names the instrument, how often (mostly every other week, monthly or
   per nine weeks — weekly only for one-minute probes), where it is kept
   (folder, tracker, recording), and what counts as progress from a
   baseline. Wherever possible it uses something that already exists — the
   department rubric, the content teacher's own quiz, a phone voice memo —
   rather than a new assessment.

   ELP Standards: 1 construct meaning · 2 participate in exchanges · 3 speak
   and write about texts · 4 claims with evidence · 5 research · 6 analyze
   arguments · 7 adapt language to audience · 8 word meaning · 9 clear and
   coherent speech/text · 10 standard English. */
window.ELPA21_GOALS = {
L: {
 1: [
  {std:1, g:"Follow one- and two-step classroom directions given with gestures or a model, correctly in 4 of 5 checks by the spring ELPT.", ev:"Once a week during a normal lesson, the EL teacher gives five one- or two-step directions and tallies correct/incorrect on a sticky note in the student folder. Baseline the first week; progress is the tally moving from 2/5 toward 4/5 by the nine-weeks review."},
  {std:1, g:"Point to or pick the picture that matches a word or short phrase the teacher says, in 8 of 10 trials by January.", ev:"Ten picture cards from the week's vocabulary, teacher says the word, student points; scored every other week, two minutes, recorded as x/10 on the First 100 Words tracker. Progress is three checks in a row at 8/10 or better."},
  {std:8, g:"Show understanding of 50 high-frequency school words heard in context (schedule, materials, routines) by responding correctly 80% of the time.", ev:"The First 100 Words tracker, marked once a month: the teacher reads 20 words in a sentence each and the student shows meaning (points, acts, picks). Progress is the running total of words mastered, graphed on the tracker."},
  {std:2, g:"Respond to yes/no and either/or questions about a lesson with a gesture, word or short phrase in 4 of 5 opportunities.", ev:"During one lesson a week the EL teacher asks five yes/no or either/or questions and tallies responses. Keep the five slips per nine weeks; progress is the ratio rising and the responses moving from gestures to words."},
 ],
 2: [
  {std:1, g:"Identify the topic and one key detail of a short teacher explanation on a familiar subject, with visual support, in 4 of 5 checks by the spring ELPT.", ev:"A two-question exit ticket after one mini-lesson a week — 'What was it about?' and 'Tell one thing you heard' — answered in words or a drawing. File the tickets; progress is correct topic in 4 of the last 5 tickets."},
  {std:1, g:"Follow multi-step oral directions for a classroom task without a model, correctly in 4 of 5 checks by March.", ev:"Every other week, a three-step task without a model ('get your notebook, write the date, underline the title'), scored right/wrong on a dated checklist. Progress is four consecutive correct checks."},
  {std:2, g:"Understand and answer simple wh- questions (who, what, where, when) about a lesson or a classmate's statement in 4 of 5 opportunities.", ev:"Once a week the teacher sits in on partner talk for two minutes and scores wh- question responses 0 (no response), 1 (partly right), 2 (right) on a clipboard sheet. Progress is the average moving above 1.5 for a month."},
  {std:8, g:"Recognize 100 academic and content words when heard in a sentence, scoring 80% on a listening vocabulary check by January.", ev:"A 20-item listening vocabulary check once a month, built from that month's content words: teacher reads a sentence, student picks the picture or definition. Recorded as a percentage; progress is 60% → 80% across the semester."},
 ],
 3: [
  {std:1, g:"Identify the main idea and two supporting details of a grade-level read-aloud or short video on a familiar academic topic, without visual support, in 4 of 5 checks.", ev:"Every other week, a main-idea-and-two-details organizer completed after a grade-level read-aloud or a 5-minute video, scored 0–3 against the teacher's key. Progress is a 3 in three of the last four."},
  {std:1, g:"Take notes on key points of a 10-minute lesson using a partially completed guide, capturing at least 70% of the targeted points by the spring ELPT.", ev:"Once a month, guided notes from a 10-minute content lesson compared against a key of ten targeted points; record the percentage captured. Progress is 50% → 70% by the spring ELPT."},
  {std:6, g:"Tell whether a speaker is giving a fact, an opinion or a reason in short oral statements, 8 of 10 correct by March.", ev:"A ten-item oral sort once a month: the teacher reads statements, the student marks fact, opinion or reason. Score kept as x/10 in the folder; progress is 8/10 twice in a row."},
  {std:2, g:"Follow a small-group discussion and respond to a classmate's idea appropriately in 3 of 4 structured talks.", ev:"During structured small-group talks, every other week, a four-box checklist: followed the thread, responded to a peer, response fit, needed a prompt. Progress is 3 of 4 boxes in three of the last four talks."},
 ],
 4: [
  {std:1, g:"Determine the central idea and how details support it in a grade-level lecture, podcast or video, scoring 3 of 4 on a listening rubric by the spring ELPT.", ev:"Every other week, a listening task from the content class (lecture clip, podcast segment) with a written central-idea response, scored on the 4-point rubric the ELA department already uses. Progress is a 3 in three of the last four."},
  {std:6, g:"Identify a speaker's claim and one piece of evidence or reasoning in a grade-level oral argument, in 4 of 5 checks.", ev:"Once a month, a claim-and-evidence organizer completed while listening to a short grade-level argument (debate clip, persuasive speech), scored right/wrong for claim and for one piece of evidence. Progress is both right in 4 of 5."},
  {std:1, g:"Take independent notes on a full-period content lesson that capture the main points and key vocabulary, usable for a quiz, in 3 of 4 lessons.", ev:"Once a month the content teacher photographs the student's notes from a full lesson and rates them 1–3 for main points and vocabulary. Progress is a 3 in three of the last four, and the student using the notes on a quiz."},
  {std:8, g:"Infer the meaning of unfamiliar academic words from spoken context and confirm them, 8 of 10 correct by March.", ev:"A monthly ten-item check: the teacher reads a sentence with one unfamiliar academic word, the student says what it probably means and why. Scored x/10; progress is 6/10 → 8/10."},
 ],
 5: [
  {std:1, g:"Comprehend fast-paced grade-level discussion, lectures and media without subtitles, scoring at the grade-level benchmark on listening tasks by the spring ELPT.", ev:"The content teacher's own listening-dependent assessments (quiz after lecture, video response), reported quarterly as a percentage. Progress is scores at or above the class median for two consecutive quarters."},
  {std:6, g:"Evaluate a speaker's reasoning and identify when evidence does not support a claim, in 4 of 5 analyzed arguments.", ev:"Once a month, an argument-analysis task on a grade-level recording: identify the claim, the evidence, and one weakness. Scored on a 4-point rubric; progress is a 3 or 4 in four of five."},
  {std:7, g:"Recognize shifts in register, tone and purpose (sarcasm, formality, persuasion) in oral language, 8 of 10 correct.", ev:"A ten-item register task each quarter: short clips, the student names the tone or purpose. Progress is 8/10 or better for two quarters."},
  {std:1, g:"Maintain Level 5 listening across content classes, with technical vocabulary monitored and pre-taught where needed.", ev:"A quarterly check-in with each content teacher (three questions: follows lectures, understands technical vocabulary, needs pre-teaching), logged on the LSP. Progress is 'no concerns' from all teachers for two quarters."},
 ],
},
S: {
 1: [
  {std:2, g:"Ask for help, a repeat or the bathroom using set phrases, independently, in 4 of 5 observed needs by January.", ev:"Each week the EL teacher tallies on a card whether the student used a phrase independently when a need arose (help, repeat, bathroom, 'I don't understand'). Progress is independent use in 4 of 5 observed needs for a month."},
  {std:3, g:"Name and describe pictures and objects with single words and short phrases, 15 items in one minute by the spring ELPT.", ev:"A one-minute picture-naming probe every other week using the same 30-card deck; record words named correctly. Baseline the first week; progress is the count rising by at least two per month toward 15."},
  {std:2, g:"Answer yes/no and either/or questions about self and the classroom with a word or phrase in 4 of 5 opportunities.", ev:"Once a week, five yes/no or either/or questions in conversation, tallied on the same card as the phrase check. Progress is a word or phrase answer (not just a nod) in 4 of 5 for three weeks."},
  {std:9, g:"Produce 10 memorized classroom sentences (greetings, requests, routines) intelligibly on demand by March.", ev:"A checklist of ten target sentences, checked monthly: the teacher prompts ('Greet me', 'Ask for a pencil'), ticks if the sentence is intelligible. Progress is the tick count rising each month to 10."},
 ],
 2: [
  {std:2, g:"Ask and answer simple questions in complete sentences about familiar topics, using sentence frames, in 4 of 5 partner talks by the spring ELPT.", ev:"Once a week during partner talk the teacher scores two exchanges 0–2 (no response / phrase / complete sentence) on the clipboard sheet. Progress is a 2 in 4 of 5 exchanges for a month, with and then without the frame visible."},
  {std:3, g:"Retell a short story or describe a process in 3 to 5 simple sentences with picture support, scoring 2 of 3 on a retell rubric.", ev:"A one-minute recorded retell once a month (phone voice memo, saved to the student folder), scored on a 3-point retell rubric: sequence, detail, sentences. Progress is 1 → 2 → 3 across the semester; the recordings are the evidence."},
  {std:4, g:"State an opinion and give one reason using a frame (I think ___ because ___) in 4 of 5 opportunities.", ev:"During class discussion, every other week, a tally of 'I think ___ because ___' (or equivalent) attempts and successes. Progress is a stated reason in 4 of 5 opinions."},
  {std:10, g:"Use present-tense subject–verb agreement and basic plurals in speech correctly 70% of the time in a one-minute sample.", ev:"A monthly one-minute speaking sample (same recording as the retell) with agreement and plural errors tallied. Progress is the error rate falling from roughly half to under 30%."},
 ],
 3: [
  {std:3, g:"Explain a process or event from a content class in 5 or more connected sentences with some academic vocabulary, scoring 3 of 4 on a speaking rubric by the spring ELPT.", ev:"A two-minute recorded explanation once a month of a process from a current content unit, scored on the 4-point speaking rubric (sequence, connectors, vocabulary, clarity). Progress is a 3 in three of the last four recordings."},
  {std:4, g:"Make a claim and support it with two reasons or a piece of evidence in class discussion, without a frame, in 3 of 4 opportunities.", ev:"Every other week, a discussion checklist: made a claim, gave a reason, gave a second reason or evidence, no frame needed. Progress is all four boxes in 3 of 4 discussions."},
  {std:2, g:"Participate in a small-group discussion by adding to, agreeing with or asking about a classmate's idea at least twice per discussion.", ev:"A weekly tally during one small-group discussion: contributions that add to, agree with or question a peer. Progress is at least two per discussion for a month, then consistently."},
  {std:9, g:"Present for 2 minutes on a prepared topic with notes, understood by the audience without repetition, by March.", ev:"A quarterly 2-minute presentation to the EL class scored on the 4-point rubric; a peer notes any point that had to be repeated. Progress is zero repeats and a rubric score of 3 by spring."},
 ],
 4: [
  {std:4, g:"Argue a position in a class discussion or debate with evidence from a text and respond to a counterargument, scoring 3 of 4 on a speaking rubric by the spring ELPT.", ev:"A structured academic controversy or mini-debate once a quarter, scored on the 4-point speaking rubric with a line for responding to a counterargument. Progress is a 3 or better by spring."},
  {std:3, g:"Summarize a grade-level text or lesson orally, including the central idea and key details, in 3 of 4 attempts.", ev:"Every other week, an oral summary of the day's text or lesson scored 1–3 (central idea, key details, order). Progress is a 3 in 3 of 4."},
  {std:7, g:"Shift between informal and academic register appropriately (partner talk vs. presenting), in 4 of 5 observed instances.", ev:"Monthly observation of two settings (partner talk, presenting or speaking to an adult) with a register checklist. Progress is appropriate register in 4 of 5 observed instances."},
  {std:9, g:"Present for 3 to 4 minutes with varied sentence structures and transitions, using notes only, by March.", ev:"A quarterly 3–4 minute presentation with notes only, scored on the 4-point rubric with a line for sentence variety and transitions. Progress is a 3 by the spring quarter."},
 ],
 5: [
  {std:2, g:"Participate in fast-paced grade-level discussion, disagree politely, and build on others' ideas at the grade-level benchmark by the spring ELPT.", ev:"The content teacher's discussion rubric (most departments have one), reported quarterly. Progress is a score at the class benchmark for two quarters."},
  {std:9, g:"Present without notes for 5 minutes with precise vocabulary and few errors that affect meaning.", ev:"A quarterly 5-minute presentation without notes, scored on the 4-point rubric, with vocabulary precision and errors-affecting-meaning noted. Progress is a 4 by spring."},
  {std:7, g:"Speak appropriately in an interview, a formal presentation and a casual exchange, adjusting register in each, in 3 of 3 observed settings.", ev:"One mock interview and one formal presentation per semester, each scored for register on a 3-point scale, plus a casual-exchange observation. Progress is appropriate register in all three."},
  {std:10, g:"Maintain Level 5 speaking; refine precision and complex grammar (conditionals, passive, reported speech) in academic talk.", ev:"A semester speaking sample analyzed for complex structures used correctly (conditionals, passive, reported speech). Progress is each structure appearing correctly at least once."},
 ],
},
R: {
 1: [
  {std:1, g:"Read and understand environmental print, labels, schedules and single sentences with picture support, 8 of 10 correct by January.", ev:"A ten-item picture-to-sentence match every other week using print from the building (signs, schedule, labels). Recorded x/10; progress is 8/10 twice in a row."},
  {std:8, g:"Read 50 high-frequency school words on sight by the spring ELPT.", ev:"The First 100 Words sight-word check once a month: flash 50 words, tally read correctly within 3 seconds. Progress is the count rising monthly toward 50."},
  {std:8, g:"Use a bilingual dictionary or glossary to find the meaning of a word independently, in 4 of 5 attempts by March.", ev:"During independent reading every other week, the teacher notes whether the student opened the dictionary/glossary and found the word without being told to. Progress is 4 of 5 attempts independent."},
  {std:1, g:"Match 10 content words to pictures or definitions after a lesson, 8 of 10 correct.", ev:"A weekly ten-item match of that week's content words to pictures or definitions. Progress is 8/10 in three consecutive weeks."},
 ],
 2: [
  {std:1, g:"Read a short text (4 to 6 sentences) on a familiar topic and identify the main idea and one detail, in 4 of 5 checks by the spring ELPT.", ev:"A short passage (4–6 sentences) with three questions every other week, taken from the EL class's leveled texts. Scored x/3; progress is 3/3 in 4 of the last 5."},
  {std:8, g:"Use context clues and cognates to work out the meaning of unfamiliar words in a short text, 6 of 10 correct by March.", ev:"A monthly ten-item task: unfamiliar words underlined in a short text, student writes or says the likely meaning; Cognate Hunt output used for the cognate items. Progress is 4/10 → 6/10 by March."},
  {std:1, g:"Follow written multi-step directions for a classroom task independently, in 4 of 5 tasks.", ev:"A weekly tally of whether the student completed a classroom task from written directions without asking. Progress is 4 of 5 tasks for a month."},
  {std:3, g:"Answer literal questions (who, what, where, when) about a leveled text in writing or speech, 8 of 10 correct.", ev:"Every other week, ten literal questions on a leveled text, answered orally or in writing. Scored x/10; progress is 8/10 twice in a row."},
 ],
 3: [
  {std:1, g:"Read an adapted grade-level text with vocabulary preview and identify the main idea, supporting details and sequence, scoring 3 of 4 on a comprehension rubric by the spring ELPT.", ev:"Every other week, a comprehension task on an adapted grade-level text (main idea, two details, sequence) scored 0–4. Progress is a 3 or better in three of the last four."},
  {std:8, g:"Determine the meaning of academic and content words using context, word parts and cognates, 8 of 10 correct by March.", ev:"A monthly ten-item word-meaning check drawn from that month's content texts, with the strategy used (context, word part, cognate) noted. Progress is 8/10 by March."},
  {std:6, g:"Distinguish fact from opinion and identify the author's point in a short informational text, in 4 of 5 checks.", ev:"Once a month, a fact/opinion sort of ten sentences plus one 'what is the author's point?' question on a short informational text. Progress is 8/10 and the author's point right in 4 of 5."},
  {std:3, g:"Locate evidence in a text to answer a text-dependent question, citing the sentence, in 4 of 5 questions.", ev:"Every other week, five text-dependent questions where the student must underline the sentence that answers each. Progress is the right sentence in 4 of 5."},
 ],
 4: [
  {std:1, g:"Read a grade-level literary or informational text with minimal support and determine the central idea, how it develops and the author's purpose, scoring 3 of 4 by the spring ELPT.", ev:"Every other week, a grade-level passage with central idea, development and author's-purpose questions, scored on the ELA 4-point rubric. Progress is a 3 in three of the last four."},
  {std:6, g:"Identify a claim, the evidence used and whether it is sufficient in a grade-level argument text, in 4 of 5 analyses.", ev:"A monthly claim–evidence organizer on a grade-level argument text, marked for claim found, evidence found, sufficiency judged. Progress is all three in 4 of 5."},
  {std:8, g:"Interpret figurative language, multiple-meaning words and technical terms in grade-level text, 8 of 10 correct.", ev:"A monthly ten-item check on figurative, multiple-meaning and technical words taken from the student's own content texts. Progress is 8/10 twice in a row."},
  {std:3, g:"Compare how two texts treat the same topic, citing evidence from each, scoring 3 of 4 on a rubric.", ev:"A quarterly paired-text task from the ELA class scored on its rubric. Progress is a 3 by spring."},
 ],
 5: [
  {std:1, g:"Read grade-level and primary-source texts independently at the grade-level benchmark on content and state assessments by the spring ELPT.", ev:"Content-class and benchmark reading assessments reported quarterly as a percentage or scale score. Progress is at or above the grade benchmark for two quarters."},
  {std:6, g:"Evaluate the reasoning and evidence in complex arguments and identify bias or missing evidence, in 4 of 5 analyses.", ev:"A monthly argument-evaluation task on a complex text (editorial, primary source), scored on a 4-point rubric that includes bias or missing evidence. Progress is a 3 or 4 in 4 of 5."},
  {std:5, g:"Gather and compare information from three sources on a research question, noting credibility, by the end of the semester.", ev:"A semester research task: three sources on one question with a one-line credibility note each, scored on the content class's research rubric. Progress is the task completed at benchmark."},
  {std:8, g:"Maintain Level 5 reading; build technical vocabulary in each content area, tracked by a personal word log.", ev:"A personal word log reviewed each quarter with the EL teacher: new technical terms per content area, with a sentence each. Progress is the log growing every quarter and the student using the terms in writing."},
 ],
},
W: {
 1: [
  {std:9, g:"Write name, date, labels and copied sentences accurately, and complete a simple form, independently by January.", ev:"A weekly check of the student's own heading, labels and a copied sentence from class work, scored right/wrong on a dated checklist. Progress is four consecutive weeks correct."},
  {std:3, g:"Write 3 simple sentences about self, family or a picture using a sentence frame and word bank, by the spring ELPT.", ev:"Every other week, a three-sentence sample from a frame and word bank, scored 0–3 (one point per complete, meaningful sentence) and kept in the writing folder. Progress is 3/3 in three of the last four."},
  {std:8, g:"Label 10 pictures or diagram parts with the correct content word, 8 of 10 correct after a lesson.", ev:"A weekly labeling task of a diagram or picture set from the content unit, ten labels, scored x/10. Progress is 8/10 in three consecutive weeks."},
  {std:10, g:"Use capital letters and end punctuation in copied and frame-supported sentences 80% of the time.", ev:"The monthly writing sample tallied for capitals and end punctuation. Progress is 50% → 80% across the semester."},
 ],
 2: [
  {std:3, g:"Write a paragraph of 4 to 6 simple sentences on a familiar topic with a topic sentence, using a word bank, scoring 2 of 3 on a rubric by the spring ELPT.", ev:"Every other week, a paragraph on a familiar topic from a word bank, scored on a 3-point rubric (topic sentence, 4+ sentences, on topic) and kept in the writing folder. Progress is a 2 or 3 in 4 of the last 5."},
  {std:4, g:"Write an opinion with one reason using a frame (I think ___ because ___), in 4 of 5 prompts.", ev:"A weekly opinion quick-write (three minutes) checked for a stated reason. Progress is a reason present in 4 of 5."},
  {std:10, g:"Use present and past tense correctly 70% of the time in a short writing sample by March.", ev:"The monthly writing sample with verb-tense errors tallied against verbs used. Progress is accuracy rising from about half to 70% by March."},
  {std:9, g:"Write complete sentences (subject and verb) 80% of the time in independent writing.", ev:"The monthly sample counted for complete sentences out of sentences attempted. Progress is 80% for two months running."},
 ],
 3: [
  {std:3, g:"Write a paragraph with a topic sentence, three details and a concluding sentence, using some academic vocabulary, scoring 3 of 4 on a rubric by the spring ELPT.", ev:"Every other week, a paragraph scored on the 4-point rubric (topic sentence, three details, conclusion, academic vocabulary), kept in the folder with the previous one for comparison. Progress is a 3 in three of the last four."},
  {std:4, g:"Write a claim supported by two pieces of evidence from a text, with a sentence explaining each, in 3 of 4 prompts.", ev:"A monthly claim–evidence–reasoning paragraph from a content-class text, scored with the CER checklist the science department uses. Progress is all three parts present in 3 of 4."},
  {std:9, g:"Use transitions (first, however, because, as a result) to connect ideas across a paragraph, at least 3 per paragraph.", ev:"A transition count on the monthly sample (circle each one). Progress is three or more per paragraph, used correctly, for two months."},
  {std:10, g:"Edit own writing for subject–verb agreement, plurals and past tense using a checklist, fixing 70% of errors.", ev:"Once a month the student edits a previous sample with the editing checklist; the teacher counts errors before and after. Progress is 70% of errors fixed independently."},
 ],
 4: [
  {std:4, g:"Write a multi-paragraph argument with a claim, evidence from two sources, reasoning and a counterclaim, scoring 3 of 4 on a grade-level rubric by the spring ELPT.", ev:"A quarterly multi-paragraph argument scored on the ELA department's rubric, with the counterclaim line checked. Progress is a 3 by spring."},
  {std:3, g:"Write a summary, lab report or analysis of a grade-level text that includes the central idea and key details, in 3 of 4 assignments.", ev:"The content teacher's own writing assignments (summary, lab report, analysis) reported monthly with the rubric score. Progress is a passing score in 3 of 4."},
  {std:9, g:"Vary sentence structure (compound, complex) and use precise vocabulary so that errors do not affect meaning, in 3 of 4 samples.", ev:"The monthly sample scored for sentence variety (count compound and complex sentences) and for errors that affect meaning. Progress is variety up, meaning errors down to two or fewer per page."},
  {std:5, g:"Write a short research piece citing two sources in the required format by the end of the semester.", ev:"A semester research piece with two cited sources, scored on the class rubric with a line for citation format. Progress is completed at benchmark."},
 ],
 5: [
  {std:4, g:"Write research-based arguments and informational pieces at the grade-level benchmark with few errors that affect meaning, by the spring ELPT.", ev:"Content-class and state writing assessments reported quarterly. Progress is a score at the grade benchmark for two quarters."},
  {std:7, g:"Write in multiple genres and registers (lab report, formal letter, narrative, analysis) adjusting tone and vocabulary to each, in 3 of 3 assigned genres.", ev:"A semester portfolio of three genres, each scored for fit of tone and vocabulary to purpose on a 3-point scale. Progress is a 3 in all three."},
  {std:9, g:"Revise own drafts for clarity, cohesion and register with minimal teacher direction, improving a rubric score by one level in 3 of 4 revisions.", ev:"Draft and final of each major piece kept together; rubric scores compared. Progress is the final a level above the draft in 3 of 4 pieces, with revisions the student made unprompted."},
  {std:10, g:"Maintain Level 5 writing; refine complex grammar (conditionals, passive voice, reported speech) and academic register.", ev:"A semester writing sample analyzed for complex grammar and register. Progress is complex structures used correctly and no register slips in academic writing."},
 ],
},
};
window.ELP_STD = {1:"Construct meaning",2:"Participate in exchanges",3:"Speak and write about texts",4:"Claims with evidence",5:"Research",6:"Analyze arguments",7:"Adapt language to audience",8:"Word meaning",9:"Clear and coherent",10:"Standard English"};
