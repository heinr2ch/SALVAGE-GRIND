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
.mmchip .ol-badge { display: inline-block; min-width: 16px; height: 16px; border-radius: 8px; background: #ff4b6a; color: #fff; font: 800 10px/16px system-ui; text-align: center; margin-left: 4px; }
'''

ONLINE_JS = r'''
/* ---------- Online: Freunde, Rangliste, Geschenke, VS, Koop (Firebase) ---------- */
const FB_CFG = { apiKey: "AIzaSyBcnwWCg5qhD-g8DWnsNh-teUZihc4CKtM", authDomain: "salvage-grind.firebaseapp.com", databaseURL: "https://salvage-grind-default-rtdb.europe-west1.firebasedatabase.app", projectId: "salvage-grind", storageBucket: "salvage-grind.firebasestorage.app", messagingSenderId: "169044714781", appId: "1:169044714781:web:38796d21b781bed839adf4" };
const FB_VER = "10.14.1", GIFT_MS = 864e5, VS_MS = 300000, COOP_SHARE = .25, COOP_COST = 1.3;
const OL = { db: null, uid: null, ready: false, err: "", code: "", friends: {}, people: {}, gifts: {}, tab: "friends", board: "friends", sent: {}, vs: null, queueRef: null, coop: null };
try { OL.coop = localStorage.getItem("welten-coop") || null; } catch (e) {}
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
      OL.db.ref("friends/" + OL.uid).on("value", s => { OL.friends = s.val() || {}; olLoadPeople(); });
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
  const n = Object.values(OL.gifts).filter(g => g && !g.c).length;
  const b = $("olChip"); if (!b) return;
  b.querySelector(".ol-badge") && b.querySelector(".ol-badge").remove();
  if (n) b.insertAdjacentHTML("beforeend", `<span class="ol-badge">${n}</span>`);
}
function olMsg(t, ok) { const el = $("olMsg"); if (!el) return; el.textContent = t || ""; el.className = "ol-msg" + (t ? (ok ? " ok" : " err") : ""); }

/* --- Dialog --- */
(function setupOnline() {
  document.body.insertAdjacentHTML("beforeend", `<div class="bonus" id="online" hidden role="dialog" aria-modal="true" aria-labelledby="olTitle" style="z-index:260">
  <div class="bonus-card"><h2 id="olTitle" style="margin:0 0 4px">Online</h2>
  <div class="ol-tabs" id="olTabs"><button type="button" data-t="friends">Freunde</button><button type="button" data-t="board">Rangliste</button><button type="button" data-t="vs">VS-Duell</button><button type="button" data-t="coop">Koop</button></div>
  <p class="ol-msg" id="olMsg" aria-live="polite"></p>
  <div class="ol-pane" id="olPane"></div>
  <div class="ar-row"><span></span><button type="button" class="bbtn ghost" id="olClose">Schließen</button></div></div></div>
  <div id="vsBar" hidden></div>`);
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
      <div class="ol-list">${ids.length ? ids.map(id => { const last = OL.sent[id] || 0, can = Date.now() - last > GIFT_MS, coop = OL.coop === id;
        return olItem(id, OL.people[id], `<button type="button" data-a="gift" data-id="${id}" ${can ? "" : "disabled"} title="Alle 24 Stunden">${can ? "🎁 Schenken" : "🎁 " + olLeft(last)}</button><button type="button" data-a="coop" data-id="${id}" class="${coop ? "hot" : ""}">${coop ? "Koop beenden" : "Koop"}</button><button type="button" data-a="rm" data-id="${id}" aria-label="Entfernen">×</button>`); }).join("")
        : `<p class="ol-info">Noch keine Freunde. Gib deinen Code weiter oder trag den Code eines Freundes ein.</p>`}</div>`;
    olGiftTimes();
  } else if (OL.tab === "board") {
    P.innerHTML = `<div class="ol-row"><button type="button" class="ol-small" data-a="bf" ${OL.board === "friends" ? 'style="border-color:var(--gold)"' : ""}>Freunde</button><button type="button" class="ol-small" data-a="bg" ${OL.board === "global" ? 'style="border-color:var(--gold)"' : ""}>Weltweit</button></div><p class="ol-info">Rangliste dieser Welt nach Rekord.</p><div class="ol-list" id="olBoard">Lade …</div>`;
    olBoard();
  } else if (OL.tab === "vs") {
    const v = OL.vs;
    P.innerHTML = `<p class="ol-info">Du gegen einen anderen Spieler in dieser Welt: 5 Minuten Zeit. Gewertet wird, wie viel du im Verhältnis zu deinem Einsatz gewinnst. Wer vorne liegt, bekommt eine Siegprämie von 25× Einsatz, für die Teilnahme gibt es 5× Einsatz.</p>
      ${!v ? `<button type="button" class="bbtn" data-a="vsfind">Gegner suchen</button>` : v.state === "wait" ? `<p class="ol-info">Suche Gegner … Sobald jemand in dieser Welt sucht, geht es los.</p><button type="button" class="ol-small" data-a="vscancel">Abbrechen</button>`
        : `<div class="ol-big">${fmtN(v.my)} <span>gegen</span> ${fmtN(v.op)}</div><p class="ol-info">Gegner: ${escapeHTML(v.opName || "?")}. Schließ dieses Fenster und dreh! Oben läuft die Zeit.</p>`}`;
  } else {
    const p = OL.coop && OL.people[OL.coop];
    P.innerHTML = `<p class="ol-info">Grindet zusammen: Solange ihr beide online seid, bekommt jeder <b>25 %</b> von dem, was der andere gewinnt, obendrauf. Dafür kosten Bauteile während der Koop-Zeit <b>30 % mehr</b>. Koop startest du bei einem Freund unter „Freunde“.</p>
      ${p ? `<div class="ol-list">${olItem(OL.coop, p, `<button type="button" data-a="coop" data-id="${OL.coop}" class="hot">Koop beenden</button>`)}</div><p class="ol-info">${olOnline(p) ? "Dein Partner ist online, der Bonus läuft." : "Dein Partner ist gerade nicht online. Der Bonus läuft, sobald ihr beide spielt."}</p>` : `<p class="ol-info">Gerade keine Koop-Crew aktiv.</p>`}`;
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
    else if (a === "rm") { await OL.db.ref().update({ [`friends/${OL.uid}/${id}`]: null, [`friends/${id}/${OL.uid}`]: null }); if (OL.coop === id) olSetCoop(null); olMsg("Entfernt.", true); }
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
    else if (a === "coop") { olSetCoop(OL.coop === id ? null : id); olRender(); }
    else if (a === "bf" || a === "bg") { OL.board = a === "bf" ? "friends" : "global"; olRender(); }
    else if (a === "vsfind") await vsFind();
    else if (a === "vscancel") vsCancel();
  } catch (er) { olMsg("Das hat nicht geklappt. Bitte nochmal versuchen.", false); try { console.warn("Online:", er); } catch (x) {} }
}

/* --- Koop-Crew --- */
const olCoopOn = () => !!OL.coop;
function coopCostMul() { try { return OL.coop ? COOP_COST : 1; } catch (e) { return 1; } }   // try: wird schon vor diesem Block aufgerufen   // Koop: Bauteile kosten mehr (wird in stepCost genutzt)
function olSetCoop(id) {
  OL.coop = id; try { id ? localStorage.setItem("welten-coop", id) : localStorage.removeItem("welten-coop"); } catch (e) {}
  if (OL.coopRef) { OL.coopRef.off(); OL.coopRef = null; }
  if (id && OL.db) olCoopListen();
  render();
  radio(id ? `Funk: Koop-Crew mit ${(OL.people[id] || {}).n || "deinem Freund"} gestartet. Bauteile kosten jetzt 30 % mehr.` : "Funk: Koop-Crew beendet. Bauteile kosten wieder normal.", true);
}
function olCoopListen() {
  const ref = OL.db.ref(`coop/${olPair(OL.uid, OL.coop)}/feed/${OL.uid}`);
  OL.coopRef = ref;
  ref.on("child_added", s => { const v = s.val(); s.ref.remove().catch(() => {}); if (!v || !v.a) return;
    state.credits += v.a; render(); toast(`Koop-Bonus +${fmtN(v.a)}`, "#6fdc8c"); });
}
let olWon = null;
function olTick() {
  if (!OL.ready) return;
  if (OL.coop && !OL.coopRef) olCoopListen();
  const won = sess.won; if (olWon === null) { olWon = won; return; }
  const d = won - olWon; olWon = won;
  if (d > 0 && OL.coop && olOnline(OL.people[OL.coop])) { const share = Math.floor(d * COOP_SHARE); if (share > 0) OL.db.ref(`coop/${olPair(OL.uid, OL.coop)}/feed/${OL.coop}`).push({ a: share, t: firebase.database.ServerValue.TIMESTAMP }).catch(() => {}); }
  if (OL.vs && OL.vs.state === "run" && d > 0) { OL.vs.my += Math.round(d / Math.max(1, bet()) * 10); OL.db.ref(`matches/${OL.vs.id}/s/${OL.vs.side}`).set(OL.vs.my).catch(() => {}); }
  if (Math.random() < .2 && OL.coop) OL.db.ref("players/" + OL.coop + "/on").get().then(s => { if (OL.people[OL.coop]) OL.people[OL.coop].on = s.val(); }).catch(() => {});
}

/* --- VS-Duell: 5 Minuten, Punkte = Gewinne im Verhältnis zum Einsatz --- */
async function vsFind() {
  const q = OL.db.ref(`queue/${WORLD_ID}`), now = Date.now();
  const s = await q.get(); let found = null;
  s.forEach(c => { const v = c.val(); if (!found && c.key !== OL.uid && v && !v.m && now - (v.t || 0) < 90000) found = c.key; });
  if (found) {
    const id = OL.db.ref("matches").push().key;
    const r = await q.child(found).transaction(v => v && !v.m ? { ...v, m: id } : undefined);
    if (r.committed) { const op = r.snapshot.val();
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
    "coop": { "$pair": { ".read": "auth != null && $pair.contains(auth.uid)", ".write": "auth != null && $pair.contains(auth.uid)" } }
  }
}'''
