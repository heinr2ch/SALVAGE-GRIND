# Neustadt Teil 3: eigenes Grundspiel "Hochstapler" (kleine Walze, Etagen stapeln, auszahlen oder Abriss)

TOWER_HTML = [
    ('''        <div class="bay net col" id="bay">
          <div class="netgrid" id="netGrid" aria-label="Werkbank mit 5 Walzen und 3 Reihen"></div>
          <div class="casc" id="casc" hidden>Rex sammelt <b id="cascN">0</b></div>''',
     '''        <div class="bay tower" id="bay">
          <div class="tw-stage" id="twStage"><svg viewBox="0 0 160 200" preserveAspectRatio="xMidYMax meet" id="twSvg" aria-label="Dein Hochhaus"><g id="twCam"><g id="twFloors"></g><g id="twTop"></g></g><g id="twFx"></g></svg>
            <div class="tw-height"><span>Höhe</span><b id="twH">0</b></div></div>
          <div class="tw-side">
            <div class="tw-reel" id="twReel" aria-label="Bauwalze"><div class="tw-strip" id="twStrip"></div><i class="tw-line" aria-hidden="true"></i></div>
            <div class="tw-val"><span>Wert</span><b id="twVal">×0</b><small id="twNext">Nächste Etage: ×1,16</small></div>
            <div class="tw-flags"><span class="tw-shield" id="twShield" hidden>Kran-Sicherung <b id="twShieldN">1</b></span><span class="tw-plans" id="twPlans">Baupläne <b id="twPlansN">0</b>/3</span></div>
            <button type="button" class="tw-cash" id="twCash" disabled>Auszahlen<b id="twCashAmt">0</b></button>
            <button type="button" class="tw-target" id="twTarget" title="Auto-Runden zahlen bei diesem Wert automatisch aus">Auto-Ziel ×2</button>
          </div>
          <div class="casc" id="casc" hidden>Etage <b id="cascN">0</b></div>'''),
    ('<span><b id="fsLeft">0</b> übrig · Rex <b id="fsStick">0</b>/4 · Sammler <em class="fsmult" id="fsMultBox">×<b id="fsMult">1</b></em> · bisher <b id="fsWin">0</b></span>',
     '<span><b id="fsLeft">0</b> übrig · Start auf Etage <em class="fsmult" id="fsMultBox"><b id="fsMult">3</b></em><b id="fsStick" hidden>0</b> · bisher <b id="fsWin">0</b></span>'),
    ('<th>Teil</th><th>3 Walzen</th><th>4 Walzen</th><th>5 Walzen</th>', '<th>Baustein</th><th>Etagen</th><th>Chance</th><th>Besonderheit</th>'),
    ('aria-controls="panel-lines">Wege</button>', 'aria-controls="panel-lines">Wert</button>'),
]

TOWER_CSS = r'''
/* ---------- Neustadt: Hochstapler (Turm und kleine Walze) ---------- */
.frame { grid-template-columns: minmax(0, 1fr); width: min(100%, 640px); margin: 0 auto; }
.bay.tower { display: grid; grid-template-columns: minmax(0, 1.25fr) minmax(0, 1fr); gap: 12px; align-items: stretch; position: relative; min-height: 0; }
.tw-stage { position: relative; border-radius: 12px; overflow: hidden; min-height: 320px; min-width: 0;
  background: linear-gradient(180deg, #1c3a5a 0%, #2a5a7a 55%, #f0b07a 100%); box-shadow: inset 0 0 0 1px rgba(255,255,255,.08); }
.tw-stage svg { position: absolute; inset: 0; width: 100%; height: 100%; }
#twCam { transition: transform .45s cubic-bezier(.3,1.2,.5,1); }
.tw-height { position: absolute; left: 8px; top: 8px; padding: 4px 9px; border-radius: 9px; background: rgba(8,16,26,.6); display: grid; line-height: 1.05; }
.tw-height span { font: 700 .55rem var(--f-body); letter-spacing: .14em; text-transform: uppercase; color: var(--ink-soft); }
.tw-height b { font: 700 1.25rem var(--f-mono); color: #ffffff; }
.tw-side { display: grid; gap: 9px; align-content: start; min-width: 0; }
.tw-reel { position: relative; height: calc(var(--twc, 64px) * 3); overflow: hidden; border-radius: 12px; background: linear-gradient(180deg, #0c1824, #16283a 50%, #0c1824); box-shadow: inset 0 0 0 1px rgba(255,255,255,.08), inset 0 0 20px rgba(0,0,0,.6); --twc: 64px; }
.tw-strip { position: absolute; left: 0; right: 0; top: 0; will-change: transform; }
.tw-strip .sym { height: var(--twc, 64px) !important; width: 100%; display: grid; place-items: center; }
.tw-strip .sym svg, .tw-strip .sym.feature svg { width: calc(var(--twc, 64px) * .8); height: calc(var(--twc, 64px) * .8); }
.tw-strip.blur { filter: blur(1.4px); }
.tw-line { position: absolute; left: 0; right: 0; top: calc(var(--twc, 64px)); height: var(--twc, 64px); border-block: 2px solid rgba(126,224,200,.55); pointer-events: none; box-shadow: 0 0 18px rgba(126,224,200,.15) inset; }
.tw-reel::before, .tw-reel::after { content: ""; position: absolute; left: 0; right: 0; height: 30%; z-index: 2; pointer-events: none; }
.tw-reel::before { top: 0; background: linear-gradient(180deg, rgba(8,14,22,.9), transparent); }
.tw-reel::after { bottom: 0; background: linear-gradient(0deg, rgba(8,14,22,.9), transparent); }
.tw-val { display: grid; gap: 1px; padding: 8px 10px; border-radius: 12px; background: rgba(0,0,0,.25); border: 1px solid var(--line); }
.tw-val span { font: 700 .58rem var(--f-body); letter-spacing: .14em; text-transform: uppercase; color: var(--ink-soft); }
.tw-val b { font: 700 1.6rem var(--f-mono); color: var(--ink); background: none; border: 0; padding: 0; box-shadow: none; }
.tw-val b.up { animation: twUp .45s cubic-bezier(.3,1.6,.5,1); color: var(--win); }
@keyframes twUp { 40% { transform: scale(1.18); } }
.tw-val small { font: 600 .66rem var(--f-mono); color: var(--ink-soft); }
.tw-flags { display: flex; flex-wrap: wrap; gap: 6px; }
.tw-flags span { padding: 3px 8px; border-radius: 99px; font: 700 .62rem var(--f-body); background: rgba(255,255,255,.06); color: var(--ink-soft); }
.tw-shield { color: #1a1408 !important; background: linear-gradient(180deg, #ffd27a, #e8a83a) !important; }
.tw-plans b { color: #9ad4ff; }
.tw-cash { display: grid; gap: 1px; padding: 10px; border-radius: 12px; border: 0; cursor: pointer; font: 800 .82rem var(--f-display); letter-spacing: .06em; text-transform: uppercase;
  color: #0c1a14; background: linear-gradient(180deg, #8ff0c8, #3fd0a0); box-shadow: 0 4px 0 #1f8a64, 0 8px 20px rgba(63,208,160,.25); transition: transform .08s, filter .15s; }
.tw-cash b { font: 700 1.15rem var(--f-mono); }
.tw-cash:active:not(:disabled) { transform: translateY(2px); box-shadow: 0 2px 0 #1f8a64; }
.tw-cash:disabled { cursor: default; filter: grayscale(.8) brightness(.6); box-shadow: none; }
.tw-cash.hot { animation: twHot 1.2s ease-in-out infinite; }
@keyframes twHot { 50% { filter: brightness(1.2); box-shadow: 0 4px 0 #1f8a64, 0 0 26px rgba(63,208,160,.6); } }
.tw-target { justify-self: start; padding: 4px 10px; border-radius: 99px; border: 1px solid var(--line); background: rgba(0,0,0,.2); color: var(--ink-soft); font: 700 .64rem var(--f-body); cursor: pointer; }
.twf { transition: opacity .3s; }
.twf.new { animation: twDrop .42s cubic-bezier(.3,1.5,.5,1); }
@keyframes twDrop { from { transform: translateY(-40px); opacity: 0; } }
#twFloors.fall .twf { transition: transform 1s cubic-bezier(.5,0,.8,.6), opacity 1s; }
.tw-crane .hook { animation: twSwing 2.4s ease-in-out infinite; transform-box: fill-box; transform-origin: 50% 0%; }
@keyframes twSwing { 50% { transform: rotate(6deg); } }
.tw-stage.shake { animation: shake .5s cubic-bezier(.36,.07,.19,.97) 2; }
.tw-stage.won { box-shadow: inset 0 0 0 2px #7ee0c8, 0 0 30px rgba(126,224,200,.4); }
.car { animation: carDrive var(--d, 10s) linear infinite; }
@keyframes carDrive { from { transform: translateX(-90px); } to { transform: translateX(300px); } }
.rotor { animation: rotor 3s linear infinite; }
@keyframes rotor { to { transform: rotate(360deg); } }
@media (max-width: 600px) { .bay.tower { gap: 8px; } .tw-stage { min-height: 250px; } .tw-flags span { font-size: .56rem; padding: 2px 6px; } .tw-val { padding: 6px 8px; } .tw-val small { font-size: .56rem; } .tw-val b { font-size: 1.25rem; } .tw-cash { padding: 8px; } .tw-cash b { font-size: 1rem; } .tw-reel { --twc: 52px; } }
@media (prefers-reduced-motion: reduce) { .car, .rotor, .tw-crane .hook, .tw-cash.hot { animation: none; } }
'''

TOWER_JS = r'''
/* ===================== Neustadt: Hochstapler (kleine Walze, Etagen stapeln) =====================
   Pro Runde zahlst du einmal den Einsatz. Jeder Dreh der kleinen Walze setzt Etagen auf dein Hochhaus, der Wert steigt.
   Du entscheidest nach jedem Dreh: weiterbauen oder auszahlen. Die Abrissbirne reißt alles ein (außer eine Kran-Sicherung fängt sie ab).
   Wert = 1,08 × 1,07^Höhe (Höhe 1: ×1,16 · 10: ×2,1 · 25: ×5,9 · 50: ×31 · 100: ×937, dann wird automatisch ausgezahlt).
   Balance per Simulation (tools/sim/hochstapler.js): Jede Ausstiegsstrategie zahlt etwa 101 bis 113 % zurück. */
const TW_W = { scrap: 30, cell: 22, chip: 16, core: 8, relic: 1.6, crystal: 5, wild: 2.5, capsule: 2.5, beacon: .3, warp: .1, crash: 14 };
const TW_D = { scrap: 1, cell: 1, chip: 2, core: 3, relic: 6, crystal: 1, wild: 1, capsule: 0, beacon: 0, warp: 0, crash: 0 };
const TW_C = 1.08, TW_G = 1.07, TW_MAX = 100, TW_FS_START = 3, TW_FS_AWARD = 3, TW_TARGETS = [1.5, 2, 3, 5, 10, 25];
const CRASH_SYM = { id: "crash", name: "Abrissbirne", w: 0, pay: null, special: "#ff4b5c" };
BY_ID.crash = CRASH_SYM;
const twSym = id => id === "wild" ? WILD : BY_ID[id];
const twMult = h => h <= 0 ? 0 : TW_C * Math.pow(TW_G, Math.min(h, TW_MAX));
const twFmt = m => "×" + String(m >= 100 ? Math.round(m) : m >= 10 ? m.toFixed(1) : m.toFixed(2)).replace(".", ",");
let tw = null, twHold = false, twSpinning = false, twFast = false, netCascading = false, colRun = null;
const twTarget = () => TW_TARGETS[Math.max(0, Math.min(TW_TARGETS.length - 1, state.twTarget ?? 1))];
function twPick() {
  const w = { ...TW_W };
  if (typeof boostOn === "function") { if (boostOn("drones")) w.wild *= 3; if (boostOn("signal")) w.beacon *= 2.5; }
  let tot = 0; for (const k in w) tot += w[k];
  let r = Math.random() * tot;
  for (const k in w) { if ((r -= w[k]) < 0) return k; }
  return "scrap";
}
const twAmount = () => tw ? Math.round(tw.bet * twMult(tw.h) * lineBoost()) : 0;

/* ----- Turmgrafik ----- */
const TW_STYLE = {
  scrap: { w: 58, fill: "#e8e2d0", win: "#ffd27a", trim: "#2f8a4a" }, cell: { w: 62, fill: "#dce6f0", win: "#9ad4ff", trim: "#4aa8ff" },
  chip: { w: 52, fill: "#3a5a7a", win: "#9ad4ff", trim: "#6fb8ff" }, core: { w: 46, fill: "#5a6a7a", win: "#cfe8ff", trim: "#ff7a59" },
  relic: { w: 50, fill: "#e8c060", win: "#fff4c8", trim: "#a87a10" }, crystal: { w: 56, fill: "#2a5aa8", win: "#ffe39a", trim: "#ffc94a" },
  wild: { w: 56, fill: "#c9ccd1", win: "#ffd27a", trim: "#ffc94a" },
};
function twFloorSVG(id, i, isNew) {
  const st = TW_STYLE[id] || TW_STYLE.scrap, y = 188 - (i + 1) * 10, x = 80 - st.w / 2;
  const wins = Math.floor((st.w - 8) / 8);
  return `<g class="twf${isNew ? " new" : ""}" data-i="${i}"><rect x="${x}" y="${y}" width="${st.w}" height="10" fill="${st.fill}" stroke="rgba(0,0,0,.35)" stroke-width=".6"/>
    <rect x="${x - 1}" y="${y}" width="${st.w + 2}" height="1.6" fill="${st.trim}"/>
    ${Array.from({ length: wins }, (_, k) => `<rect x="${x + 5 + k * 8}" y="${y + 3.4}" width="4.6" height="4.6" fill="${(i * 7 + k * 3) % 5 ? st.win : "#2a3a4a"}" opacity=".92"/>`).join("")}</g>`;
}
function twDraw(full) {
  const floors = tw ? tw.floors : [], fl = $("twFloors"), cam = $("twCam");
  if (full || !fl.children.length || fl.children.length > floors.length) {
    fl.classList.remove("fall");
    fl.innerHTML = `<rect x="0" y="188" width="160" height="12" fill="#3a3f46"/><path d="M0 191 H160" stroke="#e8e4d4" stroke-width=".7" stroke-dasharray="6 6" opacity=".6"/><rect x="34" y="185" width="92" height="3" fill="#8a8a84"/>` + floors.map((id, i) => twFloorSVG(id, i, false)).join("");
  } else {
    for (let i = fl.querySelectorAll(".twf").length; i < floors.length; i++) fl.insertAdjacentHTML("beforeend", twFloorSVG(floors[i], i, true));
  }
  const top = 188 - floors.length * 10;
  $("twTop").innerHTML = `<g class="tw-crane" transform="translate(0 ${top - 188})"><path d="M108 188 V128 M100 128 H150 M108 136 L100 128 M108 136 L116 128" stroke="#ffc94a" stroke-width="2" fill="none"/>
    <g class="hook"><path d="M140 128 V150" stroke="#c9ccd1" stroke-width=".8"/><rect x="134" y="150" width="12" height="7" fill="${tw && tw.shield ? "#ffd27a" : "#ff7a59"}" stroke="#7a3a1a" stroke-width=".6"/></g>
    ${tw && tw.shield ? `<g transform="translate(96 116)"><path d="M0 8 q8 -12 16 0z" fill="#ffd27a" stroke="#a87a10" stroke-width="1"/><path d="M-2 8 h20" stroke="#a87a10" stroke-width="1.6"/></g>` : ""}</g>`;
  const shift = Math.max(0, floors.length * 10 - 120);
  cam.style.transform = `translateY(${shift * (100 / 200)}%)`;
  cam.setAttribute("transform", `translate(0 ${shift})`);
  cam.style.transform = "";
  $("twH").textContent = tw ? tw.h : 0;
}
function twUi() {
  const v = tw ? twMult(tw.h) : 0, nextM = twMult((tw ? tw.h : 0) + 1);
  const vb = $("twVal"); vb.textContent = tw && tw.h ? twFmt(v) : "×0";
  $("twNext").textContent = tw && tw.h ? `Auszahlen: ${twAmount()} · nächste Etage ${twFmt(nextM)}` : `Erste Etage: ${twFmt(twMult(1))}`;
  $("twShield").hidden = !(tw && tw.shield); $("twShieldN").textContent = tw ? tw.shield : 0;
  $("twPlansN").textContent = tw ? tw.plans : 0;
  const can = !!tw && tw.h > 0 && !twSpinning && !twHold && !skipCelebration;
  const cb = $("twCash"); cb.disabled = !can; $("twCashAmt").textContent = tw && tw.h ? twAmount() : 0;
  cb.classList.toggle("hot", can && v >= 3);
  $("twTarget").textContent = `Auto-Ziel ${twFmt(twTarget())}`;
}
function twReelIdle() {
  const strip = $("twStrip"); if (strip.children.length) return;
  ["chip", "scrap", "core"].forEach(id => strip.appendChild(symEl(twSym(id))));
}
function twReel(result) {
  // kleine Walze: Streifen mit Zufallssymbolen, das Ergebnis landet in der Mitte
  return new Promise(res => {
    const strip = $("twStrip"), cell = strip.firstElementChild ? strip.firstElementChild.getBoundingClientRect().height || 64 : 64;
    const n = twFast || reduced ? 3 : 14;
    const ids = Array.from({ length: n }, () => { const k = twPick(); return k; });
    const keep = [...strip.children].slice(0, 3).map(el => el.dataset.sym);
    strip.replaceChildren();
    const seq = [...ids, keep[0] || "scrap", result, ids[0]].reverse();
    // oben: altes Feld, unten: neues Ergebnis; wir rollen von oben (alt) nach unten (neu)
    const all = [...keep, ...ids, "pad", result, "pad2"];
    all.forEach(id => strip.appendChild(symEl(twSym(id === "pad" || id === "pad2" ? twPick() : id))));
    strip.style.transition = "none"; strip.style.transform = "translateY(0)";
    void strip.offsetWidth;
    const target = -(all.length - 3) * cell, dur = (twFast || reduced ? 120 : 760) * T();
    strip.classList.toggle("blur", !twFast && !reduced);
    strip.style.transition = `transform ${dur}ms cubic-bezier(.2,.75,.25,1.08)`;
    strip.style.transform = `translateY(${target}px)`;
    const done = () => { strip.classList.remove("blur"); strip.style.transition = "none"; const last = [...strip.children].slice(-3); strip.replaceChildren(...last); strip.style.transform = "translateY(0)"; res(); };
    setTimeout(done, dur + 30);
    void seq;
  });
}
function twFloat(text, sub, color) {
  const st = $("twStage"), f = document.createElement("div"); f.className = "netfloat"; f.style.setProperty("--fc", color);
  f.style.left = "50%"; f.style.top = "38%"; f.innerHTML = `${text}${sub ? `<small>${sub}</small>` : ""}`;
  st.appendChild(f); setTimeout(() => f.remove(), 1150);
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
  if (!ready || twSpinning || skipCelebration || !$("scratch").hidden || !$("bonus").hidden || !$("naming").hidden || !$("worlds").hidden) return;
  if (tw) { if (!twHold) twStep(); return; }
  if (busy || spinning) return;
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
  tw = { h: free ? TW_FS_START : 0, shield: 0, plans: 0, floors: free ? Array(TW_FS_START).fill("scrap") : [], free, bet: free ? (tw && tw.bet) || bet() : bet(), spins: 0, bonus: 0, fsGain: 0, saved: 0, dust: 2, boost: false };
  boostSpinActive = false;
  if (!free && state.boostReady) { tw.shield = 2; tw.boost = true; boostSpinActive = true; state.boostReady = 0; state.luck = 0; sfx.boostSpin(); }
  busy = true; twFast = false;
  $("twStage").classList.remove("won");
  $("lastWin").textContent = "0"; $("lastWin").classList.remove("pos");
  twDraw(true); twUi(); render();
  twStep();
}
async function twStep() {
  if (!tw || twSpinning || twHold) return;
  twSpinning = spinning = true; render(); twUi();
  sfx.start();
  $("msg").className = tw.free ? "msg fs" : "msg";
  $("msg").textContent = tw.h ? `Etage ${tw.h + 1} wird gebaut …` : tw.free ? `Freibau ${fsTotal - fsLeft} von ${fsTotal} …` : "Der Grundstein wird gelegt …";
  const id = twPick();
  await twReel(id);
  sfx.stop();
  twSpinning = spinning = false; tw.spins++;
  if (id === "crash") {
    if (tw.shield) {
      tw.shield--; tw.saved++; sfx.crystal(); shakeFrame();
      twFloat("Abgefangen!", "Der Kran hält die Abrissbirne", "#ffd27a");
      $("msg").className = "msg gold"; $("msg").textContent = `Kran-Sicherung! Die Abrissbirne prallt ab. Wert bleibt ${twFmt(twMult(tw.h))}.`;
      track("laser"); bump("lasers");
      twDraw(); twUi(); render();
      return twAfterStep();
    }
    return twCrash();
  }
  const sym = twSym(id), d = TW_D[id];
  for (let i = 0; i < d; i++) tw.floors.push(id);
  tw.h += d;
  if (id === "wild") { tw.shield = Math.min(1, tw.shield + 1); }
  if (id === "crystal") tw.dust += 6;
  if (d) { track("symwin", 1, id); if (tw.h >= 20 && tw.h - d < 20) track("four"); }
  twDraw(); twUi(); render();
  const vb = $("twVal"); vb.classList.remove("up"); void vb.offsetWidth; if (d) vb.classList.add("up");
  if (d) { sfx.coin(Math.min(3, d)); twFloat(`+${d} ${d === 1 ? "Etage" : "Etagen"}`, `${sym.name} · ${twFmt(twMult(tw.h))}`, sym.color || sym.special || "#7ee0c8"); }
  $("msg").className = tw.free ? "msg fs" : "msg win";
  $("msg").textContent = d ? `${sym.name}: +${d} · Höhe ${tw.h} · Wert ${twFmt(twMult(tw.h))} = ${twAmount()}` : "";
  if (id === "capsule") {
    tw.plans++; twUi(); sfx.feature(0, 3);
    $("msg").className = "msg gold"; $("msg").textContent = `Bauplan ${tw.plans} von 3!${tw.plans === 3 ? " Bonusspiel!" : ""}`;
    if (tw.plans === 3) { tw.plans = 0; await twBonus("capsule"); }
  }
  if (id === "warp") await twBonus("warp");
  if (id === "beacon") {
    tw.fsGain += TW_FS_AWARD; fsLeft += TW_FS_AWARD; fsTotal += TW_FS_AWARD; sfx.scatter(3);
    if (!tw.free) { state.fsRounds++; fsWin = 0; }
    $("msg").className = "msg fs"; $("msg").textContent = `Baugenehmigung! +${TW_FS_AWARD} Freibauten nach dieser Runde, sie starten auf Etage ${TW_FS_START}.`;
    addLog("beacon", "Freibauten erhalten", `+${TW_FS_AWARD}`, "#c6f06b");
    if (!tw.free) { bump("fs"); track("fs"); }
  }
  if (tw.h >= TW_MAX) { $("msg").textContent = "Wolkenkratzer fertig! Höchste Höhe erreicht."; return twCash(true); }
  return twAfterStep();
}
async function twAfterStep() {
  render(); twUi();
  if (autoLeft > 0 && tw && tw.h > 0 && twMult(tw.h) >= twTarget()) { await wait(250 * T()); return twCash(); }
  if (autoLeft > 0 && tw) { await wait(320 * T()); if (tw && !twSpinning && !twHold) return twStep(); }
}
async function twBonus(id) {
  twHold = true;
  const f = { id, ...({ capsule: { bonus: "pick", title: "Bauplanauswahl", color: "#4aa8ff" }, warp: { bonus: "wheel", title: "Stadtrundfahrt", color: "#ff7a59" } })[id], cells: [] };
  await celebrateFeature(f);
  const amount = Math.round((await runBonus(f)) * bonusBoost());
  state.credits += amount; tw.bonus += amount;
  state.best = Math.max(state.best, amount); state.peak = Math.max(state.peak, state.credits);
  state.bonusCount = (state.bonusCount || 0) + 1; bump("pick"); track("bonus", 1);
  track("haul", amount); sess.won += amount; sess.best = Math.max(sess.best, amount);
  addDust(1, f.title); addLog(id, f.title, "+" + amount, f.color);
  render();
  if (amount > 0) await celebrateWin(amount, state.credits);
  bip(amount >= bet() * 10 ? "bonusGood" : "bonusMeh", 3);
  twHold = false;
  $("msg").className = "msg gold"; $("msg").textContent = `${f.title}: +${amount} Taler. Dein Hochhaus steht noch, weiterbauen oder auszahlen?`;
}
async function twCrash() {
  twHold = true;
  sfx.alarm(); shakeFrame();
  const st = $("twStage"); st.classList.remove("shake"); void st.offsetWidth; st.classList.add("shake");
  const fx = $("twFx"), top = 188 - tw.floors.length * 10 + Math.max(0, tw.floors.length * 10 - 120);
  fx.innerHTML = `<g><path d="M170 ${top - 40} Q130 ${top - 50} 100 ${top - 10}" stroke="#8a9098" stroke-width="1.2" fill="none"/><circle cx="100" cy="${top - 8}" r="11" fill="#2a2d30" stroke="#6a6f76" stroke-width="2"><animate attributeName="cx" from="190" to="100" dur=".35s" fill="freeze"/></circle></g>`;
  await wait(380 * T());
  sfx.scrap();
  const fl = $("twFloors"); fl.classList.add("fall");
  fl.querySelectorAll(".twf").forEach((el, i) => { const dx = (Math.random() - .5) * 120, rot = (Math.random() - .5) * 90; el.style.transform = `translate(${dx}px, ${220 - i * 4}px) rotate(${rot}deg)`; el.style.opacity = "0"; el.style.transformOrigin = "80px 150px"; });
  for (let i = 0; i < 18; i++) { const [x, y] = [80 + (Math.random() - .5) * 60, top + Math.random() * 40]; const p = document.createElementNS("http://www.w3.org/2000/svg", "circle"); p.setAttribute("cx", x); p.setAttribute("cy", y); p.setAttribute("r", 2 + Math.random() * 4); p.setAttribute("fill", "rgba(180,170,160,.6)"); fx.appendChild(p); }
  $("msg").className = "msg lose"; $("msg").textContent = `Abrissbirne! Das Hochhaus (Höhe ${tw.h}) ist eingestürzt.${tw.bonus ? ` Der Bonus von ${tw.bonus} bleibt dir.` : ""}`;
  addLog("crash", `Abriss bei Höhe ${tw.h}`, tw.bonus ? "+" + tw.bonus : "0", "#ff4b5c");
  await wait(900 * T());
  fx.innerHTML = "";
  return twEnd(0, true);
}
async function twCash(maxed) {
  if (!tw || tw.h <= 0 || twSpinning || twHold) return;
  twHold = true;
  const amt = twAmount(), h = tw.h;
  sfx.mission();
  $("twStage").classList.add("won");
  twFloat(`+${amt}`, `ausgezahlt bei ${twFmt(twMult(h))}`, "#7ee0c8");
  addLog(maxed ? "relic" : (tw.floors.at(-1) || "scrap"), `Höhe ${h} · ${twFmt(twMult(h))}`, "+" + amt, "#7ee0c8");
  return twEnd(amt, false);
}
async function twEnd(roundWin, crashed) {
  const free = tw.free, r = tw;
  tw = null; twHold = false; busy = true; render();
  netDust(r.dust);
  const prevStreak = streak;
  if (!free) { if (roundWin > 0) streak++; else streak = 0; }
  const sMult = free ? 1 : streakMult();
  const win = Math.round(roundWin * sMult);
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
  const msg = $("msg");
  if (win > 0) { msg.className = "msg win"; msg.textContent = `${r.boost ? "Paule-Boost! " : ""}Ausgezahlt bei Höhe ${r.h - 0}: +${win} Taler${sMult > 1 ? ` · Strähne ×${String(sMult).replace(".", ",")}` : ""}.`; }
  bipAfterSpin({ win: win + r.bonus, factor: (win + r.bonus) / r.bet, lasered: r.saved > 0, award: r.fsGain, features: 0, prevStreak, streak, free });
  if (!free && win >= r.bet * 15) setTimeout(() => addDust(1, "großer Bau"), 1200);
  if (win > 0) { bump("wins"); sess.won += win; sess.best = Math.max(sess.best, win); if (!free) maxStat("maxFactor", win / r.bet); }
  maxStat("maxStreak", streak);
  render();
  if (win > 0) { await wait(200 * T()); await celebrateWin(win, state.credits); }
  if (r.fsGain && !free) await simpleBanner({ tier: "Baugenehmigung", color: "var(--lime)", sub: `Freibauten starten auf Etage ${TW_FS_START}` }, `+${r.fsGain} Freibauten`, sfx.fs, ["#c6f06b", "#7ee0c8", "#ffffff"], 2200);
  if (inFs()) {
    busy = false; fsActive = true; render(); twDraw(true); twUi();
    msg.className = "msg fs"; msg.textContent = `${win ? `+${win} Taler. ` : crashed ? "Eingestürzt. " : ""}Noch ${fsLeft} Freibau${fsLeft === 1 ? "" : "ten"}: Drück „Bauen“, du startest auf Etage ${TW_FS_START}.`;
    saveGame(); checkAch();
    if (autoLeft > 0) { await wait(500 * T()); spin(); }
    return;
  }
  if (free) {
    fsActive = false;
    msg.className = "msg win"; msg.textContent = `Freibauten beendet: insgesamt +${fsWin} Taler.`;
    if (fsWin >= r.bet * 50) setTimeout(() => addDust(2, "starke Freibauten"), 2500);
    addLog("beacon", "Freibauten gesamt", "+" + fsWin, "#c6f06b");
    await celebrateFsEnd(fsWin, state.credits);
    bip("fsend", 2); fsTotal = 0;
  } else if (!win && crashed) {
    if (state.credits < 5) { msg.className = "msg lose"; msg.textContent = "Taler aufgebraucht."; }
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
  if (!free && Math.random() < 1 / 150) findAlbumItem(curSector().id, "Runde");
  if (!free) {
    if (win > 0 || r.fsGain || r.bonus) state.luck = 0; else state.luck = (state.luck || 0) + 1;
    if (r.boost && win > 0) { setTimeout(() => { bipState.last = 0; bip("boostWin", 3); }, 300); }
    if (state.luck >= BOOST_AT && !state.boostReady) await activateBoost();
    else if (state.luck === Math.round(BOOST_AT / 2)) bip("charging", 2);
    renderLuck();
  }
  checkAch(); sessPoint();
  if (!free && win > 0 && autoLeft === 0 && state.credits >= 5) offerGamble(win);
  busy = false; boostSpinActive = false;
  saveGame(); twUi();
  if (autoLeft > 0) {
    if (state.credits >= bet()) { autoLeft--; render(); await wait(450 * T()); if (autoLeft >= 0 && !spinning && !busy && !tw) { if (autoLeft === 0) clearAutoMarks(); spin(); return; } }
    else { autoLeft = 0; clearAutoMarks(); }
  }
  render();
}
function quickStop() { twFast = true; }
function press() {
  if (!$("bonus").hidden || !$("scratch").hidden) return;
  if (skipCelebration) { skipCelebration(); return; }
  if (twSpinning) { twFast = true; return; }
  spin();
}
function evaluate(board) { return { wins: [], scatters: [], scatterReels: 0, features: [] }; }
function finish() {}

const renderBase = render;
render = function () {
  renderBase();
  const fsMode = inFs() || fsActive, btn = $("spin");
  $("spinLabel").textContent = twSpinning ? "…" : tw ? "Weiter" : busy ? "Weiter" : fsMode ? "Frei bauen" : "Bauen";
  btn.setAttribute("aria-label", twSpinning ? "Schneller drehen" : tw ? "Nächste Etage bauen" : busy ? "Feier überspringen" : "Neue Runde: Grundstein legen");
  btn.disabled = !ready || (!tw && !busy && !twSpinning && !inFs() && state.credits < bet());
  if (tw) $("betVal").textContent = tw.free ? "frei" : tw.bet;
  $("fsMult").textContent = TW_FS_START;
  if ($("twCash")) twUi();
};
$("twCash").addEventListener("click", () => { sfx.click(); twCash(); });
$("twTarget").addEventListener("click", () => { state.twTarget = ((state.twTarget ?? 1) + 1) % TW_TARGETS.length; sfx.click(); twUi(); try { localStorage.setItem("ns-twtarget", String(state.twTarget)); } catch (e) {} });
try { const t = localStorage.getItem("ns-twtarget"); if (t !== null) state.twTarget = +t || 0; } catch (e) {}
document.addEventListener("keydown", e => { if ((e.key === "Enter" || e.key === "c" || e.key === "C") && tw && !twSpinning && !e.target.closest("input, textarea, select, button")) { e.preventDefault(); twCash(); } });

function buildInfo() {
  const tot = Object.values(TW_W).reduce((a, b) => a + b, 0), pc = id => (TW_W[id] / tot * 100).toFixed(1).replace(".", ",") + " %";
  const NOTE = { scrap: "", cell: "", chip: "", core: "", relic: "Selten, sehr hoch", crystal: "Füllt den Wappenmesser", wild: "Kran-Sicherung: fängt eine Abrissbirne ab", capsule: "3 in einer Runde: Bauplanauswahl", beacon: `+${TW_FS_AWARD} Freibauten ab Etage ${TW_FS_START}`, warp: "Sofort: Stadtrundfahrt", crash: "Reißt alles ein" };
  $("payRows").innerHTML = ["relic", "core", "chip", "cell", "scrap", "crystal", "wild", "capsule", "beacon", "warp", "crash"].map(id => { const s = twSym(id);
    return `<tr><td>${ICONS[id]}${s.name}</td><td class="pay">${TW_D[id] ? "+" + TW_D[id] : "–"}</td><td class="pay">${pc(id)}</td><td>${NOTE[id]}</td></tr>`; }).join("");
  $("panel-bonus").innerHTML = `
    <div class="feat" style="--fc:#7ee0c8">${ICONS.core}<div><h3>Hochstapeln</h3><p>Eine Runde kostet einmal den Einsatz. Jeder Dreh der kleinen Walze setzt Etagen auf dein Hochhaus. Nach jedem Dreh entscheidest du: weiterbauen oder auszahlen. Die Abrissbirne reißt alles ein.</p></div></div>
    <div class="feat" style="--fc:#ffc94a">${ICONS.wild}<div><h3>Kran-Sicherung</h3><p>Landet der Kran, gibt es eine Etage und eine Sicherung. Die nächste Abrissbirne prallt einfach ab.</p></div></div>
    <div class="feat" style="--fc:#c6f06b">${ICONS.beacon}<div><h3>Baugenehmigung · Freibauten</h3><p>Jede Baugenehmigung bringt ${TW_FS_AWARD} Freibauten. Sie kosten nichts und starten schon auf Etage ${TW_FS_START}.</p></div></div>
    <div class="feat" style="--fc:#4aa8ff">${ICONS.capsule}<div><h3>Bauplan · Bauplanauswahl</h3><p>Sammle 3 Baupläne in einer Runde: Die Bauplanauswahl startet, der Gewinn gehört dir, auch wenn das Haus danach einstürzt.</p></div></div>
    <div class="feat" style="--fc:#ff7a59">${ICONS.warp}<div><h3>Stadtbus · Stadtrundfahrt</h3><p>Selten: Der Stadtbus startet sofort die Stadtrundfahrt am Glücksrad, bis zum 300-fachen Einsatz.</p></div></div>
    <div class="feat" style="--fc:#ffc94a">${ICONS.crystal}<div><h3>Wappen und Bauamt</h3><p>Jede Runde füllt den Wappenmesser ein wenig, jedes Wappen deutlich mehr. Im Bauamt tauschst du Wappen gegen Erlasse für einige Minuten.</p></div></div>
    <div class="feat" style="--fc:#ffc94a">${ICONS.scrap}<div><h3>Paule-Boost</h3><p>Jede Runde ohne Gewinn füllt Paules Glücksladung. Nach ${BOOST_AT} leeren Runden startet die nächste Runde mit zwei Kran-Sicherungen.</p></div></div>
    <div class="feat" style="--fc:#ffc94a">${ICONS.ladder}<div><h3>Risikoleiter</h3><p>Nach einem Gewinn: Steig die Leiter hoch, von ×1 bis ×100. Kassieren geht jederzeit.</p></div></div>
    <div class="feat" style="--fc:#ff7a59">${ICONS.beacon}<div><h3>Signal-Risiko</h3><p>Nach einem Gewinn kannst du ihn verdoppeln: Grün oder Rot raten, genau 50 : 50.</p></div></div>
    <div class="feat" style="--fc:#ffd34a">${ICONS.relic}<div><h3>Stadtschatz</h3><p>Jede Runde legt 1,5 % deines Einsatzes in den Topf, der bei 500 Talern startet. Die Chance pro Runde ist Einsatz ÷ 40.000.</p></div></div>
    <div class="feat" style="--fc:#7ee0c8">${ICONS.up_engine}<div><h3>Aktionen, Viertel und Aufträge</h3><p>Starte Aktionen für deine Stadt, erschließe neue Viertel über deinen Rang und erfülle Aufträge für Taler und XP.</p></div></div>`;
  const rows = [1, 3, 5, 10, 15, 20, 25, 30, 40, 50, 75, 100];
  $("lines").innerHTML = `<div><b>Wert nach Höhe</b> (× Einsatz, vor Boni):</div><table class="pt"><tbody>${rows.map(h => `<tr><td>Höhe ${h}</td><td class="pay">${twFmt(twMult(h))}</td></tr>`).join("")}</tbody></table><p class="note">Ab Höhe ${TW_MAX} wird automatisch ausgezahlt. Auto-Runden zahlen beim gewählten Auto-Ziel aus.</p>`;
}

MISSION_TYPES.symwin.text = m => `Baue ${m.goal}-mal ${BY_ID[m.meta].name}`;
MISSION_TYPES.four.text = () => "Erreiche Höhe 20 in einer Runde";
Object.assign(SYM_HELP, {
  beacon: `Baugenehmigung. Bringt ${TW_FS_AWARD} Freibauten nach dieser Runde, sie starten auf Etage ${TW_FS_START}.`,
  capsule: "Bauplan. 3 in einer Runde starten die Bauplanauswahl.",
  warp: "Stadtbus. Startet sofort die Stadtrundfahrt am Glücksrad.",
  wild: "Kran. +1 Etage und eine Sicherung gegen die nächste Abrissbirne.",
  crash: "Abrissbirne. Reißt das Hochhaus ein, außer eine Kran-Sicherung fängt sie ab.",
});
HELP_RULES.unshift(
  [".tw-strip .sym[data-sym], .sym[data-sym]", el => { const id = el.dataset.sym, x = twSym(id); if (!x) return null;
    return [x.name, TW_D[id] ? `+${TW_D[id]} Etage${TW_D[id] > 1 ? "n" : ""}. ${SYM_HELP[id] || ""}` : (SYM_HELP[id] || "")]; }],
  ["#twCash", () => ["Auszahlen", tw && tw.h ? `Jetzt kassieren: <b>${twAmount()}</b> Taler (${twFmt(twMult(tw.h))}). Danach beginnt eine neue Runde.` : "Geht, sobald mindestens eine Etage steht."]],
  ["#twTarget", () => ["Auto-Ziel", `Auto-Runden zahlen automatisch aus, sobald dieser Wert erreicht ist. Gerade ${twFmt(twTarget())}. Antippen wechselt.`]],
  ["#twStage, #twSvg", () => ["Dein Hochhaus", `Jede Etage erhöht den Wert um 7 %. Höhe ${tw ? tw.h : 0}. Die Abrissbirne reißt alles ein.`]],
  ["#twReel", () => ["Bauwalze", "Eine kleine Walze, ein Feld zählt: das in der Mitte. Leertaste baut weiter, Enter zahlt aus."]],
  [".bay, #frame", () => ["Hochstapler", "Stapeln, bis du auszahlst. Oder bis die Abrissbirne kommt."]],
  ["#fsbar", () => ["Freibauten", `Kostenlose Runden, die schon auf Etage ${TW_FS_START} starten. Noch ${fsLeft}.`]],
);
'''
