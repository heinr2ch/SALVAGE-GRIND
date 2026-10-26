# Teil 3: Welt, Texte, Wörter
SECTORS_NEW = r'''const SECTORS = [
  { id: "orion", name: "Treibgutbucht", rank: 1, color: "#3fe0c5", transpose: 0, x: 60, y: 160, shape: "palm", land: "#0f3a44",
    sky: ["#0b3a5a", "#2c7fab", "#ffc98a"], sun: ["#fff2c4", "rgba(255,214,140,.38)"], cloud: "rgba(255,244,232,.55)", sea: ["#1f7f9a", "#05283a"], glint: "rgba(255,240,200,.8)",
    desc: "Die Heimatbucht. Viel Treibgut, ein paar Palmen und der Ort, an dem jede Floßfahrt beginnt.",
    radio: ["Funk: In der Treibgutbucht schwimmt heute viel herum. Augen auf."] },
  { id: "kryos", name: "Nebelinseln", rank: 4, color: "#9fd8ff", transpose: 2, x: 160, y: 70, shape: "mist", land: "#3c5566",
    sky: ["#2c3e50", "#6f8ea8", "#d4e3ec"], sun: ["#f4f8ff", "rgba(220,235,255,.28)"], cloud: "rgba(232,240,248,.6)", sea: ["#4f7d93", "#0d2836"], glint: "rgba(235,248,255,.6)",
    desc: "Kühle Inseln im Dauernebel, zwischen denen alte Fischerboote treiben. Expeditionen bringen hier 25 % mehr.",
    radio: ["Funk: Dichter Nebel bei den Nebelinseln. Nebelhorn bereithalten.", "Funk: Eine Robbe winkt vom Felsen. Kein Scherz."] },
  { id: "ignis", name: "Feuerinsel", rank: 8, color: "#ff9a3c", transpose: -3, x: 265, y: 150, shape: "volcano", land: "#2a1210",
    sky: ["#2a0e14", "#8a2f1e", "#ff9a5a"], sun: ["#ffd27a", "rgba(255,140,60,.42)"], cloud: "rgba(255,190,150,.4)", sea: ["#7a3a2a", "#170809"], glint: "rgba(255,200,130,.75)",
    desc: "Ein rauchender Vulkan, warmes Wasser und Ascheregen. Expeditionen bringen hier 50 % mehr.",
    radio: ["Funk: Ascheregen über der Feuerinsel. Segel einholen.", "Funk: Der Vulkan grummelt. Die Fische tun so, als wäre nichts."] },
  { id: "xeltar", name: "Versunkene Ruinen", rank: 12, color: "#5dffa8", transpose: 5, x: 350, y: 60, shape: "ruins", land: "#0b2a26",
    sky: ["#04121f", "#0d3a4a", "#2f8a7a"], sun: ["#e8fff5", "rgba(140,255,210,.26)"], cloud: "rgba(180,230,220,.25)", sea: ["#0f4a48", "#021414"], glint: "rgba(170,255,220,.6)",
    desc: "Uralte Säulen ragen aus dem Meer und leuchten nachts. Niemand weiß, wer sie gebaut hat. Expeditionen bringen hier 75 % mehr.",
    radio: ["Funk: Die Säulen der Ruinen summen wieder.", "Funk: Unbekannte Zeichen an den Ruinen entdeckt. Übersetzung läuft ... seit 300 Jahren."] },
];
'''

SECTOR_CSS = [
    (':root { --s1: #4fe3ff; --s2: #8b6cff; --s3: #ff4fd8; }', ':root { --s1: #3fe0c5; --s2: #2f8fff; --s3: #ffb36b; }'),
    ('html[data-sector="kryos"] { --s1: #9fe8ff; --s2: #5aa9ff; --s3: #e0f7ff; }', 'html[data-sector="kryos"] { --s1: #9fd8ff; --s2: #6f8ea8; --s3: #e0f0f7; }'),
    ('html[data-sector="ignis"] { --s1: #ffc94a; --s2: #ff4b3c; --s3: #ff9a3c; }', 'html[data-sector="ignis"] { --s1: #ffc94a; --s2: #ff4b3c; --s3: #ff9a3c; }'),
    ('html[data-sector="xeltar"] { --s1: #5dffa8; --s2: #1fbf8f; --s3: #c6f36b; }', 'html[data-sector="xeltar"] { --s1: #5dffa8; --s2: #1f8fbf; --s3: #9ff3d6; }'),
]

CREW_NEW = r'''const CREW = [
  { id: "mira", name: "Mira", role: "Zimmerin", cost: 800, color: "#ff9a3c", effect: "Notverkauf erstattet 10 % mehr.",
    art: face("#f1c7a6", `<path d="M14 24 q2 -14 13 -14 q12 0 13 14 q-4 -6 -13 -6 q-9 0 -13 6z" fill="#c2452d"/><rect x="13" y="17" width="28" height="5" rx="2" fill="#ff7a59"/>`, { suit: "#ff9a3c", more: `<path d="M38 40 l6 -6 l2 2 l-6 6z" fill="#c9b48a"/>` }),
    lines: ["Wer hat schon wieder mit dem Hammer auf die Feuerstelle gehauen?", "Gib mir zehn Minuten und ein Stück Tau.", "Das Floß hält. Ich hab's mit Liebe und drei Knoten gebaut."] },
  { id: "juno", name: "Juno", role: "Navigatorin", cost: 1200, color: "#3fe0c5", effect: "Expeditionen sind 25 % schneller.",
    art: face("#8d5a3b", `<path d="M13 28 q-1 -18 14 -18 q15 0 14 18 q-3 -8 -14 -8 q-11 0 -14 8z" fill="#1d1d2b"/><circle cx="27" cy="10" r="5" fill="#1d1d2b"/>`, { suit: "#2b6cff", more: `<circle cx="32" cy="26" r="4.5" fill="none" stroke="#3fe0c5" stroke-width="1.4"/>` }),
    lines: ["Ich kenne eine Abkürzung. Sie führt nur ein bisschen durch ein Riff.", "Kurs gesetzt. Ungefähr.", "Sterne lügen nie. Seekarten schon."] },
  { id: "broesel", name: "Krümel", role: "Smutje-Krabbe", cost: 1000, color: "#5dffa8", effect: "Alle XP um 10 % erhöht.",
    art: `<svg viewBox="0 0 54 54"><rect width="54" height="54" fill="#0c2a35"/><ellipse cx="27" cy="34" rx="15" ry="10" fill="#e8553a" stroke="#8a2010" stroke-width="1.4"/><path d="M12 30 q-8 -4 -6 -12 q4 0 6 4 M42 30 q8 -4 6 -12 q-4 0 -6 4" stroke="#e8553a" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M14 40 l-5 5 M18 42 l-3 6 M40 40 l5 5 M36 42 l3 6" stroke="#e8553a" stroke-width="2" stroke-linecap="round"/><path d="M22 25 v-6 M32 25 v-6" stroke="#8a2010" stroke-width="1.6"/><circle cx="22" cy="18" r="2.6" fill="#fff"/><circle cx="32" cy="18" r="2.6" fill="#fff"/><circle cx="22" cy="18" r="1.2" fill="#111"/><circle cx="32" cy="18" r="1.2" fill="#111"/><path d="M14 13 q2 -8 13 -8 q11 0 13 8z" fill="#ffffff"/><path d="M23 37 q4 3 8 0" stroke="#5a1008" stroke-width="1.4" fill="none"/></svg>`,
    lines: ["Heute gibt's Fischsuppe. Wie gestern. Und morgen.", "Ich habe den Grill repariert. Mit den Scheren.", "Mahlzeit! Bitte nicht die Gummiente essen."] },
  { id: "kael", name: "Kael", role: "Funker", cost: 1500, color: "#ff7a59", effect: "Aufträge zahlen 20 % mehr.",
    art: face("#e9b98f", `<path d="M14 22 q4 -12 13 -12 q10 0 13 12 l-2 -2 l-3 3 l-3 -4 l-3 4 l-3 -4 l-3 4 l-3 -3z" fill="#2f6fb0"/>`, { suit: "#1f4a6b", more: `<path d="M12 22 q-2 6 2 10 M42 22 q2 6 -2 10" stroke="#ff7a59" stroke-width="2.4" fill="none"/><rect x="8" y="24" width="5" height="9" rx="2" fill="#ff7a59"/><rect x="41" y="24" width="5" height="9" rx="2" fill="#ff7a59"/>` }),
    lines: ["Die Strandgilde hat angefunkt. Sie wollen wissen, ob wir noch schwimmen.", "Ich hab drei neue Aufträge reingefunkt. Gern geschehen.", "Psst, im Funk wird über dich geredet. Positiv!"] },
];
'''

EXPED_NEW = r'''const EXPED = [
  { id: "short", name: "Riff um die Ecke", min: 10, album: 0 },
  { id: "mid", name: "Treibendes Wrackfeld", min: 30, album: .12 },
  { id: "long", name: "Unbekannte Insel", min: 120, album: .3 },
];
'''

ACH_NEW = r'''const ACH = [
  A("first", "Erster Wurf", "Wirf das Netz zum ersten Mal aus.", "scrap", 10, () => state.spins >= 1),
  A("busy", "Fleißiger Fischer", "100 Würfe.", "cell", 50, () => state.spins >= 100),
  A("marathon", "Seebär", "1.000 Würfe.", "chip", 300, () => state.spins >= 1000),
  A("win1", "Erster Fang", "Gewinne zum ersten Mal.", "scrap", 10, () => (st().wins || 0) >= 1),
  A("big", "Große Bergung", "Gewinne mindestens 15× deinen Einsatz.", "core", 100, () => (st().maxFactor || 0) >= 15),
  A("mega", "Mega-Bergung", "Gewinne mindestens 40× deinen Einsatz.", "relic", 250, () => (st().maxFactor || 0) >= 40),
  A("jack", "Piratenschatz", "Knacke den Jackpot.", "crystal", 500, () => (st().jackpots || 0) >= 1),
  A("laser", "Möwenfreund", "Die Hilfsmöwe hilft 5-mal aus.", "wild", 100, () => (st().lasers || 0) >= 5),
  A("fs", "Flaschenpost", "Löse Freifahrten aus.", "beacon", 50, () => (st().fs || 0) >= 1),
  A("pick", "Kistenknacker", "Spiele die Kistenbergung.", "capsule", 75, () => (st().pick || 0) >= 1),
  A("ring3", "Strudelkern", "Erreiche den innersten Ring der Strudelfahrt.", "warp", 150, () => (st().ring3 || 0) >= 1),
  A("hot", "Heiße Strähne", "Strähne von 4 Gewinnen.", "core", 100, () => (st().maxStreak || 0) >= 4),
  A("unstop", "Unaufhaltsam", "Strähne von 6 Gewinnen.", "relic", 300, () => (st().maxStreak || 0) >= 6),
  A("tix", "Rubbelfinger", "Kaufe 10 Rubbellose.", "scrap", 75, () => (st().tickets || 0) >= 10),
  A("tixbig", "Rubbelglück", "Gewinne mindestens 20× den Lospreis.", "crystal", 250, () => (st().ticketBig || 0) >= 1),
  A("dare", "Mutprobe", "Gewinne eine Runde im Risikospiel.", "beacon", 50, () => (st().gambleWins || 0) >= 1),
  A("allin", "Alles oder nichts", "Gewinne 4 Risikorunden am Stück.", "wild", 300, () => (st().gambleChain || 0) >= 4),
  A("up1", "Erste Bastelei", "Kaufe eine Upgrade-Stufe.", "up_hull", 25, () => (st().upgrades || 0) >= 1),
  A("tier", "Großes Upgrade", "Schließe eine Ausbaustufe ab.", "up_engine", 75, () => (st().tierUps || 0) >= 1),
  A("maxed", "Voll ausgebaut", "Alle 45 Upgrade-Stufen.", "up_reactor", 1000, () => totalSteps() >= 45),
  A("crew", "Volle Besatzung", "Heuere alle vier Crewmitglieder an.", "up_scanner", 300, () => (state.crew || []).length >= 4),
  A("captain", "Kapitän", "Erreiche Rang 7.", "up_reactor", 200, () => state.level >= 7),
  A("veteran", "Gildenveteran", "Erreiche Rang 15.", "up_reactor", 600, () => state.level >= 15),
  A("exp1", "Erste Expedition", "Hol eine Expedition ab.", "up_engine", 50, () => (st().expeds || 0) >= 1),
  A("world", "Inselhüpfer", "Besuche alle vier Inseln.", "warp", 300, () => (state.visited || []).length >= 4),
  A("coll", "Sammler", "Finde 6 Sammelstücke.", "up_cargo", 200, () => (state.album || []).length >= 6),
  A("museum", "Regal voll", "Finde alle 12 Sammelstücke.", "up_cargo", 800, () => (state.album || []).length >= 12),
  A("explorer", "Floßkenner", "Alle 9 Entdeckungen am Floß.", "wild", 150, () => (state.found || []).length >= 9),
  A("paint", "Neuer Anstrich", "Ändere Farbe oder Abzeichen.", "up_hull", 25, () => (st().paints || 0) >= 1),
  A("phoenix", "Wieder aufgetaucht", "Verliere ein Floß und mach weiter.", "up_hull", 100, () => (state.shipsLost || 0) >= 1),
  A("loyal", "Treuer Kapitän", "Hol dir 7-mal die tägliche Strandsuche.", "crystal", 200, () => (st().daily || 0) >= 7),
  A("dust", "Bernsteinsammler", "Sammle insgesamt 10 Bernstein.", "crystal", 150, () => (st().dustTotal || 0) >= 10),
  A("climber", "Höhenluft", "Erreiche auf der Risikoleiter ×12 oder mehr.", "beacon", 150, () => (st().ladderTop || 0) >= 6),
  A("hunter", "Strandgutjäger", "Hol 10 Treibfässer an Bord.", "crystal", 120, () => (st().starsShot || 0) >= 10),
  A("booster", "Aufgeladen", "Trink deinen ersten Kräutertrank.", "up_scanner", 50, () => (st().boostsUsed || 0) >= 1),
];
'''

ALBUM_REPS = [
    ('name: "Gummiente Mk II"', 'name: "Gummiente"'), ('name: "Verbeulter Helm"', 'name: "Taucherhelm"'), ('name: "Alte Sternkarte"', 'name: "Schatzkarte"'),
    ('name: "Eiskristall-Herz"', 'name: "Muschelherz"'), ('name: "Gefrorener Kaffee"', 'name: "Kalter Kaffee"'), ('name: "Pinguin-Drohne"', 'name: "Verirrter Pinguin"'),
    ('name: "Lavaglas-Würfel"', 'name: "Lavaglas"'), ('name: "Glühende Schraube"', 'name: "Glühender Nagel"'), ('name: "Feuerfeste Socke"', 'name: "Feuerfeste Socke"'),
    ('name: "Alien-Ei"', 'name: "Schildkrötenei"'), ('name: "Singender Monolith"', 'name: "Singende Säule"'), ('name: "Uralter Datenstein"', 'name: "Runenstein"'),
]

RANKS_OLD = 'const RANKS = ["Kadett", "Schrottsammler", "Bergungsgehilfe", "Bergungspilot", "Wrackjäger", "Sternensegler", "Kapitän", "Gildenveteran", "Gildenmeister", "Legende der Leere"];'
RANKS_NEW = 'const RANKS = ["Schiffbrüchiger", "Strandsammler", "Floßbauer", "Leichtmatrose", "Wrackjäger", "Inselsegler", "Kapitän", "Gildenveteran", "Gildenmeister", "Legende der Sieben Meere"];'

EXTRA_CSS = '''
/* ---------- Treibgut: Segel und Wellen ---------- */
.sail { transform-box: fill-box; transform-origin: 0% 100%; animation: sailSway 3.8s ease-in-out infinite; }
@keyframes sailSway { 0%, 100% { transform: skewY(-1.5deg) scaleX(.97); } 50% { transform: skewY(1.5deg) scaleX(1.03); } }
.wavefx { animation: waveBob 2.6s ease-in-out infinite; }
@keyframes waveBob { 0%, 100% { transform: translate(0, 0); } 50% { transform: translate(-6px, 1.4px); } }
.toast { pointer-events: none; }
@media (prefers-reduced-motion: reduce) { .sail, .wavefx { animation: none; } }
</style>'''

STAR_REPS = [
    ('const x0 = VB.x + VB.w + 20, y0 = VB.y + 8 + Math.random() * 60, x1 = VB.x - 25, y1 = y0 + 50 + Math.random() * 70;',
     'const x0 = VB.x + VB.w + 20, y0 = 126 + Math.random() * 24, x1 = VB.x - 25, y1 = y0 + (Math.random() - .5) * 10;'),
    ('''  g.innerHTML = `<line x1="0" y1="0" x2="${ux * 36}" y2="${uy * 36}" stroke="${tail}" stroke-width="3" stroke-linecap="round" opacity=".55"/>
    <line x1="0" y1="0" x2="${ux * 18}" y2="${uy * 18}" stroke="#ffffff" stroke-width="1.6" stroke-linecap="round" opacity=".8"/>
    <circle class="hit" r="15"/><circle r="6" fill="${col}" opacity=".35" filter="url(#glow)"/>
    <path class="core" d="M0 -7 L1.8 -1.8 L7 0 L1.8 1.8 L0 7 L-1.8 1.8 L-7 0 L-1.8 -1.8Z" fill="${col}"/>`;''',
     '''  g.innerHTML = `<path d="M8 4 q8 -3 16 0 t16 0" stroke="#ffffff" stroke-width="1.2" fill="none" opacity=".55"/>
    <circle class="hit" r="16"/><circle r="9" fill="${col}" opacity=".25" filter="url(#glow)"/>
    <g class="core"><rect x="-7" y="-9" width="14" height="16" rx="5" fill="${gold ? "#c9952e" : "#7a4a24"}" stroke="${gold ? "#ffe39a" : "#3a2412"}" stroke-width="1.4"/><path d="M-7 -4 h14 M-7 2 h14" stroke="${gold ? "#fff2c4" : "#c9b48a"}" stroke-width="1.6"/></g>
    <path d="M-12 6 q6 -3 12 0 t12 0" stroke="#e8f7f5" stroke-width="1.3" fill="none" opacity=".8"/>`;'''),
    ('const dur = gold ? 5200 : 7000, t0 = performance.now();', 'const dur = gold ? 6500 : 9000, t0 = performance.now();'),
    ('st.x = x0 + (x1 - x0) * k; st.y = y0 + (y1 - y0) * k + Math.sin(k * 6) * 3;', 'st.x = x0 + (x1 - x0) * k; st.y = y0 + (y1 - y0) * k + Math.sin(k * 14) * 2;'),
    ('bubbleAt(svg, $("shipview"), Math.max(VB.x + 30, Math.min(VB.x + VB.w - 30, st.x)), st.y - 6, st.gold ? "Gold! +3 Staub" : "Treffer! +1 Staub");',
     'bubbleAt(svg, $("shipview"), Math.max(VB.x + 30, Math.min(VB.x + VB.w - 30, st.x)), st.y - 10, st.gold ? "Goldfass! +3 Bernstein" : "An Bord! +1 Bernstein");'),
    ('setTimeout(() => addDust(n, st.gold ? "goldene Sternschnuppe" : "Sternschnuppe"), 700);', 'setTimeout(() => addDust(n, st.gold ? "goldenes Treibfass" : "Treibfass"), 700);'),
    ('ln.setAttribute("stroke", st.gold ? "#ffd34a" : "#ff4fd8"); ln.setAttribute("stroke-width", 2.5);', 'ln.setAttribute("stroke", "#e0c890"); ln.setAttribute("stroke-width", 1.6); ln.setAttribute("stroke-dasharray", "3 2");'),
    ('sfx.pew(); setTimeout(() => sfx.shatter(), 90);', 'sfx.pew(); setTimeout(() => sfx.creak(), 120);'),
]

CHANGELOG_NEW = r'''const CHANGELOG = [
  { v: "0.7.3", date: "25.10.2026", title: "Neustart aus dem Hauptmenü repariert", items: ["Fix: Die Einstellungen lagen hinter dem Hauptmenü, wenn man sie von dort öffnete. Dadurch ließen sich weder die Knöpfe darin noch „Spielstand zurücksetzen“ richtig bedienen.", "Nach dem Zurücksetzen gehen Einstellungen und Hauptmenü jetzt zu, und das Register für den Neuanfang erscheint vorne."] },
  { v: "0.7.2", date: "25.10.2026", title: "Startknopf repariert", items: ["Fix: Wer schon in einer anderen Welt gespielt hatte, konnte das Spiel nicht starten, weil die Weltkarten im Menü beim Laden abstürzten. Der Knopf „Spielen“ funktioniert jetzt wieder."] },
  { v: "0.7.1", date: "25.10.2026", title: "Start direkt im Hauptmenü", items: ["Beim Öffnen startet das Spiel direkt im Hauptmenü. Der Startknopf heißt jetzt in allen Welten „Spielen“.", "Der Start ist abgesichert: Selbst wenn der Browser Ton oder Musik blockiert, geht das Menü zuverlässig zu und das Spiel startet."] },
  { v: "0.7.0", date: "25.10.2026", title: "Hauptmenü, Pech-Walze und Freispiel-Kauf", items: ["Neues Hauptmenü „Salvage & Grind“ mit allen vier Welten als Karten: eindeutiger Name, Thema, Spielart und dein Stand (Rang und Guthaben). Im Spiel jederzeit über „Menü“ oben erreichbar.", "Eigenes Einstellungsmenü (Zahnrad oben oder im Hauptmenü): Ton, Musik, Musiktitel, Lautstärke, Turbo, Begleiter, Pech-Walze, weniger Effekte, Sprache und Spielstand an einem Ort.", "Pech-Walze: Alle 18 bis 45 bezahlten Drehs erscheint dreimal dasselbe Pech-Symbol und kostet 25 bis 100 % des aktuellen Einsatzes. Nie in Freispielen, in den Einstellungen abschaltbar.", "Freispiele kaufen: drei Pakete mit 8, 12 oder 20 Freispielen für das 40-, 60- oder 100-fache des Einsatzes. Gekaufte Freispiele laufen wie ausgelöste."] },
  { v: "0.6.0", date: "25.10.2026", title: "Sprachen Teil 2", items: ["Jetzt übersetzt: Spielregeln, Hilfemodus, Sprechblasen von Bip, Koko, Rex und Paule, Funkzeile, Aufträge, Erfolge, Ränge und Gewinnmeldungen.", "Zusammengesetzte Meldungen mit Namen und Zahlen werden ebenfalls übersetzt.", "Nur das Versionsprotokoll bleibt auf Deutsch.", "Kleine Grammatikfehler in Neustadt, Treibgut und Eisenfront behoben."] },
  { v: "0.5.1", date: "25.10.2026", title: "Neuer Start-Knopf", items: ["Der Start-Knopf ist moderner und gibt mehr Rückmeldung: Er federt beim Drücken ein und schickt eine Lichtwelle los, beim Drehen läuft ein Lichtbogen um ihn herum und das Symbol dreht sich mit.", "Bei einem Gewinn leuchtet der Knopf golden auf. Geht gerade nichts, zum Beispiel weil der Einsatz zu hoch ist, schüttelt er kurz den Kopf.", "Am Knopf steht jetzt, wie viele Auto-Drehs oder Freispiele noch übrig sind. Auf dem Handy vibriert er beim Drücken leicht."] },
  { v: "0.5.0", date: "25.10.2026", title: "Sprachen", items: ["Neue Sprachauswahl oben neben „Ton“ und im Startbildschirm: Deutsch, Englisch, Spanisch, Japanisch, Russisch, Niederländisch und Griechisch. Die Wahl gilt für alle vier Welten.", "Übersetzt sind bisher Knöpfe, Menüs, Überschriften und kurze Hinweise. Regeln, Hilfe und Sprüche folgen.", "Eigenes Symbol im Browser-Tab für jede Welt."] },
  { v: "0.4.2", date: "25.10.2026", title: "Welt-Menü", items: ["Im Welt-Menü steht bei Neustadt jetzt das neue Grundspiel: die Stadtrundfahrt mit Würfeln, Stadtbus und Grundstücken."] },
  { v: "0.4.1", date: "25.10.2026", title: "Vierte Welt", items: ["Im Welt-Menü gibt es jetzt auch Neustadt, ein Städtebau-Spiel mit eigenem Grundspiel zum Hochstapeln."] },
  { v: "0.4.0", date: "25.10.2026", title: "Drei Fahrzeuge", items: ["Neue Fahrzeugklassen: Floß, Katamaran und Schoner, jedes mit eigenem Aussehen.", "Umsteigen geht, wenn das aktuelle Fahrzeug voll ausgebaut ist (45/45) und du den Rang erreicht hast: Rang 8 für den Katamaran, Rang 14 für den Schoner.", "Das neue Fahrzeug startet als Wrack mit teureren Teilen. Seine Wirkung baut auf dem alten auf, nichts geht verloren.", "Höhere Einsätze: bis 250 mit dem Katamaran, bis 1.000 mit dem Schoner.", "Handy: Muscheln, Einsatz und Start-Knopf bleiben unten immer sichtbar, alles ist kompakter, und schnelles Tippen zoomt nicht mehr hinein."] },
  { v: "0.3.1", date: "25.10.2026", title: "Dritte Welt", items: ["Im Welt-Menü gibt es jetzt auch Eisenfront: eine Werkstatt, in der du einen rostigen Panzer wieder flottmachst."] },
  { v: "0.3.0", date: "25.10.2026", title: "Fangnetz", items: ["Neues Grundspiel statt Walzen: ein 6×5-Fangnetz. Ab 5 gleichen Funden, die sich berühren, landet ein Schwarm im Netz.", "Nachfang: Danach rutscht alles nach unten, neues Treibgut fällt nach, und jede weitere Welle zahlt mehr (×1, ×2, ×3, ×5).", "Freispiele über 3 Flaschenposten: Der Nachfang-Multiplikator startet bei ×2, steigt bis ×10 und bleibt die ganze Runde erhalten.", "Treibkisten und Strudel starten ab 3 Stück im Netz ihre Bonusspiele. Die Hilfsmöwe wirft Rettungsringe ins Netz.", "Rustikale Geräusche: Holz, Wasser, Tau, Schiffsglocke und Marimba statt Synthesizer.", "Klick aufs Meer wirft jetzt einen Haken an der Leine statt eines Lasers.", "Die Lagune bewegt sich ruhiger. Mit besserem Segel wird das Floß schneller."] },
  { v: "0.2.0", date: "25.10.2026", title: "Rustikal", items: ["Neuer Look: Holzplanken, Messingnägel, Taurahmen um die Walzen und Funkmeldungen auf Papier.", "Neue Schriften mit Seefahrer-Charme.", "Eigene Musik: Seemannslied mit Akkordeon im 6/8-Takt, ruhige Lagerfeuer-Gitarre und ein fröhliches Inselfest mit Steeldrum.", "Neuer Knopf „Welt“: Wechsel zu Sternenwrack und zurück, auch vom Startbildschirm aus."] },
  { v: "0.1.0", date: "25.10.2026", title: "Erste Fassung", items: ["Treibgut ist da: Survival auf dem Meer mit Floß, Inseln und Treibgut.", "Basiert auf dem Spielsystem von Sternenwrack (Beta 0.10.0): Freifahrten mit steigendem Multiplikator, Risikoleiter, Bernstein und Kräutertränke, Expeditionen und vieles mehr.", "Eigenes Floß mit fünf Ausbaubereichen: Floß, Segel, Ausguck, Lager und Feuerstelle.", "Papagei Koko begleitet dich und erklärt im Hilfemodus alles.", "Treibfässer ziehen an der Lagune vorbei und lassen sich mit dem Haken an Bord holen."] },
'''

# Zeilen mit Grammatik oder eigenem Inhalt (genau ersetzen, vor der Wortliste)
PHRASES = [
    ('const FINDS = { clang: "Metallischer Klopfer", rat: "Schrottratte", pilot: "Plaudernder Pilot", boost: "Nachbrenner", reactor: "Reaktor-Überladung", scanner: "Sonar-Puls", duck: "Gummiente im All", laser: "Bordlaser", roll: "Fassrolle" };',
     'const FINDS = { clang: "Klopfender Balken", rat: "Schiffsratte", pilot: "Plaudernder Schiffbrüchiger", boost: "Rückenwind", reactor: "Funkenflug", scanner: "Ruf vom Ausguck", duck: "Gummiente im Meer", laser: "Wurfhaken", roll: "Kenterrolle" };'),
    ('const SCAN_LINES = ["Scan: 0,3 % Chance auf Weltraumkaffee.", "Scan: Ein Asteroid winkt. Vermutlich.", "Scan: Keine Konkurrenz in Reichweite.", "Scan: Spuren von verlorenen Socken.", "Scan: Signal entdeckt ... ach nein, das war der Toaster."];',
     'const SCAN_LINES = ["Ausguck: Land in Sicht! ... ach nein, das war ein Wal.", "Ausguck: Eine Möwe winkt. Vermutlich.", "Ausguck: Keine Haie in Sicht.", "Ausguck: Spuren von verlorenen Socken.", "Ausguck: Da hinten treibt eine Kokosnuss."];'),
    ('const SHIP_A = ["Rost", "Schrott", "Sternen", "Nebel", "Funken", "Blech", "Glut", "Eisen", "Nacht", "Kometen", "Staub", "Plasma", "Mond", "Polar", "Donner", "Flicken", "Nieten", "Asche"];',
     'const SHIP_A = ["Salz", "Treib", "Muschel", "Möwen", "Brandungs", "Sturm", "Tang", "Korallen", "Kokos", "Flaschen", "Strand", "Sonnen", "Nebel", "Wellen", "Bambus", "Planken", "Riff", "Ebbe"];'),
    ('const SHIP_B = ["krähe", "möwe", "falke", "fuchs", "käfer", "wal", "biene", "otter", "dachs", "hummel", "elster", "motte", "eule", "katze", "ratte", "spatz", "hai", "rabe"];',
     'const SHIP_B = ["möwe", "krabbe", "qualle", "otter", "robbe", "hai", "rochen", "muschel", "brise", "boje", "planke", "kiste", "flosse", "perle", "kogge", "schnecke", "wal", "ente"];'),
    ('const SHIP_FIX = ["Zweite Chance", "Letzter Funke", "Glückspilz", "Alte Liebe", "Klapperkiste", "Hoffnungsschimmer", "Tante Erna", "Unsinkbar II", "Lucky Strike", "Halbe Miete", "Sternschnuppe", "Nimmermüde"];',
     'const SHIP_FIX = ["Zweite Chance", "Letzter Strohhalm", "Kokosnuss", "Nasse Füße", "Seeigel", "Tante Erna", "Unsinkbar II", "Lucky Strike", "Halbe Miete", "Sonnenschein", "Treibholz Royal", "Bambusbaron"];'),
]

WORDS = [
    (r"STERNENWRACK", "TREIBGUT"), (r"Sternenwrack", "Treibgut"),
    (r"STERNENSCHATZ", "PIRATENSCHATZ"), (r"Sternenschatz", "Piratenschatz"),
    (r"Sternenstaub", "Bernstein"), (r"Sternschnuppen", "Treibfässer"), (r"Sternschnuppe", "Treibfass"),
    (r"Sternenkristall", "Bernstein"), (r"Sternenkarte", "Seekarte"),
    (r"Wild-Kristalle\b", "Rettungsringe"), (r"Wild-Kristall", "Rettungsring"),
    (r"Kristalldrohnen", "Hilfsmöwen"), (r"Kristalldrohne", "Hilfsmöwe"),
    (r"Frachtkapseln", "Treibkisten"), (r"Frachtkapsel", "Treibkiste"), (r"Kapselbergung", "Kistenbergung"), (r"Kapseln", "Kisten"), (r"Kapsel", "Kiste"),
    (r"Hyperraumsprung", "Strudelfahrt"), (r"Hyperraum", "Strudel"), (r"Sprungkerne", "Strudel"), (r"Sprungkern", "Strudel"),
    (r"Schiffsregister", "Floßregister"), (r"Schiffsname", "Floßname"), (r"Schiffsklasse", "Floßklasse"), (r"Schiffskenner", "Floßkenner"),
    (r"Schiffs-", "Floß-"), (r"Schiffes", "Floßes"), (r"Schiffe\b", "Flöße"), (r"Schiff\b", "Floß"),
    (r"Kommandopult", "Floßdeck"), (r"Bordzentrale", "Strandhütte"), (r"Bordbuch", "Logbuch"), (r"Bordroboter", "Bordpapagei"),
    (r"BIP-BOOST", "KOKO-BOOST"), (r"Bip-Boost", "Koko-Boost"), (r"\bBip\b", "Koko"),
    (r"Bergungsgilde", "Strandgilde"), (r"Pilotenrang", "Seefahrerrang"),
    (r"Boost-Labor", "Kräuterhütte"), (r"KSV-7", "SOS-7"), (r"Rostkrähe", "Salzbrise"),
    (r"Spielcredits", "Spielmuscheln"), (r"(?<![A-Za-z])Credits", "Muscheln"), (r"\bCredit\b", "Muschel"),
    (r"ins All\b", "aufs Meer"), (r"im All\b", "auf dem Meer"), (r"Weltraum", "Meer"),
]

PHRASES += [
    # Wurf statt Scan
    ('<span id="spinLabel">Scan</span>', '<span id="spinLabel">Werfen</span>'),
    (': fsMode ? "Frei" : "Scan";', ': fsMode ? "Frei" : "Werfen";'),
    ('"Scanne Frachtraum …"', '"Netz ist draußen …"'),
    ('"Frachtraum leer. Neuer Scan?"', '"Netz leer. Neuer Wurf?"'),
    ('"Frachtraum leer. Nur Staub."', '"Lager leer. Nur Sand."'),
    ('"Scan: Antenne verbogen. Ich sehe nur Rauschen."', '"Ausguck: Nur ein Stock. Ich sehe nur Wasser."'),
    ("Scannt mehrmals hintereinander. Freigeschaltet über den Antrieb.", "Wirft mehrmals hintereinander aus. Freigeschaltet über das Segel."),
    ('"Auto-Scan"', '"Auto-Wurf"'),
    ("beim Scannen im jeweiligen Sektor auf", "beim Auswerfen auf der jeweiligen Insel auf"),
    ("Manchmal fallen sie beim Scannen ab.", "Manchmal landen sie beim Auswerfen im Netz."),
    ('<b id="rankTitle">Kadett</b>', '<b id="rankTitle">Schiffbrüchiger</b>'),
    # Flaschenpost
    ('"Funk: Weiteres Notsignal geortet. Kurs gehalten." : "Funk: Notsignal geortet. Freie Bergungsfahrten genehmigt."', '"Funk: Noch eine Flaschenpost! Die Fahrt geht weiter." : "Funk: Flaschenpost gefunden! Freie Fahrt mit Rückenwind."'),
    ('tier: retrigger ? "Erneutes Notsignal" : "Notsignal empfangen"', 'tier: retrigger ? "Noch eine Flaschenpost" : "Flaschenpost gefunden"'),
    ('`Notsignal erneut empfangen: +${award} Freispiele!` : `${scatterReels} Notsignale empfangen: ${award} Freispiele!`', '`Noch eine Flaschenpost: +${award} Freispiele!` : `${scatterReels} Flaschenposten gefunden: ${award} Freispiele!`'),
    ('"Notsignal. Landen 3 oder mehr irgendwo, startet der Notruf mit Freispielen', '"Flaschenpost. Landen 3 oder mehr irgendwo, startet eine Runde Freispiele'),
    ('"Funk: Notsignal aufgefangen. Quelle unbekannt."', '"Funk: Eine Flaschenpost treibt vorbei. Absender unbekannt."'),
    # Strudel
    ("starten den Hyperraumsprung mit Multiplikator", "starten die Strudelfahrt mit Multiplikator"),
    ('id="jumpBtn" ${spinning || busy || state.exped ? "disabled" : ""}>Hyperraumsprung</button>', 'id="jumpBtn" ${spinning || busy || state.exped ? "disabled" : ""}>Hinsegeln</button>'),
    ("Erst wenn dein Schiff von der Expedition zurück ist.", "Erst wenn dein Floß von der Expedition zurück ist."),
    # Hilfsmöwe statt Bergungslaser
    ("Ohne Gewinn kann manchmal der Bergungslaser einen blockierenden Brocken wegschießen und einen Wild-Kristall erschaffen.", "Ohne Gewinn kommt manchmal die Hilfsmöwe, pickt einen störenden Fund weg und lässt einen Rettungsring fallen."),
    ("Den erschafft nur der Bergungslaser.", "Den bringt nur die Hilfsmöwe."),
    ('"Lass den Bergungslaser zuschlagen"', '"Lass die Hilfsmöwe helfen"'),
    ('effect: "Bergungslaser 4× so oft"', 'effect: "Hilfsmöwe 4× so oft"'),
    ('"Bergungslaser! Störendes Symbol wird abgebaut …"', '"Hilfsmöwe! Sie pickt den störenden Fund weg …"'),
    ('radio("Funk: Bergungsdrohne im Anflug. Laser frei.", true);', 'radio("Funk: Eine Möwe kreist über dem Netz.", true);'),
    ('`${lasered ? "Laser · " : ""}', '`${lasered ? "Möwe · " : ""}'),
    ('<h3>Bergungslaser · Wild-Kristall</h3><p>Hat ein einziges Symbol auf Schacht 3 einen Gewinn verhindert, kann manchmal eine Drohne anfliegen. Sie schneidet das Symbol heraus und lässt einen Wild-Kristall wachsen, der für jedes Fundsymbol zählt.',
     '<h3>Hilfsmöwe · Rettungsring</h3><p>Hat ein einziges Symbol auf Walze 3 einen Gewinn verhindert, kommt manchmal eine Möwe angeflogen. Sie pickt das Symbol weg und lässt einen Rettungsring fallen, der für jeden Fund zählt.'),
    # Risiko-Farben
    ('style="--gc:#4fe3ff">Cyan</button>', 'style="--gc:#4fe3ff">Türkis</button>'),
    ('style="--gc:#ff4fd8">Magenta</button>', 'style="--gc:#ff4fd8">Koralle</button>'),
    ("Cyan oder Magenta raten", "Türkis oder Koralle raten"),
    # Lagune statt Hangar
    ('"Zurück im Hangar!"', '"Zurück in der Lagune!"'),
    ('["#shipview", () => ["Hangar",', '["#shipview", () => ["Lagune",'),
    # Inseln statt Sektoren
    ('<h3>Expeditionen und Sektoren</h3><p>Schick dein Schiff in Echtzeit auf Expedition. Die Belohnung wächst mit dem Ausbau und dem Sektor. Neue Sektoren schaltest du über deinen Rang frei. Jeder hat',
     '<h3>Expeditionen und Inseln</h3><p>Schick dein Floß in Echtzeit auf Expedition. Die Belohnung wächst mit dem Ausbau und der Insel. Neue Inseln schaltest du über deinen Rang frei. Jede hat'),
    ('"Klick auf einen freigeschalteten Sektor, um dorthin zu springen."', '"Klick auf eine freigeschaltete Insel, um hinzusegeln."'),
    ('"Seltene Funde aus Sektoren.', '"Seltene Funde von den Inseln.'),
    # Floßteile
    ("Ein starker Rumpf bringt mehr zurück.", "Ein starkes Floß bringt mehr zurück."),
    ('"Embleme für den Rumpf."', '"Embleme fürs Floß."'),
    ("· Reaktor ausbauen", "· Feuerstelle ausbauen"),
    ("`Freischalten mit Antrieb Stufe", "`Freischalten mit Segel Stufe"),
    ('"Freischalten mit Antrieb Stufe 2"', '"Freischalten mit Segel Stufe 2"'),
    ('"Schnellere Walzen. Wird vom Antrieb freigeschaltet."', '"Schnelleres Netz. Wird vom Segel freigeschaltet."'),
    ("Höhere Einsätze schaltet der Reaktor frei.", "Höhere Einsätze schaltet die Feuerstelle frei."),
    ('"Der Reaktor deines Schiffs bestimmt den Höchsteinsatz. Rüste ihn im Hangar aus."', '"Die Feuerstelle deines Floßes bestimmt den Höchsteinsatz. Rüste sie in der Lagune aus."'),
    ('const CATS_HELP = { hull: "Rumpf: schützt beim Bankrott, du bekommst mehr zurück.", engine: "Antrieb: schaltet Auto-Scans und Turbo frei.", scanner: "Sensorik: erhöht alle Liniengewinne ein bisschen.", cargo: "Frachtraum: mehr Gewinn in Bonusspielen.", reactor: "Reaktor: höhere Einsätze." };',
     'const CATS_HELP = { hull: "Floß: schützt bei Pleite, du bekommst mehr zurück.", engine: "Segel: schaltet Auto-Würfe und Turbo frei.", scanner: "Ausguck: erhöht alle Liniengewinne ein bisschen.", cargo: "Lager: mehr Gewinn in Bonusspielen.", reactor: "Feuerstelle: höhere Einsätze." };'),
    ("Jeder Scan füllt den Staubmesser", "Jeder Wurf füllt den Bernsteinmesser"),
    ("Im Boost-Labor tauschst du ihn", "In der Kräuterhütte tauschst du ihn"),
    ("Ausgeben im Boost-Labor unten.", "Ausgeben in der Kräuterhütte unten."),
    ("Drei Lose im Kiosk: Schrottfund (20), Kristallfieber (100) und Hyperraum-Jackpot (500).", "Drei Lose im Kiosk: Strandfund (20), Bernsteinfieber (100) und Piraten-Jackpot (500)."),
    ('name: "Schrottfund"', 'name: "Strandfund"'), ('name: "Kristallfieber"', 'name: "Bernsteinfieber"'), ('name: "Hyperraum-Jackpot"', 'name: "Piraten-Jackpot"'),
    ('{ id: "neon", name: "Neonfahrt"', '{ id: "neon", name: "Brandung"'), ('{ id: "deep", name: "Tiefraum"', '{ id: "deep", name: "Tiefsee"'), ('{ id: "funk", name: "Schrottplatz-Funk"', '{ id: "funk", name: "Hafen-Funk"'),
    ('name: "Überladener Scanner"', 'name: "Adlerauge-Tee"'), ('name: "Drohnenschwarm"', 'name: "Möwenfutter"'), ('name: "Signalverstärker"', 'name: "Strömungskraut"'), ('name: "Gildenlizenz"', 'name: "Weisheitswurzel"'), ('name: "Schatzpeilung"', 'name: "Schatznase"'),
    ('effect: "Notsignale 2,5× so häufig"', 'effect: "Flaschenposten 2,5× so häufig"'),
    ('· Kristalle <b id="fsStick">0</b>/3 ·', '· Ringe <b id="fsStick">0</b>/3 ·'),
    ('"Multiplikator und Kristalle bleiben"', '"Multiplikator und Ringe bleiben"'),
    ("Feste Wild-Kristalle: ${fsSticky.length} von 3.", "Feste Rettungsringe: ${fsSticky.length} von 3."),
    ("Ein Schrotthändler überlässt dir ein neues Wrack", "Ein Strandhändler überlässt dir ein neues Wrack"),
    ("Der Schrotthändler trägt dein neues Schiff ins Register ein.", "Der Strandhändler trägt dein neues Floß ins Register ein."),
    ("Funk: Schrotthändler hat", "Funk: Strandhändler hat"),
    ("Die Bergungsgilde braucht deinen Namen und den Namen deines Schiffs.", "Die Strandgilde braucht deinen Namen und den Namen deines Floßes."),
    ("Dein neues Wrack braucht einen Namen.", "Dein neues Floß braucht einen Namen."),
    ('"Neues Wrack registrieren"', '"Neues Floß registrieren"'),
    ("Keine Credits und keine Teile mehr zum Verschrotten. Dein Schiff treibt ab.", "Keine Muscheln und keine Teile mehr zum Verkaufen. Dein Floß zerfällt in der Brandung."),
    ('>Schiff verloren</h2>', '>Floß verloren</h2>'),
    ('Funk: Werft bestätigt ${c.name}', 'Funk: Die Werft bestätigt ${c.name}'),
]

PHRASES += [
    ('''const RADIO = [
  "Funk: Händler auf Station Kepler-9 zahlt gut für Sternenkristalle.",
  "Funk: Ionensturm in Sektor 7. Scanner zeigen erhöhte Aktivität.",
  "Funk: Ein Gildenfrachter meldet treibende Kapseln im Asteroidengürtel.",
  "Funk: Werft Hadal-3 bietet Plasmatriebwerke an. Nur gegen Credits.",
  "Funk: Eine Flaschenpost treibt vorbei. Absender unbekannt.",
  "Funk: Sprungkern-Anomalie bei Tau Ceti. Navigation bleibt vorsichtig.",
  "Funk: Schrotthändler Varn sucht Reaktorkerne. Fragt nicht woher.",
  "Funk: Wrackfeld bei Orion-Riff gesichtet. Konkurrenz ist unterwegs.",
  "Funk: Gilde erinnert: Ein starker Rumpf rettet dir beim Notverkauf den Hals.",
];''', '''const RADIO = [
  "Funk: Der Händler auf der Kokosinsel zahlt gut für Bernstein.",
  "Funk: Sturmwarnung im Norden. Segel festzurren.",
  "Funk: Ein Fischkutter meldet treibende Kisten bei der Sandbank.",
  "Funk: Die Werft am Hafen bietet neue Segel an. Nur gegen Muscheln.",
  "Funk: Eine Flaschenpost treibt vorbei. Absender unbekannt.",
  "Funk: Haiflossen in Sicht. Füße bitte an Bord lassen.",
  "Funk: Strandhändler Varn sucht Thunfisch. Fragt nicht woher.",
  "Funk: Wrackfeld vor der Treibgutbucht gesichtet. Konkurrenz ist unterwegs.",
  "Funk: Die Gilde erinnert: Ein starkes Floß rettet dir beim Notverkauf den Hals.",
];'''),
    ('''const PILOT_LINES = [
  ["Ist das ... Rost oder Ketchup?", "Ich hab gehört, Schiffe fliegen besser mit Rumpf.", "Bitte nicht klopfen, das hält gerade so.", "Mein Sitz ist ein umgedrehter Eimer."],
  ["Die Flicken halten! Meistens.", "Kaffee ist alle. Moral sinkt.", "Klebeband ist auch ein Bauteil.", "Hast du den Funk gehört? Wir sind berühmt. Fast."],
  ["Das fühlt sich schon fast wie ein echtes Schiff an.", "Schöne Panzerung. Schade um den Kaffee.", "Wenn das die Gilde sieht ...", "Kurs halten, Kapitän!"],
  ["Ich wurde geboren, um dieses Schiff zu fliegen.", "Hörst du das? Das ist der Klang von Erfolg.", "Legenden parken nicht, sie schweben.", "Ich hab mir Sonnenbrillen für den Plasmaschweif gekauft."],
];''', '''const PILOT_LINES = [
  ["Ist das ... Seetang oder mein Frühstück?", "Ich hab gehört, Flöße schwimmen besser mit Brettern.", "Bitte nicht klopfen, das hält gerade so.", "Mein Sitz ist eine halbe Kokosnuss."],
  ["Die Knoten halten! Meistens.", "Wasser ist alle. Also, das trinkbare.", "Tau ist auch ein Bauteil.", "Hast du den Funk gehört? Wir sind berühmt. Fast."],
  ["Das fühlt sich schon fast wie ein echtes Schiff an.", "Schöne Reling. Schade um meinen Hut.", "Wenn das die Gilde sieht ...", "Kurs halten, Kapitän!"],
  ["Ich wurde geboren, um auf diesem Floß zu segeln.", "Hörst du das? Das ist das Rauschen des Erfolgs.", "Legenden ankern nicht, sie treiben mit Stil.", "Ich hab mir eine Sonnenbrille gegen die Gischt gekauft."],
];'''),
]

WORDS += [
    (r"Freifahrten", "Freispiele"), (r"Bips\b", "Kokos"),
    (r"Notsignale", "Flaschenposten"), (r"Notsignal", "Flaschenpost"),
    (r"Scans\b", "Würfe"), (r"Scan\b", "Wurf"),
    (r"Schrotthändler", "Strandhändler"),
    (r"Bergungslaser", "Hilfsmöwe"), (r"im Hangar", "in der Lagune"),
]

PHRASES += [
    ("Einsatz wählen und Scan starten.", "Einsatz wählen und Netz auswerfen."),
    ('"Scan starten"', '"Netz auswerfen"'),
    ("Starte deinen ersten Scan.", "Wirf dein Netz zum ersten Mal aus."),
    ("Ein Klick auf Scan bricht ab.", "Ein Klick auf Werfen bricht ab."),
    ('viewBox="10 20 360 190" role="img" aria-label="Dein Bergungsschiff" id="shipsvg"', 'viewBox="48 2 304 152" role="img" aria-label="Dein Floß" id="shipsvg"'),
    ('viewBox="10 20 360 190" role="img" aria-label="Dein Bergungsschiff in Großansicht"', 'viewBox="48 2 304 152" role="img" aria-label="Dein Floß in Großansicht"'),
    ('aria-label="Sternenkarte mit vier Sektoren"', 'aria-label="Seekarte mit vier Inseln"'),
    ('"Schnell anklicken! Der Bordlaser holt sie runter und du bekommst Sternenstaub. Goldene bringen mehr."', '"Schnell anklicken! Der Wurfhaken holt das Fass an Bord, drin ist Bernstein. Goldene Fässer bringen mehr."'),
    ('"Sektoren mit eigenen Farben und Musikstimmung. Neue Sektoren schaltest du mit Stufen frei."', '"Inseln mit eigenem Wetter, eigenen Farben und eigener Musikstimmung. Neue Inseln schaltest du mit Stufen frei."'),
]
WORDS[:0] = [(r"deines Schiffs", "deines Floßes"), (r"Im Boost-Labor", "In der Kräuterhütte"), (r"im Boost-Labor", "in der Kräuterhütte"), (r"ins Boost-Labor", "in die Kräuterhütte")]

PHRASES += [
    (".starmap { border-radius: 14px; overflow: hidden; border: 1px solid var(--line); background: radial-gradient(ellipse at 30% 30%, rgba(139,108,255,.22), transparent 60%), radial-gradient(ellipse at 80% 80%, rgba(255,79,216,.12), transparent 60%), #05060f; }",
     ".starmap { border-radius: 14px; overflow: hidden; border: 1px solid rgba(232,211,162,.35); background: radial-gradient(ellipse at 30% 30%, rgba(63,224,197,.25), transparent 60%), radial-gradient(ellipse at 80% 80%, rgba(47,143,255,.25), transparent 60%), repeating-linear-gradient(0deg, rgba(255,255,255,.03) 0 1px, transparent 1px 22px), repeating-linear-gradient(90deg, rgba(255,255,255,.03) 0 1px, transparent 1px 22px), #0a3a4a; }"),
    ("""  for (let i = 0; i < 70; i++) { const x = (i * 97) % 400, y = (i * 53 + (i * i) % 37) % 230; stars += `<circle cx="${x}" cy="${y}" r="${(i % 3) * .4 + .4}" fill="#fff" opacity="${.2 + (i % 5) * .1}"/>`; }""",
     """  for (let i = 0; i < 34; i++) { const x = (i * 97) % 400, y = (i * 53 + (i * i) % 37) % 230; stars += `<path d="M${x},${y} q3,-3 6,0 t6,0" stroke="#bfeee6" stroke-width="1" fill="none" opacity="${.15 + (i % 4) * .07}"/>`; }
  stars += `<g transform="translate(372 196)" opacity=".5"><circle r="16" fill="none" stroke="#e8d3a2" stroke-width="1"/><path d="M0,-20 L4,0 L0,20 L-4,0 Z" fill="#e8d3a2"/><path d="M-20,0 L0,3 L20,0 L0,-3 Z" fill="#e8d3a2" opacity=".6"/><text y="-24" text-anchor="middle" font-size="8" fill="#e8d3a2">N</text></g>`;"""),
    ("""        <circle cx="${x.x}" cy="${x.y}" r="26" fill="${x.color}" opacity="${ok ? .12 : .05}"/>""",
     """        <path d="M${x.x - 30},${x.y + 6} q8,-22 30,-20 q24,2 30,20 q-30,10 -60,0z" fill="${ok ? "#d9c08a" : "#5a6a6a"}" opacity="${ok ? .55 : .3}"/><circle cx="${x.x}" cy="${x.y}" r="26" fill="${x.color}" opacity="${ok ? .12 : .05}"/>"""),
]
WORDS += [(r"Lackierungen", "Anstriche"), (r"Lackierung", "Anstrich"), (r"verschrottet", "verkauft"), (r"Farben für dein Schiff", "Farben für dein Floß")]

PHRASES += [
    ('"Bereit für den ersten Sprung."', '"Bereit für den ersten Strudel."'),
    ('level === 0 ? "Sprung berechnen" : "Nächster Sprung"', 'level === 0 ? "Ins Ruder greifen" : "Tiefer in den Strudel"'),
    ("`Sprung gelungen! Weiter in ${RINGS[level].name}.", "`Geschafft! Weiter in ${RINGS[level].name}."),
    ("drehst du das Navigationsrad.", "drehst du das Steuerrad."),
    ("Dreh das Navigationsrad.", "Dreh das Steuerrad."),
    ('aria-label="Navigationsrad', 'aria-label="Steuerrad'),
]

PHRASES += [
    ('''const pod = `<svg viewBox="0 0 40 40"><rect x="6" y="11" width="28" height="18" rx="9" fill="#ffc94a" stroke="#7a5608" stroke-width="1.5"/><path d="M14 11v18M26 11v18" stroke="#7a5608" stroke-width="1.5"/><rect x="17" y="15.5" width="6" height="9" rx="1.4" fill="#2e2104"/></svg>`;''',
     '''const pod = `<svg viewBox="0 0 40 40"><path d="M6 14 h28 v17 h-28z" fill="#9a6a32" stroke="#ffc94a" stroke-width="1.6" stroke-linejoin="round"/><path d="M6 14 l4 -5 h20 l4 5z" fill="#c08a48" stroke="#ffc94a" stroke-width="1.4" stroke-linejoin="round"/><path d="M6 22 h28 M14 14 v17 M26 14 v17" stroke="#5a3a14" stroke-width="1.4"/><rect x="17.5" y="18.5" width="5" height="7" rx="1.2" fill="#ffc94a"/><path d="M4 33 q4 -2.5 8 0 t8 0 t8 0 t8 0" stroke="#7fc8ff" stroke-width="1.3" fill="none" opacity=".8"/></svg>`;'''),
    ('aria-label="Kapsel ${i + 1} öffnen"', 'aria-label="Kiste ${i + 1} öffnen"'),
]
