#!/usr/bin/env python3
"""Ecrit les balises <audio> des effets sonores dans index.html (entre <!--SFX--> et <!--/SFX-->).
Sons : bibliotheque HyperFrames/Pixabay (media-use). Usage: python3 -I apply_sfx.py <video_dir>"""
import re, sys
d = sys.argv[1]
cuts = [float(x) for x in re.findall(r"CUTS\s*=\s*\[([^\]]*)\]", open(f"{d}/assets/pills.js").read())[0].split(",")]
tags = []
for i, c in enumerate(cuts):
    tags.append(f'      <audio id="whoosh{i+1}" src="assets/whoosh-short.mp3" data-start="{c-0.3:.2f}" data-duration="0.57" data-track-index="11" data-volume="0.32"></audio>')
for i, (t, f, v, dur) in enumerate([(6.0, "impact-bass-1", 0.22, 2.12), (10.9, "impact-bass-1", 0.2, 2.12), (27.4, "impact-bass-1", 0.2, 2.12), (40.3, "impact-bass-2", 0.26, 2.59), (56.4, "impact-bass-1", 0.24, 2.12)]):
    tags.append(f'      <audio id="impact{i+1}" src="assets/{f}.mp3" data-start="{t:.2f}" data-duration="{dur}" data-track-index="12" data-volume="{v}"></audio>')
tags.append('      <audio id="sparkle" src="assets/sparkle.mp3" data-start="67.20" data-duration="1.8" data-track-index="14" data-volume="0.28"></audio>')
tags.append('      <audio id="ping" src="assets/ping.mp3" data-start="70.60" data-duration="1.32" data-track-index="15" data-volume="0.3"></audio>')
tags.append('      <audio id="click" src="assets/click.mp3" data-start="77.40" data-duration="0.36" data-track-index="16" data-volume="0.5"></audio>')
tags.append('      <audio id="chime" src="assets/chime.mp3" data-start="77.55" data-duration="1.5" data-track-index="17" data-volume="0.25"></audio>')
block = "<!--SFX-->\n" + "\n".join(tags) + "\n      <!--/SFX-->"
p = f"{d}/index.html"; s = open(p).read()
if "<!--SFX-->" in s: s = re.sub(r"<!--SFX-->.*?<!--/SFX-->", block, s, flags=re.S)
else: s = s.replace("<!--WHOOSH-->", block)
open(p, "w").write(s); print(len(tags), "balises audio")
