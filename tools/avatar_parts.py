# Charakterbilder: pro Welt 8 einfache, lustige Piloten (SVG aus Bausteinen), auswählbar, online sichtbar
AV_CSS = r'''
.av { display: inline-grid; place-items: center; border-radius: 50%; overflow: hidden; flex: none; background: radial-gradient(circle at 50% 35%, rgba(255,255,255,.18), rgba(0,0,0,.35)); box-shadow: 0 0 0 2px var(--avc, rgba(255,255,255,.25)); }
.av svg { width: 100%; height: 100%; display: block; }
.rank .av-me { width: 44px; height: 44px; cursor: pointer; margin-right: 2px; transition: transform .15s; }
.rank .av-me:hover { transform: scale(1.08) rotate(-4deg); }
#achPop .medal .av svg { width: 100%; height: 100%; }
#avPick .bonus-card { max-width: 620px; width: min(620px, 96vw); }
.av-grid { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px; margin: 10px 0; }
.av-grid button { display: grid; justify-items: center; gap: 6px; padding: 10px 6px; border-radius: 14px; border: 1.5px solid rgba(255,255,255,.14); background: rgba(255,255,255,.04); color: #fff; font: 700 12px var(--f-body, system-ui); cursor: pointer; transition: transform .15s, border-color .15s; }
.av-grid button:hover { transform: translateY(-2px); }
.av-grid button[aria-pressed="true"] { border-color: var(--gold, #ffc94a); background: rgba(255,201,74,.12); }
.av-grid .av { width: 72px; height: 72px; }
.av-grid small { color: rgba(255,255,255,.65); font-weight: 500; font-size: 11px; text-align: center; }
@media (max-width: 520px) { .av-grid { grid-template-columns: repeat(2, 1fr); } }
'''

AV_JS = r'''
/* ---------- Charakterbilder ---------- */
// Bausteine: Hautfarbe, Kopfform, Augen, Mund, Kopfbedeckung, Extra
const AV_SETS = {
  sternenwrack: [
    { n: "Kosmo-Katze", d: "Neun Leben, null Angst", skin: "#f2a65a", shape: "cat", eyes: "round", mouth: "cat", hat: "bubble" },
    { n: "Bolzen-Bot", d: "Piept bei Gewinnen", skin: "#9fb3c8", shape: "square", eyes: "led", mouth: "grill", hat: "antenna" },
    { n: "Glubsch", d: "Drei Augen sehen mehr", skin: "#7be07b", shape: "round", eyes: "three", mouth: "o", hat: "none" },
    { n: "Captain Keks", d: "Krümelt im Cockpit", skin: "#f1c27d", shape: "round", eyes: "wink", mouth: "grin", hat: "captain" },
    { n: "Sternen-Oma", d: "Fliegt schneller als du", skin: "#f5d0b5", shape: "round", eyes: "glasses", mouth: "smile", hat: "bun" },
    { n: "Schrott-Pinguin", d: "Friert nie im All", skin: "#2b3242", shape: "round", eyes: "round", mouth: "beak", hat: "bubble", belly: "#f4f4f4" },
    { n: "Nebel-Geist", d: "Buuuh … Jackpot!", skin: "#e9ecff", shape: "ghost", eyes: "round", mouth: "o", hat: "none" },
    { n: "Laser-Lutz", d: "Cool bleiben, Brille auf", skin: "#c68642", shape: "round", eyes: "shades", mouth: "smirk", hat: "mohawk" },
  ],
  treibgut: [
    { n: "Käpt'n Kraut", d: "Riecht nach Salz", skin: "#f1c27d", shape: "round", eyes: "patch", mouth: "grin", hat: "tricorn", beard: "#8a5a2b" },
    { n: "Papagei Polly", d: "Plappert jeden Gewinn nach", skin: "#3fbf5f", shape: "round", eyes: "round", mouth: "beak", hat: "feather" },
    { n: "Fischkopf Fred", d: "Blubb.", skin: "#5ab4e5", shape: "fish", eyes: "round", mouth: "o", hat: "none" },
    { n: "Krabben-Kai", d: "Geht seitwärts ans Ziel", skin: "#e8553c", shape: "round", eyes: "stalk", mouth: "smile", hat: "none" },
    { n: "Strand-Susi", d: "Sonnenbrand inklusive", skin: "#f5d0b5", shape: "round", eyes: "shades", mouth: "smile", hat: "straw" },
    { n: "Matrose Mo", d: "Knoten? Kann er.", skin: "#c68642", shape: "round", eyes: "wink", mouth: "grin", hat: "sailor" },
    { n: "Oktopus Otto", d: "Acht Arme für acht Walzen", skin: "#b06ad0", shape: "octo", eyes: "round", mouth: "smile", hat: "none" },
    { n: "Robbe Rita", d: "Klatscht bei jedem Fang", skin: "#8d8f99", shape: "round", eyes: "round", mouth: "cat", hat: "bandana" },
  ],
  eisenfront: [
    { n: "Feldwebel Bolz", d: "Brüllt, aber lieb", skin: "#f1c27d", shape: "square", eyes: "angry", mouth: "grin", hat: "helmet", beard: "#5b3a1a" },
    { n: "Schrauber Schmidt", d: "Hat immer Öl am Kinn", skin: "#e0ac69", shape: "round", eyes: "goggles", mouth: "smile", hat: "cap" },
    { n: "Hund Rex", d: "Bester Kamerad", skin: "#b07a45", shape: "dog", eyes: "round", mouth: "tongue", hat: "none" },
    { n: "Funkerin Frieda", d: "Hört alles, sagt nichts", skin: "#f5d0b5", shape: "round", eyes: "round", mouth: "smirk", hat: "headset" },
    { n: "Panzer-Paule", d: "Fährt rückwärts schneller", skin: "#c68642", shape: "round", eyes: "wink", mouth: "grin", hat: "helmet" },
    { n: "Opa Rostig", d: "Kennt jede Schraube", skin: "#f1d0b0", shape: "round", eyes: "glasses", mouth: "smile", hat: "beret", beard: "#dddddd" },
    { n: "Blech-Bot", d: "Quietscht ein bisschen", skin: "#8a9a52", shape: "square", eyes: "led", mouth: "grill", hat: "antenna" },
    { n: "Maulwurf Max", d: "Gräbt sich durch", skin: "#5a4a42", shape: "round", eyes: "sleepy", mouth: "smile", hat: "miner" },
  ],
  neustadt: [
    { n: "Bauleiter Bernd", d: "Termin? Läuft.", skin: "#f1c27d", shape: "round", eyes: "round", mouth: "grin", hat: "hardhat", beard: "#6b4423" },
    { n: "Waschbär Paule", d: "Klaut nur Glück", skin: "#8d8f99", shape: "raccoon", eyes: "mask", mouth: "smile", hat: "none" },
    { n: "Kran-Karla", d: "Hebt alles", skin: "#f5d0b5", shape: "round", eyes: "wink", mouth: "smile", hat: "hardhat" },
    { n: "Bürgermeisterin", d: "Hat die Schärpe", skin: "#c68642", shape: "round", eyes: "glasses", mouth: "smirk", hat: "tophat" },
    { n: "Taube Theo", d: "Gurrt Glückwünsche", skin: "#a7b0c0", shape: "round", eyes: "round", mouth: "beak", hat: "none" },
    { n: "Pizza-Pia", d: "Liefert in 5 Minuten", skin: "#e0ac69", shape: "round", eyes: "round", mouth: "tongue", hat: "cap" },
    { n: "Ziegel-Zeki", d: "Baut mit Herz", skin: "#d2691e", shape: "square", eyes: "sleepy", mouth: "grin", hat: "none" },
    { n: "Ampel-Anni", d: "Steht meist auf Grün", skin: "#6fdc8c", shape: "round", eyes: "star", mouth: "smile", hat: "beanie" },
  ],
};
const avSet = w => AV_SETS[w] || AV_SETS.sternenwrack;
function avSvg(a, uid) {
  if (!a) a = avSet(WORLD_ID)[0];
  const S = a.skin, k = "#14161f";
  let head = "", ears = "", hat = "", eyes = "", mouth = "", extra = "";
  // Kopf
  if (a.shape === "square") head = `<rect x="14" y="18" width="36" height="34" rx="7" fill="${S}" stroke="${k}" stroke-width="2"/>`;
  else if (a.shape === "ghost") head = `<path d="M14 50V30a18 18 0 0 1 36 0v20l-6-4-6 4-6-4-6 4-6-4z" fill="${S}" stroke="${k}" stroke-width="2"/>`;
  else if (a.shape === "fish") head = `<ellipse cx="32" cy="35" rx="20" ry="15" fill="${S}" stroke="${k}" stroke-width="2"/><path d="M50 35l10-8v16z" fill="${S}" stroke="${k}" stroke-width="2"/>`;
  else if (a.shape === "octo") head = `<path d="M14 36a18 18 0 0 1 36 0v6c-3 0-3 6-6 6s-3-6-6-6-3 6-6 6-3-6-6-6-3 6-6 6-3-6-6-6z" fill="${S}" stroke="${k}" stroke-width="2"/>`;
  else head = `<circle cx="32" cy="35" r="18" fill="${S}" stroke="${k}" stroke-width="2"/>`;
  if (a.shape === "cat") ears = `<path d="M17 25l2-12 9 7zM47 25l-2-12-9 7z" fill="${S}" stroke="${k}" stroke-width="2" stroke-linejoin="round"/>`;
  if (a.shape === "dog") ears = `<path d="M15 26c-6 4-5 14 0 16l4-12zM49 26c6 4 5 14 0 16l-4-12z" fill="#6b4423" stroke="${k}" stroke-width="2"/>`;
  if (a.shape === "raccoon") ears = `<circle cx="19" cy="20" r="5" fill="${S}" stroke="${k}" stroke-width="2"/><circle cx="45" cy="20" r="5" fill="${S}" stroke="${k}" stroke-width="2"/>`;
  if (a.belly) extra += `<ellipse cx="32" cy="41" rx="11" ry="10" fill="${a.belly}"/>`;
  if (a.beard) extra += `<path d="M18 40c2 10 8 14 14 14s12-4 14-14c-4 4-8 5-14 5s-10-1-14-5z" fill="${a.beard}" stroke="${k}" stroke-width="1.5"/>`;
  // Augen
  const E = (x, y) => `<circle cx="${x}" cy="${y}" r="3.2" fill="${k}"/><circle cx="${x + 1}" cy="${y - 1}" r="1" fill="#fff"/>`;
  if (a.eyes === "wink") eyes = `${E(25, 33)}<path d="M36 33h7" stroke="${k}" stroke-width="2.4" stroke-linecap="round"/>`;
  else if (a.eyes === "three") eyes = `${E(23, 34)}${E(32, 28)}${E(41, 34)}`;
  else if (a.eyes === "led") eyes = `<rect x="20" y="29" width="8" height="5" rx="1" fill="#4fe3ff"/><rect x="36" y="29" width="8" height="5" rx="1" fill="#4fe3ff"/>`;
  else if (a.eyes === "shades") eyes = `<path d="M17 30h30v3c0 4-3 6-7 6s-6-3-6-6h-4c0 3-2 6-6 6s-7-2-7-6z" fill="${k}"/><path d="M21 32l4 0" stroke="#fff" stroke-width="1.2" opacity=".6"/>`;
  else if (a.eyes === "glasses") eyes = `${E(25, 33)}${E(39, 33)}<circle cx="25" cy="33" r="6" fill="none" stroke="${k}" stroke-width="1.8"/><circle cx="39" cy="33" r="6" fill="none" stroke="${k}" stroke-width="1.8"/><path d="M31 33h2" stroke="${k}" stroke-width="1.8"/>`;
  else if (a.eyes === "patch") eyes = `${E(25, 33)}<path d="M34 29h10v7c0 2-2 3-5 3s-5-1-5-3z" fill="${k}"/><path d="M16 24l32 8" stroke="${k}" stroke-width="1.6"/>`;
  else if (a.eyes === "stalk") eyes = `<path d="M26 26v-8M38 26v-8" stroke="${k}" stroke-width="2"/>${E(26, 17)}${E(38, 17)}`;
  else if (a.eyes === "angry") eyes = `${E(25, 34)}${E(39, 34)}<path d="M20 28l9 3M44 28l-9 3" stroke="${k}" stroke-width="2.4" stroke-linecap="round"/>`;
  else if (a.eyes === "goggles") eyes = `<rect x="16" y="27" width="32" height="11" rx="5" fill="#3a3f46" stroke="${k}" stroke-width="1.5"/><circle cx="25" cy="32.5" r="4" fill="#9fd8ff"/><circle cx="39" cy="32.5" r="4" fill="#9fd8ff"/>`;
  else if (a.eyes === "sleepy") eyes = `<path d="M21 33c2 2 6 2 8 0M35 33c2 2 6 2 8 0" stroke="${k}" stroke-width="2.4" fill="none" stroke-linecap="round"/>`;
  else if (a.eyes === "mask") eyes = `<path d="M15 30c5-4 12-3 17 0 5-3 12-4 17 0-2 6-8 8-17 5-9 3-15 1-17-5z" fill="#2b2b33"/>${E(25, 32)}${E(39, 32)}`;
  else if (a.eyes === "star") eyes = `<path d="M25 28l1.5 3.5 3.5.5-2.6 2.4.7 3.6-3.1-1.8-3.1 1.8.7-3.6-2.6-2.4 3.5-.5zM39 28l1.5 3.5 3.5.5-2.6 2.4.7 3.6-3.1-1.8-3.1 1.8.7-3.6-2.6-2.4 3.5-.5z" fill="#ffd34a" stroke="${k}" stroke-width="1"/>`;
  else eyes = `${E(25, 33)}${E(39, 33)}`;
  // Mund
  if (a.mouth === "grin") mouth = `<path d="M24 41c2 5 14 5 16 0z" fill="#fff" stroke="${k}" stroke-width="2" stroke-linejoin="round"/>`;
  else if (a.mouth === "o") mouth = `<ellipse cx="32" cy="43" rx="3" ry="3.6" fill="${k}"/>`;
  else if (a.mouth === "cat") mouth = `<path d="M27 41c2 3 5 3 5 0 0 3 3 3 5 0" stroke="${k}" stroke-width="2" fill="none" stroke-linecap="round"/>`;
  else if (a.mouth === "beak") mouth = `<path d="M27 39l5 7 5-7z" fill="#ffb02e" stroke="${k}" stroke-width="1.6" stroke-linejoin="round"/>`;
  else if (a.mouth === "grill") mouth = `<rect x="24" y="40" width="16" height="6" rx="1.5" fill="${k}"/><path d="M28 40v6M32 40v6M36 40v6" stroke="${S}" stroke-width="1.4"/>`;
  else if (a.mouth === "smirk") mouth = `<path d="M26 43c4 2 9 1 12-3" stroke="${k}" stroke-width="2.4" fill="none" stroke-linecap="round"/>`;
  else if (a.mouth === "tongue") mouth = `<path d="M25 41c3 4 11 4 14 0" stroke="${k}" stroke-width="2.2" fill="none" stroke-linecap="round"/><path d="M30 43h5v4c0 2-5 2-5 0z" fill="#ff6b8a" stroke="${k}" stroke-width="1.2"/>`;
  else mouth = `<path d="M25 41c3 4 11 4 14 0" stroke="${k}" stroke-width="2.4" fill="none" stroke-linecap="round"/>`;
  // Kopfbedeckung
  const H = {
    bubble: `<circle cx="32" cy="34" r="25" fill="rgba(160,220,255,.18)" stroke="#bfe8ff" stroke-width="2"/><path d="M16 22a20 20 0 0 1 12-9" stroke="#fff" stroke-width="2.5" fill="none" stroke-linecap="round" opacity=".7"/>`,
    antenna: `<path d="M32 18V7" stroke="${k}" stroke-width="2"/><circle cx="32" cy="6" r="3.5" fill="#ff4b6a" stroke="${k}" stroke-width="1.5"/>`,
    captain: `<path d="M14 22c4-10 32-10 36 0z" fill="#1f2a5a" stroke="${k}" stroke-width="2"/><rect x="12" y="20" width="40" height="5" rx="2" fill="#141838" stroke="${k}" stroke-width="1.5"/><circle cx="32" cy="17" r="3" fill="#ffc94a"/>`,
    bun: `<circle cx="32" cy="14" r="6" fill="#d9d9e3" stroke="${k}" stroke-width="2"/><path d="M15 30c0-12 34-12 34 0-6-5-28-5-34 0z" fill="#d9d9e3" stroke="${k}" stroke-width="2"/>`,
    mohawk: `<path d="M26 18l2-10 4 8 2-9 3 9 3-6v8z" fill="#ff4fd8" stroke="${k}" stroke-width="1.5" stroke-linejoin="round"/>`,
    tricorn: `<path d="M8 24c8-14 40-14 48 0-8-4-16 2-24 2s-16-6-24-2z" fill="#2a1a12" stroke="${k}" stroke-width="2"/><path d="M28 16l4 4 4-4" stroke="#fff" stroke-width="1.6" fill="none"/>`,
    feather: `<path d="M32 18c-4-8 2-14 8-14-2 6-4 10-8 14z" fill="#ff5a3c" stroke="${k}" stroke-width="1.5"/>`,
    straw: `<ellipse cx="32" cy="20" rx="24" ry="5" fill="#e8c46a" stroke="${k}" stroke-width="2"/><path d="M20 20c0-10 24-10 24 0z" fill="#e8c46a" stroke="${k}" stroke-width="2"/><path d="M20 18h24" stroke="#e8553c" stroke-width="3"/>`,
    sailor: `<path d="M18 22c0-9 28-9 28 0z" fill="#fff" stroke="${k}" stroke-width="2"/><rect x="16" y="20" width="32" height="4" rx="2" fill="#2b5aa8"/>`,
    bandana: `<path d="M14 28c2-12 34-12 36 0z" fill="#e8553c" stroke="${k}" stroke-width="2"/><path d="M48 24l8 6-8 2" fill="#e8553c" stroke="${k}" stroke-width="1.5"/><circle cx="24" cy="22" r="1.4" fill="#fff"/><circle cx="34" cy="20" r="1.4" fill="#fff"/>`,
    helmet: `<path d="M12 28c0-16 40-16 40 0z" fill="#5a6a2c" stroke="${k}" stroke-width="2"/><path d="M10 28h44" stroke="${k}" stroke-width="3" stroke-linecap="round"/>`,
    cap: `<path d="M15 26c0-12 34-12 34 0z" fill="#d94a3a" stroke="${k}" stroke-width="2"/><path d="M40 25h16c0 3-4 4-16 3z" fill="#b8372a" stroke="${k}" stroke-width="1.5"/>`,
    headset: `<path d="M13 34c0-24 38-24 38 0" stroke="${k}" stroke-width="3" fill="none"/><rect x="9" y="30" width="7" height="11" rx="3" fill="#3a3f46" stroke="${k}" stroke-width="1.5"/><rect x="48" y="30" width="7" height="11" rx="3" fill="#3a3f46" stroke="${k}" stroke-width="1.5"/><path d="M13 41c0 6 8 8 12 6" stroke="${k}" stroke-width="2" fill="none"/>`,
    beret: `<path d="M12 24c4-10 36-10 40 2-12-4-28-5-40-2z" fill="#3a4a2a" stroke="${k}" stroke-width="2"/><circle cx="33" cy="16" r="2" fill="${k}"/>`,
    miner: `<path d="M14 26c0-14 36-14 36 0z" fill="#ffc94a" stroke="${k}" stroke-width="2"/><circle cx="32" cy="19" r="4" fill="#fff8c4" stroke="${k}" stroke-width="1.5"/>`,
    hardhat: `<path d="M13 27c0-15 38-15 38 0z" fill="#ffc94a" stroke="${k}" stroke-width="2"/><path d="M10 27h44" stroke="${k}" stroke-width="3" stroke-linecap="round"/><path d="M32 13v8" stroke="#e8a32a" stroke-width="3"/>`,
    tophat: `<rect x="22" y="4" width="20" height="16" rx="2" fill="#1a1a22" stroke="${k}" stroke-width="2"/><path d="M14 20h36" stroke="${k}" stroke-width="3.5" stroke-linecap="round"/><rect x="22" y="14" width="20" height="3" fill="#d94a3a"/>`,
    beanie: `<path d="M15 28c0-16 34-16 34 0z" fill="#4aa8ff" stroke="${k}" stroke-width="2"/><circle cx="32" cy="11" r="4" fill="#ffc94a" stroke="${k}" stroke-width="1.5"/><path d="M15 26h34" stroke="#2a78c8" stroke-width="3"/>`,
  };
  hat = H[a.hat] || "";
  const back = a.hat === "bubble" ? "" : "";
  return `<svg viewBox="-5 -6 74 74" aria-hidden="true">${back}${ears}${head}${extra}${eyes}${mouth}${hat}</svg>`;
}
const avKey = () => "welten-av-" + WORLD_ID;
let avIdx = 0; try { avIdx = Math.max(0, Math.min(7, +localStorage.getItem(avKey()) || 0)); } catch (e) {}
const avMine = () => avSet(WORLD_ID)[avIdx];
const avHtml = (a, size, color) => `<span class="av" style="width:${size}px;height:${size}px;${color ? `--avc:${color}` : ""}">${avSvg(a)}</span>`;
// Avatar eines anderen Spielers: players/{uid}/av/{welt} = Index
const avOf = p => { const i = p && p.av && p.av[WORLD_ID]; return typeof i === "number" ? avSet(WORLD_ID)[i] : null; };
(function setupAvatars() {
  const rank = document.querySelector(".metarow .rank");
  if (rank) { rank.insertAdjacentHTML("afterbegin", `<button type="button" class="av av-me" id="avMe" aria-label="Pilotenbild wählen" title="Pilotenbild wählen">${avSvg(avMine())}</button>`); $("avMe").addEventListener("click", openAvPick); }
  document.body.insertAdjacentHTML("beforeend", `<div class="bonus" id="avPick" hidden role="dialog" aria-modal="true" aria-labelledby="avTitle" style="z-index:265"><div class="bonus-card">
    <h2 id="avTitle" style="margin:0 0 4px">Pilotenbild wählen</h2><p class="ol-info">Dein Bild erscheint in der Rangleiste, bei Freunden, in der Crew und im Live-Feed.</p>
    <div class="av-grid" id="avGrid"></div><div class="ar-row"><span></span><button type="button" class="bbtn ghost" id="avClose">Fertig</button></div></div></div>`);
  $("avClose").addEventListener("click", () => { $("avPick").hidden = true; });
  $("avGrid").addEventListener("click", e => { const b = e.target.closest("button[data-i]"); if (!b) return; avIdx = +b.dataset.i;
    try { localStorage.setItem(avKey(), String(avIdx)); } catch (er) {} $("avMe").innerHTML = avSvg(avMine()); renderAvPick();
    try { sfx.upgrade(); burstAt(b, 24, ["#ffc94a", "#ffffff"], .7); } catch (er) {}
    try { if (OL.db) OL.db.ref(`players/${OL.uid}/av/${WORLD_ID}`).set(avIdx); } catch (er) {} });
  window.addEventListener("keydown", e => { if (!$("avPick").hidden && e.key === "Escape") { $("avPick").hidden = true; e.preventDefault(); e.stopImmediatePropagation(); } }, true);
})();
function renderAvPick() { $("avGrid").innerHTML = avSet(WORLD_ID).map((a, i) => `<button type="button" data-i="${i}" aria-pressed="${i === avIdx}">${avHtml(a, 72)}<span>${a.n}</span><small>${a.d}</small></button>`).join(""); }
function openAvPick() { renderAvPick(); $("avPick").hidden = false; try { sfx.click(); } catch (e) {} }
'''
