// Annotations de la vidéo « Voyager 1 » : données déclaratives (temps en secondes).
// cls : y=jaune, b=bleu, g=vert, r=rouge, k=étiquette discrète. anc : ancre 3D (ou scr = position fixe dans le cadre). off : décalage en px.
window.CUTS = [9.0, 22.4, 30.3, 40.9, 56.4, 64.4];
window.PUNCH = [12.6, 18.8, 24.0, 28.0, 33.0, 36.0, 42.5, 44.8, 46.4, 49.6, 50.3, 52.8, 54.4, 57.2, 59.2, 60.6, 61.8];
window.PILLS = [
  // accroche
  { id: "lance", cls: "g", t0: 2.3,  t1: 4.6,  txt: "LANCÉE EN 1977",           anc: { k: "voy" },   off: [-200, 160] },
  { id: "date",  cls: "y", t0: 4.9,  t1: 8.9,  txt: "18 NOV. 2026",             anc: { k: "voy" },   off: [210, -170] },
  // règle de lumière (monde 1)
  { id: "ksun",  cls: "k", t0: 9.2,  t1: 22.2, txt: "SOLEIL",                   anc: { k: "sunR" },  off: [0, 70] },
  { id: "kter",  cls: "k", t0: 9.2,  t1: 22.2, txt: "TERRE",                    anc: { k: "earthR" }, off: [0, 70] },
  { id: "kvoy",  cls: "k", t0: 9.2,  t1: 22.2, txt: "VOYAGER 1",                anc: { k: "voyR" },  off: [0, 90] },
  { id: "c24",   cls: "b", t0: 9.6,  t1: 15.4, cnt: { from: 0, to: 24, t0: 9.6, t1: 14.2, suf: " h" }, anc: { k: "photon" }, off: [0, -140] },
  { id: "km",    cls: "y", t0: 12.4, t1: 15.7, cnt: { from: 0, to: 25.9, dec: 1, t0: 12.4, t1: 14.6, suf: " MILLIARDS DE KM" }, anc: { k: "scr", x: 520, y: 850 } },
  { id: "m8",    cls: "g", t0: 16.6, t1: 18.7, txt: "8 min",                    anc: { k: "earthR" }, off: [0, -130] },
  { id: "h24",   cls: "b", t0: 19.4, t1: 22.0, txt: "24 h",                     anc: { k: "photon" }, off: [0, -140] },
  // vitesse (monde 0)
  { id: "v17",   cls: "b", t0: 22.6, t1: 25.9, cnt: { from: 0, to: 17, t0: 22.7, t1: 24.6, suf: " km/s" }, anc: { k: "voy" }, off: [190, -170] },
  { id: "v61",   cls: "b", t0: 26.0, t1: 30.2, cnt: { from: 0, to: 61000, t0: 26.0, t1: 27.6, suf: " km/h" }, anc: { k: "voy" }, off: [-200, 190] },
  // 49 ans, règle de lumière
  { id: "an",    cls: "y", t0: 30.5, t1: 34.4, cnt: { from: 1977, to: 2026, raw: true, t0: 30.6, t1: 33.4, suf: "" }, anc: { k: "scr", x: 520, y: 160 } },
  { id: "a49",   cls: "g", t0: 31.6, t1: 34.4, txt: "49 ANS = 1 JOUR-LUMIÈRE",  anc: { k: "scr", x: 520, y: 250 } },
  { id: "kvoy3", cls: "k", t0: 30.6, t1: 34.8, txt: "VOYAGER 1",                anc: { k: "voyR" },  off: [0, -120] },
  { id: "ksun2", cls: "k", t0: 34.9, t1: 40.7, txt: "TERRE",                    anc: { k: "earthR" }, off: [0, 70] },
  { id: "kvoy2", cls: "k", t0: 34.9, t1: 40.7, txt: "VOYAGER 1",                anc: { k: "voyR" },  off: [0, 90] },
  { id: "j1",    cls: "y", t0: 35.1, t1: 37.4, txt: "J + 1",                    anc: { k: "msg" },    off: [0, -140] },
  { id: "j2",    cls: "r", t0: 37.7, t1: 40.6, txt: "J + 2",                    anc: { k: "msg" },    off: [0, -140] },
  // Proxima (monde 2)
  { id: "jl",    cls: "y", t0: 41.1, t1: 44.4, txt: "1 JOUR-LUMIÈRE",           anc: { k: "vtick" },  off: [0, -150] },
  { id: "prox",  cls: "r", t0: 44.6, t1: 48.3, txt: "PROXIMA · 4,24 AL",        anc: { k: "prox" },   off: [0, -150] },
  { id: "x1500", cls: "b", t0: 46.5, t1: 48.3, txt: "× 1 500 PLUS LOIN",        anc: { k: "scr", x: 520, y: 880 } },
  { id: "y75",   cls: "r", t0: 48.6, t1: 56.3, cnt: { from: 0, to: 75000, t0: 48.8, t1: 52.2, suf: " ANS" }, anc: { k: "voyP" }, off: [0, -150] },
  // Oort (monde 3)
  { id: "ov",    cls: "y", t0: 56.9, t1: 61.2, txt: "VOYAGER 1",                anc: { k: "oortV" },  off: [-190, 150] },
  { id: "oort",  cls: "g", t0: 58.4, t1: 61.4, txt: "NUAGE DE OORT",            anc: { k: "oortS" },  off: [0, -170] },
  { id: "y300",  cls: "b", t0: 61.5, t1: 64.2, cnt: { from: 0, to: 300, t0: 61.6, t1: 62.9, suf: " ANS" }, anc: { k: "oortV" }, off: [190, 150] }
];
