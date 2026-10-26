# Training (Spielgeld → XP), Plinko und bessere Lesbarkeit (seit SW 0.16.0).
# Wird von tools/menu_apply.py zusammen mit menu_parts.py in index.html eingesetzt.

EXTRA_CSS = r'''

/* ---------- Breite Bildschirme (Ultrawide, 1440p, 4K): drei Spalten, größere Walzen ---------- */
@media (min-width: 1680px) {
  .app { max-width: 1900px; grid-template-columns: 380px minmax(0, 1fr) 470px; grid-template-rows: auto; grid-template-areas: "dock machine hangar"; }
  .dock .dockgrid, .dock .xtiles { grid-template-columns: 1fr; }
  .dock .labgrid { grid-template-columns: 1fr 1fr; }
  .frame { --cell: min(150px, calc((100cqw - 124px) / 5), max(108px, calc((100vh - 500px) / 3))); }
  /* Walzen nicht breiter ziehen als nötig, sonst werden die Felder flach */
  .stage .frame { max-width: calc(var(--cell) * 6.6 + 120px); margin-inline: auto; }
}
@media (min-width: 2300px) {
  .app { max-width: 2520px; grid-template-columns: 440px minmax(0, 1fr) 560px; gap: 24px; }
  .frame { --cell: min(180px, calc((100cqw - 124px) / 5), max(116px, calc((100vh - 480px) / 3))); }
}
/* ---------- Walzensymbole passen immer ins Feld (seit SW 0.17.1) ---------- */
html body .reel .sym { container-type: size; }
html body .reel .sym svg { max-height: 74cqh; max-width: 74cqh; }
html body .reel .sym.feature svg { max-height: 88cqh; max-width: 88cqh; }
/* ---------- Lesbarkeit: deaktivierte Knöpfe bleiben gut lesbar (seit SW 0.16.0) ---------- */
html body .bbtn:disabled, html body button.bbtn[disabled] { opacity: 1; background: rgba(255,255,255,.07); color: rgba(255,255,255,.86); box-shadow: inset 0 0 0 1.5px rgba(255,255,255,.3); text-shadow: none; filter: none; cursor: not-allowed; }
html body .vehcard .bbtn:disabled { opacity: 1; }
html body .bbtn:not(:disabled) { background: var(--bc, var(--gold, #ffc94a)); }
html body .vehcard .bbtn { --bc: var(--lime, #b8ff5c); }
html body .ghost:disabled { opacity: .72; }
html body .auto button:disabled, html body .chip:disabled { opacity: .66; }
html body .bbtn { text-shadow: 0 1px 0 rgba(255,255,255,.25); }

/* ---------- Bordzentrale: neue Kacheln ---------- */
.xtiles { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 12px 0 4px; }
.xtile { display: flex; align-items: center; gap: 10px; text-align: left; padding: 12px; border-radius: 14px; border: 1.5px solid rgba(255,255,255,.16); background: rgba(255,255,255,.05); color: inherit; cursor: pointer; font: inherit; transition: transform .15s, border-color .15s, background .15s; }
.xtile:hover { transform: translateY(-2px); border-color: var(--xc); background: color-mix(in srgb, var(--xc) 12%, transparent); }
.xtile:disabled { opacity: .6; cursor: not-allowed; transform: none; }
.xtile svg { width: 38px; height: 38px; flex: none; }
.xtile b { display: block; font-size: 14px; }
.xtile small { display: block; font-size: 11.5px; opacity: .78; line-height: 1.3; }

/* ---------- Training ---------- */
.xpgame .bonus-card, .plinkodlg .bonus-card { max-width: 760px; background: linear-gradient(180deg, rgba(22,24,34,.98), rgba(10,12,18,.98)); color: #f2f2f6; }
.xpgame, .plinkodlg { z-index: 260 !important; overflow-y: auto; }
.xp-pick { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; margin: 6px 0 10px; }
.xp-pick button { padding: 12px 8px; border-radius: 12px; border: 1.5px solid rgba(255,255,255,.18); background: rgba(255,255,255,.05); color: #fff; font: inherit; cursor: pointer; display: flex; flex-direction: column; gap: 3px; align-items: center; }
.xp-pick button[aria-pressed="true"] { border-color: var(--xt); background: color-mix(in srgb, var(--xt) 16%, transparent); }
.xp-pick button:disabled { opacity: .45; cursor: not-allowed; }
.xp-pick b { font-size: 18px; }
.xp-pick small { font-size: 11px; opacity: .75; }
.xp-track { position: relative; height: 76px; border-radius: 14px; overflow: hidden; margin: 10px 0 8px; background: var(--xbg); border: 1.5px solid rgba(255,255,255,.18); }
.xp-zones { position: absolute; inset: 22px 10px; border-radius: 8px; background: linear-gradient(90deg, #6a2730 0 18%, #a8892e 18% 34%, #3f9a5a 34% 44%, #ffd54a 44% 56%, #3f9a5a 56% 66%, #a8892e 66% 82%, #6a2730 82% 100%); opacity: .92; box-shadow: inset 0 0 0 1px rgba(0,0,0,.4); }
.xp-marker { position: absolute; top: 6px; width: 34px; height: 64px; margin-left: -17px; left: 10px; display: grid; place-items: center; filter: drop-shadow(0 2px 4px rgba(0,0,0,.7)); }
.xp-marker svg { width: 34px; height: 64px; }
.xp-rounds { display: flex; gap: 8px; justify-content: center; margin: 6px 0; }
.xp-rounds span { min-width: 74px; padding: 6px 8px; border-radius: 10px; background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.14); font: 700 12px/1.2 var(--f-mono, monospace); text-align: center; }
.xp-rounds span.g { border-color: #ffd54a; color: #ffd54a; } .xp-rounds span.o { border-color: #5fd38a; color: #7fe3a2; } .xp-rounds span.y { border-color: #d6b74a; color: #e6cc70; } .xp-rounds span.r { border-color: #d0596a; color: #ff8a98; }
.xp-res { text-align: center; font: 800 26px/1.2 var(--f-display, inherit); color: var(--xt); min-height: 32px; }
.xp-note { text-align: center; font-size: 12.5px; opacity: .8; min-height: 18px; }
.xp-flash { animation: xpFlash .4s ease; }
@keyframes xpFlash { 0% { filter: brightness(2); } 100% { filter: none; } }

/* ---------- Plinko ---------- */
.pl-wrap { display: grid; grid-template-columns: minmax(0, 1fr) 210px; gap: 14px; align-items: start; }
.pl-board { position: relative; border-radius: 16px; overflow: hidden; background: var(--pbg); border: 1.5px solid rgba(255,255,255,.16); aspect-ratio: 1 / .92; }
.pl-board svg { width: 100%; height: 100%; display: block; }
.pl-side { display: flex; flex-direction: column; gap: 10px; }
.pl-box { padding: 10px; border-radius: 12px; background: rgba(255,255,255,.05); border: 1px solid rgba(255,255,255,.12); }
.pl-box h4 { margin: 0 0 6px; font: 700 10.5px/1 var(--f-mono, monospace); letter-spacing: .16em; text-transform: uppercase; opacity: .7; }
.pl-seg { display: grid; grid-template-columns: repeat(3, 1fr); gap: 4px; }
.pl-seg button, .pl-bet button { padding: 7px 4px; border-radius: 8px; border: 1px solid rgba(255,255,255,.2); background: rgba(255,255,255,.05); color: #fff; font: 700 12px/1 var(--f-body, inherit); cursor: pointer; }
.pl-bet button { min-width: 36px; height: 32px; font-size: 16px; }
.pl-seg button[aria-pressed="true"] { background: var(--pa); color: #0a0c14; border-color: transparent; }
.pl-seg button:disabled, .pl-bet button:disabled { opacity: .45; cursor: not-allowed; }
.pl-bet { display: flex; align-items: center; gap: 6px; }
.pl-bet output { flex: 1; text-align: center; font: 800 18px/1 var(--f-display, inherit); }
.pl-drop { width: 100%; padding: 14px 10px; border-radius: 12px; border: 0; cursor: pointer; font: 800 15px/1 var(--f-display, inherit); letter-spacing: .06em; text-transform: uppercase; color: #0a0c14; background: var(--pa); box-shadow: 0 4px 0 rgba(0,0,0,.4), 0 0 24px color-mix(in srgb, var(--pa) 40%, transparent); }
.pl-drop:active { transform: translateY(2px); box-shadow: 0 2px 0 rgba(0,0,0,.4); }
.pl-drop:disabled { background: rgba(255,255,255,.08); color: rgba(255,255,255,.75); box-shadow: inset 0 0 0 1.5px rgba(255,255,255,.25); cursor: not-allowed; }
.pl-auto { width: 100%; padding: 9px; border-radius: 10px; border: 1px solid rgba(255,255,255,.22); background: rgba(255,255,255,.05); color: #fff; font: 700 12px/1 var(--f-body, inherit); cursor: pointer; }
.pl-auto[aria-pressed="true"] { border-color: var(--pa); color: var(--pa); }
.pl-stat { display: flex; justify-content: space-between; font-size: 12.5px; padding: 3px 0; }
.pl-stat b { font-family: var(--f-mono, monospace); }
.pl-last { font: 800 22px/1.1 var(--f-display, inherit); text-align: center; min-height: 26px; color: var(--pa); }
.pl-bin { transition: transform .15s; transform-box: fill-box; transform-origin: center; }
.pl-bin.hit { animation: plHit .45s ease; }
@keyframes plHit { 0% { transform: translateY(0); } 30% { transform: translateY(5px) scale(1.06); } 100% { transform: none; } }
.pl-float { position: absolute; transform: translate(-50%, -100%); font: 800 15px/1 var(--f-display, inherit); color: #fff; text-shadow: 0 2px 6px rgba(0,0,0,.8); pointer-events: none; animation: plFloat 1s ease-out forwards; }
@keyframes plFloat { from { opacity: 1; margin-top: 0; } to { opacity: 0; margin-top: -40px; } }
@media (max-width: 680px) { .pl-wrap { grid-template-columns: 1fr; } .xtiles { grid-template-columns: 1fr; } .xp-pick { grid-template-columns: 1fr 1fr 1fr; } .xp-rounds span { min-width: 0; flex: 1; } }
'''

EXTRA_JS = r'''
/* ---------- Training (Spielgeld → XP) und Plinko (seit SW 0.16.0) ---------- */
const XP_THEME = {
  sternenwrack: { name: "Flugsimulator", verb: "Kurs halten", sub: "Investiere Credits in Simulatorstunden. Stoppe das Schiff dreimal möglichst in der goldenen Mitte.", color: "#4fe3ff",
    bg: "radial-gradient(ellipse at 30% 40%, rgba(139,108,255,.35), transparent 60%), #070a1c", marker: `<svg viewBox="0 0 34 64"><path d="M17 4 L27 30 L17 26 L7 30 Z" fill="#dfe6ff" stroke="#4fe3ff" stroke-width="2"/><path d="M13 30 L17 40 L21 30" fill="#ff9a3c"/><path d="M17 42 V60" stroke="#4fe3ff" stroke-width="2" stroke-dasharray="3 3"/></svg>`,
    icon: `<svg viewBox="0 0 40 40" aria-hidden="true"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#071a26" stroke="#4fe3ff" stroke-width="2"/><path d="M20 8 L27 26 L20 23 L13 26 Z" fill="#dfe6ff" stroke="#4fe3ff" stroke-width="1.6"/><circle cx="20" cy="31" r="3" fill="none" stroke="#ffc94a" stroke-width="1.6"/></svg>` },
  treibgut: { name: "Knotenschule", verb: "Knoten ziehen", sub: "Investiere Muscheln in Seemannskurse. Ziehe den Knoten dreimal im richtigen Moment fest.", color: "#ffb36b",
    bg: "repeating-linear-gradient(180deg, #1f6f8a 0 12px, #23799a 12px 24px)", marker: `<svg viewBox="0 0 34 64"><path d="M17 2 V22" stroke="#e8d2a0" stroke-width="4"/><circle cx="17" cy="30" r="9" fill="none" stroke="#e8d2a0" stroke-width="4"/><path d="M10 37 L4 60 M24 37 L30 60" stroke="#e8d2a0" stroke-width="4" stroke-linecap="round"/></svg>`,
    icon: `<svg viewBox="0 0 40 40" aria-hidden="true"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#2a1808" stroke="#ffb36b" stroke-width="2"/><circle cx="20" cy="18" r="7" fill="none" stroke="#e8d2a0" stroke-width="3"/><path d="M14 23 L10 33 M26 23 L30 33" stroke="#e8d2a0" stroke-width="3" stroke-linecap="round"/></svg>` },
  eisenfront: { name: "Schießstand", verb: "Abdrücken", sub: "Investiere Schrauben in Schießübungen. Triff die Zielscheibe dreimal möglichst in der Mitte.", color: "#c9d68a",
    bg: "repeating-linear-gradient(-45deg, #2a2c26 0 14px, #34362e 14px 28px)", marker: `<svg viewBox="0 0 34 64"><circle cx="17" cy="32" r="13" fill="none" stroke="#ff5a4a" stroke-width="2.4"/><path d="M17 12 V24 M17 40 V52 M3 32 H11 M23 32 H31" stroke="#ff5a4a" stroke-width="2.4"/><circle cx="17" cy="32" r="2.4" fill="#ff5a4a"/></svg>`,
    icon: `<svg viewBox="0 0 40 40" aria-hidden="true"><rect x="1.5" y="1.5" width="37" height="37" rx="6" fill="#1a1c10" stroke="#c9d68a" stroke-width="2"/><circle cx="20" cy="20" r="10" fill="none" stroke="#c9d68a" stroke-width="2"/><circle cx="20" cy="20" r="5" fill="none" stroke="#c9d68a" stroke-width="2"/><circle cx="20" cy="20" r="1.6" fill="#ff5a4a"/></svg>` },
  neustadt: { name: "Bauakademie", verb: "Stein setzen", sub: "Investiere Taler in Lehrgänge. Setze den Ziegel dreimal möglichst genau auf die Markierung.", color: "#7ee0c8",
    bg: "linear-gradient(rgba(126,224,200,.12) 1px, transparent 1px) 0 0 / 14px 14px, linear-gradient(90deg, rgba(126,224,200,.12) 1px, transparent 1px) 0 0 / 14px 14px, #13324e", marker: `<svg viewBox="0 0 34 64"><path d="M17 2 V18" stroke="#ffc94a" stroke-width="2.4"/><rect x="4" y="18" width="26" height="14" rx="2" fill="#d2694a" stroke="#5a2414" stroke-width="2"/><path d="M17 18 V32 M4 25 H30" stroke="#5a2414" stroke-width="1.4"/><path d="M17 36 V60" stroke="#7ee0c8" stroke-width="2" stroke-dasharray="3 3"/></svg>`,
    icon: `<svg viewBox="0 0 40 40" aria-hidden="true"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#0c1a14" stroke="#7ee0c8" stroke-width="2"/><path d="M8 30 L20 10 L32 30 Z" fill="none" stroke="#7ee0c8" stroke-width="2"/><rect x="15" y="22" width="10" height="8" fill="#d2694a"/></svg>` },
};
const PL_THEME = {
  sternenwrack: { name: "Meteorschauer", ball: "#ffc94a", glow: "#ff9a3c", peg: "#9fb3ff", acc: "#4fe3ff", bg: "radial-gradient(ellipse at 50% 0%, rgba(139,108,255,.35), transparent 60%), #070a1c", sub: "Ein Meteor fällt durch das Asteroidenfeld." },
  treibgut: { name: "Kokosnuss-Fall", ball: "#8a5a2c", glow: "#e8b04a", peg: "#f4ecd8", acc: "#ffb36b", bg: "linear-gradient(180deg, #2c7fab, #1f5f7a)", sub: "Eine Kokosnuss kullert durch die Bojen." },
  eisenfront: { name: "Kugellager", ball: "#d6d8dc", glow: "#ffffff", peg: "#b8862e", acc: "#c9d68a", bg: "repeating-linear-gradient(-45deg, #24261f 0 14px, #2c2e26 14px 28px)", sub: "Eine Stahlkugel rattert durch die Bolzen." },
  neustadt: { name: "Baustellen-Plinko", ball: "#ff8a3c", glow: "#ffc94a", peg: "#7ee0c8", acc: "#7ee0c8", bg: "linear-gradient(180deg, #1c3a5a, #0b141d)", sub: "Eine Abrissbirne pendelt durch die Laternen." },
};
const xpTheme = () => XP_THEME[WORLD_ID] || XP_THEME.sternenwrack;
const plTheme = () => PL_THEME[WORLD_ID] || PL_THEME.sternenwrack;
const XP_PACKS = [10, 25, 50];                 // × Einsatz
const XP_ZONES = [[44, 56, 1, "g", "Perfekt"], [34, 66, .7, "o", "Gut"], [18, 82, .4, "y", "Knapp"], [0, 100, .1, "r", "Daneben"]];
const XP_RATE = c => 0.5 + 2.5 * c;            // XP pro Credit: 0,5 (alles daneben) bis 3 (dreimal perfekt)
const PL_ROWS = 12;
const PL_MULT = {
  low: [10, 3, 1.6, 1.4, 1.1, 1, .5, 1, 1.1, 1.4, 1.6, 3, 10],
  mid: [33, 11, 4, 2, 1.1, .6, .3, .6, 1.1, 2, 4, 11, 33],
  high: [170, 24, 8.1, 2, .7, .2, .2, .2, .7, 2, 8.1, 24, 170],
};   // Erwartungswert je ~99 % (Binomial, 12 Reihen)
const fmtM = m => (m >= 10 ? String(Math.round(m)) : String(m).replace(".", ",")) + "×";

/* --- Kacheln in der Bordzentrale und im Hauptmenü --- */
(function setupExtraTiles() {
  const xt = xpTheme(), pt = plTheme();
  const html = `<div class="xtiles"><button type="button" class="xtile" id="xpTile" style="--xc:${xt.color}">${xt.icon}<span><b>${xt.name}</b><small>Credits in XP umwandeln · Minispiel</small></span></button>
    <button type="button" class="xtile" id="plTile" style="--xc:${pt.acc}"><svg viewBox="0 0 40 40" aria-hidden="true"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="rgba(0,0,0,.35)" stroke="${pt.acc}" stroke-width="2"/>${[[20, 10], [14, 17], [26, 17], [8, 24], [20, 24], [32, 24]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="1.8" fill="${pt.peg}"/>`).join("")}<circle cx="17" cy="13" r="3" fill="${pt.ball}" stroke="${pt.glow}" stroke-width="1"/><path d="M5 31 H35" stroke="${pt.acc}" stroke-width="2"/><path d="M11 31v4M17 31v4M23 31v4M29 31v4" stroke="${pt.acc}" stroke-width="1.4"/></svg><span><b>Plinko · ${pt.name}</b><small>Ball fallen lassen, Multiplikator gewinnen</small></span></button></div>`;
  const grid = document.querySelector(".dock .dockgrid");
  if (grid) grid.insertAdjacentHTML("afterend", html);
  $("xpTile") && $("xpTile").addEventListener("click", openXpGame);
  $("plTile") && $("plTile").addEventListener("click", openPlinko);
  const row = document.querySelector("#intro .mm-row");
  if (row) {
    row.insertAdjacentHTML("beforeend", `<button type="button" id="mmPlinko"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="3" r="1.6" fill="currentColor"/><circle cx="5" cy="7" r="1.2" fill="currentColor"/><circle cx="11" cy="7" r="1.2" fill="currentColor"/><circle cx="8" cy="10" r="1.2" fill="currentColor"/><path d="M2 14h12" stroke="currentColor" stroke-width="1.6"/></svg>Plinko</button>`);
    $("mmPlinko").addEventListener("click", () => { const el = $("intro"); if (el.classList.contains("ingame")) closeMainMenu(); else $("introBtn").click(); setTimeout(openPlinko, 700); });
  }
})();

/* --- Training: Spielgeld in XP umwandeln --- */
document.body.insertAdjacentHTML("beforeend", `<div class="bonus xpgame" id="xpGame" hidden>
  <div class="bonus-card glass" style="--bc: var(--cyan)" role="dialog" aria-modal="true" aria-labelledby="xpTitle">
    <header><span id="xpIcon"></span><div><h2 id="xpTitle"></h2><p id="xpSub"></p></div></header>
    <div id="xpStep1">
      <div class="xp-pick" id="xpPick"></div>
      <p class="xp-note" id="xpRateNote"></p>
      <div class="bonus-foot"><div class="note">Das eingesetzte Spielgeld wird verbraucht. Je genauer du triffst, desto mehr XP gibt es.</div><button type="button" class="bbtn" id="xpStart" style="--bc:var(--xt)">Training starten</button></div>
    </div>
    <div id="xpStep2" hidden>
      <div class="xp-track" id="xpTrack"><div class="xp-zones"></div><div class="xp-marker" id="xpMarker"></div></div>
      <div class="xp-rounds" id="xpRounds"></div>
      <div class="xp-res" id="xpRes"></div>
      <p class="xp-note" id="xpNote"></p>
      <div class="bonus-foot"><div class="note">Stopp mit dem Knopf oder der Leertaste.</div><button type="button" class="bbtn" id="xpStop" style="--bc:var(--xt)">Stopp</button></div>
    </div>
    <div class="bonus-foot" id="xpFootClose"><div></div><button type="button" class="ghost" id="xpClose">Schließen</button></div>
  </div>
</div>`);
let xpSel = 1, xpRun = null;
function xpCost(i) { return Math.max(1, XP_PACKS[i] * bet()); }
function renderXpPick() {
  const t = xpTheme();
  $("xpGame").style.setProperty("--xt", t.color);
  $("xpIcon").innerHTML = t.icon.replace('aria-hidden="true"', 'aria-hidden="true" width="52" height="52"');
  $("xpTitle").textContent = `${t.name}: Credits in XP`;
  $("xpSub").textContent = t.sub;
  if (state.credits < xpCost(xpSel)) { const ok = XP_PACKS.findIndex((_, i) => state.credits >= xpCost(i)); xpSel = ok < 0 ? 0 : ok; }
  $("xpPick").innerHTML = XP_PACKS.map((x, i) => `<button type="button" data-xp="${i}" aria-pressed="${i === xpSel}"${state.credits >= xpCost(i) ? "" : " disabled"}><b>${fmtN(xpCost(i))}</b><small>Credits · ${x}× Einsatz</small><small>bis ${fmtN(xpCost(i) * XP_RATE(1))} XP</small></button>`).join("");
  $("xpRateNote").textContent = `Pro Credit gibt es 0,5 XP (alles daneben) bis 3 XP (dreimal perfekt). Dein Rang: ${state.level}, noch ${fmtN(xpNeed(state.level) - state.xp)} XP bis zum nächsten.`;
  $("xpStart").disabled = state.credits < xpCost(xpSel);
}
function openXpGame() {
  if (!machineIdle()) return;
  if (autoLeft > 0) { autoLeft = 0; clearAutoMarks(); }
  $("xpStep1").hidden = false; $("xpStep2").hidden = true; $("xpFootClose").hidden = false;
  renderXpPick(); $("xpGame").hidden = false; try { sfx.click(); } catch (e) {}
}
function closeXpGame() { if (xpRun && !xpRun.done) return; $("xpGame").hidden = true; xpRun = null; try { sfx.click(); } catch (e) {} mmResume(); }
function xpRound() {
  const r = xpRun, mk = $("xpMarker"), track = $("xpTrack");
  r.pos = 0; r.dir = 1; r.speed = 55 + r.round * 22 + Math.random() * 10;   // Prozent pro Sekunde
  let last = performance.now();
  const step = now => {
    if (!xpRun || r.stopped) return;
    const dt = Math.min(.05, (now - last) / 1000); last = now;
    r.pos += r.dir * r.speed * dt;
    if (r.pos >= 100) { r.pos = 100; r.dir = -1; } else if (r.pos <= 0) { r.pos = 0; r.dir = 1; }
    const w = track.clientWidth - 20; mk.style.left = (10 + w * r.pos / 100) + "px";
    r.raf = requestAnimationFrame(step);
  };
  r.stopped = false; r.raf = requestAnimationFrame(step);
  $("xpStop").disabled = false; $("xpStop").focus({ preventScroll: true });
}
function xpStop() {
  const r = xpRun; if (!r || r.stopped || r.done) return;
  r.stopped = true; cancelAnimationFrame(r.raf); $("xpStop").disabled = true;
  const z = XP_ZONES.find(([a, b]) => r.pos >= a && r.pos <= b) || XP_ZONES[3];
  r.scores.push(z[2]);
  const cell = $("xpRounds").children[r.round]; cell.className = z[3]; cell.textContent = z[4];
  $("xpTrack").classList.remove("xp-flash"); void $("xpTrack").offsetWidth; $("xpTrack").classList.add("xp-flash");
  try { z[2] >= 1 ? sfx.small() : tone(300 + z[2] * 600, .16, { type: "square", vol: .07 }); } catch (e) {}
  r.round++;
  if (r.round < 3) { $("xpNote").textContent = `${z[4]}! Noch ${3 - r.round} ${3 - r.round === 1 ? "Versuch" : "Versuche"}.`; setTimeout(xpRound, 650); return; }
  xpFinish();
}
async function xpFinish() {
  const r = xpRun, avg = r.scores.reduce((a, b) => a + b, 0) / 3, xp = Math.round(r.cost * XP_RATE(avg));
  r.done = true;
  const before = state.level;
  addXP(xp); bump("xpTrain"); bump("xpBought", xp);
  $("xpRes").textContent = `+${fmtN(xp)} XP`;
  $("xpNote").textContent = `${fmtN(r.cost)} Credits umgewandelt · ${String(XP_RATE(avg).toFixed(1)).replace(".", ",")} XP pro Credit${state.level > before ? ` · Rang ${state.level} erreicht!` : ""}`;
  try { sfx.mission ? sfx.mission() : sfx.small(); } catch (e) {}
  radio(`Funk: ${xpTheme().name} abgeschlossen. +${fmtN(xp)} XP.`, true);
  addLog("up_engine", xpTheme().name, `+${fmtN(xp)} XP`, xpTheme().color);
  $("xpStop").hidden = true; $("xpFootClose").hidden = false;
  render(); saveGame();
  setTimeout(() => { if (!$("xpGame").hidden) return; }, 0);
}
async function xpBegin() {
  const cost = xpCost(xpSel);
  if (spinning || busy || inFs() || state.credits < cost) return;
  state.credits -= cost; countCredits(state.credits, 300); sess.bet += cost;
  xpRun = { cost, round: 0, scores: [], done: false };
  $("xpStep1").hidden = true; $("xpStep2").hidden = false; $("xpFootClose").hidden = true; $("xpStop").hidden = false;
  $("xpMarker").innerHTML = xpTheme().marker; $("xpTrack").style.setProperty("--xbg", xpTheme().bg);
  $("xpRounds").innerHTML = "<span>1</span><span>2</span><span>3</span>"; $("xpRes").textContent = ""; $("xpNote").textContent = `${xpTheme().verb}: dreimal stoppen.`;
  render(); setTimeout(xpRound, 350);
}
$("xpPick").addEventListener("click", e => { const b = e.target.closest("[data-xp]"); if (!b || b.disabled) return; xpSel = +b.dataset.xp; renderXpPick(); try { sfx.click(); } catch (er) {} });
$("xpStart").addEventListener("click", xpBegin);
$("xpStop").addEventListener("click", xpStop);
$("xpClose").addEventListener("click", async () => { const r = xpRun; closeXpGame(); if (r && r.done) { busy = true; try { await processProgress(); } catch (e) {} busy = false; render(); } });
$("xpGame").addEventListener("click", e => { if (e.target.id === "xpGame") $("xpClose").click(); });

/* --- Plinko --- */
document.body.insertAdjacentHTML("beforeend", `<div class="bonus plinkodlg" id="plinko" hidden>
  <div class="bonus-card glass" style="--bc: var(--cyan)" role="dialog" aria-modal="true" aria-labelledby="plTitle">
    <header><span id="plIcon"></span><div><h2 id="plTitle"></h2><p id="plSub"></p></div></header>
    <div class="pl-wrap">
      <div class="pl-board" id="plBoard"><svg id="plSvg" viewBox="0 0 520 480" aria-label="Plinko-Feld"></svg></div>
      <div class="pl-side">
        <div class="pl-box"><h4>Einsatz pro Ball</h4><div class="pl-bet"><button type="button" id="plBetDown" aria-label="Einsatz senken">−</button><output id="plBet">10</output><button type="button" id="plBetUp" aria-label="Einsatz erhöhen">+</button></div></div>
        <div class="pl-box"><h4>Risiko</h4><div class="pl-seg" id="plRisk"><button type="button" data-r="low">Niedrig</button><button type="button" data-r="mid">Mittel</button><button type="button" data-r="high">Hoch</button></div></div>
        <button type="button" class="pl-drop" id="plDrop">Ball fallen lassen</button>
        <button type="button" class="pl-auto" id="plAuto" aria-pressed="false">Auto · 10 Bälle</button>
        <div class="pl-last" id="plLast"></div>
        <div class="pl-box"><div class="pl-stat"><span>Credits</span><b id="plCred">0</b></div><div class="pl-stat"><span>Bälle</span><b id="plCount">0</b></div><div class="pl-stat"><span>Gewinn hier</span><b id="plNet">0</b></div></div>
      </div>
    </div>
    <div class="bonus-foot"><div class="note">Jeder Ball wird an jedem Hindernis zufällig nach links oder rechts abgelenkt. Außen warten die großen Multiplikatoren.</div><button type="button" class="ghost" id="plClose">Schließen</button></div>
  </div>
</div>`);
let plRisk = "mid", plBalls = 0, plAutoLeft = 0, plStats = { n: 0, net: 0 };
try { plRisk = localStorage.getItem("welten-plrisk") || "mid"; if (!PL_MULT[plRisk]) plRisk = "mid"; } catch (e) {}
const PL_W = 520, PL_TOP = 40, PL_GAP = 31, PL_DX = 36;
const plPeg = (row, i) => ({ x: PL_W / 2 + (i - (row + 1) / 2) * PL_DX, y: PL_TOP + row * PL_GAP });   // Reihe r hat r + 2 Hindernisse
function plBinColor(m) { return m >= 20 ? "#ff4b6a" : m >= 5 ? "#ff8a3c" : m >= 2 ? "#ffc94a" : m >= 1 ? "#7fe3a2" : "#6f7a96"; }
function renderPlinko() {
  const t = plTheme(), mult = PL_MULT[plRisk];
  $("plinko").style.setProperty("--pa", t.acc); $("plBoard").style.setProperty("--pbg", t.bg);
  $("plTitle").textContent = `Plinko · ${t.name}`; $("plSub").textContent = `${t.sub} Unten wartet ein Multiplikator auf deinen Einsatz.`;
  $("plIcon").innerHTML = $("plTile") ? $("plTile").querySelector("svg").outerHTML.replace('aria-hidden="true"', 'aria-hidden="true" width="52" height="52"') : "";
  let pegs = "";
  for (let r = 1; r <= PL_ROWS; r++) for (let i = 0; i <= r + 1; i++) { const p = plPeg(r, i); pegs += `<circle cx="${p.x}" cy="${p.y}" r="4.2" fill="${t.peg}" opacity=".9"/>`; }
  const by = PL_TOP + (PL_ROWS + 1) * PL_GAP - 6, bw = PL_DX - 3;
  const bins = mult.map((m, k) => { const x = PL_W / 2 + (k - PL_ROWS / 2) * PL_DX; return `<g class="pl-bin" id="plBin${k}"><rect x="${x - bw / 2}" y="${by}" width="${bw}" height="30" rx="6" fill="${plBinColor(m)}"/><text x="${x}" y="${by + 20}" text-anchor="middle" font-size="${m >= 100 ? 11 : 12}" font-weight="800" fill="#0a0c14" font-family="system-ui, sans-serif">${fmtM(m)}</text></g>`; }).join("");
  $("plSvg").innerHTML = `<defs><radialGradient id="plBall"><stop offset="0" stop-color="#fff"/><stop offset=".45" stop-color="${t.ball}"/><stop offset="1" stop-color="${t.glow}"/></radialGradient></defs><path d="M${PL_W / 2 - 18} 8 h36 l-8 18 h-20 z" fill="rgba(255,255,255,.12)" stroke="${t.acc}" stroke-width="1.5"/>${pegs}${bins}<g id="plBallLayer"></g>`;
  document.querySelectorAll("#plRisk button").forEach(b => b.setAttribute("aria-pressed", String(b.dataset.r === plRisk)));
  plUi();
}
function plUi() {
  $("plBet").textContent = fmtN(bet());
  $("plCred").textContent = fmtN(state.credits);
  $("plCount").textContent = fmtN(plStats.n);
  $("plNet").textContent = (plStats.net >= 0 ? "+" : "") + fmtN(plStats.net);
  const lock = plBalls > 0;
  document.querySelectorAll("#plRisk button").forEach(b => { b.disabled = lock; });
  $("plBetDown").disabled = lock; $("plBetUp").disabled = lock;
  $("plDrop").disabled = state.credits < bet();
  $("plAuto").setAttribute("aria-pressed", String(plAutoLeft > 0));
  $("plAuto").textContent = plAutoLeft > 0 ? `Stopp · noch ${plAutoLeft}` : "Auto · 10 Bälle";
}
function openPlinko() {
  if (!machineIdle()) return;
  if (autoLeft > 0) { autoLeft = 0; clearAutoMarks(); }
  plStats = { n: 0, net: 0 }; $("plLast").textContent = "";
  renderPlinko(); $("plinko").hidden = false; try { sfx.click(); } catch (e) {}
  $("plDrop").focus({ preventScroll: true });
}
function closePlinko() {
  if (plBalls > 0) { plAutoLeft = 0; plUi(); return; }
  $("plinko").hidden = true; plAutoLeft = 0; try { sfx.click(); } catch (e) {}
  if (plStats.n) { radio(`Funk: Plinko beendet. ${fmtN(plStats.n)} Bälle, ${(plStats.net >= 0 ? "+" : "") + fmtN(plStats.net)} Credits.`); }
  render(); saveGame();
  busy = true; processProgress().catch(() => {}).finally(() => { busy = false; render(); mmResume(); });
}
function plDrop() {
  const b = bet();
  if (state.credits < b) { plAutoLeft = 0; plUi(); return false; }
  state.credits -= b; countCredits(state.credits, 200);
  sess.bet += b; addXP(b); bump("plinko"); plStats.n++; plStats.net -= b;
  plBalls++;
  // Weg: in jeder Reihe 50 % links oder rechts
  let k = 0; const path = [];
  for (let r = 1; r <= PL_ROWS; r++) { const right = Math.random() < .5; path.push(right); if (right) k++; }
  const t = plTheme(), layer = $("plBallLayer");
  const ball = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  ball.setAttribute("r", "8"); ball.setAttribute("fill", "url(#plBall)"); ball.setAttribute("stroke", t.glow); ball.setAttribute("stroke-width", "1");
  layer.appendChild(ball);
  const pts = [{ x: PL_W / 2 + (Math.random() - .5) * 6, y: 14 }];
  let col = 0;
  for (let r = 1; r <= PL_ROWS; r++) { const peg = plPeg(r, col + 1); pts.push({ x: peg.x, y: peg.y - 12 }); if (path[r - 1]) col++; }
  const binX = PL_W / 2 + (k - PL_ROWS / 2) * PL_DX, binY = PL_TOP + (PL_ROWS + 1) * PL_GAP + 6;
  pts.push({ x: binX, y: binY });
  const seg = 95 * T();
  let i = 0, t0 = performance.now();
  const step = now => {
    const a = pts[i], z = pts[i + 1];
    const f = Math.min(1, (now - t0) / seg);
    const x = a.x + (z.x - a.x) * f, y = a.y + (z.y - a.y) * f - Math.sin(f * Math.PI) * 9;
    ball.setAttribute("cx", x.toFixed(1)); ball.setAttribute("cy", y.toFixed(1));
    if (f >= 1) {
      i++; t0 = now;
      if (i < pts.length - 1) { try { if (!reduced) tone(1200 + Math.random() * 500, .025, { type: "triangle", vol: .035 }); } catch (e) {} }
      if (i >= pts.length - 1) { ball.remove(); plLand(k, b); return; }
    }
    requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
  plUi();
  return true;
}
function plLand(k, b) {
  plBalls--;
  const m = PL_MULT[plRisk][k], win = Math.round(b * m);
  state.credits += win; plStats.net += win;
  state.best = Math.max(state.best, win); state.peak = Math.max(state.peak, state.credits);
  if (win > 0) { track("haul", win); sess.won += win; sess.best = Math.max(sess.best, win); }
  countCredits(state.credits, 300);
  const bin = $("plBin" + k); if (bin) { bin.classList.remove("hit"); void bin.getBBox(); bin.classList.add("hit"); }
  const board = $("plBoard"), x = (PL_W / 2 + (k - PL_ROWS / 2) * PL_DX) / PL_W * 100;
  const fl = document.createElement("span"); fl.className = "pl-float"; fl.style.left = x + "%"; fl.style.top = "84%"; fl.textContent = `${fmtM(m)}`; board.appendChild(fl); setTimeout(() => fl.remove(), 1000);
  $("plLast").textContent = `${fmtM(m)} · +${fmtN(win)}`;
  try { m >= 5 ? sfx.small() : m >= 1 ? tone(500 + m * 80, .12, { type: "square", vol: .06 }) : tone(220, .12, { type: "triangle", vol: .05 }); } catch (e) {}
  if (m >= 10) {
    addLog("crystal", `Plinko ${fmtM(m)}`, "+" + fmtN(win), plBinColor(m));
    radio(`Funk: Plinko-Treffer ${fmtM(m)}! +${fmtN(win)} Credits.`, true);
    try { burst(60, [plTheme().ball, plTheme().acc, "#ffffff"], .9); } catch (e) {}
  }
  if (m >= 24) setTimeout(() => addDust(1, "Plinko"), 600);
  plUi(); saveGame();
}
function plAutoNext() {
  if (plAutoLeft <= 0 || $("plinko").hidden) return;
  plAutoLeft--;
  if (!plDrop()) { plAutoLeft = 0; plUi(); return; }
  if (plAutoLeft > 0) setTimeout(plAutoNext, 380 * T());
  plUi();
}
$("plDrop").addEventListener("click", () => plDrop());
$("plAuto").addEventListener("click", () => { if (plAutoLeft > 0) { plAutoLeft = 0; plUi(); return; } plAutoLeft = 10; plAutoNext(); });
$("plRisk").addEventListener("click", e => { const b = e.target.closest("[data-r]"); if (!b || b.disabled) return; plRisk = b.dataset.r; try { localStorage.setItem("welten-plrisk", plRisk); } catch (er) {} renderPlinko(); try { sfx.click(); } catch (er) {} });
$("plBetDown").addEventListener("click", () => { const x = $("betDown"); if (x && !x.disabled) x.click(); plUi(); });
$("plBetUp").addEventListener("click", () => { const x = $("betUp"); if (x && !x.disabled) x.click(); plUi(); });
$("plClose").addEventListener("click", closePlinko);
$("plinko").addEventListener("click", e => { if (e.target.id === "plinko") closePlinko(); });
addEventListener("keydown", e => {
  const xpOn = mmOpen("xpGame"), plOn = mmOpen("plinko");
  if (!xpOn && !plOn) return;
  if (e.key === "Escape") { e.stopImmediatePropagation(); if (plOn) closePlinko(); else $("xpClose").click(); return; }
  if (e.code !== "Space" || e.repeat) return;
  if (e.target.closest && e.target.closest("input, select, textarea")) return;
  e.preventDefault(); e.stopImmediatePropagation();
  if (xpOn && xpRun && !xpRun.done) xpStop();
  else if (plOn) plDrop();
}, true);
HELP_RULES.unshift(
  ["#xpTile", () => [xpTheme().name, `Minispiel: Wandle Credits in XP um. Pro Credit gibt es 0,5 bis 3 XP, je nachdem, wie genau du dreimal stoppst.`]],
  ["#plTile, #mmPlinko", () => ["Plinko", "Ein Ball fällt durch zwölf Reihen Hindernisse und landet in einem Feld mit Multiplikator. Drei Risikostufen, außen bis 170×."]],
);
'''

RISK_CSS = r'''
/* ---------- Risikospiele neu: Kartenrisiko und Leiter (seit SW 0.17.0) ---------- */
.rk { display: grid; gap: 14px; }
.rk-steps { display: flex; gap: 6px; justify-content: center; flex-wrap: wrap; }
.rk-steps span { min-width: 54px; padding: 7px 10px; border-radius: 99px; text-align: center; font: 800 13px/1 var(--f-mono, monospace); background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.16); color: rgba(255,255,255,.7); transition: all .2s; }
.rk-steps span.on { background: var(--gold, #ffc94a); color: #0a0c14; border-color: transparent; box-shadow: 0 0 14px color-mix(in srgb, var(--gold, #ffc94a) 50%, transparent); }
.rk-steps span.next { border-color: var(--gold, #ffc94a); color: #fff; }
.rk-table { display: grid; place-items: center; perspective: 900px; padding: 4px 0; }
.rk-card { width: 138px; height: 190px; position: relative; }
.rk-in { position: absolute; inset: 0; transform-style: preserve-3d; transition: transform .28s cubic-bezier(.3,1.4,.5,1); }
.rk-card.flip .rk-in { transform: rotateY(180deg); }
.rk-card.quick .rk-in { transition-duration: .14s; }
.rk-face { position: absolute; inset: 0; border-radius: 14px; backface-visibility: hidden; display: grid; place-items: center; border: 2px solid rgba(255,255,255,.25); box-shadow: 0 10px 30px rgba(0,0,0,.45); }
.rk-back { background: repeating-linear-gradient(45deg, rgba(255,255,255,.07) 0 8px, transparent 8px 16px), linear-gradient(160deg, var(--ga), var(--gb)); }
.rk-back i { width: 54px; height: 54px; border-radius: 50%; border: 3px solid rgba(255,255,255,.75); box-shadow: inset 0 0 0 6px rgba(0,0,0,.25); }
.rk-front { transform: rotateY(180deg); background: #0b0d18; }
.rk-front svg { width: 92px; height: 92px; }
.rk-card.win .rk-front { border-color: #5dffa8; box-shadow: 0 0 30px rgba(93,255,168,.5); }
.rk-card.lose .rk-front { border-color: #ff5a6a; box-shadow: 0 0 30px rgba(255,90,106,.5); }
.rk-hist { display: flex; gap: 6px; justify-content: center; min-height: 14px; }
.rk-hist i { width: 12px; height: 12px; border-radius: 50%; box-shadow: 0 0 6px currentColor; }
.rk-pick { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.rk-pick button { padding: 16px 10px 12px; border-radius: 14px; border: 2px solid var(--gc); background: color-mix(in srgb, var(--gc) 18%, rgba(0,0,0,.3)); color: #fff; font: 800 16px/1.1 var(--f-display, inherit); letter-spacing: .04em; cursor: pointer; display: flex; flex-direction: column; align-items: center; gap: 5px; transition: transform .1s, background .15s, box-shadow .15s; }
.rk-pick button:hover { background: color-mix(in srgb, var(--gc) 32%, rgba(0,0,0,.3)); box-shadow: 0 0 22px color-mix(in srgb, var(--gc) 45%, transparent); }
.rk-pick button:active { transform: scale(.97); }
.rk-pick button i { width: 22px; height: 22px; border-radius: 50%; background: var(--gc); box-shadow: 0 0 12px var(--gc); }
.rk-pick button small, .rk-btn small, .rk-take small { font: 600 10.5px/1 var(--f-mono, monospace); letter-spacing: .08em; opacity: .7; text-transform: uppercase; }
.rk-take { padding: 12px; border-radius: 12px; border: 1.5px solid rgba(255,255,255,.3); background: rgba(255,255,255,.07); color: #fff; font: 800 14px/1.2 var(--f-body, inherit); cursor: pointer; display: flex; flex-direction: column; align-items: center; gap: 3px; }
.rk-take:hover { background: rgba(255,255,255,.14); }
.rk button:disabled { opacity: .5; cursor: default; }
.rk-ladder { display: grid; grid-template-columns: minmax(0, 1.15fr) minmax(0, 1fr); gap: 14px; align-items: stretch; }
.rk-rungs { display: grid; gap: 4px; padding: 8px; border-radius: 14px; background: linear-gradient(90deg, rgba(255,201,74,.08), transparent 30%, transparent 70%, rgba(255,201,74,.08)), rgba(0,0,0,.25); border: 1px solid rgba(255,255,255,.12); position: relative; }
.rk-rung { display: grid; grid-template-columns: 52px 1fr auto; align-items: center; gap: 8px; padding: 5px 10px; border-radius: 9px; background: rgba(255,255,255,.04); border: 1px solid rgba(255,255,255,.08); font-size: 13px; transition: background .12s, border-color .12s, transform .12s, box-shadow .12s; }
.rk-rung .m { font: 800 12px/1 var(--f-mono, monospace); color: var(--gold, #ffc94a); }
.rk-rung b { font: 800 14px/1 var(--f-display, inherit); }
.rk-rung .c { font: 700 10.5px/1 var(--f-mono, monospace); opacity: .75; }
.rk-rung.past { opacity: .45; }
.rk-rung.cur { background: color-mix(in srgb, var(--gold, #ffc94a) 22%, transparent); border-color: var(--gold, #ffc94a); box-shadow: 0 0 16px color-mix(in srgb, var(--gold, #ffc94a) 35%, transparent); transform: scale(1.02); }
.rk-rung.cur::before { content: "▶"; position: absolute; left: -2px; color: var(--gold, #ffc94a); font-size: 11px; }
.rk-rung.goal { border-color: #fff; border-style: dashed; }
.rk-rung.lit { background: #ffffff; color: #0a0c14; box-shadow: 0 0 22px #fff; }
.rk-rung.lit .m, .rk-rung.lit .c { color: #0a0c14; opacity: 1; }
.rk-rung.crash { background: rgba(255,90,106,.12); border-color: rgba(255,90,106,.4); }
.rk-rung.crash.lit { background: #ff5a6a; color: #fff; box-shadow: 0 0 22px #ff5a6a; }
.rk-ctrl { display: flex; flex-direction: column; gap: 10px; justify-content: center; }
.rk-btn { padding: 14px 12px; border-radius: 14px; border: 0; cursor: pointer; display: flex; flex-direction: column; align-items: center; gap: 4px; font: 800 16px/1.1 var(--f-display, inherit); color: #0a0c14; background: linear-gradient(180deg, color-mix(in srgb, var(--gold, #ffc94a) 85%, #fff), var(--gold, #ffc94a)); box-shadow: 0 4px 0 rgba(0,0,0,.35); transition: transform .08s, filter .12s; }
.rk-btn.two { background: linear-gradient(180deg, #ff8ad8, #ff4fd8); }
.rk-btn.stop { background: linear-gradient(180deg, #ff8a96, #ff5a6a); color: #fff; font-size: 22px; padding: 22px 12px; animation: rkPulse .5s ease-in-out infinite alternate; }
.rk-btn:active { transform: translateY(2px); box-shadow: 0 2px 0 rgba(0,0,0,.35); }
.rk-btn:hover { filter: brightness(1.06); }
@keyframes rkPulse { to { box-shadow: 0 4px 0 rgba(0,0,0,.35), 0 0 30px rgba(255,90,106,.7); } }
@media (max-width: 560px) { .rk-ladder { grid-template-columns: 1fr; } .rk-rung { padding: 4px 8px; } .rk-card { width: 116px; height: 160px; } }
'''

RISK_JS = r'''
/* ---------- Risikospiele neu: Kartenrisiko und Leiter (seit SW 0.17.0) ---------- */
// Schneller und mit Tastatur: Karten ← / → (oder 1 / 2), Leiter ↑ oder Leertaste = 1 Sprosse und Stopp, 2 = zwei Sprossen, Enter = einsammeln.
const GAMBLE_THEME = {
  sternenwrack: [{ n: "Cyan", c: "#4fe3ff" }, { n: "Magenta", c: "#ff4fd8" }],
  treibgut: [{ n: "Türkis", c: "#3fd0c8" }, { n: "Koralle", c: "#ff7a59" }],
  eisenfront: [{ n: "Oliv", c: "#a7c060" }, { n: "Signalrot", c: "#e0503a" }],
  neustadt: [{ n: "Grün", c: "#6fdc8c" }, { n: "Rot", c: "#ff6b6b" }],
};
let rkKeys = null, rkClick = null;
function rkDone() { rkKeys = null; if (rkClick) $("bonusBody").removeEventListener("click", rkClick); rkClick = null; }
addEventListener("keydown", e => {
  if (!rkKeys || $("bonus").hidden || e.repeat) return;
  if (e.target.closest && e.target.closest("input, select, textarea")) return;
  const k = rkKeys(e);
  if (k) { e.preventDefault(); e.stopImmediatePropagation(); }
}, true);
async function playGamble() {
  if (!gambleOffer || spinning || busy) return;
  let stake = gambleOffer; clearGamble();
  busy = true; render();
  const [A, B] = GAMBLE_THEME[WORLD_ID] || GAMBLE_THEME.sternenwrack;
  openBonus({ id: "beacon", color: B.c }, "Signal-Risiko", `Errate die Farbe der nächsten Karte: ${A.n} oder ${B.n}. Richtig verdoppelt, falsch verliert. Genau 50 : 50, einsammeln geht jederzeit.`);
  $("bonusBtn").hidden = true;
  let chain = 0, lock = false, finished = null;
  const queue = [];
  const hist = [];
  const sig = col => `<svg viewBox="0 0 40 40"><circle cx="20" cy="20" r="15" fill="${col}" opacity=".22"/><circle cx="20" cy="20" r="8.5" fill="${col}"/><path d="M7 7 a18 18 0 0 0 0 26 M33 7 a18 18 0 0 1 0 26" stroke="${col}" stroke-width="2.2" fill="none"/></svg>`;
  $("bonusBody").innerHTML = `<div class="rk"><div class="rk-steps" id="rkSteps">${[1, 2, 3, 4, 5].map(i => `<span>×${2 ** i}</span>`).join("")}</div>
    <div class="rk-table"><div class="rk-card" id="rkCard" style="--ga:${A.c};--gb:${B.c}"><div class="rk-in"><div class="rk-face rk-back"><i></i></div><div class="rk-face rk-front" id="rkFront"></div></div></div></div>
    <div class="rk-hist" id="rkHist"></div>
    <div class="rk-pick"><button type="button" data-g="a" style="--gc:${A.c}"><i></i>${A.n}<small>Taste ← oder 1</small></button><button type="button" data-g="b" style="--gc:${B.c}"><i></i>${B.n}<small>Taste → oder 2</small></button></div>
    <button type="button" class="rk-take" id="rkTake"></button></div>`;
  const ui = () => {
    $("bonusTotal").textContent = stake;
    [...$("rkSteps").children].forEach((s, i) => { s.className = i < chain ? "on" : i === chain ? "next" : ""; });
    $("rkTake").innerHTML = `Einsammeln · ${fmtN(stake)}<small>Taste Enter</small>`;
    $("rkHist").innerHTML = hist.map(c => `<i style="color:${c};background:${c}"></i>`).join("");
  };
  ui();
  const result = await new Promise(resolve => {
    finished = resolve;
    const pick = async g => {
      if (lock) { if (queue.length < 6) queue.push(g); return; }
      lock = true;
      const real = Math.random() < .5 ? "a" : "b", col = real === "a" ? A.c : B.c, card = $("rkCard");
      card.classList.remove("win", "lose", "quick");
      $("rkFront").innerHTML = sig(col);
      try { sfx.creak(); } catch (e) {}
      card.classList.add("flip");
      await wait(300);
      hist.push(col); if (hist.length > 10) hist.shift();
      if (g === real) {
        state.credits += stake; stake *= 2; chain++;
        bump("gambleWins"); maxStat("gambleChain", chain);
        card.classList.add("win"); try { sfx.mult(); burstAt(card, 26, ["#5dffa8", "#ffffff"], .7); } catch (e) {}
        $("bonusStatus").textContent = `Richtig! Jetzt ${stake} Credits im Spiel.`;
        countCredits(state.credits, 250); ui();
        if (chain >= 5) { await wait(500); resolve("max"); return; }
        await wait(260);
        card.classList.add("quick"); card.classList.remove("flip"); await wait(150);
        lock = false;
        if (queue.length) pick(queue.shift());
      } else {
        state.credits -= stake;
        card.classList.add("lose"); try { sfx.streakBreak(); } catch (e) {}
        countCredits(state.credits, 300);
        $("bonusStatus").textContent = `Daneben. ${stake} Credits verloren.`;
        queue.length = 0; stake = 0; ui(); $("bonusTotal").textContent = 0;
        $("bonusBody").querySelectorAll("button").forEach(b => b.disabled = true);
        await wait(900); resolve("lost");
      }
    };
    rkClick = e => {
      const g = e.target.closest("[data-g]"); if (g && !g.disabled) { pick(g.dataset.g); return; }
      if (e.target.closest("#rkTake") && !lock) resolve("take");
    };
    $("bonusBody").addEventListener("click", rkClick);
    rkKeys = e => {
      if (e.key === "ArrowLeft" || e.key === "1") { pick("a"); return true; }
      if (e.key === "ArrowRight" || e.key === "2") { pick("b"); return true; }
      if (e.key === "Enter" || e.code === "Space") { if (!lock) resolve("take"); return true; }
      return false;
    };
  });
  rkDone();
  if (result !== "lost") { addLog("beacon", `Risiko gewonnen (${chain}×)`, "+" + (stake - stake / 2 ** chain), B.c); bip(chain ? "gambleWin" : "small", chain ? 3 : 1); }
  else { addLog("beacon", "Risiko verloren", "0", "#ff6b7a"); bip("gambleLoss", 3); }
  if (result !== "lost" && chain) $("bonusStatus").textContent = `Eingesammelt: ${stake} Credits.`;
  await wait(250);
  await closeBonus();
  state.peak = Math.max(state.peak, state.credits);
  busy = false; checkAch();
  if (state.credits < 5) { busy = true; render(); await handleBankruptcy(); busy = false; }
  render(); saveGame();
}

async function playLadder() {
  if (!gambleOffer || spinning || busy) return;
  const base = gambleOffer; clearGamble();
  busy = true; render();
  openBonus({ id: "ladder", color: "#ffc94a" }, "Risikoleiter", "Steig so weit hoch, wie du dich traust. Das Licht springt zwischen Ziel und Absturz, du drückst Stopp. Je größer der Sprung, desto kleiner die Chance. Kassieren geht jederzeit.");
  $("bonusBtn").hidden = true;
  const top = LADDER.length - 1, val = i => Math.round(base * LADDER[i]);
  const chance = (a, b) => LADDER[a] / LADDER[b], pct = (a, b) => Math.round(chance(a, b) * 100);
  let lvl = 0, running = false, stopReq = null;
  $("bonusBody").innerHTML = `<div class="rk rk-ladder"><div class="rk-rungs" id="rkRungs">${LADDER.map((m, i) => `<div class="rk-rung" data-i="${i}"><span class="m">×${String(m).replace(".", ",")}</span><b>${fmtN(val(i))}</b><span class="c"></span></div>`).reverse().join("")}<div class="rk-rung crash" data-i="-1"><span class="m">✕</span><b>Absturz</b><span class="c">0</span></div></div>
    <div class="rk-ctrl"><button type="button" class="rk-btn" id="rkOne" data-j="1"></button><button type="button" class="rk-btn two" id="rkTwo" data-j="2"></button><button type="button" class="rk-btn stop" id="rkStop" hidden>Stopp!<small>Leertaste</small></button><button type="button" class="rk-take" id="rkTakeL"></button></div></div>`;
  const rung = i => $("rkRungs").querySelector(`[data-i="${i}"]`);
  const ui = () => {
    $("bonusTotal").textContent = val(lvl);
    LADDER.forEach((_, i) => { const r = rung(i); r.classList.toggle("past", i < lvl); r.classList.toggle("cur", i === lvl); r.querySelector(".c").textContent = i === lvl + 1 || i === lvl + 2 ? `${pct(lvl, i)} %` : ""; });
    const one = $("rkOne"), two = $("rkTwo");
    one.hidden = lvl >= top || running; two.hidden = lvl >= top - 1 || running;
    if (lvl < top) one.innerHTML = `▲ 1 Sprosse · ${pct(lvl, lvl + 1)} %<small>auf ${fmtN(val(lvl + 1))} · Taste ↑ oder Leertaste</small>`;
    if (lvl < top - 1) two.innerHTML = `▲▲ 2 Sprossen · ${pct(lvl, lvl + 2)} %<small>auf ${fmtN(val(lvl + 2))} · Taste 2</small>`;
    $("rkStop").hidden = !running;
    const t = $("rkTakeL"); t.hidden = running; t.innerHTML = `Kassieren · ${fmtN(val(lvl))}<small>Taste Enter</small>`;
  };
  // Lauflicht: schnell, Stopp wirkt nach 2–3 Wechseln, spätestens nach etwa 1,2 Sekunden von selbst
  const run = (target, win) => new Promise(async res => {
    const rT = rung(target), rC = rung(-1);
    running = true; stopReq = null; ui(); rT.classList.add("goal");
    let n = 0, delay = 55, on = 1, stopAt = null;
    stopReq = () => { if (stopAt === null) { stopAt = n + 1 + ((Math.random() * 2) | 0); try { sfx.click(); } catch (e) {} } };
    for (;;) {
      on = 1 - on;
      rT.classList.toggle("lit", on === 0); rC.classList.toggle("lit", on === 1);
      if (state.sound) tone(on === 0 ? 1320 : 440, .04, { type: "square", vol: .03 });
      await wait(delay); n++;
      if (stopAt === null && n >= 16) stopAt = n + 2;
      if (stopAt !== null) {
        delay = Math.min(170, delay * 1.5);
        if (n >= stopAt && (on === 0) !== win) {
          on = 1 - on; rT.classList.toggle("lit", on === 0); rC.classList.toggle("lit", on === 1);
          if (state.sound) tone(on === 0 ? 1320 : 440, .08, { type: "square", vol: .05 });
          break;
        }
      }
    }
    rT.classList.remove("goal"); stopReq = null;
    await wait(110);
    rT.classList.remove("lit"); rC.classList.remove("lit");
    running = false; res();
  });
  const result = await new Promise(resolve => {
    const jump = async j => {
      if (running) { if (stopReq) stopReq(); return; }
      if (lvl + j > top) return;
      const target = lvl + j, win = Math.random() < chance(lvl, target);
      $("bonusStatus").textContent = `Ziel: ${val(target).toLocaleString("de-DE")} Credits. Drück Stopp!`;
      await run(target, win);
      if (win) {
        state.credits += val(target) - val(lvl); lvl = target;
        bump("ladderWins"); maxStat("ladderTop", lvl);
        try { sfx.mult(); burstAt(rung(lvl), 28, ["#ffc94a", "#ffffff", "#ffe08a"], .8); } catch (e) {}
        countCredits(state.credits, 250);
        $("bonusStatus").textContent = `Geschafft! ${val(lvl).toLocaleString("de-DE")} Credits auf der Leiter.`;
        ui();
        if (lvl >= top) { await wait(500); resolve("max"); }
      } else {
        state.credits -= val(lvl);
        try { sfx.streakBreak(); burstAt(rung(-1), 22, ["#ff5a6a", "#8a90b8"], .6); } catch (e) {}
        countCredits(state.credits, 300);
        $("bonusStatus").textContent = `Absturz! ${val(lvl).toLocaleString("de-DE")} Credits verloren.`;
        $("bonusTotal").textContent = 0;
        $("bonusBody").querySelectorAll("button").forEach(b => b.disabled = true);
        await wait(900); resolve("lost");
      }
    };
    rkClick = e => {
      if (e.target.closest("#rkStop")) { if (stopReq) stopReq(); return; }
      const j = e.target.closest("[data-j]"); if (j && !j.disabled) { jump(+j.dataset.j); return; }
      if (e.target.closest("#rkTakeL") && !running) resolve("take");
    };
    $("bonusBody").addEventListener("click", rkClick);
    rkKeys = e => {
      if (e.code === "Space" || e.key === "ArrowUp" || e.key === "1") { if (running) { if (stopReq) stopReq(); } else jump(1); return true; }
      if (e.key === "2") { if (running) { if (stopReq) stopReq(); } else jump(2); return true; }
      if (e.key === "Enter") { if (!running) resolve("take"); return true; }
      return false;
    };
    ui();
  });
  rkDone();
  if (result === "lost") { addLog("beacon", "Risikoleiter abgestürzt", "0", "#ff6b7a"); bip("ladderLoss", 3); }
  else {
    const gain = val(lvl) - base;
    if (lvl) { addLog("beacon", `Risikoleiter ×${String(LADDER[lvl]).replace(".", ",")}`, "+" + gain, "#ffc94a"); state.best = Math.max(state.best, val(lvl)); }
    $("bonusStatus").textContent = `Kassiert: ${val(lvl).toLocaleString("de-DE")} Credits.`;
    if (result === "max") { bip("ladderTop", 3); flashScreen(); burst(140, ["#ffc94a", "#ffffff", "#ff4fd8"], 1.3); addDust(2, "Gipfel der Risikoleiter"); }
    else if (lvl >= 4) bip("ladderWin", 3);
  }
  await wait(300);
  await closeBonus();
  state.peak = Math.max(state.peak, state.credits);
  busy = false; checkAch();
  if (state.credits < 5) { busy = true; render(); await handleBankruptcy(); busy = false; }
  render(); saveGame();
}
'''
EXTRA_CSS += RISK_CSS
EXTRA_JS += RISK_JS
