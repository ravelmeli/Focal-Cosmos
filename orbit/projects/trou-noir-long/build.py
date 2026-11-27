import json
W, H = 1920, 1080
C1 = (94.95, 102.0); C2 = (204.4, 206.1)
D1, D2 = C1[1] - C1[0], C2[1] - C2[0]
def M(t):
    """temps de la voix d'origine -> temps de la voix recoupee"""
    if t <= C1[0]: return t
    if t <= C1[1]: return C1[0]
    if t <= C2[0]: return t - D1
    if t <= C2[1]: return C2[0] - D1
    return t - D1 - D2
S = []
class Shot:
    def __init__(self, a, b, cam=None, **kw):
        self.a, self.b = a, b; self.els = []; self.cam = cam or {"zoomFrom": 1.0, "zoomTo": 1.05}; self.kw = kw
    def add(self, t, **e):
        """t = temps d'origine de la voix ; None = debut du plan"""
        e["t0"] = round(0 if t is None else M(t) - M(self.a), 2)
        if "dur" in e and e.get("_orig_dur"): pass
        self.els.append(e); return self
    def world(self, **e): self.els.append(e); return self
    def done(self, last=None):
        d = {"start": round(M(self.a), 2), "end": round(M(self.b) if last is None else last, 2), "els": self.els, "cam": self.cam}
        d.update(self.kw); S.append(d)
def sh(a, b, **kw): return Shot(a, b, **kw)
BH = lambda x, y, r: {"type": "blackhole", "x": x, "y": y, "r": r}
AST = lambda x, y, s=70, **k: {"type": "astronaut", "x": x, "y": y, "s": s, **k}
# 1 hook
s = sh(0, 3.1, cam={"zoomFrom": 1, "zoomTo": 1.1, "fx": .65})
s.world(**BH(1280, 540, 210)); s.world(**AST(520, 540, 70, vx=18, rot=.3))
s.add(.34, type="you", x=545, y=520, lx=380, ly=330, text="TOI")
s.add(.3, type="title", text="TROUS NOIRS", sub="QU'EST-CE QUI TE TUE EN PREMIER ?", dur=2.7)
s.add(1.0, type="label", text="il avale tout ce qui passe ?", size=46, x=.5, y=.9, dur=2.0)
s.done()
# 2a Soleil
s = sh(3.1, 8.6); s.world(type="sun", x=520, y=540, r=170); s.world(type="planet", kind="earth", seed=2, x=1330, y=540, r=48, light=-1.6)
s.add(3.1, type="stamp", text="FAUX", x=.5, y=.2, rot=-.08, size=170, dur=2.2)
s.add(3.8, type="label", text="et si le Soleil devenait un trou noir ?", size=48, x=.5, y=.88, dur=4.5)
s.done()
# 2b trou noir a la place
s = sh(8.6, 12.8); s.world(**BH(520, 540, 52)); s.world(type="planet", kind="earth", seed=2, x=1330, y=540, r=48, light=-1.6)
s.add(9.0, type="label", text="même masse = même orbite", size=52, x=.5, y=.88, tone="yellow", dur=3.6)
s.add(10.0, type="pill", text="LA TERRE NE BOUGE PAS", size=38, tone="red", x=.4, y=.12)
s.done()
# 2c aspirateur
s = sh(12.8, 18.4); s.world(**BH(1450, 540, 120))
s.add(12.8, type="loading", text="ASPIRATION DE LA TERRE…", to=.04, t1=3.0, tone="red", x=.3, y=.5)
s.add(14.3, type="stamp", text="PAS UN ASPIRATEUR", x=.3, y=.7, rot=-.07, size=90)
s.add(15.5, type="label", text="un endroit d'où rien ne ressort", size=50, x=.5, y=.9, tone="yellow", dur=2.5)
s.done()
# 3 promesse
s = sh(18.4, 39.0, cam={"zoomFrom": 1.0, "zoomTo": 1.06, "fx": .7}); s.world(**BH(1400, 540, 240)); s.world(**AST(330, 880, 80, vx=10, rot=.4))
s.add(19.0, type="label", text="si tu t'approchais d'un trou noir…", size=50, x=.5, y=.1, dur=4.0)
s.add(20.3, type="big", text="LE PREMIER À TE TUER ?", size=100, x=.5, y=.2, tone="yellow", dur=3.4)
s.add(26.4, type="options", title="CE QUI T'ATTEND", sc=1.3, x=.06, y=.3, items=[
  {"text": "UNE CHALEUR EXTRÊME", "at": M(27.0) - M(18.4)}, {"text": "DES RAYONS X", "at": M(29.0) - M(18.4)},
  {"text": "UN ÉTIREMENT DU CORPS", "at": M(30.4) - M(18.4)}, {"text": "UN TEMPS QUI S'ARRÊTE", "at": M(31.7) - M(18.4)},
  {"text": "UN POINT DE NON-RETOUR", "at": M(33.0) - M(18.4)}], showAll=False, dur=12.6)
s.add(34.0, type="big", text="L'INTÉRIEUR ?", size=120, x=.72, y=.8, tone="yellow", dur=4.6)
s.done()
# 4 regle
s = sh(39.0, 48.6); s.world(**BH(1500, 540, 180))
s.add(39.8, type="label", text="UNE RÈGLE À RETENIR", size=54, x=.36, y=.14, tone="yellow", dur=7)
s.add(41.7, type="label", text="LE DANGER N'EST PAS", size=60, x=.36, y=.35, dur=5)
s.add(43.2, type="big", text="L'ATTRACTION", size=130, x=.36, y=.5, tone="red", dur=3.6)
s.add(45.0, type="label", text="C'EST", size=60, x=.36, y=.67, dur=2)
s.add(45.6, type="big", text="LA DISTANCE", size=130, x=.36, y=.8, tone="yellow", dur=3.0)
s.done()
# 5 taille Soleil
s = sh(48.6, 62.6); s.world(type="sun", x=560, y=560, r=250); s.world(**BH(1300, 560, 16))
s.add(48.9, type="label", text="quelle taille fait un trou noir ?", size=54, x=.5, y=.08, tone="yellow", dur=3.2)
s.add(54.5, type="label", text="LE SOLEIL", size=44, x=.29, y=.92, dur=6)
s.add(55.0, type="label", text="TROU NOIR DE MÊME MASSE", size=44, x=.68, y=.67, tone="red", dur=6)
s.add(57.0, type="counter", label="RAYON DU TROU NOIR", **{"from": 0, "to": 3, "unit": "km", "x": .66, "y": .3, "t1": 1.6})
s.add(60.2, type="label", text="≈ UNE PETITE VILLE", size=50, x=.68, y=.8, tone="yellow", dur=2.4)
s.done()
# 6 taille Terre
s = sh(62.6, 68.1); s.world(type="planet", kind="earth", seed=2, x=560, y=560, r=240, light=-1.6); s.world(**BH(1300, 560, 9))
s.add(63.2, type="counter", label="RAYON DU TROU NOIR (TERRE)", **{"from": 0, "to": 9, "unit": "mm", "x": .62, "y": .3, "t1": 1.6})
s.add(66.0, type="label", text="≈ UNE BILLE", size=60, x=.7, y=.7, tone="yellow", dur=2.0)
s.done()
# 7 horizon
s = sh(68.1, 83.9, cam={"zoomFrom": 1.0, "zoomTo": 1.08, "fx": .6}); s.world(**BH(1250, 540, 270)); s.world(**AST(420, 540, 75, vx=25, rot=.2))
s.add(68.2, type="label", text="L'HORIZON DES ÉVÉNEMENTS", size=58, x=.5, y=.08, tone="yellow", dur=3.5)
s.add(70.8, type="tag", text="D'APRÈS LA NASA", x=.04, y=.16)
s.add(74.8, type="pill", text="RIEN NE S'ÉCHAPPE · PAS MÊME LA LUMIÈRE", size=36, tone="red", x=.04, y=.24)
s.add(76.0, type="stamp", text="POINT DE NON-RETOUR", x=.28, y=.6, rot=-.07, size=80, dur=5)
s.add(79.9, type="label", text="tu peux le traverser sans rien sentir", size=48, x=.5, y=.92, dur=3.4)
s.done()
# 8 familles
s = sh(83.9, 94.95); s.world(**BH(1560, 540, 140))
s.add(83.9, type="label", text="où trouver un trou noir ?", size=54, x=.5, y=.08, tone="yellow", dur=2.8)
s.add(87.1, type="meters", title="MASSE (EN SOLEILS)", x=.36, y=.55, bars=[
  {"label": "PETITS", "level": .18, "note": "QUELQUES DIZAINES", "at": M(88.9) - M(83.9)},
  {"label": "GÉANTS", "level": 1.0, "note": "MILLIONS À MILLIARDS", "at": M(91.5) - M(83.9)}], dur=8)
s.done()
# 9 Gaia BH1
s = sh(102.0, 121.8); s.world(type="sun", x=1180, y=540, r=90); s.world(**BH(860, 560, 46))
s.add(102.2, type="tag", text="GAIA BH1 · ESA · 2022", x=.04, y=.07)
s.add(104.9, type="label", text="LE PLUS PROCHE QU'ON CONNAISSE", size=48, x=.5, y=.9, tone="yellow", dur=4)
s.add(108.8, type="counter", label="MASSE", **{"from": 0, "to": 10, "unit": "× LE SOLEIL", "x": .04, "y": .18, "t1": 1.4})
s.add(111.0, type="counter", label="DISTANCE", **{"from": 0, "to": 1560, "unit": "années-lumière", "x": .04, "y": .35, "t1": 2.2})
s.add(114.6, type="stamp", text="C'EST LOIN", tone="green", x=.74, y=.25, rot=.07, size=90, dur=3)
s.add(116.2, type="label", text="il fait osciller son étoile", size=46, x=.5, y=.9, dur=4.5)
s.done()
# 10 Sagittarius A* (rayons X)
s = sh(121.8, 134.3); s.world(**BH(300, 800, 60))
s.add(121.9, type="label", text="LE GÉANT DE NOTRE GALAXIE", size=50, x=.5, y=.08, tone="yellow", dur=3.2)
s.add(125.0, type="evidence", src="media/PIA16213.jpg", credit="NASA/JPL-Caltech · NuSTAR", tag="SAGITTARIUS A* · RAYONS X (NUSTAR)", x=.6, y=.52, w=800, h=600, dur=9.0, zoom=.08)
s.add(125.4, type="counter", label="MASSE", **{"from": 0, "to": 4, "unit": "millions de Soleils", "x": .04, "y": .3, "t1": 1.6})
s.add(127.6, type="counter", label="DISTANCE", **{"from": 0, "to": 26000, "unit": "années-lumière", "x": .04, "y": .5, "t1": 2.2})
s.add(131.8, type="stamp", text="TRÈS LOIN", tone="green", x=.18, y=.75, rot=-.07, size=80, dur=2.4)
s.done()
# 11 on s'approche
s = sh(134.3, 139.0, cam={"zoomFrom": 1.0, "zoomTo": 1.12, "fx": .7}); s.world(**BH(1350, 540, 190)); s.world(**AST(380, 540, 75, vx=40, rot=.3))
s.add(134.6, type="you", x=405, y=525, lx=260, ly=330, text="TOI")
s.add(136.9, type="label", text="voici ce qui t'attend, dans l'ordre", size=50, x=.5, y=.9, dur=2.0)
s.done()
# 12 chaleur
s = sh(139.0, 159.2); s.world(**BH(1330, 540, 220)); s.world(**AST(420, 760, 80, rot=.3, vx=15))
s.add(139.0, type="chapter", n="DANGER 1", text="LA CHALEUR", dur=1.0)
s.add(141.5, type="label", text="le trou noir est noir, pas ce qui l'entoure", size=46, x=.5, y=.08, dur=3.5)
s.add(146.6, type="label", text="le gaz tourne, s'écrase, forme un disque", size=46, x=.5, y=.08, tone="yellow", dur=3.2)
s.add(150.2, type="counter", label="TEMPÉRATURE DU DISQUE", **{"from": 0, "to": 12, "unit": "millions de °C", "x": .04, "y": .12, "t1": 2.4})
s.add(153.6, type="balance", left="SURFACE DU SOLEIL", right="DISQUE ×2000", tilt=.42, x=.2, y=.62)
s.add(156.5, type="label", text="il brille en rayons X", size=52, x=.5, y=.92, tone="red", dur=2.6)
s.done()
# 13 couronne
s = sh(159.2, 173.7); s.world(**BH(1330, 560, 200)); s.world(**AST(1000, 880, 70, rot=.2))
s.add(159.4, type="label", text="et ce n'est pas tout", size=52, x=.5, y=.08, dur=1.2)
s.add(160.3, type="tag", text="LA COURONNE", x=.04, y=.1)
s.add(164.2, type="pill", text="DES MILLIARDS DE DEGRÉS", size=44, tone="red", x=.04, y=.2)
s.add(167.0, type="scan", text="RAYONS X", dur=5.5)
s.add(169.3, type="stick", x=.2, y=.9, s=300, pose="panic", label="TOI", dur=4.2)
s.add(171.5, type="stamp", text="CUIT", x=.3, y=.45, rot=-.1, size=170, dur=2.2)
s.done()
# 14 jets
s = sh(173.7, 185.2); s.world(**BH(300, 800, 50))
s.add(173.7, type="chapter", n="DANGER 2", text="LES JETS", dur=1.0)
s.add(177.7, type="label", text="il ne se contente pas d'avaler : il recrache", size=46, x=.5, y=.08, tone="yellow", dur=3.2)
s.add(178.8, type="evidence", src="media/PIA13168.jpg", credit="NASA/JPL · illustration", tag="ILLUSTRATION · UN TROU NOIR ET SES JETS", x=.66, y=.52, w=780, h=624, dur=6.2, zoom=.07)
s.add(179.2, type="pill", text="≈ LA VITESSE DE LA LUMIÈRE", size=40, tone="red", x=.04, y=.3)
s.add(182.0, type="label", text="DEUX FAISCEAUX OPPOSÉS", size=44, x=.16, y=.6, tone="yellow", dur=3)
s.done()
# 15 3C 273
s = sh(185.2, 204.4); s.world(**BH(300, 800, 50))
s.add(185.4, type="tag", text="3C 273 · 1963 · LE PREMIER QUASAR", x=.04, y=.07)
s.add(188.1, type="evidence", src="media/PIA15414.jpg", credit="NASA/JPL · illustration", tag="ILLUSTRATION · UN QUASAR ET SON JET", x=.64, y=.52, w=870, h=580, dur=10.0, zoom=.07)
s.add(188.8, type="counter", label="DISTANCE", **{"from": 0, "to": 2.5, "decimals": 1, "unit": "milliards d'a.l.", "x": .04, "y": .2, "t1": 2.0})
s.add(193.1, type="counter", label="LONGUEUR DU JET (PLUS DE)", **{"from": 0, "to": 100000, "unit": "a.l.", "x": .04, "y": .42, "t1": 2.4})
s.add(195.8, type="label", text="la taille de notre galaxie", size=46, x=.22, y=.7, tone="yellow", dur=3)
s.add(198.4, type="pill", text="PARMI LES OBJETS LES PLUS BRILLANTS", size=38, x=.04, y=.8)
s.add(201.4, type="stamp", text="TERMINÉ", x=.18, y=.62, rot=-.08, size=120, dur=3)
s.done()
# 16 chance
s = sh(206.1, 213.7); s.world(**BH(300, 800, 50))
s.add(206.3, type="label", text="tu as de la chance : tu arrives de côté", size=48, x=.5, y=.08, tone="yellow", dur=4)
s.add(208.2, type="radar", label="TON APPROCHE", x=.5, y=.55, r=300, blips=[{"x": 0, "y": -.85, "label": "JET", "red": True}, {"x": 0, "y": .85, "label": "JET", "red": True}, {"x": -.75, "y": 0, "label": "TOI"}])
s.add(211.5, type="label", text="tu approches calmement de l'horizon", size=44, x=.5, y=.93, dur=2.2)
s.done()
# 17a marees
s = sh(213.7, 235.7); s.world(**BH(1680, 540, 130))
s.add(213.7, type="chapter", n="DANGER 3", text="LES MARÉES", dur=1.0)
s.add(217.2, type="stick", x=.3, y=.75, s=420, pose="stand", label="TOI", dur=18)
s.add(217.8, type="label", text="TÊTE : PLUS LOIN, PLUS FAIBLE", size=40, x=.5, y=.17, dur=5)
s.add(221.3, type="label", text="PIEDS : PLUS PRÈS, PLUS FORT", size=44, x=.5, y=.9, tone="red", dur=5)
s.add(223.8, type="pill", text="C'EST LA FORCE DE MARÉE", size=40, x=.55, y=.45, tone="red")
s.add(226.3, type="label", text="comme la Lune sur l'océan", size=44, x=.55, y=.55, tone="yellow", dur=3.2)
s.add(232.2, type="label", text="étiré vers le bas, comprimé sur les côtés", size=44, x=.64, y=.72, dur=3.5)
s.done()
# 17b spaghettification
s = sh(235.7, 241.9); s.world(**BH(1560, 540, 200))
s.add(235.9, type="label", text="Stephen Hawking a trouvé un mot", size=48, x=.4, y=.1, dur=2.1)
s.add(238.0, type="big", text="SPAGHETTIFICATION", size=130, x=.42, y=.45, tone="yellow", dur=3.8)
s.add(239.6, type="receipt", title="COMMANDE", items=[["TOI, ÉTIRÉ", "×1"]], total="SPAGHETTI", x=.82, y=.78, w=330, rot=.04)
s.done()
# 18 petit vs geant
s = sh(241.9, 268.5)
s.add(241.9, type="panels", titles=["PETIT TROU NOIR", "TROU NOIR GÉANT"], bg=["#2a0f14", "#0f1a2a"], stagger=.3, dur=26.6)
s.add(244.3, type="label", text="ÉTIRÉ AVANT L'HORIZON", size=46, x=.25, y=.4, tone="red", dur=7)
s.add(250.3, type="stamp", text="DÉCHIRÉ", x=.25, y=.62, rot=-.07, size=110, dur=14)
s.add(254.5, type="label", text="DOUX À L'HORIZON", size=46, x=.75, y=.4, tone="green", dur=7)
s.add(257.5, type="stamp", text="RIEN SENTI", tone="green", x=.75, y=.62, rot=.07, size=110, dur=11)
s.add(263.4, type="pill", text="PLUS MASSIF = GRAVITÉ PLUS DOUCE", size=40, tone="red", x=.3, y=.86)
s.done()
# 19 temps
s = sh(268.5, 285.9); s.world(**BH(1400, 540, 240)); s.world(**AST(760, 540, 75, rot=.2))
s.add(268.5, type="chapter", n="DANGER 4", text="LE TEMPS", dur=1.0)
s.add(273.0, type="label", text="près d'une forte gravité, le temps ralentit", size=46, x=.5, y=.08, dur=3.6)
s.add(277.4, type="label", text="POUR TOI : RIEN D'ANORMAL", size=44, x=.25, y=.85, tone="green", dur=2.4)
s.add(279.8, type="label", text="VU DE LOIN : TU RALENTIS", size=50, x=.25, y=.85, tone="yellow", dur=2.8)
s.add(282.8, type="stamp", text="TU TE FIGES", tone="yellow", x=.3, y=.3, rot=-.07, size=110, dur=3)
s.done()
# 20 simulation NASA
s = sh(285.9, 300.3); s.world(**BH(1400, 540, 240))
s.add(286.0, type="tag", text="SIMULATION · NASA", x=.04, y=.07)
s.add(287.9, type="timer", label="CAMÉRA · SON PROPRE TEMPS", to=10800, x=.04, y=.15, t1=4.0)
s.add(291.0, type="label", text="≈ 3 H · PRESQUE 2 TOURS EN CHEMIN", size=42, x=.3, y=.55, dur=3)
s.add(293.4, type="label", text="POUR L'OBSERVATEUR LOINTAIN : JAMAIS TOUT À FAIT", size=40, x=.5, y=.92, tone="red", dur=3.2)
s.add(297.0, type="stamp", text="ÉTOILES GELÉES", tone="yellow", x=.3, y=.5, rot=-.07, size=100, dur=3.3)
s.done()
# 21 M87*
s = sh(300.3, 332.3); s.world(**BH(260, 880, 50))
s.add(300.4, type="label", text="comment le sait-on, si personne n'y est allé ?", size=48, x=.5, y=.07, tone="yellow", dur=3.2)
s.add(303.6, type="label", text="ON L'A VU", size=70, x=.5, y=.07, tone="yellow", dur=3.5)
s.add(304.0, type="evidence", src="media/eht_m87.jpg", credit="EHT Collaboration (ESO, CC BY 4.0)", tag="M87* · 10 AVRIL 2019 · PREMIÈRE IMAGE D'UN TROU NOIR", x=.6, y=.52, w=1100, h=641, dur=27.5, zoom=.06)
s.add(312.9, type="counter", label="RADIOTÉLESCOPES", **{"from": 0, "to": 8, "unit": "", "x": .03, "y": .2, "t1": 1.0})
s.add(314.9, type="label", text="UN TÉLESCOPE GRAND COMME LA TERRE", size=34, x=.14, y=.42, tone="yellow", dur=4)
s.add(322.5, type="counter", label="DISTANCE", **{"from": 0, "to": 55, "unit": "millions d'a.l.", "x": .03, "y": .55, "t1": 2.0})
s.add(325.0, type="counter", label="MASSE", **{"from": 0, "to": 6.5, "decimals": 1, "unit": "milliards de Soleils", "x": .03, "y": .72, "t1": 2.0})
s.add(328.4, type="label", text="UN ANNEAU LUMINEUX AUTOUR D'UNE OMBRE NOIRE", size=36, x=.6, y=.93, dur=3.6)
s.done()
# 22 Sgr A*
s = sh(332.3, 339.6)
s.add(332.4, type="evidence", src="media/eht_sgra.jpg", credit="EHT Collaboration (ESO, CC BY 4.0)", tag="SAGITTARIUS A* · 2022 · LE TROU NOIR DE NOTRE GALAXIE", x=.5, y=.52, w=760, h=760, dur=7.0, zoom=.06)
s.add(332.5, type="label", text="2022 · LA MÊME ÉQUIPE", size=48, x=.5, y=.07, tone="yellow", dur=3.5)
s.done()
# 23 LIGO 2015 (deux trous noirs) + fusion
s = sh(339.6, 351.9); s.world(**BH(780, 560, 95)); s.world(**BH(1130, 540, 80))
s.add(339.7, type="label", text="et on les entend aussi", size=54, x=.5, y=.08, tone="yellow", dur=2.4)
s.add(342.6, type="tag", text="2015 · LIGO · ONDES GRAVITATIONNELLES", x=.04, y=.15)
s.add(349.1, type="pill", text="36 + 29 MASSES SOLAIRES", size=44, tone="red", x=.04, y=.25)
s.done()
s = sh(351.9, 359.8); s.world(**BH(960, 540, 130))
s.add(351.9, type="balance", left="36 + 29", right="62", tilt=.28, x=.22, y=.6)
s.add(355.2, type="counter", label="ÉNERGIE RAYONNÉE", **{"from": 0, "to": 3, "unit": "masses solaires", "x": .66, "y": .12, "t1": 1.6})
s.add(357.2, type="label", text="en une fraction de seconde", size=44, x=.62, y=.9, tone="yellow", dur=2.4)
s.done()
# 24 GW250114
s = sh(359.8, 380.7); s.world(**BH(1450, 540, 170))
s.add(360.0, type="tag", text="SEPTEMBRE 2025 · LIGO-VIRGO-KAGRA", x=.04, y=.07)
s.add(361.0, type="label", text="LE SIGNAL LE PLUS NET JAMAIS ENREGISTRÉ", size=44, x=.34, y=.18, tone="yellow", dur=4)
s.add(365.7, type="pill", text="≈ 34 + 32 MASSES SOLAIRES", size=42, tone="red", x=.04, y=.26)
s.add(369.6, type="label", text="UNE PRÉDICTION DE HAWKING · 1971", size=48, x=.3, y=.5, tone="yellow", dur=4.4)
s.add(374.0, type="label", text="APRÈS LA FUSION, L'AIRE DE L'HORIZON A AUGMENTÉ", size=40, x=.3, y=.6, dur=3.8)
s.add(376.8, type="stamp", text="CONFIRMÉ", tone="green", x=.3, y=.78, rot=-.06, size=130, dur=3.6)
s.add(377.3, type="label", text="plus grand que la somme des deux", size=42, x=.5, y=.95, tone="yellow", dur=3.3)
s.done()
# 25 jeu de survie
s = sh(380.7, 413.5); s.world(**BH(1500, 560, 220)); s.world(**AST(440, 880, 80, rot=.3, vx=10))
s.add(380.8, type="label", text="LE JEU DE LA SURVIE", size=56, x=.5, y=.08, tone="yellow", dur=3)
s.add(384.5, type="options", title="TES OPTIONS", sc=1.5, x=.04, y=.2, items=[
  {"text": "FUIR EN FUSÉE", "at": M(384.7) - M(380.7), "out": M(387.3) - M(380.7)},
  {"text": "ENVOYER UN ADIEU", "at": M(393.7) - M(380.7), "out": M(396.3) - M(380.7)},
  {"text": "GÉANT, SANS DISQUE", "at": M(402.8) - M(380.7)}])
s.add(384.8, type="stick", x=.62, y=.72, s=300, pose="panic", label="TOI", dur=28)
s.add(386.8, type="stamp", text="IMPOSSIBLE", x=.5, y=.5, rot=-.08, size=110, dur=2.8)
s.add(390.4, type="label", text="pas même la lumière", size=46, x=.5, y=.7, tone="yellow", dur=2)
s.add(396.3, type="stamp", text="IMPOSSIBLE", x=.5, y=.5, rot=.08, size=110, dur=3)
s.add(399.6, type="label", text="pour ceux qui te regardent : tu es figé", size=44, x=.3, y=.55, dur=3)
s.add(410.3, type="stamp", text="TU NE REVIENS JAMAIS", tone="yellow", x=.5, y=.5, rot=-.06, size=90, dur=3.2)
s.done()
# 26 verdict
s = sh(413.5, 433.1); s.world(**BH(1560, 540, 180))
s.add(413.6, type="label", text="VERDICT", size=70, x=.34, y=.12, tone="yellow", dur=3)
s.add(415.3, type="label", text="PETIT TROU NOIR  →  LES MARÉES", size=54, x=.34, y=.35, tone="red", dur=15)
s.add(417.8, type="label", text="GÉANT  →  CHALEUR ET RAYONS X", size=54, x=.34, y=.5, tone="yellow", dur=12.5)
s.add(424.4, type="label", text="L'INTÉRIEUR  →  PERSONNE NE SAIT", size=54, x=.34, y=.65, dur=6)
s.add(429.0, type="stamp", text="À SUIVRE", x=.34, y=.82, rot=-.06, size=110, dur=3.8)
s.add(428.7, type="tag", text="MÊME LA NASA : ON IGNORE CE QU'IL Y A DEDANS", x=.04, y=.92)
s.done()
# 27 retour a la regle
s = sh(433.1, 455.2); s.world(**BH(1560, 600, 50)); s.world(type="planet", kind="earth", seed=2, x=700, y=620, r=50, light=-1.6)
s.add(433.3, type="label", text="RETOUR À LA RÈGLE DU DÉBUT", size=52, x=.5, y=.08, tone="yellow", dur=3.4)
s.add(435.4, type="label", text="LE DANGER = LA DISTANCE, PAS L'ATTRACTION", size=44, x=.5, y=.18, dur=5.2)
s.add(441.3, type="pill", text="DE LOIN : LA MÊME GRAVITÉ QU'UNE ÉTOILE", size=38, x=.2, y=.3, tone="red")
s.add(445.8, type="counter", label="GAIA BH1", **{"from": 0, "to": 1560, "unit": "a.l.", "x": .04, "y": .45, "t1": 1.4})
s.add(449.3, type="stamp", text="NE MENACE PERSONNE", tone="green", x=.5, y=.7, rot=-.06, size=90, dur=3)
s.add(451.2, type="label", text="le danger, c'est de s'en approcher", size=52, x=.5, y=.92, tone="yellow", dur=3.2)
s.done()
# 28 final
last = M(473.69) + 0.8
s = sh(455.2, 463.5, cam={"zoomFrom": 1.12, "zoomTo": 1.0, "fx": .65}); s.world(**BH(1280, 540, 210)); s.world(**AST(520, 540, 70, vx=-12, rot=.3))
s.add(456.8, type="label", text="un trou noir n'est pas un monstre qui rôde", size=50, x=.5, y=.08, dur=3.6)
s.add(459.1, type="label", text="c'est un endroit sans retour", size=52, x=.5, y=.9, tone="yellow", dur=2.6)
s.add(461.0, type="label", text="on commence tout juste à le regarder en face", size=44, x=.5, y=.08, tone="yellow", dur=2.4)
s.done()
s = sh(463.5, 473.69, cam={"zoomFrom": 1.0, "zoomTo": 1.04}, trans="fade"); s.world(**BH(900, 930, 90)); s.world(**AST(650, 930, 60, rot=.3))
s.add(463.5, type="endcard", text="MERCI D'AVOIR REGARDÉ", ask="PETIT TROU NOIR OU GÉANT ?")
s.done(last)
json.dump({"width": W, "height": H, "fps": 30, "shots": S}, open("scene.json", "w"), indent=1, ensure_ascii=False)
print(len(S), "shots, ends", S[-1]["end"])
for i in range(1, len(S)):
    assert abs(S[i]["start"] - S[i-1]["end"]) < .02, (i, S[i-1]["end"], S[i]["start"])
