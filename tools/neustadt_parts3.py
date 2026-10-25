# Neustadt Teil 3: eigenes Grundspiel "Stadtrundfahrt" (Brettspiel: würfeln, Stadtbus fährt, Grundstücke kaufen, Miete kassieren)
# Ersetzt seit Neustadt 0.3.0 den Hochstapler. Balance: tools/sim/stadtrundfahrt.js

BOARD_HTML = [
    ('''        <div class="bay net col" id="bay">
          <div class="netgrid" id="netGrid" aria-label="Werkbank mit 5 Walzen und 3 Reihen"></div>
          <div class="casc" id="casc" hidden>Rex sammelt <b id="cascN">0</b></div>''',
     '''        <div class="bay board" id="bay">
          <div class="bd-board" id="bdBoard" aria-label="Spielbrett der Stadtrundfahrt">
            <div class="bd-mid">
              <div class="bd-title"><b>Stadtrundfahrt</b><span id="bdSub">Würfeln und losfahren</span></div>
              <div class="bd-dice" id="bdDice" aria-label="Würfel"><i class="die" id="bdD1"></i><i class="die" id="bdD2"></i></div>
              <div class="bd-total"><span>Diese Fahrt</span><b id="bdTotal">0</b></div>
              <div class="bd-chips"><span id="bdPlansBox">Baupläne <b id="bdPlans">0</b>/5</span><span id="bdParkBox">Parkkasse <b id="bdPark">0</b></span></div>
              <div class="bd-card" id="bdCard" hidden></div>
            </div>
            <div class="bd-bus" id="bdBus" aria-hidden="true"></div>
            <div class="tw-mini" id="twMini" hidden></div>
          </div>
          <div class="bd-side">
            <div class="bd-info" id="bdInfo"></div>
            <button type="button" class="tw-cash bd-buy" id="bdBuy" hidden><span id="bdBuyLbl">Kaufen</span><b id="bdBuyAmt">0</b></button>
            <button type="button" class="tw-target bd-auto" id="bdAuto">Auto-Bauen: aus</button>
            <div class="bd-dists" id="bdDists"></div>
          </div>
          <div class="casc" id="casc" hidden>Feld <b id="cascN">0</b></div>'''),
    ('<span><b id="fsLeft">0</b> übrig · Rex <b id="fsStick">0</b>/4 · Sammler <em class="fsmult" id="fsMultBox">×<b id="fsMult">1</b></em> · bisher <b id="fsWin">0</b></span>',
     '<span><b id="fsLeft">0</b> übrig · alle Gewinne <em class="fsmult" id="fsMultBox">×<b id="fsMult">2</b></em><b id="fsStick" hidden>0</b> · bisher <b id="fsWin">0</b></span>'),
    ('<th>Teil</th><th>3 Walzen</th><th>4 Walzen</th><th>5 Walzen</th>', '<th>Viertel</th><th>Felder</th><th>Kaufen und Ausbauen</th><th>Miete je Halt</th>'),
    ('aria-controls="panel-lines">Wege</button>', 'aria-controls="panel-lines">Würfel</button>'),
]

BOARD_CSS = r'''
/* ---------- Neustadt: Stadtrundfahrt (Spielbrett) ---------- */
.frame { grid-template-columns: minmax(0, 1fr); width: min(100%, 680px); margin: 0 auto; }
.bay.board { display: grid; grid-template-columns: minmax(0, 1.6fr) minmax(0, 1fr); gap: 12px; align-items: start; position: relative; min-height: 0; }
.bd-board { position: relative; display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); grid-template-rows: repeat(6, minmax(0, 1fr)); gap: 3px; aspect-ratio: 1; padding: 6px; border-radius: 14px; min-width: 0;
  background: radial-gradient(circle at 50% 45%, #355a46, #1d3328 72%); box-shadow: inset 0 0 0 1px rgba(255,255,255,.08), 0 10px 30px rgba(0,0,0,.35); }
.bd-f { position: relative; display: grid; place-items: center; align-content: center; gap: 0; min-width: 0; min-height: 0; padding: 0; border: 0; border-radius: 7px; overflow: hidden; cursor: pointer;
  background: #ece6d6; color: #1c2430; font: inherit; box-shadow: inset 0 -2px 0 rgba(0,0,0,.12); transition: box-shadow .2s, transform .2s; }
.bd-f:focus-visible { outline: 2px solid #ffffff; outline-offset: 1px; }
.bd-f svg { width: 78%; height: auto; display: block; }
.bd-f.bd-plot svg { width: 86%; margin-top: 14%; }
.bd-strip { position: absolute; left: 0; right: 0; top: 0; height: 15%; }
.bd-pips { position: absolute; left: 0; right: 0; bottom: 4%; display: flex; justify-content: center; gap: 2px; }
.bd-pips b { width: 9%; aspect-ratio: 1; border-radius: 50%; background: rgba(0,0,0,.15); }
.bd-pips b.on { background: var(--dc); box-shadow: 0 0 0 1px rgba(0,0,0,.35); }
.bd-f small { font: 800 clamp(.42rem, 1.5vw, .58rem) var(--f-body); letter-spacing: .02em; color: #2a3440; line-height: 1; margin-top: 1px; white-space: nowrap; }
.bd-f .bd-ic { display: grid; place-items: center; width: 64%; }
.bd-f .bd-ic svg { width: 100%; }
.bd-start, .bd-mini, .bd-park, .bd-office { background: #f6f0de; }
.bd-start { background: linear-gradient(160deg, #d8fff0, #b6ecd8); }
.bd-office { background: linear-gradient(160deg, #f0ffd0, #d8f0a8); }
.bd-park { background: linear-gradient(160deg, #e0f8d0, #bfe8a8); }
.bd-mini { background: repeating-linear-gradient(135deg, #ffe39a 0 8px, #f6f0de 8px 16px); }
.bd-news { background: #f4f4f4; }
.bd-f.here { box-shadow: 0 0 0 2px #ffffff, 0 0 16px rgba(255,255,255,.55); z-index: 2; }
.bd-f.sel:not(.here) { box-shadow: 0 0 0 2px var(--dc, #7ee0c8); }
.bd-f.can { animation: bdCan 1.1s ease-in-out infinite; }
@keyframes bdCan { 50% { box-shadow: 0 0 0 2px #ffffff, 0 0 22px #7ee0c8; } }
.bd-f.new svg { animation: bdNew .6s cubic-bezier(.3,1.6,.5,1); transform-origin: 50% 100%; }
@keyframes bdNew { from { transform: scale(.2) translateY(20px); opacity: 0; } }
.bd-f.flash { animation: bdFl .5s ease-out; }
@keyframes bdFl { 40% { transform: scale(1.12); box-shadow: 0 0 0 2px #ffd34a, 0 0 20px #ffd34a; } }
.bd-mid { grid-area: 2 / 2 / 6 / 6; position: relative; display: grid; align-content: center; justify-items: center; gap: 6%; padding: 6%; border-radius: 12px; min-width: 0; min-height: 0;
  background: radial-gradient(circle at 50% 40%, rgba(255,255,255,.08), transparent 70%); }
.bd-title { display: grid; justify-items: center; gap: 1px; text-align: center; }
.bd-title b { font: 800 clamp(.8rem, 2.6vw, 1.05rem) var(--f-display); color: #ffd27a; letter-spacing: .04em; }
.bd-title span { font: 600 clamp(.56rem, 1.8vw, .7rem) var(--f-body); color: rgba(255,255,255,.75); min-height: 1.2em; }
.bd-dice { display: flex; gap: 10%; width: 62%; justify-content: center; }
.die { position: relative; width: 44%; aspect-ratio: 1; border-radius: 18%; background: linear-gradient(160deg, #ffffff, #e2e2e2); box-shadow: inset 0 -3px 0 rgba(0,0,0,.15), 0 4px 10px rgba(0,0,0,.35);
  display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: repeat(3, 1fr); padding: 14%; gap: 4%; }
.die b { border-radius: 50%; }
.die b.on { background: #1c2430; }
.die.dbl { box-shadow: inset 0 -3px 0 rgba(0,0,0,.15), 0 0 0 2px #ffc94a, 0 0 18px #ffc94a; }
.die.roll { animation: bdRoll .18s linear infinite; }
@keyframes bdRoll { 25% { transform: rotate(12deg) translateY(-3px); } 75% { transform: rotate(-12deg) translateY(-1px); } }
.bd-total { display: grid; justify-items: center; line-height: 1.05; }
.bd-total span { font: 700 .55rem var(--f-body); letter-spacing: .14em; text-transform: uppercase; color: rgba(255,255,255,.6); }
.bd-total b { font: 700 clamp(1.05rem, 3.6vw, 1.45rem) var(--f-mono); color: #ffffff; background: none; border: 0; padding: 0; box-shadow: none; min-width: 0; }
.bd-total b.up { animation: twUp .45s cubic-bezier(.3,1.6,.5,1); color: var(--win); }
@keyframes twUp { 40% { transform: scale(1.18); } }
.bd-chips { display: flex; flex-wrap: wrap; justify-content: center; gap: 4px; }
.bd-chips span { padding: 2px 7px; border-radius: 99px; background: rgba(0,0,0,.3); font: 700 clamp(.5rem, 1.6vw, .62rem) var(--f-body); color: rgba(255,255,255,.8); white-space: nowrap; }
.bd-chips b { color: #ffd27a; font-family: var(--f-mono); }
.bd-chips span.hot { background: #4aa8ff; color: #06121e; }
.bd-chips span.hot b { color: #06121e; }
.bd-bus { position: absolute; left: 0; top: 0; z-index: 5; width: 13%; pointer-events: none; transform: translate(-50%, -78%); transition: left .14s ease-out, top .14s ease-out; filter: drop-shadow(0 3px 3px rgba(0,0,0,.45)); }
.bd-bus svg { display: block; width: 100%; height: auto; }
.bd-bus.left svg { transform: scaleX(-1); }
.bd-bus.hop svg { animation: bdHop .14s ease-out; }
@keyframes bdHop { 50% { translate: 0 -18%; } }
.bd-bus.slow { transition-duration: .35s; }
.bd-pop { position: absolute; z-index: 6; transform: translate(-50%, -50%); pointer-events: none; display: grid; justify-items: center; padding: 2px 7px; border-radius: 9px; background: rgba(8,16,26,.85);
  font: 800 .82rem var(--f-mono); color: var(--fc, #7ee0c8); white-space: nowrap; box-shadow: 0 0 0 1px var(--fc, #7ee0c8); animation: bdPop 1.4s cubic-bezier(.2,1.2,.4,1) forwards; }
.bd-pop small { font: 700 .56rem var(--f-body); color: #ffffff; }
@keyframes bdPop { 0% { opacity: 0; transform: translate(-50%, -30%) scale(.6); } 15% { opacity: 1; transform: translate(-50%, -60%) scale(1.08); } 75% { opacity: 1; transform: translate(-50%, -110%) scale(1); } 100% { opacity: 0; transform: translate(-50%, -150%); } }
.bd-card { position: absolute; inset: 4%; z-index: 7; display: grid; align-content: center; justify-items: center; gap: 4px; padding: 10px; border-radius: 10px; text-align: center; cursor: pointer;
  background: #f7f3e8; color: #1c2430; box-shadow: 0 0 0 2px var(--fc, #4aa8ff), 0 12px 30px rgba(0,0,0,.5); }
.bd-card.in { animation: bdCard .45s cubic-bezier(.2,1.5,.4,1); }
@keyframes bdCard { from { transform: rotate(-8deg) scale(.4); opacity: 0; } }
.bd-card small { font: 800 .58rem var(--f-body); letter-spacing: .2em; text-transform: uppercase; color: #6a7480; border-bottom: 2px solid #1c2430; padding-bottom: 2px; }
.bd-card b { font: 800 clamp(.82rem, 2.8vw, 1.05rem) var(--f-display); color: #1c2430; line-height: 1.15; }
.bd-card span { font: 600 clamp(.62rem, 2vw, .76rem) var(--f-body); color: #3a4450; }
.bd-card em { font: 800 1rem var(--f-mono); font-style: normal; color: var(--fc, #2f8a4a); }
.bd-side { display: grid; gap: 9px; align-content: start; min-width: 0; }
.bd-info { display: grid; gap: 5px; padding: 10px; border-radius: 12px; background: rgba(0,0,0,.25); border: 1px solid var(--line); min-height: 128px; align-content: start; }
.bd-ih { display: flex; align-items: center; gap: 7px; }
.bd-ih i { width: 10px; height: 10px; border-radius: 3px; background: var(--dc, #7ee0c8); flex: none; }
.bd-ih b { font: 800 .9rem var(--f-display); color: var(--ink); }
.bd-ih span { margin-left: auto; font: 700 .6rem var(--f-body); color: var(--dc, #7ee0c8); text-transform: uppercase; letter-spacing: .08em; }
.bd-info p { margin: 0; font: 600 .72rem/1.35 var(--f-body); color: var(--ink-soft); }
.bd-info dl { margin: 0; display: grid; grid-template-columns: auto 1fr; gap: 2px 10px; font: 600 .7rem var(--f-body); }
.bd-info dt { color: var(--ink-soft); }
.bd-info dd { margin: 0; text-align: right; font-family: var(--f-mono); color: var(--ink); }
.bd-info .full { color: #ffd27a; font-weight: 800; }
.tw-cash { display: grid; gap: 1px; padding: 10px; border-radius: 12px; border: 0; cursor: pointer; font: 800 .82rem var(--f-display); letter-spacing: .06em; text-transform: uppercase;
  color: #0c1a14; background: linear-gradient(180deg, #8ff0c8, #3fd0a0); box-shadow: 0 4px 0 #1f8a64, 0 8px 20px rgba(63,208,160,.25); transition: transform .08s, filter .15s; }
.tw-cash b { font: 700 1.15rem var(--f-mono); }
.tw-cash:active:not(:disabled) { transform: translateY(2px); box-shadow: 0 2px 0 #1f8a64; }
.tw-cash:disabled { cursor: default; filter: grayscale(.8) brightness(.6); box-shadow: none; }
.tw-cash.hot { animation: twHot 1.2s ease-in-out infinite; }
@keyframes twHot { 50% { filter: brightness(1.2); box-shadow: 0 4px 0 #1f8a64, 0 0 26px rgba(63,208,160,.6); } }
.bd-buy span { font-size: .72rem; }
.tw-target { justify-self: start; padding: 4px 10px; border-radius: 99px; border: 1px solid var(--line); background: rgba(0,0,0,.2); color: var(--ink-soft); font: 700 .64rem var(--f-body); cursor: pointer; }
.bd-auto.on { background: #3fd0a0; border-color: #3fd0a0; color: #0c1a14; }
.bd-dists { display: grid; gap: 4px; }
.bd-dists div { display: grid; grid-template-columns: 10px minmax(0, 1fr) auto auto; align-items: center; gap: 7px; padding: 4px 8px; border-radius: 9px; background: rgba(255,255,255,.04); font: 700 .66rem var(--f-body); color: var(--ink); }
.bd-dists div > i { width: 10px; height: 10px; border-radius: 3px; background: var(--dc); }
.bd-dists span { display: flex; gap: 3px; }
.bd-dists span b { width: 14px; height: 7px; border-radius: 2px; background: rgba(255,255,255,.1); }
.bd-dists span b.l1 { background: color-mix(in srgb, var(--dc) 40%, transparent); }
.bd-dists span b.l2 { background: color-mix(in srgb, var(--dc) 60%, transparent); }
.bd-dists span b.l3 { background: color-mix(in srgb, var(--dc) 80%, transparent); }
.bd-dists span b.l4 { background: var(--dc); }
.bd-dists em { font: 800 .6rem var(--f-mono); font-style: normal; color: #ffd27a; }
.tw-flash { position: absolute; left: 50%; top: 30%; z-index: 9; transform: translate(-50%, 0); display: grid; justify-items: center; gap: 2px; padding: 8px 16px; border-radius: 14px; pointer-events: none; text-align: center;
  background: rgba(8,16,26,.86); box-shadow: 0 0 0 2px var(--fc), 0 0 30px color-mix(in srgb, var(--fc) 50%, transparent); animation: twFlash 1.7s cubic-bezier(.2,1.4,.4,1) forwards; }
.tw-flash b { font: 800 1.15rem var(--f-display); color: var(--fc); letter-spacing: .04em; white-space: nowrap; }
.tw-flash small { font: 700 .72rem var(--f-body); color: #ffffff; }
@keyframes twFlash { 0% { opacity: 0; transform: translate(-50%, 10px) scale(.6); } 15% { opacity: 1; transform: translate(-50%, 0) scale(1.08); } 80% { opacity: 1; transform: translate(-50%, 0) scale(1); } 100% { opacity: 0; transform: translate(-50%, -16px) scale(.96); } }
.bd-board.shake { animation: shake .5s cubic-bezier(.36,.07,.19,.97) 1; }
.tw-mini { position: absolute; inset: 0; z-index: 10; border-radius: 14px; background: rgba(6,12,20,.6); backdrop-filter: blur(1.5px); -webkit-backdrop-filter: blur(1.5px); overflow: hidden; touch-action: manipulation; user-select: none; -webkit-user-select: none; cursor: pointer; }
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
.car { animation: carDrive var(--d, 10s) linear infinite; }
@keyframes carDrive { from { transform: translateX(-90px); } to { transform: translateX(300px); } }
.rotor { animation: rotor 3s linear infinite; }
@keyframes rotor { to { transform: rotate(360deg); } }
@media (max-width: 600px) {
  .bay.board { grid-template-columns: minmax(0, 1fr); gap: 8px; }
  .bd-board { padding: 4px; gap: 2px; }
  .bd-side { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); align-items: start; }
  .bd-info { grid-column: 1 / -1; min-height: 0; padding: 8px; }
  .bd-buy, .bd-auto { align-self: stretch; }
  .bd-auto { justify-self: stretch; border-radius: 12px; }
  .bd-dists { grid-column: 1 / -1; grid-template-columns: 1fr 1fr; }
  .bd-pop { font-size: .7rem; }
}
@media (prefers-reduced-motion: reduce) { .tw-flash, .bd-pop, .bd-card.in { animation-duration: .01s; } .car, .rotor, .tw-cash.hot, .bd-f.can, .die.roll { animation: none; } .bd-bus { transition: none; } }
'''

BOARD_JS = r'''
/* ===================== Neustadt: Stadtrundfahrt (Brettspiel mit Stadtbus) =====================
   Eine Runde kostet einmal den Einsatz. Zwei Würfel, der Stadtbus fährt die 20 Felder ab und das Feld, auf dem er hält, wirkt.
   Pasch: noch einmal würfeln (höchstens 3 Würfe pro Runde). Über den Busbahnhof fahren gibt den Rundenbonus.
   Grundstücke kaufen und ausbauen (Stufe 1 bis 4). Hält der Bus auf deinem Grundstück, zahlt es Miete, ein ganzes Viertel ×1,5.
   Die Miete rechnet mit dem Einsatz, zu dem du gebaut hast (Durchschnitt), höchstens mit dem aktuellen Einsatz.
   Balance per Simulation (tools/sim/stadtrundfahrt.js): leere Stadt ~110 %, alles Stufe 1 ~130 %, alles Stufe 4 ~177 %. */
const BD_PRICE = [3, 5, 8, 12], BD_RENT = [0, .12, .2, .3, .42], BD_FULL = 1.5;
const BD_PASS = .25, BD_LAND = .6, BD_KIOSK = .4, BD_PARK = .05, BD_PLANS = 5, BD_FS = 3, BD_FS_MULT = 2, BD_RESERVE = 50, BD_MAX_ROLLS = 3;
const BD_DIST = [
  { name: "Gartenweg", sym: "scrap", color: "#7ed957", f: .7 },
  { name: "Marktviertel", sym: "cell", color: "#4aa8ff", f: .9 },
  { name: "Büromeile", sym: "chip", color: "#c08cff", f: 1.1 },
  { name: "Turmallee", sym: "core", color: "#ff7a59", f: 1.4 },
];
const BD_LV = ["Bauland", "Häuschen", "Stadthaus", "Wohnblock", "Hochhaus"];
const BD_F = [
  { t: "start" }, { t: "plot", d: 0, n: "Rosenweg" }, { t: "news" }, { t: "plot", d: 0, n: "Lindenweg" }, { t: "plan" },
  { t: "mini" }, { t: "plot", d: 1, n: "Bäckergasse" }, { t: "plot", d: 1, n: "Marktstraße" }, { t: "news" }, { t: "plot", d: 1, n: "Uhrmacherweg" },
  { t: "park" }, { t: "plot", d: 2, n: "Kontorstraße" }, { t: "kiosk" }, { t: "plot", d: 2, n: "Börsenplatz" }, { t: "plot", d: 2, n: "Am Funkturm" },
  { t: "office" }, { t: "plot", d: 3, n: "Glasallee" }, { t: "news" }, { t: "plot", d: 3, n: "Sonnenhöhe" }, { t: "plot", d: 3, n: "Skyline-Platz" },
];
const BD_N = BD_F.length;
const BD_ICON = {
  start: `<svg viewBox="0 0 32 32"><path d="M16 31 V14" stroke="#5a6470" stroke-width="2.4"/><circle cx="16" cy="11" r="9" fill="#ffd34a" stroke="#2f8a4a" stroke-width="2.6"/><text x="16" y="15" font-size="11" font-weight="900" font-family="sans-serif" text-anchor="middle" fill="#2f8a4a">H</text></svg>`,
  news: `<svg viewBox="0 0 32 32"><path d="M5 7 h20 v19 a2 2 0 0 1 -2 2 h-17 a2 2 0 0 1 -2 -2 v-16" fill="#ffffff" stroke="#2a3440" stroke-width="1.6"/><path d="M25 12 h3 v14 a2 2 0 0 1 -2 2" fill="#e8e8e8" stroke="#2a3440" stroke-width="1.6"/><rect x="8" y="10" width="14" height="4" fill="#2a3440"/><path d="M8 17.5 h6 M8 20.5 h6 M8 23.5 h6" stroke="#6a7480" stroke-width="1.4"/><rect x="16" y="17" width="6" height="7" fill="#4aa8ff"/></svg>`,
  park: `<svg viewBox="0 0 32 32"><circle cx="12" cy="11" r="7" fill="#3fa84a"/><circle cx="19" cy="13" r="7" fill="#2f8a4a"/><path d="M15 18 v9" stroke="#7a5a3a" stroke-width="2.4"/><path d="M4 24 h12 M5 24 v4 M15 24 v4" stroke="#8a5a2a" stroke-width="1.8"/><rect x="21" y="21" width="7" height="7" rx="1" fill="#ffd34a" stroke="#a87a10" stroke-width="1.2"/><text x="24.5" y="27" font-size="6" font-weight="900" font-family="sans-serif" text-anchor="middle" fill="#7a5a10">T</text></svg>`,
  office: `<svg viewBox="0 0 32 32"><path d="M16 2 v6" stroke="#5a6470" stroke-width="1.4"/><path d="M16 2 h6 l-2 2 l2 2 h-6z" fill="#ff7a59"/><path d="M3 13 L16 7 L29 13 Z" fill="#c8b088" stroke="#2a3440" stroke-width="1.3"/><rect x="5" y="13" width="22" height="14" fill="#f2ead6" stroke="#2a3440" stroke-width="1.3"/><path d="M9 15 v10 M13 15 v10 M19 15 v10 M23 15 v10" stroke="#9a8a6a" stroke-width="2"/><rect x="14.5" y="19" width="3" height="8" fill="#2a3440"/><rect x="3" y="27" width="26" height="3" fill="#9a9484"/></svg>`,
  mini: `<svg viewBox="0 0 32 32"><path d="M8 30 V5 M12 30 V5" stroke="#e8a83a" stroke-width="1.8"/><path d="M8 9 L12 13 M12 9 L8 13 M8 17 L12 21 M12 17 L8 21 M8 25 L12 29 M12 25 L8 29" stroke="#e8a83a" stroke-width=".9"/><path d="M4 5 H29" stroke="#ffc94a" stroke-width="2.4"/><rect x="3" y="6" width="5" height="4" fill="#6a6f76"/><path d="M24 6 V14" stroke="#5a6470" stroke-width="1"/><rect x="20" y="14" width="8" height="4" fill="#c8b088" stroke="#6a5a3a" stroke-width=".8"/><path d="M19 30 L22.5 20 L26 30 Z" fill="#ff7a59"/><path d="M20.4 26 h4.2" stroke="#ffffff" stroke-width="1.6"/><path d="M2 30.5 H30" stroke="#5a6470" stroke-width="1.6"/></svg>`,
  plan: `<svg viewBox="0 0 32 32"><rect x="4" y="6" width="22" height="20" rx="1.5" fill="#2f6fb8" stroke="#1a3a6a" stroke-width="1.2"/><path d="M4 11 h22 M4 16 h22 M4 21 h22 M9 6 v20 M14 6 v20 M19 6 v20" stroke="#9ad4ff" stroke-width=".5" opacity=".7"/><path d="M8 22 V13 L14 9 L20 13 V22 Z" fill="none" stroke="#ffffff" stroke-width="1.4"/><rect x="12.5" y="17" width="3" height="5" fill="none" stroke="#ffffff" stroke-width="1"/><ellipse cx="26" cy="16" rx="3" ry="10" fill="#4a8ad0" stroke="#1a3a6a" stroke-width="1.2"/><circle cx="24" cy="25" r="4.5" fill="#ff4b5c" stroke="#8a1a2a" stroke-width="1"/><path d="M22 25 l1.5 1.5 l3 -3" stroke="#ffffff" stroke-width="1.2" fill="none"/></svg>`,
  kiosk: `<svg viewBox="0 0 32 32"><rect x="7" y="13" width="18" height="15" fill="#f2ead6" stroke="#2a3440" stroke-width="1.3"/><path d="M5 13 L8 6 H24 L27 13 Z" fill="#ff7a59" stroke="#2a3440" stroke-width="1.3"/><path d="M10 6 L9 13 M14 6 L14 13 M18 6 L18 13 M22 6 L23 13" stroke="#ffffff" stroke-width="1.6"/><rect x="10" y="16" width="12" height="5" fill="#9ad4ff"/><rect x="11" y="22" width="4" height="3" fill="#ffd34a"/><rect x="17" y="22" width="4" height="3" fill="#7ed957"/></svg>`,
};
const BD_SPECIAL = {
  start: { name: "Busbahnhof", short: "Start", color: "#3fd0a0", icon: () => BD_ICON.start, text: () => `Drüberfahren bringt den Rundenbonus (+${bdT(BD_PASS)}). Genau hier halten: zusätzlich +${bdT(BD_LAND)}.` },
  news: { name: "Stadtanzeiger", short: "Zeitung", color: "#4aa8ff", icon: () => BD_ICON.news, text: () => "Zieh eine Meldung: Taler, Bauplan, ein geschenkter Ausbau, Zahltag, Wappen oder sogar die Stadtlotterie." },
  plan: { name: "Bauamt", short: "Bauamt", color: "#4aa8ff", icon: () => BD_ICON.plan, text: () => `Gibt einen Bauplan. Bei ${BD_PLANS} Bauplänen startet die Bauplanauswahl (Bonusspiel). Gerade ${bd().plans} von ${BD_PLANS}.` },
  mini: { name: "Baustelle", short: "Baustelle", color: "#ffc94a", icon: () => BD_ICON.mini, text: () => "Mini-Event mit Geschicklichkeit: Kran-Timing, Ziegelregen oder Tauben-Alarm. Bis zu 2,6× Einsatz." },
  park: { name: "Stadtpark", short: "Park", color: "#7ed957", icon: () => BD_ICON.park, text: () => `Jede Runde wandern 5 % des Einsatzes in die Parkkasse. Wer hier hält, bekommt alles: gerade ${Math.round(bd().park)} Taler.` },
  kiosk: { name: "Kiosk", short: "Kiosk", color: "#ff7a59", icon: () => BD_ICON.kiosk, text: () => `Kleiner Snack, kleiner Gewinn: +${bdT(BD_KIOSK)} und etwas Wappenstaub.` },
  office: { name: "Rathaus", short: "Rathaus", color: "#c6f06b", icon: () => BD_ICON.office, text: () => `Der Bürgermeister spendiert ${BD_FS + (boostOn("signal") ? 2 : 0)} Freifahrten. Sie kosten nichts und alle Gewinne zählen doppelt.` },
};
const BD_CARDS = [
  { k: "cash", v: .5, w: 5, t: ["Straßenfest im Viertel", "Flohmarkt-Erlös", "Fundsache abgegeben"], s: "Die Nachbarschaft legt zusammen." },
  { k: "cash", v: 1.5, w: 3, t: ["Der Bäckerverein spendet", "Glück im Stadtteil-Lotto"], s: "Ein schöner Batzen für die Stadtkasse." },
  { k: "cash", v: 4, w: 1, t: ["Preis: Schönste Stadt!"], s: "Die Jury ist begeistert." },
  { k: "start", w: 2, t: ["Umleitung zum Busbahnhof"], s: "Der Bus fährt direkt zum Start." },
  { k: "plan", w: 1.5, t: ["Bauplan im Briefkasten"], s: "+1 Bauplan." },
  { k: "wheel", w: .2, t: ["Stadtlotterie!"], s: "Ab zum Glücksrad." },
  { k: "free", w: 1, t: ["Das Bauamt schenkt dir was"], s: "Ein kostenloser Ausbau." },
  { k: "none", w: 4, t: ["Regen in Neustadt", "Baustellenumleitung", "Funkstille im Rathaus"], s: "Heute passiert nichts." },
  { k: "payday", v: .3, w: 1, t: ["Zahltag!"], s: "Alle Mieter zahlen ein Drittel Miete extra." },
  { k: "dust", w: 1, t: ["Wappen gefunden!"], s: "+1 Wappen für das Bauamt." },
];
const BD_CARD_W = BD_CARDS.reduce((a, c) => a + c.w, 0);
const BD_PIPS = { 1: [4], 2: [0, 8], 3: [0, 4, 8], 4: [0, 2, 6, 8], 5: [0, 2, 4, 6, 8], 6: [0, 2, 3, 5, 6, 8] };
const BD_BUS = `<svg viewBox="0 0 48 30"><rect x="2" y="3" width="42" height="20" rx="5" fill="#ff9a3a" stroke="#7a3a10" stroke-width="1.4"/><rect x="2" y="15" width="42" height="3" fill="#ffd34a"/><path d="M38 6 h4 a2 2 0 0 1 2 2 v6 h-6z" fill="#bfe6ff" stroke="#7a3a10" stroke-width="1"/>
  <rect x="6" y="6" width="7" height="6" rx="1" fill="#bfe6ff"/><rect x="15" y="6" width="7" height="6" rx="1" fill="#bfe6ff"/><rect x="24" y="6" width="7" height="6" rx="1" fill="#bfe6ff"/><rect x="32" y="6" width="4" height="13" rx="1" fill="#e8f4ff" stroke="#7a3a10" stroke-width=".8"/>
  <circle cx="12" cy="24" r="4.2" fill="#22262a"/><circle cx="12" cy="24" r="1.6" fill="#c9ccd1"/><circle cx="35" cy="24" r="4.2" fill="#22262a"/><circle cx="35" cy="24" r="1.6" fill="#c9ccd1"/><rect x="43" y="17" width="3" height="3" rx="1" fill="#fff4c8"/></svg>`;

let rd = null, bdRolling = false, bdFast = false, bdBuilt = -1, bdSel = -1, bdFsBet = 0, twMiniKey = null, netCascading = false, colRun = null, bdDir = 1;
function bdFresh() { return { pos: 0, plots: {}, plans: 0, park: 0 }; }
function bd() { if (!state.board || typeof state.board !== "object" || !state.board.plots) state.board = bdFresh(); return state.board; }
const bdPlot = i => bd().plots[i] || { l: 0, inv: 0 };
const bdDF = i => BD_DIST[BD_F[i].d].f;
const bdUnits = (l, i) => { let u = 0; for (let k = 0; k < l; k++) u += BD_PRICE[k] * bdDF(i); return u; };
const bdBbar = i => { const p = bdPlot(i); return p.l ? p.inv / bdUnits(p.l, i) : 0; };
const bdFull = d => BD_F.every((f, i) => f.t !== "plot" || f.d !== d || bdPlot(i).l > 0);
const bdOwned = () => BD_F.reduce((a, f, i) => a + (f.t === "plot" && bdPlot(i).l > 0 ? 1 : 0), 0);
const bdT = u => Math.max(1, Math.round(u * bet() * lineBoost())).toLocaleString("de-DE");
const bdName = i => BD_F[i].t === "plot" ? BD_F[i].n : BD_SPECIAL[BD_F[i].t].name;
function bdRentRaw(i, b) { const p = bdPlot(i); if (!p.l) return 0; return BD_RENT[p.l] * bdDF(i) * Math.min(b, bdBbar(i)) * (bdFull(BD_F[i].d) ? BD_FULL : 1); }
const bdPriceFull = i => BD_PRICE[Math.min(3, bdPlot(i).l)] * bdDF(i) * bet();
const bdCost = i => bdPlot(i).l >= 4 ? 0 : Math.max(1, Math.ceil(bdPriceFull(i) * (boostOn("drones") ? .75 : 1)));
function bdRC(i) { if (i <= 5) return [6, 6 - i]; if (i <= 10) return [6 - (i - 5), 1]; if (i <= 15) return [1, 1 + (i - 10)]; return [1 + (i - 15), 6]; }
const bdTile = i => document.querySelector(`.bd-f[data-i="${i}"]`);

/* ----- Grafik ----- */
function bdHouse(l, c) {
  const W = "#fff4c8", S = `stroke="#2a3440" stroke-width="1"`;
  if (!l) return `<svg viewBox="0 0 40 34"><path d="M3 31 h34" stroke="#b8b0a0" stroke-width="2"/><path d="M20 31 V15" stroke="#7a6a50" stroke-width="2"/><rect x="8" y="5" width="24" height="11" rx="2" fill="#ffffff" stroke="${c}" stroke-width="1.8"/><text x="20" y="13.2" font-size="6.6" font-weight="800" font-family="sans-serif" text-anchor="middle" fill="#3a4a5a">frei</text></svg>`;
  if (l === 1) return `<svg viewBox="0 0 40 34"><path d="M3 31 h34" stroke="#8a9a6a" stroke-width="2"/><rect x="12" y="18" width="16" height="13" fill="${c}" ${S}/><path d="M9.5 19 L20 9.5 L30.5 19 Z" fill="#c8553d" ${S}/><rect x="18" y="24" width="4" height="7" fill="#2a3440"/><rect x="14" y="21" width="3" height="3" fill="${W}"/><rect x="23" y="21" width="3" height="3" fill="${W}"/></svg>`;
  if (l === 2) return `<svg viewBox="0 0 40 34"><path d="M3 31 h34" stroke="#8a9a6a" stroke-width="2"/><rect x="11" y="12" width="18" height="19" fill="${c}" ${S}/><path d="M9 13 L20 4 L31 13 Z" fill="#a8443a" ${S}/>${[14, 20.5].map(y => [13.5, 18.5, 23.5].map(x => `<rect x="${x}" y="${y}" width="3" height="3.4" fill="${W}"/>`).join("")).join("")}<rect x="18.5" y="26" width="3" height="5" fill="#2a3440"/></svg>`;
  if (l === 3) return `<svg viewBox="0 0 40 34"><path d="M3 31 h34" stroke="#8a9a6a" stroke-width="2"/><rect x="7" y="8" width="26" height="23" fill="${c}" ${S}/><rect x="6" y="6" width="28" height="3" fill="#5a6470"/>${[11, 16, 21].map(y => [9.5, 14.5, 19.5, 24.5, 29].map(x => `<rect x="${x}" y="${y}" width="2.6" height="3" fill="${W}"/>`).join("")).join("")}<rect x="18" y="26" width="4" height="5" fill="#2a3440"/></svg>`;
  return `<svg viewBox="0 0 40 34"><path d="M3 31 h34" stroke="#8a9a6a" stroke-width="2"/><rect x="5" y="17" width="9" height="14" fill="${c}" opacity=".75" ${S}/><rect x="14" y="3" width="15" height="28" fill="${c}" ${S}/><path d="M21.5 3 V0" stroke="#2a3440" stroke-width="1.2"/><circle cx="21.5" cy="0.6" r=".9" fill="#ff4b5c"/>${[6, 10, 14, 18, 22].map(y => [16, 20, 24.5].map(x => `<rect x="${x}" y="${y}" width="2.6" height="2.6" fill="${W}"/>`).join("")).join("")}${[20, 24].map(y => `<rect x="7" y="${y}" width="5" height="2" fill="${W}"/>`).join("")}<rect x="20" y="26.5" width="3" height="4.5" fill="#2a3440"/></svg>`;
}
function bdTileHTML(i) {
  const f = BD_F[i];
  if (f.t === "plot") { const D = BD_DIST[f.d], p = bdPlot(i);
    return `<i class="bd-strip" style="background:${D.color}"></i>${bdHouse(p.l, D.color)}<span class="bd-pips">${[1, 2, 3, 4].map(k => `<b class="${k <= p.l ? "on" : ""}"></b>`).join("")}</span>`; }
  const S = BD_SPECIAL[f.t];
  return `<span class="bd-ic">${S.icon()}</span><small>${S.short}</small>`;
}
function bdRender() {
  const el = $("bdBoard"); if (!el) return;
  el.querySelectorAll(".bd-f").forEach(x => x.remove());
  BD_F.forEach((f, i) => {
    const [r, c] = bdRC(i), b = document.createElement("button");
    b.type = "button"; b.className = `bd-f bd-${f.t}`; b.dataset.i = i; b.style.gridArea = `${r} / ${c}`;
    if (f.t === "plot") b.style.setProperty("--dc", BD_DIST[f.d].color);
    b.setAttribute("aria-label", bdName(i)); b.innerHTML = bdTileHTML(i);
    el.insertBefore(b, el.firstChild);
  });
  $("bdBus").innerHTML = BD_BUS;
  bdBusTo(bd().pos, true); bdUi();
}
function bdRedrawTile(i, fresh) { const t = bdTile(i); if (!t) return; t.innerHTML = bdTileHTML(i); if (fresh) { t.classList.remove("new"); void t.offsetWidth; t.classList.add("new"); } }
function bdBusTo(i, instant) {
  const t = bdTile(i), bus = $("bdBus"); if (!t || !bus) return;
  if (instant) bus.style.transition = "none";
  bus.style.left = (t.offsetLeft + t.offsetWidth / 2) + "px"; bus.style.top = (t.offsetTop + t.offsetHeight / 2) + "px";
  if (i >= 1 && i <= 5) bdDir = -1; else if (i >= 11 && i <= 15) bdDir = 1;
  bus.classList.toggle("left", bdDir < 0);
  if (instant) { void bus.offsetWidth; bus.style.transition = ""; }
  else { bus.classList.remove("hop"); void bus.offsetWidth; bus.classList.add("hop"); }
  document.querySelectorAll(".bd-f.here").forEach(x => x.classList.remove("here"));
  t.classList.add("here");
}
function bdDie(el, v) { el.innerHTML = Array.from({ length: 9 }, (_, k) => `<b class="${BD_PIPS[v].includes(k) ? "on" : ""}"></b>`).join(""); el.dataset.v = v; }
function bdPop(i, text, sub, color) {
  const t = bdTile(i), b = $("bdBoard"); if (!t) return;
  const p = document.createElement("div"); p.className = "bd-pop"; p.style.setProperty("--fc", color || "#7ee0c8");
  p.style.left = (t.offsetLeft + t.offsetWidth / 2) + "px"; p.style.top = (t.offsetTop + t.offsetHeight * .3) + "px";
  p.innerHTML = `${text}${sub ? `<small>${sub}</small>` : ""}`; b.appendChild(p); setTimeout(() => p.remove(), 1450);
}
function bdFlash(title, sub, color) {
  const st = $("bdBoard"), f = document.createElement("div"); f.className = "tw-flash"; f.style.setProperty("--fc", color);
  f.innerHTML = `<b>${title}</b><small>${sub}</small>`; st.appendChild(f); setTimeout(() => f.remove(), 1700);
}
function bdTotal(pop) { const b = $("bdTotal"); b.textContent = rd ? (rd.win + rd.bonus).toLocaleString("de-DE") : $("bdTotal").dataset.last || "0"; if (pop) { b.classList.remove("up"); void b.offsetWidth; b.classList.add("up"); } }

function bdUi() {
  if (!$("bdInfo")) return;
  const B = bd(), pos = B.pos;
  $("bdPlans").textContent = B.plans; $("bdPlansBox").classList.toggle("hot", B.plans >= BD_PLANS - 1);
  $("bdPark").textContent = Math.round(B.park).toLocaleString("de-DE");
  bdTotal(false);
  const i = bdSel >= 0 ? bdSel : pos, f = BD_F[i];
  document.querySelectorAll(".bd-f.sel").forEach(x => x.classList.remove("sel")); const st = bdTile(i); if (st) st.classList.add("sel");
  let h;
  if (f.t === "plot") {
    const D = BD_DIST[f.d], p = bdPlot(i), full = bdFull(f.d), rentNow = p.l ? Math.max(1, Math.round(bdRentRaw(i, bet()) * lineBoost())) : 0;
    const fullAfter = BD_F.every((g, k) => g.t !== "plot" || g.d !== f.d || k === i || bdPlot(k).l > 0);
    const rentNext = p.l < 4 ? Math.max(1, Math.round(BD_RENT[p.l + 1] * bdDF(i) * bet() * (fullAfter ? BD_FULL : 1) * lineBoost())) : 0;
    h = `<div class="bd-ih" style="--dc:${D.color}"><i></i><b>${f.n}</b><span>${D.name}</span></div>
      <p>${p.l ? `${BD_LV[p.l]} · Stufe ${p.l} von 4` : "Freies Bauland"}${full && p.l ? ` · <span class="full">ganzes Viertel ×1,5</span>` : ""}</p>
      <dl>${p.l ? `<dt>Miete je Halt</dt><dd>${rentNow.toLocaleString("de-DE")}</dd>` : ""}${p.l < 4 ? `<dt>${p.l ? "Ausbau" : "Kaufpreis"}</dt><dd>${bdCost(i).toLocaleString("de-DE")}</dd><dt>Miete danach</dt><dd>${rentNext.toLocaleString("de-DE")}</dd>` : `<dt>Ausbau</dt><dd>fertig</dd>`}</dl>
      ${i !== pos && p.l < 4 ? `<p>Kaufen und ausbauen geht nur, wenn der Bus hier hält.</p>` : ""}`;
  } else {
    const S = BD_SPECIAL[f.t];
    h = `<div class="bd-ih" style="--dc:${S.color}"><i></i><b>${S.name}</b><span>Sonderfeld</span></div><p>${S.text()}</p>`;
  }
  $("bdInfo").innerHTML = h;
  // Kaufen-Knopf: nur für das Feld, auf dem der Bus steht
  const pf = BD_F[pos], pp = bdPlot(pos), show = pf.t === "plot" && pp.l < 4 && bdBuilt !== pos;
  const btn = $("bdBuy"); btn.hidden = !show;
  if (show) {
    const cost = bdCost(pos), can = !rd && !busy && !spinning && state.credits >= cost;
    $("bdBuyLbl").textContent = `${pp.l ? "Ausbauen" : "Kaufen"}: ${pf.n}`; $("bdBuyAmt").textContent = cost.toLocaleString("de-DE");
    btn.disabled = !can; btn.classList.toggle("hot", can);
  }
  document.querySelectorAll(".bd-f.can").forEach(x => x.classList.remove("can"));
  if (show && !btn.disabled) { const t = bdTile(pos); if (t) t.classList.add("can"); }
  const a = $("bdAuto"); a.textContent = `Auto-Bauen: ${state.bdAuto ? "an" : "aus"}`; a.classList.toggle("on", !!state.bdAuto);
  $("bdDists").innerHTML = BD_DIST.map((D, d) => `<div style="--dc:${D.color}"><i></i>${D.name}<span>${BD_F.map((g, k) => g.t === "plot" && g.d === d ? `<b class="l${bdPlot(k).l}"></b>` : "").join("")}</span>${bdFull(d) ? "<em>×1,5</em>" : ""}</div>`).join("");
}

/* ----- Kaufen und Ausbauen ----- */
function bdApplyLevel(i, invAdd) {
  const B = bd(), p = bdPlot(i), d = BD_F[i].d, wasFull = bdFull(d);
  B.plots[i] = { l: p.l + 1, inv: Math.round((p.inv + invAdd) * 100) / 100 };
  bdRedrawTile(i, true);
  if (p.l + 1 === 4) { bump("tower4"); }
  if (!wasFull && bdFull(d)) { bump("fullDistrict"); bdFlash(`${BD_DIST[d].name} komplett!`, "Ganzes Viertel: Miete ×1,5", BD_DIST[d].color); sfx.fanfare(0); bipState.last = 0; bip("district", 3); }
}
function bdCanBuild(i, auto) {
  const f = BD_F[i], p = bdPlot(i); if (f.t !== "plot" || p.l >= 4 || bdBuilt === i) return false;
  const cost = bdCost(i);
  return auto ? state.credits - cost >= BD_RESERVE * bet() : state.credits >= cost;
}
function bdBuild(i, auto) {
  if (!bdCanBuild(i, auto)) return false;
  if (!auto && (rd || busy || spinning || bd().pos !== i)) return false;
  const cost = bdCost(i), l = bdPlot(i).l, name = BD_F[i].n;
  state.credits -= cost; countCredits(state.credits, 300);
  bdApplyLevel(i, bdPriceFull(i));
  bdBuilt = i; bump("plotsBought"); track("upgrade");
  sfx.upgrade(); bdPop(i, "-" + cost.toLocaleString("de-DE"), BD_LV[l + 1], "#ffd27a");
  addLog(BD_DIST[BD_F[i].d].sym, `${l ? "Ausbau" : "Kauf"}: ${name} (${BD_LV[l + 1]})`, "-" + cost, "#ffd27a");
  if (!auto) { bipState.last = 0; bip("buy", 2); $("msg").className = "msg gold"; $("msg").textContent = `${name}: ${BD_LV[l + 1]} gebaut. Ab jetzt zahlt es Miete, wenn der Bus hier hält.`; }
  bdUi(); render(); saveGame(); checkAch();
  return true;
}
function bdFreeUpgrade() {
  const plots = BD_F.map((f, i) => i).filter(i => BD_F[i].t === "plot");
  let cand = plots.filter(i => bdPlot(i).l > 0 && bdPlot(i).l < 4);
  if (!cand.length) cand = plots.filter(i => bdPlot(i).l === 0);
  if (!cand.length) return -1;
  const i = cand[(Math.random() * cand.length) | 0];
  bdApplyLevel(i, BD_PRICE[bdPlot(i).l] * bdDF(i) * rd.bet);
  return i;
}

/* ----- Ablauf einer Runde ----- */
function netDust(pts) {
  state.dustMeter = (state.dustMeter || 0) + pts;
  let whole = 0;
  while (state.dustMeter >= 100) { state.dustMeter -= 100; whole++; }
  if (whole) addDust(whole, null); else renderDust(false);
}
function gainDustFromSpin() {}
function renderSticky() {}

function spin(auto) {
  if (!ready || rd || busy || spinning || skipCelebration || !$("scratch").hidden || !$("bonus").hidden || !$("naming").hidden || !$("worlds").hidden) return;
  const free = inFs();
  if (!free && state.credits < bet()) return;
  slammed = false;
  if (free) { fsLeft--; fsActive = true; }
  else {
    state.credits -= bet(); state.spins++; countCredits(state.credits, 250);
    sess.spins++; sess.bet += bet(); clearGamble();
    state.pot += bet() * JP_FEED; addXP(bet()); track("spins");
    bd().park += bet() * BD_PARK;
    bipState.lastSession++;
    if (bipState.lastSession % 200 === 0) setTimeout(() => bip("session", 2), 400);
  }
  rd = { bet: free ? (bdFsBet || bet()) : bet(), free, win: 0, bonus: 0, fs: 0, dust: 2, boost: false, rolls: 0, doubles: 0 };
  boostSpinActive = false;
  if (!free && state.boostReady) { rd.boost = true; boostSpinActive = true; state.boostReady = 0; state.luck = 0; sfx.boostSpin(); }
  rd.mult = (free ? BD_FS_MULT : 1) * (rd.boost ? 2 : 1) * lineBoost();
  busy = true; bdFast = false; bdBuilt = -1; bdSel = -1;
  $("lastWin").textContent = "0"; $("lastWin").classList.remove("pos");
  bdUi(); render();
  bdRound();
}
function bdGain(taler, i, label, color) {
  const amt = Math.max(1, Math.round(taler * rd.mult));
  rd.win += amt; bdPop(i, "+" + amt.toLocaleString("de-DE"), label, color); bdTotal(true);
  return amt;
}
async function bdRound() {
  const msg = $("msg");
  for (;;) {
    rd.rolls++;
    msg.className = rd.free ? "msg fs" : "msg";
    msg.textContent = rd.rolls > 1 ? `Pasch! Wurf ${rd.rolls} …` : rd.free ? `Freifahrt ${fsTotal - fsLeft} von ${fsTotal} …` : "Die Würfel rollen …";
    $("bdSub").textContent = rd.rolls > 1 ? `Wurf ${rd.rolls} von ${BD_MAX_ROLLS}` : rd.free ? "Freifahrt · Gewinne ×2" : rd.boost ? "Paule-Boost · Gewinne ×2" : "Gute Fahrt!";
    const [a, b] = await bdRollDice();
    const dbl = a === b;
    $("bdSub").textContent = `${a} + ${b} = ${a + b}${dbl ? " · Pasch!" : ""}`;
    await bdMove(a + b);
    await bdLand(bd().pos);
    if (dbl) { rd.doubles++; bump("lasers"); track("laser"); if (rd.doubles === 2) track("four"); }
    bdUi();
    if (!dbl || rd.rolls >= BD_MAX_ROLLS) break;
    sfx.mult(); bdFlash("Pasch!", "Noch einmal würfeln", "#ffc94a"); if (rd.doubles === 1) { bipState.last = 0; bip("pasch", 1); }
    await wait((bdFast || autoLeft > 0 ? 450 : 900) * T());
  }
  return bdEnd();
}
function bdRollDice() {
  bdRolling = spinning = true; render();
  sfx.roll();
  const d1 = $("bdD1"), d2 = $("bdD2"), a = 1 + ((Math.random() * 6) | 0), b = 1 + ((Math.random() * 6) | 0);
  d1.classList.remove("dbl"); d2.classList.remove("dbl"); d1.classList.add("roll"); d2.classList.add("roll");
  return new Promise(res => {
    let k = 0;
    const tick = () => {
      const n = bdFast || reduced ? 1 : 9;
      if (k++ < n) { bdDie(d1, 1 + ((Math.random() * 6) | 0)); bdDie(d2, 1 + ((Math.random() * 6) | 0)); sfx.wheelTick(); setTimeout(tick, 60 * T()); return; }
      bdDie(d1, a); bdDie(d2, b); d1.classList.remove("roll"); d2.classList.remove("roll");
      if (a === b) { d1.classList.add("dbl"); d2.classList.add("dbl"); }
      sfx.stop(); bdRolling = spinning = false; render(); res([a, b]);
    };
    tick();
  });
}
async function bdMove(steps) {
  const B = bd();
  for (let s = 0; s < steps; s++) {
    B.pos = (B.pos + 1) % BD_N;
    bdBusTo(B.pos);
    sfx.wheelTick();
    if (B.pos === 0) { bdGain(BD_PASS * rd.bet, 0, "Rundenbonus", "#3fd0a0"); sfx.coin(1); }
    await wait((bdFast || reduced ? 45 : autoLeft > 0 ? 110 : 150) * T());
  }
}
async function bdLand(i) {
  const f = BD_F[i], B = bd(), msg = $("msg"), t = bdTile(i);
  if (t) { t.classList.remove("flash"); void t.offsetWidth; t.classList.add("flash"); }
  msg.className = rd.free ? "msg fs" : "msg win";
  if (f.t === "start") { const a = bdGain(BD_LAND * rd.bet, i, "Busbahnhof", "#3fd0a0"); sfx.coin(2); msg.textContent = `Genau am Busbahnhof gehalten: +${a} extra.`; }
  else if (f.t === "plot") {
    const D = BD_DIST[f.d], p = bdPlot(i);
    track("symwin", 1, D.sym);
    if (p.l) {
      const a = bdGain(bdRentRaw(i, rd.bet), i, `Miete · ${f.n}`, D.color); sfx.coin(Math.min(3, p.l)); bump("rents");
      msg.textContent = `${f.n} (${BD_LV[p.l]}) zahlt Miete: +${a}${bdFull(f.d) ? " · ganzes Viertel ×1,5" : ""}.`;
      if (p.l >= 3 && Math.random() < .25) { bipState.last = 0; bip("rent", 1); }
    } else { msg.className = rd.free ? "msg fs" : "msg"; msg.textContent = `${f.n} ist noch frei. Kaufpreis: ${bdCost(i).toLocaleString("de-DE")} Taler.`; }
    if (state.bdAuto && bdCanBuild(i, true)) { await wait(250 * T()); bdBuild(i, true); }
  }
  else if (f.t === "news") await bdNews(i);
  else if (f.t === "plan") await bdPlan(i, false);
  else if (f.t === "mini") await bdMini(i);
  else if (f.t === "park") {
    if (B.park >= 1) { const a = bdGain(B.park, i, "Parkkasse", "#7ed957"); B.park = 0; sfx.coin(3); msg.textContent = `Stadtpark! Die Parkkasse gehört dir: +${a}.`; }
    else { msg.className = "msg"; msg.textContent = "Stadtpark. Die Parkkasse ist gerade leer."; }
  }
  else if (f.t === "kiosk") { const a = bdGain(BD_KIOSK * rd.bet, i, "Kiosk", "#ff7a59"); rd.dust += 12; sfx.coin(1); msg.textContent = `Kiosk: +${a} und ein bisschen Wappenstaub.`; }
  else if (f.t === "office") {
    const n = BD_FS + (boostOn("signal") ? 2 : 0);
    rd.fs += n; fsLeft += n; fsTotal += n; bdFsBet = rd.bet;
    if (!rd.free) { state.fsRounds++; fsWin = 0; bump("fs"); track("fs"); }
    sfx.scatter(3); bdFlash("Rathaus!", `+${n} Freifahrten · Gewinne ×2`, "#c6f06b");
    addLog("beacon", "Freifahrten erhalten", `+${n}`, "#c6f06b");
    msg.className = "msg fs"; msg.textContent = `Rathaus! +${n} Freifahrten nach dieser Runde. Sie kosten nichts, alle Gewinne zählen doppelt.`;
    await wait(500 * T());
  }
  bdUi();
}
async function bdPlan(i, card) {
  const B = bd(); B.plans++;
  sfx.feature(0, 3); bdPop(i, `Bauplan ${B.plans}/${BD_PLANS}`, card ? "aus der Zeitung" : "vom Bauamt", "#4aa8ff");
  $("msg").className = "msg gold"; $("msg").textContent = `Bauplan ${B.plans} von ${BD_PLANS}!${B.plans >= BD_PLANS ? " Bonusspiel!" : ""}`;
  bdUi();
  if (B.plans >= BD_PLANS) { B.plans = 0; await wait(400 * T()); await bdBonus("capsule"); bdUi(); }
}
function bdCardShow(title, sub, color, extra) {
  const c = $("bdCard"); c.style.setProperty("--fc", color);
  c.innerHTML = `<small>Stadtanzeiger</small><b>${title}</b><span>${sub}</span>${extra ? `<em>${extra}</em>` : ""}`;
  c.hidden = false; c.classList.remove("in"); void c.offsetWidth; c.classList.add("in");
  sfx.feature(0, 2);
  return new Promise(res => {
    let done = false;
    const end = () => { if (done) return; done = true; c.hidden = true; c.onclick = null; twMiniKey = null; res(); };
    c.onclick = end; twMiniKey = end;
    setTimeout(end, (bdFast || autoLeft > 0 ? 1000 : 2100) * T());
  });
}
async function bdNews(i) {
  let r = Math.random() * BD_CARD_W, c = BD_CARDS[0];
  for (const x of BD_CARDS) { if ((r -= x.w) < 0) { c = x; break; } }
  const title = c.t[(Math.random() * c.t.length) | 0], msg = $("msg");
  if (c.k === "cash") { const amt = Math.max(1, Math.round(c.v * rd.bet * rd.mult)); await bdCardShow(title, c.s, "#2f8a4a", "+" + amt.toLocaleString("de-DE")); bdGain(c.v * rd.bet, i, "Stadtanzeiger", "#4aa8ff"); msg.textContent = `${title}: +${amt}.`; }
  else if (c.k === "start") {
    await bdCardShow(title, c.s, "#3fd0a0");
    const B = bd(); $("bdBus").classList.add("slow");
    while (B.pos !== 0) { B.pos = (B.pos + 1) % BD_N; bdBusTo(B.pos); await wait((bdFast ? 40 : 90) * T()); }
    $("bdBus").classList.remove("slow");
    const a = bdGain(BD_LAND * rd.bet, 0, "Busbahnhof", "#3fd0a0"); sfx.coin(2); msg.textContent = `Umleitung: Der Bus steht am Busbahnhof, +${a}.`;
  }
  else if (c.k === "plan") { await bdCardShow(title, c.s, "#4aa8ff"); await bdPlan(i, true); }
  else if (c.k === "wheel") { await bdCardShow(title, c.s, "#ff7a59"); await bdBonus("warp"); }
  else if (c.k === "free") {
    await bdCardShow(title, c.s, "#ffc94a");
    const k = bdFreeUpgrade();
    if (k >= 0) { sfx.upgrade(); bdPop(k, BD_LV[bdPlot(k).l], "geschenkt!", "#ffc94a"); addLog(BD_DIST[BD_F[k].d].sym, `Geschenkt: ${BD_F[k].n} (${BD_LV[bdPlot(k).l]})`, "0", "#ffc94a"); msg.textContent = `Geschenkt: ${BD_F[k].n} ist jetzt ${BD_LV[bdPlot(k).l]}.`; checkAch(); }
    else msg.textContent = "Alles schon voll ausgebaut. Das Bauamt staunt.";
  }
  else if (c.k === "payday") {
    let raw = 0; BD_F.forEach((g, k) => { if (g.t === "plot") raw += bdRentRaw(k, rd.bet) * c.v; });
    if (raw > 0) { const amt = Math.max(1, Math.round(raw * rd.mult)); await bdCardShow(title, c.s, "#ffc94a", "+" + amt.toLocaleString("de-DE")); bdGain(raw, i, "Zahltag", "#ffc94a"); msg.textContent = `Zahltag: Alle Mieter zahlen extra, +${amt}.`; }
    else { await bdCardShow(title, "Leider hast du noch keine Mieter. Kauf ein Grundstück!", "#ffc94a"); msg.textContent = "Zahltag, aber noch keine Mieter."; }
  }
  else if (c.k === "dust") { await bdCardShow(title, c.s, "#ffc94a"); addDust(1, "Stadtanzeiger"); msg.textContent = "Ein Wappen gefunden!"; }
  else { await bdCardShow(title, c.s, "#6a7480"); msg.className = "msg"; msg.textContent = `${title}. Heute passiert nichts.`; }
}

/* ----- Baustelle: Mini-Events mit Geschicklichkeit ----- */
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
  const ms = 5000, m = mgOverlay("Kran-Timing", "Tippe, wenn der Block genau über der Baugrube schwebt!", ms);
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
  const ms = 3800, N = 5, m = mgOverlay("Tauben-Alarm", "Verscheuch alle Tauben von der Baustelle! Tipp sie an.", ms);
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
async function bdMini(i) {
  const kind = (Math.random() * 3) | 0, auto = autoLeft > 0, msg = $("msg");
  bipState.last = 0; bip("mini", 3); sfx.alarm();
  await wait(300);
  let u = .2, label = "Baustelle", text;
  if (kind === 0) {
    const r = auto ? [0, 1, 3][(Math.random() * 3) | 0] : await mgCrane();
    u = r === 3 ? 2.6 : r ? 1 : .2; label = "Kran-Timing";
    if (!auto) await mgClose(r === 3 ? "Perfekt gesetzt!" : r ? "Gut gesetzt!" : "Daneben! Trostpflaster.", r > 0);
    text = r === 3 ? "Kran-Timing perfekt" : r ? "Kran-Timing gut" : "Kran-Timing verpasst";
  } else if (kind === 1) {
    const c = auto ? 3 : await mgBricks();
    u = .2 + .3 * c; label = `Ziegelregen ×${c}`;
    if (!auto) await mgClose(c ? `${c} Ziegel gefangen!` : "Kein Ziegel gefangen.", c > 0);
    text = `Ziegelregen: ${c} gefangen`;
  } else {
    const ok = auto ? Math.random() < .6 : await mgPigeons();
    u = ok ? 2 : .2; label = "Tauben-Alarm";
    if (!auto) await mgClose(ok ? "Alle Tauben weg!" : "Die Tauben bleiben sitzen. Gurr.", ok);
    text = ok ? "Tauben verscheucht" : "Tauben-Alarm verloren";
  }
  if (!auto) { const m = $("twMini"); m.hidden = true; m.innerHTML = ""; }
  twMiniKey = null; bump("minis");
  const a = bdGain(u * rd.bet, i, label, "#ffc94a"); sfx.coin(2);
  msg.className = "msg gold"; msg.textContent = `${text}: +${a}.`;
}
async function bdBonus(id) {
  const f = { id, ...({ capsule: { bonus: "pick", title: "Bauplanauswahl", color: "#4aa8ff" }, warp: { bonus: "wheel", title: "Stadtlotterie", color: "#ff7a59" } })[id], cells: [] };
  await celebrateFeature(f);
  const amount = Math.round((await runBonus(f)) * bonusBoost() * (rd.free ? BD_FS_MULT : 1));
  state.credits += amount; rd.bonus += amount;
  state.best = Math.max(state.best, amount); state.peak = Math.max(state.peak, state.credits);
  state.bonusCount = (state.bonusCount || 0) + 1; bump("pick"); track("bonus", 1);
  track("haul", amount); sess.won += amount; sess.best = Math.max(sess.best, amount);
  addDust(1, f.title); addLog(id, f.title, "+" + amount, f.color);
  render(); bdTotal(true);
  if (amount > 0) await celebrateWin(amount, state.credits);
  bip(amount >= bet() * 10 ? "bonusGood" : "bonusMeh", 3);
  $("msg").className = "msg gold"; $("msg").textContent = `${f.title}: +${amount} Taler. Der Bus fährt weiter.`;
}
async function bdEnd() {
  const r = rd, free = r.free, msg = $("msg");
  let roundWin = r.win, paule = 0;
  if (r.boost && roundWin + r.bonus < r.bet) { paule = r.bet - roundWin - r.bonus; roundWin += paule; }
  rd = null; busy = true;
  $("bdTotal").dataset.last = (roundWin + r.bonus).toLocaleString("de-DE");
  netDust(r.dust);
  const prevStreak = streak;
  if (!free) { if (roundWin + r.bonus >= r.bet) streak++; else streak = 0; }
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
  if (win > 0) { msg.className = free ? "msg fs" : "msg win"; msg.textContent = `${r.boost ? "Paule-Boost! " : ""}Fahrt beendet: +${win} Taler${sMult > 1 ? ` · Strähne ×${String(sMult).replace(".", ",")}` : ""}${paule ? " · Paule hat aufgerundet" : ""}.`; }
  else { msg.className = "msg"; msg.textContent = "Diese Fahrt brachte nichts. Nächste Runde!"; }
  bipAfterSpin({ win: win + r.bonus, factor: (win + r.bonus) / r.bet, lasered: false, award: r.fs && !free ? r.fs : 0, features: 0, prevStreak, streak, free });
  if (!free && win >= r.bet * 15) setTimeout(() => addDust(1, "große Fahrt"), 1200);
  if (win > 0) { bump("wins"); sess.won += win; sess.best = Math.max(sess.best, win); if (!free) maxStat("maxFactor", (win + r.bonus) / r.bet); }
  maxStat("maxStreak", streak);
  render(); bdUi();
  if (win > 0) { await wait(150 * T()); await celebrateWin(win, state.credits); }
  if (r.fs && !free) await simpleBanner({ tier: "Rathaus", color: "var(--lime)", sub: "Freifahrten: kostenlos, alle Gewinne ×2" }, `+${r.fs} Freifahrten`, sfx.fs, ["#c6f06b", "#7ee0c8", "#ffffff"], 2200);
  if (inFs()) {
    busy = false; fsActive = true; render(); bdUi();
    msg.className = "msg fs"; msg.textContent = `${win ? `+${win} Taler. ` : ""}Noch ${fsLeft} Freifahrt${fsLeft === 1 ? "" : "en"}: Drück „Würfeln“, alle Gewinne zählen doppelt.`;
    saveGame(); checkAch();
    if (autoLeft > 0) { await wait(500 * T()); spin(); }
    return;
  }
  if (free) {
    fsActive = false;
    msg.className = "msg win"; msg.textContent = `Freifahrten beendet: insgesamt +${fsWin} Taler.`;
    if (fsWin >= r.bet * 50) setTimeout(() => addDust(2, "starke Freifahrten"), 2500);
    addLog("beacon", "Freifahrten gesamt", "+" + fsWin, "#c6f06b");
    await celebrateFsEnd(fsWin, state.credits);
    bip("fsend", 2); fsTotal = 0;
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
    if (win > 0 || r.fs || r.bonus) state.luck = 0; else state.luck = (state.luck || 0) + 1;
    if (r.boost && win > 0) { setTimeout(() => { bipState.last = 0; bip("boostWin", 3); }, 300); }
    if (state.luck >= BOOST_AT && !state.boostReady) await activateBoost();
    else if (state.luck === Math.round(BOOST_AT / 2)) bip("charging", 2);
    renderLuck();
  }
  checkAch(); sessPoint();
  if (!free && win >= r.bet && autoLeft === 0 && state.credits >= 5) offerGamble(win);
  busy = false; boostSpinActive = false;
  saveGame(); bdUi();
  if (autoLeft > 0) {
    if (state.credits >= bet()) { autoLeft--; render(); await wait(450 * T()); if (autoLeft >= 0 && !spinning && !busy && !rd) { if (autoLeft === 0) clearAutoMarks(); spin(); return; } }
    else { autoLeft = 0; clearAutoMarks(); }
  }
  render();
}
function quickStop() { bdFast = true; }
function press() {
  if (!$("bonus").hidden || !$("scratch").hidden) return;
  if (skipCelebration) { skipCelebration(); return; }
  if (twMiniKey) { twMiniKey(); return; }
  if (rd) { bdFast = true; return; }
  spin();
}
function evaluate(board) { return { wins: [], scatters: [], scatterReels: 0, features: [] }; }
function finish() {}

/* ----- Spielstand: Brett mitspeichern ----- */
const bdSerializeBase = serialize;
serialize = function () { const o = bdSerializeBase(); const B = bd(); o.board = { pos: B.pos, plans: B.plans, park: Math.round(B.park * 100) / 100, plots: JSON.parse(JSON.stringify(B.plots)) }; return o; };
const bdApplyBase = applySave;
applySave = function (d) {
  bdApplyBase(d);
  const B = bdFresh(), x = d && d.board;
  if (x && typeof x === "object") {
    if (Number.isInteger(x.pos) && x.pos >= 0 && x.pos < BD_N) B.pos = x.pos;
    if (typeof x.plans === "number" && isFinite(x.plans)) B.plans = Math.max(0, Math.min(BD_PLANS - 1, x.plans | 0));
    if (typeof x.park === "number" && isFinite(x.park)) B.park = Math.max(0, x.park);
    if (x.plots && typeof x.plots === "object") for (const k in x.plots) { const i = +k, p = x.plots[k];
      if (BD_F[i] && BD_F[i].t === "plot" && p && Number.isInteger(p.l) && p.l >= 1 && p.l <= 4 && typeof p.inv === "number" && isFinite(p.inv) && p.inv > 0) B.plots[i] = { l: p.l, inv: p.inv }; }
  }
  state.board = B; bdRender();
};
const bdFreshBase = freshState;
freshState = function () { return { ...bdFreshBase(), board: bdFresh() }; };
const bdAfterLoadBase = afterLoad;
afterLoad = function () { bdAfterLoadBase(); bdRender(); };
const bdGameOverBase = gameOver;
gameOver = function () { state.board = bdFresh(); bdRender(); return bdGameOverBase(); };
const bdBankBase = handleBankruptcy;
handleBankruptcy = async function () {
  // Bei Pleite verkauft der Makler zuerst Grundstücke (Stufe für Stufe, 50 % zurück), erst danach Ausbauten der Stadt
  while (state.credits < 5) {
    let pick = -1;
    BD_F.forEach((f, i) => { const p = bdPlot(i); if (f.t === "plot" && p.l > 0 && (pick < 0 || p.l > bdPlot(pick).l || (p.l === bdPlot(pick).l && p.inv > bdPlot(pick).inv))) pick = i; });
    if (pick < 0) break;
    const p = bdPlot(pick), share = p.inv * BD_PRICE[p.l - 1] / BD_PRICE.slice(0, p.l).reduce((a, b) => a + b, 0), refund = Math.max(1, Math.round(share * .5)), name = BD_F[pick].n, lv = BD_LV[p.l];
    if (p.l === 1) delete bd().plots[pick]; else bd().plots[pick] = { l: p.l - 1, inv: Math.round((p.inv - share) * 100) / 100 };
    state.credits += refund; bdRedrawTile(pick, false); bdUi();
    sfx.scrap(); bip("scrap", 3);
    addLog(BD_DIST[BD_F[pick].d].sym, `Notverkauf: ${name} (${lv})`, "+" + refund, "#ff6b7a");
    $("msg").className = "msg lose"; $("msg").textContent = `Pleite! Der Makler kauft ${name} (${lv}) für ${refund} Taler.`;
    render();
    await simpleBanner({ tier: "Notverkauf", color: "var(--lose)", sub: `${name}: ${lv} verkauft · 50 % zurück` }, "+" + refund, () => {}, ["#ff6b7a", "#b9a684"], 2200);
    countCredits(state.credits, 0);
  }
  if (state.credits < 5) return bdBankBase();
  saveGame();
};

/* ----- Oberfläche ----- */
const renderBase = render;
render = function () {
  renderBase();
  const fsMode = inFs() || fsActive, btn = $("spin");
  $("spinLabel").textContent = bdRolling ? "…" : rd ? "Schneller" : busy ? "Weiter" : fsMode ? "Freifahrt" : "Würfeln";
  btn.setAttribute("aria-label", bdRolling || rd ? "Schneller fahren" : busy ? "Feier überspringen" : "Neue Runde: würfeln");
  btn.disabled = !ready || (!rd && !busy && !inFs() && state.credits < bet());
  if (rd) $("betVal").textContent = rd.free ? "frei" : rd.bet;
  $("fsMult").textContent = BD_FS_MULT;
  if ($("bdInfo") && !rd) bdUi();
};
$("bdBoard").addEventListener("click", e => { const t = e.target.closest(".bd-f"); if (!t) return; const i = +t.dataset.i; bdSel = bdSel === i ? -1 : i; sfx.click(); bdUi(); });
$("bdBuy").addEventListener("click", () => { sfx.click(); bdBuild(bd().pos, false); });
$("bdAuto").addEventListener("click", () => { state.bdAuto = !state.bdAuto; sfx.click(); bdUi(); try { localStorage.setItem("ns-bdauto", state.bdAuto ? "1" : "0"); } catch (e) {} });
try { state.bdAuto = localStorage.getItem("ns-bdauto") === "1"; } catch (e) {}
document.addEventListener("keydown", e => { if ((e.key === "b" || e.key === "B") && !rd && !e.target.closest("input, textarea, select")) { e.preventDefault(); bdBuild(bd().pos, false); } });
window.addEventListener("resize", () => bdBusTo(bd().pos, true));
if (window.ResizeObserver) new ResizeObserver(() => bdBusTo(bd().pos, true)).observe($("bdBoard"));
bdDie($("bdD1"), 3); bdDie($("bdD2"), 4);

/* Boosts aus dem Bauamt passend zur Stadtrundfahrt */
Object.assign(BOOSTS.find(b => b.id === "drones"), { name: "Bauhilfe", effect: "Kaufen und Ausbauen 25 % günstiger" });
Object.assign(BOOSTS.find(b => b.id === "signal"), { name: "Eilantrag", effect: "Rathaus gibt 5 statt 3 Freifahrten" });

function buildInfo() {
  $("payRows").innerHTML = BD_DIST.map((D, d) => {
    const n = BD_F.filter(f => f.t === "plot" && f.d === d).length;
    return `<tr><td>${ICONS[D.sym]}${D.name}</td><td class="pay">${n}</td><td class="pay">${BD_PRICE.map(p => Math.ceil(p * D.f * bet())).join(" · ")}</td><td class="pay">${BD_RENT.slice(1).map(r => Math.max(1, Math.round(r * D.f * bet() * lineBoost()))).join(" · ")}</td></tr>`;
  }).join("");
  $("panel-bonus").innerHTML = `
    <div class="feat" style="--fc:#ff7a59">${ICONS.warp}<div><h3>Stadtrundfahrt</h3><p>Eine Runde kostet einmal den Einsatz. Du würfelst mit zwei Würfeln, der Stadtbus fährt so viele Felder weiter und das Feld, auf dem er hält, wirkt. Bei einem <b>Pasch</b> würfelst du noch einmal (höchstens 3 Würfe).</p></div></div>
    <div class="feat" style="--fc:#7ed957">${ICONS.scrap}<div><h3>Grundstücke und Miete</h3><p>Hält der Bus auf freiem Bauland, kannst du es kaufen. Bei jedem weiteren Halt baust du eine Stufe aus: Häuschen, Stadthaus, Wohnblock, Hochhaus. Hält der Bus auf deinem Grundstück, zahlt es Miete. Gehört dir ein ganzes Viertel, gibt es Miete ×1,5.</p></div></div>
    <div class="feat" style="--fc:#3fd0a0">${ICONS.cell}<div><h3>Auto-Bauen</h3><p>Ist Auto-Bauen an, kauft und baut der Bus von selbst, solange danach noch ${BD_RESERVE} Einsätze in der Kasse bleiben.</p></div></div>
    <div class="feat" style="--fc:#3fd0a0">${BD_ICON.start}<div><h3>Busbahnhof</h3><p>Jedes Mal, wenn der Bus über den Start fährt: Rundenbonus (${Math.round(BD_PASS * 100)} % vom Einsatz). Genau dort halten: noch mal ${Math.round(BD_LAND * 100)} % extra.</p></div></div>
    <div class="feat" style="--fc:#4aa8ff">${BD_ICON.news}<div><h3>Stadtanzeiger</h3><p>Drei Zeitungsfelder mit Meldungen: Taler, Bauplan, Umleitung zum Busbahnhof, geschenkter Ausbau, Zahltag für alle Mieter, Wappen oder selten die Stadtlotterie am Glücksrad.</p></div></div>
    <div class="feat" style="--fc:#4aa8ff">${BD_ICON.plan}<div><h3>Bauamt · Bauplanauswahl</h3><p>Das Bauamt gibt einen Bauplan. Bei ${BD_PLANS} Bauplänen startet die Bauplanauswahl. Die Baupläne bleiben über die Runden hinweg gesammelt.</p></div></div>
    <div class="feat" style="--fc:#ffc94a">${BD_ICON.mini}<div><h3>Baustelle · Mini-Events</h3><p><b>Kran-Timing</b> (tippen, wenn der Block über der Baugrube ist), <b>Ziegelregen</b> (goldene Ziegel fangen) und <b>Tauben-Alarm</b> (alle Tauben verscheuchen). Bis zu 2,6× Einsatz.</p></div></div>
    <div class="feat" style="--fc:#7ed957">${BD_ICON.park}<div><h3>Stadtpark</h3><p>Jede Runde wandern ${Math.round(BD_PARK * 100)} % des Einsatzes in die Parkkasse. Wer im Park hält, bekommt alles.</p></div></div>
    <div class="feat" style="--fc:#c6f06b">${BD_ICON.office}<div><h3>Rathaus · Freifahrten</h3><p>Das Rathaus spendiert ${BD_FS} Freifahrten. Sie kosten nichts und alle Gewinne zählen doppelt.</p></div></div>
    <div class="feat" style="--fc:#ffc94a">${ICONS.crystal}<div><h3>Wappen und Bauamt</h3><p>Jede Runde füllt den Wappenmesser ein wenig, der Kiosk etwas mehr. Im Bauamt tauschst du Wappen gegen Erlasse für einige Minuten.</p></div></div>
    <div class="feat" style="--fc:#ffc94a">${ICONS.scrap}<div><h3>Paule-Boost</h3><p>Jede Runde ohne Gewinn füllt Paules Glücksladung. Nach ${BOOST_AT} leeren Runden zahlt die nächste Fahrt doppelt, mindestens einen Einsatz.</p></div></div>
    <div class="feat" style="--fc:#ffc94a">${ICONS.ladder}<div><h3>Risikoleiter</h3><p>Nach einem Gewinn ab einem Einsatz: Steig die Leiter hoch, von ×1 bis ×100. Kassieren geht jederzeit.</p></div></div>
    <div class="feat" style="--fc:#ff7a59">${ICONS.beacon}<div><h3>Signal-Risiko</h3><p>Nach einem Gewinn ab einem Einsatz kannst du ihn verdoppeln: Grün oder Rot raten, genau 50 : 50.</p></div></div>
    <div class="feat" style="--fc:#ffd34a">${ICONS.relic}<div><h3>Stadtschatz</h3><p>Jede Runde legt 1,5 % deines Einsatzes in den Topf, der bei 500 Talern startet. Die Chance pro Runde ist Einsatz ÷ 40.000.</p></div></div>
    <div class="feat" style="--fc:#7ee0c8">${ICONS.up_engine}<div><h3>Aktionen, Viertel und Aufträge</h3><p>Starte Aktionen für deine Stadt, erschließe neue Viertel über deinen Rang und erfülle Aufträge für Taler und XP.</p></div></div>`;
  const pc = s => { let n = 0; for (let a = 1; a <= 6; a++) for (let b = 1; b <= 6; b++) if (a + b === s) n++; return n; };
  $("lines").innerHTML = `<div><b>Würfelsummen</b> (zwei Würfel):</div><table class="pt"><tbody>${[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12].map(s => `<tr><td>${s} Felder</td><td class="pay">${(pc(s) / 36 * 100).toFixed(1).replace(".", ",")} %</td></tr>`).join("")}</tbody></table><p class="note">Ein Pasch (zwei gleiche Zahlen) kommt in 1 von 6 Würfen und erlaubt einen weiteren Wurf, höchstens 3 pro Runde. Am häufigsten fährt der Bus 7 Felder.</p>`;
}

MISSION_TYPES.symwin.text = m => `Halte ${m.goal}-mal im Viertel ${(BD_DIST.find(D => D.sym === m.meta) || BD_DIST[0]).name}`;
MISSION_TYPES.laser.text = () => "Würfle einen Pasch";
MISSION_TYPES.four.text = () => "Würfle zwei Pasche in einer Runde";
MISSION_TYPES.upgrade.text = m => `Kaufe ${m.goal} Ausbau${m.goal > 1 ? "ten" : ""} (Stadtbild oder Grundstück)`;
MISSION_TYPES.haul.text = m => `Verdiene insgesamt ${m.goal} Taler`;
HELP_RULES.unshift(
  [".bd-f[data-i]", el => { const i = +el.dataset.i, f = BD_F[i];
    if (f.t !== "plot") return [BD_SPECIAL[f.t].name, BD_SPECIAL[f.t].text()];
    const p = bdPlot(i); return [f.n, `${BD_DIST[f.d].name} · ${BD_LV[p.l]}. ${p.l ? `Miete je Halt: <b>${Math.max(1, Math.round(bdRentRaw(i, bet()) * lineBoost()))}</b> Taler. ` : ""}${p.l < 4 ? `${p.l ? "Ausbau" : "Kauf"}: ${bdCost(i)} Taler, wenn der Bus hier hält.` : "Voll ausgebaut."} Antippen zeigt Details.`]; }],
  ["#bdDice, .die", () => ["Würfel", "Zwei Würfel bestimmen, wie weit der Bus fährt. Pasch: noch einmal würfeln, höchstens 3-mal pro Runde."]],
  ["#bdBuy", () => ["Kaufen und Ausbauen", "Kauft das Grundstück, auf dem der Bus steht, oder baut es eine Stufe aus. Einmal pro Halt. Taste <b>B</b> geht auch."]],
  ["#bdAuto", () => ["Auto-Bauen", `Kauft und baut automatisch, wenn der Bus hält, solange danach noch ${BD_RESERVE} Einsätze übrig bleiben. Gerade ${state.bdAuto ? "an" : "aus"}.`]],
  ["#bdDists", () => ["Deine Viertel", "Jeder Balken ist ein Grundstück, je kräftiger, desto höher ausgebaut. Ein ganzes Viertel zahlt Miete ×1,5."]],
  ["#bdInfo", () => ["Feld-Info", "Zeigt das Feld, auf dem der Bus steht. Tipp ein anderes Feld an, um es dir anzusehen."]],
  ["#bdTotal, .bd-total", () => ["Diese Fahrt", "Alles, was der Bus in dieser Runde eingesammelt hat."]],
  ["#bdPlansBox", () => ["Baupläne", `Bei ${BD_PLANS} Bauplänen startet die Bauplanauswahl. Gerade ${bd().plans}.`]],
  ["#bdParkBox", () => ["Parkkasse", `Wer im Stadtpark hält, bekommt sie: gerade ${Math.round(bd().park)} Taler.`]],
  [".bay, #frame", () => ["Stadtrundfahrt", "Würfeln, fahren, Miete kassieren. Kauf Grundstücke, wenn der Bus darauf hält."]],
  ["#fsbar", () => ["Freifahrten", `Kostenlose Runden, alle Gewinne zählen doppelt. Noch ${fsLeft}.`]],
);
'''
