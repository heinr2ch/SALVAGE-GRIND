# Eisenfront Teil 5: drei Fahrzeuge (Panzer, Schwerer Panzer, Mammut)

VEHICLES_EF = '''const VEHICLES = [
  { name: "Panzer", rank: 1, cost: 1, color: "#a7c060", desc: "Ein rostiger Panzer, der kaum noch rollt." },
  { name: "Schwerer Panzer", acc: "einen schweren Panzer", rank: 8, cost: 4, color: "#e8b04a", desc: "Seitenschürzen, Bugplatte, Zusatz-MG und eine zweite Kette. Neue Teile kosten mehr, dafür steigen Einsätze bis 250." },
  { name: "Mammut", acc: "ein Mammut", rank: 14, cost: 12, color: "#e07a4a", desc: "Ein Koloss mit Heckturm, Räumschild und Antennenmast. Einsätze bis 1.000." },
];
'''

VEH_EF = r'''
/* Fahrzeugklassen: Schwerer Panzer (Schürzen, Bugplatte, MG, zweite Kette) und Mammut (Heckturm, Räumschild, Antennenmast). */
function vehLayers(L, k) {
  const V = veh(); if (!V) return ["", ""];
  const H = Math.min(3, Math.floor(L.hull / 3)), g = GEO[H], { l, t, b, n } = g, tb = b - 12, tx = Math.round(l + (n - l) * .55);
  const armor = ["#6e4a32", "#5f5a3e", "#4f5a2c", "#56632e"][H], dark = ["#3a2618", "#33301f", "#2a3214", "#1e2410"][H], light = ["#9a6a48", "#8a8458", "#7a8a44", "#9aa860"][H];
  const pf = `style="filter:${paintFilter()}"`;
  let back = "", front = "";
  // zweite (hintere) Kette und Auspuffrohre
  back += `<rect x="${l - 12}" y="${tb - 6}" width="${n - l + 6}" height="${b - tb}" rx="${(b - tb) / 2}" fill="#18191b" stroke="#3a3d42" stroke-width="1.4"/>
    <rect class="tracks" x="${l - 10}" y="${tb - 5}" width="${n - l + 2}" height="${b - tb - 2}" rx="${(b - tb) / 2 - 1}" fill="none" stroke="#4a4e54" stroke-width="1.2" stroke-dasharray="2 3"/>
    ${[l + 34, l + 44].map(x => `<path d="M${x},${t + 2} V${t - 18}" stroke="#4a4f55" stroke-width="3.4" stroke-linecap="round"/><circle class="flick" cx="${x}" cy="${t - 20}" r="1.6" fill="${H ? "#5a5a5a" : "#8a4a2a"}"/>`).join("")}`;
  // Seitenschürzen, Bugplatte, Zusatz-MG
  front += `<g ${pf}><path d="M${l - 2},${tb - 4} H${n - 8} L${n - 14},${tb + 7} H${l + 2} Z" fill="${armor}" stroke="${dark}" stroke-width="1.4"/>
    ${Array.from({ length: 10 }, (_, i) => `<circle cx="${l + 6 + i * ((n - l - 24) / 9)}" cy="${tb + 1.5}" r=".9" fill="${light}"/>`).join("")}
    ${H === 0 ? `<path d="M${l + 40},${tb - 4} l4,11 M${n - 60},${tb - 4} l-3,11" stroke="#120c08" stroke-width="3"/><ellipse cx="${l + 80}" cy="${tb + 1}" rx="10" ry="3" fill="#8a4a2a" opacity=".6"/>` : ""}
    <path d="M${n - 4},${t + 9} L${n + 10},${t + 16} L${n + 6},${tb + 2} L${n - 6},${tb} Z" fill="${armor}" stroke="${dark}" stroke-width="1.4"/>
    <rect x="${tx + 2}" y="${t - 27}" width="9" height="6" rx="1.5" fill="${armor}" stroke="${dark}" stroke-width="1"/><path d="M${tx + 10},${t - 24} H${tx + 26}" stroke="#3a3d42" stroke-width="1.6"/>
    <path d="M${l + 2},${tb + 5} H${n - 13}" stroke="${H ? "#e8b04a" : "#6a4a2a"}" stroke-width="2.6" stroke-dasharray="5 4"/>
    ${[n - 80, n - 64].map(x => `<circle cx="${x}" cy="${t + 9}" r="5.4" fill="#2a2d30" stroke="#6a6f76" stroke-width="1.3"/><circle cx="${x}" cy="${t + 9}" r="1.6" fill="#9aa0a8"/>`).join("")}
    ${[0, 1, 2].map(i => `<rect x="${tx - 30 - i * 5}" y="${t - 14 + i * 2}" width="4" height="7" rx="1.5" fill="#3a3d42" stroke="#6a6f76" stroke-width=".7"/>`).join("")}</g>`;
  if (V >= 2) {
    // Heckaufbau mit zweitem Turm (zeigt nach hinten), Räumschild vorne, hoher Antennenmast
    back += `<g ${pf}><rect x="${l - 2}" y="${t - 34}" width="58" height="36" rx="2" fill="${armor}" stroke="${dark}" stroke-width="1.6"/>
      ${[0, 1, 2].map(i => `<rect x="${l + 6 + i * 16}" y="${t - 28}" width="10" height="5" rx="1" fill="${H ? "#e8c070" : "#1a120a"}" opacity=".75"/>`).join("")}
      <path d="M${l + 6},${t - 34} L${l + 12},${t - 52} H${l + 44} L${l + 52},${t - 34} Z" fill="${armor}" stroke="${dark}" stroke-width="1.6"/>
      <path d="M${l + 12},${t - 43} H${l - 30}" stroke="${H ? "#5a5f4a" : "#5a4a3a"}" stroke-width="4"/><rect x="${l - 34}" y="${t - 46}" width="7" height="6" rx="1" fill="#3a3d42"/>
      <path d="M${l + 6},${t - 6} H${l + 50}" stroke="${light}" stroke-width="1" opacity=".6"/>
      <path d="M${l + 30},${t - 52} V${t - 96}" stroke="#8a9098" stroke-width="1.2"/><path d="M${l + 24},${t - 80} h12 M${l + 26},${t - 88} h8" stroke="#8a9098" stroke-width="1"/>
      <circle class="blink" cx="${l + 30}" cy="${t - 97}" r="1.8" fill="#e07a4a"/><path class="sail" d="M${l + 30},${t - 94} l11,3 l-11,3z" fill="#a33a2a"/></g>`;
    front += `<g ${pf}><path d="M${n + 6},${t + 2} Q${n + 26},${(t + b) / 2} ${n + 12},${b} L${n + 24},${b} Q${n + 36},${(t + b) / 2} ${n + 16},${t} Z" fill="${H ? "#6a6f76" : "#6a4a32"}" stroke="#2a2d30" stroke-width="1.4"/>
      <path d="M${n + 2},${t + 18} L${n + 14},${t + 18} M${n + 2},${tb} L${n + 14},${tb - 2}" stroke="#3a3d42" stroke-width="2.4"/>
      ${[0, 1, 2].map(i => `<path d="M${n + 17 + i * 2},${t + 16 + i * 9} l3,4" stroke="#e8b04a" stroke-width="1.6" opacity="${H ? .9 : .4}"/>`).join("")}</g>`;
  }
  return [back, front];
}
'''

ACH_EF_REPS = [
    ('  A("maxed", "Voll ausgebaut", "Alle 45 Upgrade-Stufen.", "up_reactor", 1000, () => totalSteps() >= 45),',
     '''  A("maxed", "Voll ausgebaut", "Alle 45 Upgrade-Stufen.", "up_reactor", 1000, () => totalSteps() >= 45 || (state.vehicle | 0) >= 1),
  A("veh2", "Schweres Gerät", "Steig auf den schweren Panzer um.", "up_engine", 500, () => (state.vehicle | 0) >= 1),
  A("veh3", "Mammutaufgabe", "Steig auf das Mammut um.", "up_reactor", 2000, () => (state.vehicle | 0) >= 2),
  A("allmax", "Alles ausgebaut", "Bau auch das Mammut komplett aus.", "up_reactor", 5000, () => (state.vehicle | 0) >= 2 && totalSteps() >= 45),'''),
]
