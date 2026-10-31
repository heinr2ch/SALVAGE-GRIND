# Teil 5: Fangnetz-Kaskaden (neues Grundspiel), rustikale Geräusche, Wurfhaken, ruhigeres Meer
TG_VERSION_NET = "1.1.0"

FRAME_OLD = '''        <div class="lp" aria-hidden="true">
          <div><span data-l="1">2</span><span data-l="3">4</span></div>
          <div><span data-l="0">1</span></div>
          <div><span data-l="2">3</span><span data-l="4">5</span></div>
        </div>
        <div class="bay" id="bay">
          <div class="reel"><div class="strip"></div></div>
          <div class="reel"><div class="strip"></div></div>
          <div class="reel"><div class="strip"></div></div>
          <div class="reel"><div class="strip"></div></div>
          <div class="reel"><div class="strip"></div></div>
          <div class="sheen" aria-hidden="true"></div>'''
FRAME_NEW = '''        <div class="bay net" id="bay">
          <div class="netgrid" id="netGrid" aria-label="Fangnetz mit 6 mal 5 Feldern"></div>
          <div class="casc" id="casc" hidden>Nachfang <b id="cascN">×1</b></div>'''
FRAME_OLD2 = '''        <div class="lp" aria-hidden="true">
          <div><span data-l="1">2</span><span data-l="3">4</span></div>
          <div><span data-l="0">1</span></div>
          <div><span data-l="2">3</span><span data-l="4">5</span></div>
        </div>
      </div>'''
FRAME_NEW2 = '''      </div>'''

HTML_NET = [
    ('<table class="pt"><thead><tr><th>Fund</th><th>3×</th><th>4×</th><th>5×</th></tr></thead><tbody id="payRows"></tbody></table>',
     '<table class="pt"><thead><tr><th>Schwarm</th><th>5–6</th><th>7–8</th><th>9–10</th><th>11–12</th><th>13+</th></tr></thead><tbody id="payRows"></tbody></table>'),
    ('<p class="note">Werte pro Linie × Linieneinsatz (Einsatz ÷ 5). Gleiche Funde zählen ab dem linken Schacht in Folge.</p>',
     '<p class="note">Gewinn = Wert × Einsatz. Ein Schwarm sind mindestens 5 gleiche Funde, die sich waagerecht oder senkrecht berühren. Rettungsringe zählen für jeden Schwarm.</p>'),
    ('aria-controls="panel-lines">Linien</button>', 'aria-controls="panel-lines">Schwärme</button>'),
    ('<p class="note">Fünf feste Gewinnlinien. Die Nummern am Rand der Walzen leuchten bei einem Treffer in der Farbe der Linie.</p>',
     '<p class="note">Gefangene Schwärme landen im Netz, alles darüber rutscht nach unten und neues Treibgut fällt nach. Jede weitere Welle erhöht den Nachfang-Multiplikator: ×1, ×2, ×3, dann ×5.</p>'),
    ('<span><b id="fsLeft">0</b> übrig · <em class="fsmult" id="fsMultBox">×<b id="fsMult">2</b></em> · Kristalle <b id="fsStick">0</b>/3 · bisher <b id="fsWin">0</b></span>',
     '<span><b id="fsLeft">0</b> übrig · Nachfang <em class="fsmult" id="fsMultBox">×<b id="fsMult">2</b></em><b id="fsStick" hidden>0</b> · bisher <b id="fsWin">0</b></span>'),
]

NET_CSS = """
/* ---------- Treibgut: Fangnetz ---------- */
.frame { grid-template-columns: minmax(0, 1fr); width: min(100%, calc(min(62vh, 500px) * 1.2 + 38px)); margin: 0 auto; }
.bay.net { display: block; position: relative; aspect-ratio: 6 / 5; width: 100%; }
.netgrid { position: absolute; inset: 0; overflow: hidden; border-radius: 8px;
  background:
    linear-gradient(rgba(243,230,200,.09) 1.5px, transparent 1.5px) 0 0 / calc(100% / 6) calc(100% / 5),
    linear-gradient(90deg, rgba(243,230,200,.09) 1.5px, transparent 1.5px) 0 0 / calc(100% / 6) calc(100% / 5),
    radial-gradient(ellipse at 50% 120%, rgba(63,134,192,.35), transparent 70%),
    linear-gradient(180deg, #13303a, #0c1f26 60%, #081419); }
.netgrid::after { content: ""; position: absolute; inset: 0; pointer-events: none; background: repeating-linear-gradient(45deg, transparent 0 14px, rgba(255,255,255,.025) 14px 15px), repeating-linear-gradient(-45deg, transparent 0 14px, rgba(255,255,255,.025) 14px 15px); }
.tile { position: absolute; z-index: 1; left: calc(var(--c) * 100% / 6); top: calc(var(--r) * 100% / 5); width: calc(100% / 6); height: calc(100% / 5) !important;
  transition: top .42s cubic-bezier(.35,1.35,.55,1), opacity .3s; }
.tile.sym svg { width: 72%; height: 72%; }
.tile.sink { transition: top .3s ease-in, opacity .3s ease-in; opacity: 0; }
.tile.caught { animation: caught .36s ease-in forwards; z-index: 3; }
@keyframes caught { 35% { transform: scale(1.28); filter: brightness(1.7) drop-shadow(0 0 10px #fff); } 100% { transform: scale(.15) translateY(-30px) rotate(25deg); opacity: 0; } }
.tile.grow svg { animation: ringDrop .55s cubic-bezier(.3,1.6,.5,1); }
@keyframes ringDrop { from { transform: translateY(-120%) scale(.6) rotate(-90deg); opacity: 0; } }
.casc { position: absolute; z-index: 6; top: 8px; left: 50%; transform: translateX(-50%); padding: 4px 12px; border-radius: 99px; pointer-events: none;
  background: linear-gradient(180deg, #f1d08a, #c98e3a); color: #2a1808; border: 2px solid #7a4e1a; font: 700 .78rem var(--f-body); letter-spacing: .06em; box-shadow: 0 4px 0 rgba(0,0,0,.35); }
.casc b { font: 700 .95rem var(--f-mono); }
.casc.pop { animation: fsPop .6s cubic-bezier(.2,1.6,.4,1); }
.netfloat { position: absolute; z-index: 7; transform: translate(-50%, -50%); pointer-events: none; white-space: nowrap;
  font: 700 clamp(1rem, 3.6vw, 1.5rem) var(--f-mono); color: #fff1c8; text-shadow: 0 2px 0 #1a0f06, 0 0 14px var(--fc, #8fe07a); animation: netFloat 1.1s ease-out forwards; }
.netfloat small { display: block; text-align: center; font-size: .7em; color: var(--fc, #8fe07a); }
@keyframes netFloat { 0% { opacity: 0; transform: translate(-50%, -30%) scale(.6); } 20% { opacity: 1; transform: translate(-50%, -50%) scale(1.12); } 100% { opacity: 0; transform: translate(-50%, -140%) scale(1); } }
.netgull { position: absolute; inset: 0; z-index: 8; width: 100%; height: 100%; pointer-events: none; overflow: visible; }
.swarmdemo { display: grid; grid-template-columns: repeat(6, 1fr); gap: 3px; max-width: 220px; margin: 6px 0; }
.swarmdemo i { aspect-ratio: 1; border-radius: 4px; background: rgba(243,230,200,.08); }
.swarmdemo i.on { background: #7fc8ff; box-shadow: 0 0 8px #7fc8ff; }
.swarmdemo i.w { background: #ff5a4a; }
@media (prefers-reduced-motion: reduce) { .tile, .tile.sink { transition: none; } .tile.caught, .netfloat, .tile.grow svg { animation-duration: .01s; } }
"""

NET_JS = r'''
/* ===================== Treibgut: Fangnetz-Kaskaden statt Walzen =====================
   6×5-Feld. Schwärme ab 5 gleichen Funden, die sich waagerecht oder senkrecht berühren, landen im Netz.
   Danach rutscht alles nach unten und neues Treibgut fällt nach (Nachfang). Jede Welle erhöht den Multiplikator.
   Balance per Simulation (300.000 Runden): Etwa jede zweite Runde fängt etwas, Freispiele etwa alle 114 Würfe,
   im Mittel 32× Einsatz. Gesamt rund 119 % Auszahlung (ähnlich wie Sternenwrack). */
const NET_C = 6, NET_R = 5;
const NET_W = { scrap: 30, cell: 26, chip: 20, core: 14, crystal: 7, relic: 4, beacon: 1.25, capsule: .75, warp: .75 };
const NET_PAY = { scrap: [.3, .6, 1.2, 2.25, 6], cell: [.45, .9, 1.8, 3.75, 9], chip: [.6, 1.2, 2.4, 5.25, 12], core: [.9, 1.8, 3.75, 7.5, 18], crystal: [1.5, 3, 6, 12, 30], relic: [2.25, 4.5, 9, 22.5, 60] };
const netBucket = n => n >= 13 ? 4 : n >= 11 ? 3 : n >= 9 ? 2 : n >= 7 ? 1 : 0;
const CASCADE_MULT = [1, 2, 3, 5];
const GULL_P = .08;
const FS_NET_MAX = 10;
const NET_FEAT = { capsule: { bonus: "pick", title: "Kistenbergung", color: "#ffc94a" }, warp: { bonus: "wheel", title: "Strudelfahrt", color: "#e0704a" } };
let netRun = null, netCascading = false;
const fmtF = f => String(f).replace(".", ",");
function netPick() {
  const w = { ...NET_W };
  if (typeof boostOn === "function" && boostOn("signal")) w.beacon *= 2.5;
  let tot = 0; for (const k in w) tot += w[k];
  let r = Math.random() * tot;
  for (const k in w) { if ((r -= w[k]) < 0) return BY_ID[k]; }
  return BY_ID.scrap;
}
const netNewBoard = () => Array.from({ length: NET_C }, () => Array.from({ length: NET_R }, netPick));
function netTile(sym, c, r, fromRow, delay) {
  const el = symEl(sym); el.classList.add("tile");
  el.style.setProperty("--c", c); el.style.setProperty("--r", fromRow ?? r);
  if (delay) el.style.transitionDelay = delay + "ms";
  $("netGrid").appendChild(el);
  return el;
}
function netFill(board, animate) {
  const g = $("netGrid"); g.replaceChildren();
  const tf = T(), els = [];
  board.forEach((col, c) => col.forEach((s, r) => els.push([netTile(s, c, r, animate ? r - NET_R - 1 : undefined, animate ? Math.round((c * 70 + (NET_R - r) * 22) * tf) : 0), r])));
  if (animate) { void g.offsetWidth; els.forEach(([el, r]) => el.style.setProperty("--r", r)); }
}
const netEl = (c, r) => [...$("netGrid").children].find(el => !el.classList.contains("caught") && +el.style.getPropertyValue("--c") === c && +el.style.getPropertyValue("--r") === r);
function netClusters(board) {
  const res = [], seen = new Set();
  for (let c = 0; c < NET_C; c++) for (let r = 0; r < NET_R; r++) {
    const s = board[c][r]; if (!s.pay || seen.has(c * 10 + r)) continue;
    const stack = [[c, r]], cl = new Set([c * 10 + r]);
    while (stack.length) {
      const [x, y] = stack.pop();
      for (const [dx, dy] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
        const nx = x + dx, ny = y + dy;
        if (nx < 0 || ny < 0 || nx >= NET_C || ny >= NET_R) continue;
        const k = nx * 10 + ny; if (cl.has(k)) continue;
        const t = board[nx][ny]; if (t === s || t.wild) { cl.add(k); stack.push([nx, ny]); }
      }
    }
    for (const k of cl) if (board[(k / 10) | 0][k % 10] === s) seen.add(k);
    if (cl.size >= 5) res.push({ sym: s, cells: [...cl].map(k => [(k / 10) | 0, k % 10]) });
  }
  return res;
}
function evaluate(board) {
  // für Hilfe und Tests: Schwärme als "wins", Flaschenposten als "scatters"
  const wins = netClusters(board).map(x => ({ sym: x.sym, count: x.cells.length, factor: NET_PAY[x.sym.id][netBucket(x.cells.length)], cells: x.cells }));
  const scatters = []; board.forEach((col, c) => col.forEach((s, r) => { if (s.id === "beacon") scatters.push([c, r]); }));
  return { wins, scatters, scatterReels: scatters.length, features: [] };
}
function netForceWin(board) {
  // Koko-Boost: ein kleiner, zusammenhängender Schwarm aus einfachen Funden
  const pool = [["scrap", 50], ["cell", 35], ["chip", 12], ["core", 3]];
  let rr = Math.random() * 100, id = "scrap";
  for (const [k, w] of pool) { if ((rr -= w) < 0) { id = k; break; } }
  const sym = BY_ID[id], cells = [[(Math.random() * NET_C) | 0, (Math.random() * NET_R) | 0]], key = ([c, r]) => c * 10 + r, have = new Set(cells.map(key));
  while (cells.length < 5) {
    const [c, r] = cells[(Math.random() * cells.length) | 0], [dx, dy] = [[1, 0], [-1, 0], [0, 1], [0, -1]][(Math.random() * 4) | 0];
    const nc = c + dx, nr = r + dy;
    if (nc < 0 || nr < 0 || nc >= NET_C || nr >= NET_R || have.has(nc * 10 + nr)) continue;
    cells.push([nc, nr]); have.add(nc * 10 + nr);
  }
  cells.forEach(([c, r]) => { board[c][r] = sym; });
}
function netFloat(cells, text, sub, color) {
  const bay = $("bay"), w = bay.clientWidth / NET_C, h = bay.clientHeight / NET_R;
  const cx = cells.reduce((a, [c]) => a + c, 0) / cells.length, cy = cells.reduce((a, [, r]) => a + r, 0) / cells.length;
  const f = document.createElement("div"); f.className = "netfloat"; f.style.setProperty("--fc", color);
  f.style.left = ((cx + .5) * w) + "px"; f.style.top = ((cy + .5) * h) + "px";
  f.innerHTML = `${text}${sub ? `<small>${sub}</small>` : ""}`;
  bay.appendChild(f); setTimeout(() => f.remove(), 1150);
}
function netCasc(m, show) {
  const b = $("casc"); b.hidden = !show; $("cascN").textContent = "×" + m;
  if (show) { b.classList.remove("pop"); void b.offsetWidth; b.classList.add("pop"); }
}
const netWait = ms => wait(netRun && netRun.fast ? Math.min(ms, 120) : ms * T());
async function netGull(board) {
  // Hilfsmöwe: fliegt über das Netz und lässt 1 bis 3 Rettungsringe fallen
  const bay = $("bay"), W = bay.clientWidth, H = bay.clientHeight;
  const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  svg.setAttribute("class", "netgull"); svg.setAttribute("viewBox", `0 0 ${W} ${H}`);
  svg.innerHTML = `<g id="gullG">${DRONE}</g>`; bay.appendChild(svg);
  const g = svg.querySelector("#gullG"), dur = 1300 * T(), t0 = performance.now();
  $("msg").className = "msg gold"; $("msg").textContent = "Hilfsmöwe! Sie lässt Rettungsringe ins Netz fallen …";
  radio("Funk: Eine Möwe kreist über dem Netz.", true);
  sfx.droneIn();
  const cand = []; board.forEach((col, c) => col.forEach((s, r) => { if (s.pay) cand.push([c, r]); }));
  const n = Math.min(cand.length, 1 + ((Math.random() * 3) | 0)), drops = [];
  for (let i = 0; i < n; i++) drops.push(cand.splice((Math.random() * cand.length) | 0, 1)[0]);
  await new Promise(res => {
    const fr = now => {
      const k = Math.min(1, (now - t0) / dur);
      g.setAttribute("transform", `translate(${W + 40 - (W + 80) * k} ${H * .12 + Math.sin(k * 9) * 6}) scale(${Math.max(1, W / 380)}) scale(-1 1)`);
      if (k < 1) requestAnimationFrame(fr); else res();
    };
    requestAnimationFrame(fr);
    drops.forEach(([c, r], i) => setTimeout(() => {
      board[c][r] = WILD;
      const old = netEl(c, r); if (old) old.remove();
      const el = netTile(WILD, c, r); el.classList.add("grow", "wildborn");
      sfx.crystal();
    }, dur * (.25 + i * .22)));
  });
  svg.remove();
  track("laser"); bump("lasers");
}
async function netGravity(board, removed) {
  // entfernte Felder raus, Rest rutscht nach unten, neues Treibgut fällt von oben nach
  let crystals = 0;
  const tf = T();
  for (let c = 0; c < NET_C; c++) {
    const keep = [];
    for (let r = 0; r < NET_R; r++) if (!removed.has(c * 10 + r)) keep.push({ s: board[c][r], el: netEl(c, r) });
    const missing = NET_R - keep.length; if (!missing) continue;
    const fresh = Array.from({ length: missing }, () => { const s = netPick(); if (s.id === "crystal") crystals++; return { s, el: null }; });
    const col = [...fresh, ...keep];
    col.forEach((it, r) => {
      board[c][r] = it.s;
      if (it.el) { it.el.style.transitionDelay = "0ms"; it.el.style.setProperty("--r", r); }
      else { const el = netTile(it.s, c, r, r - missing - 1, Math.round((c * 30) * tf)); void el.offsetWidth; el.style.setProperty("--r", r); }
    });
  }
  return crystals;
}
function netDust(pts) {
  state.dustMeter = (state.dustMeter || 0) + pts;
  let whole = 0;
  while (state.dustMeter >= 100) { state.dustMeter -= 100; whole++; }
  if (whole) addDust(whole, null); else renderDust(false);
}
function gainDustFromSpin() {}
function renderSticky() {}

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
  $("bay").classList.remove("showing"); netCasc(1, false);
  $("msg").className = free ? "msg fs" : "msg";
  $("msg").textContent = free ? `Freispiel ${fsTotal - fsLeft} von ${fsTotal} …` : autoLeft > 0 ? `Auto-Wurf · noch ${autoLeft} …` : "Das Netz fliegt …";
  $("lastWin").textContent = "0"; $("lastWin").classList.remove("pos");
  render();
  sfx.start();
  const board = netNewBoard();
  boostSpinActive = false;
  if (!free && state.boostReady) { netForceWin(board); boostSpinActive = true; state.boostReady = 0; state.luck = 0; sfx.boostSpin(); }
  const tf = T();
  [...$("netGrid").children].forEach(el => { el.style.transitionDelay = Math.round(+el.style.getPropertyValue("--c") * 35 * tf) + "ms"; el.classList.add("sink"); el.style.setProperty("--r", NET_R + 1); });
  const run = netRun = { board, free, fast: false, timers: [], done: false };
  const dropAt = reduced ? 0 : 300 * tf, landAt = reduced ? 30 : dropAt + (NET_C * 70 + NET_R * 22 + 420) * tf;
  run.timers.push(setTimeout(() => { if (!run.done) netFill(board, !reduced); }, dropAt));
  for (let c = 0; c < NET_C; c++) run.timers.push(setTimeout(() => { if (!run.done && !slammed) sfx.stop(); }, dropAt + (c * 70 + 330) * tf));
  run.timers.push(setTimeout(() => netLanded(run), landAt));
}
function netLanded(run) {
  if (run.done) return;
  run.done = true; run.timers.forEach(clearTimeout);
  [...$("netGrid").children].forEach(el => { el.style.transitionDelay = "0ms"; });
  finish(run.board, run.free);
}
function quickStop() {
  if (!spinning || slammed || !netRun || netRun.done) return;
  slammed = true; sfx.slam();
  netFill(netRun.board, false);
  netLanded(netRun);
}
function press() {
  if (!$("bonus").hidden || !$("scratch").hidden) return;
  if (skipCelebration) { skipCelebration(); return; }
  if (spinning) { quickStop(); return; }
  if (netCascading && netRun) { netRun.fast = true; return; }
  spin();
}

async function finish(board, free) {
  faces = board;
  spinning = false; busy = true; netCascading = true; render();
  let total = 0, waves = 0, gull = false, dustPts = 2 + board.flat().filter(s => s.id === "crystal").length * 3;
  const caught = [];
  for (;;) {
    let cl = netClusters(board);
    if (!cl.length && waves === 0 && !gull && !free && Math.random() < GULL_P * (boostOn("drones") ? 4 : 1)) { gull = true; await netGull(board); await netWait(450); cl = netClusters(board); }
    if (!cl.length && waves === 0 && free && !gull && Math.random() < .25) { gull = true; await netGull(board); await netWait(450); cl = netClusters(board); }
    if (!cl.length) break;
    let m;
    if (free) { m = fsMult; if (fsMult < FS_NET_MAX) fsMult++; }
    else m = CASCADE_MULT[Math.min(waves, CASCADE_MULT.length - 1)];
    waves++;
    const removed = new Set(); let w = 0;
    for (const x of cl) {
      const f = NET_PAY[x.sym.id][netBucket(x.cells.length)];
      w += f; caught.push({ sym: x.sym, count: x.cells.length, factor: f });
      track("symwin", 1, x.sym.id); if (x.cells.length >= 8) track("four");
      x.cells.forEach(([c, r]) => { removed.add(c * 10 + r); const el = netEl(c, r); if (el) { el.classList.add("hit"); el.style.setProperty("--hc", x.sym.color || "#ffffff"); } });
    }
    const cw = Math.round(w * bet() * m * lineBoost());
    total += cw;
    $("bay").classList.add("showing");
    cl.forEach((x, i) => netFloat(x.cells, `+${Math.round(NET_PAY[x.sym.id][netBucket(x.cells.length)] * bet() * m * lineBoost())}`, `${x.cells.length}× ${x.sym.name}${m > 1 ? " · ×" + m : ""}`, x.sym.color));
    netCasc(m, waves > 1 || free);
    if (waves > 1) sfx.streakUp(Math.min(4, waves)); else sfx.small();
    $("lastWin").textContent = total; $("lastWin").classList.add("pos");
    $("msg").className = free ? "msg fs" : "msg win";
    $("msg").textContent = `${waves > 1 ? `Nachfang ${waves}: ` : ""}${cl.map(x => `${x.cells.length}× ${x.sym.name}`).join(", ")}${m > 1 ? ` (×${m})` : ""} · bisher +${total}`;
    await netWait(700);
    removed.forEach(k => { const el = netEl((k / 10) | 0, k % 10); if (el) el.classList.add("caught"); });
    sfx.coin(waves);
    await netWait(360);
    [...$("netGrid").querySelectorAll(".caught")].forEach(el => el.remove());
    $("bay").classList.remove("showing");
    [...$("netGrid").children].forEach(el => el.classList.remove("hit"));
    dustPts += (await netGravity(board, removed)) * 3;
    await netWait(480);
    if (free) multUp();
  }
  netCascading = false;
  netDust(dustPts);

  const cells = id => { const out = []; board.forEach((col, c) => col.forEach((s, r) => { if (s.id === id) out.push([c, r]); })); return out; };
  const scatters = cells("beacon");
  const award = scatters.length >= 3 ? FS_AWARD[Math.min(scatters.length, 5)] : 0;
  const features = ["capsule", "warp"].map(id => ({ id, ...NET_FEAT[id], cells: cells(id) })).filter(f => f.cells.length >= 3);
  const mark = (list, col) => list.forEach(([c, r]) => { const el = netEl(c, r); if (el) { el.classList.add("hit"); el.style.setProperty("--hc", col); } });
  if (award) { mark(scatters, "#b5d65a"); sfx.scatter(scatters.length); }
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
    const top = caught.slice().sort((a, b) => b.factor - a.factor)[0];
    parts.push(`${boostSpinActive ? "Koko-Boost! " : ""}${gull ? "Rettungsring! " : ""}${caught.length} ${caught.length > 1 ? "Schwärme" : "Schwarm"}${waves > 1 ? ` in ${waves} Wellen` : ""}: +${win} Muscheln${sMult > 1 ? ` · Strähne ×${String(sMult).replace(".", ",")}` : ""}.`);
    addLog(gull ? "wild" : top.sym.id, `${top.count}× ${top.sym.name}${caught.length > 1 ? ` +${caught.length - 1}` : ""}${waves > 1 ? ` · ${waves} Wellen` : ""}`, "+" + win, gull ? "#ffffff" : top.sym.color);
  }
  netCasc(1, false);
  bipAfterSpin({ win, factor: win / bet(), lasered: gull, award, features: features.length, prevStreak, streak, free });
  if (!free && win >= bet() * 15) setTimeout(() => addDust(1, "große Bergung"), 1200);
  if (win > 0) { bump("wins"); sess.won += win; sess.best = Math.max(sess.best, win); if (!free) maxStat("maxFactor", win / bet()); }
  if (award && !free) bump("fs");
  if (features.some(f => f.id === "capsule")) bump("pick");
  maxStat("maxStreak", streak);
  if (award && !free) track("fs");
  if (features.length) track("bonus", features.length);
  if (award) {
    parts.push(free ? `Noch eine Flaschenpost: +${award} Freispiele!` : `${scatters.length} Flaschenposten gefunden: ${award} Freispiele!`);
    addLog("beacon", free ? "Freispiele verlängert" : "Freispiele ausgelöst", `${award} FS`, "#b5d65a");
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
    msg.className = "msg gold"; msg.textContent = `${f.title} abgeschlossen: +${amount} Muscheln.`;
    bip(amount >= bet() * 10 ? "bonusGood" : "bonusMeh", 3);
  }
  if (award) {
    fsLeft += award; fsTotal += award;
    if (!free) { state.fsRounds++; fsWin = 0; fsMult = FS_MULT; }
    render();
    await celebrateFs(award, free);
  }

  if (inFs()) {
    if (!parts.length) { msg.className = "msg fs"; msg.textContent = `Kein Fang. Noch ${fsLeft} Freispiel${fsLeft === 1 ? "" : "e"}, Nachfang bleibt bei ×${fsMult}.`; }
    busy = false; fsActive = true; render();
    await wait((parts.length ? 500 : 650) * T());
    spin(true);
    return;
  }

  if (free) {
    fsActive = false;
    msg.className = "msg win";
    msg.textContent = `Freispiele beendet: insgesamt +${fsWin} Muscheln, Nachfang bis ×${fsMult}.`;
    if (fsWin >= bet() * 50) setTimeout(() => addDust(2, "starke Freispiele"), 2500);
    fsMult = FS_MULT;
    addLog("beacon", "Freispiele gesamt", "+" + fsWin, "#b5d65a");
    render();
    await celebrateFsEnd(fsWin, state.credits);
    bip("fsend", 2);
    fsTotal = 0;
  } else if (!parts.length) {
    if (state.credits < 5) { msg.className = "msg lose"; msg.textContent = "Muscheln erschöpft."; }
    else if (state.credits < bet()) { msg.className = "msg lose"; msg.textContent = "Zu wenig Muscheln für diesen Einsatz. Senke den Einsatz."; }
    else { msg.className = "msg"; msg.textContent = "Kein Schwarm im Netz. Neuer Wurf?"; }
  }
  countCredits(state.credits, 0);
  fsActive = false;
  if (!free && Math.random() < bet() / JP_DIV * (boostOn("treasure") ? 5 : 1)) {
    const amount = Math.floor(state.pot);
    state.pot = JP_SEED; state.credits += amount;
    state.best = Math.max(state.best, amount); state.peak = Math.max(state.peak, state.credits);
    autoLeft = 0; clearAutoMarks();
    addLog("crystal", "PIRATENSCHATZ", "+" + amount, "#ffc94a");
    radio(`Funk: PIRATENSCHATZ GEHOBEN! ${amount} Muscheln. Alle Inseln reden davon.`, true, 15000);
    renderMeta();
    bump("jackpots"); sess.won += amount; setTimeout(() => addDust(5, "Piratenschatz"), 5000);
    await celebrateJackpot(amount, state.credits);
    bip("jackpot", 3);
    msg.className = "msg gold"; msg.textContent = `Piratenschatz gehoben: +${amount} Muscheln!`;
  }
  await processProgress();
  if (state.credits < 5) { autoLeft = 0; clearAutoMarks(); await handleBankruptcy(); }
  if (!free && Math.random() < 1 / 150) findAlbumItem(curSector().id, "Wurf");
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
    `<tr><td>${ICONS[x.id]}${x.name}</td>${NET_PAY[x.id].map(p => `<td class="pay">${fmtF(p)}</td>`).join("")}</tr>`).join("");
  $("panel-bonus").innerHTML = `
    <div class="feat" style="--fc:#5cc8b0">${ICONS.core}<div><h3>Schwärme und Nachfang</h3><p>Ab 5 gleichen Funden, die sich waagerecht oder senkrecht berühren, landet ein Schwarm im Netz. Danach rutscht alles nach unten und neues Treibgut fällt nach. Jede weitere Welle in derselben Runde zahlt mehr: ×1, ×2, ×3, dann ×5.</p></div></div>
    <div class="feat" style="--fc:#b5d65a">${ICONS.beacon}<div><h3>Flaschenpost · Freispiele</h3><p>Liegen nach dem letzten Nachfang 3, 4 oder 5 Flaschenposten irgendwo im Netz, gibt es 8, 12 oder 20 Freispiele. Der Nachfang-Multiplikator startet bei ×2, steigt mit jeder Welle bis ×10 und bleibt bis zum Ende der Freispiele erhalten. Neue Flaschenposten verlängern die Runde.</p></div></div>
    <div class="feat" style="--fc:#ffc94a">${ICONS.capsule}<div><h3>Treibkiste · Kistenbergung</h3><p>3 oder mehr Treibkisten im Netz starten die Kistenbergung: Kisten öffnen, Muscheln sammeln, ein ×2 verdoppelt alles. Beim dritten Alarm ist Schluss.</p></div></div>
    <div class="feat" style="--fc:#e0704a">${ICONS.warp}<div><h3>Strudel · Strudelfahrt</h3><p>3 oder mehr Strudel im Netz starten die Strudelfahrt am Steuerrad. „Weiter“ führt in höhere Ringe, bis zum 300-fachen Einsatz.</p></div></div>
    <div class="feat" style="--fc:#8fbfdf">${ICONS.wild}<div><h3>Hilfsmöwe · Rettungsring</h3><p>Bleibt das Netz leer, kommt manchmal eine Möwe und lässt 1 bis 3 Rettungsringe fallen. Ein Rettungsring zählt für jeden Schwarm. In Freispielen hilft sie öfter.</p></div></div>
    <div class="feat" style="--fc:#ffb347">${ICONS.crystal}<div><h3>Bernstein und Kräuterhütte</h3><p>Jeder Wurf füllt den Bernsteinmesser ein wenig, jeder Bernstein im Netz deutlich mehr, auch die nachgefallenen. Ist er voll, gibt es 1 Bernstein. In der Kräuterhütte tauschst du ihn gegen Tränke für einige Minuten.</p></div></div>
    <div class="feat" style="--fc:#ffc94a">${ICONS.wild}<div><h3>Koko-Boost</h3><p>Jeder Wurf ohne Fang füllt Kokos Glücksladung. Nach ${BOOST_AT} leeren Würfen ist sie voll, und der nächste Wurf fängt garantiert einen Schwarm.</p></div></div>
    <div class="feat" style="--fc:#ffc94a">${ICONS.ladder}<div><h3>Risikoleiter</h3><p>Nach einem normalen Gewinn: Steig die Leiter hoch, von ×1 bis ×100. Das Licht springt zwischen Ziel und Absturz, du drückst Stopp. Die Chancen sind fair, kassieren geht jederzeit.</p></div></div>
    <div class="feat" style="--fc:#e0704a">${ICONS.beacon}<div><h3>Signal-Risiko</h3><p>Nach einem normalen Gewinn kannst du ihn verdoppeln: Türkis oder Koralle raten, genau 50 : 50, höchstens fünf Runden.</p></div></div>
    <div class="feat" style="--fc:#ff9a3c">${ICONS.core}<div><h3>Strähne</h3><p>Fängst du mehrere Würfe hintereinander etwas, gibt es einen Bonus auf den Fang: 2 in Folge ×1,1, 3 in Folge ×1,25, ab 4 in Folge ×1,5.</p></div></div>
    <div class="feat" style="--fc:#ffc94a">${ICONS.relic}<div><h3>Piratenschatz</h3><p>Jeder Wurf legt 1,5 % deines Einsatzes in den Topf, der bei 500 Muscheln startet. Die Chance pro Wurf ist Einsatz ÷ 40.000.</p></div></div>
    <div class="feat" style="--fc:#5cc8b0">${ICONS.up_engine}<div><h3>Expeditionen, Inseln und Aufträge</h3><p>Schick dein Floß auf Expedition, erkunde neue Inseln über deinen Rang und erfülle Aufträge für Muscheln und XP.</p></div></div>`;
  const demo = [0,0,1,0,0,0, 0,1,1,2,0,0, 0,0,1,1,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0];
  $("lines").innerHTML = `<div><b>Beispiel:</b> 6 Thunfische, die sich berühren, plus ein Rettungsring = ein Schwarm aus 7.</div><div class="swarmdemo">${demo.map(v => `<i class="${v === 1 ? "on" : v === 2 ? "w" : ""}"></i>`).join("")}</div>`;
}

MISSION_TYPES.symwin.text = m => `Fange ${m.goal} Schwärme mit ${BY_ID[m.meta].name}`;
MISSION_TYPES.four.text = () => "Fange einen Schwarm aus 8 oder mehr";
Object.assign(SYM_HELP, {
  beacon: "Flaschenpost. Liegen 3 oder mehr nach dem letzten Nachfang im Netz, gibt es Freispiele (3 = 8, 4 = 12, 5 = 20). Dort bleibt der Nachfang-Multiplikator bis ×10 erhalten.",
  capsule: "Treibkiste. 3 oder mehr im Netz starten die Kistenbergung.",
  warp: "Strudel. 3 oder mehr im Netz starten die Strudelfahrt am Steuerrad.",
  wild: "Rettungsring. Kommt nur von der Hilfsmöwe und zählt für jeden Schwarm.",
});
HELP_RULES.unshift(
  [".tile[data-sym]", el => { const id = el.dataset.sym, x = id === "wild" ? WILD : BY_ID[id]; if (!x) return null;
    if (x.pay) { const p = NET_PAY[id]; return [x.name, `Schwarm aus 5–6: <b>${Math.round(p[0] * bet())}</b>, 7–8: <b>${Math.round(p[1] * bet())}</b>, 9–10: <b>${Math.round(p[2] * bet())}</b>, 13+: <b>${Math.round(p[4] * bet())}</b> Muscheln beim aktuellen Einsatz, vor dem Nachfang-Multiplikator.${id === "crystal" ? " Jeder Bernstein füllt außerdem den Bernsteinmesser." : ""}`]; }
    return [x.name, SYM_HELP[id]]; }],
  [".bay, #frame, #netGrid", () => ["Fangnetz", "6 × 5 Felder. Ab 5 gleichen Funden, die sich berühren, landet ein Schwarm im Netz. Danach fällt neues Treibgut nach, und jede weitere Welle zahlt mehr (×1, ×2, ×3, ×5)."]],
  ["#casc", () => ["Nachfang", "Der aktuelle Multiplikator dieser Runde. Er steigt mit jeder neuen Welle."]],
);
'''

SFX_JS = r'''
/* ---------- Treibgut: rustikale Geräusche (Holz, Wasser, Tau, Glocke, Marimba) ---------- */
function lnoise(dur, vol = .3, at = 0, lp = 1200) {
  const c = audio(); if (!c) return;
  const t = c.currentTime + at;
  const buf = c.createBuffer(1, Math.max(1, Math.floor(c.sampleRate * dur)), c.sampleRate);
  const d = buf.getChannelData(0); for (let i = 0; i < d.length; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / d.length, 2);
  const s = c.createBufferSource(), f = c.createBiquadFilter(), g = c.createGain();
  f.type = "lowpass"; f.frequency.value = lp; g.gain.value = vol;
  s.buffer = buf; s.connect(f); f.connect(g); g.connect(master); s.start(t);
}
const marimba = (f, at = 0, vol = .14) => { tone(f, .35, { type: "sine", vol, at }); tone(f * 4, .08, { type: "sine", vol: vol * .25, at }); };
const shipBell = (f, at = 0, vol = .12) => { tone(f, 1.6, { type: "sine", vol, at }); tone(f * 2.76, .8, { type: "sine", vol: vol * .35, at }); tone(f * 5.4, .3, { type: "sine", vol: vol * .15, at }); };
const knock = (at = 0, vol = .3, f = 220) => { tone(f, .09, { type: "triangle", vol, at, slide: .6 }); lnoise(.05, vol * .5, at, 900); };
const plop = (at = 0, vol = .18) => { tone(620, .14, { type: "sine", vol, at, slide: .35 }); lnoise(.12, vol * .6, at, 1600); };
const splash = (at = 0, vol = .25) => { lnoise(.45, vol, at, 2200); noise(.18, vol * .3, at, 3000); tone(180, .2, { type: "sine", vol: vol * .6, at, slide: .5 }); };
const creakR = (at = 0, vol = .06) => { tone(150 + Math.random() * 40, .35, { type: "sawtooth", vol, at, slide: 1.4 }); };
Object.assign(sfx, {
  start() { lnoise(.4, .2, 0, 900); noise(.3, .05, .05, 2500); creakR(.02, .05); },
  tick() {},
  stop() { plop(0, .16); },
  slam() { splash(0, .3); },
  scatter(n) { [1568, 2093].forEach((f, i) => tone(f * Math.pow(1.06, n), .25, { type: "triangle", vol: .12, at: i * .06 })); },
  tease() {},
  coin(i) { [1319, 1760, 2093].slice(0, 2 + (i > 1 ? 1 : 0)).forEach((f, k) => tone(f, .12, { type: "triangle", vol: .08, at: k * .05 })); lnoise(.08, .08, 0, 3000); },
  small() { marimba(523); marimba(659, .08); },
  fanfare(level) {
    const runs = [[523, 659, 784, 1047], [392, 523, 659, 784, 1047, 1319], [392, 523, 659, 784, 1047, 1319, 1568]][level];
    runs.forEach((f, i) => marimba(f, i * .08, .14));
    shipBell(784, runs.length * .08, .1 + level * .02);
    if (level >= 1) splash(runs.length * .08, .15);
  },
  fs() { shipBell(659, 0, .14); shipBell(659, .45, .14); tone(147, 1.2, { type: "sawtooth", vol: .06, at: .9 }); tone(220, 1.2, { type: "triangle", vol: .08, at: .9 }); },
  click() { knock(0, .14, 520); },
  feature(kind) { if (kind === 0) { knock(0, .25, 180); knock(.08, .2, 220); } else { lnoise(.6, .15, 0, 700); tone(300, .6, { type: "sine", vol: .08, slide: .5 }); } },
  bonusStart() { tone(147, 1.1, { type: "sawtooth", vol: .06 }); tone(220, 1.1, { type: "triangle", vol: .08 }); [523, 659, 784, 1047].forEach((f, i) => marimba(f, .5 + i * .08)); },
  pick(n) { creakR(0, .05); marimba(659 + n * 30, .08, .1); },
  alarm() { shipBell(440, 0, .16); shipBell(440, .25, .16); knock(0, .3, 120); },
  mult() { [784, 988, 1175, 1568].forEach((f, i) => marimba(f, i * .06, .12)); },
  wheelTick() { knock(0, .1, 900); },
  upgrade() { knock(0, .3, 200); knock(.12, .3, 240); knock(.24, .25, 260); },
  bigUpgrade() { [0, .12, .24, .36].forEach((t, i) => knock(t, .3, 180 + i * 30)); [523, 659, 784, 1047, 1319].forEach((f, i) => marimba(f, .5 + i * .07)); shipBell(784, .9, .1); },
  scrap() { lnoise(.4, .3, 0, 600); knock(0, .4, 110); creakR(.05, .08); },
  lost() { tone(220, 1.6, { type: "sine", vol: .14, slide: .3 }); lnoise(1.4, .2, 0, 500); [0, .3, .55, .8].forEach(t => plop(t, .08)); },
  clang() { knock(0, .4, 170); knock(.06, .2, 260); },
  squeak(p = 1) { tone(1200 * p, .12, { vol: .14, slide: 1.6 }); tone(1800 * p, .1, { vol: .1, at: .1, slide: .7 }); },
  blips() { [660, 590, 740].forEach((f, i) => tone(f, .1, { type: "triangle", vol: .06, at: i * .09, slide: 1.05 })); },
  cough() { splash(0, .15); },
  boost() { lnoise(1.4, .22, 0, 600); noise(1.2, .05, .1, 1500); },
  zap() { lnoise(.3, .2, 0, 3000); [0, .07, .15].forEach(t => noise(.04, .1, t, 4000)); },
  sonar() { tone(220, .9, { type: "triangle", vol: .12, slide: 1.02 }); tone(330, .7, { type: "sine", vol: .06, at: .2 }); },
  creak() { creakR(0, .06); },
  pew() { noise(.25, .1, 0, 1800); creakR(.05, .05); },
  roll() { splash(0, .2); [523, 659, 784, 1047].forEach((f, i) => marimba(f, .4 + i * .06)); },
  ticket() { lnoise(.15, .12, 0, 4000); marimba(784, .1, .1); },
  streakUp(n) { [523, 659, 784, 988, 1175].slice(0, Math.min(5, n + 1)).forEach((f, i) => marimba(f * (1 + n * .04), i * .05, .11)); },
  streakBreak() { knock(0, .3, 130); },
  mission() { shipBell(1047, 0, .1); marimba(1319, .15); },
  rankUp() { [523, 659, 784, 1047, 1319].forEach((f, i) => marimba(f, i * .08)); shipBell(659, .45, .14); shipBell(988, .7, .1); },
  jackpot() { splash(0, .3); [0, .35, .7, 1.05].forEach(t => shipBell(784, t, .15)); [392, 523, 659, 784, 1047, 1319, 1568].forEach((f, i) => marimba(f, 1.2 + i * .08, .14)); },
  dust() { [1568, 2093, 2637].forEach((f, i) => tone(f, .3, { type: "sine", vol: .06, at: i * .06 })); },
  powerUp() { [0, .1, .2, .3, .4].forEach(t => plop(t, .08)); [659, 784, 988, 1319].forEach((f, i) => marimba(f, .6 + i * .07)); },
  boostSpin() { [784, 1047, 1319].forEach((f, i) => marimba(f, i * .05, .1)); },
  jump() { lnoise(1.5, .25, 0, 700); tone(110, 1.4, { type: "sine", vol: .1, slide: 2 }); shipBell(659, 1.1, .1); },
  droneIn() { tone(1400, .28, { type: "sawtooth", vol: .04, slide: .6 }); tone(1250, .3, { type: "sawtooth", vol: .04, at: .3, slide: .55 }); },
  laser(dur) { noise(dur, .04, 0, 2500); },
  shatter() { knock(0, .4, 140); lnoise(.4, .25, 0, 1200); },
  crystal() { plop(0, .1); [1319, 1760, 2093].forEach((f, i) => tone(f, .4, { type: "triangle", vol: .07, at: .05 + i * .05 })); },
  levelUp() { [523, 784, 1047].forEach((f, i) => marimba(f, i * .1)); },
});
function skySparks(sky, x, y, n) {
  const [sx, sy] = toSky(sky, x, y);
  for (let i = 0; i < n; i++) sky.parts.push({ x: sx, y: sy, vx: (Math.random() - .5) * 4, vy: -1 - Math.random() * 2.5, r: 1.4, life: 1, kind: "drop" });
}
'''

COUGH_OLD = '''for (let i = 0; i < 14; i++) { const [x, y, sc] = toSky(sky, g.l - 14, 106); sky.parts.push({ x, y, vx: -Math.random() * 2, vy: (Math.random() - .5) * 1.5, r: 3 * sc, life: 1, kind: "smoke" }); } skySparks(sky, g.l - 14, 106, 8, [], 1.2); bubbleAt(svg, view, g.l, 92, "*hust*");'''
COUGH_NEW = '''skySparks(sky, g.l - 24, 118, 14); bubbleAt(svg, view, g.l, 92, "*platsch*");'''

HOOK_OLD = '''    // Klick ins All: Bordlaser
    sfx.pew();
    const ln = document.createElementNS("http://www.w3.org/2000/svg", "line");
    ln.setAttribute("x1", g.n - 4); ln.setAttribute("y1", 106); ln.setAttribute("x2", p.x); ln.setAttribute("y2", p.y);
    ln.setAttribute("stroke", ["#ff6b3c", "#ff9a3c", "#4fe3ff", "#ff4fd8"][H]); ln.setAttribute("stroke-width", 2.5); ln.setAttribute("stroke-linecap", "round"); ln.setAttribute("filter", "url(#glow)");
    fxG.appendChild(ln);
    let o = 1; const fade = () => { o -= .12; ln.setAttribute("opacity", o); if (o > 0) requestAnimationFrame(fade); else ln.remove(); }; requestAnimationFrame(fade);
    skySparks(sky, p.x, p.y, 12, [], 1.1);
    discover("laser");'''
HOOK_NEW = '''    // Klick aufs Meer: Wurfhaken an der Leine
    sfx.pew();
    const hx = g.n - 22, hy = g.t - 14, mx2 = (hx + p.x) / 2, my2 = Math.min(hy, p.y) - 26;
    const hook = document.createElementNS("http://www.w3.org/2000/svg", "g");
    hook.innerHTML = `<path d="M${hx},${hy} Q${mx2},${my2} ${p.x},${p.y}" stroke="#e0c890" stroke-width="1.3" fill="none" stroke-dasharray="3 2"/><g transform="translate(${p.x} ${p.y})"><path d="M0,-6 V2 q0,4 -4,4 q-3,0 -3,-3" stroke="#c9ccd4" stroke-width="1.6" fill="none" stroke-linecap="round"/><circle r="5" fill="none" stroke="#ffffff" stroke-width="1" opacity=".6"><animate attributeName="r" from="3" to="14" dur=".6s" fill="freeze"/><animate attributeName="opacity" from=".8" to="0" dur=".6s" fill="freeze"/></circle></g>`;
    fxG.appendChild(hook);
    setTimeout(() => sfx.stop(), 180);
    let o = 1; const fade = () => { o -= .03; hook.setAttribute("opacity", o); if (o > 0) requestAnimationFrame(fade); else hook.remove(); }; setTimeout(() => requestAnimationFrame(fade), 300);
    skySparks(sky, p.x, p.y, 10);
    discover("laser");'''

# ruhigeres Meer: Ersetzungen in OCEAN_SKY (vor dem Einfügen anwenden)
SKY_SLOW = [
    ("const speed = (0.03 + E * 0.12 + warpBoost * 0.35 + (performance.now() < shipBoostUntil ? 0.9 : 0)) * dt;\n  const sec = curSector()",
     "const speed = (0.01 + E * 0.03 + warpBoost * 0.05 + (performance.now() < shipBoostUntil ? 0.22 : 0)) * dt;\n  const sec = curSector()"),
    ("for (const cl of o.stars) { cl.x -= (.04 + speed * .02) * cl.z * dt * .5;", "for (const cl of o.stars) { cl.x -= (.012 + speed * .01) * cl.z * dt * .5;"),
    ("  skyIsland(c, o, sec, hz, now);", "  o.isl = (o.isl || 0) + dt * (.0022 + E * .0012);\n  skyIsland(c, o, sec, hz, now, o.isl);"),
    ("function skyIsland(c, o, sec, hz, now) {\n  const span = o.w * 1.8, ix = ((o.w * 1.15 - now * .006) % span + span) % span - o.w * .35",
     "function skyIsland(c, o, sec, hz, now, isl = 0) {\n  const span = o.w * 1.8, ix = ((o.w * 1.15 - isl) % span + span) % span - o.w * .35"),
    ("o.off = (o.off || 0) + speed * 3 + dt * .015;", "o.off = (o.off || 0) + speed * 2.2 + dt * .006;"),
    ("d.x -= (d.v + speed * .3) * (dt / 16);", "d.x -= (d.v * .35 + speed * .25) * (dt / 16);"),
    ("o.parts.push({ x, y, vx: -1.4 - E * 1.1, vy: (Math.random() - .5) * .25, r: (1.2 + E * .45) * s, life: 1, kind: \"trail\", col: \"255,255,255\" });",
     "o.parts.push({ x, y, vx: -.45 - E * .35, vy: (Math.random() - .5) * .15, r: (1.2 + E * .45) * s, life: 1, kind: \"trail\", col: \"255,255,255\" });"),
    ("d.x -= speed * 1.5 + .05 * dt * .06;", "d.x -= speed * .8 + .02 * dt * .06;"),
    ("bd.x -= (bd.v + speed * .05) * dt * .06;", "bd.x -= (bd.v * .6 + speed * .03) * dt * .06;"),
]
