# Neustadt Teil 3: eigenes Grundspiel "Skyline-Walzen" (6 Walzen als Hochhäuser, jede pro Dreh 2 bis 7 Felder hoch)
# Seit Neustadt 0.4.0. Vorher: Hochstapler (0.1/0.2), Stadtrundfahrt (0.3). Balance: tools/sim/skyline.js

SKY_HTML = [
    ('''        <div class="bay net col" id="bay">
          <div class="netgrid" id="netGrid" aria-label="Werkbank mit 5 Walzen und 3 Reihen"></div>
          <div class="casc" id="casc" hidden>Rex sammelt <b id="cascN">0</b></div>''',
     '''        <div class="bay sky" id="bay">
          <div class="sk-head"><div class="sk-ways"><span>Gewinnwege</span><b id="skWays">0</b><small id="skWaysCalc">&nbsp;</small></div><div class="sk-mult" id="skMultBox" hidden><span>Multiplikator</span><b id="skMult">×1</b></div></div>
          <div class="sk-city" id="skCity" aria-label="Skyline mit 6 Walzen"></div>
          <div class="casc" id="casc" hidden>Nachbau <b id="cascN">0</b></div>'''),
    ('<span><b id="fsLeft">0</b> übrig · Rex <b id="fsStick">0</b>/4 · Sammler <em class="fsmult" id="fsMultBox">×<b id="fsMult">1</b></em> · bisher <b id="fsWin">0</b></span>',
     '<span><b id="fsLeft">0</b> übrig · Multiplikator <em class="fsmult" id="fsMultBox">×<b id="fsMult">1</b></em><b id="fsStick" hidden>0</b> · bisher <b id="fsWin">0</b></span>'),
    ('<th>Teil</th><th>3 Walzen</th><th>4 Walzen</th><th>5 Walzen</th>', '<th>Symbol</th><th>3 Walzen</th><th>4 Walzen</th><th>5 Walzen</th><th>6 Walzen</th>'),
    ('aria-controls="panel-lines">Wege</button>', 'aria-controls="panel-lines">Höhen</button>'),
]

SKY_CSS = r'''
/* ---------- Neustadt: Stadtbild in Pixeloptik ---------- */
#sky, #focusSky { image-rendering: pixelated; image-rendering: crisp-edges; }
.ship.pixel { shape-rendering: crispEdges; }
/* ---------- Neustadt: Skyline-Walzen ---------- */
.frame { grid-template-columns: minmax(0, 1fr); width: min(100%, 680px); margin: 0 auto; }
.bay.sky { display: grid; grid-template-columns: minmax(0, 1fr); gap: 8px; position: relative; min-height: 0; }
.sk-head { display: flex; justify-content: space-between; align-items: stretch; gap: 8px; }
.sk-ways, .sk-mult { display: grid; gap: 0; padding: 6px 12px; border-radius: 10px; background: rgba(0,0,0,.3); border: 1px solid var(--line); line-height: 1.1; min-width: 0; }
.sk-ways span, .sk-mult span { font: 700 .56rem var(--f-body); letter-spacing: .14em; text-transform: uppercase; color: var(--ink-soft); }
.sk-ways b { font: 700 1.25rem var(--f-mono); color: #ffd27a; background: none; border: 0; padding: 0; box-shadow: none; }
.sk-ways small { font: 600 .64rem var(--f-mono); color: var(--ink-soft); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.sk-ways b.up { animation: skUp .45s cubic-bezier(.3,1.6,.5,1); }
@keyframes skUp { 40% { transform: scale(1.15); color: #ffffff; } }
.sk-mult { justify-items: end; border-color: #c6f06b; background: rgba(198,240,107,.12); }
.sk-mult b { font: 800 1.4rem var(--f-mono); color: #c6f06b; background: none; border: 0; padding: 0; box-shadow: none; }
.sk-mult b.up { animation: skUp .5s cubic-bezier(.3,1.6,.5,1); }
.sk-city { --skc: 52px; position: relative; display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 6px; align-items: end; overflow: hidden; border-radius: 12px; padding: 8px 8px 0;
  height: calc(var(--skc) * 7.6 + 22px); image-rendering: pixelated;
  background: linear-gradient(180deg, #0c1430 0%, #1c2858 55%, #3a3a6a 82%, #5a4a6a 100%); box-shadow: inset 0 0 0 1px rgba(255,255,255,.08); }
.sk-city::before { content: ""; position: absolute; inset: 0 0 auto; height: 60%; pointer-events: none; opacity: .7;
  background-image: radial-gradient(#ffffff 1px, transparent 1.4px), radial-gradient(#9ad4ff 1px, transparent 1.4px); background-size: 61px 47px, 89px 71px; background-position: 7px 11px, 33px 29px; }
.sk-city::after { content: ""; position: absolute; left: 0; right: 0; bottom: 0; height: 14px; pointer-events: none;
  background: repeating-linear-gradient(90deg, #3a3a42 0 12px, #2e2e36 12px 24px); box-shadow: 0 -3px 0 #5a5a64; }
.sk-col { position: relative; z-index: 1; display: flex; flex-direction: column; justify-content: flex-end; min-width: 0; margin-bottom: 14px; }
.sk-roof { height: calc(var(--skc) * .5); }
.sk-roof svg { display: block; width: 100%; height: 100%; }
.sk-roof .blink { animation: skBlink 1.2s steps(2) infinite; }
@keyframes skBlink { 50% { opacity: .2; } }
.sk-stack { position: relative; height: calc(var(--skc) * 4); transition: height .32s cubic-bezier(.3,1.3,.5,1); background: var(--face);
  box-shadow: inset 4px 0 0 rgba(255,255,255,.12), inset -4px 0 0 rgba(0,0,0,.25), 0 0 0 2px var(--trim); }
.sk-c { position: absolute; left: 0; right: 0; height: var(--skc); display: grid; place-items: center; transition: bottom .34s cubic-bezier(.3,1.25,.5,1), opacity .25s, transform .25s; }
.sk-c::before { content: ""; position: absolute; inset: 3px 4px; border-radius: 2px; background: rgba(8,14,30,.55); box-shadow: inset 0 0 0 2px rgba(0,0,0,.35); }
.sk-c svg { position: relative; width: 82%; height: 82%; max-width: calc(var(--skc) * .92); }
.sk-c.out { opacity: 0; transform: translateY(30px); }
.sk-c.hit::before { background: rgba(255,211,74,.35); box-shadow: inset 0 0 0 2px #ffd34a, 0 0 12px #ffd34a; }
.sk-c.hit svg { animation: skPop .45s cubic-bezier(.3,1.7,.5,1) infinite alternate; }
@keyframes skPop { to { transform: scale(1.12); } }
.sk-c.boom { transform: scale(0) rotate(25deg); opacity: 0; transition: transform .25s ease-in, opacity .25s; }
.sk-h { position: absolute; right: 2px; top: -2px; z-index: 2; font: 700 .55rem var(--f-mono); color: rgba(255,255,255,.7); font-style: normal; text-shadow: 0 1px 0 #000; }
.sk-float { position: absolute; left: 50%; top: 30%; z-index: 9; transform: translate(-50%, 0); display: grid; justify-items: center; gap: 2px; padding: 8px 16px; border-radius: 8px; pointer-events: none; text-align: center;
  background: rgba(8,12,30,.9); box-shadow: 0 0 0 3px var(--fc, #ffd34a), 6px 6px 0 rgba(0,0,0,.4); animation: skFloat 1.3s steps(12) forwards; }
.sk-float b { font: 800 1.3rem var(--f-mono); color: var(--fc, #ffd34a); white-space: nowrap; }
.sk-float small { font: 700 .7rem var(--f-body); color: #ffffff; white-space: nowrap; }
@keyframes skFloat { 0% { opacity: 0; transform: translate(-50%, 12px); } 15% { opacity: 1; transform: translate(-50%, 0); } 80% { opacity: 1; } 100% { opacity: 0; transform: translate(-50%, -14px); } }
.bay.sky .casc { position: absolute; left: 50%; top: 64px; transform: translateX(-50%); z-index: 8; }
@media (max-width: 600px) { .sk-city { gap: 4px; padding: 6px 5px 0; } .sk-ways b { font-size: 1.05rem; } .sk-float b { font-size: 1.05rem; } .sk-float small { white-space: normal; } }
@media (prefers-reduced-motion: reduce) { .sk-c, .sk-stack { transition: none; } .sk-c.hit svg, .sk-roof .blink { animation: none; } }
'''

SKY_JS = r'''
/* ===================== Neustadt: Skyline-Walzen =====================
   6 Walzen, jede ist bei jedem Dreh 2 bis 7 Felder hoch (sichtbar als Hochhaus). Gewinnwege = Produkt der Höhen.
   Gewinn: gleiches Symbol auf mindestens 3 Walzen nebeneinander ab Walze 1, Kran (Wild, Walze 2 bis 5) ersetzt alles.
   Wert = Auszahlung × Anzahl der Wege (Treffer je Walze multipliziert) × Einsatz × SK_SCALE.
   Nachbau: Gewinnteile verschwinden, Neues rutscht von oben nach, bis kein Gewinn mehr kommt.
   Freibauten: 4+ Baugenehmigungen = 10 (+2 je weitere), Multiplikator +1 pro Nachbau bis ×15, bleibt über alle Freibauten.
   3+ Stadtbusse: Stadtlotterie (Glücksrad).
   Balance per Simulation (tools/sim/skyline.js): Auszahlung ~113 %, Freibauten ~1/124. */
const SK_HW = { 2: 14, 3: 24, 4: 24, 5: 18, 6: 12, 7: 8 };
const SK_W = { tree: 19, lamp: 19, scrap: 17, cell: 16, chip: 14, core: 12, crystal: 9, relic: 6, wild: 3.2, beacon: 3.8, warp: 1.1 };
const SK_PAY = { relic: [.5, 1, 2.5, 5], crystal: [.3, .6, 1, 2], core: [.2, .4, .6, 1.2], chip: [.15, .25, .4, .8], cell: [.1, .2, .3, .6], scrap: [.1, .15, .25, .5], lamp: [.05, .1, .2, .4], tree: [.05, .1, .2, .4] };
const SK_SCALE = .56, SK_FS = 10, SK_FS_EXTRA = 2, SK_FS_RE = 5, SK_MULT_MAX = 15, SK_N = 6;
const SK_SYMS = Object.keys(SK_PAY);
const SK_COL = [{ face: "#5a4a7a", trim: "#3a2a5a" }, { face: "#2f5a7a", trim: "#1c3a52" }, { face: "#7a4a3a", trim: "#52281c" }, { face: "#2f6a5a", trim: "#1c4a3a" }, { face: "#6a5a3a", trim: "#4a3a1c" }, { face: "#4a5a72", trim: "#2c3a4e" }];
ICONS.tree = `<svg viewBox="0 0 40 40" shape-rendering="crispEdges"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#13283a" stroke="#5fbf4a" stroke-width="1.6" shape-rendering="auto"/><rect x="18" y="24" width="4" height="9" fill="#7a5a3a"/><rect x="12" y="10" width="16" height="14" fill="#3fa84a"/><rect x="10" y="14" width="20" height="7" fill="#3fa84a"/><rect x="15" y="7" width="10" height="4" fill="#5fbf4a"/><rect x="14" y="12" width="4" height="3" fill="#7ed957"/><rect x="22" y="17" width="3" height="3" fill="#2f8a3a"/><rect x="11" y="33" width="18" height="2" fill="#5a8a3a"/></svg>`;
ICONS.lamp = `<svg viewBox="0 0 40 40" shape-rendering="crispEdges"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#13283a" stroke="#ffd27a" stroke-width="1.6" shape-rendering="auto"/><rect x="11" y="7" width="18" height="16" fill="#ffd27a" opacity=".18"/><rect x="18" y="16" width="4" height="17" fill="#4a5a6a"/><rect x="15" y="9" width="10" height="2" fill="#2a3440"/><rect x="16" y="11" width="8" height="6" fill="#ffe39a"/><rect x="17" y="12" width="3" height="3" fill="#ffffff"/><rect x="15" y="17" width="10" height="2" fill="#2a3440"/><rect x="14" y="32" width="12" height="2" fill="#2a3440"/></svg>`;
BY_ID.tree = { id: "tree", name: "Baum", color: "#5fbf4a" };
BY_ID.lamp = { id: "lamp", name: "Laterne", color: "#ffd27a" };
const skSym = id => id === "wild" ? WILD : BY_ID[id];
let sk = null, skGrid = null, skCols = [], skSpinning = false, skFast = false, skM = 1, skFsBet = 0, twMiniKey = null, netCascading = false, colRun = null;

function skPickH() { let t = 0; for (const k in SK_HW) t += SK_HW[k]; let r = Math.random() * t; for (const k in SK_HW) if ((r -= SK_HW[k]) < 0) return +k; return 4; }
function skPick(reel) {
  const w = { ...SK_W };
  if (!(reel >= 1 && reel <= 4)) w.wild = 0;
  if (boostOn("drones")) w.wild *= 3;
  if (boostOn("signal")) w.beacon *= 2.5;
  let t = 0; for (const k in w) t += w[k];
  let r = Math.random() * t; for (const k in w) if ((r -= w[k]) < 0) return k;
  return "tree";
}
const skNewGrid = () => Array.from({ length: SK_N }, (_, r) => Array.from({ length: skPickH() }, () => skPick(r)));
function skEvaluate(g) {
  let total = 0; const wins = [], hit = g.map(c => c.map(() => false));
  for (const s of SK_SYMS) {
    let ways = 1, run = 0, wild = false;
    for (let r = 0; r < SK_N; r++) { const c = g[r].filter(x => x === s || x === "wild").length; if (!c) break; if (g[r].includes("wild")) wild = true; ways *= c; run++; }
    if (run >= 3) {
      const f = SK_PAY[s][run - 3] * ways * SK_SCALE; total += f; wins.push({ s, run, ways, f, wild });
      for (let r = 0; r < run; r++) g[r].forEach((x, i) => { if (x === s || x === "wild") hit[r][i] = true; });
    }
  }
  return { total, wins, hit };
}
const skWaysOf = g => g.reduce((a, c) => a * c.length, 1);
const skFmt = n => n.toLocaleString("de-DE");

/* ----- Grafik: Hochhäuser in Pixeloptik ----- */
function skRoof(h, r) {
  const c = SK_COL[r]; let px;
  if (h <= 3) px = [[1, 6, 14, 2, "#8a3a30"], [3, 4, 10, 2, "#a8443a"], [5, 2, 6, 2, "#c8553d"], [7, 0, 2, 2, "#e06a4a"], [11, 1, 2, 4, "#4a4a52"]];
  else if (h <= 5) px = [[0, 6, 16, 2, c.trim], [3, 2, 5, 4, "#7a8a98"], [3, 2, 5, 1, "#9aaab8"], [10, 4, 3, 2, "#5a6a78"], [12, 3, 1, 1, "#9aaab8"]];
  else if (h === 6) px = [[0, 6, 16, 2, c.trim], [2, 4, 12, 2, c.face], [7, 0, 2, 4, "#c9ccd1"], [7, 0, 2, 1, "#ff4b5c", 1]];
  else px = [[0, 6, 16, 2, c.trim], [2, 4, 12, 2, c.face], [4, 2, 8, 2, c.face], [6, 1, 4, 1, "#ffd34a"], [7, 0, 2, 1, "#ffffff", 1]];
  return `<svg viewBox="0 0 16 8" shape-rendering="crispEdges" preserveAspectRatio="none">${px.map(([x, y, w, hh, f, b]) => `<rect x="${x}" y="${y}" width="${w}" height="${hh}" fill="${f}"${b ? ' class="blink"' : ""}/>`).join("")}</svg>`;
}
function skCell(id) {
  const d = document.createElement("div"), x = skSym(id);
  d.className = "sk-c"; d.dataset.sym = id; d.innerHTML = ICONS[id] || ""; d.setAttribute("aria-label", x ? x.name : id);
  return d;
}
const skRow = row => `calc(var(--skc) * ${row})`;
function skSize() {
  const city = $("skCity"); if (!city || !city.clientWidth) return;
  const small = innerWidth <= 600, w = city.clientWidth - (small ? 10 : 16), gap = small ? 4 : 6, col = (w - gap * 5) / 6;
  const c = Math.max(28, Math.min(60, Math.floor(col * .95), Math.floor((small ? 340 : 430) / 7.6)));
  city.style.setProperty("--skc", c + "px");
}
function skSetup() {
  const city = $("skCity"); city.innerHTML = ""; skCols = [];
  for (let r = 0; r < SK_N; r++) {
    const el = document.createElement("div"); el.className = "sk-col"; el.dataset.r = r;
    el.style.setProperty("--face", SK_COL[r].face); el.style.setProperty("--trim", SK_COL[r].trim);
    el.innerHTML = `<div class="sk-roof"></div><div class="sk-stack"></div><i class="sk-h"></i>`;
    city.appendChild(el);
    skCols.push({ el, roof: el.firstElementChild, stack: el.children[1], lab: el.children[2] });
  }
  skSize();
  skGrid = skNewGrid();
  skGrid.forEach((ids, r) => skBuildCol(r, ids, false));
  skWaysUi(false);
}
function skBuildCol(r, ids, drop) {
  const col = skCols[r], h = ids.length;
  col.stack.innerHTML = ""; col.stack.style.height = skRow(h); col.roof.innerHTML = skRoof(h, r); col.lab.textContent = h;
  const els = ids.map((id, row) => { const el = skCell(id); el.style.bottom = skRow(drop ? row + h + 1 : row); if (drop) el.style.opacity = "0"; col.stack.appendChild(el); return el; });
  if (drop) { void col.stack.offsetWidth; els.forEach((el, row) => { el.style.transitionDelay = (row * 22) + "ms"; el.style.bottom = skRow(row); el.style.opacity = "1"; }); setTimeout(() => els.forEach(el => el.style.transitionDelay = ""), 700); }
}
function skWaysUi(pop) {
  const ways = skWaysOf(skGrid), b = $("skWays");
  b.textContent = skFmt(ways); $("skWaysCalc").textContent = skGrid.map(c => c.length).join(" · ");
  if (pop) { b.classList.remove("up"); void b.offsetWidth; b.classList.add("up"); }
  maxStat("maxWays", ways);
}
function skMultUi(pop) {
  const show = !!(sk && sk.free) || inFs() || fsActive;
  $("skMultBox").hidden = !show; $("skMult").textContent = "×" + skM; $("fsMult").textContent = skM;
  if (pop) { const b = $("skMult"); b.classList.remove("up"); void b.offsetWidth; b.classList.add("up"); }
}
function skFloat(text, sub, color) {
  const f = document.createElement("div"); f.className = "sk-float"; f.style.setProperty("--fc", color || "#ffd34a");
  f.innerHTML = `<b>${text}</b>${sub ? `<small>${sub}</small>` : ""}`; $("bay").appendChild(f); setTimeout(() => f.remove(), 1350);
}
function netDust(pts) {
  state.dustMeter = (state.dustMeter || 0) + pts;
  let whole = 0;
  while (state.dustMeter >= 100) { state.dustMeter -= 100; whole++; }
  if (whole) addDust(whole, null); else renderDust(false);
}
function gainDustFromSpin() {}
function renderSticky() {}

/* ----- Ablauf eines Drehs ----- */
function spin(auto) {
  if (!ready || sk || busy || spinning || skipCelebration || !$("scratch").hidden || !$("bonus").hidden || !$("naming").hidden || !$("worlds").hidden) return;
  const free = inFs();
  if (!free && state.credits < bet()) return;
  slammed = false;
  if (free) { fsLeft--; fsActive = true; }
  else {
    state.credits -= bet(); state.spins++; countCredits(state.credits, 250);
    sess.spins++; sess.bet += bet(); clearGamble();
    state.pot += bet() * JP_FEED; addXP(bet()); track("spins");
    bipState.lastSession++;
    if (bipState.lastSession % 200 === 0) setTimeout(() => bip("session", 2), 400);
  }
  sk = { bet: free ? (skFsBet || bet()) : bet(), free, win: 0, bonus: 0, fs: 0, dust: 2, boost: false, casc: 0 };
  boostSpinActive = false;
  if (!free && state.boostReady) { sk.boost = true; boostSpinActive = true; state.boostReady = 0; state.luck = 0; sfx.boostSpin(); }
  busy = true; skFast = false;
  $("lastWin").textContent = "0"; $("lastWin").classList.remove("pos");
  $("msg").className = free ? "msg fs" : "msg"; $("msg").textContent = free ? `Freibau ${fsTotal - fsLeft} von ${fsTotal} …` : "Die Skyline wird neu gebaut …";
  skMultUi(false); render();
  skRun();
}
async function skDrop(g) {
  skSpinning = spinning = true; render(); sfx.start();
  skCols.forEach(c => c.stack.querySelectorAll(".sk-c").forEach(el => el.classList.add("out")));
  await wait(skFast || reduced ? 0 : 180 * T());
  skGrid = g.map(c => c.slice());
  for (let r = 0; r < SK_N; r++) {
    skBuildCol(r, g[r], !reduced);
    sfx.stop();
    if (!skFast && !reduced) await wait(115 * T());
  }
  skWaysUi(true);
  await wait(skFast || reduced ? 80 : 360 * T());
  skSpinning = spinning = false; render();
}
async function skRun() {
  let g = skNewGrid();
  if (sk.boost) for (let k = 0; k < 300 && skEvaluate(g).total <= 0; k++) g = skNewGrid();
  await skDrop(g);
  const flat = skGrid.flat(), scat = flat.filter(x => x === "beacon").length, bus = flat.filter(x => x === "warp").length;
  sk.dust += 8 * flat.filter(x => x === "crystal").length;
  const msg = $("msg");
  for (;;) {
    const e = skEvaluate(skGrid); if (e.total <= 0) break;
    sk.casc++;
    const m = sk.free ? skM : 1, amt = Math.max(1, Math.round(e.total * sk.bet * m * lineBoost()));
    sk.win += amt;
    e.wins.forEach(w => { track("symwin", 1, w.s); if (w.run === 6) { track("four"); bump("six"); } if (w.wild) { track("laser"); bump("lasers"); } });
    await skShowWin(e, amt, m);
    if (sk.free) { skM = Math.min(SK_MULT_MAX, skM + 1); skMultUi(true); }
    await skCascade(e.hit);
  }
  maxStat("maxCasc", sk.casc);
  if (sk.casc >= 3) { bipState.last = 0; bip("casc", 2); }
  // Baugenehmigungen zählen auf der ersten Skyline des Drehs
  let award = 0;
  if (!sk.free && scat >= 4) award = SK_FS + (scat - 4) * SK_FS_EXTRA;
  else if (sk.free && scat >= 3) award = SK_FS_RE;
  if (award) {
    sk.fs = award; fsLeft += award; fsTotal += award; skFsBet = sk.bet;
    if (!sk.free) { state.fsRounds++; fsWin = 0; skM = 1; bump("fs"); track("fs"); }
    sfx.scatter(scat); skFloat(`+${award} Freibauten`, `${scat} Baugenehmigungen`, "#c6f06b");
    addLog("beacon", sk.free ? "Freibauten verlängert" : "Freibauten ausgelöst", `+${award}`, "#c6f06b");
    msg.className = "msg fs"; msg.textContent = sk.free ? `Noch mehr Baugenehmigungen: +${award} Freibauten!` : `${scat} Baugenehmigungen: ${award} Freibauten! Der Multiplikator wächst mit jedem Nachbau.`;
    await wait(700 * T());
  }
  if (bus >= 3) await skBonus("warp");
  return skEnd();
}
async function skShowWin(e, amt, m) {
  e.hit.forEach((col, r) => col.forEach((h, i) => { if (h) { const el = skCols[r].stack.children[i]; if (el) el.classList.add("hit"); } }));
  const best = e.wins.slice().sort((a, b) => b.f - a.f)[0], s = skSym(best.s);
  sfx.coin(Math.min(3, e.wins.length + 1)); if (sk.casc >= 2) sfx.mult();
  skFloat(`+${skFmt(amt)}`, `${s.name} · ${best.run} Häuser · ${skFmt(best.ways)} Wege${m > 1 ? ` · ×${m}` : ""}`, s.color || "#ffd34a");
  const c = $("casc"); if (sk.casc >= 2) { c.hidden = false; $("cascN").textContent = sk.casc; } else c.hidden = true;
  $("lastWin").textContent = sk.win; $("lastWin").classList.add("pos");
  const msg = $("msg"); msg.className = sk.free ? "msg fs" : "msg win";
  msg.textContent = `${e.wins.map(w => `${skSym(w.s).name} ×${w.run}`).join(", ")}: +${skFmt(amt)} Taler${sk.casc >= 2 ? ` · Nachbau ${sk.casc}` : ""}`;
  await wait((skFast ? 300 : 850) * T());
}
async function skCascade(hit) {
  skCols.forEach((c, r) => [...c.stack.children].forEach((el, i) => { if (hit[r][i]) { el.classList.remove("hit"); el.classList.add("boom"); } }));
  sfx.small();
  await wait((reduced ? 0 : 260) * T());
  skCols.forEach((c, r) => {
    const els = [...c.stack.children], keep = els.filter((el, i) => !hit[r][i]);
    els.forEach((el, i) => { if (hit[r][i]) el.remove(); });
    const h = skGrid[r].length, add = [];
    while (keep.length + add.length < h) add.push(skPick(r));
    add.forEach((id, k) => { const el = skCell(id); el.style.bottom = skRow(h + k + 1); el.style.opacity = "0"; c.stack.appendChild(el); });
    skGrid[r] = [...keep.map(el => el.dataset.sym), ...add];
  });
  skCols.forEach(c => void c.stack.offsetWidth);
  skCols.forEach(c => [...c.stack.children].forEach((el, row) => { el.style.bottom = skRow(row); el.style.opacity = "1"; }));
  await wait((skFast || reduced ? 120 : 420) * T());
}
async function skBonus(id) {
  const f = { id, bonus: "wheel", title: "Stadtlotterie", color: "#ff7a59", cells: [] };
  await celebrateFeature(f);
  const amount = Math.round((await runBonus(f)) * bonusBoost() * (sk.free ? Math.max(1, skM) : 1));
  state.credits += amount; sk.bonus += amount;
  state.best = Math.max(state.best, amount); state.peak = Math.max(state.peak, state.credits);
  state.bonusCount = (state.bonusCount || 0) + 1; bump("pick"); track("bonus", 1);
  track("haul", amount); sess.won += amount; sess.best = Math.max(sess.best, amount);
  addDust(1, f.title); addLog(id, f.title, "+" + amount, f.color);
  render();
  if (amount > 0) await celebrateWin(amount, state.credits);
  bip(amount >= bet() * 10 ? "bonusGood" : "bonusMeh", 3);
}
async function skEnd() {
  const r = sk, free = r.free, msg = $("msg");
  sk = null; busy = true; $("casc").hidden = true;
  netDust(r.dust);
  const prevStreak = streak;
  if (!free) { if (r.win + r.bonus >= r.bet) streak++; else streak = 0; }
  const sMult = free ? 1 : streakMult();
  const win = Math.round(r.win * sMult);
  if (!free) {
    if (streak >= 2 && streak > prevStreak) { sfx.streakUp(streak); renderStreak(true); }
    else if (prevStreak >= 2 && streak === 0) { sfx.streakBreak(); renderStreak(false); radio("Funk: Strähne gerissen. Neuer Anlauf.", false, 4000); }
    else renderStreak(false);
  }
  if (win >= r.bet * 10) track("bigwin");
  if (!free && streak >= 3) track("streak");
  if (win > 0) track("haul", win);
  state.credits += win;
  if (free) fsWin += win + r.bonus;
  state.best = Math.max(state.best, win);
  state.peak = Math.max(state.peak, state.credits);
  if (win > 0) { msg.className = free ? "msg fs" : "msg win"; msg.textContent = `${r.boost ? "Paule-Boost! " : ""}Gewinn: +${skFmt(win)} Taler${r.casc >= 2 ? ` · ${r.casc} Nachbauten` : ""}${sMult > 1 ? ` · Strähne ×${String(sMult).replace(".", ",")}` : ""}.`; }
  else if (!r.fs) { msg.className = "msg"; msg.textContent = "Kein Gewinn. Die nächste Skyline wartet."; }
  bipAfterSpin({ win: win + r.bonus, factor: (win + r.bonus) / r.bet, lasered: false, award: r.fs && !free ? r.fs : 0, features: 0, prevStreak, streak, free });
  if (!free && win >= r.bet * 15) setTimeout(() => addDust(1, "großer Bau"), 1200);
  if (win > 0) { bump("wins"); sess.won += win; sess.best = Math.max(sess.best, win); if (!free) maxStat("maxFactor", (win + r.bonus) / r.bet); }
  maxStat("maxStreak", streak);
  render();
  if (win > 0) { await wait(120 * T()); await celebrateWin(win, state.credits); }
  if (r.fs && !free) await simpleBanner({ tier: "Baugenehmigung", color: "var(--lime)", sub: "Freibauten: kostenlos, Multiplikator wächst mit jedem Nachbau" }, `+${r.fs} Freibauten`, sfx.fs, ["#c6f06b", "#7ee0c8", "#ffffff"], 2200);
  if (inFs()) {
    busy = false; fsActive = true; render(); skMultUi(false);
    msg.className = "msg fs"; msg.textContent = `${win ? `+${skFmt(win)} Taler. ` : ""}Noch ${fsLeft} Freibau${fsLeft === 1 ? "" : "ten"}, Multiplikator ×${skM}.`;
    saveGame(); checkAch();
    if (autoLeft > 0) { await wait(500 * T()); spin(); }
    return;
  }
  if (free) {
    fsActive = false;
    msg.className = "msg win"; msg.textContent = `Freibauten beendet: insgesamt +${skFmt(fsWin)} Taler.`;
    if (fsWin >= r.bet * 50) setTimeout(() => addDust(2, "starke Freibauten"), 2500);
    addLog("beacon", "Freibauten gesamt", "+" + fsWin, "#c6f06b");
    await celebrateFsEnd(fsWin, state.credits);
    bip("fsend", 2); fsTotal = 0; skM = 1; skMultUi(false);
  }
  countCredits(state.credits, 0);
  fsActive = false;
  if (!free && Math.random() < r.bet / JP_DIV * (boostOn("treasure") ? 5 : 1)) {
    const amount = Math.floor(state.pot);
    state.pot = JP_SEED; state.credits += amount;
    state.best = Math.max(state.best, amount); state.peak = Math.max(state.peak, state.credits);
    autoLeft = 0; clearAutoMarks();
    addLog("relic", "STADTSCHATZ", "+" + amount, "#ffd34a");
    radio(`Funk: STADTSCHATZ GEHOBEN! ${amount} Taler. Die ganze Stadt feiert.`, true, 15000);
    renderMeta(); bump("jackpots"); sess.won += amount; setTimeout(() => addDust(5, "Stadtschatz"), 5000);
    await celebrateJackpot(amount, state.credits);
    bip("jackpot", 3);
    msg.className = "msg gold"; msg.textContent = `Stadtschatz gehoben: +${amount} Taler!`;
  }
  await processProgress();
  if (state.credits < 5) { autoLeft = 0; clearAutoMarks(); await handleBankruptcy(); }
  if (!free && Math.random() < 1 / 150) findAlbumItem(curSector().id, "Dreh");
  if (!free) {
    if (win > 0 || r.fs || r.bonus) state.luck = 0; else state.luck = (state.luck || 0) + 1;
    if (r.boost && win > 0) { setTimeout(() => { bipState.last = 0; bip("boostWin", 3); }, 300); }
    if (state.luck >= BOOST_AT && !state.boostReady) await activateBoost();
    else if (state.luck === Math.round(BOOST_AT / 2)) bip("charging", 2);
    renderLuck();
  }
  checkAch(); sessPoint();
  if (!free && win >= r.bet && autoLeft === 0 && state.credits >= 5) offerGamble(win);
  busy = false; boostSpinActive = false;
  saveGame();
  if (autoLeft > 0) {
    if (state.credits >= bet()) { autoLeft--; render(); await wait(400 * T()); if (autoLeft >= 0 && !spinning && !busy && !sk) { if (autoLeft === 0) clearAutoMarks(); spin(); return; } }
    else { autoLeft = 0; clearAutoMarks(); }
  }
  render();
}
function quickStop() { skFast = true; }
function press() {
  if (!$("bonus").hidden || !$("scratch").hidden) return;
  if (skipCelebration) { skipCelebration(); return; }
  if (sk) { skFast = true; return; }
  spin();
}
function evaluate(board) { return { wins: [], scatters: [], scatterReels: 0, features: [] }; }
function finish() {}

/* ----- Oberfläche ----- */
const renderBase = render;
render = function () {
  renderBase();
  const fsMode = inFs() || fsActive, btn = $("spin");
  $("spinLabel").textContent = skSpinning ? "…" : sk ? "Schneller" : busy ? "Weiter" : fsMode ? "Freibau" : "Bauen";
  btn.setAttribute("aria-label", sk ? "Schneller bauen" : busy ? "Feier überspringen" : "Neue Skyline bauen");
  btn.disabled = !ready || (!sk && !busy && !inFs() && state.credits < bet());
  if (sk) $("betVal").textContent = sk.free ? "frei" : sk.bet;
  if ($("skMultBox")) skMultUi(false);
};
window.addEventListener("resize", skSize);
if (window.ResizeObserver) new ResizeObserver(skSize).observe($("bay"));

function buildInfo() {
  const v = (s, k) => { const t = SK_PAY[s][k] * SK_SCALE * bet() * lineBoost(); return t >= 10 ? Math.round(t).toLocaleString("de-DE") : t.toFixed(2).replace(".", ","); };
  $("payRows").innerHTML = SK_SYMS.map(s => `<tr><td>${ICONS[s]}${skSym(s).name}</td>${[0, 1, 2, 3].map(k => `<td class="pay">${v(s, k)}</td>`).join("")}</tr>`).join("");
  $("panel-bonus").innerHTML = `
    <div class="feat" style="--fc:#ffd27a">${ICONS.core}<div><h3>Skyline-Walzen</h3><p>Sechs Walzen stehen als sechs Hochhäuser nebeneinander. Bei jedem Dreh ist jedes Haus 2 bis 7 Felder hoch. Die Zahl der Gewinnwege ist das Produkt der Höhen, bis zu 117.649.</p></div></div>
    <div class="feat" style="--fc:#7ed957">${ICONS.scrap}<div><h3>Gewinne</h3><p>Gleiche Symbole auf mindestens 3 Häusern nebeneinander, beginnend links. Wie viele davon pro Haus stehen, wird multipliziert: 2 × 3 × 1 = 6 Wege. Die Tabelle zeigt Taler pro Weg beim aktuellen Einsatz.</p></div></div>
    <div class="feat" style="--fc:#ffc94a">${ICONS.relic}<div><h3>Nachbau</h3><p>Gewinnfelder verschwinden, Neues rutscht von oben nach. Das geht so lange, bis kein Gewinn mehr kommt.</p></div></div>
    <div class="feat" style="--fc:#ffffff">${ICONS.wild}<div><h3>Kran</h3><p>Der Kran kommt auf den Häusern 2 bis 5 vor und ersetzt jedes Symbol außer Baugenehmigung und Stadtbus.</p></div></div>
    <div class="feat" style="--fc:#c6f06b">${ICONS.beacon}<div><h3>Baugenehmigung · Freibauten</h3><p>4 oder mehr Baugenehmigungen irgendwo bringen ${SK_FS} Freibauten, jede weitere +${SK_FS_EXTRA}. In den Freibauten wächst der Multiplikator mit jedem Nachbau um 1, bis ×${SK_MULT_MAX}, und bleibt bis zum Ende. 3 Baugenehmigungen in den Freibauten: +${SK_FS_RE}.</p></div></div>
    <div class="feat" style="--fc:#ff7a59">${ICONS.warp}<div><h3>Stadtbus · Stadtlotterie</h3><p>3 oder mehr Stadtbusse starten die Stadtlotterie am Glücksrad, bis zum 300-fachen Einsatz.</p></div></div>
    <div class="feat" style="--fc:#ffc94a">${ICONS.crystal}<div><h3>Wappen und Bauamt</h3><p>Jeder Dreh füllt den Wappenmesser ein wenig, jedes Wappen-Symbol deutlich mehr. Im Bauamt tauschst du Wappen gegen Erlasse für einige Minuten.</p></div></div>
    <div class="feat" style="--fc:#ffc94a">${ICONS.scrap}<div><h3>Paule-Boost</h3><p>Jeder Dreh ohne Gewinn füllt Paules Glücksladung. Nach ${BOOST_AT} leeren Drehs gewinnt der nächste garantiert.</p></div></div>
    <div class="feat" style="--fc:#ffc94a">${ICONS.ladder}<div><h3>Risikoleiter</h3><p>Nach einem Gewinn ab einem Einsatz: Steig die Leiter hoch, von ×1 bis ×100. Kassieren geht jederzeit.</p></div></div>
    <div class="feat" style="--fc:#ff7a59">${ICONS.beacon}<div><h3>Signal-Risiko</h3><p>Nach einem Gewinn ab einem Einsatz kannst du ihn verdoppeln: Grün oder Rot raten, genau 50 : 50.</p></div></div>
    <div class="feat" style="--fc:#ffd34a">${ICONS.relic}<div><h3>Stadtschatz</h3><p>Jeder Dreh legt 1,5 % deines Einsatzes in den Topf, der bei 500 Talern startet. Die Chance pro Dreh ist Einsatz ÷ 40.000.</p></div></div>
    <div class="feat" style="--fc:#7ee0c8">${ICONS.up_engine}<div><h3>Aktionen, Viertel und Aufträge</h3><p>Starte Aktionen für deine Stadt, erschließe neue Viertel über deinen Rang und erfülle Aufträge für Taler und XP.</p></div></div>`;
  const tot = Object.values(SK_HW).reduce((a, b) => a + b, 0);
  $("lines").innerHTML = `<div><b>Haushöhen</b> (pro Walze und Dreh):</div><table class="pt"><tbody>${Object.keys(SK_HW).map(h => `<tr><td>${h} Felder</td><td class="pay">${(SK_HW[h] / tot * 100).toFixed(0)} %</td></tr>`).join("")}</tbody></table><p class="note">Gewinnwege = Höhe 1 × Höhe 2 × … × Höhe 6. Mindestens 64, höchstens 117.649.</p>`;
}

MISSION_TYPES.symwin.text = m => `Gewinne ${m.goal}-mal mit ${BY_ID[m.meta].name}`;
MISSION_TYPES.laser.text = () => "Gewinne mit Hilfe eines Krans";
MISSION_TYPES.four.text = () => "Gewinne über alle 6 Häuser";
MISSION_TYPES.upgrade.text = m => `Kaufe ${m.goal} Ausbaustufe${m.goal > 1 ? "n" : ""} im Stadtbild`;
MISSION_TYPES.haul.text = m => `Verdiene insgesamt ${m.goal} Taler`;
Object.assign(SYM_HELP, {
  beacon: `Baugenehmigung. 4 oder mehr irgendwo bringen ${SK_FS} Freibauten.`,
  warp: "Stadtbus. 3 oder mehr starten die Stadtlotterie.",
  wild: "Kran. Ersetzt jedes Symbol außer Baugenehmigung und Stadtbus. Nur auf den Häusern 2 bis 5.",
});
HELP_RULES.unshift(
  [".sk-c[data-sym]", el => { const id = el.dataset.sym, x = skSym(id); if (!x) return null;
    if (SK_PAY[id]) return [x.name, `Pro Weg beim aktuellen Einsatz: 3 Häuser <b>${(SK_PAY[id][0] * SK_SCALE * bet()).toFixed(2).replace(".", ",")}</b>, 6 Häuser <b>${(SK_PAY[id][3] * SK_SCALE * bet()).toFixed(2).replace(".", ",")}</b> Taler.`];
    return [x.name, SYM_HELP[id] || ""]; }],
  [".sk-roof, .sk-h", () => ["Haushöhe", "Jedes Haus ist pro Dreh 2 bis 7 Felder hoch. Je höher, desto mehr Gewinnwege."]],
  ["#skWays, .sk-ways", () => ["Gewinnwege", `Produkt der sechs Haushöhen. Gerade ${skFmt(skWaysOf(skGrid))}.`]],
  ["#skMultBox", () => ["Multiplikator", `In den Freibauten +1 pro Nachbau, bis ×${SK_MULT_MAX}. Gerade ×${skM}.`]],
  [".bay, #frame", () => ["Skyline-Walzen", "Sechs Hochhäuser als Walzen. Gleiche Symbole von links auf mindestens 3 Häusern gewinnen."]],
  ["#fsbar", () => ["Freibauten", `Kostenlose Drehs mit wachsendem Multiplikator. Noch ${fsLeft}.`]],
);
'''
