#!/usr/bin/env python3
"""Genere compositions/captions.html depuis assets/words.json (timestamps Whisper).
Usage: python3 build_captions.py <video_dir> <fin_en_secondes>"""
import json, sys, re, html
d, END = sys.argv[1], float(sys.argv[2])
raw = json.load(open(f"{d}/assets/words.json"))
FIX = {"voit": "vaut", "salle": "celle", "incenseur": "ascenseur", "levies": "levers", "Tira": "Tire"}
words = []
for x in raw:
    t = x["w"]
    if t.startswith("'") and words:
        words[-1]["w"] += t; words[-1]["e"] = x["e"]; continue
    if t.startswith("-") and words:
        words[-1]["w"] += t; words[-1]["e"] = x["e"]; continue
    if t in ("?", "%") and words:
        words[-1]["w"] += ("" if t == "?" else " ") + t; words[-1]["e"] = x["e"]; continue
    words.append(dict(x))
for w in words:
    w["w"] = FIX.get(w["w"], w["w"])
groups, cur = [], []
def flush():
    global cur
    if cur: groups.append(cur); cur = []
for i, w in enumerate(words):
    cur.append(w)
    nxt = words[i + 1] if i + 1 < len(words) else None
    end_sentence = bool(re.search(r"[.?!:]$", w["w"]))
    pause = nxt and nxt["s"] - w["e"] >= 0.18
    maxw = 3
    if end_sentence or pause or len(cur) >= maxw or (nxt and len(cur) == 2 and len(nxt["w"]) <= 3 and False):
        flush()
flush()
out = []
for gi, g in enumerate(groups):
    s = max(g[0]["s"], 0.1)
    if s >= END: break
    nxt_s = groups[gi + 1][0]["s"] if gi + 1 < len(groups) else None
    e = g[-1]["e"] + 0.12
    if nxt_s is not None and nxt_s - e < 0.2: e = nxt_s
    e = min(e, END)
    out.append((s, e, g))
KEY = re.compile(r"\d|%|orbite|tombe|gravit|flottent|f[ée]licitations|seconde|minutes|m[èe]tres|ISS", re.I)
def words_html(i, g):
    return " ".join(f'<span class="w{" k" if KEY.search(w["w"]) else ""}" id="w{i}_{j}">{html.escape(w["w"])}</span>' for j, w in enumerate(g))
els = "\n".join(
    f'      <div id="cg{i}" class="cg clip" data-start="{s:.3f}" data-duration="{e-s:.3f}"><span class="cb">{words_html(i, g)}</span></div>'
    for i, (s, e, g) in enumerate(out))
def tween(i, s, e, g):
    L = [f'    tl.fromTo("#cg{i} .cb", {{ opacity: 0, scale: 0.94 }}, {{ opacity: 1, scale: 1, duration: 0.09, ease: "power2.out" }}, {s:.3f});']
    for j, w in enumerate(g):
        ws = max(w["s"], s); we = min(w["e"], e)
        L.append(f'    tl.to("#w{i}_{j}", {{ scale: 1.08, duration: 0.08, ease: "power2.out" }}, {ws:.3f});')
        L.append(f'    tl.to("#w{i}_{j}", {{ scale: 1, duration: 0.12, ease: "power2.inOut" }}, {max(ws + 0.08, we):.3f});')
    L.append(f'    tl.to("#cg{i} .cb", {{ opacity: 0, duration: 0.06, ease: "power2.in" }}, {max(s, e-0.06):.3f});')
    return "\n".join(L)
tw = "\n".join(tween(i, s, e, g) for i, (s, e, g) in enumerate(out))
page = f'''<template>
  <style>
    #root {{ position: absolute; inset: 0; }}
    .cg {{ position: absolute; left: 0; right: 0; top: 1440px; height: 110px; display: flex; justify-content: center; align-items: center; }}
    .w {{ display: inline-block; margin: 0 .09em; }} .w.k {{ color: #fbbf24; }}
    .cb {{ display: inline-block; font-family: "Inter", sans-serif; font-weight: 700; font-size: 58px; line-height: 1; color: #fff;
      background: #04060c; border: 2px solid rgba(255,255,255,.22); padding: 20px 34px; white-space: nowrap; }}
  </style>
  <div id="root" data-composition-id="captions" data-width="1080" data-height="1920">
{els}
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
{tw}
    window.__timelines["captions"] = tl;
  </script>
</template>
'''
open(f"{d}/compositions/captions.html", "w").write(page)
print(len(out), "groupes")
for s, e, g in out: print(f"{s:6.2f}-{e:6.2f} " + " ".join(w["w"] for w in g))
