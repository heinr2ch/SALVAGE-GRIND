# Teil 2: Papagei, Floß, Meer
PARROT_SVG = '''    <svg viewBox="0 0 80 92" data-mood="normal" id="bipSvg" aria-hidden="true">
      <ellipse class="bip-thrust" cx="40" cy="88" rx="14" ry="2.6" fill="#7fc8ff" opacity=".35"/>
      <path d="M33 74 q-6 10 -3 17 q4 -5 6 -14z" fill="#2f8fff"/><path d="M40 75 q0 11 4 16 q2 -7 -1 -16z" fill="#ffc65a"/><path d="M47 74 q6 10 3 17 q-4 -5 -6 -14z" fill="#2f8fff"/>
      <path d="M40 16 q-3 -9 3 -13 q-.5 6 2.5 9 q-1 -6 4 -8 q-2 5 0 9z" fill="#ffc65a"/>
      <circle class="bip-ant" cx="44" cy="3.5" r="2.6" fill="#ff7a59"/>
      <g class="bip-arm l"><path d="M24 52 q-15 6 -12 26 q9 -3 13 -15z" fill="#2f8fff" stroke="#1b5aa8" stroke-width="1.4"/><path d="M15 68 q4 -2 8 -8 M14 74 q5 -3 9 -9" stroke="#ffc65a" stroke-width="1.6" fill="none" stroke-linecap="round"/></g>
      <g class="bip-arm r"><path d="M56 52 q15 6 12 26 q-9 -3 -13 -15z" fill="#2f8fff" stroke="#1b5aa8" stroke-width="1.4"/><path d="M65 68 q-4 -2 -8 -8 M66 74 q-5 -3 -9 -9" stroke="#ffc65a" stroke-width="1.6" fill="none" stroke-linecap="round"/></g>
      <ellipse cx="40" cy="62" rx="17" ry="20" fill="#ef4a32" stroke="#a52a1a" stroke-width="1.8"/>
      <ellipse cx="40" cy="66" rx="9.5" ry="12" fill="#ff8a5c" opacity=".55"/>
      <path class="bip-heart" d="M40 72 l-4 -4 a2.6 2.6 0 0 1 4 -3.4 a2.6 2.6 0 0 1 4 3.4 z" fill="#ffd34a"/>
      <path d="M33 82 l-2 5 M35 82 l0 5 M45 82 l0 5 M47 82 l2 5" stroke="#ffb347" stroke-width="2" stroke-linecap="round"/>
      <circle cx="40" cy="33" r="19" fill="#ff5a3c" stroke="#a52a1a" stroke-width="2"/>
      <ellipse cx="30" cy="31" rx="8" ry="9" fill="#fff3e6"/><ellipse cx="50" cy="31" rx="8" ry="9" fill="#fff3e6"/>
      <path d="M26 25 q2 -1 3 1 M30 23 q2 -1 3 1 M47 23 q2 -1 3 1 M51 25 q2 -1 3 1" stroke="#e3c9b5" stroke-width=".9" fill="none"/>
      <path d="M34.5 37 q5.5 -5 11 0 q-.5 9 -5.5 12 q-5 -3 -5.5 -12z" fill="#ffd34a" stroke="#8a5a08" stroke-width="1.3" stroke-linejoin="round"/>
      <path d="M36.5 39 q3.5 -2 7 0" stroke="#8a5a08" stroke-width="1" fill="none"/>
      <circle cx="17" cy="42" r="3" fill="#ff9ac6" opacity=".55"/><circle cx="63" cy="42" r="3" fill="#ff9ac6" opacity=".55"/>
      <g class="m m-normal"><g class="bip-eyes"><ellipse cx="31" cy="31" rx="3.4" ry="4.4" fill="#10202a"/><ellipse cx="49" cy="31" rx="3.4" ry="4.4" fill="#10202a"/><circle cx="32.2" cy="29.4" r="1.2" fill="#fff"/><circle cx="50.2" cy="29.4" r="1.2" fill="#fff"/></g></g>
      <g class="m m-happy"><path d="M26.5 32 q4.5 -6 9 0 M44.5 32 q4.5 -6 9 0" stroke="#10202a" stroke-width="2.6" fill="none" stroke-linecap="round"/><path d="M38 47 q2 3 4 0" stroke="#c0392b" stroke-width="1.6" fill="none"/></g>
      <g class="m m-excited"><path d="M31 25 l1.6 3.6 3.9 .4 -2.9 2.6 .9 3.8 -3.5 -2 -3.5 2 .9 -3.8 -2.9 -2.6 3.9 -.4z M49 25 l1.6 3.6 3.9 .4 -2.9 2.6 .9 3.8 -3.5 -2 -3.5 2 .9 -3.8 -2.9 -2.6 3.9 -.4z" fill="#ffb347" stroke="#8a5a08" stroke-width=".6"/><path d="M36 47 q4 6 8 0 z" fill="#c0392b"/></g>
      <g class="m m-sad"><path d="M25.5 26 l7 3 M54.5 26 l-7 3" stroke="#10202a" stroke-width="2.2" stroke-linecap="round"/><ellipse cx="31" cy="33" rx="2.8" ry="3.2" fill="#10202a"/><ellipse cx="49" cy="33" rx="2.8" ry="3.2" fill="#10202a"/><path class="bip-tear" d="M53 37 q2 3 0 5 q-2 -2 0 -5z" fill="#7fc8ff"/></g>
      <g class="m m-wow"><circle cx="31" cy="31" r="5" fill="#10202a"/><circle cx="49" cy="31" r="5" fill="#10202a"/><circle cx="32.6" cy="29.2" r="1.8" fill="#fff"/><circle cx="50.6" cy="29.2" r="1.8" fill="#fff"/><ellipse cx="40" cy="48" rx="3" ry="2.6" fill="#c0392b"/></g>
    </svg>
'''

BIP_NEW = r'''const BIP = {
  hello: [["happy", "Krah! Hallo Kapitän! Ich bin <b>Koko</b>, dein Bordpapagei. Ich drück die Daumen. Also ... die Krallen."], ["happy", "Koko meldet sich zum Dienst! Ich hab extra die Federn geputzt."]],
  small: [["happy", "Ein kleiner Fang ist auch ein Fang!"], ["happy", "Plitsch! Ich mag dieses Geräusch."], ["happy", "Jede Muschel zählt. Ich zähl mit!"]],
  good: [["happy", "Schöner Fang! Ich mach einen kleinen Freudentanz auf dem Mast."], ["happy", "Das lief gut! Merkst du, wie das Floß lächelt?"], ["excited", "Krah! Gute Bergung!"]],
  big: [["excited", "WOAH! Das war eine <b>große Bergung</b>! Meine Federn stehen ab!"], ["excited", "Ich hab das gesehen! Das war richtig stark!"], ["wow", "Sag mal ... bist du Profi-Schiffbrüchiger?"]],
  mega: [["wow", "MEGA! Ich ... ich brauch kurz einen Moment. Mir ist ganz schwindelig!"], ["excited", "Das erzähl ich allen Möwen im Umkreis!"]],
  laser: [["excited", "Die Möwe hat geliefert! Ein Rettungsring!"], ["happy", "Rettungsring! Der passt zu allem. Wie ich."]],
  streak3: [["excited", "Drei in Folge! Du hast den Wind im Rücken."], ["happy", "Strähne läuft! Ich spür die Sonne bis hierher."]],
  streak5: [["wow", "Fünf in Folge?! Ich hab mit allen Krallen nachgezählt. Stimmt wirklich!"]],
  broke: [["normal", "Strähne vorbei. War trotzdem schön, solange sie lief."], ["normal", "Na ja, Strähnen kommen und gehen. Wie Ebbe und Flut."]],
  dry: [["sad", "Gerade läuft's zäh, ich weiß. Das Meer hat leider kein Gedächtnis, aber ich bin trotzdem hier."], ["sad", "Puh, Flaute. Wenn du magst, schau dir das Floß an. Da gibt's lustige Sachen."], ["normal", "Kopf hoch, Kapitän. Muscheln sind nur Muscheln, Spaß ist das, was zählt."], ["sad", "Pech gehabt. Ich halt dir den Flügel."]],
  fs: [["excited", "Freifahrten! Festhalten!"], ["excited", "Flaschenpost gefunden! Jetzt wird's spannend!"]],
  starFirst: [["wow", "Da treibt ein <b>Fass</b> vorbei! Schnell, klick drauf, dann holt der Haken es an Bord. Da ist Bernstein drin!"]],
  star: [["excited", "Treibgut voraus! Haken bereit!"], ["happy", "Da schwimmt was! Schnapp es dir!"]],
  sticky: [["wow", "Ein fester Rettungsring! Der bleibt die ganze Runde liegen!"], ["excited", "Die Möwe hilft! Jetzt wird's richtig gut."]],
  fsend: [["happy", "Freifahrten vorbei. Hat Spaß gemacht!"], ["happy", "Das war eine schöne Rückenwind-Fahrt!"]],
  bonusGood: [["excited", "Bonus geschafft! Das war Teamarbeit. Ich hab laut gekräht."], ["happy", "Gut gemacht im Bonusspiel!"]],
  bonusMeh: [["normal", "Nicht der große Fang, aber Bonusspiele sind immer ein kleines Abenteuer."]],
  jackpot: [["wow", "DER PIRATENSCHATZ! Ich ... ich hab keine Worte. Nur Krächzer. Krah! KRAAAH!"]],
  upgrade: [["happy", "Schick! Das Floß sieht gleich zufriedener aus."], ["happy", "Gute Investition, Kapitän!"]],
  bigUpgrade: [["excited", "Großes Upgrade! Schau dir dieses Floß an! Ich bin ganz stolz."], ["wow", "Ist das noch unser alter Bretterhaufen? Kaum wiederzuerkennen!"]],
  rank: [["excited", "Beförderung! Darf ich dich jetzt <b>Käpt'n</b> nennen?"], ["happy", "Neuer Rang! Ich hab dir eine Muschelkette gebastelt. In Gedanken."]],
  mission: [["happy", "Auftrag erledigt! Abgehakt und mit Salz versiegelt."], ["happy", "Wieder einer geschafft. Die Strandgilde ist zufrieden."]],
  scrap: [["sad", "Oh nein, wir mussten ein Teil verkaufen. Das wird wieder, versprochen."], ["sad", "Autsch. Aber hey, wir schwimmen noch!"]],
  lost: [["sad", "Das Floß ist weg ... Aber du hast ein neues und mich. Wir schaffen das zusammen."]],
  scratchWin: [["excited", "Gerubbelt und gewonnen! Hast du goldene Finger?"], ["happy", "Rubbel-Glück! Herzlichen Glückwunsch!"]],
  scratchLoss: [["normal", "Diesmal nix. Aber das Rubbeln selbst macht schon Spaß, oder?"], ["sad", "Leer. Das Los wollte wohl nicht teilen."]],
  found: [["happy", "Oh, was entdeckt! Du kennst dein Floß immer besser."], ["wow", "Huch! Das wusste nicht mal ich."]],
  session: [["normal", "Wir sind schon eine ganze Weile auf See. Kurz strecken und was trinken? Ich warte hier."], ["normal", "Kleine Erinnerung von Koko: Pausen gehören zu jeder guten Seefahrt."]],
  idle: [["normal", "Ich putz solange meine Federn."], ["happy", "Psst ... klick mal auf das Segel."], ["happy", "Unsicher, was etwas macht? Klick auf das <b>?</b> neben mir, dann erkläre ich alles, worüber du fährst."], ["normal", "Ich zähle Wellen. Bin bei 4.812."]],
  crew: [["excited", "Neue Crew! Endlich jemand zum Quatschen außer mir."], ["happy", "Willkommen an Bord! Ich hab dir einen Platz auf der Planke freigehalten."]],
  paint: [["happy", "Ooh, schicke Farbe! Steht dem Floß richtig gut."]],
  expedGo: [["normal", "Gute Fahrt, Floß! Ich pass hier solange auf."], ["happy", "Expedition gestartet. Ich zähle die Sekunden. Laut."]],
  expedBack: [["excited", "Das Floß ist zurück! Und es hat was mitgebracht!"]],
  sector: [["wow", "Neue Insel in Sicht! Alles sieht so anders aus. Ich bin ganz aufgeregt."], ["excited", "Land in Sicht! Ich hab nur ein bisschen gekreischt."]],
  album: [["wow", "Ein Sammelstück! Das kommt ins Regal. Ganz vorne."]],
  ach: [["excited", "Erfolg freigeschaltet! Ich mal ein Bild davon in den Sand."], ["happy", "Krah! Ein neuer Erfolg. Du wirst immer besser."]],
  daily: [["happy", "Tagesbonus abgeholt! Schön, dass du wieder da bist."]],
  gambleWin: [["wow", "Mutig! Und es hat sich gelohnt!"], ["excited", "Richtig geraten! Meine Federn kribbeln."]],
  ladderWin: [["excited", "Hoch hinaus! Mir wird schon schwindelig. Und ich kann fliegen!"], ["wow", "So weit oben! Nicht runterschauen, Kapitän!"]],
  ladderTop: [["wow", "GANZ OBEN! Hundertfach! Ich fasse es nicht!"]],
  ladderLoss: [["sad", "Abgestürzt ... Die Leiter war heute wackelig."], ["sad", "Platsch. Aber hey, der Ausblick war schön."]],
  gambleLoss: [["sad", "Oh je. Das Risiko war echt 50 zu 50, diesmal leider gegen uns."]],
  dustFirst: [["wow", "Oh! Dein erster <b>Bernstein</b>! Der ist super selten. In der Kräuterhütte kannst du ihn eintauschen."]],
  boostOn: [["excited", "Trank wirkt! Jetzt aber schnell auswerfen, die Uhr tickt!"], ["happy", "Ui, das kribbelt im Gefieder. Boost aktiv!"]],
  boostEnd: [["normal", "Der Boost ist abgelaufen. War schön, solange er hielt."]],
  charging: [["normal", "Ich sammle schon mal Glück für dich. Siehst du den Balken neben mir?"], ["happy", "Halbe Glücksladung! Ich pfeif extra laut."]],
  boostReady: [["wow", "KOKO-BOOST! Volle Glücksladung! Der nächste Wurf gewinnt garantiert!"], ["excited", "Genug Pech gehabt! Ich hab dir Glück ins Netz gepustet. Nächster Wurf gewinnt!"]],
  boostWin: [["excited", "Siehste! Auf Koko ist Verlass!"], ["happy", "Koko-Boost geliefert! Gern geschehen, Kapitän."]],
  pet: [["happy", "Hihi! Das kitzelt!"], ["happy", "Krah! Danke!"], ["excited", "Noch mal! Noch mal!"], ["happy", "Ich mag dich auch, Kapitän."], ["wow", "Vorsicht, frisch geputzt!"]],
};
'''

CATS_NEW = r'''const CATS = [
  { id: "hull", name: "Floß", color: "#d9b27c", tiers: ["Morsch", "Gezurrt", "Verstärkt", "Doppelrumpf"],
    icon: `<svg viewBox="0 0 24 24"><path d="M3 13h18l-2 5H5z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M7 13v5M12 13v5M17 13v5" stroke="currentColor" stroke-width="1.6"/><path d="M2 21q2.5-1.5 5 0t5 0 5 0 5 0" stroke="currentColor" stroke-width="1.6" fill="none"/></svg>`,
    effect: s => `Notverkauf erstattet ${30 + 5 * s} % des Teilwerts.` },
  { id: "engine", name: "Segel", color: "#ff9a3c", tiers: ["Paddel", "Lumpensegel", "Großsegel", "Zweimaster"],
    icon: `<svg viewBox="0 0 24 24"><path d="M11 3v16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path d="M12 4q8 6 7 12h-7z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M10 7q-5 4-5 9h5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M3 20h18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>`,
    effect: s => {
      const un = [[1, "Auto 10"], [2, "Turbo"], [4, "Auto 25"], [7, "Auto 50"]];
      const have = un.filter(u => s >= u[0]).map(u => u[1]);
      const next = un.find(u => s < u[0]);
      return `${have.length ? "Frei: " + have.join(", ") + "." : "Noch nichts freigeschaltet."}${next ? ` Nächstes: ${next[1]} ab Stufe ${next[0]}.` : ""}`;
    } },
  { id: "scanner", name: "Ausguck", color: "#3fe0c5", tiers: ["Stock", "Fernrohr", "Krähennest", "Leuchtfeuer"],
    icon: `<svg viewBox="0 0 24 24"><path d="M4 16l12-7 2 3.5-12 7z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M16 9l3-1.7 2 3.4-3 1.8M8 18l-2 4M12 16l1 6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" fill="none"/></svg>`,
    effect: s => `Liniengewinne +${(0.2 * s).toFixed(1).replace(".", ",")} %.` },
  { id: "cargo", name: "Lager", color: "#ffc94a", tiers: ["Leer", "Kiste", "Fässer", "Vorratshütte"],
    icon: `<svg viewBox="0 0 24 24"><rect x="3" y="9" width="12" height="11" rx="1" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 14h12M9 9v11" stroke="currentColor" stroke-width="1.6"/><ellipse cx="18.5" cy="15" rx="3" ry="5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M15.6 13h5.8M15.6 17h5.8" stroke="currentColor" stroke-width="1.2"/></svg>`,
    effect: s => `Bonusspiel-Gewinne +${(0.6 * s).toFixed(1).replace(".", ",")} %.` },
  { id: "reactor", name: "Feuerstelle", color: "#ff7a59", tiers: ["Kalt", "Glimmt", "Grill", "Kombüse"],
    icon: `<svg viewBox="0 0 24 24"><path d="M12 3c3 4 5 6 5 9.5a5 5 0 0 1-10 0c0-2 1-3.5 2-5 .5 2 1.5 3 3 3-1-3 0-5.5 0-7.5z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M4 21l16-3M4 18l16 3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>`,
    effect: s => { const caps = [10, 10, 10, 25, 25, 25, 50, 50, 50, 100]; const n = [3, 6, 9].find(x => s < x); return `Max. Einsatz ${caps[s]}.${n ? ` ${caps[n]} ab Stufe ${n}.` : ""}`; } },
];
'''

CLASS_NEW = 'const CLASS_NAMES = [[1, "Wrack", "#ff6b7a"], [4, "Bretterhaufen", "#ff9a3c"], [8, "Floß", "#ffc94a"], [12, "Segelfloß", "#3fe0c5"], [14, "Hausfloß", "#7fc8ff"], [15, "Legende", "#ff7a59"]];'

RAFT_SVG = r'''/* Floßgrafik: jede Kategorie hat 4 sichtbare Ausbaustufen, Zwischenstufen zeigen kleine Lichter. Wasserlinie bei y = 112. */
const VB = { x: 48, y: 2, w: 304, h: 152 };
const WL = 112;
const GEO = [{ l: 120, t: 104, b: 118, n: 280 }, { l: 104, t: 103, b: 119, n: 300 }, { l: 92, t: 102, b: 120, n: 318 }, { l: 80, t: 100, b: 122, n: 336 }];
function hullPath(H, g) {
  const { l, t, b, n } = g, m = (t + b) / 2;
  return `M${l},${t} L${n - 7},${t} Q${n + 1},${t} ${n + 2},${m} Q${n + 1},${b} ${n - 8},${b} L${l + 4},${b} Q${l - 3},${b} ${l - 3},${m} Q${l - 3},${t} ${l},${t} Z`;
}
function partAnchors(L) {
  const H = Math.min(3, Math.floor(L.hull / 3)), g = GEO[H], mx = g.l + Math.round((g.n - g.l) * .28);
  return { hull: [(g.l + g.n) / 2 - 30, g.b + 4], engine: [mx + 14, g.t - 46], scanner: [186, g.t - 44], cargo: [236, g.t - 16], reactor: [205, g.t - 8] };
}
function shipSVG(L, k = "a") {
  const T = id => Math.min(3, Math.floor(L[id] / 3)), lo = id => L[id] >= 9 ? 3 : L[id] % 3;
  const H = T("hull"), E = T("engine"), S = T("scanner"), C = T("cargo"), R = T("reactor");
  const g = GEO[H], { l, t, b, n } = g, hp = hullPath(H, g), m = (t + b) / 2;
  const mx = l + Math.round((n - l) * .28), px = n - 22;
  const lights = (x, y, cnt, col, dx = 8) => Array.from({ length: cnt }, (_, i) => `<circle class="blink d${i + 1}" cx="${x + i * dx}" cy="${y}" r="2" fill="${col}"/>`).join("");
  const wood = ["#6b5a48", "#8a5e34", "#9a6a3a", "#a8743f"][H], dark = ["#3a3128", "#4a3018", "#52371b", "#583b1c"][H], light = ["#8f7f6c", "#c99a62", "#d9aa6c", "#e6b877"][H];
  let back = "", hull = "", det = "", front = "";

  /* ----- Schwimmkörper unter dem Floß ----- */
  if (H === 2) back += [l + 24, (l + n) / 2 - 10, n - 46].map(x => `<rect x="${x}" y="${b - 6}" width="30" height="13" rx="6.5" fill="#2a6fb0" stroke="#173f66" stroke-width="1.4"/><path d="M${x + 9},${b - 6} v13 M${x + 21},${b - 6} v13" stroke="#173f66" stroke-width="1.2"/>`).join("");
  if (H === 3) back += `<path d="M${l - 6},${b - 2} Q${(l + n) / 2},${b + 16} ${n + 6},${b - 2} Q${n - 4},${b + 6} ${(l + n) / 2},${b + 7} Q${l + 4},${b + 6} ${l - 6},${b - 2} Z" fill="#4a2e14" stroke="#2a180a" stroke-width="1.6"/>
    <path d="M${l + 20},${b + 3} Q${(l + n) / 2},${b + 12} ${n - 20},${b + 3}" stroke="#7a5228" stroke-width="1.2" fill="none"/>`;

  /* ----- Segel und Antrieb ----- */
  if (E === 0) back += `<path d="M${l + 18},${t - 18} L${l - 22},${WL + 9}" stroke="#8a6a45" stroke-width="3" stroke-linecap="round"/><ellipse cx="${l - 25}" cy="${WL + 12}" rx="4" ry="9" transform="rotate(-55 ${l - 25} ${WL + 12})" fill="#9a7a50" stroke="#5a4028" stroke-width="1.2"/>`;
  if (E >= 1) {
    const mh = [0, 56, 78, 84][E];
    back += `<path d="M${mx},${t} V${t - mh}" stroke="#6e4f30" stroke-width="${E === 1 ? 3 : 3.6}" stroke-linecap="round"/>`;
    if (E === 1) back += `<path class="sail" d="M${mx + 2},${t - 52} Q${mx + 30},${t - 40} ${mx + 34},${t - 12} L${mx + 2},${t - 10} Z" fill="#d9c9a8" stroke="#8a7a5a" stroke-width="1.4" stroke-linejoin="round"/>
      <rect x="${mx + 8}" y="${t - 40}" width="9" height="8" fill="#b5634a" opacity=".85"/><rect x="${mx + 16}" y="${t - 24}" width="10" height="7" fill="#5a7a9a" opacity=".85"/>
      <path d="M${mx + 8},${t - 40} h9 v8 h-9z M${mx + 16},${t - 24} h10 v7 h-10z" fill="none" stroke="#f2ead8" stroke-width=".7" stroke-dasharray="1.5 1.5"/><path d="M${mx + 24},${t - 46} l4,7 l-3,3" stroke="#8a7a5a" stroke-width="1" fill="none"/>`;
    if (E >= 2) back += `<path d="M${mx},${t - 12} H${mx + 62}" stroke="#6e4f30" stroke-width="2.4" stroke-linecap="round"/>
      <path class="sail" d="M${mx + 2},${t - 76} Q${mx + 48},${t - 48} ${mx + 60},${t - 14} L${mx + 2},${t - 14} Z" fill="#f4ecd8" stroke="#9a8a6a" stroke-width="1.4" stroke-linejoin="round"/>
      <path d="M${mx + 2},${t - 40} Q${mx + 28},${t - 36} ${mx + 50},${t - 32} M${mx + 2},${t - 26} Q${mx + 30},${t - 22} ${mx + 56},${t - 20}" stroke="#ff7a59" stroke-width="2.4" fill="none" opacity=".8"/>
      <path class="sail" d="M${mx},${t - mh} l14,4 l-14,4 z" fill="#ff7a59"/>`;
    if (E === 3) back += `<path class="sail" d="M${mx + 3},${t - 80} L${n - 16},${t - 4} L${mx + 70},${t - 6} Z" fill="#f4ecd8" opacity=".92" stroke="#9a8a6a" stroke-width="1.2" stroke-linejoin="round"/>
      <path d="M${mx + 3},${t - 80} L${n - 16},${t - 4}" stroke="#6e4f30" stroke-width="1"/>
      <rect x="${l - 14}" y="${t - 8}" width="14" height="12" rx="3" fill="#3a4250" stroke="#8792a8" stroke-width="1.4"/><path d="M${l - 8},${t + 4} V${WL + 6}" stroke="#5a6272" stroke-width="2.4"/>
      <circle class="blink" cx="${mx}" cy="${t - mh - 3}" r="2.4" fill="#ffe39a"/>`;
  }
  front += lights(l + 4, t - 4, lo("engine"), "#ff9a3c", 7);

  /* ----- Floß (Rumpf) ----- */
  const fills = [wood, wood, wood, "url(#hullG)"];
  hull += `<clipPath id="hc-${k}"><path d="${hp}"/></clipPath>`;
  hull += `<g style="filter:${paintFilter()}">`;
  if (H === 0) {
    const segs = [[l, l + 50, 1], [l + 56, l + 108, -1], [l + 113, n, 2]];
    segs.forEach(([a, z, yo], i) => {
      hull += `<path d="M${a + 6},${t + yo - 6} L${z + 2},${t + yo - 6 + (i === 1 ? 2 : 0)} L${z - 2},${t + yo} L${a + 2},${t + yo} Z" fill="${light}" opacity=".9"/>
        <path d="M${a + 2},${t + yo} L${z - 2},${t + yo} L${z},${b + yo} L${a},${b + yo} Z" fill="${wood}" stroke="${dark}" stroke-width="1.6" stroke-linejoin="round"/>
        <path d="M${a + 5},${m + yo} H${z - 4}" stroke="${dark}" stroke-width="1"/>
        <ellipse cx="${a + 2}" cy="${m + yo}" rx="2.4" ry="${(b - t) / 2 - 1}" fill="${light}" stroke="${dark}" stroke-width="1"/>`;
    });
    hull += `<path d="M${l + 48},${m} q4,-3 9,2 M${l + 106},${m + 1} q3,3 8,-1" stroke="#b8a070" stroke-width="1.6" fill="none"/><path d="M${l + 30},${t - 2} l5,-3 M${l + 80},${t - 4} l4,-4" stroke="#5a4a3a" stroke-width="1.4"/>`;
  } else {
    hull += `<path d="M${l + 6},${t - 6} L${n - 2},${t - 6} L${n - 7},${t} L${l},${t} Z" fill="${light}" stroke="${dark}" stroke-width="1.2" stroke-linejoin="round"/>`;
    for (let x = l + 12; x < n - 6; x += 13) hull += `<path d="M${x},${t} L${x + 6},${t - 6}" stroke="${dark}" stroke-width="1" opacity=".7"/>`;
    hull += `<path d="${hp}" fill="${fills[H]}" stroke="${dark}" stroke-width="1.8" stroke-linejoin="round"/>`;
    det += `<path d="M${l},${m} H${n}" stroke="${dark}" stroke-width="1.1"/>`;
    for (let x = l + 30; x < n - 14; x += 34) det += `<path d="M${x},${t} v${b - t} M${x + 4},${t} v${b - t}" stroke="#d9c49a" stroke-width="1.6"/><path d="M${x - 1},${t + 3} l6,4 M${x - 1},${b - 6} l6,4" stroke="#8a7650" stroke-width="1"/>`;
    det += `<text x="${l + 10}" y="${b - 3}" font-family="JetBrains Mono, monospace" font-size="4.2" font-weight="700" fill="${dark}" opacity=".8">WERFT HEINR2CH</text>
      <text x="${n - 44}" y="${m + 3}" font-family="Fredoka, sans-serif" font-size="7.5" font-weight="700" fill="#f2ead8" opacity=".85">SOS-7</text>`;
    if (H === 3) det += `<path d="M${l},${t + 4} H${n - 4}" stroke="#ffe39a" stroke-width="1" opacity=".5"/>`;
  }
  hull += `<g clip-path="url(#hc-${k})">${det}${decalSVG(g)}<path d="${hp}" fill="url(#shadeG)"/><rect class="hsheen" x="${l - 90}" y="${t - 10}" width="70" height="${b - t + 20}" fill="url(#sheenG)" opacity=".5"/></g></g>`;
  front += lights(l + 14, b + 4, lo("hull"), "#d9b27c");

  /* ----- Reling ----- */
  if (H >= 2) {
    const posts = []; for (let x = l + 6; x <= n - 40; x += H === 3 ? 22 : 30) posts.push(x);
    front += posts.map(x => `<path d="M${x},${t - 3} V${t - 15}" stroke="${dark}" stroke-width="2"/>`).join("") +
      (H === 3 ? `<path d="M${posts[0]},${t - 15} H${posts[posts.length - 1]}" stroke="${light}" stroke-width="2.4"/>` : `<path d="M${posts[0]},${t - 13} Q${(posts[0] + posts[posts.length - 1]) / 2},${t - 9} ${posts[posts.length - 1]},${t - 13}" stroke="#d9c49a" stroke-width="1.3" fill="none"/>`);
    if (H === 3) front += `<circle class="blink" cx="${posts[0]}" cy="${t - 18}" r="2.4" fill="#ffd27a"/><circle class="blink d2" cx="${posts[posts.length - 1]}" cy="${t - 18}" r="2.4" fill="#ffd27a"/>`;
  }

  /* ----- Ausguck ----- */
  const sx = 186;
  if (S === 0) front += `<path d="M${sx},${t - 2} L${sx + 2},${t - 26}" stroke="#7a5a3a" stroke-width="2.4" stroke-linecap="round"/><path class="sail" d="M${sx + 2},${t - 26} l11,3 l-9,6 z" fill="#c9b48a"/>`;
  if (S >= 1) { const ph = [0, 36, 56, 64][S]; front += `<path d="M${sx},${t - 2} V${t - ph}" stroke="#6e4f30" stroke-width="2.8" stroke-linecap="round"/><path d="M${sx - 6},${t - 2} L${sx},${t - 16} L${sx + 6},${t - 2}" stroke="#6e4f30" stroke-width="1.4" fill="none"/>`; }
  if (S === 1) front += `<g transform="rotate(-18 ${sx} ${t - 36})"><rect x="${sx - 2}" y="${t - 39}" width="18" height="5" rx="1.5" fill="#c9952e" stroke="#7a5608" stroke-width="1"/><rect x="${sx + 13}" y="${t - 40}" width="5" height="7" rx="1" fill="#ffd34a"/></g>`;
  if (S >= 2) front += `<rect x="${sx - 9}" y="${t - 58}" width="18" height="11" rx="2" fill="#8a5e34" stroke="#4a3018" stroke-width="1.4"/><path d="M${sx - 9},${t - 54} h18 M${sx - 9},${t - 50} h18" stroke="#4a3018" stroke-width="1"/>`;
  if (S === 2) front += `<path class="sail" d="M${sx},${t - 58} V${t - 70} l12,3 l-12,4" fill="#ff7a59" stroke="#6e4f30" stroke-width="1.2"/>`;
  if (S === 3) front += `<polygon class="cone" points="${sx},${t - 66} ${n + 70},${t - 104} ${n + 70},${t - 34}" fill="#ffe39a" opacity=".18"/>
    <rect x="${sx - 5}" y="${t - 72}" width="10" height="12" rx="2" fill="#2a3240" stroke="#ffd27a" stroke-width="1.4"/><circle class="pulse" cx="${sx}" cy="${t - 66}" r="3.6" fill="#ffe39a" filter="url(#glow)"/>
    <circle class="ping" cx="${sx}" cy="${t - 66}" r="6" fill="none" stroke="#ffe39a" stroke-width="1.2"/><path d="M${sx - 6},${t - 72} l6,-5 l6,5z" fill="#6e4f30"/>`;
  front += lights(sx + 9, t - 8, lo("scanner"), "#3fe0c5", 6);

  /* ----- Feuerstelle ----- */
  const rx = 205, ry = t - 2;
  const stones = `${[-9, -4.5, 0, 4.5, 9].map(d => `<ellipse cx="${rx + d}" cy="${ry}" rx="3" ry="2.2" fill="#8a8f9c" stroke="#4a4f5c" stroke-width=".8"/>`).join("")}`;
  if (R === 0) front += `<ellipse cx="${rx}" cy="${ry}" rx="9" ry="2.6" fill="#2a2420"/>${stones}<circle class="flick" cx="${rx - 1}" cy="${ry - 2}" r="1.6" fill="#ff5a3c"/>`;
  if (R >= 1 && R <= 2) front += `<path class="flame" d="M${rx},${ry - (R === 2 ? 20 : 15)} q${R === 2 ? 8 : 6},9 0,${R === 2 ? 17 : 13} q-${R === 2 ? 8 : 6},-6 0,-${R === 2 ? 17 : 13}z" fill="#ff9a3c"/><path class="flame d2" d="M${rx},${ry - (R === 2 ? 12 : 9)} q3.5,5 0,9 q-3.5,-3.5 0,-9z" fill="#ffe08a"/>${stones}`;
  if (R === 2) front += `<path d="M${rx - 12},${ry - 9} H${rx + 12} M${rx - 11},${ry - 9} V${ry} M${rx + 11},${ry - 9} V${ry}" stroke="#3a3f4a" stroke-width="1.4"/><path d="M${rx - 8},${ry - 11} q8,-4 14,0 l3,-2 v4 l-3,-2 q-6,4 -14,0z" fill="#7fc8ff" stroke="#3a5a7a" stroke-width=".8"/>`;
  if (R === 3) front += `<rect x="${rx - 11}" y="${ry - 16}" width="22" height="16" rx="3" fill="#7a6a5a" stroke="#3a3028" stroke-width="1.4"/><rect x="${rx - 6}" y="${ry - 9}" width="12" height="7" rx="2" fill="#2a1a10"/><path class="flame" d="M${rx},${ry - 8} q4,3 0,5 q-4,-2 0,-5z" fill="#ff9a3c"/>
    <rect x="${rx + 5}" y="${ry - 30}" width="5" height="14" fill="#5a4a3a"/><ellipse cx="${rx - 4}" cy="${ry - 18}" rx="7" ry="2.4" fill="#3a3f4a"/><path d="M${rx - 10},${ry - 18} v-5 h12 v5" fill="#4a505c"/>
    <path class="pulse" d="M${rx - 6},${ry - 26} q2,-4 0,-7 M${rx - 2},${ry - 27} q2,-4 0,-7" stroke="#ffffff" stroke-width="1.2" fill="none" opacity=".6"/>`;
  front += lights(rx + 14, ry - 12, lo("reactor"), "#ff7a59", 6);

  /* ----- Lager ----- */
  const cx0 = 218, cw = Math.max(26, px - 14 - cx0), sc = Math.min(1, cw / 84);
  let cg = "";
  if (C === 0) cg = `<path d="M10,0 q-6,-14 6,-20 q12,6 6,20 z" fill="none" stroke="#c9b48a" stroke-width="1.4" stroke-dasharray="2 2"/><path d="M12,-20 l2,-5" stroke="#c9b48a" stroke-width="1.2"/>`;
  if (C >= 1) cg += `<rect x="2" y="-18" width="22" height="18" rx="1.5" fill="#9a6a32" stroke="#4e331a" stroke-width="1.4"/><path d="M2,-9 h22 M9,-18 v18 M17,-18 v18" stroke="#4e331a" stroke-width="1.1"/>`;
  if (C >= 2) cg += [30, 46].map(x => `<rect x="${x}" y="-20" width="13" height="20" rx="5" fill="#7a4a24" stroke="#3a2412" stroke-width="1.3"/><path d="M${x},-14 h13 M${x},-6 h13" stroke="#c9b48a" stroke-width="1.4"/>`).join("");
  if (C === 3) cg += `<path d="M-2,0 V-30 M80,0 V-30" stroke="#6e4f30" stroke-width="2.4"/><path d="M-8,-28 L39,-46 L86,-28 Z" fill="#c9a24a" stroke="#7a5a1a" stroke-width="1.4" stroke-linejoin="round"/>
    <path d="M-8,-28 l4,4 l4,-4 l4,4 l4,-4 l4,4 l4,-4 l4,4 l4,-4 l4,4 l4,-4 l4,4 l4,-4 l4,4 l4,-4 l4,4 l4,-4 l4,4 l4,-4 l4,4 l4,-4 l4,4 l4,-4 l2,2" stroke="#7a5a1a" stroke-width="1" fill="none"/><rect x="62" y="-16" width="14" height="16" rx="1.5" fill="#9a6a32" stroke="#4e331a" stroke-width="1.2"/>`;
  front += `<g transform="translate(${cx0} ${t - 1}) scale(${sc.toFixed(3)})">${cg}</g>`;
  front += lights(cx0 + 2, b + 4, lo("cargo"), "#ffc94a");

  /* ----- Schiffbrüchige Person am Bug ----- */
  const hat = H === 0 ? "" : H === 1 ? `<path d="M${px - 5},${t - 18} h10" stroke="#3a6aa8" stroke-width="2.2" stroke-linecap="round"/>` : H === 2 ? `<ellipse cx="${px}" cy="${t - 18}" rx="7.5" ry="2" fill="#e0c06a"/><path d="M${px - 4},${t - 18} q4,-6 8,0" fill="#e0c06a"/>` : `<path d="M${px - 7},${t - 18} h14 l-3,-5 h-8 z" fill="#1a2a40"/><path d="M${px - 2},${t - 21} h4" stroke="#ffd34a" stroke-width="1.2"/><path d="M${px + 6},${t - 8} L${px + 26},${t - 34}" stroke="#6e4f30" stroke-width="1.4"/><path d="M${px + 26},${t - 34} Q${px + 30},${t - 10} ${px + 28},${WL + 6}" stroke="#e8f7f5" stroke-width=".6" fill="none" opacity=".7"/>`;
  front += `<path d="M${px - 6},${t - 1} q0,-9 6,-10 q6,1 6,10 z" fill="${["#8a7a6a", "#c0563a", "#3a8a6a", "#2f6fb0"][H]}"/><path d="M${px + 2},${t - 2} l6,-4 l4,4" stroke="#e0a878" stroke-width="2.4" fill="none" stroke-linecap="round"/>
    <circle cx="${px}" cy="${t - 15}" r="4.2" fill="#e0a878"/><circle cx="${px + 1.6}" cy="${t - 15.5}" r=".7" fill="#1a1a1a"/>${H === 0 ? `<path d="M${px - 4},${t - 18} q2,-3 5,-1 q2,-3 4,1" stroke="#5a3a1a" stroke-width="1.4" fill="none"/>` : ""}${hat}`;

  /* ----- Wasser vor dem Floß ----- */
  const wv = (y, amp, ph) => { let d = `M${l - 40},${y}`; for (let x = l - 40; x < n + 50; x += 16) d += ` q4,${-amp} 8,0 t8,0`; return d; };
  front += `<g class="wavefx"><path d="${wv(WL, 2.4)} V${b + 14} H${l - 40} Z" fill="#1d7a95" opacity=".5"/><path d="${wv(WL, 2.4)}" stroke="#e8f7f5" stroke-width="1.2" fill="none" opacity=".55"/><path d="${wv(WL + 6, 1.6)}" stroke="#e8f7f5" stroke-width=".8" fill="none" opacity=".25"/></g>`;

  // unsichtbare Klickzonen für die Spielereien (oben liegend)
  const z = (part, shape) => shape.replace(/^<(\w+)/, `<$1 class="zone" data-part="${part}" fill="#ffffff" fill-opacity="0"`);
  const zones = [
    z("cargo", `<rect x="${cx0 - 4}" y="${t - (C === 3 ? 50 : 26)}" width="${cw + 8}" height="${C === 3 ? 50 : 26}"/>`),
    z("hull", `<path d="${hp}"/>`),
    z("engine", E === 0 ? `<rect x="${l - 36}" y="${t - 22}" width="56" height="${WL - t + 40}"/>` : `<rect x="${mx - 6}" y="${t - 86}" width="${E === 3 ? 90 : 68}" height="74"/>`),
    z("cockpit", `<rect x="${px - 10}" y="${t - 26}" width="20" height="26"/>`),
    z("reactor", `<circle cx="${rx}" cy="${ry - 6}" r="13"/>`),
    z("scanner", `<rect x="${sx - 11}" y="${t - 76}" width="22" height="74"/>`),
  ].join("");
  return `<g class="ship t${H}">${back}${hull}${front}${zones}</g>`;
}

'''

OCEAN_SKY = r'''function sizeSkyObj(o) {
  const r = o.host.getBoundingClientRect(), d = devicePixelRatio || 1;
  o.w = r.width; o.h = r.height;
  if (!o.w) return;
  o.canvas.width = o.w * d; o.canvas.height = o.h * d; o.cx.setTransform(d, 0, 0, d, 0, 0);
  o.stars = Array.from({ length: 5 }, () => ({ x: Math.random() * o.w, y: o.h * (.05 + Math.random() * .26), z: .5 + Math.random() * .8, w: 50 + Math.random() * 70 }));
  o.dust = Array.from({ length: 30 }, () => ({ x: Math.random() * o.w, y: Math.random(), p: Math.random() * 6 }));
  o.debris = Array.from({ length: 7 }, () => newDebris(o, true));
  o.birds = Array.from({ length: 3 }, () => ({ x: Math.random() * o.w, y: o.h * (.08 + Math.random() * .22), v: .2 + Math.random() * .25, p: Math.random() * 6 }));
}
function newDebris(o, anywhere) {
  const hz = toSky(o, 0, 96)[1];
  return { x: anywhere ? Math.random() * o.w : o.w + 30, y: hz + 8 + Math.random() * Math.max(10, o.h - hz - 16), s: 3 + Math.random() * 4, kind: Math.random() < .55 ? "plank" : "barrel", rot: (Math.random() - .5) * .6, v: .12 + Math.random() * .25, p: Math.random() * 6 };
}
function toSky(o, x, y) { const s = Math.min(o.w / VB.w, o.h / VB.h); return [(o.w - VB.w * s) / 2 + (x - VB.x) * s, (o.h - VB.h * s) / 2 + (y - VB.y) * s, s]; }
function skyCloud(c, x, y, w, col) {
  c.fillStyle = col; c.beginPath();
  c.ellipse(x, y, w * .5, w * .15, 0, 0, 7); c.ellipse(x - w * .22, y + w * .03, w * .28, w * .12, 0, 0, 7); c.ellipse(x + w * .18, y - w * .06, w * .26, w * .15, 0, 0, 7);
  c.fill();
}
function skyIsland(c, o, sec, hz, now) {
  const span = o.w * 1.8, ix = ((o.w * 1.15 - now * .006) % span + span) % span - o.w * .35, s = Math.max(.6, o.h / 200);
  c.fillStyle = sec.land;
  if (sec.shape === "palm") {
    c.beginPath(); c.ellipse(ix, hz + 1, 70 * s, 13 * s, 0, Math.PI, 0); c.fill();
    c.strokeStyle = sec.land; c.lineWidth = 3 * s;
    [[-18, 30], [10, 38]].forEach(([dx, hh]) => {
      c.beginPath(); c.moveTo(ix + dx * s, hz - 6 * s); c.quadraticCurveTo(ix + (dx + 6) * s, hz - hh * .6 * s, ix + (dx + 2) * s, hz - hh * s); c.stroke();
      for (let a = 0; a < 5; a++) { const ang = Math.PI * (1.05 + a * .23); c.beginPath(); c.moveTo(ix + (dx + 2) * s, hz - hh * s); c.quadraticCurveTo(ix + (dx + 2 + Math.cos(ang) * 10) * s, hz - (hh + 6) * s, ix + (dx + 2 + Math.cos(ang) * 18) * s, hz - (hh - Math.sin(ang) * -10) * s); c.stroke(); }
    });
  } else if (sec.shape === "mist") {
    [[0, 60, 16], [70, 40, 11], [-60, 34, 9]].forEach(([dx, w, h]) => { c.beginPath(); c.ellipse(ix + dx * s, hz + 1, w * s, h * s, 0, Math.PI, 0); c.fill(); });
    const fg = c.createLinearGradient(0, hz - 14 * s, 0, hz + 4); fg.addColorStop(0, "rgba(230,240,248,0)"); fg.addColorStop(1, "rgba(230,240,248,.45)");
    c.fillStyle = fg; c.fillRect(0, hz - 14 * s, o.w, 18 * s);
  } else if (sec.shape === "volcano") {
    c.beginPath(); c.moveTo(ix - 80 * s, hz + 1); c.lineTo(ix - 14 * s, hz - 46 * s); c.lineTo(ix + 10 * s, hz - 46 * s); c.lineTo(ix + 80 * s, hz + 1); c.fill();
    c.fillStyle = "rgba(255,120,50,.7)"; c.beginPath(); c.ellipse(ix - 2 * s, hz - 46 * s, 12 * s, 3 * s, 0, 0, 7); c.fill();
    for (let i = 0; i < 4; i++) { const k = ((now * .0004 + i / 4) % 1); c.fillStyle = `rgba(90,70,70,${.35 * (1 - k)})`; c.beginPath(); c.arc(ix + (k * 30 - 4) * s, hz - (50 + k * 60) * s, (6 + k * 16) * s, 0, 7); c.fill(); }
  } else {
    c.beginPath(); c.ellipse(ix, hz + 1, 64 * s, 8 * s, 0, Math.PI, 0); c.fill();
    [[-30, 26], [-16, 34], [14, 22], [28, 30]].forEach(([dx, hh]) => c.fillRect(ix + dx * s, hz - hh * s, 6 * s, hh * s));
    c.fillRect(ix - 34 * s, hz - 38 * s, 30 * s, 5 * s);
    c.fillStyle = "rgba(140,255,210,.5)"; c.beginPath(); c.arc(ix - 13 * s, hz - 30 * s, 2.2 * s, 0, 7); c.fill();
  }
}
function drawSky(o, now, dt) {
  if (!o.w) { sizeSkyObj(o); if (!o.w) return; }
  const c = o.cx, E = Math.floor(state.ship.engine / 3), H = Math.floor(state.ship.hull / 3), R = Math.floor(state.ship.reactor / 3);
  const speed = (0.03 + E * 0.12 + warpBoost * 0.35 + (performance.now() < shipBoostUntil ? 0.9 : 0)) * dt;
  const sec = curSector(), hz = toSky(o, 0, 96)[1];
  c.clearRect(0, 0, o.w, o.h);
  // Himmel
  const sg = c.createLinearGradient(0, 0, 0, hz); sg.addColorStop(0, sec.sky[0]); sg.addColorStop(.65, sec.sky[1]); sg.addColorStop(1, sec.sky[2]);
  c.fillStyle = sg; c.fillRect(0, 0, o.w, hz + 1);
  // Sonne oder Mond
  const sx = o.w * .8, sy = hz * .4, sr = Math.max(12, o.h * .085);
  const gl = c.createRadialGradient(sx, sy, sr * .5, sx, sy, sr * 4.2); gl.addColorStop(0, sec.sun[1]); gl.addColorStop(1, "rgba(0,0,0,0)");
  c.fillStyle = gl; c.fillRect(0, 0, o.w, hz);
  c.fillStyle = sec.sun[0]; c.beginPath(); c.arc(sx, sy, sr, 0, 7); c.fill();
  // Wolken
  for (const cl of o.stars) { cl.x -= (.04 + speed * .02) * cl.z * dt * .5; if (cl.x < -cl.w) cl.x = o.w + cl.w; skyCloud(c, cl.x, cl.y, cl.w * cl.z, sec.cloud); }
  // Möwen
  c.strokeStyle = "rgba(240,248,255,.75)"; c.lineWidth = 1.4;
  for (const bd of o.birds) {
    bd.x -= (bd.v + speed * .05) * dt * .06; bd.p += dt * .012; if (bd.x < -20) { bd.x = o.w + 20; bd.y = o.h * (.08 + Math.random() * .22); }
    const f = Math.sin(bd.p) * 3; c.beginPath(); c.moveTo(bd.x - 6, bd.y - f); c.quadraticCurveTo(bd.x - 3, bd.y - 3, bd.x, bd.y); c.quadraticCurveTo(bd.x + 3, bd.y - 3, bd.x + 6, bd.y - f); c.stroke();
  }
  // Insel am Horizont
  skyIsland(c, o, sec, hz, now);
  // Meer
  const mg = c.createLinearGradient(0, hz, 0, o.h); mg.addColorStop(0, sec.sea[0]); mg.addColorStop(1, sec.sea[1]);
  c.fillStyle = mg; c.fillRect(0, hz, o.w, o.h - hz);
  // Glitzern unter der Sonne
  c.fillStyle = sec.glint;
  for (let i = 0; i < 16; i++) { const k = (i * 37 % 16) / 16, y = hz + 3 + k * (o.h - hz) * .7, w = (4 + k * 20) * (.6 + .4 * Math.sin(now * .004 + i * 1.7)); c.globalAlpha = .25 + .5 * Math.max(0, Math.sin(now * .003 + i)); c.fillRect(sx - w / 2 + Math.sin(i * 2.3) * (8 + k * 30), y, w, 1.4); }
  c.globalAlpha = 1;
  // Wellen
  o.off = (o.off || 0) + speed * 3 + dt * .015;
  for (let i = 0; i < 9; i++) {
    const y = hz + (o.h - hz) * Math.pow((i + 1) / 10, 1.5), amp = .8 + i * .55, wl = 28 + i * 12;
    c.strokeStyle = `rgba(255,255,255,${.05 + i * .012})`; c.lineWidth = 1 + i * .12;
    c.beginPath();
    for (let x = -wl; x <= o.w + wl; x += 6) { const yy = y + Math.sin((x + o.off * (1 + i * .35)) / wl * 6.283) * amp; x === -wl ? c.moveTo(x, yy) : c.lineTo(x, yy); }
    c.stroke();
  }
  // Treibgut beim Wrack
  const debrisCount = H === 0 ? 7 : H === 1 ? 3 : 0;
  o.debris.slice(0, debrisCount).forEach((d, i) => {
    d.x -= (d.v + speed * .3) * (dt / 16); d.p += dt * .003;
    if (d.x < -30) o.debris[i] = newDebris(o, false);
    const by = d.y + Math.sin(d.p) * 1.5;
    c.save(); c.translate(d.x, by); c.rotate(d.rot + Math.sin(d.p) * .05);
    if (d.kind === "plank") { c.fillStyle = "#6b5034"; c.fillRect(-d.s * 2.4, -d.s * .35, d.s * 4.8, d.s * .7); c.fillStyle = "rgba(255,255,255,.15)"; c.fillRect(-d.s * 2.4, -d.s * .35, d.s * 4.8, d.s * .18); }
    else { c.fillStyle = "#7a4a24"; c.beginPath(); c.ellipse(0, 0, d.s * .9, d.s * 1.2, Math.PI / 2, 0, 7); c.fill(); c.strokeStyle = "#c9b48a"; c.lineWidth = 1; c.beginPath(); c.moveTo(-d.s * .5, -d.s * .9); c.lineTo(-d.s * .5, d.s * .9); c.moveTo(d.s * .5, -d.s * .9); c.lineTo(d.s * .5, d.s * .9); c.stroke(); }
    c.restore();
  });
  const g = GEO[H];
  // Kielwasser und Paddelspritzer
  if (E >= 1 && Math.random() < .55 + E * .12) {
    const [x, y, s] = toSky(o, g.l - (E === 3 ? 10 : 2), 113 + (Math.random() - .5) * 4);
    o.parts.push({ x, y, vx: -1.4 - E * 1.1, vy: (Math.random() - .5) * .25, r: (1.2 + E * .45) * s, life: 1, kind: "trail", col: "255,255,255" });
  }
  if (E === 0 && Math.random() < .03) { const [x, y] = toSky(o, g.l - 26, 120); for (let i = 0; i < 8; i++) o.parts.push({ x, y, vx: (Math.random() - .7) * 2, vy: -1 - Math.random() * 2, r: 1.4, life: 1, kind: "drop" }); }
  // Rauch und Funken der Feuerstelle
  if (R >= 1 && Math.random() < .2 + R * .08) { const [x, y, s] = toSky(o, R === 3 ? 212 : 205, g.t - (R === 3 ? 34 : 18)); o.parts.push({ x, y, vx: -.3 - speed * .02, vy: -.5 - Math.random() * .3, r: 1.6 * s, life: .8, kind: "smoke" }); }
  if (R >= 1 && R <= 2 && Math.random() < .05) { const [x, y] = toSky(o, 205, g.t - 12); for (let i = 0; i < 3; i++) o.parts.push({ x, y, vx: (Math.random() - .5) * 1.4, vy: -1 - Math.random() * 1.6, r: 1, life: 1, kind: "spark" }); }
  if (H === 0 && Math.random() < .015) { const [x, y] = toSky(o, g.l + 70, 114); for (let i = 0; i < 5; i++) o.parts.push({ x, y, vx: (Math.random() - .5) * 1.5, vy: -.6 - Math.random(), r: 1.2, life: 1, kind: "drop" }); }
  o.parts = o.parts.filter(p => p.life > 0);
  for (const p of o.parts) {
    p.x += p.vx * dt * .06; p.y += p.vy * dt * .06;
    if (p.kind === "trail") { p.life -= .0022 * dt; p.r += .004 * dt; c.fillStyle = `rgba(${p.col},${p.life * .45})`; c.beginPath(); c.ellipse(p.x, p.y, p.r * 1.6, p.r * .6, 0, 0, 7); c.fill(); }
    else if (p.kind === "smoke") { p.r += .02 * dt; p.life -= .0009 * dt; c.fillStyle = `rgba(200,200,205,${p.life * .3})`; c.beginPath(); c.arc(p.x, p.y, p.r, 0, 7); c.fill(); }
    else if (p.kind === "drop") { p.vy += .006 * dt; p.life -= .002 * dt; c.fillStyle = `rgba(220,245,255,${p.life * .8})`; c.beginPath(); c.arc(p.x, p.y, p.r, 0, 7); c.fill(); }
    else { p.vy += .002 * dt; p.life -= .0025 * dt; c.fillStyle = `rgba(255,${150 + (Math.random() * 80 | 0)},60,${p.life})`; c.fillRect(p.x, p.y, p.r * 2, p.r * 2); }
  }
  // Funkeln auf dem Wasser
  for (const d of o.dust) {
    d.x -= speed * 1.5 + .05 * dt * .06; d.p += dt * .004;
    if (d.x < -4) d.x = o.w + 4;
    const y = hz + 6 + d.y * (o.h - hz - 8), a = Math.max(0, Math.sin(d.p)) * .5;
    if (a > .05) { c.fillStyle = `rgba(255,255,255,${a})`; c.fillRect(d.x, y, 2 + d.y * 3, 1); }
  }
}
'''

BUBBLES = r'''function drawStars(dt) {
  scx.clearRect(0, 0, innerWidth, innerHeight);
  // ab und zu zieht ein Fischschwarm durch die Tiefe
  if (!shooter && Math.random() < .0012 * (dt || 0)) shooter = { x: -80, y: innerHeight * (.5 + Math.random() * .4), vx: 1.2 + Math.random() * .8, s: 5 + Math.random() * 5 };
  if (shooter) {
    const f = shooter; f.x += f.vx * dt * .12;
    for (let i = 0; i < 8; i++) {
      const fx = f.x - i * 15 - (i % 2) * 7, fy = f.y + Math.sin((f.x + i * 40) / 30) * 4 + (i % 3) * 8;
      scx.fillStyle = "rgba(160,225,235,.12)"; scx.beginPath(); scx.ellipse(fx, fy, f.s, f.s * .42, 0, 0, 7);
      scx.moveTo(fx - f.s * .9, fy); scx.lineTo(fx - f.s * 1.6, fy - f.s * .5); scx.lineTo(fx - f.s * 1.6, fy + f.s * .5); scx.closePath(); scx.fill();
    }
    if (f.x > innerWidth + 220) shooter = null;
  }
  for (const s of stars) {
    s.y -= (0.025 + warpBoost * 1.1) * s.z * dt; s.p += 0.002 * dt;
    if (s.y < -10) { s.y = innerHeight + 10; s.x = Math.random() * innerWidth; }
    const x = s.x + Math.sin(s.p * 2) * 4 * s.z;
    scx.strokeStyle = `rgba(200,245,255,${.1 + .22 * s.z})`; scx.lineWidth = 1;
    scx.beginPath(); scx.arc(x, s.y, s.z * 2.2 + warpBoost * 1.2, 0, 7); scx.stroke();
  }
}
'''

GULL_NEW = r'''const DRONE = `<g class="drone">
  <path d="M-3 0 q-14 -13 -27 -5 q12 -1 22 9z" fill="#f4f8fb" stroke="#5b6b78" stroke-width="1.2"><animateTransform attributeName="transform" type="rotate" values="0 -3 0;-28 -3 0;0 -3 0" dur=".34s" repeatCount="indefinite"/></path>
  <path d="M3 0 q14 -13 27 -5 q-12 -1 -22 9z" fill="#f4f8fb" stroke="#5b6b78" stroke-width="1.2"><animateTransform attributeName="transform" type="rotate" values="0 3 0;28 3 0;0 3 0" dur=".34s" repeatCount="indefinite"/></path>
  <ellipse cx="0" cy="3" rx="12" ry="6" fill="#ffffff" stroke="#5b6b78" stroke-width="1.2"/>
  <path d="M-12 3 l-7 -2 l1 5z" fill="#8a9aa6"/>
  <circle cx="9" cy="-1" r="5" fill="#ffffff" stroke="#5b6b78" stroke-width="1.2"/>
  <circle cx="10.5" cy="-2" r="1.2" fill="#10202a"/>
  <path d="M13 -1 l7 2 l-7 2z" fill="#ffb347"/>
</g>`;
'''

DECAL_NEW = r'''function decalSVG(g) {
  const { l, t, b, n } = g, d = state.decal || "none", m = (t + b) / 2;
  if (d === "stripes") return `<path d="M${l},${m - 2.4} H${n}" stroke="#ffffff" stroke-width="2.2" opacity=".8"/><path d="M${l},${m + 2.4} H${n}" stroke="#ff7a59" stroke-width="2" opacity=".85"/>`;
  if (d === "flames") { let p = `M${l},${m}`; for (let x = l; x < n; x += 12) p += ` q3,-4 6,0 t6,0`; return `<path d="${p}" stroke="#7fdcff" stroke-width="2" fill="none" opacity=".9"/><path d="${p.replace(`M${l},${m}`, `M${l},${m + 4}`)}" stroke="#ffffff" stroke-width="1" fill="none" opacity=".6"/>`; }
  if (d === "crest") return `<g transform="translate(${(l + n) / 2 - 8} ${t + 1}) scale(.5)"><path d="M0 4 L28 26 M28 4 L0 26" stroke="#f2ead8" stroke-width="3.4" stroke-linecap="round"/><circle cx="14" cy="11" r="8" fill="#f2ead8"/><rect x="9" y="16" width="10" height="6" rx="2" fill="#f2ead8"/><circle cx="11" cy="11" r="2" fill="#2a1a0a"/><circle cx="17" cy="11" r="2" fill="#2a1a0a"/></g>`;
  return "";
}
'''

PAINTS_NEW = r'''const PAINTS = [
  { id: "std", name: "Naturholz", filter: "none", sw: "linear-gradient(135deg,#c99a62,#7a4f2a)", need: "" },
  { id: "cobalt", name: "Meerblau", filter: "hue-rotate(180deg) saturate(1.3)", sw: "linear-gradient(135deg,#3a8ad8,#1a3f7a)", rank: 2, need: "ab Rang 2" },
  { id: "ruby", name: "Korallenrot", filter: "hue-rotate(-25deg) saturate(1.8)", sw: "linear-gradient(135deg,#ff6b4a,#8a2010)", rank: 4, need: "ab Rang 4" },
  { id: "emerald", name: "Moosgrün", filter: "hue-rotate(60deg) saturate(1.2)", sw: "linear-gradient(135deg,#6aa84a,#2a5a1a)", rank: 6, need: "ab Rang 6" },
  { id: "gold", name: "Gold", filter: "sepia(1) saturate(2.8) hue-rotate(-12deg) brightness(1.15)", sw: "linear-gradient(135deg,#ffe39a,#b07a1a)", rank: 10, need: "ab Rang 10" },
  { id: "night", name: "Teerschwarz", filter: "brightness(.5) contrast(1.3) saturate(.5)", sw: "linear-gradient(135deg,#3a3028,#0a0806)", ach: "explorer", need: "Erfolg: Floßkenner" },
];
'''

DECALS_NEW = r'''const DECALS = [
  { id: "none", name: "Keins", sw: "#0c2a35", need: "" },
  { id: "stripes", name: "Seemannsstreifen", sw: "repeating-linear-gradient(90deg,#0c2a35 0 8px,#ffffff 8px 11px,#0c2a35 11px 14px,#ff7a59 14px 17px)", rank: 3, need: "ab Rang 3" },
  { id: "flames", name: "Wellenmuster", sw: "linear-gradient(90deg,#3a8ad8,#7fdcff)", ach: "mega", need: "Erfolg: Mega-Bergung" },
  { id: "crest", name: "Totenkopf", sw: "radial-gradient(circle,#f2ead8 30%,#0c2a35 32%)", rank: 9, need: "ab Rang 9" },
];
'''
