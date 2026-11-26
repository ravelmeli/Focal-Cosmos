import json
W, H = 1080, 1920
EAR = {"kind": "earth", "seed": 2}
AST = {"kind": "moon", "seed": 7}
def sh(a, b, els, cam=None, **kw):
    d = {"start": a, "end": b, "els": els}
    if cam: d["cam"] = cam
    d.update(kw); return d
def r(a, t): return round(t - a, 2)
S = []
# 1 hook 0-6.4
a, b = 0, 6.4
S.append(sh(a, b, [
  {"type": "sun", "x": 60, "y": 1750, "r": 40},
  {"type": "planet", **EAR, "x": 740, "y": 1400, "r": 380, "light": 2.6, "spin": .03},
  {"type": "planet", **AST, "x": 930, "y": 720, "r": 120, "light": 2.6, "spin": .3},
  {"type": "astronaut", "x": 420, "y": 1250, "s": 70, "vx": 6, "rot": .35},
  {"type": "you", "x": 440, "y": 1220, "lx": 250, "ly": 1000, "text": "TOI", "t0": .34},
  {"type": "title", "text": "ASTÉROÏDE", "sub": "ET SI ÇA ARRIVAIT ?", "tx": 80, "ty": 330, "t0": .2, "dur": 1.1},
  {"type": "label", "text": "un astéroïde fonce vers la Terre", "size": 52, "x": .5, "y": .15, "t0": 1.4, "dur": 1.7},
  {"type": "label", "text": "la NASA fait un test", "size": 62, "x": .5, "y": .15, "t0": r(a, 3.28), "dur": 1.6},
  {"type": "big", "text": "LE PERCUTER", "size": 130, "x": .5, "y": .22, "tone": "yellow", "t0": r(a, 5.04), "dur": 1.3}],
  {"zoomFrom": 1, "zoomTo": 1.08, "fx": .6}))
# 2 DART impact 6.4-14.2
a, b = 6.4, 14.2
S.append(sh(a, b, [
  {"type": "planet", **AST, "x": 800, "y": 1000, "r": 170, "light": -2.4, "spin": .1},
  {"type": "rocket", "x": 100, "y": 1000, "s": 110, "rot": 0, "vx": 150, "vy": 0},
  {"type": "tag", "text": "DART · NASA · 2022", "x": .05, "y": .12, "t0": .15},
  {"type": "evidence", "src": "media/PIA25329.jpg", "credit": "NASA/JPL · illustration", "tag": "ILLUSTRATION · DART ET DIMORPHOS", "x": .5, "y": .34, "w": 960, "h": 540, "t0": r(a, 8.2), "dur": 2.4, "zoom": .08},
  {"type": "counter", "label": "VITESSE DU VAISSEAU", "from": 0, "to": 20000, "unit": "km/h", "x": .06, "y": .62, "t0": r(a, 10.18), "t1": 1.5},
  {"type": "flash", "t0": r(a, 11.9), "dur": .4, "a": .8},
  {"type": "stamp", "text": "IMPACT", "x": .5, "y": .8, "rot": -.07, "size": 140, "t0": r(a, 12.0)},
  {"type": "label", "text": "elle ne menaçait pas la Terre", "size": 46, "x": .5, "y": .9, "tone": "green", "t0": r(a, 12.6), "dur": 1.6}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}))
# 3 result 14.2-26.0
a, b = 14.2, 26.0
S.append(sh(a, b, [
  {"type": "planet", **AST, "x": 560, "y": 1300, "r": 330, "light": -2.4, "spin": .02},
  {"type": "planet", "kind": "moon", "seed": 11, "x": 880, "y": 700, "r": 105, "light": -2.4, "spin": .2},
  {"type": "counter", "label": "SON TOUR RACCOURCI DE", "from": 0, "to": 33, "unit": "min", "x": .06, "y": .1, "t0": r(a, 15.3), "t1": 2.3},
  {"type": "balance", "left": "PRÉVU : 7 MIN", "right": "RÉEL : 33 MIN", "tilt": .35, "x": .5, "y": .45, "t0": r(a, 19.6)},
  {"type": "label", "text": "les débris ont poussé", "size": 54, "x": .5, "y": .65, "t0": r(a, 23.08), "dur": 2.5},
  {"type": "stamp", "text": "COUP DE POUCE", "tone": "yellow", "x": .5, "y": .76, "rot": -.07, "size": 100, "t0": r(a, 24.06)}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}))
# 4 Hera arrives 26.0-36.4
a, b = 26.0, 36.4
S.append(sh(a, b, [
  {"type": "planet", **AST, "x": 720, "y": 1300, "r": 300, "light": -2.4, "spin": .02},
  {"type": "planet", "kind": "moon", "seed": 11, "x": 330, "y": 1100, "r": 90, "light": -2.4, "spin": .2},
  {"type": "rocket", "x": 150, "y": 600, "s": 110, "rot": .6, "vx": 60, "vy": 50},
  {"type": "label", "text": "personne n'a vu le résultat de près", "size": 46, "x": .5, "y": .13, "t0": r(a, 26.24), "dur": 2.4},
  {"type": "tag", "text": "HERA · ESA · DÉBUT NOVEMBRE 2026", "x": .05, "y": .2, "t0": r(a, 28.48)},
  {"type": "stamp", "text": "ARRIVÉE", "tone": "green", "x": .5, "y": .42, "rot": -.08, "size": 120, "t0": r(a, 31.72), "dur": 1.2},
  {"type": "big", "text": "25 NOV.", "size": 200, "x": .5, "y": .4, "tone": "yellow", "t0": r(a, 33.06), "sub": "PREMIÈRES IMAGES DE PRÈS", "dur": 3.1}],
  {"zoomFrom": 1.0, "zoomTo": 1.08}))
# 5 findings 36.4-46.8
a, b = 36.4, 46.8
S.append(sh(a, b, [
  {"type": "planet", **AST, "x": 540, "y": 1700, "r": 800, "light": -1.6, "spin": .01},
  {"type": "chapter", "n": "CE QU'ELLE A TROUVÉ", "text": "HERA", "dur": .9},
  {"type": "pill", "text": "CRATÈRE GRAND COMME UN STADE", "tone": "red", "size": 40, "x": .06, "y": .15, "t0": r(a, 37.68)},
  {"type": "icons", "count": 100, "cols": 10, "icon": "dot", "size": 56, "label": "ROCHERS", "caption": "DES CENTAINES", "x": .5, "y": .27, "t0": r(a, 39.48), "dur": 3.0},
  {"type": "label", "text": "gros comme une machine à laver", "size": 46, "x": .5, "y": .63, "t0": r(a, 40.84), "dur": 1.9},
  {"type": "planet", "kind": "moon", "seed": 11, "x": 540, "y": 1100, "r": 140, "light": -2.4, "spin": 1.4, "t0": r(a, 42.84)},
  {"type": "label", "text": "semble tourner de façon chaotique", "size": 46, "x": .5, "y": .78, "tone": "yellow", "t0": r(a, 43.36), "dur": 3.0},
  {"type": "stamp", "text": "À CONFIRMER", "tone": "yellow", "x": .5, "y": .9, "rot": .06, "size": 70, "t0": r(a, 45.5)}],
  {"zoomFrom": 1.0, "zoomTo": 1.05}))
# 6 defense 46.8-55.2
a, b = 46.8, 55.2
S.append(sh(a, b, [
  {"type": "planet", **EAR, "x": 780, "y": 1500, "r": 400, "light": 2.6, "spin": .03},
  {"type": "planet", **AST, "x": 220, "y": 620, "r": 110, "light": 2.6, "spin": .3},
  {"type": "label", "text": "et si un vrai astéroïde fonçait ?", "size": 52, "x": .5, "y": .13, "tone": "yellow", "t0": r(a, 46.84), "dur": 3.4},
  {"type": "stamp", "text": "ON PEUT LE DÉVIER", "tone": "green", "x": .5, "y": .35, "rot": -.07, "size": 80, "t0": r(a, 50.56)},
  {"type": "label", "text": "à condition de le voir arriver assez tôt", "size": 42, "x": .5, "y": .55, "tone": "red", "underline": True, "t0": r(a, 52.72)}],
  {"zoomFrom": 1.0, "zoomTo": 1.07}))
# 7 next steps 55.2-61.4
a, b = 55.2, 61.4
S.append(sh(a, b, [
  {"type": "planet", **AST, "x": 720, "y": 1300, "r": 300, "light": -2.4, "spin": .02},
  {"type": "rocket", "x": 260, "y": 800, "s": 120, "rot": .6, "vx": 30, "vy": 40},
  {"type": "pill", "text": "DÉCEMBRE · HERA SE RAPPROCHE", "size": 38, "x": .06, "y": .15, "t0": r(a, 56.26)},
  {"type": "pill", "text": "JANVIER · 2 MINI-SATELLITES", "size": 38, "tone": "red", "x": .06, "y": .25, "t0": r(a, 58.82)},
  {"type": "rocket", "x": 380, "y": 980, "s": 50, "rot": 1.0, "vx": 30, "vy": 25, "t0": r(a, 59.56)},
  {"type": "rocket", "x": 460, "y": 880, "s": 50, "rot": .8, "vx": 40, "vy": 30, "t0": r(a, 60.02)}],
  {"zoomFrom": 1.0, "zoomTo": 1.07}, trans="fade"))
# 8 closing 61.4-67.63
a, b = 61.4, 67.63
S.append(sh(a, b, [
  {"type": "sun", "x": 60, "y": 1750, "r": 40},
  {"type": "planet", **EAR, "x": 740, "y": 1400, "r": 380, "light": 2.6, "spin": .03},
  {"type": "planet", **AST, "x": 930, "y": 720, "r": 120, "light": 2.6, "spin": .3},
  {"type": "astronaut", "x": 420, "y": 1250, "s": 70, "vx": -6, "rot": .35},
  {"type": "label", "text": "sur quelle planète veux-tu mourir ?", "size": 52, "x": .5, "y": .2, "tone": "yellow", "t0": r(a, 61.58), "dur": 2.0},
  {"type": "label", "text": "dis-le en commentaire", "size": 62, "x": .5, "y": .2, "tone": "yellow", "t0": r(a, 63.74), "dur": 1.2},
  {"type": "big", "text": "ABONNE-TOI", "size": 150, "x": .5, "y": .29, "tone": "red", "t0": r(a, 64.96)}],
  {"zoomFrom": 1.1, "zoomTo": 1.0, "fx": .6}, trans="fade"))
json.dump({"width": W, "height": H, "fps": 30, "k": 1, "shots": S}, open("scene.json", "w"), indent=1, ensure_ascii=False)
print(len(S), "shots, ends", S[-1]["end"])
