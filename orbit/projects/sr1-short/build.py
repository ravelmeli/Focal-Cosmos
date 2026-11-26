import json
W, H = 1080, 1920
MARS = {"kind": "mars", "seed": 5}
EAR = {"kind": "earth", "seed": 2}
def sh(a, b, els, cam=None, **kw):
    d = {"start": a, "end": b, "els": els}
    if cam: d["cam"] = cam
    d.update(kw); return d
def r(a, t): return round(t - a, 2)
S = []
# 1 hook 0-7.3
a, b = 0, 7.3
S.append(sh(a, b, [
  {"type": "sun", "x": 60, "y": 1750, "r": 30},
  {"type": "planet", **MARS, "x": 700, "y": 1500, "r": 560, "light": 2.6, "spin": .03},
  {"type": "rocket", "x": 260, "y": 800, "s": 220, "rot": .7, "vx": 30, "vy": 20},
  {"type": "title", "text": "NUCLÉAIRE", "sub": "DIRECTION MARS", "tx": 80, "ty": 330, "t0": .3, "dur": 1.4},
  {"type": "label", "text": "sa propre centrale nucléaire", "size": 54, "x": .5, "y": .15, "t0": 1.84, "dur": 2.0},
  {"type": "label", "text": "la NASA le prépare", "size": 62, "x": .5, "y": .15, "tone": "yellow", "t0": 4.8, "dur": 2.2}],
  {"zoomFrom": 1, "zoomTo": 1.08}))
# 2 SR-1 Freedom 7.3-15.7
a, b = 7.3, 15.7
S.append(sh(a, b, [
  {"type": "planet", **MARS, "x": 540, "y": 2000, "r": 900, "light": -1.6, "spin": .02},
  {"type": "rocket", "x": 540, "y": 900, "s": 300, "rot": 0, "vx": 0, "vy": 0},
  {"type": "tag", "text": "SR-1 FREEDOM · NASA", "x": .05, "y": .12, "t0": .24},
  {"type": "big", "text": "SR-1 FREEDOM", "size": 120, "x": .5, "y": .2, "tone": "yellow", "t0": r(a, 8.1), "dur": 2.4},
  {"type": "pill", "text": "LANCEMENT · FIN 2028", "size": 42, "x": .06, "y": .3, "t0": r(a, 10.4)},
  {"type": "pill", "text": "ARRIVÉE · ≈ 1 AN PLUS TARD", "size": 42, "tone": "red", "x": .06, "y": .38, "t0": r(a, 12.64)}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}))
# 3a how it works 15.7-22.9
a, b = 15.7, 22.9
S.append(sh(a, b, [
  {"type": "planet", **EAR, "x": 540, "y": 2150, "r": 900, "light": -1.6, "spin": .02},
  {"type": "label", "text": "comment ça marche ?", "size": 64, "x": .5, "y": .1, "tone": "yellow", "t0": .05, "dur": 1.3},
  {"type": "evidence", "src": "media/FSP.jpg", "credit": "NASA/GRC · Sara Lowthian-Hanna", "tag": "ESSAIS POUR UN RÉACTEUR À FISSION · NASA/GRC", "x": .5, "y": .3, "w": 940, "h": 627, "t0": r(a, 17.0), "dur": 5.9, "zoom": .06},
  {"type": "counter", "label": "PUISSANCE MINIMALE", "from": 0, "to": 20, "unit": "kW", "x": .06, "y": .55, "t0": r(a, 19.84), "t1": .8},
  {"type": "label", "text": "selon MIT Technology Review", "size": 40, "x": .5, "y": .68, "t0": r(a, 20.7), "dur": 2.0}],
  {"zoomFrom": 1.0, "zoomTo": 1.05}))
# 3b ion engines 22.9-30.2
a, b = 22.9, 30.2
S.append(sh(a, b, [
  {"type": "planet", **EAR, "x": 540, "y": 2150, "r": 900, "light": -1.6, "spin": .02},
  {"type": "evidence", "src": "media/PIA04668.jpg", "credit": "NASA/JPL · archive", "tag": "TEST D'UN MOTEUR IONIQUE · NASA/JPL (ARCHIVE)", "x": .5, "y": .3, "w": 900, "h": 675, "t0": .02, "dur": 7.2, "zoom": .06},
  {"type": "label", "text": "des moteurs ioniques", "size": 52, "x": .5, "y": .58, "t0": r(a, 24.28), "dur": 2.6},
  {"type": "label", "text": "poussent très doucement", "size": 52, "x": .5, "y": .64, "t0": r(a, 27.54), "dur": 1.6},
  {"type": "label", "text": "mais très longtemps", "size": 60, "x": .5, "y": .7, "tone": "yellow", "t0": r(a, 28.9), "dur": 1.3}],
  {"zoomFrom": 1.0, "zoomTo": 1.05}))
# 4 first 30.2-34.9
a, b = 30.2, 34.9
S.append(sh(a, b, [
  {"type": "planet", **MARS, "x": 540, "y": 2000, "r": 900, "light": -1.6, "spin": .02},
  {"type": "rocket", "x": 540, "y": 1000, "s": 260, "rot": 0, "vx": 0, "vy": 0},
  {"type": "stamp", "text": "PREMIÈRE", "tone": "green", "x": .5, "y": .15, "rot": -.07, "size": 130, "t0": r(a, 30.66)},
  {"type": "label", "text": "propulsion nucléaire électrique", "size": 46, "x": .5, "y": .28, "t0": r(a, 32.0), "dur": 2.7},
  {"type": "label", "text": "dans l'espace profond", "size": 54, "x": .5, "y": .34, "tone": "yellow", "t0": r(a, 33.26), "dur": 1.5}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}))
# 5 architecture 34.9-44.0
a, b = 34.9, 44.0
S.append(sh(a, b, [
  {"type": "planet", **EAR, "x": 540, "y": 2150, "r": 900, "light": -1.6, "spin": .02},
  {"type": "tag", "text": "NASA · ARCHITECTURE VERROUILLÉE", "x": .05, "y": .1, "t0": r(a, 35.18)},
  {"type": "doc", "org": "NASA", "title": "SR-1 FREEDOM", "fields": [["LANCEMENT", "FIN 2028"], ["RÉACTEUR", "INL (IDAHO)"], ["VAISSEAU", "LANTERIS SPACE SYSTEMS"]], "stamp": "VERROUILLÉE", "stampTone": "green", "x": .5, "y": .38, "w": 860, "h": 640, "t0": r(a, 35.5)}],
  {"zoomFrom": 1.0, "zoomTo": 1.05}))
# 6 realistic? 44.0-52.1
a, b = 44.0, 52.1
S.append(sh(a, b, [
  {"type": "planet", **MARS, "x": 540, "y": 2000, "r": 900, "light": -1.6, "spin": .02},
  {"type": "label", "text": "est-ce réaliste ?", "size": 66, "x": .5, "y": .1, "tone": "yellow", "t0": .04, "dur": 1.3},
  {"type": "label", "text": "certains experts", "size": 52, "x": .5, "y": .2, "t0": r(a, 45.32), "dur": 2.0},
  {"type": "stamp", "text": "EXTRÊMEMENT AMBITIEUX", "tone": "yellow", "x": .5, "y": .34, "rot": -.06, "size": 70, "t0": r(a, 46.98)},
  {"type": "loading", "text": "CONCEPTION : DES ANNÉES…", "to": .3, "t1": 2.4, "tone": "red", "x": .5, "y": .52, "t0": r(a, 49.1), "dur": 3.0}],
  {"zoomFrom": 1.0, "zoomTo": 1.05}))
# 7 why 52.1-59.2
a, b = 52.1, 59.2
S.append(sh(a, b, [
  {"type": "planet", **MARS, "x": 700, "y": 1500, "r": 560, "light": 2.6, "spin": .03},
  {"type": "rocket", "x": 260, "y": 800, "s": 220, "rot": .7, "vx": 30, "vy": 20},
  {"type": "label", "text": "alors, pourquoi tenter ?", "size": 56, "x": .5, "y": .1, "tone": "yellow", "t0": .1, "dur": 1.3},
  {"type": "pill", "text": "UN VAISSEAU QUI PRODUIT SON ÉNERGIE", "size": 36, "x": .05, "y": .2, "t0": r(a, 54.0)},
  {"type": "big", "text": "RACCOURCIR", "size": 140, "x": .5, "y": .3, "tone": "yellow", "t0": r(a, 57.46)},
  {"type": "label", "text": "le voyage vers Mars ?", "size": 58, "x": .5, "y": .38, "t0": r(a, 57.96), "dur": 1.2}],
  {"zoomFrom": 1.0, "zoomTo": 1.06}, trans="fade"))
# 8 closing 59.2-65.35
a, b = 59.2, 65.35
S.append(sh(a, b, [
  {"type": "sun", "x": 60, "y": 1750, "r": 30},
  {"type": "planet", **MARS, "x": 700, "y": 1500, "r": 560, "light": 2.6, "spin": .03},
  {"type": "rocket", "x": 260, "y": 800, "s": 220, "rot": .7, "vx": 30, "vy": 20},
  {"type": "label", "text": "sur quelle planète veux-tu mourir ?", "size": 52, "x": .5, "y": .2, "tone": "yellow", "t0": r(a, 59.4), "dur": 2.2},
  {"type": "label", "text": "dis-le en commentaire", "size": 62, "x": .5, "y": .2, "tone": "yellow", "t0": r(a, 61.78), "dur": 1.2},
  {"type": "big", "text": "ABONNE-TOI", "size": 150, "x": .5, "y": .29, "tone": "red", "t0": r(a, 63.08)}],
  {"zoomFrom": 1.1, "zoomTo": 1.0}, trans="fade"))
json.dump({"width": W, "height": H, "fps": 30, "k": 1, "shots": S}, open("scene.json", "w"), indent=1, ensure_ascii=False)
print(len(S), "shots, ends", S[-1]["end"])
