import json
# Vertical 1080x1920, k=1 : coordonnees du monde = pixels ecran
VEN = {"kind": "venus", "seed": 4}
W, H = 1080, 1920
def sh(a, b, els, cam=None, **kw):
    d = {"start": a, "end": b, "els": els}
    if cam: d["cam"] = cam
    d.update(kw); return d
def r(a, t): return round(t - a, 2)
S = []
# 1 hook 0-2.4
a, b = 0, 2.4
S.append(sh(a, b, [
  {"type": "sun", "x": 60, "y": 1700, "r": 30},
  {"type": "planet", **VEN, "x": 640, "y": 1180, "r": 520, "light": 2.6, "spin": .03},
  {"type": "astronaut", "x": 330, "y": 860, "s": 70, "vx": 8, "rot": .35},
  {"type": "you", "x": 352, "y": 830, "lx": 200, "ly": 600, "text": "TOI", "t0": .34},
  {"type": "title", "text": "VÉNUS", "sub": "LA JUMELLE DE LA TERRE ?", "tx": 80, "ty": 330, "t0": .9, "dur": 1.5}],
  {"zoomFrom": 1, "zoomTo": 1.1, "fx": .62}))
# 2 jumelle: meme taille 2.4-6.0
a, b = 2.4, 6.0
S.append(sh(a, b, [
  {"type": "lineup", "y": .55, "gap": 20, "items": [
     {"kind": "venus", "seed": 4, "r": 240, "label": "VÉNUS", "note": "12 104 km", "at": r(a, 3.1)},
     {"kind": "earth", "r": 250, "label": "TERRE", "note": "12 742 km", "at": r(a, 3.86)}]},
  {"type": "label", "text": "12 104 km ≈ 12 742 km", "size": 54, "x": .5, "y": .66, "t0": r(a, 3.9), "dur": 2.0},
  {"type": "label", "text": "presque notre taille", "size": 70, "x": .5, "y": .2, "t0": r(a, 4.66), "dur": 1.3}],
  {"zoomFrom": 1.0, "zoomTo": 1.05}))
# 3 piege + question 6.0-10.7
a, b = 6.0, 10.7
S.append(sh(a, b, [
  {"type": "planet", **VEN, "x": 540, "y": 1650, "r": 900, "light": -1.6, "spin": .02},
  {"type": "astronaut", "x": 540, "y": 720, "s": 150, "spin": .9, "vy": 30},
  {"type": "stamp", "text": "PIÈGE", "x": .5, "y": .3, "rot": -.1, "size": 130, "t0": r(a, 7.3), "dur": 1.2},
  {"type": "label", "text": "qu'est-ce qui te tuerait", "size": 60, "x": .5, "y": .17, "t0": r(a, 8.46)},
  {"type": "big", "text": "EN PREMIER ?", "size": 150, "x": .5, "y": .25, "tone": "yellow", "t0": r(a, 9.34)}],
  {"zoomFrom": 1.0, "zoomTo": 1.12, "fy": .4}))
# 4 acid clouds 10.7-22.2
a, b = 10.7, 22.2
S.append(sh(a, b, [
  {"type": "descent", "sky": ["#ecca86", "#b98a3e"], "cols": ["#f2dca4", "#dab36a", "#b8893e"], "speed": 700, "rain": "#e8f27a"},
  {"type": "astronaut", "x": 760, "y": 1000, "s": 200, "spin": .5, "rot": -.4, "lamp": 0},
  {"type": "chapter", "n": "DANGER 1", "text": "NUAGES D'ACIDE", "dur": .9},
  {"type": "counter", "label": "ALTITUDE", "from": 70, "to": 45, "unit": "km", "x": .06, "y": .12, "t0": r(a, 12.9), "t1": 1.2},
  {"type": "pill", "text": "ACIDE SULFURIQUE", "tone": "red", "size": 42, "x": .06, "y": .3, "t0": r(a, 16.4)},
  {"type": "label", "text": "comme une batterie de voiture", "size": 52, "x": .5, "y": .62, "t0": r(a, 17.76), "dur": 1.8},
  {"type": "loading", "text": "PARAPLUIE : FONTE…", "to": 1, "t1": 1.2, "tone": "red", "x": .5, "y": .72, "t0": r(a, 19.64), "dur": 2.4},
  {"type": "stamp", "text": "FONDU", "x": .5, "y": .56, "rot": .1, "size": 130, "t0": r(a, 21.0), "dur": 1.1}],
  {"zoomFrom": 1.0, "zoomTo": 1.1, "shake": 3}))
# 5 heat 22.2-30.0
a, b = 22.2, 30.0
S.append(sh(a, b, [
  {"type": "surface", "kind": "venus", "heat": 2.4, "rocks": True},
  {"type": "astronaut", "x": 760, "y": 1330, "s": 190, "rot": .6, "lamp": .4},
  {"type": "chapter", "n": "DANGER 2", "text": "LA CHALEUR", "dur": .9},
  {"type": "thermo", "from": 20, "to": 470, "max": 500, "label": "TEMPÉRATURE AU SOL", "x": .13, "y": .56, "t0": r(a, 22.7), "t1": 1.5},
  {"type": "pill", "text": "PLUS CHAUD QUE MERCURE", "tone": "red", "size": 38, "x": .06, "y": .15, "t0": r(a, 24.6)},
  {"type": "label", "text": "le plomb fond à 327 °C", "tone": "yellow", "size": 56, "x": .5, "y": .66, "t0": r(a, 25.36), "dur": 2.2},
  {"type": "melt", "x": .5, "y": .79, "t0": r(a, 27.6)},
  {"type": "stamp", "text": "FLAQUE", "x": .5, "y": .55, "rot": -.1, "size": 120, "t0": r(a, 28.9)}],
  {"zoomFrom": 1.0, "zoomTo": 1.07, "fy": .6}))
# 6 pressure 30.0-37.0
a, b = 30.0, 37.0
S.append(sh(a, b, [
  {"type": "descent", "sky": ["#b06a22", "#4a2208"], "cols": ["#c98a40", "#a2621f", "#7a4212"], "speed": 380, "alpha": .85},
  {"type": "astronaut", "x": 250, "y": 1500, "s": 170, "spin": .25, "rot": .2, "lamp": .6},
  {"type": "chapter", "n": "DANGER 3", "text": "LA PRESSION", "dur": .9},
  {"type": "gauge", "label": "PRESSION (TERRE = 1×)", "to": 90, "max": 100, "unit": "×", "x": .5, "y": .33, "r": 220, "t0": r(a, 31.3), "t1": 1.0},
  {"type": "depth", "label": "MÊME PRESSION À 900 M SOUS L'EAU", "max": 1000, "to": 900, "x": .36, "y": .5, "t0": r(a, 33.4)}],
  {"zoomFrom": 1.04, "zoomTo": 1.0, "shake": 2}))
# 7 Venera 13 37.0-49.2
a, b = 37.0, 49.2
S.append(sh(a, b, [
  {"type": "surface", "kind": "venus", "heat": 2.6, "rocks": True},
  {"type": "probe", "x": 640, "y": 1330, "s": 330, "drop": 2.4, "t0": r(a, 39.4), "dead": r(a, 46.9) - r(a, 39.4), "cook": 7},
  {"type": "tag", "text": "VENERA 13 · 1ER MARS 1982 · VÉNUS", "x": .05, "y": .12, "t0": r(a, 40.6)},
  {"type": "timer", "label": "CONÇUE POUR TENIR", "to": 1920, "x": .07, "y": .2, "t0": r(a, 42.3), "t1": 1.1, "dur": 11},
  {"type": "timer", "label": "A RÉELLEMENT TENU", "to": 7620, "x": .07, "y": .33, "t0": r(a, 44.38), "t1": 1.6, "dead": 2.5, "dur": 10.5},
  {"type": "evidence", "src": "media/PIA00271.jpg", "credit": "NASA/JPL · radar Magellan", "tag": "SOL DE VÉNUS VU PAR RADAR NASA", "x": .5, "y": .66, "w": 700, "h": 700, "t0": r(a, 46.7), "dur": 2.4, "zoom": .1}],
  {"zoomFrom": 1.0, "zoomTo": 1.08, "fy": .78}))
# 8 survival game 49.2-60.4
a, b = 49.2, 60.4
S.append(sh(a, b, [
  {"type": "surface", "kind": "venus", "heat": 2.0, "rocks": True, "cols": ["#3a1a0a", "#a24e18", "#e0904a", "#8a3e14", "#62280c", "#3a1606"]},
  {"type": "astronaut", "x": 300, "y": 1500, "s": 170, "rot": .3, "lamp": .4},
  {"type": "options", "title": "TES OPTIONS", "sc": 1.9, "x": .07, "y": .2, "t0": 0, "items": [
      {"text": "PARACHUTE", "at": r(a, 50.74), "out": r(a, 52.5)},
      {"text": "COMBINAISON", "at": r(a, 53.2), "out": r(a, 54.9)}]},
  {"type": "stick", "x": .78, "y": .8, "s": 200, "pose": "panic", "label": "TOI", "t0": r(a, 50.7)},
  {"type": "stamp", "text": "1ER : ACIDE", "tone": "yellow", "x": .5, "y": .45, "rot": .06, "size": 100, "t0": r(a, 56.7), "dur": 1.5},
  {"type": "stamp", "text": "LE PLUS VIOLENT : LE SOL", "x": .5, "y": .56, "rot": -.07, "size": 70, "t0": r(a, 59.1)}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}))
# 9a twist 60.4-62.4
a, b = 60.4, 62.4
S.append(sh(a, b, [{"type": "big", "text": "MAIS…", "size": 300, "tone": "yellow", "t0": 0}], {"zoomFrom": 1.0, "zoomTo": 1.1}, trans="fade"))
a, b = 62.4, 66.9
S.append(sh(a, b, [
  {"type": "descent", "sky": ["#fbe6b6", "#e9c27a"], "cols": ["#fff1cf", "#f2d79a", "#e0b56c"], "speed": 60, "alpha": .95},
  {"type": "astronaut", "x": 740, "y": 1050, "s": 200, "rot": .1, "lamp": 0},
  {"type": "counter", "label": "ALTITUDE", "from": 50, "to": 50, "unit": "km", "x": .06, "y": .12, "t0": .2, "t1": .5},
  {"type": "gauge", "label": "PRESSION (TERRE = 1×)", "from": 90, "to": 1, "max": 100, "unit": "×", "x": .5, "y": .38, "r": 200, "t0": r(a, 62.92), "t1": 1.0},
  {"type": "big", "text": "30 À 70 °C", "size": 150, "x": .5, "y": .6, "t0": r(a, 64.8), "tone": "yellow"},
  {"type": "stamp", "text": "COMME SUR TERRE", "tone": "green", "x": .5, "y": .73, "rot": -.08, "size": 90, "t0": r(a, 66.0)}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}))
a, b = 66.9, 70.1
S.append(sh(a, b, [
  {"type": "descent", "sky": ["#fbe6b6", "#e9c27a"], "cols": ["#fff1cf", "#f2d79a", "#e0b56c"], "speed": 50, "alpha": .95},
  {"type": "airship", "x": 540, "y": 780, "s": 260},
  {"type": "pill", "text": "ÉTUDE NASA · PROJET HAVOC", "size": 40, "x": .06, "y": .13, "t0": .2},
  {"type": "label", "text": "concept, jamais construit", "size": 56, "x": .5, "y": .68, "tone": "red", "t0": r(a, 68.5), "underline": True}],
  {"zoomFrom": 1.1, "zoomTo": 1.0, "panFrom": 40, "panTo": -40}, trans="fade"))
# 10 closing: mirror of shot 1
a, b = 70.1, 81.34
S.append(sh(a, b, [
  {"type": "sun", "x": 60, "y": 1700, "r": 30},
  {"type": "planet", **VEN, "x": 640, "y": 1180, "r": 520, "light": 2.6, "spin": .03},
  {"type": "astronaut", "x": 330, "y": 860, "s": 70, "vx": -6, "rot": .35},
  {"type": "caption", "text": "la *jumelle* de la Terre", "y": .27, "size": 90, "t0": .1, "dur": 2.3},
  {"type": "label", "text": "à 50 km d'altitude seulement", "tone": "yellow", "size": 56, "x": .5, "y": .38, "t0": r(a, 72.7), "dur": 2.2},
  {"type": "label", "text": "sur quelle planète veux-tu mourir ?", "size": 52, "x": .5, "y": .18, "tone": "yellow", "t0": r(a, 75.3), "dur": 2.2},
  {"type": "label", "text": "dis-le en commentaire", "size": 62, "x": .5, "y": .2, "tone": "yellow", "t0": r(a, 77.48)},
  {"type": "big", "text": "ABONNE-TOI", "size": 150, "x": .5, "y": .29, "tone": "red", "t0": r(a, 78.74)}],
  {"zoomFrom": 1.12, "zoomTo": 1.0, "fx": .62}, trans="fade"))
json.dump({"width": W, "height": H, "fps": 30, "k": 1, "shots": S}, open("scene.json", "w"), indent=1, ensure_ascii=False)
print(len(S), "shots, ends", S[-1]["end"])
