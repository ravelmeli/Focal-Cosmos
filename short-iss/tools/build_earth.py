#!/usr/bin/env python3
"""Textures Terre stylisees a partir de la carte NASA "Earth (A)" (NASA-3D-Resources, sans copyright).
Genere assets/tex/earth_day.jpg et assets/tex/earth_night.png (2048x1024, equirectangulaires).
Usage: python3 -I build_earth.py <Earth(A).jpg> <video_dir>"""
import sys, numpy as np
from PIL import Image, ImageFilter, ImageDraw
src, out = sys.argv[1], sys.argv[2]
W, H = 2048, 1024
im = Image.open(src).convert("RGB")
a = np.asarray(im.resize((W, H), Image.BICUBIC)).astype(np.float32) / 255
r, g, b = a[..., 0], a[..., 1], a[..., 2]
mx, mn = a.max(-1), a.min(-1)
sat = (mx - mn) / (mx + 1e-6)
# terre = teintes chaudes/vertes (r ou g domine nettement le bleu)
landness = np.clip(((np.maximum(r, g) - b) - 0.02) / 0.10, 0, 1)
land = np.asarray(Image.fromarray((landness * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.6))).astype(np.float32) / 255
land = np.clip((land - 0.5) * 6 + 0.5, 0, 1)
lat = (0.5 - (np.arange(H) + 0.5) / H) * np.pi
lon = ((np.arange(W) + 0.5) / W) * 2 * np.pi - np.pi
LON, LAT = np.meshgrid(lon, lat)
alat = np.abs(LAT) / (np.pi / 2)
# --- bruit de valeur pour les nuages (vectorise, periodique en longitude via 3D)
def hash3(x, y, z, s):
    h = (x * 374761393 + y * 668265263 + z * 2147483647 + s * 1274126177) & 0xFFFFFFFF
    h = ((h ^ (h >> 13)) * 1274126177) & 0xFFFFFFFF
    return ((h ^ (h >> 16)) & 0xFFFFFFFF) / 4294967296.0
def sm(t): return t * t * (3 - 2 * t)
def vnoise(x, y, z, s):
    xi, yi, zi = np.floor(x).astype(np.int64), np.floor(y).astype(np.int64), np.floor(z).astype(np.int64)
    xf, yf, zf = sm(x - xi), sm(y - yi), sm(z - zi)
    c = lambda i, j, k: hash3(xi + i, yi + j, zi + k, s)
    l = lambda p, q, t: p + (q - p) * t
    return l(l(l(c(0,0,0), c(1,0,0), xf), l(c(0,1,0), c(1,1,0), xf), yf), l(l(c(0,0,1), c(1,0,1), xf), l(c(0,1,1), c(1,1,1), xf), yf), zf)
def fbm(x, y, z, s, o=4):
    amp, tot, f = 0.5, 0, 1
    for i in range(o): tot = tot + amp * vnoise(x * f, y * f, z * f, s + i); f *= 2.05; amp *= 0.5
    return tot
X, Y, Z = np.cos(LAT) * np.cos(LON), np.sin(LAT), np.cos(LAT) * np.sin(LON)
# --- relief : luminance de la carte -> 3 bandes de vert/sable
lum = np.asarray(Image.fromarray((((r * 0.3 + g * 0.5 + b * 0.2)) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))).astype(np.float32) / 255
dry = np.clip((r - g) * 5 + 0.35, 0, 1)                      # orange/brun (relief sec) vs vert
dryq = np.floor(dry * 3) / 3
pal_g = np.array([74, 150, 80]) / 255.0; pal_s = np.array([212, 176, 104]) / 255.0
landcol = pal_g[None, None, :] * (1 - dryq[..., None]) + pal_s[None, None, :] * dryq[..., None]
landcol *= (0.82 + 0.3 * np.floor(lum * 4) / 4)[..., None]
# --- ocean : bandes selon la distance a la cote (flou de la terre)
near = np.asarray(Image.fromarray((land * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(12))).astype(np.float32) / 255
band = np.floor(np.clip(near * 2.2, 0, 1) * 3) / 3
deep = np.array([16, 70, 156]) / 255.0; shal = np.array([62, 156, 224]) / 255.0
ocean = deep[None, None, :] * (1 - band[..., None]) + shal[None, None, :] * band[..., None]
col = ocean * (1 - land[..., None]) + landcol * land[..., None]
# --- glace : calottes et Groenland
ice = np.clip((alat - 0.90) / 0.03, 0, 1) + (land * np.clip((-LAT - np.radians(62)) / np.radians(3), 0, 1))
gl = ((LAT > np.radians(60)) & (LAT < np.radians(84)) & (LON > np.radians(-74)) & (LON < np.radians(-12))).astype(np.float32)
gl = np.asarray(Image.fromarray((gl * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(5))).astype(np.float32) / 255
ice = np.clip(np.maximum(ice, gl * land), 0, 1)
col = col * (1 - ice[..., None]) + np.array([0.78, 0.84, 0.92])[None, None, :] * ice[..., None]
# --- nuages stylises (formes nettes, peu opaques)
cl = fbm(X * 6.0 + 50, Y * 6.0 + 50, Z * 6.0 + 50, 77, 4)
cm = np.clip((cl - 0.60) / 0.025, 0, 1) * 0.55
col = col * (1 - cm[..., None]) + np.array([0.97, 0.98, 1.0])[None, None, :] * cm[..., None]
Image.fromarray((np.clip(col, 0, 1) * 255).astype(np.uint8)).save(f"{out}/assets/tex/earth_day.jpg", quality=92)
# --- nuit : terres sombres + lumieres de villes (grandes agglomerations reelles + diffusion)
CITIES = [(40.7,-74,1.0),(34,-118.2,0.9),(41.9,-87.6,0.7),(19.4,-99.1,0.9),(-23.5,-46.6,1.0),(-22.9,-43.2,0.7),(-34.6,-58.4,0.8),(4.7,-74.1,0.5),(-12,-77,0.5),(51.5,-0.1,0.9),(48.9,2.35,0.8),(52.5,13.4,0.6),(40.4,-3.7,0.6),(41.9,12.5,0.5),(55.8,37.6,0.9),(41,29,0.8),(30,31.2,0.9),(6.5,3.4,0.8),(-4.3,15.3,0.5),(-26.2,28,0.6),(-1.3,36.8,0.4),(35.7,51.4,0.7),(24.9,67,0.8),(28.6,77.2,1.0),(19,72.8,1.0),(22.6,88.4,0.8),(23.8,90.4,0.9),(13.8,100.5,0.7),(-6.2,106.8,0.9),(14.6,121,0.8),(22.3,114.2,0.8),(31.2,121.5,1.0),(39.9,116.4,1.0),(37.6,127,0.9),(35.7,139.7,1.0),(34.7,135.5,0.8),(-33.9,151.2,0.6),(-37.8,145,0.5),(43.7,-79.4,0.6),(25.8,-80.2,0.6),(29.8,-95.4,0.6),(33.7,-84.4,0.5),(38.9,-77,0.6),(42.4,-71,0.5),(37.8,-122.4,0.6),(47.6,-122.3,0.4),(24.7,46.7,0.6),(33.3,44.4,0.6),(36.8,3,0.4),(33.6,-7.6,0.4),(9,38.7,0.4),(-33.4,-70.7,0.5),(10.5,-66.9,0.4),(50.5,30.5,0.5),(52.2,21,0.4),(59.3,18,0.3),(31.5,74.3,0.8),(13.1,80.3,0.7),(12.97,77.6,0.7),(10.8,106.7,0.7),(23.1,113.3,0.9),(29.6,106.5,0.7),(30.7,104,0.6),(30.6,114.3,0.7),(25,121.5,0.7),(1.35,103.8,0.5),(3.1,101.7,0.5),(38.7,-9.1,0.4),(45.5,9.2,0.6),(48.2,16.4,0.4),(38,23.7,0.4),(32.1,34.8,0.5),(25.2,55.3,0.5),(5.6,-0.2,0.5),(14.7,-17.5,0.3),(-8.8,13.2,0.3),(-6.8,39.3,0.4),(23.1,-82.4,0.3),(45.5,-73.6,0.4),(39.7,-105,0.3),(33.4,-112,0.4),(-36.8,174.8,0.3),(-32,115.9,0.3),(53.5,-2.2,0.5),(50.1,8.7,0.5),(51.4,7,0.6),(45.8,4.8,0.4),(41.4,2.2,0.5),(59.9,30.3,0.5),(56,37,0.4),(40.4,49.9,0.3),(41.3,69.2,0.4),(43.2,76.9,0.3),(35.2,129,0.5),(34.4,132.4,0.3),(26.2,127.7,0.2),(18.5,73.9,0.6),(17.4,78.5,0.7),(23,72.6,0.6),(26.8,80.9,0.6),(25.6,85.1,0.5),(21.2,72.8,0.5),(11,76.9,0.4),(6.9,79.9,0.3),(27.7,85.3,0.3),(34,71.5,0.4),(33.7,73,0.5),(35.7,51.4,0.5),(32.6,51.7,0.3),(36.3,59.6,0.3),(15.5,32.5,0.4),(-18.9,47.5,0.2),(-25.9,32.6,0.2),(-33.9,18.4,0.4),(-29.9,31,0.3),(0.3,32.6,0.3),(-1.9,30.1,0.2),(12,8.5,0.4),(7.4,3.9,0.5),(-4.4,-38.5,0.3),(-12.9,-38.5,0.4),(-30,-51.2,0.4),(-34.9,-56.2,0.3),(-0.2,-78.5,0.3),(10.5,-66.9,0.3),(14.6,-90.5,0.3),(18.5,-69.9,0.2),(44,-79.5,0.2),(41.5,-81.7,0.4),(42.3,-83,0.4),(39.3,-76.6,0.3),(36.2,-86.8,0.2),(32.8,-96.8,0.6),(30.3,-97.7,0.3),(35.1,-106.6,0.2),(36.2,-115.1,0.4),(32.7,-117.2,0.4),(45.5,-122.7,0.3),(39.1,-94.6,0.2),(44.9,-93.3,0.3),(38.6,-90.2,0.3)]
n = Image.new("L", (W, H), 0); d = ImageDraw.Draw(n)
rng = np.random.default_rng(11)
def px(la, lo): return ((lo + 180) / 360 * W, (90 - la) / 180 * H)
for la, lo, wgt in CITIES:
    cx, cy = px(la, lo)
    for _ in range(int(120 * wgt) + 25):
        rr = abs(rng.normal(0, 7 + 11 * wgt)); th = rng.uniform(0, 2 * np.pi)
        x, y = cx + rr * np.cos(th) * 0.9, cy + rr * np.sin(th)
        s = 0.7 + 1.0 * rng.random() * (0.6 + 0.4 * wgt)
        d.ellipse([x - s, y - s, x + s, y + s], fill=int(150 + 105 * rng.random()))
    s = 1.6 + 1.8 * wgt; d.ellipse([cx - s, cy - s, cx + s, cy + s], fill=255)
glow = n.filter(ImageFilter.GaussianBlur(3))
ln = np.asarray(n).astype(np.float32) / 255
lg = np.asarray(glow).astype(np.float32) / 255
lights = np.clip(ln + lg * 1.6, 0, 1) * land   # uniquement sur les terres
night = np.zeros((H, W, 3), np.float32)
night += np.array([4, 8, 26])[None, None, :] / 255.0
night += (land[..., None] * np.array([10, 20, 46])[None, None, :] / 255.0)
warm = np.array([255, 178, 78])[None, None, :] / 255.0
night = night + lights[..., None] * warm * 1.1
Image.fromarray((np.clip(night, 0, 1) * 255).astype(np.uint8)).save(f"{out}/assets/tex/earth_night.png")
print("ok")
