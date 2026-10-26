#!/usr/bin/env python3
"""Spanish for Teachers — the content of the 90-minute workshop, in one place.

tools/make-workshop.py reads this and writes spanish-for-teachers.html and
spanish-for-teachers-packet.pdf. Edit the words here, not in the outputs.

Phrases are (spanish, say-it, english, note). Say-it uses the convention of
the Using Spanish handouts: capitals mark the stressed syllable. Spanish is
neutral Latin American usage; students' own versions are always welcome.
"""

RULES = [
 ("Five vowels, never changing",
  "a = ah · e = eh · i = ee · o = oh · u = oo. English vowels wander; Spanish vowels do not. "
  "Say every vowel short and clean and you are already halfway there.",
  "casa (KAH-sah) · mesa (MEH-sah) · libro (LEE-broh)"),
 ("Stress the next-to-last syllable",
  "If a word ends in a vowel, n or s, the stress falls on the syllable before the last one. "
  "Any other ending puts the stress on the last syllable. A written accent mark wins over both.",
  "escuela (es-KWEH-lah) · papel (pah-PEL) · página (PAH-hee-nah) · José (ho-SEH)"),
 ("h is silent, j sounds like h",
  "hola is OH-lah. Jorge is HOR-heh. ñ is the ny in canyon (niño = NEE-nyoh). "
  "ll and y both sound like the y in yes (me llamo = meh YAH-moh).",
  "hija (EE-hah) · Guillermo (ghee-YER-moh) · mañana (mah-NYAH-nah)"),
 ("One r taps, two rr roll",
  "A single r is a quick tap of the tongue, like the tt in butter said fast. rr rolls. "
  "If you cannot roll it, tap it twice; everyone will understand you.",
  "pero (PEH-roh) · perro (PEH-rroh) · Rodríguez (rroh-DREE-ghes)"),
 ("Say it with a smile",
  "A wrong accent with a kind face lands better than silence. Students correct a brave "
  "teacher gladly; they cannot correct one who never tries.",
  "Then say: ¿Lo dije bien? — Did I say it right? (loh DEE-heh byen)"),
]

NAMES = [
 ("José", "ho-SEH"), ("Jorge", "HOR-heh"), ("Guillermo", "ghee-YER-moh"), ("Ángel", "AHN-hel"),
 ("Joaquín", "hwah-KEEN"), ("Javier", "hah-VYER"), ("Jesús", "heh-SOOS"), ("Xiomara", "syoh-MAH-rah"),
 ("Yesenia", "yeh-SEH-nyah"), ("Itzel", "eet-SEL"), ("Ximena", "hee-MEH-nah"), ("Rocío", "rroh-SEE-oh"),
 ("Hernández", "er-NAHN-des"), ("Jiménez", "hee-MEH-nes"), ("Villarreal", "vee-yah-rreh-AHL"),
 ("Rodríguez", "rroh-DREE-ghes"), ("Vásquez", "VAHS-kes"), ("Ruiz", "rroo-EES"),
]

ROUNDS = [
 dict(id="greet", n=1, title="Greet and say their names", minutes=12,
  goal="Say hello, say your name, and say every student's name the way the student says it.",
  phrases=[
   ("Hola", "OH-lah", "Hi", ""),
   ("Buenos días", "BWEH-nohs DEE-ahs", "Good morning", "until about noon"),
   ("Buenas tardes", "BWEH-nahs TAR-dehs", "Good afternoon", "noon until dark"),
   ("¿Cómo estás?", "KOH-moh es-TAHS", "How are you?", "to a student"),
   ("Bien, gracias. ¿Y tú?", "byen GRAH-syahs · ee TOO", "Fine, thanks. And you?", ""),
   ("Me llamo …", "meh YAH-moh", "My name is …", ""),
   ("¿Cómo te llamas?", "KOH-moh teh YAH-mahs", "What's your name?", ""),
   ("Mucho gusto", "MOO-choh GOOS-toh", "Nice to meet you", ""),
   ("Bienvenido / Bienvenida", "byen-veh-NEE-doh / -dah", "Welcome", "-o to a boy, -a to a girl"),
   ("¿Cómo se pronuncia tu nombre?", "KOH-moh seh proh-NOON-syah too NOHM-breh", "How do you pronounce your name?", "then say it back"),
   ("Hasta mañana", "AHS-tah mah-NYAH-nah", "See you tomorrow", ""),
   ("Nos vemos", "nohs VEH-mohs", "See you", "at the door"),
  ],
  practice=("Roll call, done right",
   "Pairs. Partner A reads a name from the name card (or a real class list); Partner B says it using "
   "the stress rule. Switch after each name. Then every teacher greets three people in the room with "
   "a different greeting each time — Hola, Buenos días, Mucho gusto — and asks ¿Cómo te llamas?"),
  script=[
   "Play each phrase twice from the page, then everyone says it together. Twelve phrases, two minutes.",
   "Put the name card on the screen. Read the first four names badly on purpose — stress on the wrong syllable — then correctly. Ask the room which one they would want to hear at the door.",
   "Run the roll-call practice for five minutes. Walk the room; nobody is allowed to skip a name.",
   "Close the round: ‘Tomorrow, greet one student in Spanish at the door and say their name the way they say it. That is the whole assignment.’",
  ]),

 dict(id="room", n=2, title="Run the room", minutes=15,
  goal="Give the fifteen directions a class hears every day, to one student or to everyone.",
  phrases=[
   ("Siéntate / Siéntense", "SYEN-tah-teh / SYEN-ten-seh", "Sit down", "one student / everyone"),
   ("Levántate / Levántense", "leh-VAHN-tah-teh / leh-VAHN-ten-seh", "Stand up", "one / everyone"),
   ("Abre el libro / Abran el libro", "AH-breh el LEE-broh / AH-brahn", "Open the book", ""),
   ("Página veinte", "PAH-hee-nah VAYN-teh", "Page twenty", "numbers below"),
   ("Escribe / Escriban", "es-KREE-beh / es-KREE-bahn", "Write", ""),
   ("Lee / Lean", "LEH-eh / LEH-ahn", "Read", ""),
   ("Escucha / Escuchen", "es-KOO-chah / es-KOO-chen", "Listen", ""),
   ("Mira / Miren", "MEE-rah / MEE-ren", "Look", "point while you say it"),
   ("Levanta la mano", "leh-VAHN-tah lah MAH-noh", "Raise your hand", ""),
   ("Trabajen en parejas", "trah-BAH-hen en pah-REH-hahs", "Work in pairs", ""),
   ("En silencio, por favor", "en see-LEN-syoh · por fah-VOR", "Quietly, please", ""),
   ("¿Entiendes? / ¿Entienden?", "en-TYEN-des / en-TYEN-den", "Do you understand?", "one / everyone"),
   ("Otra vez", "OH-trah ves", "Again", ""),
   ("Más despacio", "mahs des-PAH-syoh", "Slower", ""),
   ("Saquen una hoja", "SAH-ken OO-nah OH-hah", "Take out a sheet of paper", ""),
   ("Guarden todo", "GWAR-den TOH-doh", "Put everything away", ""),
   ("Es hora de salir", "es OH-rah deh sah-LEER", "It's time to go", ""),
   ("La tarea", "lah tah-REH-ah", "The homework", ""),
  ],
  practice=("Simón dice",
   "Simon Says, in Spanish, standing up. The facilitator (or a volunteer) gives directions from the "
   "list — Simón dice: levántense… Simón dice: miren la puerta… siéntense (no Simón — anyone who sits is out). "
   "Three rounds, then a teacher who has never studied Spanish leads the last round reading from the card."),
  script=[
   "Say every direction with the gesture you would use anyway: palm down for siéntense, hand up for levanta la mano. The gesture carries the meaning; the Spanish carries the welcome.",
   "Point out the pattern: one student ends in -a or -e, the whole class ends in -n. Escucha, escuchen. Mira, miren. They can build the plural themselves.",
   "Numbers one to thirty, counted together once, then page numbers called out and found in any book on the table.",
   "Simón dice for six minutes. Make the last leader someone who said ‘I can't do this’ at the start.",
  ],
  extra=("Numbers for pages and groups",
   "uno · dos · tres · cuatro · cinco · seis · siete · ocho · nueve · diez · once · doce · trece · catorce · quince · "
   "dieciséis · diecisiete · dieciocho · diecinueve · veinte · veintiuno … treinta (30) · cuarenta (40) · "
   "cincuenta (50) · cien (100). Página cincuenta y dos = page 52. Grupos de tres = groups of three.")),

 dict(id="encourage", n=3, title="Encourage and check in", minutes=12,
  goal="Praise, reassure, and ask the two questions that keep a student working.",
  phrases=[
   ("Muy bien", "mwee BYEN", "Very good", ""),
   ("¡Excelente!", "ek-seh-LEN-teh", "Excellent!", ""),
   ("Casi", "KAH-see", "Almost", "a kind ‘not yet’"),
   ("Inténtalo", "een-TEN-tah-loh", "Try it", ""),
   ("No te preocupes", "noh teh preh-oh-KOO-pes", "Don't worry", ""),
   ("Sigue así", "SEE-gheh ah-SEE", "Keep it up", ""),
   ("¿Necesitas ayuda?", "neh-seh-SEE-tahs ah-YOO-dah", "Do you need help?", ""),
   ("¿Tienes preguntas?", "TYEH-nes preh-GOON-tahs", "Do you have questions?", ""),
   ("Piénsalo en español. Escríbelo en inglés.", "PYEN-sah-loh en es-pah-NYOL · es-KREE-beh-loh en een-GLES", "Think it in Spanish. Write it in English.", "the sentence of the workshop"),
   ("Dímelo en inglés", "DEE-meh-loh en een-GLES", "Tell me in English", ""),
   ("¿Cómo se dice ___ en inglés?", "KOH-moh seh DEE-seh … en een-GLES", "How do you say ___ in English?", ""),
   ("Está bien equivocarse", "es-TAH byen eh-kee-voh-KAR-seh", "It's okay to make mistakes", ""),
   ("Estoy orgulloso / orgullosa de ti", "es-TOY or-goo-YOH-soh / -sah deh tee", "I'm proud of you", "-o if you are a man, -a if you are a woman"),
   ("Gracias por tu trabajo", "GRAH-syahs por too trah-BAH-hoh", "Thanks for your work", ""),
  ],
  practice=("The encouragement deck",
   "Cut the phrase cards apart. In groups of three, one teacher holds up a card in English; the other two race "
   "to say it in Spanish. Then reverse: hold up the Spanish, say the English. Keep going until every card has been "
   "said by every person."),
  script=[
   "Explain the one sentence that matters most: Piénsalo en español. Escríbelo en inglés. It tells a Spanish-speaking student that their first language is a tool, not a problem, and that the product is still in English.",
   "Say it together five times until nobody is reading it.",
   "Run the encouragement deck for six minutes.",
   "Ask each table: which two of these will you actually say this week? Write them on the pocket card now.",
  ]),

 dict(id="hear", n=4, title="Hear what students say", minutes=12,
  goal="Recognize the fifteen things a Spanish-speaking student says to a teacher most often.",
  phrases=[
   ("No entiendo", "noh en-TYEN-doh", "I don't understand", "the one to listen for"),
   ("No sé", "noh SEH", "I don't know", ""),
   ("¿Puedo ir al baño?", "PWEH-doh eer al BAH-nyoh", "Can I go to the bathroom?", ""),
   ("¿Puedo tomar agua?", "PWEH-doh toh-MAR AH-gwah", "Can I get water?", ""),
   ("¿Qué página?", "keh PAH-hee-nah", "What page?", ""),
   ("¿Me ayuda?", "meh ah-YOO-dah", "Can you help me?", "polite, to a teacher"),
   ("¿Cómo se dice ___?", "KOH-moh seh DEE-seh", "How do you say ___?", ""),
   ("¿Qué significa ___?", "keh seeg-nee-FEE-kah", "What does ___ mean?", ""),
   ("Ya terminé", "yah ter-mee-NEH", "I'm done", ""),
   ("Se me olvidó", "seh meh ol-vee-DOH", "I forgot it", ""),
   ("¿Hay tarea?", "eye tah-REH-ah", "Is there homework?", ""),
   ("¿Puedo trabajar con él / ella?", "PWEH-doh trah-bah-HAR kon EL / EH-yah", "Can I work with him / her?", ""),
   ("Me duele la cabeza / el estómago", "meh DWEH-leh lah kah-BEH-sah / el es-TOH-mah-goh", "My head / stomach hurts", "send to the nurse"),
   ("Tengo hambre", "TEN-goh AHM-breh", "I'm hungry", "tell the counselor"),
   ("Maestro / Maestra · Míster / Miss", "mah-ES-troh / mah-ES-trah", "Teacher", "how students will address you"),
  ],
  practice=("Listen and answer",
   "The facilitator plays a student line from the page (or a Spanish-speaking colleague or student says it). "
   "Teachers write what it means in English on a whiteboard or scrap paper and hold it up. Ten lines, then switch: "
   "the facilitator says the English and teachers call out the Spanish."),
  script=[
   "This round is listening, not speaking. Teachers do not need to say these; they need to catch them.",
   "Play No entiendo first and stop. Ask: what do you do when you hear this? The answer is not ‘repeat louder.’ It is: show it, slow it, say it again with the gesture, and hand them a sentence frame.",
   "Run the listen-and-answer game for seven minutes. Keep score by table if the room wants it.",
   "Mark the two lines that are health or welfare — me duele, tengo hambre — and say who in your building those go to.",
  ]),

 dict(id="call", n=5, title="The two-minute family call", minutes=14,
  goal="Make a good-news call home in formal Spanish, reading from a script, in under two minutes.",
  phrases=[
   ("Buenas tardes. Soy la maestra / el maestro de ___ de ___.", "BWEH-nahs TAR-dehs · soy lah mah-ES-trah / el mah-ES-troh deh … deh …", "Good afternoon. I'm ___'s ___ teacher.", "subject first, then the student's name"),
   ("Hablo poco español.", "AH-bloh POH-koh es-pah-NYOL", "I speak a little Spanish.", "say it early — it buys patience"),
   ("Llamo con buenas noticias.", "YAH-moh kon BWEH-nahs noh-TEE-syahs", "I'm calling with good news.", ""),
   ("Su hijo / Su hija está trabajando muy bien.", "soo EE-hoh / soo EE-hah es-TAH trah-bah-HAHN-doh mwee BYEN", "Your son / daughter is working very well.", ""),
   ("Estoy muy contento / contenta con su progreso.", "es-TOY mwee kon-TEN-toh / -tah kon soo proh-GREH-soh", "I'm very pleased with his / her progress.", "-o man, -a woman"),
   ("Participa mucho en clase.", "par-tee-SEE-pah MOO-choh en KLAH-seh", "He / she participates a lot in class.", ""),
   ("¿Tiene alguna pregunta?", "TYEH-neh al-GOO-nah preh-GOON-tah", "Do you have any questions?", ""),
   ("Un momento, por favor.", "oon moh-MEN-toh · por fah-VOR", "One moment, please.", "while you find a colleague"),
   ("Gracias por su tiempo.", "GRAH-syahs por soo TYEM-poh", "Thank you for your time.", ""),
   ("Que tenga buena tarde.", "keh TEN-gah BWEH-nah TAR-deh", "Have a good afternoon.", ""),
  ],
  practice=("Rehearse the call",
   "Pairs, back to back so you cannot see each other, like a phone. Partner A is the teacher and reads the "
   "six-line script with a real student's name and subject. Partner B is the parent and answers only Gracias, maestra "
   "or ¿Cómo? (what?). If B says ¿Cómo?, A repeats the line slower. Switch. Time it: under two minutes each."),
  script=[
   "Note the shift to usted: su hijo, ¿tiene?, que tenga. Parents are addressed formally. The student forms from Round 1 would sound wrong here.",
   "Subjects: matemáticas, álgebra, ciencias, biología, historia, inglés. Write yours into the blank before you rehearse.",
   "Rehearse for eight minutes. Every teacher makes the call at least twice.",
   "Say plainly: this script is for the good-news call only. Grades at risk, attendance, discipline and anything about an IEP or placement go through the district's interpreter — that is a right, not a courtesy.",
  ],
  extra=("Subjects to drop into the blank",
   "matemáticas (mah-teh-MAH-tee-kahs) · álgebra (AHL-heh-brah) · ciencias (SYEN-syahs) · biología (byoh-loh-HEE-ah) · "
   "historia (ees-TOH-ryah) · inglés (een-GLES) · educación física (eh-doo-kah-SYON FEE-see-kah) · arte (AR-teh)")),
]

COGNATES = [
 ("problema", "problem"), ("ejemplo", "example"), ("importante", "important"), ("diferente", "different"),
 ("similar", "similar"), ("experimento", "experiment"), ("análisis", "analysis"), ("evidencia", "evidence"),
 ("resultado", "result"), ("causa", "cause"), ("efecto", "effect"), ("comparar", "compare"),
 ("describir", "describe"), ("explicar", "explain"), ("identificar", "identify"), ("organizar", "organize"),
 ("examen", "exam"), ("proyecto", "project"), ("laboratorio", "laboratory"), ("texto", "text"),
]
PATTERNS = [
 ("-tion → -ción", "education → educación · information → información"),
 ("-ty → -dad", "university → universidad · community → comunidad"),
 ("-ly → -mente", "finally → finalmente · exactly → exactamente"),
 ("-ic → -ico", "basic → básico · scientific → científico"),
 ("-ous → -oso", "famous → famoso · curious → curioso"),
]
FALSE = [
 ("éxito", "success", "not exit"), ("librería", "bookstore", "not library"), ("asistir", "to attend", "not assist"),
 ("realizar", "to carry out", "not realize"), ("actual", "current", "not actual"), ("carpeta", "folder", "not carpet"),
 ("colegio", "school", "not college"), ("largo", "long", "not large"), ("embarazada", "pregnant", "not embarrassed"),
]

FOLLOWUP = [
 ("Week 1", "Greet at the door", "Hola, buenos días, and every name said right."),
 ("Week 2", "One direction a day", "Siéntense on Monday, escuchen on Tuesday, miren on Wednesday…"),
 ("Week 3", "The sentence", "Piénsalo en español. Escríbelo en inglés — on the board all week."),
 ("Week 4", "Catch the question", "Listen for no entiendo and ¿qué página? and answer them without words first."),
 ("Week 5", "The call", "One good-news call home, read from the script, two minutes."),
 ("Week 6", "Ask a student to teach", "Frase de la semana: a Spanish speaker teaches the class one phrase every Monday."),
]

PREP = [
 "Print the packet: one facilitator script for you, one participant handout per teacher (phrase cards, pocket card, exit ticket).",
 "A projector or a TV and a speaker. The page plays every phrase in a Spanish voice; test the sound before people arrive.",
 "Cut the phrase cards for Round 3 (one set per table of three) — or hand each table scissors and give them the first two minutes.",
 "If a Spanish-speaking colleague, paraprofessional or student is willing to sit in, invite them. They are not required; the page carries the sound.",
 "Tables of three or four. Mixed departments work best — the math teacher and the English teacher hear each other's students.",
 "Set a 90-minute clock where you can see it. The timers on this page run each round for you.",
]
