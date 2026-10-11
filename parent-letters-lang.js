/* EL parent notification letters — text in each family language.
   Placeholders in {braces} are filled from the form: {parent} {student} {child}
   {grade} {lang} {test} {program} {year} {meeting} {contact} {phone} {school}
   {date} {LV} (the four-level box) {SIG} (signature block) {RESULT} (monitoring
   result line). English is the source; Spanish was written by the author; the
   other languages are careful translations that a district should have a
   native-speaking staff member or its translation vendor read once before
   adopting as official notices. */
window.PL_LANGS = [
  ["en", "English", "English"],
  ["es", "Spanish", "Español"],
  ["vi", "Vietnamese", "Tiếng Việt"],
  ["ar", "Arabic", "العربية"],
  ["zh", "Chinese (Simplified)", "中文（简体）"],
  ["ht", "Haitian Creole", "Kreyòl Ayisyen"],
];
window.PL_RTL = { ar: true };
window.PL = {
/* ───────────────────────────── ENGLISH ───────────────────────────── */
en: {
 d: { parent: "[Parent/guardian]", student: "[student]", child: "your child", grade: "__", lang: "[language]", test: "[test, date]", program: "[program description]", year: "[year]", meeting: "[date, time, place]", contact: "[EL contact]", phone: "[phone · email]", school: "[school]", signer: "[Signer, title]", overall: "________" },
 ui: { program: "English Learner Program", year: "School year", sign: "Signature", L: "Listening", S: "Speaking", R: "Reading", W: "Writing", O: "Overall",
       foot: "This notice is provided under federal law (ESSA §1112(e)(3)) and Title VI of the Civil Rights Act. You have the right to receive this information in a language you understand and to a free interpreter at any meeting. · If you prefer another language, call the number above.",
       result: "☐ Progressing well — no action needed &nbsp; ☐ Some concern — supports added in class &nbsp; ☐ Recommend a meeting to discuss re-entering EL services" },
 init: `<h3>Your child has been identified as an English learner — and what that means</h3>
<p>Dear {parent},</p>
<p>When you enrolled {student} (grade {grade}), the Home Language Survey showed that {lang} is spoken at home. As federal law requires, the school then measured your child's English with the {test}. The results:</p>{LV}
<p><b>Why this matters.</b> Because of these results, your child qualifies for English learner (EL) services. This is <b>support, not a judgment</b>: it means the school is responsible for teaching your child English <i>and</i> for making every class understandable while that happens.</p>
<p><b>The program.</b> {program} Your child stays in grade-level classes with everyone else; EL support is added, never substituted. If your child has an IEP or 504 plan, EL services are coordinated with it so both plans are met.</p>
<p><b>How your child finishes the program.</b> Every spring your child takes the state English test (ELPT). A student exits when they score Level 4 or 5 in all four areas. Most students need several years; progress of about one level per year is typical. After exiting, we check on your child's grades for four more years.</p>
<p><b>Graduation.</b> English learners earn the same diploma with the same requirements as every other student. Students in this program graduate at a rate the school tracks and reports; your child's counselor will show you the credit plan at any time.</p>
<p><b>Your rights.</b> You may visit the program, ask for a meeting with an interpreter at no cost, and request this letter in another language. You may also <b>decline</b> EL services in writing; if you do, your child will still take the yearly English test and will still receive help in class, and you can change your mind at any time.</p>
<p>Please call or email with any question — we would rather hear from you than have you wonder.</p>{SIG}`,
 annual: `<h3>Annual notice: your child's English learner services for {year}</h3>
<p>Dear {parent},</p>
<p>{student} (grade {grade}) will continue to receive English learner (EL) services this year. On the most recent state English test ({test}) the results were:</p>{LV}
<p><b>This year's plan.</b> {program} The area we will focus on most is the lowest level above. Your child's teachers have a written Language Service Plan listing the supports and accommodations your child receives in every class and on state tests.</p>
<p><b>Exit requirement.</b> Level 4 or 5 in all four areas on the spring ELPT. Students who reach it are exited and monitored for four years.</p>
<p><b>Your rights</b> are unchanged: a free interpreter at any meeting, this letter in another language on request, the right to visit, and the right to decline services in writing. We welcome a conference at any time — just call the number below.</p>{SIG}`,
 exit: `<h3>Congratulations — {student} has completed the English learner program</h3>
<p>Dear {parent},</p>
<p>On the {test}, {student} (grade {grade}) reached the state exit standard — Level 4 or 5 in all four areas:</p>{LV}
<p><b>What changes.</b> Your child is now a <b>former English learner</b>. The EL label and the yearly ELPT test end. Classes, grades and graduation requirements do not change.</p>
<p><b>What continues.</b> By law we will <b>monitor</b> your child's grades and test scores for the next <b>four years</b>. If your child begins to struggle in a way that is related to language, we will contact you and can restart support. Classroom accommodations can continue if a teacher sees they are still needed.</p>
<p><b>A word about the achievement.</b> Learning a second language well enough to do grade-level work in it is one of the hardest things a student does. Please tell {child} we noticed. If your family's language is still spoken at home, keep it strong — students who are fully bilingual may qualify for Mississippi's Seal of Biliteracy on the diploma.</p>{SIG}`,
 monitor: `<h3>Monitoring notice for a former English learner</h3>
<p>Dear {parent},</p>
<p>{student} (grade {grade}) exited the English learner program and is in the four-year monitoring period required by federal law. This letter is to tell you what we check and what we found this period.</p>
<div class="box"><b>Checked this period:</b> grades in English, math, science and social studies · state test results · teacher reports · attendance<br><b>Result:</b> {RESULT}</div>
<p>If supports were added, they are listed in your child's file and the teacher will explain them. If we recommended a meeting, please call to schedule it; an interpreter will be provided at no cost. Re-entering EL services requires your agreement and restarts the yearly ELPT test.</p>
<p>If you have noticed anything at home — homework taking much longer, avoiding reading or writing, lower grades — please tell us. You see things we cannot.</p>{SIG}`,
 refuse: `<h3>Parent request to decline English learner services</h3>
<p>Student: {student} &nbsp; Grade: {grade} &nbsp; School: {school} &nbsp; Date: {date}</p>
<p>I, {parent}, have been told in a language I understand that my child qualifies for English learner (EL) services, what the program offers, and the benefits of participating. I understand that:</p>
<ul>
<li>I am choosing to <b>decline</b> the EL program (ESL/ELD class and/or EL pull-out or push-in support) for the {year} school year.</li>
<li>My child <b>remains identified as an English learner</b> under federal law and will <b>take the state English test (ELPT) every spring</b> until exiting.</li>
<li>The school still must ensure my child can understand and take part in every class, and teachers will still use supports and accommodations in class and on tests.</li>
<li>The school will monitor my child's progress and will contact me if my child is struggling.</li>
<li>I may <b>change this decision at any time</b> by writing to the school; services begin again at once.</li>
</ul>
<p>Reason (optional): ___________________________________________________</p>
<div class="sig"><div>Parent/guardian signature · Date</div><div>{contact} · School representative · Date</div></div>`,
 meet: `<h3>You're invited: a meeting about {student}'s English learning plan</h3>
<p>Dear {parent},</p>
<p>We would like to meet with you to talk about {student} (grade {grade}) — how English is coming along, the Language Service Plan for this year, and what we can do together at school and at home.</p>
<div class="box"><b>When &amp; where:</b> {meeting}<br><b>With:</b> {contact} and your child's teacher(s)<br><b>Interpreter:</b> provided at no cost — {lang} · Please tell us if you prefer another language.<br><b>Bring (if you have them):</b> report cards or papers from a previous school, questions, and {child} — students are welcome.</div>
<p>If this time does not work, call or email and we will find one that does, including by phone or video. You may also bring a friend or family member for support.</p>
<p>Please return the slip below or call {phone}.</p>
<div class="box">☐ Yes, I will attend. &nbsp; ☐ Please call me to reschedule. &nbsp; Best phone number: ____________________ &nbsp; Signature: ____________________</div>{SIG}`
},

/* ───────────────────────────── ESPAÑOL ───────────────────────────── */
es: {
 d: { parent: "[Padre/madre/tutor]", student: "[estudiante]", child: "su hijo/a", grade: "__", lang: "[idioma]", test: "[prueba, fecha]", program: "[descripción del programa]", year: "[año]", meeting: "[fecha, hora, lugar]", contact: "[contacto EL]", phone: "[teléfono · correo]", school: "[escuela]", signer: "[Firmante, cargo]", overall: "________" },
 ui: { program: "Programa de Aprendices de Inglés", year: "Año escolar", sign: "Firma", L: "Escuchar", S: "Hablar", R: "Leer", W: "Escribir", O: "General",
       foot: "Este aviso se entrega conforme a la ley federal (ESSA §1112(e)(3)) y al Título VI de la Ley de Derechos Civiles. Usted tiene derecho a recibir esta información en un idioma que entienda y a un intérprete gratuito en cualquier reunión. · Si prefiere otro idioma, llame al número de arriba.",
       result: "☐ Progresa bien — no se requiere acción &nbsp; ☐ Alguna preocupación — se añadieron apoyos en clase &nbsp; ☐ Se recomienda una reunión para hablar de volver a los servicios EL" },
 init: `<h3>Su hijo/a ha sido identificado/a como aprendiz de inglés — y qué significa</h3>
<p>Estimado/a {parent}:</p>
<p>Cuando inscribió a {student} (grado {grade}), la Encuesta del Idioma del Hogar indicó que en casa se habla {lang}. Como exige la ley federal, la escuela midió entonces el inglés de su hijo/a con la prueba {test}. Los resultados:</p>{LV}
<p><b>Por qué importa.</b> Por estos resultados, su hijo/a califica para los servicios de aprendiz de inglés (EL). Esto es <b>apoyo, no un juicio</b>: significa que la escuela es responsable de enseñarle inglés <i>y</i> de hacer que cada clase sea comprensible mientras tanto.</p>
<p><b>El programa.</b> {program} Su hijo/a permanece en las clases de su grado con los demás; el apoyo EL se añade, nunca se sustituye. Si tiene un IEP o plan 504, los servicios EL se coordinan con él para cumplir ambos planes.</p>
<p><b>Cómo termina el programa.</b> Cada primavera su hijo/a toma el examen estatal de inglés (ELPT). Un estudiante sale del programa cuando obtiene Nivel 4 o 5 en las cuatro áreas. La mayoría necesita varios años; avanzar más o menos un nivel por año es lo normal. Después de salir, revisamos sus calificaciones durante cuatro años más.</p>
<p><b>Graduación.</b> Los aprendices de inglés obtienen el mismo diploma con los mismos requisitos que cualquier otro estudiante. La escuela registra y reporta la tasa de graduación de este programa; el consejero le mostrará el plan de créditos cuando lo pida.</p>
<p><b>Sus derechos.</b> Puede visitar el programa, pedir una reunión con intérprete sin costo y solicitar esta carta en otro idioma. También puede <b>rechazar</b> los servicios EL por escrito; si lo hace, su hijo/a tomará igualmente el examen anual de inglés y seguirá recibiendo ayuda en clase, y usted puede cambiar de opinión en cualquier momento.</p>
<p>Llame o escriba con cualquier pregunta — preferimos escucharle a que se quede con la duda.</p>{SIG}`,
 annual: `<h3>Aviso anual: servicios de aprendiz de inglés de su hijo/a para {year}</h3>
<p>Estimado/a {parent}:</p>
<p>{student} (grado {grade}) seguirá recibiendo servicios de aprendiz de inglés (EL) este año. En el examen estatal de inglés más reciente ({test}) los resultados fueron:</p>{LV}
<p><b>El plan de este año.</b> {program} El área en la que más nos enfocaremos es el nivel más bajo de arriba. Los maestros de su hijo/a tienen un Plan de Servicios de Idioma por escrito con los apoyos y adaptaciones que recibe en cada clase y en los exámenes estatales.</p>
<p><b>Requisito de salida.</b> Nivel 4 o 5 en las cuatro áreas en el ELPT de primavera. Los estudiantes que lo alcanzan salen del programa y son monitoreados durante cuatro años.</p>
<p><b>Sus derechos</b> no cambian: intérprete gratuito en cualquier reunión, esta carta en otro idioma si la pide, el derecho a visitar y el derecho a rechazar los servicios por escrito. Con gusto tendremos una reunión cuando lo desee — solo llame al número de abajo.</p>{SIG}`,
 exit: `<h3>Felicidades — {student} ha completado el programa de aprendices de inglés</h3>
<p>Estimado/a {parent}:</p>
<p>En el {test}, {student} (grado {grade}) alcanzó el estándar estatal de salida — Nivel 4 o 5 en las cuatro áreas:</p>{LV}
<p><b>Qué cambia.</b> Su hijo/a es ahora un/a <b>ex aprendiz de inglés</b>. Terminan la etiqueta EL y el examen anual ELPT. Las clases, calificaciones y requisitos de graduación no cambian.</p>
<p><b>Qué continúa.</b> Por ley <b>monitorearemos</b> las calificaciones y los exámenes de su hijo/a durante los próximos <b>cuatro años</b>. Si empieza a tener dificultades relacionadas con el idioma, le avisaremos y podemos reiniciar el apoyo. Las adaptaciones en clase pueden continuar si un maestro ve que aún se necesitan.</p>
<p><b>Sobre este logro.</b> Aprender un segundo idioma lo suficiente para hacer el trabajo de su grado en él es una de las cosas más difíciles que hace un estudiante. Por favor, dígale a {child} que lo notamos. Si en casa todavía se habla su idioma, manténganlo fuerte — los estudiantes completamente bilingües pueden calificar para el Sello de Alfabetización Bilingüe de Mississippi en el diploma.</p>{SIG}`,
 monitor: `<h3>Aviso de monitoreo para ex aprendiz de inglés</h3>
<p>Estimado/a {parent}:</p>
<p>{student} (grado {grade}) salió del programa de aprendices de inglés y está en el período de monitoreo de cuatro años que exige la ley federal. Esta carta le informa qué revisamos y qué encontramos en este período.</p>
<div class="box"><b>Revisado en este período:</b> calificaciones en inglés, matemáticas, ciencias y estudios sociales · resultados de exámenes estatales · reportes de maestros · asistencia<br><b>Resultado:</b> {RESULT}</div>
<p>Si se añadieron apoyos, están en el expediente de su hijo/a y el maestro los explicará. Si recomendamos una reunión, llame para programarla; habrá intérprete sin costo. Volver a los servicios EL requiere su acuerdo y reinicia el examen anual ELPT.</p>
<p>Si ha notado algo en casa — la tarea toma mucho más tiempo, evita leer o escribir, bajan las calificaciones — díganoslo. Usted ve cosas que nosotros no podemos ver.</p>{SIG}`,
 refuse: `<h3>Solicitud del padre/madre para rechazar los servicios de aprendiz de inglés</h3>
<p>Estudiante: {student} &nbsp; Grado: {grade} &nbsp; Escuela: {school} &nbsp; Fecha: {date}</p>
<p>Yo, {parent}, he sido informado/a en un idioma que entiendo de que mi hijo/a califica para los servicios de aprendiz de inglés (EL), de lo que ofrece el programa y de los beneficios de participar. Entiendo que:</p>
<ul>
<li>Elijo <b>rechazar</b> el programa EL (la clase de ESL/ELD y/o el apoyo EL dentro o fuera del salón) para el año escolar {year}.</li>
<li>Mi hijo/a <b>sigue identificado/a como aprendiz de inglés</b> según la ley federal y <b>tomará el examen estatal de inglés (ELPT) cada primavera</b> hasta salir del programa.</li>
<li>La escuela sigue obligada a asegurar que mi hijo/a entienda y participe en cada clase, y los maestros seguirán usando apoyos y adaptaciones en clase y en los exámenes.</li>
<li>La escuela monitoreará el progreso de mi hijo/a y me avisará si tiene dificultades.</li>
<li>Puedo <b>cambiar esta decisión en cualquier momento</b> escribiendo a la escuela; los servicios se reanudan de inmediato.</li>
</ul>
<p>Motivo (opcional): ___________________________________________________</p>
<div class="sig"><div>Firma del padre/madre/tutor · Fecha</div><div>{contact} · Representante de la escuela · Fecha</div></div>`,
 meet: `<h3>Le invitamos: una reunión sobre el plan de inglés de {student}</h3>
<p>Estimado/a {parent}:</p>
<p>Nos gustaría reunirnos con usted para hablar de {student} (grado {grade}) — cómo va su inglés, el Plan de Servicios de Idioma de este año y qué podemos hacer juntos en la escuela y en casa.</p>
<div class="box"><b>Cuándo y dónde:</b> {meeting}<br><b>Con:</b> {contact} y el/los maestro(s) de su hijo/a<br><b>Intérprete:</b> sin costo — {lang} · Díganos si prefiere otro idioma.<br><b>Traiga (si los tiene):</b> boletas o papeles de la escuela anterior, preguntas y a {child} — los estudiantes son bienvenidos.</div>
<p>Si esta hora no le funciona, llame o escriba y buscaremos otra, incluso por teléfono o video. También puede traer a un amigo o familiar como apoyo.</p>
<p>Por favor devuelva el talón de abajo o llame al {phone}.</p>
<div class="box">☐ Sí, asistiré. &nbsp; ☐ Por favor llámenme para cambiar la fecha. &nbsp; Mejor teléfono: ____________________ &nbsp; Firma: ____________________</div>{SIG}`
},

/* ───────────────────────────── TIẾNG VIỆT ───────────────────────────── */
vi: {
 d: { parent: "[Phụ huynh/người giám hộ]", student: "[học sinh]", child: "con quý vị", grade: "__", lang: "[ngôn ngữ]", test: "[bài kiểm tra, ngày]", program: "[mô tả chương trình]", year: "[năm học]", meeting: "[ngày, giờ, địa điểm]", contact: "[người liên hệ EL]", phone: "[điện thoại · email]", school: "[trường]", signer: "[Người ký, chức vụ]", overall: "________" },
 ui: { program: "Chương trình Học sinh học tiếng Anh", year: "Năm học", sign: "Chữ ký", L: "Nghe", S: "Nói", R: "Đọc", W: "Viết", O: "Tổng thể",
       foot: "Thông báo này được gửi theo luật liên bang (ESSA §1112(e)(3)) và Điều VI của Đạo luật Dân quyền. Quý vị có quyền nhận thông tin này bằng ngôn ngữ mà quý vị hiểu và có thông dịch viên miễn phí trong mọi cuộc họp. · Nếu quý vị muốn dùng ngôn ngữ khác, xin gọi số điện thoại ở trên.",
       result: "☐ Tiến bộ tốt — không cần hành động &nbsp; ☐ Có chút lo ngại — đã thêm hỗ trợ trong lớp &nbsp; ☐ Đề nghị họp để bàn về việc trở lại dịch vụ EL" },
 init: `<h3>Con quý vị đã được xác định là học sinh học tiếng Anh — và điều đó có nghĩa gì</h3>
<p>Kính gửi {parent},</p>
<p>Khi quý vị ghi danh cho {student} (lớp {grade}), Bản khảo sát ngôn ngữ tại nhà cho thấy gia đình nói {lang}. Theo yêu cầu của luật liên bang, nhà trường đã đánh giá trình độ tiếng Anh của con quý vị bằng {test}. Kết quả:</p>{LV}
<p><b>Vì sao điều này quan trọng.</b> Với kết quả này, con quý vị đủ điều kiện nhận dịch vụ dành cho học sinh học tiếng Anh (EL). Đây là <b>sự hỗ trợ, không phải sự đánh giá</b>: nhà trường có trách nhiệm dạy tiếng Anh cho con quý vị <i>và</i> làm cho mọi lớp học dễ hiểu trong thời gian đó.</p>
<p><b>Chương trình.</b> {program} Con quý vị vẫn học các lớp đúng cấp lớp cùng các bạn; hỗ trợ EL được thêm vào, không bao giờ thay thế. Nếu con quý vị có IEP hoặc kế hoạch 504, dịch vụ EL sẽ được phối hợp để đáp ứng cả hai kế hoạch.</p>
<p><b>Con quý vị hoàn thành chương trình như thế nào.</b> Mỗi mùa xuân, con quý vị làm bài kiểm tra tiếng Anh của tiểu bang (ELPT). Học sinh ra khỏi chương trình khi đạt Mức 4 hoặc 5 ở cả bốn lĩnh vực. Hầu hết học sinh cần vài năm; tiến bộ khoảng một mức mỗi năm là bình thường. Sau khi ra khỏi chương trình, chúng tôi tiếp tục theo dõi điểm số của em trong bốn năm nữa.</p>
<p><b>Tốt nghiệp.</b> Học sinh học tiếng Anh nhận cùng một bằng tốt nghiệp với cùng yêu cầu như mọi học sinh khác. Nhà trường theo dõi và báo cáo tỷ lệ tốt nghiệp của chương trình này; cố vấn học tập sẽ cho quý vị xem kế hoạch tín chỉ bất cứ lúc nào.</p>
<p><b>Quyền của quý vị.</b> Quý vị có thể đến thăm chương trình, yêu cầu họp với thông dịch viên miễn phí và yêu cầu thư này bằng ngôn ngữ khác. Quý vị cũng có thể <b>từ chối</b> dịch vụ EL bằng văn bản; nếu vậy, con quý vị vẫn làm bài kiểm tra tiếng Anh hằng năm và vẫn được giúp đỡ trong lớp, và quý vị có thể thay đổi quyết định bất cứ lúc nào.</p>
<p>Xin gọi điện hoặc gửi email nếu có bất kỳ câu hỏi nào — chúng tôi muốn nghe từ quý vị hơn là để quý vị băn khoăn.</p>{SIG}`,
 annual: `<h3>Thông báo hằng năm: dịch vụ học tiếng Anh của con quý vị trong năm học {year}</h3>
<p>Kính gửi {parent},</p>
<p>{student} (lớp {grade}) sẽ tiếp tục nhận dịch vụ dành cho học sinh học tiếng Anh (EL) trong năm nay. Trong bài kiểm tra tiếng Anh của tiểu bang gần nhất ({test}), kết quả là:</p>{LV}
<p><b>Kế hoạch năm nay.</b> {program} Lĩnh vực chúng tôi sẽ tập trung nhiều nhất là mức thấp nhất ở trên. Giáo viên của con quý vị có Kế hoạch Dịch vụ Ngôn ngữ bằng văn bản liệt kê các hỗ trợ và điều chỉnh mà em nhận được trong mọi lớp học và trong các kỳ thi của tiểu bang.</p>
<p><b>Điều kiện ra khỏi chương trình.</b> Mức 4 hoặc 5 ở cả bốn lĩnh vực trong kỳ ELPT mùa xuân. Học sinh đạt điều kiện sẽ ra khỏi chương trình và được theo dõi trong bốn năm.</p>
<p><b>Quyền của quý vị</b> không thay đổi: thông dịch viên miễn phí trong mọi cuộc họp, thư này bằng ngôn ngữ khác khi yêu cầu, quyền đến thăm và quyền từ chối dịch vụ bằng văn bản. Chúng tôi sẵn sàng họp với quý vị bất cứ lúc nào — chỉ cần gọi số bên dưới.</p>{SIG}`,
 exit: `<h3>Chúc mừng — {student} đã hoàn thành chương trình học sinh học tiếng Anh</h3>
<p>Kính gửi {parent},</p>
<p>Trong {test}, {student} (lớp {grade}) đã đạt tiêu chuẩn ra khỏi chương trình của tiểu bang — Mức 4 hoặc 5 ở cả bốn lĩnh vực:</p>{LV}
<p><b>Điều gì thay đổi.</b> Con quý vị nay là <b>cựu học sinh học tiếng Anh</b>. Việc phân loại EL và bài kiểm tra ELPT hằng năm chấm dứt. Lớp học, điểm số và yêu cầu tốt nghiệp không thay đổi.</p>
<p><b>Điều gì tiếp tục.</b> Theo luật, chúng tôi sẽ <b>theo dõi</b> điểm số và kết quả thi của con quý vị trong <b>bốn năm</b> tới. Nếu em bắt đầu gặp khó khăn liên quan đến ngôn ngữ, chúng tôi sẽ liên hệ với quý vị và có thể khởi động lại hỗ trợ. Các điều chỉnh trong lớp có thể tiếp tục nếu giáo viên thấy vẫn cần.</p>
<p><b>Đôi lời về thành tích này.</b> Học một ngôn ngữ thứ hai đủ tốt để làm bài đúng cấp lớp bằng ngôn ngữ đó là một trong những việc khó nhất mà một học sinh làm được. Xin nói với {child} rằng chúng tôi đã ghi nhận. Nếu gia đình vẫn nói tiếng mẹ đẻ ở nhà, hãy giữ gìn — học sinh thông thạo hai ngôn ngữ có thể đủ điều kiện nhận Dấu Song ngữ của Mississippi trên bằng tốt nghiệp.</p>{SIG}`,
 monitor: `<h3>Thông báo theo dõi dành cho cựu học sinh học tiếng Anh</h3>
<p>Kính gửi {parent},</p>
<p>{student} (lớp {grade}) đã ra khỏi chương trình học sinh học tiếng Anh và đang trong giai đoạn theo dõi bốn năm theo yêu cầu của luật liên bang. Thư này cho quý vị biết chúng tôi kiểm tra những gì và kết quả trong kỳ này.</p>
<div class="box"><b>Đã kiểm tra trong kỳ này:</b> điểm môn tiếng Anh, toán, khoa học và xã hội · kết quả thi tiểu bang · nhận xét của giáo viên · chuyên cần<br><b>Kết quả:</b> {RESULT}</div>
<p>Nếu đã thêm hỗ trợ, các hỗ trợ đó được ghi trong hồ sơ của em và giáo viên sẽ giải thích. Nếu chúng tôi đề nghị họp, xin gọi để sắp xếp; sẽ có thông dịch viên miễn phí. Việc trở lại dịch vụ EL cần sự đồng ý của quý vị và khởi động lại bài kiểm tra ELPT hằng năm.</p>
<p>Nếu quý vị nhận thấy điều gì ở nhà — làm bài tập lâu hơn nhiều, tránh đọc hoặc viết, điểm số giảm — xin cho chúng tôi biết. Quý vị thấy những điều chúng tôi không thể thấy.</p>{SIG}`,
 refuse: `<h3>Yêu cầu của phụ huynh từ chối dịch vụ học sinh học tiếng Anh</h3>
<p>Học sinh: {student} &nbsp; Lớp: {grade} &nbsp; Trường: {school} &nbsp; Ngày: {date}</p>
<p>Tôi, {parent}, đã được thông báo bằng ngôn ngữ tôi hiểu rằng con tôi đủ điều kiện nhận dịch vụ dành cho học sinh học tiếng Anh (EL), chương trình cung cấp những gì và lợi ích của việc tham gia. Tôi hiểu rằng:</p>
<ul>
<li>Tôi chọn <b>từ chối</b> chương trình EL (lớp ESL/ELD và/hoặc hỗ trợ EL trong hay ngoài lớp) cho năm học {year}.</li>
<li>Con tôi <b>vẫn được xác định là học sinh học tiếng Anh</b> theo luật liên bang và sẽ <b>làm bài kiểm tra tiếng Anh của tiểu bang (ELPT) mỗi mùa xuân</b> cho đến khi ra khỏi chương trình.</li>
<li>Nhà trường vẫn phải bảo đảm con tôi hiểu và tham gia mọi lớp học, và giáo viên vẫn dùng các hỗ trợ và điều chỉnh trong lớp và trong các kỳ thi.</li>
<li>Nhà trường sẽ theo dõi tiến bộ của con tôi và liên hệ với tôi nếu em gặp khó khăn.</li>
<li>Tôi có thể <b>thay đổi quyết định này bất cứ lúc nào</b> bằng cách viết thư cho nhà trường; dịch vụ sẽ bắt đầu lại ngay.</li>
</ul>
<p>Lý do (không bắt buộc): ___________________________________________________</p>
<div class="sig"><div>Chữ ký phụ huynh/người giám hộ · Ngày</div><div>{contact} · Đại diện nhà trường · Ngày</div></div>`,
 meet: `<h3>Kính mời: cuộc họp về kế hoạch học tiếng Anh của {student}</h3>
<p>Kính gửi {parent},</p>
<p>Chúng tôi muốn gặp quý vị để trao đổi về {student} (lớp {grade}) — tiếng Anh của em tiến triển ra sao, Kế hoạch Dịch vụ Ngôn ngữ năm nay và những gì chúng ta có thể cùng làm ở trường và ở nhà.</p>
<div class="box"><b>Thời gian và địa điểm:</b> {meeting}<br><b>Với:</b> {contact} và (các) giáo viên của em<br><b>Thông dịch viên:</b> miễn phí — {lang} · Xin cho chúng tôi biết nếu quý vị muốn dùng ngôn ngữ khác.<br><b>Mang theo (nếu có):</b> phiếu điểm hoặc giấy tờ từ trường cũ, câu hỏi, và {child} — học sinh được hoan nghênh.</div>
<p>Nếu giờ này không thuận tiện, xin gọi hoặc gửi email và chúng tôi sẽ tìm giờ khác, kể cả qua điện thoại hoặc video. Quý vị cũng có thể đưa bạn bè hoặc người thân đi cùng để hỗ trợ.</p>
<p>Xin gửi lại phiếu bên dưới hoặc gọi {phone}.</p>
<div class="box">☐ Có, tôi sẽ tham dự. &nbsp; ☐ Xin gọi cho tôi để đổi lịch. &nbsp; Số điện thoại tốt nhất: ____________________ &nbsp; Chữ ký: ____________________</div>{SIG}`
},

/* ───────────────────────────── العربية ───────────────────────────── */
ar: {
 d: { parent: "[ولي الأمر]", student: "[الطالب/ة]", child: "ابنكم/ابنتكم", grade: "__", lang: "[اللغة]", test: "[الاختبار، التاريخ]", program: "[وصف البرنامج]", year: "[العام الدراسي]", meeting: "[التاريخ، الوقت، المكان]", contact: "[مسؤول برنامج EL]", phone: "[الهاتف · البريد الإلكتروني]", school: "[المدرسة]", signer: "[الموقّع، الصفة]", overall: "________" },
 ui: { program: "برنامج متعلمي اللغة الإنجليزية", year: "العام الدراسي", sign: "التوقيع", L: "الاستماع", S: "التحدث", R: "القراءة", W: "الكتابة", O: "الإجمالي",
       foot: "يُقدَّم هذا الإشعار بموجب القانون الفيدرالي (ESSA §1112(e)(3)) والباب السادس من قانون الحقوق المدنية. يحق لكم الحصول على هذه المعلومات بلغة تفهمونها وعلى مترجم فوري مجاني في أي اجتماع. · إذا كنتم تفضلون لغة أخرى، فاتصلوا بالرقم أعلاه.",
       result: "☐ يتقدم جيدًا — لا حاجة لأي إجراء &nbsp; ☐ بعض القلق — أُضيف دعم داخل الصف &nbsp; ☐ نوصي بعقد اجتماع لمناقشة العودة إلى خدمات EL" },
 init: `<h3>تم تحديد ابنكم/ابنتكم كمتعلم للغة الإنجليزية — وماذا يعني ذلك</h3>
<p>عزيزي/عزيزتي {parent}،</p>
<p>عند تسجيلكم {student} (الصف {grade})، أظهر استبيان لغة المنزل أن {lang} هي اللغة المستخدمة في المنزل. وكما يقتضي القانون الفيدرالي، قامت المدرسة بقياس مستوى اللغة الإنجليزية لدى ابنكم/ابنتكم عبر {test}. النتائج:</p>{LV}
<p><b>لماذا هذا مهم.</b> بناءً على هذه النتائج، يستحق ابنكم/ابنتكم خدمات متعلمي اللغة الإنجليزية (EL). هذا <b>دعم وليس حكمًا</b>: فهو يعني أن المدرسة مسؤولة عن تعليم ابنكم/ابنتكم اللغة الإنجليزية <i>و</i>عن جعل كل حصة مفهومة في أثناء ذلك.</p>
<p><b>البرنامج.</b> {program} يبقى ابنكم/ابنتكم في صفوف مستوى الصف مع بقية الطلاب؛ يُضاف دعم EL ولا يحل محل أي شيء. وإذا كان لدى ابنكم/ابنتكم خطة IEP أو خطة 504، فتُنسَّق خدمات EL معها بحيث تُنفَّذ الخطتان.</p>
<p><b>كيف يُنهي ابنكم/ابنتكم البرنامج.</b> في كل ربيع يخضع ابنكم/ابنتكم لاختبار الولاية في اللغة الإنجليزية (ELPT). يخرج الطالب من البرنامج عندما يحقق المستوى 4 أو 5 في المجالات الأربعة جميعها. يحتاج معظم الطلاب إلى عدة سنوات؛ والتقدم بمقدار مستوى واحد تقريبًا في السنة أمر معتاد. وبعد الخروج، نتابع درجات ابنكم/ابنتكم لأربع سنوات أخرى.</p>
<p><b>التخرج.</b> يحصل متعلمو اللغة الإنجليزية على الشهادة نفسها وبالمتطلبات نفسها مثل أي طالب آخر. تتابع المدرسة معدل تخرج طلاب هذا البرنامج وتُبلّغ عنه؛ وسيعرض عليكم المرشد الأكاديمي خطة الساعات المعتمدة في أي وقت.</p>
<p><b>حقوقكم.</b> يمكنكم زيارة البرنامج، وطلب اجتماع مع مترجم فوري مجانًا، وطلب هذه الرسالة بلغة أخرى. ويمكنكم أيضًا <b>رفض</b> خدمات EL كتابيًا؛ وفي هذه الحالة سيستمر ابنكم/ابنتكم في أداء اختبار اللغة الإنجليزية السنوي وسيستمر في تلقي المساعدة داخل الصف، ويمكنكم تغيير قراركم في أي وقت.</p>
<p>يرجى الاتصال أو مراسلتنا بالبريد الإلكتروني لأي سؤال — نفضّل أن نسمع منكم على أن تبقوا في حيرة.</p>{SIG}`,
 annual: `<h3>إشعار سنوي: خدمات متعلمي اللغة الإنجليزية لابنكم/ابنتكم للعام {year}</h3>
<p>عزيزي/عزيزتي {parent}،</p>
<p>سيواصل {student} (الصف {grade}) تلقي خدمات متعلمي اللغة الإنجليزية (EL) هذا العام. وفي أحدث اختبار للولاية في اللغة الإنجليزية ({test}) كانت النتائج:</p>{LV}
<p><b>خطة هذا العام.</b> {program} المجال الذي سنركز عليه أكثر هو أدنى مستوى في الجدول أعلاه. لدى معلمي ابنكم/ابنتكم خطة خدمات لغوية مكتوبة تُدرج أشكال الدعم والتسهيلات التي يتلقاها في كل حصة وفي اختبارات الولاية.</p>
<p><b>شرط الخروج من البرنامج.</b> المستوى 4 أو 5 في المجالات الأربعة جميعها في اختبار ELPT في الربيع. الطلاب الذين يحققونه يخرجون من البرنامج وتتم متابعتهم لأربع سنوات.</p>
<p><b>حقوقكم</b> لم تتغير: مترجم فوري مجاني في أي اجتماع، وهذه الرسالة بلغة أخرى عند الطلب، وحق الزيارة، وحق رفض الخدمات كتابيًا. نرحب بعقد اجتماع في أي وقت — ما عليكم سوى الاتصال بالرقم أدناه.</p>{SIG}`,
 exit: `<h3>تهانينا — أكمل/أكملت {student} برنامج متعلمي اللغة الإنجليزية</h3>
<p>عزيزي/عزيزتي {parent}،</p>
<p>في {test}، حقق/حققت {student} (الصف {grade}) معيار الخروج الذي حددته الولاية — المستوى 4 أو 5 في المجالات الأربعة جميعها:</p>{LV}
<p><b>ما الذي يتغير.</b> أصبح ابنكم/ابنتكم الآن <b>متعلمًا سابقًا للغة الإنجليزية</b>. ينتهي تصنيف EL واختبار ELPT السنوي. ولا تتغير الحصص ولا الدرجات ولا متطلبات التخرج.</p>
<p><b>ما الذي يستمر.</b> بموجب القانون سوف <b>نتابع</b> درجات ابنكم/ابنتكم ونتائج اختباراته خلال <b>السنوات الأربع</b> القادمة. فإذا بدأ يواجه صعوبة مرتبطة باللغة، فسنتواصل معكم ويمكننا إعادة الدعم. ويمكن أن تستمر التسهيلات الصفية إذا رأى المعلم أنها ما زالت ضرورية.</p>
<p><b>كلمة عن هذا الإنجاز.</b> تعلّم لغة ثانية بما يكفي لأداء عمل مستوى الصف بها هو من أصعب ما يقوم به طالب. يرجى إخبار {child} بأننا لاحظنا ذلك. وإذا كانت لغة أسرتكم ما زالت تُستخدم في المنزل، فحافظوا عليها قوية — فالطلاب ثنائيو اللغة بالكامل قد يستحقون ختم ثنائية اللغة لولاية ميسيسيبي على الشهادة.</p>{SIG}`,
 monitor: `<h3>إشعار متابعة لمتعلم سابق للغة الإنجليزية</h3>
<p>عزيزي/عزيزتي {parent}،</p>
<p>خرج/خرجت {student} (الصف {grade}) من برنامج متعلمي اللغة الإنجليزية وهو/هي الآن في فترة المتابعة التي تمتد أربع سنوات والتي يقتضيها القانون الفيدرالي. تُخبركم هذه الرسالة بما نتحقق منه وبما وجدناه في هذه الفترة.</p>
<div class="box"><b>ما تم التحقق منه في هذه الفترة:</b> الدرجات في اللغة الإنجليزية والرياضيات والعلوم والدراسات الاجتماعية · نتائج اختبارات الولاية · تقارير المعلمين · الحضور<br><b>النتيجة:</b> {RESULT}</div>
<p>إذا أُضيف دعم، فهو مدوَّن في ملف ابنكم/ابنتكم وسيشرحه المعلم. وإذا أوصينا بعقد اجتماع، فيرجى الاتصال لتحديد موعده؛ وسيُوفَّر مترجم فوري مجانًا. تتطلب العودة إلى خدمات EL موافقتكم وتُعيد اختبار ELPT السنوي.</p>
<p>إذا لاحظتم أي شيء في المنزل — الواجبات تستغرق وقتًا أطول بكثير، أو تجنّب القراءة أو الكتابة، أو انخفاض الدرجات — فيرجى إخبارنا. فأنتم ترون ما لا نستطيع رؤيته.</p>{SIG}`,
 refuse: `<h3>طلب ولي الأمر رفض خدمات متعلمي اللغة الإنجليزية</h3>
<p>الطالب/ة: {student} &nbsp; الصف: {grade} &nbsp; المدرسة: {school} &nbsp; التاريخ: {date}</p>
<p>أنا، {parent}، قد أُبلغت بلغة أفهمها بأن ابني/ابنتي يستحق خدمات متعلمي اللغة الإنجليزية (EL)، وبما يقدمه البرنامج، وبفوائد المشاركة فيه. وأفهم ما يلي:</p>
<ul>
<li>أختار <b>رفض</b> برنامج EL (حصة ESL/ELD و/أو دعم EL داخل الصف أو خارجه) للعام الدراسي {year}.</li>
<li>يبقى ابني/ابنتي <b>مصنَّفًا كمتعلم للغة الإنجليزية</b> بموجب القانون الفيدرالي وسوف <b>يؤدي اختبار الولاية في اللغة الإنجليزية (ELPT) كل ربيع</b> حتى الخروج من البرنامج.</li>
<li>تظل المدرسة ملزمة بضمان أن يفهم ابني/ابنتي كل حصة ويشارك فيها، وسيستمر المعلمون في استخدام أشكال الدعم والتسهيلات في الصف وفي الاختبارات.</li>
<li>ستتابع المدرسة تقدم ابني/ابنتي وستتواصل معي إذا واجه صعوبة.</li>
<li>يمكنني <b>تغيير هذا القرار في أي وقت</b> بالكتابة إلى المدرسة؛ وتُستأنف الخدمات فورًا.</li>
</ul>
<p>السبب (اختياري): ___________________________________________________</p>
<div class="sig"><div>توقيع ولي الأمر · التاريخ</div><div>{contact} · ممثل المدرسة · التاريخ</div></div>`,
 meet: `<h3>دعوة: اجتماع حول خطة تعلم اللغة الإنجليزية لـ{student}</h3>
<p>عزيزي/عزيزتي {parent}،</p>
<p>نود الاجتماع بكم للحديث عن {student} (الصف {grade}) — كيف يسير تعلم اللغة الإنجليزية، وخطة الخدمات اللغوية لهذا العام، وما يمكننا فعله معًا في المدرسة والمنزل.</p>
<div class="box"><b>الزمان والمكان:</b> {meeting}<br><b>مع:</b> {contact} ومعلم/معلمي ابنكم/ابنتكم<br><b>المترجم الفوري:</b> يُوفَّر مجانًا — {lang} · يرجى إخبارنا إذا كنتم تفضلون لغة أخرى.<br><b>أحضروا معكم (إن وُجد):</b> كشوف الدرجات أو أوراقًا من المدرسة السابقة، وأسئلتكم، و{child} — الطلاب مرحَّب بهم.</div>
<p>إذا لم يناسبكم هذا الموعد، فاتصلوا أو راسلونا وسنجد موعدًا مناسبًا، بما في ذلك عبر الهاتف أو الفيديو. ويمكنكم أيضًا إحضار صديق أو أحد أفراد الأسرة للدعم.</p>
<p>يرجى إعادة القسيمة أدناه أو الاتصال بالرقم {phone}.</p>
<div class="box">☐ نعم، سأحضر. &nbsp; ☐ يرجى الاتصال بي لتغيير الموعد. &nbsp; أفضل رقم هاتف: ____________________ &nbsp; التوقيع: ____________________</div>{SIG}`
},

/* ───────────────────────────── 中文（简体） ───────────────────────────── */
zh: {
 d: { parent: "[家长/监护人]", student: "[学生]", child: "您的孩子", grade: "__", lang: "[语言]", test: "[测试名称、日期]", program: "[项目说明]", year: "[学年]", meeting: "[日期、时间、地点]", contact: "[EL 联系人]", phone: "[电话 · 电子邮件]", school: "[学校]", signer: "[签署人、职务]", overall: "________" },
 ui: { program: "英语学习者项目", year: "学年", sign: "签名", L: "听力", S: "口语", R: "阅读", W: "写作", O: "总体",
       foot: "本通知依据联邦法律（ESSA §1112(e)(3)）和《民权法案》第六章发出。您有权以自己能理解的语言获得这些信息，并在任何会议上获得免费口译服务。· 如需其他语言，请拨打上方电话。",
       result: "☐ 进步良好——无需采取行动 &nbsp; ☐ 略有担忧——已在课堂上增加支持 &nbsp; ☐ 建议召开会议，讨论重新加入 EL 服务" },
 init: `<h3>您的孩子已被认定为英语学习者——这意味着什么</h3>
<p>尊敬的{parent}：</p>
<p>您为{student}（{grade}年级）办理入学时，《家庭语言调查》显示家中使用{lang}。按照联邦法律的要求，学校随后通过{test}评估了孩子的英语水平。结果如下：</p>{LV}
<p><b>为什么这很重要。</b>根据这些结果，您的孩子有资格获得英语学习者（EL）服务。这是<b>支持，而不是评判</b>：它意味着学校有责任教您的孩子英语，<i>同时</i>在此期间让每一堂课都能被孩子理解。</p>
<p><b>项目内容。</b>{program} 您的孩子将与其他同学一起留在年级常规班级中；EL 支持是额外增加的，绝不取代任何课程。如果孩子有 IEP 或 504 计划，EL 服务将与之协调，确保两项计划都得到落实。</p>
<p><b>孩子如何完成项目。</b>每年春季，孩子将参加州英语测试（ELPT）。学生在四个领域均达到 4 级或 5 级时即可退出项目。大多数学生需要几年时间；每年进步约一个等级是正常的。退出后，我们还会继续关注孩子的成绩四年。</p>
<p><b>毕业。</b>英语学习者获得与其他所有学生相同的文凭，要求也相同。学校会跟踪并报告本项目学生的毕业率；您孩子的升学辅导员随时可以向您展示学分计划。</p>
<p><b>您的权利。</b>您可以参观项目、要求安排带免费口译的会议，并要求以其他语言提供本信函。您也可以书面<b>拒绝</b> EL 服务；如果您这样做，孩子仍将参加每年的英语测试并在课堂上继续获得帮助，而且您随时可以改变主意。</p>
<p>如有任何疑问，请致电或发送电子邮件——我们宁愿听到您的声音，也不愿让您心存疑虑。</p>{SIG}`,
 annual: `<h3>年度通知：{year}学年您孩子的英语学习者服务</h3>
<p>尊敬的{parent}：</p>
<p>{student}（{grade}年级）本学年将继续接受英语学习者（EL）服务。在最近一次州英语测试（{test}）中，结果如下：</p>{LV}
<p><b>本学年计划。</b>{program} 我们将重点关注上表中等级最低的领域。孩子的各科老师都持有一份书面《语言服务计划》，其中列出了孩子在每一堂课和州考试中获得的支持与便利措施。</p>
<p><b>退出要求。</b>在春季 ELPT 中四个领域均达到 4 级或 5 级。达标的学生将退出项目并接受四年的跟踪。</p>
<p><b>您的权利</b>保持不变：任何会议均提供免费口译、可应要求以其他语言提供本信函、有权参观、有权书面拒绝服务。我们随时欢迎您前来面谈——请拨打下方电话。</p>{SIG}`,
 exit: `<h3>祝贺——{student}已完成英语学习者项目</h3>
<p>尊敬的{parent}：</p>
<p>在{test}中，{student}（{grade}年级）达到了州退出标准——四个领域均为 4 级或 5 级：</p>{LV}
<p><b>有何变化。</b>您的孩子现在是<b>前英语学习者</b>。EL 身份和每年的 ELPT 测试到此结束。课程、成绩和毕业要求均不变。</p>
<p><b>有何延续。</b>依法我们将在未来<b>四年</b>内继续<b>跟踪</b>孩子的成绩和考试分数。如果孩子出现与语言相关的困难，我们会联系您，并可以重新提供支持。如果老师认为课堂便利措施仍有必要，可以继续提供。</p>
<p><b>关于这项成就。</b>把第二语言学到足以用它完成年级水平的学业，是学生能做到的最难的事情之一。请告诉{child}，我们看到了。如果家里仍在使用你们的母语，请继续保持——完全双语的学生可能有资格在文凭上获得密西西比州双语能力印章。</p>{SIG}`,
 monitor: `<h3>前英语学习者跟踪通知</h3>
<p>尊敬的{parent}：</p>
<p>{student}（{grade}年级）已退出英语学习者项目，目前处于联邦法律规定的四年跟踪期。本信函告知您我们检查了哪些内容以及本期的结果。</p>
<div class="box"><b>本期检查内容：</b>英语、数学、科学和社会研究的成绩 · 州考试结果 · 教师反馈 · 出勤<br><b>结果：</b>{RESULT}</div>
<p>如已增加支持，相关内容记录在孩子的档案中，老师会向您说明。如我们建议召开会议，请致电安排；会议将提供免费口译。重新加入 EL 服务需要您的同意，并将重新开始每年的 ELPT 测试。</p>
<p>如果您在家中注意到任何情况——作业用时明显变长、回避阅读或写作、成绩下降——请告诉我们。您能看到我们看不到的情况。</p>{SIG}`,
 refuse: `<h3>家长拒绝英语学习者服务申请</h3>
<p>学生：{student} &nbsp; 年级：{grade} &nbsp; 学校：{school} &nbsp; 日期：{date}</p>
<p>本人{parent}已以本人能理解的语言获知：我的孩子有资格获得英语学习者（EL）服务，项目提供的内容，以及参加的益处。本人理解：</p>
<ul>
<li>本人选择<b>拒绝</b>{year}学年的 EL 项目（ESL/ELD 课程和/或课内外 EL 支持）。</li>
<li>根据联邦法律，我的孩子<b>仍被认定为英语学习者</b>，并将<b>每年春季参加州英语测试（ELPT）</b>，直至退出项目。</li>
<li>学校仍须确保我的孩子能够理解并参与每一堂课，老师仍将在课堂和考试中使用支持与便利措施。</li>
<li>学校将跟踪我孩子的进步，如孩子遇到困难会与我联系。</li>
<li>本人可以<b>随时改变此决定</b>，只需书面通知学校；服务将立即恢复。</li>
</ul>
<p>原因（选填）：___________________________________________________</p>
<div class="sig"><div>家长/监护人签名 · 日期</div><div>{contact} · 学校代表 · 日期</div></div>`,
 meet: `<h3>诚邀您参加：关于{student}英语学习计划的会议</h3>
<p>尊敬的{parent}：</p>
<p>我们希望与您面谈，讨论{student}（{grade}年级）的情况——英语学习进展、本学年的《语言服务计划》，以及我们在学校和家中可以共同做些什么。</p>
<div class="box"><b>时间与地点：</b>{meeting}<br><b>参会人员：</b>{contact}及孩子的任课老师<br><b>口译：</b>免费提供——{lang} · 如需其他语言，请告知我们。<br><b>请携带（如有）：</b>以前学校的成绩单或资料、您的问题，以及{child}——欢迎学生一同参加。</div>
<p>如果这个时间不方便，请致电或发送电子邮件，我们会另行安排，包括电话或视频方式。您也可以带一位朋友或家人陪同。</p>
<p>请交回下方回执或致电{phone}。</p>
<div class="box">☐ 是，我会参加。&nbsp; ☐ 请致电我改期。&nbsp; 最佳联系电话：____________________ &nbsp; 签名：____________________</div>{SIG}`
},

/* ───────────────────────────── KREYÒL AYISYEN ───────────────────────────── */
ht: {
 d: { parent: "[Paran/responsab]", student: "[elèv]", child: "pitit ou", grade: "__", lang: "[lang]", test: "[tès, dat]", program: "[deskripsyon pwogram nan]", year: "[ane]", meeting: "[dat, lè, kote]", contact: "[kontak EL]", phone: "[telefòn · imel]", school: "[lekòl]", signer: "[Moun ki siyen, tit]", overall: "________" },
 ui: { program: "Pwogram Elèv k ap Aprann Anglè", year: "Ane eskolè", sign: "Siyati", L: "Koute", S: "Pale", R: "Li", W: "Ekri", O: "Jeneral",
       foot: "Avi sa a bay dapre lwa federal (ESSA §1112(e)(3)) ak Tit VI Lwa sou Dwa Sivil yo. Ou gen dwa resevwa enfòmasyon sa a nan yon lang ou konprann epi gen yon entèprèt gratis nan nenpòt reyinyon. · Si ou pito yon lòt lang, rele nimewo ki anwo a.",
       result: "☐ L ap pwogrese byen — pa gen aksyon ki nesesè &nbsp; ☐ Yon ti enkyetid — nou ajoute sipò nan klas &nbsp; ☐ Nou rekòmande yon reyinyon pou pale sou retounen nan sèvis EL yo" },
 init: `<h3>Yo idantifye pitit ou kòm yon elèv k ap aprann anglè — e sa sa vle di</h3>
<p>Chè {parent},</p>
<p>Lè ou te enskri {student} (klas {grade}), Sondaj sou Lang Lakay la te montre yo pale {lang} lakay. Jan lwa federal la mande sa, lekòl la te mezire anglè pitit ou a ak {test}. Men rezilta yo:</p>{LV}
<p><b>Poukisa sa enpòtan.</b> Akòz rezilta sa yo, pitit ou kalifye pou sèvis elèv k ap aprann anglè (EL). Sa se <b>yon sipò, se pa yon jijman</b>: sa vle di lekòl la responsab pou anseye pitit ou anglè <i>epi</i> pou fè chak klas konprann pandan tan sa a.</p>
<p><b>Pwogram nan.</b> {program} Pitit ou rete nan klas nivo li yo ak tout lòt elèv yo; sipò EL la ajoute, li pa janm ranplase anyen. Si pitit ou gen yon IEP oswa yon plan 504, sèvis EL yo kowòdone avèk li pou tou de plan yo respekte.</p>
<p><b>Kijan pitit ou fini pwogram nan.</b> Chak prentan pitit ou pase tès anglè leta a (ELPT). Yon elèv soti nan pwogram nan lè li jwenn Nivo 4 oswa 5 nan tout kat domèn yo. Pifò elèv bezwen plizyè ane; pwogrese apeprè yon nivo pa ane se nòmal. Apre li soti, nou kontinye verifye nòt li yo pandan kat ane anplis.</p>
<p><b>Gradyasyon.</b> Elèv k ap aprann anglè yo jwenn menm diplòm nan ak menm egzijans yo tankou tout lòt elèv. Lekòl la swiv epi rapòte to gradyasyon elèv pwogram sa a; konseye pitit ou a ap montre ou plan kredi yo nenpòt lè.</p>
<p><b>Dwa ou yo.</b> Ou ka vizite pwogram nan, mande yon reyinyon ak yon entèprèt gratis, epi mande lèt sa a nan yon lòt lang. Ou ka tou <b>refize</b> sèvis EL yo alekri; si ou fè sa, pitit ou ap toujou pase tès anglè chak ane a epi l ap toujou resevwa èd nan klas, epi ou ka chanje lide nenpòt lè.</p>
<p>Tanpri rele oswa voye yon imel pou nenpòt kesyon — nou pito tande ou pase kite ou ap mande tèt ou.</p>{SIG}`,
 annual: `<h3>Avi anyèl: sèvis elèv k ap aprann anglè pou pitit ou pou {year}</h3>
<p>Chè {parent},</p>
<p>{student} (klas {grade}) ap kontinye resevwa sèvis elèv k ap aprann anglè (EL) ane sa a. Nan dènye tès anglè leta a ({test}) rezilta yo te:</p>{LV}
<p><b>Plan ane sa a.</b> {program} Domèn n ap konsantre sou li plis la se nivo ki pi ba a anwo a. Pwofesè pitit ou yo gen yon Plan Sèvis Lang alekri ki bay lis sipò ak akomodasyon pitit ou resevwa nan chak klas ak nan tès leta yo.</p>
<p><b>Egzijans pou soti.</b> Nivo 4 oswa 5 nan tout kat domèn yo nan ELPT prentan an. Elèv ki rive la soti nan pwogram nan epi yo swiv yo pandan kat ane.</p>
<p><b>Dwa ou yo</b> pa chanje: yon entèprèt gratis nan nenpòt reyinyon, lèt sa a nan yon lòt lang si ou mande l, dwa pou vizite, ak dwa pou refize sèvis yo alekri. Nou akeyi yon reyinyon nenpòt lè — jis rele nimewo ki anba a.</p>{SIG}`,
 exit: `<h3>Felisitasyon — {student} fini pwogram elèv k ap aprann anglè a</h3>
<p>Chè {parent},</p>
<p>Nan {test}, {student} (klas {grade}) rive nan estanda leta pou soti a — Nivo 4 oswa 5 nan tout kat domèn yo:</p>{LV}
<p><b>Sa ki chanje.</b> Pitit ou se kounye a yon <b>ansyen elèv k ap aprann anglè</b>. Etikèt EL la ak tès ELPT chak ane a fini. Klas yo, nòt yo ak egzijans gradyasyon yo pa chanje.</p>
<p><b>Sa ki kontinye.</b> Dapre lwa a n ap <b>swiv</b> nòt ak rezilta tès pitit ou pandan <b>kat ane</b> k ap vini yo. Si pitit ou kòmanse gen difikilte ki gen rapò ak lang, n ap kontakte ou epi nou ka rekòmanse sipò a. Akomodasyon nan klas yo ka kontinye si yon pwofesè wè yo toujou nesesè.</p>
<p><b>Yon mo sou reyalizasyon sa a.</b> Aprann yon dezyèm lang ase byen pou fè travay nivo klas ou ladan l se youn nan bagay ki pi difisil yon elèv fè. Tanpri di {child} nou remake sa. Si lang fanmi ou toujou pale lakay, kenbe l fò — elèv ki vrèman bileng ka kalifye pou So Bilitera Mississippi a sou diplòm yo.</p>{SIG}`,
 monitor: `<h3>Avi swivi pou yon ansyen elèv k ap aprann anglè</h3>
<p>Chè {parent},</p>
<p>{student} (klas {grade}) soti nan pwogram elèv k ap aprann anglè a epi li nan peryòd swivi kat ane lwa federal la mande a. Lèt sa a se pou di ou sa nou verifye ak sa nou jwenn nan peryòd sa a.</p>
<div class="box"><b>Sa nou verifye nan peryòd sa a:</b> nòt nan anglè, matematik, syans ak syans sosyal · rezilta tès leta yo · rapò pwofesè yo · prezans<br><b>Rezilta:</b> {RESULT}</div>
<p>Si nou te ajoute sipò, yo nan dosye pitit ou a epi pwofesè a ap eksplike yo. Si nou rekòmande yon reyinyon, tanpri rele pou pwograme l; y ap bay yon entèprèt gratis. Pou retounen nan sèvis EL yo, fòk ou dakò, epi sa rekòmanse tès ELPT chak ane a.</p>
<p>Si ou remake yon bagay lakay — devwa yo pran pi plis tan, li evite li oswa ekri, nòt yo bese — tanpri di nou sa. Ou wè bagay nou pa ka wè.</p>{SIG}`,
 refuse: `<h3>Demann paran pou refize sèvis elèv k ap aprann anglè yo</h3>
<p>Elèv: {student} &nbsp; Klas: {grade} &nbsp; Lekòl: {school} &nbsp; Dat: {date}</p>
<p>Mwen menm, {parent}, yo te enfòme m nan yon lang mwen konprann ke pitit mwen kalifye pou sèvis elèv k ap aprann anglè (EL), sa pwogram nan ofri, ak avantaj pou patisipe. Mwen konprann ke:</p>
<ul>
<li>Mwen chwazi <b>refize</b> pwogram EL la (klas ESL/ELD ak/oswa sipò EL anndan oswa deyò klas la) pou ane eskolè {year} la.</li>
<li>Pitit mwen <b>rete idantifye kòm yon elèv k ap aprann anglè</b> dapre lwa federal la epi l ap <b>pase tès anglè leta a (ELPT) chak prentan</b> jiskaske li soti nan pwogram nan.</li>
<li>Lekòl la toujou dwe asire pitit mwen ka konprann epi patisipe nan chak klas, epi pwofesè yo ap toujou itilize sipò ak akomodasyon nan klas ak nan tès yo.</li>
<li>Lekòl la ap swiv pwogrè pitit mwen epi l ap kontakte m si pitit mwen gen difikilte.</li>
<li>Mwen ka <b>chanje desizyon sa a nenpòt lè</b> lè m ekri lekòl la; sèvis yo rekòmanse touswit.</li>
</ul>
<p>Rezon (si ou vle): ___________________________________________________</p>
<div class="sig"><div>Siyati paran/responsab · Dat</div><div>{contact} · Reprezantan lekòl la · Dat</div></div>`,
 meet: `<h3>Nou envite ou: yon reyinyon sou plan aprantisaj anglè {student}</h3>
<p>Chè {parent},</p>
<p>Nou ta renmen rankontre ou pou pale sou {student} (klas {grade}) — kijan anglè a ap avanse, Plan Sèvis Lang pou ane sa a, ak sa nou ka fè ansanm lekòl ak lakay.</p>
<div class="box"><b>Kilè ak ki kote:</b> {meeting}<br><b>Avèk:</b> {contact} ak pwofesè pitit ou (yo)<br><b>Entèprèt:</b> gratis — {lang} · Tanpri di nou si ou pito yon lòt lang.<br><b>Pote (si ou genyen yo):</b> bilten oswa papye ki soti nan ansyen lekòl la, kesyon, ak {child} — elèv yo byenvini.</div>
<p>Si lè sa a pa bon pou ou, rele oswa voye yon imel epi n ap jwenn yon lòt, menm pa telefòn oswa videyo. Ou ka vini ak yon zanmi oswa yon manm fanmi pou sipò tou.</p>
<p>Tanpri retounen ti fèy ki anba a oswa rele {phone}.</p>
<div class="box">☐ Wi, m ap vini. &nbsp; ☐ Tanpri rele m pou chanje dat la. &nbsp; Pi bon nimewo telefòn: ____________________ &nbsp; Siyati: ____________________</div>{SIG}`
}
};
