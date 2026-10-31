# Hauptmenü, Einstellungen, Pech-Walze und Freispiel-Kauf (seit SW 0.15.0).
# Wird per tools/menu_apply.py in die Sternenwrack-Quelle (index.html) eingesetzt und von dort an alle Welten vererbt.

MENU_CSS = r'''
/* ---------- Hauptmenü, Einstellungen, Pech-Walze, Freispiel-Kauf (seit SW 0.15.0) ---------- */
.intro { overflow-y: auto; align-items: flex-start; }
.intro-inner { margin: auto; padding: 28px 16px 36px; max-width: 980px; width: 100%; box-sizing: border-box; }
.mm-brand { display: flex; align-items: baseline; justify-content: center; gap: .28em; font: 800 clamp(1.5rem, 5.4vw, 3.4rem)/1 var(--f-display, system-ui); letter-spacing: .12em; margin: 0 0 4px; white-space: nowrap; animation: mmBrand .9s .1s both; }
.mm-brand .mmb-a, .mm-brand .mmb-b { background: linear-gradient(180deg, #fff 10%, #d6dbe8 55%, #8a93a8); -webkit-background-clip: text; background-clip: text; color: transparent; filter: drop-shadow(0 2px 0 rgba(0,0,0,.45)) drop-shadow(0 0 18px rgba(255,201,74,.18)); }
.mm-brand .mmb-amp { color: var(--gold, #ffc94a); font-size: .82em; letter-spacing: 0; text-shadow: 0 0 14px rgba(255,201,74,.55); transform: translateY(-.04em) rotate(-8deg); display: inline-block; }
@keyframes mmBrand { from { opacity: 0; letter-spacing: .5em; filter: blur(6px); } to { opacity: 1; letter-spacing: .12em; filter: none; } }
.intro .intro-title { font-size: clamp(1.1rem, 4.2vw, 2.4rem); }
.mm-strip { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px; width: min(980px, 100%); margin: 14px auto 4px; }
.mms { position: relative; display: flex; gap: 10px; align-items: flex-start; text-align: left; padding: 10px 12px 11px; border-radius: 12px; background: linear-gradient(180deg, rgba(255,255,255,.06), rgba(0,0,0,.25)); border: 1px solid rgba(255,255,255,.12); border-top: 2px solid var(--wc); color: #fff; text-decoration: none; font: inherit; cursor: pointer; transition: transform .16s, border-color .16s, background .16s; overflow: hidden; }
.mms::after { content: ""; position: absolute; inset: 0; background: radial-gradient(120% 80% at 0% 0%, color-mix(in srgb, var(--wc) 22%, transparent), transparent 60%); pointer-events: none; }
.mms:hover, .mms:focus-visible { transform: translateY(-2px); border-color: color-mix(in srgb, var(--wc) 60%, transparent); outline: none; }
.mms.cur { background: linear-gradient(180deg, color-mix(in srgb, var(--wc) 20%, transparent), rgba(0,0,0,.3)); border-color: color-mix(in srgb, var(--wc) 55%, transparent); box-shadow: 0 0 22px color-mix(in srgb, var(--wc) 25%, transparent); }
.mms .mms-n { font: 800 20px/1 var(--f-mono, monospace); color: var(--wc); opacity: .9; }
.mms .mms-t { display: flex; flex-direction: column; gap: 2px; min-width: 0; }
.mms b { font-size: 15px; letter-spacing: .03em; }
.mms .mms-k { font: 700 10px/1.2 var(--f-mono, monospace); letter-spacing: .14em; text-transform: uppercase; color: var(--wc); }
.mms .mms-m { font-size: 12px; color: rgba(255,255,255,.82); line-height: 1.3; }
.mms .mms-here { position: absolute; top: 6px; right: 8px; font: 700 9px/1 var(--f-mono, monospace); letter-spacing: .1em; text-transform: uppercase; color: #0b0d14; background: var(--wc); padding: 3px 6px; border-radius: 99px; }
.intro.ingame .mm-brand { animation: none; }
@media (max-width: 900px) { .mm-strip { grid-template-columns: 1fr 1fr; } }
@media (max-width: 600px) { .mm-brand { letter-spacing: .06em; } .mms { padding: 8px 9px; gap: 7px; } .mms .mms-n { font-size: 15px; } .mms b { font-size: 13px; } .mms .mms-m { font-size: 11px; } .mms .mms-here { display: none; } }
@media (prefers-reduced-motion: reduce) { .mm-brand { animation: none; } }
.mm-eyebrow { display: inline-flex; align-items: center; gap: 8px; font: 700 12px/1 var(--f-mono, monospace); letter-spacing: .28em; text-transform: uppercase; color: rgba(255,255,255,.75); padding: 7px 12px; border: 1px solid rgba(255,255,255,.18); border-radius: 99px; background: rgba(0,0,0,.25); margin-bottom: 10px; }
.mm-eyebrow i { width: 7px; height: 7px; border-radius: 50%; background: var(--gold, #ffc94a); box-shadow: 0 0 10px var(--gold, #ffc94a); }
.mm-row { display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; margin: 14px 0 4px; }
.mm-row button { display: inline-flex; align-items: center; gap: 8px; font: 600 14px/1 var(--f-body, inherit); color: #fff; background: rgba(255,255,255,.08); border: 1px solid rgba(255,255,255,.22); border-radius: 12px; padding: 11px 16px; cursor: pointer; transition: background .15s, transform .15s; }
.mm-row button:hover { background: rgba(255,255,255,.16); transform: translateY(-1px); }
.mm-row svg { width: 16px; height: 16px; }
.mm-head { margin: 26px 0 10px; font: 700 12px/1 var(--f-mono, monospace); letter-spacing: .22em; text-transform: uppercase; color: rgba(255,255,255,.6); }
.intro-worlds.mm-grid, .worldgrid.mm-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; text-align: left; }
.mmw { position: relative; display: flex; flex-direction: column; border-radius: 16px; overflow: hidden; background: rgba(8,10,20,.72); border: 1.5px solid rgba(255,255,255,.12); color: #fff; text-decoration: none; transition: transform .18s, border-color .18s, box-shadow .18s; cursor: pointer; font: inherit; padding: 0; text-align: left; }
.intro-worlds.mm-grid a.mmw, .intro-worlds.mm-grid .mmw { border-radius: 16px; padding: 0; font: inherit; color: #fff; background: rgba(8,10,20,.72); border: 1.5px solid rgba(255,255,255,.12); }
.intro-worlds.mm-grid .mmw.cur { border-color: var(--wc); }
.mmw:hover, .mmw:focus-visible { transform: translateY(-3px); border-color: var(--wc); box-shadow: 0 10px 30px rgba(0,0,0,.45), 0 0 0 1px var(--wc); outline: none; }
.mmw.cur { border-color: var(--wc); box-shadow: 0 0 0 1px var(--wc), 0 0 24px color-mix(in srgb, var(--wc) 35%, transparent); }
.mmw .mmw-art { height: 86px; display: block; }
.mmw .mmw-art svg { width: 100%; height: 100%; display: block; }
.mmw .mmw-body { padding: 10px 12px 12px; display: flex; flex-direction: column; gap: 4px; flex: 1; }
.mmw .mmw-tag { font: 700 10px/1.2 var(--f-mono, monospace); letter-spacing: .14em; text-transform: uppercase; color: var(--wc); }
.mmw b { font-size: 18px; letter-spacing: .02em; }
.mmw .mmw-mode { font-size: 12px; color: rgba(255,255,255,.75); }
.mmw .mmw-prog { margin-top: auto; padding-top: 8px; font-size: 12px; color: rgba(255,255,255,.6); border-top: 1px solid rgba(255,255,255,.1); display: flex; justify-content: space-between; gap: 8px; }
.mmw .mmw-go { color: var(--wc); font-weight: 700; white-space: nowrap; }
.mmw .mmw-here { position: absolute; top: 8px; right: 8px; font: 700 10px/1 var(--f-mono, monospace); letter-spacing: .1em; text-transform: uppercase; background: var(--wc); color: #0a0c14; padding: 5px 8px; border-radius: 99px; }
.intro.ingame { background-color: rgba(4,6,14,.86); backdrop-filter: blur(6px); }
.intro.ingame .intro-inner > *, .intro.ingame .intro-title span { animation: none !important; opacity: 1 !important; }
.intro.ingame .intro-hint { display: none; }
.intro-worlds.mm-grid { justify-self: stretch; width: 100%; }
.chip.mmchip svg { width: 15px; height: 15px; }
.toggles #worldBtn, .toggles #bipToggle, .toggles .trackchip { display: none !important; }
/* Einstellungen */
.mmset, .fsbuy { z-index: 260 !important; }
.mmset > .bonus-card, .fsbuy > .bonus-card { background: linear-gradient(180deg, rgba(22,24,34,.98), rgba(10,12,18,.98)); color: #f2f2f6; }
.mmset, .fsbuy { overflow-y: auto; }
.mmset .bonus-card { max-width: 560px; }
.mmset .mms-sec { margin: 4px 0 14px; }
.mmset .mms-sec h3 { margin: 0 0 6px; font: 700 11px/1 var(--f-mono, monospace); letter-spacing: .18em; text-transform: uppercase; opacity: .7; }
.mmset .mms-row, .mmset .setrow { display: flex; align-items: center; justify-content: space-between; gap: 12px; padding: 9px 2px; border-bottom: 1px solid rgba(255,255,255,.08); }
.mmset .mms-row > span { display: flex; flex-direction: column; }
.mmset .mms-row small { opacity: .65; font-size: 12px; }
.mmset select { font: inherit; color: inherit; background: rgba(255,255,255,.08); border: 1px solid rgba(255,255,255,.22); border-radius: 8px; padding: 6px 8px; max-width: 55%; }
.mmset select option { color: #000; }
.mms-sw { position: relative; width: 46px; height: 26px; flex: none; border-radius: 99px; border: 1px solid rgba(255,255,255,.25); background: rgba(255,255,255,.12); cursor: pointer; transition: background .2s; padding: 0; }
.mms-sw::after { content: ""; position: absolute; top: 3px; left: 3px; width: 18px; height: 18px; border-radius: 50%; background: #fff; transition: transform .2s; }
.mms-sw[aria-checked="true"] { background: var(--lime, #b8ff5c); border-color: transparent; }
.mms-sw[aria-checked="true"]::after { transform: translateX(20px); background: #0a0c14; }
.mmset .coderow { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 10px; }
/* Freispiel-Kauf */
.fsbuybtn { display: inline-flex; align-items: center; justify-content: center; gap: 6px; margin-top: 6px; width: 100%; font: 700 12px/1 var(--f-body, inherit); letter-spacing: .03em; color: #0a0c14; background: linear-gradient(180deg, var(--lime, #b8ff5c), color-mix(in srgb, var(--lime, #b8ff5c) 70%, #000)); border: 0; border-radius: 10px; padding: 9px 10px; cursor: pointer; box-shadow: 0 3px 0 rgba(0,0,0,.35); transition: transform .12s, filter .12s; }
.fsbuybtn:hover { filter: brightness(1.08); }
.fsbuybtn:active { transform: translateY(2px); box-shadow: 0 1px 0 rgba(0,0,0,.35); }
.fsbuybtn:disabled { filter: grayscale(.8) brightness(.7); cursor: not-allowed; }
.fsbuybtn svg { width: 14px; height: 14px; }
.fsbuy .bonus-card { max-width: 720px; }
.fsb-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; margin: 6px 0 12px; }
.fsb-card { display: flex; flex-direction: column; align-items: center; gap: 6px; padding: 16px 10px 12px; border-radius: 16px; border: 1.5px solid rgba(255,255,255,.14); background: rgba(255,255,255,.05); text-align: center; position: relative; }
.fsb-card.best { border-color: var(--lime, #b8ff5c); box-shadow: 0 0 22px color-mix(in srgb, var(--lime, #b8ff5c) 30%, transparent); }
.fsb-card .fsb-flag { position: absolute; top: -10px; font: 700 10px/1 var(--f-mono, monospace); letter-spacing: .12em; text-transform: uppercase; background: var(--lime, #b8ff5c); color: #0a0c14; padding: 5px 9px; border-radius: 99px; }
.fsb-card .fsb-n { font: 800 44px/1 var(--f-display, inherit); color: var(--lime, #b8ff5c); }
.fsb-card .fsb-l { font-size: 13px; opacity: .8; }
.fsb-card .fsb-x { font: 600 12px/1.2 var(--f-mono, monospace); opacity: .6; }
.fsb-card .fsb-p { font: 800 20px/1 var(--f-display, inherit); }
.fsb-card .bbtn { width: 100%; margin-top: 4px; }
.fsb-card .bbtn:disabled { opacity: .45; cursor: not-allowed; }
.fsb-card .fsb-miss { font-size: 11px; color: #ff8a8a; min-height: 14px; }
@media (max-width: 600px) { html body .fsbuybtn { width: 34px; height: 32px; margin: 0; padding: 0; flex: none; border-radius: 9px; } html body .fsbuybtn .fsbl { display: none; } html body .fsbuybtn svg { width: 16px; height: 16px; } .mm-eyebrow { letter-spacing: .14em; font-size: 10px; } .fsb-grid { grid-template-columns: 1fr; } .fsb-card { flex-direction: row; flex-wrap: wrap; justify-content: space-between; padding: 12px; } .fsb-card .fsb-n { font-size: 32px; } .fsb-card .bbtn { width: auto; } .intro-worlds.mm-grid, .worldgrid.mm-grid { grid-template-columns: 1fr 1fr; } .mmw .mmw-art { height: 60px; } .mmw b { font-size: 15px; } }
/* Pech-Walze */
.jinx { position: fixed; inset: 0; z-index: 80; display: grid; place-items: center; pointer-events: none; }
.jinx-card { pointer-events: auto; min-width: min(420px, 92vw); padding: 18px 20px 16px; border-radius: 20px; text-align: center; color: #fff; background: radial-gradient(ellipse at 50% 0%, rgba(255,60,60,.35), transparent 70%), rgba(20,4,8,.94); border: 2px solid #ff4b4b; box-shadow: 0 0 0 4px rgba(255,75,75,.15), 0 20px 60px rgba(0,0,0,.6), 0 0 60px rgba(255,40,40,.35); animation: jinxIn .35s cubic-bezier(.2,1.4,.4,1) both; }
.jinx-card.out { animation: jinxOut .35s ease-in both; }
.jinx-card.shake { animation: jinxShake .45s ease both; }
.jinx-title { font: 800 22px/1 var(--f-display, inherit); letter-spacing: .14em; color: #ff6b6b; text-transform: uppercase; }
.jinx-sub { font-size: 12px; opacity: .7; margin-top: 4px; }
.jinx-slots { display: flex; gap: 10px; justify-content: center; margin: 14px 0 10px; }
.jinx-slot { width: 84px; height: 84px; border-radius: 14px; background: #0a0204; border: 2px solid rgba(255,90,90,.45); display: grid; place-items: center; overflow: hidden; position: relative; }
.jinx-slot .jx-roll { font: 800 34px/1 var(--f-display, inherit); color: rgba(255,120,120,.5); animation: jinxRoll .12s linear infinite; }
.jinx-slot svg { width: 70px; height: 70px; animation: jinxDrop .3s cubic-bezier(.2,1.5,.4,1) both; }
.jinx-slot.hit { border-color: #ff4b4b; box-shadow: 0 0 18px rgba(255,60,60,.6) inset; }
.jinx-amt { font: 800 34px/1 var(--f-display, inherit); color: #ff5252; text-shadow: 0 0 18px rgba(255,40,40,.6); min-height: 36px; }
.jinx-note { font-size: 12px; opacity: .7; margin-top: 6px; min-height: 16px; }
@keyframes jinxIn { from { transform: scale(.6) rotate(-4deg); opacity: 0; } to { transform: none; opacity: 1; } }
@keyframes jinxOut { to { transform: scale(.85); opacity: 0; } }
@keyframes jinxShake { 0%, 100% { transform: none; } 20% { transform: translateX(-10px) rotate(-1deg); } 40% { transform: translateX(9px) rotate(1deg); } 60% { transform: translateX(-6px); } 80% { transform: translateX(4px); } }
@keyframes jinxRoll { 0% { transform: translateY(-30%); } 100% { transform: translateY(30%); } }
@keyframes jinxDrop { from { transform: translateY(-60px) scale(.6); opacity: 0; } to { transform: none; opacity: 1; } }
body.jinx-flash .machine { box-shadow: 0 0 0 3px #ff4b4b, 0 0 60px rgba(255,40,40,.5) !important; transition: box-shadow .2s; }
@media (prefers-reduced-motion: reduce) { .jinx-card, .jinx-card.shake, .jinx-slot svg { animation: none; } }
'''

MENU_JS = r'''
/* ---------- Hauptmenü, Einstellungen, Pech-Walze, Freispiel-Kauf (seit SW 0.15.0) ---------- */
const COLLECTION = "Salvage & Grind";
const FS_BUY = [{ n: 8, x: 40 }, { n: 12, x: 60, best: true }, { n: 20, x: 100 }];   // Preis = x × Einsatz
const JINX_MIN = 18, JINX_MAX = 45, JINX_LO = .25, JINX_HI = 1;                    // alle 18–45 bezahlten Drehs, kostet 25–100 % des Einsatzes
const JINX_SYMS = {
  sternenwrack: { name: "Weltraumpirat", svg: `<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M14 30a18 18 0 0 1 36 0v6c0 4-3 6-6 7v7H20v-7c-3-1-6-3-6-7z" fill="#e9e4ef" stroke="#3a0d14" stroke-width="2.5"/><path d="M12 24c4-12 36-12 40 0-6-3-34-3-40 0z" fill="#2a0a12"/><path d="M14 26l36-10" stroke="#2a0a12" stroke-width="3.5"/><circle cx="25" cy="33" r="5.5" fill="#2a0a12"/><circle cx="40" cy="33" r="5" fill="#2a0a12"/><circle cx="40" cy="33" r="1.8" fill="#ff4b4b"/><path d="M30 41l2-4 2 4z" fill="#2a0a12"/><path d="M24 50v-5M29 50v-5M34 50v-5M39 50v-5" stroke="#3a0d14" stroke-width="2"/></svg>` },
  treibgut: { name: "Hai", svg: `<svg viewBox="0 0 64 64" aria-hidden="true"><rect x="4" y="40" width="56" height="20" rx="4" fill="#123a52"/><path d="M4 42q8-5 16 0t16 0 16 0 12 0" stroke="#7fd3ff" stroke-width="2.5" fill="none"/><path d="M22 42C26 28 34 14 46 10c-4 10-4 22 0 32z" fill="#5a6a78" stroke="#1d2730" stroke-width="2.5" stroke-linejoin="round"/><path d="M30 34c4-6 8-10 13-12" stroke="#8fa0ad" stroke-width="2" fill="none"/><path d="M8 52q6-3 12 0t12 0 12 0 12 0" stroke="#7fd3ff" stroke-width="2" fill="none" opacity=".6"/></svg>` },
  eisenfront: { name: "Mine", svg: `<svg viewBox="0 0 64 64" aria-hidden="true"><g stroke="#1a1c10" stroke-width="3" stroke-linecap="round"><path d="M32 8v8M32 48v8M8 32h8M48 32h8M15 15l6 6M43 43l6 6M49 15l-6 6M21 43l-6 6"/></g><circle cx="32" cy="32" r="16" fill="#4a4f2c" stroke="#1a1c10" stroke-width="3"/><circle cx="32" cy="32" r="6" fill="#ff4b4b"/><circle cx="27" cy="27" r="3" fill="#7a8050"/><path d="M14 56h36" stroke="#2a2614" stroke-width="3"/></svg>` },
  neustadt: { name: "Abrissbirne", svg: `<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M10 6h44" stroke="#ffc94a" stroke-width="4" stroke-linecap="round"/><path d="M32 6v24" stroke="#3a3f46" stroke-width="2.5" stroke-dasharray="3 2"/><circle cx="32" cy="44" r="15" fill="#2a2e36" stroke="#0e1014" stroke-width="3"/><circle cx="27" cy="39" r="4" fill="#5a606c"/><rect x="29" y="27" width="6" height="5" fill="#0e1014"/><path d="M6 60l6-6M58 60l-6-6" stroke="#ff8a3c" stroke-width="2.5" stroke-linecap="round"/></svg>` },
};
const jinxSym = () => JINX_SYMS[WORLD_ID] || JINX_SYMS.sternenwrack;
function fmtN(n) { return Math.round(n || 0).toLocaleString("de-DE"); }   // als Funktion, weil renderWorlds schon vor diesem Block aufgerufen wird
let jinxOn = true, jinxLeft = JINX_MIN + ((Math.random() * (JINX_MAX - JINX_MIN + 1)) | 0), jinxArmed = false, jinxBusy = false;
try { jinxOn = localStorage.getItem("welten-jinx") !== "0"; } catch (e) {}
if (typeof BIP === "object" && BIP) BIP.jinx = [["sad", "Autsch. Die Pech-Walze hat zugeschlagen."], ["sad", "Dreimal das falsche Symbol. Das tut weh."], ["wow", "Huch! Wer hat denn das bestellt?"], ["sad", "Pech gehabt. Gleich läuft's wieder besser."]];

const mmOpen = id => { const el = $(id); return !!el && !el.hidden; };
const mmBlocking = () => jinxBusy || mmOpen("mmSet") || mmOpen("fsBuy") || mmOpen("xpGame") || mmOpen("plinko") || mmOpen("arcade") || (mmOpen("intro") && $("intro").classList.contains("ingame"));
const machineIdle = () => ready && !spinning && !busy && !inFs() && !skipCelebration && (typeof sk === "undefined" || !sk)
  && $("scratch").hidden && $("bonus").hidden && $("naming").hidden && $("worlds").hidden && !mmBlocking();

/* --- Weltenwahl mit eindeutigen Namen und Spielstand --- */
function worldProgress(w) {
  if (w.id === WORLD_ID) return ready ? { level: state.level, credits: state.credits } : null;
  try { const d = JSON.parse(localStorage.getItem(w.key) || "null"); if (d && typeof d.level === "number") return { level: d.level, credits: d.credits || 0 }; } catch (e) {}
  return null;
}
function worldCard(w, inMenu) {
  const cur = w.id === WORLD_ID, p = worldProgress(w);
  const prog = p ? `Rang ${p.level} · ${fmtN(p.credits)} ${w.cur}` : "Noch kein Spielstand";
  const go = cur ? (inMenu ? "Spielen ▶" : "Du bist hier") : "Wechseln →";
  const inner = `<span class="mmw-art">${w.art}</span>${cur ? `<span class="mmw-here">Du bist hier</span>` : ""}<span class="mmw-body"><span class="mmw-tag">${w.tag}</span><b>${w.name}</b><span class="mmw-mode">${w.mode}</span><span class="mmw-prog"><span>${prog}</span><span class="mmw-go">${go}</span></span></span>`;
  return cur ? `<button type="button" class="mmw cur" data-cur="1" style="--wc:${w.color}">${inner}</button>`
    : `<a class="mmw" style="--wc:${w.color}" href="${worldUrl(w)}" target="${worldTarget()}" rel="noopener">${inner}</a>`;
}
function renderWorlds() {
  // wird schon beim Laden aufgerufen (vor diesem Block), darf deshalb nie einen Fehler werfen
  try {
    $("worldGrid").classList.add("mm-grid"); $("introWorlds").classList.add("mm-grid");
    $("worldGrid").innerHTML = WORLDS.map(w => worldCard(w, false)).join("");
    $("introWorlds").innerHTML = WORLDS.map(w => worldCard(w, true)).join("");
  } catch (e) { try { console.warn("Welten:", e); } catch (er) {} }
}
(function setupMenu() {
  const intro = $("intro"), inner = intro.querySelector(".intro-inner");
  $("introBtn").textContent = "Spielen";
  const idx = WORLDS.findIndex(w => w.id === WORLD_ID);
  inner.insertAdjacentHTML("afterbegin", `<div class="mm-brand" role="img" aria-label="Salvage &amp; Grind"><span class="mmb-a">SALVAGE</span><span class="mmb-amp">&amp;</span><span class="mmb-b">GRIND</span></div><div class="mm-eyebrow"><i></i>Welt ${idx + 1} von ${WORLDS.length} · ${WORLDS[idx] ? WORLDS[idx].name : ""}</div>`);
  // Die vier Welten mit ihren Untertiteln als Leiste unter dem Start-Knopf
  const strip = WORLDS.map((w, i) => {
    const m = w.motto || ["", ""], cur = w.id === WORLD_ID;
    const body = `<span class="mms-n">0${i + 1}</span><span class="mms-t"><b>${w.name}</b><span class="mms-k">${m[0]}</span><span class="mms-m">${m[1]}</span></span>${cur ? `<span class="mms-here">Du bist hier</span>` : ""}`;
    return cur ? `<button type="button" class="mms cur" style="--wc:${w.color}">${body}</button>`
      : `<a class="mms" style="--wc:${w.color}" href="${worldUrl(w)}" target="${worldTarget()}" rel="noopener">${body}</a>`;
  }).join("");
  $("introBtn").insertAdjacentHTML("beforebegin", `<div class="mm-strip">${strip}</div>`);
  inner.querySelector(".mm-strip").addEventListener("click", e => { if (e.target.closest(".mms.cur")) { e.preventDefault(); $("introBtn").click(); } });
  try { document.title = COLLECTION + " · " + (WORLDS[idx] ? WORLDS[idx].name : ""); } catch (e) {}
  const gear = `<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="2.4" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M12.6 3.4l-1.4 1.4M4.8 11.2l-1.4 1.4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>`;
  $("introBtn").insertAdjacentHTML("afterend", `<div class="mm-row"><button type="button" id="mmSettings">${gear}Einstellungen</button><button type="button" id="mmWorldsJump"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M1.8 8h12.4M8 1.8c2.2 2.2 2.2 10.2 0 12.4M8 1.8c-2.2 2.2-2.2 10.2 0 12.4" fill="none" stroke="currentColor" stroke-width="1.2"/></svg>Welt wählen</button></div>`);
  $("introWorlds").insertAdjacentHTML("beforebegin", `<div class="mm-head" id="mmWorldsHead">${COLLECTION.replace("&", "&amp;")} · Welten</div>`);
  $("mmWorldsJump").addEventListener("click", () => { $("mmWorldsHead").scrollIntoView({ behavior: "smooth", block: "start" }); try { sfx.click(); } catch (e) {} });
  $("mmSettings").addEventListener("click", openSettings);
  $("introWorlds").addEventListener("click", e => { if (e.target.closest(".mmw[data-cur]")) { e.preventDefault(); $("introBtn").click(); } });
  $("worldGrid").addEventListener("click", e => { if (e.target.closest(".mmw[data-cur]")) closeWorlds(); });
  const wt = $("worldsTitle"); if (wt) wt.textContent = "Welt wählen";
  // Knöpfe oben: Menü und Einstellungen
  const tg = document.querySelector(".toggles");
  tg.insertAdjacentHTML("afterbegin", `<button type="button" class="chip mmchip" id="menuBtn" aria-haspopup="dialog"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2.5 4h11M2.5 8h11M2.5 12h11" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>Menü</button>`);
  tg.insertAdjacentHTML("beforeend", `<button type="button" class="chip mmchip" id="setBtn" aria-haspopup="dialog" title="Einstellungen">${gear}<span class="sr">Einstellungen</span></button>`);
  $("menuBtn").addEventListener("click", openMainMenu);
  $("setBtn").addEventListener("click", openSettings);
  // Im Spiel: Menü schließt nur, ohne den Start noch einmal auszulösen
  $("introBtn").addEventListener("click", e => { if (intro.classList.contains("ingame")) { e.stopImmediatePropagation(); closeMainMenu(); } }, true);
  setTimeout(renderWorlds, 1500);
})();
let introLabel = null;
// Start aus dem Hauptmenü: erst das Menü schließen, dann Ton, Musik und Begrüßung – jeder Schritt einzeln abgesichert,
// damit ein Fehler (z. B. Audio im Browser blockiert) den Start nie verhindert.
function closeIntro() {
  const el = $("intro");
  if (el.classList.contains("ingame")) { closeMainMenu(); return; }
  if (el.classList.contains("out")) return;
  el.classList.add("out");
  setTimeout(() => { el.hidden = true; }, 650);
  const safe = f => { try { f(); } catch (e) { try { console.warn("Start:", e); } catch (er) {} } };
  safe(() => getCtx());
  safe(() => { if (state.sound) { tone(110, 1.1, { type: "sawtooth", vol: .1, slide: 7 }); [523, 784, 1047].forEach((f, i) => tone(f, .9, { type: "triangle", vol: .1, at: .35 + i * .08 })); } });
  safe(startMusic);
  safe(flashScreen);
  safe(() => { if (needsNaming()) setTimeout(() => openNaming("start"), 900); else setTimeout(() => bip("hello", 3), 1600); });
  safe(announceVersion);
  safe(bipActivity);
}
function openMainMenu() {
  const el = $("intro");
  if (autoLeft > 0) { autoLeft = 0; clearAutoMarks(); }
  renderWorlds();
  if (introLabel == null) introLabel = $("introBtn").textContent;
  $("introBtn").textContent = "Weiterspielen";
  el.classList.remove("out"); el.classList.add("ingame"); el.hidden = false; el.scrollTop = 0;
  try { sfx.click(); } catch (e) {}
  setTimeout(() => $("introBtn").focus({ preventScroll: true }), 50);
}
function closeMainMenu() {
  const el = $("intro");
  el.classList.add("out");
  setTimeout(() => { el.hidden = true; el.classList.remove("ingame"); if (introLabel != null) $("introBtn").textContent = introLabel; mmResume(); }, 400);
  try { sfx.click(); } catch (e) {}
}

/* --- Einstellungen als eigenes Menü --- */
document.body.insertAdjacentHTML("beforeend", `<div class="bonus mmset" id="mmSet" hidden>
  <div class="bonus-card glass" style="--bc: var(--cyan)" role="dialog" aria-modal="true" aria-labelledby="mmSetTitle">
    <header><span><svg viewBox="0 0 40 40" width="52" height="52" aria-hidden="true"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#0b1626" stroke="currentColor" stroke-width="2" style="color:var(--cyan)"/><circle cx="20" cy="20" r="5" fill="none" stroke="#fff" stroke-width="2.2"/><path d="M20 8v4M20 28v4M8 20h4M28 20h4M11.5 11.5l2.8 2.8M25.7 25.7l2.8 2.8M28.5 11.5l-2.8 2.8M14.3 25.7l-2.8 2.8" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/></svg></span>
      <div><h2 id="mmSetTitle">Einstellungen</h2><p>Gilt für diese Welt. Die Sprache gilt für alle Welten.</p></div></header>
    <div class="mms-sec" id="mmsSound"><h3>Ton und Musik</h3>
      <div class="mms-row"><span>Soundeffekte</span><button type="button" class="mms-sw" role="switch" data-chip="sound" aria-label="Soundeffekte"></button></div>
      <div class="mms-row"><span>Musik</span><button type="button" class="mms-sw" role="switch" data-chip="music" aria-label="Musik"></button></div>
      <div class="mms-row" id="mmsTrack"><span>Musiktitel</span></div>
    </div>
    <div class="mms-sec" id="mmsGame"><h3>Spiel</h3>
      <div class="mms-row"><span>Turbo<small>Schnellere Drehs, sobald der Antrieb Stufe 2 erreicht hat</small></span><button type="button" class="mms-sw" role="switch" data-chip="turbo" aria-label="Turbo"></button></div>
      <div class="mms-row"><span>Bip anzeigen<small>Dein Begleiter mit Sprüchen und Hilfe</small></span><button type="button" class="mms-sw" role="switch" data-chip="bipToggle" aria-label="Bip anzeigen"></button></div>
      <div class="mms-row"><span>Pech-Walze<small>Ab und zu kostet dreimal dasselbe Pech-Symbol einen Teil des Einsatzes</small></span><button type="button" class="mms-sw" role="switch" id="mmsJinx" aria-label="Pech-Walze"></button></div>
    </div>
    <div class="mms-sec"><h3>Sprache</h3><div class="mms-row" id="mmsLang"><span>Sprache · Language</span></div></div>
    <div class="mms-sec" id="mmsSave"><h3>Spielstand</h3>
      <div class="coderow"><button type="button" class="ghost" id="mmsCodes">Spielstand-Codes und Bestenliste</button></div>
    </div>
    <div class="bonus-foot"><div></div><button type="button" class="bbtn" id="mmSetClose" style="--bc:var(--cyan)">Fertig</button></div>
  </div>
</div>`);
(function setupSettings() {
  // vorhandene Regler und Knöpfe aus dem Bordbuch hierher holen (Listener bleiben erhalten)
  const vm = $("volMusic"), vs = $("volSfx"), lf = $("lowFx"), rb = $("resetBtn");
  const oldSec = vm && vm.closest(".psec");
  if (vm) $("mmsSound").appendChild(vm.closest(".setrow"));
  if (vs) $("mmsSound").appendChild(vs.closest(".setrow"));
  if (lf) $("mmsGame").appendChild(lf.closest(".setrow"));
  if (rb) $("mmsSave").querySelector(".coderow").appendChild(rb);
  // Nach dem Zurücksetzen: Einstellungen und Hauptmenü schließen, damit das Schiffsregister vorne erscheint
  if (rb) {
    let wasArmed = false;
    rb.addEventListener("click", () => { wasArmed = rb.classList.contains("armed"); }, true);
    rb.addEventListener("click", () => setTimeout(() => {
      if (!wasArmed || rb.classList.contains("armed")) return;
      closeSettings();
      const el = $("intro");
      if (!el.hidden) {
        if (!el.classList.contains("ingame")) { el.classList.add("ingame"); try { getCtx(); startMusic(); } catch (e) {} }
        closeMainMenu();
      }
    }, 0));
  }
  const ts = $("trackSel"); if (ts) $("mmsTrack").appendChild(ts);
  const ls = $("langSel"); if (ls) $("mmsLang").appendChild(ls);
  if (oldSec) { oldSec.querySelectorAll(".setrow, .coderow").forEach(n => { if (!n.children.length) n.remove(); }); oldSec.insertAdjacentHTML("beforeend", `<div class="coderow"><button type="button" class="ghost" id="mmsFromLog">Einstellungen öffnen</button></div>`); $("mmsFromLog").addEventListener("click", openSettings); }
  $("mmSet").querySelectorAll(".mms-sw[data-chip]").forEach(sw => sw.addEventListener("click", () => { const c = $(sw.dataset.chip); if (c) c.click(); syncSettings(); }));
  $("mmsJinx").addEventListener("click", () => { jinxOn = !jinxOn; try { localStorage.setItem("welten-jinx", jinxOn ? "1" : "0"); } catch (e) {} syncSettings(); try { sfx.click(); } catch (e) {} });
  $("mmsCodes").addEventListener("click", () => { closeSettings(); if ($("intro").classList.contains("ingame")) closeMainMenu(); switchPv("log"); const t = $("exportBtn"); if (t) setTimeout(() => t.scrollIntoView({ behavior: "smooth", block: "center" }), 120); });
  $("mmSetClose").addEventListener("click", closeSettings);
  $("mmSet").addEventListener("click", e => { if (e.target.id === "mmSet") closeSettings(); });
})();
function syncSettings() {
  $("mmSet").querySelectorAll(".mms-sw[data-chip]").forEach(sw => { const c = $(sw.dataset.chip); sw.setAttribute("aria-checked", String(!!c && c.getAttribute("aria-pressed") === "true")); });
  $("mmsJinx").setAttribute("aria-checked", String(jinxOn));
}
function openSettings() { syncSettings(); $("mmSet").hidden = false; try { sfx.click(); } catch (e) {} $("mmSetClose").focus({ preventScroll: true }); }
function closeSettings() { $("mmSet").hidden = true; try { sfx.click(); } catch (e) {} mmResume(); }

/* --- Freispiele kaufen --- */
document.body.insertAdjacentHTML("beforeend", `<div class="bonus fsbuy" id="fsBuy" hidden>
  <div class="bonus-card glass" style="--bc: var(--lime)" role="dialog" aria-modal="true" aria-labelledby="fsBuyTitle">
    <header><span><svg viewBox="0 0 40 40" width="52" height="52" aria-hidden="true"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#0f1a06" stroke="#b8ff5c" stroke-width="2"/><path d="M20 8l3.4 7.6 8.1.8-6.1 5.4 1.8 8-7.2-4.3-7.2 4.3 1.8-8-6.1-5.4 8.1-.8z" fill="#b8ff5c"/></svg></span>
      <div><h2 id="fsBuyTitle">Freispiele kaufen</h2><p id="fsBuyInfo"></p></div></header>
    <div class="fsb-grid" id="fsBuyGrid"></div>
    <div class="bonus-foot"><div class="note">Gekaufte Freispiele laufen genau wie ausgelöste, inklusive Multiplikator und Extras.</div><button type="button" class="ghost" id="fsBuyClose">Schließen</button></div>
  </div>
</div>`);
const fsPrice = p => p.x * bet();
function renderFsBuy() {
  $("fsBuyInfo").textContent = `Startet sofort eine Freispielrunde zum aktuellen Einsatz von ${fmtN(bet())} Credits. Der Preis richtet sich nach dem Einsatz.`;
  $("fsBuyGrid").innerHTML = FS_BUY.map((p, i) => {
    const price = fsPrice(p), ok = state.credits >= price;
    return `<div class="fsb-card${p.best ? " best" : ""}">${p.best ? `<span class="fsb-flag">Beliebt</span>` : ""}<span class="fsb-n">${p.n}</span><span class="fsb-l">Freispiele</span><span class="fsb-x">${p.x}× Einsatz</span><span class="fsb-p">${fmtN(price)} Credits</span><button type="button" class="bbtn" data-buy="${i}" style="--bc:var(--lime)"${ok ? "" : " disabled"}>Kaufen</button><span class="fsb-miss">${ok ? "" : "Zu wenig Credits"}</span></div>`;
  }).join("");
}
function openFsBuy() { if (!machineIdle()) return; renderFsBuy(); $("fsBuy").hidden = false; try { sfx.click(); } catch (e) {} $("fsBuyClose").focus({ preventScroll: true }); }
function closeFsBuy() { $("fsBuy").hidden = true; mmResume(); }
function fsBuyPrep() {
  // setzt den Freispiel-Zustand der jeweiligen Welt zurück (Sternenwrack, Treibgut, Eisenfront, Neustadt)
  try { fsMult = FS_MULT; } catch (e) {}
  try { fsSticky = []; renderSticky(); } catch (e) {}
  if (typeof colFsUi === "function") { try { colLev = 0; colMeter = 0; colFsUi(); } catch (e) {} }
  if (typeof skMultUi === "function") { try { skM = 1; skFsBet = bet(); skMultUi(false); } catch (e) {} }
}
async function buyFs(i) {
  const p = FS_BUY[i], price = p && fsPrice(p);
  if (!p) return;
  closeFsBuy();
  if (!machineIdle() || state.credits < price) return;
  if (autoLeft > 0) { autoLeft = 0; clearAutoMarks(); }
  state.credits -= price; countCredits(state.credits, 300);
  sess.bet += price; bump("fsBought");
  state.fsRounds++; fsWin = 0; fsBuyPrep();
  fsLeft = p.n; fsTotal = p.n;
  busy = true; render();
  radio(`Funk: ${p.n} Freispiele gekauft für ${fmtN(price)} Credits. Viel Glück!`, true);
  await simpleBanner({ tier: "Freispiele gekauft", color: "var(--lime)", sub: `${p.n} Freispiele · Einsatz ${fmtN(bet())}` }, `+${p.n} Freispiele`, sfx.fs, ["#b8ff5c", "#4fe3ff", "#ffffff"], 2000);
  busy = false; fsActive = true; render(); saveGame();
  spin(true);
}
(function setupFsBuy() {
  const host = document.querySelector(".deck .bets") || document.querySelector(".deck");
  if (!host) return;
  host.insertAdjacentHTML("beforeend", `<button type="button" class="fsbuybtn" id="fsBuyBtn" aria-haspopup="dialog" aria-label="Freispiele kaufen" title="Freispiele kaufen"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 1.5l1.9 4.2 4.6.5-3.4 3.1 1 4.5L8 11.4 3.9 13.8l1-4.5L1.5 6.2l4.6-.5z" fill="currentColor"/></svg><span class="fsbl">Freispiele kaufen</span></button>`);
  $("fsBuyBtn").addEventListener("click", openFsBuy);
  $("fsBuyGrid").addEventListener("click", e => { const b = e.target.closest("[data-buy]"); if (b && !b.disabled) buyFs(+b.dataset.buy); });
  $("fsBuyClose").addEventListener("click", closeFsBuy);
  $("fsBuy").addEventListener("click", e => { if (e.target.id === "fsBuy") closeFsBuy(); });
  setInterval(() => { const b = $("fsBuyBtn"); const off = !machineIdle() || state.credits < fsPrice(FS_BUY[0]); if (b.disabled !== off) b.disabled = off; if (!$("fsBuy").hidden && !machineIdle() && !mmOpen("fsBuy")) closeFsBuy(); }, 300);
})();

/* --- Pech-Walze: ab und zu dreimal dasselbe Pech-Symbol, kostet einen Teil des Einsatzes --- */
document.body.insertAdjacentHTML("beforeend", `<div class="jinx" id="jinx" hidden aria-live="assertive"></div>`);
async function runJinx() {
  const j = jinxSym(), b = bet();
  let x = Math.max(1, Math.round(b * (JINX_LO + Math.random() * (JINX_HI - JINX_LO))));
  x = Math.min(x, state.credits);
  if (x <= 0) return;
  jinxBusy = true;
  const box = $("jinx");
  box.innerHTML = `<div class="jinx-card" id="jinxCard"><div class="jinx-title">Pech-Walze</div><div class="jinx-sub">Dreimal ${j.name} kostet einen Teil des Einsatzes</div><div class="jinx-slots">${[0, 1, 2].map(i => `<div class="jinx-slot" id="jxs${i}"><span class="jx-roll">?</span></div>`).join("")}</div><div class="jinx-amt" id="jinxAmt"></div><div class="jinx-note" id="jinxNote"></div></div>`;
  box.hidden = false;
  try { tone(150, .5, { type: "sawtooth", vol: .1, slide: .5 }); } catch (e) {}
  for (let i = 0; i < 3; i++) {
    await wait((i ? 380 : 520) * T());
    $("jxs" + i).innerHTML = j.svg; $("jxs" + i).classList.add("hit");
    try { tone(240 - i * 50, .22, { type: "square", vol: .09 }); } catch (e) {}
  }
  await wait(260 * T());
  const card = $("jinxCard"); card.classList.add("shake");
  document.body.classList.add("jinx-flash");
  try { tone(90, .7, { type: "sawtooth", vol: .14, slide: .4 }); noise(.35, .12, 0, 900); } catch (e) {}
  $("jinxAmt").textContent = `−${fmtN(x)} Credits`;
  $("jinxNote").textContent = `${Math.round(x / b * 100)} % deines Einsatzes von ${fmtN(b)}`;
  state.credits -= x; countCredits(state.credits, 500);
  sess.won -= x; bump("jinx");
  radio(`Funk: Pech-Walze! Dreimal ${j.name}. Das kostet ${fmtN(x)} Credits.`, true);
  render(); saveGame();
  bip("jinx", 2);
  await wait(1500 * T());
  card.classList.remove("shake"); card.classList.add("out"); document.body.classList.remove("jinx-flash");
  await wait(340);
  box.hidden = true; box.innerHTML = "";
  jinxBusy = false; mmResume();
}
const spinMenuBase = spin;
let mmPending = null;
function mmResume() { if (!mmPending) return; setTimeout(() => { if (!mmPending || mmBlocking()) return; const a = mmPending; mmPending = null; spin(...a); }, 300); }
spin = function (auto) {
  if (mmBlocking()) { if (inFs() || autoLeft > 0) mmPending = [...arguments]; return; }
  const n = state.spins, r = spinMenuBase.apply(this, arguments);
  if (state.spins > n) jinxArmed = true;
  return r;
};
const progressMenuBase = processProgress;
processProgress = async function () {
  await progressMenuBase.apply(this, arguments);
  if (!jinxArmed) return;
  jinxArmed = false;
  if (!jinxOn || inFs() || state.credits <= 0) return;
  if (--jinxLeft > 0) return;
  jinxLeft = JINX_MIN + ((Math.random() * (JINX_MAX - JINX_MIN + 1)) | 0);
  await runJinx();
};
// Tastatur: Menü/Dialoge zuerst bedienen, Leertaste startet dann keinen Dreh im Hintergrund
addEventListener("keydown", e => {
  const ingame = mmOpen("intro") && $("intro").classList.contains("ingame");
  if (e.key === "Escape") {
    if (mmOpen("mmSet")) { closeSettings(); e.stopImmediatePropagation(); return; }
    if (mmOpen("fsBuy")) { closeFsBuy(); e.stopImmediatePropagation(); return; }
    if (ingame) { closeMainMenu(); e.stopImmediatePropagation(); return; }
  }
  if ((e.code === "Space" || e.code === "Enter") && (mmOpen("mmSet") || mmOpen("fsBuy") || ingame || jinxBusy)) {
    if (e.target instanceof HTMLButtonElement || (e.target.closest && e.target.closest("input, select, a"))) { e.stopImmediatePropagation(); return; }
    e.preventDefault(); e.stopImmediatePropagation();
    if (ingame && e.code !== "Space") closeMainMenu();
  }
}, true);
HELP_RULES.unshift(
  ["#menuBtn", () => ["Hauptmenü", `Zurück zum Hauptmenü von ${COLLECTION}: Welt wechseln, Einstellungen, weiterspielen.`]],
  ["#setBtn, #mmSettings", () => ["Einstellungen", "Ton, Musik, Turbo, Begleiter, Pech-Walze, Sprache und Spielstand an einem Ort."]],
  ["#fsBuyBtn", () => ["Freispiele kaufen", `Drei Pakete: ${FS_BUY.map(p => `<b>${p.n}</b> für <b>${fmtN(fsPrice(p))}</b>`).join(", ")} Credits beim aktuellen Einsatz. Geht nur zwischen den Drehs.`]],
  [".mmw", () => ["Welten", "Jede Welt ist ein eigenes Spiel mit eigenem Spielstand. Du kannst jederzeit zurück."]],
);
'''
