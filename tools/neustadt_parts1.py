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
CITY_SVG = r'''/* Stadtbild: jede Kategorie hat 4 sichtbare Ausbaustufen, Zwischenstufen zeigen kleine Lichter. Straße bei y = 119 bis 126. */
const VB = { x: 48, y: 2, w: 304, h: 152 };
const WL = 126;
const GEO = [{ l: 108, t: 92, b: 126, n: 292 }, { l: 100, t: 86, b: 126, n: 300 }, { l: 92, t: 80, b: 126, n: 310 }, { l: 84, t: 74, b: 126, n: 320 }];
const GY = 117;
function hullPath(H, g) { return `M${g.l + 18},${GY} V${g.t + 8} H${Math.round(g.l + (g.n - g.l) * .46)} V${GY} Z`; }
function cityX(g) { const w = g.n - g.l; return { res0: g.l + 18, res1: Math.round(g.l + w * .46), hall: Math.round(g.l + w * .56), tower: Math.round(g.l + w * .74), mk0: g.n - 52, pw: g.l - 14 }; }
function partAnchors(L) {
  const H = Math.min(3, Math.floor(L.hull / 3)), g = GEO[H], X = cityX(g);
  return { hull: [(X.res0 + X.res1) / 2, g.t + 4], engine: [X.res0 + 20, 123], scanner: [X.tower, g.t - 40], cargo: [X.mk0 + 26, g.t + 6], reactor: [X.pw + 6, g.t + 2] };
}
function shipSVG(L, k = "a") {
  const T = id => Math.min(3, Math.floor(L[id] / 3)), lo = id => L[id] >= 9 ? 3 : L[id] % 3;
  const H = T("hull"), E = T("engine"), S = T("scanner"), C = T("cargo"), R = T("reactor");
  const g = GEO[H], { l, t, b, n } = g, X = cityX(g), hp = hullPath(H, g);
  const lights = (x, y, cnt, col, dx = 7) => Array.from({ length: cnt }, (_, i) => `<circle class="blink d${i + 1}" cx="${x + i * dx}" cy="${y}" r="1.9" fill="${col}"/>`).join("");
  const win = (x, y, w, h, lit) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${lit ? "#ffd27a" : "#2a3a4a"}" opacity="${lit ? .9 : .8}"/>`;
  let back = "", hull = "", det = "", front = "";

  /* ----- Boden: Gehweg und Straße (Verkehr) ----- */
  back += `<rect x="${l - 60}" y="${GY}" width="${n - l + 120}" height="3" fill="${["#5a5448", "#8a8a84", "#9a9a94", "#a8aab0"][E]}"/>`;
  if (E === 0) back += `<rect x="${l - 60}" y="${GY + 3}" width="${n - l + 120}" height="${b - GY - 3}" fill="#6a5a44"/>${[l + 10, l + 80, n - 40].map(x => `<ellipse cx="${x}" cy="${GY + 7}" rx="7" ry="1.8" fill="#3a3020"/>`).join("")}
    <g transform="translate(${l + 40} ${GY + 2}) rotate(-12)"><rect x="0" y="-6" width="16" height="6" fill="#7a5a3a" stroke="#3a2a1a" stroke-width=".8"/><circle cx="3" cy="1" r="2.4" fill="none" stroke="#3a2a1a" stroke-width="1"/></g>`;
  else back += `<rect x="${l - 60}" y="${GY + 3}" width="${n - l + 120}" height="${b - GY - 3}" fill="#3a3f46"/><path class="lane" d="M${l - 60},${GY + 6.5} H${n + 60}" stroke="#e8e4d4" stroke-width=".9" stroke-dasharray="6 6" opacity=".7"/>`;
  if (E === 1) front += `<g class="car" style="--d:9s"><rect x="${l + 30}" y="${GY + 1}" width="16" height="5" rx="2" fill="#ff7a59"/><rect x="${l + 33}" y="${GY - 2}" width="9" height="4" rx="1.5" fill="#ff9a7a"/><rect x="${l + 34}" y="${GY - 1.4}" width="3" height="2.4" fill="#9ad4ff"/><circle cx="${l + 34}" cy="${GY + 6}" r="1.6" fill="#1a1a1a"/><circle cx="${l + 43}" cy="${GY + 6}" r="1.6" fill="#1a1a1a"/></g>`;
  if (E === 2) {
    back += `<path d="M${l - 60},${GY + 4.5} H${n + 60} M${l - 60},${GY + 7.5} H${n + 60}" stroke="#9aa0a8" stroke-width=".8"/>${[l - 10, l + 60, X.hall + 30, n + 20].map(x => `<path d="M${x},${GY} V${GY - 26} h6" stroke="#5a6068" stroke-width="1.2" fill="none"/>`).join("")}<path d="M${l - 60},${GY - 25} H${n + 60}" stroke="#5a6068" stroke-width=".5"/>`;
    front += `<g class="car" style="--d:14s"><rect x="${l + 20}" y="${GY - 9}" width="44" height="13" rx="3" fill="#ffc94a" stroke="#7a5608" stroke-width="1"/>${[0, 1, 2, 3, 4].map(i => `<rect x="${l + 23 + i * 8}" y="${GY - 7}" width="6" height="5" rx="1" fill="#9ad4ff"/>`).join("")}<path d="M${l + 20},${GY - 1} h44" stroke="#ff7a59" stroke-width="1.6"/><path d="M${l + 40},${GY - 9} l4 -6 h6" stroke="#3a3d42" stroke-width=".9" fill="none"/></g>`;
  }
  if (E === 3) {
    front += `<path d="M${l - 60},${GY - 30} H${n + 60}" stroke="#c9d3e0" stroke-width="3"/><path d="M${l - 60},${GY - 28} H${n + 60}" stroke="#7a8a9a" stroke-width="1"/>${[l - 20, l + 70, X.hall + 20, n + 10].map(x => `<rect x="${x}" y="${GY - 29}" width="4" height="${29}" fill="#9aa4b0"/>`).join("")}
      <g class="car" style="--d:7s"><path d="M${l + 10},${GY - 31} h52 q8 0 10 -6 q-2 -6 -10 -6 h-52z" fill="#ffffff" stroke="#4aa8ff" stroke-width="1.2"/>${[0, 1, 2, 3, 4, 5].map(i => `<rect x="${l + 14 + i * 8}" y="${GY - 41}" width="6" height="4" rx="1" fill="#4aa8ff"/>`).join("")}<path d="M${l + 10},${GY - 33} h56" stroke="#3fd0b0" stroke-width="1.4"/></g>`;
  }
  front += lights(X.res0 + 2, b - 2, lo("engine"), "#ffc94a");

  /* ----- Energie (links) ----- */
  const pw = X.pw;
  if (R === 0) back += `<rect x="${pw - 8}" y="${GY - 12}" width="20" height="12" fill="#4a4038" stroke="#2a2018" stroke-width="1"/><path d="M${pw - 4},${GY - 12} l3 -4 l4 3" stroke="#2a2018" stroke-width="1.4" fill="none"/><circle class="flick" cx="${pw + 6}" cy="${GY - 14}" r="1.6" fill="#ff9a3c"/>`;
  if (R === 1) back += `<path d="M${pw},${GY} L${pw + 1.5},${GY - 46} L${pw + 3},${GY}" fill="#e8ecf0" stroke="#8a9098" stroke-width=".6"/><g class="rotor" style="transform-origin:${pw + 1.5}px ${GY - 46}px">${[0, 120, 240].map(a => `<path d="M${pw + 1.5},${GY - 46} l-1.4,-18 l1.4,-2 l1.4,2z" fill="#ffffff" stroke="#8a9098" stroke-width=".5" transform="rotate(${a} ${pw + 1.5} ${GY - 46})"/>`).join("")}</g><circle cx="${pw + 1.5}" cy="${GY - 46}" r="1.6" fill="#c9ccd1"/>`;
  if (R >= 2) back += `<path d="M${pw - 16},${GY} L${pw - 12},${GY - 30} Q${pw - 4},${GY - 34} ${pw + 4},${GY - 30} L${pw + 8},${GY} Z" fill="#9aa4ae" stroke="#5a6068" stroke-width="1"/><rect x="${pw + 10}" y="${GY - 18}" width="16" height="18" fill="#6a7480" stroke="#3a4048" stroke-width="1"/><rect x="${pw + 20}" y="${GY - 40}" width="4" height="22" fill="#8a2a2a"/><path d="M${pw + 20},${GY - 36} h4 M${pw + 20},${GY - 30} h4" stroke="#ffffff" stroke-width="1"/>${win(pw + 12, GY - 14, 4, 3, true)}${win(pw + 19, GY - 14, 4, 3, true)}`;
  if (R === 3) back += `${[0, 1, 2].map(i => `<path d="M${pw - 40 + i * 9},${GY} l3,-6 h7 l-3,6z" fill="#2a5aa8" stroke="#9ad4ff" stroke-width=".6"/>`).join("")}<circle class="pulse" cx="${pw - 4}" cy="${GY - 36}" r="5" fill="#9ad4ff" opacity=".35"/>`;
  front += lights(pw - 6, GY + 6, lo("reactor"), "#3fd0b0", 6);

  /* ----- Wohnviertel (Rumpf) ----- */
  hull += `<clipPath id="hc-${k}"><path d="${hp}"/></clipPath><g style="filter:${paintFilter()}">`;
  const r0 = X.res0, r1 = X.res1, rw = r1 - r0;
  if (H === 0) {
    hull += `<path d="M${r0},${GY} V${t + 18} l6,-6 l4,8 l6,-10 V${GY} Z M${r0 + 24},${GY} V${t + 10} l8,4 l4,-6 l6,10 V${GY} Z M${r0 + 54},${GY} V${t + 22} l10,-4 l6,6 V${GY} Z" fill="#7a6a5a" stroke="#3a3028" stroke-width="1.2"/>
      ${[[r0 + 4, t + 24], [r0 + 30, t + 18], [r0 + 58, t + 28]].map(([x, y]) => `<rect x="${x}" y="${y}" width="6" height="7" fill="#1a1410"/>`).join("")}
      <path d="M${r0 - 4},${GY} q10,-8 20,0 q8,-6 16,0 q12,-9 24,0 q10,-6 20,0z" fill="#5a4a3a"/>`;
  } else {
    const houses = H === 1 ? 4 : H === 2 ? 5 : 3, hw = rw / houses;
    for (let i = 0; i < houses; i++) {
      const x = r0 + i * hw, w = hw - 3;
      if (H === 1) { const top = t + 18 + (i % 2) * 4, col = ["#d8c8a8", "#c8b898", "#e0d0b0", "#c0b090"][i % 4];
        hull += `<rect x="${x}" y="${top}" width="${w}" height="${GY - top}" fill="${col}" stroke="#5a5040" stroke-width="1"/><path d="M${x - 2},${top} L${x + w / 2},${top - 9} L${x + w + 2},${top} Z" fill="#a85a3a" stroke="#5a2a1a" stroke-width="1"/>${win(x + 3, top + 4, 5, 5, i % 2)}<rect x="${x + w - 8}" y="${GY - 9}" width="5" height="9" fill="#7a5a3a"/>`; }
      if (H === 2) { const top = t + 6 + (i % 3) * 5, col = ["#e8a87a", "#8ac8a8", "#e8d07a", "#a8b8e8", "#e88a8a"][i];
        hull += `<rect x="${x}" y="${top}" width="${w}" height="${GY - top}" fill="${col}" stroke="#3a3a3a" stroke-width="1"/><path d="M${x - 1},${top} H${x + w + 1} V${top - 3} H${x - 1}z" fill="#5a5a5a"/>${[0, 1, 2].map(r => [0, 1].map(c => win(x + 3 + c * (w / 2), top + 5 + r * 9, 4, 5, (r + c + i) % 2)).join("")).join("")}`; }
      if (H === 3) { const top = t - 2 + (i % 2) * 8, col = ["#e8eef4", "#dce8e4", "#ece4dc"][i];
        hull += `<rect x="${x}" y="${top}" width="${w}" height="${GY - top}" fill="${col}" stroke="#5a6068" stroke-width="1"/><path d="M${x - 2},${top} H${x + w + 2}" stroke="#3fd0b0" stroke-width="3"/>${[0, 1, 2, 3, 4].map(r => [0, 1, 2].map(c => win(x + 3 + c * ((w - 6) / 3), top + 5 + r * 7.2, (w - 12) / 3, 4, (r * 3 + c + i) % 3 !== 0)).join("")).join("")}${[0, 1, 2, 3].map(r => `<path d="M${x},${top + 10 + r * 7.2} h${w}" stroke="#9aa4ae" stroke-width=".6"/>`).join("")}<circle cx="${x + 6}" cy="${top - 3}" r="3" fill="#5aa860"/><circle cx="${x + w - 6}" cy="${top - 3}" r="3.4" fill="#4a9850"/>`; }
    }
  }
  hull += `<g clip-path="url(#hc-${k})">${decalSVG(g)}</g></g>`;
  front += lights(r0 + 4, GY + 6, lo("hull"), "#7ed957");

  /* ----- Rathaus (Mitte, Kommandostand) ----- */
  const hx = X.hall, hw2 = 22 + H * 2, ht = t - 4 - H * 3;
  back += `<rect x="${hx - hw2}" y="${ht + 14}" width="${hw2 * 2}" height="${GY - ht - 14}" fill="${["#8a7a6a", "#d8ccb4", "#e8dcc4", "#f0e8d8"][H]}" stroke="#5a5040" stroke-width="1.2"/>
    <path d="M${hx - hw2 - 3},${ht + 14} L${hx},${ht + 2} L${hx + hw2 + 3},${ht + 14} Z" fill="${["#5a4a3a", "#7a8a9a", "#3a6a8a", "#2a5a7a"][H]}" stroke="#2a2a2a" stroke-width="1"/>
    ${H >= 1 ? [-1, 1].map(s => [0, 1].map(r => win(hx + s * (hw2 - 9) - 3, ht + 20 + r * 10, 6, 6, r === 0)).join("")).join("") : `<path d="M${hx - 10},${ht + 20} l6,8 l-4,6" stroke="#2a2018" stroke-width="1.6" fill="none"/>`}
    <rect x="${hx - 5}" y="${GY - 12}" width="10" height="12" rx="5" fill="#5a3a2a"/>`;
  if (H >= 2) back += `<rect x="${hx - 6}" y="${ht - 16}" width="12" height="18" fill="${["#8a7a6a", "#d8ccb4", "#e8dcc4", "#f0e8d8"][H]}" stroke="#5a5040" stroke-width="1"/><circle cx="${hx}" cy="${ht - 8}" r="4" fill="#ffffff" stroke="#3a3a3a" stroke-width=".8"/><path d="M${hx},${ht - 8} v-3 M${hx},${ht - 8} h2.4" stroke="#1a1a1a" stroke-width=".8"/><path d="M${hx - 8},${ht - 16} L${hx},${ht - 26} L${hx + 8},${ht - 16} Z" fill="#2a5a7a"/>`;
  if (H >= 1) back += `<path d="M${hx},${ht + (H >= 2 ? -26 : 2)} v-12" stroke="#5a5a5a" stroke-width=".9"/><path class="sail" d="M${hx},${ht + (H >= 2 ? -38 : -10)} l10,2.5 l-10,2.5z" fill="${["#888", "#3fd0b0", "#4aa8ff", "#ff7a59"][H]}"/>`;
  const px = hx - hw2 + 9, py = ht + 26;
  front += `<circle cx="${px}" cy="${py - 4}" r="2.6" fill="#e0a878"/><path d="M${px - 3},${py + 1} q3,-3 6,0" fill="#3a5a8a"/><path d="M${px - 3},${py - 6} q3,-3 6,0" fill="${["#5a3a1a", "#8a3a2a", "#2a2a2a", "#c9a24a"][H]}"/>`;

  /* ----- Funkturm (Scanner) ----- */
  const sx = X.tower, sb = GY;
  if (S === 0) front += `<path d="M${sx},${sb} L${sx + 2},${sb - 22} L${sx + 14},${sb - 30}" stroke="#7a7f86" stroke-width="1.6" fill="none"/><path d="M${sx - 3},${sb} L${sx + 3},${sb}" stroke="#5a5f66" stroke-width="2"/>`;
  if (S === 1) front += `<path d="M${sx - 5},${sb} L${sx},${sb - 46} L${sx + 5},${sb} M${sx - 4},${sb - 10} L${sx + 4},${sb - 20} M${sx + 4},${sb - 10} L${sx - 4},${sb - 20} M${sx - 2},${sb - 26} L${sx + 2},${sb - 34}" stroke="#a8aeb6" stroke-width="1" fill="none"/><circle class="blink" cx="${sx}" cy="${sb - 47}" r="1.6" fill="#ff4b5c"/>`;
  if (S === 2) front += `<path d="M${sx - 6},${sb} L${sx - 1.5},${sb - 62} M${sx + 6},${sb} L${sx + 1.5},${sb - 62}" stroke="#d8dce0" stroke-width="2"/>${[12, 24, 36, 48].map(y => `<path d="M${sx - 5 + y * .07},${sb - y} H${sx + 5 - y * .07}" stroke="#d8dce0" stroke-width="1"/>`).join("")}<g class="dish"><path d="M${sx + 2},${sb - 44} q8,-2 10,6 z" fill="#e8ecf0" stroke="#8a9098" stroke-width=".8"/></g><circle class="blink" cx="${sx}" cy="${sb - 64}" r="1.8" fill="#ff4b5c"/>`;
  if (S === 3) front += `<path d="M${sx - 4},${sb} L${sx - 2},${sb - 56} H${sx + 2} L${sx + 4},${sb}" fill="#e8ecf0" stroke="#8a9098" stroke-width=".8"/><circle cx="${sx}" cy="${sb - 62}" r="8" fill="#c9d3e0" stroke="#5a6068" stroke-width="1"/><path d="M${sx - 8},${sb - 62} h16" stroke="#4aa8ff" stroke-width="2"/><path d="M${sx},${sb - 70} V${sb - 88}" stroke="#d8dce0" stroke-width="1.4"/><circle class="blink" cx="${sx}" cy="${sb - 89}" r="1.8" fill="#ff4b5c"/><circle class="ping" cx="${sx}" cy="${sb - 88}" r="5" fill="none" stroke="#9ad4ff" stroke-width=".8"/>`;
  front += lights(sx - 6, sb + 6, lo("scanner"), "#4aa8ff", 6);

  /* ----- Markt / Handel (Lager) ----- */
  const mk = X.mk0;
  if (C === 0) front += `<g transform="rotate(14 ${mk + 20} ${GY})"><rect x="${mk + 8}" y="${GY - 10}" width="24" height="10" fill="#7a5a3a" stroke="#3a2a1a" stroke-width="1"/><path d="M${mk + 6},${GY - 10} l4,-8 h20 l4,8" fill="#8a7a6a" opacity=".7"/></g><rect x="${mk + 30}" y="${GY - 6}" width="6" height="6" fill="#6a4a2a" transform="rotate(-20 ${mk + 33} ${GY - 3})"/>`;
  if (C === 1) front += `<rect x="${mk + 6}" y="${GY - 12}" width="30" height="12" fill="#a8743f" stroke="#5a3a1a" stroke-width="1"/><path d="M${mk + 3},${GY - 12} l3,-8 h30 l3,8z" fill="#ff7a59"/><path d="M${mk + 3},${GY - 12} q3,3 6.6,0 q3,3 6.6,0 q3,3 6.6,0 q3,3 6.6,0 q3,3 6.6,0" fill="#ffffff" stroke="#ff7a59" stroke-width=".6"/>${[0, 1, 2].map(i => `<circle cx="${mk + 12 + i * 8}" cy="${GY - 9}" r="2.2" fill="${["#ff4b5c", "#ffc94a", "#7ed957"][i]}"/>`).join("")}`;
  if (C === 2) front += `<rect x="${mk}" y="${t + 10}" width="44" height="${GY - t - 10}" fill="#dce6f0" stroke="#4a5a6a" stroke-width="1"/><rect x="${mk - 2}" y="${t + 6}" width="48" height="7" fill="#4aa8ff"/><text x="${mk + 22}" y="${t + 11.4}" text-anchor="middle" font-family="Rubik, sans-serif" font-weight="700" font-size="5" fill="#ffffff">LADEN</text><rect x="${mk + 4}" y="${GY - 16}" width="22" height="13" fill="#9ad4ff"/><rect x="${mk + 30}" y="${GY - 16}" width="9" height="16" fill="#5a6a7a"/>`;
  if (C === 3) front += `<rect x="${mk - 4}" y="${t - 6}" width="52" height="${GY - t + 6}" fill="#c9d8e8" stroke="#3a4a5a" stroke-width="1"/>${[0, 1, 2, 3, 4].map(r => `<rect x="${mk}" y="${t + r * 9}" width="44" height="6" fill="#4aa8ff" opacity="${.55 + r * .08}"/>`).join("")}<rect x="${mk - 6}" y="${t - 12}" width="56" height="7" fill="#ff7a59"/><text x="${mk + 22}" y="${t - 6.8}" text-anchor="middle" font-family="Rubik, sans-serif" font-weight="700" font-size="5" fill="#ffffff">KAUFHAUS</text><rect x="${mk + 14}" y="${GY - 10}" width="16" height="10" fill="#2a3a4a"/>`;
  front += lights(mk + 6, GY + 6, lo("cargo"), "#ffc94a");

  // unsichtbare Klickzonen
  const z = (part, shape) => shape.replace(/^<(\w+)/, `<$1 class="zone" data-part="${part}" fill="#ffffff" fill-opacity="0"`);
  const zones = [
    z("cargo", `<rect x="${mk - 6}" y="${t - 14}" width="58" height="${GY - t + 14}"/>`),
    z("hull", `<rect x="${r0 - 4}" y="${t - 4}" width="${rw + 8}" height="${GY - t + 4}"/>`),
    z("engine", `<rect x="${l - 50}" y="${GY}" width="${n - l + 100}" height="${b - GY + 2}"/>`),
    z("cockpit", `<rect x="${hx - hw2}" y="${ht}" width="${hw2 * 2}" height="${GY - ht}"/>`),
    z("reactor", `<rect x="${pw - 20}" y="${GY - 50}" width="44" height="50"/>`),
    z("scanner", `<rect x="${sx - 10}" y="${GY - 90}" width="22" height="90"/>`),
  ].join("");
  return `<g class="ship t${H}">${back}${hull}${front}${zones}</g>`;
}

/* Stadtstufen: Kleinstadt (Kirche, zweite Häuserreihe) und Metropole (Hochhauskulisse, Brücke). */
function vehLayers(L, k) {
  const V = veh(); if (!V) return ["", ""];
  const H = Math.min(3, Math.floor(L.hull / 3)), g = GEO[H], { l, t, n } = g;
  const col = ["#5a5a5a", "#7a8a9a", "#8a9aae", "#9aaac0"][H], pf = `style="filter:${paintFilter()}"`;
  let back = "";
  const row = Array.from({ length: 9 }, (_, i) => { const x = l - 30 + i * ((n - l + 70) / 9), h = 22 + ((i * 37) % 18), w = (n - l + 70) / 9 - 3;
    return `<rect x="${x}" y="${GY - 8 - h - 14}" width="${w}" height="${h + 14}" fill="${col}" opacity=".55"/>${H ? `<rect x="${x + 3}" y="${GY - h - 16}" width="${w - 6}" height="2" fill="#ffd27a" opacity=".5"/>` : ""}`; }).join("");
  back += `<g ${pf}>${row}<path d="M${l + 30},${GY - 30} V${GY - 72} l6,-12 l6,12 V${GY - 30}" fill="${col}" opacity=".7"/><circle cx="${l + 36}" cy="${GY - 62}" r="3" fill="${H ? "#ffd27a" : "#2a2a2a"}" opacity=".7"/></g>`;
  if (V >= 2) {
    const sky = Array.from({ length: 7 }, (_, i) => { const x = l - 20 + i * ((n - l + 40) / 7), h = 60 + ((i * 53) % 46), w = 16 + (i % 3) * 6;
      return `<rect x="${x}" y="${GY - h - 20}" width="${w}" height="${h}" fill="${H ? "#2a4a6a" : "#3a3a3a"}" opacity=".75"/>${H ? Array.from({ length: Math.floor(h / 8) }, (_, r) => `<rect x="${x + 3}" y="${GY - h - 16 + r * 8}" width="${w - 6}" height="2" fill="#9ad4ff" opacity="${.25 + ((r + i) % 3) * .15}"/>`).join("") : ""}${i === 3 ? `<path d="M${x + w / 2},${GY - h - 20} v-14" stroke="#c9d3e0" stroke-width="1"/><circle class="blink" cx="${x + w / 2}" cy="${GY - h - 35}" r="1.6" fill="#ff4b5c"/>` : ""}`; }).join("");
    back = `<g ${pf}>${sky}</g>` + back;
    back += `<path d="M${n - 10},${GY - 20} Q${n + 30},${GY - 50} ${n + 70},${GY - 20}" stroke="${H ? "#ff7a59" : "#6a5a4a"}" stroke-width="2.4" fill="none"/>${[0, 1, 2, 3, 4].map(i => `<path d="M${n + i * 16},${GY - 20 - Math.sin((i + .5) / 5 * Math.PI) * 24} V${GY - 20}" stroke="${H ? "#ff7a59" : "#6a5a4a"}" stroke-width=".8"/>`).join("")}<path d="M${n - 14},${GY - 20} H${n + 74}" stroke="#5a6068" stroke-width="2"/>`;
  }
  return [back, ""];
}
'''

CITY_SKY = r'''function sizeSkyObj(o) {
  const r = o.host.getBoundingClientRect(), d = devicePixelRatio || 1;
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
