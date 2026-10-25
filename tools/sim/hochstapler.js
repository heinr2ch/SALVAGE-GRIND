// Hochstapler-Simulation (Neustadt)
const P = JSON.parse(process.argv[2] || "{}");
const W = Object.assign({ scrap: 30, cell: 22, chip: 16, core: 8, relic: 1.6, crystal: 5, wild: 4, capsule: 4, beacon: 1, warp: .7, crash: 14 }, P.W || {});
const D = { scrap: 1, cell: 1, chip: 2, core: 3, relic: 6, crystal: 1, wild: 1, capsule: 0, beacon: 0, warp: 0 };
const C = P.c ?? 1, G = P.g ?? 1.1, MAXH = P.maxh ?? 50, PICK = 22, WHEEL = 25, FS_START = P.fsstart ?? 3;
const M = h => C * Math.pow(G, h);
function pick() { let t = 0; for (const k in W) t += W[k]; let r = Math.random() * t; for (const k in W) if ((r -= W[k]) < 0) return k; return "scrap"; }
function round(target, free) {
  let h = free ? FS_START : 0, shield = 0, plans = 0, extra = 0, fs = 0, spins = 0;
  for (;;) {
    const s = pick(); spins++;
    if (s === "crash") { if (shield) { shield--; continue; } return { win: extra, fs, spins }; }
    h += D[s];
    if (s === "wild") shield = Math.min(P.shmax ?? 1, shield + 1);
    if (s === "capsule" && ++plans === 3) extra += PICK;
    if (s === "warp") extra += WHEEL;
    if (s === "beacon") fs += 3;
    if (h >= MAXH || (h >= 1 && M(h) >= target)) return { win: M(Math.min(h, MAXH)) + extra, fs, spins };
  }
}
for (const target of P.targets || [1.3, 2, 3, 5, 10, 25]) {
  let N = P.n || 300000, tot = 0, hits = 0, sp = 0;
  for (let i = 0; i < N; i++) { let q = [round(target, false)]; let r = q[0]; let w = r.win; sp += r.spins; let fs = r.fs; while (fs > 0) { fs--; const f = round(target, true); w += f.win; fs += f.fs; } tot += w; if (r.win > 0) hits++; }
  console.log(target, "rtp", (tot / N * 100).toFixed(1), "hit", (hits / N * 100).toFixed(1), "spins/round", (sp / N).toFixed(2));
}
