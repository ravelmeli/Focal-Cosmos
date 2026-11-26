import json
W, H = 1080, 1920
EAR = {"kind": "earth", "seed": 2}
def sh(a, b, els, cam=None, **kw):
    d = {"start": a, "end": b, "els": els}
    if cam: d["cam"] = cam
    d.update(kw); return d
def r(a, t): return round(t - a, 2)
S = []
# 1 hook 0-5.1
a, b = 0, 5.1
S.append(sh(a, b, [
  {"type": "sun", "x": 60, "y": 1700, "r": 40},
  {"type": "planet", **EAR, "x": 640, "y": 1180, "r": 520, "light": 2.6, "spin": .03},
  {"type": "astronaut", "x": 330, "y": 860, "s": 70, "vx": 8, "rot": .35},
  {"type": "you", "x": 352, "y": 830, "lx": 200, "ly": 600, "text": "TOI", "t0": .34},
  {"type": "title", "text": "L'ESPACE", "sub": "SANS COMBINAISON", "tx": 80, "ty": 330, "t0": .3, "dur": 0.85},
  {"type": "label", "text": "ton corps explose ?", "size": 62, "x": .5, "y": .15, "t0": r(a, 1.1), "dur": 1.9},
  {"type": "label", "text": "il gèle en une seconde ?", "size": 62, "x": .5, "y": .15, "t0": r(a, 3.1), "dur": 1.9}],
  {"zoomFrom": 1, "zoomTo": 1.1, "fx": .62}))
# 2 faux + question 5.1-9.6
a, b = 5.1, 9.6
S.append(sh(a, b, [
  {"type": "planet", **EAR, "x": 540, "y": 1650, "r": 900, "light": -1.6, "spin": .02},
  {"type": "astronaut", "x": 540, "y": 720, "s": 150, "spin": .9, "vy": 30},
  {"type": "stamp", "text": "FAUX", "x": .5, "y": .3, "rot": -.1, "size": 190, "t0": 0, "dur": 1.0},
  {"type": "label", "text": "combien de temps tiendrais-tu", "size": 52, "x": .5, "y": .17, "t0": r(a, 6.14)},
  {"type": "big", "text": "SANS COMBINAISON ?", "size": 100, "x": .5, "y": .25, "tone": "yellow", "t0": r(a, 7.98)}],
  {"zoomFrom": 1.0, "zoomTo": 1.12, "fy": .4}))
# 3 pressure 9.6-22.2
a, b = 9.6, 22.2
S.append(sh(a, b, [
  {"type": "planet", **EAR, "x": 540, "y": 2050, "r": 900, "light": -1.6, "spin": .01},
  {"type": "astronaut", "x": 540, "y": 900, "s": 230, "spin": .35, "rot": .4},
  {"type": "label", "text": "éjecté d'un sas", "size": 60, "x": .5, "y": .15, "t0": .1, "dur": 1.8},
  {"type": "chapter", "n": "DANGER 1", "text": "LA PRESSION", "dur": .9, "t0": r(a, 11.5)},
  {"type": "counter", "label": "PRESSION AUTOUR DE TOI", "from": 1, "to": 0, "decimals": 2, "unit": "atm", "x": .06, "y": .12, "t0": r(a, 13.8), "t1": 2.0},
  {"type": "label", "text": "l'eau veut se vaporiser", "size": 50, "x": .5, "y": .3, "tone": "yellow", "t0": r(a, 14.66), "dur": 3.0},
  {"type": "stamp", "text": "LA PEAU TIENT", "tone": "green", "x": .5, "y": .62, "rot": -.07, "size": 90, "t0": r(a, 19.14), "dur": 3.0},
  {"type": "big", "text": "TU GONFLES", "size": 130, "x": .5, "y": .76, "tone": "yellow", "t0": r(a, 20.9), "sub": "TU N'EXPLOSES PAS"}],
  {"zoomFrom": 1.0, "zoomTo": 1.08}))
# 4 cold 22.2-28.9
a, b = 22.2, 28.9
S.append(sh(a, b, [
  {"type": "planet", **EAR, "x": 540, "y": 2100, "r": 900, "light": -1.6, "spin": .01},
  {"type": "astronaut", "x": 540, "y": 800, "s": 230, "spin": -.3, "rot": -.3},
  {"type": "chapter", "n": "DANGER 2", "text": "LE FROID", "dur": .9, "t0": 0},
  {"type": "label", "text": "la chaleur s'évacue lentement", "size": 44, "x": .5, "y": .17, "t0": r(a, 24.72), "dur": 3.5},
  {"type": "loading", "text": "REFROIDISSEMENT…", "to": .12, "t1": 3.5, "tone": "red", "x": .5, "y": .6, "t0": r(a, 24.9), "dur": 3.8},
  {"type": "stamp", "text": "PAS D'UN COUP", "tone": "green", "x": .5, "y": .72, "rot": .06, "size": 90, "t0": r(a, 27.14)}],
  {"zoomFrom": 1.0, "zoomTo": 1.07}))
# 5 oxygen 28.9-37.7
a, b = 28.9, 37.7
S.append(sh(a, b, [
  {"type": "astronaut", "x": 540, "y": 1350, "s": 230, "spin": .3, "rot": .4},
  {"type": "chapter", "n": "DANGER 3", "text": "L'OXYGÈNE", "dur": .9, "t0": 0},
  {"type": "label", "text": "le vrai tueur", "size": 70, "x": .5, "y": .12, "tone": "red", "underline": True, "t0": r(a, 31.48), "dur": 3.0},
  {"type": "xray", "part": "brain", "label": "CERVEAU", "title": "PLUS D'AIR", "x": .5, "y": .5, "s": 220, "t0": r(a, 33.28)},
  {"type": "gauge", "label": "TEMPS AVANT PERTE DE CONSCIENCE", "to": 15, "max": 15, "unit": " s", "x": .5, "y": .8, "r": 190, "t0": r(a, 35.0), "t1": 1.8}],
  {"zoomFrom": 1.0, "zoomTo": 1.05}))
# 6 technician 37.7-48.4
a, b = 37.7, 48.4
S.append(sh(a, b, [
  {"type": "planet", **EAR, "x": 540, "y": 2000, "r": 900, "light": -1.6, "spin": .01},
  {"type": "label", "text": "un technicien de la NASA", "size": 56, "x": .5, "y": .15, "t0": .1, "dur": 3.0},
  {"type": "evidence", "src": "media/jsc2022e045246.jpg", "credit": "NASA/JSC · Radislav Sinyak", "tag": "CHAMBRE À VIDE NASA · IMAGE D'ILLUSTRATION", "x": .5, "y": .4, "w": 940, "h": 640, "t0": r(a, 38.4), "dur": 6.2, "zoom": .1},
  {"type": "counter", "label": "RESTÉ CONSCIENT", "from": 0, "to": 14, "unit": "s", "x": .06, "y": .62, "t0": r(a, 41.7), "t1": 1.4},
  {"type": "stamp", "text": "RÉCUPÉRÉ", "tone": "green", "x": .6, "y": .8, "rot": -.08, "size": 110, "t0": r(a, 44.6)},
  {"type": "label", "text": "aucune séquelle apparente", "size": 46, "x": .5, "y": .9, "tone": "green", "t0": r(a, 46.24), "dur": 2.0}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}))
# 7 total time 48.4-57.5
a, b = 48.4, 57.5
S.append(sh(a, b, [
  {"type": "planet", **EAR, "x": 540, "y": 1900, "r": 1000, "light": -1.6, "spin": .01},
  {"type": "astronaut", "x": 760, "y": 1000, "s": 200, "spin": .4, "rot": .3},
  {"type": "label", "text": "combien de temps en tout ?", "size": 56, "x": .5, "y": .13, "tone": "yellow", "t0": .1, "dur": 2.0},
  {"type": "timer", "label": "LIMITE DES EXPERTS", "to": 120, "x": .07, "y": .22, "t0": r(a, 51.64), "t1": 1.0, "dur": 5.0},
  {"type": "label", "text": "tests sur des chiens", "size": 52, "x": .5, "y": .4, "t0": r(a, 53.6), "dur": 3.3},
  {"type": "counter", "label": "EXPOSITION", "from": 0, "to": 90, "unit": "s", "x": .06, "y": .46, "t0": r(a, 54.7), "t1": 1.3, "dur": 2.9},
  {"type": "stamp", "text": "PAS MORTEL", "tone": "green", "x": .5, "y": .74, "rot": -.07, "size": 100, "t0": r(a, 56.2)}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}))
# 8 survival game 57.5-69.9
a, b = 57.5, 69.9
S.append(sh(a, b, [
  {"type": "planet", **EAR, "x": 540, "y": 2000, "r": 900, "light": -1.6, "spin": .01},
  {"type": "astronaut", "x": 300, "y": 1350, "s": 170, "spin": .3, "rot": .3},
  {"type": "options", "title": "TES OPTIONS", "sc": 1.9, "x": .07, "y": .2, "t0": 0, "items": [
      {"text": "CRIER À L'AIDE", "at": r(a, 59.28), "out": r(a, 61.9)},
      {"text": "ATTENDRE QU'ON TE RATTRAPE", "at": r(a, 62.84), "out": r(a, 65.5)}]},
  {"type": "label", "text": "sans air, aucun son", "size": 52, "x": .5, "y": .52, "tone": "yellow", "t0": r(a, 60.6), "dur": 2.4},
  {"type": "stick", "x": .78, "y": .82, "s": 200, "pose": "panic", "label": "TOI", "t0": r(a, 59.3)},
  {"type": "stamp", "text": "MANQUE D'AIR", "x": .5, "y": .6, "rot": -.07, "size": 100, "t0": r(a, 68.5)}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}))
# 9 reversal 69.9-75.4
a, b = 69.9, 75.4
S.append(sh(a, b, [
  {"type": "planet", **EAR, "x": 540, "y": 1500, "r": 900, "light": -1.6, "spin": .02},
  {"type": "astronaut", "x": 540, "y": 650, "s": 170, "spin": .3, "rot": .2},
  {"type": "big", "text": "MAIS…", "size": 200, "x": .5, "y": .25, "tone": "yellow", "t0": 0, "dur": 1.2},
  {"type": "label", "text": "remis vite sous pression", "size": 52, "x": .5, "y": .15, "t0": r(a, 70.54), "dur": 2.8},
  {"type": "stamp", "text": "ÇA SE SOIGNE", "tone": "green", "x": .5, "y": .5, "rot": -.07, "size": 100, "t0": r(a, 72.6), "dur": 2.6},
  {"type": "counter", "label": "TEMPS DISPONIBLE", "from": 15, "to": 0, "unit": "s", "x": .06, "y": .12, "t0": r(a, 73.48), "t1": 1.8}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}, trans="fade"))
# 10 closing 75.4-86.54
a, b = 75.4, 86.54
S.append(sh(a, b, [
  {"type": "sun", "x": 60, "y": 1700, "r": 40},
  {"type": "planet", **EAR, "x": 640, "y": 1180, "r": 520, "light": 2.6, "spin": .03},
  {"type": "astronaut", "x": 330, "y": 860, "s": 70, "vx": -6, "rot": .35},
  {"type": "label", "text": "ni l'explosion, ni le froid", "size": 56, "x": .5, "y": .15, "t0": .05, "dur": 3.2},
  {"type": "label", "text": "c'est l'air qui manque", "size": 62, "x": .5, "y": .2, "tone": "red", "underline": True, "t0": r(a, 78.4), "dur": 2.0},
  {"type": "label", "text": "sur quelle planète veux-tu mourir ?", "size": 52, "x": .5, "y": .2, "tone": "yellow", "t0": r(a, 80.56), "dur": 2.0},
  {"type": "label", "text": "dis-le en commentaire", "size": 62, "x": .5, "y": .2, "tone": "yellow", "t0": r(a, 82.76)},
  {"type": "big", "text": "ABONNE-TOI", "size": 150, "x": .5, "y": .29, "tone": "red", "t0": r(a, 84.04)}],
  {"zoomFrom": 1.12, "zoomTo": 1.0, "fx": .62}, trans="fade"))
json.dump({"width": W, "height": H, "fps": 30, "k": 1, "shots": S}, open("scene.json", "w"), indent=1, ensure_ascii=False)
print(len(S), "shots, ends", S[-1]["end"])
