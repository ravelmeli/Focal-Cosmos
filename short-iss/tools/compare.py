#!/usr/bin/env python3
"""Compare des metriques simples entre la video de reference et la notre.
Usage: python3 -I compare.py ref.mp4 ours.mp4 [...]"""
import subprocess, sys, numpy as np
def frames(path, fps=4, w=108, h=192):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-vf", f"fps={fps},scale={w}:{h}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    raw = subprocess.run(cmd, capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, h, w, 3).astype(np.float32)
def loud(path):
    r = subprocess.run(["ffmpeg", "-i", path, "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
    l = [x for x in r.splitlines() if "I:" in x and "LUFS" in x]
    return l[-1].split("I:")[1].split("LUFS")[0].strip() if l else "?"
def dur(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path], capture_output=True, text=True).stdout)
print(f"{'video':32s} {'duree':>7s} {'activite':>9s} {'chg/min':>8s} {'lum':>6s} {'sat':>6s} {'LUFS':>7s}")
for p in sys.argv[1:]:
    f = frames(p); g = f.mean(-1)
    d = np.abs(np.diff(g, axis=0)).mean((1, 2))             # activite visuelle (4 fps)
    big = int((d > 6.0).sum())                              # fortes variations = changements de plan / mouvements marques
    mx, mn = f.max(-1), f.min(-1); sat = ((mx - mn) / (mx + 1e-6)).mean()
    D = dur(p)
    print(f"{p.split('/')[-1][:32]:32s} {D:7.1f} {d.mean():9.2f} {big / D * 60:8.1f} {g.mean():6.1f} {sat:6.2f} {loud(p):>7s}")
