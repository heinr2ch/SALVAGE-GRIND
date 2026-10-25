# Eisenfront Teil 1: Grafiken (Symbole, Emblem, Hund Rex, Brieftaube, Panzer, Gelände)

EMBLEM_TG = """          <path d="M31 36 V15" stroke="#e8d3a2" stroke-width="2.2" stroke-linecap="round"/>
          <path d="M32.5 16 Q44 24 43 33 H32.5 Z" fill="url(#emb)" stroke="#e8f7f5" stroke-width="1" stroke-linejoin="round"/>
          <path d="M29.5 19 Q22 26 23 33 H29.5 Z" fill="#e8f7f5" opacity=".85"/>
          <rect x="19" y="35" width="26" height="5" rx="2" fill="#7a4f2a" stroke="#e8d3a2" stroke-width="1.4"/>
          <path d="M13 44 q4.75 -3 9.5 0 t9.5 0 t9.5 0 t9.5 0" stroke="url(#emb)" stroke-width="2.4" fill="none" stroke-linecap="round"/>"""
EMBLEM_EF = """          <path d="M22 30 L25 23 H37 L40 30 Z" fill="#4a5a24" stroke="#e8dcb8" stroke-width="1.3" stroke-linejoin="round"/>
          <path d="M39 26 H52" stroke="#e8dcb8" stroke-width="2.4" stroke-linecap="round"/>
          <path d="M14 36 L18 30 H46 L50 36 Z" fill="#5a6a2c" stroke="#e8dcb8" stroke-width="1.4" stroke-linejoin="round"/>
          <rect x="13" y="36" width="38" height="8" rx="4" fill="#2a2d30" stroke="#e8dcb8" stroke-width="1.3"/>
          <circle cx="19" cy="40" r="2.2" fill="#e8dcb8"/><circle cx="26" cy="40" r="2.2" fill="#e8dcb8"/><circle cx="33" cy="40" r="2.2" fill="#e8dcb8"/><circle cx="40" cy="40" r="2.2" fill="#e8dcb8"/><circle cx="46" cy="40" r="2.2" fill="#e8dcb8"/>"""

ICONS_EF = r'''const ICONS = {
  scrap: `<svg viewBox="0 0 40 40"><path d="M17.5 4h5l1 4.2 3 1.3 3.7-2.3 3.5 3.5-2.3 3.7 1.3 3 4.3 1v5l-4.3 1-1.3 3 2.3 3.7-3.5 3.5-3.7-2.3-3 1.3-1 4.3h-5l-1-4.3-3-1.3-3.7 2.3-3.5-3.5 2.3-3.7-1.3-3-4.3-1v-5l4.3-1 1.3-3-2.3-3.7 3.5-3.5 3.7 2.3 3-1.3z" fill="#7a8088" stroke="#c9ccd1" stroke-width="1.6" stroke-linejoin="round"/><circle cx="20" cy="20" r="5.5" fill="#2a2d30" stroke="#c9ccd1" stroke-width="1.6"/></svg>`,
  cell: `<svg viewBox="0 0 40 40"><path d="M10 9 h14 l6 6 v19 a2 2 0 0 1 -2 2 h-18 a2 2 0 0 1 -2 -2 v-23 a2 2 0 0 1 2 -2z" fill="#4f6b2c" stroke="#b5cc6a" stroke-width="2" stroke-linejoin="round"/><path d="M12 9 v-3 h6 v3" stroke="#b5cc6a" stroke-width="2" fill="none"/><path d="M12.5 16 L26 32 M26 16 L12.5 32" stroke="#b5cc6a" stroke-width="1.6" opacity=".7"/><rect x="25.5" y="7" width="4" height="4" rx="1" fill="#b5cc6a"/></svg>`,
  chip: `<svg viewBox="0 0 40 40"><rect x="5" y="12" width="30" height="16" rx="3" fill="#3a3d42" stroke="#a6acb4" stroke-width="2"/><path d="M11 12 v16 M29 12 v16" stroke="#a6acb4" stroke-width="1.6"/><rect x="14" y="15" width="12" height="10" rx="2" fill="#5a5f66"/><circle cx="8" cy="20" r="2" fill="#d9dde2"/><circle cx="32" cy="20" r="2" fill="#d9dde2"/><path d="M15 16 l10 8 M25 16 l-10 8" stroke="#2a2d30" stroke-width="1.2"/></svg>`,
  core: `<svg viewBox="0 0 40 40"><path d="M11 12 v-4 h5 v4 M18 12 v-4 h5 v4 M25 12 v-4 h5 v4" stroke="#e07a4a" stroke-width="1.8" fill="#8a4a2a"/><rect x="7" y="12" width="26" height="18" rx="2" fill="#6a3a22" stroke="#e07a4a" stroke-width="2"/><path d="M7 18 h-3 v6 h3 M33 18 h3 v6 h-3" stroke="#e07a4a" stroke-width="1.8" fill="none"/><circle cx="14" cy="21" r="2.4" fill="#2a1a10"/><circle cx="20" cy="21" r="2.4" fill="#2a1a10"/><circle cx="26" cy="21" r="2.4" fill="#2a1a10"/><path d="M10 27 h20" stroke="#ffb07a" stroke-width="1.2"/></svg>`,
  crystal: `<svg viewBox="0 0 40 40"><path d="M13 3 h14 l-3 12 h-8z" fill="#a33a2a"/><path d="M17.5 3 h5 l-1.3 12 h-2.4z" fill="#e8d6a0"/><circle cx="20" cy="25" r="11" fill="#c9952e" stroke="#ffe39a" stroke-width="2"/><path d="M20 17 l2.4 5 5.4 .6 -4 3.6 1.2 5.3 -5 -2.8 -5 2.8 1.2 -5.3 -4 -3.6 5.4 -.6z" fill="#fff1c8"/></svg>`,
  relic: `<svg viewBox="0 0 40 40"><path d="M5 31 L11 17 H29 L35 31 Z" fill="#b8862e" stroke="#ffe39a" stroke-width="2" stroke-linejoin="round"/><path d="M11 17 L15 11 H25 L29 17" fill="#e0b040" stroke="#ffe39a" stroke-width="1.6" stroke-linejoin="round"/><path d="M14 24 h12" stroke="#7a5608" stroke-width="1.4"/><path d="M8 8 l2 2 M32 8 l-2 2 M20 3.5 v3" stroke="#fff1c8" stroke-width="1.4" stroke-linecap="round"/></svg>`,
  beacon: `<svg viewBox="0 0 40 40"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#232a14" stroke="#d9c75a" stroke-width="2"/><rect x="9" y="9" width="22" height="15" rx="1.5" fill="#e8dcb8" stroke="#7a6a3a" stroke-width="1.2"/><path d="M9 9.5 l11 8.5 l11 -8.5" stroke="#7a6a3a" stroke-width="1.2" fill="none"/><circle cx="20" cy="18.5" r="3" fill="#a33a2a"/><path d="M5 9 a10 10 0 0 0 0 11 M35 9 a10 10 0 0 1 0 11" stroke="#d9c75a" stroke-width="1.6" fill="none" stroke-linecap="round"/>${band("FREE", "#d9c75a", "#232a14")}</svg>`,
  capsule: `<svg viewBox="0 0 40 40"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#2a2410" stroke="#e8b04a" stroke-width="2"/><path d="M11 12 q9 -11 18 0 z" fill="#e8dcb8" stroke="#a89a6a" stroke-width="1"/><path d="M11 12 l7 5 M29 12 l-7 5" stroke="#e8dcb8" stroke-width="1"/><rect x="11" y="16" width="18" height="11" rx="1" fill="#5a6a2c" stroke="#e8b04a" stroke-width="1.5"/><path d="M11 21.5 h18 M17 16 v11 M23 16 v11" stroke="#2a3214" stroke-width="1.2"/>${band("BONUS", "#e8b04a", "#2a2410")}</svg>`,
  warp: `<svg viewBox="0 0 40 40"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#2a1a12" stroke="#e07a4a" stroke-width="2"/><circle cx="20" cy="16.5" r="11" fill="#2a2d22" stroke="#e8b04a" stroke-width="1.8"/><path d="M20 7 l3 9.5 -3 9.5 -3 -9.5z" fill="#e07a4a"/><path d="M17 16.5 h6 l-3 9.5z" fill="#e8dcb8"/><circle cx="20" cy="16.5" r="1.6" fill="#fff"/><path d="M20 5.5 v2 M31 16.5 h-2 M9 16.5 h2" stroke="#e8b04a" stroke-width="1.2"/>${band("BONUS", "#e07a4a", "#2a1a12")}</svg>`,
};
'''

WILD_EF = r'''ICONS.wild = `<svg viewBox="0 0 40 40"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#1e2410" stroke="url(#wildG)" stroke-width="2.4"/><path d="M28 5 a7 7 0 0 0 -8.5 9 L8 25.5 a3 3 0 0 0 4.2 4.2 L23.7 18.2 a7 7 0 0 0 9 -8.5 l-4.2 4.2 -4 -1 -1 -4z" fill="#e2e6ea" stroke="#6a7078" stroke-width="1.2" stroke-linejoin="round"/><circle cx="10.3" cy="27.8" r="1.2" fill="#6a7078"/><path d="M5 5 l1 2.4 2.4 1 -2.4 1 -1 2.4 -1 -2.4 -2.4 -1 2.4 -1z" fill="#ffffff"/>${band("WILD", "url(#wildG)", "#1e2410")}</svg>`;'''

DOG_SVG = '''    <svg viewBox="0 0 80 92" data-mood="normal" id="bipSvg" aria-hidden="true">
      <ellipse class="bip-thrust" cx="40" cy="88" rx="17" ry="2.6" fill="#000000" opacity=".28"/>
      <path d="M55 76 q15 -1 13 -17" stroke="#8a5a2a" stroke-width="5" fill="none" stroke-linecap="round"/>
      <ellipse cx="40" cy="70" rx="17" ry="16" fill="#b07a42" stroke="#5a3a1a" stroke-width="1.8"/>
      <ellipse cx="40" cy="73" rx="9" ry="11" fill="#ead6ab"/>
      <path class="bip-heart" d="M40 77 l-3.5 -3.5 a2.3 2.3 0 0 1 3.5 -3 a2.3 2.3 0 0 1 3.5 3 z" fill="#d9653b"/>
      <ellipse cx="32" cy="85" rx="5.5" ry="3.2" fill="#ead6ab" stroke="#5a3a1a" stroke-width="1.2"/><ellipse cx="48" cy="85" rx="5.5" ry="3.2" fill="#ead6ab" stroke="#5a3a1a" stroke-width="1.2"/>
      <circle cx="40" cy="35" r="18" fill="#b07a42" stroke="#5a3a1a" stroke-width="2"/>
      <ellipse cx="49" cy="35" rx="7.5" ry="6.5" fill="#8a5a2a" opacity=".75"/>
      <g class="bip-arm l"><path d="M25 21 q-13 2 -11 23 q9 -2 13 -13z" fill="#6a4422" stroke="#3a2410" stroke-width="1.4"/></g>
      <g class="bip-arm r"><path d="M55 21 q13 2 11 23 q-9 -2 -13 -13z" fill="#6a4422" stroke="#3a2410" stroke-width="1.4"/></g>
      <path d="M24 24 q16 -15 32 0 l-2 3 h-28z" fill="#5a6a2c" stroke="#2a3214" stroke-width="1.2"/><path d="M26 27 h28" stroke="#2a3214" stroke-width="2.2"/>
      <ellipse cx="40" cy="45" rx="10.5" ry="7.5" fill="#ead6ab" stroke="#5a3a1a" stroke-width="1.2"/>
      <ellipse cx="40" cy="41" rx="4.2" ry="3" fill="#1a1208"/><ellipse cx="38.8" cy="40.2" rx="1.2" ry=".7" fill="#ffffff" opacity=".6"/>
      <path d="M26 55 q14 7 28 0" stroke="#a33a2a" stroke-width="4" fill="none" stroke-linecap="round"/>
      <circle class="bip-ant" cx="40" cy="59" r="3" fill="#e8b04a" stroke="#7a5608" stroke-width="1"/>
      <circle cx="25" cy="43" r="2.8" fill="#ff9ac6" opacity=".45"/><circle cx="55" cy="43" r="2.8" fill="#ff9ac6" opacity=".45"/>
      <g class="m m-normal"><g class="bip-eyes"><ellipse cx="32" cy="34" rx="3" ry="3.8" fill="#1a1208"/><ellipse cx="48" cy="34" rx="3" ry="3.8" fill="#1a1208"/><circle cx="33" cy="32.6" r="1" fill="#fff"/><circle cx="49" cy="32.6" r="1" fill="#fff"/></g><path d="M36 48 q4 3 8 0" stroke="#3a2410" stroke-width="1.4" fill="none" stroke-linecap="round"/></g>
      <g class="m m-happy"><path d="M28 35 q4 -5 8 0 M44 35 q4 -5 8 0" stroke="#1a1208" stroke-width="2.4" fill="none" stroke-linecap="round"/><path d="M35 47 q5 7 10 0z" fill="#5a1a10"/><path d="M38 49 q2 5 4 0" fill="#e86a7a"/></g>
      <g class="m m-excited"><path d="M32 28 l1.5 3.3 3.6 .4 -2.7 2.4 .8 3.5 -3.2 -1.8 -3.2 1.8 .8 -3.5 -2.7 -2.4 3.6 -.4z M48 28 l1.5 3.3 3.6 .4 -2.7 2.4 .8 3.5 -3.2 -1.8 -3.2 1.8 .8 -3.5 -2.7 -2.4 3.6 -.4z" fill="#e8b04a" stroke="#7a5608" stroke-width=".6"/><path d="M35 47 q5 7 10 0z" fill="#5a1a10"/><path d="M38 49 q2 7 4 0" fill="#e86a7a"/></g>
      <g class="m m-sad"><path d="M27 29 l7 2.5 M53 29 l-7 2.5" stroke="#1a1208" stroke-width="2" stroke-linecap="round"/><ellipse cx="32" cy="35.5" rx="2.6" ry="3" fill="#1a1208"/><ellipse cx="48" cy="35.5" rx="2.6" ry="3" fill="#1a1208"/><path d="M36 50 q4 -3 8 0" stroke="#3a2410" stroke-width="1.4" fill="none"/><path class="bip-tear" d="M51 39 q2 3 0 5 q-2 -2 0 -5z" fill="#8fbfdf"/></g>
      <g class="m m-wow"><circle cx="32" cy="34" r="4.6" fill="#1a1208"/><circle cx="48" cy="34" r="4.6" fill="#1a1208"/><circle cx="33.5" cy="32.3" r="1.6" fill="#fff"/><circle cx="49.5" cy="32.3" r="1.6" fill="#fff"/><ellipse cx="40" cy="49" rx="2.6" ry="2.4" fill="#5a1a10"/></g>
    </svg>
'''

PIGEON = r'''const DRONE = `<g class="drone">
  <path d="M-2 0 q-13 -13 -26 -6 q12 0 21 9z" fill="#b8c0c8" stroke="#4a525a" stroke-width="1.1"><animateTransform attributeName="transform" type="rotate" values="0 -2 0;-30 -2 0;0 -2 0" dur=".26s" repeatCount="indefinite"/></path>
  <path d="M2 0 q13 -13 26 -6 q-12 0 -21 9z" fill="#a6aeb6" stroke="#4a525a" stroke-width="1.1"><animateTransform attributeName="transform" type="rotate" values="0 2 0;30 2 0;0 2 0" dur=".26s" repeatCount="indefinite"/></path>
  <ellipse cx="0" cy="3" rx="11" ry="6.5" fill="#9aa3ad" stroke="#4a525a" stroke-width="1.1"/>
  <path d="M-11 3 l-7 -3 l1 6z" fill="#6a727a"/>
  <path d="M5 1 q4 -3 6 1" fill="#5a8a6a" opacity=".8"/>
  <circle cx="9" cy="-2" r="4.6" fill="#8a929c" stroke="#4a525a" stroke-width="1.1"/>
  <circle cx="10.4" cy="-3" r="1.2" fill="#e07a2a"/>
  <path d="M13 -2 l5 1.4 l-5 1.4z" fill="#3a3d42"/>
  <rect x="-1" y="9" width="4" height="3" rx="1" fill="#a33a2a"/>
</g>`;
'''

EMBERS = r'''function drawStars(dt) {
  scx.clearRect(0, 0, innerWidth, innerHeight);
  // langsam aufsteigende Funken und Staub in der Werkhalle
  for (const s of stars) {
    s.y -= (0.012 + warpBoost * .5) * s.z * dt; s.p += 0.0015 * dt;
    if (s.y < -10) { s.y = innerHeight + 10; s.x = Math.random() * innerWidth; }
    const x = s.x + Math.sin(s.p * 2) * 6 * s.z, a = (.08 + .22 * s.z) * (.6 + .4 * Math.sin(s.p * 5));
    scx.fillStyle = s.z > .8 ? `rgba(255,170,90,${a})` : `rgba(220,210,190,${a * .6})`;
    scx.fillRect(x, s.y, s.z * 1.8, s.z * 1.8);
  }
}
'''

TANK_SVG = r'''/* Panzergrafik: jede Kategorie hat 4 sichtbare Ausbaustufen, Zwischenstufen zeigen kleine Lichter. Boden bei y = 126. */
const VB = { x: 48, y: 2, w: 304, h: 152 };
const WL = 126;
const GEO = [{ l: 112, t: 100, b: 126, n: 282 }, { l: 102, t: 98, b: 126, n: 296 }, { l: 94, t: 96, b: 126, n: 310 }, { l: 86, t: 94, b: 126, n: 324 }];
function hullPath(H, g) {
  const { l, t, b, n } = g, tb = b - 12;
  return `M${l},${t + 6} L${l + 10},${t} L${n - 24},${t} L${n},${t + 10} L${n - 6},${tb} L${l + 4},${tb} Z`;
}
function partAnchors(L) {
  const H = Math.min(3, Math.floor(L.hull / 3)), g = GEO[H], tx = g.l + (g.n - g.l) * .55;
  return { hull: [(g.l + g.n) / 2 - 30, g.b - 14], engine: [g.l + 4, g.t + 2], scanner: [186, g.t - 44], cargo: [g.l + 34, g.t - 10], reactor: [tx + 34, g.t - 12] };
}
function shipSVG(L, k = "a") {
  const T = id => Math.min(3, Math.floor(L[id] / 3)), lo = id => L[id] >= 9 ? 3 : L[id] % 3;
  const H = T("hull"), E = T("engine"), S = T("scanner"), C = T("cargo"), R = T("reactor");
  const g = GEO[H], { l, t, b, n } = g, hp = hullPath(H, g), tb = b - 12, tx = Math.round(l + (n - l) * .55);
  const lights = (x, y, cnt, col, dx = 7) => Array.from({ length: cnt }, (_, i) => `<circle class="blink d${i + 1}" cx="${x + i * dx}" cy="${y}" r="1.9" fill="${col}"/>`).join("");
  const armor = ["#6e4a32", "#5f5a3e", "#4f5a2c", "#56632e"][H], dark = ["#3a2618", "#33301f", "#2a3214", "#1e2410"][H], light = ["#9a6a48", "#8a8458", "#7a8a44", "#9aa860"][H];
  let back = "", hull = "", det = "", front = "";

  /* ----- Schatten und Ketten ----- */
  back += `<ellipse cx="${(l + n) / 2}" cy="${b + 1}" rx="${(n - l) / 2 + 12}" ry="4" fill="#000000" opacity=".3"/>`;
  const trackEnd = H === 0 ? n - 42 : n + 2;
  back += `<rect x="${l - 4}" y="${tb}" width="${trackEnd - l + 4}" height="${b - tb}" rx="${(b - tb) / 2}" fill="#26282b" stroke="#55595f" stroke-width="1.6"/>
    <rect class="tracks" x="${l - 2}" y="${tb + 1}" width="${trackEnd - l}" height="${b - tb - 2}" rx="${(b - tb) / 2 - 1}" fill="none" stroke="#6a6f76" stroke-width="1.4" stroke-dasharray="2 3"/>`;
  const wheels = 5 + H, step = (trackEnd - l - 8) / (wheels - 1);
  for (let i = 0; i < wheels; i++) { const x = l + 2 + i * step; back += `<circle cx="${x}" cy="${b - 6}" r="4.6" fill="#3a3d42" stroke="#7a8088" stroke-width="1.2"/><circle cx="${x}" cy="${b - 6}" r="1.4" fill="#9aa0a8"/>`; }
  if (H === 0) back += `<path d="M${n - 40},${b - 1} q10,2 20,0 t22,1" stroke="#3a3d42" stroke-width="4" fill="none" stroke-dasharray="3 1.5"/><circle cx="${n - 24}" cy="${b - 5}" r="4.6" fill="#3a3d42" stroke="#7a8088" stroke-width="1.2" opacity=".8"/>`;

  /* ----- Motor (hinten) ----- */
  if (E === 0) back += `<path d="M${l + 6},${t + 2} l-4,-9 l5,-2" stroke="#4a4038" stroke-width="3" fill="none" stroke-linecap="round"/><ellipse cx="${l + 10}" cy="${t + 4}" rx="9" ry="3" fill="#1a1612" opacity=".6"/>`;
  if (E >= 1) back += `<path d="M${l + 8},${t + 1} V${t - 12} h6" stroke="#5a5f66" stroke-width="3.2" fill="none" stroke-linecap="round"/>`;
  if (E >= 2) back += `<path d="M${l + 18},${t + 1} V${t - 9} h5" stroke="#5a5f66" stroke-width="3.2" fill="none" stroke-linecap="round"/><rect x="${l + 22}" y="${t - 3}" width="22" height="4" rx="1" fill="#2a2d30"/><path d="M${l + 25},${t - 3} v4 M${l + 30},${t - 3} v4 M${l + 35},${t - 3} v4 M${l + 40},${t - 3} v4" stroke="#6a6f76" stroke-width="1"/>`;
  if (E === 3) back += `<rect x="${l - 2}" y="${t - 9}" width="18" height="10" rx="3" fill="#3a3f46" stroke="#9aa0a8" stroke-width="1.4"/><path class="pulse" d="M${l + 1},${t - 6} h12 M${l + 1},${t - 3} h12" stroke="#ff9a3c" stroke-width="1.2"/>`;
  front += lights(l + 14, t + 8, lo("engine"), "#ff9a3c");

  /* ----- Rumpf ----- */
  hull += `<clipPath id="hc-${k}"><path d="${hp}"/></clipPath><g style="filter:${paintFilter()}">`;
  hull += `<path d="${hp}" fill="${armor}" stroke="${dark}" stroke-width="1.8" stroke-linejoin="round"/>`;
  det += `<path d="M${l + 10},${t + 1} H${n - 24}" stroke="${light}" stroke-width="1.2" opacity=".7"/>`;
  if (H === 0) det += `${[[l + 30, t + 10, 9, 5], [l + 90, t + 14, 12, 6], [n - 50, t + 8, 8, 4]].map(([x, y, rx, ry]) => `<ellipse cx="${x}" cy="${y}" rx="${rx}" ry="${ry}" fill="#8a4a2a" opacity=".55"/>`).join("")}
    <circle cx="${l + 60}" cy="${t + 9}" r="2.6" fill="#120c08"/><circle cx="${l + 66}" cy="${t + 13}" r="1.6" fill="#120c08"/><circle cx="${n - 40}" cy="${t + 12}" r="2" fill="#120c08"/>
    <path d="M${l + 44},${t + 3} l6,9 M${n - 70},${t + 4} l-4,8" stroke="${dark}" stroke-width="1.4"/>`;
  if (H === 1) det += `<rect x="${l + 26}" y="${t + 4}" width="22" height="9" fill="#7a6a4a" stroke="#e8b04a" stroke-width=".8" stroke-dasharray="1.5 1.5"/><rect x="${n - 64}" y="${t + 6}" width="18" height="8" fill="#4a5038" stroke="#e8b04a" stroke-width=".8" stroke-dasharray="1.5 1.5"/>`;
  if (H >= 2) det += `${Array.from({ length: 16 }, (_, i) => `<circle cx="${l + 14 + i * ((n - l - 40) / 15)}" cy="${t + 4}" r=".9" fill="${dark}"/>`).join("")}<path d="M${l + 50},${t} v${tb - t} M${n - 60},${t} v${tb - t}" stroke="${dark}" stroke-width="1" opacity=".6"/>`;
  if (H === 3) det += `<path d="M${l + 20},${t + 4} q12,-4 22,3 q-6,6 -18,4z M${l + 80},${t + 10} q14,-6 26,2 q-8,6 -22,5z M${n - 70},${t + 3} q12,-2 20,5 q-10,4 -18,1z" fill="#3a4420" opacity=".8"/><path d="M${l + 54},${t + 12} q10,-3 16,2 q-6,4 -14,3z M${n - 36},${t + 10} q8,-3 12,2 q-5,3 -10,2z" fill="#7a7048" opacity=".7"/>`;
  if (H >= 1) det += `<text x="${l + 12}" y="${tb - 3}" font-family="JetBrains Mono, monospace" font-size="4.2" font-weight="700" fill="${H === 1 ? "#e8dcb8" : "#e8dcb8"}" opacity=".7">WERFT HEINR2CH</text><text x="${n - 52}" y="${tb - 4}" font-family="Black Ops One, sans-serif" font-size="8" fill="#e8dcb8" opacity=".85">PZ-7</text>`;
  hull += `<g clip-path="url(#hc-${k})">${det}${decalSVG(g)}<path d="${hp}" fill="url(#shadeG)"/></g></g>`;
  if (H >= 2) front += `<rect x="${l + 2}" y="${tb - 3}" width="${n - l - 10}" height="7" rx="1.5" fill="${armor}" stroke="${dark}" stroke-width="1.2"/>${Array.from({ length: 8 }, (_, i) => `<circle cx="${l + 10 + i * ((n - l - 28) / 7)}" cy="${tb + .5}" r=".9" fill="${light}"/>`).join("")}`;
  if (H === 3) front += `${[0, 1, 2].map(i => `<rect x="${n - 58 + i * 9}" y="${t + 5}" width="7" height="10" rx="1.2" fill="#3a3d42" stroke="#6a6f76" stroke-width=".8"/>`).join("")}`;
  front += lights(l + 20, b + 5, lo("hull"), "#d9b27c");

  /* ----- Lager auf dem Heck ----- */
  const cx0 = l + 14, cw = Math.max(24, tx - 34 - cx0), sc = Math.min(1, cw / 60);
  let cg = "";
  if (C === 0) cg = `<path d="M0,0 V-6 H40 V0 M10,-6 V0 M20,-6 V0 M30,-6 V0" stroke="#6a6f76" stroke-width="1.4" fill="none"/>`;
  if (C >= 1) cg += `<rect x="2" y="-13" width="20" height="13" rx="1" fill="#5a6a2c" stroke="#2a3214" stroke-width="1.2"/><path d="M2,-6.5 h20 M8,-13 v13 M16,-13 v13" stroke="#2a3214" stroke-width="1"/>`;
  if (C >= 2) cg += [26, 36].map(x => `<rect x="${x}" y="-14" width="8" height="14" rx="1.5" fill="#4f6b2c" stroke="#b5cc6a" stroke-width="1"/><path d="M${x + 1},-12 l6,10 M${x + 7},-12 l-6,10" stroke="#b5cc6a" stroke-width=".7" opacity=".7"/>`).join("");
  if (C === 3) cg += `<path d="M-2,-13 q24,-14 48,0 v13 h-48z" fill="#7a7048" stroke="#4a4428" stroke-width="1.2" opacity=".95"/><path d="M8,-17 v17 M22,-20 v20 M36,-17 v17" stroke="#4a4428" stroke-width="1"/><circle cx="54" cy="-8" r="8" fill="#26282b" stroke="#7a8088" stroke-width="1.6"/><circle cx="54" cy="-8" r="2.4" fill="#9aa0a8"/>`;
  front += `<g transform="translate(${cx0} ${t}) scale(${sc.toFixed(3)})">${cg}</g>`;
  front += lights(cx0, b + 5, lo("cargo"), "#ffc94a");

  /* ----- Turm, Kanone, Kommandant ----- */
  const tw = 26 + H * 2;
  front += `<path d="M${tx - tw},${t} L${tx - tw + 6},${t - 20} L${tx + tw - 10},${t - 20} L${tx + tw},${t} Z" fill="${armor}" stroke="${dark}" stroke-width="1.8" stroke-linejoin="round"/>
    <path d="M${tx - tw + 6},${t - 20} L${tx + tw - 10},${t - 20}" stroke="${light}" stroke-width="1.2"/>
    ${H === 0 ? `<ellipse cx="${tx + 6}" cy="${t - 10}" rx="6" ry="3.5" fill="#8a4a2a" opacity=".6"/>` : ""}
    ${H === 3 ? `<path d="M${tx - 12},${t - 14} q8,-4 16,1 q-6,4 -14,2z" fill="#3a4420" opacity=".8"/>` : ""}`;
  const mx = tx + tw, my = t - 10, bl = [30, 40, 54, 66][R], bt = [3.4, 3.6, 4, 4.4][R];
  front += `<rect x="${mx - 4}" y="${my - 6}" width="8" height="12" rx="2" fill="${armor}" stroke="${dark}" stroke-width="1.4"/>`;
  if (R === 0) front += `<path d="M${mx + 3},${my} L${mx + 18},${my - 1} L${mx + 30},${my + 5}" stroke="#5a4a3a" stroke-width="${bt}" fill="none" stroke-linecap="round"/><circle class="flick" cx="${mx + 30}" cy="${my + 5}" r="1.4" fill="#8a4a2a"/>`;
  else front += `<path d="M${mx + 3},${my} H${mx + bl}" stroke="${R === 3 ? "#7a8a50" : "#5a5f4a"}" stroke-width="${bt}" stroke-linecap="butt"/><path d="M${mx + 3},${my - bt / 2 + .6} H${mx + bl}" stroke="#ffffff" stroke-width=".7" opacity=".25"/>`;
  if (R >= 2) front += `<rect x="${mx + bl - 3}" y="${my - bt / 2 - 1.6}" width="7" height="${bt + 3.2}" rx="1" fill="#3a3d42" stroke="#7a8088" stroke-width=".8"/>`;
  if (R === 3) front += `<rect x="${mx + bl * .5}" y="${my - bt / 2 - 1}" width="9" height="${bt + 2}" rx="${bt / 2 + 1}" fill="#6a7a40" stroke="#3a4420" stroke-width=".8"/>`;
  front += lights(mx - 2, my - 9, lo("reactor"), "#e07a4a", 6);
  const hx = tx - 8, hy = t - 20;
  const hat = [`<path d="M${hx - 5},${hy - 10} q5,-5 10,0z" fill="#7a5a3a"/>`, `<path d="M${hx - 5.5},${hy - 10} h11 l-1.5,-3.5 h-8z" fill="#5a6a2c"/><path d="M${hx - 6},${hy - 10} h4" stroke="#2a3214" stroke-width="1.2"/>`, `<path d="M${hx - 6},${hy - 9} q6,-9 12,0z" fill="#4f5a2c" stroke="#2a3214" stroke-width=".8"/>`, `<ellipse cx="${hx - 1}" cy="${hy - 11}" rx="6.5" ry="2.6" fill="#7a2a22"/><path d="M${hx - 5},${hy - 8} a5 5 0 0 1 10 0" stroke="#2a2d30" stroke-width="1.2" fill="none"/>`][H];
  front += `<ellipse cx="${hx}" cy="${hy}" rx="7" ry="2" fill="#2a2d30"/><path d="M${hx - 5},${hy} q0,-4 5,-4 q5,0 5,4z" fill="${["#7a6a5a", "#5a6a2c", "#4f5a2c", "#3a4428"][H]}"/><circle cx="${hx}" cy="${hy - 7.5}" r="3.6" fill="#e0a878"/><circle cx="${hx + 1.6}" cy="${hy - 8}" r=".6" fill="#1a1a1a"/>${hat}`;

  /* ----- Funk und Optik ----- */
  const sx = 186, sy = t - 18;
  if (S === 0) front += `<path d="M${sx},${sy} L${sx + 2},${sy - 14} L${sx + 10},${sy - 20}" stroke="#6a6f76" stroke-width="1.6" fill="none" stroke-linecap="round"/>`;
  if (S >= 1) front += `<path d="M${sx},${sy} V${sy - [0, 40, 46, 50][S]}" stroke="#8a9098" stroke-width="1.3"/><circle class="blink" cx="${sx}" cy="${sy - [0, 40, 46, 50][S]}" r="1.8" fill="#e07a4a"/><path class="sail" d="M${sx},${sy - [0, 40, 46, 50][S] + 4} l9,2.5 l-9,2.5z" fill="#d9c75a"/>`;
  if (S >= 2) front += `<rect x="${sx + 8}" y="${sy - 8}" width="8" height="7" rx="1" fill="#3a3d42" stroke="#8a9098" stroke-width=".8"/><rect x="${sx + 9.5}" y="${sy - 6.5}" width="5" height="2.5" fill="#8fbfdf" opacity=".8"/>`;
  if (S === 3) front += `<path d="M${sx - 10},${sy} V${sy - 16}" stroke="#8a9098" stroke-width="1.6"/><g class="dish"><path d="M${sx - 20},${sy - 22} Q${sx - 10},${sy - 12} ${sx},${sy - 22} Z" fill="#4a5038" stroke="#d9c75a" stroke-width="1.2"/></g><circle class="ping" cx="${sx - 10}" cy="${sy - 24}" r="5" fill="none" stroke="#d9c75a" stroke-width="1"/>`;
  front += lights(sx + 4, sy + 4, lo("scanner"), "#a7c060", 6);

  // unsichtbare Klickzonen für die Spielereien (oben liegend)
  const z = (part, shape) => shape.replace(/^<(\w+)/, `<$1 class="zone" data-part="${part}" fill="#ffffff" fill-opacity="0"`);
  const zones = [
    z("cargo", `<rect x="${cx0 - 4}" y="${t - 22}" width="${cw + 8}" height="22"/>`),
    z("hull", `<path d="${hp}"/>`),
    z("engine", `<rect x="${l - 8}" y="${t - 16}" width="22" height="30"/>`),
    z("cockpit", `<rect x="${hx - 9}" y="${hy - 16}" width="18" height="16"/>`),
    z("reactor", `<rect x="${mx - 6}" y="${my - 8}" width="${bl + 10}" height="16"/>`),
    z("scanner", `<rect x="${sx - 22}" y="${sy - 54}" width="40" height="52"/>`),
  ].join("");
  return `<g class="ship t${H}">${back}${hull}${front}${zones}</g>`;
}

'''

FIELD_SKY = r'''function sizeSkyObj(o) {
  const r = o.host.getBoundingClientRect(), d = devicePixelRatio || 1;
  o.w = r.width; o.h = r.height;
  if (!o.w) return;
  o.canvas.width = o.w * d; o.canvas.height = o.h * d; o.cx.setTransform(d, 0, 0, d, 0, 0);
  o.stars = Array.from({ length: 5 }, () => ({ x: Math.random() * o.w, y: o.h * (.05 + Math.random() * .3), z: .5 + Math.random() * .8, w: 60 + Math.random() * 80 }));
  o.dust = Array.from({ length: 22 }, () => ({ x: Math.random() * o.w, y: Math.random(), p: Math.random() * 6 }));
  o.debris = Array.from({ length: 7 }, () => newDebris(o, true));
  o.craters = Array.from({ length: 5 }, () => ({ x: Math.random() * o.w, y: Math.random(), s: .6 + Math.random() * .8 }));
  o.birds = [];
}
function newDebris(o, anywhere) {
  const hz = toSky(o, 0, 104)[1];
  return { x: anywhere ? Math.random() * o.w : o.w + 30, y: hz + 6 + Math.random() * Math.max(10, o.h - hz - 12), s: 3 + Math.random() * 4, kind: Math.random() < .5 ? "plate" : "wheel", rot: (Math.random() - .5) * 1.2, v: .1 };
}
function toSky(o, x, y) { const s = Math.min(o.w / VB.w, o.h / VB.h); return [(o.w - VB.w * s) / 2 + (x - VB.x) * s, (o.h - VB.h * s) / 2 + (y - VB.y) * s, s]; }
function skyCloud(c, x, y, w, col) {
  c.fillStyle = col; c.beginPath();
  c.ellipse(x, y, w * .5, w * .14, 0, 0, 7); c.ellipse(x - w * .24, y + w * .03, w * .3, w * .12, 0, 0, 7); c.ellipse(x + w * .2, y - w * .05, w * .28, w * .15, 0, 0, 7);
  c.fill();
}
function skyLand(c, o, sec, hz, isl) {
  // Silhouetten am Horizont, ziehen langsam vorbei
  const span = o.w * 1.6, s = Math.max(.6, o.h / 200);
  c.fillStyle = sec.land;
  for (let k = 0; k < 2; k++) {
    const ix = ((o.w * (.3 + k * .8) - isl) % span + span) % span - o.w * .3;
    if (sec.shape === "depot") {
      c.beginPath(); c.moveTo(ix - 70 * s, hz + 1); c.lineTo(ix - 70 * s, hz - 16 * s); c.quadraticCurveTo(ix - 45 * s, hz - 34 * s, ix - 20 * s, hz - 16 * s); c.lineTo(ix - 20 * s, hz + 1); c.fill();
      c.fillRect(ix - 10 * s, hz - 22 * s, 40 * s, 23 * s); c.fillRect(ix + 36 * s, hz - 40 * s, 4 * s, 41 * s); c.fillRect(ix + 30 * s, hz - 48 * s, 16 * s, 9 * s);
    } else if (sec.shape === "mud") {
      c.beginPath(); c.ellipse(ix, hz + 2, 90 * s, 12 * s, 0, Math.PI, 0); c.fill();
      c.strokeStyle = sec.land; c.lineWidth = 2 * s;
      [[-30, 22], [20, 28], [50, 18]].forEach(([dx, h]) => { c.beginPath(); c.moveTo(ix + dx * s, hz - 6 * s); c.lineTo(ix + dx * s, hz - h * s); c.moveTo(ix + dx * s, hz - h * .6 * s); c.lineTo(ix + (dx + 6) * s, hz - h * .85 * s); c.moveTo(ix + dx * s, hz - h * .4 * s); c.lineTo(ix + (dx - 5) * s, hz - h * .65 * s); c.stroke(); });
    } else if (sec.shape === "desert") {
      c.beginPath(); c.moveTo(ix - 100 * s, hz + 1); c.quadraticCurveTo(ix - 50 * s, hz - 22 * s, ix, hz - 4 * s); c.quadraticCurveTo(ix + 40 * s, hz - 26 * s, ix + 100 * s, hz + 1); c.fill();
      c.fillRect(ix + 60 * s, hz - 30 * s, 10 * s, 30 * s); c.fillRect(ix + 56 * s, hz - 34 * s, 18 * s, 5 * s);
    } else {
      for (let i = 0; i < 7; i++) { const px = ix - 70 * s + i * 22 * s, ph = (22 + (i * 37 % 14)) * s; c.beginPath(); c.moveTo(px, hz - ph); c.lineTo(px - 8 * s, hz + 1); c.lineTo(px + 8 * s, hz + 1); c.fill(); }
      c.fillStyle = "rgba(240,245,250,.7)"; for (let i = 0; i < 7; i++) { const px = ix - 70 * s + i * 22 * s, ph = (22 + (i * 37 % 14)) * s; c.beginPath(); c.moveTo(px, hz - ph); c.lineTo(px - 3 * s, hz - ph + 7 * s); c.lineTo(px + 3 * s, hz - ph + 7 * s); c.fill(); }
    }
  }
}
function drawSky(o, now, dt) {
  if (!o.w) { sizeSkyObj(o); if (!o.w) return; }
  const c = o.cx, E = Math.floor(state.ship.engine / 3), H = Math.floor(state.ship.hull / 3), R = Math.floor(state.ship.reactor / 3);
  const speed = (0.01 + E * 0.03 + warpBoost * 0.05 + (performance.now() < shipBoostUntil ? 0.22 : 0)) * dt;
  const sec = curSector(), hz = toSky(o, 0, 104)[1], gy = toSky(o, 0, 126)[1];
  c.clearRect(0, 0, o.w, o.h);
  const sg = c.createLinearGradient(0, 0, 0, hz); sg.addColorStop(0, sec.sky[0]); sg.addColorStop(.65, sec.sky[1]); sg.addColorStop(1, sec.sky[2]);
  c.fillStyle = sg; c.fillRect(0, 0, o.w, hz + 1);
  const sx = o.w * .78, sy = hz * .42, sr = Math.max(11, o.h * .075);
  const gl = c.createRadialGradient(sx, sy, sr * .4, sx, sy, sr * 4); gl.addColorStop(0, sec.sun[1]); gl.addColorStop(1, "rgba(0,0,0,0)");
  c.fillStyle = gl; c.fillRect(0, 0, o.w, hz);
  c.fillStyle = sec.sun[0]; c.beginPath(); c.arc(sx, sy, sr, 0, 7); c.fill();
  for (const cl of o.stars) { cl.x -= (.01 + speed * .01) * cl.z * dt * .5; if (cl.x < -cl.w) cl.x = o.w + cl.w; skyCloud(c, cl.x, cl.y, cl.w * cl.z, sec.cloud); }
  o.isl = (o.isl || 0) + dt * (.002 + E * .001);
  skyLand(c, o, sec, hz, o.isl);
  const mg = c.createLinearGradient(0, hz, 0, o.h); mg.addColorStop(0, sec.ground[0]); mg.addColorStop(1, sec.ground[1]);
  c.fillStyle = mg; c.fillRect(0, hz, o.w, o.h - hz);
  // Spurrillen
  o.off = (o.off || 0) + speed * 2.4 + dt * .004;
  for (let i = 0; i < 7; i++) {
    const y = hz + (o.h - hz) * Math.pow((i + 1) / 8, 1.5), seg = 18 + i * 9;
    c.strokeStyle = `rgba(0,0,0,${.08 + i * .015})`; c.lineWidth = 1 + i * .25;
    c.setLineDash([seg, seg * .7]); c.lineDashOffset = o.off * (1 + i * .45);
    c.beginPath(); c.moveTo(0, y); c.lineTo(o.w, y); c.stroke();
  }
  c.setLineDash([]);
  // Krater
  for (const k of o.craters) {
    k.x -= (speed * 1.1 + .01 * dt * .06) * (.5 + k.y); if (k.x < -40) { k.x = o.w + 40; k.y = Math.random(); }
    const y = hz + 10 + k.y * (o.h - hz - 14), rr = (10 + k.y * 22) * k.s;
    c.fillStyle = "rgba(0,0,0,.22)"; c.beginPath(); c.ellipse(k.x, y, rr, rr * .3, 0, 0, 7); c.fill();
    c.strokeStyle = "rgba(255,255,255,.06)"; c.lineWidth = 1.2; c.beginPath(); c.ellipse(k.x, y - 1, rr, rr * .3, 0, Math.PI, 0); c.stroke();
  }
  // Schrott beim Wrack
  const debrisCount = H === 0 ? 7 : H === 1 ? 3 : 0;
  o.debris.slice(0, debrisCount).forEach((d, i) => {
    d.x -= (d.v * .35 + speed * .25) * (dt / 16);
    if (d.x < -30) o.debris[i] = newDebris(o, false);
    c.save(); c.translate(d.x, d.y); c.rotate(d.rot);
    if (d.kind === "plate") { c.fillStyle = "#4a4038"; c.fillRect(-d.s * 2, -d.s * .5, d.s * 4, d.s); c.fillStyle = "rgba(255,255,255,.1)"; c.fillRect(-d.s * 2, -d.s * .5, d.s * 4, d.s * .25); }
    else { c.strokeStyle = "#3a3d42"; c.lineWidth = d.s * .5; c.beginPath(); c.arc(0, 0, d.s, 0, 7); c.stroke(); }
    c.restore();
  });
  const g = GEO[H];
  // Abgase und Staub
  if (Math.random() < (E === 0 ? .35 : .18 + E * .06)) { const [x, y, s] = toSky(o, g.l + (E === 0 ? 8 : 12), g.t - (E === 0 ? 6 : 13)); o.parts.push({ x, y, vx: -.35 - E * .2, vy: -.45 - Math.random() * .3, r: (E === 0 ? 2.6 : 1.8) * s, life: .9, kind: "smoke", dark: E === 0 }); }
  if (E >= 1 && Math.random() < .3 + E * .1) { const [x, y, s] = toSky(o, g.l - 4, 125); o.parts.push({ x, y, vx: -.4 - E * .3, vy: -.15 - Math.random() * .2, r: 1.6 * s, life: .8, kind: "dust" }); }
  if (R === 0 && Math.random() < .02) { const [x, y] = toSky(o, g.l + 150, g.t - 6); for (let i = 0; i < 4; i++) o.parts.push({ x, y, vx: (Math.random() - .5) * 1.6, vy: -1 - Math.random(), r: 1, life: 1, kind: "spark" }); }
  o.parts = o.parts.filter(p => p.life > 0);
  for (const p of o.parts) {
    p.x += p.vx * dt * .06; p.y += p.vy * dt * .06;
    if (p.kind === "smoke") { p.r += .02 * dt; p.life -= .0009 * dt; c.fillStyle = p.dark ? `rgba(30,26,24,${p.life * .45})` : `rgba(170,170,165,${p.life * .3})`; c.beginPath(); c.arc(p.x, p.y, p.r, 0, 7); c.fill(); }
    else if (p.kind === "dust") { p.r += .012 * dt; p.life -= .0014 * dt; c.fillStyle = `rgba(150,120,85,${p.life * .35})`; c.beginPath(); c.arc(p.x, p.y, p.r, 0, 7); c.fill(); }
    else if (p.kind === "drop") { p.vy += .004 * dt; p.life -= .002 * dt; c.fillStyle = `rgba(255,220,150,${p.life * .9})`; c.beginPath(); c.arc(p.x, p.y, p.r, 0, 7); c.fill(); }
    else { p.vy += .002 * dt; p.life -= .0025 * dt; c.fillStyle = `rgba(255,${150 + (Math.random() * 80 | 0)},60,${p.life})`; c.fillRect(p.x, p.y, p.r * 2, p.r * 2); }
  }
  // Grasbüschel im Vordergrund
  c.strokeStyle = sec.grass; c.lineWidth = 1;
  for (const d of o.dust) {
    d.x -= speed * 1.2 + .01 * dt * .06; if (d.x < -6) d.x = o.w + 6;
    const y = Math.max(gy + 4, hz + 6 + d.y * (o.h - hz - 8));
    c.beginPath(); c.moveTo(d.x, y); c.lineTo(d.x - 2, y - 5); c.moveTo(d.x, y); c.lineTo(d.x + 1, y - 6); c.moveTo(d.x, y); c.lineTo(d.x + 3, y - 4); c.stroke();
  }
}
'''
