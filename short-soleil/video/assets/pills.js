// Annotations de la vidéo « Si le Soleil disparaissait » : données déclaratives (temps en secondes).
// cls : y=jaune, b=bleu, g=vert, r=rouge, k=étiquette discrète. anc : ancre 3D (ou scr = position fixe). off : décalage en px.
window.CUTS = [27.0, 30.2, 45.1, 54.4, 60.1];
window.PUNCH = [3.4, 8.6, 12.0, 20.0, 27.4, 36.0, 40.0, 47.9, 52.0, 57.8, 62.0];
window.PILLS = [
  { id: "ici",   cls: "k", t0: 4.2,  t1: 9.0,  txt: "ICI : LE SOLEIL",          anc: { k: "sunC" },    off: [0, 90] },
  { id: "rien",  cls: "g", t0: 8.5,  t1: 12.2, txt: "RIEN NE CHANGE",           anc: { k: "scr", x: 520, y: 170 } },
  { id: "timer", cls: "y", t0: 8.6,  t1: 27.0, cnt: { from: 0, to: 500, clock: true, t0: 8.6, t1: 26.8 }, anc: { k: "scr", x: 520, y: 260 } },
  { id: "front", cls: "b", t0: 9.4,  t1: 17.0, txt: "DERNIÈRE LUMIÈRE",         anc: { k: "front" },   off: [0, -130] },
  { id: "grav",  cls: "b", t0: 17.4, t1: 26.9, txt: "GRAVITÉ ENCORE ACTIVE",    anc: { k: "earth" },   off: [0, -150] },
  { id: "noir",  cls: "r", t0: 27.2, t1: 30.0, txt: "LE NOIR",                  anc: { k: "scr", x: 520, y: 190 } },
  { id: "lune",  cls: "k", t0: 30.4, t1: 35.2, txt: "LUNE",                     anc: { k: "moon" },    off: [0, -110] },
  { id: "refl",  cls: "g", t0: 32.2, t1: 35.2, txt: "ELLE RÉFLÉCHIT LE SOLEIL", anc: { k: "scr", x: 520, y: 190 } },
  { id: "orb",   cls: "r", t0: 35.6, t1: 38.4, txt: "PLUS D'ORBITE",            anc: { k: "earth" },   off: [0, -150] },
  { id: "v30",   cls: "b", t0: 39.0, t1: 45.0, cnt: { from: 0, to: 30, t0: 39.1, t1: 40.9, suf: " km/s" }, anc: { k: "earth" }, off: [190, -140] },
  { id: "ans",   cls: "y", t0: 45.4, t1: 50.2, cnt: { from: 0, to: 40000, t0: 47.1, t1: 49.2, suf: " ANS" }, anc: { k: "scr", x: 520, y: 190 } },
  { id: "prox",  cls: "r", t0: 45.6, t1: 50.2, txt: "ÉTOILE LA PLUS PROCHE",    anc: { k: "proxM" },   off: [-150, 150] },
  { id: "photo", cls: "r", t0: 50.4, t1: 53.4, txt: "PLUS DE PHOTOSYNTHÈSE",    anc: { k: "scr", x: 520, y: 170 } },
  { id: "il8",   cls: "y", t0: 56.4, t1: 60.0, txt: "IL Y A 8 min",             anc: { k: "sunC" },    off: [0, -190] },
  { id: "tel",   cls: "g", t0: 57.4, t1: 60.0, txt: "TEL QU'IL ÉTAIT",          anc: { k: "scr", x: 520, y: 880 } }
];
