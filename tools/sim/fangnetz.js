// Simulation Fangnetz-Kaskaden: 6x5, Schwärme ab 5, Nachfang-Multiplikator
const P = eval("(" + (process.argv[2] || "{}") + ")");
const C = 6, R = 5;
const W = Object.assign({ scrap: 30, cell: 26, chip: 20, core: 14, crystal: 7, relic: 4, beacon: 1.6, capsule: 1.6, warp: 1.6 }, P.w || {});
const PAY = Object.assign({ scrap: [.2,.4,.8,1.5,4], cell: [.3,.6,1.2,2.5,6], chip: [.4,.8,1.6,3.5,8], core: [.6,1.2,2.5,5,12], crystal: [1,2,4,8,20], relic: [1.5,3,6,15,40] }, P.pay || {});
const scale = P.scale || 1;
const ids = Object.keys(W), tot = ids.reduce((a, k) => a + W[k], 0);
const pick = () => { let r = Math.random() * tot; for (const k of ids) if ((r -= W[k]) < 0) return k; return ids[0]; };
const bucket = n => n >= 13 ? 4 : n >= 11 ? 3 : n >= 9 ? 2 : n >= 7 ? 1 : 0;
const MULT = P.mult || [1, 2, 3, 5, 5, 5, 5, 5, 5, 5];
const PICK=[1,1,1,1,2,2,2,3,3,3,5,8,"x2","A","A","A"];
function pickGame(){const a=PICK.slice().sort(()=>Math.random()-.5);let t=0,m=1,al=0;for(const v of a){if(v==="A"){if(++al===3)break}else if(v==="x2")m=2;else t+=v}return t*m}
const RINGS=[[2,3,5,5,8,10,"W","W"],[8,10,15,15,25,"W",20,30],[40,50,75,100,150,300,60,50]];
function wheel(){let l=0;for(;;){const v=RINGS[l][Math.random()*8|0];if(v==="W")l++;else return v}}
function clusters(g) {
  const res = [], seen = new Set();
  for (let c = 0; c < C; c++) for (let r = 0; r < R; r++) {
    const s = g[c][r]; if (!PAY[s] || seen.has(c * 9 + r)) continue;
    const st = [[c, r]], cl = new Set([c * 9 + r]);
    while (st.length) { const [x, y] = st.pop(); for (const [dx, dy] of [[1,0],[-1,0],[0,1],[0,-1]]) { const nx = x + dx, ny = y + dy; if (nx < 0 || ny < 0 || nx >= C || ny >= R) continue; const k = nx * 9 + ny; if (cl.has(k)) continue; const t = g[nx][ny]; if (t === s || t === "wild") { cl.add(k); st.push([nx, ny]); } } }
    for (const k of cl) if (g[(k / 9) | 0][k % 9] === s) seen.add(k);
    if (cl.size >= 5) res.push({ s, cells: [...cl] });
  }
  return res;
}
function round(fsState, gull) {
  const g = Array.from({ length: C }, () => Array.from({ length: R }, pick));
  let win = 0, k = 0, gullUsed = false;
  for (;;) {
    let cl = clusters(g);
    if (!cl.length && k === 0 && !gullUsed && Math.random() < gull) { gullUsed = true; const n = 1 + (Math.random() * 3 | 0); for (let i = 0; i < n; i++) { const c = Math.random() * C | 0, r = Math.random() * R | 0; if (PAY[g[c][r]]) g[c][r] = "wild"; } cl = clusters(g); }
    if (!cl.length) break;
    let m;
    if (fsState) { m = fsState.m; fsState.m = Math.min(P.fsMax || 10, fsState.m + 1); } else m = MULT[Math.min(k, MULT.length - 1)];
    k++;
    const rm = new Set();
    for (const x of cl) { win += PAY[x.s][bucket(x.cells.length)] * scale * m; x.cells.forEach(q => rm.add(q)); }
    for (let c = 0; c < C; c++) { const keep = []; for (let r = 0; r < R; r++) if (!rm.has(c * 9 + r)) keep.push(g[c][r]); while (keep.length < R) keep.unshift(pick()); g[c] = keep; }
  }
  const cnt = id => g.flat().filter(x => x === id).length;
  return { win, k, b: cnt("beacon"), cap: cnt("capsule"), warp: cnt("warp") };
}
const FS = { 3: 8, 4: 12, 5: 20 };
let bn = 0, N = P.n || 300000, tot2 = 0, hits = 0, fsN = 0, fsSum = 0, bon = 0, any = 0, base = 0;
for (let i = 0; i < N; i++) {
  const r = round(null, P.gull ?? .08);
  let t = r.win; base += r.win; if (r.win > 0) hits++;
  if (r.cap >= 3) { const v = pickGame(); t += v; bon += v; bn++; }
  if (r.warp >= 3) { const v = wheel(); t += v; bon += v; bn++; }
  if (r.b >= 3) {
    fsN++; let left = FS[Math.min(r.b, 5)], fw = 0; const st = { m: P.fsStart || 1 };
    while (left-- > 0) { const q = round(st, P.fsGull ?? .25); fw += q.win; if (q.b >= 3) left += FS[Math.min(q.b, 5)]; if (q.cap >= 3) fw += pickGame(); if (q.warp >= 3) fw += wheel(); }
    t += fw; fsSum += fw;
  }
  tot2 += t; if (t > 0) any++;
}
console.log(JSON.stringify(P).slice(0, 80), "RTP", (tot2 / N).toFixed(3), "Basis", (base / N).toFixed(3), "Treffer", (hits / N).toFixed(3), "FS 1/" + (fsN ? N / fsN | 0 : 0), "FS-Mittel", fsN ? (fsSum / fsN).toFixed(1) : 0, "Bonus", (bon / N).toFixed(3), "Bonus 1/" + (N / bn | 0));
