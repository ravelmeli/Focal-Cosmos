// Annotations de la vidéo « Si le Soleil était une balle de basket » : données déclaratives (temps en secondes).
// cls : y=jaune, b=bleu, g=vert, r=rouge, k=étiquette discrète. anc : ancre 3D (ou scr = position fixe). off : décalage en px.
window.CUTS = [4.1, 9.4, 19.0, 46.4, 60.4];
window.PUNCH = [6.0, 10.9, 14.3, 23.3, 27.4, 33.0, 40.3, 49.5, 56.4, 63.8, 67.6];
window.PILLS = [
  { id: "m26",   cls: "y", t0: 5.8,  t1: 9.3,  cnt: { from: 0, to: 26, t0: 5.9, t1: 7.2, suf: " m" }, anc: { k: "earthPin" }, off: [0, -130] },
  { id: "cou",   cls: "g", t0: 7.3,  t1: 9.3,  txt: "UN GRAND COULOIR",         anc: { k: "scr", x: 520, y: 170 } },
  { id: "tete",  cls: "y", t0: 10.1, t1: 13.2, txt: "TÊTE D'ÉPINGLE · 2 mm",    anc: { k: "pinhead" },  off: [230, -170] },
  { id: "lune",  cls: "g", t0: 14.0, t1: 19.0, txt: "LUNE · 0,6 mm",            anc: { k: "moon" },     off: [0, -150] },
  { id: "d6",    cls: "b", t0: 16.4, t1: 19.0, txt: "6 cm",                     anc: { k: "midEM" },    off: [0, 130] },
  { id: "mer",   cls: "k", t0: 19.0, t1: 22.6, txt: "MERCURE · 10 m",           anc: { k: "mer" },      off: [-10, 100] },
  { id: "mar",   cls: "k", t0: 20.9, t1: 24.8, txt: "MARS · 40 m",              anc: { k: "mar" },      off: [10, -110] },
  { id: "jup",   cls: "y", t0: 23.2, t1: 32.4, txt: "JUPITER · 134 m",          anc: { k: "jup" },      off: [-30, 150] },
  { id: "bille", cls: "g", t0: 27.2, t1: 30.0, txt: "BILLE DE 2,5 cm",          anc: { k: "jup" },      off: [-30, -150] },
  { id: "sat",   cls: "k", t0: 30.2, t1: 35.0, txt: "SATURNE · 250 m",          anc: { k: "sat" },      off: [20, -120] },
  { id: "nep",   cls: "b", t0: 32.7, t1: 36.4, txt: "NEPTUNE · 800 m",          anc: { k: "nep" },      off: [0, 150] },
  { id: "nepk",  cls: "k", t0: 36.6, t1: 40.0, txt: "NEPTUNE",                  anc: { k: "nep" },      off: [0, 90] },
  { id: "voy",   cls: "y", t0: 40.2, t1: 46.3, cnt: { from: 0, to: 4.5, dec: 1, t0: 40.3, t1: 42.4, suf: " km" }, anc: { k: "voyD" }, off: [0, -150] },
  { id: "a49",   cls: "g", t0: 43.1, t1: 46.3, txt: "49 ANS DE VOYAGE",         anc: { k: "scr", x: 520, y: 880 } },
  { id: "oort",  cls: "g", t0: 46.6, t1: 53.5, txt: "NUAGE DE OORT",            anc: { k: "oortE" },    off: [0, -150] },
  { id: "o50",   cls: "b", t0: 49.3, t1: 53.5, cnt: { from: 0, to: 50, t0: 49.4, t1: 50.6, pre: "DÈS ", suf: " km" }, anc: { k: "scr", x: 520, y: 170 } },
  { id: "o1000", cls: "r", t0: 51.4, t1: 53.5, txt: "JUSQU'À 1 000 km",         anc: { k: "scr", x: 520, y: 260 } },
  { id: "prox",  cls: "r", t0: 54.8, t1: 60.3, cnt: { from: 0, to: 6900, t0: 56.2, t1: 57.6, pre: "PROXIMA · ", suf: " km" }, anc: { k: "proxS" }, off: [0, -150] },
  { id: "desert", cls: "y", t0: 63.7, t1: 66.8, txt: "UN DÉSERT",               anc: { k: "scr", x: 520, y: 190 } }
];
