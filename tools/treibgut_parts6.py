# Treibgut Teil 6: drei Fahrzeuge (Floß, Katamaran, Schoner)

VEHICLES_TG = '''const VEHICLES = [
  { name: "Floß", rank: 1, cost: 1, color: "#d9b27c", desc: "Ein paar Bretter, ein Segel und viel Hoffnung." },
  { name: "Katamaran", acc: "einen Katamaran", rank: 8, cost: 4, color: "#5cc8b0", desc: "Zwei Rümpfe, ein Vorsegel und mehr Platz. Neue Teile kosten mehr, dafür steigen Einsätze bis 250." },
  { name: "Schoner", acc: "einen Schoner", rank: 14, cost: 12, color: "#e0704a", desc: "Ein echtes Segelschiff mit Achterkajüte und zweitem Mast. Einsätze bis 1.000." },
];
'''

VEH_TG = r'''
/* Fahrzeugklassen: Katamaran (zwei Rümpfe, Vorsegel) und Schoner (Schiffsrumpf, Achterkajüte, zweiter Mast). */
function vehLayers(L, k) {
  const V = veh(); if (!V) return ["", ""];
  const H = Math.min(3, Math.floor(L.hull / 3)), g = GEO[H], { l, t, b, n } = g, mx = l + Math.round((n - l) * .28);
  const wood = ["#5a4a3a", "#7a5230", "#8a5c32", "#9a6838"][H], dark = ["#2e261e", "#3e2814", "#46301a", "#4a3218"][H], light = ["#8f7f6c", "#c99a62", "#d9aa6c", "#e6b877"][H];
  const cloth = H === 0 ? "#c9b896" : "#efe4c8", pf = `style="filter:${paintFilter()}"`;
  let back = "", front = "";
  if (V === 1) {
    const canoe = (y, sc, op) => `<path d="M${l - 18},${y - 6} Q${l - 12},${y + 6 * sc} ${l + 12},${y + 7 * sc} L${n - 6},${y + 7 * sc} Q${n + 22},${y + 5 * sc} ${n + 30},${y - 8} Q${n + 8},${y - 1} ${n - 10},${y} L${l + 8},${y} Q${l - 6},${y - 1} ${l - 18},${y - 6} Z" fill="${wood}" stroke="${dark}" stroke-width="1.6" opacity="${op}"/>
      <path d="M${l + 6},${y + 3 * sc} H${n - 8}" stroke="${light}" stroke-width="1" opacity="${op * .6}"/>`;
    const hullC = H === 0 ? "#4a3a2a" : ["#4a3a2a", "#3aa0ae", "#2f9aa8", "#2a90a0"][H];
    front += `<g ${pf}><path d="M${l - 34},${b - 8} Q${l - 26},${b + 14} ${l + 4},${b + 14} L${n - 4},${b + 14} Q${n + 34},${b + 13} ${n + 44},${b - 12} Q${n + 18},${b + 1} ${n - 6},${b + 2} L${l + 2},${b + 2} Q${l - 20},${b + 1} ${l - 34},${b - 8} Z" fill="${hullC}" stroke="${dark}" stroke-width="1.6"/>
      <path d="M${l - 6},${b + 8} H${n + 4}" stroke="${H ? "#e8f0e8" : light}" stroke-width="1.4" opacity=".7"/>
      ${H === 0 ? `<path d="M${l + 40},${b + 3} l5,6 M${n - 50},${b + 3} l-4,6" stroke="#1a120a" stroke-width="2"/>` : `<path d="M${n + 30},${b - 6} l6,-2" stroke="#e8b04a" stroke-width="1.6"/>`}</g>`;
    back += `<g ${pf}>${canoe(WL - 4, .7, .75)}
      <path d="M${l - 6},${t + 4} L${l - 10},${WL + 2} M${n + 10},${t + 4} L${n + 14},${WL + 1}" stroke="${dark}" stroke-width="3" stroke-linecap="round"/></g>
      <path d="M${mx + 2},${t - 70} L${n + 24},${WL - 10}" stroke="#8a6a45" stroke-width="1.2"/>
      <path class="sail" d="M${mx + 4},${t - 64} L${n + 18},${t - 6} L${mx + 6},${t - 6} Z" fill="${cloth}" stroke="#8a6a45" stroke-width="1.2" opacity=".95"/>
      ${H === 0 ? `<circle cx="${mx + 26}" cy="${t - 22}" r="3" fill="#2a1d12"/><path d="M${mx + 14},${t - 40} l8,3" stroke="#8a6a45" stroke-width="1"/>` : `<path d="M${mx + 8},${t - 30} L${n},${t - 10}" stroke="#c9a46a" stroke-width="1" opacity=".6"/>`}`;
  }
  if (V === 2) {
    const sx = Math.min(n + 46, 348), st = l - 26;
    back += `<g ${pf}>
      <path d="M${st},${t - 24} L${l + 10},${t - 24} L${l + 14},${t + 2} L${n + 6},${t + 2} Q${n + 30},${t - 2} ${sx - 6},${t - 20} Q${n + 30},${WL + 2} ${n - 12},${WL + 13} L${l},${WL + 13} Q${st - 2},${WL + 6} ${st},${t - 24} Z" fill="${wood}" stroke="${dark}" stroke-width="1.8" stroke-linejoin="round"/>
      ${[0, 1, 2].map(i => `<path d="M${st + 4},${b + 2 + i * 5} Q${(l + n) / 2},${b + 6 + i * 5} ${n + 20},${b - 2 + i * 4}" stroke="${dark}" stroke-width="1" fill="none" opacity=".6"/>`).join("")}
      <path d="M${st},${t - 24} H${l + 10}" stroke="${light}" stroke-width="2"/>
      ${[0, 1, 2].map(i => `<rect x="${st + 5 + i * 11}" y="${t - 18}" width="7" height="7" rx="1.5" fill="${H === 0 ? "#1a120a" : "#ffd27a"}" stroke="${dark}" stroke-width="1" opacity="${H === 0 ? .9 : .85}"/>`).join("")}
      ${H >= 2 ? `<path d="M${st + 2},${t - 8} H${l + 10}" stroke="#e8b04a" stroke-width="1.2"/>` : ""}
      <path d="M${n + 26},${t - 12} L${sx + 6},${t - 30}" stroke="${dark}" stroke-width="2.6" stroke-linecap="round"/>
      <path d="M${st + 18},${t - 24} V${t - 104}" stroke="${dark}" stroke-width="3" stroke-linecap="round"/>
      <path class="sail" d="M${st + 20},${t - 98} L${st + 52},${t - 92} L${st + 58},${t - 32} L${st + 20},${t - 30} Z" fill="${cloth}" stroke="#8a6a45" stroke-width="1.2"/>
      ${H === 0 ? `<path d="M${st + 34},${t - 70} l6,8 M${st + 44},${t - 50} l-5,6" stroke="#7a6a50" stroke-width="1.4"/><circle cx="${st + 40}" cy="${t - 60}" r="3" fill="#2a1d12"/>` : `<path d="M${st + 22},${t - 64} L${st + 55},${t - 62}" stroke="#c9a46a" stroke-width="1" opacity=".6"/>`}
      <path class="sail" d="M${st + 18},${t - 104} l12,3 l-12,4z" fill="${["#8a7a6a", "#c0563a", "#3a8a6a", "#2f6fb0"][H]}"/>
      <path class="sail" d="M${sx + 4},${t - 30} L${mx + 6},${t - 76} L${mx + 8},${t - 8} Z" fill="${cloth}" stroke="#8a6a45" stroke-width="1.1" opacity=".95"/>
    </g>`;
  }
  return [back, front];
}
'''

ACH_TG_REPS = [
    ('  A("maxed", "Voll ausgebaut", "Alle 45 Upgrade-Stufen.", "up_reactor", 1000, () => totalSteps() >= 45),',
     '''  A("maxed", "Voll ausgebaut", "Alle 45 Upgrade-Stufen.", "up_reactor", 1000, () => totalSteps() >= 45 || (state.vehicle | 0) >= 1),
  A("veh2", "Zwei Rümpfe", "Steig auf den Katamaran um.", "up_engine", 500, () => (state.vehicle | 0) >= 1),
  A("veh3", "Kapitän eines Schoners", "Steig auf den Schoner um.", "up_reactor", 2000, () => (state.vehicle | 0) >= 2),
  A("allmax", "Alles ausgebaut", "Bau auch den Schoner komplett aus.", "up_reactor", 5000, () => (state.vehicle | 0) >= 2 && totalSteps() >= 45),'''),
]
