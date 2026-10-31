# Online-Funktionen über Firebase (seit SW 0.18.0, Zweig experimente):
# Freunde per Code, Rangliste (Freunde und weltweit), Geschenk alle 24 h, VS-Duell 5 Minuten, Koop-Crew.
ONLINE_CSS = r'''
#online .bonus-card { max-width: 720px; width: min(720px, 96vw); }
.ol-tabs { display: flex; gap: 6px; flex-wrap: wrap; margin: 4px 0 12px; }
.ol-tabs button { font: 700 13px var(--f-body, system-ui); padding: 8px 14px; border-radius: 99px; border: 1.5px solid rgba(255,255,255,.2); background: rgba(255,255,255,.05); color: #fff; cursor: pointer; }
.ol-tabs button[aria-pressed="true"] { border-color: var(--gold, #ffc94a); background: rgba(255,201,74,.16); }
.ol-pane[hidden] { display: none; }
.ol-me { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; justify-content: space-between; padding: 10px 12px; border-radius: 12px; background: rgba(255,255,255,.05); border: 1px solid rgba(255,255,255,.12); margin-bottom: 10px; }
.ol-code { font: 800 20px var(--f-mono, monospace); letter-spacing: .18em; color: var(--gold, #ffc94a); }
.ol-row { display: flex; gap: 8px; flex-wrap: wrap; margin: 8px 0; }
.ol-row input { flex: 1; min-width: 140px; font: 700 15px var(--f-mono, monospace); letter-spacing: .12em; text-transform: uppercase; padding: 9px 12px; border-radius: 10px; border: 1.5px solid rgba(255,255,255,.25); background: rgba(0,0,0,.3); color: #fff; }
.ol-list { display: grid; gap: 6px; margin-top: 8px; max-height: 46vh; overflow: auto; }
.ol-item { display: grid; grid-template-columns: auto 1fr auto; gap: 10px; align-items: center; padding: 8px 10px; border-radius: 10px; background: rgba(255,255,255,.04); border: 1px solid rgba(255,255,255,.08); }
.ol-item.me { border-color: rgba(255,201,74,.5); background: rgba(255,201,74,.08); }
.ol-item b { font-size: 14px; } .ol-item small { display: block; color: rgba(255,255,255,.7); font-size: 12px; }
.ol-dot { width: 9px; height: 9px; border-radius: 50%; background: #555c6e; } .ol-dot.on { background: #6fdc8c; box-shadow: 0 0 8px #6fdc8c; }
.ol-rank { font: 800 14px var(--f-mono, monospace); color: var(--gold, #ffc94a); min-width: 2.2em; text-align: right; }
.ol-acts { display: flex; gap: 6px; flex-wrap: wrap; justify-content: flex-end; }
.ol-acts button, .ol-small { font: 700 12px var(--f-body, system-ui); padding: 6px 10px; border-radius: 8px; border: 1.5px solid rgba(255,255,255,.25); background: rgba(255,255,255,.06); color: #fff; cursor: pointer; }
.ol-acts button:disabled { opacity: .45; cursor: not-allowed; }
.ol-acts button.hot { border-color: var(--gold, #ffc94a); color: var(--gold, #ffc94a); }
.ol-msg { min-height: 1.4em; font-size: 13px; color: rgba(255,255,255,.85); margin: 6px 0; }
.ol-msg.err { color: #ff8a8a; } .ol-msg.ok { color: #8fe6a6; }
.ol-gifts { display: grid; gap: 6px; margin-bottom: 10px; }
.ol-gift { display: flex; justify-content: space-between; align-items: center; gap: 8px; padding: 8px 12px; border-radius: 10px; background: rgba(255,201,74,.12); border: 1px solid rgba(255,201,74,.45); }
.ol-info { font-size: 13px; color: rgba(255,255,255,.82); line-height: 1.5; margin: 0 0 10px; }
.ol-big { display: flex; gap: 12px; justify-content: center; align-items: center; margin: 14px 0; font: 800 28px var(--f-mono, monospace); }
.ol-big span { color: rgba(255,255,255,.6); font-size: 16px; }
#vsBar { position: fixed; top: 8px; left: 50%; transform: translateX(-50%); z-index: 250; display: flex; gap: 14px; align-items: center; padding: 8px 16px; border-radius: 99px; background: rgba(8,10,20,.92); border: 1.5px solid var(--gold, #ffc94a); font: 800 14px var(--f-mono, monospace); color: #fff; box-shadow: 0 6px 24px rgba(0,0,0,.5); }
#vsBar[hidden] { display: none; }
#vsBar .t { color: var(--gold, #ffc94a); }
#vsBar .lead { color: #6fdc8c; }
#crewFeed { position: fixed; top: 86px; right: 14px; z-index: 230; width: 290px; pointer-events: none; font: 700 13px var(--f-body, system-ui); }
#crewFeed[hidden] { display: none; }
#crewFeed .cf-head { pointer-events: auto; display: flex; justify-content: space-between; align-items: center; gap: 8px; padding: 5px 10px; border-radius: 10px 10px 0 0; background: rgba(8,10,20,.85); border: 1px solid rgba(255,255,255,.14); border-bottom: 0; font: 800 10px var(--f-mono, monospace); letter-spacing: .2em; color: #6fdc8c; }
#crewFeed .cf-head button { background: none; border: 0; color: rgba(255,255,255,.7); cursor: pointer; font: 800 12px var(--f-mono, monospace); padding: 0 2px; }
#crewFeed .cf-head i { width: 7px; height: 7px; border-radius: 50%; background: #ff4b6a; box-shadow: 0 0 8px #ff4b6a; display: inline-block; margin-right: 6px; animation: cfLive 1.2s ease-in-out infinite; }
@keyframes cfLive { 50% { opacity: .3; } }
#crewFeed .cf-list { display: grid; gap: 4px; padding-top: 4px; }
#crewFeed.min .cf-list { display: none; }
#crewFeed .cf-row { display: flex; align-items: center; gap: 8px; padding: 6px 10px; border-radius: 8px; background: linear-gradient(90deg, rgba(0,0,0,.78), rgba(0,0,0,.55)); border-left: 3px solid var(--pc); color: #fff; animation: cfIn .35s cubic-bezier(.2,1.3,.4,1); transition: opacity .6s, transform .6s; text-shadow: 0 1px 2px #000; }
#crewFeed .cf-row.old { opacity: .45; }
#crewFeed .cf-row.gone { opacity: 0; transform: translateX(30px); }
#crewFeed .cf-row b { color: var(--pc); max-width: 105px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
#crewFeed .cf-row .cf-ic { font-size: 14px; }
#crewFeed .cf-row .cf-amt { margin-left: auto; color: #ffc94a; font-family: var(--f-mono, monospace); white-space: nowrap; }
#crewFeed .cf-row small { color: rgba(255,255,255,.6); font-weight: 600; font-size: 11px; white-space: nowrap; }
#crewFeed .cf-row.big { background: linear-gradient(90deg, rgba(120,80,0,.85), rgba(0,0,0,.6)); }
#crewFeed .cf-row.me { border-left-color: #ffffff; }
@keyframes cfIn { from { opacity: 0; transform: translateX(40px); } to { opacity: 1; transform: none; } }
@media (max-width: 700px) { #crewFeed { top: auto; bottom: 86px; right: 8px; width: 230px; font-size: 12px; } }
.mmchip .ol-badge { display: inline-block; min-width: 16px; height: 16px; border-radius: 8px; background: #ff4b6a; color: #fff; font: 800 10px/16px system-ui; text-align: center; margin-left: 4px; }
'''

ONLINE_JS = r'''
/* ---------- Online: Freunde, Rangliste, Geschenke, VS, Koop (Firebase) ---------- */
const FB_CFG = { apiKey: "AIzaSyBcnwWCg5qhD-g8DWnsNh-teUZihc4CKtM", authDomain: "salvage-grind.firebaseapp.com", databaseURL: "https://salvage-grind-default-rtdb.europe-west1.firebasedatabase.app", projectId: "salvage-grind", storageBucket: "salvage-grind.firebasestorage.app", messagingSenderId: "169044714781", appId: "1:169044714781:web:38796d21b781bed839adf4" };
const FB_VER = "10.14.1", GIFT_MS = 864e5, VS_MS = 300000, COOP_SHARE = .2, CREW_MAX = 4, VAULT_MS = 300000;
const OL = { db: null, uid: null, ready: false, err: "", code: "", friends: {}, people: {}, gifts: {}, tab: "friends", board: "friends", sent: {}, vs: null, queueRef: null,
  crew: null, crewM: {}, crewInv: {}, ticker: [], live: {}, dayBest: 0, vault: null, vaultAt: 0, confirm: false };
try { OL.crew = localStorage.getItem("welten-crew") || null; OL.vault = localStorage.getItem("welten-vault") || null; } catch (e) {}
const olDay = () => new Date().toISOString().slice(0, 10);
try { const d = JSON.parse(localStorage.getItem("welten-daybest") || "{}"); if (d.d === olDay()) OL.dayBest = d.a || 0; } catch (e) {}
const olName = () => (state.captain || state.shipName || "Kapitän").slice(0, 20);
const olPair = (a, b) => [a, b].sort().join("_");
function olScript(src) { return new Promise((ok, no) => { const s = document.createElement("script"); s.src = src; s.onload = ok; s.onerror = () => no(new Error("Laden fehlgeschlagen")); document.head.appendChild(s); }); }
async function olInit() {
  if (OL.ready || OL.loading) return OL.loading;
  OL.loading = (async () => {
    try {
      if (!window.firebase) { const base = `https://www.gstatic.com/firebasejs/${FB_VER}/`; await olScript(base + "firebase-app-compat.js"); await Promise.all([olScript(base + "firebase-auth-compat.js"), olScript(base + "firebase-database-compat.js")]); }
      const app = firebase.apps.length ? firebase.app() : firebase.initializeApp(FB_CFG);
      const cred = firebase.auth().currentUser ? null : await firebase.auth().signInAnonymously();
      OL.uid = firebase.auth().currentUser.uid; OL.db = firebase.database();
      const me = (await OL.db.ref("players/" + OL.uid).get()).val() || {};
      OL.code = me.code || await olNewCode();
      await olPublish();
      OL.db.ref("friends/" + OL.uid).on("value", s => { OL.friends = s.val() || {}; olLoadPeople(); olTickerListen(); });
      OL.db.ref("crewInv/" + OL.uid).on("value", s => { OL.crewInv = s.val() || {}; olBadge(); if (mmOpen("online")) olRender(); });
      if (OL.crew) olCrewListen();
      OL.db.ref("gifts/" + OL.uid).on("value", s => { OL.gifts = s.val() || {}; olBadge(); if (mmOpen("online")) olRender(); });
      setInterval(olPublish, 60000);
      setInterval(olTick, 2000);
      OL.ready = true; OL.err = "";
    } catch (e) { OL.err = "Keine Verbindung zum Online-Dienst. Prüfe deine Internetverbindung."; try { console.warn("Online:", e); } catch (er) {} }
    OL.loading = null; if (mmOpen("online")) olRender();
  })();
  return OL.loading;
}
async function olNewCode() {
  const A = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
  for (let i = 0; i < 8; i++) {
    const c = Array.from({ length: 6 }, () => A[Math.floor(Math.random() * A.length)]).join("");
    const r = await OL.db.ref("codes/" + c).transaction(v => v ? undefined : OL.uid);
    if (r.committed) return c;
  }
  throw new Error("Kein freier Code");
}
function olPublish() {
  if (!OL.db) return Promise.resolve();
  return OL.db.ref("players/" + OL.uid).update({ n: olName(), code: OL.code, on: firebase.database.ServerValue.TIMESTAMP,
    ["w/" + WORLD_ID]: { l: state.level, p: Math.round(state.peak || 0), c: Math.round(state.credits) } }).catch(() => {});
}
async function olLoadPeople() {
  const ids = Object.keys(OL.friends);
  await Promise.all(ids.map(async id => { try { OL.people[id] = (await OL.db.ref("players/" + id).get()).val() || { n: "?" }; } catch (e) {} }));
  if (mmOpen("online")) olRender();
}
const olOnline = p => p && p.on && Date.now() - p.on < 150000;
function olBadge() {
  const n = Object.values(OL.gifts).filter(g => g && !g.c).length + Object.keys(OL.crewInv).length;
  const b = $("olChip"); if (!b) return;
  b.querySelector(".ol-badge") && b.querySelector(".ol-badge").remove();
  if (n) b.insertAdjacentHTML("beforeend", `<span class="ol-badge">${n}</span>`);
}
function olMsg(t, ok) { const el = $("olMsg"); if (!el) return; el.textContent = t || ""; el.className = "ol-msg" + (t ? (ok ? " ok" : " err") : ""); }

/* --- Dialog --- */
(function setupOnline() {
  document.body.insertAdjacentHTML("beforeend", `<div class="bonus" id="online" hidden role="dialog" aria-modal="true" aria-labelledby="olTitle" style="z-index:260">
  <div class="bonus-card"><h2 id="olTitle" style="margin:0 0 4px">Online</h2>
  <div class="ol-tabs" id="olTabs"><button type="button" data-t="friends">Freunde</button><button type="button" data-t="board">Rangliste</button><button type="button" data-t="vs">VS-Duell</button><button type="button" data-t="coop">Koop-Crew</button><button type="button" data-t="save">Spielstand</button></div>
  <p class="ol-msg" id="olMsg" aria-live="polite"></p>
  <div class="ol-pane" id="olPane"></div>
  <div class="ar-row"><span></span><button type="button" class="bbtn ghost" id="olClose">Schließen</button></div></div></div>
  <div id="vsBar" hidden></div>
  <div id="crewFeed" hidden aria-live="polite"><div class="cf-head"><span><i></i>CREW LIVE</span><button type="button" id="cfMin" aria-label="Feed einklappen">–</button></div><div class="cf-list" id="cfList"></div></div>`);
  $("cfMin").addEventListener("click", () => { const f = $("crewFeed"); f.classList.toggle("min"); $("cfMin").textContent = f.classList.contains("min") ? "+" : "–"; try { localStorage.setItem("welten-cfmin", f.classList.contains("min") ? "1" : "0"); } catch (e) {} });
  try { if (localStorage.getItem("welten-cfmin") === "1") { $("crewFeed").classList.add("min"); $("cfMin").textContent = "+"; } } catch (e) {}
  const tg = document.querySelector(".toggles");
  if (tg) { tg.insertAdjacentHTML("afterbegin", `<button type="button" class="chip mmchip" id="olChip"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="5.5" cy="6" r="2.4" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="11" cy="6.5" r="2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M1.5 13.5c.6-2.6 2.2-3.8 4-3.8s3.4 1.2 4 3.8M9.6 10.2c.5-.3 1-.4 1.6-.4 1.6 0 2.8 1 3.3 3.2" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>Online</button>`); $("olChip").addEventListener("click", openOnline); }
  const row = document.querySelector("#intro .mm-row");
  if (row) { row.insertAdjacentHTML("beforeend", `<button type="button" id="mmOnline"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="6" r="2.6" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M3 14c.8-3 2.8-4.3 5-4.3s4.2 1.3 5 4.3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>Online</button>`);
    $("mmOnline").addEventListener("click", () => { const el = $("intro"); if (el.classList.contains("ingame")) closeMainMenu(); else $("introBtn").click(); setTimeout(openOnline, 700); }); }
  $("olClose").addEventListener("click", closeOnline);
  $("olTabs").addEventListener("click", e => { const b = e.target.closest("button[data-t]"); if (b) { OL.tab = b.dataset.t; olMsg(""); olRender(); } });
  $("online").addEventListener("click", olClick);
  window.addEventListener("keydown", e => { if (mmOpen("online") && e.key === "Escape") { closeOnline(); e.preventDefault(); e.stopImmediatePropagation(); } }, true);
  setTimeout(() => olInit(), 2500);
})();
function openOnline() { if (!machineIdle() && !OL.vs) return; $("online").hidden = false; try { sfx.click(); } catch (e) {} olRender(); olInit(); }
function closeOnline() { $("online").hidden = true; try { sfx.click(); } catch (e) {} render(); mmResume(); }
function olItem(id, p, extra, me) {
  const w = (p && p.w && p.w[WORLD_ID]) || {};
  return `<div class="ol-item${me ? " me" : ""}"><span class="ol-dot${me || olOnline(p) ? " on" : ""}"></span><span><b>${escapeHTML((p && p.n) || "?")}${me ? " (du)" : ""}</b><small>Rang ${w.l || "–"} · Rekord ${fmtN(w.p || 0)}</small></span><span class="ol-acts">${extra || ""}</span></div>`;
}
function olRender() {
  document.querySelectorAll("#olTabs button").forEach(b => b.setAttribute("aria-pressed", String(b.dataset.t === OL.tab)));
  const P = $("olPane");
  if (!OL.ready) { P.innerHTML = `<p class="ol-info">${OL.err || "Verbinde mit dem Online-Dienst …"}</p>${OL.err ? `<button type="button" class="ol-small" data-a="retry">Nochmal versuchen</button>` : ""}`; return; }
  const ids = Object.keys(OL.friends);
  if (OL.tab === "friends") {
    const gifts = Object.entries(OL.gifts).filter(([, g]) => g && !g.c);
    P.innerHTML = `<div class="ol-me"><span>Dein Freundescode<br><span class="ol-code">${OL.code}</span></span><button type="button" class="ol-small" data-a="copy">Kopieren</button></div>
      ${gifts.length ? `<div class="ol-gifts">${gifts.map(([from, g]) => `<div class="ol-gift"><span>🎁 Geschenk von <b>${escapeHTML((OL.people[from] || {}).n || "einem Freund")}</b>: ${fmtN(g.a)} Credits</span><button type="button" class="ol-small" data-a="claim" data-id="${from}">Annehmen</button></div>`).join("")}</div>` : ""}
      <div class="ol-row"><input id="olAdd" maxlength="6" placeholder="Code eines Freundes" aria-label="Code eines Freundes"><button type="button" class="ol-small" data-a="add">Hinzufügen</button></div>
      <div class="ol-list">${ids.length ? ids.map(id => { const last = OL.sent[id] || 0, can = Date.now() - last > GIFT_MS, inCrew = !!OL.crewM[id], full = Object.keys(OL.crewM).length >= CREW_MAX;
        return olItem(id, OL.people[id], `<button type="button" data-a="gift" data-id="${id}" ${can ? "" : "disabled"} title="Alle 24 Stunden">${can ? "🎁 Schenken" : "🎁 " + olLeft(last)}</button><button type="button" data-a="invite" data-id="${id}" ${inCrew || full ? "disabled" : ""} class="${inCrew ? "hot" : ""}">${inCrew ? "In deiner Crew" : "In Crew einladen"}</button><button type="button" data-a="rm" data-id="${id}" aria-label="Entfernen">×</button>`); }).join("")
        : `<p class="ol-info">Noch keine Freunde. Gib deinen Code weiter oder trag den Code eines Freundes ein.</p>`}</div>`;
    olGiftTimes();
  } else if (OL.tab === "board") {
    P.innerHTML = `<div class="ol-row"><button type="button" class="ol-small" data-a="bf" ${OL.board === "friends" ? 'style="border-color:var(--gold)"' : ""}>Freunde</button><button type="button" class="ol-small" data-a="bg" ${OL.board === "global" ? 'style="border-color:var(--gold)"' : ""}>Weltweit</button><button type="button" class="ol-small" data-a="bd" ${OL.board === "day" ? 'style="border-color:var(--gold)"' : ""}>Höchster Gewinn heute</button></div><p class="ol-info">${OL.board === "day" ? "Der größte Einzelgewinn des Tages, weltweit über alle Welten." : "Rangliste dieser Welt nach Rekord."}</p><div class="ol-list" id="olBoard">Lade …</div>`;
    olBoard();
  } else if (OL.tab === "vs") {
    const v = OL.vs;
    P.innerHTML = `<p class="ol-info">Du gegen einen anderen Spieler in dieser Welt: 5 Minuten Zeit. Gewertet wird, wie viel du im Verhältnis zu deinem Einsatz gewinnst. Wer vorne liegt, bekommt eine Siegprämie von 25× Einsatz, für die Teilnahme gibt es 5× Einsatz.</p>
      ${!v ? `<button type="button" class="bbtn" data-a="vsfind">Gegner suchen</button>` : v.state === "wait" ? `<p class="ol-info">Suche Gegner … Sobald jemand in dieser Welt sucht, geht es los.</p><button type="button" class="ol-small" data-a="vscancel">Abbrechen</button>`
        : `<div class="ol-big">${fmtN(v.my)} <span>gegen</span> ${fmtN(v.op)}</div><p class="ol-info">Gegner: ${escapeHTML(v.opName || "?")}. Schließ dieses Fenster und dreh! Oben läuft die Zeit.</p>`}`;
  } else if (OL.tab === "coop") {
    const ids2 = Object.keys(OL.crewM), n = ids2.length, inv = Object.entries(OL.crewInv);
    P.innerHTML = `<p class="ol-info">Grindet zu zweit, dritt oder viert: Jeder bekommt <b>20 %</b> von dem, was die anderen gewinnen, obendrauf. Je größer die Crew, desto teurer die Bauteile: 2 Spieler +25 %, 3 Spieler +50 %, 4 Spieler +75 %. Einladen kannst du Freunde unter „Freunde“.</p>
      ${inv.length ? `<div class="ol-gifts">${inv.map(([cid, v]) => `<div class="ol-gift"><span>👥 <b>${escapeHTML(v.n || "Ein Freund")}</b> lädt dich in seine Crew ein</span><span class="ol-acts"><button type="button" data-a="accept" data-id="${cid}">Beitreten</button><button type="button" data-a="decline" data-id="${cid}">Ablehnen</button></span></div>`).join("")}</div>` : ""}
      ${OL.crew ? `<p class="ol-info"><b>Deine Crew (${n}/${CREW_MAX})</b> · Bauteile kosten gerade ${Math.round((coopCostMul() - 1) * 100)} % mehr.</p><div class="ol-list">${ids2.map(id => olItem(id, id === OL.uid ? { n: olName(), w: { [WORLD_ID]: { l: state.level, p: state.peak } } } : OL.people[id] || { n: OL.crewM[id] }, "", id === OL.uid)).join("")}</div><div class="ol-row"><button type="button" class="ol-small" data-a="leave">Crew verlassen</button></div>`
        : `<p class="ol-info">Du bist in keiner Crew. Lade unter „Freunde“ jemanden ein.</p>`}
      <h3 style="margin:14px 0 6px;font-size:15px">Live-Ticker deiner Freunde</h3><div class="ol-list">${OL.ticker.length ? OL.ticker.slice(0, 12).map(t => `<div class="ol-item"><span class="ol-dot on"></span><span><b>${escapeHTML(t.n)}</b><small>${escapeHTML(t.wn || "")} · ${new Date(t.t).toLocaleTimeString("de-DE", { hour: "2-digit", minute: "2-digit" })}</small></span><span class="ol-acts"><b>+${fmtN(t.a)}</b></span></div>`).join("") : `<p class="ol-info">Noch nichts los. Große Gewinne deiner Freunde erscheinen hier sofort.</p>`}</div>`;
  } else {
    P.innerHTML = `<p class="ol-info">Sichere deinen Fortschritt aller vier Welten in der Cloud, ganz ohne E-Mail, Name oder Passwort. Du bekommst einen <b>Wiederherstellungscode</b>. Mit ihm holst du deinen Spielstand auf jedes Gerät. Wer den Code kennt, kann den Spielstand laden, also gib ihn nicht weiter.</p>
      ${OL.vault ? `<div class="ol-me"><span>Dein Wiederherstellungscode<br><span class="ol-code" style="font-size:16px">${olFmtVault(OL.vault)}</span></span><button type="button" class="ol-small" data-a="vcopy">Kopieren</button></div><p class="ol-info">Automatische Sicherung alle 5 Minuten. Zuletzt: ${OL.vaultAt ? new Date(OL.vaultAt).toLocaleTimeString("de-DE", { hour: "2-digit", minute: "2-digit" }) : "noch nicht"}.</p><button type="button" class="bbtn" data-a="vsave">Jetzt sichern</button>`
        : `<button type="button" class="bbtn" data-a="vsave">Code erstellen und sichern</button>`}
      <h3 style="margin:16px 0 6px;font-size:15px">Spielstand von einem anderen Gerät laden</h3>
      <div class="ol-row"><input id="olVault" maxlength="19" placeholder="XXXX-XXXX-XXXX-XXXX" aria-label="Wiederherstellungscode"><button type="button" class="ol-small" data-a="vload">Laden</button></div>`;
  }
}
function olLeft(t) { const ms = GIFT_MS - (Date.now() - t), h = Math.floor(ms / 36e5), m = Math.ceil(ms % 36e5 / 6e4); return h ? `${h} h` : `${m} min`; }
async function olGiftTimes() {
  const ids = Object.keys(OL.friends).filter(id => !(id in OL.sent)); if (!ids.length) return;
  await Promise.all(ids.map(async id => { try { const g = (await OL.db.ref(`gifts/${id}/${OL.uid}/t`).get()).val(); OL.sent[id] = g || 0; } catch (e) { OL.sent[id] = 0; } }));
  if (mmOpen("online") && OL.tab === "friends") olRender();
}
async function olBoard() {
  let rows = [];
  try {
    if (OL.board === "day") { const s = await OL.db.ref("daily/" + olDay()).orderByChild("a").limitToLast(30).get(); s.forEach(c => { rows.push([c.key, c.val()]); });
      rows.reverse(); $("olBoard").innerHTML = rows.map(([id, v], i) => `<div class="ol-item${id === OL.uid ? " me" : ""}"><span class="ol-rank">${i + 1}.</span><span><b>${escapeHTML(v.n || "?")}${id === OL.uid ? " (du)" : ""}</b><small>${escapeHTML(v.wn || "")}</small></span><span class="ol-acts"><b>+${fmtN(v.a)}</b></span></div>`).join("") || `<p class="ol-info">Heute hat noch niemand gewonnen. Sei der Erste!</p>`; return; }
    if (OL.board === "global") { const s = await OL.db.ref("players").orderByChild(`w/${WORLD_ID}/p`).limitToLast(30).get(); s.forEach(c => { rows.push([c.key, c.val()]); }); }
    else { rows = [[OL.uid, { n: olName(), w: { [WORLD_ID]: { l: state.level, p: state.peak } } }], ...Object.keys(OL.friends).map(id => [id, OL.people[id] || {}])]; }
  } catch (e) { $("olBoard").textContent = "Konnte die Rangliste nicht laden."; return; }
  rows.sort((a, b) => ((b[1].w || {})[WORLD_ID] || {}).p - ((a[1].w || {})[WORLD_ID] || {}).p || 0);
  $("olBoard").innerHTML = rows.map(([id, p], i) => olItem(id, p, `<span class="ol-rank">${i + 1}.</span>`, id === OL.uid)).join("") || `<p class="ol-info">Noch keine Einträge.</p>`;
}
async function olClick(e) {
  const b = e.target.closest("[data-a]"); if (!b) return;
  const a = b.dataset.a, id = b.dataset.id;
  try {
    if (a === "retry") { OL.err = ""; olRender(); await olInit(); }
    else if (a === "copy") { try { await navigator.clipboard.writeText(OL.code); olMsg("Code kopiert.", true); } catch (er) { olMsg("Kopieren nicht erlaubt. Schreib den Code ab.", false); } }
    else if (a === "add") {
      const c = ($("olAdd").value || "").trim().toUpperCase(); if (c.length !== 6) { olMsg("Ein Code hat 6 Zeichen.", false); return; }
      if (c === OL.code) { olMsg("Das ist dein eigener Code.", false); return; }
      const uid = (await OL.db.ref("codes/" + c).get()).val(); if (!uid) { olMsg("Diesen Code gibt es nicht.", false); return; }
      await OL.db.ref().update({ [`friends/${OL.uid}/${uid}`]: true, [`friends/${uid}/${OL.uid}`]: true });
      olMsg("Freund hinzugefügt!", true);
    }
    else if (a === "rm") { await OL.db.ref().update({ [`friends/${OL.uid}/${id}`]: null, [`friends/${id}/${OL.uid}`]: null }); olMsg("Entfernt.", true); }
    else if (a === "gift") {
      const amt = Math.min(5000, Math.max(100, bet() * 20));
      await OL.db.ref(`gifts/${id}/${OL.uid}`).set({ t: firebase.database.ServerValue.TIMESTAMP, a: amt, c: false });
      OL.sent[id] = Date.now(); olMsg(`Geschenk über ${fmtN(amt)} Credits verschickt.`, true); olRender(); try { sfx.upgrade(); } catch (er) {}
    }
    else if (a === "claim") {
      const g = OL.gifts[id]; if (!g || g.c) return;
      await OL.db.ref(`gifts/${OL.uid}/${id}/c`).set(true);
      state.credits += g.a; render(); saveGame(); olMsg(`+${fmtN(g.a)} Credits!`, true); try { sfx.upgrade(); } catch (er) {}
      radio(`Funk: Geschenk von ${(OL.people[id] || {}).n || "einem Freund"} angenommen. +${fmtN(g.a)} Credits.`, true);
    }
    else if (a === "bf" || a === "bg" || a === "bd") { OL.board = a === "bf" ? "friends" : a === "bg" ? "global" : "day"; olRender(); }
    else if (a === "invite") await crewInvite(id);
    else if (a === "accept") await crewAccept(id);
    else if (a === "decline") { await OL.db.ref(`crewInv/${OL.uid}/${id}`).remove(); }
    else if (a === "leave") await crewLeave();
    else if (a === "vsave") { await vaultSave(true); }
    else if (a === "vcopy") { try { await navigator.clipboard.writeText(olFmtVault(OL.vault)); olMsg("Code kopiert. Bewahr ihn gut auf.", true); } catch (er) { olMsg("Kopieren nicht erlaubt. Schreib den Code ab.", false); } }
    else if (a === "vload") { if (!OL.confirm) { OL.confirm = true; olMsg("Achtung: Dein Spielstand auf diesem Gerät wird ersetzt. Zum Bestätigen nochmal auf „Laden“ tippen.", false); return; } OL.confirm = false; await vaultLoad(); }
    else if (a === "vsfind") await vsFind();
    else if (a === "vscancel") vsCancel();
  } catch (er) { olMsg("Das hat nicht geklappt. Bitte nochmal versuchen.", false); try { console.warn("Online:", er); } catch (x) {} }
}

/* --- Koop-Crew (bis 4 Spieler) --- */
function coopCostMul() { try { const n = OL.crew ? Object.keys(OL.crewM).length : 0; return n >= 2 ? 1 + .25 * (n - 1) : 1; } catch (e) { return 1; } }   // try: wird schon vor diesem Block aufgerufen (stepCost)
function olSetCrew(cid) { if (OL.logRef) { OL.logRef.off(); OL.logRef = null; } $("crewFeed").hidden = !cid; if (!cid) $("cfList").innerHTML = ""; OL.crew = cid; try { cid ? localStorage.setItem("welten-crew", cid) : localStorage.removeItem("welten-crew"); } catch (e) {} if (OL.crewRef) { OL.crewRef.off(); OL.feedRef.off(); OL.crewRef = OL.feedRef = null; } OL.crewM = {}; if (cid) olCrewListen(); render(); }
function olCrewListen() {
  OL.crewRef = OL.db.ref(`crews/${OL.crew}/m`);
  OL.crewRef.on("value", s => { OL.crewM = s.val() || {}; if (OL.crew && !OL.crewM[OL.uid]) { olSetCrew(null); } Object.keys(OL.crewM).forEach(id => { if (id !== OL.uid && !OL.people[id]) OL.db.ref("players/" + id).get().then(x => { OL.people[id] = x.val() || { n: OL.crewM[id] }; }).catch(() => {}); }); render(); if (mmOpen("online")) olRender(); });
  $("crewFeed").hidden = false;
  const since = Date.now() - 60000;
  OL.logRef = OL.db.ref(`crews/${OL.crew}/log`).limitToLast(6);
  OL.logRef.on("child_added", s => { const v = s.val(); if (v && (v.t || 0) > since) cfAdd(v); });
  OL.feedRef = OL.db.ref(`crews/${OL.crew}/feed/${OL.uid}`);
  OL.feedRef.on("child_added", s => { const v = s.val(); s.ref.remove().catch(() => {}); if (!v || !v.a) return; state.credits += v.a; render(); toast(`Crew-Bonus +${fmtN(v.a)} (${v.n || ""})`, "#6fdc8c"); });
}
async function crewInvite(id) {
  if (!OL.crew) { const cid = OL.db.ref("crews").push().key; await OL.db.ref(`crews/${cid}/m/${OL.uid}`).set(olName()); olSetCrew(cid); }
  if (Object.keys(OL.crewM).length >= CREW_MAX) { olMsg("Die Crew ist voll (4 Spieler).", false); return; }
  await OL.db.ref(`crewInv/${id}/${OL.crew}`).set({ n: olName(), t: firebase.database.ServerValue.TIMESTAMP });
  olMsg(`Einladung an ${(OL.people[id] || {}).n || "deinen Freund"} verschickt.`, true);
}
async function crewAccept(cid) {
  const m = (await OL.db.ref(`crews/${cid}/m`).get()).val() || {};
  await OL.db.ref(`crewInv/${OL.uid}/${cid}`).remove();
  if (!Object.keys(m).length) { olMsg("Diese Crew gibt es nicht mehr.", false); return; }
  if (Object.keys(m).length >= CREW_MAX) { olMsg("Die Crew ist schon voll.", false); return; }
  if (OL.crew && OL.crew !== cid) await crewLeave(true);
  await OL.db.ref(`crews/${cid}/m/${OL.uid}`).set(olName()); olSetCrew(cid);
  olMsg("Du bist der Crew beigetreten!", true); radio("Funk: Willkommen in der Crew! Ihr teilt jetzt 20 % eurer Gewinne.", true);
}
async function crewLeave(quiet) {
  if (!OL.crew) return; const cid = OL.crew;
  await OL.db.ref(`crews/${cid}/m/${OL.uid}`).remove().catch(() => {}); olSetCrew(null);
  if (!quiet) { olMsg("Crew verlassen. Bauteile kosten wieder normal.", true); olRender(); }
}
/* --- Crew-Feed (wie ein Kill-Feed): letzte Gewinne der Crew, live --- */
const CF_COL = ["#4fe3ff", "#ffb36b", "#a7c060", "#ff7ad9", "#7ee0c8", "#b9a4ff"];
function cfColor(uid) { let h = 0; for (const c of uid || "") h = (h * 31 + c.charCodeAt(0)) >>> 0; return CF_COL[h % CF_COL.length]; }
function cfAdd(v) {
  const list = $("cfList"); if (!list) return;
  const me = v.u === OL.uid, big = (v.x || 0) >= 25;
  const ic = big ? "💥" : (v.x || 0) >= 10 ? "🔥" : "💰";
  list.insertAdjacentHTML("afterbegin", `<div class="cf-row${me ? " me" : ""}${big ? " big" : ""}" style="--pc:${cfColor(v.u)}"><span class="cf-ic">${ic}</span><b>${escapeHTML(me ? "Du" : v.n || "?")}</b><small>${escapeHTML(v.wn || "")}${v.x ? " · " + v.x + "×" : ""}</small><span class="cf-amt">+${fmtN(v.a)}</span></div>`);
  const rows = [...list.children];
  rows.forEach((r, i) => { r.classList.toggle("old", i >= 3); if (i >= 5) r.remove(); });
  const row = list.firstElementChild;
  setTimeout(() => { row.classList.add("old"); }, 8000);
  setTimeout(() => { row.classList.add("gone"); setTimeout(() => row.remove(), 650); }, 20000);
}
/* --- Live-Ticker: große Gewinne der Freunde --- */
function olTickerListen() {
  Object.keys(OL.friends).forEach(id => { if (OL.live[id]) return;
    let first = true;
    OL.live[id] = OL.db.ref(`players/${id}/live`); OL.live[id].on("value", s => { const v = s.val(); if (first) { first = false; return; } if (!v || !v.a) return;
      const t = { n: (OL.people[id] || {}).n || "Freund", a: v.a, wn: v.wn, t: Date.now() }; OL.ticker.unshift(t); OL.ticker = OL.ticker.slice(0, 30);
      toast(`📈 ${t.n}: +${fmtN(t.a)} in ${t.wn}`, "#7ee0c8"); if (mmOpen("online") && OL.tab === "coop") olRender(); }); });
}
/* --- Spielstand in der Cloud (Wiederherstellungscode, keine persönlichen Daten) --- */
const olFmtVault = c => (c || "").match(/.{1,4}/g).join("-");
function olSaves() { const s = {}; [...WORLDS.map(w => w.key), "welten-lang"].forEach(k => { try { const v = localStorage.getItem(k); if (v != null) s[k.replace(/[.#$\[\]\/]/g, "_")] = v; } catch (e) {} }); return s; }
async function vaultSave(manual) {
  if (!OL.db) return;
  if (!OL.vault) { const A = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789", r = crypto.getRandomValues(new Uint32Array(16)); OL.vault = Array.from(r, x => A[x % A.length]).join(""); try { localStorage.setItem("welten-vault", OL.vault); } catch (e) {} }
  try { flushSave && flushSave(); } catch (e) {}
  await OL.db.ref("vault/" + OL.vault).set({ s: olSaves(), f: Object.keys(OL.friends), t: firebase.database.ServerValue.TIMESTAMP });
  OL.vaultAt = Date.now();
  if (manual) { olMsg("Gesichert! Notier dir den Code.", true); olRender(); }
}
async function vaultLoad() {
  const code = ($("olVault").value || "").toUpperCase().replace(/[^A-Z0-9]/g, "");
  if (code.length !== 16) { olMsg("Der Code hat 16 Zeichen.", false); return; }
  const v = (await OL.db.ref("vault/" + code).get()).val();
  if (!v || !v.s) { olMsg("Zu diesem Code gibt es keinen Spielstand.", false); return; }
  ready = false;   // verhindert, dass der alte Spielstand beim Neuladen zurückgeschrieben wird
  Object.entries(v.s).forEach(([k, val]) => { try { localStorage.setItem(k, val); } catch (e) {} });
  try { localStorage.setItem("welten-vault", code); } catch (e) {}
  const up = {}; (v.f || []).forEach(f => { if (f !== OL.uid) { up[`friends/${OL.uid}/${f}`] = true; up[`friends/${f}/${OL.uid}`] = true; } });
  if (Object.keys(up).length) await OL.db.ref().update(up).catch(() => {});
  olMsg("Spielstand geladen. Das Spiel startet neu …", true);
  setTimeout(() => location.reload(), 900);
}
let olWon = null, olN = 0, olBest = null;
function olTick() {
  if (!OL.ready) return;
  olN++;
  const won = sess.won; if (olWon === null) { olWon = won; olBest = sess.best; return; }
  const d = won - olWon; olWon = won;
  const wn = (WORLDS.find(w => w.id === WORLD_ID) || {}).name || "";
  if (d > 0 && OL.crew && d >= bet() * 2) OL.db.ref(`crews/${OL.crew}/log`).push({ u: OL.uid, n: olName(), a: d, x: Math.round(d / Math.max(1, bet())), wn, t: firebase.database.ServerValue.TIMESTAMP }).catch(() => {});
  if (d > 0 && OL.crew) { const share = Math.floor(d * COOP_SHARE); if (share > 0) Object.keys(OL.crewM).forEach(id => { if (id !== OL.uid && olOnline(OL.people[id])) OL.db.ref(`crews/${OL.crew}/feed/${id}`).push({ a: share, n: olName() }).catch(() => {}); }); }
  if (d >= bet() * 10) OL.db.ref(`players/${OL.uid}/live`).set({ a: d, wn, t: firebase.database.ServerValue.TIMESTAMP }).catch(() => {});
  if (sess.best > OL.dayBest && sess.best > olBest) { OL.dayBest = sess.best; try { localStorage.setItem("welten-daybest", JSON.stringify({ d: olDay(), a: OL.dayBest })); } catch (e) {}
    OL.db.ref(`daily/${olDay()}/${OL.uid}`).set({ n: olName(), a: OL.dayBest, wn }).catch(() => {}); }
  olBest = Math.max(olBest, sess.best);
  if (OL.vs && OL.vs.state === "run" && d > 0) { OL.vs.my += Math.round(d / Math.max(1, bet()) * 10); OL.db.ref(`matches/${OL.vs.id}/s/${OL.vs.side}`).set(OL.vs.my).catch(() => {}); }
  if (olN % 15 === 0 && OL.crew) Object.keys(OL.crewM).forEach(id => { if (id !== OL.uid) OL.db.ref("players/" + id + "/on").get().then(s => { OL.people[id] = { ...(OL.people[id] || {}), on: s.val() }; }).catch(() => {}); });
  if (OL.vault && olN % Math.round(VAULT_MS / 2000) === 0) vaultSave(false).catch(() => {});
}

/* --- VS-Duell: 5 Minuten, Punkte = Gewinne im Verhältnis zum Einsatz --- */
async function vsFind() {
  const q = OL.db.ref(`queue/${WORLD_ID}`), now = Date.now();
  const s = await q.get(); let found = null;
  s.forEach(c => { const v = c.val(); if (!found && c.key !== OL.uid && v && !v.m && now - (v.t || 0) < 90000) found = c.key; });
  if (found) {
    const id = OL.db.ref("matches").push().key;
    const r = await q.child(found).transaction(v => v === null ? null : !v.m ? { ...v, m: id } : undefined);   // null: Wert noch nicht geladen, Firebase versucht es erneut
    if (r.committed && r.snapshot.val() && r.snapshot.val().m === id) { const op = r.snapshot.val();
      await OL.db.ref("matches/" + id).set({ a: found, b: OL.uid, an: op.n || "?", bn: olName(), start: firebase.database.ServerValue.TIMESTAMP, s: { a: 0, b: 0 } });
      vsJoin(id, "b"); return; }
  }
  OL.vs = { state: "wait" }; olRender();
  OL.queueRef = q.child(OL.uid); await OL.queueRef.set({ n: olName(), t: firebase.database.ServerValue.TIMESTAMP });
  OL.queueRef.onDisconnect().remove();
  OL.queueRef.on("value", c => { const v = c.val(); if (v && v.m) { OL.queueRef.off(); OL.queueRef.remove().catch(() => {}); OL.queueRef = null; vsJoin(v.m, "a"); } });
}
function vsCancel() { if (OL.queueRef) { OL.queueRef.off(); OL.queueRef.remove().catch(() => {}); OL.queueRef = null; } OL.vs = null; olRender(); }
function vsJoin(id, side) {
  OL.vs = { state: "run", id, side, my: 0, op: 0, opName: "", start: Date.now() };
  OL.db.ref("matches/" + id).on("value", s => { const m = s.val(); if (!m || !OL.vs) return;
    OL.vs.opName = side === "a" ? m.bn : m.an; OL.vs.op = (m.s || {})[side === "a" ? "b" : "a"] || 0; if (m.start) OL.vs.start = m.start; vsBar(); if (mmOpen("online") && OL.tab === "vs") olRender(); });
  try { sfx.upgrade(); } catch (e) {} radio("Funk: VS-Duell gestartet! 5 Minuten, gewinne so viel du kannst.", true);
  OL.vsTimer = setInterval(vsBar, 1000); olRender();
}
function vsBar() {
  const v = OL.vs, el = $("vsBar"); if (!v || v.state !== "run") { el.hidden = true; return; }
  const left = Math.max(0, VS_MS - (Date.now() - v.start)), mm = Math.floor(left / 60000), ss = String(Math.floor(left / 1000) % 60).padStart(2, "0");
  el.hidden = false;
  el.innerHTML = `<span class="t">VS ${mm}:${ss}</span><span class="${v.my >= v.op ? "lead" : ""}">Du ${fmtN(v.my)}</span><span>·</span><span class="${v.op > v.my ? "lead" : ""}">${escapeHTML(v.opName || "Gegner")} ${fmtN(v.op)}</span>`;
  if (!left) vsEnd();
}
function vsEnd() {
  const v = OL.vs; if (!v || v.state !== "run") return; v.state = "done"; clearInterval(OL.vsTimer);
  OL.db.ref("matches/" + v.id).off();
  const won = v.my > v.op, prize = bet() * (won ? 25 : 5);
  state.credits += prize; render(); saveGame();
  $("vsBar").hidden = true;
  radio(won ? `Funk: VS-Duell gewonnen, ${fmtN(v.my)} zu ${fmtN(v.op)}! Siegprämie +${fmtN(prize)} Credits.` : `Funk: VS-Duell vorbei, ${fmtN(v.my)} zu ${fmtN(v.op)}. Für die Teilnahme +${fmtN(prize)} Credits.`, true);
  try { won ? sfx.upgrade() : sfx.click(); } catch (e) {}
  OL.vs = null; if (mmOpen("online")) olRender();
}
'''

# Sicherheitsregeln für die Realtime Database (in der Firebase-Konsole unter Regeln einfügen)
RULES = r'''{
  "rules": {
    "players": {
      ".read": "auth != null",
      ".indexOn": ["w/sternenwrack/p", "w/treibgut/p", "w/eisenfront/p", "w/neustadt/p"],
      "$uid": { ".write": "auth != null && auth.uid === $uid" }
    },
    "codes": {
      "$code": { ".read": "auth != null", ".write": "auth != null && !data.exists() && newData.val() === auth.uid" }
    },
    "friends": {
      "$uid": {
        ".read": "auth != null && auth.uid === $uid",
        "$f": { ".write": "auth != null && (auth.uid === $uid || auth.uid === $f)" }
      }
    },
    "gifts": {
      "$to": {
        ".read": "auth != null && auth.uid === $to",
        "$from": {
          ".read": "auth != null && auth.uid === $from",
          ".write": "auth != null && auth.uid === $from && $from !== $to && newData.child('t').val() === now && (!data.exists() || data.child('t').val() + 86400000 <= now)",
          ".validate": "newData.child('a').isNumber() && newData.child('a').val() > 0 && newData.child('a').val() <= 5000",
          "c": { ".write": "auth != null && auth.uid === $to && newData.val() === true" }
        }
      }
    },
    "queue": { "$world": { ".read": "auth != null", "$uid": { ".write": "auth != null" } } },
    "matches": { "$id": { ".read": "auth != null", ".write": "auth != null" } },
    "crews": { "$cid": { ".read": "auth != null", ".write": "auth != null && (data.child('m').child(auth.uid).exists() || newData.child('m').child(auth.uid).exists())" } },
    "crewInv": { "$to": { ".read": "auth != null && auth.uid === $to", "$cid": { ".write": "auth != null" } } },
    "daily": { "$day": { ".read": "auth != null", ".indexOn": ["a"], "$uid": { ".write": "auth != null && auth.uid === $uid", ".validate": "newData.child('a').isNumber()" } } },
    "vault": { "$k": { ".read": "auth != null", ".write": "auth != null && $k.length >= 16" } }
  }
}'''
