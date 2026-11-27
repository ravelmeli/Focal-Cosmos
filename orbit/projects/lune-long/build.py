import json
W, H = 1920, 1080
C1 = (96.8, 99.15); D1 = C1[1] - C1[0]
def M(t):
    if t <= C1[0]: return t
    if t <= C1[1]: return C1[0]
    return t - D1
S = []
class Shot:
    def __init__(self, a, b, cam=None, **kw):
        self.a, self.b = a, b; self.els = []; self.cam = cam or {"zoomFrom": 1.0, "zoomTo": 1.05}; self.kw = kw
    def add(self, t, **e):
        e["t0"] = round(0 if t is None else M(t) - M(self.a), 2); self.els.append(e); return self
    def world(self, **e): self.els.append(e); return self
    def done(self, last=None):
        d = {"start": round(M(self.a), 2), "end": round(M(self.b) if last is None else last, 2), "els": self.els, "cam": self.cam}
        d.update(self.kw); S.append(d)
def sh(a, b, **kw): return Shot(a, b, **kw)
MOON = lambda x, y, r, **k: {"type": "planet", "kind": "moon", "seed": 7, "x": x, "y": y, "r": r, "light": k.get("light", -1.6), "spin": k.get("spin", .01)}
EARTH = lambda x, y, r: {"type": "planet", "kind": "earth", "seed": 2, "x": x, "y": y, "r": r, "light": -1.6, "spin": .02}
ROCKET = lambda x, y, s=110, **k: {"type": "rocket", "x": x, "y": y, "s": s, **k}
def ev(s, t, src, credit, tag, x, y, w, h, dur, zoom=.06):
    s.add(t, type="evidence", src="media/" + src, credit=credit, tag=tag, x=x, y=y, w=w, h=h, dur=dur, zoom=zoom)
# 1 hook
s = sh(0, 3.2, cam={"zoomFrom": 1, "zoomTo": 1.1, "fx": .65}); s.world(**MOON(1300, 560, 300)); s.world(**EARTH(760, 860, 60)); s.world(type="astronaut", x=600, y=640, s=70, vx=15, rot=.3)
s.add(.3, type="title", text="LA LUNE", sub="OÙ EN EST-ON, FIN 2026 ?", dur=2.7)
s.add(.5, type="label", text="cette année, l'humanité y est retournée ?", size=46, x=.5, y=.9, dur=2.6)
s.done()
# 2 faux
s = sh(3.2, 12.0); s.world(**MOON(1300, 560, 280)); s.world(**EARTH(330, 300, 70))
s.add(3.2, type="stamp", text="FAUX", x=.5, y=.25, rot=-.08, size=170, dur=2.4)
s.add(4.2, type="label", text="enfin, pas tout à fait", size=50, x=.5, y=.88, tone="yellow", dur=2.0)
s.add(8.0, type="pill", text="RECORD DE DISTANCE · VIEUX DE 56 ANS", size=40, tone="red", x=.04, y=.55)
s.done()
# 3 personne
s = sh(12.0, 21.6); s.world(**MOON(1350, 560, 320))
s.add(12.0, type="stamp", text="PERSONNE SUR LE SOL LUNAIRE", x=.35, y=.25, rot=-.06, size=80, dur=3.2)
s.add(15.4, type="big", text="DÉCEMBRE 1972", size=130, x=.35, y=.5, tone="yellow", dur=4.2)
s.add(19.4, type="counter", label="DEPUIS", **{"from": 0, "to": 54, "unit": "ans", "x": .04, "y": .7, "t1": 1.0})
s.done()
# 4 question + programme
s = sh(21.6, 39.7); s.world(**MOON(1500, 600, 300)); s.world(**EARTH(300, 260, 60))
s.add(22.0, type="label", text="alors, voici la vraie question", size=52, x=.5, y=.08, tone="yellow", dur=3)
s.add(23.5, type="big", text="OÙ EN EST-ON ?", size=120, x=.4, y=.22, dur=3.4)
s.add(26.0, type="options", title="AU PROGRAMME", sc=1.4, x=.05, y=.38, items=[
  {"text": "CE QUI S'EST PASSÉ EN 2026", "at": M(26.8) - M(21.6)}, {"text": "CE QUI A CHANGÉ DANS LES PLANS", "at": M(28.7) - M(21.6)},
  {"text": "QUAND ON Y MARCHE", "at": M(30.2) - M(21.6)}, {"text": "CE QUI PEUT TOUT FAIRE DÉRAILLER", "at": M(37.0) - M(21.6)}])
s.done()
# 5 regle
s = sh(39.7, 48.8); s.world(**MOON(1500, 700, 260))
s.add(39.8, type="label", text="UNE RÈGLE À RETENIR", size=56, x=.4, y=.12, tone="yellow", dur=7)
s.add(42.3, type="big", text="ALLER SUR LA LUNE", size=100, x=.4, y=.4, dur=6)
s.add(43.2, type="label", text="N'EST PAS LA MÊME CHOSE QUE", size=54, x=.4, y=.58, dur=5)
s.add(44.0, type="big", text="SE POSER SUR LA LUNE", size=100, x=.4, y=.75, tone="yellow", dur=4.5)
s.done()
# 6 pourquoi y retourner
s = sh(48.8, 68.9); s.world(**MOON(1450, 600, 280))
s.add(49.4, type="label", text="pourquoi y retourner ?", size=56, x=.4, y=.08, tone="yellow", dur=3)
s.add(52.4, type="counter", label="HUMAINS SUR LA LUNE", **{"from": 0, "to": 12, "unit": "", "x": .04, "y": .2, "t1": 1.0})
s.add(53.8, type="label", text="1969 – 1972", size=54, x=.17, y=.42, tone="yellow", dur=3)
s.add(56.7, type="pill", text="DES VISITES DE QUELQUES JOURS · À L'ÉQUATEUR", size=38, x=.04, y=.55)
s.add(62.4, type="big", text="RESTER", size=170, x=.3, y=.78, tone="yellow", dur=2.6)
s.add(66.8, type="stamp", text="PÔLE SUD", x=.3, y=.3, rot=-.07, size=110, dur=2.2)
s.done()
# 7 eau
s = sh(68.9, 91.8); s.world(**MOON(1450, 1000, 520, light=-2.4))
s.add(69.0, type="label", text="À CAUSE DE L'EAU", size=70, x=.4, y=.1, tone="yellow", dur=2.6)
s.add(71.2, type="label", text="des zones qui ne voient jamais le Soleil", size=46, x=.4, y=.2, dur=3.6)
s.add(74.9, type="tag", text="LCROSS · NASA · 2009 · CRATÈRE CABEUS", x=.04, y=.3)
s.add(77.0, type="pill", text="UN ÉTAGE DE FUSÉE S'Y ÉCRASE", size=38, tone="red", x=.04, y=.38)
s.add(80.6, type="stamp", text="DE L'EAU", tone="green", x=.3, y=.55, rot=-.07, size=120, dur=3.5)
s.add(82.7, type="thermo", **{"from": 20, "to": -173, "min": -200, "max": 40, "label": "CRATÈRES POLAIRES", "x": .62, "y": .78, "t1": 1.6})
s.add(87.6, type="label", text="la glace d'eau y reste piégée", size=46, x=.4, y=.92, tone="yellow", dur=3.4)
s.done()
# 8 deuxieme avantage
s = sh(91.8, 109.7); s.world(**MOON(1400, 1000, 520, light=-2.4)); s.world(type="sun", x=1850, y=120, r=60)
s.add(91.9, type="label", text="un deuxième avantage", size=56, x=.4, y=.1, tone="yellow", dur=2)
s.add(93.3, type="label", text="des crêtes presque toujours éclairées", size=50, x=.4, y=.22, dur=3.4)
s.add(99.3, type="pill", text="GLACE D'UN CÔTÉ · LUMIÈRE DE L'AUTRE", size=42, tone="red", x=.04, y=.42)
s.add(105.3, type="tag", text="LE CRATÈRE SHACKLETON · LE SITE MIS EN AVANT PAR LA NASA", x=.04, y=.55)
s.add(106.5, type="stamp", text="EMPLACEMENT DE RÊVE", tone="green", x=.35, y=.75, rot=-.06, size=90, dur=3)
s.done()
# 9 Artemis II decollage
s = sh(109.7, 127.8); s.world(**MOON(1500, 1000, 400, light=-2.4))
s.add(109.8, type="label", text="que s'est-il passé en avril ?", size=56, x=.5, y=.07, tone="yellow", dur=2.8)
ev(s, 115.4, "launch.jpg", "NASA/MAF · Michael DeMocker", "ARTEMIS II · DÉCOLLAGE · 1ER AVRIL 2026", .62, .5, 1000, 667, 12.0, .08)
s.add(115.9, type="counter", label="ASTRONAUTES À BORD", **{"from": 0, "to": 4, "unit": "", "x": .03, "y": .2, "t1": 1.0})
s.add(120.5, type="tag", text="CAPSULE ORION · « INTEGRITY »", x=.03, y=.4)
s.add(123.3, type="pill", text="1ER VOL HABITÉ AUTOUR DE LA LUNE DEPUIS 1972", size=34, tone="red", x=.03, y=.5)
s.done()
# 10 survol
s = sh(127.8, 143.7); s.world(**MOON(1500, 1000, 400, light=-2.4))
s.add(127.9, type="label", text="la capsule s'éloigne de la Terre", size=50, x=.5, y=.07, dur=2.8)
s.add(131.1, type="tag", text="6 AVRIL · DERRIÈRE LA LUNE", x=.03, y=.15)
ev(s, 131.6, "moon_flyby.jpg", "NASA/JSC", "ARTEMIS II · FACE VISIBLE ET FACE CACHÉE", .64, .5, 1000, 667, 11.5, .08)
s.add(134.0, type="counter", label="DISTANCE DE LA SURFACE", **{"from": 0, "to": 4067, "unit": "miles", "x": .03, "y": .28, "t1": 2.0})
s.add(138.0, type="pill", text="≈ 6 500 KM", size=44, tone="red", x=.03, y=.5)
s.add(140.2, type="label", text="3 H À PHOTOGRAPHIER", size=44, x=.17, y=.68, tone="yellow", dur=3)
s.done()
# 11 silence radio
s = sh(143.7, 160.8)
ev(s, 143.9, "eclipse.jpg", "NASA/JSC", "ARTEMIS II · ÉCLIPSE VUE DEPUIS ORION", .6, .5, 880, 660, 16.5, .06)
s.add(144.0, type="label", text="UN MOMENT TRÈS PARTICULIER", size=48, x=.5, y=.07, tone="yellow", dur=3)
s.add(146.5, type="timer", label="SANS CONTACT AVEC LA TERRE", to=2400, x=.03, y=.2, t1=3.2)
s.add(151.5, type="label", text="40 MIN DE SILENCE RADIO", size=40, x=.2, y=.55, tone="red", dur=4.4)
s.add(156.7, type="stamp", text="SIGNAL RETROUVÉ", tone="green", x=.18, y=.8, rot=-.06, size=80, dur=3.6)
s.done()
# 12 record
s = sh(160.8, 186.2); s.world(**MOON(1600, 1000, 300, light=-2.4))
s.add(161.0, type="label", text="LE PLUS IMPRESSIONNANT : LA DISTANCE", size=56, x=.5, y=.07, tone="yellow", dur=3)
s.add(165.0, type="counter", label="ARTEMIS II · DISTANCE DE LA TERRE", **{"from": 0, "to": 406771, "unit": "km", "x": .04, "y": .2, "t1": 3.2})
s.add(172.3, type="tag", text="ANCIEN RECORD · APOLLO 13 · AVRIL 1970", x=.04, y=.42)
s.add(177.0, type="counter", label="APOLLO 13", **{"from": 0, "to": 400000, "unit": "km", "x": .04, "y": .5, "t1": 2.0})
s.add(180.7, type="pill", text="+ DE 6 000 KM", size=50, tone="red", x=.04, y=.72)
s.add(183.0, type="stamp", text="RECORD DE 56 ANS BATTU", tone="green", x=.5, y=.5, rot=-.06, size=100, dur=3.2)
s.done()
# 13 comparaison distance
s = sh(186.2, 203.1); s.world(**EARTH(250, 540, 60)); s.world(**MOON(1100, 540, 45, light=-2.4)); s.world(**ROCKET(1450, 540, 90, rot=1.5, vx=0, vy=0))
s.add(186.3, type="label", text="DISTANCE MOYENNE TERRE – LUNE : ≈ 384 000 KM", size=44, x=.5, y=.15, dur=5)
s.add(191.8, type="label", text="LA CAPSULE : PLUS DE 20 000 KM AU-DELÀ", size=46, x=.5, y=.25, tone="yellow", dur=5)
s.add(197.7, type="label", text="là-bas, la Terre paraît toute petite", size=50, x=.5, y=.8, dur=2.2)
s.add(200.4, type="stamp", text="AUCUN HUMAIN PLUS LOIN", tone="green", x=.5, y=.55, rot=-.06, size=90, dur=2.6)
s.done()
# 14 amerrissage
s = sh(203.1, 214.3); s.world(**EARTH(300, 900, 200))
ev(s, 203.5, "splash.jpg", "NASA/KSC · Josh Valcarcel", "ARTEMIS II · AMERRISSAGE · 10 AVRIL", .5, .5, 560, 747, 10.5, .05)
s.add(205.9, type="tag", text="PACIFIQUE · AU LARGE DE SAN DIEGO", x=.04, y=.15)
s.add(209.1, type="stamp", text="MISSION RÉUSSIE", tone="green", x=.8, y=.4, rot=.06, size=90, dur=4)
s.add(211.0, type="counter", label="DURÉE DU VOL", **{"from": 0, "to": 10, "unit": "jours", "x": .04, "y": .6, "t1": 1.2})
s.done()
# 15 regle appliquee
s = sh(214.3, 230.5); s.world(**MOON(1400, 560, 300))
s.add(214.4, type="label", text="C'EST ICI QUE LA RÈGLE S'APPLIQUE", size=54, x=.4, y=.1, tone="yellow", dur=3)
s.add(218.1, type="stamp", text="PAS EN ORBITE LUNAIRE", x=.3, y=.3, rot=-.06, size=80, dur=2.6)
s.add(220.7, type="stamp", text="PAS POSÉE", x=.3, y=.5, rot=.06, size=110, dur=2.4)
s.add(223.5, type="label", text="UN TEST, AVEC DES HUMAINS À BORD", size=46, x=.4, y=.7, dur=3.4)
s.add(227.4, type="big", text="ON Y EST ALLÉS", size=90, x=.4, y=.84, tone="yellow", dur=1.3)
s.add(228.7, type="big", text="ON NE S'Y EST PAS POSÉS", size=70, x=.4, y=.84, tone="red", dur=1.8)
s.done()
# 16 changement de plan
s = sh(230.5, 259.1); s.world(**MOON(1500, 700, 300))
s.add(230.6, type="label", text="alors, quand se pose-t-on ?", size=56, x=.4, y=.08, tone="yellow", dur=3)
s.add(233.6, type="label", text="et là, une surprise", size=50, x=.4, y=.18, dur=1.3)
s.add(235.3, type="big", text="27 FÉVRIER 2026", size=110, x=.4, y=.35, tone="yellow", dur=4.2)
s.add(239.4, type="stamp", text="CHANGEMENT DE PLAN", x=.3, y=.55, rot=-.06, size=80, dur=4.5)
s.add(240.3, type="label", text="ARTEMIS III DEVAIT ÊTRE L'ALUNISSAGE", size=44, x=.4, y=.7, dur=4)
s.add(246.1, type="pill", text="LES CONSEILLERS DE SÉCURITÉ : RISQUES SUR L'ATTERRISSEUR", size=36, tone="red", x=.03, y=.78)
s.add(256.0, type="big", text="UN SAUT → DEUX MARCHES", size=80, x=.4, y=.9, tone="yellow", dur=3)
s.done()
# 17 Artemis III
s = sh(259.1, 285.5); s.world(**EARTH(1450, 900, 330)); s.world(**ROCKET(1000, 420, 100, rot=.7, vx=30, vy=20)); s.world(**ROCKET(1250, 330, 160, rot=.5, vx=20, vy=10))
s.add(259.2, type="tag", text="MARCHE N°1 · ARTEMIS III · 2027 (MILIEU D'ANNÉE)", x=.03, y=.07)
s.add(265.3, type="counter", label="ASTRONAUTES", **{"from": 0, "to": 4, "unit": "", "x": .03, "y": .18, "t1": 1.0})
s.add(266.5, type="stamp", text="PAS VERS LA LUNE", x=.25, y=.42, rot=-.06, size=80, dur=3)
s.add(267.7, type="label", text="en orbite autour de la Terre", size=46, x=.25, y=.55, dur=2.6)
s.add(273.3, type="pill", text="STARSHIP (SPACEX)  +  BLUE MOON (BLUE ORIGIN)", size=36, tone="red", x=.03, y=.65)
s.add(277.9, type="label", text="personne n'entre dans le Starship d'essai", size=40, x=.25, y=.78, dur=3)
s.add(281.2, type="loading", text="PARKING SPATIAL : MANŒUVRE…", to=.8, t1=2.6, tone="red", x=.2, y=.9)
s.done()
# 18 Artemis IV / V
s = sh(285.5, 306.9); s.world(**MOON(1500, 700, 300)); s.world(**ROCKET(1200, 300, 120, rot=.6, vx=20, vy=10))
s.add(285.6, type="tag", text="MARCHE N°2", x=.03, y=.07)
s.add(287.7, type="pill", text="ARTEMIS IV · DÉBUT 2028 · L'ALUNISSAGE", size=46, tone="red", x=.03, y=.22)
s.add(292.2, type="pill", text="ARTEMIS V · FIN 2028 · UN ALUNISSAGE PAR AN", size=42, x=.03, y=.34)
s.add(298.6, type="label", text="PAS EN 2026 · PAS EN 2027", size=54, x=.3, y=.6, dur=4)
s.add(302.8, type="stamp", text="AU PLUS TÔT : DÉBUT 2028", tone="yellow", x=.3, y=.78, rot=-.06, size=80, dur=3.8)
s.done()
# 19 Starship
s = sh(306.9, 335.6); s.world(**EARTH(1500, 1050, 420))
s.add(307.0, type="label", text="et Starship, où en est-il ?", size=56, x=.4, y=.07, tone="yellow", dur=2.6)
ev(s, 309.8, "hls_moon.jpg", "NASA/MSFC · image courtesy SpaceX", "ILLUSTRATION · STARSHIP HLS SUR LA LUNE (CONCEPT)", .28, .45, 780, 435, 6.0, .06)
s.add(313.8, type="label", text="novembre : une étape spectaculaire", size=44, x=.28, y=.75, dur=3)
s.add(317.3, type="counter", label="VOL N°", **{"from": 0, "to": 15, "unit": "", "x": .04, "y": .08, "t1": .8})
s.add(321.1, type="counter", label="SATELLITES STARLINK", **{"from": 0, "to": 26, "unit": "", "x": .04, "y": .22, "t1": 1.0})
s.add(324.5, type="counter", label="TOURS DE LA TERRE", **{"from": 0, "to": 14, "unit": "", "x": .04, "y": .36, "t1": 1.0})
s.add(328.1, type="you", x=1500, y=620, lx=1100, ly=900, text="LES BRAS DE LA TOUR", dur=3.5)
s.add(329.5, type="stamp", text="ATTRAPÉ", tone="green", x=.5, y=.35, rot=-.07, size=130, dur=1.8)
s.add(331.6, type="big", text="1RE FOIS", size=150, x=.5, y=.6, tone="yellow", dur=3.6)
s.done()
# 20 propulseur + incertitude
s = sh(335.6, 353.7); s.world(**EARTH(1500, 1050, 420))
s.add(335.7, type="stamp", text="PROPULSEUR : PAS RATTRAPÉ", x=.35, y=.2, rot=-.05, size=80, dur=3.5)
s.add(338.2, type="loading", text="CAPTURE DU PROPULSEUR…", to=.6, t1=1.6, tone="red", x=.3, y=.45)
s.add(339.8, type="stamp", text="ANNULÉE", x=.3, y=.58, rot=.06, size=100, dur=3.4)
s.add(340.8, type="label", text="point de secours : en mer", size=46, x=.35, y=.75, dur=2.5)
s.add(344.8, type="label", text="la question de fond reste ouverte", size=54, x=.5, y=.07, tone="yellow", dur=3)
s.add(345.6, type="pill", text="STARSHIP ET BLUE MOON : PRÊTS À TEMPS POUR ARTEMIS III ?", size=40, tone="red", x=.03, y=.88)
s.add(351.2, type="stamp", text="INCERTITUDE", tone="yellow", x=.7, y=.5, rot=-.06, size=100, dur=2.2)
s.done()
# 21 Moon Base
s = sh(353.7, 390.4); s.world(**MOON(1600, 1000, 300, light=-2.4))
s.add(353.8, type="label", text="et la base ?", size=60, x=.5, y=.07, tone="yellow", dur=2.4)
ev(s, 358.9, "moonbase.jpg", "NASA/HQ · illustration", "MOON BASE · ILLUSTRATION (NASA)", .6, .5, 1100, 619, 31.0, .06)
s.add(362.4, type="counter", label="PHASES DE CONSTRUCTION", **{"from": 0, "to": 3, "unit": "", "x": .02, "y": .2, "t1": .8})
s.add(365.7, type="label", text="phase 1 : surtout robotique", size=36, x=.14, y=.42, dur=4)
s.add(371.9, type="pill", text="MOON BASE 1 · BLUE MOON Mk 1 « ENDURANCE »", size=30, tone="red", x=.02, y=.55)
s.add(377.4, type="label", text="AUTOMNE 2026 AU PLUS TÔT · PEUT GLISSER", size=32, x=.14, y=.66, dur=6)
s.add(383.9, type="pill", text="MOON BASE 2 · GRIFFIN · ASTROBOTIC", size=30, x=.02, y=.74)
s.add(386.0, type="label", text="lancé par une Falcon Heavy", size=34, x=.14, y=.82, dur=3.5)
s.done()
# 22 CLPS, MoonFall, Isaacman
s = sh(390.4, 410.7); s.world(**MOON(1400, 1000, 520, light=-2.4))
s.add(390.5, type="counter", label="MISSIONS CONFIÉES (DEPUIS 2018)", **{"from": 0, "to": 14, "unit": "", "x": .04, "y": .1, "t1": 1.0})
s.add(394.0, type="counter", label="ENTREPRISES", **{"from": 0, "to": 5, "unit": "", "x": .04, "y": .27, "t1": .8})
s.add(397.6, type="tag", text="MOONFALL · 4 DRONES AU PÔLE SUD", x=.04, y=.46)
s.add(404.2, type="tag", text="JARED ISAACMAN · ADMINISTRATEUR DE LA NASA", x=.04, y=.58)
s.add(408.2, type="big", text="« MISSION PAR MISSION »", size=100, x=.5, y=.78, tone="yellow", dur=3)
s.done()
# 23 dates
s = sh(410.7, 424.7); s.world(**MOON(1500, 700, 300))
s.add(410.8, type="pill", text="≈ 2029 : SÉJOURS D'ÉQUIPAGE PLUS LONGS", size=44, x=.03, y=.2)
s.add(415.0, type="pill", text="≈ 2032 ET AU-DELÀ : BASE PERMANENTE", size=44, tone="red", x=.03, y=.32)
s.add(419.2, type="label", text="LES DATES CHANGENT D'UN DOCUMENT À L'AUTRE", size=44, x=.4, y=.55, dur=4.5)
s.add(421.5, type="stamp", text="INTENTIONS ≠ PROMESSES", tone="yellow", x=.35, y=.75, rot=-.05, size=90, dur=3)
s.done()
# 24 nucleaire
s = sh(424.7, 447.3); s.world(**MOON(1600, 1000, 300, light=-2.4))
s.add(424.8, type="label", text="avec quelle énergie ?", size=56, x=.5, y=.07, tone="yellow", dur=2.6)
s.add(427.5, type="counter", label="LA NUIT LUNAIRE DURE", **{"from": 0, "to": 14, "unit": "jours terrestres", "x": .03, "y": .2, "t1": 1.4})
ev(s, 435.4, "fsp.jpg", "NASA/GRC · Sara Lowthian-Hanna", "ESSAIS POUR UN RÉACTEUR À FISSION · NASA/GRC", .62, .5, 860, 573, 11.0, .05)
s.add(435.9, type="counter", label="RÉACTEUR LUNAIRE (APPEL DE 2025)", **{"from": 0, "to": 100, "unit": "kW minimum", "x": .03, "y": .42, "t1": 1.6})
s.add(441.0, type="pill", text="OBJECTIF ≈ 2030", size=44, tone="red", x=.03, y=.65)
s.add(444.0, type="label", text="un petit réacteur n'a pas besoin du Soleil", size=36, x=.62, y=.9, tone="yellow", dur=3)
s.done()
# 25 derapage
s = sh(447.3, 475.6); s.world(**MOON(1500, 700, 300))
s.add(447.4, type="label", text="qu'est-ce qui peut déraper ?", size=60, x=.4, y=.08, tone="yellow", dur=3.8)
s.add(451.4, type="label", text="TROIS RISQUES · SANS RIEN INVENTER", size=44, x=.4, y=.2, dur=2.4)
s.add(453.4, type="options", title="CE QUI PEUT DÉRAPER", sc=1.5, x=.04, y=.32, items=[
  {"text": "L'ATTERRISSEUR", "at": M(453.5) - M(447.3)}, {"text": "LES RETARDS", "at": M(459.0) - M(447.3)}, {"text": "LE RYTHME", "at": M(468.6) - M(447.3)}])
s.add(454.9, type="label", text="il a déjà fait changer le plan", size=40, x=.4, y=.72, dur=3.8)
s.add(464.6, type="label", text="un calendrier coupé en deux : rarement bon signe", size=40, x=.4, y=.72, dur=3.4)
s.add(470.2, type="label", text="UN ALUNISSAGE PAR AN : TRÈS AMBITIEUX", size=40, x=.4, y=.72, dur=5)
s.done()
# 26 a surveiller
s = sh(475.6, 490.5); s.world(**MOON(1500, 700, 300))
s.add(475.7, type="label", text="ce qu'on ignore encore", size=56, x=.4, y=.1, tone="yellow", dur=2.4)
s.add(477.8, type="options", title="À SURVEILLER L'AN PROCHAIN", sc=1.5, x=.04, y=.3, items=[
  {"text": "LA DATE D'ARTEMIS III", "at": M(478.0) - M(475.6)}, {"text": "L'ATTERRISSEUR D'ARTEMIS IV", "at": M(481.5) - M(475.6)}, {"text": "LE CALENDRIER DE MOON BASE", "at": M(485.5) - M(475.6)}])
s.done()
# 27 jeu de survie calendrier
s = sh(490.5, 514.9); s.world(**MOON(1500, 700, 300))
s.add(490.6, type="label", text="LE JEU DE LA SURVIE · VERSION CALENDRIER", size=48, x=.4, y=.07, tone="yellow", dur=3)
s.add(493.0, type="options", title="UN ATTERRISSAGE HABITÉ…", sc=1.5, x=.04, y=.22, items=[
  {"text": "EN 2026", "at": M(493.3) - M(490.5), "out": M(496.5) - M(490.5)},
  {"text": "EN 2027", "at": M(498.4) - M(490.5), "out": M(500.6) - M(490.5)},
  {"text": "DÉBUT 2028 · ARTEMIS IV", "at": M(502.7) - M(490.5)}])
s.add(496.4, type="stamp", text="IMPOSSIBLE", x=.3, y=.7, rot=-.06, size=100, dur=2)
s.add(500.4, type="stamp", text="IMPOSSIBLE", x=.3, y=.7, rot=.06, size=100, dur=2.3)
s.add(506.2, type="stamp", text="CIBLE OFFICIELLE", tone="green", x=.3, y=.7, rot=-.05, size=90, dur=3)
s.add(511.9, type="stamp", text="UNE FOURCHETTE · RISQUE DE GLISSER", tone="yellow", x=.35, y=.85, rot=-.04, size=60, dur=3)
s.done()
# 28 frise
s = sh(514.9, 537.1); s.world(**MOON(1500, 700, 300))
s.add(515.0, type="label", text="LA FRISE", size=60, x=.4, y=.07, tone="yellow", dur=2)
s.add(516.3, type="pill", text="AVRIL 2026 · ARTEMIS II · SURVOL HABITÉ", size=44, tone="red", x=.03, y=.22)
s.add(520.5, type="pill", text="2027 · ARTEMIS III · AMARRAGE EN ORBITE TERRESTRE", size=44, x=.03, y=.36)
s.add(525.1, type="pill", text="DÉBUT 2028 · ARTEMIS IV · 1ER ALUNISSAGE", size=44, tone="red", x=.03, y=.5)
s.add(532.0, type="pill", text="FIN 2028 · ARTEMIS V · UN ALUNISSAGE PAR AN", size=44, x=.03, y=.64)
s.done()
# 29 regle revue
s = sh(537.1, 559.5); s.world(**MOON(1600, 1000, 300, light=-2.4))
s.add(537.2, type="label", text="RETOUR À LA RÈGLE DU DÉBUT", size=56, x=.5, y=.07, tone="yellow", dur=2.6)
ev(s, 540.0, "rollout.jpg", "NASA/MSFC · Brandon Hancock", "ARTEMIS II · SLS SUR LE PAS DE TIR · JANVIER 2026", .45, .45, 940, 538, 10.0, .05)
s.add(543.1, type="label", text="ARTEMIS II : ON SAIT Y ALLER ET REVENIR", size=40, x=.45, y=.8, dur=3.6)
s.add(549.5, type="label", text="LA MARCHE LA PLUS DIFFICILE", size=48, x=.45, y=.9, tone="red", dur=2.4)
s.add(552.5, type="counter", label="SANS HUMAIN SUR LE SOL LUNAIRE", **{"from": 0, "to": 54, "unit": "ans", "x": .66, "y": .55, "t1": 1.0})
s.done()
# 30 puzzle
s = sh(559.5, 568.4); s.world(**MOON(1350, 540, 300)); s.world(**EARTH(330, 300, 70))
s.add(559.6, type="label", text="la Lune n'est pas encore revenue dans les mains des humains", size=44, x=.5, y=.08, dur=4)
s.add(563.0, type="label", text="les pièces du puzzle bougent toutes en même temps", size=46, x=.5, y=.9, tone="yellow", dur=4.4)
s.done()
# 31 closing
last = M(581.92) + 0.8
s = sh(568.4, 578.1, cam={"zoomFrom": 1.1, "zoomTo": 1.0, "fx": .65}); s.world(**MOON(1300, 600, 300)); s.world(**EARTH(760, 900, 60)); s.world(type="astronaut", x=600, y=700, s=70, vx=-10, rot=.3)
s.add(569.8, type="label", text="quelle année pour le prochain pas ?", size=52, x=.5, y=.08, tone="yellow", dur=4)
s.add(573.7, type="big", text="2028 ? 2029 ? PLUS TARD ?", size=100, x=.5, y=.22, dur=3.3)
s.add(576.7, type="label", text="dis-le en commentaire", size=60, x=.5, y=.9, tone="yellow", dur=2.4)
s.done()
s = sh(578.1, 581.92, cam={"zoomFrom": 1.0, "zoomTo": 1.04}, trans="fade"); s.world(**MOON(900, 960, 120)); s.world(**EARTH(560, 940, 50))
s.add(578.1, type="endcard", text="MERCI D'AVOIR REGARDÉ", ask="QUELLE ANNÉE POUR LE PROCHAIN PAS ?")
s.done(last)
json.dump({"width": W, "height": H, "fps": 30, "shots": S}, open("scene.json", "w"), indent=1, ensure_ascii=False)
print(len(S), "shots, ends", S[-1]["end"])
for i in range(1, len(S)):
    assert abs(S[i]["start"] - S[i-1]["end"]) < .02, (i, S[i-1]["end"], S[i]["start"])
