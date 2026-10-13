/* The Picture Dictionary — scene art. Flat vector, drawn in code, original.
   Each scene is 1000×560. Objects are small functions; a scene places them
   and the page draws the numbered hotspots at the same coordinates. */
(function(){
'use strict';
var C={navy:'#1E2761',navy2:'#2B3470',gold:'#C9A227',gold2:'#EBD9A0',teal:'#17606F',teal2:'#4FC7D2',red:'#B5213F',pink:'#F3A6B8',paper:'#FFFFFF',cream:'#F4F1E8',gray:'#C9CEEA',gray2:'#8A8FA8',dark:'#1F2340',wood:'#B07A45',wood2:'#8B5A2B',skin:'#C9915F',skin2:'#8D5A3C',skin3:'#E8B98F',green:'#4C9A6A',green2:'#7FD3A1',sky:'#DDEBFF',blue:'#3B6FD1',orange:'#E07A3F',brown:'#6E4520'};
function g(x,y,s,inner){return '<g transform="translate('+x+' '+y+') scale('+(s||1)+')">'+inner+'</g>'}
function r(x,y,w,h,f,rx,extra){return '<rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" fill="'+f+'"'+(rx?' rx="'+rx+'"':'')+(extra||'')+'/>'}
function c(x,y,rad,f,extra){return '<circle cx="'+x+'" cy="'+y+'" r="'+rad+'" fill="'+f+'"'+(extra||'')+'/>'}
function p(d,f,extra){return '<path d="'+d+'" fill="'+f+'"'+(extra||'')+'/>'}
function ln(x1,y1,x2,y2,st,w){return '<line x1="'+x1+'" y1="'+y1+'" x2="'+x2+'" y2="'+y2+'" stroke="'+st+'" stroke-width="'+(w||3)+'" stroke-linecap="round"/>'}
function t(x,y,s,f,size,extra){return '<text x="'+x+'" y="'+y+'" fill="'+f+'" font-family="Inter,sans-serif" font-size="'+size+'" font-weight="700" text-anchor="middle"'+(extra||'')+'>'+s+'</text>'}
function room(wall,floor,split){return r(0,0,1000,560,wall)+r(0,split||380,1000,560-(split||380),floor)+r(0,(split||380)-8,1000,8,'rgba(0,0,0,.08)')}
/* ── people ── */
function person(o){o=o||{};var sk=o.skin||C.skin,sh=o.shirt||C.teal,pa=o.pants||C.navy,hair=o.hair||'#2a1d14',hat=o.hat||'',face=o.face||'';
 var s='';s+=p('M-28 190 L-28 95 L28 95 L28 190 Z',pa)+r(-30,180,22,16,C.dark,3)+r(8,180,22,16,C.dark,3);
 s+=p('M-38 100 C-38 60 -22 48 0 48 C22 48 38 60 38 100 L38 110 L-38 110 Z',sh)+p('M-38 70 L-62 120 L-50 126 L-34 92 Z',sh)+p('M38 70 L62 120 L50 126 L34 92 Z',sh)+c(-58,128,8,sk)+c(58,128,8,sk);
 s+=r(-9,36,18,16,sk)+c(0,20,24,sk)+p('M-24 18 C-24 -4 -10 -8 0 -8 C10 -8 24 -4 24 18 C18 6 8 2 0 4 C-8 2 -18 6 -24 18 Z',hair);
 s+=c(-8,20,2.5,C.dark)+c(8,20,2.5,C.dark)+(face==='sad'?p('M-8 32 Q0 26 8 32',"none",' stroke="#7a3a3a" stroke-width="2.5" stroke-linecap="round"'):face==='open'?c(0,30,4,'#7a3a3a'):p('M-8 28 Q0 34 8 28',"none",' stroke="#7a3a3a" stroke-width="2.5" stroke-linecap="round"'));
 if(hat==='cap')s+=p('M-26 10 C-26 -8 26 -8 26 10 L34 12 L-26 12 Z',o.hatc||C.navy);
 if(hat==='chef')s+=p('M-22 6 C-26 -18 26 -18 22 6 Z',C.paper)+r(-22,2,44,10,C.paper);
 if(hat==='hard')s+=p('M-26 10 C-26 -10 26 -10 26 10 Z',C.gold)+r(-30,8,60,6,C.gold,2);
 if(hat==='police')s+=p('M-24 8 C-24 -6 24 -6 24 8 Z',C.navy)+r(-28,6,56,6,C.dark,2)+c(0,0,4,C.gold);
 if(hat==='fire')s+=p('M-26 10 C-26 -8 26 -8 26 10 Z',C.red)+r(-32,8,64,6,C.red,2)+r(-4,-4,8,8,C.gold,1);
 if(hat==='helmet')s+=p('M-26 12 C-26 -10 26 -10 26 12 Z',C.gray2)+r(-18,0,36,10,'#2b2b2b',2);
 if(hat==='straw')s+=p('M-22 8 C-22 -8 22 -8 22 8 Z',C.gold2)+r(-34,6,68,6,C.gold2,3)+r(-22,2,44,5,C.navy);
 if(o.coat)s+=p('M-40 100 C-40 60 -22 50 0 50 C22 50 40 60 40 100 L40 150 L-40 150 Z',C.paper)+p('M-6 52 L0 90 L6 52 Z',sh);
 if(o.vest)s+=r(-30,60,60,50,C.orange,4)+r(-30,78,60,6,C.gold2)+r(-30,94,60,6,C.gold2);
 if(o.scrubs)s+=p('M-38 100 C-38 60 -22 48 0 48 C22 48 38 60 38 100 L38 110 L-38 110 Z',C.teal2)+p('M-10 48 L0 64 L10 48 Z',C.paper);
 if(o.apron)s+=p('M-24 70 L24 70 L30 150 L-30 150 Z',C.paper)+r(-10,52,20,20,C.paper);
 return s}
/* ── classroom ── */
function desk(){return r(-60,0,120,10,C.wood,3)+r(-54,10,8,60,C.wood2)+r(46,10,8,60,C.wood2)}
function chair(){return r(-22,0,44,8,C.navy,2)+r(-20,-40,40,40,C.navy,6)+r(-18,8,5,44,C.gray2)+r(13,8,5,44,C.gray2)}
function whiteboard(){return r(-170,-70,340,140,C.paper,4,' stroke="#9aa0b4" stroke-width="6"')+ln(-140,-30,-20,-30,C.navy,4)+ln(-140,-6,60,-6,C.navy,4)+ln(-140,18,20,18,C.red,4)+r(-170,70,340,8,C.gray2,2)}
function marker(){return r(-22,-6,44,12,C.red,6)+r(10,-6,12,12,C.dark,3)}
function clock(){return c(0,0,30,C.paper,' stroke="'+C.navy+'" stroke-width="5"')+ln(0,0,0,-18,C.dark,4)+ln(0,0,12,8,C.dark,4)+c(0,0,3,C.red)}
function backpack(){return r(-26,-30,52,70,C.red,14)+r(-18,-40,36,24,C.red,10)+r(-18,0,36,30,'#8E1A33',8)+r(-6,-34,12,6,C.dark,3)}
function notebook(){return r(-26,-34,52,68,C.teal,4)+r(-26,-34,10,68,C.navy)+ln(-8,-16,16,-16,C.paper,3)+ln(-8,0,16,0,C.paper,3)+ln(-8,16,16,16,C.paper,3)}
function pencil(){return r(-40,-6,70,12,C.gold,2)+p('M30 -6 L46 0 L30 6 Z',C.skin3)+p('M40 -2.5 L46 0 L40 2.5 Z',C.dark)+r(-48,-6,8,12,C.pink,2)}
function laptop(){return r(-50,-34,100,64,C.dark,5)+r(-44,-28,88,52,C.sky)+r(-60,30,120,8,C.gray2,3)}
function globe(){return c(0,-10,34,C.blue)+p('M-24 -32 C-6 -18 -4 0 -20 14 C-8 8 8 6 22 -4 C14 -20 6 -30 -24 -32 Z',C.green)+p('M4 2 C14 10 20 18 10 24 C4 16 0 10 4 2 Z',C.green)+r(-6,22,12,16,C.gray2)+r(-24,36,48,8,C.wood2,3)}
function wallmap(){return r(-70,-45,140,90,C.sky,3,' stroke="'+C.gray2+'" stroke-width="4"')+p('M-56 -20 C-40 -36 -10 -34 0 -18 C12 -6 30 -10 50 -24 L52 20 C34 30 10 24 -10 32 C-30 36 -54 20 -56 -20 Z',C.green2)}
function trash(){return p('M-22 -24 L22 -24 L18 36 L-18 36 Z',C.gray2)+r(-26,-30,52,8,C.dark,3)+ln(-8,-12,-6,24,C.paper,3)+ln(8,-12,6,24,C.paper,3)}
/* ── school ── */
function locker(){return r(-18,-60,36,120,C.navy,3)+r(-12,-50,24,6,C.navy2)+r(-12,-40,24,6,C.navy2)+c(8,0,3,C.gold)}
function door(){return r(-30,-80,60,160,C.wood,3)+c(18,0,4,C.gold)+r(-24,-72,48,60,C.wood2,2)}
function sign(txt,col){return r(-60,-20,120,40,col||C.navy,6)+t(0,6,txt,C.paper,16)}
function bus(){return r(-110,-40,220,80,C.gold,10)+r(-96,-30,40,30,C.sky,3)+r(-46,-30,40,30,C.sky,3)+r(4,-30,40,30,C.sky,3)+r(54,-30,44,30,C.sky,3)+c(-70,42,16,C.dark)+c(70,42,16,C.dark)+r(-110,8,220,8,C.dark)}
function stairs(){var s='';for(var i=0;i<5;i++)s+=r(-60+i*24,40-i*18,24,18+i*18,C.gray2);return s}
function exitsign(){return r(-34,-14,68,28,C.green,4)+t(0,6,'EXIT',C.paper,16)}
function table(){return r(-70,0,140,10,C.wood,3)+r(-62,10,8,50,C.wood2)+r(54,10,8,50,C.wood2)}
function books(){return r(-30,-30,12,60,C.red,2)+r(-16,-30,12,60,C.teal,2)+r(-2,-30,12,60,C.gold,2)+r(12,-30,12,60,C.navy,2)}
function ball(){return c(0,0,22,C.orange)+ln(-22,0,22,0,C.dark,2)+ln(0,-22,0,22,C.dark,2)+p('M-15 -16 Q0 0 -15 16',"none",' stroke="'+C.dark+'" stroke-width="2"')+p('M15 -16 Q0 0 15 16',"none",' stroke="'+C.dark+'" stroke-width="2"')}
/* ── kitchen ── */
function stove(){return r(-60,-20,120,80,C.gray,4)+r(-60,-20,120,12,C.dark,2)+c(-32,-14,12,C.dark)+c(32,-14,12,C.dark)+c(-32,-14,6,C.red)+c(32,-14,6,C.red)+r(-50,6,100,40,C.dark,3)+r(-40,14,80,24,'#3a3a3a',2)}
function fridge(){return r(-45,-110,90,220,C.gray,6)+ln(-45,-40,45,-40,C.gray2,4)+r(30,-80,6,30,C.dark,3)+r(30,-20,6,40,C.dark,3)}
function sink(){return r(-60,-14,120,30,C.gray,6)+r(-48,-8,96,18,'#9aa0b4',4)+p('M0 -14 L0 -40 C0 -52 24 -52 24 -40',"none",' stroke="'+C.dark+'" stroke-width="6" stroke-linecap="round"')+r(-60,16,120,60,C.wood,3)}
function microwave(){return r(-50,-28,100,56,C.dark,6)+r(-42,-20,64,40,'#4a4a4a',3)+c(34,-12,5,C.gold)+c(34,6,5,C.paper)}
function pot(){return r(-34,-20,68,40,C.gray2,4)+r(-40,-26,80,8,C.dark,3)+r(-50,-6,12,6,C.dark,2)+r(38,-6,12,6,C.dark,2)}
function pan(){return c(0,0,30,C.dark)+c(0,0,22,'#4a4a4a')+r(28,-5,50,10,C.dark,4)}
function knife(){return p('M-40 0 L10 -10 L10 10 Z',C.gray)+r(10,-5,40,10,C.wood2,3)}
function board(){return r(-50,-30,100,60,C.wood,5)+c(36,-18,5,C.cream)}
function plate(){return c(0,0,34,C.paper,' stroke="'+C.gray+'" stroke-width="5"')+c(0,0,20,C.cream)}
function cup(){return r(-20,-24,40,48,C.teal,5)+p('M20 -14 C40 -14 40 10 20 10',"none",' stroke="'+C.teal+'" stroke-width="7"')}
function spoon(){return c(-22,0,12,C.gray)+r(-12,-4,50,8,C.gray,4)}
/* ── home ── */
function bed(){return r(-110,-10,220,60,C.navy,8)+r(-110,-40,220,40,C.teal2,8)+r(-100,-60,70,26,C.paper,8)+r(-110,50,10,20,C.wood2)+r(100,50,10,20,C.wood2)}
function pillow(){return r(-36,-20,72,40,C.paper,12,' stroke="'+C.gray+'" stroke-width="3"')}
function blanket(){return r(-60,-30,120,60,C.red,8)+ln(-60,-10,60,-10,C.pink,4)+ln(-60,10,60,10,C.pink,4)}
function lamp(){return p('M-30 -20 L30 -20 L18 -60 L-18 -60 Z',C.gold2)+r(-3,-20,6,50,C.dark)+r(-20,30,40,8,C.dark,3)}
function dresser(){return r(-60,-50,120,100,C.wood,4)+r(-50,-40,100,22,C.wood2,3)+r(-50,-10,100,22,C.wood2,3)+r(-50,20,100,22,C.wood2,3)+c(0,-29,3,C.gold)+c(0,1,3,C.gold)+c(0,31,3,C.gold)}
function closet(){return r(-60,-90,120,180,C.cream,4,' stroke="'+C.wood2+'" stroke-width="5"')+ln(0,-90,0,90,C.wood2,5)+c(-10,0,4,C.gold)+c(10,0,4,C.gold)}
function windowf(){return r(-70,-60,140,120,C.sky,3,' stroke="'+C.paper+'" stroke-width="8"')+ln(0,-60,0,60,C.paper,6)+ln(-70,0,70,0,C.paper,6)+c(40,-30,14,C.gold)}
function curtain(){return p('M-20 -70 C-10 -30 -10 30 -20 70 L-60 70 C-50 30 -50 -30 -60 -70 Z',C.red)}
function mirror(){return '<ellipse cx="0" cy="0" rx="34" ry="46" fill="'+C.sky+'" stroke="'+C.gold+'" stroke-width="6"/>'+ln(-14,-24,-4,-34,C.paper,4)}
function rug(){return '<ellipse cx="0" cy="0" rx="120" ry="34" fill="'+C.teal+'"/><ellipse cx="0" cy="0" rx="90" ry="22" fill="'+C.teal2+'"/>'}
function alarm(){return c(0,0,26,C.paper,' stroke="'+C.red+'" stroke-width="6"')+ln(0,0,0,-14,C.dark,4)+ln(0,0,10,6,C.dark,4)+c(-18,-22,7,C.red)+c(18,-22,7,C.red)}
/* ── grocery ── */
function cart(){return p('M-50 -40 L-34 -40 L-20 20 L40 20 L50 -20 L-30 -20',"none",' stroke="'+C.gray2+'" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"')+c(-14,34,8,C.dark)+c(34,34,8,C.dark)+r(-26,-18,66,38,'rgba(138,143,168,.25)')}
function basket(){return p('M-36 -10 L36 -10 L28 30 L-28 30 Z',C.red)+p('M-24 -10 C-24 -40 24 -40 24 -10',"none",' stroke="'+C.red+'" stroke-width="6"')}
function receipt(){return p('M-20 -40 L20 -40 L20 34 L12 28 L4 34 L-4 28 L-12 34 L-20 28 Z',C.paper,' stroke="'+C.gray2+'" stroke-width="2"')+ln(-12,-26,12,-26,C.gray2,3)+ln(-12,-14,12,-14,C.gray2,3)+ln(-12,-2,4,-2,C.gray2,3)}
function shelf(){var s=r(-90,-70,180,8,C.wood)+r(-90,-20,180,8,C.wood)+r(-90,30,180,8,C.wood);for(var i=0;i<5;i++){s+=r(-80+i*34,-104,24,34,[C.red,C.gold,C.teal,C.navy,C.green][i],3)+r(-80+i*34,-54,24,34,[C.teal,C.navy,C.red,C.gold,C.orange][i],3)+r(-80+i*34,-4,24,34,[C.green,C.orange,C.gold,C.teal,C.red][i],3)}return s}
function scale(){return r(-40,0,80,14,C.gray2,4)+r(-30,-10,60,10,C.gray,2)+r(-4,14,8,30,C.dark)+r(-30,44,60,10,C.dark,3)+c(0,-20,16,C.paper,' stroke="'+C.dark+'" stroke-width="4"')+ln(0,-20,8,-28,C.red,3)}
function bag(){return p('M-28 -20 L28 -20 L34 40 L-34 40 Z',C.wood,' stroke="'+C.wood2+'" stroke-width="2"')+p('M-14 -20 C-14 -40 14 -40 14 -20',"none",' stroke="'+C.wood2+'" stroke-width="4"')}
function coupon(){return r(-40,-20,80,40,C.gold2,4,' stroke="'+C.gold+'" stroke-width="3" stroke-dasharray="6 4"')+t(0,6,'50¢ OFF',C.navy,13)}
function pricetag(){return p('M-30 -16 L16 -16 L30 0 L16 16 L-30 16 Z',C.gold)+t(-8,5,'$2.49',C.navy,12)}
function register(){return r(-40,-10,80,40,C.dark,5)+r(-30,-40,40,30,C.gray,3)+r(-24,-34,28,18,C.green2,2)+r(16,-34,20,22,C.gray2,2)}
function freezer(){return r(-70,-50,140,100,C.gray,6)+r(-62,-42,124,50,C.sky,3)+r(-62,10,124,34,'#9aa0b4',3)+c(40,-20,6,C.paper)}
/* ── clinic ── */
function thermometer(){return r(-6,-40,12,60,C.paper,6,' stroke="'+C.gray2+'" stroke-width="3"')+c(0,26,10,C.red)+r(-3,-20,6,44,C.red)}
function bandage(){return r(-34,-12,68,24,C.skin3,12)+r(-14,-10,28,20,C.paper,2)+c(-6,-4,1.5,C.gray2)+c(6,4,1.5,C.gray2)}
function medicine(){return r(-20,-30,40,60,C.orange,6)+r(-22,-36,44,12,C.paper,3)+r(-14,-10,28,20,C.paper,2)}
function prescription(){return r(-30,-40,60,80,C.paper,3,' stroke="'+C.gray2+'" stroke-width="3"')+t(-12,-16,'Rx',C.navy,18)+ln(-18,0,18,0,C.gray2,3)+ln(-18,12,10,12,C.gray2,3)+ln(-18,24,18,24,C.gray2,3)}
function stethoscope(){return p('M-26 -40 C-26 10 26 10 26 -40',"none",' stroke="'+C.dark+'" stroke-width="6"')+p('M0 -16 L0 20 C0 36 24 36 24 20',"none",' stroke="'+C.dark+'" stroke-width="6"')+c(26,22,10,C.gray2)}
function wheelchair(){return c(-10,30,30,'none',' stroke="'+C.dark+'" stroke-width="6"')+c(34,44,12,'none',' stroke="'+C.dark+'" stroke-width="5"')+p('M-6 -34 L-6 10 L34 10 L40 30',"none",' stroke="'+C.navy+'" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"')}
function calendar(){return r(-40,-36,80,72,C.paper,4,' stroke="'+C.gray2+'" stroke-width="3"')+r(-40,-36,80,18,C.red,4)+t(0,12,'14',C.navy,30)}
function waitingchairs(){return chair()+g(56,0,1,chair())+g(112,0,1,chair())}
/* ── street ── */
function trafficlight(){return r(-16,-60,32,100,C.dark,6)+c(0,-40,10,C.red)+c(0,-10,10,C.gold)+c(0,20,10,C.green2)+r(-4,40,8,60,C.gray2)}
function crosswalk(){var s='';for(var i=0;i<6;i++)s+=r(-90+i*32,-30,18,60,C.paper);return s}
function busstop(){return r(-4,-80,8,110,C.gray2)+r(-34,-90,68,30,C.navy,4)+t(0,-70,'BUS',C.paper,16)}
function building(w,h,col,label){var s=r(-w/2,-h,w,h,col,4);for(var y=-h+16;y<-30;y+=28)for(var x=-w/2+12;x<w/2-20;x+=26)s+=r(x,y,14,18,C.sky,2);s+=r(-18,-30,36,30,C.dark,3);if(label)s+=r(-w/2+6,-h+4,w-12,22,C.paper,3)+t(0,-h+20,label,C.navy,13);return s}
function gaspump(){return r(-20,-50,40,80,C.red,5)+r(-12,-42,24,18,C.paper,2)+r(14,-30,8,40,C.dark,3)}
function bench(){return r(-50,-8,100,10,C.wood,3)+r(-50,-30,100,8,C.wood,3)+r(-44,2,6,28,C.dark)+r(38,2,6,28,C.dark)}
function mailbox(){return r(-22,-30,44,36,C.blue,10)+r(-4,6,8,34,C.dark)+r(-16,-24,32,6,C.paper,2)}
function parking(){return r(-80,-40,160,80,'#5a5f73',4)+ln(-40,-40,-40,40,C.paper,3)+ln(0,-40,0,40,C.paper,3)+ln(40,-40,40,40,C.paper,3)+t(-60,8,'P',C.paper,30)}
function sidewalk(){return r(0,330,1000,30,'#bfc3cf')+r(0,360,1000,200,'#5a5f73')+ln(0,460,1000,460,C.gold,4)}
/* ── weather ── */
function sun(){var s=c(0,0,34,C.gold);for(var i=0;i<8;i++){var a=i*Math.PI/4;s+=ln(Math.cos(a)*44,Math.sin(a)*44,Math.cos(a)*58,Math.sin(a)*58,C.gold,6)}return s}
function cloud(col){col=col||C.paper;return c(-24,6,22,col)+c(0,-8,30,col)+c(26,8,22,col)+r(-30,8,60,20,col)}
function rain(){var s=cloud(C.gray);for(var i=0;i<5;i++)s+=ln(-30+i*15,34,-36+i*15,56,C.blue,4);return s}
function storm(){return cloud('#6b7190')+p('M-6 30 L10 30 L0 54 L14 54 L-10 86 L-2 60 L-14 60 Z',C.gold)}
function wind(){return p('M-50 -10 C-20 -30 10 -30 10 -10 C10 2 -8 2 -8 -8',"none",' stroke="'+C.teal2+'" stroke-width="6" stroke-linecap="round"')+p('M-50 20 C0 0 40 0 40 20 C40 34 20 34 20 22',"none",' stroke="'+C.teal2+'" stroke-width="6" stroke-linecap="round"')}
function snow(){var s=cloud(C.paper);for(var i=0;i<5;i++)s+=c(-30+i*15,44+(i%2)*10,5,C.paper,' stroke="'+C.sky+'" stroke-width="2"');return s}
function fog(){return ln(-50,-20,50,-20,'#9aa0b4',8)+ln(-40,0,40,0,'#9aa0b4',8)+ln(-50,20,50,20,'#9aa0b4',8)}
function hot(){return thermometer()+c(0,26,12,C.red)+r(-3,-30,6,54,C.red)}
function cold(){return thermometer()+c(0,26,10,C.blue)+r(-3,10,6,14,C.blue)}
function umbrella(){return p('M-50 0 C-50 -40 50 -40 50 0 Z',C.red)+ln(-50,0,50,0,C.dark,3)+ln(0,0,0,50,C.dark,4)+p('M0 50 C0 64 -16 64 -16 52',"none",' stroke="'+C.dark+'" stroke-width="4"')}
function hurricane(){return p('M0 -40 C40 -40 50 10 10 20 C-10 24 -20 6 -6 -2 C4 -6 10 4 2 8',"none",' stroke="'+C.gray2+'" stroke-width="8" stroke-linecap="round"')+p('M0 40 C-40 40 -50 -10 -10 -20 C10 -24 20 -6 6 2',"none",' stroke="'+C.gray2+'" stroke-width="8" stroke-linecap="round"')}
/* ── clothes ── */
function shirt(col){col=col||C.teal;return p('M-40 -30 L-16 -40 C-8 -30 8 -30 16 -40 L40 -30 L52 -8 L36 2 L36 50 L-36 50 L-36 2 L-52 -8 Z',col)}
function pants(col){col=col||C.navy;return p('M-30 -50 L30 -50 L34 50 L8 50 L0 -10 L-8 50 L-34 50 Z',col)}
function dress(){return p('M-20 -50 L20 -50 L26 -20 L44 50 L-44 50 L-26 -20 Z',C.red)+r(-20,-56,40,8,C.red,3)}
function jacket(){return shirt(C.navy)+p('M-6 -30 L0 50 L6 -30 Z',C.gold)}
function shoes(){return p('M-50 10 L-10 10 L10 -6 L30 10 L50 10 L50 24 L-50 24 Z',C.dark)+r(-50,20,100,6,C.paper)}
function socks(){return p('M-20 -40 L10 -40 L10 10 C30 10 34 36 10 36 L-14 36 C-26 36 -26 20 -14 16 L-20 10 Z',C.paper,' stroke="'+C.gray2+'" stroke-width="3"')+r(-20,-40,30,8,C.teal)}
function hatc(){return p('M-26 10 C-26 -26 26 -26 26 10 Z',C.red)+r(-40,8,80,8,C.red,3)}
function gloves(){return p('M-26 20 L-26 -14 L-18 -14 L-18 -30 L-10 -30 L-10 -14 L-2 -14 L-2 -34 L6 -34 L6 -14 L14 -14 L14 -28 L22 -28 L22 20 Z',C.gold)+r(-26,16,48,12,C.gold2)}
function scarf(){return p('M-34 -30 C-10 -10 10 -10 34 -30 L34 -14 C10 6 -10 6 -34 -14 Z',C.teal)+r(-10,-20,20,60,C.teal,4)+ln(-10,30,10,30,C.teal2,3)}
function belt(){return r(-50,-8,100,16,C.wood2,4)+r(-10,-12,20,24,C.gold,3,' stroke="'+C.navy+'" stroke-width="2"')}
function uniform(){return shirt(C.navy)+r(-30,-8,60,10,C.gold)+r(-26,-24,10,10,C.gold,2)}
/* ── body ── */
function bodyfig(){return person({shirt:C.teal2,pants:C.navy,skin:C.skin})}
/* ── faces ── */
function face(kind){var s=c(0,0,44,C.gold2,' stroke="'+C.gold+'" stroke-width="4"')+c(-15,-10,5,C.dark)+c(15,-10,5,C.dark);
 var m={happy:'M-18 10 Q0 30 18 10',sad:'M-18 22 Q0 6 18 22',tired:'M-16 18 L16 18',angry:'M-18 20 Q0 6 18 20',nervous:'M-18 18 Q-9 10 0 18 Q9 26 18 18',excited:'M-20 8 Q0 36 20 8 Z',bored:'M-14 18 L14 18',confused:'M-16 18 Q0 10 16 22',proud:'M-18 8 Q0 24 18 8',scared:'M-10 12 Q0 30 10 12 Z',hungry:'M-14 12 Q0 26 14 12 Z',sick:'M-16 22 Q0 10 16 22'}[kind];
 s+=p(m,kind==='excited'||kind==='scared'||kind==='hungry'?'#7a2f2f':'none',' stroke="#7a2f2f" stroke-width="4" stroke-linecap="round"');
 if(kind==='angry')s+=ln(-26,-28,-8,-20,C.dark,4)+ln(26,-28,8,-20,C.dark,4);if(kind==='sad')s+=c(18,0,3,C.blue);if(kind==='tired')s+=ln(-24,-14,-6,-14,C.dark,4)+ln(6,-14,24,-14,C.dark,4);
 if(kind==='confused')s+=t(36,-30,'?',C.navy,30);if(kind==='nervous')s+=c(-30,-26,4,C.blue)+c(-34,-14,3,C.blue);if(kind==='excited')s+=t(0,-50,'!',C.red,28);if(kind==='sick')s+=c(0,0,44,'rgba(76,154,106,.25)');if(kind==='scared')s+=c(-15,-10,8,C.paper)+c(15,-10,8,C.paper)+c(-15,-10,4,C.dark)+c(15,-10,4,C.dark);
 if(kind==='proud')s+=r(-22,-60,44,14,C.gold,3);if(kind==='hungry')s+=g(44,24,0.5,plate());if(kind==='bored')s+=ln(-24,-16,-6,-12,C.dark,4)+ln(24,-16,6,-12,C.dark,4);return s}
/* ── scenes ── */
var S={};
S.classroom=function(){return room('#EEF1FB','#D9C7A8')+g(500,150,1,whiteboard())+g(120,110,1,clock())+g(860,120,1,wallmap())+g(850,300,0.9,globe())+g(300,310,1,desk())+g(300,300,0.9,chair())+g(560,310,1,desk())+g(560,300,0.9,chair())+g(510,265,0.8,laptop())+g(240,268,0.8,notebook())+g(330,258,0.7,pencil())+g(430,230,0.8,marker())+g(150,430,1,backpack())+g(920,440,1,trash())+g(700,460,1,person({shirt:C.navy,coat:true}))}
S.school=function(){return room('#F6F2EA','#C9CEEA',400)+g(90,250,1,locker())+g(130,250,1,locker())+g(170,250,1,locker())+g(300,300,1,door())+g(300,180,0.9,sign('CAFETERIA',C.red))+g(470,300,1,door())+g(470,180,0.9,sign('LIBRARY',C.teal))+g(640,300,1,door())+g(640,180,0.9,sign('GYM',C.navy))+g(810,300,1,door())+g(810,180,0.9,sign('OFFICE',C.gold))+g(940,120,0.9,exitsign())+g(940,250,0.8,stairs())+g(560,520,0.9,bus())+g(180,470,0.8,ball())+g(380,480,0.9,person({shirt:C.red}))+g(860,470,0.9,books())}
S.kitchen=function(){return room('#FFF8E6','#D9D4C4')+g(150,260,1,fridge())+g(380,330,1,stove())+g(620,330,1,sink())+g(620,180,1,microwave())+g(300,296,0.7,pot())+g(820,300,0.8,pan())+g(830,420,0.8,board())+g(900,372,0.9,knife())+g(260,470,0.8,plate())+g(400,470,0.8,cup())+g(520,480,0.9,spoon())}
S.home=function(){return room('#EAF4F6','#C8B597')+g(330,370,1,bed())+g(270,330,0.9,pillow())+g(380,345,0.9,blanket())+g(140,300,1,lamp())+g(140,380,0.8,dresser())+g(770,230,1,closet())+g(580,170,1,windowf())+g(520,170,1,curtain())+g(920,160,0.9,mirror())+g(520,500,1,rug())+g(900,420,0.8,alarm())+g(970,300,1,door())}
S.grocery=function(){return room('#F2F4FF','#DCDEE9')+g(160,230,1,shelf())+g(400,230,1,shelf())+g(640,180,1,freezer())+g(880,300,1,register())+g(880,240,0.8,person({shirt:C.teal,apron:true}))+g(300,450,1,cart())+g(520,470,1,basket())+g(720,470,1,bag())+g(960,400,0.8,receipt())+g(620,330,0.8,scale())+g(140,440,0.9,coupon())+g(420,330,1,pricetag())}
S.clinic=function(){return room('#EEF7F6','#DDE5E4')+g(250,440,1,person({scrubs:true,coat:true,shirt:C.teal}))+g(420,440,1,person({scrubs:true,skin:C.skin3,hair:'#5a3a1a'}))+g(600,440,1,person({shirt:C.gold,face:'sad',skin:C.skin2}))+g(760,120,0.9,calendar())+g(150,150,1,thermometer())+g(300,140,1,bandage())+g(450,150,1,medicine())+g(600,150,1,prescription())+g(880,160,1,stethoscope())+g(880,420,1,wheelchair())+g(130,340,0.8,scale())+g(800,300,0.9,waitingchairs())}
S.body=function(){return room('#FFF8E6','#F4F1E8',500)+g(500,160,1.8,bodyfig())}
S.clothes=function(){return room('#F6F2EA','#EBD9A0',480)+g(130,120,1,shirt())+g(330,120,1,pants())+g(530,120,1,pants('#3B6FD1'))+g(730,120,1,dress())+g(900,120,1,jacket())+g(130,320,1,shoes())+g(330,320,1,socks())+g(530,320,1,hatc())+g(730,320,1,gloves())+g(900,310,1,scarf())+g(300,500,1,belt())+g(650,500,0.9,uniform())}
S.street=function(){return r(0,0,1000,330,C.sky)+sidewalk()+g(150,230,1,building(180,220,'#E9E6DC','BANK'))+g(380,230,1,building(160,180,'#F2DDD0','PHARMACY'))+g(620,230,1,building(200,230,'#DCE6F2','POST OFFICE'))+g(880,260,0.9,gaspump())+g(900,140,0.8,sign('GAS',C.red))+g(60,290,1,trafficlight())+g(300,420,1,crosswalk())+g(500,300,1,busstop())+g(740,310,1,bench())+g(830,320,1,mailbox())+g(560,500,0.9,parking())+t(240,350,'STOP',C.paper,12)+g(240,330,1,r(-20,-30,40,30,C.red,6)+r(-3,0,6,30,C.gray2))}
S.weather=function(){return r(0,0,1000,560,'#DDEBFF')+r(0,470,1000,90,C.green2)+g(120,120,1,sun())+g(330,110,1,cloud())+g(540,110,1,rain())+g(760,110,1,storm())+g(940,120,1,wind())+g(120,300,1,snow())+g(330,300,1,fog())+g(540,300,1,hot())+g(700,300,1,cold())+g(870,300,1,umbrella())+g(500,480,0.8,hurricane())+g(200,480,0.6,sun())}
S.jobs=function(){var row=[['teacher',{shirt:C.navy,coat:false}],['nurse',{scrubs:true}],['cook',{hat:'chef',apron:true,shirt:C.paper}],['mechanic',{shirt:C.blue,hat:'cap',hatc:C.blue}],['cashier',{shirt:C.teal,apron:true}],['farmer',{hat:'straw',shirt:C.green}],['carpenter',{hat:'hard',shirt:C.orange}],['electrician',{vest:true,shirt:C.gray2}],['truck driver',{hat:'cap',hatc:C.red,shirt:C.red}],['police officer',{hat:'police',shirt:C.navy}],['firefighter',{hat:'fire',shirt:C.red,coat:true}],['welder',{hat:'helmet',shirt:C.gray2}]];
 var s=room('#F2F4FF','#DCDEE9',300);row.forEach(function(x,i){var col=i%6,rw=Math.floor(i/6);s+=g(110+col*156,(rw?400:160),0.78,person(x[1]))});return s}
S.feelings=function(){var kinds=['happy','sad','tired','angry','nervous','excited','bored','confused','proud','scared','hungry','sick'];var s=r(0,0,1000,560,'#FFF8E6');kinds.forEach(function(k,i){s+=g(110+(i%6)*156,(i<6?150:400),1,face(k))});return s}
window.PDScenes=S;
})();
