// Kit d'overlays "Orbit" pour les Shorts en 3D : tout est une fonction du temps (deterministe), dessine en DOM.
// Usage : const ov = createOverlays(hostElement, W, H, items); puis a chaque image : ov.update(t, { project })
// project(nom) -> [x, y] en pixels ecran du point 3D nomme (pour la fleche YOU).
// Types : title, caption, chapter, stamp, label, counter, you, flash.  Couleurs : y (jaune), r (rouge), g (vert).
const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const seg = (t, a, b) => clamp((t - a) / (b - a));
const eo = (t) => 1 - Math.pow(1 - clamp(t), 3);
const back = (t) => { t = clamp(t) - 1; return 1 + t * t * (2.7 * t + 1.7); };
const lerp = (a, b, k) => a + (b - a) * k;
const TONE = { y: "#FFC93C", r: "#FF3B30", g: "#4CFF8A", w: "#F3F5FA" };
const fmt = (v, dec) => { const s = (dec ? v.toFixed(dec).replace(".", ",") : String(Math.round(v))); return s.replace(/\B(?=(\d{3})+(?!\d))/g, " "); };
// *mot* = jaune, !mot! = rouge
const rich = (txt) => txt.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/\*(.+?)\*/g, '<span style="color:#FFC93C">$1</span>').replace(/!(.+?)!/g, '<span style="color:#FF3B30">$1</span>');

export function createOverlays(host, W, H, items) {
  const K = W / 1080;                       // 1.0 pour 1080 de large
  const els = items.map((it) => {
    const d = document.createElement("div"); d.className = "ov ov-" + it.type; d.style.opacity = "0"; host.appendChild(d);
    const o = { it, d };
    if (it.type === "title") d.innerHTML = `<div class="tt">${it.text}</div><div class="tu"></div><div class="ts">${it.sub || ""}</div>`;
    else if (it.type === "caption") d.innerHTML = `<div class="ci">${rich(it.text.toUpperCase())}</div>`;
    else if (it.type === "chapter") d.innerHTML = `<div class="chc"></div><div class="cht"><div class="chn">${it.n || ""}</div><div class="chx">${it.text}</div></div>`;
    else if (it.type === "stamp") d.innerHTML = `<div class="si" style="color:${TONE[it.tone || "r"]};border-color:${TONE[it.tone || "r"]}">${it.text}</div>`;
    else if (it.type === "label") d.innerHTML = `<div class="li" style="color:${TONE[it.tone || "w"]}">${rich(it.text.toUpperCase())}</div><div class="lu"></div>`;
    else if (it.type === "counter") d.innerHTML = `<div class="cl">${it.label}</div><div class="cv"><span class="cn">0</span><span class="cu">${it.unit || ""}</span></div>`;
    else if (it.type === "you") d.innerHTML = `<svg class="ys" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}"><path class="yp" pathLength="1" fill="none" stroke="#FF3B30" stroke-width="${9 * K}" stroke-linecap="round"/><polygon class="yh" fill="#FF3B30"/></svg><div class="yt">${it.text || "TOI"}</div>`;
    else if (it.type === "flash") { d.style.background = "#fff"; d.style.inset = "0"; }
    return o;
  });
  function update(t, ctx) {
    for (const o of els) {
      const it = o.it, d = o.d, lt = t - it.t0, dur = it.dur ?? 99;
      if (lt < 0 || lt > dur + 0.45 || (it.type !== "chapter" && lt > dur)) { d.style.opacity = "0"; continue; }
      const aIn = seg(lt, 0, 0.18), aOut = 1 - seg(lt, dur - 0.2, dur);
      switch (it.type) {
        case "title": d.style.opacity = String(aIn * aOut); d.style.transform = `translateY(${(1 - eo(seg(lt, 0, 0.4))) * -30 * K}px)`; break;
        case "caption": { const s = 0.86 + 0.14 * back(seg(lt, 0, 0.28)); d.style.opacity = String(aIn * aOut); d.firstChild.style.transform = `scale(${s})`; if (it.y != null) d.style.top = it.y * 100 + "%"; break; }
        case "chapter": {
          const open = eo(seg(lt, 0, 0.3)), close = seg(lt, dur, dur + 0.35), r = open - close * close;
          d.style.opacity = r > 0.001 ? "1" : "0"; const c = d.querySelector(".chc"); c.style.transform = `translate(-50%,-50%) scale(${Math.max(0, r)})`;
          const tx = d.querySelector(".cht"); tx.style.opacity = String(clamp((r - 0.55) * 4)); tx.style.transform = `translate(-50%,-50%) scale(${0.92 + 0.08 * back(seg(lt, 0.25, 0.55))})`; break; }
        case "stamp": { const s = lerp(2.4, 1, eo(seg(lt, 0, 0.22))), a = seg(lt, 0, 0.1) * aOut; d.style.opacity = String(a); d.style.left = it.x * 100 + "%"; d.style.top = it.y * 100 + "%"; d.style.transform = `translate(-50%,-50%) rotate(${it.rot ?? -0.12}rad) scale(${s})`; break; }
        case "label": { d.style.opacity = String(seg(lt, 0, 0.25) * aOut); d.style.left = it.x * 100 + "%"; d.style.top = it.y * 100 + "%"; const u = d.querySelector(".lu"); u.style.width = (it.underline === false ? 0 : 100 * eo(seg(lt, 0.15, 0.6))) + "%"; break; }
        case "counter": {
          d.style.opacity = String(aIn * aOut); d.style.left = it.x * 100 + "%"; d.style.top = it.y * 100 + "%";
          const k = eo(seg(lt, it.t1 != null ? 0 : 0, it.run ?? 2)), v = lerp(it.from, it.to, k), n = d.querySelector(".cn"); const txt = fmt(v, it.decimals || 0); if (n.textContent !== txt) n.textContent = txt;
          n.style.color = (it.redAbove != null && v >= it.redAbove) ? TONE.r : TONE.w; break; }
        case "you": {
          const p = eo(seg(lt, 0, 0.5)), out = aOut; d.style.opacity = String(out);
          const tgt = ctx.project(it.target), lx = it.lx * W, ly = it.ly * H; const ax = tgt[0], ay = tgt[1];
          const cx = lx + (ax - lx) * 0.1 + 120 * K, cy = ly - 150 * K + (ay - ly) * 0.3;
          const path = d.querySelector(".yp"); path.setAttribute("d", `M ${lx} ${ly - 40 * K} Q ${cx} ${cy} ${ax} ${ay}`); path.style.strokeDasharray = "1"; path.style.strokeDashoffset = String(1 - p);
          const ang = Math.atan2(ay - cy, ax - cx), hs = 34 * K, pts = [[ax, ay], [ax - hs * Math.cos(ang - 0.45), ay - hs * Math.sin(ang - 0.45)], [ax - hs * Math.cos(ang + 0.45), ay - hs * Math.sin(ang + 0.45)]];
          d.querySelector(".yh").setAttribute("points", pts.map((q) => q.join(",")).join(" ")); d.querySelector(".yh").style.opacity = String(p > 0.85 ? 1 : 0);
          const yt = d.querySelector(".yt"); yt.style.left = lx + "px"; yt.style.top = ly + "px"; yt.style.transform = `translate(-50%,-50%) scale(${back(seg(lt, 0, 0.35))})`; break; }
        case "flash": d.style.opacity = String((it.a ?? 0.9) * (1 - seg(lt, 0, dur))); break;
      }
    }
  }
  return { update };
}
