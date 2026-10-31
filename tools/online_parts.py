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
#crewFeed { position: relative; width: 100%; max-width: 330px; justify-self: stretch; font: 700 12.5px var(--f-body, system-ui); border-radius: 12px; background: linear-gradient(180deg, rgba(0,0,0,.45), rgba(0,0,0,.25)); border: 1px solid rgba(255,255,255,.12); overflow: hidden; }
#crewFeed[hidden] { display: none; }
#crewFeed .cf-head { display: flex; justify-content: space-between; align-items: center; gap: 8px; padding: 5px 10px; font: 800 9.5px var(--f-mono, monospace); letter-spacing: .2em; color: #6fdc8c; background: rgba(255,255,255,.04); border-bottom: 1px solid rgba(255,255,255,.08); }
#crewFeed .cf-head button { background: none; border: 0; color: rgba(255,255,255,.7); cursor: pointer; font: 800 12px var(--f-mono, monospace); padding: 0 2px; }
#crewFeed .cf-head i { width: 7px; height: 7px; border-radius: 50%; background: #ff4b6a; box-shadow: 0 0 8px #ff4b6a; display: inline-block; margin-right: 6px; animation: cfLive 1.2s ease-in-out infinite; }
@keyframes cfLive { 50% { opacity: .3; } }
#crewFeed .cf-list { display: grid; gap: 3px; padding: 4px; height: 92px; overflow: hidden; align-content: start; }
#crewFeed.min .cf-list { display: none; }
#crewFeed .cf-empty { color: rgba(255,255,255,.45); font-weight: 600; font-size: 11.5px; padding: 6px; }
#crewFeed .cf-row { position: relative; display: flex; align-items: center; gap: 7px; padding: 5px 8px; border-radius: 7px; background: linear-gradient(90deg, color-mix(in srgb, var(--pc) 22%, rgba(0,0,0,.6)), rgba(0,0,0,.35)); border-left: 3px solid var(--pc); color: #fff; overflow: hidden;
  animation: cfIn .5s cubic-bezier(.2,1.5,.35,1); transition: opacity .6s, transform .6s, filter .6s; text-shadow: 0 1px 2px #000; }
#crewFeed .cf-row::after { content: ""; position: absolute; inset: 0; background: linear-gradient(100deg, transparent 30%, rgba(255,255,255,.35) 50%, transparent 70%); transform: translateX(-120%); animation: cfFlash .9s ease-out .1s; pointer-events: none; }
#crewFeed .cf-row.old { opacity: .5; filter: saturate(.5); }
#crewFeed .cf-row.gone { opacity: 0; transform: translateX(40px) scale(.95); }
#crewFeed .cf-row b { color: var(--pc); max-width: 92px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
#crewFeed .cf-row .cf-ic { font-size: 14px; }
#crewFeed .cf-row .cf-amt { margin-left: auto; color: #ffc94a; font-family: var(--f-mono, monospace); white-space: nowrap; }
#crewFeed .cf-row small { color: rgba(255,255,255,.65); font-weight: 600; font-size: 10.5px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
#crewFeed .cf-row.me { --pc: #ffffff; }
#crewFeed .cf-row.big .cf-amt { animation: cfAmt .6s cubic-bezier(.2,1.6,.4,1) 2; }
#crewFeed .cf-row.ft { border-left-width: 0; padding-left: 10px; background: linear-gradient(90deg, color-mix(in srgb, var(--fc) 45%, #000), color-mix(in srgb, var(--fc) 12%, #000)); box-shadow: inset 0 0 0 1.5px var(--fc), 0 0 14px color-mix(in srgb, var(--fc) 55%, transparent); animation: cfIn .5s cubic-bezier(.2,1.5,.35,1), cfPulse 1.2s ease-in-out 3; }
#crewFeed .cf-row.ft .cf-amt { color: var(--fc); font-family: var(--f-display, system-ui); letter-spacing: .08em; font-size: 11px; }
#crewFeed .cf-row.jp { animation: cfIn .5s cubic-bezier(.2,1.5,.35,1), cfShake .5s ease-in-out .5s 2, cfPulse 1.2s ease-in-out 3; }
#crewFeed.flash { animation: cfBox .7s ease-out; }
@keyframes cfIn { from { opacity: 0; transform: translateX(60px) scale(.8); filter: brightness(2.5); } 60% { transform: translateX(-4px) scale(1.03); } to { opacity: 1; transform: none; filter: none; } }
@keyframes cfFlash { to { transform: translateX(120%); } }
@keyframes cfAmt { 50% { transform: scale(1.35); text-shadow: 0 0 12px #ffc94a; } }
@keyframes cfPulse { 50% { box-shadow: inset 0 0 0 1.5px var(--fc), 0 0 26px var(--fc); } }
@keyframes cfShake { 25% { transform: translateX(-3px) rotate(-1deg); } 75% { transform: translateX(3px) rotate(1deg); } }
@keyframes cfBox { 0% { box-shadow: 0 0 0 0 var(--fc, #ffc94a); } 40% { box-shadow: 0 0 0 3px var(--fc, #ffc94a), 0 0 30px var(--fc, #ffc94a); } 100% { box-shadow: none; } }
@media (max-width: 600px) { #crewFeed .cf-p b { display: none; } #crewFeed .cf-p { flex: 0 1 auto; padding-right: 6px; } #crewFeed .cf-crew { padding: 4px 6px; } #crewFeed { position: fixed; left: 8px; right: 8px; bottom: 132px; max-width: none; width: auto; z-index: 71; } #crewFeed .cf-list { height: 62px; } }
@media (prefers-reduced-motion: reduce) { #crewFeed .cf-row, #crewFeed .cf-row::after { animation: none !important; } }
.mp-bar { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin: 8px 0 2px; padding: 8px 10px; border-radius: 14px; background: linear-gradient(90deg, rgba(111,220,140,.16), rgba(0,0,0,.25) 60%); border: 1.5px solid rgba(111,220,140,.5); box-shadow: 0 0 22px rgba(111,220,140,.15); }
.mp-bar[hidden] { display: none; }
#credits.tmUp { animation: tmUp 1s ease-out; }
@keyframes tmUp { 30% { filter: drop-shadow(0 0 10px #6fdc8c); transform: scale(1.08); } }
#crewFeed.mp { border-color: rgba(111,220,140,.55); box-shadow: 0 0 18px rgba(111,220,140,.18); }
#crewFeed .cf-crew { display: flex; flex-wrap: wrap; gap: 5px; padding: 6px 8px; border-bottom: 1px solid rgba(255,255,255,.08); background: rgba(111,220,140,.06); }
#crewFeed .cf-crew:empty { display: none; }
.cf-p { display: flex; align-items: center; gap: 5px; padding: 2px 8px 2px 2px; border-radius: 99px; background: rgba(0,0,0,.35); border: 1.5px solid color-mix(in srgb, var(--pc) 55%, transparent); opacity: .6; min-width: 0; flex: 1 1 0; }
.cf-p.on { opacity: 1; }
.cf-p.me { border-color: #fff; }
.cf-p .av { position: relative; flex: none; }
.cf-p.on .av::after { content: ""; position: absolute; right: -1px; bottom: -1px; width: 7px; height: 7px; border-radius: 50%; background: #6fdc8c; box-shadow: 0 0 6px #6fdc8c; border: 1.5px solid #111; }
.cf-p span { display: grid; min-width: 0; line-height: 1.1; }
.cf-p b { font-size: 11px; color: #fff; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.cf-p em { font: 800 10.5px var(--f-mono, monospace); font-style: normal; white-space: nowrap; }
.cf-p em.pos { color: #6fdc8c; } .cf-p em.neg { color: #ff7a8a; }
#cfSync { font: 700 9px var(--f-mono, monospace); letter-spacing: .08em; color: rgba(255,255,255,.55); margin-left: auto; margin-right: 6px; }
#cfSync.ok { color: #6fdc8c; } #cfSync.bad { color: #ff7a8a; }
.ol-team { display: grid; gap: 6px; padding: 10px 12px; border-radius: 12px; background: rgba(255,255,255,.05); border: 1.5px solid rgba(255,255,255,.12); }
.ol-team.cur { border-color: #6fdc8c; box-shadow: 0 0 14px rgba(111,220,140,.2); }
.ol-team.sel { border-color: var(--gold, #ffc94a); }
.ol-team h4 { margin: 0; font-size: 15px; display: flex; gap: 8px; align-items: baseline; flex-wrap: wrap; }
.ol-team h4 small { font-size: 11px; color: rgba(255,255,255,.6); font-weight: 600; }
.ol-team .tw { display: flex; flex-wrap: wrap; gap: 5px; }
.ol-team .tw span { font: 700 11px var(--f-mono, monospace); padding: 3px 7px; border-radius: 8px; background: rgba(0,0,0,.3); color: rgba(255,255,255,.85); }
.ol-team .tm { display: flex; flex-wrap: wrap; gap: 6px; font-size: 12px; color: rgba(255,255,255,.8); }
.ol-team .tm em { font-style: normal; font-weight: 800; } .ol-team .tm em.pos { color: #6fdc8c; } .ol-team .tm em.neg { color: #ff7a8a; }
.mp-tag { display: grid; font: 800 11px var(--f-mono, monospace); letter-spacing: .18em; color: #6fdc8c; padding-right: 8px; border-right: 1px solid rgba(255,255,255,.15); }
.mp-tag small { font-size: 10px; color: rgba(255,255,255,.6); letter-spacing: .1em; }
.mp-pilot { display: flex; align-items: center; gap: 7px; padding: 4px 10px 4px 4px; border-radius: 99px; background: rgba(0,0,0,.35); border: 1.5px solid color-mix(in srgb, var(--pc) 60%, transparent); opacity: .55; transition: opacity .3s; }
.mp-pilot.on { opacity: 1; box-shadow: 0 0 12px color-mix(in srgb, var(--pc) 35%, transparent); }
.mp-pilot b { font-size: 13px; color: #fff; display: block; line-height: 1.1; }
.mp-pilot small { font-size: 10px; color: var(--pc); font-weight: 700; }
.mp-pilot.me { border-color: #fff; }
.mmchip .ol-badge { display: inline-block; min-width: 16px; height: 16px; border-radius: 8px; background: #ff4b6a; color: #fff; font: 800 10px/16px system-ui; text-align: center; margin-left: 4px; }
'''

ONLINE_JS = r'''
/* ---------- Online: Freunde, Rangliste, Geschenke, VS, Koop (Firebase) ---------- */
const FB_CFG = { apiKey: "AIzaSyBcnwWCg5qhD-g8DWnsNh-teUZihc4CKtM", authDomain: "salvage-grind.firebaseapp.com", databaseURL: "https://salvage-grind-default-rtdb.europe-west1.firebasedatabase.app", projectId: "salvage-grind", storageBucket: "salvage-grind.firebasestorage.app", messagingSenderId: "169044714781", appId: "1:169044714781:web:38796d21b781bed839adf4" };
const FB_VER = "10.14.1", GIFT_MS = 864e5, VS_MS = 300000, COOP_SHARE = .2, CREW_MAX = 4, VAULT_MS = 300000;
const OL = { db: null, uid: null, ready: false, err: "", code: "", friends: {}, people: {}, gifts: {}, tab: "friends", board: "friends", sent: {}, vs: null, queueRef: null,
  crew: null, crewM: {}, crewInv: {}, team: null, teamM: {}, teamInv: {}, ticker: [], live: {}, dayBest: 0, vault: null, vaultAt: 0, confirm: false };
OL.tinfo = {}; OL.bal = {};
try { OL.team = localStorage.getItem("welten-myteam") || null; OL.crew = localStorage.getItem("welten-crew") || null; OL.vault = localStorage.getItem("welten-vault") || null; } catch (e) {}
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
      OL.db.ref("teamInv/" + OL.uid).on("value", s => { OL.teamInv = s.val() || {}; olBadge(); if (mmOpen("online")) olRender(); });
      [OL.team, window.TEAM_ID].forEach(t => { if (t && !teamList()[t]) teamRemember(t, "Team"); });
      if (window.TEAM_ID || OL.team) { const t0 = window.TEAM_ID || OL.team; OL.team = null; teamSet(t0); }
      if (window.TEAM_ID) teamStart().catch(e => { try { console.warn("Team:", e); } catch (x) {} });
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
    ["w/" + WORLD_ID]: { l: state.level, p: Math.round(state.peak || 0), c: Math.round(state.credits) }, ["av/" + WORLD_ID]: typeof avIdx === "number" ? avIdx : 0 }).catch(() => {});
}
async function olLoadPeople() {
  const ids = Object.keys(OL.friends);
  await Promise.all(ids.map(async id => { try { OL.people[id] = (await OL.db.ref("players/" + id).get()).val() || { n: "?" }; } catch (e) {} }));
  if (mmOpen("online")) olRender();
}
const olOnline = p => p && p.on && Date.now() - p.on < 150000;
function olBadge() {
  const n = Object.values(OL.gifts).filter(g => g && !g.c).length + Object.keys(OL.crewInv).length + Object.keys(OL.teamInv || {}).length;
  const b = $("olChip"); if (!b) return;
  b.querySelector(".ol-badge") && b.querySelector(".ol-badge").remove();
  if (n) b.insertAdjacentHTML("beforeend", `<span class="ol-badge">${n}</span>`);
}
function olMsg(t, ok) { const el = $("olMsg"); if (!el) return; el.textContent = t || ""; el.className = "ol-msg" + (t ? (ok ? " ok" : " err") : ""); }

/* --- Dialog --- */
(function setupOnline() {
  document.body.insertAdjacentHTML("beforeend", `<div class="bonus" id="online" hidden role="dialog" aria-modal="true" aria-labelledby="olTitle" style="z-index:260">
  <div class="bonus-card"><h2 id="olTitle" style="margin:0 0 4px">Online</h2>
  <div class="ol-tabs" id="olTabs"><button type="button" data-t="friends">Freunde</button><button type="button" data-t="board">Rangliste</button><button type="button" data-t="vs">VS-Duell</button><button type="button" data-t="coop">Koop-Crew</button><button type="button" data-t="team">Team-Spielstand</button><button type="button" data-t="save">Spielstand</button></div>
  <p class="ol-msg" id="olMsg" aria-live="polite"></p>
  <div class="ol-pane" id="olPane"></div>
  <div class="ar-row"><span></span><button type="button" class="bbtn ghost" id="olClose">Schließen</button></div></div></div>
  <div id="vsBar" hidden></div>
  <div id="crewFeed" hidden aria-live="polite"><div class="cf-head"><span id="cfTitle"><i></i>CREW LIVE</span><span id="cfSync"></span><button type="button" id="cfMin" aria-label="Feed einklappen">–</button></div><div class="cf-crew" id="cfCrew"></div><div class="cf-list" id="cfList"><div class="cf-empty">Gewinne deiner Mitspieler erscheinen hier live.</div></div></div>`);
  setTimeout(() => { const fb = $("fsBuyBtn"), cf = $("crewFeed"); if (fb && cf) fb.parentNode.insertBefore(cf, fb); }, 0);
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
const olNet = id => { const b = (OL.bal || {})[id]; return b ? Math.round((b.w || 0) - (b.s || 0)) : null; };
const olNetTxt = v => v == null ? "" : `${v >= 0 ? "+" : "−"}${fmtN(Math.abs(v))}`;
function olItem(id, p, extra, me, bal) {
  const w = (p && p.w && p.w[WORLD_ID]) || {};
  const av = me ? avMine() : avOf(p);
  return `<div class="ol-item${me ? " me" : ""}" style="grid-template-columns:auto auto 1fr auto"><span class="ol-dot${me || olOnline(p) ? " on" : ""}"></span>${av ? avHtml(av, 34, cfColor(id)) : `<span class="av" style="width:34px;height:34px;--avc:${cfColor(id)};font:800 14px system-ui;color:#fff">${escapeHTML(((p && p.n) || "?").slice(0, 1))}</span>`}<span><b>${escapeHTML((p && p.n) || "?")}${me ? " (du)" : ""}</b><small>Rang ${w.l || "–"} · Rekord ${fmtN(w.p || 0)}${bal != null ? ` · Bilanz <b style="color:${bal >= 0 ? "#6fdc8c" : "#ff7a8a"}">${olNetTxt(bal)}</b>` : ""}</small></span><span class="ol-acts">${extra || ""}</span></div>`;
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
      ${OL.crew ? `<p class="ol-info"><b>Deine Crew (${n}/${CREW_MAX})</b> · Bauteile kosten gerade ${Math.round((coopCostMul() - 1) * 100)} % mehr.</p><div class="ol-list">${ids2.map(id => olItem(id, id === OL.uid ? { n: olName(), w: { [WORLD_ID]: { l: state.level, p: state.peak } } } : OL.people[id] || { n: OL.crewM[id] }, "", id === OL.uid, olNet(id))).join("")}</div><div class="ol-row"><button type="button" class="ol-small" data-a="leave">Crew verlassen</button></div>`
        : `<p class="ol-info">Du bist in keiner Crew. Lade unter „Freunde“ jemanden ein.</p>`}
      <h3 style="margin:14px 0 6px;font-size:15px">Live-Ticker deiner Freunde</h3><div class="ol-list">${OL.ticker.length ? OL.ticker.slice(0, 12).map(t => `<div class="ol-item"><span class="ol-dot on"></span><span><b>${escapeHTML(t.n)}</b><small>${escapeHTML(t.wn || "")} · ${new Date(t.t).toLocaleTimeString("de-DE", { hour: "2-digit", minute: "2-digit" })}</small></span><span class="ol-acts"><b>+${fmtN(t.a)}</b></span></div>`).join("") : `<p class="ol-info">Noch nichts los. Große Gewinne deiner Freunde erscheinen hier sofort.</p>`}</div>`;
  } else if (OL.tab === "team") {
    const inv = Object.entries(OL.teamInv || {}), L = teamList(), tids = Object.keys(L).sort((a, b) => (((OL.tinfo || {})[b] || {}).i || {}).p - (((OL.tinfo || {})[a] || {}).i || {}).p || 0), ids3 = Object.keys(OL.teamM || {});
    P.innerHTML = `<p class="ol-info">Ein <b>gemeinsamer Spielstand</b> für bis zu 4 Spieler, getrennt von deinem eigenen: Ihr teilt Credits, Erfahrung, Schiff und Ausbau. Jeder Gewinn und jeder Kauf zählt sofort für alle. Dein eigener Spielstand bleibt unberührt, du kannst jederzeit zurückwechseln.</p>
      ${inv.length ? `<div class="ol-gifts">${inv.map(([tid, v]) => `<div class="ol-gift"><span>🤝 <b>${escapeHTML(v.n || "Ein Freund")}</b> lädt dich in sein Team ein</span><span class="ol-acts"><button type="button" data-a="tjoin" data-id="${tid}">Beitreten</button><button type="button" data-a="tdecline" data-id="${tid}">Ablehnen</button></span></div>`).join("")}</div>` : ""}
      <h3 style="margin:10px 0 6px;font-size:15px">Deine Team-Spielstände (${tids.length})</h3>
      <div class="ol-list">${tids.length ? tids.map(teamCard).join("") : `<p class="ol-info">Noch keine Team-Spielstände. Leg unten einen an.</p>`}</div>
      ${OL.team && L[OL.team] ? `<p class="ol-info" style="margin-top:10px"><b>Einladen in „${escapeHTML(L[OL.team].n)}“ (${ids3.length}/4):</b></p><div class="ol-list">${Object.keys(OL.friends).filter(f => !OL.teamM[f]).map(f => olItem(f, OL.people[f], `<button type="button" data-a="tinvite" data-id="${f}" ${ids3.length >= 4 ? "disabled" : ""}>Einladen</button>`)).join("") || `<p class="ol-info">Alle Freunde sind schon im Team.</p>`}</div>` : ""}
      <h3 style="margin:14px 0 6px;font-size:15px">Neuer Team-Spielstand</h3>
      <div class="ol-row"><input id="olTeamName" maxlength="24" placeholder="Name, z. B. Freitagsrunde" aria-label="Name des Team-Spielstands"><button type="button" class="ol-small" data-a="tnew">Anlegen</button></div>`;
    teamInfoLoad(false);
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
    else if (a === "tnew") { const nm = (($("olTeamName") || {}).value || "").trim().slice(0, 24) || `Team ${olDate(Date.now())}`; const tid = OL.db.ref("teams").push().key; await OL.db.ref(`teams/${tid}/m/${OL.uid}`).set(olName()); await OL.db.ref(`teams/${tid}/i`).set({ n: nm, t: firebase.database.ServerValue.TIMESTAMP, p: 0 }); teamRemember(tid, nm, Date.now()); teamSet(tid); await teamInfoLoad(true); olMsg(`„${nm}“ angelegt. Lade jetzt Freunde ein oder tippe auf „Spielen“.`, true); }
    else if (a === "tsel") { teamSet(id); }
    else if (a === "tforget") { teamForget(id); if (OL.team === id) teamSet(null); olRender(); }
    else if (a === "tren") { const inp = $("olTeamName"), nm = ((inp || {}).value || "").trim().slice(0, 24); if (!nm) { olMsg("Schreib den neuen Namen unten ins Namensfeld und tippe dann nochmal auf „Umbenennen“.", false); if (inp) inp.focus(); return; } await OL.db.ref(`teams/${id}/i/n`).set(nm); teamRemember(id, nm); inp.value = ""; await teamInfoLoad(true); olMsg(`Umbenannt in „${nm}“.`, true); }
    else if (a === "tinvite") { await OL.db.ref(`teamInv/${id}/${OL.team}`).set({ n: olName(), tn: (teamList()[OL.team] || {}).n || "", t: firebase.database.ServerValue.TIMESTAMP }); olMsg(`Einladung an ${(OL.people[id] || {}).n || "deinen Freund"} verschickt.`, true); }
    else if (a === "tjoin") { const mm = (await OL.db.ref(`teams/${id}/m`).get()).val() || {}; if (!Object.keys(mm).length) { await OL.db.ref(`teamInv/${OL.uid}/${id}`).remove(); olMsg("Dieses Team gibt es nicht mehr.", false); return; } if (Object.keys(mm).length >= 4) { olMsg("Das Team ist schon voll (4 Spieler).", false); return; } await OL.db.ref(`teams/${id}/m/${OL.uid}`).set(olName()).catch(() => { throw new Error("voll"); }); await OL.db.ref(`teamInv/${OL.uid}/${id}`).remove(); const ti = (await OL.db.ref(`teams/${id}/i`).get()).val() || {}; teamRemember(id, ti.n || (OL.teamInv[id] || {}).tn || "Team", ti.t || Date.now()); teamSet(id); await teamInfoLoad(true); olMsg("Du bist dem Team beigetreten. Tippe auf „Spielen“.", true); }
    else if (a === "tdecline") await OL.db.ref(`teamInv/${OL.uid}/${id}`).remove();
    else if (a === "tplay") teamSwitch(id || OL.team);
    else if (a === "tsolo") teamSwitch(null);
    else if (a === "tleave") { const tid = id || OL.team; if (OL.confirmLeave !== tid) { OL.confirmLeave = tid; olMsg("Wirklich verlassen? Der Team-Spielstand ist dann für dich weg. Zum Bestätigen nochmal auf „Verlassen“ tippen.", false); return; } OL.confirmLeave = null; await OL.db.ref(`teams/${tid}/m/${OL.uid}`).remove().catch(() => {}); teamForget(tid); if (OL.team === tid) teamSet(null); if (window.TEAM_ID === tid) teamSwitch(null); else { olMsg("Team verlassen.", true); olRender(); } }
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
function olSetCrew(cid) { if (OL.logRef) { OL.logRef.off(); OL.logRef = null; } $("crewFeed").hidden = !cid; if (!cid && window.TEAM_ID && OL.db) cfListen(`teams/${TEAM_ID}/log`, "TEAM LIVE"); OL.crew = cid; try { cid ? localStorage.setItem("welten-crew", cid) : localStorage.removeItem("welten-crew"); } catch (e) {} if (OL.crewRef) { OL.crewRef.off(); OL.feedRef.off(); OL.crewRef = OL.feedRef = null; } OL.crewM = {}; if (cid) olCrewListen(); render(); }
function olCrewListen() {
  OL.crewRef = OL.db.ref(`crews/${OL.crew}/m`);
  OL.crewRef.on("value", s => { OL.crewM = s.val() || {}; if (OL.crew && !OL.crewM[OL.uid]) { olSetCrew(null); } Object.keys(OL.crewM).forEach(id => { if (id !== OL.uid && !OL.people[id]) OL.db.ref("players/" + id).get().then(x => { OL.people[id] = x.val() || { n: OL.crewM[id] }; }).catch(() => {}); }); render(); if (mmOpen("online")) olRender(); });
  $("crewFeed").hidden = false;
  const since = Date.now() - 60000;
  cfListen(`crews/${OL.crew}/log`, "CREW LIVE");
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
function cfListen(path, title) {
  if (OL.logRef) OL.logRef.off();
  $("crewFeed").hidden = false; $("cfTitle").innerHTML = `<i></i>${title}`;
  const since = Date.now() - 60000;
  OL.logRef = OL.db.ref(path).limitToLast(6);
  OL.logRef.on("child_added", s => { const v = s.val(); if (v && (v.t || 0) > since) cfAdd(v); });
}
/* --- Crew-Feed (wie ein Kill-Feed): letzte Gewinne der Crew, live --- */
const CF_COL = ["#4fe3ff", "#ffb36b", "#a7c060", "#ff7ad9", "#7ee0c8", "#b9a4ff"];
function cfColor(uid) { let h = 0; for (const c of uid || "") h = (h * 31 + c.charCodeAt(0)) >>> 0; return CF_COL[h % CF_COL.length]; }
const CF_FT = { buy: ["🔧", "Ausbau", "#ffb36b"], fs: ["🎰", "FREISPIELE!", "#b8ff5c"], fsb: ["🛒", "Freispiele gekauft", "#7ee0c8"], bonus: ["🎁", "BONUSSPIEL!", "#ff7ad9"], jp: ["👑", "JACKPOT!", "#ffc94a"], ladder: ["🪜", "Risikoleiter geschafft", "#4fe3ff"], gamble: ["🃏", "Risiko gewonnen", "#9fb3ff"] };
function cfAdd(v) {
  const list = $("cfList"); if (!list) return;
  const em = list.querySelector(".cf-empty"); if (em) em.remove();
  const me = v.u === OL.uid, ft = v.k && CF_FT[v.k], big = (v.x || 0) >= 25;
  const ic = ft ? ft[0] : big ? "💥" : (v.x || 0) >= 10 ? "🔥" : "💰";
  const right = v.k === "buy" ? `${escapeHTML(v.part || "Bauteil")} ${v.lvl || ""}` : ft ? ft[1] + (v.a ? ` +${fmtN(v.a)}` : "") : `+${fmtN(v.a)}`;
  const avA = typeof v.av === "number" && AV_SETS[v.w || WORLD_ID] ? AV_SETS[v.w || WORLD_ID][v.av] : null;
  list.insertAdjacentHTML("afterbegin", `<div class="cf-row${me ? " me" : ""}${big ? " big" : ""}${ft ? " ft" : ""}${v.k === "jp" ? " jp" : ""}" style="--pc:${cfColor(v.u)};${ft ? `--fc:${ft[2]}` : ""}">${avA ? avHtml(avA, 22, cfColor(v.u)) : ""}<span class="cf-ic">${ic}</span><b>${escapeHTML(me ? "Du" : v.n || "?")}</b><small>${escapeHTML(v.wn || "")}${!ft && v.x ? " · " + v.x + "×" : ""}</small><span class="cf-amt">${right}</span></div>`);
  [...list.children].forEach((r, i) => { r.classList.toggle("old", i >= 3); if (i >= 5) r.remove(); });
  const row = list.firstElementChild, box = $("crewFeed");
  if (ft || big) { box.style.setProperty("--fc", ft ? ft[2] : "#ffc94a"); box.classList.remove("flash"); void box.offsetWidth; box.classList.add("flash");
    try { burstAt(row, ft ? 26 : 18, ft ? [ft[2], "#ffffff"] : ["#ffc94a", "#ffffff"], .7); } catch (e) {}
    if (!me) { try { tone(ft ? 880 : 660, .18, { type: "triangle", vol: .05 }); tone(ft ? 1320 : 990, .2, { type: "triangle", vol: .04, at: .09 }); } catch (e) {} } }
  if (v.k === "buy" && !me) mpBuyNotice(v);
  setTimeout(() => row.classList.add("old"), 8000);
  setTimeout(() => { row.classList.add("gone"); setTimeout(() => { row.remove(); if (!list.children.length) list.innerHTML = `<div class="cf-empty">Gewinne deiner Mitspieler erscheinen hier live.</div>`; }, 650); }, 22000);
}
/* --- Team-Spielstand: bis 4 Spieler teilen einen eigenen Spielstand --- */
function teamList() { try { return JSON.parse(localStorage.getItem("welten-teams") || "{}") || {}; } catch (e) { return {}; } }
function teamRemember(tid, n, t) { const o = teamList(); o[tid] = { n: n || (o[tid] || {}).n || "Team", t: t || (o[tid] || {}).t || Date.now() }; try { localStorage.setItem("welten-teams", JSON.stringify(o)); } catch (e) {} }
function teamForget(tid) { const o = teamList(); delete o[tid]; try { localStorage.setItem("welten-teams", JSON.stringify(o)); } catch (e) {} delete OL.tinfo[tid]; }
const olDate = t => t ? new Date(t).toLocaleDateString("de-DE", { day: "2-digit", month: "2-digit", year: "numeric" }) : "–";
const olTime = t => t ? olDate(t) + " " + new Date(t).toLocaleTimeString("de-DE", { hour: "2-digit", minute: "2-digit" }) : "–";
async function teamInfoLoad(force) {
  const L = teamList(); OL.tinfo = OL.tinfo || {};
  const todo = Object.keys(L).filter(tid => force || !OL.tinfo[tid] || Date.now() - OL.tinfo[tid].at >= 30000);
  if (!todo.length || OL.tLoading) return; OL.tLoading = true;
  await Promise.all(todo.map(async tid => {
    try {
      const [i, m, b, w] = await Promise.all(["i", "m", "b", "w"].map(k => OL.db.ref(`teams/${tid}/${k}`).get().then(x => x.val())));
      const ws = {}; Object.entries(w || {}).forEach(([wid, v]) => { let sv = {}; try { sv = JSON.parse(v.save || "{}"); } catch (e) {} const st = sv.ship ? Object.values(sv.ship).reduce((a, x) => a + (x || 0), 0) : 0; ws[wid] = { c: v.c || 0, l: sv.level || 1, v: (sv.vehicle | 0) + 1, st }; });
      if (i && i.n && i.n !== L[tid].n) teamRemember(tid, i.n, i.t);
      OL.tinfo[tid] = { at: Date.now(), i: i || {}, m: m || {}, b: b || {}, w: ws, gone: !m || !m[OL.uid] };
    } catch (e) { OL.tinfo[tid] = { at: Date.now(), i: {}, m: {}, b: {}, w: {}, gone: true }; }
  }));
  OL.tLoading = false;
  if (mmOpen("online") && OL.tab === "team") olRender();
}
function teamCard(tid) {
  const L = teamList()[tid] || {}, I = (OL.tinfo || {})[tid], cur = window.TEAM_ID === tid, sel = OL.team === tid;
  const info = I ? I.i : {}, m = I ? I.m : {}, b = I ? I.b : {};
  const worlds = I ? WORLDS.filter(w => I.w[w.id]).map(w => { const x = I.w[w.id]; return `<span title="${escapeHTML(w.name)}">${escapeHTML(w.name)} · Rang ${x.l} · ${fmtN(x.c)} · Fz. ${x.v} (${x.st}/45)</span>`; }).join("") : "";
  const mem = I ? Object.keys(m).map(id => { const bb = b[id], net = bb ? Math.round((bb.w || 0) - (bb.s || 0)) : null; return `<span>${escapeHTML(id === OL.uid ? olName() + " (du)" : (OL.people[id] || {}).n || m[id] || "?")}${net != null ? ` <em class="${net >= 0 ? "pos" : "neg"}">${olNetTxt(net)}</em>` : ""}</span>`; }).join(" · ") : "Lade …";
  return `<div class="ol-team${cur ? " cur" : ""}${sel && !cur ? " sel" : ""}"><h4>${escapeHTML(info.n || L.n || "Team")}<small>erstellt ${olDate(info.t || L.t)} · zuletzt gespielt ${olTime(info.p)}</small></h4>
    ${I && I.gone ? `<p class="ol-info">Dieses Team gibt es nicht mehr oder du bist nicht mehr dabei.</p><div class="ol-row"><button type="button" class="ol-small" data-a="tforget" data-id="${tid}">Aus der Liste entfernen</button></div></div>` : `
    <div class="tm">👥 ${mem}</div>${worlds ? `<div class="tw">${worlds}</div>` : `<div class="tw"><span>Noch nicht gespielt</span></div>`}
    <div class="ol-row">${cur ? `<button type="button" class="bbtn" data-a="tsolo">Zurück zu meinem Spielstand</button>` : `<button type="button" class="bbtn" data-a="tplay" data-id="${tid}">Spielen</button>`}<button type="button" class="ol-small" data-a="tsel" data-id="${tid}">${sel ? "✓ Ausgewählt" : "Mitspieler einladen"}</button><button type="button" class="ol-small" data-a="tren" data-id="${tid}">Umbenennen</button><button type="button" class="ol-small" data-a="tleave" data-id="${tid}">Verlassen</button></div></div>`}`;
}
function teamSet(tid) {
  if (OL.team && OL.db) OL.db.ref(`teams/${OL.team}/m`).off();
  OL.team = tid; OL.teamM = {}; try { tid ? localStorage.setItem("welten-myteam", tid) : localStorage.removeItem("welten-myteam"); } catch (e) {}
  if (tid) OL.db.ref(`teams/${tid}/m`).on("value", s => { OL.teamM = s.val() || {}; Object.keys(OL.teamM).forEach(id => { if (id !== OL.uid && !OL.people[id]) OL.db.ref("players/" + id).get().then(x => { OL.people[id] = x.val() || { n: OL.teamM[id] }; if (mmOpen("online")) olRender(); }).catch(() => {}); }); if (mmOpen("online")) olRender(); });
  if (mmOpen("online")) olRender();
}
function teamSwitch(tid) {
  try { flushSave && flushSave(); } catch (e) {}
  setTimeout(() => {
    ready = false;   // verhindert, dass der gerade geladene Stand beim Wechsel überschrieben wird
    try { tid ? localStorage.setItem("welten-team", tid) : localStorage.removeItem("welten-team"); } catch (e) {}
    olMsg(tid ? "Wechsle zum Team-Spielstand …" : "Wechsle zu deinem Spielstand …", true);
    setTimeout(() => location.reload(), 600);
  }, 400);
}
const TM = { on: false, c: 0, x: 0, busy: false, n: 0 };
const teamPath = () => `teams/${TEAM_ID}/w/${WORLD_ID}`;
function teamMerge(a, b) {
  const o = { ...a };
  if (!b) return o;
  SAVE_KEYS.forEach(k => { if (k !== "credits" && k !== "xp" && typeof b[k] === "number") o[k] = Math.max(a[k] || 0, b[k]); });
  const va = a.vehicle | 0, vb = b.vehicle | 0;   // neues Fahrzeug startet als Wrack: Ausbau nur innerhalb desselben Fahrzeugs zusammenführen
  if (vb > va) o.ship = { ...(b.ship || {}) };
  else if (vb === va && b.ship) { o.ship = { ...(a.ship || {}) }; Object.keys(b.ship).forEach(k => { o.ship[k] = Math.max(o.ship[k] || 0, b.ship[k] || 0); }); }
  ["found", "visited", "album", "ach", "crew"].forEach(k => { if (Array.isArray(b[k])) o[k] = [...new Set([...(a[k] || []), ...b[k]])]; });
  if (b.stats) { o.stats = { ...(a.stats || {}) }; Object.keys(b.stats).forEach(k => { if (typeof b.stats[k] === "number") o.stats[k] = Math.max(o.stats[k] || 0, b.stats[k]); }); }
  if (b.shipNamed && !a.shipNamed) { o.shipName = b.shipName; o.shipNamed = true; }
  return o;
}
function teamApply(remote) {
  const c = state.credits, x = state.xp, v0 = state.vehicle | 0, s0 = JSON.stringify(state.ship || {});
  applySave(teamMerge(serialize(), remote)); state.credits = c; state.xp = x;
  if ((state.vehicle | 0) !== v0 || JSON.stringify(state.ship || {}) !== s0) { try { lastShipKey = ""; lastVehKey = ""; } catch (e) {} OL.lastShip = JSON.stringify(state.ship || {}); }
  try { render(); renderHangar(); } catch (e) {}
}
async function teamStart() {
  const m = (await OL.db.ref(`teams/${TEAM_ID}/m`).get()).val() || {};
  if (!m[OL.uid]) { teamSwitch(null); return; }   // nicht (mehr) im Team: zurück zum eigenen Spielstand
  const r = (await OL.db.ref(teamPath()).get()).val();
  if (r && r.save) { try { teamApply(JSON.parse(r.save)); } catch (e) {} state.credits = r.c; state.xp = r.x || 0; render(); }
  else await OL.db.ref(teamPath()).set({ save: JSON.stringify(serialize()), c: state.credits, x: state.xp });
  TM.c = state.credits; TM.x = state.xp; TM.on = true; TM.ok = Date.now();
  const L = teamList()[TEAM_ID] || {};
  OL.db.ref(`teams/${TEAM_ID}/i`).get().then(x => { const i = x.val() || {}; const up = { p: firebase.database.ServerValue.TIMESTAMP }; if (!i.n) { up.n = L.n || "Team"; up.t = L.t || Date.now(); } return OL.db.ref(`teams/${TEAM_ID}/i`).update(up); }).catch(() => {});
  teamLive();
  if (!OL.crew) cfListen(`teams/${TEAM_ID}/log`, "TEAM LIVE");
  const chip = $("olChip"); if (chip) { chip.style.borderColor = "#6fdc8c"; chip.title = "Team-Spielstand aktiv"; }
  radio(`Funk: Team-Spielstand aktiv (${Object.values(m).join(", ")}). Alles, was ihr gewinnt und kauft, teilt ihr.`, true);
  saveGame();
}
/* Live: Credits, Erfahrung und Spielstand der Mitspieler sofort übernehmen (nicht erst beim nächsten Abgleich) */
function teamLive() {
  const live = (k, f) => OL.db.ref(teamPath() + "/" + k).on("value", s => { const V = s.val(); if (V == null || TM.busy) return; f(V); TM.ok = Date.now(); });
  live("c", V => { if (V === TM.c) return; const up = V > TM.c; state.credits = V + (state.credits - TM.c); TM.c = V; teamShow(up); });
  live("x", V => { if (V === TM.x) return; state.xp = V + (state.xp - TM.x); TM.x = V; });
  live("save", V => { if (V === TM.mine) return; TM.remote = V; if (machineIdle()) teamApplyRemote(); });
}
/* Credits-Anzeige nachziehen, wenn Mitspieler gewinnen oder ausgeben (sonst sähe man es erst nach dem nächsten Dreh) */
function teamShow(up) { if (!machineIdle() || shownCredits === state.credits) return; countCredits(state.credits, 700); if (up) { const el = $("credits"); el.classList.remove("tmUp"); void el.offsetWidth; el.classList.add("tmUp"); } render(); }
function teamApplyRemote() { const v = TM.remote; TM.remote = null; if (!v) return; try { teamApply(JSON.parse(v)); } catch (e) {} }
const teamSig = () => { const o = serialize(); delete o.credits; delete o.xp; return JSON.stringify(o); };
async function teamSaveSync() {
  const r = await OL.db.ref(teamPath() + "/save").transaction(v => { let rem = null; try { rem = v ? JSON.parse(v) : null; } catch (e) {} TM.mine = JSON.stringify(teamMerge(serialize(), rem)); return TM.mine; });
  TM.sig = teamSig();
  if (machineIdle()) { try { teamApply(JSON.parse(r.snapshot.val())); } catch (e) {} TM.sig = teamSig(); } else TM.now = true;
}
function teamMergeNow() { TM.now = true; }
async function teamPull() { if (!TM.on) return; const v = (await OL.db.ref(teamPath() + "/save").get()).val(); if (v && machineIdle()) { try { teamApply(JSON.parse(v)); } catch (e) {} } else TM.now = true; }
async function teamTick() {
  if (!TM.on || TM.busy) return;
  TM.busy = true; TM.n++;
  try {
    const c0 = state.credits, x0 = state.xp, dc = c0 - TM.c, dx = x0 - TM.x;
    const rc = await OL.db.ref(teamPath() + "/c").transaction(v => Math.max(0, (v || 0) + dc));
    const rx = await OL.db.ref(teamPath() + "/x").transaction(v => Math.max(0, (v || 0) + dx));
    const C = rc.snapshot.val() || 0, X = rx.snapshot.val() || 0;
    state.credits = C + (state.credits - c0); state.xp = X + (state.xp - x0);   // was während der Übertragung dazukam, bleibt erhalten
    TM.c = C; TM.x = X;
    TM.ok = Date.now();
    if (TM.remote && machineIdle()) teamApplyRemote();
    if (TM.now || teamSig() !== TM.sig || TM.n % 5 === 0) { TM.now = false; await teamSaveSync(); }
    if (TM.n % 30 === 0) OL.db.ref(`teams/${TEAM_ID}/i/p`).set(firebase.database.ServerValue.TIMESTAMP).catch(() => {});
    teamShow(false); if (machineIdle()) render();
  } catch (e) {} finally { TM.busy = false; }
}
function mpBuyNotice(v) {
  const el = $("achPop"); if (!el) return;
  const avA = typeof v.av === "number" && AV_SETS[v.w || WORLD_ID] ? AV_SETS[v.w || WORLD_ID][v.av] : null;
  el.style.setProperty("--mc", "#ffb36b");
  el.innerHTML = `<small>${window.TEAM_ID ? "TEAM-AUSBAU" : "CREW-AUSBAU"}</small><div class="medal" style="background:none;box-shadow:none">${avA ? avHtml(avA, 70, cfColor(v.u)) : "🔧"}</div><b>${escapeHTML(v.n || "?")}</b><p>hat <b style="font-size:1rem">${escapeHTML(v.part || "ein Bauteil")} ${escapeHTML(v.lvl || "")}</b> gekauft${window.TEAM_ID && v.w === WORLD_ID ? " – für euch alle!" : "."}</p>`;
  el.classList.add("on");
  try { sfx.bigUpgrade ? sfx.bigUpgrade() : sfx.upgrade(); flashScreen(); const sv = $("shipview"); if (sv) { burstAt(sv, 90, ["#ffb36b", "#ffffff", "#ffc94a"], 1.1); sv.classList.remove("flash"); void sv.offsetWidth; sv.classList.add("flash"); } } catch (e) {}
  setTimeout(() => el.classList.remove("on"), 3600);
  if (window.TEAM_ID && v.w === WORLD_ID) teamPull().catch(() => {});
}
/* --- Bilanz je Spieler (Gewinn minus Einsatz) in Crew oder Team --- */
const balPath = () => OL.crew ? `crews/${OL.crew}/b` : window.TEAM_ID ? `teams/${TEAM_ID}/b` : null;
function balListen() { const p = balPath(); if (OL.balKey === p) return; if (OL.balRef) OL.balRef.off(); OL.balKey = p; OL.bal = {}; OL.balRef = null; if (!p) return; OL.balRef = OL.db.ref(p); OL.balRef.on("value", s => { OL.bal = s.val() || {}; mpBar(); }); }
/* --- Crew-/Team-Leiste im Live-Feed: Pilotenbilder, Namen, online, Bilanz --- */
function mpBar() {
  const old = $("mpBar"); if (old) old.remove();
  const box = $("crewFeed"), el = $("cfCrew"); if (!box || !el) return;
  const ids = OL.crew ? Object.keys(OL.crewM) : window.TEAM_ID ? Object.keys(OL.teamM || {}) : [];
  box.classList.toggle("mp", !!ids.length);
  if (!ids.length) { el.innerHTML = ""; return; }
  const names = OL.crew ? OL.crewM : OL.teamM, team = window.TEAM_ID && !OL.crew;
  const t = $("cfTitle"); if (t) t.innerHTML = `<i></i>${team ? "TEAM LIVE" : "CREW LIVE"} · ${ids.length}/4`;
  const sy = $("cfSync"); if (sy) { const ok = team ? Date.now() - (TM.ok || 0) < 8000 : true; sy.className = ok ? "ok" : "bad"; sy.textContent = team ? (ok ? "● synchron" : "● verbinde …") : ""; }
  const order = ids.slice().sort((a, b) => (olNet(b) ?? -1e18) - (olNet(a) ?? -1e18));
  el.innerHTML = order.map(id => { const me = id === OL.uid, p = me ? { n: olName() } : OL.people[id] || { n: names[id] }, on = me || olOnline(OL.people[id]), av = me ? avMine() : avOf(OL.people[id]), net = olNet(id);
    return `<span class="cf-p${on ? " on" : ""}${me ? " me" : ""}" style="--pc:${cfColor(id)}" title="${escapeHTML((me ? "Du" : p.n || names[id] || "?") + " · " + (on ? "online" : "offline"))}">${av ? avHtml(av, 22, cfColor(id)) : `<span class="av" style="width:22px;height:22px;--avc:${cfColor(id)}"></span>`}<span><b>${escapeHTML(me ? "Du" : p.n || names[id] || "?")}</b><em class="${(net || 0) >= 0 ? "pos" : "neg"}">${net == null ? "±0" : olNetTxt(net)}</em></span></span>`; }).join("");
}
setInterval(() => { try { if (OL.ready) mpBar(); } catch (e) {} }, 3000);
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
function olSaves() { const s = {}; [...WORLDS.map(w => w.key), "welten-lang", "welten-teams"].forEach(k => { try { const v = localStorage.getItem(k); if (v != null) s[k.replace(/[.#$\[\]\/]/g, "_")] = v; } catch (e) {} }); return s; }
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
let olWon = null, olBet = 0, olN = 0, olBest = null, olFt = null;
const olFtNow = () => { const t = state.stats || {}; return { fs: t.fs || 0, fsb: t.fsBought || 0, bonus: state.bonusCount || 0, jp: t.jackpots || 0, ladder: t.ladderWins || 0, gamble: t.gambleWins || 0 }; };
const olLogPath = () => OL.crew ? `crews/${OL.crew}/log` : window.TEAM_ID ? `teams/${TEAM_ID}/log` : null;
function olTick() {
  if (!OL.ready) return;
  olN++;
  const won = sess.won; if (olWon === null) { olWon = won; olBet = sess.bet; olBest = sess.best; return; }
  const d = won - olWon; olWon = won; const db = sess.bet - olBet; olBet = sess.bet;
  balListen();
  const bp = balPath(); if (bp && (d > 0 || db > 0)) OL.db.ref(`${bp}/${OL.uid}`).update({ w: firebase.database.ServerValue.increment(Math.max(0, d)), s: firebase.database.ServerValue.increment(Math.max(0, db)), n: olName() }).catch(() => {});
  const wn = (WORLDS.find(w => w.id === WORLD_ID) || {}).name || "";
  const lp = olLogPath(), ftNow = olFtNow();
  if (lp && olFt) Object.keys(ftNow).forEach(k => { if (ftNow[k] > olFt[k]) OL.db.ref(lp).push({ u: OL.uid, n: olName(), k, a: 0, wn, w: WORLD_ID, av: avIdx, t: firebase.database.ServerValue.TIMESTAMP }).catch(() => {}); });
  olFt = ftNow;
  const shipNow = JSON.stringify(state.ship || {});
  if (lp && OL.lastShip && shipNow !== OL.lastShip) { const old = JSON.parse(OL.lastShip);
    Object.keys(state.ship).forEach(id => { if ((state.ship[id] || 0) > (old[id] || 0)) { const c = CATS.find(x => x.id === id) || {};
      OL.db.ref(lp).push({ u: OL.uid, n: olName(), k: "buy", part: c.name || id, lvl: `St. ${state.ship[id]}`, a: 0, wn, w: WORLD_ID, av: avIdx, t: firebase.database.ServerValue.TIMESTAMP }).catch(() => {}); } });
    if (TM.on) teamMergeNow(); }
  OL.lastShip = shipNow;
  if (d > 0 && lp && d >= bet() * 2) OL.db.ref(lp).push({ u: OL.uid, n: olName(), a: d, x: Math.round(d / Math.max(1, bet())), wn, w: WORLD_ID, av: avIdx, t: firebase.database.ServerValue.TIMESTAMP }).catch(() => {});
  if (d > 0 && OL.crew) { const share = Math.floor(d * COOP_SHARE); if (share > 0) Object.keys(OL.crewM).forEach(id => { if (id !== OL.uid && olOnline(OL.people[id])) OL.db.ref(`crews/${OL.crew}/feed/${id}`).push({ a: share, n: olName() }).catch(() => {}); }); }
  if (d >= bet() * 10) OL.db.ref(`players/${OL.uid}/live`).set({ a: d, wn, t: firebase.database.ServerValue.TIMESTAMP }).catch(() => {});
  if (sess.best > OL.dayBest && sess.best > olBest) { OL.dayBest = sess.best; try { localStorage.setItem("welten-daybest", JSON.stringify({ d: olDay(), a: OL.dayBest })); } catch (e) {}
    OL.db.ref(`daily/${olDay()}/${OL.uid}`).set({ n: olName(), a: OL.dayBest, wn }).catch(() => {}); }
  olBest = Math.max(olBest, sess.best);
  if (OL.vs && OL.vs.state === "run" && d > 0) { OL.vs.my += Math.round(d / Math.max(1, bet()) * 10); OL.db.ref(`matches/${OL.vs.id}/s/${OL.vs.side}`).set(OL.vs.my).catch(() => {}); }
  if (olN % 15 === 0 && (OL.crew || window.TEAM_ID)) Object.keys(OL.crew ? OL.crewM : OL.teamM || {}).forEach(id => { if (id !== OL.uid) OL.db.ref("players/" + id + "/on").get().then(s => { OL.people[id] = { ...(OL.people[id] || {}), on: s.val() }; }).catch(() => {}); });
  if (OL.vault && olN % Math.round(VAULT_MS / 2000) === 0 && !window.TEAM_ID) vaultSave(false).catch(() => {});
  if (TM.on) teamTick();
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
    "teams": { "$tid": {
      ".read": "auth != null && data.child('m').child(auth.uid).exists()",
      ".write": "auth != null && (data.child('m').child(auth.uid).exists() || newData.child('m').child(auth.uid).exists())",
      "m": { ".read": "auth != null" } } },
    "teamInv": { "$to": { ".read": "auth != null && auth.uid === $to", "$tid": { ".write": "auth != null" } } },
    "vault": { "$k": { ".read": "auth != null", ".write": "auth != null && $k.length >= 16" } }
  }
}'''
