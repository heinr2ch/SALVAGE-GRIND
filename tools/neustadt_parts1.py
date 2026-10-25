# Neustadt Teil 1: Grafiken (Symbole, Emblem, Waschbär Paule, Stadtbild, Himmel)

EMBLEM_NS = """          <path d="M14 44 V30 h8 V44 M24 44 V20 h10 V44 M36 44 V26 h8 V44 M46 44 V34 h6 V44" fill="#1c3a4a" stroke="#7ee0c8" stroke-width="1.6" stroke-linejoin="round"/>
          <path d="M27 24 h4 M27 29 h4 M27 34 h4 M39 30 h2 M39 35 h2" stroke="#ffd27a" stroke-width="1.6"/>
          <path d="M12 44.5 H54" stroke="#7ee0c8" stroke-width="2" stroke-linecap="round"/>
          <path d="M29 20 V12 h10" stroke="#ffc94a" stroke-width="1.6" fill="none"/><path d="M37 12 v4" stroke="#ffc94a" stroke-width="1.2"/>"""

ICONS_NS = r'''const ICONS = {
  scrap: `<svg viewBox="0 0 40 40"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#13283a" stroke="#7ed957" stroke-width="1.6"/><path d="M8 20 L20 9 L32 20" fill="#2f8a4a" stroke="#1a4a28" stroke-width="1.4" stroke-linejoin="round"/><rect x="11" y="19" width="18" height="13" fill="#e8e2d0" stroke="#5a5448" stroke-width="1.2"/><rect x="14" y="22" width="5" height="4" fill="#ffd27a"/><rect x="22" y="23" width="4" height="9" fill="#7a5a3a"/></svg>`,
  cell: `<svg viewBox="0 0 40 40"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#13283a" stroke="#4aa8ff" stroke-width="1.6"/><rect x="8" y="12" width="24" height="20" fill="#dce6f0" stroke="#4a5a6a" stroke-width="1.2"/><path d="M7 12 h26 l-2 -5 h-22z" fill="#4aa8ff"/><path d="M7 12 q2.2 3 4.3 0 q2.2 3 4.3 0 q2.2 3 4.3 0 q2.2 3 4.3 0 q2.2 3 4.3 0 q2.2 3 4.3 0" fill="#ffffff" stroke="#4aa8ff" stroke-width=".8"/><rect x="11" y="19" width="10" height="8" fill="#9ad4ff"/><rect x="24" y="20" width="5" height="12" fill="#5a6a7a"/></svg>`,
  chip: `<svg viewBox="0 0 40 40"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#13283a" stroke="#6fb8ff" stroke-width="1.6"/><rect x="11" y="6" width="18" height="27" fill="#3a5a7a" stroke="#1a2a3a" stroke-width="1.2"/>${[0,1,2,3,4].map(r => [0,1,2].map(c => `<rect x="${13.5 + c * 5}" y="${9 + r * 4.6}" width="3.4" height="3" fill="${(r + c) % 3 ? "#9ad4ff" : "#ffd27a"}"/>`).join("")).join("")}<path d="M8 33 H32" stroke="#6fb8ff" stroke-width="1.6"/></svg>`,
  core: `<svg viewBox="0 0 40 40"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#13283a" stroke="#ff7a59" stroke-width="1.6"/><path d="M14 33 V8 l6 -4 l6 4 V33z" fill="#5a6a7a" stroke="#1a2a3a" stroke-width="1.2"/><path d="M20 4 V1.5" stroke="#ff7a59" stroke-width="1.2"/><circle cx="20" cy="1.8" r="1" fill="#ff7a59"/>${[0,1,2,3,4,5].map(r => `<rect x="16" y="${10 + r * 3.8}" width="8" height="2.2" fill="#9ad4ff" opacity=".9"/>`).join("")}<rect x="8" y="22" width="6" height="11" fill="#7a8a9a"/><rect x="26" y="18" width="6" height="15" fill="#7a8a9a"/></svg>`,
  crystal: `<svg viewBox="0 0 40 40"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#13283a" stroke="#ffc94a" stroke-width="1.6"/><path d="M10 7 H30 V20 Q30 30 20 34 Q10 30 10 20 Z" fill="#c9952e" stroke="#ffe39a" stroke-width="1.6"/><path d="M14 11 H26 V20 Q26 26 20 29 Q14 26 14 20 Z" fill="#2a5aa8"/><path d="M16 22 V16 l4 -3 l4 3 V22z" fill="#ffe39a"/><path d="M19 19 h2 v3 h-2z" fill="#2a5aa8"/></svg>`,
  relic: `<svg viewBox="0 0 40 40"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#13283a" stroke="#ffd34a" stroke-width="1.6"/><path d="M9 22 Q9 9 20 8 Q31 9 31 22 Z" fill="#ffd34a" stroke="#a87a10" stroke-width="1.3"/><path d="M14 20 Q14 12 20 11" stroke="#fff4c8" stroke-width="1.6" fill="none"/><path d="M20 8 V3" stroke="#a87a10" stroke-width="1.4"/><circle cx="20" cy="3" r="1.6" fill="#ffd34a"/><rect x="8" y="22" width="24" height="11" fill="#e8dcc0" stroke="#7a6a4a" stroke-width="1.2"/>${[0,1,2,3].map(i => `<rect x="${10.5 + i * 5.6}" y="24" width="2.4" height="8" fill="#a89a7a"/>`).join("")}</svg>`,
  beacon: `<svg viewBox="0 0 40 40"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#13283a" stroke="#c6f06b" stroke-width="1.8"/><rect x="9" y="5" width="22" height="24" rx="1.5" fill="#f4f0e4" stroke="#8a8470" stroke-width="1"/><path d="M12 10 h16 M12 14 h16 M12 18 h10" stroke="#9a9480" stroke-width="1.2"/><circle cx="25" cy="22" r="5.4" fill="#d9443a" opacity=".92"/><path d="M22.5 22 l2 2 l3.5 -4" stroke="#fff" stroke-width="1.5" fill="none"/>${band("FREE", "#c6f06b", "#13283a")}</svg>`,
  capsule: `<svg viewBox="0 0 40 40"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#13283a" stroke="#4aa8ff" stroke-width="2"/><rect x="7" y="6" width="26" height="21" rx="1" fill="#2a6ab0" stroke="#9ad4ff" stroke-width="1.2"/><path d="M7 11 h26 M7 16 h26 M7 21 h26 M12 6 v21 M18 6 v21 M24 6 v21 M30 6 v21" stroke="#5a9ad8" stroke-width=".5"/><path d="M11 22 V12 h8 v5 h6 v5 z" fill="none" stroke="#ffffff" stroke-width="1.4"/>${band("BONUS", "#4aa8ff", "#13283a")}</svg>`,
  warp: `<svg viewBox="0 0 40 40"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#13283a" stroke="#ff7a59" stroke-width="2"/><rect x="6" y="9" width="28" height="16" rx="4" fill="#ffc94a" stroke="#7a5608" stroke-width="1.2"/><path d="M6 17 h28" stroke="#7a5608" stroke-width="1"/>${[0,1,2,3].map(i => `<rect x="${8.5 + i * 6.2}" y="11" width="4.6" height="5" rx="1" fill="#9ad4ff"/>`).join("")}<circle cx="12" cy="26" r="2.6" fill="#2a2d30"/><circle cx="28" cy="26" r="2.6" fill="#2a2d30"/>${band("BONUS", "#ff7a59", "#13283a")}</svg>`,
};
'''

WILD_NS = r'''ICONS.wild = `<svg viewBox="0 0 40 40"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#13283a" stroke="url(#wildG)" stroke-width="2.4"/><path d="M12 30 V7 M12 9 H33 M12 9 L18 4 M16 9 L12 13" stroke="#ffc94a" stroke-width="2" fill="none" stroke-linejoin="round"/><path d="M12 9 l5 0 M17 9 l-5 6 M22 9 l-5 6" stroke="#ffc94a" stroke-width="1"/><path d="M29 9 V17" stroke="#c9ccd1" stroke-width="1"/><rect x="26" y="17" width="6" height="5" fill="#ff7a59"/><rect x="9" y="27" width="7" height="4" fill="#6a7a8a"/><path d="M5 5 l1 2.4 2.4 1 -2.4 1 -1 2.4 -1 -2.4 -2.4 -1 2.4 -1z" fill="#ffffff"/>${band("WILD", "url(#wildG)", "#13283a")}</svg>`;
ICONS.crash = `<svg viewBox="0 0 40 40"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#2a1418" stroke="#ff4b5c" stroke-width="2.2"/><path d="M8 4 L22 20" stroke="#8a9098" stroke-width="1.6"/><circle cx="24" cy="23" r="9" fill="#2a2d30" stroke="#6a6f76" stroke-width="1.6"/><circle cx="21" cy="20" r="2.4" fill="#ffffff" opacity=".2"/><path d="M5 30 l4 -3 l3 4 l4 -4 M28 34 l3 -4 l3 3" stroke="#ff4b5c" stroke-width="1.6" fill="none"/></svg>`;'''

RACCOON_SVG = '''    <svg viewBox="0 0 80 92" data-mood="normal" id="bipSvg" aria-hidden="true">
      <ellipse class="bip-thrust" cx="40" cy="88" rx="17" ry="2.6" fill="#000000" opacity=".28"/>
      <path d="M54 78 q18 -2 16 -20 q-1 -6 -5 -8" stroke="#7a7f86" stroke-width="7" fill="none" stroke-linecap="round"/>
      <path d="M58 77 q4 -1 6 -4 M64 70 q3 -3 3 -7 M66 60 q0 -4 -2 -6" stroke="#2a2d30" stroke-width="3" fill="none" stroke-linecap="round"/>
      <ellipse cx="40" cy="70" rx="16" ry="15.5" fill="#8a8f96" stroke="#3a3d42" stroke-width="1.8"/>
      <ellipse cx="40" cy="73" rx="9" ry="10.5" fill="#d8d4cc"/>
      <path d="M27 60 h26 v6 h-26z" fill="#ff8a1a"/><path d="M27 63 h26" stroke="#e8e4da" stroke-width="1.4"/>
      <path class="bip-heart" d="M40 79 l-3.5 -3.5 a2.3 2.3 0 0 1 3.5 -3 a2.3 2.3 0 0 1 3.5 3 z" fill="#ff7a59"/>
      <ellipse cx="32" cy="85" rx="5.5" ry="3.2" fill="#3a3d42"/><ellipse cx="48" cy="85" rx="5.5" ry="3.2" fill="#3a3d42"/>
      <g class="bip-arm l"><path d="M24 22 l-6 -12 l12 6z" fill="#8a8f96" stroke="#3a3d42" stroke-width="1.4"/><path d="M23 18 l-3 -5 l5 3z" fill="#3a3d42"/></g>
      <g class="bip-arm r"><path d="M56 22 l6 -12 l-12 6z" fill="#8a8f96" stroke="#3a3d42" stroke-width="1.4"/><path d="M57 18 l3 -5 l-5 3z" fill="#3a3d42"/></g>
      <path d="M22 38 q0 -20 18 -20 q18 0 18 20 q0 12 -18 14 q-18 -2 -18 -14z" fill="#9a9fa6" stroke="#3a3d42" stroke-width="2"/>
      <path d="M22 34 q9 -6 18 0 q9 -6 18 0 q-2 9 -9 9 q-5 0 -9 -4 q-4 4 -9 4 q-7 0 -9 -9z" fill="#2a2d30"/>
      <path d="M24 16 q16 -12 32 0 l-1 5 h-30z" fill="#ffc94a" stroke="#a87a10" stroke-width="1.3"/><path d="M22 21 h36" stroke="#a87a10" stroke-width="2.4" stroke-linecap="round"/><rect x="37" y="10" width="6" height="5" rx="1" fill="#ffffff" opacity=".7"/>
      <ellipse cx="40" cy="46" rx="7" ry="5" fill="#e8e4da"/>
      <ellipse cx="40" cy="43.5" rx="3.4" ry="2.4" fill="#1a1a1a"/><ellipse cx="39" cy="42.8" rx="1" ry=".6" fill="#ffffff" opacity=".6"/>
      <circle class="bip-ant" cx="40" cy="64" r="2" fill="#ffffff"/>
      <circle cx="25" cy="44" r="2.8" fill="#ff9ac6" opacity=".4"/><circle cx="55" cy="44" r="2.8" fill="#ff9ac6" opacity=".4"/>
      <g class="m m-normal"><g class="bip-eyes"><ellipse cx="32" cy="35" rx="3" ry="3.6" fill="#ffffff"/><ellipse cx="48" cy="35" rx="3" ry="3.6" fill="#ffffff"/><circle cx="32.6" cy="35.4" r="1.8" fill="#1a1a1a"/><circle cx="48.6" cy="35.4" r="1.8" fill="#1a1a1a"/></g><path d="M37 49 q3 2 6 0" stroke="#1a1a1a" stroke-width="1.4" fill="none" stroke-linecap="round"/></g>
      <g class="m m-happy"><path d="M28 36 q4 -5 8 0 M44 36 q4 -5 8 0" stroke="#ffffff" stroke-width="2.4" fill="none" stroke-linecap="round"/><path d="M36 48 q4 6 8 0z" fill="#5a1a10"/></g>
      <g class="m m-excited"><path d="M32 30 l1.4 3 3.3 .4 -2.5 2.2 .7 3.2 -2.9 -1.6 -2.9 1.6 .7 -3.2 -2.5 -2.2 3.3 -.4z M48 30 l1.4 3 3.3 .4 -2.5 2.2 .7 3.2 -2.9 -1.6 -2.9 1.6 .7 -3.2 -2.5 -2.2 3.3 -.4z" fill="#ffc94a"/><path d="M35 48 q5 7 10 0z" fill="#5a1a10"/></g>
      <g class="m m-sad"><ellipse cx="32" cy="36" rx="2.4" ry="2.8" fill="#ffffff"/><ellipse cx="48" cy="36" rx="2.4" ry="2.8" fill="#ffffff"/><circle cx="32" cy="37" r="1.4" fill="#1a1a1a"/><circle cx="48" cy="37" r="1.4" fill="#1a1a1a"/><path d="M36 51 q4 -3 8 0" stroke="#1a1a1a" stroke-width="1.4" fill="none"/><path class="bip-tear" d="M30 41 q-1.5 3 0 4 q1.5 -1 0 -4z" fill="#9ad4ff"/></g>
      <g class="m m-wow"><circle cx="32" cy="35" r="4.2" fill="#ffffff"/><circle cx="48" cy="35" r="4.2" fill="#ffffff"/><circle cx="32" cy="35" r="2.2" fill="#1a1a1a"/><circle cx="48" cy="35" r="2.2" fill="#1a1a1a"/><ellipse cx="40" cy="49.5" rx="2.6" ry="2.4" fill="#5a1a10"/></g>
    </svg>
'''

# Stadtbild: fünf Bereiche mit je vier Ausbaustufen, Boden bei y = 126 (Straße), Gehweg bei y = 117
CITY_SVG = r'''/* Stadtbild in Pixeloptik (seit Neustadt 0.4.0): alles aus Rechtecken auf einem 2er-Raster. Jede Kategorie hat 4 sichtbare Ausbaustufen,
   Zwischenstufen zeigen kleine blinkende Lichter. Straße bei y = 117 bis 126. */
const VB = { x: 48, y: 2, w: 304, h: 152 };
const WL = 126;
const GEO = [{ l: 108, t: 92, b: 126, n: 292 }, { l: 100, t: 86, b: 126, n: 300 }, { l: 92, t: 80, b: 126, n: 310 }, { l: 84, t: 74, b: 126, n: 320 }];
const GY = 116;
const PXS = 2, pq = v => Math.round(v / PXS) * PXS;
const pr = (x, y, w, h, f, cls) => `<rect x="${pq(x)}" y="${pq(y)}" width="${Math.max(PXS, pq(w))}" height="${Math.max(PXS, pq(h))}" fill="${f}"${cls ? ` class="${cls}"` : ""}/>`;
function hullPath(H, g) { return `M${g.l + 16},${GY} V${g.t - 30} H${Math.round(g.l + (g.n - g.l) * .48)} V${GY} Z`; }
function cityX(g) { const w = g.n - g.l; return { res0: pq(g.l + 18), res1: pq(g.l + w * .46), hall: pq(g.l + w * .57), tower: pq(g.l + w * .74), mk0: pq(g.n - 52), pw: pq(g.l - 14) }; }
function partAnchors(L) {
  const H = Math.min(3, Math.floor(L.hull / 3)), g = GEO[H], X = cityX(g);
  return { hull: [(X.res0 + X.res1) / 2, g.t + 4], engine: [X.res0 + 20, 122], scanner: [X.tower, g.t - 40], cargo: [X.mk0 + 26, g.t + 6], reactor: [X.pw + 6, g.t + 2] };
}
/* Pixel-Haus: Umriss, Körper, Licht links, Schatten rechts, Fensterraster, Tür */
function pxHouse(x, top, w, body, o = {}) {
  const dark = o.dark || "#1c1a24", lit = o.lit ?? .5, ww = o.ww || 4, wh = o.wh || 4, gx = o.gx || 8, gy = o.gy || 8, seed = o.seed || 0;
  let s = pr(x - 2, top - 2, w + 4, GY - top + 2, dark) + pr(x, top, w, GY - top, body) + pr(x, top, 2, GY - top, "rgba(255,255,255,.18)") + pr(x + w - 2, top, 2, GY - top, "rgba(0,0,0,.22)");
  if (!o.noWin) for (let y = top + 4, r = 0; y < GY - 10; y += gy, r++) for (let xx = x + 4, c = 0; xx + ww <= x + w - 3; xx += gx, c++) {
    const on = ((r * 7 + c * 3 + seed) % 10) / 10 < lit;
    s += pr(xx, y, ww, wh, on ? (o.wc || "#ffd27a") : "#2a3448");
  }
  if (!o.noDoor) s += pr(x + Math.floor(w / 2 / PXS) * PXS - 2, GY - 8, 4, 8, "#3a2418");
  return s;
}
const pxLights = (x, y, cnt, col, dx = 6) => Array.from({ length: cnt }, (_, i) => pr(x + i * dx, y, 2, 2, col, `blink d${i + 1}`)).join("");
function shipSVG(L, k = "a") {
  const T = id => Math.min(3, Math.floor(L[id] / 3)), lo = id => L[id] >= 9 ? 3 : L[id] % 3;
  const H = T("hull"), E = T("engine"), S = T("scanner"), C = T("cargo"), R = T("reactor");
  const g = GEO[H], { l, t, b, n } = g, X = cityX(g), hp = hullPath(H, g);
  let back = "", hull = "", front = "";
  const L0 = l - 60, LW = n - l + 120;

  /* ----- Boden und Verkehr ----- */
  back += pr(L0, GY, LW, 2, ["#6a5a44", "#9a9a94", "#a8aab0", "#c0c4cc"][E]);
  if (E === 0) {
    back += pr(L0, GY + 2, LW, b - GY, "#5a4a36") + [l + 6, l + 50, l + 120, n - 40].map((x, i) => pr(x, GY + 4 + (i % 2) * 2, 8, 2, "#3a3024") + pr(x + 2, GY + 2 + (i % 2) * 2, 4, 2, "#7a6a54")).join("");
    back += pr(l + 34, GY - 4, 14, 4, "#7a5a3a") + pr(l + 36, GY - 6, 6, 2, "#5a4028") + pr(l + 36, GY, 4, 4, "#2a2018");
  } else {
    back += pr(L0, GY + 2, LW, b - GY, "#3a3d46") + Array.from({ length: Math.ceil(LW / 16) }, (_, i) => pr(L0 + i * 16, GY + 6, 8, 2, "#e8e4d4", "lane")).join("");
  }
  const pxCar = (x, y, c, d) => `<g class="car" style="--d:${d}s">${pr(x, y + 2, 16, 4, c)}${pr(x + 4, y - 2, 8, 4, c)}${pr(x + 6, y, 4, 2, "#9ad4ff")}${pr(x + 2, y + 6, 4, 2, "#1a1a1a")}${pr(x + 10, y + 6, 4, 2, "#1a1a1a")}</g>`;
  if (E === 1) front += pxCar(l + 30, GY - 4, "#ff7a59", 9);
  if (E === 2) {
    back += pr(L0, GY + 4, LW, 2, "#9aa0a8") + pr(L0, GY - 26, LW, 2, "#5a6068") + [l - 10, l + 60, X.hall + 30, n + 20].map(x => pr(x, GY - 26, 2, 26, "#5a6068")).join("");
    front += `<g class="car" style="--d:14s">${pr(l + 20, GY - 12, 44, 14, "#7a5608")}${pr(l + 22, GY - 10, 40, 10, "#ffc94a")}${[0, 1, 2, 3, 4].map(i => pr(l + 24 + i * 8, GY - 8, 6, 4, "#9ad4ff")).join("")}${pr(l + 22, GY - 2, 40, 2, "#ff7a59")}${pr(l + 40, GY - 18, 2, 6, "#3a3d42")}${pr(l + 40, GY - 20, 8, 2, "#3a3d42")}</g>`;
  }
  if (E === 3) {
    front += pr(L0, GY - 32, LW, 4, "#c9d3e0") + pr(L0, GY - 28, LW, 2, "#7a8a9a") + [l - 20, l + 70, X.hall + 20, n + 10].map(x => pr(x, GY - 28, 4, 28, "#9aa4b0")).join("");
    front += `<g class="car" style="--d:7s">${pr(l + 10, GY - 44, 62, 12, "#4aa8ff")}${pr(l + 12, GY - 42, 58, 8, "#ffffff")}${[0, 1, 2, 3, 4, 5].map(i => pr(l + 14 + i * 9, GY - 41, 6, 4, "#4aa8ff")).join("")}${pr(l + 70, GY - 40, 4, 6, "#3fd0b0")}</g>`;
  }
  front += pxLights(X.res0 + 2, b - 4, lo("engine"), "#ffc94a");

  /* ----- Energie (links) ----- */
  const pw = X.pw;
  if (R === 0) back += pr(pw - 8, GY - 12, 20, 12, "#2a2018") + pr(pw - 6, GY - 10, 16, 10, "#4a4038") + pr(pw - 4, GY - 16, 2, 4, "#2a2018") + pr(pw + 4, GY - 14, 2, 2, "#ff9a3c", "flick");
  if (R === 1) back += pr(pw, GY - 46, 4, 46, "#e8ecf0") + pr(pw + 2, GY - 46, 2, 46, "#b8c0c8") + `<g class="rotor" style="transform-origin:${pw + 2}px ${GY - 46}px">${[0, 120, 240].map(a => `<g transform="rotate(${a} ${pw + 2} ${GY - 46})">${pr(pw, GY - 66, 4, 20, "#ffffff")}</g>`).join("")}</g>` + pr(pw, GY - 48, 4, 4, "#8a9098");
  if (R >= 2) {
    back += pr(pw - 18, GY - 30, 26, 30, "#5a6068") + pr(pw - 16, GY - 28, 22, 28, "#9aa4ae") + pr(pw + 8, GY - 20, 20, 20, "#3a4048") + pr(pw + 10, GY - 18, 16, 18, "#6a7480");
    back += pr(pw + 18, GY - 46, 6, 26, "#8a2a2a") + pr(pw + 18, GY - 40, 6, 2, "#ffffff") + pr(pw + 18, GY - 32, 6, 2, "#ffffff") + pr(pw + 12, GY - 14, 4, 4, "#ffd27a") + pr(pw + 20, GY - 14, 4, 4, "#ffd27a");
    back += pr(pw + 16, GY - 54, 4, 4, "rgba(200,200,210,.5)", "pulse") + pr(pw + 22, GY - 60, 6, 4, "rgba(200,200,210,.35)", "pulse");
  }
  if (R === 3) back += [0, 1, 2].map(i => pr(pw - 44 + i * 10, GY - 6, 8, 4, "#2a5aa8") + pr(pw - 44 + i * 10, GY - 6, 8, 2, "#9ad4ff") + pr(pw - 42 + i * 10, GY - 2, 2, 2, "#5a6068")).join("") + pr(pw - 6, GY - 40, 6, 6, "#9ad4ff", "pulse");
  front += pxLights(pw - 6, GY + 6, lo("reactor"), "#3fd0b0");

  /* ----- Wohnviertel ----- */
  hull += `<clipPath id="hc-${k}"><path d="${hp}"/></clipPath><g style="filter:${paintFilter()}">`;
  const r0 = X.res0, r1 = X.res1, rw = r1 - r0;
  if (H === 0) {
    [[r0, 20, 10], [r0 + 22, 30, 14], [r0 + 52, 14, 12]].forEach(([x, hh, w], i) => {
      hull += pr(x - 2, GY - hh - 2, w + 4, hh + 2, "#2a2420") + pr(x, GY - hh, w, hh, "#7a6a5a") + pr(x + w - 4, GY - hh - 4, 4, 4, "#7a6a5a") + pr(x + 2, GY - hh + 6, 4, 4, "#1a1410");
    });
    hull += pr(r0 - 4, GY - 4, rw + 10, 4, "#5a4a3a") + pr(r0 + 10, GY - 6, 8, 2, "#6a5a48") + pr(r0 + 40, GY - 6, 10, 2, "#6a5a48");
  } else {
    const houses = H === 1 ? 4 : H === 2 ? 5 : 3, hw = pq(rw / houses);
    for (let i = 0; i < houses; i++) {
      const x = r0 + i * hw, w = hw - 4;
      if (H === 1) { const top = t + 18 + (i % 2) * 4, col = ["#d8c8a8", "#c8b898", "#e0d0b0", "#c0b090"][i % 4];
        hull += pxHouse(x, top, w, col, { lit: .4, seed: i, gy: 10 }) + pr(x - 2, top - 4, w + 4, 4, "#8a3a28") + pr(x + 2, top - 8, w - 4, 4, "#a8443a") + pr(x + 6, top - 12, w - 12, 4, "#c8553d"); }
      if (H === 2) { const top = t + 4 + (i % 3) * 6, col = ["#e8a87a", "#8ac8a8", "#e8d07a", "#a8b8e8", "#e88a8a"][i];
        hull += pxHouse(x, top, w, col, { lit: .55, seed: i * 3 }) + pr(x - 2, top - 4, w + 4, 2, "#4a4a52") + pr(x + 2, top - 6, 4, 2, "#4a4a52"); }
      if (H === 3) { const top = t - 6 + (i % 2) * 8, col = ["#e8eef4", "#dce8e4", "#ece4dc"][i];
        hull += pxHouse(x, top, w, col, { lit: .7, seed: i * 5, ww: 6, gx: 8, gy: 7, wc: "#9ad4ff" }) + pr(x - 2, top - 2, w + 4, 2, "#3fd0b0") + pr(x + 2, top - 6, 4, 4, "#4a9850") + pr(x + w - 6, top - 8, 6, 6, "#5aa860"); }
    }
  }
  hull += `<g clip-path="url(#hc-${k})">${decalSVG(g)}</g></g>`;
  front += pxLights(r0 + 4, GY + 6, lo("hull"), "#7ed957");

  /* ----- Rathaus (Mitte) ----- */
  const hx = X.hall, hw2 = pq(22 + H * 2), ht = pq(t - 4 - H * 3), hcol = ["#8a7a6a", "#d8ccb4", "#e8dcc4", "#f0e8d8"][H], roof = ["#5a4a3a", "#7a8a9a", "#3a6a8a", "#2a5a7a"][H];
  back += pxHouse(hx - hw2, ht + 14, hw2 * 2, hcol, { lit: H ? .6 : 0, gx: 10, gy: 10, seed: 2 });
  back += pr(hx - hw2 - 4, ht + 10, hw2 * 2 + 8, 4, roof) + pr(hx - hw2 + 4, ht + 6, hw2 * 2 - 8, 4, roof) + pr(hx - hw2 + 12, ht + 2, hw2 * 2 - 24, 4, roof);
  if (H >= 1) back += [-1, 1].map(s => pr(hx + s * (hw2 - 6) - 2, ht + 16, 4, GY - ht - 16, "rgba(255,255,255,.35)")).join("");
  if (H >= 2) back += pr(hx - 8, ht - 18, 16, 22, "#2a2420") + pr(hx - 6, ht - 16, 12, 20, hcol) + pr(hx - 4, ht - 12, 8, 8, "#ffffff") + pr(hx, ht - 10, 2, 4, "#1a1a1a") + pr(hx - 6, ht - 22, 12, 4, "#2a5a7a") + pr(hx - 2, ht - 26, 4, 4, "#2a5a7a");
  if (H >= 1) { const fy = ht + (H >= 2 ? -40 : -12); back += pr(hx, fy, 2, 14, "#5a5a5a") + `<g class="sail">${pr(hx + 2, fy, 10, 6, ["#888", "#3fd0b0", "#4aa8ff", "#ff7a59"][H])}</g>`; }
  const mx = hx - hw2 + 8, my = GY - 12;
  front += pr(mx, my, 4, 4, "#e0a878") + pr(mx, my - 2, 4, 2, ["#5a3a1a", "#8a3a2a", "#2a2a2a", "#c9a24a"][H]) + pr(mx - 2, my + 4, 8, 6, "#3a5a8a") + pr(mx, my + 10, 2, 2, "#1a1a1a") + pr(mx + 2, my + 10, 2, 2, "#1a1a1a");

  /* ----- Funkturm ----- */
  const sx = X.tower, sb = GY;
  if (S === 0) front += pr(sx, sb - 22, 2, 22, "#7a7f86") + pr(sx + 2, sb - 26, 6, 2, "#7a7f86") + pr(sx + 8, sb - 30, 6, 2, "#7a7f86") + pr(sx - 2, sb - 2, 6, 2, "#5a5f66");
  if (S === 1) front += pr(sx - 4, sb - 46, 2, 46, "#a8aeb6") + pr(sx + 2, sb - 46, 2, 46, "#a8aeb6") + [6, 14, 22, 30, 38].map(y => pr(sx - 2, sb - y, 4, 2, "#a8aeb6")).join("") + pr(sx - 2, sb - 50, 4, 4, "#ff4b5c", "blink");
  if (S === 2) front += pr(sx - 6, sb - 62, 2, 62, "#d8dce0") + pr(sx + 4, sb - 62, 2, 62, "#d8dce0") + [10, 22, 34, 46, 58].map(y => pr(sx - 4, sb - y, 8, 2, "#d8dce0")).join("") + `<g class="dish">${pr(sx + 6, sb - 46, 8, 2, "#e8ecf0")}${pr(sx + 8, sb - 48, 6, 2, "#e8ecf0")}${pr(sx + 12, sb - 52, 2, 4, "#8a9098")}</g>` + pr(sx - 2, sb - 66, 4, 4, "#ff4b5c", "blink");
  if (S === 3) front += pr(sx - 4, sb - 56, 8, 56, "#8a9098") + pr(sx - 2, sb - 56, 4, 56, "#e8ecf0") + pr(sx - 6, sb - 70, 12, 2, "#5a6068") + pr(sx - 8, sb - 68, 16, 10, "#c9d3e0") + pr(sx - 6, sb - 58, 12, 2, "#5a6068") + pr(sx - 8, sb - 64, 16, 2, "#4aa8ff") + pr(sx - 1, sb - 88, 2, 18, "#d8dce0") + pr(sx - 2, sb - 92, 4, 4, "#ff4b5c", "blink") + `<circle class="ping" cx="${sx}" cy="${sb - 90}" r="5" fill="none" stroke="#9ad4ff" stroke-width="1"/>`;
  front += pxLights(sx - 6, sb + 6, lo("scanner"), "#4aa8ff");

  /* ----- Handel ----- */
  const mk = X.mk0;
  if (C === 0) front += pr(mk + 8, GY - 10, 24, 10, "#3a2a1a") + pr(mk + 10, GY - 8, 20, 8, "#7a5a3a") + pr(mk + 6, GY - 14, 12, 4, "#8a7a6a") + pr(mk + 30, GY - 6, 6, 6, "#6a4a2a") + pr(mk + 12, GY, 4, 2, "#2a2018");
  if (C === 1) front += pr(mk + 6, GY - 12, 30, 12, "#5a3a1a") + pr(mk + 8, GY - 10, 26, 10, "#a8743f") + Array.from({ length: 8 }, (_, i) => pr(mk + 4 + i * 4, GY - 20, 4, 6, i % 2 ? "#ffffff" : "#ff7a59")).join("") + ["#ff4b5c", "#ffc94a", "#7ed957"].map((c, i) => pr(mk + 12 + i * 8, GY - 10, 4, 4, c)).join("");
  if (C === 2) front += pxHouse(mk, t + 10, 44, "#dce6f0", { lit: .6, seed: 4, noDoor: true, gy: 9 }) + pr(mk - 2, t + 6, 48, 6, "#4aa8ff") + [0, 1, 2, 3, 4].map(i => pr(mk + 8 + i * 6, t + 8, 4, 2, "#ffffff")).join("") + pr(mk + 4, GY - 16, 22, 14, "#9ad4ff") + pr(mk + 30, GY - 16, 8, 16, "#5a6a7a");
  if (C === 3) front += pxHouse(mk - 4, t - 6, 52, "#c9d8e8", { noWin: true, noDoor: true }) + [0, 1, 2, 3, 4, 5].map(r => pr(mk, t + r * 10, 44, 6, r % 2 ? "#6ab8ff" : "#4aa8ff")).join("") + pr(mk - 6, t - 12, 56, 6, "#ff7a59") + [0, 1, 2, 3, 4, 5].map(i => pr(mk + 2 + i * 8, t - 10, 4, 2, "#ffffff")).join("") + pr(mk + 14, GY - 10, 16, 10, "#2a3a4a");
  front += pxLights(mk + 6, GY + 6, lo("cargo"), "#ffc94a");

  // unsichtbare Klickzonen
  const z = (part, x, y, w, h) => `<rect class="zone" data-part="${part}" fill="#ffffff" fill-opacity="0" x="${x}" y="${y}" width="${w}" height="${h}"/>`;
  const zones = [
    z("cargo", mk - 6, t - 14, 58, GY - t + 14), z("hull", r0 - 4, t - 14, rw + 8, GY - t + 14), z("engine", l - 50, GY, n - l + 100, b - GY + 2),
    z("cockpit", hx - hw2, ht, hw2 * 2, GY - ht), z("reactor", pw - 20, GY - 50, 44, 50), z("scanner", sx - 10, GY - 90, 22, 90),
  ].join("");
  return `<g class="ship pixel t${H}" shape-rendering="crispEdges">${back}${hull}${front}${zones}</g>`;
}

/* Stadtstufen in Pixeloptik: Kleinstadt (zweite Häuserreihe, Kirchturm) und Metropole (Hochhauskulisse, Brücke). */
function vehLayers(L, k) {
  const V = veh(); if (!V) return ["", ""];
  const H = Math.min(3, Math.floor(L.hull / 3)), g = GEO[H], { l, n } = g;
  const col = ["#4a4a52", "#5a6a7a", "#6a7a8e", "#7a8aa0"][H], pf = `style="filter:${paintFilter()}" shape-rendering="crispEdges"`;
  let back = "";
  const span = n - l + 70, cw = pq(span / 9);
  const row = Array.from({ length: 9 }, (_, i) => { const x = pq(l - 30 + i * cw), h = pq(24 + ((i * 37) % 18)), top = GY - 8 - h;
    return pr(x, top, cw - 2, h + 8, col) + pr(x + 2, top - 2, cw - 6, 2, col) + (H ? Array.from({ length: Math.floor(h / 8) }, (_, r) => pr(x + 4, top + 4 + r * 8, cw - 10, 2, (r + i) % 3 ? "#ffd27a" : "#2a3448")).join("") : ""); }).join("");
  const cx = pq(l + 30);
  back += `<g ${pf} opacity=".75">${row}${pr(cx, GY - 76, 12, 46, col)}${pr(cx + 2, GY - 82, 8, 6, col)}${pr(cx + 4, GY - 88, 4, 6, col)}${pr(cx + 5, GY - 94, 2, 6, "#c9a24a")}${pr(cx + 4, GY - 66, 4, 6, H ? "#ffd27a" : "#2a2a2a")}</g>`;
  if (V >= 2) {
    const sky = Array.from({ length: 7 }, (_, i) => { const w = pq(16 + (i % 3) * 6), x = pq(l - 20 + i * ((n - l + 40) / 7)), h = pq(60 + ((i * 53) % 46)), top = GY - h - 20;
      return pr(x, top, w, h, H ? "#2a4a6a" : "#3a3a3a") + (H ? Array.from({ length: Math.floor(h / 6) }, (_, r) => Array.from({ length: Math.floor((w - 4) / 4) }, (_, c) => (r * 5 + c * 3 + i) % 4 ? pr(x + 2 + c * 4, top + 4 + r * 6, 2, 2, "#9ad4ff") : "").join("")).join("") : "") +
        (i === 3 ? pr(x + w / 2 - 1, top - 14, 2, 14, "#c9d3e0") + pr(x + w / 2 - 2, top - 18, 4, 4, "#ff4b5c", "blink") : ""); }).join("");
    back = `<g ${pf} opacity=".85">${sky}</g>` + back;
    const bc = H ? "#ff7a59" : "#6a5a4a";
    back += `<g shape-rendering="crispEdges">${Array.from({ length: 21 }, (_, i) => { const x = n - 10 + i * 4, y = GY - 22 - Math.round(Math.sin(i / 20 * Math.PI) * 26 / 2) * 2; return pr(x, y, 4, 2, bc) + (i % 4 === 2 ? pr(x + 1, y, 2, GY - 20 - y, bc) : ""); }).join("")}${pr(n - 14, GY - 22, 92, 4, "#5a6068")}</g>`;
  }
  return [back, ""];
}
'''

CITY_SKY = r'''function sizeSkyObj(o) {
  // Pixeloptik: der Himmel wird in grober Auflösung gemalt und hochskaliert (CSS image-rendering: pixelated)
  const r = o.host.getBoundingClientRect(), d = 1 / 3;
  o.w = r.width; o.h = r.height;
  if (!o.w) return;
  o.canvas.width = o.w * d; o.canvas.height = o.h * d; o.cx.setTransform(d, 0, 0, d, 0, 0);
  o.stars = Array.from({ length: 5 }, () => ({ x: Math.random() * o.w, y: o.h * (.05 + Math.random() * .3), z: .5 + Math.random() * .8, w: 60 + Math.random() * 80 }));
  o.dust = Array.from({ length: 40 }, () => ({ x: Math.random() * o.w, y: Math.random() * o.h * .5, p: Math.random() * 6 }));
  o.debris = Array.from({ length: 6 }, () => newDebris(o, true));
  o.birds = Array.from({ length: 3 }, () => ({ x: Math.random() * o.w, y: o.h * (.1 + Math.random() * .2), p: Math.random() * 6, v: .3 + Math.random() * .3 }));
}
function newDebris(o, anywhere) {
  const gy = toSky(o, 0, 117)[1];
  return { x: anywhere ? Math.random() * o.w : o.w + 30, y: gy - 2 + Math.random() * 6, s: 3 + Math.random() * 4, kind: Math.random() < .5 ? "brick" : "beam", rot: (Math.random() - .5) * 1.2 };
}
function toSky(o, x, y) { const s = Math.min(o.w / VB.w, o.h / VB.h); return [(o.w - VB.w * s) / 2 + (x - VB.x) * s, (o.h - VB.h * s) / 2 + (y - VB.y) * s, s]; }
function skyCloud(c, x, y, w, col) {
  c.fillStyle = col; c.beginPath();
  c.ellipse(x, y, w * .5, w * .14, 0, 0, 7); c.ellipse(x - w * .24, y + w * .03, w * .3, w * .12, 0, 0, 7); c.ellipse(x + w * .2, y - w * .05, w * .28, w * .15, 0, 0, 7);
  c.fill();
}
function skyLand(c, o, sec, hz) {
  // ferne Silhouette je Viertel
  const s = Math.max(.6, o.h / 200);
  c.fillStyle = sec.land;
  if (sec.shape === "old") { for (let i = 0; i < 12; i++) { const x = i * o.w / 11 - 10, h = (14 + (i * 29 % 16)) * s, w = o.w / 13; c.fillRect(x, hz - h, w, h + 2); c.beginPath(); c.moveTo(x - 2, hz - h); c.lineTo(x + w / 2, hz - h - 8 * s); c.lineTo(x + w + 2, hz - h); c.fill(); }
    c.fillRect(o.w * .3, hz - 44 * s, 8 * s, 44 * s); c.beginPath(); c.moveTo(o.w * .3 - 2 * s, hz - 44 * s); c.lineTo(o.w * .3 + 4 * s, hz - 60 * s); c.lineTo(o.w * .3 + 10 * s, hz - 44 * s); c.fill(); }
  else if (sec.shape === "harbor") { c.fillRect(0, hz - 6 * s, o.w, 8 * s); for (let i = 0; i < 4; i++) { const x = o.w * (.1 + i * .25); c.fillRect(x, hz - 40 * s, 3 * s, 34 * s); c.fillRect(x - 14 * s, hz - 40 * s, 30 * s, 3 * s); c.fillRect(x + 12 * s, hz - 40 * s, 1 * s, 14 * s); }
    for (let i = 0; i < 6; i++) { const x = o.w * (.05 + i * .17); c.fillRect(x, hz - 12 * s, 14 * s, 6 * s); } }
  else if (sec.shape === "industry") { for (let i = 0; i < 6; i++) { const x = o.w * (.05 + i * .17), h = (16 + (i % 3) * 6) * s; c.fillRect(x, hz - h, 26 * s, h + 2); c.fillRect(x + 18 * s, hz - h - 22 * s, 4 * s, 22 * s); } }
  else { c.beginPath(); c.moveTo(0, hz + 2); for (let x = 0; x <= o.w; x += 20) c.lineTo(x, hz - (10 + Math.sin(x * .02) * 8 + Math.sin(x * .05) * 4) * s); c.lineTo(o.w, hz + 2); c.fill();
    for (let i = 0; i < 9; i++) { const x = o.w * (.06 + i * .11), h = (8 + (i % 3) * 4) * s; c.fillRect(x, hz - 16 * s - h, 10 * s, h); } }
}
function drawSky(o, now, dt) {
  if (!o.w) { sizeSkyObj(o); if (!o.w) return; }
  const c = o.cx, E = Math.floor(state.ship.engine / 3), H = Math.floor(state.ship.hull / 3), R = Math.floor(state.ship.reactor / 3);
  const sec = curSector(), hz = toSky(o, 0, 104)[1], gy = toSky(o, 0, 117)[1];
  c.clearRect(0, 0, o.w, o.h);
  const sg = c.createLinearGradient(0, 0, 0, hz); sg.addColorStop(0, sec.sky[0]); sg.addColorStop(.65, sec.sky[1]); sg.addColorStop(1, sec.sky[2]);
  c.fillStyle = sg; c.fillRect(0, 0, o.w, hz + 1);
  // Sterne bei Nacht
  if (sec.night) for (const d of o.dust) { d.p += .002 * dt; c.fillStyle = `rgba(255,255,255,${.25 + .25 * Math.sin(d.p * 3)})`; c.fillRect(d.x, d.y, 1.2, 1.2); }
  const sx = o.w * .8, sy = hz * .38, sr = Math.max(10, o.h * .07);
  const gl = c.createRadialGradient(sx, sy, sr * .4, sx, sy, sr * 4); gl.addColorStop(0, sec.sun[1]); gl.addColorStop(1, "rgba(0,0,0,0)");
  c.fillStyle = gl; c.fillRect(0, 0, o.w, hz);
  c.fillStyle = sec.sun[0]; c.beginPath(); c.arc(sx, sy, sr, 0, 7); c.fill();
  for (const cl of o.stars) { cl.x -= .006 * cl.z * dt; if (cl.x < -cl.w) cl.x = o.w + cl.w; skyCloud(c, cl.x, cl.y, cl.w * cl.z, sec.cloud); }
  for (const b of o.birds) { b.x -= b.v * dt * .05; b.p += .01 * dt; if (b.x < -10) { b.x = o.w + 10; b.y = o.h * (.08 + Math.random() * .2); }
    const f = Math.sin(b.p) * 3; c.strokeStyle = sec.night ? "rgba(200,210,230,.5)" : "rgba(30,40,50,.6)"; c.lineWidth = 1.2; c.beginPath(); c.moveTo(b.x - 5, b.y - f); c.quadraticCurveTo(b.x - 2, b.y - 2, b.x, b.y); c.quadraticCurveTo(b.x + 2, b.y - 2, b.x + 5, b.y - f); c.stroke(); }
  skyLand(c, o, sec, hz);
  const mg = c.createLinearGradient(0, hz, 0, o.h); mg.addColorStop(0, sec.ground[0]); mg.addColorStop(1, sec.ground[1]);
  c.fillStyle = mg; c.fillRect(0, hz, o.w, o.h - hz);
  // Schutt in der Ruinenstadt
  const debrisCount = H === 0 ? 6 : H === 1 ? 2 : 0;
  o.debris.slice(0, debrisCount).forEach(d => {
    c.save(); c.translate(d.x, d.y); c.rotate(d.rot);
    if (d.kind === "brick") { c.fillStyle = "#8a5a3a"; c.fillRect(-d.s, -d.s * .5, d.s * 2, d.s); } else { c.fillStyle = "#5a5048"; c.fillRect(-d.s * 2, -d.s * .3, d.s * 4, d.s * .6); }
    c.restore();
  });
  const g = GEO[H];
  // Rauch: Ruinen qualmen, Kraftwerk dampft
  if (H === 0 && Math.random() < .2) { const [x, y, s] = toSky(o, g.l + 40 + Math.random() * 60, g.t + 16); o.parts.push({ x, y, vx: -.1, vy: -.4 - Math.random() * .3, r: 2.2 * s, life: .9, kind: "smoke", dark: true }); }
  if (R >= 2 && Math.random() < .25) { const [x, y, s] = toSky(o, g.l - 14 - 4, 117 - 34); o.parts.push({ x, y, vx: -.2, vy: -.5 - Math.random() * .3, r: 2.4 * s, life: .9, kind: "smoke" }); }
  if (R === 0 && Math.random() < .02) { const [x, y] = toSky(o, g.l - 10, 105); for (let i = 0; i < 4; i++) o.parts.push({ x, y, vx: (Math.random() - .5) * 1.6, vy: -1 - Math.random(), r: 1, life: 1, kind: "spark" }); }
  o.parts = o.parts.filter(p => p.life > 0);
  for (const p of o.parts) {
    p.x += p.vx * dt * .06; p.y += p.vy * dt * .06;
    if (p.kind === "smoke") { p.r += .02 * dt; p.life -= .0009 * dt; c.fillStyle = p.dark ? `rgba(40,36,34,${p.life * .4})` : `rgba(230,234,240,${p.life * .35})`; c.beginPath(); c.arc(p.x, p.y, Math.max(0, p.r), 0, 7); c.fill(); }
    else if (p.kind === "dust") { p.r += .012 * dt; p.life -= .0014 * dt; c.fillStyle = `rgba(150,130,100,${p.life * .35})`; c.beginPath(); c.arc(p.x, p.y, Math.max(0, p.r), 0, 7); c.fill(); }
    else if (p.kind === "drop") { p.vy += .004 * dt; p.life -= .002 * dt; c.fillStyle = `rgba(255,220,150,${p.life * .9})`; c.beginPath(); c.arc(p.x, p.y, Math.max(0, p.r), 0, 7); c.fill(); }
    else { p.vy += .002 * dt; p.life -= .0025 * dt; c.fillStyle = p.col || `rgba(255,${150 + (Math.random() * 80 | 0)},60,${p.life})`; c.globalAlpha = Math.max(0, p.life); c.fillRect(p.x, p.y, p.r * 2, p.r * 2); c.globalAlpha = 1; }
  }
  // Straßenlaternen am Gehweg
  if (H >= 1) for (let i = 0; i < 6; i++) { const x = o.w * (.08 + i * .17); c.strokeStyle = "rgba(90,96,104,.9)"; c.lineWidth = 1.2; c.beginPath(); c.moveTo(x, gy); c.lineTo(x, gy - 16); c.stroke(); c.fillStyle = sec.night ? "rgba(255,210,122,.9)" : "rgba(255,240,200,.5)"; c.beginPath(); c.arc(x, gy - 17, 1.8, 0, 7); c.fill(); if (sec.night) { const lg = c.createRadialGradient(x, gy - 17, 0, x, gy - 17, 14); lg.addColorStop(0, "rgba(255,210,122,.25)"); lg.addColorStop(1, "rgba(255,210,122,0)"); c.fillStyle = lg; c.fillRect(x - 14, gy - 31, 28, 28); } }
}
'''

CITY_BG = r'''function drawStars(dt) {
  scx.clearRect(0, 0, innerWidth, innerHeight);
  // ruhig schwebende Stadtlichter (Bokeh)
  for (const s of stars) {
    s.y -= (0.006 + warpBoost * .5) * s.z * dt; s.p += 0.001 * dt;
    if (s.y < -10) { s.y = innerHeight + 10; s.x = Math.random() * innerWidth; }
    const x = s.x + Math.sin(s.p * 2) * 4 * s.z, a = (.05 + .12 * s.z) * (.6 + .4 * Math.sin(s.p * 4));
    scx.fillStyle = s.z > .9 ? `rgba(255,210,122,${a})` : s.z > .6 ? `rgba(126,224,200,${a})` : `rgba(154,212,255,${a})`;
    scx.beginPath(); scx.arc(x, s.y, s.z * 2.2, 0, 7); scx.fill();
  }
}
'''
