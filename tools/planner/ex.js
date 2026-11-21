/* Example texts for ELA standards, taken from CommonLit's own published lists and a ReadWorks passage list. Checked November 21, 2026.
   EXT: id -> [title, author, grade, library, direct link or ""]. EXM: standard -> grade band -> [[id, why it fits]]. */
const CL="https://www.commonlit.org/texts/",CLLIB="https://www.commonlit.org/text-library",RWLIB="https://www.readworks.org/find-content";
const EXT={
eleven:["Eleven","Sandra Cisneros","5","CommonLit",""],jasmine:["Jasmine Girl","Jey Manokaran","3","CommonLit",""],champion:["The Champion of Quiet","Tracy Stewart","4","CommonLit",""],
cobra:["Cobra Kite","Mahani Zubaidy Gunnel","4","CommonLit",""],marble:["Marble Champ","Gary Soto","","CommonLit",""],secret:["A Secret Code","Christine Henderson","","CommonLit",""],
dream:["Sometimes a Dream Needs a Push","Walter Dean Myers","","CommonLit",""],zebra:["Zebra and Wasp","Clare Mishica","3","CommonLit",""],twodollars:["Two Dollars","Sharona F. Vedol","","CommonLit",""],hazel:["Hazel Grove","Leslie Barnard Booth","","CommonLit",""],
tsunami:["Tsunami","JonArno Lawson","3","CommonLit",CL+"tsunami"],impossibles:["The Impossibles","J. Patrick Lewis","4","CommonLit",CL+"the-impossibles"],dearsky:["Dear Sky","Naomi Shihab Nye","5","CommonLit",CL+"dear-sky"],
antarctica:["What is Antarctica?","","3","CommonLit",""],icecream:["We All Scream for Ice Cream","","4","CommonLit",""],inventors:["Are Animals Inventors?","Gail Jarrow and Paul Sherman","4","CommonLit",""],
braille:["Making Books in Braille","Sara Matson","3","CommonLit",""],solar:["Learning About the Solar System","Barbara Radner","4","CommonLit",""],bessie:["Fly High, Bessie Coleman","Jane Sutcliffe","4","CommonLit",""],
frida:["Frida Kahlo","Jessica McBirney","5","CommonLit",""],mlk5:["Dr. Martin Luther King Jr., Changing America","Barbara Radner","5","CommonLit",""],pumpkins:["These Pumpkins Sure Can Kick!","Patricia Cuff","4","CommonLit",""],
pixar:["How Pixar Tells a Story","Rachel Slivnick","4","CommonLit",""],plastic:["The Plastic Problem","Jacqueline Pratt-Tuke","5","CommonLit",""],chavez:["Sí Se Puede! The Legacy of Cesar E. Chavez","Carlos Lossada","3","CommonLit",""],
girlsfootball:["Should Girls Be Allowed to Play High School Football?","","","CommonLit",""],
insideout:["Inside Out","Francisco Jiménez","6","CommonLit",CL+"fyc-inside-out"],button:["Button, Button","Richard Matheson","7","CommonLit",CL+"fyc-button-button"],party:["The Party","Pam Muñoz Ryan","7","CommonLit",CL+"the-party"],
fanclub:["The Fan Club","Rona Maynard","7","CommonLit",CL+"the-fan-club"],lather:["Lather and Nothing Else","Hernando Téllez","8","CommonLit",CL+"fyc-lather-and-nothing-else"],stoneboy:["The Stone Boy","Gina Berriault","8","CommonLit",CL+"the-stone-boy"],
lastdog:["The Last Dog","Katherine Paterson","8","CommonLit",CL+"the-last-dog"],thankyou:["Thank You, M'am","Langston Hughes","7","CommonLit",""],selfish:["The Selfish Giant","Oscar Wilde","6","CommonLit",""],
sidewalk:["Where the Sidewalk Ends","Shel Silverstein","6","CommonLit",""],lovefriend:["Love and Friendship","Emily Brontë","8","CommonLit",""],
fishcheeks:["Fish Cheeks","Amy Tan","6","CommonLit","https://www.commonlit.org/en/texts/fish-cheeks"],names:["Names/Nombres","Julia Alvarez","6","CommonLit",""],drivein:["The Drive-In Movies","Gary Soto","6","CommonLit",""],
herd:["Herd Behavior","CommonLit Staff","7","CommonLit",""],cinco:["Celebrating Cinco de Mayo","Sanjana Chetia","6","CommonLit",""],
malala:["Malala Yousafzai's Nobel Peace Prize Lecture","Malala Yousafzai","8","CommonLit",CL+"malala-yousafzai-s-nobel-lecture"],wiesel8:["Elie Wiesel's Nobel Acceptance Speech","Elie Wiesel","8","CommonLit",CL+"elie-wiesel-s-nobel-lecture"],
itoo:["I, Too","Langston Hughes","9","CommonLit",""],bergeron:["Harrison Bergeron","Kurt Vonnegut","9","CommonLit",""],lottery:["The Lottery","Shirley Jackson","9","CommonLit",""],
eraser:["Eraser Tattoo","Jason Reynolds","10","CommonLit",""],sound:["A Sound of Thunder","Ray Bradbury","10","CommonLit",""],aandp:["A&P","John Updike","11","CommonLit",""],
sweat:["Sweat","Zora Neale Hurston","12","CommonLit",""],oldman:["A Very Old Man With Enormous Wings","Gabriel García Márquez","12","CommonLit",""],
gold:["Nothing Gold Can Stay","Robert Frost","9","CommonLit",""],sonnet17:["Sonnet XVII","Pablo Neruda","10","CommonLit",""],dickinson:["Because I Could Not Stop for Death","Emily Dickinson","11","CommonLit",""],
summerjob:["Endless Summer Job","Carolyn Ferrell","9","CommonLit",""],douglass:["The Narrative of the Life of Frederick Douglass: Excerpts from Chapters 1 and 7","Frederick Douglass","9","CommonLit",""],alexie:["You Don't Have to Say You Love Me (excerpt)","Sherman Alexie","10","CommonLit",""],
youthsports:["The Pros and Cons of Youth Sports Aren't Only Physical","Dr. Marika Lindholm","9","CommonLit",""],phones:["No, Mobile Phones Should Not Be Banned in UK Schools","Stephen Corbett","9","CommonLit",""],lifefair:["Life Isn't Fair - Deal With It","Mike Myatt","9","CommonLit",""],
gatsby:["Why I Despise The Great Gatsby","Kathryn Schulz","11","CommonLit",""],fallacy:["The Fallacy of Success","G.K. Chesterton","11","CommonLit",""],staples:["What Adolescents Miss When We Let Them Grow Up In Cyberspace","Brent Staples","12","CommonLit",""],
dream10:["American Dream Faces Harsh New Reality","Ari Shapiro","10","CommonLit","https://www.commonlit.org/en/texts/american-dream-faces-harsh-new-reality"],facebook:["Here's what happens when you 'like' a brand on Facebook","Alisha Horky and Mark J. Pelletier","10","CommonLit",""],
goodbad:["What makes good people do bad things?","Melissa Dittmann","11","CommonLit",""],wieselbio:["Elie Wiesel","United States Holocaust Memorial Museum","9","CommonLit",CL+"elie-wiesel"],
mandela:["Nelson Mandela's Nobel Peace Prize Lecture","Nelson Mandela","9","CommonLit",CL+"nelson-mandela-nobel-lecture"],obama:["Barack Obama's Nobel Lecture","Barack Obama","10","CommonLit",CL+"barack-obama-s-nobel-lecture"],
kingnobel:["Martin Luther King, Jr. Nobel Acceptance Speech","Martin Luther King, Jr.","11","CommonLit",CL+"martin-luther-king-jr-nobel-acceptance-speech"],carter:["Jimmy Carter's Nobel Lecture","Jimmy Carter","11","CommonLit",CL+"jimmy-carter-s-nobel-lecture"],
liberty:["The Liberty Bell","","K","ReadWorks",""],americans:["We Are Americans","","K","ReadWorks",""],alaska:["Getting Around Alaska","","K","ReadWorks",""],playground:["Fun on the Playground","","K","ReadWorks",""],daykinder:["A Day in Kindergarten","","K","ReadWorks",""]};
const EXM={
RL1:{b35:[["eleven","Find the details that show how the narrator feels and what she does not say aloud."],["jasmine","Use details from the story to explain the choice the main character makes."],["champion","Point to the details that show why the shy student's choice is brave."]],
 b68:[["stoneboy","Infer what the boy feels from the way other people talk about him."],["button","Cite the lines that build tension between the two characters."],["thankyou","Infer why Mrs. Jones treats Roger the way she does."]],
 b912:[["lottery","Cite the clues that foreshadow the ending."],["aandp","Use evidence to trace how the narrator's view changes."],["bergeron","Cite the details that show what forced equality costs the characters."]]},
RL2:{b35:[["zebra","A fable, so the lesson is easy to find and state."],["marble","Theme of determination. A Spanish version, Campeona de canicas, is also in the library."],["secret","Themes of friendship and accepting differences."]],
 b68:[["thankyou","Trace how one act of kindness develops the theme."],["fanclub","Themes of integrity and fitting in."],["selfish","Theme of how love is shown to others."]],
 b912:[["bergeron","What does equality mean? The theme builds across the whole story."],["sound","Theme of small actions with large consequences."],["itoo","A short poem with a clear theme of identity and equality."]]},
RL3:{b35:[["dream","Follow how the main character changes with his family's support."],["champion","Describe the character before and after the choice."],["eleven","Describe the narrator using her thoughts, words, and actions."]],
 b68:[["lastdog","Track how the character develops through caring for the dog."],["stoneboy","See how other characters' reactions shape the main character."],["lather","A whole story built on one character's inner conflict."]],
 b912:[["aandp","Analyze how the narrator's perspective changes scene by scene."],["sweat","Analyze how the two main characters act on each other. Preview first for mature content."],["oldman","Analyze how the townspeople respond to the stranger."]]},
RL4:{b35:[["tsunami","Simile."],["impossibles","Metaphor."],["dearsky","Personification."]],
 b68:[["sidewalk","Alliteration and imagery."],["lovefriend","Extended metaphor."],["insideout","Symbolism. The narrator is a child who is learning English."]],
 b912:[["gold","Personification in eight short lines."],["sonnet17","Juxtaposition. The poet wrote in Spanish."],["eraser","Symbolism."]]},
RI1:{bk2:[["liberty","A short passage for finding one detail that answers a question."],["americans","Students point to the sentence that answers each question."]],
 b35:[["braille","Use details to explain how braille books are made."],["bessie","Use details to explain what Bessie Coleman overcame."],["pumpkins","Use details to explain why the team matters to the girls."]],
 b68:[["cinco","Cite evidence about what the holiday does and does not celebrate."],["herd","Cite the examples the author uses to support each idea."],["malala","Cite the evidence Malala gives for educating every child."]],
 b912:[["dream10","Cite evidence for how the American Dream is changing."],["goodbad","Cite the findings the author uses from the prison experiment."],["wieselbio","Cite evidence for Wiesel's influence on human rights work."]]},
RI2:{bk2:[["alaska","Students tell what the passage is mostly about."],["daykinder","A familiar topic for naming the main topic and two details."]],
 b35:[["antarctica","Part of CommonLit's main idea lessons."],["icecream","Part of CommonLit's main idea lessons."],["inventors","Part of CommonLit's main idea lessons."]],
 b68:[["herd","One clear central idea developed with examples."],["cinco","Summarize the history in a few sentences."],["wiesel8","Find the central idea of a short speech."]],
 b912:[["goodbad","Trace how the central idea develops through the research."],["facebook","Summarize the study and its findings objectively."],["dream10","Find the central idea and the evidence behind it."]]},
RI4:{bk2:[["playground","Everyday words students can match to pictures."],["liberty","Teach two or three social studies words before reading."]],
 b35:[["solar","Subject words about space."],["plastic","Science and environment words."],["pixar","Storytelling terms students already know from films."]],
 b68:[["herd","Social science terms explained in context."],["malala","Abstract words such as rights and education, used in a speech."],["wiesel8","Word choice that carries moral weight."]],
 b912:[["goodbad","Psychology terms defined through examples."],["mandela","Figurative language in a formal speech."],["facebook","Marketing and research terms."]]},
RI8:{b35:[["plastic","Find the problem, the reasons, and the solutions the author gives."],["girlsfootball","A question with two sides. The grade level is not listed, so preview it first."]],
 b68:[["malala","Trace the claim that every child deserves an education and the support for it."],["wiesel8","Evaluate the argument for speaking up against injustice."]],
 b912:[["youthsports","Evaluate claims and evidence on both sides."],["phones","A clear claim students can test against the evidence."],["staples","An opinion piece that will start a debate."]]},
W1:{b35:[["girlsfootball","A mentor text for taking a side and giving reasons. Preview it first; the grade level is not listed."],["plastic","Students use its facts as evidence for their own opinion."]],
 b68:[["malala","A model of a claim supported with reasons and personal evidence."],["wiesel8","A model of a short, forceful argument."]],
 b912:[["phones","A model of claim, reasons, and counterclaim."],["lifefair","Students argue for or against the author's claim."],["gatsby","A model of a strong opinion that students can evaluate."]]},
W2:{b35:[["bessie","A model biography."],["frida","A model biography with clear sections."],["pixar","A model of explaining how something works."]],
 b68:[["herd","A model of explaining an idea with examples."],["cinco","A model of explaining the history behind a tradition."]],
 b912:[["goodbad","A model of explaining research to a general reader."],["wieselbio","A model of a short, factual biography."],["facebook","A model of reporting a study."]]},
W3:{b35:[["cobra","A childhood memoir to imitate."],["eleven","A model of telling one small moment in detail."],["marble","A model of a clear sequence of events."]],
 b68:[["fishcheeks","A one-page memoir with vivid details."],["names","A memoir about names in two languages."],["drivein","A memoir built around one day."]],
 b912:[["summerjob","A memoir about a first job."],["douglass","A classic first-person narrative."],["alexie","A contemporary memoir excerpt."]]},
SL1:{b35:[["secret","Discuss: how should we treat people who communicate differently?"],["twodollars","Discuss: what does it mean to be generous?"],["hazel","Comes with a paired story, so students can compare two characters."]],
 b68:[["party","Discuss: what should the narrator do?"],["fanclub","Discuss: when is it hard to do the right thing?"],["button","Discuss: would you push the button?"]],
 b912:[["lottery","Discuss: why do people follow traditions they do not understand?"],["staples","Students take sides on teens and the internet."],["obama","Debate: can there be peace without war?"]]},
SL4:{b35:[["mlk5","Students report on one strategy Dr. King used."],["bessie","Students present Bessie Coleman's story in order."],["chavez","Students present facts about Cesar Chavez."]],
 b68:[["malala","A model speech. Students present its claim and evidence."],["wiesel8","A model of a short speech with a clear line of reasoning."]],
 b912:[["mandela","A model of presenting ideas to a world audience."],["kingnobel","Compare its style with I Have a Dream."],["carter","A model of a formal argument given aloud."]]},
L4:{b35:[["marble","Read it beside the Spanish version to compare words."],["solar","Use context to work out space words."],["braille","Use context and word parts for new words."]],
 b68:[["insideout","Context clues, with a narrator who is learning English himself."],["herd","Terms defined by examples in the text."],["names","Names and words in Spanish and English."]],
 b912:[["sweat","Use context to read regional dialect."],["fallacy","Older vocabulary to work out from context and word parts."],["dickinson","Words with more than one meaning."]]}};
function exBand(g){return /^(K|1|2)$/.test(g)?"bk2":/^[345]$/.test(g)?"b35":/^[678]$/.test(g)?"b68":"b912";}
function exKey(){const p=S.c.split(".");return p[0]+p[p.length-1];}
function exList(){if(S.s!=="ELA")return null;const m=EXM[exKey()];return m&&m[exBand(S.g)]?m[exBand(S.g)].map(x=>{const t=EXT[x[0]];return{id:x[0],title:t[0],author:t[1],grade:t[2],lib:t[3],url:t[4]||(t[3]==="ReadWorks"?RWLIB:CLLIB),direct:!!t[4],why:x[1]};}):[];}
function exGrade(g){return g?(g==="K"?"Kindergarten":"Grade "+g):"Grade not listed";}
function exOn(){if(!Array.isArray(S.ex))S.ex=[];const L=exList()||[];return L.filter(x=>S.ex.includes(x.id));}
function exPlan(){const on=exOn();if(!on.length)return[];const L=["","Example texts to use:"];on.forEach(x=>L.push(` - ${x.title}${x.author?" by "+x.author:""} (${x.lib}, ${exGrade(x.grade).toLowerCase()}): ${x.why}`));return L;}
function exCard(){const L=exList();if(L===null)return "";const d=std(),on=exOn(),band={bk2:"kindergarten to grade 2",b35:"grades 3 to 5",b68:"grades 6 to 8",b912:"grades 9 to 12"}[exBand(S.g)];
 return `<div class="card ${on.length?"":"none"}" id="excard"><h3>Example texts for this standard</h3><p class="hint"><b>${esc(d.c)}</b> · ${esc(d.k)}. Real texts for ${band} from free libraries, with what to use each one for.</p>
 ${L.length?`<div class="sites">${L.map(x=>{const sel=S.ex.includes(x.id);return `<div class="site ${sel?"on":""}"><div class="sh"><a href="${x.url}" target="_blank" rel="noopener noreferrer">${esc(x.title)} <span aria-hidden="true">↗</span></a></div><p class="su">${x.author?esc(x.author)+" · ":""}${exGrade(x.grade)} · ${x.lib}${x.direct?"":" · search the library for this title"}</p><p>${esc(x.why)}</p><button class="btn ghost noprint noshow" data-ex="${x.id}" aria-pressed="${sel}">${sel?"In my plan ✓":"Add to my plan"}</button></div>`;}).join("")}</div>`:`<p class="note">No confirmed example yet for this standard in ${band}. Search ReadWorks by grade and topic: <a href="${RWLIB}" target="_blank" rel="noopener noreferrer">readworks.org</a>.</p>`}
 <p class="note">Titles and grade levels come from the libraries' own lists, checked November 21, 2026. Libraries add and remove texts, and some of these deal with mature subjects, so read each one before you assign it. A free teacher account is needed to open most of them.</p></div>`;}
document.addEventListener("click",e=>{const b=e.target.closest("button");if(!b||!b.dataset.ex)return;if(!Array.isArray(S.ex))S.ex=[];const i=S.ex.indexOf(b.dataset.ex);i>=0?S.ex.splice(i,1):S.ex.push(b.dataset.ex);keep();});
