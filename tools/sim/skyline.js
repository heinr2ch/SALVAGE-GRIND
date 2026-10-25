// Skyline-Walzen (Neustadt 0.4): 6 Walzen, jede pro Dreh 2 bis 7 Felder hoch, Gewinnwege = Produkt der Treffer je Walze.
// Gewinne verschwinden, Neues rutscht nach (Nachbau). Freispiele: Multiplikator +1 pro Nachbau, bleibt über alle Freispiele.
// Ergebnis (Beta 0.4.0): Auszahlung ~115 %, Treffer ~54 % (viele kleine), Freispiele ~1/124 mit im Mittel ~60×.
// Aufruf: node skyline.js '{"n":200000}'   (Werte wie in tools/neustadt_parts3.py: SK_*)
const P = JSON.parse(process.argv[2] || "{}");
const HW = P.hw || { 2: 14, 3: 24, 4: 24, 5: 18, 6: 12, 7: 8 };
const W = Object.assign({ tree: 19, lamp: 19, scrap: 17, cell: 16, chip: 14, core: 12, crystal: 9, relic: 6, wild: 3.2, beacon: 3.8, warp: 1.1 }, P.w || {});
const PAY = P.pay || { tree: [.05, .1, .2, .4], lamp: [.05, .1, .2, .4], scrap: [.1, .15, .25, .5], cell: [.1, .2, .3, .6], chip: [.15, .25, .4, .8], core: [.2, .4, .6, 1.2], crystal: [.3, .6, 1, 2], relic: [.5, 1, 2.5, 5] };
const SCALE = P.scale ?? .56;
const FS_N = P.fsn ?? 10, FS_EXTRA = 2, FS_RE = 5, MULT_MAX = P.mmax ?? 15, WHEEL = 25;
const SYMS = Object.keys(PAY);
function pickH() { let t = 0; for (const k in HW) t += HW[k]; let r = Math.random() * t; for (const k in HW) if ((r -= HW[k]) < 0) return +k; return 4; }
function pick(reel) { let t = 0; for (const k in W) if (k !== "wild" || (reel >= 1 && reel <= 4)) t += W[k]; let r = Math.random() * t;
  for (const k in W) { if (k === "wild" && !(reel >= 1 && reel <= 4)) continue; if ((r -= W[k]) < 0) return k; } return "scrap"; }
function evaluate(g) {
  let total = 0; const hit = g.map(c => c.map(() => false));
  for (const s of SYMS) {
    let ways = 1, run = 0;
    for (let r = 0; r < 6; r++) { const c = g[r].filter(x => x === s || x === "wild").length; if (!c) break; ways *= c; run++; }
    if (run >= 3) { total += PAY[s][run - 3] * ways * SCALE; for (let r = 0; r < run; r++) g[r].forEach((x, i) => { if (x === s || x === "wild") hit[r][i] = true; }); }
  }
  return { total, hit };
}
function spin(free, multState) {
  const g = Array.from({ length: 6 }, (_, r) => Array.from({ length: pickH() }, () => pick(r)));
  let win = 0, casc = 0;
  const scat = g.flat().filter(x => x === "beacon").length, bus = g.flat().filter(x => x === "warp").length;
  for (;;) {
    const e = evaluate(g); if (e.total <= 0) break;
    const m = free ? multState.m : 1;
    win += e.total * m; casc++;
    if (free) multState.m = Math.min(MULT_MAX, multState.m + 1);
    for (let r = 0; r < 6; r++) { const keep = g[r].filter((x, i) => !e.hit[r][i]); while (keep.length < g[r].length) keep.push(pick(r)); g[r] = keep; }
  }
  let fs = 0;
  if (!free && scat >= 4) fs = FS_N + (scat - 4) * FS_EXTRA;
  if (free && scat >= 3) fs = FS_RE;
  if (bus >= 3) win += WHEEL;
  return { win, fs, casc };
}
const N = P.n || 200000; let tot = 0, hits = 0, fsTrig = 0, fsTot = 0, big = 0, baseTot = 0;
for (let i = 0; i < N; i++) {
  const b = spin(false); let w = b.win; baseTot += b.win;
  if (b.fs) { fsTrig++; let left = b.fs, st = { m: 1 }, fw = 0; while (left > 0) { left--; const f = spin(true, st); fw += f.win; left += f.fs; } w += fw; fsTot += fw; }
  tot += w; if (b.win > 0) hits++; if (w >= 10) big++;
}
console.log(`Auszahlung ${(tot / N * 100).toFixed(1)} % (Grundspiel ${(baseTot / N * 100).toFixed(1)} %) · Treffer ${(hits / N * 100).toFixed(1)} % · Freispiele 1/${(N / fsTrig).toFixed(0)}, im Mittel ${(fsTot / fsTrig).toFixed(1)}× · ab 10×: 1/${(N / big).toFixed(0)}`);
