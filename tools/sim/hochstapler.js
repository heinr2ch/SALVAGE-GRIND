// Hochstapler 0.2: Richtfest, Bauboom, Investor, Mini-Events
const P = JSON.parse(process.argv[2] || "{}");
const W = Object.assign({ scrap: 30, cell: 22, chip: 16, core: 8, relic: 1.6, crystal: 5, wild: 2.5, capsule: 2.5, beacon: .3, warp: .1, crash: 14 }, P.W || {});
const D = { scrap: 1, cell: 1, chip: 2, core: 3, relic: 6, crystal: 1, wild: 1, capsule: 0, beacon: 0, warp: 0 };
const C = P.c ?? 1, G = 1.07, MAXH = 100, PICK = 22, WHEEL = 25, FS_START = 3;
const RF = P.rf || [.5, 1, 2, 3, 5, 8, 12, 20, 30, 50];
const EV = P.ev ?? .06, INV = P.inv ?? .025, INVF = P.invf ?? 1.3, BOOM = P.boom ?? 4;
const M = h => C * Math.pow(G, Math.min(h, MAXH));
function pick() { let t = 0; for (const k in W) t += W[k]; let r = Math.random() * t; for (const k in W) if ((r -= W[k]) < 0) return k; return "scrap"; }
function round(target, free) {
  let h = free ? FS_START : 0, shield = 0, plans = 0, extra = 0, fs = 0, run = 0, boom = 0;
  for (;;) {
    const s = pick();
    if (s === "crash") { run = 0; boom = 0; if (shield) { shield--; continue; } return { win: extra, fs }; }
    let d = D[s]; if (boom > 0 && d) { d += 1; boom--; }
    const h0 = h; h += d;
    if (d) { run++; if (run >= BOOM && !boom) { boom = 3; run = 0; } } else run = 0;
    for (let k = Math.floor(h0 / 10) + 1; k <= Math.floor(Math.min(h, MAXH) / 10); k++) extra += RF[Math.min(k - 1, RF.length - 1)];
    if (s === "wild") shield = Math.min(1, shield + 1);
    if (s === "capsule" && ++plans === 3) extra += PICK;
    if (s === "warp") extra += WHEEL;
    if (s === "beacon") fs += 3;
    if (h >= 2 && Math.random() < EV) { const g = Math.random() * 3 | 0; if (g === 0) h += [0, 1, 3][Math.random() * 3 | 0]; else if (g === 1) extra += .3 * (2 + Math.random() * 4 | 0); else if (Math.random() < .6) { shield = Math.min(1, shield + 1); h += 1; } }
    if (h >= MAXH) return { win: M(MAXH) + extra, fs };
    if (h >= 5 && Math.random() < INV && M(h) * INVF >= target) return { win: M(h) * INVF + extra, fs };
    if (h >= 1 && M(h) >= target) return { win: M(h) + extra, fs };
  }
}
for (const target of P.targets || [1.3, 2, 3, 5, 10, 25, 100]) {
  let N = P.n || 200000, tot = 0, hits = 0;
  for (let i = 0; i < N; i++) { const r = round(target, false); let w = r.win, fs = r.fs; while (fs > 0) { fs--; const f = round(target, true); w += f.win; fs += f.fs; } tot += w; if (r.win > 0) hits++; }
  console.log(target, "rtp", (tot / N * 100).toFixed(1), "hit", (hits / N * 100).toFixed(1));
}
