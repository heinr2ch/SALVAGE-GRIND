# Neustadt Teil 3: eigenes Grundspiel "Hochstapler" (kleine Walze, Etagen stapeln, auszahlen oder Abriss)

TOWER_HTML = [
    ('''        <div class="bay net col" id="bay">
          <div class="netgrid" id="netGrid" aria-label="Werkbank mit 5 Walzen und 3 Reihen"></div>
          <div class="casc" id="casc" hidden>Rex sammelt <b id="cascN">0</b></div>''',
     '''        <div class="bay tower" id="bay">
          <div class="tw-stage" id="twStage"><svg viewBox="0 0 160 200" preserveAspectRatio="xMidYMax meet" id="twSvg" aria-label="Dein Hochhaus"><g id="twCam"><g id="twFloors"></g><g id="twTop"></g></g><g id="twFx"></g></svg>
            <div class="tw-height"><span>Höhe</span><b id="twH">0</b></div><div class="tw-next10" id="twNext10">Richtfest bei 10</div><div class="tw-mini" id="twMini" hidden></div></div>
          <div class="tw-side">
            <div class="tw-reel" id="twReel" aria-label="Bauwalze"><div class="tw-strip" id="twStrip"></div><i class="tw-line" aria-hidden="true"></i></div>
            <div class="tw-val"><span>Wert</span><b id="twVal">×0</b><small id="twNext">Nächste Etage: ×1,16</small></div>
            <div class="tw-flags"><span class="tw-shield" id="twShield" hidden>Kran-Sicherung <b id="twShieldN">1</b></span><span class="tw-plans" id="twPlans">Baupläne <b id="twPlansN">0</b>/3</span><span class="tw-boom" id="twBoom" hidden>Bauboom <b id="twBoomN">3</b></span><span class="tw-run" id="twRun">Serie <b id="twRunN">0</b>/5</span></div>
            <div class="tw-offer" id="twOffer" hidden></div>
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
.tw-next10 { position: absolute; right: 8px; top: 8px; padding: 4px 9px; border-radius: 9px; background: rgba(8,16,26,.6); font: 700 .62rem var(--f-body); color: #ffd27a; }
.tw-flash { position: absolute; left: 50%; top: 22%; z-index: 9; transform: translate(-50%, 0); display: grid; justify-items: center; gap: 2px; padding: 8px 16px; border-radius: 14px; pointer-events: none; text-align: center;
  background: rgba(8,16,26,.82); box-shadow: 0 0 0 2px var(--fc), 0 0 30px color-mix(in srgb, var(--fc) 50%, transparent); animation: twFlash 1.7s cubic-bezier(.2,1.4,.4,1) forwards; }
.tw-flash b { font: 800 1.15rem var(--f-display); color: var(--fc); letter-spacing: .04em; white-space: nowrap; }
.tw-flash small { font: 700 .72rem var(--f-body); color: #ffffff; }
@keyframes twFlash { 0% { opacity: 0; transform: translate(-50%, 10px) scale(.6); } 15% { opacity: 1; transform: translate(-50%, 0) scale(1.08); } 80% { opacity: 1; transform: translate(-50%, 0) scale(1); } 100% { opacity: 0; transform: translate(-50%, -16px) scale(.96); } }
.tw-boom { color: #1a0a04 !important; background: linear-gradient(180deg, #ffb07a, #ff7a59) !important; animation: twHot 1s ease-in-out infinite; }
.tw-run b { color: #ff9a7a; }
.tw-mini { position: absolute; inset: 0; z-index: 10; background: rgba(6,12,20,.55); backdrop-filter: blur(1.5px); -webkit-backdrop-filter: blur(1.5px); overflow: hidden; touch-action: manipulation; user-select: none; -webkit-user-select: none; cursor: pointer; }
.mg-head { position: absolute; left: 8px; right: 8px; top: 8px; display: grid; gap: 3px; padding: 8px 10px; border-radius: 12px; background: rgba(8,16,26,.85); text-align: center; pointer-events: none; }
.mg-head b { font: 800 1rem var(--f-display); color: #ffd27a; letter-spacing: .04em; }
.mg-head span { font: 600 .7rem var(--f-body); color: #ffffff; }
.mg-time { display: block; height: 4px; border-radius: 3px; background: rgba(255,255,255,.12); overflow: hidden; }
.mg-time i { display: block; height: 100%; width: 100%; background: linear-gradient(90deg, #ff7a59, #ffc94a); }
.mg-guide { position: absolute; left: 50%; top: 30%; bottom: 12%; width: 22%; transform: translateX(-50%); border: 2px dashed rgba(126,224,200,.7); border-radius: 8px; background: rgba(126,224,200,.08); pointer-events: none; }
.mg-block { position: absolute; top: 42%; left: 50%; width: 20%; height: 9%; transform: translateX(-50%); border-radius: 3px; background: repeating-linear-gradient(90deg, #dce6f0 0 8px, #9ad4ff 8px 12px); box-shadow: 0 0 0 2px #2a3a4a, 0 6px 14px rgba(0,0,0,.4); pointer-events: none; }
.mg-block::before { content: ""; position: absolute; left: 50%; bottom: 100%; width: 1px; height: 400px; background: #c9ccd1; }
.mg-block.ok { box-shadow: 0 0 0 2px #7ed957, 0 0 24px #7ed957; }
.mg-block.miss { animation: mgFall .7s ease-in forwards; }
@keyframes mgFall { to { transform: translate(-50%, 260px) rotate(40deg); opacity: 0; } }
.mg-go { position: absolute; left: 50%; bottom: 10px; transform: translateX(-50%); padding: 10px 26px; border: 0; border-radius: 99px; font: 800 .9rem var(--f-display); color: #0c1a14; background: linear-gradient(180deg, #8ff0c8, #3fd0a0); box-shadow: 0 4px 0 #1f8a64; pointer-events: none; }
.mg-brick { position: absolute; top: -12%; width: 16%; aspect-ratio: 2 / 1; border: 0; border-radius: 4px; cursor: pointer; padding: 0;
  background: linear-gradient(180deg, #ffe39a, #e8a83a); box-shadow: inset 0 -3px 0 rgba(0,0,0,.25), 0 0 14px rgba(255,201,74,.6); animation: mgDrop 1.7s linear forwards; }
.mg-brick::after { content: ""; position: absolute; inset: 30% 10%; border-top: 1px solid rgba(122,86,8,.5); border-bottom: 1px solid rgba(122,86,8,.5); }
.mg-brick.got { animation: mgGot .3s ease-out forwards; }
@keyframes mgDrop { to { top: 104%; } }
@keyframes mgGot { to { transform: scale(1.8); opacity: 0; } }
.mg-pigeon { position: absolute; width: 18%; aspect-ratio: 1.4; border: 0; padding: 0; background: rgba(255,255,255,.08); border-radius: 50%; cursor: pointer; transform: translate(-50%, -50%); animation: mgLand .4s cubic-bezier(.3,1.5,.5,1) both; }
.mg-pigeon svg { width: 100%; height: 100%; pointer-events: none; }
.mg-pigeon.gone { animation: mgFly .5s ease-in forwards; }
@keyframes mgLand { from { transform: translate(-50%, -160%) scale(.5); opacity: 0; } }
@keyframes mgFly { to { transform: translate(60%, -260%) scale(.6); opacity: 0; } }
.mg-count { position: absolute; left: 50%; bottom: 10px; transform: translateX(-50%); padding: 4px 12px; border-radius: 99px; background: rgba(8,16,26,.85); font: 700 .8rem var(--f-body); color: #ffffff; pointer-events: none; }
.mg-count b { color: #ffd27a; font-family: var(--f-mono); }
.mg-result { position: absolute; left: 50%; top: 55%; transform: translate(-50%, -50%); padding: 10px 16px; border-radius: 14px; font: 800 .95rem var(--f-display); text-align: center; animation: fsPop .5s cubic-bezier(.2,1.6,.4,1); pointer-events: none; }
.mg-result.good { background: #7ed957; color: #0c1a08; }
.mg-result.bad { background: #ff6b7a; color: #2a0408; }
.tw-offer { display: grid; gap: 6px; padding: 10px; border-radius: 12px; background: linear-gradient(180deg, rgba(126,224,200,.18), rgba(74,168,255,.12)); border: 1px solid #7ee0c8; animation: fsPop .5s cubic-bezier(.2,1.6,.4,1); }
.tw-offer > b { font: 800 .95rem var(--f-display); color: #7ee0c8; }
.tw-offer span { font: 600 .72rem var(--f-body); color: var(--ink); }
.tw-offer em { font: 700 .9rem var(--f-mono); font-style: normal; color: #ffd27a; }
.tw-offer div { display: grid; grid-template-columns: 1fr 1fr; gap: 6px; }
.tw-yes, .tw-no { padding: 8px 6px; border: 0; border-radius: 10px; font: 800 .74rem var(--f-body); cursor: pointer; }
.tw-yes { background: linear-gradient(180deg, #8ff0c8, #3fd0a0); color: #0c1a14; }
.tw-no { background: rgba(255,255,255,.1); color: var(--ink); }
@media (prefers-reduced-motion: reduce) { .tw-flash, .tw-boom { animation-duration: .01s; } }
@media (max-width: 600px) { .bay.tower { gap: 8px; } .tw-stage { min-height: 250px; } .tw-flags span { font-size: .56rem; padding: 2px 6px; } .tw-val { padding: 6px 8px; } .tw-val small { font-size: .56rem; } .tw-val b { font-size: 1.25rem; } .tw-cash { padding: 8px; } .tw-cash b { font-size: 1rem; } .tw-reel { --twc: 52px; } }
@media (prefers-reduced-motion: reduce) { .car, .rotor, .tw-crane .hook, .tw-cash.hot { animation: none; } }
'''

TOWER_JS = r'''
/* ===================== Neustadt: Hochstapler (kleine Walze, Etagen stapeln) =====================
   Pro Runde zahlst du einmal den Einsatz. Jeder Dreh der kleinen Walze setzt Etagen auf dein Hochhaus, der Wert steigt.
   Du entscheidest nach jedem Dreh: weiterbauen oder auszahlen. Die Abrissbirne reißt alles ein (außer eine Kran-Sicherung fängt sie ab).
   Wert = 1,1 × 1,07^Höhe (Höhe 1: ×1,18 · 10: ×2,2 · 25: ×6 · 50: ×32 · 100: ×954, dann wird automatisch ausgezahlt).
   Dazu: Richtfest alle 10 Etagen (Sofortbonus), Bauboom (5 Bausteine in Folge: 3 Drehs je +1 Etage), Investor (Kaufangebot +30 %),
   Mini-Events mit Geschicklichkeit (Kran-Timing, Ziegelregen, Tauben-Alarm).
   Balance per Simulation (tools/sim/hochstapler.js): je nach Ausstiegsstrategie etwa 97 bis 129 % (mutiges Bauen lohnt sich etwas mehr). */
const TW_W = { scrap: 30, cell: 22, chip: 16, core: 8, relic: 1.6, crystal: 5, wild: 2.5, capsule: 2.5, beacon: .3, warp: .1, crash: 20 };
const TW_D = { scrap: 1, cell: 1, chip: 2, core: 3, relic: 6, crystal: 1, wild: 1, capsule: 0, beacon: 0, warp: 0, crash: 0 };
const TW_RF = [.5, .75, 1, 1.5, 2, 2.5, 3, 4, 5, 6], TW_EVENT_P = .06, TW_INVEST_P = .025, TW_INVEST_F = 1.3, TW_BOOM_AT = 5;
const TW_C = 1.1, TW_G = 1.07, TW_MAX = 100, TW_FS_START = 3, TW_FS_AWARD = 3, TW_TARGETS = [1.5, 2, 3, 5, 10, 25];
const CRASH_SYM = { id: "crash", name: "Abrissbirne", w: 0, pay: null, special: "#ff4b5c" };
BY_ID.crash = CRASH_SYM;
const twSym = id => id === "wild" ? WILD : BY_ID[id];
const twMult = h => h <= 0 ? 0 : TW_C * Math.pow(TW_G, Math.min(h, TW_MAX));
const twFmt = m => "×" + String(m >= 100 ? Math.round(m) : m >= 10 ? m.toFixed(1) : m.toFixed(2)).replace(".", ",");
let twMiniKey = null, tw = null, twHold = false, twSpinning = false, twFast = false, netCascading = false, colRun = null;
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
  const top = 188 - floors.length * 10, ct = Math.min(140, top - 30), mx = 132;
  let lattice = ""; for (let y = 186; y > ct + 6; y -= 8) lattice += `M${mx - 3},${y} L${mx + 3},${y - 8} M${mx + 3},${y} L${mx - 3},${y - 8} `;
  const hookY = Math.max(ct + 10, top - 14), shield = tw && tw.shield;
  $("twTop").innerHTML = `<g class="tw-crane">
    <rect x="${mx - 8}" y="184" width="16" height="4" fill="#5a5f66"/>
    <path d="M${mx - 3},188 V${ct} M${mx + 3},188 V${ct}" stroke="#ffc94a" stroke-width="1.6"/><path d="${lattice}" stroke="#e8a83a" stroke-width=".7"/>
    <path d="M${mx - 4},${ct} L${mx},${ct - 10} L${mx + 4},${ct} Z" fill="#ffc94a"/>
    <path d="M44,${ct} H${mx + 22}" stroke="#ffc94a" stroke-width="2.4"/><path d="M48,${ct} L${mx},${ct - 10} L${mx + 20},${ct}" stroke="#e8a83a" stroke-width=".8" fill="none"/>
    <rect x="${mx + 10}" y="${ct + 1}" width="12" height="7" fill="#6a6f76"/>
    <rect x="${mx - 9}" y="${ct + 1}" width="9" height="7" rx="1" fill="#ffffff" stroke="#5a5f66" stroke-width=".6"/><rect x="${mx - 8}" y="${ct + 2}" width="5" height="3" fill="#9ad4ff"/>
    <rect x="76" y="${ct + 1}" width="8" height="3" fill="#5a5f66"/>
    <g class="hook"><path d="M80,${ct + 4} V${hookY}" stroke="#c9ccd1" stroke-width=".8"/><rect x="${80 - 13}" y="${hookY}" width="26" height="6" fill="${shield ? "#ffd27a" : "#c8b088"}" stroke="${shield ? "#a87a10" : "#6a5a3a"}" stroke-width=".7"/><path d="M${80 - 13},${hookY + 3} h26" stroke="rgba(0,0,0,.2)" stroke-width=".6"/></g>
    ${shield ? `<g transform="translate(${mx - 10} ${ct - 22})"><path d="M0 9 q10 -14 20 0z" fill="#ffd27a" stroke="#a87a10" stroke-width="1"/><path d="M-2 9 h24" stroke="#a87a10" stroke-width="1.8"/></g>` : ""}</g>`;
  const shift = Math.max(0, floors.length * 10 - 96);
  cam.setAttribute("transform", `translate(0 ${shift})`);
  $("twH").textContent = tw ? tw.h : 0;
}
function twUi() {
  const v = tw ? twMult(tw.h) : 0, nextM = twMult((tw ? tw.h : 0) + 1);
  const vb = $("twVal"); vb.textContent = tw && tw.h ? twFmt(v) : "×0";
  $("twNext").textContent = tw && tw.h ? `Auszahlen: ${twAmount()} · nächste Etage ${twFmt(nextM)}` : `Erste Etage: ${twFmt(twMult(1))}`;
  $("twShield").hidden = !(tw && tw.shield); $("twShieldN").textContent = tw ? tw.shield : 0;
  $("twPlansN").textContent = tw ? tw.plans : 0;
  $("twBoom").hidden = !(tw && tw.boom); $("twBoomN").textContent = tw ? tw.boom : 0;
  $("twRun").hidden = !!(tw && tw.boom); $("twRunN").textContent = tw ? tw.run : 0;
  const nx = (Math.floor((tw ? tw.h : 0) / 10) + 1) * 10;
  $("twNext10").textContent = nx <= TW_MAX ? `Richtfest bei ${nx}: +${Math.max(1, Math.round((tw ? tw.bet : bet()) * TW_RF[Math.min(nx / 10 - 1, TW_RF.length - 1)]))}` : "Höchste Höhe";
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
  tw = { h: free ? TW_FS_START : 0, shield: 0, plans: 0, floors: free ? Array(TW_FS_START).fill("scrap") : [], free, bet: free ? (tw && tw.bet) || bet() : bet(), spins: 0, bonus: 0, fsGain: 0, saved: 0, dust: 2, boost: false, run: 0, boom: 0 };
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
  const sym = twSym(id), h0 = tw.h;
  let d = TW_D[id], boomed = false;
  if (d && tw.boom > 0) { d += 1; tw.boom--; boomed = true; }
  if (d) tw.run++; else tw.run = 0;
  for (let i = 0; i < d; i++) tw.floors.push(id);
  tw.h += d;
  if (id === "wild") { tw.shield = Math.min(1, tw.shield + 1); }
  if (id === "crystal") tw.dust += 6;
  if (d) { track("symwin", 1, id); if (tw.h >= 20 && tw.h - d < 20) track("four"); }
  twDraw(); twUi(); render();
  const vb = $("twVal"); vb.classList.remove("up"); void vb.offsetWidth; if (d) vb.classList.add("up");
  if (d) { sfx.coin(Math.min(3, d)); twFloat(`+${d} ${d === 1 ? "Etage" : "Etagen"}`, `${sym.name}${boomed ? " · Bauboom" : ""} · ${twFmt(twMult(tw.h))}`, boomed ? "#ff7a59" : sym.color || sym.special || "#7ee0c8"); }
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
  await twMilestones(h0);
  if (tw.run >= TW_BOOM_AT && !tw.boom) {
    tw.boom = 3; tw.run = 0; sfx.mult(); twFlash("BAUBOOM!", "3 Drehs: je +1 Etage extra", "#ff7a59"); bipState.last = 0; bip("boom", 2);
    $("msg").className = "msg gold"; $("msg").textContent = "Bauboom! Fünf Bausteine in Folge: Die nächsten 3 Bausteine bringen je eine Etage extra.";
  }
  twUi();
  if (tw.h >= TW_MAX) { $("msg").textContent = "Wolkenkratzer fertig! Höchste Höhe erreicht."; return twCash(true); }
  if (tw.h >= 2 && Math.random() < TW_EVENT_P) { await twMiniEvent(); if (!tw) return; }
  if (tw.h >= 5 && Math.random() < TW_INVEST_P) { const sold = await twInvestor(); if (sold || !tw) return; }
  return twAfterStep();
}
async function twMilestones(h0) {
  // Richtfest alle 10 Etagen: Sofortbonus, bleibt auch bei Abriss
  for (let k = Math.floor(h0 / 10) + 1; k <= Math.floor(Math.min(tw.h, TW_MAX) / 10); k++) {
    const amt = Math.max(1, Math.round(tw.bet * TW_RF[Math.min(k - 1, TW_RF.length - 1)]));
    state.credits += amt; tw.bonus += amt; countCredits(state.credits, 500);
    sfx.fanfare(0); twFlash(`Richtfest! Etage ${k * 10}`, `+${amt} Taler sofort`, "#ffc94a"); burstAt($("twStage"), 60, ["#ffc94a", "#ff7a59", "#7ee0c8", "#ffffff"], 1);
    addLog("relic", `Richtfest Etage ${k * 10}`, "+" + amt, "#ffc94a");
    bipState.last = 0; bip("richtfest", 2);
    await wait(650 * T());
  }
}
function twFlash(title, sub, color) {
  const st = $("twStage"), f = document.createElement("div"); f.className = "tw-flash"; f.style.setProperty("--fc", color);
  f.innerHTML = `<b>${title}</b><small>${sub}</small>`; st.appendChild(f); setTimeout(() => f.remove(), 1700);
}

/* ----- Mini-Events: kurze Geschicklichkeitsspiele ----- */
function mgOverlay(title, sub, ms) {
  const m = $("twMini"); m.hidden = false; m.className = "tw-mini";
  m.innerHTML = `<div class="mg-head"><b>${title}</b><span>${sub}</span><i class="mg-time"><i id="mgBar"></i></i></div>`;
  const bar = $("mgBar"); bar.style.transition = "none"; bar.style.width = "100%"; void bar.offsetWidth; bar.style.transition = `width ${ms}ms linear`; bar.style.width = "0%";
  return m;
}
function mgClose(text, good) {
  const m = $("twMini"); twMiniKey = null;
  m.insertAdjacentHTML("beforeend", `<div class="mg-result ${good ? "good" : "bad"}">${text}</div>`);
  return wait(1100).then(() => { m.hidden = true; m.innerHTML = ""; });
}
function mgCrane() {
  const ms = 5000, m = mgOverlay("Kran-Timing", "Tippe, wenn der Block genau über dem Haus schwebt!", ms);
  m.insertAdjacentHTML("beforeend", `<i class="mg-guide"></i><div class="mg-block" id="mgBlock"></div><button type="button" class="mg-go" id="mgGo">Jetzt!</button>`);
  const blk = $("mgBlock");
  return new Promise(res => {
    const t0 = performance.now(), sp = .0034 + Math.random() * .0016; let done = false, raf = 0;
    const pos = now => Math.sin((now - t0) * sp);
    const finish = p => { if (done) return; done = true; cancelAnimationFrame(raf); const d = p === null ? 9 : Math.abs(p); const r = d < .1 ? 3 : d < .28 ? 1 : 0; blk.classList.add(r ? "ok" : "miss"); res(r); };
    const frame = now => { if (done) return; blk.style.left = (50 + pos(now) * 40) + "%"; if (now - t0 > ms) finish(null); else raf = requestAnimationFrame(frame); };
    m.addEventListener("pointerdown", e => { e.preventDefault(); finish(pos(performance.now())); }, { once: true });
    twMiniKey = () => finish(pos(performance.now()));
    raf = requestAnimationFrame(frame);
  });
}
function mgBricks() {
  const ms = 4300, N = 7, m = mgOverlay("Ziegelregen", "Fang die goldenen Ziegel, bevor sie unten sind!", ms);
  let caught = 0;
  return new Promise(res => {
    for (let i = 0; i < N; i++) setTimeout(() => {
      if (m.hidden) return;
      const b = document.createElement("button"); b.type = "button"; b.className = "mg-brick"; b.setAttribute("aria-label", "Ziegel fangen");
      b.style.left = (8 + Math.random() * 76) + "%"; b.style.animationDuration = (1.5 + Math.random() * .5) + "s";
      b.addEventListener("pointerdown", e => { e.preventDefault(); e.stopPropagation(); if (b.classList.contains("got")) return; b.classList.add("got"); caught++; sfx.coin(1); $("mgCount").textContent = caught; setTimeout(() => b.remove(), 300); });
      b.addEventListener("animationend", () => b.remove());
      m.appendChild(b);
    }, 150 + i * 480);
    m.insertAdjacentHTML("beforeend", `<div class="mg-count">Gefangen: <b id="mgCount">0</b></div>`);
    setTimeout(() => res(caught), ms);
  });
}
function mgPigeons() {
  const ms = 3800, N = 5, m = mgOverlay("Tauben-Alarm", "Verscheuch alle Tauben vom Dach! Tipp sie an.", ms);
  let left = N, done = false;
  return new Promise(res => {
    for (let i = 0; i < N; i++) {
      const b = document.createElement("button"); b.type = "button"; b.className = "mg-pigeon"; b.setAttribute("aria-label", "Taube verscheuchen");
      b.style.left = (10 + Math.random() * 72) + "%"; b.style.top = (30 + Math.random() * 45) + "%"; b.style.animationDelay = (i * .12) + "s";
      b.innerHTML = `<svg viewBox="-20 -14 40 28">${DRONE.replace('class="drone"', "")}</svg>`;
      b.addEventListener("pointerdown", e => { e.preventDefault(); e.stopPropagation(); if (b.classList.contains("gone")) return; b.classList.add("gone"); sfx.squeak(1.3); left--; if (!left && !done) { done = true; res(true); } });
      m.appendChild(b);
    }
    setTimeout(() => { if (!done) { done = true; res(false); } }, ms);
  });
}
async function twMiniEvent() {
  twHold = true; twUi();
  const kind = (Math.random() * 3) | 0, auto = autoLeft > 0;
  bipState.last = 0; bip("mini", 3); sfx.alarm();
  await wait(300);
  if (kind === 0) {
    const r = auto ? 1 : await mgCrane();
    if (r) { for (let i = 0; i < r; i++) tw.floors.push("chip"); const h0 = tw.h; tw.h += r; twDraw(); sfx.mult(); if (!auto) await mgClose(r === 3 ? "Perfekt! +3 Etagen" : "Gut! +1 Etage", true); await twMilestones(h0); }
    else if (!auto) await mgClose("Daneben! Der Block landet im Container.", false);
    $("msg").className = "msg gold"; $("msg").textContent = r ? `Kran-Timing: +${r} Etage${r > 1 ? "n" : ""}. Wert ${twFmt(twMult(tw.h))}.` : "Kran-Timing verpasst.";
  } else if (kind === 1) {
    const c = auto ? 3 : await mgBricks();
    const amt = Math.round(tw.bet * .3 * c);
    if (amt) { state.credits += amt; tw.bonus += amt; countCredits(state.credits, 500); addLog("scrap", `Ziegelregen ×${c}`, "+" + amt, "#ffc94a"); }
    if (!auto) await mgClose(c ? `${c} Ziegel gefangen: +${amt} Taler` : "Kein Ziegel gefangen.", c > 0);
    $("msg").className = "msg gold"; $("msg").textContent = `Ziegelregen: ${c} gefangen, +${amt} Taler sofort.`;
  } else {
    const ok = auto ? Math.random() < .6 : await mgPigeons();
    if (ok) { tw.shield = Math.min(1, tw.shield + 1); tw.floors.push("wild"); const h0 = tw.h; tw.h += 1; twDraw(); sfx.crystal(); if (!auto) await mgClose("Alle weg! +1 Etage und eine Kran-Sicherung", true); await twMilestones(h0); }
    else if (!auto) await mgClose("Die Tauben bleiben sitzen. Gurr.", false);
    $("msg").className = "msg gold"; $("msg").textContent = ok ? "Tauben verscheucht: +1 Etage und eine Kran-Sicherung." : "Tauben-Alarm verloren.";
  }
  if (!auto) { const m = $("twMini"); m.hidden = true; m.innerHTML = ""; }
  bump("minis"); twHold = false; twMiniKey = null; twUi(); render();
}
function twInvestor() {
  const amount = Math.round(twAmount() * TW_INVEST_F);
  if (autoLeft > 0) { if (twMult(tw.h) * TW_INVEST_F >= twTarget()) { twFlash("Investor kauft!", `+${amount} Taler`, "#7ee0c8"); return twCash(false, amount).then(() => true); } return Promise.resolve(false); }
  twHold = true; twUi(); sfx.feature(0, 3); bipState.last = 0; bip("investor", 3);
  const o = $("twOffer"); o.hidden = false;
  o.innerHTML = `<b>Investor!</b><span>Bietet <em>${amount}</em> Taler für dein Haus, 30 % über Wert.</span><div><button type="button" class="tw-yes" id="offYes">Verkaufen</button><button type="button" class="tw-no" id="offNo">Weiterbauen</button></div><i class="mg-time"><i id="offBar"></i></i>`;
  const bar = $("offBar"); bar.style.width = "100%"; void bar.offsetWidth; bar.style.transition = "width 7s linear"; bar.style.width = "0%";
  return new Promise(res => {
    let done = false;
    const end = async yes => { if (done) return; done = true; o.hidden = true; o.innerHTML = ""; twHold = false; twMiniKey = null;
      if (yes) { await twCash(false, amount); res(true); } else { $("msg").className = "msg"; $("msg").textContent = "Angebot abgelehnt. Weiterbauen!"; twUi(); res(false); } };
    $("offYes").addEventListener("click", () => end(true)); $("offNo").addEventListener("click", () => end(false));
    twMiniKey = () => end(false);
    setTimeout(() => end(false), 7000);
  });
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
async function twCash(maxed, offer) {
  if (!tw || tw.h <= 0 || twSpinning || (twHold && !offer)) return;
  twHold = true;
  const amt = offer || twAmount(), h = tw.h;
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
  if (twMiniKey) { twMiniKey(); return; }
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
    <div class="feat" style="--fc:#ffc94a">${ICONS.relic}<div><h3>Richtfest</h3><p>Alle 10 Etagen gibt es sofort einen Bonus, der dir bleibt, auch wenn das Haus danach einstürzt.</p></div></div>
    <div class="feat" style="--fc:#ff7a59">${ICONS.core}<div><h3>Bauboom</h3><p>Fünf Bausteine in Folge ohne Pause starten den Bauboom: Die nächsten 3 Bausteine bringen je eine Etage extra.</p></div></div>
    <div class="feat" style="--fc:#7ee0c8">${ICONS.chip}<div><h3>Investor</h3><p>Ab Etage 5 klopft manchmal ein Investor an und bietet 30 % mehr als den aktuellen Wert. Verkaufen oder weiterbauen?</p></div></div>
    <div class="feat" style="--fc:#4aa8ff">${ICONS.wild}<div><h3>Mini-Events</h3><p>Ab und zu passiert etwas auf der Baustelle: <b>Kran-Timing</b> (tippen, wenn der Block über dem Haus ist: bis +3 Etagen), <b>Ziegelregen</b> (goldene Ziegel fangen: Taler sofort) und <b>Tauben-Alarm</b> (alle Tauben verscheuchen: Etage plus Kran-Sicherung).</p></div></div>
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
