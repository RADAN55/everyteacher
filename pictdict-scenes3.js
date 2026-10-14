/* The Picture Dictionary, Issue 3 — scene art. Builds on the Issue 1 library. */
(function(){
'use strict';
var L=window.PDLib,C=L.C,g=L.g,r=L.r,c=L.c,p=L.p,ln=L.ln,t=L.t,room=L.room,DEFS=L.DEFS,vignette=L.vignette,person=L.person;
function el(cx,cy,rx,ry,f,extra){return '<ellipse cx="'+cx+'" cy="'+cy+'" rx="'+rx+'" ry="'+ry+'" fill="'+f+'"'+(extra||'')+'/>'}
function poly(pts,f,extra){return '<polygon points="'+pts+'" fill="'+f+'"'+(extra||'')+'/>'}
/* ── science lab ── */
function beaker(){return p('M-24 -40 L24 -40 L30 30 L-30 30 Z',C.sky,' stroke="'+C.gray2+'" stroke-width="3"')+p('M-27 0 L27 0 L30 30 L-30 30 Z',C.teal2)+ln(-16,-26,-16,20,C.paper,2)}
function testtube(){return r(-10,-46,20,86,C.sky,10,' stroke="'+C.gray2+'" stroke-width="3"')+r(-8,0,16,36,C.pink,8)+r(-14,-50,28,8,C.gray2,3)}
function microscope(){return r(-40,30,80,10,C.dark,3)+r(-6,-40,12,70,C.dark)+p('M-6 -40 L30 -70 L40 -60 L4 -30 Z',C.gray2)+r(26,-90,16,30,C.dark,3)+r(-30,-10,30,6,C.gray,2)+c(-15,-2,8,C.paper)}
function goggles(){return r(-44,-14,40,28,C.sky,10,' stroke="'+C.dark+'" stroke-width="4"')+r(4,-14,40,28,C.sky,10,' stroke="'+C.dark+'" stroke-width="4"')+ln(-4,0,4,0,C.dark,4)+p('M-44 -4 C-60 -4 -60 4 -44 4',"none",' stroke="'+C.dark+'" stroke-width="4"')+p('M44 -4 C60 -4 60 4 44 4',"none",' stroke="'+C.dark+'" stroke-width="4"')}
function magnet(){return p('M-30 -30 L-30 10 C-30 40 30 40 30 10 L30 -30 L10 -30 L10 10 C10 16 -10 16 -10 10 L-10 -30 Z',C.red)+r(-30,-30,20,16,C.gray)+r(10,-30,20,16,C.gray)}
function scalebal(){return r(-4,-40,8,80,C.dark)+r(-50,40,100,8,C.dark,3)+ln(-50,-30,50,-30,C.dark,5)+p('M-50 -30 L-66 -4 L-34 -4 Z',C.gold)+p('M50 -30 L34 -4 L66 -4 Z',C.gold)}
function dropper(){return r(-5,-30,10,70,C.sky,4,' stroke="'+C.gray2+'" stroke-width="2"')+el(0,-40,12,14,C.red)+p('M-5 40 L0 52 L5 40 Z',C.sky)+c(0,66,5,C.teal2)}
function labcoat(){return person({coat:true,shirt:C.teal})}
function flame(){return r(-20,20,40,10,C.dark,3)+r(-4,-10,8,30,C.gray2)+p('M0 -60 C14 -40 18 -24 6 -14 C8 -24 2 -30 0 -36 C-2 -30 -8 -24 -6 -14 C-18 -24 -14 -40 0 -60 Z',C.orange)+p('M0 -40 C6 -30 6 -20 2 -14 C0 -20 -4 -22 -2 -28 Z',C.gold)}
function labnotebook(){return r(-28,-36,56,72,C.paper,3,' stroke="'+C.gray2+'" stroke-width="3"')+ln(-16,-20,16,-20,C.gray2,2)+ln(-16,-6,16,-6,C.gray2,2)+p('M-14 20 L-6 8 L2 14 L14 0',"none",' stroke="'+C.teal+'" stroke-width="3"')}
function periodic(){var s=r(-70,-50,140,100,C.paper,4,' stroke="'+C.gray2+'" stroke-width="3"');var cols=[C.teal2,C.gold2,C.pink,C.green2,C.sky];for(var y=0;y<5;y++)for(var x=0;x<9;x++)if(!(y<2&&x>1&&x<7))s+=r(-64+x*15,-44+y*18,13,16,cols[(x+y)%5],1);return s}
function gloves2(){return p('M-26 20 L-26 -14 L-18 -14 L-18 -30 L-10 -30 L-10 -14 L-2 -14 L-2 -34 L6 -34 L6 -14 L14 -14 L14 -28 L22 -28 L22 20 Z',C.blue)+r(-26,16,48,12,'#2C57A8')}
function labtable(){return r(-200,0,400,12,'#1F2340',3)+r(-190,12,10,80,C.gray2)+r(180,12,10,80,C.gray2)}
/* ── shapes & measurement ── */
function shape(kind){var f=C.teal;if(kind==='circle')return c(0,0,36,f);if(kind==='square')return r(-34,-34,68,68,f,4);if(kind==='triangle')return poly('0,-38 40,32 -40,32',f);if(kind==='rectangle')return r(-50,-28,100,56,f,4);if(kind==='oval')return el(0,0,46,28,f);if(kind==='star')return poly('0,-40 11,-12 40,-12 17,6 25,34 0,18 -25,34 -17,6 -40,-12 -11,-12',C.gold);if(kind==='cube')return poly('-30,-10 10,-10 10,30 -30,30',f)+poly('-30,-10 -14,-26 26,-26 10,-10','#4FC7D2')+poly('10,-10 26,-26 26,14 10,30','#0B5560');return ''}
function ruler(){var s=r(-80,-14,160,28,C.gold2,3,' stroke="'+C.gold+'" stroke-width="2"');for(var i=-72;i<=72;i+=12)s+=ln(i,-14,i,(i%36===0?-2:-8),C.navy,2);return s}
function anglef(){return ln(-40,30,40,30,C.navy,5)+ln(-40,30,30,-30,C.navy,5)+p('M-10 30 A30 30 0 0 0 -16 12',"none",' stroke="'+C.red+'" stroke-width="4"')}
function linef(){return ln(-50,20,50,-20,C.navy,6)+c(-50,20,6,C.gold)+c(50,-20,6,C.gold)}
function half(){return c(0,0,36,C.paper,' stroke="'+C.navy+'" stroke-width="4"')+p('M0 -36 A36 36 0 0 1 0 36 Z',C.red)+ln(0,-36,0,36,C.navy,3)}
function measuring(){return p('M-30 -30 L30 -30 L26 40 L-26 40 Z',C.sky,' stroke="'+C.gray2+'" stroke-width="3"')+ln(-20,-10,-6,-10,C.navy,2)+ln(-20,4,-6,4,C.navy,2)+ln(-20,18,-6,18,C.navy,2)+r(-24,8,48,30,'rgba(23,162,184,.4)')}
/* ── colors ── */
function swatch(col,extra){return r(-40,-40,80,80,col,16,' stroke="rgba(0,0,0,.12)" stroke-width="2"')+r(-30,-30,24,24,'rgba(255,255,255,.3)',6)+(extra||'')}
/* ── house & yard ── */
function house(){return r(-120,-20,240,140,'#F4EFE4')+p('M-140 -20 L0 -120 L140 -20 Z',C.red)+r(-30,40,60,80,C.wood2,3)+c(16,84,4,C.gold)+r(-100,0,50,44,C.sky,2,' stroke="'+C.paper+'" stroke-width="4"')+r(50,0,50,44,C.sky,2,' stroke="'+C.paper+'" stroke-width="4"')+r(60,-110,24,50,'#8B5A2B')}
function garage(){return r(-70,-10,140,90,'#E9E6DC')+p('M-80 -10 L0 -60 L80 -10 Z','#B5213F')+r(-56,10,112,70,C.gray2,3)+ln(-56,30,56,30,C.paper,2)+ln(-56,50,56,50,C.paper,2)}
function fence(){var s=ln(-120,0,120,0,C.paper,6)+ln(-120,24,120,24,C.paper,6);for(var i=-110;i<=110;i+=28)s+=poly((i-7)+',40 '+(i+7)+',40 '+(i+7)+',-14 '+i+',-24 '+(i-7)+',-14',C.paper);return s}
function mailbox2(){return r(-24,-20,48,30,C.navy,12)+r(-4,10,8,50,C.wood2)+p('M24 -16 L34 -16 L34 -2 L24 -2 Z',C.red)}
function driveway(){return p('M-80 0 L80 0 L120 120 L-120 120 Z','#9aa0b4')+ln(0,10,0,110,'rgba(255,255,255,.25)',3)}
function lawnmower(){return r(-40,-10,80,30,C.red,6)+c(-30,26,12,C.dark)+c(30,26,12,C.dark)+p('M30 -10 L70 -60',"none",' stroke="'+C.dark+'" stroke-width="6"')+ln(60,-66,80,-54,C.dark,6)}
function porch(){return r(-90,0,180,14,C.wood)+r(-84,-80,8,80,C.paper)+r(76,-80,8,80,C.paper)+r(-96,-88,192,10,C.paper)+g(0,-20,0.6,L.chair())}
function chimney(){return r(-18,-60,36,80,'#8B5A2B')+r(-22,-66,44,10,'#6E4520')+c(0,-80,10,'rgba(200,200,210,.6)')+c(10,-98,13,'rgba(200,200,210,.45)')}
function gate(){return r(-6,-50,12,100,C.dark)+r(-70,-40,64,80,'none',' stroke="'+C.dark+'" stroke-width="5"')+ln(-38,-40,-38,40,C.dark,4)+ln(-70,0,-6,0,C.dark,4)}
function roof(){return p('M-120 20 L0 -60 L120 20 Z',C.red)+ln(-100,8,100,8,'rgba(0,0,0,.15)',3)+ln(-80,-6,80,-6,'rgba(0,0,0,.15)',3)}
function yard(){return r(-140,0,280,60,C.green2,8)+c(-100,10,3,C.green)+c(-40,30,3,C.green)+c(60,14,3,C.green)+g(100,-30,0.5,tree())}
function tree(){return r(-10,0,20,70,C.wood2,3)+c(0,-24,44,C.green)+c(-26,-6,30,'#3C8A58')+c(26,-6,30,'#3C8A58')}
function bush(){return c(-20,0,22,C.green)+c(10,-8,26,'#3C8A58')+c(28,6,18,C.green)}
/* ── daily routines ── */
function routine(kind){var s=person({shirt:[C.teal,C.red,C.gold,C.navy,C.green,C.orange][kind.length%6]});
 if(kind==='wake')s+=g(60,-10,0.5,L.clock())+t(-60,0,'z z',C.navy,20);if(kind==='brush')s+=g(60,110,0.5,'<rect x="-6" y="-40" width="12" height="80" rx="6" fill="'+C.blue+'"/><rect x="-8" y="-44" width="16" height="22" rx="4" fill="'+C.paper+'"/>');
 if(kind==='shower')s+=g(70,-40,0.6,'<ellipse cx="0" cy="0" rx="22" ry="8" fill="'+C.gray+'"/><line x1="-14" y1="10" x2="-18" y2="60" stroke="'+C.teal2+'" stroke-width="3"/><line x1="0" y1="10" x2="0" y2="64" stroke="'+C.teal2+'" stroke-width="3"/><line x1="14" y1="10" x2="18" y2="60" stroke="'+C.teal2+'" stroke-width="3"/>');
 if(kind==='dress')s+=g(-70,100,0.6,L.shirt(C.red));if(kind==='breakfast')s+=g(70,110,0.5,L.plate())+g(70,80,0.4,L.cup());if(kind==='walk')s+=g(0,200,1,'<line x1="-60" y1="0" x2="60" y2="0" stroke="'+C.gray2+'" stroke-width="4"/><line x1="-80" y1="-10" x2="-50" y2="-10" stroke="'+C.gray2+'" stroke-width="2"/>');
 if(kind==='study')s+=g(60,110,0.5,L.notebook())+g(90,96,0.4,L.pencil());if(kind==='lunch')s+=g(-70,110,0.6,'<path d="M-30 -10 L30 -10 C26 16 -26 16 -30 -10 Z" fill="'+C.paper+'" stroke="'+C.gray+'" stroke-width="3"/><circle cx="-8" cy="-14" r="8" fill="'+C.green+'"/><circle cx="8" cy="-14" r="8" fill="'+C.red+'"/>');
 if(kind==='work')s+=g(70,120,0.5,'<rect x="-40" y="-26" width="80" height="52" rx="6" fill="'+C.wood2+'"/><rect x="-10" y="-34" width="20" height="10" rx="3" fill="'+C.dark+'"/>');if(kind==='cook')s+=g(70,120,0.5,'<rect x="-34" y="-20" width="68" height="40" rx="4" fill="'+C.gray2+'"/><rect x="-40" y="-26" width="80" height="8" rx="3" fill="'+C.dark+'"/>');
 if(kind==='homework')s+=g(0,-40,0.6,L.desk())+g(0,-50,0.5,L.laptop());if(kind==='sleep')s=g(0,70,0.9,L.rug().replace(/#17606F/g,C.navy).replace(/#4FC7D2/g,C.teal2))+'<g transform="rotate(-90) translate(-60,0) scale(.8)">'+person({shirt:C.sky})+'</g>'+t(60,-60,'z z z',C.navy,22);
 return s}
/* ── describing people ── */
function descr(kind){var o={shirt:C.teal};var s='';
 if(kind==='tall')s='<g transform="scale(1,1.25) translate(0,-30)">'+person(o)+'</g>';else if(kind==='short')s='<g transform="scale(.9,.75) translate(0,60)">'+person(o)+'</g>';
 else if(kind==='young')s='<g transform="scale(.85) translate(0,30)">'+person({shirt:C.gold,hair:'#5a3a1a'})+'</g>';else if(kind==='old')s=person({shirt:C.brown,hair:'#C9CEEA'})+p('M-14 32 C-6 42 6 42 14 32',"none",' stroke="#C9CEEA" stroke-width="5"')+ln(50,100,56,196,C.wood2,5);
 else if(kind==='curly')s=person(o)+c(-24,4,10,'#2a1d14')+c(24,4,10,'#2a1d14')+c(-14,-10,10,'#2a1d14')+c(14,-10,10,'#2a1d14')+c(0,-14,10,'#2a1d14');else if(kind==='straight')s=person({shirt:C.red,hair:'#1a1a1a'})+p('M-26 10 L-30 80 L-14 80 L-16 20 Z','#1a1a1a')+p('M26 10 L30 80 L14 80 L16 20 Z','#1a1a1a');
 else if(kind==='long')s=person({shirt:C.pink,hair:'#3a2418'})+p('M-26 10 L-34 110 L-10 110 L-16 20 Z','#3a2418')+p('M26 10 L34 110 L10 110 L16 20 Z','#3a2418');else if(kind==='glasses')s=person(o)+r(-24,12,20,16,'none',' stroke="'+C.dark+'" stroke-width="3" rx="5"')+r(4,12,20,16,'none',' stroke="'+C.dark+'" stroke-width="3" rx="5"')+ln(-4,18,4,18,C.dark,3);
 else if(kind==='beard')s=person({shirt:C.navy})+p('M-22 22 C-18 50 18 50 22 22 C16 40 -16 40 -22 22 Z','#2a1d14');else if(kind==='bald')s=person(o).replace(/<path d="M-24 18 C-24 -4 -10 -8 0 -8 C10 -8 24 -4 24 18[^>]*>/,'');
 else if(kind==='strong')s=person({shirt:C.red}).replace('<path d="M-38 70 L-62 120 L-50 126 L-34 92 Z"','<path d="M-38 70 L-70 60 L-74 40 L-50 48 L-34 70 Z"').replace('<circle cx="-58" cy="128"','<circle cx="-72" cy="40"')+c(-72,36,10,C.skin);else if(kind==='thin')s='<g transform="scale(.8,1)">'+person(o)+'</g>';
 return s}
/* ── opposites ── */
function opp(kind){var s='';
 if(kind==='big')s=c(0,0,46,C.gold);if(kind==='small')s=c(0,0,14,C.gold);if(kind==='open')s=r(-30,-40,60,80,C.wood,3)+r(-30,-40,20,80,'rgba(0,0,0,.2)')+c(-6,0,4,C.gold)+r(-44,-40,14,80,'#2a2a2a');if(kind==='closed')s=r(-30,-40,60,80,C.wood,3)+c(18,0,4,C.gold);
 if(kind==='full')s=p('M-26 -36 L26 -36 L22 36 L-22 36 Z',C.sky,' stroke="'+C.gray2+'" stroke-width="3"')+p('M-25 -30 L25 -30 L22 36 L-22 36 Z',C.orange);if(kind==='empty')s=p('M-26 -36 L26 -36 L22 36 L-22 36 Z',C.sky,' stroke="'+C.gray2+'" stroke-width="3"');
 if(kind==='clean')s=L.shirt(C.paper)+c(20,-10,4,C.sky);if(kind==='dirty')s=L.shirt(C.paper)+c(-10,0,8,'#8B5A2B')+c(14,16,6,'#8B5A2B')+c(0,30,5,'#6E4520');
 if(kind==='fast')s=g(0,0,0.5,'<path d="M-80 10 L-80 -10 L-50 -14 L-30 -40 L34 -40 L60 -14 L80 -10 L80 10 Z" fill="'+C.red+'"/><circle cx="-46" cy="20" r="14" fill="'+C.dark+'"/><circle cx="46" cy="20" r="14" fill="'+C.dark+'"/>')+ln(-70,-10,-100,-10,C.gray2,4)+ln(-70,4,-110,4,C.gray2,4);if(kind==='slow')s=el(0,10,30,20,C.green)+c(30,0,12,C.green2)+c(34,-4,2,C.dark)+r(-16,26,8,10,C.green2)+r(8,26,8,10,C.green2);
 if(kind==='heavy')s=r(-36,-16,72,40,C.dark,6)+r(-14,-34,28,20,C.dark,4)+t(0,10,'50',C.paper,16);if(kind==='light')s=p('M0 -40 C30 -30 24 20 0 30 C-24 20 -30 -30 0 -40 Z',C.paper,' stroke="'+C.gray2+'" stroke-width="2"')+ln(0,-40,0,30,C.gray2,2);
 if(kind==='wet')s=p('M0 -40 C24 -4 24 14 0 30 C-24 14 -24 -4 0 -40 Z',C.blue)+c(-6,0,4,'rgba(255,255,255,.5)');if(kind==='dry')s=p('M-30 20 L30 20 L24 -20 L-24 -20 Z','#D9A066')+ln(-10,-10,-14,10,'#B07A45',2)+ln(8,-12,12,8,'#B07A45',2);
 if(kind==='hot')s=g(0,0,0.9,L.sun());if(kind==='cold')s=c(0,0,6,C.sky)+ln(0,-40,0,40,C.sky,4)+ln(-35,-20,35,20,C.sky,4)+ln(-35,20,35,-20,C.sky,4);
 if(kind==='new')s=r(-30,-20,60,40,C.teal,6)+t(0,6,'NEW',C.paper,14);if(kind==='old2')s=r(-30,-20,60,40,'#9a8f78',6)+ln(-20,-10,10,10,'#6E4520',2)+ln(0,-16,20,12,'#6E4520',2);
 if(kind==='loud')s=p('M-30 -14 L-10 -14 L14 -34 L14 34 L-10 14 L-30 14 Z',C.dark)+p('M24 -20 C40 -8 40 8 24 20',"none",' stroke="'+C.red+'" stroke-width="4"')+p('M34 -32 C58 -12 58 12 34 32',"none",' stroke="'+C.red+'" stroke-width="4"');if(kind==='quiet')s=p('M-30 -14 L-10 -14 L14 -34 L14 34 L-10 14 L-30 14 Z',C.dark)+ln(24,-10,44,10,C.red,4)+ln(44,-10,24,10,C.red,4);
 if(kind==='up')s=p('M0 -40 L30 -6 L12 -6 L12 40 L-12 40 L-12 -6 L-30 -6 Z',C.gold);if(kind==='same')s=poly('-30,20 -10,-20 10,20',C.teal)+poly('10,20 30,-20 50,20',C.teal);if(kind==='diff')s=poly('-30,20 -10,-20 10,20',C.teal)+c(34,0,20,C.red);if(kind==='down')s=p('M0 40 L30 6 L12 6 L12 -40 L-12 -40 L-12 6 L-30 6 Z',C.gold);
 return s}
/* ── animals ── */
function dog(){return el(0,10,40,22,'#B07A45')+c(34,-10,18,'#B07A45')+el(44,-6,8,5,C.dark)+c(30,-16,3,C.dark)+p('M20 -26 L14 -44 L30 -30 Z','#8B5A2B')+r(-26,28,8,18,'#8B5A2B')+r(14,28,8,18,'#8B5A2B')+p('M-40 6 C-60 -10 -60 -30 -46 -30',"none",' stroke="#8B5A2B" stroke-width="7" stroke-linecap="round"')}
function cat(){return el(0,10,36,20,C.gray2)+c(30,-8,16,C.gray2)+poly('18,-18 14,-36 28,-22',C.gray2)+poly('36,-20 44,-36 44,-18',C.gray2)+c(26,-10,2.5,C.green2)+c(36,-10,2.5,C.green2)+p('M-36 10 C-60 0 -60 -24 -40 -34',"none",' stroke="'+C.gray2+'" stroke-width="7" stroke-linecap="round"')+r(-22,26,8,16,C.gray2)+r(12,26,8,16,C.gray2)}
function bird(){return el(0,0,26,16,C.red)+c(22,-10,11,C.red)+poly('32,-10 44,-6 32,-2',C.gold)+c(25,-12,2,C.dark)+p('M-6 -6 C-20 -26 6 -26 4 -6 Z','#8E1A33')+r(-4,14,3,12,C.gold)+r(6,14,3,12,C.gold)}
function fish(){return el(0,0,40,22,C.orange)+poly('-40,0 -62,-18 -56,0 -62,18',C.orange)+c(22,-6,4,C.dark)+p('M-4 -22 L4 -36 L12 -22 Z',C.orange)}
function rabbit(){return el(0,14,32,22,C.paper,' stroke="'+C.gray+'" stroke-width="2"')+c(26,-8,16,C.paper,' stroke="'+C.gray+'" stroke-width="2"')+el(18,-38,6,18,C.paper,' stroke="'+C.gray+'" stroke-width="2"')+el(32,-38,6,18,C.paper,' stroke="'+C.gray+'" stroke-width="2"')+el(18,-38,3,12,C.pink)+el(32,-38,3,12,C.pink)+c(32,-10,2.5,C.dark)+c(-30,12,8,C.paper,' stroke="'+C.gray+'" stroke-width="2"')}
function horse(){return r(-50,-20,100,50,'#8B5A2B',14)+p('M40 -20 L60 -60 L80 -56 L74 -16 L50 0 Z','#8B5A2B')+p('M44 -40 L60 -62 L66 -30 Z','#2a1d14')+c(70,-50,3,C.dark)+r(-40,28,10,40,'#8B5A2B')+r(-14,28,10,40,'#8B5A2B')+r(14,28,10,40,'#8B5A2B')+r(36,28,10,40,'#8B5A2B')+p('M-50 -10 C-70 -4 -70 30 -56 40',"none",' stroke="#2a1d14" stroke-width="7" stroke-linecap="round"')}
function snake(){return p('M-60 20 C-40 -20 -20 -20 0 10 C20 40 40 40 60 0',"none",' stroke="'+C.green+'" stroke-width="12" stroke-linecap="round"')+c(62,-4,10,C.green)+c(66,-6,2.5,C.dark)+ln(72,-2,82,2,C.red,2)}
function turtle(){return el(0,0,44,26,C.green)+el(0,-4,30,16,'#3C8A58')+c(44,0,12,C.green2)+c(48,-3,2.5,C.dark)+r(-30,18,10,14,C.green2)+r(20,18,10,14,C.green2)}
function deer(){return r(-40,-10,80,44,'#B07A45',12)+p('M30 -10 L46 -50 L62 -46 L58 -8 L40 6 Z','#B07A45')+ln(50,-50,42,-80,'#6E4520',4)+ln(50,-50,62,-78,'#6E4520',4)+ln(46,-66,36,-70,'#6E4520',3)+ln(56,-64,66,-68,'#6E4520',3)+c(56,-44,3,C.dark)+r(-32,30,8,40,'#B07A45')+r(-10,30,8,40,'#B07A45')+r(14,30,8,40,'#B07A45')+r(30,30,8,40,'#B07A45')}
function alligator(){return el(0,10,60,18,'#3C8A58')+p('M50 6 L110 0 L110 14 L50 20 Z','#3C8A58')+c(56,-2,4,C.gold)+poly('-40,-6 -30,-18 -20,-6',C.green)+poly('-10,-6 0,-18 10,-6',C.green)+poly('20,-6 30,-18 40,-6',C.green)+r(-40,26,10,12,'#3C8A58')+r(20,26,10,12,'#3C8A58')+ln(60,12,100,12,C.paper,2)}
function mosquito(){return el(0,0,14,6,C.dark)+el(-10,-14,16,6,'rgba(200,200,220,.6)')+el(10,-14,16,6,'rgba(200,200,220,.6)')+ln(14,-2,40,-6,C.dark,2)+ln(-6,4,-16,16,C.dark,1.5)+ln(0,6,0,18,C.dark,1.5)+ln(6,4,16,16,C.dark,1.5)}
function squirrel(){return el(0,10,26,20,'#B07A45')+c(22,-10,13,'#B07A45')+poly('18,-22 16,-32 24,-24','#B07A45')+c(26,-12,2.5,C.dark)+p('M-24 0 C-50 -10 -56 -50 -30 -56 C-10 -60 -6 -30 -22 -20',"none",' stroke="#8B5A2B" stroke-width="12" stroke-linecap="round"')+r(-10,26,6,10,'#8B5A2B')+r(8,26,6,10,'#8B5A2B')}
/* ── safety ── */
function extinguisher(){return r(-16,-40,32,80,C.red,10)+r(-10,-50,20,12,C.dark,3)+p('M-10 -46 C-30 -46 -30 -10 -20 0',"none",' stroke="'+C.dark+'" stroke-width="4"')+r(-10,-20,20,30,C.paper,2)}
function firstaid(){return r(-40,-30,80,60,C.paper,6,' stroke="'+C.gray2+'" stroke-width="3"')+r(-8,-22,16,44,C.red)+r(-22,-8,44,16,C.red)+r(-14,-38,28,10,C.gray2,3)}
function smokedet(){return c(0,0,34,C.paper,' stroke="'+C.gray+'" stroke-width="3"')+c(0,0,22,C.gray,' stroke="'+C.gray2+'" stroke-width="2"')+c(18,-18,4,C.red)+c(0,0,6,C.dark)}
function caution(){return poly('0,-44 48,40 -48,40',C.gold,' stroke="'+C.dark+'" stroke-width="4" stroke-linejoin="round"')+t(0,30,'!',C.dark,34)}
function ambulance(){return r(-80,-30,160,60,C.paper,6,' stroke="'+C.gray2+'" stroke-width="3"')+r(-80,-30,60,60,C.red,6)+r(-74,-22,40,24,C.sky,2)+r(10,-16,20,6,C.red)+r(17,-23,6,20,C.red)+c(-50,36,14,C.dark)+c(50,36,14,C.dark)+r(-10,-42,30,12,C.blue,3)}
function policecar(){return p('M-80 10 L-80 -10 L-50 -14 L-30 -40 L34 -40 L60 -14 L80 -10 L80 10 Z',C.paper,' stroke="'+C.gray2+'" stroke-width="2"')+r(-80,-4,160,16,C.navy)+p('M-26 -36 L-4 -36 L-4 -14 L-44 -14 Z',C.sky)+p('M4 -36 L28 -36 L52 -14 L4 -14 Z',C.sky)+r(-14,-50,28,10,C.red,3)+r(-14,-50,14,10,C.blue,3)+c(-46,20,14,C.dark)+c(46,20,14,C.dark)+t(0,10,'POLICE',C.paper,10)}
function firetruck(){return r(-100,-40,200,70,C.red,6)+r(-90,-30,50,30,C.sky,2)+r(-20,-30,100,10,C.gray,2)+r(-30,-54,130,10,C.gray2,3)+c(-66,40,16,C.dark)+c(-6,40,16,C.dark)+c(66,40,16,C.dark)+r(-100,-52,30,10,C.gold,3)}
function phone911(){return r(-30,-50,60,100,C.dark,10)+r(-24,-42,48,84,C.sky,4)+t(0,8,'911',C.red,22)}
function flashlight(){return r(-40,-12,60,24,C.dark,6)+p('M20 -18 L40 -24 L40 24 L20 18 Z',C.gray2)+p('M40 -24 L90 -50 L90 50 L40 24 Z','rgba(246,226,122,.5)')+c(-20,0,4,C.red)}
function crossingguard(){return person({vest:true,shirt:C.navy})+g(70,60,0.8,'<rect x="-20" y="-30" width="40" height="30" rx="6" fill="'+C.red+'"/><text x="0" y="-10" text-anchor="middle" fill="#fff" font-family="Inter,sans-serif" font-size="10" font-weight="700">STOP</text><rect x="-3" y="0" width="6" height="40" fill="'+C.gray2+'"/>')}
function lifejacket(){return p('M-30 -30 L-12 -40 L12 -40 L30 -30 L30 40 L-30 40 Z',C.orange)+r(-8,-40,16,80,C.gold)+r(-30,0,60,8,C.dark)+r(-30,20,60,8,C.dark)}
function tornado(){return p('M-60 -60 L60 -60 L30 -20 L40 10 L10 30 L12 60 L-6 60 L-10 30 L-30 10 L-20 -20 Z','#8A8FA8')+p('M-60 -60 L60 -60 L50 -46 L-50 -46 Z','#6b7190')}
/* ── park ── */
function slide(){return p('M-60 60 L-60 -50 L-40 -50 L-40 -30 L60 50 L60 60 Z',C.gold)+r(-70,-60,40,14,C.red,4)+ln(-56,-46,-56,60,C.red,4)+ln(-44,-46,-44,-30,C.red,4)}
function swing(){return p('M-60 60 L-30 -60 L30 -60 L60 60',"none",' stroke="'+C.dark+'" stroke-width="6" stroke-linecap="round"')+ln(-30,-60,30,-60,C.dark,8)+ln(-14,-60,-14,30,C.gray2,3)+ln(14,-60,14,30,C.gray2,3)+r(-20,30,40,8,C.red,3)}
function picnic(){return r(-70,-6,140,10,C.wood,3)+r(-80,20,160,8,C.wood,3)+p('M-50 4 L-30 50 M50 4 L30 50 M-20 4 L-40 50 M20 4 L40 50',"none",' stroke="'+C.wood2+'" stroke-width="6" stroke-linecap="round"')}
function grill(){return c(0,0,36,C.dark)+el(0,-4,30,6,'#4a4a4a')+ln(-20,30,-30,70,C.dark,5)+ln(20,30,30,70,C.dark,5)+r(-20,-46,40,8,C.dark,3)+c(0,-12,4,C.orange)+c(-10,-6,3,C.red)+c(10,-6,3,C.red)}
function fountain(){return el(0,30,60,16,C.sky,' stroke="'+C.gray2+'" stroke-width="3"')+r(-6,-30,12,60,C.gray2)+p('M0 -30 C-30 -60 -30 -10 -12 -20',"none",' stroke="'+C.teal2+'" stroke-width="4"')+p('M0 -30 C30 -60 30 -10 12 -20',"none",' stroke="'+C.teal2+'" stroke-width="4"')+ln(0,-30,0,-56,C.teal2,4)}
function path(){return p('M0 420 C300 380 600 460 1000 400 L1000 440 C600 500 300 420 0 460 Z','#D9A066')}
function pond(){return el(0,0,120,40,'#5AA9E6')+el(-30,-6,40,10,'rgba(255,255,255,.3)')}
function duck(){return el(0,0,24,14,C.paper,' stroke="'+C.gray+'" stroke-width="2"')+c(18,-14,10,C.paper,' stroke="'+C.gray+'" stroke-width="2"')+poly('28,-14 40,-10 28,-8',C.orange)+c(21,-16,2,C.dark)}
function kite(){return poly('0,-50 30,-10 0,40 -30,-10',C.red)+ln(0,-50,0,40,C.dark,2)+ln(-30,-10,30,-10,C.dark,2)+p('M0 40 C10 60 -10 80 0 100',"none",' stroke="'+C.dark+'" stroke-width="2"')+poly('4,56 12,60 6,66',C.gold)+poly('-6,76 -14,80 -8,86',C.gold)}
function scooter(){return c(-40,30,12,C.dark)+c(40,30,12,C.dark)+r(-40,20,70,8,C.teal,3)+ln(30,24,50,-50,C.dark,6)+ln(36,-52,64,-52,C.dark,6)}
function sign2(txt){return r(-50,-18,100,36,C.green,6)+t(0,6,txt,C.paper,13)+r(-3,18,6,50,C.gray2)}
/* ── celebrations ── */
function cake(){return r(-50,0,100,40,C.pink,6)+r(-50,-6,100,14,C.paper,6)+r(-40,-36,80,34,'#E07A8F',6)+r(-40,-40,80,12,C.paper,6)+r(-14,-62,6,24,C.sky)+r(8,-62,6,24,C.gold2)+c(-11,-68,5,C.orange)+c(11,-68,5,C.orange)}
function candle(){return r(-8,-30,16,70,C.teal2,4)+r(-1,-40,2,10,C.dark)+p('M0 -62 C8 -50 8 -42 0 -38 C-8 -42 -8 -50 0 -62 Z',C.orange)}
function gift(){return r(-40,-20,80,60,C.red,6)+r(-44,-30,88,16,C.red,4)+r(-6,-30,12,70,C.gold)+r(-44,-26,88,6,C.gold)+p('M0 -30 C-20 -56 -36 -40 -6 -30 M0 -30 C20 -56 36 -40 6 -30',"none",' stroke="'+C.gold+'" stroke-width="5"')}
function balloon(){return el(-20,-20,22,28,C.red)+el(14,-30,22,28,C.teal2)+el(40,-6,20,26,C.gold)+ln(-20,8,-10,70,C.dark,2)+ln(14,-2,0,70,C.dark,2)+ln(40,20,10,70,C.dark,2)}
function cardf(){return p('M-36 -30 L0 -30 L0 40 L-36 40 Z',C.paper,' stroke="'+C.gray2+'" stroke-width="2"')+p('M0 -30 L36 -24 L36 46 L0 40 Z',C.pink,' stroke="'+C.gray2+'" stroke-width="2"')+c(18,8,8,C.red)}
function invitation(){return r(-44,-30,88,60,C.gold2,4,' stroke="'+C.gold+'" stroke-width="3"')+t(0,-6,'You are',C.navy,10)+t(0,10,'invited!',C.navy,12)}
function music(){return c(-20,20,12,C.dark)+r(-10,-40,5,60,C.dark)+c(20,10,12,C.dark)+r(30,-50,5,60,C.dark)+p('M-5 -40 L35 -50 L35 -36 L-5 -26 Z',C.dark)}
function dance(){return person({shirt:C.pink,skin:C.skin3}).replace('<path d="M38 70 L62 120 L50 126 L34 92 Z"','<path d="M38 70 L70 40 L78 50 L50 80 Z"').replace('<circle cx="58" cy="128"','<circle cx="76" cy="44"')+g(90,-20,0.4,music())}
function flag(){return r(-4,-70,8,140,C.gray2)+r(4,-70,100,60,C.red)+r(4,-70,100,8,C.paper)+r(4,-54,100,8,C.paper)+r(4,-38,100,8,C.paper)+r(4,-22,100,8,C.paper)+r(4,-70,44,32,C.navy)+c(14,-62,2,C.paper)+c(26,-62,2,C.paper)+c(38,-62,2,C.paper)+c(20,-50,2,C.paper)+c(32,-50,2,C.paper)}
function fireworks(){var s='';for(var i=0;i<8;i++){var a=i*Math.PI/4;s+=ln(0,0,Math.cos(a)*44,Math.sin(a)*44,C.gold,3)+c(Math.cos(a)*50,Math.sin(a)*50,4,C.red)}return s+c(0,0,6,C.paper)}
function costume(){return person({shirt:C.navy})+r(-24,10,48,18,C.red,4)+c(-10,18,5,C.paper)+c(10,18,5,C.paper)+p('M-30 100 L-60 170 L-30 160 Z',C.red)}
function parade(){return g(-60,0,0.6,person({shirt:C.red,hat:'cap',hatc:C.red}))+g(0,0,0.6,person({shirt:C.gold,hat:'cap',hatc:C.gold}))+g(60,0,0.6,person({shirt:C.teal,hat:'cap',hatc:C.teal}))+g(100,-40,0.5,flag())}
function pinata(){return el(0,0,40,30,C.pink)+el(-30,-10,16,10,C.teal2)+el(30,-10,16,10,C.gold)+r(-6,20,12,30,C.red)+ln(0,-30,0,-80,C.dark,2)+c(40,-24,5,C.gold)}
/* ── arts & music ── */
function guitar(){return el(0,20,34,40,C.wood)+el(0,-30,26,28,C.wood)+c(0,10,12,C.dark)+r(-6,-100,12,80,C.wood2)+r(-10,-110,20,16,C.dark,3)+ln(-2,-100,-2,50,C.paper,1)+ln(2,-100,2,50,C.paper,1)}
function drum(){return el(0,-30,50,16,C.paper,' stroke="'+C.gray2+'" stroke-width="3"')+r(-50,-30,100,60,C.red)+el(0,30,50,16,C.red)+ln(-50,-10,50,20,C.paper,3)+ln(50,-10,-50,20,C.paper,3)+ln(-40,-60,-10,-34,C.wood2,4)+ln(40,-60,10,-34,C.wood2,4)}
function piano(){var s=r(-80,-30,160,60,C.dark,4)+r(-72,-6,144,30,C.paper,2);for(var i=-72;i<72;i+=12)s+=ln(i,-6,i,24,C.gray,1);for(var i=-66;i<66;i+=12)if((i+66)/12%7!==2&&(i+66)/12%7!==6)s+=r(i-3,-6,6,18,C.dark);return s}
function paintbrush(){return r(-6,-50,12,70,C.wood,3)+r(-8,20,16,10,C.gray2)+p('M-8 30 L8 30 L4 54 L-4 54 Z',C.red)+r(-2,-56,4,8,C.dark)}
function paint(){return r(-40,-20,80,50,C.paper,8,' stroke="'+C.gray2+'" stroke-width="3"')+c(-22,-4,8,C.red)+c(0,-4,8,C.gold)+c(22,-4,8,C.blue)+c(-11,14,8,C.green)+c(11,14,8,C.orange)}
function canvas(){return r(-50,-40,100,80,C.paper,2,' stroke="'+C.wood+'" stroke-width="6"')+p('M-40 20 L-10 -14 L6 4 L18 -6 L40 20 Z',C.green)+c(22,-22,8,C.gold)+p('M-56 40 L-62 90 M56 40 L62 90 M-56 60 L56 60',"none",' stroke="'+C.wood2+'" stroke-width="4"')}
function mic(){return r(-16,-50,32,60,C.gray2,16)+r(-6,10,12,40,C.dark)+r(-30,50,60,8,C.dark,3)+ln(-16,-40,16,-40,C.dark,2)+ln(-16,-30,16,-30,C.dark,2)+ln(-16,-20,16,-20,C.dark,2)}
function choir(){return g(-70,10,0.5,person({shirt:C.navy,face:'open'}))+g(0,0,0.5,person({shirt:C.navy,face:'open',skin:C.skin3}))+g(70,10,0.5,person({shirt:C.navy,face:'open',skin:C.skin2}))}
function stage(){return r(-220,0,440,20,C.wood2,4)+r(-240,-180,20,200,C.red)+r(220,-180,20,200,C.red)+r(-240,-190,480,14,C.red,4)}
function camera2(){return r(-44,-24,88,54,C.dark,8)+c(0,4,18,C.gray2)+c(0,4,10,C.sky)+r(-16,-34,32,12,C.dark,3)+c(30,-12,4,C.red)}
function marker2(){return r(-30,-8,60,16,C.teal,6)+r(24,-8,12,16,C.dark,3)}
function clay(){return el(0,20,36,14,'#B07A45')+p('M-26 20 C-30 -20 30 -20 26 20 Z','#8B5A2B')+el(0,-6,14,6,'#6E4520')}
function trumpet(){return r(-60,-6,90,12,C.gold,4)+p('M30 -20 L70 -34 L70 34 L30 20 Z',C.gold)+r(-20,-20,6,14,C.gold)+r(-6,-20,6,14,C.gold)+r(8,-20,6,14,C.gold)}
/* ── scenes ── */
var S={};
S.lab=function(){return DEFS+room('#EEF7F6','#DDE5E4',380,true)+g(300,330,1,labtable())+g(700,330,1,labtable())+g(140,290,1,beaker())+g(230,286,1,testtube())+g(380,270,0.9,microscope())+g(520,300,1,goggles())+g(640,290,1,magnet())+g(780,280,0.9,scalebal())+g(900,290,1,dropper())+g(140,470,0.9,flame())+g(300,470,0.9,labnotebook())+g(500,130,1,periodic())+g(820,130,1,gloves2())+g(900,440,0.8,labcoat())}
S.shapes=function(){return DEFS+room('#F6F2EA','#EBD9A0',480)+g(120,140,1,shape('circle'))+g(290,140,1,shape('square'))+g(460,140,1,shape('triangle'))+g(640,140,1,shape('rectangle'))+g(830,140,1,shape('oval'))+g(120,290,1,shape('star'))+g(290,290,1,shape('cube'))+g(470,290,1,ruler())+g(660,290,1,anglef())+g(840,290,1,linef())+g(300,460,0.9,half())+g(700,450,1,measuring())}
S.colors=function(){var cols=[['#D8342A','red'],['#3B6FD1','blue'],['#F2C14E','yellow'],['#4C9A6A','green'],['#E07A3F','orange'],['#7C4DFF','purple'],['#F3A6B8','pink'],['#8B5A2B','brown'],['#1F2340','black'],['#FFFFFF','white'],['#8A8FA8','gray'],['#C9A227','gold']];var s=DEFS+r(0,0,1000,560,'#F4F5FA')+r(0,0,1000,560,'url(#pdlight)');cols.forEach(function(x,i){s+=g(110+(i%6)*156,(i<6?150:400),1,swatch(x[0]))});return s}
S.house=function(){return DEFS+'<defs><linearGradient id="pdsky5" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#BFD6FF"/><stop offset="1" stop-color="#EEF4FF"/></linearGradient></defs>'+r(0,0,1000,560,'url(#pdsky5)')+r(0,330,1000,230,C.green2)+g(860,70,0.7,L.sun())+g(420,230,1,house())+g(440,100,1,chimney())+g(700,290,1,garage())+g(160,340,1,fence())+g(860,370,0.9,mailbox2())+g(560,420,0.9,driveway())+g(260,470,0.9,lawnmower())+g(420,350,0.9,porch())+g(80,230,0.9,tree())+g(940,470,0.9,bush())+g(140,460,0.9,gate())+g(600,500,0.7,yard())}
S.routines=function(){var k=['wake','brush','shower','dress','breakfast','walk','study','lunch','work','cook','homework','sleep'];var s=DEFS+room('#FFF8E6','#D9C7A8',300);k.forEach(function(x,i){s+=g(100+(i%6)*160,(i<6?110:360),0.6,routine(x))});return s}
S.people=function(){var k=['tall','short','young','old','curly','straight','long','glasses','beard','bald','strong','thin'];var s=DEFS+room('#EEF1FB','#C9CEEA',300);k.forEach(function(x,i){s+=g(100+(i%6)*160,(i<6?110:360),0.6,descr(x))});return s}
S.opposites=function(){var k=['big','small','open','closed','full','empty','clean','dirty','fast','slow','heavy','light','wet','dry','hot','cold','new','old2','loud','quiet','up','down','same','diff'];var s=DEFS+r(0,0,1000,560,'#F2F4FF')+r(0,0,1000,560,'url(#pdlight)');for(var i=0;i<12;i++){var x=90+(i%6)*160,y=i<6?120:360;s+=r(x-70,y-70,140,150,'rgba(255,255,255,.7)',14)+g(x-30,y-10,0.55,opp(k[i*2]))+g(x+32,y-10,0.55,opp(k[i*2+1]))+ln(x,y-50,x,y+50,C.rule||'#DCDEE9',2)}return s}
S.animals=function(){return DEFS+r(0,0,1000,560,'#DDEBFF')+r(0,250,1000,310,C.green2)+p('M600 420 C700 380 900 380 1000 420 L1000 560 L600 560 Z','#5AA9E6')+g(130,180,1,dog())+g(330,180,1,cat())+g(520,150,1,bird())+g(760,170,0.9,horse())+g(130,340,1,rabbit())+g(330,340,0.9,turtle())+g(520,330,0.9,deer())+g(760,330,1,snake())+g(130,490,1,fish())+g(330,490,0.9,alligator())+g(560,490,1.2,mosquito())+g(820,490,1,squirrel())}
S.safety=function(){return DEFS+room('#FFF4F4','#E8DADA',380,true)+g(120,180,1,extinguisher())+g(280,170,1,firstaid())+g(440,160,1,smokedet())+g(600,170,1,caution())+g(780,180,1,phone911())+g(920,180,0.9,flashlight())+g(140,330,0.8,ambulance())+g(400,330,0.8,policecar())+g(680,330,0.8,firetruck())+g(900,330,0.8,tornado())+g(160,480,0.8,crossingguard())+g(500,480,0.9,lifejacket())}
S.park=function(){return DEFS+'<defs><linearGradient id="pdsky6" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#BFD6FF"/><stop offset="1" stop-color="#EEF4FF"/></linearGradient></defs>'+r(0,0,1000,560,'url(#pdsky6)')+r(0,260,1000,300,C.green2)+path()+g(140,250,1,slide())+g(330,260,1,swing())+g(560,310,1,picnic())+g(760,300,0.9,grill())+g(920,290,0.9,fountain())+g(220,500,1,pond())+g(220,490,1,duck())+g(640,120,0.9,kite())+g(880,480,0.9,scooter())+g(560,480,0.9,sign2('PARK'))+g(80,150,1,tree())+g(440,160,1,tree())}
S.celebrations=function(){return DEFS+room('#FFF8E6','#EBD9A0',380)+g(150,300,1,cake())+g(290,290,1,candle())+g(420,300,1,gift())+g(580,270,1,balloon())+g(740,300,1,cardf())+g(900,300,1,invitation())+g(120,470,1,music())+g(300,460,0.7,dance())+g(480,460,0.9,flag())+g(680,460,0.9,fireworks())+g(820,470,0.7,costume())+g(920,120,0.9,pinata())+g(400,120,0.7,parade())}
S.arts=function(){return DEFS+room('#F2EAF6','#C8B597',380)+g(500,380,1,stage())+g(130,260,0.9,guitar())+g(300,290,0.9,drum())+g(500,280,1,piano())+g(700,290,1,mic())+g(880,270,0.9,trumpet())+g(120,470,1,paintbrush())+g(280,470,1,paint())+g(440,460,0.9,canvas())+g(620,470,0.9,camera2())+g(760,470,1,marker2())+g(900,470,1,clay())+g(500,150,1,choir())}
Object.keys(S).forEach(function(k){var f=S[k];S[k]=function(){return f()+vignette()}});
window.PDScenes3=S;
})();
