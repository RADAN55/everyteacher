/* Suggested lesson ideas. Each standard gets two subject ideas and two language ideas, chosen by its code and filled in
   with its topic {k} and key words {w1} {w2} {w3}. {write} and {text} change with the grade band.
   Row: [title, minutes, what students do, support for Levels 1-2] */
const IDS={
ELA:[
["Anchor chart together",15,"Build a class anchor chart for {k} with one clear example from today's reading. Each student adds a sticky note with an example of their own.","Students copy one labeled example from the chart and point to it when they share."],
["Text hunt",15,"Partners search {text} for two examples of {k}, mark them, and explain one choice to another pair.","Give a shorter passage with four parts already underlined. Students sort them into yes and no."],
["Mentor sentence",10,"Show one strong sentence that models {k}. Students name what the writer did, then imitate it with a topic of their own.","Turn the mentor sentence into a frame with two blanks to fill."],
["Read, talk, write",20,"Use {text} twice: once for the gist and once with {k} in mind. Partners talk for two minutes, then {write}.","Partners may talk in the home language first. Give a word bank with {w1} and {w2}."],
["Word sort",10,"Give cards for {w1}, {w2}, {w3}, and three related words. Groups sort them into categories they choose and defend the groups.","Add a picture to each card and let students sort by picture first."],
["Gallery walk",20,"Post four short excerpts around the room. Groups rotate, mark each one for {k}, and leave one comment.","Assign the excerpt with the most picture support first, and give a comment starter."],
["Revise one thing",15,"Students return to a piece of their own writing and revise it with one focus: {k}. They show a partner the before and the after.","Revise one sentence together first, then students change one sentence of their own."],
["Two texts, one topic",20,"Give two short texts on the same topic. Students use a two-column chart to show how each one handles {k}.","Provide one text in simpler language and fill in the first row of the chart together."]],
MATH:[
["Number talk",10,"Open with one problem about {k} that can be solved in several ways. Record three strategies on the board and label each with the student's name.","Accept gestures, drawings, and numbers. Restate the student's idea in a full sentence."],
["Objects, picture, numbers",20,"Model {k} with objects, then with a drawing, then with numbers. Students complete one of each and match them.","Start with the objects and name each one. Add {w1} and {w2} to the drawing as labels."],
["Find the mistake",10,"Show a worked example about {k} with one error. Partners find it, fix it, and explain what went wrong.","Circle the step that holds the error so students explain it instead of searching for it."],
["Three reads",15,"Read one word problem about {k} three times: first for the story, then for the quantities, then for the question. Only then solve it.","Act out or sketch the story after the first read. Underline the numbers together."],
["Which one does not belong",10,"Show four examples related to {k}. Students choose one that does not belong and give a reason. Every answer can be defended.","Offer the starter: This one is different because __."],
["Real-world task",25,"Use a store flyer, a recipe, or a sports table to pose a problem about {k}. Groups show their thinking on a poster.","Choose a context students know from home. Give the poster headings in advance."],
["Vocabulary in action",10,"Students draw or act out {w1}, {w2}, and {w3}, then use each word in a sentence about a problem they solved.","Pair each word with a picture and a home-language translation in the notebook."],
["Three stations",30,"Run three stations for {k}: partner practice, a game, and a small group with you.","Meet the Levels 1-2 group first so they hear the directions and the key words before the others."]],
SCI:[
["Phenomenon first",10,"Show a short video or photo of something puzzling that involves {k}. Students record what they notice and what they wonder before you explain anything.","Accept single words and drawings. Chart the class's words to reuse later."],
["Hands-on investigation",30,"Investigate {k} with everyday materials. Groups collect data in a shared table and report one result.","Give the group a job card with pictures: materials, measurer, recorder, reporter."],
["Build a model",20,"Students draw or build a labeled model of {k} and use it to explain the idea to another group.","Provide the labels {w1}, {w2}, and {w3} on cards to place on the model."],
["Claim, evidence, reasoning",20,"Pose one question about {k}. Students write a claim, list evidence from data or {text}, and connect the two.","Provide two claims to choose from and a sorted list of evidence."],
["Label the diagram",10,"Give an unlabeled diagram about {k}. Students add {w1}, {w2}, and {w3}, then write one sentence for each arrow.","Give a word bank with pictures and let students match before they write."],
["Data talk",10,"Display one graph or table about {k}. Ask three questions: What do you notice? What does it mean? What would change it?","Point to and name the title, the labels, and the largest and smallest values first."],
["Science notebook",15,"Students record a drawing, three key words, and one sentence about {k}. Partners trade notebooks and add a question.","Accept labels in the home language beside the English words."],
["Local connection",15,"Connect {k} to something students can see in Mississippi, such as the weather, a river, a farm, or the coast. Students describe one local example.","Bring a photo of the local example and name its parts together."]],
SS:[
["Source detective",15,"Give a photograph, map, or short document about {k}. Students list what they see, what they think it means, and one question.","Use an image source. Offer the starters I see __ and I think __."],
["Timeline",20,"Students place four to six events about {k} on a timeline and explain how one event led to the next.","Give the events as picture cards with dates to put in order."],
["Map it",15,"Students find the places connected to {k} on a map and add notes that use {w1} and {w2}.","Students label the map with a word bank and color the key areas."],
["Whose view?",20,"Assign groups a person or group connected to {k}. Each group explains what that person wanted and why.","Give a role card with a picture and two facts written in simple sentences."],
["Four corners",10,"Post a statement about {k}. Students move to the corner that matches their opinion and give one reason.","Let students choose a corner first and listen, then repeat a reason they agree with."],
["Then and now",15,"Students compare {k} with a similar situation today in a two-column chart and discuss what changed.","Fill the Now column from students' own lives first, where they have the words."],
["Jigsaw",25,"Split a reading about {k} into four parts. Expert groups study one part and teach it to their home groups.","Give the part with the most pictures and a short summary to read first."],
["One-pager",20,"Students create a one-page summary of {k}: a title, a drawing, three key words, and two sentences.","Require the drawing and the three words. The sentences may use a frame."]]
};
const IDF={
explain:[
["Teach a younger student",15,"Students explain {k} as if to a student two grades younger, using a drawing and the word because.","Students label the drawing and say one sentence with because."],
["Because chain",10,"In a circle, one student makes a statement about {k}. Each next student adds a sentence that begins with because or this means.","Give students a card with the starter and one key word to use."],
["Explain the model",10,"Students point to parts of a diagram or object and explain {k} to a partner, who repeats the explanation back.","Partners explain in the home language first, then try in English."],
["Record and replay",15,"Students record a 30-second explanation of {k}, listen to it, and record a second, clearer take.","Students rehearse with a frame and read from it on the first take."],
["Why wall",10,"Post three why questions about {k}. Students answer one on a sticky note and read two classmates' answers.","Accept a labeled sketch as the answer, with one word in English."]],
compare:[
["Venn diagram",15,"Students compare two parts of {k} in a Venn diagram, then say one sentence with both and one with but.","Give six facts on cards to place in the diagram."],
["Same or different",10,"Partners get pairs of cards about {k} and decide whether each pair is the same or different, and why.","Use picture cards and the starters They are the same and They are different."],
["Side by side",15,"Show two examples of {k} next to each other. Students list two things in common and two differences.","Point and name features together before students list."],
["Comparison paragraph",20,"Using a chart they completed, students {write} that compares two parts of {k} with both, but, and however.","Provide a paragraph frame with the signal words already in place."],
["Find your match",10,"Each student gets a card about {k} and finds a classmate whose card is similar, then explains the link.","Give cards with pictures, and model one match first."]],
sequence:[
["Sentence strips",10,"Give the steps or events of {k} on mixed-up strips. Groups put them in order and read them aloud with first, next, and finally.","Number two strips in advance and add a picture to each strip."],
["Flow chart",15,"Students draw a flow chart of {k} with one box for each step and an arrow between boxes.","Provide the empty boxes and a word bank."],
["Retell with signal cards",10,"Partners retell {k}. The listener holds up cards (first, next, then, finally) to prompt each step.","Students retell with pictures in hand and one sentence per picture."],
["Comic strip",20,"Students show {k} in a four-panel comic with a caption under each panel.","Captions may be single words or labels."],
["How-to guide",20,"Students write the steps of {k} as directions for someone who was absent.","Students number the steps and use command verbs from a word bank."]],
cause:[
["Cause and effect chain",15,"Students build a chain of three linked boxes for {k}: cause, effect, next effect. They read it aloud with so and as a result.","Give the three boxes as picture cards to arrange."],
["Match it",10,"Give cause cards and effect cards about {k}. Partners match them and say each pair in one sentence with because.","Use picture cards. Students say the pair with a frame."],
["Change one thing",15,"Ask what would happen to {k} if one condition changed. Students predict, give a reason, and check it against a source.","Offer two predictions to choose from and the starter I think __ because __."],
["Fishbone",20,"Groups sort the causes of {k} onto a fishbone diagram and star the most important one.","Provide the causes on strips so that students place them instead of writing."],
["Before and after",10,"Show a before picture and an after picture related to {k}. Students explain what caused the change.","Students label both pictures, then finish the sentence __ changed because __."]],
argue:[
["Opinion line",10,"Read a claim about {k}. Students stand on a line from agree to disagree, and three students explain their place.","Students choose a place, then repeat or add to a classmate's reason."],
["Evidence sort",15,"Give six pieces of evidence about {k}. Groups sort them into strong and weak and defend one choice.","Read each card aloud together and sort the first two as a class."],
["Mini debate",20,"Two sides prepare one claim and two pieces of evidence about {k}, then take turns. The class names the strongest evidence.","Students present one rehearsed sentence and hold up the evidence card."],
["Convince me",20,"Students {write} to convince a reader of one claim about {k}, with at least one piece of evidence.","Provide the claim and a frame: I think __ because __."],
["Agree, disagree, add",10,"After a partner's claim about {k}, each student must agree, disagree, or add on, and say why.","Post the three starters with thumbs-up, thumbs-down, and plus icons."]],
describe:[
["Describe and draw",15,"One partner describes a picture or object related to {k} without showing it. The other draws it, and then they compare.","Give the describer a word bank with {w1} and {w2}."],
["Feature chart",10,"Students complete a chart for {k}: what it is, what it has, what it does, and an example.","Fill in the first column together and use pictures in the last one."],
["Label the picture",10,"Students label a picture about {k} with {w1}, {w2}, and {w3}, then turn two labels into sentences.","Labels only. Add the home-language word beside each label."],
["What am I?",10,"Students write three clues that describe something from {k}. Classmates guess the answer.","Students choose clues from a list and read them aloud."],
["Stretch the sentence",10,"Start with a three-word sentence about {k}. Students add what kind, where, and why to make it longer.","Add only one detail, using a picture as support."]],
summarize:[
["Main idea and two details",10,"After {text} about {k}, students write the main idea and the two details that matter most.","Students choose the main idea from three options and copy one detail."],
["Ten-word summary",10,"Students summarize {k} in exactly ten words, then compare with a partner and improve the wording.","Students summarize in five words, using the key words."],
["Write the headline",10,"Students write a newspaper headline and one sentence that capture the most important point about {k}.","Students choose the best of three headlines and say why."],
["Shrink it",15,"Students summarize {k} in 25 words, then 15, then 8, and discuss what had to stay.","Students do the 8-word version only, with a word bank."],
["Thirty-second share",10,"Partners take turns summarizing {k} aloud in 30 seconds. The listener names one thing that was left out.","Students rehearse with the frame It is about __, then share."]],
solve:[
["Solver and listener",15,"One partner solves a problem about {k} aloud while the other only listens and asks why. Then they switch.","Give the listener two question cards: Why? and How do you know?"],
["Two ways",15,"Students solve one problem about {k} in two different ways and explain which way they prefer.","Students solve one way with a drawing and label each step."],
["Check and defend",10,"Students trade solutions about {k}, check each other's work, and defend or correct the answer.","Give a three-item checklist with pictures to check against."],
["Write your own problem",20,"Students write a new problem about {k} from their own lives, solve it, and trade with a partner.","Students change only the numbers and names in a model problem."],
["Strategy share",10,"Three students show different strategies for the same problem about {k}. The class names how they are alike.","Students show their work under the camera and point while you narrate."]]
};
const IDW=[["draw and label a picture","a read-aloud"],["write two or three sentences","a short text"],["write a short paragraph","a short text"]];
function ideaHash(c){let h=7;for(let i=0;i<c.length;i++)h=(h*31+c.charCodeAt(i))>>>0;return h;}
function ideaPick(){const h=ideaHash(S.c),o=S.io||0,a=(h+o)%8,b=(a+1+((h>>>3)+o)%7)%8,f=((h>>>6)+o)%5,g=(f+1+((h>>>9)+o)%4)%5;return[["S",a],["F",f],["S",b],["F",g]];}
function ideaFill(t){const d=std(),v=vocab().length>=3?vocab():d.v,w=IDW[band(S.g)];return t.replace(/\{k\}/g,d.k).replace(/\{w1\}/g,v[0]||d.k).replace(/\{w2\}/g,v[1]||v[0]||d.k).replace(/\{w3\}/g,v[2]||v[0]||d.k).replace(/\{write\}/g,w[0]).replace(/\{text\}/g,w[1]);}
function ideaGet(id){const r=id[0]==="S"?IDS[S.s][+id.slice(1)]:IDF[fn()][+id.slice(1)];return r?{id:id,tag:id[0]==="S"?subjName():F[fn()].label,kind:id[0],title:r[0],min:r[1],desc:ideaFill(r[2]),el:ideaFill(r[3])}:null;}
function ideasFor(){return ideaPick().map(p=>ideaGet(p[0]+p[1]));}
function ideasOn(){if(!Array.isArray(S.ideas))S.ideas=[];return S.ideas.map(ideaGet).filter(Boolean);}
function ideasPlan(){const on=ideasOn();if(!on.length)return[];const L=["","Lesson ideas chosen for this standard:"+(band(S.g)===0?" (run aloud with pictures; students draw and say their answers)":"")];on.forEach(x=>{L.push(` - ${x.title} (${x.min} min): ${x.desc}`,`   Levels 1-2: ${x.el}`);});return L;}
function ideasCard(){const d=std(),list=ideasFor(),on=ideasOn(),shown=list.map(x=>x.id),extra=on.filter(x=>!shown.includes(x.id)),g=groups(),
 row=x=>{const sel=S.ideas.includes(x.id);return `<div class="idea ${sel?"on":""}"><div class="ih"><b>${esc(x.title)}</b><span class="g ${x.kind==="S"?"all":"act"}">${esc(x.tag)}</span><span class="im">${x.min} min</span></div><p>${esc(x.desc)}</p><p class="iel ${g.em?"":"dim"}"><span class="g em">Levels 1-2</span>${esc(x.el)}</p><button class="btn ghost noprint noshow" data-idea="${x.id}" aria-pressed="${sel}">${sel?"In my plan ✓":"Add to my plan"}</button></div>`;};
 return `<div class="card ${on.length?"":"none"}" id="ideacard"><h3>Lesson ideas for this standard</h3><p class="hint"><b>${esc(d.c)}</b> · ${esc(d.k)}. Two ideas fit the subject and two build the language students need. Tap the ones you want in your plan.${band(S.g)===0?" For kindergarten to grade 2, run these aloud as a class with pictures, and let students draw and say their answers instead of writing.":""}</p>
 <div class="ideas">${list.map(row).join("")}${extra.map(row).join("")}</div>
 <div class="row noprint noshow"><button class="btn" id="ideamore">Show different ideas</button>${on.length?`<span class="hint" style="margin:0">${on.length} in your plan</span>`:""}</div></div>`;}
document.addEventListener("click",e=>{const b=e.target.closest("button");if(!b)return;
 if(b.dataset.idea){if(!Array.isArray(S.ideas))S.ideas=[];const i=S.ideas.indexOf(b.dataset.idea);i>=0?S.ideas.splice(i,1):S.ideas.push(b.dataset.idea);keep();}
 else if(b.id==="ideamore"){S.io=((S.io||0)+1)%40;keep();}
});
