/* Standards bank. One line per standard: code|short wording (verb first)|language function|lesson focus|key words */
const MATH={
"K":`K.CC.4|Count objects and tell how many, matching one number to each object.|so|counting objects|count,number,how many,more,one,match
K.CC.6|Compare two groups of objects: greater than, less than, or equal.|co|two groups of objects|greater,less,equal,more,fewer,compare
K.OA.1|Show addition and subtraction with objects, fingers, drawings, or equations.|so|addition and subtraction|add,subtract,plus,minus,equals,altogether
K.NBT.1|Compose and decompose numbers 11 to 19 into ten ones and some more ones.|so|teen numbers|ten,ones,teen,compose,group,more
K.MD.3|Classify objects into categories and count the number in each.|de|sorting objects|sort,category,count,same,different,group
K.G.2|Name shapes correctly, whatever their size or position.|de|shapes|circle,square,triangle,rectangle,side,corner`,
"1":`1.OA.1|Solve addition and subtraction word problems within 20.|so|word problems within 20|add,subtract,sum,difference,unknown,equation
1.OA.6|Add and subtract within 20 using strategies.|so|adding and subtracting within 20|sum,difference,make ten,double,strategy,equal
1.NBT.2|Explain that the two digits of a two-digit number represent tens and ones.|ex|tens and ones|digit,tens,ones,place value,bundle,number
1.NBT.4|Add within 100 using models and place value.|so|adding within 100|tens,ones,add,sum,model,place value
1.MD.3|Tell and write time in hours and half-hours.|de|telling time|hour,half hour,clock,minute,o'clock,time
1.G.3|Partition circles and rectangles into halves and fourths.|de|halves and fourths|half,fourth,quarter,equal,share,whole`,
"2":`2.OA.1|Solve one- and two-step addition and subtraction word problems within 100.|so|two-step word problems|step,sum,difference,unknown,equation,solve
2.NBT.1|Explain that the three digits of a number represent hundreds, tens, and ones.|ex|hundreds, tens, and ones|hundreds,tens,ones,digit,place value,expanded form
2.NBT.5|Fluently add and subtract within 100.|so|adding and subtracting within 100|regroup,sum,difference,tens,ones,strategy
2.MD.1|Measure the length of an object with the right tool.|so|measuring length|length,inch,centimeter,ruler,measure,unit
2.MD.8|Solve word problems with dollar bills and coins.|so|money|dollar,cent,coin,quarter,dime,total
2.G.1|Recognize and draw shapes with given attributes.|de|shapes and their attributes|angle,side,face,attribute,quadrilateral,pentagon`,
"3":`3.OA.1|Interpret products of whole numbers as equal groups.|ex|multiplication as equal groups|multiply,product,factor,equal groups,array,times
3.OA.3|Solve multiplication and division word problems within 100.|so|multiplication and division|product,quotient,factor,divide,array,unknown
3.NF.1|Explain a fraction as equal parts of a whole.|ex|fractions as parts of a whole|fraction,numerator,denominator,equal parts,whole,unit fraction
3.NF.3|Explain equivalent fractions and compare fractions.|co|fractions|equivalent,compare,numerator,denominator,greater than,less than
3.MD.7|Relate area to multiplication and addition.|so|area|area,square unit,length,width,multiply,rectangle
3.NBT.2|Fluently add and subtract within 1,000.|so|adding and subtracting within 1,000|regroup,sum,difference,place value,hundreds,estimate`,
"4":`4.OA.3|Solve multistep word problems with the four operations.|so|multistep word problems|operation,remainder,estimate,equation,reasonable,unknown
4.NBT.5|Multiply multi-digit whole numbers using place value strategies.|so|multi-digit multiplication|product,factor,place value,partial product,array,estimate
4.NBT.6|Divide numbers of up to four digits by one-digit divisors.|so|division with remainders|quotient,divisor,dividend,remainder,divide,estimate
4.NF.1|Explain why fractions are equivalent using visual models.|ex|equivalent fractions|equivalent,numerator,denominator,model,multiply,fraction
4.NF.3|Add and subtract fractions with like denominators.|so|adding and subtracting fractions|numerator,denominator,sum,difference,mixed number,like
4.MD.3|Apply the area and perimeter formulas for rectangles.|so|area and perimeter|area,perimeter,formula,length,width,square unit`,
"5":`5.OA.1|Use parentheses and brackets and evaluate expressions.|so|numerical expressions|expression,parentheses,evaluate,order of operations,bracket,simplify
5.NBT.7|Add, subtract, multiply, and divide decimals to hundredths.|so|decimals|decimal,tenths,hundredths,place value,product,quotient
5.NF.1|Add and subtract fractions with unlike denominators.|so|fractions with unlike denominators|common denominator,equivalent,numerator,sum,difference,mixed number
5.NF.4|Multiply a fraction or a whole number by a fraction.|so|multiplying fractions|product,numerator,denominator,area model,factor,of
5.MD.5|Solve volume problems using multiplication and addition.|so|volume|volume,cubic unit,length,width,height,rectangular prism
5.G.2|Graph points on the coordinate plane to solve problems.|so|the coordinate plane|coordinate,ordered pair,x-axis,y-axis,origin,graph`,
"6":`6.RP.1|Use ratio language to describe a relationship between two quantities.|de|ratios|ratio,quantity,for every,per,compare,relationship
6.RP.3|Use ratio and rate reasoning to solve real-world problems.|so|ratios and unit rates|rate,unit rate,ratio,percent,table,equivalent
6.NS.1|Divide fractions by fractions and solve word problems.|so|dividing fractions|quotient,reciprocal,divisor,dividend,fraction,model
6.EE.2|Write, read, and evaluate expressions with variables.|so|algebraic expressions|variable,expression,term,coefficient,evaluate,substitute
6.EE.7|Solve real-world problems with one-step equations.|so|one-step equations|equation,variable,solution,inverse operation,solve,balance
6.SP.5|Summarize numerical data sets in context.|su|a data set|mean,median,range,data,distribution,outlier`,
"7":`7.RP.2|Recognize and represent proportional relationships.|ex|proportional relationships|proportional,constant,unit rate,ratio,graph,equation
7.RP.3|Solve multistep ratio and percent problems.|so|percents|percent,discount,tax,interest,increase,decrease
7.NS.1|Add and subtract rational numbers.|so|adding and subtracting rational numbers|integer,rational number,opposite,absolute value,negative,number line
7.EE.4|Use variables to write and solve equations and inequalities.|so|equations and inequalities|equation,inequality,variable,solution,solve,represent
7.G.4|Use the formulas for the area and circumference of a circle.|so|circles|circumference,radius,diameter,pi,area,formula
7.SP.6|Approximate the probability of a chance event from data.|ex|probability|probability,likely,outcome,event,frequency,predict`,
"8":`8.EE.5|Graph proportional relationships and interpret the unit rate as the slope.|ex|slope|slope,unit rate,proportional,graph,rise,run
8.EE.7|Solve linear equations in one variable.|so|linear equations|equation,variable,solution,distribute,like terms,inverse
8.EE.8|Analyze and solve pairs of simultaneous linear equations.|so|systems of equations|system,solution,intersect,substitution,elimination,graph
8.F.1|Explain that a function assigns exactly one output to each input.|ex|functions|function,input,output,rule,domain,graph
8.G.7|Apply the Pythagorean Theorem to find unknown side lengths.|so|the Pythagorean Theorem|hypotenuse,leg,right triangle,square root,squared,theorem
8.SP.1|Construct and interpret scatter plots.|de|scatter plots|scatter plot,association,positive,negative,outlier,trend`,
"Algebra I":`A-CED.1|Create equations and inequalities in one variable and use them to solve problems.|so|equations and inequalities|equation,inequality,variable,constraint,model,solution
A-REI.3|Solve linear equations and inequalities in one variable.|so|linear equations and inequalities|solve,inverse,variable,solution set,coefficient,inequality
A-REI.6|Solve systems of linear equations exactly and approximately.|so|systems of linear equations|system,substitution,elimination,intersection,solution,graph
F-IF.4|Interpret key features of the graphs and tables of functions.|de|the key features of a function|intercept,increasing,decreasing,maximum,minimum,interval
F-LE.1|Distinguish between situations modeled by linear and exponential functions.|co|linear and exponential functions|linear,exponential,constant rate,growth,factor,interval
A-SSE.3|Write expressions in equivalent forms to reveal their properties.|ex|equivalent expressions|factor,quadratic,zeros,equivalent,expression,complete the square
S-ID.6|Represent two-variable data on a scatter plot and describe the relationship.|de|two-variable data|scatter plot,correlation,line of fit,residual,trend,variable`,
"Geometry":`G-CO.10|Prove theorems about triangles.|ar|triangle theorems|theorem,proof,congruent,angle,isosceles,midpoint
G-SRT.5|Use congruence and similarity criteria to solve problems and prove relationships.|ar|congruence and similarity|congruent,similar,corresponding,proportion,criteria,prove
G-SRT.8|Use trigonometric ratios and the Pythagorean Theorem to solve right triangles.|so|right triangle trigonometry|sine,cosine,tangent,hypotenuse,opposite,adjacent
G-GPE.5|Prove and use the slope criteria for parallel and perpendicular lines.|ar|parallel and perpendicular lines|slope,parallel,perpendicular,reciprocal,equation,line
G-GMD.3|Use the volume formulas for cylinders, pyramids, cones, and spheres.|so|the volume of solids|volume,cylinder,cone,sphere,pyramid,formula
G-C.2|Identify and describe relationships among angles, radii, and chords.|de|the parts of a circle|chord,radius,central angle,inscribed,tangent,arc`,
"Algebra II":`A-APR.3|Identify the zeros of polynomials and use them to sketch a graph.|ex|the zeros of polynomials|polynomial,zero,factor,root,degree,graph
A-REI.4|Solve quadratic equations in one variable.|so|quadratic equations|quadratic,factor,square root,quadratic formula,complex,solution
F-BF.3|Identify the effect of transformations on the graph of a function.|ex|transformations of functions|transformation,shift,stretch,reflect,parent function,translate
F-LE.4|Use logarithms to solve exponential equations.|so|exponential equations and logarithms|logarithm,exponent,base,exponential,inverse,solve
F-IF.7|Graph functions and show their key features.|de|the graphs of functions|intercept,asymptote,end behavior,period,amplitude,maximum
S-IC.1|Explain how statistics lets us make inferences about a population from a sample.|ex|samples and populations|sample,population,random,inference,parameter,statistic`};
const SCI={
"K":`L.K.1|Explain what makes things living and how animals use their body parts and senses.|de|living things|living,nonliving,senses,body part,animal,plant
L.K.2|Describe how living things change as they grow and how the young resemble their parents.|se|a life cycle|life cycle,grow,change,parent,young,adult
L.K.3|Explain what plants and animals need to live and how they depend on their environment.|ex|what plants and animals need|need,food,water,air,shelter,environment
L.K.4|Explain why some plants and animals are extinct.|ca|extinction|extinct,survive,need,fossil,dinosaur,habitat
P.K.5|Describe and sort solids and liquids by their properties.|de|solids and liquids|solid,liquid,property,sort,shape,texture
E.K.8|Describe seasonal changes and how the Sun provides heat and light.|de|the seasons and the Sun|season,Sun,heat,light,weather,pattern
E.K.10|Explain how people use Earth's resources and how to conserve them.|ex|Earth's resources|resource,reuse,recycle,reduce,conserve,water`,
"1":`L.1.1|Describe the basic needs and structures of plants.|de|the parts and needs of a plant|root,stem,leaf,flower,seed,sunlight
L.1.2|Describe how living things change through the stages of a life cycle.|se|a life cycle|life cycle,stage,seed,seedling,adult,grow
L.1.3A|Explain what plants need from their environment.|ex|what plants need|soil,water,sunlight,air,space,environment
L.1.3B|Explain how flowering plants and pollinating insects depend on each other.|ex|plants and pollinators|pollinate,insect,flower,nectar,pollen,depend
L.1.4|Explain how plants adapt to their environments to survive.|ex|plant adaptations|adapt,survive,environment,desert,thorn,leaf
P.1.6A|Explain that light is needed to make objects visible.|ex|light|light,shadow,visible,reflect,transparent,opaque
P.1.6B|Explain how vibrations make sound.|ca|sound|sound,vibrate,volume,pitch,loud,soft
E.1.9A|Describe weather patterns using data.|de|weather patterns|weather,temperature,pattern,data,cloud,forecast
E.1.9B|Describe how water and land are distributed on Earth.|de|land and water on Earth|ocean,river,lake,land,map,globe
E.1.10|Explain why people depend on clean water.|ex|clean water|water,clean,pollution,conserve,resource,renewable`,
"2":`L.2.1|Classify animals by their physical characteristics.|co|animal groups|classify,vertebrate,invertebrate,mammal,reptile,backbone
L.2.2|Describe how living things change form through a life cycle.|se|an animal life cycle|life cycle,egg,larva,tadpole,metamorphosis,adult
L.2.3A|Explain how living things depend on the environment they live in.|ex|living things and their environment|environment,habitat,change,depend,shelter,respond
L.2.3B|Explain how living things depend on one another.|ex|how living things depend on each other|food chain,predator,prey,depend,plant,space
L.2.4|Explain how animals adapt to their environment to survive.|ex|animal adaptations|adapt,survive,camouflage,migrate,hibernate,habitat
P.2.5|Classify matter by its properties and describe changes caused by heat.|de|the properties of matter|matter,property,solid,liquid,gas,melt
P.2.6|Explain how pushes, pulls, and friction affect motion.|ca|pushes, pulls, and friction|push,pull,force,friction,motion,speed
E.2.8|Describe the patterns of the Sun, Moon, and stars.|de|the Sun, Moon, and stars|Sun,Moon,star,pattern,phase,sunrise
E.2.10|Explain how people use Earth's resources.|ex|Earth's materials|soil,rock,erosion,resource,mineral,conserve`,
"3":`L.3.1|Explain how the internal and external structures of organisms help them survive, grow, and reproduce.|ex|the structures of organisms|structure,function,organism,survive,reproduce,external
L.3.2|Explain how offspring inherit traits and how the environment can influence them.|ex|inherited traits|trait,inherit,offspring,parent,environment,variation
L.3.4|Explain how habitat changes affect organisms and how adaptations help them survive.|ca|habitat change|adaptation,habitat,survive,change,species,environment
P.3.5|Explain how adding or removing heat changes the state of matter.|ca|changes in the state of matter|solid,liquid,gas,melt,freeze,evaporate
P.3.6|Explain how forces and magnets affect the motion of objects.|ca|forces and magnets|force,magnet,attract,repel,motion,friction
E.3.7A|Describe the processes that form rocks, rock layers, and fossils.|se|how rocks and fossils form|rock,fossil,layer,sediment,mineral,form
E.3.7B|Describe Earth's layers and the processes that reshape landforms.|de|Earth's layers and landforms|crust,mantle,core,landform,erosion,weathering
E.3.9|Explain how Earth's four systems interact.|ex|Earth's systems|geosphere,hydrosphere,atmosphere,biosphere,system,interact
E.3.10|Explain how people use and protect natural resources.|ex|natural resources|renewable,nonrenewable,resource,conserve,pollution,protect`,
"4":`L.4.1|Explain how human body systems are organized and work together.|ex|human body systems|organ,system,skeletal,muscular,digestive,function
L.4.2|Compare the life cycles of familiar plants and animals.|co|the life cycles of plants and animals|life cycle,stage,germinate,metamorphosis,reproduce,compare
P.4.6|Describe the sources and uses of heat, electricity, light, and sound energy.|de|forms of energy|energy,heat,electricity,circuit,light,sound
E.4.9|Explain how the Sun drives the water cycle, weather, and climate.|ca|the water cycle and weather|evaporation,condensation,precipitation,water cycle,climate,weather
E.4.10|Compare energy sources and their effects on the environment.|co|energy sources|renewable,nonrenewable,fossil fuel,solar,wind,impact`,
"5":`L.5.3A|Explain how plants use photosynthesis to turn sunlight into chemical energy.|ex|photosynthesis|photosynthesis,sunlight,carbon dioxide,oxygen,energy,chlorophyll
L.5.3B|Explain the roles of producers, consumers, and decomposers in an ecosystem.|ex|food chains and food webs|producer,consumer,decomposer,ecosystem,food web,energy
P.5.5A|Identify and measure the physical properties of solids, liquids, and gases.|de|the physical properties of matter|mass,volume,property,solid,liquid,gas
P.5.5B|Explain how substances behave in mixtures and solutions.|ex|mixtures and solutions|mixture,solution,dissolve,solute,solvent,separate
P.5.5C|Distinguish physical changes from chemical changes.|co|physical and chemical changes|physical change,chemical change,reversible,substance,react,new material
P.5.6|Explain how forces change the motion of an object.|ca|forces and motion|force,motion,gravity,friction,speed,balanced
E.5.8A|Describe the solar system, the brightness of stars, and how constellations appear to move.|de|the solar system and the stars|solar system,planet,orbit,star,constellation,gravity
E.5.8B|Explain Moon phases, day and night, and the seasons.|ca|Moon phases and the seasons|phase,rotate,revolve,axis,season,orbit
E.5.10|Explain how people can conserve resources and prepare for natural disasters.|ex|conserving Earth's resources|conserve,resource,natural disaster,pollution,recycle,solution`,
"6":`L.6.1|Explain how living things are organized, from cells to whole organisms.|ex|cells and the organization of living things|cell,tissue,organ,organism,cell theory,organelle
L.6.3|Explain how survival, environmental change, and diversity are related in ecosystems.|ca|change in an ecosystem|ecosystem,population,community,biotic,abiotic,competition
L.6.4|Classify organisms into kingdoms using tools such as dichotomous keys.|co|groups of living things|classify,kingdom,dichotomous key,species,bacteria,characteristic
P.6.6|Explain Newton's laws of motion using real-world examples.|ex|Newton's laws of motion|force,motion,inertia,acceleration,mass,friction
E.6.8|Explain Earth's place in the solar system and how gravity keeps objects in orbit.|ex|Earth and the solar system|gravity,orbit,solar system,planet,rotation,revolution`,
"7":`L.7.3|Explain how matter cycles between the living and nonliving parts of an ecosystem.|se|the cycling of matter in an ecosystem|cycle,carbon,nitrogen,decomposer,photosynthesis,respiration
P.7.5A|Identify the physical and chemical properties of matter.|de|the properties of matter|physical property,chemical property,density,substance,mass,reactivity
P.7.5B|Explain how temperature and pressure affect the state of matter and the motion of particles.|ca|changes in temperature and pressure|particle,temperature,pressure,state,kinetic energy,gas
P.7.5C|Use the periodic table to predict how elements behave and interact.|ex|the periodic table|element,atom,periodic table,proton,group,period
P.7.5D|Use chemical formulas and reactions to predict outcomes.|ex|chemical reactions|reactant,product,chemical formula,compound,react,bond
P.7.5E|Explain the conservation of mass in chemical reactions.|ex|the conservation of mass|mass,conserve,reactant,product,equation,balance
E.7.9A|Explain how the movement of air and water, driven by sunlight, shapes weather and climate.|ca|weather and climate|air mass,front,current,climate,pressure,convection
E.7.9B|Explain how human activity and natural processes contribute to climate change.|ca|climate change|climate,greenhouse gas,carbon dioxide,atmosphere,fossil fuel,temperature
E.7.9C|Explain how Earth's tilt causes the seasons.|ca|the seasons|tilt,axis,season,orbit,hemisphere,sunlight`,
"8":`L.8.2|Explain how traits are passed on through reproduction and genes.|ex|reproduction and heredity|gene,trait,inherit,DNA,dominant,recessive
L.8.4|Explain how natural selection and common ancestry shape the diversity of species.|ca|natural selection|natural selection,adaptation,species,variation,ancestor,fossil
P.8.6|Describe the properties, behavior, and uses of waves.|de|waves|wave,wavelength,frequency,amplitude,reflect,energy
E.8.7|Use geologic evidence to explain Earth's history.|ar|Earth's history|fossil,rock layer,geologic time,evidence,erosion,era
E.8.9|Explain how Earth's internal energy moves plates and causes natural hazards.|ca|plate movement|plate,earthquake,volcano,mantle,boundary,tsunami
E.8.10|Explain how population growth affects resources and why conservation matters.|ca|population growth and resource use|resource,renewable,nonrenewable,conservation,population,sustainable`,
"Biology":`BIO.1|Explain how cells work as systems.|ex|cells|cell,organelle,membrane,macromolecule,mitosis,cell theory
BIO.2|Explain how cells transform energy through photosynthesis and cellular respiration.|ex|photosynthesis and cellular respiration|photosynthesis,cellular respiration,ATP,glucose,chloroplast,mitochondria
BIO.3|Explain how traits are inherited and how DNA directs the making of proteins.|ex|heredity and DNA|DNA,gene,allele,meiosis,protein,trait
BIO.4|Use evidence to explain common ancestry, natural selection, and how new species form.|ar|evolution and natural selection|natural selection,adaptation,species,ancestor,evidence,variation
BIO.5|Explain how organisms interact with one another and with their environment.|ex|ecosystems and interdependence|ecosystem,population,community,energy flow,carrying capacity,biodiversity`};
const SS={
"K":`K.CI.1|Show how to be a productive citizen.|de|being a good citizen|citizen,rule,help,share,fair
K.CI.2|Explain the purpose of rules and consequences.|ex|rules and consequences|rule,consequence,safe,fair,choice
K.CI.3|Tell the difference between the roles of authority figures and leaders.|co|the jobs of leaders and helpers|leader,teacher,principal,police officer,job
K.E.1|Explain how money is earned and used.|ex|earning and using money|money,earn,work,buy,save
K.E.2|Tell the difference between goods and services.|co|goods and services|goods,service,buy,sell,worker
K.E.3|Tell the difference between needs and wants.|co|needs and wants|need,want,food,shelter,choice
K.CR.1|Describe how people and families are alike and different.|co|people and families|family,alike,different,home,culture
K.CR.2|Describe the diversity in the classroom.|de|our classroom community|different,same,respect,language,friend
K.CR.3|Describe the customs, traditions, and celebrations of families and schools.|de|customs and celebrations|custom,tradition,celebration,holiday,family
K.G.1|Describe where you are: home, school, and community.|de|my place in the community|home,school,community,address,near
K.G.2|Describe the physical features of the environment.|de|the land and water around us|land,water,hill,river,weather
K.G.3|Recognize maps and globes as models of the Earth.|de|maps and globes|map,globe,Earth,land,water
K.H.1|Recognize symbols and celebrations of the community, Mississippi, and the United States.|de|symbols and celebrations|symbol,flag,holiday,state,country
K.H.2|Describe the impact of important historical figures and events.|ex|people and events from the past|past,history,leader,event,long ago`,
"1":`1.CI.1|Explain the rights and responsibilities of citizens in different roles.|co|rights and responsibilities|right,responsibility,citizen,vote,respect
1.CI.2|Explain how rules and laws are different.|co|rules and laws|rule,law,government,obey,community
1.CI.3|Explain what patriotism is and how citizens show it.|ex|patriotism|patriotism,flag,pledge,anthem,country
1.E.1|Explain why people work to earn money.|ex|work and money|work,earn,job,income,pay
1.E.2|Describe how people meet their basic needs.|de|basic needs|need,food,clothing,shelter,goods
1.CR.1|Explain how cooperation and compromise work among groups.|ex|cooperation and compromise|cooperate,compromise,agree,group,solve
1.CR.2|Describe the cultures in the school and the local community.|de|the cultures in our community|culture,tradition,language,custom,community
1.G.1|Describe where places are in the world.|de|places in the world|continent,ocean,country,state,city
1.G.2|Explain how location, climate, and land features shape how people live.|ex|how places shape the way people live|climate,landform,location,weather,region
1.G.3|Read maps using directions.|so|map directions|north,south,east,west,compass rose
1.H.1|Explain how important historical figures and events shaped the United States.|ex|people and events in United States history|history,president,independence,leader,event
1.H.2|Compare life in the past and present in the United States.|co|life in the past and life today|past,present,then,now,change`,
"2":`2.CI.1|Tell civic virtues from civic responsibilities and explain their role in communities.|co|civic virtues and responsibilities|virtue,responsibility,honesty,respect,community
2.CI.2|Explain how rules and laws are made to serve and protect all citizens.|ex|how laws are made|law,rule,fair,protect,government
2.E.1|Explain how the availability of resources affects the local economy.|ca|resource availability|resource,economy,scarce,natural,business
2.E.2|Explain how consumers and producers depend on each other.|ex|consumers and producers|consumer,producer,goods,service,depend
2.E.3|Explain what affects the price and availability of goods and services.|ca|changes in prices|price,supply,demand,cost,scarce
2.E.4|Describe the roles of financial institutions in the community.|de|banks|bank,save,loan,deposit,account
2.CR.1|Explain how traditions and customs unite groups and celebrate diversity.|ex|traditions and customs|tradition,custom,diversity,unite,celebrate
2.CR.2|Explain how diverse cultures build unity through respect and acceptance.|ex|unity in a diverse community|culture,respect,accept,unity,diverse
2.G.1|Compare types of maps and the borders they show.|co|types of maps|map,border,political,physical,key
2.G.2|Explain how Earth's physical features affect where people settle.|ex|where people settle|landform,river,settle,coast,resource
2.G.3|Use latitude and longitude to read maps and compare hemispheres.|so|latitude and longitude|latitude,longitude,equator,hemisphere,grid
2.G.4|Explain how humans change the Earth and weigh the effects.|ca|human changes to the land|modify,dam,pollution,benefit,harm
2.H.1|Use primary sources to explain how people and events shaped communities.|ex|the people and events that shaped our community|primary source,community,event,photograph,past
2.H.2|Use timelines to explain how history relates to time.|se|events on a timeline|timeline,decade,century,era,order`,
"3":`3.CI.1|Explain how democratic values shape citizens' everyday lives.|ex|democratic values|democracy,equality,freedom,justice,vote
3.CI.2|Explain the three branches of government at the federal, state, and local levels.|co|the three branches of government|legislative,executive,judicial,branch,law
3.CI.3|Explain what civic leadership requires of officials and citizens.|ex|civic leadership|leader,elect,official,responsibility,serve
3.E.1|Explain how local governments collect and spend money for the community.|ex|taxes and local government|tax,budget,service,government,community
3.E.2|Explain how people and communities use resources and trade to meet needs.|ex|resources and trade|trade,resource,import,export,goods
3.E.3|Explain the factors that determine where people settle.|ex|where people settle|settle,population,resource,job,climate
3.CR.1|Connect the founding documents to democratic principles and civil liberties.|ex|the founding documents and our rights|Constitution,Bill of Rights,liberty,amendment,rights
3.CR.2|Explain how democracy depends on citizens taking part.|ex|citizen participation in a democracy|participate,vote,volunteer,citizen,voice
3.G.1|Explain how people change the land to meet their needs.|ca|human changes to the land|modify,farm,build,irrigation,environment
3.G.2|Explain how natural disasters change the Earth.|ca|natural disasters|hurricane,tornado,flood,earthquake,damage
3.G.3|Compare renewable and nonrenewable energy sources.|co|energy sources|renewable,nonrenewable,solar,oil,energy
3.G.4|Interpret maps, charts, and other representations of the Earth.|so|maps and charts|map,scale,legend,chart,symbol
3.H.1|Compare types of government used through history.|co|types of government|democracy,dictatorship,monarchy,power,ruler
3.H.2|Explain the framework of the United States government.|ex|how the United States government is set up|Constitution,federal,Congress,president,court`,
"4":`4.MS.1|Describe the physical features and natural resources of Mississippi's regions.|de|Mississippi's regions|region,Delta,coast,soil,resource
4.MS.2|Explain how the Mississippi Territory was explored and settled.|se|the exploration and settlement of Mississippi|explorer,territory,settler,colony,river
4.MS.3|Describe the Choctaw, Chickasaw, and Natchez peoples of early Mississippi.|co|the Choctaw, Chickasaw, and Natchez peoples|Choctaw,Chickasaw,Natchez,nation,tradition
4.MS.4|Trace Mississippi's path from territory to statehood.|se|Mississippi's path to statehood|territory,statehood,capital,constitution,treaty
4.MS.5|Describe antebellum society, the cotton economy, and the growth of slavery in Mississippi.|ca|the growth of slavery and the cotton economy in Mississippi|antebellum,cotton,plantation,slavery,enslaved
4.MS.6|Explain Mississippi's role in secession and the Civil War.|ca|Mississippi's secession and the Civil War|secede,Confederacy,Union,Vicksburg,battle
4.MS.7|Explain how Reconstruction and the following decades affected Mississippi.|ca|Reconstruction in Mississippi|Reconstruction,freedmen,sharecropping,amendment,segregation
4.MS.8|Explain how the modern Civil Rights Movement changed Mississippi.|ca|the Civil Rights Movement in Mississippi|civil rights,segregation,protest,vote,equality
4.MS.9|Describe how Mississippi's literature, arts, architecture, and music set it apart.|de|Mississippi's arts and music|blues,author,artist,culture,heritage
4.MS.10|Describe key historical figures and events in Mississippi's past and present.|de|important Mississippians|leader,governor,activist,event,legacy
4.MS.11|Explain how geography and economics shape work and life in Mississippi.|ex|work and life in Mississippi|industry,agriculture,economy,job,export`,
"5":`5.1|Locate major geographic areas of the world, especially North America.|de|the geography of North America|continent,region,landform,climate,border
5.2|Describe the ways of life of Native American and Caribbean peoples before the Columbian era.|co|the Native peoples of North America and the Caribbean|nation,culture,region,tradition,resource
5.3|Explain the motives for and effects of European exploration of North America.|ca|European exploration|explorer,motive,trade,colony,exchange
5.4|Explain the economic, political, and religious reasons for founding the colonies.|ca|the founding of the colonies|colony,religion,charter,trade,settlement
5.5|Trace the development of the revolutionary movement in North America.|se|the road to revolution|tax,protest,boycott,Parliament,liberty
5.6|Explain the major events of the American Revolution.|se|the American Revolution|revolution,independence,battle,Patriot,treaty
5.7|Explain how the nation's founding documents developed.|ex|the founding documents|Declaration,Articles,Constitution,rights,document
5.8|Explain how the United States Constitution developed.|se|the writing of the Constitution|Constitution,compromise,convention,ratify,amendment
5.9|Recognize American symbols, customs, and celebrations.|de|American symbols|symbol,flag,anthem,monument,holiday
5.10|Locate the United States and its fifty states on maps and globes.|de|the fifty states|state,capital,region,map,border`,
"6":`6.1|Use maps, globes, and technology to understand the world's geography.|so|maps and geographic tools|map,latitude,longitude,scale,projection
6.2|Describe the environmental patterns created by Earth's physical systems.|de|Earth's physical systems|climate,biome,ecosystem,landform,pattern
6.3|Explain how regions are used to describe the Earth's surface.|ex|regions|region,physical,cultural,boundary,characteristic
6.4|Explain what natural resources are and why they matter.|ex|natural resources|resource,renewable,nonrenewable,scarce,distribution
6.5|Explain how places come to have meaning for people.|ex|the meaning of places|place,culture,identity,landmark,perception
6.6|Explain how and why populations change and people migrate.|ca|migration|migration,population,push factor,pull factor,immigrant
6.7|Describe how human settlements form and why.|ex|human settlements|settlement,urban,rural,city,growth
6.8|Explain how resource extraction and natural hazards affect people and land.|ca|resource extraction and natural hazards|extract,mining,hazard,drought,impact
6.9|Analyze how independent nation-states interact.|ex|how nations interact|nation,alliance,trade,conflict,treaty
6.10|Explain how governments are organized.|co|forms of government|government,democracy,monarchy,constitution,power
6.11|Contrast limited and unlimited governments.|co|limited and unlimited governments|limited,unlimited,dictator,rights,rule of law
6.12|Explain the rights and responsibilities of American citizenship.|ex|citizenship|citizen,right,responsibility,vote,naturalization
6.13|Identify challenges to civic participation today.|ex|civic participation today|participate,vote,barrier,community,issue
6.14|Compare how citizens' rights vary across cultures and governments.|co|citizens' rights in different countries|rights,freedom,government,culture,compare
6.15|Describe the geographic patterns of economic interaction.|de|world trade|trade,import,export,economy,interdependence
6.16|Describe the world's major cultural regions and their characteristics.|de|the cultural regions of the world|culture,religion,language,tradition,region`,
"7":`7.1|Explain how civilization developed along the Nile River.|ca|the rise of civilization along the Nile|Nile,pharaoh,pyramid,irrigation,civilization
7.2|Explain how civilization developed in China's river valleys.|ca|the rise of civilization in ancient China|dynasty,emperor,river valley,Great Wall,philosophy
7.3|Explain how civilization developed in the Indus Valley.|ca|the rise of civilization in the Indus Valley|Indus,city planning,trade,monsoon,civilization
7.4|Explain how civilizations developed in ancient Greece.|ca|the rise of civilization in ancient Greece|city-state,democracy,philosopher,myth,Athens
7.5|Trace the history of ancient Rome.|se|the history of ancient Rome|republic,empire,senate,emperor,citizen
7.6|Describe how civilizations developed across sub-Saharan Africa.|de|the kingdoms of sub-Saharan Africa|kingdom,trade route,gold,salt,empire
7.7|Compare the early world religions and philosophies.|co|early world religions and philosophies|religion,belief,monotheism,philosophy,sacred text
7.8|Explain the Middle Ages and the rise of nation-states in Europe.|ca|the rise of nation-states in medieval Europe|feudalism,knight,manor,plague,monarch
7.9|Explain how the Renaissance and the Reformation changed Europe.|ca|the Renaissance and the Reformation|Renaissance,Reformation,humanism,printing press,Protestant`,
"8":`8.1|Examine the development of the United States from exploration to 1754.|se|the colonization of North America|colony,explorer,settlement,trade,charter
8.2|Explain the people, factors, and events that led to the American Revolution and a new government.|ca|the American Revolution|tax,representation,independence,revolution,Patriot
8.3|Explain how the Constitution of the United States developed.|se|the writing of the Constitution|Constitution,compromise,federalism,ratify,Bill of Rights
8.4|Analyze the challenges and central ideas involved in creating the new nation.|ex|the challenges of the new nation|precedent,cabinet,political party,neutrality,federal
8.5|Explain the causes, effects, and challenges of westward expansion.|ca|westward expansion|expansion,Manifest Destiny,territory,removal,frontier
8.6|Explain the causes, effects, and challenges of the Industrial Revolution.|ca|the Industrial Revolution|factory,invention,labor,urban,textile
8.7|Evaluate the impact of social and political reforms on American society.|ar|the reform movements|reform,abolition,suffrage,temperance,movement
8.8|Explain the conflicts between the North and the South that led to the Civil War.|ca|the conflict between the North and the South|sectionalism,slavery,compromise,secede,states' rights
8.9|Identify key people and evaluate the major events of the Civil War.|se|the Civil War|Union,Confederacy,battle,Emancipation,surrender
8.10|Analyze Reconstruction after the Civil War.|ca|Reconstruction|Reconstruction,amendment,freedmen,Black Codes,sharecropping`,
"Mississippi Studies":`MS.1|Examine Mississippi's geographic features and how they shaped its development.|ex|Mississippi's geography|region,Delta,soil,river,landform
MS.2|Compare the Indigenous cultures of Mississippi and their lasting influence.|co|the Indigenous cultures of Mississippi|Choctaw,Chickasaw,Natchez,culture,mound
MS.3|Explain the motives for and effects of European arrival in Mississippi.|ca|European arrival in Mississippi|explorer,colony,trade,settlement,conflict
MS.4|Explain how the Mississippi Territory became a state.|se|Mississippi's path to statehood|territory,statehood,treaty,removal,constitution
MS.5|Analyze antebellum plantation life and the growth of slavery in Mississippi.|ca|the growth of slavery in antebellum Mississippi|antebellum,plantation,cotton,enslaved,economy
MS.6|Analyze Mississippi's role in the Civil War and the effects of Reconstruction.|ca|the Civil War and Reconstruction in Mississippi|secession,Vicksburg,Reconstruction,amendment,freedmen
MS.7|Examine the economic, political, and social changes of the Jim Crow era through World War II.|ca|Jim Crow in Mississippi|Jim Crow,segregation,sharecropping,migration,disenfranchise
MS.8|Evaluate Mississippi's role in the Civil Rights Movement.|ar|the Civil Rights Movement in Mississippi|civil rights,boycott,Freedom Summer,voter registration,activist
MS.9|Analyze the economy of modern Mississippi.|de|Mississippi's economy today|industry,agriculture,manufacturing,tourism,workforce
MS.10|Explain how state and local government are structured and how they work.|ex|state and local government|legislature,governor,county,municipal,constitution
MS.11|Explain how Mississippi's artists, musicians, and writers influenced the world.|ex|Mississippi's artists, musicians, and writers|blues,author,literature,influence,heritage
MS.12|Describe the contributions of Mississippi's ethnic and religious groups.|de|Mississippi's ethnic and religious groups|ethnic,immigrant,religion,contribution,community`,
"World History":`WH.1|Investigate the key ideas and achievements of the Scientific Revolution and the Enlightenment.|ex|the Scientific Revolution and the Enlightenment|reason,scientific method,natural rights,philosopher,social contract
WH.2|Analyze the causes of the French Revolution and its effects on Europe.|ca|the French Revolution|monarchy,estate,revolution,republic,Napoleon
WH.3|Examine the origins and spread of the Agricultural and Industrial Revolutions.|ca|the Industrial Revolution|industrialization,factory,enclosure,urbanization,steam engine
WH.4|Compare capitalism with the economic responses to industrialization.|co|capitalism, socialism, and communism|capitalism,socialism,communism,labor union,market
WH.5|Explain the role of nationalism in nineteenth-century revolutions and unifications.|ca|nationalism in the 1800s|nationalism,unification,nation-state,empire,revolution
WH.6|Explain the global impact of Western imperialism.|ca|imperialism|imperialism,colony,resource,resistance,sphere of influence
WH.7|Explain the causes, major events, and effects of World War I.|ca|World War I|alliance,militarism,trench,armistice,treaty
WH.8|Explain the challenges of the interwar period, including the rise of totalitarian states.|ca|the rise of totalitarian states|totalitarian,fascism,depression,dictator,propaganda
WH.9|Explain the causes, major events, and effects of World War II.|ca|World War II|Axis,Allies,Holocaust,appeasement,atomic bomb
WH.10|Explain the recovery after World War II and the effects of the Cold War.|ca|the Cold War|Cold War,communism,containment,arms race,superpower
WH.11|Explain the changing role of globalization in the contemporary world.|ex|globalization|globalization,trade,technology,migration,interdependence`,
"U.S. History":`USH.1|Trace how westward movement and economic change reshaped regions and democracy after Reconstruction.|ca|westward expansion after Reconstruction|frontier,railroad,reservation,New South,homestead
USH.2|Analyze industrialization and its effects on the economy, immigration, and labor.|ca|industrialization|industry,monopoly,immigration,labor union,urbanization
USH.3|Explain the causes, goals, and results of the Progressive Movement.|ca|the Progressive Movement|progressive,reform,muckraker,suffrage,regulation
USH.4|Explain America's rise to world power through imperialism and World War I.|ca|America's rise to world power|imperialism,annex,neutrality,alliance,armistice
USH.5|Explain the clash between tradition and modern life in the 1920s and 1930s.|ex|tradition and change in the 1920s|prohibition,Harlem Renaissance,consumer,mass culture,nativism
USH.6|Explain the causes of the Great Depression and how the New Deal expanded federal power.|ca|the Great Depression|depression,stock market,unemployment,New Deal,relief
USH.7|Explain the shift from isolationism, the strategy, and the home front in World War II.|ca|America's entry into World War II|isolationism,mobilize,home front,internment,Allies
USH.8|Explain Cold War policy and social change under Presidents Truman and Eisenhower.|ex|the early Cold War|containment,Cold War,Korea,space race,suburb
USH.9|Explain the major issues of the Kennedy, Johnson, and Nixon years.|ex|the 1960s and early 1970s|Great Society,Vietnam,protest,Watergate,counterculture
USH.10|Explain the rise of conservatism from 1974 to 1992 and its effects on policy.|ca|the rise of conservatism|conservatism,deregulation,inflation,Cold War,tax cut
USH.11|Evaluate the leaders, federal actions, and protests of the Civil Rights Movement.|ar|the Civil Rights Movement|segregation,boycott,nonviolence,Civil Rights Act,voting rights
USH.12|Explain key domestic issues and America's role in the world from 1992 to the present.|ex|the United States since 1992|globalization,terrorism,technology,election,economy`,
"U.S. Government":`USG.1|Explain the core principles of democracy.|ex|the principles of democracy|democracy,popular sovereignty,rule of law,consent,majority rule
USG.2|Explain the ideas that shaped the government of the United States.|ex|the ideas behind the United States government|Enlightenment,natural rights,social contract,republic,federalism
USG.3|Assess how the federal government is organized and how it operates.|ex|the three branches of the federal government|legislative,executive,judicial,checks and balances,separation of powers
USG.4|Explain how public policy is made and carried out.|se|the policy process|policy,bill,agency,budget,regulation
USG.5|Explain how power is divided among national, state, and local governments.|co|national, state, and local governments|federalism,reserved powers,concurrent,state,local
USG.6|Distinguish civil rights from civil liberties and explain how their interpretation has changed.|co|civil rights and civil liberties|civil rights,civil liberties,amendment,due process,equal protection
USG.7|Explain how the media, interest groups, and political parties link citizens to government.|ex|the media, interest groups, and political parties|media,interest group,political party,lobby,campaign
USG.8|Assess the rights and responsibilities of citizens in American democracy.|ar|the rights and responsibilities of citizens|citizen,vote,jury,participate,responsibility`};
/* ELA: strand, number, [K-2, 3-5, 6-12 wording], function, focus, words. Codes are built per grade. */
const ELA=[
["RL",1,["Ask and answer questions about key details in a story.","Use details and examples from a story to explain what it says and to make inferences.","Cite evidence from a literary text to support what it says and what it implies."],"ar","what a story says and implies","detail,evidence,infer,cite,quote,support"],
["RL",2,["Retell stories and tell the central message or lesson.","Determine the theme of a story from its details and summarize it.","Determine a theme, analyze how it develops, and summarize the text objectively."],"su","a story and its theme","theme,central message,summarize,detail,develop,lesson"],
["RL",3,["Describe the characters, settings, and major events in a story.","Describe a character, setting, or event in depth using details from the text.","Analyze how characters, events, and setting interact and develop over the text."],"de","the characters, setting, and events of a story","character,setting,event,trait,motive,conflict"],
["RL",4,["Identify words and phrases in a story that suggest feelings or appeal to the senses.","Determine the meaning of words and phrases in a story, including figurative language.","Determine figurative and connotative meanings and explain how word choice shapes meaning and tone."],"ex","the meaning of words and phrases in a story","figurative,literal,tone,phrase,connotation,simile"],
["RI",1,["Ask and answer questions about key details in an informational text.","Use details and examples from a text to explain what it says and to make inferences.","Cite evidence from an informational text to support what it says and what it implies."],"ar","what an informational text says and implies","detail,evidence,infer,cite,source,support"],
["RI",2,["Identify the main topic of a text and retell key details.","Determine the main idea of a text, explain how details support it, and summarize.","Determine central ideas, analyze how they develop, and summarize the text objectively."],"su","an informational text and its central idea","main idea,central idea,key detail,summarize,support,topic"],
["RI",4,["Ask and answer questions to learn the meaning of words in a text.","Determine the meaning of academic and subject-specific words in a text.","Determine the meaning of words and phrases in a text, including technical and figurative meanings."],"ex","the meaning of key words in a text","context clue,definition,technical,phrase,meaning,synonym"],
["RI",8,["Identify the reasons an author gives to support points in a text.","Explain how an author uses reasons and evidence to support points in a text.","Trace and evaluate an argument, judging whether the reasoning is sound and the evidence is relevant and sufficient."],"ar","an author's argument","claim,reason,evidence,argument,relevant,sufficient"],
["W",1,["Write, or draw and dictate, an opinion and give a reason for it.","Write opinion pieces that support a point of view with reasons and information.","Write arguments that support claims with clear reasons and relevant evidence."],"ar","a topic or text","claim,opinion,reason,evidence,counterclaim,conclusion"],
["W",2,["Write, or draw and dictate, to name a topic and give facts about it.","Write informative texts that examine a topic and convey ideas clearly.","Write informative texts that examine a topic through well-chosen, organized, and analyzed content."],"ex","a topic","topic,fact,definition,detail,organize,explain"],
["W",3,["Write, or draw and dictate, to tell about events in order.","Write narratives about real or imagined events using details and a clear sequence.","Write narratives using effective technique, well-chosen details, and well-structured event sequences."],"se","a real or imagined experience","narrative,event,sequence,dialogue,detail,conclusion"],
["SL",1,["Take part in conversations with partners, following agreed rules.","Engage in collaborative discussions, building on others' ideas and expressing your own clearly.","Come prepared and take part in collaborative discussions, building on others' ideas and expressing your own clearly."],"ex","their ideas in a discussion","discuss,agree,disagree,build on,clarify,respond"],
["SL",4,["Describe people, places, things, and events with relevant details.","Report on a topic or tell a story with facts and details, speaking clearly.","Present claims and findings in a clear, logical order with relevant evidence."],"de","a topic for an audience","present,audience,detail,clearly,order,evidence"],
["L",4,["Determine the meaning of unknown and multiple-meaning words.","Determine the meaning of unknown and multiple-meaning words using context, word parts, and references.","Determine the meaning of unknown and multiple-meaning words using context, word parts, and references."],"ex","the meaning of unknown words","context,prefix,suffix,root,multiple-meaning,dictionary"]];
