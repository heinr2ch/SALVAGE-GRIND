# Spielhalle: ein eigener Spielmodus pro Welt (seit SW 0.18.0, Zweig experimente)
# Sternenwrack: Asteroidenfeld · Treibgut: Tiefsee-Angel · Eisenfront: Panzerjagd · Neustadt: Turmbau
ARCADE_CSS = r'''
#arcade .bonus-card { max-width: 760px; width: min(760px, 96vw); }
.ar-head { display: flex; gap: 12px; align-items: center; margin-bottom: 8px; }
.ar-head h2 { margin: 0; font: 800 1.3rem var(--f-display, system-ui); color: var(--ac); }
.ar-head p { margin: 2px 0 0; font-size: .85rem; color: rgba(255,255,255,.78); }
.ar-stage { position: relative; border-radius: 14px; overflow: hidden; border: 1.5px solid color-mix(in srgb, var(--ac) 55%, transparent); background: #05060d; touch-action: none; }
.ar-stage canvas { display: block; width: 100%; height: auto; aspect-ratio: 16 / 10; cursor: crosshair; }
.ar-hud { position: absolute; left: 10px; right: 10px; top: 8px; display: flex; justify-content: space-between; gap: 8px; pointer-events: none; font: 700 13px/1.2 var(--f-mono, monospace); color: #fff; text-shadow: 0 1px 3px #000; }
.ar-hud b { color: var(--ac); }
.ar-over { position: absolute; inset: 0; display: grid; place-items: center; background: rgba(4,5,10,.72); text-align: center; padding: 16px; }
.ar-over[hidden] { display: none; }
.ar-over h3 { margin: 0 0 6px; font: 800 1.25rem var(--f-display, system-ui); color: var(--ac); }
.ar-over p { margin: 0 0 12px; color: rgba(255,255,255,.85); font-size: .9rem; max-width: 46ch; }
.ar-packs { display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; margin-bottom: 10px; }
.ar-packs button { font: 700 13px var(--f-body, system-ui); padding: 8px 14px; border-radius: 10px; border: 1.5px solid rgba(255,255,255,.25); background: rgba(255,255,255,.06); color: #fff; cursor: pointer; }
.ar-packs button[aria-pressed="true"] { border-color: var(--ac); background: color-mix(in srgb, var(--ac) 22%, transparent); }
.ar-packs button:disabled { opacity: .45; cursor: not-allowed; }
.ar-table { display: flex; flex-wrap: wrap; gap: 6px; justify-content: center; margin: 0 0 12px; font: 600 11px var(--f-mono, monospace); color: rgba(255,255,255,.75); }
.ar-table span { padding: 3px 7px; border-radius: 6px; background: rgba(255,255,255,.07); }
.ar-row { display: flex; gap: 8px; justify-content: space-between; align-items: center; margin-top: 10px; flex-wrap: wrap; }
.ar-row .ar-keys { font-size: .78rem; color: rgba(255,255,255,.7); }
.ar-row .bbtn { --bc: var(--ac); }
#arCash[hidden] { display: none; }
'''

ARCADE_JS = r'''
/* ---------- Spielhalle: ein eigener Modus pro Welt ---------- */
const AR_W = 640, AR_H = 400;
const AR_PACKS = [5, 10, 25];
const AR_THEME = {
  sternenwrack: { key: "astro", name: "Asteroidenfeld", sub: "Steuere den Bergungsjäger durch den Steinschlag und schieß Asteroiden ab.", ac: "#4fe3ff", keys: "Steuern: ← → oder A D oder Maus · Feuer läuft automatisch" },
  treibgut: { key: "deep", name: "Tiefsee-Angel", sub: "Die Leine sinkt immer tiefer, die Fische werden wertvoller. Aber je tiefer, desto eher reißt das Seil.", ac: "#3fd0c8", keys: "Einholen: Leertaste, Enter oder Knopf" },
  eisenfront: { key: "tank", name: "Panzerjagd", sub: "Feindliche Panzer rücken an. Halte die Stellung, so lange die Zeit läuft.", ac: "#a7c060", keys: "Fahren: W A S D oder Pfeile · Zielen: Maus · Feuer: Klick oder Leertaste" },
  neustadt: { key: "tower", name: "Turmbau", sub: "Der Kran schwenkt ein Stockwerk. Lass es genau auf den Turm fallen. Kassieren geht jederzeit, ein Fehlwurf bringt alles zum Einsturz.", ac: "#6fdc8c", keys: "Ablassen: Leertaste oder Klick · Kassieren: Enter" },
};
const arTheme = () => AR_THEME[WORLD_ID] || AR_THEME.sternenwrack;
// Gewinn-Tabellen der Geschicklichkeitsspiele: [Punkte ab, Multiplikator]
const AR_TABLE = {
  astro: [[0, 0], [15, .5], [30, 1], [45, 1.5], [65, 2.5], [90, 4], [120, 6]],
  tank: [[0, 0], [4, .5], [8, 1], [12, 1.5], [17, 2.5], [23, 4], [30, 6]],
};
const arMult = (tab, pts) => { let m = 0; for (const [p, x] of tab) if (pts >= p) m = x; return m; };
const DEEP_P = .9, DEEP_MAX = 18;                 // Seil hält pro Meter mit 90 %; Erwartungswert bleibt immer 96 %
const deepMult = n => n ? .96 / Math.pow(DEEP_P, n) : 0;

let ar = null, arPack = 10, arRaf = 0, arLast = 0, arStats = { n: 0, net: 0 };
const arKeys = new Set();

(function setupArcade() {
  const t = arTheme();
  document.body.insertAdjacentHTML("beforeend", `<div class="bonus" id="arcade" hidden role="dialog" aria-modal="true" aria-labelledby="arTitle" style="z-index:260;--ac:${t.ac}">
  <div class="bonus-card"><div class="ar-head"><div><h2 id="arTitle">${t.name}</h2><p>${t.sub}</p></div></div>
  <div class="ar-stage" id="arStage"><canvas id="arCanvas" width="${AR_W}" height="${AR_H}"></canvas>
    <div class="ar-hud"><span id="arHudL"></span><span id="arHudR"></span></div>
    <div class="ar-over" id="arOver"><div><h3 id="arOverT"></h3><p id="arOverP"></p>
      <div class="ar-packs" id="arPacks">${AR_PACKS.map(p => `<button type="button" data-p="${p}">${p}× Einsatz</button>`).join("")}</div>
      <div class="ar-table" id="arTable"></div>
      <button type="button" class="bbtn" id="arStart">Spielen</button></div></div></div>
  <div class="ar-row"><span class="ar-keys">${t.keys}</span><span><button type="button" class="bbtn" id="arCash" hidden>Kassieren</button> <button type="button" class="bbtn ghost" id="arClose">Schließen</button></span></div>
  </div></div>`);
  const grid = document.querySelector(".dock .xtiles");
  const ic = `<svg viewBox="0 0 40 40" aria-hidden="true"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="rgba(0,0,0,.35)" stroke="${t.ac}" stroke-width="2"/><rect x="10" y="12" width="20" height="14" rx="3" fill="none" stroke="${t.ac}" stroke-width="2"/><path d="M14 19h5M16.5 16.5v5" stroke="${t.ac}" stroke-width="2" stroke-linecap="round"/><circle cx="24" cy="18" r="1.6" fill="${t.ac}"/><circle cx="26.5" cy="21" r="1.6" fill="${t.ac}"/><path d="M15 30h10" stroke="${t.ac}" stroke-width="2" stroke-linecap="round"/></svg>`;
  if (grid) grid.insertAdjacentHTML("beforeend", `<button type="button" class="xtile" id="arTile" style="--xc:${t.ac}">${ic}<span><b>${t.name}</b><small>Spielhalle · nur in dieser Welt</small></span></button>`);
  $("arTile") && $("arTile").addEventListener("click", openArcade);
  $("arClose").addEventListener("click", closeArcade);
  $("arStart").addEventListener("click", arStart);
  $("arCash").addEventListener("click", () => arCashOut());
  $("arPacks").addEventListener("click", e => { const b = e.target.closest("button[data-p]"); if (!b || b.disabled) return; arPack = +b.dataset.p; arMenu(); });
  const cv = $("arCanvas");
  const pos = e => { const r = cv.getBoundingClientRect(); return { x: (e.clientX - r.left) * AR_W / r.width, y: (e.clientY - r.top) * AR_H / r.height }; };
  cv.addEventListener("pointermove", e => { if (ar) { ar.mouse = pos(e); } });
  cv.addEventListener("pointerdown", e => { if (!ar || !ar.run) return; ar.mouse = pos(e); ar.down = true; ar.tap = true; e.preventDefault(); });
  window.addEventListener("pointerup", () => { if (ar) ar.down = false; });
  window.addEventListener("keydown", e => {
    if (!mmOpen("arcade")) return;
    if (e.key === "Escape") { closeArcade(); e.preventDefault(); e.stopImmediatePropagation(); return; }
    arKeys.add(e.key.toLowerCase());
    if (ar && ar.run) { if (e.key === " " || e.key === "ArrowUp") ar.tap = true; if (e.key === "Enter") arCashOut(); }
    else if (e.key === "Enter" || e.key === " ") { if (!$("arStart").disabled) arStart(); }
    e.preventDefault(); e.stopImmediatePropagation();
  }, true);
  window.addEventListener("keyup", e => { arKeys.delete(e.key.toLowerCase()); });
})();

const arStake = () => bet() * arPack;
function arMenu(title, text) {
  const t = arTheme();
  $("arOverT").textContent = title || t.name;
  $("arOverP").textContent = text || `Einsatz ${fmtN(arStake())} Credits. ${t.key === "deep" ? "Jeder Meter Tiefe erhöht den Gewinn, aber das Seil kann reißen." : t.key === "tower" ? "Jedes Stockwerk erhöht den Gewinn, je genauer, desto mehr." : "Je mehr Punkte, desto höher der Gewinn."}`;
  document.querySelectorAll("#arPacks button").forEach(b => { const p = +b.dataset.p; b.setAttribute("aria-pressed", String(p === arPack)); b.disabled = state.credits < bet() * p; });
  const tab = t.key === "deep" ? [3, 6, 9, 12, 15, 18].map(n => `${n} m: ${fmtM(+deepMult(n).toFixed(1))}`)
    : t.key === "tower" ? ["Präzise Stockwerke bringen am meisten", "perfekt +0,30×", "knapp +0,08×"]
    : AR_TABLE[t.key].filter(r => r[1] > 0).map(([p, m]) => `ab ${p}: ${fmtM(m)}`);
  $("arTable").innerHTML = tab.map(s => `<span>${s}</span>`).join("");
  $("arStart").disabled = state.credits < arStake();
  $("arStart").textContent = state.credits < arStake() ? "Zu wenig Credits" : "Spielen";
  $("arOver").hidden = false; $("arCash").hidden = true;
  arHud();
}
function openArcade() {
  if (!machineIdle()) return;
  if (typeof autoLeft !== "undefined" && autoLeft > 0) { autoLeft = 0; try { clearAutoMarks(); } catch (e) {} }
  arStats = { n: 0, net: 0 }; ar = null;
  $("arcade").hidden = false; try { sfx.click(); } catch (e) {}
  arMenu(); arDrawIdle();
  $("arStart").focus({ preventScroll: true });
}
function closeArcade() {
  if (ar && ar.run) { if (arTheme().key === "deep" || arTheme().key === "tower") { arCashOut(); } else { arEnd(true); } return; }
  cancelAnimationFrame(arRaf); ar = null;
  $("arcade").hidden = true; try { sfx.click(); } catch (e) {}
  if (arStats.n) radio(`Funk: Spielhalle beendet. ${fmtN(arStats.n)} Runden, ${(arStats.net >= 0 ? "+" : "") + fmtN(arStats.net)} Credits.`);
  render(); saveGame();
  busy = true; processProgress().catch(() => {}).finally(() => { busy = false; render(); mmResume(); });
}
function arStart() {
  const stake = arStake(); if (state.credits < stake) return;
  state.credits -= stake; render();
  const k = arTheme().key;
  ar = { k, stake, run: true, t: 0, score: 0, lives: 3, mouse: { x: AR_W / 2, y: AR_H / 2 }, down: false, tap: false, fx: [] };
  AR_GAMES[k].init(ar);
  $("arOver").hidden = true; $("arCash").hidden = !(k === "deep" || k === "tower");
  try { sfx.click(); } catch (e) {}
  arLast = performance.now(); cancelAnimationFrame(arRaf); arRaf = requestAnimationFrame(arLoop);
}
function arLoop(now) {
  if (!ar) return;
  const dt = Math.min(.05, (now - arLast) / 1000); arLast = now;
  if (ar.run) { AR_GAMES[ar.k].step(ar, dt); ar.tap = false; }
  ar.fx = ar.fx.filter(p => (p.life -= dt) > 0);
  ar.fx.forEach(p => { p.x += p.vx * dt; p.y += p.vy * dt; });
  const c = $("arCanvas").getContext("2d");
  AR_GAMES[ar.k].draw(c, ar);
  ar.fx.forEach(p => { c.globalAlpha = Math.min(1, p.life * 2); c.fillStyle = p.c; c.beginPath(); c.arc(p.x, p.y, p.r, 0, 7); c.fill(); });
  c.globalAlpha = 1;
  arHud();
  if (ar.run || ar.fx.length) arRaf = requestAnimationFrame(arLoop);
}
function arBoom(x, y, col, n = 14, sp = 160) { for (let i = 0; i < n; i++) { const a = Math.random() * 7, v = sp * (.3 + Math.random()); ar.fx.push({ x, y, vx: Math.cos(a) * v, vy: Math.sin(a) * v, r: 1.5 + Math.random() * 2.5, c: col, life: .4 + Math.random() * .5 }); } }
function arHud() {
  if (!ar) { $("arHudL").textContent = ""; $("arHudR").innerHTML = `Credits <b>${fmtN(state.credits)}</b>`; return; }
  const g = AR_GAMES[ar.k];
  $("arHudL").innerHTML = g.hud(ar);
  $("arHudR").innerHTML = `Gewinn jetzt <b>${fmtM(+g.mult(ar).toFixed(2))}</b> · ${fmtN(Math.floor(ar.stake * g.mult(ar)))}`;
}
function arCashOut() { if (!ar || !ar.run) return; if (ar.k === "deep" || ar.k === "tower") arEnd(false); }
function arEnd(lost, why) {
  if (!ar || !ar.run) return;
  ar.run = false;
  const m = lost ? 0 : AR_GAMES[ar.k].mult(ar), win = Math.floor(ar.stake * m);
  state.credits += win; arStats.n++; arStats.net += win - ar.stake;
  if (typeof bump === "function") bump("arcadeRounds");
  if (win > ar.stake) { try { sfx.win && sfx.win(); } catch (e) {} } else { try { sfx.click(); } catch (e) {} }
  render(); saveGame();
  const head = win > 0 ? `${fmtM(+m.toFixed(2))} · +${fmtN(win)} Credits` : (why || "Leider nichts gewonnen");
  arMenu(head, `${AR_GAMES[ar.k].summary(ar)} Nochmal?`);
}
function arDrawIdle() { const c = $("arCanvas").getContext("2d"); const g = AR_GAMES[arTheme().key]; const dummy = { idle: true, t: 0, fx: [], mouse: { x: AR_W / 2, y: AR_H / 2 } }; g.init(dummy); g.draw(c, dummy); }

/* --- Hilfen fürs Zeichnen --- */
function arBg(c, top, bottom) { const g = c.createLinearGradient(0, 0, 0, AR_H); g.addColorStop(0, top); g.addColorStop(1, bottom); c.fillStyle = g; c.fillRect(0, 0, AR_W, AR_H); }
function arStars(c, a, t, speed) { c.fillStyle = "#fff"; for (const s of a.stars) { const y = (s.y + t * speed * s.z) % AR_H; c.globalAlpha = .3 + s.z * .5; c.fillRect(s.x, y, s.z * 1.6, s.z * 1.6); } c.globalAlpha = 1; }

const AR_GAMES = {
  /* ===== Sternenwrack: Asteroidenfeld ===== */
  astro: {
    init(a) { a.dur = 45; a.x = AR_W / 2; a.shots = []; a.rocks = []; a.cool = 0; a.spawn = 0; a.inv = 0; a.stars = Array.from({ length: 70 }, () => ({ x: Math.random() * AR_W, y: Math.random() * AR_H, z: Math.random() })); },
    step(a, dt) {
      a.t += dt; const left = arKeys.has("arrowleft") || arKeys.has("a"), right = arKeys.has("arrowright") || arKeys.has("d");
      if (left || right) a.x += (right - left) * 330 * dt; else a.x += (a.mouse.x - a.x) * Math.min(1, dt * 9);
      a.x = Math.max(24, Math.min(AR_W - 24, a.x));
      if ((a.cool -= dt) <= 0) { a.cool = .17; a.shots.push({ x: a.x - 7, y: AR_H - 52 }, { x: a.x + 7, y: AR_H - 52 }); }
      a.shots.forEach(s => s.y -= 520 * dt); a.shots = a.shots.filter(s => s.y > -10);
      const lvl = Math.min(1, a.t / a.dur);
      if ((a.spawn -= dt) <= 0) { a.spawn = .55 - lvl * .33; const r = 12 + Math.random() * 20; a.rocks.push({ x: 20 + Math.random() * (AR_W - 40), y: -r, r, hp: r > 24 ? 3 : r > 17 ? 2 : 1, vx: (Math.random() - .5) * 60, vy: 70 + Math.random() * 60 + lvl * 90, rot: Math.random() * 6, vr: (Math.random() - .5) * 2, pts: Array.from({ length: 9 }, () => .75 + Math.random() * .35) }); }
      for (const r of a.rocks) { r.x += r.vx * dt; r.y += r.vy * dt; r.rot += r.vr * dt;
        for (const s of a.shots) if (!s.hit && Math.hypot(s.x - r.x, s.y - r.y) < r.r) { s.hit = true; r.hp--; arBoom(s.x, s.y, "#9fb3ff", 4, 90); if (r.hp <= 0) { r.dead = true; a.score += r.r > 24 ? 3 : r.r > 17 ? 2 : 1; arBoom(r.x, r.y, "#ffc94a", 18, 200); try { tone(180 + Math.random() * 60, .12, { type: "square", vol: .05, slide: -.5 }); } catch (e) {} } }
        if (!r.dead && a.inv <= 0 && Math.hypot(r.x - a.x, r.y - (AR_H - 36)) < r.r + 14) { r.dead = true; a.lives--; a.inv = 1.5; arBoom(a.x, AR_H - 36, "#ff5a6a", 26, 240); try { tone(90, .4, { type: "sawtooth", vol: .08, slide: -.6 }); } catch (e) {} }
      }
      a.shots = a.shots.filter(s => !s.hit); a.rocks = a.rocks.filter(r => !r.dead && r.y < AR_H + 40);
      a.inv -= dt;
      if (a.lives <= 0) arEnd(false, "Schiff zerstört"); else if (a.t >= a.dur) arEnd(false);
    },
    draw(c, a) {
      arBg(c, "#04061a", "#0d0a2a"); arStars(c, a, a.t || performance.now() / 1000, 60);
      c.save(); c.globalAlpha = .35; c.fillStyle = "#3d2470"; c.beginPath(); c.arc(560, 70, 60, 0, 7); c.fill(); c.restore();
      for (const r of a.rocks || []) { c.save(); c.translate(r.x, r.y); c.rotate(r.rot); c.beginPath(); r.pts.forEach((k, i) => { const an = i / r.pts.length * Math.PI * 2; c.lineTo(Math.cos(an) * r.r * k, Math.sin(an) * r.r * k); }); c.closePath(); c.fillStyle = "#4a5262"; c.fill(); c.strokeStyle = "#9fb3ff"; c.lineWidth = 2; c.stroke(); c.restore(); }
      c.fillStyle = "#7ff7ff"; for (const s of a.shots || []) c.fillRect(s.x - 1.5, s.y - 8, 3, 12);
      const y = AR_H - 36; if (!(a.inv > 0 && Math.floor(a.inv * 10) % 2)) { c.save(); c.translate(a.x, y);
        c.fillStyle = "#ff9a3c"; c.beginPath(); c.moveTo(-6, 14); c.lineTo(0, 22 + Math.random() * 8); c.lineTo(6, 14); c.fill();
        c.fillStyle = "#4a5262"; c.strokeStyle = "#9fb3ff"; c.lineWidth = 2; c.beginPath(); c.moveTo(0, -18); c.lineTo(16, 14); c.lineTo(0, 8); c.lineTo(-16, 14); c.closePath(); c.fill(); c.stroke();
        c.fillStyle = "#4fe3ff"; c.beginPath(); c.arc(0, -2, 4, 0, 7); c.fill(); c.restore(); }
    },
    mult: a => arMult(AR_TABLE.astro, a.score),
    hud: a => `Punkte <b>${a.score}</b> · Leben <b>${"♥".repeat(Math.max(0, a.lives))}</b> · Zeit <b>${Math.max(0, Math.ceil(a.dur - a.t))}</b>`,
    summary: a => `${a.score} Punkte.`,
  },

  /* ===== Treibgut: Tiefsee-Angel ===== */
  deep: {
    init(a) { a.depth = 0; a.tick = 0; a.hook = 30; a.fish = []; a.snap = false; a.bub = Array.from({ length: 30 }, () => ({ x: Math.random() * AR_W, y: Math.random() * AR_H, z: Math.random() })); },
    step(a, dt) {
      a.t += dt; a.hook += (Math.min(AR_H - 70, 60 + a.depth * 16) - a.hook) * Math.min(1, dt * 4);
      if ((a.tick += dt) >= .8) { a.tick = 0;
        if (a.depth >= DEEP_MAX) { arCashOut(); return; }
        if (Math.random() > DEEP_P) { a.snap = true; arBoom(AR_W / 2, a.hook, "#cfe8ff", 22, 160); try { tone(220, .5, { type: "triangle", vol: .08, slide: -.8 }); } catch (e) {} arEnd(true, "Das Seil ist gerissen"); return; }
        a.depth++; a.fish.push({ d: a.depth, x: AR_W / 2 + (Math.random() < .5 ? -1 : 1) * (60 + Math.random() * 140), s: 8 + a.depth * 1.1 });
        try { tone(500 + a.depth * 40, .12, { type: "sine", vol: .05 }); } catch (e) {}
      }
      if (a.tap) arCashOut();
    },
    draw(c, a) {
      const d = a.depth || 0, k = Math.min(1, d / DEEP_MAX);
      const top = `rgb(${Math.round(30 - 26 * k)},${Math.round(110 - 95 * k)},${Math.round(150 - 120 * k)})`;
      arBg(c, top, "#020611");
      c.fillStyle = "rgba(255,255,255,.08)"; for (const b of a.bub) { const y = (b.y - (a.t || performance.now() / 1000) * 30 * b.z + AR_H * 10) % AR_H; c.beginPath(); c.arc(b.x, y, 1 + b.z * 2.5, 0, 7); c.fill(); }
      c.fillStyle = "#8a5e34"; c.fillRect(AR_W / 2 - 60, 6, 120, 10);
      c.strokeStyle = a.snap ? "rgba(255,255,255,.2)" : "#e9e2cf"; c.lineWidth = 1.5; c.beginPath(); c.moveTo(AR_W / 2, 16); c.lineTo(AR_W / 2, a.hook); c.stroke();
      c.strokeStyle = "#ffd27a"; c.lineWidth = 2.5; c.beginPath(); c.arc(AR_W / 2 - 5, a.hook, 6, 0, Math.PI); c.stroke();
      for (const f of (a.fish || []).slice(-6)) { const y = Math.min(AR_H - 40, 60 + f.d * 16) - 30, hue = 180 - f.d * 9;
        c.save(); c.translate(f.x + Math.sin((a.t || 0) * 2 + f.d) * 8, y); c.fillStyle = `hsl(${hue},70%,60%)`; c.beginPath(); c.ellipse(0, 0, f.s, f.s * .5, 0, 0, 7); c.fill();
        c.beginPath(); c.moveTo(-f.s, 0); c.lineTo(-f.s - 8, -6); c.lineTo(-f.s - 8, 6); c.fill(); c.fillStyle = "#fff"; c.beginPath(); c.arc(f.s * .5, -2, 2, 0, 7); c.fill(); c.restore(); }
      c.fillStyle = "rgba(255,255,255,.75)"; c.font = "700 14px system-ui"; c.textAlign = "left"; c.fillText(`${d} m`, 14, AR_H - 14);
      c.fillStyle = "rgba(255,120,100,.85)"; c.textAlign = "right"; c.fillText(`Reißrisiko ${Math.round((1 - DEEP_P) * 100)} % pro Meter`, AR_W - 14, AR_H - 14); c.textAlign = "left";
    },
    mult: a => deepMult(a.depth),
    hud: a => `Tiefe <b>${a.depth} m</b> · Fische <b>${a.fish.length}</b>`,
    summary: a => `Tiefe ${a.depth} m.`,
  },

  /* ===== Eisenfront: Panzerjagd (Vogelperspektive, düster) ===== */
  tank: {
    init(a) { a.dur = 60; a.p = { x: AR_W / 2, y: AR_H / 2, a: 0, t: 0 }; a.foes = []; a.shells = []; a.spawn = 1; a.cool = 0; a.inv = 0;
      a.decor = Array.from({ length: 14 }, () => ({ x: Math.random() * AR_W, y: Math.random() * AR_H, r: 10 + Math.random() * 26, k: Math.random() < .5 })); },
    step(a, dt) {
      a.t += dt; const p = a.p;
      let mx = (arKeys.has("d") || arKeys.has("arrowright")) - (arKeys.has("a") || arKeys.has("arrowleft")), my = (arKeys.has("s") || arKeys.has("arrowdown")) - (arKeys.has("w") || arKeys.has("arrowup"));
      if (!mx && !my && a.down) { const dx = a.mouse.x - p.x, dy = a.mouse.y - p.y, l = Math.hypot(dx, dy); if (l > 30) { mx = dx / l; my = dy / l; } }
      const l = Math.hypot(mx, my); if (l) { p.x += mx / l * 120 * dt; p.y += my / l * 120 * dt; p.a = Math.atan2(my, mx); }
      p.x = Math.max(18, Math.min(AR_W - 18, p.x)); p.y = Math.max(18, Math.min(AR_H - 18, p.y));
      p.t = Math.atan2(a.mouse.y - p.y, a.mouse.x - p.x);
      a.cool -= dt;
      if ((a.tap || arKeys.has(" ") || a.down) && a.cool <= 0) { a.cool = .45; a.shells.push({ x: p.x + Math.cos(p.t) * 22, y: p.y + Math.sin(p.t) * 22, vx: Math.cos(p.t) * 380, vy: Math.sin(p.t) * 380, own: true, life: 1.4 }); try { tone(110, .15, { type: "sawtooth", vol: .06, slide: -.5 }); } catch (e) {} }
      const lvl = Math.min(1, a.t / a.dur);
      if ((a.spawn -= dt) <= 0 && a.foes.length < 3 + Math.floor(lvl * 4)) { a.spawn = 2.4 - lvl * 1.4; const side = Math.floor(Math.random() * 4);
        const x = side === 0 ? -20 : side === 1 ? AR_W + 20 : Math.random() * AR_W, y = side === 2 ? -20 : side === 3 ? AR_H + 20 : Math.random() * AR_H;
        a.foes.push({ x, y, a: 0, cool: 1.5 + Math.random() * 1.5, hp: lvl > .6 && Math.random() < .3 ? 2 : 1 }); }
      for (const f of a.foes) { const dx = p.x - f.x, dy = p.y - f.y, d = Math.hypot(dx, dy); f.a = Math.atan2(dy, dx);
        if (d > 130) { f.x += dx / d * (45 + lvl * 25) * dt; f.y += dy / d * (45 + lvl * 25) * dt; }
        if ((f.cool -= dt) <= 0) { f.cool = 2.2 - lvl * .9 + Math.random(); a.shells.push({ x: f.x + Math.cos(f.a) * 20, y: f.y + Math.sin(f.a) * 20, vx: Math.cos(f.a) * 210, vy: Math.sin(f.a) * 210, own: false, life: 2.5 }); } }
      for (const s of a.shells) { s.x += s.vx * dt; s.y += s.vy * dt; s.life -= dt;
        if (s.own) { for (const f of a.foes) if (!f.dead && Math.hypot(s.x - f.x, s.y - f.y) < 17) { s.life = 0; f.hp--; arBoom(s.x, s.y, "#ffb04a", 8, 120); if (f.hp <= 0) { f.dead = true; a.score++; arBoom(f.x, f.y, "#ff6a3a", 26, 220); try { tone(70, .35, { type: "sawtooth", vol: .08, slide: -.4 }); } catch (e) {} } } }
        else if (a.inv <= 0 && Math.hypot(s.x - p.x, s.y - p.y) < 15) { s.life = 0; a.lives--; a.inv = 1.2; arBoom(p.x, p.y, "#ff3a3a", 24, 200); } }
      a.shells = a.shells.filter(s => s.life > 0); a.foes = a.foes.filter(f => !f.dead); a.inv -= dt;
      if (a.lives <= 0) arEnd(false, "Panzer zerstört"); else if (a.t >= a.dur) arEnd(false);
    },
    draw(c, a) {
      c.fillStyle = "#1b1c17"; c.fillRect(0, 0, AR_W, AR_H);
      for (const d of a.decor) { if (d.k) { c.fillStyle = "rgba(0,0,0,.35)"; c.beginPath(); c.arc(d.x, d.y, d.r, 0, 7); c.fill(); } else { c.fillStyle = "#2b2a22"; c.fillRect(d.x, d.y, d.r, d.r * .7); c.strokeStyle = "#3d3b30"; c.strokeRect(d.x, d.y, d.r, d.r * .7); } }
      const tank = (x, y, a1, t1, body, top, flash) => { c.save(); c.translate(x, y); c.rotate(a1); c.fillStyle = "#121310"; c.fillRect(-16, -13, 32, 6); c.fillRect(-16, 7, 32, 6); c.fillStyle = flash ? "#fff" : body; c.fillRect(-13, -9, 26, 18); c.restore();
        c.save(); c.translate(x, y); c.rotate(t1); c.fillStyle = top; c.fillRect(0, -2.5, 22, 5); c.beginPath(); c.arc(0, 0, 7, 0, 7); c.fill(); c.restore(); };
      for (const f of a.foes || []) tank(f.x, f.y, f.a, f.a, f.hp > 1 ? "#5a2a24" : "#4a3a30", "#2e211b");
      const p = a.p; if (!(a.inv > 0 && Math.floor(a.inv * 10) % 2)) tank(p.x, p.y, p.a, p.t, "#5a6a2c", "#3e4a1e");
      for (const s of a.shells || []) { c.fillStyle = s.own ? "#ffe08a" : "#ff6a4a"; c.beginPath(); c.arc(s.x, s.y, 3, 0, 7); c.fill(); }
      const g = c.createRadialGradient(a.p.x, a.p.y, 60, a.p.x, a.p.y, 420); g.addColorStop(0, "rgba(0,0,0,0)"); g.addColorStop(1, "rgba(0,0,0,.78)"); c.fillStyle = g; c.fillRect(0, 0, AR_W, AR_H);
    },
    mult: a => arMult(AR_TABLE.tank, a.score),
    hud: a => `Abschüsse <b>${a.score}</b> · Panzerung <b>${"■".repeat(Math.max(0, a.lives))}</b> · Zeit <b>${Math.max(0, Math.ceil(a.dur - a.t))}</b>`,
    summary: a => `${a.score} Abschüsse.`,
  },

  /* ===== Neustadt: Turmbau ===== */
  tower: {
    init(a) { a.floors = [{ x: AR_W / 2 - 70, w: 140 }]; a.m = 0; a.cur = { x: 0, w: 140, dir: 1 }; a.drop = null; a.cam = 0; a.perfect = 0; },
    step(a, dt) {
      a.t += dt; const n = a.floors.length, sp = 170 + n * 18;
      if (!a.drop) { a.cur.x += a.cur.dir * sp * dt; if (a.cur.x < 0) { a.cur.x = 0; a.cur.dir = 1; } if (a.cur.x + a.cur.w > AR_W) { a.cur.x = AR_W - a.cur.w; a.cur.dir = -1; }
        if (a.tap) a.drop = { x: a.cur.x, w: a.cur.w, y: 60, vy: 0 }; }
      else { const d = a.drop; d.vy += 1400 * dt; d.y += d.vy * dt;
        const land = AR_H - 40 - n * 22 + a.cam;
        if (d.y >= land) { const top = a.floors[n - 1], l = Math.max(d.x, top.x), r = Math.min(d.x + d.w, top.x + top.w), ov = r - l;
          if (ov <= 4) { arBoom(d.x + d.w / 2, land, "#c9b38a", 30, 220); try { tone(80, .6, { type: "sawtooth", vol: .08, slide: -.6 }); } catch (e) {} a.drop = null; arEnd(true, "Der Turm ist eingestürzt"); return; }
          const f = ov / d.w;
          if (f > .95) { a.floors.push({ x: top.x, w: top.w }); a.m += .3; a.perfect++; arBoom(top.x + top.w / 2, land, "#ffe08a", 14, 140); try { tone(880, .15, { type: "sine", vol: .06 }); } catch (e) {} }
          else { a.floors.push({ x: l, w: ov }); a.m += .08 + .2 * f; try { tone(330 + f * 300, .1, { type: "triangle", vol: .06 }); } catch (e) {} }
          a.cur = { x: Math.random() < .5 ? 0 : AR_W - ov, w: a.floors[a.floors.length - 1].w, dir: Math.random() < .5 ? 1 : -1 }; a.drop = null;
          if (a.floors.length > 12) a.cam += 22;
          if (a.floors.length > 30) { arCashOut(); return; } } }
    },
    draw(c, a) {
      arBg(c, "#2a5a8a", "#f0c890");
      c.fillStyle = "rgba(28,58,90,.55)"; [[30, 160], [90, 120], [470, 140], [540, 100], [590, 150]].forEach(([x, h]) => c.fillRect(x, AR_H - h, 44, h));
      c.fillStyle = "#3a3f46"; c.fillRect(0, AR_H - 18 + (a.cam || 0), AR_W, 18);
      const col = i => ["#ffc94a", "#7ee0c8", "#4aa8ff", "#ff7a59"][i % 4];
      (a.floors || []).forEach((f, i) => { const y = AR_H - 40 - i * 22 + (a.cam || 0); if (y > AR_H) return; c.fillStyle = col(i); c.fillRect(f.x, y, f.w, 20); c.fillStyle = "rgba(255,244,200,.8)"; for (let x = f.x + 6; x < f.x + f.w - 6; x += 12) c.fillRect(x, y + 6, 5, 7); });
      c.strokeStyle = "#ffc94a"; c.lineWidth = 3; c.beginPath(); c.moveTo(0, 26); c.lineTo(AR_W, 26); c.stroke();
      const cur = a.cur || { x: AR_W / 2 - 70, w: 140 }, n = (a.floors || []).length;
      if (!a.drop) { c.strokeStyle = "#3a3f46"; c.lineWidth = 1.5; c.beginPath(); c.moveTo(cur.x + cur.w / 2, 26); c.lineTo(cur.x + cur.w / 2, 60); c.stroke(); c.fillStyle = col(n); c.fillRect(cur.x, 60, cur.w, 20); }
      else { c.fillStyle = col(n); c.fillRect(a.drop.x, a.drop.y, a.drop.w, 20); }
    },
    mult: a => Math.round(a.m * 100) / 100,
    hud: a => `Stockwerke <b>${a.floors.length - 1}</b> · Perfekt <b>${a.perfect}</b>`,
    summary: a => `${a.floors.length - 1} Stockwerke, davon ${a.perfect} perfekt.`,
  },
};
'''
