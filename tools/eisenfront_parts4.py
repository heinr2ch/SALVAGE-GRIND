# Eisenfront Teil 4: eigenes Grundspiel "Rex sammelt" (Sammler-Slot, 5×3, 243 Wege)

COL_HTML = [
    ('<div class="bay net" id="bay">\n          <div class="netgrid" id="netGrid" aria-label="Ersatzteillager mit 6 mal 5 Feldern"></div>\n          <div class="casc" id="casc" hidden>Nachschub <b id="cascN">×1</b></div>',
     '<div class="bay net col" id="bay">\n          <div class="netgrid" id="netGrid" aria-label="Werkbank mit 5 Walzen und 3 Reihen"></div>\n          <div class="casc" id="casc" hidden>Rex sammelt <b id="cascN">0</b></div>'),
    ('<span><b id="fsLeft">0</b> übrig · Nachschub <em class="fsmult" id="fsMultBox">×<b id="fsMult">2</b></em><b id="fsStick" hidden>0</b> · bisher <b id="fsWin">0</b></span>',
     '<span><b id="fsLeft">0</b> übrig · Rex <b id="fsStick">0</b>/4 · Sammler <em class="fsmult" id="fsMultBox">×<b id="fsMult">1</b></em> · bisher <b id="fsWin">0</b></span>'),
    ('<th>Satz</th><th>5–6</th><th>7–8</th><th>9–10</th><th>11–12</th><th>13+</th>', '<th>Teil</th><th>3 Walzen</th><th>4 Walzen</th><th>5 Walzen</th>'),
    ('Gewinn = Wert × Einsatz. Ein Satz sind mindestens 5 gleiche Teile, die sich waagerecht oder senkrecht berühren. Schraubenschlüssel zählen für jeden Satz.',
     'Gewinn = Wert × Einsatz × Wege. Gleiche Teile zählen, wenn sie auf nebeneinanderliegenden Walzen ab der linken Walze liegen, egal in welcher Reihe. Liegen auf einer Walze zwei davon, verdoppeln sich die Wege. Schraubenschlüssel (nur Walze 2 bis 4) ersetzen jedes Teil.'),
    ('aria-controls="panel-lines">Sätze</button>', 'aria-controls="panel-lines">Wege</button>'),
    ('Verbaute Sätze verschwinden, alles darüber rutscht nach unten und Nachschub fällt nach. Jeder weitere Schub erhöht den Nachschub-Multiplikator: ×1, ×2, ×3, dann ×5.',
     '243 Wege: Ein Teil muss nur auf Walze 1, 2 und 3 liegen, egal in welcher Reihe. Jede weitere Fundstelle auf denselben Walzen zählt als eigener Weg.'),
    ('<p class="hint">Leertaste fordert Nachschub an. Erneut drücken lädt alles sofort ab.</p>', '<p class="hint">Leertaste fordert Nachschub an. Erneut drücken stoppt sofort.</p>'),
]

COL_CSS = r'''
/* ---------- Eisenfront: Werkbank (5 × 3, Rex sammelt) ---------- */
.frame { width: min(100%, calc(min(46vh, 380px) * 5 / 3 + 38px)); }
.bay.net.col { aspect-ratio: 5 / 3; }
.bay.col .netgrid { background:
    linear-gradient(90deg, rgba(0,0,0,.55) 2px, transparent 2px) 0 0 / 20% 100%,
    linear-gradient(rgba(232,228,212,.05) 1px, transparent 1px) 0 0 / 100% calc(100% / 3),
    radial-gradient(ellipse at 50% -20%, rgba(255,190,110,.10), transparent 65%),
    linear-gradient(180deg, #1a1c1a, #121412 60%, #0c0d0c); }
.bay.col .tile { left: calc(var(--c) * 20%); top: calc(var(--r) * 100% / 3); width: 20%; height: calc(100% / 3) !important; transition: top .38s cubic-bezier(.3,1.25,.55,1), opacity .25s; }
.bay.col .tile.sym svg { width: 74%; height: 74%; }
.tile .cv { position: absolute; z-index: 3; left: 50%; top: 56%; transform: translate(-50%, -50%); padding: 1px 7px; border-radius: 4px; white-space: nowrap; pointer-events: none;
  font: 700 clamp(.75rem, 2.8vw, 1.15rem) var(--f-mono); color: #1a1408; background: linear-gradient(180deg, #f0d68a, #c9a24a); border: 1px solid #5a4410; box-shadow: 0 2px 0 rgba(0,0,0,.5); }
.tile .cv.big { background: linear-gradient(180deg, #ffe7a0, #e8a03a); color: #2a0e04; box-shadow: 0 0 10px rgba(255,190,80,.7), 0 2px 0 rgba(0,0,0,.5); }
.tile .cv.rexsum { top: 18%; background: linear-gradient(180deg, #e86a4a, #a33a2a); color: #fff4dc; border-color: #3a0e08; font-size: clamp(.8rem, 3vw, 1.2rem); }
.tile.rexon { z-index: 4; animation: rexBark .5s ease-in-out 3; }
@keyframes rexBark { 50% { transform: scale(1.14) rotate(-4deg); filter: brightness(1.3) drop-shadow(0 0 12px #e8b04a); } }
.tile.jumpin svg { animation: rexJump .7s cubic-bezier(.3,1.5,.5,1); }
@keyframes rexJump { 0% { transform: translate(-160%, -140%) rotate(-40deg) scale(.6); opacity: 0; } 60% { opacity: 1; } }
.tile.dim { opacity: .38; filter: grayscale(.7); }
.colfly { position: absolute; z-index: 9; pointer-events: none; transform: translate(-50%, -50%); padding: 1px 6px; border-radius: 4px;
  font: 700 clamp(.62rem, 2.4vw, .95rem) var(--f-mono); color: #1a1408; background: linear-gradient(180deg, #f0d68a, #c9a24a); border: 1px solid #5a4410;
  transition: left .45s cubic-bezier(.5,0,.7,1), top .45s cubic-bezier(.5,0,.7,1), transform .45s, opacity .45s; }
.colfly.gone { transform: translate(-50%, -50%) scale(.4); opacity: .2; }
.waysdemo { display: grid; grid-template-columns: repeat(5, 1fr); gap: 3px; max-width: 200px; margin: 6px 0; }
.waysdemo i { aspect-ratio: 1; border-radius: 4px; background: rgba(232,228,212,.08); }
.waysdemo i.on { background: #e07a4a; box-shadow: 0 0 8px #e07a4a; }
.waysdemo i.w { background: #c9ccd1; }
@media (prefers-reduced-motion: reduce) { .tile.rexon, .tile.jumpin svg { animation: none; } .colfly { transition-duration: .01s; } }
'''

COL_JS = r'''
/* ===================== Eisenfront: Rex sammelt (Sammler-Slot) =====================
   5 Walzen × 3 Reihen, 243 Wege (gleiche Teile auf Walze 1, 2, 3 … in beliebiger Reihe).
   Schraubenkisten tragen Werte (× Einsatz). Landet Rex, holt er alle Kisten ein. Mehrere Rex holen jeder einzeln.
   Kisten ohne Rex: manchmal springt Rex selbst rein. Rex ohne Kisten: manchmal bringt die Brieftaube Kisten.
   Freispiele (3+ Depeschen): Rex kommt öfter, jeder sammelnde Rex füllt den Knochenzähler. Je 4 Rex: +10 Freispiele
   und der Sammler-Multiplikator steigt ×1 → ×2 → ×3 → ×10.
   Balance per Simulation (600.000 Runden, tools/sim/rexsammelt.js): Treffer ~47 %, Rex sammelt ~14 %,
   Freispiele ~1/205 im Mittel 68×, Gesamt rund 114 % (vergleichbar mit den anderen Welten). */
const COL_C = 5, COL_R = 3;
const COL_W = { scrap: 22, cell: 20, chip: 16, core: 12, crystal: 7, relic: 4, wild: 1.5, cash: 14, rex: .8, beacon: 2.4, capsule: 1.3, warp: 1.3 };
const COL_PAY = { scrap: [.1, .25, .6], cell: [.15, .3, .75], chip: [.2, .4, 1], core: [.25, .6, 1.5], crystal: [.4, 1, 2.5], relic: [.6, 2, 6] };
const COL_VALS = [[.2, 30], [.5, 28], [1, 18], [2, 12], [3, 7], [5, 3.5], [10, 1.5], [25, .5], [50, .15]];
const COL_JUMP = .05, COL_FS_JUMP = .2, COL_DROP = .25, COL_FS_REX = 1.6, COL_FS_CASH = 1.1;
const COL_LEV = [1, 2, 3, 10], COL_FS_AWARD = { 3: 10, 4: 15, 5: 20 };
const COL_FEAT = { capsule: { bonus: "pick", title: "Kistenbergung", color: "#e8b04a" }, warp: { bonus: "wheel", title: "Geländefahrt", color: "#e07a4a" } };
const REX_SYM = { id: "rex", name: "Rex", w: 0, pay: null, special: "#e8b04a" };
const CASH_SYM = { id: "cash", name: "Schraubenkiste", w: 0, pay: null, special: "#c9a24a" };
BY_ID.rex = REX_SYM; BY_ID.cash = CASH_SYM;
ICONS.cash = `<svg viewBox="0 0 40 40"><rect x="1.5" y="1.5" width="37" height="37" rx="7" fill="#24200f" stroke="#8a6a2a" stroke-width="1.6"/><rect x="7" y="8" width="26" height="19" rx="1.5" fill="#6a4a22" stroke="#2a1a08" stroke-width="1.3"/><path d="M7 14 h26 M7 20.5 h26" stroke="#3a2610" stroke-width="1.1"/><path d="M7 8 L33 27 M33 8 L7 27" stroke="#8a6232" stroke-width="1.6" opacity=".8"/><rect x="5.5" y="6.5" width="5" height="5" fill="#9aa0a6" stroke="#3a3d42" stroke-width=".8"/><rect x="29.5" y="6.5" width="5" height="5" fill="#9aa0a6" stroke="#3a3d42" stroke-width=".8"/><circle cx="20" cy="17" r="3.4" fill="#c9ccd1" stroke="#3a3d42" stroke-width="1"/><path d="M18.3 17 h3.4 M20 15.3 v3.4" stroke="#3a3d42" stroke-width=".9"/></svg>`;
ICONS.rex = `<svg viewBox="0 0 40 40"><defs><radialGradient id="rexG" cx="50%" cy="40%" r="60%"><stop offset="0" stop-color="#4a3a1a"/><stop offset="1" stop-color="#1a140a"/></radialGradient></defs><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="url(#rexG)" stroke="#e8b04a" stroke-width="2.2"/>
  <path d="M9.5 9 q-5 2 -4 12 q5 -1 7 -6z M30.5 9 q5 2 4 12 q-5 -1 -7 -6z" fill="#6a4422" stroke="#2a1a08" stroke-width="1"/>
  <circle cx="20" cy="17" r="10" fill="#b07a42" stroke="#3a2410" stroke-width="1.3"/>
  <path d="M10.5 12.5 q9.5 -9 19 0 l-1.2 2 h-16.6z" fill="#4f5a2c" stroke="#1e240c" stroke-width="1"/><path d="M11.6 14.5 h16.8" stroke="#1e240c" stroke-width="1.4"/>
  <ellipse cx="20" cy="22.5" rx="6" ry="4.3" fill="#ead6ab" stroke="#5a3a1a" stroke-width=".9"/><ellipse cx="20" cy="20.3" rx="2.5" ry="1.8" fill="#1a1208"/>
  <ellipse cx="15.6" cy="17" rx="1.7" ry="2.1" fill="#1a1208"/><ellipse cx="24.4" cy="17" rx="1.7" ry="2.1" fill="#1a1208"/><circle cx="16.1" cy="16.3" r=".6" fill="#fff"/><circle cx="24.9" cy="16.3" r=".6" fill="#fff"/>
  <path d="M17.6 24.3 q2.4 3 4.8 0" fill="#e86a7a" stroke="#5a1a10" stroke-width=".6"/><path d="M12 28 q8 3.5 16 0" stroke="#a33a2a" stroke-width="2.2" fill="none" stroke-linecap="round"/><circle cx="20" cy="29.6" r="1.6" fill="#e8b04a"/>
  ${band("SAMMLER", "#e8b04a", "#1a140a")}</svg>`;

let colRun = null, colLev = 0, colMeter = 0, netCascading = false;
const colWait = ms => wait(colRun && colRun.fast ? Math.min(ms, 90) : ms * T());
function colVal() { let t = 0; for (const [, w] of COL_VALS) t += w; let r = Math.random() * t; for (const [v, w] of COL_VALS) if ((r -= w) < 0) return v; return 1; }
function colPick(c, free) {
  const w = { ...COL_W };
  if (c === 0 || c === 4) w.wild = 0;
  if (typeof boostOn === "function" && boostOn("signal")) w.beacon *= 2.5;
  if (free) { w.rex *= COL_FS_REX; w.cash *= COL_FS_CASH; w.beacon *= .8; w.capsule = 0; w.warp = 0; }
  let tot = 0; for (const k in w) tot += w[k];
  let r = Math.random() * tot, id = "scrap";
  for (const k in w) { if ((r -= w[k]) < 0) { id = k; break; } }
  if (id === "cash") return { s: CASH_SYM, v: colVal() };
  return { s: id === "wild" ? WILD : BY_ID[id] };
}
const colBoard = free => Array.from({ length: COL_C }, (_, c) => Array.from({ length: COL_R }, () => colPick(c, free)));
const colAmt = v => Math.max(1, Math.round(v * bet() * lineBoost()));
function colTile(cell, c, r, fromRow, delay) {
  const el = symEl(cell.s); el.classList.add("tile");
  if (cell.s.id === "cash") { const b = document.createElement("b"); b.className = "cv" + (cell.v >= 10 ? " big" : ""); b.textContent = colAmt(cell.v); el.appendChild(b); el.dataset.v = cell.v; }
  el.style.setProperty("--c", c); el.style.setProperty("--r", fromRow ?? r);
  if (delay) el.style.transitionDelay = delay + "ms";
  $("netGrid").appendChild(el);
  return el;
}
function colFill(board, animate) {
  const g = $("netGrid"); g.replaceChildren();
  const tf = T(), els = [];
  board.forEach((col, c) => col.forEach((cell, r) => els.push([colTile(cell, c, r, animate ? r - COL_R - 1 : undefined, animate ? Math.round((c * 150 + (COL_R - r) * 30) * tf) : 0), r])));
  if (animate) { void g.offsetWidth; els.forEach(([el, r]) => el.style.setProperty("--r", r)); }
}
const colEl = (c, r) => [...$("netGrid").children].find(el => +el.style.getPropertyValue("--c") === c && +el.style.getPropertyValue("--r") === r);
function colWays(board) {
  const res = [];
  for (const id in COL_PAY) {
    let ways = 1, k = 0; const cells = [];
    for (let c = 0; c < COL_C; c++) {
      const hit = board[c].map((x, r) => [x, r]).filter(([x]) => x.s.id === id || x.s.wild);
      if (!hit.length) break;
      ways *= hit.length; k++; hit.forEach(([, r]) => cells.push([c, r]));
    }
    if (k >= 3 && board.slice(0, k).some(col => col.some(x => x.s.id === id))) res.push({ sym: BY_ID[id], k, ways, factor: COL_PAY[id][k - 3] * ways, cells });
  }
  return res;
}
function evaluate(board) {
  const b = board[0] && board[0][0] && board[0][0].s ? board : board.map(col => col.map(s => ({ s })));
  const wins = colWays(b).map(x => ({ sym: x.sym, count: x.k, factor: x.factor, cells: x.cells }));
  const scatters = []; b.forEach((col, c) => col.forEach((x, r) => { if (x.s.id === "beacon") scatters.push([c, r]); }));
  return { wins, scatters, scatterReels: scatters.length, features: [] };
}
function colForce(board) {
  // Rex-Boost: Rex und zwei, drei kleine Kisten sicher aufs Feld
  const spots = []; for (let c = 0; c < COL_C; c++) for (let r = 0; r < COL_R; r++) spots.push([c, r]);
  const take = () => spots.splice((Math.random() * spots.length) | 0, 1)[0];
  const [rc, rr] = take(); board[rc][rr] = { s: REX_SYM };
  const n = 2 + ((Math.random() * 2) | 0);
  for (let i = 0; i < n; i++) { const [c, r] = take(); board[c][r] = { s: CASH_SYM, v: [.5, 1, 1, 2, 3][(Math.random() * 5) | 0] }; }
}
function colFloat(c, r, text, sub, color) {
  const bay = $("bay"), w = bay.clientWidth / COL_C, h = bay.clientHeight / COL_R;
  const f = document.createElement("div"); f.className = "netfloat"; f.style.setProperty("--fc", color);
  f.style.left = ((c + .5) * w) + "px"; f.style.top = ((r + .5) * h) + "px";
  f.innerHTML = `${text}${sub ? `<small>${sub}</small>` : ""}`;
  bay.appendChild(f); setTimeout(() => f.remove(), 1150);
}
function colCasc(n, show) { const b = $("casc"); b.hidden = !show; $("cascN").textContent = n; if (show) { b.classList.remove("pop"); void b.offsetWidth; b.classList.add("pop"); } }
function colSet(board, c, r, cell, cls) {
  board[c][r] = cell;
  const old = colEl(c, r); if (old) old.remove();
  const el = colTile(cell, c, r); if (cls) el.classList.add(cls);
  return el;
}
async function colJump(board) {
  // Rex springt selbst aufs Feld, auf einen Platz ohne Kiste
  const free = []; board.forEach((col, c) => col.forEach((x, r) => { if (x.s.id !== "cash" && !x.s.special) free.push([c, r]); }));
  if (!free.length) return false;
  const [c, r] = free[(Math.random() * free.length) | 0];
  $("msg").className = "msg gold"; $("msg").textContent = "Wuff! Rex springt selbst auf die Werkbank …";
  sfx.squeak(1.2);
  colSet(board, c, r, { s: REX_SYM }, "jumpin");
  if (typeof bip === "function") { bipState.last = 0; bip("star", 2); }
  await colWait(750);
  return true;
}
async function colPigeon(board) {
  // Brieftaube bringt 1 bis 3 Schraubenkisten, wenn Rex ohne Beute dasteht
  const bay = $("bay"), W = bay.clientWidth, H = bay.clientHeight;
  const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  svg.setAttribute("class", "netgull"); svg.setAttribute("viewBox", `0 0 ${W} ${H}`);
  svg.innerHTML = `<g id="gullG">${DRONE}</g>`; bay.appendChild(svg);
  const g = svg.querySelector("#gullG"), dur = 1300 * T(), t0 = performance.now();
  $("msg").className = "msg gold"; $("msg").textContent = "Brieftaube! Sie bringt Schraubenkisten für Rex …";
  radio("Funk: Eine Brieftaube landet an der Werkbank.", true);
  sfx.droneIn();
  const cand = []; board.forEach((col, c) => col.forEach((x, r) => { if (x.s.pay) cand.push([c, r]); }));
  const n = Math.min(cand.length, 1 + ((Math.random() * 3) | 0)), drops = [];
  for (let i = 0; i < n; i++) drops.push(cand.splice((Math.random() * cand.length) | 0, 1)[0]);
  await new Promise(res => {
    const fr = now => {
      const k = Math.min(1, (now - t0) / dur);
      g.setAttribute("transform", `translate(${W + 40 - (W + 80) * k} ${H * .14 + Math.sin(k * 9) * 6}) scale(${Math.max(1, W / 380)}) scale(-1 1)`);
      if (k < 1) requestAnimationFrame(fr); else res();
    };
    requestAnimationFrame(fr);
    drops.forEach(([c, r], i) => setTimeout(() => { colSet(board, c, r, { s: CASH_SYM, v: colVal() }, "grow"); sfx.crystal(); }, dur * (.25 + i * .22)));
  });
  svg.remove();
  track("laser"); bump("lasers");
  return n;
}
async function colCollect(board, rexes, mult) {
  // jeder Rex holt nacheinander alle Kisten ein
  const bay = $("bay"), w = bay.clientWidth / COL_C, h = bay.clientHeight / COL_R;
  const crates = []; board.forEach((col, c) => col.forEach((x, r) => { if (x.s.id === "cash") crates.push([c, r, x.v]); }));
  const sumV = crates.reduce((a, x) => a + x[2], 0);
  let total = 0;
  for (const [rc, rr] of rexes) {
    const rex = colEl(rc, rr); if (rex) rex.classList.add("rexon");
    sfx.squeak(1);
    let got = 0;
    for (const [c, r, v] of crates) {
      const ce = colEl(c, r); if (ce) ce.classList.add("hit");
      const f = document.createElement("div"); f.className = "colfly"; f.textContent = colAmt(v);
      f.style.left = ((c + .5) * w) + "px"; f.style.top = ((r + .78) * h) + "px"; bay.appendChild(f);
      void f.offsetWidth; f.style.left = ((rc + .5) * w) + "px"; f.style.top = ((rr + .5) * h) + "px"; f.classList.add("gone");
      setTimeout(() => f.remove(), 480);
      await colWait(colRun && colRun.fast ? 40 : 170);
      got += colAmt(v); sfx.coin(1);
      if (rex) { let sb = rex.querySelector(".cv"); if (!sb) { sb = document.createElement("b"); sb.className = "cv rexsum"; rex.appendChild(sb); } sb.textContent = got * mult; }
      colCasc(total + got * mult, true);
    }
    const amt = got * mult; total += amt;
    colFloat(rc, rr, `+${amt}`, `Rex holt ${crates.length} Kiste${crates.length === 1 ? "" : "n"}${mult > 1 ? " · ×" + mult : ""}`, "#e8b04a");
    sfx.streakUp(Math.min(4, 1 + Math.floor(sumV / 5)));
    await colWait(650);
    if (rex) rex.classList.remove("rexon");
  }
  return total;
}
function netDust(pts) {
  state.dustMeter = (state.dustMeter || 0) + pts;
  let whole = 0;
  while (state.dustMeter >= 100) { state.dustMeter -= 100; whole++; }
  if (whole) addDust(whole, null); else renderDust(false);
}
function gainDustFromSpin() {}
function renderSticky() {}
function colFsUi() { fsMult = COL_LEV[colLev]; fsSticky = Array(colLev >= 3 ? 4 : colMeter).fill(0); render(); }

function spin(auto) {
  if (spinning || busy || !ready || !$("scratch").hidden || !$("bonus").hidden || !$("naming").hidden || !$("worlds").hidden) return;
  const free = inFs();
  if (free && auto !== true) return;
  if (!free && state.credits < bet()) return;
  spinning = true; fsActive = free; slammed = false;
  if (free) fsLeft--; else {
    state.credits -= bet(); state.spins++; countCredits(state.credits, 250);
    sess.spins++; sess.bet += bet(); clearGamble();
    state.pot += bet() * JP_FEED; addXP(bet()); track("spins");
    bipState.lastSession++;
    if (bipState.lastSession % 200 === 0) setTimeout(() => bip("session", 2), 400);
  }
  $("bay").classList.remove("showing"); colCasc(0, false);
  $("msg").className = free ? "msg fs" : "msg";
  $("msg").textContent = free ? `Freispiel ${fsTotal - fsLeft} von ${fsTotal} …` : autoLeft > 0 ? `Auto-Schub · noch ${autoLeft} …` : "Nachschub rollt an …";
  $("lastWin").textContent = "0"; $("lastWin").classList.remove("pos");
  render();
  sfx.start();
  const board = colBoard(free);
  boostSpinActive = false;
  if (!free && state.boostReady) { colForce(board); boostSpinActive = true; state.boostReady = 0; state.luck = 0; sfx.boostSpin(); }
  const tf = T();
  [...$("netGrid").children].forEach(el => { el.style.transitionDelay = Math.round(+el.style.getPropertyValue("--c") * 60 * tf) + "ms"; el.classList.add("sink"); el.style.setProperty("--r", COL_R + 1); });
  const run = colRun = { board, free, fast: false, timers: [], done: false };
  const dropAt = reduced ? 0 : 280 * tf, landAt = reduced ? 30 : dropAt + (COL_C * 150 + COL_R * 30 + 400) * tf;
  run.timers.push(setTimeout(() => { if (!run.done) colFill(board, !reduced); }, dropAt));
  for (let c = 0; c < COL_C; c++) run.timers.push(setTimeout(() => { if (!run.done && !slammed) sfx.stop(); }, dropAt + (c * 150 + 360) * tf));
  run.timers.push(setTimeout(() => colLanded(run), landAt));
}
function colLanded(run) {
  if (run.done) return;
  run.done = true; run.timers.forEach(clearTimeout);
  [...$("netGrid").children].forEach(el => { el.style.transitionDelay = "0ms"; });
  finish(run.board, run.free);
}
function quickStop() {
  if (!spinning || slammed || !colRun || colRun.done) return;
  slammed = true; sfx.slam();
  colFill(colRun.board, false);
  colLanded(colRun);
}
function press() {
  if (!$("bonus").hidden || !$("scratch").hidden) return;
  if (skipCelebration) { skipCelebration(); return; }
  if (spinning) { quickStop(); return; }
  if (netCascading && colRun) { colRun.fast = true; return; }
  spin();
}

async function finish(board, free) {
  faces = board;
  spinning = false; busy = true; netCascading = true; render();
  const mult = free ? COL_LEV[colLev] : 1;
  const find = id => { const out = []; board.forEach((col, c) => col.forEach((x, r) => { if (x.s.id === id) out.push([c, r]); })); return out; };
  let total = 0, helper = false, dustPts = 2 + find("crystal").length * 3, collected = 0, rexCount = 0;

  // 1. Wege
  const ways = colWays(board);
  if (ways.length) {
    $("bay").classList.add("showing");
    for (const x of ways) {
      const amt = Math.round(x.factor * bet() * lineBoost());
      total += amt;
      track("symwin", 1, x.sym.id); if (x.k >= 5) track("four");
      x.cells.forEach(([c, r]) => { const el = colEl(c, r); if (el) { el.classList.add("hit"); el.style.setProperty("--hc", x.sym.color || "#ffffff"); } });
      const mid = x.cells.find(([c]) => c === 1) || x.cells[0];
      colFloat(mid[0], mid[1], `+${amt}`, `${x.k} Walzen ${x.sym.name}${x.ways > 1 ? ` · ${x.ways} Wege` : ""}`, x.sym.color);
    }
    sfx.small();
    $("lastWin").textContent = total; $("lastWin").classList.add("pos");
    $("msg").className = free ? "msg fs" : "msg win";
    $("msg").textContent = ways.map(x => `${x.k}× ${x.sym.name}${x.ways > 1 ? ` (${x.ways} Wege)` : ""}`).join(", ") + ` · +${total}`;
    await colWait(900);
    [...$("netGrid").children].forEach(el => el.classList.remove("hit"));
    $("bay").classList.remove("showing");
  }

  // 2. Rex sammelt
  let rex = find("rex"), crates = find("cash");
  const boostDrop = boostOn("drones") ? 2 : 1;
  if (crates.length && !rex.length && Math.random() < (free ? COL_FS_JUMP : COL_JUMP) * boostDrop) { helper = true; await colJump(board); rex = find("rex"); }
  if (rex.length && !crates.length && Math.random() < COL_DROP * boostDrop) { helper = true; await colPigeon(board); await colWait(350); crates = find("cash"); }
  if (rex.length && crates.length) {
    [...$("netGrid").children].forEach(el => { const id = el.dataset.sym; if (id !== "rex" && id !== "cash") el.classList.add("dim"); });
    $("msg").className = "msg gold"; $("msg").textContent = rex.length > 1 ? `${rex.length}× Rex! Jeder holt alle Kisten …` : "Rex holt die Kisten …";
    collected = await colCollect(board, rex, mult);
    total += collected; rexCount = rex.length;
    $("lastWin").textContent = total; $("lastWin").classList.add("pos");
    [...$("netGrid").children].forEach(el => el.classList.remove("dim", "hit"));
    track("symwin", rex.length, "rex");
  } else if (rex.length) {
    $("msg").className = "msg"; $("msg").textContent = "Rex schnüffelt, aber keine Kiste in Sicht.";
  }
  netCascading = false;
  netDust(dustPts);

  // 3. Freispiele: Knochenzähler
  let fsGain = 0;
  if (free && rexCount) {
    colMeter += rexCount;
    while (colMeter >= 4 && colLev < 3) { colMeter -= 4; colLev++; fsGain += 10; }
    if (colLev >= 3) colMeter = Math.min(colMeter, 4);
    colFsUi();
    if (fsGain) {
      fsLeft += fsGain; fsTotal += fsGain; multUp(); render();
      await simpleBanner({ tier: "Rex bekommt Verstärkung", color: "#e8b04a", sub: `Sammler jetzt ×${COL_LEV[colLev]}` }, `+${fsGain} Freispiele`, sfx.fs, ["#e8b04a", "#e07a4a", "#f4f0dc"], 2300);
    }
  }

  const scatters = find("beacon");
  const award = scatters.length >= 3 ? COL_FS_AWARD[Math.min(scatters.length, 5)] : 0;
  const features = ["capsule", "warp"].map(id => ({ id, ...COL_FEAT[id], cells: find(id) })).filter(f => f.cells.length >= 3);
  const mark = (list, col) => list.forEach(([c, r]) => { const el = colEl(c, r); if (el) { el.classList.add("hit"); el.style.setProperty("--hc", col); } });
  if (award) { mark(scatters, "#d9c75a"); sfx.scatter(scatters.length); }
  features.forEach(f => { mark(f.cells, f.color); sfx.feature(f.id === "capsule" ? 0 : 1, 3); });
  if (award || features.length) $("bay").classList.add("showing");

  const prevStreak = streak;
  if (!free) { if (total > 0) streak++; else streak = 0; }
  const sMult = free ? 1 : streakMult();
  const win = Math.round(total * sMult);
  if (!free) {
    if (streak >= 2 && streak > prevStreak) { sfx.streakUp(streak); renderStreak(true); }
    else if (prevStreak >= 2 && streak === 0) { sfx.streakBreak(); renderStreak(false); radio("Funk: Strähne gerissen. Neuer Anlauf.", false, 4000); }
    else renderStreak(false);
  }
  if (win >= bet() * 10) track("bigwin");
  if (!free && streak >= 3) track("streak");
  if (win > 0) track("haul", win);
  state.credits += win;
  if (free) fsWin += win;
  state.best = Math.max(state.best, win);
  state.peak = Math.max(state.peak, state.credits);

  const msg = $("msg"), parts = [];
  if (win > 0) {
    const what = [ways.length ? `${ways.length} Weg-Gewinn${ways.length > 1 ? "e" : ""}` : "", collected ? `Rex sammelt${rexCount > 1 ? ` ×${rexCount}` : ""}` : ""].filter(Boolean).join(", ");
    parts.push(`${boostSpinActive ? "Rex-Boost! " : ""}${what}: +${win} Schrauben${sMult > 1 ? ` · Strähne ×${String(sMult).replace(".", ",")}` : ""}.`);
    const top = ways.slice().sort((a, b) => b.factor - a.factor)[0];
    addLog(collected ? "rex" : top.sym.id, collected ? `Rex sammelt${rexCount > 1 ? ` ×${rexCount}` : ""}${mult > 1 ? ` · ×${mult}` : ""}` : `${top.k}× ${top.sym.name}`, "+" + win, collected ? "#e8b04a" : top.sym.color);
  }
  if (fsGain) parts.push(`Rex-Zähler voll: +${fsGain} Freispiele, Sammler ×${COL_LEV[colLev]}!`);
  colCasc(0, false);
  bipAfterSpin({ win, factor: win / bet(), lasered: helper, award, features: features.length, prevStreak, streak, free });
  if (!free && win >= bet() * 15) setTimeout(() => addDust(1, "große Bergung"), 1200);
  if (win > 0) { bump("wins"); sess.won += win; sess.best = Math.max(sess.best, win); if (!free) maxStat("maxFactor", win / bet()); }
  if (award && !free) bump("fs");
  if (features.some(f => f.id === "capsule")) bump("pick");
  maxStat("maxStreak", streak);
  if (award && !free) track("fs");
  if (features.length) track("bonus", features.length);
  if (award) {
    parts.push(free ? `Noch eine Depesche: +${award} Freispiele!` : `${scatters.length} Depeschen erhalten: ${award} Freispiele!`);
    addLog("beacon", free ? "Freispiele verlängert" : "Freispiele ausgelöst", `${award} FS`, "#d9c75a");
  }
  features.forEach(f => parts.push(`Bonus: ${f.title}!`));
  if (parts.length) { msg.className = features.length ? "msg gold" : award ? "msg fs" : "msg win"; msg.textContent = parts.join(" "); }
  if (features.length && autoLeft > 0) { autoLeft = 0; clearAutoMarks(); }

  render();
  if (win > 0) { await wait(250 * T()); await celebrateWin(win, state.credits); }
  for (const f of features) {
    await celebrateFeature(f);
    const amount = Math.round((await runBonus(f)) * bonusBoost());
    state.credits += amount;
    state.best = Math.max(state.best, amount);
    state.peak = Math.max(state.peak, state.credits);
    state.bonusCount = (state.bonusCount || 0) + 1;
    track("haul", amount); sess.won += amount; sess.best = Math.max(sess.best, amount);
    addDust(1, f.title);
    addLog(f.id, f.title, "+" + amount, f.color);
    render();
    if (amount > 0) await celebrateWin(amount, state.credits);
    msg.className = "msg gold"; msg.textContent = `${f.title} abgeschlossen: +${amount} Schrauben.`;
    bip(amount >= bet() * 10 ? "bonusGood" : "bonusMeh", 3);
  }
  if (award) {
    fsLeft += award; fsTotal += award;
    if (!free) { state.fsRounds++; fsWin = 0; colLev = 0; colMeter = 0; }
    colFsUi();
    await simpleBanner({ tier: free ? "Noch eine Depesche" : "Großeinsatz", color: "var(--lime)", sub: free ? "Rex-Zähler und Sammler bleiben" : "Rex kommt öfter · je 4 Rex: +10 Freispiele und mehr Sammler" },
      `+${award} Freispiele`, sfx.fs, ["#d9c75a", "#e8b04a", "#f4f0dc"], 2400);
  }

  if (inFs()) {
    if (!parts.length) { msg.className = "msg fs"; msg.textContent = `Kein Fund. Noch ${fsLeft} Freispiel${fsLeft === 1 ? "" : "e"}, Rex ${colLev >= 3 ? "4" : colMeter}/4, Sammler ×${COL_LEV[colLev]}.`; }
    busy = false; fsActive = true; render();
    await wait((parts.length ? 500 : 650) * T());
    spin(true);
    return;
  }

  if (free) {
    fsActive = false;
    msg.className = "msg win";
    msg.textContent = `Freispiele beendet: insgesamt +${fsWin} Schrauben, Sammler bis ×${COL_LEV[colLev]}.`;
    if (fsWin >= bet() * 50) setTimeout(() => addDust(2, "starke Freispiele"), 2500);
    addLog("beacon", "Freispiele gesamt", "+" + fsWin, "#d9c75a");
    colLev = 0; colMeter = 0; colFsUi();
    await celebrateFsEnd(fsWin, state.credits);
    bip("fsend", 2);
    fsTotal = 0;
  } else if (!parts.length && !rex.length) {
    if (state.credits < 5) { msg.className = "msg lose"; msg.textContent = "Schrauben erschöpft."; }
    else if (state.credits < bet()) { msg.className = "msg lose"; msg.textContent = "Zu wenig Schrauben für diesen Einsatz. Senke den Einsatz."; }
    else { msg.className = "msg"; msg.textContent = crates.length ? "Kisten da, aber kein Rex. Neuer Schub?" : "Nichts Brauchbares dabei. Neuer Schub?"; }
  }
  countCredits(state.credits, 0);
  fsActive = false;
  if (!free && Math.random() < bet() / JP_DIV * (boostOn("treasure") ? 5 : 1)) {
    const amount = Math.floor(state.pot);
    state.pot = JP_SEED; state.credits += amount;
    state.best = Math.max(state.best, amount); state.peak = Math.max(state.peak, state.credits);
    autoLeft = 0; clearAutoMarks();
    addLog("relic", "GOLDTRESOR", "+" + amount, "#ffc94a");
    radio(`Funk: GOLDTRESOR GEKNACKT! ${amount} Schrauben. Alle Fronten reden davon.`, true, 15000);
    renderMeta();
    bump("jackpots"); sess.won += amount; setTimeout(() => addDust(5, "Goldtresor"), 5000);
    await celebrateJackpot(amount, state.credits);
    bip("jackpot", 3);
    msg.className = "msg gold"; msg.textContent = `Goldtresor geknackt: +${amount} Schrauben!`;
  }
  await processProgress();
  if (state.credits < 5) { autoLeft = 0; clearAutoMarks(); await handleBankruptcy(); }
  if (!free && Math.random() < 1 / 150) findAlbumItem(curSector().id, "Schub");
  if (!free) {
    if (win > 0 || features.length || award) state.luck = 0; else state.luck = (state.luck || 0) + 1;
    if (boostSpinActive && win > 0) { setTimeout(() => { bipState.last = 0; bip("boostWin", 3); }, 300); boostSpinActive = false; }
    if (state.luck >= BOOST_AT && !state.boostReady) await activateBoost();
    else if (state.luck === Math.round(BOOST_AT / 2)) bip("charging", 2);
    renderLuck();
  }
  checkAch(); sessPoint();
  if (!free && win > 0 && autoLeft === 0 && !features.length && state.credits >= 5) offerGamble(win);
  busy = false;
  saveGame();
  if (autoLeft > 0) {
    if (state.credits >= bet()) {
      autoLeft--;
      render();
      if (autoLeft >= 0) { await wait(450 * T()); if (autoLeft >= 0 && !spinning && !busy) { if (autoLeft === 0) clearAutoMarks(); spin(); return; } }
    } else { autoLeft = 0; clearAutoMarks(); }
  }
  render();
}

function buildInfo() {
  $("payRows").innerHTML = SYMBOLS.filter(x => x.pay).reverse().map(x =>
    `<tr><td>${ICONS[x.id]}${x.name}</td>${COL_PAY[x.id].map(p => `<td class="pay">${fmtF(p)}</td>`).join("")}</tr>`).join("");
  $("panel-bonus").innerHTML = `
    <div class="feat" style="--fc:#e8b04a">${ICONS.rex}<div><h3>Rex sammelt</h3><p>Schraubenkisten tragen Beträge. Landet Rex irgendwo auf der Werkbank, holt er alle Kisten ein und du bekommst die Summe. Zwei Rex holen alles doppelt, drei dreifach.</p></div></div>
    <div class="feat" style="--fc:#c9a24a">${ICONS.cash}<div><h3>Schraubenkisten</h3><p>Werte von 0,2- bis 50-fachem Einsatz. Ohne Rex bleiben sie liegen. Aber manchmal springt Rex von selbst auf die Werkbank, wenn Kisten da sind.</p></div></div>
    <div class="feat" style="--fc:#b8c0c8">${ICONS.wild}<div><h3>Brieftaube</h3><p>Steht Rex ohne Kisten da, bringt manchmal eine Brieftaube 1 bis 3 Kisten vorbei. Der Schraubenschlüssel (Walze 2 bis 4) ersetzt jedes Teil.</p></div></div>
    <div class="feat" style="--fc:#d9c75a">${ICONS.beacon}<div><h3>Depesche · Großeinsatz</h3><p>3, 4 oder 5 Depeschen bringen 10, 15 oder 20 Freispiele. Rex kommt dort öfter. Jeder Rex, der Kisten holt, füllt den Rex-Zähler. Je 4 Rex gibt es +10 Freispiele, und der Sammler-Multiplikator steigt: ×1, ×2, ×3, dann ×10.</p></div></div>
    <div class="feat" style="--fc:#e8b04a">${ICONS.capsule}<div><h3>Nachschubkiste · Kistenbergung</h3><p>3 oder mehr Nachschubkisten irgendwo starten die Kistenbergung: Kisten öffnen, Schrauben sammeln, ein ×2 verdoppelt alles. Beim dritten Alarm ist Schluss.</p></div></div>
    <div class="feat" style="--fc:#e07a4a">${ICONS.warp}<div><h3>Kompass · Geländefahrt</h3><p>3 oder mehr Kompasse irgendwo starten die Geländefahrt am Kartenrad. „Weiter“ führt in höhere Ringe, bis zum 300-fachen Einsatz.</p></div></div>
    <div class="feat" style="--fc:#e8b04a">${ICONS.crystal}<div><h3>Orden und Feldküche</h3><p>Jeder Schub füllt den Ordensmesser ein wenig, jeder Orden auf der Werkbank deutlich mehr. Ist er voll, gibt es 1 Orden. In der Feldküche tauschst du ihn gegen Rationen für einige Minuten.</p></div></div>
    <div class="feat" style="--fc:#e8b04a">${ICONS.rex}<div><h3>Rex-Boost</h3><p>Jeder Schub ohne Fund füllt Rex' Glücksladung. Nach ${BOOST_AT} leeren Schüben ist sie voll, und beim nächsten Schub bringt Rex garantiert Kisten mit.</p></div></div>
    <div class="feat" style="--fc:#ffc94a">${ICONS.ladder}<div><h3>Risikoleiter</h3><p>Nach einem normalen Gewinn: Steig die Leiter hoch, von ×1 bis ×100. Das Licht springt zwischen Ziel und Absturz, du drückst Stopp. Die Chancen sind fair, kassieren geht jederzeit.</p></div></div>
    <div class="feat" style="--fc:#e07a4a">${ICONS.beacon}<div><h3>Signal-Risiko</h3><p>Nach einem normalen Gewinn kannst du ihn verdoppeln: Oliv oder Signalrot raten, genau 50 : 50, höchstens fünf Runden.</p></div></div>
    <div class="feat" style="--fc:#ff9a3c">${ICONS.core}<div><h3>Strähne</h3><p>Findest du mehrere Schübe hintereinander etwas, gibt es einen Bonus: 2 in Folge ×1,1, 3 in Folge ×1,25, ab 4 in Folge ×1,5.</p></div></div>
    <div class="feat" style="--fc:#ffc94a">${ICONS.relic}<div><h3>Goldtresor</h3><p>Jeder Schub legt 1,5 % deines Einsatzes in den Topf, der bei 500 Schrauben startet. Die Chance pro Schub ist Einsatz ÷ 40.000.</p></div></div>
    <div class="feat" style="--fc:#a7c060">${ICONS.up_engine}<div><h3>Expeditionen, Fronten und Aufträge</h3><p>Schick deinen Panzer auf Expedition, erkunde neue Fronten über deinen Rang und erfülle Aufträge für Schrauben und XP.</p></div></div>`;
  const demo = [1,0,0,0,0, 0,1,0,0,0, 0,2,1,0,0];
  $("lines").innerHTML = `<div><b>Beispiel:</b> Motorblock auf Walze 1, 2 und 3, auf Walze 2 zweimal (einmal als Schraubenschlüssel) = 2 Wege über 3 Walzen.</div><div class="waysdemo">${[0,1,2].map(r => [0,1,2,3,4].map(c => demo[r * 5 + c])).flat().map(v => `<i class="${v === 1 ? "on" : v === 2 ? "w" : ""}"></i>`).join("")}</div>`;
}

MISSION_TYPES.symwin.text = m => m.meta === "rex" ? `Lass Rex ${m.goal}-mal sammeln` : `Gewinne ${m.goal}-mal mit ${BY_ID[m.meta].name}`;
MISSION_TYPES.four.text = () => "Gewinne mit einem Teil über alle 5 Walzen";
Object.assign(SYM_HELP, {
  beacon: "Depesche. 3 oder mehr irgendwo bringen Freispiele (3 = 10, 4 = 15, 5 = 20). Dort kommt Rex öfter, und je 4 sammelnde Rex gibt es +10 Freispiele und einen höheren Sammler-Multiplikator (bis ×10).",
  capsule: "Nachschubkiste. 3 oder mehr irgendwo starten die Kistenbergung.",
  warp: "Kompass. 3 oder mehr irgendwo starten die Geländefahrt am Kartenrad.",
  wild: "Schraubenschlüssel. Nur auf Walze 2 bis 4, ersetzt jedes Teil.",
  rex: "Rex, der Sammler. Holt alle Schraubenkisten auf der Werkbank ein. Mehrere Rex holen jeder einzeln.",
});
HELP_RULES.unshift(
  [".tile[data-sym]", el => { const id = el.dataset.sym, x = id === "wild" ? WILD : BY_ID[id]; if (!x) return null;
    if (id === "cash") return ["Schraubenkiste", `Wert <b>${el.querySelector(".cv") ? el.querySelector(".cv").textContent : ""}</b> Schrauben. Zählt nur, wenn Rex auf der Werkbank landet, dann holt er alle Kisten ein.`];
    if (x.pay) { const p = COL_PAY[id]; return [x.name, `Pro Weg über 3 Walzen: <b>${Math.round(p[0] * bet())}</b>, 4 Walzen: <b>${Math.round(p[1] * bet())}</b>, 5 Walzen: <b>${Math.round(p[2] * bet())}</b> Schrauben beim aktuellen Einsatz.${id === "crystal" ? " Jeder Orden füllt außerdem den Ordensmesser." : ""}`]; }
    return [x.name, SYM_HELP[id]]; }],
  [".bay, #frame, #netGrid", () => ["Werkbank", "5 Walzen, 3 Reihen, 243 Wege. Gleiche Teile ab der linken Walze gewinnen, egal in welcher Reihe. Schraubenkisten holt Rex ein, sobald er landet."]],
  ["#casc", () => ["Rex sammelt", "So viel hat Rex in dieser Runde schon eingeholt."]],
  ["#fsbar", () => ["Großeinsatz", `Kostenlose Schübe. Rex-Zähler ${colLev >= 3 ? 4 : colMeter} von 4: Je 4 sammelnde Rex gibt es +10 Freispiele. Sammler-Multiplikator gerade ×${COL_LEV[colLev]} (Stufen ×1, ×2, ×3, ×10).`]],
);
'''

DARK_CSS = r'''
/* ---------- Eisenfront: düsterer Grundton (Ruß, Rauch, Glut) ---------- */
:root { --ink: #d6d2c2; --ink-soft: #8e8c7c; --line: rgba(214,210,194,.1); --glass: rgba(214,210,194,.025); --glass-2: rgba(214,210,194,.05);
  --cyan: #8a9a52; --lime: #b8a84a; --win: #9cc46a; --grad: linear-gradient(135deg, #a8b46a, #4a5426); }
body { background:
    radial-gradient(ellipse 90% 60% at 50% 115%, rgba(160,60,20,.22), transparent 65%),
    radial-gradient(ellipse 70% 50% at 15% -10%, rgba(80,80,74,.25), transparent 70%),
    radial-gradient(ellipse 120% 90% at 50% 50%, transparent 45%, rgba(0,0,0,.75) 100%),
    repeating-linear-gradient(90deg, transparent 0 119px, rgba(0,0,0,.5) 119px 121px, rgba(255,255,255,.02) 121px 122px),
    repeating-linear-gradient(0deg, transparent 0 79px, rgba(0,0,0,.4) 79px 81px),
    linear-gradient(180deg, #161816, #0a0b0a); background-color: #0a0b0a; }
.glass { border-color: #0c0d0c;
  background:
    radial-gradient(ellipse 40% 30% at 85% 100%, rgba(120,60,20,.12), transparent 70%),
    radial-gradient(ellipse 30% 25% at 10% 90%, rgba(90,50,20,.1), transparent 70%),
    linear-gradient(180deg, rgba(255,255,255,.03), rgba(0,0,0,.35)),
    repeating-linear-gradient(115deg, rgba(255,255,255,.01) 0 2px, rgba(0,0,0,.025) 2px 5px),
    linear-gradient(180deg, #252824, #1b1d1b);
  box-shadow: 0 18px 44px rgba(0,0,0,.75), inset 0 1px 0 rgba(255,255,255,.05), inset 0 0 0 1px rgba(0,0,0,.5), inset 0 0 50px rgba(0,0,0,.5); }
.glass::after { opacity: .7; }
.brand h1, .topbar .brand h1 { background: linear-gradient(180deg, #d6d2c2 0%, #8e9a5a 55%, #3a4220 100%); -webkit-background-clip: text; background-clip: text; filter: drop-shadow(0 2px 0 #000); }
.intro { background: radial-gradient(ellipse at 50% 110%, rgba(170,70,20,.3), transparent 60%), radial-gradient(ellipse at 50% 40%, rgba(120,110,90,.12), transparent 60%), linear-gradient(180deg, #121412, #050605); }
.intro-title span { background: linear-gradient(180deg, #d6d2c2, #8e9a5a 55%, #3a4220); -webkit-background-clip: text; background-clip: text; filter: drop-shadow(0 3px 0 #000) drop-shadow(0 0 22px rgba(200,90,30,.35)); }
.intro-btn { background: repeating-linear-gradient(-45deg, #b8862e 0 12px, #8a6420 12px 24px); color: #120e04; }
.radio { background: linear-gradient(180deg, #a8a080, #8e866a); border-color: #4a4430; color: #14120a; }
.radio span, .radio.hot span { color: #14120a; }
.frame { background: linear-gradient(#0d0e0d, #0d0e0d) padding-box, repeating-linear-gradient(-45deg, #b8862e 0 10px, #141510 10px 20px) border-box; box-shadow: 0 0 0 2px #000, 0 14px 34px rgba(0,0,0,.75), inset 0 0 50px rgba(0,0,0,.85); }
.frame.fs { background: linear-gradient(#0d0e0d, #0d0e0d) padding-box, repeating-linear-gradient(-45deg, #b8a84a 0 10px, #141510 10px 20px) border-box; box-shadow: 0 0 0 2px #000, 0 0 30px rgba(200,110,40,.45), inset 0 0 50px rgba(0,0,0,.85); }
.spin { background: radial-gradient(circle at 50% 30%, #4e5a2a 0%, #232a12 70%); }
.jackpot { background: linear-gradient(135deg, rgba(184,134,46,.14), rgba(30,24,10,.4)); border-color: #5a4a1e; }
.shipview { border-color: #141614; box-shadow: inset 0 0 0 2px #000, inset 0 0 60px rgba(0,0,0,.6); }
.shipview::after { content: ""; position: absolute; inset: 0; pointer-events: none; border-radius: inherit; background: radial-gradient(ellipse 110% 90% at 50% 45%, transparent 55%, rgba(0,0,0,.55) 100%); }
.toast, .ticket, .bip-bubble { filter: brightness(.86) saturate(.85); }
#stars { opacity: .65; }
'''
