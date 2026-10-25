// Stadtrundfahrt (Neustadt 0.3): Brettspiel mit 20 Feldern, 2 Würfeln, Grundstücken und Mieten.
// Aufruf: node stadtrundfahrt.js '{"n":200000}'
// Ergebnis (Beta 0.3.0): leere Stadt ~110 %, alles Stufe 1 ~130 %, alles Stufe 2 ~143 %, alles Stufe 4 ~177 %, Treffer 60 bis 97 %.
// Werte wie im Spiel (tools/neustadt_parts3.py: BD_PRICE, BD_RENT, BD_DIST.f). Strähne zählt nur Runden ab 1× Einsatz.
// Gibt die Auszahlung (in % vom Einsatz) für verschiedene Ausbaustände aus und eine Langzeit-Strategie mit Bauen.
const P = JSON.parse(process.argv[2] || "{}");
const F = ["start", "plot", "news", "plot", "plan", "mini", "plot", "plot", "news", "plot", "park", "plot", "kiosk", "plot", "plot", "office", "plot", "news", "plot", "plot"];
const DIST = { 1: 0, 3: 0, 6: 1, 7: 1, 9: 1, 11: 2, 13: 2, 14: 2, 16: 3, 18: 3, 19: 3 };
const DF = P.df || [.7, .9, 1.1, 1.4];                // Viertel-Faktor für Preis und Miete
const PRICE = P.price || [3, 5, 8, 12];              // Kosten je Ausbaustufe × Einsatz × Faktor
const RENT = P.rent || [0, .12, .2, .3, .42];      // Miete je Stufe × Einsatz × Faktor
const FULL = P.full ?? 1.5;                          // ganzes Viertel
const PASS = P.pass ?? .25, LAND = P.land ?? .6, KIOSK = P.kiosk ?? .4, PARK = P.park ?? .05;
const PLANS = P.plans ?? 5, PICK = 22, WHEEL = 25, FSN = 3, FSX = P.fsx ?? 2;
const CARDS = P.cards || [["cash", .5, 5], ["cash", 1.5, 3], ["cash", 4, 1], ["start", 0, 2], ["plan", 0, 1.5], ["wheel", 0, P.wheelW ?? .2], ["free", 0, 1], ["none", 0, 4], ["payday", .3, 1], ["dust", 0, 1]];
const CT = CARDS.reduce((a, c) => a + c[2], 0);
const card = () => { let r = Math.random() * CT; for (const c of CARDS) if ((r -= c[2]) < 0) return c; return CARDS[0]; };
const die = () => 1 + (Math.random() * 6 | 0);

function makeCity(level) { const o = {}; for (const k in DIST) o[k] = level; return o; }
function fullD(city, d) { return Object.keys(DIST).filter(k => DIST[k] === d).every(k => city[k] > 0); }
function rent(city, i) { const L = city[i] || 0; if (!L) return 0; return RENT[L] * DF[DIST[i]] * (fullD(city, DIST[i]) ? FULL : 1); }

function round(S, free) {
  // S: { pos, city, plans, park, build(i) } ; liefert Gewinn × Einsatz
  let win = 0, fs = 0, rolls = 0;
  S.park += PARK;
  for (;;) {
    const a = die(), b = die(); rolls++;
    let steps = a + b;
    const from = S.pos; S.pos = (S.pos + steps) % 20;
    if (S.pos < from || steps >= 20) win += PASS;
    const f = F[S.pos];
    if (f === "start") win += LAND;
    else if (f === "plot") { const r = rent(S.city, S.pos); if (r) win += r; if (S.build) S.build(S.pos); }
    else if (f === "kiosk") win += KIOSK;
    else if (f === "park") { win += S.park; S.park = 0; }
    else if (f === "mini") win += [0, 1, 2.5][Math.random() * 3 | 0] * .8 + .2;
    else if (f === "office") fs += FSN;
    else if (f === "plan") { if (++S.plans >= PLANS) { S.plans = 0; win += PICK; } }
    else if (f === "news") {
      const c = card();
      if (c[0] === "cash") win += c[1];
      else if (c[0] === "start") { S.pos = 0; win += LAND; }
      else if (c[0] === "plan") { if (++S.plans >= PLANS) { S.plans = 0; win += PICK; } }
      else if (c[0] === "wheel") win += WHEEL;
      else if (c[0] === "payday") { for (const k in DIST) win += rent(S.city, k) * c[1]; }
      else if (c[0] === "free" && S.freeUp) S.freeUp();
    }
    if (a !== b || rolls >= 3) break;
  }
  return { win: win * (free ? FSX : 1), fs };
}
const SM = [1, 1, 1.1, 1.25, 1.5];
function rtp(city, N) {
  const S = { pos: 0, city, plans: 0, park: 0 };
  let tot = 0, hits = 0, streak = 0;
  for (let i = 0; i < N; i++) {
    const r = round(S, false); let w = r.win, fs = r.fs;
    if (P.streak !== 0) { if (w >= 1) streak++; else streak = 0; w *= SM[Math.min(streak, 4)]; }
    while (fs > 0) { fs--; const q = round(S, true); w += q.win; fs += q.fs; }
    tot += w; if (w > 0) hits++;
  }
  return [(tot / N * 100).toFixed(1), (hits / N * 100).toFixed(1)];
}
const N = P.n || 300000;
for (const L of [0, 1, 2, 3, 4]) { const [r, h] = rtp(makeCity(L), N); console.log(`alle Grundstücke Stufe ${L}: Auszahlung ${r} %, Treffer ${h} %`); }
{ const c = makeCity(0); [1, 3, 6, 7, 9].forEach(k => c[k] = 2); const [r, h] = rtp(c, N); console.log(`halbe Stadt Stufe 2: ${r} %, Treffer ${h} %`); }

// Langzeit: Start 500 Taler, Einsatz 5, baut, wenn danach noch 20 Einsätze übrig sind
const cost = (i, L) => PRICE[L] * DF[DIST[i]];
for (const reserve of P.reserves || [20, 60]) {
  const runs = P.runs || 400, R = P.rounds || 3000, marks = [100, 300, 1000, 3000];
  const acc = marks.map(() => ({ cr: 0, inv: 0, broke: 0 }));
  for (let t = 0; t < runs; t++) {
    let cr = 100, inv = 0; const city = makeCity(0);  // Taler in Einsätzen (500 / 5)
    const S = { pos: 0, city, plans: 0, park: 0 };
    S.build = i => { const L = city[i]; if (L < 4 && cr - cost(i, L) >= reserve) { cr -= cost(i, L); inv += cost(i, L); city[i] = L + 1; } };
    S.freeUp = () => { const k = Object.keys(DIST).find(k => city[k] > 0 && city[k] < 4); if (k) city[k]++; };
    let broke = false;
    for (let r = 1; r <= R; r++) {
      if (!broke) {
        if (cr < 1) broke = true;
        else { cr -= 1; const q = round(S, false); cr += q.win; let fs = q.fs; while (fs > 0) { fs--; const z = round(S, true); cr += z.win; fs += z.fs; } }
      }
      const m = marks.indexOf(r); if (m >= 0) { acc[m].cr += cr; acc[m].inv += inv; acc[m].broke += broke ? 1 : 0; }
    }
  }
  console.log(`Strategie Reserve ${reserve}:`, marks.map((m, i) => `nach ${m}: ${(acc[i].cr / runs).toFixed(0)} Einsätze, verbaut ${(acc[i].inv / runs).toFixed(0)}, pleite ${(acc[i].broke / runs * 100).toFixed(0)} %`).join(" | "));
}
