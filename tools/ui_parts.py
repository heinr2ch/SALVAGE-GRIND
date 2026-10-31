# Neues Hauptmenü, aufgewertete Erfolge, Sicherheits- und Datenschutzhinweise, Hilfe bei Glücksspielproblemen,
# Pausen-Erinnerung (seit SW 0.18.0, Zweig experimente)
UI_CSS = r'''
/* ---------- Steuerleiste neu (Credits, Gewinn, Staub, Start, Einsatz) ---------- */
@media (min-width: 601px) {
  .deck { position: relative; gap: 16px 22px; padding: 18px 20px; border-radius: 20px; overflow: hidden;
    background: radial-gradient(120% 140% at 50% 120%, color-mix(in srgb, var(--cyan) 14%, transparent), transparent 60%), linear-gradient(180deg, rgba(255,255,255,.06), rgba(0,0,0,.35));
    border: 1px solid rgba(255,255,255,.12); box-shadow: inset 0 1px 0 rgba(255,255,255,.08), 0 18px 40px rgba(0,0,0,.35); }
  .deck::before { content: ""; position: absolute; left: 18px; right: 18px; top: 0; height: 2px; border-radius: 2px; background: linear-gradient(90deg, transparent, var(--cyan), var(--gold), transparent); opacity: .8; }
  .deck { grid-template-columns: minmax(0, 1.15fr) auto minmax(0, 1fr); }
  .wallet { gap: 8px; align-self: center; }
  .wallet .stat { position: relative; align-content: center; gap: 4px; padding: 12px 10px 12px 14px; min-height: 78px; border-radius: 14px; background: linear-gradient(160deg, rgba(255,255,255,.07), rgba(0,0,0,.28)); border: 1px solid rgba(255,255,255,.1); overflow: hidden; --sc: var(--gold); }
  .wallet .stat::before { content: ""; position: absolute; left: 0; top: 10px; bottom: 10px; width: 3px; border-radius: 0 3px 3px 0; background: var(--sc); box-shadow: 0 0 12px var(--sc); }
  .wallet .stat:nth-child(2) { --sc: var(--win, #5dffa8); }
  .wallet .stat.dust { --sc: var(--violet, #8b6cff); }
  .wallet .stat > span:first-child { display: flex; align-items: center; gap: 6px; font-size: .56rem; letter-spacing: .05em; color: color-mix(in srgb, var(--sc) 70%, #fff); white-space: nowrap; overflow: hidden; text-overflow: clip; }
  .wallet .stat b { font-size: clamp(1.25rem, 2.2vw, 1.75rem); letter-spacing: .02em; text-shadow: 0 0 18px color-mix(in srgb, var(--sc) 35%, transparent); }
  .wallet .stat #credits { background: linear-gradient(180deg, #fff 30%, color-mix(in srgb, var(--gold) 70%, #fff)); -webkit-background-clip: text; background-clip: text; color: transparent; }
  .wallet .stat #credits.counting { background: none; color: var(--win); -webkit-text-fill-color: currentColor; }
  .wallet .stat #lastWin.pos { animation: wlWin .7s cubic-bezier(.2,1.6,.4,1); }
  @keyframes wlWin { 40% { transform: scale(1.18); text-shadow: 0 0 22px var(--win); } }
  .spinwrap { width: 122px; height: 122px; }
  .spinwrap .spin { font-size: .84rem; }
  .spinwrap .spin svg { width: 34px; height: 34px; }
  .bets { gap: 10px; align-content: center; }
  .stepper { border-radius: 14px; border: 1px solid rgba(255,255,255,.16); background: linear-gradient(180deg, rgba(255,255,255,.08), rgba(0,0,0,.25)); box-shadow: inset 0 1px 0 rgba(255,255,255,.08); }
  .stepper button { width: 42px; height: 46px; font-size: 1.3rem; transition: background .15s, color .15s; }
  .stepper button:hover:not(:disabled) { background: color-mix(in srgb, var(--gold) 18%, transparent); color: var(--gold); }
  .stepper output b { font-size: 1.35rem; }
  .auto { gap: 6px; }
  .auto button { border-radius: 99px !important; padding: 7px 12px !important; border: 1px solid rgba(255,255,255,.16) !important; background: rgba(255,255,255,.05) !important; transition: border-color .15s, background .15s; }
  .auto button[aria-pressed="true"] { border-color: var(--gold) !important; background: color-mix(in srgb, var(--gold) 20%, transparent) !important; color: var(--gold) !important; }
  .fsbuybtn { position: relative; overflow: hidden; border-radius: 12px; padding: 11px 14px; font-size: 13px; }
  .fsbuybtn::after { content: ""; position: absolute; inset: 0; background: linear-gradient(105deg, transparent 35%, rgba(255,255,255,.45) 50%, transparent 65%); transform: translateX(-120%); animation: fsShine 4s ease-in-out infinite; pointer-events: none; }
  @keyframes fsShine { 0%, 70% { transform: translateX(-120%); } 100% { transform: translateX(120%); } }
}
@media (prefers-reduced-motion: reduce) { .fsbuybtn::after, .wallet .stat #lastWin.pos { animation: none !important; } }

/* ---------- Hauptmenü, zweispaltig ---------- */
#intro .intro-inner.mm2 { max-width: 1240px; display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.15fr); grid-template-areas: "top top" "hero side" "foot foot"; gap: 22px 36px; align-items: start; justify-items: stretch; text-align: left; padding-top: 22px; }
.mm2 .mm2-top { grid-area: top; display: flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap; }
.mm2 .mm2-top .mm-brand { justify-content: flex-start; margin: 0; font-size: clamp(1.4rem, 3.4vw, 2.6rem); }
.mm2 .mm2-top .mm-eyebrow { margin: 0; }
.mm2 .mm2-tools { display: flex; gap: 8px; align-items: center; margin-left: auto; }
.mm2 .mm2-tools button { display: inline-flex; gap: 6px; align-items: center; font: 700 12px var(--f-body, system-ui); padding: 8px 12px; border-radius: 99px; border: 1.5px solid rgba(255,255,255,.22); background: rgba(0,0,0,.3); color: #fff; cursor: pointer; }
.mm2 .mm2-tools button[aria-pressed="true"] { border-color: var(--gold, #ffc94a); color: var(--gold, #ffc94a); }
.mm2 .mm2-tools svg { width: 14px; height: 14px; }
.mm2 .mm2-hero { grid-area: hero; display: grid; justify-items: start; gap: 12px; padding: 22px; border-radius: 22px; background: linear-gradient(160deg, rgba(255,255,255,.07), rgba(0,0,0,.35)); border: 1px solid rgba(255,255,255,.12); box-shadow: 0 20px 60px rgba(0,0,0,.35); }
.mm2 .mm2-hero .emblem.big { width: 84px; height: 84px; }
.mm2 .mm2-hero .intro-title { text-align: left; padding-left: 0; font-size: clamp(1.4rem, 3.2vw, 2.4rem); }
.mm2 .mm2-hero .intro-sub { text-align: left; }
.mm2 .mm2-hero .intro-btn { width: 100%; max-width: 420px; font-size: 1.15rem; padding: 16px 24px; }
.mm2 .mm2-list { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; width: 100%; max-width: 420px; }
.mm2 .mm2-list button { display: grid; grid-template-columns: 22px 1fr; column-gap: 10px; align-items: center; text-align: left; padding: 10px 12px; border-radius: 12px; border: 1px solid rgba(255,255,255,.14); background: rgba(255,255,255,.05); color: #fff; font: 700 13px var(--f-body, system-ui); cursor: pointer; transition: border-color .15s, background .15s, transform .15s; }
.mm2 .mm2-list button:hover, .mm2 .mm2-list button:focus-visible { border-color: var(--gold, #ffc94a); background: rgba(255,201,74,.08); transform: translateY(-1px); outline: none; }
.mm2 .mm2-list button svg { width: 18px; height: 18px; grid-row: span 2; }
.mm2 .mm2-list button small { grid-column: 2; font: 500 11px var(--f-body, system-ui); color: rgba(255,255,255,.66); }
.mm2 .mm2-list button.wide { grid-column: span 2; }
.mm2 .mm2-hero .intro-hint { text-align: left; }
.mm2 .mm2-side { grid-area: side; display: grid; gap: 10px; align-content: start; }
.mm2 .mm2-side .mm-head { text-align: left; }
.mm2 .mm2-side .intro-worlds.mm-grid { grid-template-columns: 1fr 1fr; }
.mm2 .mmw .mmw-motto { font: 700 11px var(--f-mono, monospace); letter-spacing: .06em; color: var(--wc); opacity: .95; }
.mm2 .mm2-foot { grid-area: foot; display: flex; flex-wrap: wrap; gap: 10px 18px; justify-content: space-between; align-items: center; padding: 12px 16px; border-radius: 14px; background: rgba(0,0,0,.32); border: 1px solid rgba(255,255,255,.1); font-size: 12px; color: rgba(255,255,255,.8); }
.mm2 .mm2-foot .safe { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }
.mm2 .mm2-foot .safe b { color: #fff; }
.mm2 .mm2-foot button.link { background: none; border: 0; color: var(--gold, #ffc94a); font: 700 12px var(--f-body, system-ui); text-decoration: underline; cursor: pointer; padding: 0; }
@media (max-width: 900px) {
  #intro .intro-inner.mm2 { grid-template-columns: 1fr; grid-template-areas: "top" "hero" "side" "foot"; }
  .mm2 .mm2-hero { justify-items: center; text-align: center; } .mm2 .mm2-hero .intro-title, .mm2 .mm2-hero .intro-sub, .mm2 .mm2-hero .intro-hint { text-align: center; }
}
@media (max-width: 520px) { .mm2 .mm2-list { grid-template-columns: 1fr; } .mm2 .mm2-list button.wide { grid-column: auto; } .mm2 .mm2-side .intro-worlds.mm-grid { grid-template-columns: 1fr 1fr; } }

/* ---------- Erfolge ---------- */
.achhead { display: flex; align-items: center; gap: 10px; margin: -2px 0 10px; font-size: 12px; color: rgba(255,255,255,.75); }
.achhead .bar { flex: 1; height: 8px; border-radius: 99px; background: rgba(255,255,255,.08); overflow: hidden; }
.achhead .bar i { display: block; height: 100%; background: linear-gradient(90deg, #cd7f32, #e8e8f0, #ffc94a); border-radius: 99px; }
.achgrid.ach2 { grid-template-columns: repeat(auto-fill, minmax(96px, 1fr)); gap: 10px; }
.ach2 .ach { padding: 12px 6px 10px; gap: 6px; cursor: pointer; overflow: hidden; border-radius: 14px; }
.ach2 .ach .medal { position: relative; width: 52px; height: 52px; display: grid; place-items: center; border-radius: 50%; background: radial-gradient(circle at 35% 30%, color-mix(in srgb, var(--mc) 85%, #fff), var(--mc) 55%, color-mix(in srgb, var(--mc) 55%, #000)); box-shadow: 0 0 0 3px color-mix(in srgb, var(--mc) 40%, transparent), 0 6px 14px rgba(0,0,0,.45); }
.ach2 .ach .medal svg { width: 32px; height: 32px; filter: drop-shadow(0 1px 1px rgba(0,0,0,.6)); }
.ach2 .ach span { font-size: .62rem; }
.ach2 .ach em { font: 700 10px var(--f-mono, monospace); font-style: normal; color: var(--mc); }
.ach2 .ach.t1 { --mc: #cd7f32; } .ach2 .ach.t2 { --mc: #c9ced8; } .ach2 .ach.t3 { --mc: #ffc94a; }
.ach2 .ach.got { border-color: color-mix(in srgb, var(--mc) 60%, transparent); background: radial-gradient(120% 90% at 50% 0%, color-mix(in srgb, var(--mc) 16%, transparent), rgba(255,255,255,.02)); }
.ach2 .ach.got::after { content: ""; position: absolute; inset: -40%; background: linear-gradient(115deg, transparent 42%, rgba(255,255,255,.22) 50%, transparent 58%); transform: translateX(-60%); animation: achShine 5s ease-in-out infinite; pointer-events: none; }
@keyframes achShine { 0%, 70% { transform: translateX(-60%); } 100% { transform: translateX(60%); } }
.ach2 .ach.locked .medal { background: rgba(255,255,255,.06); box-shadow: inset 0 0 0 2px rgba(255,255,255,.12); }
.ach2 .ach.locked .medal svg { filter: grayscale(1) brightness(.35); }
.ach2 .ach.locked .medal::after { content: "🔒"; position: absolute; right: -4px; bottom: -4px; font-size: 14px; }
.ach2 .ach.sel { outline: 2px solid var(--mc); }
.achdetail { margin-top: 10px; padding: 10px 12px; border-radius: 12px; background: rgba(255,255,255,.05); border: 1px solid rgba(255,255,255,.12); font-size: 13px; }
.achdetail[hidden] { display: none; }
#achPop { position: fixed; left: 50%; top: 18%; transform: translate(-50%, -20px) scale(.9); opacity: 0; z-index: 300; pointer-events: none; display: grid; justify-items: center; gap: 6px; padding: 18px 28px 16px; border-radius: 20px; background: radial-gradient(120% 100% at 50% 0%, rgba(255,201,74,.25), rgba(10,12,22,.95) 60%); border: 2px solid var(--mc, #ffc94a); box-shadow: 0 20px 60px rgba(0,0,0,.6), 0 0 40px color-mix(in srgb, var(--mc, #ffc94a) 40%, transparent); text-align: center; transition: opacity .35s, transform .35s cubic-bezier(.2,1.4,.4,1); }
#achPop.on { opacity: 1; transform: translate(-50%, 0) scale(1); }
#achPop small { font: 800 11px var(--f-mono, monospace); letter-spacing: .3em; color: var(--mc, #ffc94a); }
#achPop b { font: 800 1.3rem var(--f-display, system-ui); color: #fff; }
#achPop p { margin: 0; font-size: 13px; color: rgba(255,255,255,.85); max-width: 34ch; }
#achPop .medal { width: 70px; height: 70px; border-radius: 50%; display: grid; place-items: center; background: radial-gradient(circle at 35% 30%, #fff, var(--mc, #ffc94a) 45%, color-mix(in srgb, var(--mc, #ffc94a) 50%, #000)); box-shadow: 0 0 30px var(--mc, #ffc94a); animation: achSpin 1.2s ease-out; }
#achPop .medal svg { width: 42px; height: 42px; }
#achPop em { font: 800 15px var(--f-mono, monospace); font-style: normal; color: #6fdc8c; }
@keyframes achSpin { from { transform: rotateY(540deg) scale(.4); } to { transform: none; } }

/* ---------- Hinweise und Hilfe ---------- */
#mmInfo .bonus-card { max-width: 680px; width: min(680px, 96vw); text-align: left; }
#mmInfo h3 { margin: 16px 0 6px; font-size: 15px; color: var(--gold, #ffc94a); }
#mmInfo p, #mmInfo li { font-size: 13.5px; line-height: 1.55; color: rgba(255,255,255,.88); }
#mmInfo ul { margin: 6px 0; padding-left: 20px; }
#mmInfo a { color: #7ee0c8; }
#mmInfo .help { display: grid; gap: 8px; }
#mmInfo .help div { padding: 10px 12px; border-radius: 12px; background: rgba(126,224,200,.08); border: 1px solid rgba(126,224,200,.3); }
#mmInfo .help b { color: #fff; }
#mmInfo .danger { border-color: rgba(255,120,120,.5) !important; background: rgba(255,90,90,.08) !important; }
#pauseNote { position: fixed; left: 50%; bottom: 18px; transform: translateX(-50%); z-index: 240; display: flex; gap: 12px; align-items: center; padding: 12px 16px; border-radius: 14px; background: rgba(10,12,22,.95); border: 1.5px solid #7ee0c8; color: #fff; font-size: 13.5px; box-shadow: 0 10px 30px rgba(0,0,0,.5); max-width: min(92vw, 620px); }
#pauseNote[hidden] { display: none; }
#pauseNote button { font: 700 12px var(--f-body, system-ui); padding: 7px 12px; border-radius: 8px; border: 1.5px solid rgba(255,255,255,.3); background: rgba(255,255,255,.08); color: #fff; cursor: pointer; white-space: nowrap; }
'''

UI_JS = r'''
/* ---------- Hauptmenü neu ordnen ---------- */
const UI_ICON = {
  play: '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M5 3l8 5-8 5z" fill="currentColor"/></svg>',
  arcade: '<svg viewBox="0 0 16 16" aria-hidden="true"><rect x="2" y="4" width="12" height="8" rx="2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M5 8h3M6.5 6.5v3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><circle cx="11" cy="7.3" r="1" fill="currentColor"/><circle cx="12" cy="9.2" r="1" fill="currentColor"/></svg>',
  help: '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 1.8l5.2 2v3.7c0 3.2-2.2 5.6-5.2 6.7-3-1.1-5.2-3.5-5.2-6.7V3.8z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M5.6 8l1.7 1.7L10.6 6.3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  note: '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M6 12.5V3.2l7-1.4v9.3" fill="none" stroke="currentColor" stroke-width="1.5"/><circle cx="4.5" cy="12.5" r="1.8" fill="currentColor"/><circle cx="11.5" cy="11.1" r="1.8" fill="currentColor"/></svg>',
};
(function setupMenu2() {
  const intro = $("intro"), inner = intro && intro.querySelector(".intro-inner"); if (!inner) return;
  const q = s => inner.querySelector(s), mk = c => { const d = document.createElement("div"); d.className = c; return d; };
  const top = mk("mm2-top"), hero = mk("mm2-hero"), side = mk("mm2-side"), foot = mk("mm2-foot");
  const strip = q(".mm-strip"); if (strip) strip.remove();
  [q(".mm-brand"), q(".mm-eyebrow")].forEach(e => e && top.appendChild(e));
  top.insertAdjacentHTML("beforeend", `<div class="mm2-tools"><button type="button" id="mm2Music">${UI_ICON.note}<span>Musik</span></button></div>`);
  [q("svg.emblem"), q(".intro-title"), q(".intro-sub"), q(".betatag"), $("introBtn")].forEach(e => e && hero.appendChild(e));
  const row = q(".mm-row");
  if (row) {
    row.className = "mm2-list";
    const sub = { mmSettings: "Ton, Tempo, Sprache", mmWorldsJump: "Vier Welten, eigener Spielstand", mmPlinko: "Ball fallen lassen", mmOnline: "Freunde, Duell, Crew" };
    row.insertAdjacentHTML("beforeend", `<button type="button" id="mmArcade">${UI_ICON.arcade}${typeof arTheme === "function" ? arTheme().name : "Spielhalle"}</button><button type="button" id="mmHelp">${UI_ICON.help}Sicher spielen & Hilfe</button>`);
    Object.assign(sub, { mmArcade: "Spielmodus dieser Welt", mmHelp: "Hinweise, Datenschutz, Anlaufstellen" });
    row.querySelectorAll("button").forEach(b => { if (sub[b.id]) b.insertAdjacentHTML("beforeend", `<small>${sub[b.id]}</small>`); });
    hero.appendChild(row);
  }
  const hint = q(".intro-hint"); if (hint) hero.appendChild(hint);
  [$("mmWorldsHead"), $("introWorlds")].forEach(e => e && side.appendChild(e));
  foot.innerHTML = `<span class="safe">🛡️ <b>Nur Spielgeld.</b> Kein Echtgeld, keine Auszahlung, nichts zu kaufen. Spiel bewusst und mach Pausen. <button type="button" class="link" id="mm2Help">Hilfe bei Glücksspielproblemen</button></span>`;
  [q(".intro-lang"), q(".intro-by")].forEach(e => e && foot.appendChild(e));
  inner.innerHTML = ""; inner.classList.add("mm2"); [top, hero, side, foot].forEach(e => inner.appendChild(e));
  // erst jetzt hängen die Knöpfe wieder im Dokument
  const fromMenu = fn => () => { if (intro.classList.contains("ingame")) closeMainMenu(); else $("introBtn").click(); setTimeout(fn, 700); };
  $("mmArcade") && $("mmArcade").addEventListener("click", fromMenu(() => typeof openArcade === "function" && openArcade()));
  $("mmHelp") && $("mmHelp").addEventListener("click", () => openInfo());
  $("mm2Help").addEventListener("click", () => openInfo("help"));
  // Musik im Menü: startet mit dem ersten Tipp (Browser erlauben vorher keinen Ton)
  const musicUi = () => $("mm2Music").setAttribute("aria-pressed", String(!!state.music));
  $("mm2Music").addEventListener("click", e => { e.stopPropagation(); const m = $("music"); if (m) m.click(); else { state.music = !state.music; state.music ? startMusic() : stopMusic(); } setTimeout(musicUi, 50); });
  const wake = () => { try { if (state.music) { getCtx(); startMusic(); } } catch (e) {} };
  intro.addEventListener("pointerdown", wake, { once: true }); intro.addEventListener("keydown", wake, { once: true });
  setTimeout(musicUi, 300);
})();

/* ---------- Hinweise, Datenschutz und Hilfe ---------- */
(function setupInfo() {
  document.body.insertAdjacentHTML("beforeend", `<div class="bonus" id="mmInfo" hidden role="dialog" aria-modal="true" aria-labelledby="infoTitle" style="z-index:270"><div class="bonus-card">
  <h2 id="infoTitle" style="margin:0 0 6px">Sicher spielen & Hilfe</h2>
  <div class="ol-tabs" id="infoTabs"><button type="button" data-t="safe">Hinweise</button><button type="button" data-t="help">Hilfe bei Glücksspielproblemen</button><button type="button" data-t="privacy">Datenschutz</button></div>
  <div id="infoBody"></div>
  <div class="ar-row"><span></span><button type="button" class="bbtn ghost" id="infoClose">Schließen</button></div></div></div>
  <div id="pauseNote" hidden role="status"><span id="pauseText"></span><button type="button" id="pauseOk">Weiterspielen</button><button type="button" id="pauseHelp">Hilfe</button></div>
  <div id="achPop" aria-live="polite"></div>`);
  $("infoClose").addEventListener("click", () => { $("mmInfo").hidden = true; });
  $("infoTabs").addEventListener("click", e => { const b = e.target.closest("button[data-t]"); if (b) openInfo(b.dataset.t); });
  $("infoBody").addEventListener("click", e => { if (e.target.closest("#infoDelete")) infoDelete(); });
  window.addEventListener("keydown", e => { if (!$("mmInfo").hidden && e.key === "Escape") { $("mmInfo").hidden = true; e.preventDefault(); e.stopImmediatePropagation(); } }, true);
  $("pauseOk").addEventListener("click", () => { $("pauseNote").hidden = true; });
  $("pauseHelp").addEventListener("click", () => { $("pauseNote").hidden = true; openInfo("help"); });
})();
const INFO = {
  safe: `<p><b>Salvage &amp; Grind ist ein Spiel mit Spielgeld.</b> Es gibt kein Echtgeld, keine Auszahlung von Gewinnen und du kannst keine Credits kaufen. Credits, Muscheln, Schrauben und Taler haben keinen Geldwert.</p>
    <ul><li>Die Walzen arbeiten mit Zufall. Es gibt keine Muster, Tricks oder „fälligen“ Gewinne.</li>
    <li>Das Spiel simuliert Glücksspiel. Das kann echtes Glücksspiel verharmlosen. Erfolge hier sagen nichts über Chancen in echten Spielhallen oder Online-Casinos aus.</li>
    <li>Empfohlen für Erwachsene ab 18 Jahren.</li>
    <li>Mach regelmäßig Pausen. Nach jeder Stunde Spielzeit erinnert dich das Spiel daran.</li>
    <li>Online: Gib deinen Freundescode nur Menschen, die du kennst. Deinen Wiederherstellungscode gibst du niemandem. Wir fragen nie nach Passwörtern, Zahlungsdaten oder persönlichen Angaben.</li></ul>`,
  help: `<p>Wenn Glücksspiel – echt oder simuliert – dir Sorgen macht, du mehr spielst als du willst oder an echtes Geld denkst: Du bist nicht allein, und es gibt kostenlose Hilfe.</p>
    <div class="help">
      <div><b>Deutschland · BIÖG-Telefonberatung</b><br>📞 <b>0800 1 37 27 00</b> (kostenlos)<br>Mo–Do 10–22 Uhr, Fr–So 10–18 Uhr · für Spielende und Angehörige</div>
      <div><b>Deutschland · Online</b><br>Selbsttest und Beratung: <a href="https://www.check-dein-spiel.de" target="_blank" rel="noopener">check-dein-spiel.de</a><br>Kostenloses, anonymes Selbsthilfeprogramm: <a href="https://www.neustart-spielerhilfe.de" target="_blank" rel="noopener">neustart-spielerhilfe.de</a></div>
      <div><b>Österreich · Spielsuchthilfe</b><br>Kostenlos, auf Wunsch anonym: <a href="https://www.spielsuchthilfe.at" target="_blank" rel="noopener">spielsuchthilfe.at</a></div>
      <div><b>Schweiz · SOS Spielsucht</b><br>📞 <b>0800 040 080</b> (kostenlos) · <a href="https://www.sos-spielsucht.ch" target="_blank" rel="noopener">sos-spielsucht.ch</a></div>
      <div class="danger"><b>Akute Krise?</b> Wenn es dir sehr schlecht geht oder du an Selbstverletzung denkst: Notruf <b>112</b> oder TelefonSeelsorge <b>0800 111 0 111</b> (Deutschland, rund um die Uhr, kostenlos).</div>
    </div>`,
  privacy: () => `<p><b>Ohne Online-Funktionen</b> bleibt alles auf deinem Gerät: Spielstand und Einstellungen liegen nur im Speicher deines Browsers.</p>
    <p><b>Mit Online-Funktionen</b> (Freunde, Rangliste, Duell, Crew, Cloud-Spielstand) nutzt das Spiel Google Firebase. Die Daten liegen auf Servern in Belgien (EU). Gespeichert werden nur:</p>
    <ul><li>eine zufällige, anonyme Kennung (keine E-Mail, kein Name, kein Passwort)</li><li>dein selbst gewählter Kapitänsname und dein Freundescode</li><li>Rang, Rekord und Credits je Welt, dein größter Tagesgewinn, Zeitpunkt der letzten Aktivität</li><li>Freundesliste, Geschenke, Crew und Duell-Ergebnisse</li><li>dein Spielstand, nur wenn du ihn in der Cloud sicherst</li></ul>
    <p>Keine Werbung, kein Tracking, keine Weitergabe an Dritte. Die Kennung wird auf diesem Gerät im Browser gespeichert.</p>
    ${typeof OL !== "undefined" && OL.ready ? `<p><button type="button" class="ol-small" id="infoDelete">Meine Online-Daten löschen</button> Entfernt Profil, Ranglisten-Einträge, Freundschaften, Crew und Cloud-Spielstand. Dein lokaler Spielstand bleibt erhalten.</p>` : ""}
    <p id="infoMsg" class="ol-msg"></p>`,
};
function openInfo(tab) {
  tab = tab || "safe";
  document.querySelectorAll("#infoTabs button").forEach(b => b.setAttribute("aria-pressed", String(b.dataset.t === tab)));
  const c = INFO[tab]; $("infoBody").innerHTML = typeof c === "function" ? c() : c;
  $("mmInfo").hidden = false; try { sfx.click(); } catch (e) {}
}
async function infoDelete() {
  const m = $("infoMsg");
  if (!infoDelete.armed) { infoDelete.armed = true; m.textContent = "Wirklich löschen? Nochmal tippen zum Bestätigen."; m.className = "ol-msg err"; return; }
  infoDelete.armed = false;
  try {
    if (OL.crew) await crewLeave(true);
    const up = { [`players/${OL.uid}`]: null, [`daily/${olDay()}/${OL.uid}`]: null };
    Object.keys(OL.friends).forEach(f => { up[`friends/${OL.uid}/${f}`] = null; up[`friends/${f}/${OL.uid}`] = null; });
    await OL.db.ref().update(up);
    if (OL.vault) await OL.db.ref("vault/" + OL.vault).remove();
    try { localStorage.removeItem("welten-vault"); localStorage.removeItem("welten-crew"); } catch (e) {}
    OL.vault = null; m.textContent = "Deine Online-Daten wurden gelöscht."; m.className = "ol-msg ok";
  } catch (e) { m.textContent = "Löschen hat nicht geklappt. Bitte später nochmal."; m.className = "ol-msg err"; }
}
// Pausen-Erinnerung nach jeder Stunde Spielzeit
let pauseHours = 0;
setInterval(() => {
  if (!ready || typeof sess === "undefined") return;
  const h = Math.floor((Date.now() - sess.start) / 3600000);
  if (h > pauseHours) { pauseHours = h; $("pauseText").textContent = `Du spielst seit ${h === 1 ? "einer Stunde" : h + " Stunden"}. Zeit für eine kurze Pause? Trink was, beweg dich kurz.`; $("pauseNote").hidden = false; }
}, 30000);

/* ---------- Erfolge: Medaillen, Fortschritt, Freischalt-Moment ---------- */
const achTier = a => a.reward >= 300 ? 3 : a.reward >= 120 ? 2 : 1;
const ACH_TIER = ["", "Bronze", "Silber", "Gold"];
renderCollection = (orig => function () {
  orig.apply(this, arguments);
  const got = state.ach || [], grid = $("achGrid"); if (!grid) return;
  grid.classList.add("ach2");
  const pct = Math.round(got.length / ACH.length * 100);
  if (!$("achHead")) grid.insertAdjacentHTML("beforebegin", `<div class="achhead" id="achHead"></div>`);
  $("achHead").innerHTML = `<div class="bar"><i style="width:${pct}%"></i></div><span>${pct} %</span>`;
  grid.innerHTML = ACH.map(a => { const has = got.includes(a.id), t = achTier(a);
    return `<div class="ach t${t} ${has ? "got" : "locked"}" data-ach="${a.id}" tabindex="0" title="${a.name}"><div class="medal">${ICONS[a.icon] || ICONS.scrap}</div><span>${a.name}</span><em>${ACH_TIER[t]} · +${fmtN(a.reward)}</em></div>`; }).join("");
  if (!$("achDetail")) grid.insertAdjacentHTML("afterend", `<div class="achdetail" id="achDetail" hidden></div>`);
})(renderCollection);
document.addEventListener("click", e => {
  const el = e.target.closest("#achGrid .ach"); if (!el) return;
  const a = ACH.find(x => x.id === el.dataset.ach); if (!a) return;
  document.querySelectorAll("#achGrid .ach.sel").forEach(x => x.classList.remove("sel")); el.classList.add("sel");
  const has = (state.ach || []).includes(a.id);
  $("achDetail").innerHTML = `<b>${a.name}</b> · ${ACH_TIER[achTier(a)]}<br>${a.desc}<br><span style="color:${has ? "#6fdc8c" : "rgba(255,255,255,.65)"}">${has ? "Geschafft! Belohnung erhalten: " : "Belohnung: "}+${fmtN(a.reward)} Credits</span>`;
  $("achDetail").hidden = false;
});
let achQueue = [], achBusy = false;
toast = (orig => function (text, color) {
  const m = /^Erfolg: (.+) \(\+\d+\)$/.exec(String(text));
  const a = m && ACH.find(x => x.name === m[1]);
  if (!a) return orig.apply(this, arguments);
  achQueue.push(a); if (!achBusy) achShow();
})(toast);
function achShow() {
  const a = achQueue.shift(); if (!a) { achBusy = false; return; }
  achBusy = true; const t = achTier(a), col = ["", "#cd7f32", "#c9ced8", "#ffc94a"][t], el = $("achPop");
  el.style.setProperty("--mc", col);
  el.innerHTML = `<small>ERFOLG FREIGESCHALTET</small><div class="medal">${ICONS[a.icon] || ICONS.scrap}</div><b>${a.name}</b><p>${a.desc}</p><em>+${fmtN(a.reward)} Credits · ${ACH_TIER[t]}</em>`;
  el.classList.add("on");
  try { burst(t === 3 ? 90 : 50, [col, "#ffffff", "#ffc94a"], 1); } catch (e) {}
  setTimeout(() => { el.classList.remove("on"); setTimeout(achShow, 450); }, 3200);
}
'''
