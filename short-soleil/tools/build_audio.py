#!/usr/bin/env python3
"""Genere assets/ambiance.wav : nappe spatiale evolutive (accord lent + souffle + scintillement), tres discrete sous la voix,
avec une montee progressive vers la chute finale (34 -> 50 s puis 55 -> 60 s). Les effets (whoosh, impacts, riser, sparkle) viennent de la
bibliotheque HyperFrames/Pixabay (voir tools/apply_sfx.py). Usage: python3 -I build_audio.py <video_dir>"""
import sys, wave
import numpy as np
d = sys.argv[1]; SR = 44100; DUR = 76.0
n = int(SR * DUR); t = np.arange(n) / SR
rng = np.random.default_rng(4)
def sm(x): x = np.clip(x, 0, 1); return x * x * (3 - 2 * x)
# accord lent (La mineur ouvert) avec derive de phase et ondulation lente
notes = [(55.0, 0.50), (82.4, 0.36), (110.0, 0.26), (130.8, 0.18), (164.8, 0.10)]
pad = np.zeros(n)
for k, (f, a) in enumerate(notes):
    lfo = 0.65 + 0.35 * np.sin(2 * np.pi * (0.05 + 0.017 * k) * t + k)
    pad += a * lfo * (np.sin(2 * np.pi * f * t + 0.3 * np.sin(2 * np.pi * 0.11 * t + k)) + 0.4 * np.sin(2 * np.pi * f * 1.004 * t))
# souffle (bruit filtre) qui "respire"
noise = rng.standard_normal(n); noise = np.convolve(noise, np.ones(500) / 500, mode="same") * 9
breath = noise * (0.5 + 0.5 * np.sin(2 * np.pi * 0.08 * t))
# scintillement tres haut, leger
shim = (np.sin(2 * np.pi * 1318.5 * t) * (0.5 + 0.5 * np.sin(2 * np.pi * 0.21 * t)) + 0.6 * np.sin(2 * np.pi * 1760 * t) * (0.5 + 0.5 * np.sin(2 * np.pi * 0.13 * t + 1))) * 0.012
base = 1.0 + 0.9 * sm((t - 8.0) / 18.9) * (1 - sm((t - 27.0) / 0.2))
dark = 1 - 0.55 * sm((t - 27.0) / 0.25) * (1 - sm((t - 54.4) / 0.6))
swell = base * dark + 0.5 * sm((t - 60.0) / 3.0) * (1 - sm((t - 66.0) / 3.0))
amb = (0.040 * pad + 0.016 * breath + shim) * swell
amb *= np.minimum(1, np.minimum(t / 2.0, (DUR - t) / 2.0))
amb = np.clip(amb, -1, 1)
w = wave.open(f"{d}/assets/ambiance.wav", "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((amb * 32767).astype(np.int16).tobytes()); w.close()
print("ambiance.wav genere, crete =", round(float(np.abs(amb).max()), 3))
