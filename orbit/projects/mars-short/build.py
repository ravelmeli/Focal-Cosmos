import json
W, H = 1080, 1920
MARS = {"kind": "mars", "seed": 5}
SURF = {"type": "surface", "kind": "mars", "heat": .8, "rocks": True}
def sh(a, b, els, cam=None, **kw):
    d = {"start": a, "end": b, "els": els}
    if cam: d["cam"] = cam
    d.update(kw); return d
def r(a, t): return round(t - a, 2)
S = []
# 1 hook 0-5.2
a, b = 0, 5.2
S.append(sh(a, b, [
  {"type": "sun", "x": 60, "y": 1750, "r": 30},
  {"type": "planet", **MARS, "x": 640, "y": 1180, "r": 520, "light": 2.6, "spin": .03},
  {"type": "astronaut", "x": 330, "y": 860, "s": 70, "vx": 8, "rot": .35},
  {"type": "you", "x": 352, "y": 830, "lx": 200, "ly": 600, "text": "TOI", "t0": .34},
  {"type": "title", "text": "MARS", "sub": "UNE TERRE ROUGE ?", "tx": 80, "ty": 330, "t0": .2, "dur": 1.2},
  {"type": "label", "text": "un désert rouge", "size": 62, "x": .5, "y": .15, "t0": 1.58, "dur": 1.5},
  {"type": "label", "text": "marcher en t-shirt ?", "size": 62, "x": .5, "y": .15, "t0": 3.1, "dur": 1.3},
  {"type": "stamp", "text": "FAUX", "x": .66, "y": .3, "rot": -.1, "size": 170, "t0": 4.36, "dur": 0.8}],
  {"zoomFrom": 1, "zoomTo": 1.1, "fx": .62}))
# 2 question 5.2-7.5
a, b = 5.2, 7.5
S.append(sh(a, b, [
  {"type": "planet", **MARS, "x": 540, "y": 1650, "r": 900, "light": -1.6, "spin": .02},
  {"type": "astronaut", "x": 540, "y": 720, "s": 150, "spin": .9, "vy": 30},
  {"type": "label", "text": "qu'est-ce qui te tuerait", "size": 60, "x": .5, "y": .17, "t0": .05},
  {"type": "big", "text": "EN PREMIER ?", "size": 150, "x": .5, "y": .25, "tone": "yellow", "t0": r(a, 6.06)}],
  {"zoomFrom": 1.0, "zoomTo": 1.12, "fy": .4}))
# 3 air 7.5-18.1
a, b = 7.5, 18.1
S.append(sh(a, b, [
  dict(SURF),
  {"type": "astronaut", "x": 800, "y": 1450, "s": 190, "rot": -.3, "lamp": 0},
  {"type": "chapter", "n": "DANGER 1", "text": "L'AIR", "dur": .9, "t0": r(a, 7.58)},
  {"type": "pie", "title": "L'AIR DE MARS", "slices": [{"v": 95.3, "label": "GAZ CARBONIQUE", "col": "#FF3B30"}, {"v": 4.7, "label": "AUTRES", "col": "#6FE3FF"}], "stat": {"label": "GAZ CARBONIQUE", "big": "95 %", "small": ""}, "r": 300, "x": .36, "y": .35, "t0": r(a, 10.0), "dur": 2.2},
  {"type": "gauge", "label": "PRESSION (TERRE = 100 %)", "from": 100, "to": 1, "max": 100, "unit": " %", "x": .5, "y": .4, "r": 200, "t0": r(a, 12.1), "t1": 1.4, "dur": 3.2},
  {"type": "xray", "part": "lungs", "label": "POUMONS", "title": "RESPIRE", "x": .5, "y": .5, "s": 220, "t0": r(a, 15.5)}],
  {"zoomFrom": 1.0, "zoomTo": 1.05}))
# 4 cold 18.1-25.4
a, b = 18.1, 25.4
S.append(sh(a, b, [
  dict(SURF),
  {"type": "chapter", "n": "DANGER 2", "text": "LE FROID", "dur": .9, "t0": r(a, 18.12)},
  {"type": "thermo", "from": 20, "to": -60, "min": -100, "max": 40, "label": "TEMPÉRATURE MOYENNE", "x": .15, "y": .5, "t0": r(a, 20.3), "t1": 1.6},
  {"type": "stick", "x": .74, "y": .78, "s": 220, "pose": "panic", "label": "T-SHIRT", "t0": r(a, 23.3)},
  {"type": "stamp", "text": "AUCUNE CHANCE", "x": .5, "y": .18, "rot": -.07, "size": 90, "t0": r(a, 23.98)}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}))
# 5 radiation 25.4-38.7
a, b = 25.4, 38.7
S.append(sh(a, b, [
  {"type": "planet", **MARS, "x": 540, "y": 1900, "r": 900, "light": -1.6, "spin": .01},
  {"type": "astronaut", "x": 540, "y": 1400, "s": 200, "spin": .3, "rot": .3},
  {"type": "chapter", "n": "DANGER 3", "text": "LES RADIATIONS", "dur": .9, "t0": 0},
  {"type": "counter", "label": "RADIATION EN SURFACE", "from": 0, "to": 0.64, "decimals": 2, "unit": "mSv / jour", "x": .06, "y": .1, "t0": r(a, 28.14), "t1": 1.6},
  {"type": "pill", "text": "180 J · ALLER", "size": 44, "x": .08, "y": .26, "t0": r(a, 32.5)},
  {"type": "pill", "text": "500 J · SUR PLACE", "size": 44, "x": .08, "y": .33, "t0": r(a, 33.8)},
  {"type": "pill", "text": "180 J · RETOUR", "size": 44, "x": .08, "y": .4, "t0": r(a, 35.2)},
  {"type": "big", "text": "≈ 1 SIEVERT", "size": 150, "x": .5, "y": .53, "tone": "red", "t0": r(a, 37.14)}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}))
# 6 proof 38.7-50.4
a, b = 38.7, 50.4
S.append(sh(a, b, [
  {"type": "planet", **MARS, "x": 540, "y": 2000, "r": 900, "light": -1.6, "spin": .01},
  {"type": "label", "text": "on s'y prépare", "size": 62, "x": .5, "y": .12, "tone": "green", "t0": .1, "dur": 1.5},
  {"type": "evidence", "src": "media/PIA24542.jpg", "credit": "NASA/JPL-Caltech · Perseverance", "tag": "ROVER PERSEVERANCE · MARS", "x": .5, "y": .34, "w": 940, "h": 690, "t0": r(a, 40.3), "dur": 4.3, "zoom": .08},
  {"type": "evidence", "src": "media/PIA24203.jpg", "credit": "NASA/JPL-Caltech · MOXIE", "tag": "MOXIE · FABRIQUE DE L'OXYGÈNE", "x": .5, "y": .34, "w": 900, "h": 675, "t0": r(a, 44.7), "dur": 5.5, "zoom": .08},
  {"type": "counter", "label": "OXYGÈNE FABRIQUÉ", "from": 0, "to": 122, "unit": "g", "x": .06, "y": .66, "t0": r(a, 46.0), "t1": 1.0},
  {"type": "label", "text": "un petit chien pendant 10 h", "size": 52, "x": .5, "y": .82, "tone": "yellow", "t0": r(a, 48.2), "dur": 2.1}],
  {"zoomFrom": 1.0, "zoomTo": 1.05}))
# 7 survival game 50.4-59.8
a, b = 50.4, 59.8
S.append(sh(a, b, [
  dict(SURF),
  {"type": "astronaut", "x": 300, "y": 1500, "s": 170, "rot": .3, "lamp": .3},
  {"type": "options", "title": "TES OPTIONS", "sc": 1.9, "x": .07, "y": .2, "t0": 0, "items": [
      {"text": "RESPIRER L'AIR", "at": r(a, 51.72), "out": r(a, 54.4)},
      {"text": "SORTIR EN T-SHIRT", "at": r(a, 55.14), "out": r(a, 57.0)}]},
  {"type": "stick", "x": .78, "y": .82, "s": 200, "pose": "panic", "label": "TOI", "t0": r(a, 51.8)},
  {"type": "stamp", "text": "L'AIR EN PREMIER", "tone": "yellow", "x": .5, "y": .5, "rot": -.07, "size": 90, "t0": r(a, 58.4)}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}))
# 8 reversal 59.8-62.8
a, b = 59.8, 62.8
S.append(sh(a, b, [
  {"type": "planet", **MARS, "x": 540, "y": 1500, "r": 900, "light": -1.6, "spin": .02},
  {"type": "astronaut", "x": 540, "y": 650, "s": 170, "spin": .3, "rot": .2},
  {"type": "label", "text": "le gaz qui te tue", "size": 60, "x": .5, "y": .15, "tone": "red", "t0": .3, "dur": 1.8},
  {"type": "stamp", "text": "L'OXYGÈNE DE DEMAIN", "tone": "green", "x": .5, "y": .3, "rot": -.07, "size": 80, "t0": r(a, 61.64)}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}, trans="fade"))
# 9 closing 62.8-70.22
a, b = 62.8, 70.22
S.append(sh(a, b, [
  {"type": "sun", "x": 60, "y": 1750, "r": 30},
  {"type": "planet", **MARS, "x": 640, "y": 1180, "r": 520, "light": 2.6, "spin": .03},
  {"type": "astronaut", "x": 330, "y": 860, "s": 70, "vx": -6, "rot": .35},
  {"type": "label", "text": "mars n'est pas une terre rouge", "size": 52, "x": .5, "y": .15, "t0": .06, "dur": 1.9},
  {"type": "label", "text": "sur quelle planète veux-tu mourir ?", "size": 52, "x": .5, "y": .2, "tone": "yellow", "t0": r(a, 64.88), "dur": 2.0},
  {"type": "label", "text": "dis-le en commentaire", "size": 62, "x": .5, "y": .2, "tone": "yellow", "t0": r(a, 67.0), "dur": .8},
  {"type": "big", "text": "ABONNE-TOI", "size": 150, "x": .5, "y": .29, "tone": "red", "t0": r(a, 67.82)}],
  {"zoomFrom": 1.12, "zoomTo": 1.0, "fx": .62}, trans="fade"))
json.dump({"width": W, "height": H, "fps": 30, "k": 1, "shots": S}, open("scene.json", "w"), indent=1, ensure_ascii=False)
print(len(S), "shots, ends", S[-1]["end"])
