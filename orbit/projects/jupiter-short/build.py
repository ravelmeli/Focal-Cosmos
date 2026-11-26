import json
W, H = 1080, 1920
JUP = {"kind": "jupiter", "seed": 3}
def sh(a, b, els, cam=None, **kw):
    d = {"start": a, "end": b, "els": els}
    if cam: d["cam"] = cam
    d.update(kw); return d
def r(a, t): return round(t - a, 2)
S = []
# 1 hook 0-5.7
a, b = 0, 5.7
S.append(sh(a, b, [
  {"type": "sun", "x": 60, "y": 1750, "r": 30},
  {"type": "planet", **JUP, "x": 640, "y": 1180, "r": 560, "light": 2.6, "spin": .04},
  {"type": "astronaut", "x": 330, "y": 800, "s": 70, "vx": 8, "rot": .35},
  {"type": "you", "x": 352, "y": 770, "lx": 200, "ly": 560, "text": "TOI", "t0": .34},
  {"type": "title", "text": "JUPITER", "sub": "ON PEUT S'Y POSER ?", "tx": 80, "ty": 330, "t0": .3, "dur": 1.3},
  {"type": "label", "text": "si grosse qu'on peut s'y poser ?", "size": 48, "x": .5, "y": .15, "t0": 1.4, "dur": 1.9},
  {"type": "stamp", "text": "FAUX", "x": .66, "y": .3, "rot": -.1, "size": 170, "t0": 3.36, "dur": 1.6},
  {"type": "label", "text": "elle n'a pas de sol", "size": 56, "x": .5, "y": .15, "tone": "red", "underline": True, "t0": 4.2, "dur": 1.5}],
  {"zoomFrom": 1, "zoomTo": 1.08, "fx": .62}))
# 2 question 5.7-8.0
a, b = 5.7, 8.0
S.append(sh(a, b, [
  {"type": "planet", **JUP, "x": 540, "y": 1650, "r": 900, "light": -1.6, "spin": .02},
  {"type": "astronaut", "x": 540, "y": 720, "s": 150, "spin": .9, "vy": 30},
  {"type": "label", "text": "qu'est-ce qui te tuerait", "size": 60, "x": .5, "y": .17, "t0": .02},
  {"type": "big", "text": "EN PREMIER ?", "size": 150, "x": .5, "y": .25, "tone": "yellow", "t0": r(a, 6.52)}],
  {"zoomFrom": 1.0, "zoomTo": 1.12, "fy": .4}))
# 3 radiation 8.0-20.7
a, b = 8.0, 20.7
S.append(sh(a, b, [
  {"type": "planet", **JUP, "x": 540, "y": 2000, "r": 1000, "light": -1.6, "spin": .02},
  {"type": "astronaut", "x": 540, "y": 1250, "s": 200, "spin": .3, "rot": .3},
  {"type": "chapter", "n": "DANGER 1", "text": "LES RADIATIONS", "dur": .9, "t0": r(a, 8.06)},
  {"type": "evidence", "src": "media/PIA13257.jpg", "credit": "NASA/JPL · Juno", "tag": "JUNO · LE COFFRE EN TITANE (SALLE BLANCHE)", "x": .5, "y": .33, "w": 900, "h": 697, "t0": r(a, 12.7), "dur": 6.0, "zoom": .08},
  {"type": "pill", "text": "MURS : ≈ 1 CM DE TITANE", "tone": "red", "size": 40, "x": .06, "y": .58, "t0": r(a, 16.2)},
  {"type": "stamp", "text": "TOI : PAS DE COFFRE", "x": .5, "y": .7, "rot": -.07, "size": 80, "t0": r(a, 18.6), "dur": 2.0}],
  {"zoomFrom": 1.0, "zoomTo": 1.05}))
# 4 winds 20.7-31.5
a, b = 20.7, 31.5
S.append(sh(a, b, [
  {"type": "descent", "sky": ["#e8c9a0", "#b9784a"], "cols": ["#f1dcc0", "#d9a374", "#b9784a"], "speed": 900, "alpha": .9},
  {"type": "astronaut", "x": 760, "y": 1100, "s": 200, "spin": .6, "rot": -.4, "lamp": 0},
  {"type": "chapter", "n": "DANGER 2", "text": "LES VENTS", "dur": .9, "t0": r(a, 20.72)},
  {"type": "tag", "text": "SONDE GALILEO · 1995", "x": .05, "y": .12, "t0": r(a, 22.9)},
  {"type": "pill", "text": "PLUS FORT QUE PRÉVU", "tone": "red", "size": 42, "x": .06, "y": .2, "t0": r(a, 25.64)},
  {"type": "counter", "label": "VENT MESURÉ", "from": 0, "to": 500, "unit": "km/h", "x": .06, "y": .3, "t0": r(a, 27.2), "t1": 1.5},
  {"type": "label", "text": "pas plus faible en profondeur", "size": 48, "x": .5, "y": .62, "tone": "yellow", "t0": r(a, 29.44), "dur": 2.0}],
  {"zoomFrom": 1.0, "zoomTo": 1.08, "shake": 3}))
# 5 pressure + heat 31.5-41.7
a, b = 31.5, 41.7
S.append(sh(a, b, [
  {"type": "descent", "sky": ["#8a4a24", "#3a1a0a"], "cols": ["#b9784a", "#8a4a24", "#5a2e14"], "speed": 450, "alpha": .85},
  {"type": "astronaut", "x": 800, "y": 1500, "s": 190, "spin": .25, "rot": .2, "lamp": .6},
  {"type": "chapter", "n": "DANGER 3", "text": "PRESSION ET CHALEUR", "dur": .9, "t0": r(a, 31.7)},
  {"type": "label", "text": "là où Galileo a cessé d'émettre", "size": 42, "x": .5, "y": .12, "t0": r(a, 34.78), "dur": 3.5},
  {"type": "gauge", "label": "PRESSION (TERRE = 1×)", "to": 23, "max": 30, "unit": "×", "x": .5, "y": .3, "r": 200, "t0": r(a, 36.5), "t1": 1.4},
  {"type": "thermo", "to": 152, "from": 20, "max": 200, "label": "TEMPÉRATURE", "x": .12, "y": .72, "t0": r(a, 39.3), "t1": 1.2}],
  {"zoomFrom": 1.04, "zoomTo": 1.0, "shake": 2}))
# 6 no ground 41.7-50.5
a, b = 41.7, 50.5
S.append(sh(a, b, [
  {"type": "descent", "sky": ["#3a1a0a", "#150805"], "cols": ["#6a3a1a", "#4a2410", "#2a1208"], "speed": 200, "alpha": .9},
  {"type": "astronaut", "x": 540, "y": 1000, "s": 220, "spin": .2, "rot": .2, "lamp": .7},
  {"type": "stamp", "text": "PAS DE SOL", "x": .5, "y": .15, "rot": -.07, "size": 130, "t0": r(a, 43.0), "dur": 3.0},
  {"type": "label", "text": "gaz → hydrogène liquide", "size": 52, "x": .5, "y": .3, "t0": r(a, 44.2), "dur": 3.3},
  {"type": "label", "text": "sans frontière nette", "size": 56, "x": .5, "y": .36, "tone": "yellow", "t0": r(a, 46.54), "dur": 1.5},
  {"type": "big", "text": "TU T'ENFONCES", "size": 120, "x": .5, "y": .72, "tone": "yellow", "t0": r(a, 49.2)}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}))
# 7 Galileo proof 50.5-56.6
a, b = 50.5, 56.6
S.append(sh(a, b, [
  {"type": "planet", **JUP, "x": 540, "y": 2000, "r": 900, "light": -1.6, "spin": .02},
  {"type": "evidence", "src": "media/PIA01259.jpg", "credit": "NASA/JPL · Hubble", "tag": "SITE D'ENTRÉE DE GALILEO · HUBBLE · 1995", "x": .5, "y": .3, "w": 940, "h": 542, "t0": r(a, 50.74), "dur": 5.7, "zoom": .05},
  {"type": "timer", "label": "GALILEO A TENU", "to": 3480, "x": .06, "y": .55, "t0": r(a, 51.2), "t1": 1.0},
  {"type": "label", "text": "une sonde qui n'en est jamais revenue", "size": 42, "x": .5, "y": .8, "tone": "yellow", "t0": r(a, 54.58), "dur": 2.0}],
  {"zoomFrom": 1.0, "zoomTo": 1.05}))
# 8 options 56.6-65.0
a, b = 56.6, 65.0
S.append(sh(a, b, [
  {"type": "planet", **JUP, "x": 540, "y": 2000, "r": 900, "light": -1.6, "spin": .02},
  {"type": "astronaut", "x": 300, "y": 1350, "s": 170, "spin": .3, "rot": .3},
  {"type": "options", "title": "TES OPTIONS", "sc": 1.9, "x": .07, "y": .2, "t0": 0, "items": [
      {"text": "TE POSER", "at": r(a, 58.12), "out": r(a, 59.7)},
      {"text": "RÉSISTER AU VENT", "at": r(a, 59.84), "out": r(a, 61.8)}]},
  {"type": "stick", "x": .78, "y": .82, "s": 200, "pose": "panic", "label": "TOI", "t0": r(a, 58.1)},
  {"type": "stamp", "text": "RADIATIONS D'ABORD", "tone": "yellow", "x": .5, "y": .55, "rot": -.07, "size": 80, "t0": r(a, 62.92)}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}))
# 9 closing 65.0-73.35
a, b = 65.0, 73.35
S.append(sh(a, b, [
  {"type": "sun", "x": 60, "y": 1750, "r": 30},
  {"type": "planet", **JUP, "x": 640, "y": 1180, "r": 560, "light": 2.6, "spin": .04},
  {"type": "astronaut", "x": 330, "y": 800, "s": 70, "vx": -6, "rot": .35},
  {"type": "label", "text": "pas un endroit où se poser", "size": 52, "x": .5, "y": .15, "t0": r(a, 65.16), "dur": 2.3},
  {"type": "label", "text": "sur quelle planète veux-tu mourir ?", "size": 52, "x": .5, "y": .2, "tone": "yellow", "t0": r(a, 67.68), "dur": 2.0},
  {"type": "label", "text": "dis-le en commentaire", "size": 62, "x": .5, "y": .2, "tone": "yellow", "t0": r(a, 69.76), "dur": 1.0},
  {"type": "big", "text": "ABONNE-TOI", "size": 150, "x": .5, "y": .29, "tone": "red", "t0": r(a, 70.78)}],
  {"zoomFrom": 1.12, "zoomTo": 1.0, "fx": .62}, trans="fade"))
json.dump({"width": W, "height": H, "fps": 30, "k": 1, "shots": S}, open("scene.json", "w"), indent=1, ensure_ascii=False)
print(len(S), "shots, ends", S[-1]["end"])
