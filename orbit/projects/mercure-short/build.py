import json
W, H = 1080, 1920
MER = {"kind": "mercury", "seed": 3}
DAY = ["#1a1410", "#8c7a66", "#d9c4a4", "#6e5b48", "#4a3c2e", "#26201a"]
def sh(a, b, els, cam=None, **kw):
    d = {"start": a, "end": b, "els": els}
    if cam: d["cam"] = cam
    d.update(kw); return d
def r(a, t): return round(t - a, 2)
S = []
# 1 hook 0-6.3
a, b = 0, 6.3
S.append(sh(a, b, [
  {"type": "sun", "x": 60, "y": 1700, "r": 40},
  {"type": "planet", **MER, "x": 640, "y": 1180, "r": 520, "light": 2.6, "spin": .03},
  {"type": "astronaut", "x": 330, "y": 860, "s": 70, "vx": 8, "rot": .35},
  {"type": "you", "x": 352, "y": 830, "lx": 200, "ly": 600, "text": "TOI", "t0": .34},
  {"type": "title", "text": "MERCURE", "sub": "LA PLUS PROCHE DU SOLEIL", "tx": 80, "ty": 330, "t0": .6, "dur": 2.6},
  {"type": "label", "text": "donc la plus chaude ?", "size": 62, "x": .5, "y": .15, "t0": r(a, 2.54), "dur": 1.9},
  {"type": "stamp", "text": "FAUX", "x": .64, "y": .3, "rot": -.1, "size": 170, "t0": r(a, 3.56)}],
  {"zoomFrom": 1, "zoomTo": 1.1, "fx": .62}))
# 2 question 6.3-8.8
a, b = 6.3, 8.8
S.append(sh(a, b, [
  {"type": "planet", **MER, "x": 540, "y": 1650, "r": 900, "light": -1.6, "spin": .02},
  {"type": "astronaut", "x": 540, "y": 720, "s": 150, "spin": .9, "vy": 30},
  {"type": "label", "text": "qu'est-ce qui te tuerait", "size": 60, "x": .5, "y": .17, "t0": r(a, 6.36)},
  {"type": "big", "text": "EN PREMIER ?", "size": 150, "x": .5, "y": .25, "tone": "yellow", "t0": r(a, 7.28)}],
  {"zoomFrom": 1.0, "zoomTo": 1.12, "fy": .4}))
# 3 day 8.8-16.7
a, b = 8.8, 16.7
S.append(sh(a, b, [
  {"type": "surface", "kind": "moon", "cols": DAY, "heat": 2.0, "rocks": True},
  {"type": "sun", "x": 760, "y": 330, "r": 230, "surface": True},
  {"type": "astronaut", "x": 380, "y": 1560, "s": 190, "rot": .5, "lamp": 0},
  {"type": "chapter", "n": "DANGER 1", "text": "LE JOUR", "dur": .9},
  {"type": "thermo", "from": 20, "to": 430, "max": 500, "label": "JOUR", "x": .12, "y": .5, "t0": r(a, 10.9), "t1": 1.3},
  {"type": "balance", "left": "MERCURE 430°", "right": "VÉNUS 470°", "tilt": .3, "x": .66, "y": .6, "t0": r(a, 13.42)},
  {"type": "stamp", "text": "THERMOMÈTRE HS", "x": .5, "y": .22, "rot": -.07, "size": 80, "t0": r(a, 15.2)}],
  {"zoomFrom": 1.0, "zoomTo": 1.07, "fy": .6}))
# 4 night 16.7-26.0
a, b = 16.7, 26.0
S.append(sh(a, b, [
  {"type": "surface", "kind": "moon", "heat": 0, "rocks": True},
  {"type": "astronaut", "x": 800, "y": 1400, "s": 190, "rot": -.3, "lamp": .6, "flip": True},
  {"type": "chapter", "n": "DANGER 2", "text": "LA NUIT", "dur": .9},
  {"type": "label", "text": "pas d'atmosphère", "size": 62, "x": .5, "y": .17, "t0": r(a, 18.84), "dur": 2.8},
  {"type": "thermo", "from": 430, "to": -180, "min": -200, "max": 500, "label": "NUIT", "x": .3, "y": .62, "t0": r(a, 20.9), "t1": 1.4, "dur": 2.4},
  {"type": "panels", "titles": ["FOUR", "CONGÉLATEUR"], "bg": ["#8a2e10", "#0a2a4a"], "stagger": .3, "t0": r(a, 23.3), "dur": 2.6},
  {"type": "big", "text": "430 °C", "size": 110, "x": .25, "y": .5, "t0": r(a, 23.54), "tone": "red", "dur": 2.4},
  {"type": "big", "text": "-180 °C", "size": 110, "x": .75, "y": .5, "t0": r(a, 24.04), "dur": 1.9}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}))
# 5 air 26.0-32.0
a, b = 26.0, 32.0
S.append(sh(a, b, [
  {"type": "surface", "kind": "moon", "cols": DAY, "heat": 0, "rocks": True},
  {"type": "astronaut", "x": 760, "y": 1400, "s": 190, "rot": -.3, "lamp": 0},
  {"type": "chapter", "n": "DANGER 3", "text": "L'AIR", "dur": .9},
  {"type": "label", "text": "presque pas d'air", "size": 60, "x": .5, "y": .1, "t0": r(a, 28.14), "tone": "red", "underline": True},
  {"type": "xray", "part": "lungs", "label": "POUMONS", "title": "RESPIRE", "x": .5, "y": .56, "s": 220, "t0": r(a, 28.86)},
  {"type": "stamp", "text": "PAS D'AIR", "x": .5, "y": .8, "rot": .06, "size": 110, "t0": r(a, 31.0)}],
  {"zoomFrom": 1.0, "zoomTo": 1.05}))
# 6 time 32.0-42.0
a, b = 32.0, 42.0
S.append(sh(a, b, [
  {"type": "sun", "x": 60, "y": 1700, "r": 40},
  {"type": "planet", **MER, "x": 640, "y": 1250, "r": 480, "light": 2.6, "spin": .15},
  {"type": "counter", "label": "ANNÉE DE MERCURE", "from": 0, "to": 88, "unit": "jours", "x": .06, "y": .12, "t0": r(a, 33.4), "t1": 1.5},
  {"type": "counter", "label": "D'UN LEVER DE SOLEIL AU SUIVANT", "from": 0, "to": 176, "unit": "jours", "x": .06, "y": .27, "t0": r(a, 35.8), "t1": 1.7, "col": "#FFC93C"},
  {"type": "big", "text": "1 JOUR = 2 ANS", "size": 150, "x": .5, "y": .5, "tone": "yellow", "t0": r(a, 39.28), "dur": 2.4}],
  {"zoomFrom": 1.0, "zoomTo": 1.08, "fx": .62}))
# 7 BepiColombo 42.0-50.3
a, b = 42.0, 50.3
S.append(sh(a, b, [
  {"type": "planet", **MER, "x": 760, "y": 1150, "r": 400, "light": -2.4, "spin": .05},
  {"type": "rocket", "x": 250, "y": 700, "s": 120, "rot": .5, "vx": 70, "vy": 55},
  {"type": "tag", "text": "BEPICOLOMBO · 21 NOVEMBRE 2026 · ESA/JAXA", "x": .05, "y": .12, "t0": r(a, 43.58)},
  {"type": "stamp", "text": "EN ORBITE", "tone": "green", "x": .5, "y": .3, "rot": -.08, "size": 120, "t0": r(a, 45.66)},
  {"type": "big", "text": "8 ANS", "size": 220, "x": .5, "y": .6, "tone": "yellow", "t0": r(a, 47.0), "sub": "DE VOYAGE", "dur": 2.0},
  {"type": "pill", "text": "BUG LOGICIEL", "tone": "red", "size": 44, "x": .06, "y": .8, "t0": r(a, 48.8)}],
  {"zoomFrom": 1.0, "zoomTo": 1.1, "fx": .7}))
# 8 survival game 50.3-61.3
a, b = 50.3, 61.3
S.append(sh(a, b, [
  {"type": "surface", "kind": "moon", "cols": DAY, "heat": 1.2, "rocks": True},
  {"type": "astronaut", "x": 300, "y": 1500, "s": 170, "rot": .3, "lamp": .3},
  {"type": "options", "title": "TES OPTIONS", "sc": 1.9, "x": .07, "y": .2, "t0": 0, "items": [
      {"text": "PARASOL", "at": r(a, 51.88), "out": r(a, 54.2)},
      {"text": "COURIR VERS LA NUIT", "at": r(a, 54.86), "out": r(a, 57.0)}]},
  {"type": "stick", "x": .78, "y": .8, "s": 200, "pose": "panic", "label": "TOI", "t0": r(a, 51.9)},
  {"type": "stamp", "text": "LE CONTRASTE", "x": .5, "y": .5, "rot": -.07, "size": 100, "t0": r(a, 59.7)}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}))
# 9 poles 61.3-70.4
a, b = 61.3, 70.4
S.append(sh(a, b, [
  {"type": "planet", **MER, "x": 540, "y": 1900, "r": 1000, "light": -1.6, "spin": .01},
  {"type": "label", "text": "regarde les pôles", "size": 70, "x": .5, "y": .15, "tone": "yellow", "t0": r(a, 61.48), "dur": 3.2},
  {"type": "evidence", "src": "media/PIA19416.jpg", "credit": "NASA/JPL · MESSENGER", "tag": "CRATÈRES POLAIRES, JAMAIS AU SOLEIL", "x": .5, "y": .5, "w": 900, "h": 500, "t0": r(a, 62.76), "dur": 2.3, "zoom": .1},
  {"type": "evidence", "src": "media/PIA19411.jpg", "credit": "NASA/JPL · MESSENGER", "tag": "GLACE D'EAU (EN JAUNE)", "x": .5, "y": .5, "w": 980, "h": 560, "t0": r(a, 65.08), "dur": 4.3, "zoom": .12},
  {"type": "stamp", "text": "GLACE", "tone": "green", "x": .5, "y": .8, "rot": .06, "size": 130, "t0": r(a, 66.5)}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}))
# 10 closing: mirror of shot 1
a, b = 70.4, 75.8
S.append(sh(a, b, [
  {"type": "sun", "x": 60, "y": 1700, "r": 40},
  {"type": "planet", **MER, "x": 640, "y": 1180, "r": 520, "light": 2.6, "spin": .03},
  {"type": "astronaut", "x": 330, "y": 860, "s": 70, "vx": -6, "rot": .35},
  {"type": "label", "text": "sur quelle planète veux-tu mourir ?", "size": 52, "x": .5, "y": .2, "tone": "yellow", "t0": r(a, 70.52), "dur": 1.8},
  {"type": "label", "text": "dis-le en commentaire", "size": 62, "x": .5, "y": .2, "tone": "yellow", "t0": r(a, 72.4)},
  {"type": "big", "text": "ABONNE-TOI", "size": 150, "x": .5, "y": .29, "tone": "red", "t0": r(a, 73.62)}],
  {"zoomFrom": 1.12, "zoomTo": 1.0, "fx": .62}, trans="fade"))
json.dump({"width": W, "height": H, "fps": 30, "k": 1, "shots": S}, open("scene.json", "w"), indent=1, ensure_ascii=False)
print(len(S), "shots, ends", S[-1]["end"])
