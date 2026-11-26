import json
W, H = 1080, 1920
EAR = {"kind": "earth", "seed": 2}
MOON = {"kind": "moon", "seed": 7}
def sh(a, b, els, cam=None, **kw):
    d = {"start": a, "end": b, "els": els}
    if cam: d["cam"] = cam
    d.update(kw); return d
def r(a, t): return round(t - a, 2)
S = []
# 1 hook 0-7.6
a, b = 0, 7.6
S.append(sh(a, b, [
  {"type": "sun", "x": 60, "y": 1750, "r": 40},
  {"type": "planet", **EAR, "x": 640, "y": 1500, "r": 600, "light": 2.6, "spin": .03},
  {"type": "rocket", "x": 540, "y": 700, "s": 260, "rot": 0, "vx": 0, "vy": 40},
  {"type": "title", "text": "STARSHIP", "sub": "REVIENT D'ORBITE", "tx": 80, "ty": 330, "t0": .3, "dur": 1.4},
  {"type": "label", "text": "une fusée revient de l'espace", "size": 50, "x": .5, "y": .15, "t0": 1.9, "dur": 1.9},
  {"type": "label", "text": "dans les bras d'une tour", "size": 56, "x": .5, "y": .15, "t0": 3.5, "dur": 1.8},
  {"type": "big", "text": "14 NOV.", "size": 200, "x": .5, "y": .22, "tone": "yellow", "t0": r(a, 5.48), "dur": 2.0}],
  {"zoomFrom": 1, "zoomTo": 1.08}))
# 2 Starship, 15th flight 7.6-15.0
a, b = 7.6, 15.0
S.append(sh(a, b, [
  {"type": "planet", **EAR, "x": 540, "y": 2050, "r": 800, "light": -1.6, "spin": .02},
  {"type": "rocket", "x": 540, "y": 950, "s": 420, "rot": 0, "vx": 0, "vy": 0},
  {"type": "tag", "text": "STARSHIP · SPACEX", "x": .05, "y": .12, "t0": .1},
  {"type": "label", "text": "la plus grande fusée jamais construite", "size": 44, "x": .5, "y": .2, "t0": r(a, 9.16), "dur": 1.9},
  {"type": "tag", "text": "DÉCOLLAGE · 13 NOVEMBRE", "x": .05, "y": .26, "t0": r(a, 12.18)},
  {"type": "counter", "label": "NUMÉRO DU VOL", "from": 0, "to": 15, "unit": "", "x": .06, "y": .32, "t0": r(a, 13.5), "t1": .8}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}))
# 3 orbit 15.0-26.9
a, b = 15.0, 26.9
S.append(sh(a, b, [
  {"type": "planet", **EAR, "x": 540, "y": 1900, "r": 1000, "light": -1.6, "spin": .02},
  {"type": "tag", "text": "VAISSEAU · SHIP 42", "x": .05, "y": .06, "t0": .2},
  {"type": "counter", "label": "SATELLITES STARLINK", "from": 0, "to": 26, "unit": "", "x": .06, "y": .1, "t0": r(a, 17.1), "t1": 1.0},
  {"type": "counter", "label": "ALTITUDE", "from": 0, "to": 275, "unit": "km", "x": .06, "y": .19, "t0": r(a, 19.4), "t1": 1.2},
  {"type": "evidence", "src": "media/11_14_24_fuel_depot.jpg", "credit": "NASA/MSFC · image courtesy SpaceX", "tag": "ILLUSTRATION · STARSHIP EN ORBITE (CONCEPT)", "x": .5, "y": .56, "w": 940, "h": 492, "t0": r(a, 18.5), "dur": 4.0, "zoom": .08},
  {"type": "counter", "label": "TOURS DE LA TERRE", "from": 0, "to": 14, "unit": "", "x": .06, "y": .28, "t0": r(a, 23.1), "t1": 1.0},
  {"type": "timer", "label": "DURÉE EN ORBITE", "to": 81000, "x": .06, "y": .37, "t0": r(a, 24.8), "t1": 1.2}],
  {"zoomFrom": 1.0, "zoomTo": 1.05}))
# 4 catch 26.9-39.2
a, b = 26.9, 39.2
S.append(sh(a, b, [
  {"type": "planet", **EAR, "x": 540, "y": 2150, "r": 900, "light": -1.6, "spin": .02},
  {"type": "rocket", "x": 540, "y": 700, "s": 330, "rot": 1.45, "vx": 20, "vy": 0, "dur": r(a, 31.7)},
  {"type": "label", "text": "sorti des nuages à l'horizontale", "size": 46, "x": .5, "y": .13, "t0": r(a, 27.84), "dur": 2.0},
  {"type": "pill", "text": "3 MOTEURS RALLUMÉS", "tone": "red", "size": 42, "x": .06, "y": .2, "t0": r(a, 30.3), "dur": 4.0},
  {"type": "rocket", "x": 540, "y": 1000, "s": 330, "rot": 0, "vx": 0, "vy": 10, "t0": r(a, 31.74)},
  {"type": "label", "text": "il se redresse", "size": 56, "x": .5, "y": .13, "tone": "yellow", "t0": r(a, 31.74), "dur": 1.6},
  {"type": "you", "x": 540, "y": 1180, "lx": 540, "ly": 1500, "text": "LES BRAS DE LA TOUR", "t0": r(a, 33.2), "dur": 3.0},
  {"type": "flash", "t0": r(a, 34.66), "dur": .4, "a": .7},
  {"type": "stamp", "text": "ATTRAPÉ", "tone": "green", "x": .5, "y": .22, "rot": -.08, "size": 150, "t0": r(a, 34.7), "dur": 1.4},
  {"type": "big", "text": "1RE FOIS", "size": 190, "x": .5, "y": .31, "tone": "yellow", "t0": r(a, 35.66), "sub": "UN ÉTAGE SUPÉRIEUR RATTRAPÉ"}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}))
# 5 why 39.2-46.0
a, b = 39.2, 46.0
S.append(sh(a, b, [
  {"type": "planet", **EAR, "x": 540, "y": 2100, "r": 900, "light": -1.6, "spin": .02},
  {"type": "rocket", "x": 540, "y": 1050, "s": 300, "rot": 0, "vx": 0, "vy": 0},
  {"type": "label", "text": "pourquoi c'est important ?", "size": 54, "x": .5, "y": .12, "t0": .1, "dur": 1.2},
  {"type": "big", "text": "RÉUTILISABLE", "size": 130, "x": .5, "y": .24, "tone": "yellow", "t0": r(a, 40.54), "dur": 2.3},
  {"type": "label", "text": "le pari de SpaceX", "size": 56, "x": .5, "y": .36, "t0": r(a, 42.92), "dur": 3.0},
  {"type": "pill", "text": "OBJECTIF : BAISSER LE PRIX D'UN VOL", "tone": "red", "size": 38, "x": .06, "y": .44, "t0": r(a, 44.42)}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}))
# 6 booster 46.0-55.5
a, b = 46.0, 55.5
S.append(sh(a, b, [
  {"type": "planet", **EAR, "x": 540, "y": 2050, "r": 900, "light": -1.6, "spin": .02},
  {"type": "rocket", "x": 540, "y": 500, "s": 240, "rot": 0, "vx": 0, "vy": 70},
  {"type": "stamp", "text": "PAS PARFAIT", "x": .5, "y": .15, "rot": -.07, "size": 110, "t0": r(a, 46.3), "dur": 3.0},
  {"type": "label", "text": "le propulseur, lui, pas rattrapé", "size": 46, "x": .5, "y": .3, "t0": r(a, 48.0), "dur": 2.5},
  {"type": "loading", "text": "CAPTURE DU PROPULSEUR…", "to": .6, "t1": 1.0, "tone": "red", "x": .5, "y": .5, "t0": r(a, 50.58), "dur": 2.6},
  {"type": "stamp", "text": "ANNULÉE", "x": .5, "y": .62, "rot": .08, "size": 110, "t0": r(a, 51.9)},
  {"type": "label", "text": "point de secours : en mer", "size": 50, "x": .5, "y": .78, "tone": "yellow", "t0": r(a, 53.3), "dur": 2.0}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}))
# 7 Moon 55.5-62.9
a, b = 55.5, 62.9
S.append(sh(a, b, [
  {"type": "planet", **MOON, "x": 540, "y": 2000, "r": 1000, "light": -1.6, "spin": .01},
  {"type": "label", "text": "et la Lune ?", "size": 66, "x": .5, "y": .1, "tone": "yellow", "t0": .1, "dur": 1.2},
  {"type": "evidence", "src": "media/11_03_24_artemis_3_on_surface.jpg", "credit": "NASA/MSFC · image courtesy SpaceX", "tag": "ILLUSTRATION · STARSHIP HLS SUR LA LUNE (CONCEPT)", "x": .5, "y": .38, "w": 940, "h": 525, "t0": r(a, 56.73), "dur": 6.0, "zoom": .08},
  {"type": "pill", "text": "NASA · ARTEMIS · ALLUNISSAGE", "size": 40, "x": .06, "y": .64, "t0": r(a, 58.0)},
  {"type": "stamp", "text": "PROCHAINE ÉTAPE", "tone": "green", "x": .5, "y": .78, "rot": -.07, "size": 90, "t0": r(a, 61.5)}],
  {"zoomFrom": 1.0, "zoomTo": 1.05}, trans="fade"))
# 8 closing 62.9-68.97
a, b = 62.9, 68.97
S.append(sh(a, b, [
  {"type": "sun", "x": 60, "y": 1750, "r": 40},
  {"type": "planet", **EAR, "x": 640, "y": 1500, "r": 600, "light": 2.6, "spin": .03},
  {"type": "rocket", "x": 540, "y": 700, "s": 260, "rot": 0, "vx": 0, "vy": 40},
  {"type": "label", "text": "sur quelle planète veux-tu mourir ?", "size": 52, "x": .5, "y": .2, "tone": "yellow", "t0": r(a, 62.96), "dur": 2.2},
  {"type": "label", "text": "dis-le en commentaire", "size": 62, "x": .5, "y": .2, "tone": "yellow", "t0": r(a, 65.28), "dur": 1.1},
  {"type": "big", "text": "ABONNE-TOI", "size": 150, "x": .5, "y": .29, "tone": "red", "t0": r(a, 66.44)}],
  {"zoomFrom": 1.1, "zoomTo": 1.0}, trans="fade"))
json.dump({"width": W, "height": H, "fps": 30, "k": 1, "shots": S}, open("scene.json", "w"), indent=1, ensure_ascii=False)
print(len(S), "shots, ends", S[-1]["end"])
