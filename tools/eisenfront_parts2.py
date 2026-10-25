# Eisenfront Teil 2: Inhalte und Texte (Quelle ist die fertige Treibgut-Datei)

BIP_EF = r'''const BIP = {
  hello: [["happy", "Wuff! Hallo Kapitän! Ich bin <b>Rex</b>, der Werkstatthund. Ich pass auf die Schrauben auf. Meistens."], ["happy", "Rex meldet sich zum Dienst! Schwanz wedelt, Ohren gespitzt."]],
  small: [["happy", "Ein kleiner Fund ist auch ein Fund!"], ["happy", "Klonk! Ich mag dieses Geräusch."], ["happy", "Jede Schraube zählt. Ich zähl mit!"]],
  good: [["happy", "Schöner Fund! Ich dreh mich vor Freude im Kreis."], ["happy", "Das lief gut! Merkst du, wie der Panzer schnurrt?"], ["excited", "Wuff! Gute Bergung!"]],
  big: [["excited", "WOAH! Das war eine <b>große Bergung</b>! Mein Schwanz wedelt von allein!"], ["excited", "Ich hab das gesehen! Das war richtig stark!"], ["wow", "Sag mal ... bist du Profi-Mechaniker?"]],
  mega: [["wow", "MEGA! Ich ... ich muss kurz bellen. WUFF!"], ["excited", "Das erzähl ich allen Hunden in der Kaserne!"]],
  laser: [["excited", "Die Brieftaube hat geliefert! Ein Schraubenschlüssel!"], ["happy", "Schraubenschlüssel! Der passt überall. Wie ich."]],
  streak3: [["excited", "Drei in Folge! Der Motor läuft heiß. Im guten Sinne."], ["happy", "Strähne läuft! Ich spür das bis in die Pfoten."]],
  streak5: [["wow", "Fünf in Folge?! Ich hab mit allen Pfoten nachgezählt. Stimmt wirklich!"]],
  broke: [["normal", "Strähne vorbei. War trotzdem schön, solange sie lief."], ["normal", "Na ja, Strähnen kommen und gehen. Wie Postboten."]],
  dry: [["sad", "Gerade läuft's zäh, ich weiß. Glück hat leider kein Gedächtnis, aber ich bin trotzdem hier."], ["sad", "Puh, Durststrecke. Wenn du magst, schau dir den Panzer an. Da gibt's lustige Sachen."], ["normal", "Kopf hoch, Kapitän. Schrauben sind nur Schrauben, Spaß ist das, was zählt."], ["sad", "Pech gehabt. Ich leg dir die Pfote aufs Knie."]],
  fs: [["excited", "Sondereinsatz! Freispiele! Ich hol schon mal das Werkzeug!"], ["excited", "Depesche angekommen! Jetzt wird's spannend!"]],
  starFirst: [["wow", "Da schwebt eine <b>Kiste am Fallschirm</b>! Schnell, klick drauf, dann fangen wir sie ab. Da sind Orden drin!"]],
  star: [["excited", "Nachschub von oben! Schnapp ihn dir!"], ["happy", "Da kommt eine Kiste geflogen! Fang sie!"]],
  sticky: [["wow", "Ein fester Schraubenschlüssel! Der bleibt liegen!"], ["excited", "Die Taube hilft! Jetzt wird's richtig gut."]],
  fsend: [["happy", "Sondereinsatz vorbei. Hat Spaß gemacht!"], ["happy", "Das war eine schöne Schicht!"]],
  bonusGood: [["excited", "Bonus geschafft! Das war Teamarbeit. Ich hab laut gebellt."], ["happy", "Gut gemacht im Bonusspiel!"]],
  bonusMeh: [["normal", "Nicht der große Fund, aber Bonusspiele sind immer ein kleines Abenteuer."]],
  jackpot: [["wow", "DER GOLDTRESOR! Ich ... ich hab keine Worte. Nur Bellen. WUFF! WUFF!"]],
  upgrade: [["happy", "Schick! Der Panzer sieht gleich zufriedener aus."], ["happy", "Gute Investition, Kapitän!"]],
  bigUpgrade: [["excited", "Großes Upgrade! Schau dir diesen Panzer an! Ich bin ganz stolz."], ["wow", "Ist das noch unsere alte Rostbeule? Kaum wiederzuerkennen!"]],
  rank: [["excited", "Beförderung! Darf ich dich jetzt <b>Chef</b> nennen?"], ["happy", "Neuer Rang! Ich hab dir einen Knochen als Orden zurückgelegt."]],
  mission: [["happy", "Auftrag erledigt! Abgehakt und abgestempelt."], ["happy", "Wieder einer geschafft. Die Gilde ist zufrieden."]],
  scrap: [["sad", "Oh nein, wir mussten ein Teil verkaufen. Das wird wieder, versprochen."], ["sad", "Autsch. Aber hey, er rollt noch!"]],
  lost: [["sad", "Der Panzer ist hinüber ... Aber du hast ein neues Wrack und mich. Wir schaffen das zusammen."]],
  scratchWin: [["excited", "Gerubbelt und gewonnen! Hast du goldene Finger?"], ["happy", "Rubbel-Glück! Herzlichen Glückwunsch!"]],
  scratchLoss: [["normal", "Diesmal nix. Aber das Rubbeln selbst macht schon Spaß, oder?"], ["sad", "Leer. Das Los wollte wohl nicht teilen."]],
  found: [["happy", "Oh, was entdeckt! Du kennst deinen Panzer immer besser."], ["wow", "Huch! Das wusste nicht mal ich."]],
  session: [["normal", "Wir schrauben schon eine ganze Weile. Kurz strecken und was trinken? Ich warte hier."], ["normal", "Kleine Erinnerung von Rex: Pausen gehören zu jeder guten Schicht."]],
  idle: [["normal", "Ich kau solange auf meinem Gummiknochen."], ["happy", "Psst ... klick mal auf den Auspuff."], ["happy", "Unsicher, was etwas macht? Klick auf das <b>?</b> neben mir, dann erkläre ich alles, worüber du fährst."], ["normal", "Ich zähle Schrauben. Bin bei 4.812."]],
  crew: [["excited", "Neue Crew! Endlich jemand zum Ballwerfen."], ["happy", "Willkommen in der Werkstatt! Ich hab dir einen Platz auf der Werkbank freigehalten."]],
  paint: [["happy", "Ooh, schicke Farbe! Steht dem Panzer richtig gut."]],
  expedGo: [["normal", "Gute Fahrt, Panzer! Ich pass hier solange auf."], ["happy", "Expedition gestartet. Ich zähle die Sekunden. Laut."]],
  expedBack: [["excited", "Der Panzer ist zurück! Und er hat was mitgebracht!"]],
  sector: [["wow", "Neue Front! Alles sieht so anders aus. Ich bin ganz aufgeregt."], ["excited", "Angekommen! Ich hab nur ein bisschen gejault."]],
  album: [["wow", "Ein Sammelstück! Das kommt in den Spind. Ganz vorne."]],
  ach: [["excited", "Erfolg freigeschaltet! Ich buddel ein Loch zur Feier."], ["happy", "Wuff! Ein neuer Erfolg. Du wirst immer besser."]],
  daily: [["happy", "Tagesbonus abgeholt! Schön, dass du wieder da bist."]],
  gambleWin: [["wow", "Mutig! Und es hat sich gelohnt!"], ["excited", "Richtig geraten! Meine Ohren stehen."]],
  ladderWin: [["excited", "Hoch hinaus! Mir wird schon schwindelig."], ["wow", "So weit oben! Nicht runterschauen, Kapitän!"]],
  ladderTop: [["wow", "GANZ OBEN! Hundertfach! Ich fasse es nicht!"]],
  ladderLoss: [["sad", "Abgestürzt ... Die Leiter war heute wackelig."], ["sad", "Autsch. Aber hey, der Ausblick war schön."]],
  gambleLoss: [["sad", "Oh je. Das Risiko war echt 50 zu 50, diesmal leider gegen uns."]],
  dustFirst: [["wow", "Oh! Dein erster <b>Orden</b>! Der ist super selten. In der Feldküche kannst du ihn eintauschen."]],
  boostOn: [["excited", "Ration wirkt! Jetzt aber schnell, die Uhr tickt!"], ["happy", "Ui, das kribbelt im Fell. Boost aktiv!"]],
  boostEnd: [["normal", "Der Boost ist abgelaufen. War schön, solange er hielt."]],
  charging: [["normal", "Ich sammle schon mal Glück für dich. Siehst du den Balken neben mir?"], ["happy", "Halbe Glücksladung! Ich wedel extra doll."]],
  boostReady: [["wow", "REX-BOOST! Volle Glücksladung! Der nächste Schub gewinnt garantiert!"], ["excited", "Genug Pech gehabt! Ich hab dir Glück ins Lager getragen. Nächster Schub gewinnt!"]],
  boostWin: [["excited", "Siehste! Auf Rex ist Verlass!"], ["happy", "Rex-Boost geliefert! Gern geschehen, Kapitän."]],
  pet: [["happy", "Hihi! Das kitzelt!"], ["happy", "Wuff! Danke!"], ["excited", "Noch mal! Noch mal!"], ["happy", "Ich mag dich auch, Kapitän."], ["wow", "Hinter den Ohren! Genau da!"]],
};
'''

CATS_EF = r'''const CATS = [
  { id: "hull", name: "Panzerung", color: "#d9b27c", tiers: ["Rostig", "Geflickt", "Verstärkt", "Schwer"],
    icon: `<svg viewBox="0 0 24 24"><path d="M3 14l3-6h12l3 6z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><rect x="2" y="14" width="20" height="6" rx="3" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="7" cy="17" r="1" fill="currentColor"/><circle cx="12" cy="17" r="1" fill="currentColor"/><circle cx="17" cy="17" r="1" fill="currentColor"/></svg>`,
    effect: s => `Notverkauf erstattet ${30 + 5 * s} % des Teilwerts.` },
  { id: "engine", name: "Motor", color: "#ff9a3c", tiers: ["Stotternd", "Diesel", "Turbodiesel", "Gasturbine"],
    icon: `<svg viewBox="0 0 24 24"><rect x="4" y="8" width="14" height="10" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M7 8V5h3v3M12 8V5h3v3M18 11h3v4h-3M4 13H2" stroke="currentColor" stroke-width="1.8" fill="none"/></svg>`,
    effect: s => {
      const un = [[1, "Auto 10"], [2, "Turbo"], [4, "Auto 25"], [7, "Auto 50"]];
      const have = un.filter(u => s >= u[0]).map(u => u[1]);
      const next = un.find(u => s < u[0]);
      return `${have.length ? "Frei: " + have.join(", ") + "." : "Noch nichts freigeschaltet."}${next ? ` Nächstes: ${next[1]} ab Stufe ${next[0]}.` : ""}`;
    } },
  { id: "scanner", name: "Funk", color: "#a7c060", tiers: ["Verbogen", "Antenne", "Periskop", "Radar"],
    icon: `<svg viewBox="0 0 24 24"><path d="M12 21V9" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="7" r="2" fill="currentColor"/><path d="M7 3a7 7 0 0 0 0 8M17 3a7 7 0 0 1 0 8M4 1a11 11 0 0 0 0 13M20 1a11 11 0 0 1 0 13" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round"/></svg>`,
    effect: s => `Liniengewinne +${(0.2 * s).toFixed(1).replace(".", ",")} %.` },
  { id: "cargo", name: "Lager", color: "#ffc94a", tiers: ["Leer", "Kiste", "Kanister", "Vollgepackt"],
    icon: `<svg viewBox="0 0 24 24"><rect x="3" y="9" width="12" height="11" rx="1" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 14h12M9 9v11" stroke="currentColor" stroke-width="1.6"/><path d="M16 8h4l1 2v10h-5z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>`,
    effect: s => `Bonusspiel-Gewinne +${(0.6 * s).toFixed(1).replace(".", ",")} %.` },
  { id: "reactor", name: "Kanone", color: "#e07a4a", tiers: ["Verbogen", "Kurzrohr", "Langrohr", "Präzision"],
    icon: `<svg viewBox="0 0 24 24"><path d="M3 15l3-5h7l2 5z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M13 11h9" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/><rect x="2" y="15" width="15" height="5" rx="2.5" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>`,
    effect: s => { const caps = [10, 10, 10, 25, 25, 25, 50, 50, 50, 100]; const n = [3, 6, 9].find(x => s < x); return `Max. Einsatz ${caps[s]}.${n ? ` ${caps[n]} ab Stufe ${n}.` : ""}`; } },
];
'''

CLASS_TG = 'const CLASS_NAMES = [[1, "Wrack", "#ff6b7a"], [4, "Bretterhaufen", "#ff9a3c"], [8, "Floß", "#ffc94a"], [12, "Segelfloß", "#3fe0c5"], [14, "Hausfloß", "#7fc8ff"], [15, "Legende", "#ff7a59"]];'
CLASS_EF = 'const CLASS_NAMES = [[1, "Wrack", "#ff6b7a"], [4, "Rostbeule", "#ff9a3c"], [8, "Fahrbereit", "#ffc94a"], [12, "Einsatzbereit", "#a7c060"], [14, "Schwerer Brocken", "#b8c7cf"], [15, "Legende", "#e07a4a"]];'

SECTORS_EF = r'''const SECTORS = [
  { id: "orion", name: "Werkhof Nord", rank: 1, color: "#a7c060", transpose: 0, x: 60, y: 160, shape: "depot", land: "#2a2c26", grass: "rgba(140,150,90,.45)",
    sky: ["#3a4652", "#7a8a8e", "#d8c49a"], sun: ["#fff0c8", "rgba(255,214,150,.3)"], cloud: "rgba(200,200,195,.45)", ground: ["#5a5440", "#2a261a"],
    desc: "Der Heimatwerkhof. Hallen, Schrottberge und der Ort, an dem jeder Panzer wieder flottgemacht wird.",
    radio: ["Funk: Im Werkhof Nord ist heute viel los. Werkzeug bereithalten."] },
  { id: "kryos", name: "Schlammfeld", rank: 4, color: "#b8a070", transpose: 2, x: 160, y: 70, shape: "mud", land: "#2a241c", grass: "rgba(110,100,70,.45)",
    sky: ["#2e333a", "#5e6268", "#a8a090"], sun: ["#e8e4d8", "rgba(220,220,210,.2)"], cloud: "rgba(150,150,150,.55)", ground: ["#4a3e2c", "#1e180f"],
    desc: "Zäher Schlamm, kahle Bäume, Nieselregen. Expeditionen bringen hier 25 % mehr.",
    radio: ["Funk: Schlammwarnung. Ketten gut fetten.", "Funk: Ein Frosch sitzt auf dem Funkgerät. Kein Scherz."] },
  { id: "ignis", name: "Wüstenpass", rank: 8, color: "#ffb36b", transpose: -3, x: 265, y: 150, shape: "desert", land: "#7a5a34", grass: "rgba(150,120,70,.4)",
    sky: ["#3a6a9a", "#9ab8c8", "#ffd9a0"], sun: ["#fff6d8", "rgba(255,220,150,.45)"], cloud: "rgba(255,245,230,.4)", ground: ["#c9a46a", "#7a5a34"],
    desc: "Sand, Hitze und Luftflimmern. Expeditionen bringen hier 50 % mehr.",
    radio: ["Funk: Sandsturm am Pass. Luftfilter wechseln nicht vergessen.", "Funk: Die Kühlung läuft heiß. Die Kamele tun so, als wäre nichts."] },
  { id: "xeltar", name: "Eiswald", rank: 12, color: "#b8c7cf", transpose: 5, x: 350, y: 60, shape: "snow", land: "#2a3a3a", grass: "rgba(220,230,235,.5)",
    sky: ["#1e2a3a", "#5a7088", "#c8d8e0"], sun: ["#f4f8ff", "rgba(220,235,255,.3)"], cloud: "rgba(230,238,245,.5)", ground: ["#d8e2e8", "#8a9aa4"],
    desc: "Tiefer Schnee zwischen dunklen Tannen. Niemand weiß, wer hier die alte Werkstatt gebaut hat. Expeditionen bringen hier 75 % mehr.",
    radio: ["Funk: Frost im Eiswald. Motor warm laufen lassen.", "Funk: Spuren im Schnee entdeckt. Vermutlich ein Hase."] },
];
'''

SECTOR_CSS_EF = [
    (':root { --s1: #3fe0c5; --s2: #2f8fff; --s3: #ffb36b; }', ':root { --s1: #a7c060; --s2: #6f8fa8; --s3: #ffb36b; }'),
    ('html[data-sector="kryos"] { --s1: #9fd8ff; --s2: #6f8ea8; --s3: #e0f0f7; }', 'html[data-sector="kryos"] { --s1: #b8a070; --s2: #6a6258; --s3: #d8cfb8; }'),
    ('html[data-sector="xeltar"] { --s1: #8fe07a; --s2: #1f8fbf; --s3: #9ff3d6; }', 'html[data-sector="xeltar"] { --s1: #b8c7cf; --s2: #6f8fa8; --s3: #e8f0f4; }'),
]

CREW_EF = r'''const CREW = [
  { id: "mira", name: "Mira", role: "Schweißerin", cost: 800, color: "#ff9a3c", effect: "Notverkauf erstattet 10 % mehr.",
    art: face("#f1c7a6", `<path d="M14 24 q2 -14 13 -14 q12 0 13 14 q-4 -6 -13 -6 q-9 0 -13 6z" fill="#c2452d"/><rect x="12" y="15" width="30" height="7" rx="2" fill="#3a3d42"/><rect x="17" y="16.5" width="20" height="4" rx="1" fill="#6fa8a0"/>`, { suit: "#5a6a2c", more: `` }),
    lines: ["Wer hat schon wieder mit dem Hammer auf die Kanone geklopft?", "Gib mir zehn Minuten und ein Schweißgerät.", "Der Motor schnurrt wie ein Kätzchen. Ein sehr lautes Kätzchen."] },
  { id: "juno", name: "Juno", role: "Fahrerin", cost: 1200, color: "#a7c060", effect: "Expeditionen sind 25 % schneller.",
    art: face("#8d5a3b", `<path d="M13 28 q-1 -18 14 -18 q15 0 14 18 q-3 -8 -14 -8 q-11 0 -14 8z" fill="#1d1d2b"/><path d="M12 18 h30 l-3 -6 h-24z" fill="#4f5a2c"/>`, { suit: "#4f5a2c", more: `` }),
    lines: ["Ich kenne eine Abkürzung. Sie führt nur ein bisschen durch den Schlamm.", "Kurs gesetzt. Ungefähr.", "Karten lügen nie. Wegweiser schon."] },
  { id: "broesel", name: "Bolle", role: "Feldkoch", cost: 1000, color: "#8fe07a", effect: "Alle XP um 10 % erhöht.",
    art: face("#e9b98f", `<path d="M14 18 q0 -12 13 -12 q13 0 13 12z" fill="#f4f4ee"/><rect x="14" y="16" width="26" height="4" fill="#e0e0d8"/>`, { suit: "#d8d4c8", more: `` }),
    lines: ["Heute gibt's Eintopf. Wie gestern. Und morgen.", "Ich habe den Kessel repariert. Er kocht jetzt auch Kaffee.", "Mahlzeit! Bitte nicht die Gummiente essen."] },
  { id: "kael", name: "Kael", role: "Funker", cost: 1500, color: "#e07a4a", effect: "Aufträge zahlen 20 % mehr.",
    art: face("#e9b98f", `<path d="M14 22 q4 -12 13 -12 q10 0 13 12 l-2 -2 l-3 3 l-3 -4 l-3 4 l-3 -4 l-3 4 l-3 -3z" fill="#5a3a1a"/>`, { suit: "#3a4428", more: `<path d="M12 22 q-2 6 2 10 M42 22 q2 6 -2 10" stroke="#e07a4a" stroke-width="2.4" fill="none"/><rect x="8" y="24" width="5" height="9" rx="2" fill="#3a3d42"/><rect x="41" y="24" width="5" height="9" rx="2" fill="#3a3d42"/>` }),
    lines: ["Die Gilde hat angefunkt. Sie wollen wissen, ob wir noch rollen.", "Ich hab drei neue Aufträge reingefunkt. Gern geschehen.", "Psst, im Funk wird über dich geredet. Positiv!"] },
];
'''

EXPED_EF = r'''const EXPED = [
  { id: "short", name: "Schrottplatz am Fluss", min: 10, album: 0 },
  { id: "mid", name: "Verlassenes Depot", min: 30, album: .12 },
  { id: "long", name: "Hinter den Hügeln", min: 120, album: .3 },
];
'''

ACH_EF = r'''const ACH = [
  A("first", "Erster Schub", "Fordere zum ersten Mal Nachschub an.", "scrap", 10, () => state.spins >= 1),
  A("busy", "Fleißiger Schrauber", "100 Schübe.", "cell", 50, () => state.spins >= 100),
  A("marathon", "Alter Hase", "1.000 Schübe.", "chip", 300, () => state.spins >= 1000),
  A("win1", "Erster Fund", "Gewinne zum ersten Mal.", "scrap", 10, () => (st().wins || 0) >= 1),
  A("big", "Große Bergung", "Gewinne mindestens 15× deinen Einsatz.", "core", 100, () => (st().maxFactor || 0) >= 15),
  A("mega", "Mega-Bergung", "Gewinne mindestens 40× deinen Einsatz.", "relic", 250, () => (st().maxFactor || 0) >= 40),
  A("jack", "Goldtresor", "Knacke den Jackpot.", "crystal", 500, () => (st().jackpots || 0) >= 1),
  A("laser", "Taubenfreund", "Die Brieftaube hilft 5-mal aus.", "wild", 100, () => (st().lasers || 0) >= 5),
  A("fs", "Depesche", "Löse Freispiele aus.", "beacon", 50, () => (st().fs || 0) >= 1),
  A("pick", "Kistenknacker", "Spiele die Kistenbergung.", "capsule", 75, () => (st().pick || 0) >= 1),
  A("ring3", "Pfadfinder", "Erreiche den innersten Ring der Geländefahrt.", "warp", 150, () => (st().ring3 || 0) >= 1),
  A("hot", "Heiße Strähne", "Strähne von 4 Gewinnen.", "core", 100, () => (st().maxStreak || 0) >= 4),
  A("unstop", "Unaufhaltsam", "Strähne von 6 Gewinnen.", "relic", 300, () => (st().maxStreak || 0) >= 6),
  A("tix", "Rubbelfinger", "Kaufe 10 Rubbellose.", "scrap", 75, () => (st().tickets || 0) >= 10),
  A("tixbig", "Rubbelglück", "Gewinne mindestens 20× den Lospreis.", "crystal", 250, () => (st().ticketBig || 0) >= 1),
  A("dare", "Mutprobe", "Gewinne eine Runde im Risikospiel.", "beacon", 50, () => (st().gambleWins || 0) >= 1),
  A("allin", "Alles oder nichts", "Gewinne 4 Risikorunden am Stück.", "wild", 300, () => (st().gambleChain || 0) >= 4),
  A("up1", "Erste Schraube", "Kaufe eine Upgrade-Stufe.", "up_hull", 25, () => (st().upgrades || 0) >= 1),
  A("tier", "Großes Upgrade", "Schließe eine Ausbaustufe ab.", "up_engine", 75, () => (st().tierUps || 0) >= 1),
  A("maxed", "Voll ausgebaut", "Alle 45 Upgrade-Stufen.", "up_reactor", 1000, () => totalSteps() >= 45),
  A("crew", "Volle Besatzung", "Heuere alle vier Crewmitglieder an.", "up_scanner", 300, () => (state.crew || []).length >= 4),
  A("captain", "Kapitän", "Erreiche Rang 7.", "up_reactor", 200, () => state.level >= 7),
  A("veteran", "Gildenveteran", "Erreiche Rang 15.", "up_reactor", 600, () => state.level >= 15),
  A("exp1", "Erste Expedition", "Hol eine Expedition ab.", "up_engine", 50, () => (st().expeds || 0) >= 1),
  A("world", "Frontreisender", "Besuche alle vier Fronten.", "warp", 300, () => (state.visited || []).length >= 4),
  A("coll", "Sammler", "Finde 6 Sammelstücke.", "up_cargo", 200, () => (state.album || []).length >= 6),
  A("museum", "Spind voll", "Finde alle 12 Sammelstücke.", "up_cargo", 800, () => (state.album || []).length >= 12),
  A("explorer", "Panzerkenner", "Alle 9 Entdeckungen am Panzer.", "wild", 150, () => (state.found || []).length >= 9),
  A("paint", "Neuer Anstrich", "Ändere Tarnung oder Abzeichen.", "up_hull", 25, () => (st().paints || 0) >= 1),
  A("phoenix", "Wieder flott", "Verliere einen Panzer und mach weiter.", "up_hull", 100, () => (state.shipsLost || 0) >= 1),
  A("loyal", "Treuer Kapitän", "Hol dir 7-mal die tägliche Lieferung.", "crystal", 200, () => (st().daily || 0) >= 7),
  A("dust", "Ordenssammler", "Sammle insgesamt 10 Orden.", "crystal", 150, () => (st().dustTotal || 0) >= 10),
  A("climber", "Höhenluft", "Erreiche auf der Risikoleiter ×12 oder mehr.", "beacon", 150, () => (st().ladderTop || 0) >= 6),
  A("hunter", "Kistenjäger", "Fang 10 Fallschirmkisten ab.", "crystal", 120, () => (st().starsShot || 0) >= 10),
  A("booster", "Gut versorgt", "Iss deine erste Feldration.", "up_scanner", 50, () => (st().boostsUsed || 0) >= 1),
];
'''

PAINTS_EF = r'''const PAINTS = [
  { id: "std", name: "Feldgrau", filter: "none", sw: "linear-gradient(135deg,#7a7a68,#3a3a2a)", need: "" },
  { id: "cobalt", name: "Wüstensand", filter: "sepia(.8) saturate(1.4) hue-rotate(-10deg) brightness(1.25)", sw: "linear-gradient(135deg,#d9b27c,#8a6a3a)", rank: 2, need: "ab Rang 2" },
  { id: "ruby", name: "Winterweiß", filter: "grayscale(.6) brightness(1.7) contrast(.9)", sw: "linear-gradient(135deg,#f0f2f4,#9aa4aa)", rank: 4, need: "ab Rang 4" },
  { id: "emerald", name: "Waldgrün", filter: "hue-rotate(25deg) saturate(1.3)", sw: "linear-gradient(135deg,#5a7a3a,#2a3a1a)", rank: 6, need: "ab Rang 6" },
  { id: "gold", name: "Gold", filter: "sepia(1) saturate(2.8) hue-rotate(-12deg) brightness(1.15)", sw: "linear-gradient(135deg,#ffe39a,#b07a1a)", rank: 10, need: "ab Rang 10" },
  { id: "night", name: "Nachtschwarz", filter: "brightness(.5) contrast(1.3) saturate(.5)", sw: "linear-gradient(135deg,#3a3a3a,#0a0a0a)", ach: "explorer", need: "Erfolg: Panzerkenner" },
];
'''
DECALS_EF = r'''const DECALS = [
  { id: "none", name: "Keins", sw: "#2a2c26", need: "" },
  { id: "stripes", name: "Warnstreifen", sw: "repeating-linear-gradient(45deg,#2a2c26 0 6px,#e8b04a 6px 12px)", rank: 3, need: "ab Rang 3" },
  { id: "flames", name: "Haifischmaul", sw: "linear-gradient(90deg,#a33a2a,#f4f4ee)", ach: "mega", need: "Erfolg: Mega-Bergung" },
  { id: "crest", name: "Glücksstern", sw: "radial-gradient(circle,#e8b04a 30%,#2a2c26 32%)", rank: 9, need: "ab Rang 9" },
];
'''
DECAL_EF = r'''function decalSVG(g) {
  const { l, t, b, n } = g, d = state.decal || "none", tb = b - 12;
  if (d === "stripes") { let s = ""; for (let x = l + 6; x < n - 20; x += 10) s += `<path d="M${x},${tb} l6,-${tb - t}" stroke="#e8b04a" stroke-width="3" opacity=".7"/>`; return s; }
  if (d === "flames") return `<path d="M${n - 4},${t + 10} l-14,4 l4,3 l-5,3 l5,3 l-4,3 l14,2z" fill="#f4f4ee" stroke="#a33a2a" stroke-width="1.2"/><circle cx="${n - 22}" cy="${t + 7}" r="2" fill="#1a1208"/>`;
  if (d === "crest") return `<g transform="translate(${(l + n) / 2 - 6} ${t + 3})"><circle cx="6" cy="6" r="6" fill="none" stroke="#e8b04a" stroke-width="1.4"/><path d="M6 1.5 l1.3 3 3.2 .3 -2.4 2.1 .7 3.1 -2.8 -1.6 -2.8 1.6 .7 -3.1 -2.4 -2.1 3.2 -.3z" fill="#e8b04a"/></g>`;
  return "";
}
'''

ALBUM_REPS_EF = [
    ('name: "Gummiente"', 'name: "Quietschente"'), ('name: "Taucherhelm"', 'name: "Alter Helm"'), ('name: "Schatzkarte"', 'name: "Vergilbte Landkarte"'),
    ('name: "Muschelherz"', 'name: "Herz-Anhänger"'), ('name: "Kalter Kaffee"', 'name: "Kalter Kaffee"'), ('name: "Verirrter Pinguin"', 'name: "Gummipinguin"'),
    ('name: "Lavaglas"', 'name: "Wüstenglas"'), ('name: "Glühender Nagel"', 'name: "Glühende Schraube"'),
    ('name: "Schildkrötenei"', 'name: "Dino-Ei"'), ('name: "Singende Säule"', 'name: "Alter Funkturm"'), ('name: "Runenstein"', 'name: "Eiskristall"'),
]

RANKS_TG = 'const RANKS = ["Schiffbrüchiger", "Strandsammler", "Floßbauer", "Leichtmatrose", "Wrackjäger", "Inselsegler", "Kapitän", "Gildenveteran", "Gildenmeister", "Legende der Sieben Meere"];'
RANKS_EF = 'const RANKS = ["Rekrut", "Schrottsammler", "Schrauber", "Mechaniker", "Wrackjäger", "Panzerfahrer", "Kapitän", "Gildenveteran", "Werkmeister", "Legende aus Stahl"];'

LINES_REPS = [
    ('const FINDS = { clang: "Klopfender Balken", rat: "Schiffsratte", pilot: "Plaudernder Schiffbrüchiger", boost: "Rückenwind", reactor: "Funkenflug", scanner: "Ruf vom Ausguck", duck: "Gummiente im Meer", laser: "Wurfhaken", roll: "Kenterrolle" };',
     'const FINDS = { clang: "Klopfende Panzerplatte", rat: "Werkstattmaus", pilot: "Plaudernder Kommandant", boost: "Vollgas", reactor: "Rohrputzen", scanner: "Funkspruch", duck: "Quietschente im Lager", laser: "Leuchtkugel", roll: "Pirouette" };'),
    ('const SCAN_LINES = ["Ausguck: Land in Sicht! ... ach nein, das war ein Wal.", "Ausguck: Eine Möwe winkt. Vermutlich.", "Ausguck: Keine Haie in Sicht.", "Ausguck: Spuren von verlorenen Socken.", "Ausguck: Da hinten treibt eine Kokosnuss."];',
     'const SCAN_LINES = ["Funk: Nur Rauschen ... und ein Schlagerlied.", "Funk: Ein Kuhhirte grüßt. Vermutlich.", "Funk: Keine Konkurrenz in Reichweite.", "Funk: Spuren von verlorenen Socken.", "Funk: Die Kantine hat Kuchen!"];'),
    ('const SHIP_A = ["Salz", "Treib", "Muschel", "Möwen", "Brandungs", "Sturm", "Tang", "Korallen", "Kokos", "Flaschen", "Strand", "Sonnen", "Nebel", "Wellen", "Bambus", "Planken", "Riff", "Ebbe"];',
     'const SHIP_A = ["Rost", "Eisen", "Stahl", "Donner", "Schlamm", "Ketten", "Blech", "Nieten", "Funken", "Staub", "Brumm", "Diesel", "Kraft", "Panzer", "Granit", "Hammer", "Ruß", "Bolzen"];'),
    ('const SHIP_B = ["möwe", "krabbe", "qualle", "otter", "robbe", "hai", "rochen", "muschel", "brise", "boje", "planke", "kiste", "flosse", "perle", "kogge", "schnecke", "wal", "ente"];',
     'const SHIP_B = ["beule", "bär", "dachs", "keiler", "hummel", "käfer", "nashorn", "igel", "bulle", "biber", "kröte", "wal", "eber", "elch", "maulwurf", "schildkröte", "hund", "ochse"];'),
    ('const SHIP_FIX = ["Zweite Chance", "Letzter Strohhalm", "Kokosnuss", "Nasse Füße", "Seeigel", "Tante Erna", "Unsinkbar II", "Lucky Strike", "Halbe Miete", "Sonnenschein", "Treibholz Royal", "Bambusbaron"];',
     'const SHIP_FIX = ["Zweite Chance", "Alte Liebe", "Klapperkiste", "Tante Erna", "Dicke Berta", "Lucky Strike", "Halbe Miete", "Sonnenschein", "Eiserne Lady", "Rostlaube", "Brummbär", "Nimmermüde"];'),
    ('''const PILOT_LINES = [
  ["Ist das ... Seetang oder mein Frühstück?", "Ich hab gehört, Flöße schwimmen besser mit Brettern.", "Bitte nicht klopfen, das hält gerade so.", "Mein Sitz ist eine halbe Kokosnuss."],
  ["Die Knoten halten! Meistens.", "Wasser ist alle. Also, das trinkbare.", "Tau ist auch ein Bauteil.", "Hast du den Funk gehört? Wir sind berühmt. Fast."],
  ["Das fühlt sich schon fast wie ein echtes Schiff an.", "Schöne Reling. Schade um meinen Hut.", "Wenn das die Gilde sieht ...", "Kurs halten, Kapitän!"],
  ["Ich wurde geboren, um auf diesem Floß zu segeln.", "Hörst du das? Das ist das Rauschen des Erfolgs.", "Legenden ankern nicht, sie treiben mit Stil.", "Ich hab mir eine Sonnenbrille gegen die Gischt gekauft."],
];''', '''const PILOT_LINES = [
  ["Ist das ... Rost oder Ketchup?", "Ich hab gehört, Panzer fahren besser mit Ketten.", "Bitte nicht klopfen, das hält gerade so.", "Mein Sitz ist ein umgedrehter Eimer."],
  ["Die Flicken halten! Meistens.", "Kaffee ist alle. Moral sinkt.", "Draht ist auch ein Bauteil.", "Hast du den Funk gehört? Wir sind berühmt. Fast."],
  ["Das fühlt sich schon fast wie ein echter Panzer an.", "Schöne Panzerung. Schade um den Kaffee.", "Wenn das die Gilde sieht ...", "Kurs halten, Kapitän!"],
  ["Ich wurde geboren, um diesen Panzer zu fahren.", "Hörst du das? Das ist der Klang von Erfolg.", "Legenden parken nicht, sie rollen vor.", "Ich hab mir eine Sonnenbrille gegen den Staub gekauft."],
];'''),
    ('''const RADIO = [
  "Funk: Der Händler auf der Kokosinsel zahlt gut für Bernstein.",
  "Funk: Sturmwarnung im Norden. Segel festzurren.",
  "Funk: Ein Fischkutter meldet treibende Kisten bei der Sandbank.",
  "Funk: Die Werft am Hafen bietet neue Segel an. Nur gegen Muscheln.",
  "Funk: Eine Flaschenpost treibt vorbei. Absender unbekannt.",
  "Funk: Haiflossen in Sicht. Füße bitte an Bord lassen.",
  "Funk: Strandhändler Varn sucht Thunfisch. Fragt nicht woher.",
  "Funk: Wrackfeld vor der Treibgutbucht gesichtet. Konkurrenz ist unterwegs.",
  "Funk: Die Gilde erinnert: Ein starkes Floß rettet dir beim Notverkauf den Hals.",
];''', '''const RADIO = [
  "Funk: Der Händler im Depot zahlt gut für Orden.",
  "Funk: Regen im Anmarsch. Planen über das Lager.",
  "Funk: Ein Lastwagen meldet verlorene Kisten an der Brücke.",
  "Funk: Die Werkstatt am Bahnhof bietet neue Ketten an. Nur gegen Schrauben.",
  "Funk: Eine Depesche ist unterwegs. Absender unbekannt.",
  "Funk: Kühe auf der Straße. Bitte langsam fahren.",
  "Funk: Schrotthändler Varn sucht Motorblöcke. Fragt nicht woher.",
  "Funk: Schrottfeld hinter dem Werkhof gesichtet. Konkurrenz ist unterwegs.",
  "Funk: Die Gilde erinnert: Eine starke Panzerung rettet dir beim Notverkauf den Hals.",
];'''),
    ('{ id: "neon"', '{ id: "neon"'),
]

HTML_EF = [
    ('<title>Treibgut</title>', '<title>Eisenfront</title>'),
    ('<h1 class="intro-title" id="introTitle" aria-label="Treibgut">TREIBGUT</h1>', '<h1 class="intro-title" id="introTitle" aria-label="Eisenfront">EISENFRONT</h1>'),
    ('<p class="intro-sub">Survival Slots · Fischen. Bauen. Überleben.</p>', '<p class="intro-sub">Werkstatt-Slots · Bergen. Reparieren. Durchhalten.</p>'),
    ('<button type="button" class="intro-btn" id="introBtn">Ablegen</button>', '<button type="button" class="intro-btn" id="introBtn">Anwerfen</button>'),
    ('          <h1>Treibgut</h1>\n          <small>Survival Slots · nur Spielmuscheln ·', '          <h1>Eisenfront</h1>\n          <small>Werkstatt-Slots · nur Spielschrauben ·'),
    ('<span id="radioText">Funk: Das Funkgerät knistert. Die Strandgilde hört mit.</span>', '<span id="radioText">Funk: Das Funkgerät knackt. Die Mechanikergilde hört mit.</span>'),
    ('title="Papagei Koko ein- oder ausblenden"', 'title="Werkstatthund Rex ein- oder ausblenden"'),
    ('<button type="button" class="bip-bot" id="bipBot" aria-label="Koko, dein Bordpapagei. Antippen zum Kraulen.">', '<button type="button" class="bip-bot" id="bipBot" aria-label="Rex, dein Werkstatthund. Antippen zum Kraulen.">'),
    ('<p class="hint">Leertaste wirft das Netz aus. Erneut drücken holt es sofort ein.</p>', '<p class="hint">Leertaste fordert Nachschub an. Erneut drücken lädt alles sofort ab.</p>'),
    ('<h3>Kräuterhütte <span>bezahlt mit Bernstein · zeitlich begrenzt</span></h3>', '<h3>Feldküche <span>bezahlt mit Orden · zeitlich begrenzt</span></h3>'),
    ('<h2>Strandhütte <span>Tagesbonus und Rubbellose</span></h2>', '<h2>Kantine <span>Tagesbonus und Rubbellose</span></h2>'),
    ('<b>Tägliche Strandsuche</b>', '<b>Tägliche Lieferung</b>'),
    ('data-pv="ship" aria-selected="true">Floß<i', 'data-pv="ship" aria-selected="true">Panzer<i'),
    ('<h2>Lagune<small id="shipName">SOS-7 Salzbrise</small></h2>', '<h2>Werkhalle<small id="shipName">PZ-7 Rostbeule</small></h2>'),
    ('name: "Strandfund"', 'name: "Schrottfund"'), ('name: "Bernsteinfieber"', 'name: "Ordensfieber"'), ('name: "Piraten-Jackpot"', 'name: "Tresor-Jackpot"'),
    ('name: "Adlerauge-Tee"', 'name: "Scharfes Fernglas"'), ('name: "Möwenfutter"', 'name: "Taubenfutter"'), ('name: "Strömungskraut"', 'name: "Funkverstärker"'), ('name: "Weisheitswurzel"', 'name: "Feldhandbuch"'), ('name: "Schatznase"', 'name: "Spürnase"'),
    ('{ id: "scrap",   name: "Treibholz",       w: 42, pay: [3, 12, 30],     color: "#d9b27c" },', '{ id: "scrap",   name: "Zahnrad",         w: 42, pay: [3, 12, 30],     color: "#c9ccd1" },'),
    ('{ id: "cell",    name: "Palmblatt",       w: 30, pay: [5, 18, 52],     color: "#6fe08a" },', '{ id: "cell",    name: "Kanister",        w: 30, pay: [5, 18, 52],     color: "#b5cc6a" },'),
    ('{ id: "chip",    name: "Tau",             w: 14, pay: [9, 29, 88],     color: "#e0b878" },', '{ id: "chip",    name: "Kettenglied",     w: 14, pay: [9, 29, 88],     color: "#a6acb4" },'),
    ('{ id: "core",    name: "Thunfisch",       w: 9,  pay: [15, 52, 175],   color: "#7fc8ff" },', '{ id: "core",    name: "Motorblock",      w: 9,  pay: [15, 52, 175],   color: "#e07a4a" },'),
    ('{ id: "crystal", name: "Bernstein",       w: 5,  pay: [29, 118, 440],  color: "#ffb347" },', '{ id: "crystal", name: "Orden",           w: 5,  pay: [29, 118, 440],  color: "#e8b04a" },'),
    ('{ id: "relic",   name: "Piratenmünze",    w: 3,  pay: [49, 175, 735],  color: "#ffd34a" },', '{ id: "relic",   name: "Goldbarren",      w: 3,  pay: [49, 175, 735],  color: "#ffd34a" },'),
    ('{ id: "beacon",  name: "Flaschenpost",    w: 4,  pay: null, special: "#c6f06b" },', '{ id: "beacon",  name: "Depesche",        w: 4,  pay: null, special: "#d9c75a" },'),
    ('{ id: "capsule", name: "Treibkiste",      w: 6,  pay: null, reels: [0, 2, 4], special: "#ffc94a" },', '{ id: "capsule", name: "Nachschubkiste",  w: 6,  pay: null, reels: [0, 2, 4], special: "#e8b04a" },'),
    ('{ id: "warp",    name: "Strudel",         w: 6,  pay: null, reels: [1, 2, 3], special: "#ff7a59" },', '{ id: "warp",    name: "Kompass",         w: 6,  pay: null, reels: [1, 2, 3], special: "#e07a4a" },'),
    ('const WILD = { id: "wild", name: "Rettungsring",', 'const WILD = { id: "wild", name: "Schraubenschlüssel",'),
]

STAR_EF = [
    ('const x0 = VB.x + VB.w + 20, y0 = 126 + Math.random() * 24, x1 = VB.x - 25, y1 = y0 + (Math.random() - .5) * 10;',
     'const x0 = VB.x + VB.w * (.55 + Math.random() * .4), y0 = VB.y - 14, x1 = x0 - 60 - Math.random() * 80, y1 = 112 + Math.random() * 14;'),
    ('''  g.innerHTML = `<path d="M8 4 q8 -3 16 0 t16 0" stroke="#ffffff" stroke-width="1.2" fill="none" opacity=".55"/>
    <circle class="hit" r="16"/><circle r="9" fill="${col}" opacity=".25" filter="url(#glow)"/>
    <g class="core"><rect x="-7" y="-9" width="14" height="16" rx="5" fill="${gold ? "#c9952e" : "#7a4a24"}" stroke="${gold ? "#ffe39a" : "#3a2412"}" stroke-width="1.4"/><path d="M-7 -4 h14 M-7 2 h14" stroke="${gold ? "#fff2c4" : "#c9b48a"}" stroke-width="1.6"/></g>
    <path d="M-12 6 q6 -3 12 0 t12 0" stroke="#e8f7f5" stroke-width="1.3" fill="none" opacity=".8"/>`;''',
     '''  g.innerHTML = `<circle class="hit" r="20"/><path d="M-13 -14 q13 -18 26 0 z" fill="${gold ? "#e8b04a" : "#e8dcb8"}" stroke="${gold ? "#7a5608" : "#8a7a5a"}" stroke-width="1"/><path d="M-13 -14 l11 12 M13 -14 l-11 12 M0 -14 v12" stroke="#c9bfa0" stroke-width=".7"/>
    <g class="core"><rect x="-7" y="-2" width="14" height="11" rx="1.5" fill="${gold ? "#c9952e" : "#5a6a2c"}" stroke="${gold ? "#ffe39a" : "#2a3214"}" stroke-width="1.3"/><path d="M-7 3.5 h14 M-2 -2 v11 M2 -2 v11" stroke="${gold ? "#fff2c4" : "#2a3214"}" stroke-width="1"/></g>`;'''),
    ('st.x = x0 + (x1 - x0) * k; st.y = y0 + (y1 - y0) * k + Math.sin(k * 14) * 2;', 'st.x = x0 + (x1 - x0) * k + Math.sin(k * 9) * 6; st.y = y0 + (y1 - y0) * k;'),
    ('bubbleAt(svg, $("shipview"), Math.max(VB.x + 30, Math.min(VB.x + VB.w - 30, st.x)), st.y - 10, st.gold ? "Goldfass! +3 Bernstein" : "An Bord! +1 Bernstein");',
     'bubbleAt(svg, $("shipview"), Math.max(VB.x + 30, Math.min(VB.x + VB.w - 30, st.x)), st.y - 16, st.gold ? "Goldkiste! +3 Orden" : "Abgefangen! +1 Orden");'),
    ('setTimeout(() => addDust(n, st.gold ? "goldenes Treibfass" : "Treibfass"), 700);', 'setTimeout(() => addDust(n, st.gold ? "goldene Fallschirmkiste" : "Fallschirmkiste"), 700);'),
]

HOOK_TG = '''    // Klick aufs Meer: Wurfhaken an der Leine
    sfx.pew();
    const hx = g.n - 22, hy = g.t - 14, mx2 = (hx + p.x) / 2, my2 = Math.min(hy, p.y) - 26;
    const hook = document.createElementNS("http://www.w3.org/2000/svg", "g");
    hook.innerHTML = `<path d="M${hx},${hy} Q${mx2},${my2} ${p.x},${p.y}" stroke="#e0c890" stroke-width="1.3" fill="none" stroke-dasharray="3 2"/><g transform="translate(${p.x} ${p.y})"><path d="M0,-6 V2 q0,4 -4,4 q-3,0 -3,-3" stroke="#c9ccd4" stroke-width="1.6" fill="none" stroke-linecap="round"/><circle r="5" fill="none" stroke="#ffffff" stroke-width="1" opacity=".6"><animate attributeName="r" from="3" to="14" dur=".6s" fill="freeze"/><animate attributeName="opacity" from=".8" to="0" dur=".6s" fill="freeze"/></circle></g>`;
    fxG.appendChild(hook);
    setTimeout(() => sfx.stop(), 180);
    let o = 1; const fade = () => { o -= .03; hook.setAttribute("opacity", o); if (o > 0) requestAnimationFrame(fade); else hook.remove(); }; setTimeout(() => requestAnimationFrame(fade), 300);
    skySparks(sky, p.x, p.y, 10);
    discover("laser");'''
HOOK_EF = '''    // Klick ins Gelände: Leuchtkugel aus der Signalpistole
    sfx.pew();
    const hx = g.l + (g.n - g.l) * .55 - 8, hy = g.t - 30, mx2 = (hx + p.x) / 2, my2 = Math.min(hy, p.y) - 34;
    const fl = document.createElementNS("http://www.w3.org/2000/svg", "g");
    fl.innerHTML = `<path d="M${hx},${hy} Q${mx2},${my2} ${p.x},${p.y}" stroke="#ffd27a" stroke-width="1" fill="none" stroke-dasharray="1 3" opacity=".7"/><circle cx="${p.x}" cy="${p.y}" r="3" fill="#fff4c8" filter="url(#glow)"><animate attributeName="r" from="2" to="9" dur=".5s" fill="freeze"/></circle><circle cx="${p.x}" cy="${p.y}" r="16" fill="#ffd27a" opacity=".25"><animate attributeName="opacity" from=".45" to="0" dur="1.2s" fill="freeze"/></circle>`;
    fxG.appendChild(fl);
    setTimeout(() => sfx.dust(), 160);
    let o = 1; const fade = () => { o -= .025; fl.setAttribute("opacity", o); if (o > 0) requestAnimationFrame(fade); else fl.remove(); }; setTimeout(() => requestAnimationFrame(fade), 500);
    skySparks(sky, p.x, p.y, 12);
    discover("laser");'''
COUGH_TG = 'skySparks(sky, g.l - 24, 118, 14); bubbleAt(svg, view, g.l, 92, "*platsch*");'
COUGH_EF = 'for (let i = 0; i < 12; i++) { const [x, y, sc] = toSky(sky, g.l + 8, g.t - 8); sky.parts.push({ x, y, vx: -Math.random() * 1.6, vy: -Math.random() * 1.2, r: 2.6 * sc, life: .9, kind: "smoke", dark: true }); } bubbleAt(svg, view, g.l, 86, "*knatter*");'

CHANGELOG_EF = r'''const CHANGELOG = [
  { v: "0.1.0", date: "25.10.2026", title: "Erste Fassung", items: ["Eisenfront ist da: Werkstatt-Slots mit einem rostigen Panzer, den du Stück für Stück wieder flottmachst.", "Fünf Ausbaubereiche in je vier sichtbaren Stufen: Panzerung, Motor, Funk, Lager und Kanone.", "Grundspiel mit Ersatzteil-Lager: Ab 5 gleichen Teilen, die sich berühren, wird ein Satz verbaut, Nachschub fällt nach und jeder Schub zahlt mehr.", "Werkstatthund Rex begleitet dich, die Brieftaube bringt Schraubenschlüssel, und Kisten schweben am Fallschirm vorbei.", "Eigener Look mit Stahl, Oliv und Schablonenschrift, eigene Musik (Marsch, Mundharmonika, Werkhalle) und metallische Geräusche.", "Wie alle Welten: nur Spielgeld, eigener Spielstand, über „Welt“ jederzeit wechselbar."] },
'''

# Feinkorrekturen (vor der Wortliste, auf Treibgut-Text)
PHRASES_EF = [
    ('"Das Netz fliegt …"', '"Nachschub rollt an …"'),
    ('"Kein Schwarm im Netz. Neuer Wurf?"', '"Kein Satz komplett. Neuer Schub?"'),
    ('"Hilfsmöwe! Sie lässt Rettungsringe ins Netz fallen …"', '"Brieftaube! Sie bringt Schraubenschlüssel …"'),
    ('radio("Funk: Eine Möwe kreist über dem Netz.", true);', 'radio("Funk: Eine Brieftaube landet an der Werkbank.", true);'),
    ('aria-label="Fangnetz mit 6 mal 5 Feldern"', 'aria-label="Ersatzteillager mit 6 mal 5 Feldern"'),
    ("Ab 5 gleichen Funden, die sich berühren, landet ein Schwarm im Netz. Danach fällt neues Treibgut nach, und jede weitere Welle zahlt mehr (×1, ×2, ×3, ×5).",
     "Ab 5 gleichen Teilen, die sich berühren, wird ein Satz verbaut. Danach fällt Nachschub nach, und jeder weitere Schub zahlt mehr (×1, ×2, ×3, ×5)."),
    ('["Fangnetz", "6 × 5 Felder.', '["Ersatzteillager", "6 × 5 Felder.'),
    ('"Der aktuelle Multiplikator dieser Runde. Er steigt mit jeder neuen Welle."', '"Der aktuelle Multiplikator dieser Runde. Er steigt mit jedem neuen Schub."'),
    ("Ab 5 gleichen Funden, die sich waagerecht oder senkrecht berühren, landet ein Schwarm im Netz. Danach rutscht alles nach unten und neues Treibgut fällt nach. Jede weitere Welle in derselben Runde zahlt mehr: ×1, ×2, ×3, dann ×5.",
     "Ab 5 gleichen Teilen, die sich waagerecht oder senkrecht berühren, wird ein Satz verbaut. Danach rutscht alles nach unten und Nachschub fällt nach. Jeder weitere Schub in derselben Runde zahlt mehr: ×1, ×2, ×3, dann ×5."),
    ("Liegen nach dem letzten Nachfang 3, 4 oder 5 Flaschenposten irgendwo im Netz", "Liegen nach dem letzten Nachschub 3, 4 oder 5 Depeschen irgendwo im Lager"),
    ("Der Nachfang-Multiplikator startet bei ×2, steigt mit jeder Welle bis ×10", "Der Nachschub-Multiplikator startet bei ×2, steigt mit jedem Schub bis ×10"),
    ("3 oder mehr Treibkisten im Netz starten die Kistenbergung", "3 oder mehr Nachschubkisten im Lager starten die Kistenbergung"),
    ("3 oder mehr Strudel im Netz starten die Strudelfahrt am Steuerrad.", "3 oder mehr Kompasse im Lager starten die Geländefahrt am Kartenrad."),
    ("Bleibt das Netz leer, kommt manchmal eine Möwe und lässt 1 bis 3 Rettungsringe fallen. Ein Rettungsring zählt für jeden Schwarm. In Freispielen hilft sie öfter.",
     "Bleibt das Lager leer, kommt manchmal eine Brieftaube und bringt 1 bis 3 Schraubenschlüssel. Ein Schraubenschlüssel zählt für jeden Satz. In Freispielen hilft sie öfter."),
    ("jeder Bernstein im Netz deutlich mehr, auch die nachgefallenen", "jeder Orden im Lager deutlich mehr, auch die nachgefallenen"),
    ("In der Kräuterhütte tauschst du ihn gegen Tränke für einige Minuten.", "In der Feldküche tauschst du ihn gegen Rationen für einige Minuten."),
    ("Jeder Wurf ohne Fang füllt Kokos Glücksladung. Nach ${BOOST_AT} leeren Würfen ist sie voll, und der nächste Wurf fängt garantiert einen Schwarm.",
     "Jeder Schub ohne Fund füllt Rex' Glücksladung. Nach ${BOOST_AT} leeren Schüben ist sie voll, und der nächste Schub bringt garantiert einen Satz."),
    ("Türkis oder Koralle raten", "Oliv oder Signalrot raten"),
    ('style="--gc:#5cc8b0">Türkis</button>', 'style="--gc:#5cc8b0">Oliv</button>'),
    ('style="--gc:#e0704a">Koralle</button>', 'style="--gc:#e0704a">Signalrot</button>'),
    ("Fängst du mehrere Würfe hintereinander etwas", "Findest du mehrere Schübe hintereinander etwas"),
    ("Schick dein Floß auf Expedition, erkunde neue Inseln über deinen Rang und erfülle Aufträge für Muscheln und XP.", "Schick deinen Panzer auf Expedition, erkunde neue Fronten über deinen Rang und erfülle Aufträge für Schrauben und XP."),
    ("<b>Beispiel:</b> 6 Thunfische, die sich berühren, plus ein Rettungsring = ein Schwarm aus 7.", "<b>Beispiel:</b> 6 Motorblöcke, die sich berühren, plus ein Schraubenschlüssel = ein Satz aus 7."),
    ("Gefangene Schwärme landen im Netz, alles darüber rutscht nach unten und neues Treibgut fällt nach. Jede weitere Welle erhöht den Nachfang-Multiplikator: ×1, ×2, ×3, dann ×5.",
     "Verbaute Sätze verschwinden, alles darüber rutscht nach unten und Nachschub fällt nach. Jeder weitere Schub erhöht den Nachschub-Multiplikator: ×1, ×2, ×3, dann ×5."),
    ("Gewinn = Wert × Einsatz. Ein Schwarm sind mindestens 5 gleiche Funde, die sich waagerecht oder senkrecht berühren. Rettungsringe zählen für jeden Schwarm.",
     "Gewinn = Wert × Einsatz. Ein Satz sind mindestens 5 gleiche Teile, die sich waagerecht oder senkrecht berühren. Schraubenschlüssel zählen für jeden Satz."),
    ("<th>Schwarm</th>", "<th>Satz</th>"),
    ('aria-controls="panel-lines">Schwärme</button>', 'aria-controls="panel-lines">Sätze</button>'),
    ('`Kein Fang. Noch ${fsLeft} Freispiel${fsLeft === 1 ? "" : "e"}, Nachfang bleibt bei ×${fsMult}.`', '`Kein Fund. Noch ${fsLeft} Freispiel${fsLeft === 1 ? "" : "e"}, Nachschub bleibt bei ×${fsMult}.`'),
    ("`Freispiele beendet: insgesamt +${fsWin} Muscheln, Nachfang bis ×${fsMult}.`", "`Freispiele beendet: insgesamt +${fsWin} Schrauben, Nachschub bis ×${fsMult}.`"),
    ('${waves > 1 ? ` in ${waves} Wellen` : ""}', '${waves > 1 ? ` in ${waves} Schüben` : ""}'),
    ('${waves > 1 ? ` · ${waves} Wellen` : ""}', '${waves > 1 ? ` · ${waves} Schübe` : ""}'),
    ('${waves > 1 ? `Nachfang ${waves}: ` : ""}', '${waves > 1 ? `Nachschub ${waves}: ` : ""}'),
    ('<div class="casc" id="casc" hidden>Nachfang <b id="cascN">×1</b></div>', '<div class="casc" id="casc" hidden>Nachschub <b id="cascN">×1</b></div>'),
    ('übrig · Nachfang <em class="fsmult"', 'übrig · Nachschub <em class="fsmult"'),
    ('"Flaschenpost. Liegen 3 oder mehr nach dem letzten Nachfang im Netz, gibt es Freispiele (3 = 8, 4 = 12, 5 = 20). Dort bleibt der Nachfang-Multiplikator bis ×10 erhalten."',
     '"Depesche. Liegen 3 oder mehr nach dem letzten Nachschub im Lager, gibt es Freispiele (3 = 8, 4 = 12, 5 = 20). Dort bleibt der Nachschub-Multiplikator bis ×10 erhalten."'),
    ('"Treibkiste. 3 oder mehr im Netz starten die Kistenbergung."', '"Nachschubkiste. 3 oder mehr im Lager starten die Kistenbergung."'),
    ('"Strudel. 3 oder mehr im Netz starten die Strudelfahrt am Steuerrad."', '"Kompass. 3 oder mehr im Lager starten die Geländefahrt am Kartenrad."'),
    ('"Rettungsring. Kommt nur von der Hilfsmöwe und zählt für jeden Schwarm."', '"Schraubenschlüssel. Kommt nur von der Brieftaube und zählt für jeden Satz."'),
    ("Schwarm aus 5–6: <b>", "Satz aus 5–6: <b>"),
    ("Muscheln beim aktuellen Einsatz, vor dem Nachfang-Multiplikator.", "Schrauben beim aktuellen Einsatz, vor dem Nachschub-Multiplikator."),
    ('" Jeder Bernstein füllt außerdem den Bernsteinmesser."', '" Jeder Orden füllt außerdem den Ordensmesser."'),
    ('"Schnell anklicken! Der Wurfhaken holt das Fass an Bord, drin ist Bernstein. Goldene Fässer bringen mehr."', '"Schnell anklicken, dann fängst du die Kiste ab. Drin sind Orden. Goldene Kisten bringen mehr."'),
    ('["Lagune", "Dein Floß. Klick auf Bauteile oder aufs Meer, da gibt es', '["Werkhalle", "Dein Panzer. Klick auf Bauteile oder ins Gelände, da gibt es'),
    ("Mit Upgrades wird es vom Wrack zum Kreuzer.", "Mit Upgrades wird er vom Wrack zum schweren Brocken."),
    ('"Tipp: Klick mal auf die Bauteile deines Floßes oder aufs Meer."', '"Tipp: Klick mal auf die Bauteile deines Panzers oder ins Gelände."'),
    ("Tipp: Klick mal auf die Bauteile deines Floßes oder aufs Meer.", "Tipp: Klick mal auf die Bauteile deines Panzers oder ins Gelände."),
    ("Funk: Das Funkgerät knistert.", "Funk: Das Funkgerät knackt."),
    ('"Kistenbergung", color: "#ffc94a" }, warp: { bonus: "wheel", title: "Strudelfahrt"', '"Kistenbergung", color: "#ffc94a" }, warp: { bonus: "wheel", title: "Geländefahrt"'),
    ('"Bereit für den ersten Strudel."', '"Bereit für die erste Etappe."'),
    ('level === 0 ? "Ins Ruder greifen" : "Tiefer in den Strudel"', 'level === 0 ? "Kurs bestimmen" : "Weiter ins Gelände"'),
    ("drehst du das Steuerrad.", "drehst du das Kartenrad."), ("Dreh das Steuerrad.", "Dreh das Kartenrad."), ('aria-label="Steuerrad', 'aria-label="Kartenrad'),
    ("am Steuerrad", "am Kartenrad"),
    ("Keine Muscheln und keine Teile mehr zum Verkaufen. Dein Floß zerfällt in der Brandung.", "Keine Schrauben und keine Teile mehr zum Verkaufen. Dein Panzer bleibt endgültig liegen."),
    ("Die Strandgilde braucht deinen Namen und den Namen deines Floßes.", "Die Mechanikergilde braucht deinen Namen und den Namen deines Panzers."),
    ("Der Strandhändler trägt dein neues Floß ins Register ein.", "Der Schrotthändler trägt deinen neuen Panzer ins Register ein."),
    ("Dein neues Floß braucht einen Namen.", "Dein neuer Panzer braucht einen Namen."),
    ('"Neues Floß registrieren"', '"Neuen Panzer registrieren"'),
    ('`Die ${state.shipName || "Salzbrise"} ist verloren.', '`Die ${state.shipName || "Rostbeule"} ist verloren.'),
    ("Ein Strandhändler überlässt dir ein neues Wrack", "Ein Schrotthändler überlässt dir ein neues Wrack"),
    (">Floß verloren</h2>", ">Panzer verloren</h2>"),
    ("Ein starkes Floß bringt mehr zurück.", "Eine starke Panzerung bringt mehr zurück."),
    ('"Embleme fürs Floß."', '"Embleme für den Panzer."'),
    ('"Farben für dein Floß"', '"Farben für deinen Panzer"'),
    ("Wirft mehrmals hintereinander aus. Freigeschaltet über das Segel.", "Fordert mehrmals hintereinander an. Freigeschaltet über den Motor."),
    ('"Schnelleres Netz. Wird vom Segel freigeschaltet."', '"Schnellerer Nachschub. Wird vom Motor freigeschaltet."'),
    ("`Freischalten mit Segel Stufe", "`Freischalten mit Motor Stufe"), ('"Freischalten mit Segel Stufe 2"', '"Freischalten mit Motor Stufe 2"'),
    ('"Die Feuerstelle deines Floßes bestimmt den Höchsteinsatz. Rüste sie in der Lagune aus."', '"Die Kanone deines Panzers bestimmt den Höchsteinsatz. Rüste sie in der Werkhalle aus."'),
    ("Höhere Einsätze schaltet die Feuerstelle frei.", "Höhere Einsätze schaltet die Kanone frei."),
    ("· Feuerstelle ausbauen", "· Kanone ausbauen"),
    ('const CATS_HELP = { hull: "Floß: schützt bei Pleite, du bekommst mehr zurück.", engine: "Segel: schaltet Auto-Würfe und Turbo frei.", scanner: "Ausguck: erhöht alle Liniengewinne ein bisschen.", cargo: "Lager: mehr Gewinn in Bonusspielen.", reactor: "Feuerstelle: höhere Einsätze." };',
     'const CATS_HELP = { hull: "Panzerung: schützt bei Pleite, du bekommst mehr zurück.", engine: "Motor: schaltet Auto-Schübe und Turbo frei.", scanner: "Funk: erhöht alle Gewinne ein bisschen.", cargo: "Lager: mehr Gewinn in Bonusspielen.", reactor: "Kanone: höhere Einsätze." };'),
    ('<span id="spinLabel">Werfen</span>', '<span id="spinLabel">Anfordern</span>'),
    (': fsMode ? "Frei" : "Werfen";', ': fsMode ? "Frei" : "Anfordern";'),
    ('"Netz auswerfen"', '"Nachschub anfordern"'),
    ("Einsatz wählen und Netz auswerfen. Drei Flaschenposten lösen Freispiele aus.", "Einsatz wählen und Nachschub anfordern. Drei Depeschen lösen Freispiele aus."),
    ("Wirf dein Netz zum ersten Mal aus.", "Fordere zum ersten Mal Nachschub an."),
    ("Ein Klick auf Werfen bricht ab.", "Ein Klick auf Anfordern bricht ab."),
    ('"Netz ist draußen …"', '"Nachschub rollt an …"'),
    ('"Lager leer. Nur Sand."', '"Lager leer. Nur Staub."'),
    ('"Ausguck: Nur ein Stock. Ich sehe nur Wasser."', '"Funk: Antenne verbogen. Nur Rauschen."'),
    ('"Inseln mit eigenem Wetter, eigenen Farben und eigener Musikstimmung. Neue Inseln schaltest du mit Stufen frei."', '"Fronten mit eigenem Wetter, eigenen Farben und eigener Musikstimmung. Neue Fronten schaltest du mit Stufen frei."'),
    ('"Klick auf eine freigeschaltete Insel, um hinzusegeln."', '"Klick auf eine freigeschaltete Front, um hinzufahren."'),
    ('"Seltene Funde von den Inseln.', '"Seltene Funde von den Fronten.'),
    ("Manchmal landen sie beim Auswerfen im Netz.", "Manchmal stecken sie im Nachschub."),
    ("beim Auswerfen auf der jeweiligen Insel auf", "beim Nachschub an der jeweiligen Front auf"),
    ('aria-label="Seekarte mit vier Inseln"', 'aria-label="Frontkarte mit vier Fronten"'),
    ('id="jumpBtn" ${spinning || busy || state.exped ? "disabled" : ""}>Hinsegeln</button>', 'id="jumpBtn" ${spinning || busy || state.exped ? "disabled" : ""}>Hinfahren</button>'),
    ("Erst wenn dein Floß von der Expedition zurück ist.", "Erst wenn dein Panzer von der Expedition zurück ist."),
    ('"Zurück in der Lagune!"', '"Zurück in der Werkhalle!"'),
    ('"Funk: Noch eine Flaschenpost! Die Fahrt geht weiter." : "Funk: Flaschenpost gefunden! Freie Fahrt mit Rückenwind."', '"Funk: Noch eine Depesche! Der Einsatz geht weiter." : "Funk: Depesche erhalten! Sondereinsatz genehmigt."'),
    ('tier: retrigger ? "Noch eine Flaschenpost" : "Flaschenpost gefunden"', 'tier: retrigger ? "Noch eine Depesche" : "Depesche erhalten"'),
    ('`Noch eine Flaschenpost: +${award} Freispiele!` : `${scatters.length} Flaschenposten gefunden: ${award} Freispiele!`', '`Noch eine Depesche: +${award} Freispiele!` : `${scatters.length} Depeschen erhalten: ${award} Freispiele!`'),
    ('"Funk: Eine Flaschenpost treibt vorbei. Absender unbekannt."', '"Funk: Eine Depesche ist unterwegs. Absender unbekannt."'),
    ("`Funk: PIRATENSCHATZ GEHOBEN! ${amount} Muscheln. Alle Inseln reden davon.`", "`Funk: GOLDTRESOR GEKNACKT! ${amount} Schrauben. Alle Fronten reden davon.`"),
    ("`Piratenschatz gehoben: +${amount} Muscheln!`", "`Goldtresor geknackt: +${amount} Schrauben!`"),
    ("Jeder Wurf füllt den Bernsteinmesser ein wenig", "Jeder Schub füllt den Ordensmesser ein wenig"),
    ("Survival auf dem Meer: Floß, Inseln und Papagei Koko.", "Survival auf dem Meer: Floß, Inseln und Papagei Koko."),
]

WORDS_EF = [
    (r"Spielmuscheln", "Spielschrauben"), (r"Muscheln", "Schrauben"), (r"\bMuschel\b", "Schraube"),
    (r"Bernsteinmesser", "Ordensmesser"), (r"Bernsteinsammler", "Ordenssammler"), (r"Bernsteine\b", "Orden"), (r"Bernstein", "Orden"),
    (r"PIRATENSCHATZ", "GOLDTRESOR"), (r"Piratenschatz", "Goldtresor"), (r"Piratenmünze", "Goldbarren"),
    (r"Flaschenposten", "Depeschen"), (r"Flaschenpost", "Depesche"),
    (r"Treibkisten", "Nachschubkisten"), (r"Treibkiste", "Nachschubkiste"),
    (r"Strudelfahrt", "Geländefahrt"), (r"\bStrudel\b", "Kompass"),
    (r"Rettungsringe", "Schraubenschlüssel"), (r"Rettungsring", "Schraubenschlüssel"),
    (r"Hilfsmöwen", "Brieftauben"), (r"Hilfsmöwe", "Brieftaube"), (r"Möwen", "Tauben"), (r"Möwe", "Taube"),
    (r"Schwärme", "Sätze"), (r"Schwarm", "Satz"),
    (r"Nachfang", "Nachschub"), (r"Auto-Wurf", "Auto-Schub"), (r"Auto-Würfe", "Auto-Schübe"), (r"Würfe\b", "Schübe"), (r"Würfen\b", "Schüben"), (r"\bWurf\b", "Schub"),
    (r"Treibfässer", "Fallschirmkisten"), (r"Treibfass", "Fallschirmkiste"),
    (r"Floßregister", "Panzerregister"), (r"Floßname", "Panzername"), (r"Floßklasse", "Panzerklasse"), (r"Floßkenner", "Panzerkenner"), (r"Floßdeck", "Kommandostand"),
    (r"Floß-", "Panzer-"), (r"deines Floßes", "deines Panzers"), (r"Floßes", "Panzers"), (r"Flöße", "Panzer"),
    (r"Das Floß", "Der Panzer"), (r"das Floß", "den Panzer"), (r"dein Floß", "deinen Panzer"), (r"Dein Floß", "Dein Panzer"), (r"Floß", "Panzer"),
    (r"in der Lagune", "in der Werkhalle"), (r"Lagune", "Werkhalle"),
    (r"Inseln", "Fronten"), (r"\bInsel\b", "Front"), (r"Seekarte", "Frontkarte"),
    (r"KOKO-BOOST", "REX-BOOST"), (r"Koko-Boost", "Rex-Boost"), (r"\bKokos\b", "Rex'"), (r"\bKoko\b", "Rex"), (r"Bordpapagei", "Werkstatthund"), (r"Papagei", "Hund"),
    (r"Strandgilde", "Mechanikergilde"), (r"Strandhändler", "Schrotthändler"), (r"Strandhütte", "Kantine"), (r"Strandsuche", "Lieferung"),
    (r"Kräuterhütte", "Feldküche"), (r"Kräutertrank", "Feldration"),
    (r"\bSegel\b", "Motor"), (r"Ausguck", "Funk"), (r"Feuerstelle", "Kanone"),
    (r"SOS-7", "PZ-7"), (r"Salzbrise", "Rostbeule"),
    (r"aufs Meer", "ins Gelände"), (r"auf dem Meer", "im Gelände"),
    (r"Thunfisch", "Motorblock"), (r"Palmblatt", "Kanister"), (r"Treibholz", "Zahnrad"), (r"\bTau\b", "Kettenglied"),
    (r"TREIBGUT", "EISENFRONT"), (r"Treibgut", "Eisenfront"),
    (r"\bFang\b", "Fund"),
]

COLOR_MAP_EF = [
    ("#5cc8b0", "#a7c060"), ("#3f86c0", "#6f8fa8"), ("#8fbfdf", "#b8c7cf"), ("#b5d65a", "#d9c75a"),
    ("#3fe0c5", "#a7c060"), ("#7fc8ff", "#b8c7cf"), ("#2f8fff", "#6f8fa8"), ("#c6f06b", "#d9c75a"), ("#ff7a59", "#e07a4a"),
    ("rgba(92,200,176,", "rgba(167,192,96,"), ("rgba(63,134,192,", "rgba(111,143,168,"), ("rgba(181,214,90,", "rgba(217,199,90,"),
]
