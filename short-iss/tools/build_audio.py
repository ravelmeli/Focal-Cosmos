#!/usr/bin/env python3
"""Genere assets/ambiance.wav (nappe discrete). Les whoosh de coupe viennent de assets/whoosh-short.mp3
(bibliotheque HyperFrames, Pixabay), places dans index.html. Usage: python3 build_audio.py <video_dir>"""
import re, sys, wave
import numpy as np
d = sys.argv[1]; SR = 44100; DUR = 88.0
js = open(f"{d}/assets/pills.js").read()
pills = [float(x) for x in re.findall(r"t0:\s*([\d.]+)", js)]
cuts = [float(x) for x in re.findall(r"CUTS\s*=\s*\[([^\]]*)\]", js)[0].split(",")]
n = int(SR * DUR); t = np.arange(n) / SR
rng = np.random.default_rng(4)
# ambiance : drone grave + souffle filtre, tres discret
drone = 0.5*np.sin(2*np.pi*55*t) + 0.35*np.sin(2*np.pi*82.4*t + 1.3) + 0.2*np.sin(2*np.pi*110.5*t)
drone *= 0.7 + 0.3*np.sin(2*np.pi*0.07*t)
noise = rng.standard_normal(n); k = np.ones(400)/400; noise = np.convolve(noise, k, mode="same")*6
amb = 0.05*drone + 0.02*noise
fade = np.minimum(1, np.minimum(t/2.0, (DUR-t)/2.0)); amb *= fade
def save(name, x):
    x = np.clip(x, -1, 1); w = wave.open(f"{d}/assets/{name}", "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((x*32767).astype(np.int16).tobytes()); w.close()
save("ambiance.wav", amb)
print("ambiance.wav genere")
