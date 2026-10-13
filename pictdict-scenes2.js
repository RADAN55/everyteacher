/* The Picture Dictionary, Issue 2 — scene art. Builds on the Issue 1 library. */
(function(){
'use strict';
var L=window.PDLib,C=L.C,g=L.g,r=L.r,c=L.c,p=L.p,ln=L.ln,t=L.t,room=L.room,DEFS=L.DEFS,vignette=L.vignette,person=L.person;
function el(cx,cy,rx,ry,f,extra){return '<ellipse cx="'+cx+'" cy="'+cy+'" rx="'+rx+'" ry="'+ry+'" fill="'+f+'"'+(extra||'')+'/>'}
/* ── food ── */
function apple(){return c(0,4,26,C.red)+p('M0 -20 C2 -30 8 -34 14 -34',"none",' stroke="'+C.brown+'" stroke-width="4" stroke-linecap="round"')+el(6,-12,10,6,C.green)+c(-9,-4,6,'rgba(255,255,255,.35)')}
function banana(){return p('M-34 -6 C-20 24 20 24 34 -6 C30 -2 20 10 0 12 C-20 10 -30 -2 -34 -6 Z',C.gold)+p('M-34 -6 C-20 24 20 24 34 -6 C28 4 10 16 0 16 C-10 16 -28 4 -34 -6 Z','rgba(0,0,0,.08)')+r(30,-12,6,8,C.brown,2)}
function orange(){return c(0,0,26,C.orange)+el(0,-22,8,5,C.green)+c(-8,-6,5,'rgba(255,255,255,.3)')}
function tomato(){return c(0,4,26,'#D8342A')+p('M-14 -16 L0 -8 L14 -16 L8 -22 L0 -14 L-8 -22 Z',C.green)+c(-9,-4,5,'rgba(255,255,255,.3)')}
function onion(){return el(0,6,24,26,'#E9C6A0')+p('M0 -20 L-4 -34 L0 -30 L4 -34 Z',C.brown)+p('M-14 -10 C-10 20 10 20 14 -10',"none",' stroke="#C9915F" stroke-width="2"')}
function rice(){return r(-28,-36,56,72,C.paper,5,' stroke="'+C.gray+'" stroke-width="3"')+r(-20,-28,40,30,C.teal,3)+t(0,-8,'RICE',C.paper,11)+c(-10,16,3,C.cream)+c(2,22,3,C.cream)+c(12,14,3,C.cream)}
function beans(){return r(-24,-30,48,60,C.red,6)+r(-24,-30,48,22,C.gold2,6)+t(0,-14,'BEANS',C.navy,9)+el(-6,8,5,8,C.brown)+el(8,12,5,8,C.brown)}
function bread(){return p('M-40 20 L40 20 L40 -4 C40 -24 -40 -24 -40 -4 Z','#D9A066')+p('M-30 -14 C-20 -24 20 -24 30 -14',"none",' stroke="#B07A45" stroke-width="3"')}
function eggs(){return r(-40,-14,80,30,'#D9D4C4',4)+el(-24,-8,10,13,C.paper)+el(0,-8,10,13,C.paper)+el(24,-8,10,13,C.paper)}
function milk(){return p('M-20 -30 L20 -30 L28 -16 L28 40 L-28 40 L-28 -16 Z',C.paper,' stroke="'+C.gray+'" stroke-width="3"')+r(-22,-4,44,20,C.blue)+t(0,10,'MILK',C.paper,11)}
function chickenmeat(){return p('M-30 10 C-36 -16 -6 -30 14 -16 C34 -2 30 24 8 26 C-10 28 -26 26 -30 10 Z','#E8B98F')+p('M14 -16 L34 -34 L40 -26 L28 -14 Z','#F4E3D2')}
function cheese(){return p('M-36 20 L36 20 L36 -6 L-36 -26 Z',C.gold)+c(-6,0,6,'#E6B93A')+c(14,8,5,'#E6B93A')+c(-20,8,4,'#E6B93A')}
/* ── living room ── */
function sofa(){return r(-110,-30,220,60,C.teal,10)+r(-120,-10,24,50,C.teal,8)+r(96,-10,24,50,C.teal,8)+r(-96,-30,96,34,'#2A7F8F',6)+r(0,-30,96,34,'#2A7F8F',6)+r(-100,40,10,14,C.dark)+r(90,40,10,14,C.dark)}
function tv(){return r(-80,-50,160,100,C.dark,6)+r(-72,-42,144,84,'#2C3E7A')+p('M-40 -20 L-40 20 L0 0 Z','rgba(255,255,255,.5)')+r(-20,50,40,8,C.dark,3)+r(-40,58,80,6,C.gray2,3)}
function remote(){return r(-10,-30,20,60,C.dark,6)+c(0,-20,4,C.red)+c(-4,-6,2.5,C.gray)+c(4,-6,2.5,C.gray)+c(-4,4,2.5,C.gray)+c(4,4,2.5,C.gray)}
function coffeetable(){return r(-80,-6,160,12,C.wood,4)+r(-70,6,8,34,C.wood2)+r(62,6,8,34,C.wood2)}
function bookshelf(){var s=r(-60,-100,120,200,C.wood,4)+r(-54,-94,108,188,C.cream,2);for(var y=-90;y<80;y+=48){s+=r(-54,y+40,108,6,C.wood2);for(var i=0;i<6;i++)s+=r(-50+i*17,y+4,13,36,[C.red,C.teal,C.gold,C.navy,C.green,C.orange][(i+y)%6],2)}return s}
function picture(){return r(-44,-34,88,68,C.gold,3)+r(-36,-26,72,52,C.sky)+p('M-36 26 L-10 -4 L6 14 L18 2 L36 26 Z',C.green)+c(18,-12,7,C.gold)}
function plant(){return p('M-20 20 L20 20 L16 50 L-16 50 Z',C.orange)+p('M0 20 C-10 0 -30 -10 -34 -30 C-10 -26 -2 -6 0 20 Z',C.green)+p('M0 20 C10 0 30 -10 34 -30 C10 -26 2 -6 0 20 Z',C.green)+p('M0 20 C-4 -4 -4 -24 0 -44 C4 -24 4 -4 0 20 Z','#3C8A58')}
function cushion(){return r(-26,-26,52,52,C.gold,12)+r(-18,-18,36,36,'rgba(255,255,255,.18)',8)}
function lightswitch(){return r(-16,-24,32,48,C.paper,4,' stroke="'+C.gray+'" stroke-width="3"')+r(-6,-14,12,28,C.gray,2)+r(-6,-14,12,12,C.gray2,2)}
function outlet(){return r(-16,-22,32,44,C.paper,4,' stroke="'+C.gray+'" stroke-width="3"')+r(-8,-14,4,10,C.dark)+r(4,-14,4,10,C.dark)+c(0,8,3,C.dark)}
function fan(){return c(0,-40,8,C.dark)+p('M0 -40 L-60 -52 L-60 -28 Z',C.wood)+p('M0 -40 L60 -52 L60 -28 Z',C.wood)+p('M0 -40 L-10 10 L10 10 Z',C.wood)+r(-3,-80,6,40,C.dark)}
function charger(){return r(-16,-10,32,20,C.paper,4,' stroke="'+C.gray2+'" stroke-width="3"')+r(-8,10,4,10,C.gray2)+r(4,10,4,10,C.gray2)+p('M16 0 C40 0 40 30 60 30',"none",' stroke="'+C.dark+'" stroke-width="4"')}
/* ── bathroom ── */
function toilet(){return r(-24,-60,48,50,C.paper,6,' stroke="'+C.gray+'" stroke-width="3"')+el(0,10,36,20,C.paper,' stroke="'+C.gray+'" stroke-width="3"')+r(-30,20,60,30,C.paper,6,' stroke="'+C.gray+'" stroke-width="3"')+c(14,-50,4,C.gray2)}
function shower(){return r(-4,-100,8,40,C.gray2)+p('M4 -100 C40 -100 40 -80 40 -70',"none",' stroke="'+C.gray2+'" stroke-width="8"')+el(40,-66,22,8,C.gray)+ln(26,-56,20,20,C.teal2,3)+ln(40,-56,40,24,C.teal2,3)+ln(54,-56,60,20,C.teal2,3)}
function bathtub(){return p('M-90 -20 L90 -20 L80 40 L-80 40 Z',C.paper,' stroke="'+C.gray+'" stroke-width="4"')+r(-80,-16,160,14,C.teal2)+r(-80,40,10,14,C.gray2)+r(70,40,10,14,C.gray2)+r(-70,-50,6,30,C.gray2)}
function towel(){return r(-30,-40,60,80,C.teal,4)+r(-30,-10,60,8,C.paper)+r(-30,10,60,8,C.paper)+r(-36,-46,72,8,C.gray2,3)}
function toothbrush(){return r(-6,-40,12,80,C.blue,6)+r(-8,-44,16,22,C.paper,4)+ln(-4,-40,-4,-28,C.gray,2)+ln(4,-40,4,-28,C.gray,2)}
function toothpaste(){return r(-40,-12,80,24,C.paper,12,' stroke="'+C.gray+'" stroke-width="3"')+r(-30,-6,40,12,C.teal,6)+r(38,-8,10,16,C.blue,3)}
function soap(){return r(-30,-16,60,32,C.pink,14)+r(-20,-8,24,8,'rgba(255,255,255,.5)',4)+c(26,-26,5,'rgba(255,255,255,.7)')+c(36,-16,3,'rgba(255,255,255,.7)')}
function shampoo(){return r(-18,-30,36,70,C.teal2,8)+r(-10,-44,20,16,C.teal,4)+r(-12,-6,24,26,C.paper,3)}
function tpaper(){return c(0,0,26,C.paper,' stroke="'+C.gray+'" stroke-width="3"')+c(0,0,8,C.cream,' stroke="'+C.gray+'" stroke-width="3"')+r(14,0,40,24,C.paper,' stroke="'+C.gray+'" stroke-width="3"')}
function comb(){var s=r(-40,-6,80,12,C.navy,3);for(var i=-34;i<36;i+=7)s+=r(i,6,3,16,C.navy);return s}
/* ── transportation ── */
function car(){return p('M-80 10 L-80 -10 L-50 -14 L-30 -40 L34 -40 L60 -14 L80 -10 L80 10 Z',C.red)+p('M-26 -36 L-4 -36 L-4 -14 L-44 -14 Z',C.sky)+p('M4 -36 L28 -36 L52 -14 L4 -14 Z',C.sky)+r(-80,10,160,10,C.dark,3)+c(-46,20,14,C.dark)+c(46,20,14,C.dark)+c(-46,20,6,C.gray)+c(46,20,6,C.gray)}
function truck(){return r(-100,-50,120,70,C.navy,4)+r(20,-30,70,50,C.teal,4)+r(30,-24,30,20,C.sky,2)+r(-100,20,190,10,C.dark,3)+c(-66,30,14,C.dark)+c(-10,30,14,C.dark)+c(60,30,14,C.dark)}
function bicycle(){return c(-40,20,26,'none',' stroke="'+C.dark+'" stroke-width="5"')+c(40,20,26,'none',' stroke="'+C.dark+'" stroke-width="5"')+p('M-40 20 L-10 -20 L30 -20 L40 20 L0 20 L-10 -20',"none",' stroke="'+C.red+'" stroke-width="5" stroke-linejoin="round"')+ln(-16,-26,-4,-26,C.dark,5)+ln(26,-30,40,-30,C.dark,5)}
function motorcycle(){return c(-44,20,24,'none',' stroke="'+C.dark+'" stroke-width="6"')+c(44,20,24,'none',' stroke="'+C.dark+'" stroke-width="6"')+p('M-44 20 L-20 -10 L20 -14 L44 20',"none",' stroke="'+C.dark+'" stroke-width="6"')+r(-26,-24,56,18,C.red,6)+ln(20,-14,40,-34,C.dark,5)}
function train(){return r(-110,-40,220,70,C.teal,8)+r(-100,-30,40,26,C.sky,3)+r(-50,-30,40,26,C.sky,3)+r(0,-30,40,26,C.sky,3)+r(50,-30,44,26,C.sky,3)+r(-110,30,220,8,C.dark)+c(-70,42,10,C.dark)+c(-20,42,10,C.dark)+c(30,42,10,C.dark)+c(80,42,10,C.dark)+r(-120,-20,12,40,C.gold,3)}
function airplane(){return p('M-80 0 L60 -14 L90 0 L60 14 Z',C.paper,' stroke="'+C.gray2+'" stroke-width="3"')+p('M0 -6 L-40 -50 L-10 -50 L30 -8 Z',C.gray)+p('M0 6 L-40 50 L-10 50 L30 8 Z',C.gray)+p('M-80 0 L-96 -26 L-78 -26 L-60 -4 Z',C.red)+c(40,-4,4,C.sky)+c(26,-4,4,C.sky)+c(12,-4,4,C.sky)}
function taxi(){return car().replace(/#B5213F/g,C.gold)+r(-14,-50,28,10,C.dark,2)+t(0,-42,'TAXI',C.paper,8)}
function boat(){return p('M-80 0 L80 0 L60 30 L-60 30 Z',C.navy)+r(-4,-70,6,70,C.dark)+p('M2 -66 L50 -10 L2 -10 Z',C.paper)+p('M-2 -60 L-40 -10 L-2 -10 Z',C.red)}
function helmet(){return p('M-34 10 C-34 -36 34 -36 34 10 Z',C.red)+r(-38,8,76,10,C.dark,3)+p('M-24 -14 C-16 -28 0 -30 8 -28',"none",' stroke="rgba(255,255,255,.5)" stroke-width="4" stroke-linecap="round"')}
function seatbelt(){return r(-40,-40,80,80,C.gray,8)+p('M-30 -36 L30 36',"none",' stroke="'+C.dark+'" stroke-width="10"')+r(14,14,24,18,C.gray2,3)+c(24,23,4,C.red)}
function ticket(){return r(-40,-20,80,40,C.gold2,4,' stroke="'+C.gold+'" stroke-width="3"')+ln(10,-20,10,20,C.gold,2)+t(-14,6,'TICKET',C.navy,10)+c(22,0,6,C.navy)}
/* ── money ── */
function dollar(){return r(-50,-24,100,48,'#8FBF9F',4)+r(-44,-18,88,36,'none',' stroke="#2E7D4F" stroke-width="2"')+c(0,0,12,'#CFE8D6')+t(0,5,'$1',C.navy,12)}
function coin(){return c(0,0,22,C.gold,' stroke="#A3831F" stroke-width="3"')+t(0,6,'25¢',C.navy,11)}
function wallet(){return r(-40,-26,80,52,C.wood2,6)+r(-40,-6,80,32,C.brown,6)+r(20,-2,20,14,C.gold,2)+r(-30,-20,50,10,'#8FBF9F',2)}
function card(){return r(-40,-26,80,52,C.navy,6)+r(-40,-10,80,10,C.dark)+r(-32,8,24,10,C.gold,2)+t(10,16,'DEBIT',C.paper,8)}
function atm(){return r(-50,-90,100,180,C.gray,8)+r(-40,-80,80,50,C.navy,3)+t(0,-50,'ATM',C.paper,14)+r(-30,-20,60,8,C.dark,2)+r(-30,0,60,24,C.gray2,2)+r(-30,40,60,8,C.dark,2)}
function check(){return r(-50,-24,100,48,C.paper,3,' stroke="'+C.gray2+'" stroke-width="2"')+ln(-40,-8,20,-8,C.gray2,2)+ln(-40,4,0,4,C.gray2,2)+ln(10,14,40,14,C.navy,2)+t(32,-6,'$',C.navy,12)}
function piggy(){return el(0,4,34,26,C.pink)+c(26,-6,14,C.pink)+c(34,-8,3,C.dark)+el(40,-4,6,4,'#E07A8F')+r(-22,22,8,14,C.pink)+r(14,22,8,14,C.pink)+r(-10,-24,20,5,C.dark,2)}
function paycheck(){return r(-50,-30,100,60,C.cream,3,' stroke="'+C.gray2+'" stroke-width="2"')+r(-50,-30,100,14,C.navy)+t(0,-19,'PAY',C.paper,9)+ln(-40,-4,20,-4,C.gray2,2)+ln(-40,8,0,8,C.gray2,2)+t(30,14,'$',C.ok,16)}
function ebill(){return r(-40,-50,80,100,C.paper,3,' stroke="'+C.gray2+'" stroke-width="2"')+r(-40,-50,80,16,C.gold)+t(0,-38,'ELECTRIC',C.navy,8)+ln(-30,-20,30,-20,C.gray2,2)+ln(-30,-6,30,-6,C.gray2,2)+ln(-30,8,10,8,C.gray2,2)+t(0,36,'DUE',C.red,12)}
function teller(){return r(-110,0,220,16,C.wood,3)+r(-100,16,200,70,C.wood2)+g(0,-150,0.7,person({shirt:C.navy,coat:false}))+r(-60,-80,120,60,'rgba(255,255,255,.15)',4)}
/* ── time ── */
function bigclock(){return c(0,0,70,C.paper,' stroke="'+C.navy+'" stroke-width="8"')+t(0,-42,'12',C.navy,14)+t(50,6,'3',C.navy,14)+t(0,56,'6',C.navy,14)+t(-50,6,'9',C.navy,14)+ln(0,0,0,-40,C.dark,6)+ln(0,0,28,16,C.dark,5)+c(0,0,5,C.red)}
function bigcal(){var s=r(-110,-90,220,180,C.paper,6,' stroke="'+C.gray2+'" stroke-width="3"')+r(-110,-90,220,34,C.red,6)+t(0,-66,'OCTOBER',C.paper,16);for(var i=0;i<28;i++){var x=-96+(i%7)*31,y=-40+Math.floor(i/7)*30;s+=r(x,y,26,24,i===13?C.gold:C.cream,3)+t(x+13,y+17,String(i+1),C.navy,10)}return s}
function moon(){return c(0,0,30,C.gold2)+c(12,-8,26,'#1A2250')}
function sunrise(){return r(-60,0,120,8,C.navy)+p('M-40 0 A40 40 0 0 1 40 0 Z',C.gold)+ln(-54,-20,-44,-14,C.gold,4)+ln(54,-20,44,-14,C.gold,4)+ln(0,-56,0,-46,C.gold,4)}
function week(){var d=['M','T','W','T','F','S','S'],s='';for(var i=0;i<7;i++)s+=r(-105+i*30,-14,26,28,i<5?C.teal:C.gold,4)+t(-92+i*30,6,d[i],C.paper,13);return s}
function hourglass(){return p('M-24 -40 L24 -40 L4 0 L24 40 L-24 40 L-4 0 Z',C.sky,' stroke="'+C.navy+'" stroke-width="4" stroke-linejoin="round"')+p('M-16 -34 L16 -34 L2 -6 L-2 -6 Z',C.gold)+p('M-20 36 L20 36 L6 20 L-6 20 Z',C.gold)}
/* ── sports ── */
function soccerball(){return c(0,0,24,C.paper,' stroke="'+C.dark+'" stroke-width="3"')+p('M0 -10 L10 -3 L6 9 L-6 9 L-10 -3 Z',C.dark)}
function basketball(){return c(0,0,24,C.orange)+ln(-24,0,24,0,C.dark,2)+ln(0,-24,0,24,C.dark,2)+p('M-17 -17 Q0 0 -17 17',"none",' stroke="'+C.dark+'" stroke-width="2"')+p('M17 -17 Q0 0 17 17',"none",' stroke="'+C.dark+'" stroke-width="2"')}
function football(){return el(0,0,34,20,C.brown)+ln(-12,0,12,0,C.paper,3)+ln(-8,-5,-8,5,C.paper,2)+ln(0,-5,0,5,C.paper,2)+ln(8,-5,8,5,C.paper,2)}
function baseball(){return c(0,0,22,C.paper,' stroke="'+C.gray+'" stroke-width="3"')+p('M-14 -17 Q-2 0 -14 17',"none",' stroke="'+C.red+'" stroke-width="3"')+p('M14 -17 Q2 0 14 17',"none",' stroke="'+C.red+'" stroke-width="3"')}
function volleyball(){return c(0,0,24,C.paper,' stroke="'+C.gray+'" stroke-width="3"')+p('M-20 -12 Q0 -4 20 -12',"none",' stroke="'+C.navy+'" stroke-width="3"')+p('M-20 12 Q0 4 20 12',"none",' stroke="'+C.gold+'" stroke-width="3"')}
function jumprope(){return p('M-40 20 C-60 -40 60 -40 40 20',"none",' stroke="'+C.red+'" stroke-width="5"')+r(-46,18,12,30,C.wood,4)+r(34,18,12,30,C.wood,4)}
function goal(){return r(-80,-50,160,100,'none',' stroke="'+C.paper+'" stroke-width="8"')+r(-76,-46,152,92,'url(#pdtile)')}
function whistle(){return r(-30,-10,40,22,C.gray2,8)+c(14,2,14,C.gray2)+c(14,2,4,C.dark)+p('M-30 -4 C-50 -24 -50 10 -30 4',"none",' stroke="'+C.dark+'" stroke-width="3"')}
function bottle(){return r(-14,-30,28,70,C.teal2,8)+r(-8,-44,16,16,C.navy,3)+r(-10,-6,20,28,C.paper,2)}
function sneakers(){return p('M-44 10 L-10 10 L10 -8 L30 8 L48 8 L48 22 L-44 22 Z',C.paper,' stroke="'+C.gray+'" stroke-width="3"')+p('M-10 10 L10 -8 L30 8 Z',C.teal)+r(-44,18,92,6,C.navy)}
function teamgroup(){return g(-60,0,0.55,person({shirt:C.gold}))+g(0,0,0.55,person({shirt:C.gold}))+g(60,0,0.55,person({shirt:C.gold,skin:C.skin3}))}
function track(){return p('M0 420 C0 300 1000 300 1000 420',"none",' stroke="#D9A066" stroke-width="40"')+p('M0 440 C0 340 1000 340 1000 440',"none",' stroke="#fff" stroke-width="3" stroke-dasharray="20 14"')}
/* ── tech ── */
function monitor(){return r(-70,-50,140,96,C.dark,6)+r(-62,-42,124,80,'#2C3E7A')+r(-50,-30,60,8,C.teal2,2)+r(-50,-14,90,6,C.gray,2)+r(-50,-2,70,6,C.gray,2)+r(-14,46,28,10,C.dark)+r(-40,56,80,6,C.gray2,3)}
function keyboard(){var s=r(-80,-20,160,40,C.gray,6);for(var y=-14;y<10;y+=10)for(var x=-74;x<70;x+=12)s+=r(x,y,9,7,C.paper,1);return s+r(-30,8,60,7,C.paper,1)}
function mouse(){return el(0,0,20,30,C.gray)+ln(0,-30,0,-6,C.gray2,2)+ln(-20,-6,20,-6,C.gray2,2)}
function printer(){return r(-60,-20,120,60,C.gray,6)+r(-40,-44,80,30,C.paper,2)+r(-50,-6,100,8,C.dark,2)+r(-30,40,60,20,C.paper,2)+c(40,10,5,C.green2)}
function headphones(){return p('M-40 10 C-40 -44 40 -44 40 10',"none",' stroke="'+C.dark+'" stroke-width="8"')+r(-50,0,20,36,C.navy,8)+r(30,0,20,36,C.navy,8)}
function wifi(){return p('M-44 -8 C-20 -34 20 -34 44 -8',"none",' stroke="'+C.navy+'" stroke-width="6" stroke-linecap="round"')+p('M-28 8 C-12 -8 12 -8 28 8',"none",' stroke="'+C.navy+'" stroke-width="6" stroke-linecap="round"')+c(0,26,7,C.navy)}
function password(){return r(-60,-20,120,40,C.paper,6,' stroke="'+C.navy+'" stroke-width="3"')+t(-6,8,'••••••',C.navy,22)+r(28,-12,24,24,C.gold,4)+c(40,-4,4,C.navy)+r(38,-4,4,10,C.navy)}
function emailic(){return r(-50,-32,100,64,C.paper,6,' stroke="'+C.navy+'" stroke-width="4"')+p('M-50 -32 L0 8 L50 -32',"none",' stroke="'+C.navy+'" stroke-width="4" stroke-linejoin="round"')+c(40,-26,10,C.red)+t(40,-21,'1',C.paper,12)}
function camera(){return r(-44,-24,88,54,C.dark,8)+c(0,4,18,C.gray2)+c(0,4,10,C.sky)+r(-16,-34,32,12,C.dark,3)+c(30,-12,4,C.red)}
function tablet(){return r(-40,-56,80,112,C.dark,10)+r(-34,-48,68,94,C.sky)+c(0,50,3,C.gray2)+r(-24,-38,48,8,C.teal2,2)+r(-24,-24,30,6,C.gray,2)}
/* ── restaurant ── */
function menu(){return r(-30,-44,60,88,C.red,4)+r(-24,-38,48,76,C.cream,2)+t(0,-20,'MENU',C.navy,12)+ln(-16,-6,16,-6,C.gray2,2)+ln(-16,6,16,6,C.gray2,2)+ln(-16,18,10,18,C.gray2,2)}
function fork(){return r(-3,-10,6,50,C.gray)+r(-10,-40,4,32,C.gray)+r(-2,-40,4,32,C.gray)+r(6,-40,4,32,C.gray)+r(-10,-14,20,6,C.gray,2)}
function napkin(){return p('M-30 -30 L30 -30 L30 30 L-30 30 Z',C.paper,' stroke="'+C.gray+'" stroke-width="2"')+p('M-30 -30 L30 30',"none",' stroke="'+C.gray+'" stroke-width="2"')}
function glass(){return p('M-18 -36 L18 -36 L14 30 L-14 30 Z',C.sky,' stroke="'+C.gray2+'" stroke-width="3"')+r(-14,-10,28,36,'rgba(23,162,184,.35)')}
function soup(){return el(0,-6,34,10,'#D9A066')+p('M-34 -6 L34 -6 C34 20 -34 20 -34 -6 Z',C.paper,' stroke="'+C.gray+'" stroke-width="3"')+el(0,-6,28,6,C.orange)+p('M-10 -20 C-6 -28 -14 -34 -10 -42',"none",' stroke="'+C.gray2+'" stroke-width="2"')+p('M8 -20 C12 -28 4 -34 8 -42',"none",' stroke="'+C.gray2+'" stroke-width="2"')}
function salad(){return p('M-36 -4 L36 -4 C30 24 -30 24 -36 -4 Z',C.paper,' stroke="'+C.gray+'" stroke-width="3"')+c(-14,-10,10,C.green)+c(10,-12,11,C.green2)+c(0,-2,8,C.red)+c(20,-2,6,C.orange)}
function dessert(){return p('M-30 10 L30 10 L22 36 L-22 36 Z',C.brown)+r(-30,0,60,12,C.pink,4)+c(0,-8,7,C.red)+r(-22,36,44,6,C.paper,2)}
function tipjar(){return r(-26,-20,52,50,C.sky,6,' stroke="'+C.gray2+'" stroke-width="3"')+r(-30,-28,60,10,C.dark,3)+t(0,8,'TIP',C.navy,13)+r(-10,-24,20,4,C.green)}
function waiter(){return person({shirt:C.paper,pants:C.dark,apron:true})+r(-70,40,10,6,C.gray)}
/* ── farm ── */
function tree(){return r(-10,0,20,70,C.wood2,3)+c(0,-24,44,C.green)+c(-26,-6,30,'#3C8A58')+c(26,-6,30,'#3C8A58')}
function pine(){return r(-8,30,16,40,C.wood2)+p('M0 -80 L-40 -10 L40 -10 Z','#2E7D4F')+p('M0 -40 L-50 30 L50 30 Z','#3C8A58')}
function river(){return p('M0 480 C200 440 300 540 500 500 C700 460 800 540 1000 500 L1000 560 L0 560 Z','#5AA9E6')+p('M0 500 C200 460 300 560 500 520 C700 480 800 560 1000 520',"none",' stroke="rgba(255,255,255,.4)" stroke-width="4"')}
function field(){var s=r(0,330,1000,150,'#D9A066');for(var y=350;y<470;y+=24)s+=ln(0,y,1000,y,'#B07A45',3);return s}
function cow(){return r(-50,-20,100,50,C.paper,16)+c(-30,-10,12,C.dark)+c(20,10,10,C.dark)+r(40,-36,34,30,C.paper,10)+c(66,-30,3,C.dark)+r(50,-14,20,10,C.pink,4)+r(-40,28,10,26,C.dark)+r(30,28,10,26,C.dark)+p('M46 -42 L50 -56 L56 -42',C.gray2)}
function hen(){return el(0,0,30,22,'#D9A066')+c(26,-16,14,'#D9A066')+p('M38 -14 L50 -10 L38 -6 Z',C.gold)+p('M22 -28 L28 -36 L32 -26 Z',C.red)+c(30,-18,2.5,C.dark)+r(-6,20,4,14,C.gold)+r(6,20,4,14,C.gold)+p('M-30 -4 L-50 -16 L-46 2 Z','#B07A45')}
function pig(){return el(0,0,44,30,C.pink)+c(36,-10,18,C.pink)+el(48,-8,8,6,'#E07A8F')+c(45,-9,2,C.dark)+c(51,-9,2,C.dark)+c(30,-20,3,C.dark)+r(-30,24,10,20,C.pink)+r(16,24,10,20,C.pink)+p('M28 -28 L34 -40 L40 -26 Z',C.pink)}
function barn(){return p('M-90 -20 L0 -90 L90 -20 Z',C.red)+r(-90,-20,180,110,C.red)+r(-30,20,60,70,C.wood2,3)+ln(-30,20,30,90,C.paper,4)+ln(30,20,-30,90,C.paper,4)+r(-14,-50,28,24,C.paper,3)}
function tractor(){return r(-60,-30,70,50,C.green)+r(-40,-70,40,40,C.green,4)+r(-32,-62,24,22,C.sky,2)+c(-50,30,24,C.dark)+c(-50,30,10,C.gray)+c(30,36,16,C.dark)+r(0,-10,60,24,C.green,3)+r(-10,-90,6,24,C.dark)}
function garden(){var s=r(-80,0,160,30,C.wood2,3);for(var i=0;i<5;i++)s+=p('M'+(-60+i*30)+' 0 C'+(-66+i*30)+' -20 '+(-54+i*30)+' -20 '+(-60+i*30)+' 0 Z',C.green)+c(-60+i*30,-24,5,[C.red,C.gold,C.red,C.orange,C.red][i]);return s}
function flower(){return r(-3,0,6,50,C.green)+p('M0 10 C-14 10 -14 24 0 20 Z',C.green)+c(0,-10,8,C.gold)+c(-12,-10,8,C.pink)+c(12,-10,8,C.pink)+c(0,-22,8,C.pink)+c(0,2,8,C.pink)+c(0,-10,5,C.orange)}
function catfish(){return el(0,0,44,20,'#6B7A8F')+p('M-44 0 L-66 -16 L-60 0 L-66 16 Z','#6B7A8F')+c(28,-6,4,C.dark)+ln(40,4,62,-4,C.dark,2)+ln(40,8,62,14,C.dark,2)+p('M-10 -20 L0 -36 L10 -20 Z','#6B7A8F')}
/* ── classroom actions (people) ── */
function act(kind){var o={shirt:[C.teal,C.red,C.gold,C.navy,C.green,C.orange][kind.length%6]};var s=person(o);
 if(kind==='read')s+=g(-10,120,0.6,L.books());if(kind==='write')s+=g(30,110,0.6,L.notebook())+g(60,96,0.5,L.pencil());if(kind==='listen')s+=g(0,10,0.6,headphones());
 if(kind==='speak')s+=p('M30 10 C60 -10 80 20 50 30 L40 46 L40 26 C30 24 24 16 30 10 Z',C.paper,' stroke="'+C.navy+'" stroke-width="3"');
 if(kind==='raise')s=s.replace('<path d="M38 70 L62 120 L50 126 L34 92 Z"','<path d="M38 70 L58 -10 L70 -6 L50 76 Z"').replace('<circle cx="58" cy="128"','<circle cx="64" cy="-10"');
 if(kind==='open')s+=g(40,120,0.6,L.books());if(kind==='close')s+=r(10,96,40,50,C.red,3);if(kind==='sit')s+=g(0,186,0.9,L.chair());if(kind==='stand')s+=ln(-60,196,60,196,C.gray2,4);
 if(kind==='line')s+=g(-90,0,0.7,person({shirt:C.gold}))+g(90,0,0.7,person({shirt:C.navy}));if(kind==='share')s+=g(70,0,0.8,person({shirt:C.green,skin:C.skin3}))+g(30,110,0.5,L.notebook());if(kind==='turn')s+=g(0,-40,0.6,L.desk())+g(0,-50,0.6,L.notebook());
 return s}
/* ── family ── */
function fam(kind){var o={teacher:{shirt:C.navy},mother:{shirt:C.red,hair:'#3a2418'},father:{shirt:C.navy},sister:{shirt:C.pink,skin:C.skin3},brother:{shirt:C.teal},grandmother:{shirt:C.purp||'#5B3FA8',hair:'#C9CEEA'},grandfather:{shirt:C.brown,hair:'#C9CEEA'},aunt:{shirt:C.gold,skin:C.skin3},uncle:{shirt:C.green},cousin:{shirt:C.orange},baby:{shirt:C.sky},husband:{shirt:C.teal},wife:{shirt:C.red}}[kind]||{};var s=person(o);
 if(kind==='grandfather')s+=p('M-14 32 C-6 44 6 44 14 32',"none",' stroke="#C9CEEA" stroke-width="5"')+r(-26,-6,52,8,C.gray2,3);if(kind==='grandmother')s+=r(-26,8,52,6,C.gray2,3)+c(-30,14,5,C.gold)+c(30,14,5,C.gold);
 if(kind==='baby')s='<g transform="scale(.55) translate(0,120)">'+person({shirt:C.sky,hair:'#C9915F'})+'</g>';if(kind==='husband'||kind==='wife')s+=c(60,128,4,C.gold);return s}
/* ── scenes ── */
var S={};
S.food=function(){return DEFS+room('#FFF8E6','#D9D4C4',300,true)+r(60,300,880,14,C.wood,4)+r(60,314,880,160,C.wood2,0)+r(60,314,880,160,'url(#pdfloor)')+g(140,250,1,apple())+g(270,250,1,banana())+g(400,250,1,orange())+g(530,250,1,tomato())+g(660,250,1,onion())+g(800,240,1,bread())+g(140,420,1,rice())+g(270,420,1,beans())+g(400,420,1,eggs())+g(530,420,1,milk())+g(670,420,1,chickenmeat())+g(810,420,1,cheese())}
S.living=function(){return DEFS+room('#F4EFE4','#C8B597')+g(300,170,1,tv())+g(300,290,1,coffeetable())+g(300,260,0.9,remote())+g(620,340,1,sofa())+g(560,320,0.8,cushion())+g(840,230,0.9,bookshelf())+g(620,120,1,picture())+g(940,420,1,plant())+g(90,250,1,lightswitch())+g(90,340,1,outlet())+g(130,110,1,fan())+g(480,460,1,charger())}
S.bathroom=function(){return DEFS+room('#E6F2F3','#CFE3E6',380,true)+g(130,330,1,toilet())+g(300,330,1,L.sink())+g(300,180,0.8,L.mirror())+g(560,180,1,shower())+g(620,400,1,bathtub())+g(860,180,1,towel())+g(420,240,0.8,toothbrush())+g(470,290,0.8,toothpaste())+g(860,330,1,soap())+g(940,420,1,shampoo())+g(130,470,0.9,tpaper())+g(860,470,1,comb())}
S.transport=function(){return DEFS+'<defs><linearGradient id="pdsky3" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#BFD6FF"/><stop offset="1" stop-color="#EAF2FF"/></linearGradient></defs>'+r(0,0,1000,560,'url(#pdsky3)')+r(0,330,1000,230,'#5a5f73')+ln(0,445,1000,445,C.gold,4)+g(150,290,1,car())+g(400,280,1,truck())+g(640,300,1,bicycle())+g(850,290,1,motorcycle())+g(300,480,0.8,L.bus())+g(700,480,0.8,train())+g(200,110,0.8,airplane())+g(560,160,0.8,taxi())+g(860,150,0.8,boat())+g(120,190,0.8,helmet())+g(960,400,0.8,seatbelt())+g(960,500,0.8,ticket())}
S.money=function(){return DEFS+room('#F2F4FF','#DCDEE9',380,true)+g(360,330,1,teller())+g(820,250,1,atm())+g(130,170,1,dollar())+g(130,260,1,coin())+g(130,460,1,wallet())+g(300,470,1,card())+g(560,470,1,check())+g(700,470,1,piggy())+g(860,470,1,paycheck())+g(560,160,1,ebill())+g(700,160,0.9,L.receipt())}
S.time=function(){return DEFS+r(0,0,1000,560,'#1A2250')+r(0,0,500,560,'#F2F4FF')+g(160,180,1,bigclock())+g(380,180,0.7,bigcal())+g(140,420,1,sunrise())+g(380,380,0.7,week())+g(640,120,1,L.sun())+g(850,120,1,moon())+g(640,300,1,hourglass())+g(850,300,0.8,L.calendar())+g(740,460,1,L.clock())+t(640,420,'TODAY',C.gold,18)+t(850,420,'TOMORROW',C.gold2,16)}
S.actions=function(){var k=['read','write','listen','speak','raise','open','close','sit','stand','line','share','turn'];var s=DEFS+room('#EEF1FB','#D9C7A8',300);k.forEach(function(x,i){s+=g(100+(i%6)*160,(i<6?110:360),0.62,act(x))});return s}
S.family=function(){var k=['mother','father','sister','brother','grandmother','grandfather','aunt','uncle','cousin','baby','husband','wife'];var s=DEFS+room('#FFF8E6','#C8B597',300);k.forEach(function(x,i){s+=g(100+(i%6)*160,(i<6?110:360),0.62,fam(x))});return s}
S.sports=function(){return DEFS+r(0,0,1000,560,'#CFE8D6')+track()+g(130,130,1,soccerball())+g(290,130,1,basketball())+g(450,130,1,football())+g(610,130,1,baseball())+g(770,130,1,volleyball())+g(930,130,0.9,jumprope())+g(150,300,0.9,goal())+g(360,320,1,whistle())+g(480,320,1,bottle())+g(620,320,1,sneakers())+g(830,300,1,teamgroup())+g(500,400,0.7,person({shirt:C.red,face:'open'}))}
S.tech=function(){return DEFS+room('#EEF1FB','#C9CEEA')+g(260,200,1,monitor())+g(260,300,1,keyboard())+g(400,300,1,mouse())+g(620,280,1,printer())+g(860,170,1,headphones())+g(860,300,1,wifi())+g(560,120,1,password())+g(380,110,1,emailic())+g(140,460,1,camera())+g(300,460,0.8,tablet())+g(560,460,1,charger())+g(820,460,0.8,L.laptop())}
S.restaurant=function(){return DEFS+room('#F6F2EA','#8B5A2B',380)+r(0,380,1000,180,'url(#pdplank)')+g(500,250,1.2,L.table())+r(320,222,360,34,C.red,4)+g(820,330,1,waiter())+g(140,200,1,menu())+g(300,225,0.9,L.plate())+g(380,215,0.9,fork())+g(460,225,0.9,napkin())+g(560,215,0.9,glass())+g(680,225,0.9,soup())+g(800,225,0.9,salad())+g(300,470,1,dessert())+g(500,470,1,tipjar())+g(700,470,0.9,L.receipt())+g(900,470,0.9,L.chair())}
S.farm=function(){return DEFS+'<defs><linearGradient id="pdsky4" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#BFD6FF"/><stop offset="1" stop-color="#EEF4FF"/></linearGradient></defs>'+r(0,0,1000,560,'url(#pdsky4)')+r(0,250,1000,310,'#7FD3A1')+field()+river()+g(880,60,0.7,L.sun())+g(150,200,1,tree())+g(300,200,1,pine())+g(520,180,1,barn())+g(760,220,1,tractor())+g(180,330,0.8,cow())+g(420,350,0.9,hen())+g(600,350,0.8,pig())+g(880,380,1,garden())+g(120,440,1,flower())+g(500,520,0.8,catfish())+g(900,480,0.6,cow().replace(/#FFFFFF/g,'#D9A066'))}
Object.keys(S).forEach(function(k){var f=S[k];S[k]=function(){return f()+vignette()}});
window.PDScenes2=S;
})();
