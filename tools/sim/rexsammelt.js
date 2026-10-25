// Sammler-Simulation Eisenfront
const P = JSON.parse(process.argv[2] || "{}");
const C = 5, R = P.R || 3;
const W = Object.assign({ scrap: 22, cell: 20, chip: 16, core: 12, crystal: 7, relic: 4, wild: 1.5, cash: 14, rex: 2, beacon: 1.2, capsule: .6, warp: .6 }, P.W || {});
const PAYSC = P.paysc ?? 1;
const PAY = P.PAY || { scrap: [.1, .2, .5], cell: [.1, .25, .6], chip: [.15, .3, .8], core: [.2, .5, 1.2], crystal: [.3, .8, 2], relic: [.5, 1.5, 5] };
const VALS = P.vals || [[1, 30], [2, 25], [3, 16], [5, 12], [10, 7], [15, 4], [25, 2.2], [50, 1], [100, .3]];
const JUMP = P.jump ?? .1, DROP = P.drop ?? .25, FSREX = P.fsrex ?? 2, FSCASH = P.fscash ?? 1.4, FSJUMP = P.fsjump ?? .2;
const LEV = [1, 2, 3, 10];
const BONUS_PICK = P.pick ?? 22, BONUS_WHEEL = P.wheel ?? 25; // mittlere Bonusgewinne × Einsatz (wie bisher grob)
function wpick(w) { let t = 0; for (const k in w) t += w[k]; let r = Math.random() * t; for (const k in w) if ((r -= w[k]) < 0) return k; return "scrap"; }
function val() { let t = 0; for (const [, w] of VALS) t += w; let r = Math.random() * t; for (const [v, w] of VALS) if ((r -= w) < 0) return v; return 1; }
function board(free) {
  const b = [];
  for (let c = 0; c < C; c++) { const col = []; const w = { ...W }; if (c === 0 || c === 4) w.wild = 0; if (free) { w.rex *= FSREX; w.cash *= FSCASH; w.beacon *= .8; w.capsule = 0; w.warp = 0; }
    for (let r = 0; r < R; r++) { const id = wpick(w); col.push(id === "cash" ? { id, v: val() } : { id }); } b.push(col); }
  return b;
}
function ways(b) {
  let tot = 0;
  for (const s in PAY) {
    let w = 1, k = 0;
    for (let c = 0; c < C; c++) { const n = b[c].filter(x => x.id === s || x.id === "wild").length; if (!n) break; w *= n; k++; }
    if (k >= 3) tot += PAY[s][k - 3] * w * PAYSC;
  }
  return tot;
}
function collect(b, free, mult) {
  let cash = 0, nc = 0, rex = 0;
  b.flat().forEach(x => { if (x.id === "cash") { cash += x.v; nc++; } if (x.id === "rex") rex++; });
  if (nc && !rex && Math.random() < (free ? FSJUMP : JUMP)) rex = 1;
  if (rex && !nc && Math.random() < DROP) { const n = 1 + (Math.random() * 3 | 0); for (let i = 0; i < n; i++) cash += val(); nc = n; }
  return { win: nc ? cash * rex * mult : 0, rex: nc ? rex : 0 };
}
function count(b, id) { return b.flat().filter(x => x.id === id).length; }
let wayT = 0, colT = 0, wayH = 0;
let N = P.n || 300000, total = 0, hits = 0, fsN = 0, fsTot = 0, bon = 0, maxW = 0, colN = 0;
for (let i = 0; i < N; i++) {
  const b = board(false);
  let w = ways(b); wayT += w; if (w) wayH++; const co = collect(b, false, 1); colT += co.win; w += co.win; if (co.win) colN++;
  const sc = count(b, "beacon");
  if (count(b, "capsule") >= 3) { w += BONUS_PICK; bon++; }
  if (count(b, "warp") >= 3) { w += BONUS_WHEEL; bon++; }
  if (sc >= 3) {
    fsN++; let left = { 3: 10, 4: 15, 5: 20 }[Math.min(sc, 5)], lev = 0, meter = 0, fw = 0;
    while (left > 0) { left--; const fb = board(true); fw += ways(fb); const c2 = collect(fb, true, LEV[lev]); fw += c2.win; meter += c2.rex;
      while (meter >= 4 && lev < 3) { meter -= 4; lev++; left += 10; } if (lev >= 3) meter = Math.min(meter, 4); }
    w += fw; fsTot += fw;
  }
  if (w > 0) hits++; total += w; maxW = Math.max(maxW, w);
}
console.log(JSON.stringify({ way: +(wayT / N * 100).toFixed(1), wayHit: +(wayH / N * 100).toFixed(1), col: +(colT / N * 100).toFixed(1), rtp: +(total / N * 100).toFixed(1), hit: +(hits / N * 100).toFixed(1), collect: +(colN / N * 100).toFixed(1), fsEvery: Math.round(N / fsN), fsMean: +(fsTot / fsN).toFixed(1), fsShare: +(fsTot / total * 100).toFixed(1), bonusEvery: Math.round(N / bon), maxW }));
