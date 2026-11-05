// Annotations de la vidéo « Tu es immobile ? » : données déclaratives (temps en secondes).
// cls : y=jaune, b=bleu, g=vert, r=rouge. anc : ancre 3D (ou scr = position fixe dans le cadre). off : décalage en px.
window.CUTS = [8.2, 16.9, 25.4, 34.5, 42.0, 60.1];
window.PUNCH = [12.1, 21.0, 28.4, 38.0, 47.4, 60.4];
window.PILLS = [
  { id: "v0",    cls: "y", t0: 2.0,  t1: 4.3,  txt: "0 km/h ?",                 anc: { k: "astro" },  off: [270, 90] },
  { id: "quoi",  cls: "r", t0: 6.1,  t1: 8.3,  txt: "PAR RAPPORT À QUOI ?",     anc: { k: "scr", x: 520, y: 150 } },
  { id: "toi",   cls: "g", t0: 8.5,  t1: 11.8, txt: "TOI",                      anc: { k: "pin" },    off: [-150, -130] },
  { id: "v1",    cls: "b", t0: 12.0, t1: 16.8, cnt: { from: 0, to: 1670, t0: 12.0, t1: 14.3, suf: " km/h" }, anc: { k: "pin" }, off: [190, 120] },
  { id: "v2",    cls: "b", t0: 20.3, t1: 25.2, cnt: { from: 0, to: 107000, t0: 20.4, t1: 22.4, suf: " km/h" }, anc: { k: "earthS" }, off: [0, -190] },
  { id: "v2b",   cls: "y", t0: 23.2, t1: 25.2, txt: "30 km / s",                anc: { k: "earthS" }, off: [0, 190] },
  { id: "v3",    cls: "b", t0: 28.9, t1: 34.3, cnt: { from: 0, to: 800000, t0: 29.0, t1: 31.2, suf: " km/h" }, anc: { k: "sunM" }, off: [-170, -170] },
  { id: "tour",  cls: "y", t0: 31.5, t1: 34.3, txt: "1 TOUR = 200 M D'ANNÉES",  anc: { k: "sunM" },   off: [-110, 200] },
  { id: "v4",    cls: "b", t0: 39.8, t1: 42.0, cnt: { from: 0, to: 2000000, t0: 39.8, t1: 41.3, suf: " km/h" }, anc: { k: "gal" }, off: [0, -210] },
  { id: "cmb",   cls: "g", t0: 37.2, t1: 41.9, txt: "PLUS ANCIENNE LUMIÈRE",    anc: { k: "scr", x: 520, y: 900 } },
  { id: "a1",    cls: "g", t0: 42.4, t1: 50.2, txt: "ROTATION · 1 670",         anc: { k: "arr1" },   off: [-80, -90] },
  { id: "a2",    cls: "b", t0: 42.9, t1: 50.2, txt: "ORBITE · 107 000",         anc: { k: "arr2" },   off: [90, 90] },
  { id: "a3",    cls: "y", t0: 43.4, t1: 50.2, txt: "GALAXIE · 800 000",        anc: { k: "arr3" },   off: [0, -100] },
  { id: "add",   cls: "r", t0: 43.9, t1: 46.4, txt: "ELLES NE S'ADDITIONNENT PAS", anc: { k: "scr", x: 520, y: 130 } },
  { id: "rr",    cls: "r", t0: 47.2, t1: 50.2, cnt: { from: 0, to: 1000000, t0: 47.3, t1: 49.3, pre: "+ ", suf: " km/h" }, anc: { k: "arrR" }, off: [0, 120] },
  { id: "feel1", cls: "y", t0: 51.0, t1: 53.4, txt: "ON NE SENT JAMAIS LA VITESSE", anc: { k: "scr", x: 520, y: 190 } },
  { id: "feel2", cls: "b", t0: 53.5, t1: 55.5, txt: "SEULEMENT LES ACCÉLÉRATIONS",  anc: { k: "scr", x: 520, y: 280 } },
  { id: "abs",   cls: "r", t0: 55.6, t1: 57.7, txt: "AUCUN REPÈRE ABSOLU",      anc: { k: "scr", x: 520, y: 190 } },
  { id: "rel",   cls: "y", t0: 57.9, t1: 60.0, txt: "IMMOBILE = RELATIF",       anc: { k: "scr", x: 520, y: 190 } }
];
