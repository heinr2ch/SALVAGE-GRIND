# Neustadt Teil 2: Inhalte und Texte (Quelle ist die fertige Eisenfront-Datei)

BIP_NS = r'''const BIP = {
  hello: [["happy", "Hallo, Bürgermeister! Ich bin <b>Paule</b>, der Stadtwaschbär. Ich kenne jede Mülltonne. Und jede Abkürzung."], ["happy", "Paule meldet sich! Helm auf, wir bauen."]],
  small: [["happy", "Kleingeld ist auch Geld!"], ["happy", "Ein Fenster mehr mit Licht."], ["happy", "Jeder Taler zählt. Ich zähl mit!"]],
  good: [["happy", "Schöne Skyline! Da will ich wohnen."], ["happy", "Das lief gut! Die Stadt wächst."], ["excited", "Hui, guter Bau!"]],
  big: [["excited", "WOW! So viele Wege? Mir wird ganz schwindelig!"], ["excited", "Ich hab das gesehen! Was für eine Skyline!"], ["wow", "Sag mal ... bist du Architekt?"]],
  mega: [["wow", "MEGA! Ich muss kurz auf eine Mülltonne klettern und jubeln!"], ["excited", "Das erzähl ich allen Waschbären im Park!"]],
  laser: [["excited", "Der Kran hat's abgefangen! Puh!"], ["happy", "Gut gesichert ist halb gewonnen."]],
  streak3: [["excited", "Drei in Folge! Die Stadt boomt!"], ["happy", "Strähne läuft! Ich spür das im Schwanz."]],
  streak5: [["wow", "Fünf in Folge?! Ich hab's an allen Ringen meines Schwanzes abgezählt."]],
  broke: [["normal", "Strähne vorbei. Kommt wieder, wie die Müllabfuhr."], ["normal", "Na ja, Strähnen kommen und gehen."]],
  dry: [["sad", "Gerade bröckelt's, ich weiß. Aber die Stadt läuft nicht weg."], ["sad", "Puh, viel Abriss heute. Wenn du magst, schau dir die Stadt an, da gibt's lustige Ecken."], ["normal", "Kopf hoch. Taler sind nur Taler, Spaß ist, was zählt."], ["sad", "Pech gehabt. Ich teil meinen Keks mit dir."]],
  fs: [["excited", "Baugenehmigung! Freibauten! Ich hol die Helme!"], ["excited", "Gestempelt und genehmigt!"]],
  starFirst: [["wow", "Da schwebt ein <b>Ballon</b> über der Stadt! Schnell, tipp drauf, da hängt ein Wappen dran!"]],
  star: [["excited", "Ballon in Sicht! Schnapp ihn dir!"], ["happy", "Da fliegt ein Ballon! Fang ihn!"]],
  sticky: [["wow", "Kran-Sicherung aktiv!"], ["excited", "Der Kran passt auf!"]],
  fsend: [["happy", "Freibauten vorbei. Hat Spaß gemacht!"], ["happy", "Das war eine schöne Bauphase!"]],
  bonusGood: [["excited", "Bonus geschafft! Ich hab ganz laut gequiekt."], ["happy", "Gut gemacht im Bonusspiel!"]],
  bonusMeh: [["normal", "Nicht der große Wurf, aber Bonusspiele sind immer ein kleines Abenteuer."]],
  jackpot: [["wow", "DER STADTSCHATZ! Ich ... ich hab keine Worte. Nur Quieken!"]],
  upgrade: [["happy", "Schick! Die Stadt sieht gleich freundlicher aus."], ["happy", "Gute Investition, Bürgermeister!"]],
  bigUpgrade: [["excited", "Großer Ausbau! Schau dir diese Stadt an! Ich bin ganz stolz."], ["wow", "Ist das noch unser Trümmerfeld? Kaum wiederzuerkennen!"]],
  rank: [["excited", "Beförderung! Darf ich dich jetzt <b>Oberbürgermeister</b> nennen?"], ["happy", "Neuer Rang! Ich hab dir einen glänzenden Kronkorken als Orden aufgehoben."]],
  mission: [["happy", "Auftrag erledigt! Abgestempelt."], ["happy", "Wieder einer geschafft. Der Stadtrat ist zufrieden."]],
  scrap: [["sad", "Oh nein, wir mussten etwas verkaufen. Das bauen wir wieder auf, versprochen."], ["sad", "Autsch. Aber hey, die Stadt steht noch!"]],
  lost: [["sad", "Die Stadt liegt in Trümmern ... Aber du hast neues Bauland und mich. Wir schaffen das zusammen."]],
  scratchWin: [["excited", "Gerubbelt und gewonnen! Hast du goldene Pfoten?"], ["happy", "Rubbel-Glück! Herzlichen Glückwunsch!"]],
  scratchLoss: [["normal", "Diesmal nix. Aber das Rubbeln selbst macht schon Spaß, oder?"], ["sad", "Leer. Das Los wollte wohl nicht teilen."]],
  found: [["happy", "Oh, was entdeckt! Du kennst deine Stadt immer besser."], ["wow", "Huch! Das wusste nicht mal ich."]],
  session: [["normal", "Wir bauen schon eine ganze Weile. Kurz strecken und was trinken? Ich warte hier."], ["normal", "Kleine Erinnerung von Paule: Pausen gehören zu jeder guten Baustelle."]],
  idle: [["normal", "Ich such solange was Leckeres in der Tonne."], ["happy", "Psst ... tipp mal auf das Rathaus."], ["happy", "Unsicher, was etwas macht? Tipp auf das <b>?</b> neben mir, dann erkläre ich alles, worüber du fährst."], ["normal", "Ich zähle Fenster. Bin bei 4.812."]],
  crew: [["excited", "Neue Leute in der Stadt! Endlich jemand, der Kekse fallen lässt."], ["happy", "Willkommen im Rathaus! Ich hab dir einen Stuhl vorgewärmt."]],
  paint: [["happy", "Ooh, frische Farbe! Steht der Stadt richtig gut."]],
  expedGo: [["normal", "Viel Erfolg bei der Aktion! Ich pass hier solange auf."], ["happy", "Aktion gestartet. Ich zähle die Sekunden. Laut."]],
  expedBack: [["excited", "Die Aktion ist vorbei! Und sie hat was eingebracht!"]],
  sector: [["wow", "Neues Viertel! Alles sieht so anders aus. Ich bin ganz aufgeregt."], ["excited", "Angekommen! Ich hab nur ein bisschen gequiekt."]],
  album: [["wow", "Ein Sammelstück! Das kommt in die Vitrine im Rathaus. Ganz vorne."]],
  ach: [["excited", "Erfolg freigeschaltet! Ich tanz auf der Mülltonne!"], ["happy", "Juhu! Ein neuer Erfolg. Du wirst immer besser."]],
  daily: [["happy", "Tagesbonus abgeholt! Schön, dass du wieder da bist."]],
  gambleWin: [["wow", "Mutig! Und es hat sich gelohnt!"], ["excited", "Richtig geraten! Meine Ohren stehen."]],
  ladderWin: [["excited", "Hoch hinaus! Fast so hoch wie dein Hochhaus."], ["wow", "So weit oben! Nicht runterschauen, Bürgermeister!"]],
  ladderTop: [["wow", "GANZ OBEN! Hundertfach! Ich fasse es nicht!"]],
  ladderLoss: [["sad", "Abgestürzt ... Die Leiter war heute wackelig."], ["sad", "Autsch. Aber hey, der Ausblick war schön."]],
  gambleLoss: [["sad", "Oh je. Das Risiko war echt 50 zu 50, diesmal leider gegen uns."]],
  dustFirst: [["wow", "Oh! Dein erstes <b>Wappen</b>! Das ist super selten. Im Bauamt kannst du es eintauschen."]],
  boostOn: [["excited", "Erlass gilt! Jetzt aber schnell, die Uhr tickt!"], ["happy", "Ui, das kribbelt im Fell. Boost aktiv!"]],
  boostEnd: [["normal", "Der Erlass ist abgelaufen. War schön, solange er galt."]],
  charging: [["normal", "Ich sammle schon mal Glück für dich. Siehst du den Balken neben mir?"], ["happy", "Halbe Glücksladung! Ich wedel extra doll."]],
  boostReady: [["wow", "PAULE-BOOST! Der nächste Dreh gewinnt garantiert!"], ["excited", "Genug Pech gehabt! Ich hab dir einen Gewinn reserviert."]],
  boostWin: [["excited", "Siehste! Auf Paule ist Verlass!"], ["happy", "Paule-Boost geliefert! Gern geschehen, Bürgermeister."]],
  mini: [["excited", "Achtung, auf der Baustelle ist was los! Schnell!"], ["wow", "Mini-Event! Zeig, was du kannst!"]],
  casc: [["excited", "Nachbau, Nachbau, Nachbau! Die Bagger kommen kaum hinterher!"], ["wow", "Das rutscht ja immer weiter nach!"]],
  pet: [["happy", "Hihi! Das kitzelt!"], ["happy", "Danke! Du riechst nach Baustelle."], ["excited", "Noch mal! Noch mal!"], ["happy", "Ich mag dich auch, Bürgermeister."], ["wow", "Hinter den Ohren! Genau da!"]],
};
'''

CATS_NS = r'''const CATS = [
  { id: "hull", name: "Wohnviertel", color: "#7ed957", tiers: ["Ruinen", "Häuschen", "Reihenhäuser", "Wohnblöcke"],
    icon: `<svg viewBox="0 0 24 24"><path d="M3 11 L9 6 L15 11 V20 H3z M15 13 h6 v7 h-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><rect x="7" y="14" width="4" height="6" fill="currentColor"/></svg>`,
    effect: s => "" },
  { id: "engine", name: "Verkehr", color: "#ffc94a", tiers: ["Schotterweg", "Straße", "Straßenbahn", "Hochbahn"],
    icon: `<svg viewBox="0 0 24 24"><rect x="4" y="5" width="16" height="12" rx="3" fill="none" stroke="currentColor" stroke-width="2"/><path d="M4 11 h16" stroke="currentColor" stroke-width="1.6"/><circle cx="8" cy="19.5" r="1.6" fill="currentColor"/><circle cx="16" cy="19.5" r="1.6" fill="currentColor"/></svg>`,
    effect: s => "" },
  { id: "scanner", name: "Funkturm", color: "#4aa8ff", tiers: ["Umgeknickt", "Funkmast", "Sendeturm", "Fernsehturm"],
    icon: `<svg viewBox="0 0 24 24"><path d="M12 22 V8 M9 22 L12 8 L15 22" stroke="currentColor" stroke-width="1.8" fill="none"/><circle cx="12" cy="6" r="2.4" fill="currentColor"/><path d="M6 3 a8 8 0 0 0 0 7 M18 3 a8 8 0 0 1 0 7" stroke="currentColor" stroke-width="1.6" fill="none"/></svg>`,
    effect: s => "" },
  { id: "cargo", name: "Handel", color: "#ff7a59", tiers: ["Umgekippt", "Marktstand", "Laden", "Kaufhaus"],
    icon: `<svg viewBox="0 0 24 24"><path d="M3 9 L5 4 H19 L21 9 Z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M4 9 V20 H20 V9" fill="none" stroke="currentColor" stroke-width="2"/><rect x="9" y="13" width="6" height="7" fill="currentColor"/></svg>`,
    effect: s => "" },
  { id: "reactor", name: "Energie", color: "#3fd0b0", tiers: ["Kaputt", "Windrad", "Kraftwerk", "Solarpark"],
    icon: `<svg viewBox="0 0 24 24"><path d="M13 2 L5 13 h6 l-2 9 l9 -12 h-6 z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>`,
    effect: s => "" },
];
'''
CLASS_NS = 'const CLASS_NAMES = [[1, "Trümmerfeld", "#ff6b7a"], [4, "Notlager", "#ff9a3c"], [8, "Dorf", "#ffc94a"], [12, "Städtchen", "#7ed957"], [14, "Großstadt", "#4aa8ff"], [15, "Legende", "#ff7a59"]];'

SECTORS_NS = r'''const SECTORS = [
  { id: "orion", name: "Altstadt", rank: 1, color: "#7ee0c8", transpose: 0, x: 60, y: 160, shape: "old", land: "rgba(30,50,70,.75)",
    sky: ["#2a5a8a", "#6aa8d0", "#f0c890"], sun: ["#fff4d0", "rgba(255,220,150,.35)"], cloud: "rgba(255,255,255,.55)", ground: ["#5a7a5a", "#3a5a40"],
    desc: "Das Herz der Stadt. Kopfsteinpflaster, ein Kirchturm und der Ort, an dem jeder Wiederaufbau beginnt.",
    radio: ["Funk: In der Altstadt wird gehämmert. Die Bäckerei hat wieder offen."] },
  { id: "kryos", name: "Hafenviertel", rank: 4, color: "#4aa8ff", transpose: 2, x: 160, y: 70, shape: "harbor", land: "rgba(20,40,60,.8)",
    sky: ["#3a5a7a", "#7a9ab8", "#c8d8e4"], sun: ["#f4f8ff", "rgba(220,235,255,.25)"], cloud: "rgba(230,238,245,.6)", ground: ["#4a6a7a", "#2a3a4a"],
    desc: "Kräne, Container und Möwengeschrei. Aktionen bringen hier 25 % mehr.",
    radio: ["Funk: Ein Frachter läuft ein. Die Kräne drehen sich.", "Funk: Eine Möwe hat das Fischbrötchen des Hafenmeisters geklaut."] },
  { id: "ignis", name: "Industriepark", rank: 8, color: "#ffc94a", transpose: -3, x: 265, y: 150, shape: "industry", land: "rgba(50,30,24,.8)",
    sky: ["#3a2a3a", "#a85a4a", "#ffb070"], sun: ["#ffd8a0", "rgba(255,150,80,.35)"], cloud: "rgba(255,200,170,.4)", ground: ["#6a5a4a", "#3a2e24"],
    desc: "Schlote, Hallen und Feierabendrot. Aktionen bringen hier 50 % mehr.",
    radio: ["Funk: Schichtwechsel im Industriepark. Stau an der Kreuzung.", "Funk: Die Fabrik meldet Rekordproduktion. Von Gartenzwergen."] },
  { id: "xeltar", name: "Lichterhöhe", rank: 12, color: "#ff7a59", transpose: 5, x: 350, y: 60, shape: "hills", land: "rgba(10,14,30,.85)", night: true,
    sky: ["#0a1028", "#1c2a54", "#3a4a7a"], sun: ["#f4f4e8", "rgba(220,230,255,.18)"], cloud: "rgba(120,130,170,.35)", ground: ["#1c2a3a", "#0e1622"],
    desc: "Die Villen auf dem Hügel, nachts ein Lichtermeer. Aktionen bringen hier 75 % mehr.",
    radio: ["Funk: Auf der Lichterhöhe ist Sternennacht. Laternen an.", "Funk: Ein Uhu wurde auf dem Rathausdach gesichtet. Er schaut kritisch."] },
];
'''
SECTOR_CSS_NS = [
    (':root { --s1: #a7c060; --s2: #6f8fa8; --s3: #ffb36b; }', ':root { --s1: #7ee0c8; --s2: #4aa8ff; --s3: #ffc94a; }'),
    ('html[data-sector="kryos"] { --s1: #b8a070; --s2: #6a6258; --s3: #d8cfb8; }', 'html[data-sector="kryos"] { --s1: #4aa8ff; --s2: #3a6a8a; --s3: #c8d8e4; }'),
    ('html[data-sector="xeltar"] { --s1: #b8c7cf; --s2: #6f8fa8; --s3: #e8f0f4; }', 'html[data-sector="xeltar"] { --s1: #ff7a59; --s2: #4a5aa8; --s3: #ffd27a; }'),
]

CREW_NS = r'''const CREW = [
  { id: "mira", name: "Mira", role: "Architektin", cost: 800, color: "#ff9a3c", effect: "Notverkauf erstattet 10 % mehr.",
    art: face("#f1c7a6", `<path d="M14 24 q2 -14 13 -14 q12 0 13 14 q-4 -6 -13 -6 q-9 0 -13 6z" fill="#c2452d"/><path d="M13 18 q14 -12 28 0 l-1 3 h-26z" fill="#ffc94a" stroke="#a87a10" stroke-width="1"/>`, { suit: "#3a6a8a", more: `` }),
    lines: ["Wer hat schon wieder auf meinen Plan Kaffee geschüttet?", "Gib mir zehn Minuten und ein Lineal.", "Das wird mein bestes Gebäude. Bis zum nächsten."] },
  { id: "juno", name: "Juno", role: "Stadtplanerin", cost: 1200, color: "#7ee0c8", effect: "Aktionen sind 25 % schneller.",
    art: face("#8d5a3b", `<path d="M13 28 q-1 -18 14 -18 q15 0 14 18 q-3 -8 -14 -8 q-11 0 -14 8z" fill="#1d1d2b"/>`, { suit: "#2a7a6a", more: `<rect x="30" y="34" width="12" height="9" rx="1" fill="#f4f0e4"/>` }),
    lines: ["Ich hab eine neue Busspur geplant. Sie führt nur ein bisschen durch den Park.", "Laut Plan steht hier ein Brunnen. Laut Realität eine Pfütze.", "Karten lügen nie. Bauzeitenpläne schon."] },
  { id: "broesel", name: "Bolle", role: "Bäcker", cost: 1000, color: "#8fe07a", effect: "Alle XP um 10 % erhöht.",
    art: face("#e9b98f", `<path d="M14 18 q0 -12 13 -12 q13 0 13 12z" fill="#f4f4ee"/><rect x="14" y="16" width="26" height="4" fill="#e0e0d8"/>`, { suit: "#d8d4c8", more: `` }),
    lines: ["Frische Brötchen für die Baustelle!", "Ich hab den Ofen repariert. Er backt jetzt auch Pizza.", "Mahlzeit! Bitte nicht die Gummiente essen."] },
  { id: "kael", name: "Kael", role: "Pressesprecher", cost: 1500, color: "#ff7a59", effect: "Aufträge zahlen 20 % mehr.",
    art: face("#e9b98f", `<path d="M14 22 q4 -12 13 -12 q10 0 13 12 l-2 -2 l-3 3 l-3 -4 l-3 4 l-3 -4 l-3 4 l-3 -3z" fill="#5a3a1a"/>`, { suit: "#2a2a3a", more: `<path d="M24 40 l3 6 l3 -6z" fill="#ff7a59"/>` }),
    lines: ["Die Zeitung will ein Interview. Über den Waschbären.", "Ich hab drei neue Aufträge reingeholt. Gern geschehen.", "Psst, in der Stadt wird über dich geredet. Positiv!"] },
];
'''
EXPED_NS = r'''const EXPED = [
  { id: "short", name: "Spendenlauf im Park", min: 10, album: 0 },
  { id: "mid", name: "Fördergeld beantragen", min: 30, album: .12 },
  { id: "long", name: "Großes Stadtfest", min: 120, album: .3 },
];
'''

ACH_NS = r'''const ACH = [
  A("first", "Grundstein", "Bau deine erste Skyline.", "scrap", 10, () => state.spins >= 1),
  A("ways", "Wegebauer", "Erreiche 10.000 Gewinnwege in einem Dreh.", "cell", 100, () => (st().maxWays || 0) >= 10000),
  A("casc5", "Dauerbaustelle", "Schaffe 5 Nachbauten in einem Dreh.", "chip", 150, () => (st().maxCasc || 0) >= 5),
  A("six", "Skyline", "Gewinne 25-mal über alle 6 Häuser.", "core", 200, () => (st().six || 0) >= 25),
  A("busy", "Fleißige Baustelle", "100 Runden.", "cell", 50, () => state.spins >= 100),
  A("marathon", "Alter Hase", "1.000 Runden.", "chip", 300, () => state.spins >= 1000),
  A("win1", "Erster Gewinn", "Gewinne zum ersten Mal Taler.", "scrap", 10, () => (st().wins || 0) >= 1),
  A("big", "Hoch hinaus", "Gewinne mindestens 15× deinen Einsatz.", "core", 100, () => (st().maxFactor || 0) >= 15),
  A("mega", "Wolkenkratzer", "Gewinne mindestens 40× deinen Einsatz.", "relic", 250, () => (st().maxFactor || 0) >= 40),
  A("jack", "Stadtschatz", "Hebe den Jackpot.", "crystal", 500, () => (st().jackpots || 0) >= 1),
  A("laser", "Kranführer", "Gewinne 100-mal mit Hilfe eines Krans.", "wild", 100, () => (st().lasers || 0) >= 100),
  A("fs", "Genehmigt", "Erhalte Freibauten.", "beacon", 50, () => (st().fs || 0) >= 1),
  A("pick", "Planer", "Spiele ein Bonusspiel.", "capsule", 75, () => (st().pick || 0) >= 1),
  A("ring3", "Stadtführer", "Erreiche den innersten Ring der Stadtlotterie.", "warp", 150, () => (st().ring3 || 0) >= 1),
  A("hot", "Heiße Strähne", "Strähne von 4 Gewinnen.", "core", 100, () => (st().maxStreak || 0) >= 4),
  A("unstop", "Unaufhaltsam", "Strähne von 6 Gewinnen.", "relic", 300, () => (st().maxStreak || 0) >= 6),
  A("tix", "Rubbelfinger", "Kaufe 10 Rubbellose.", "scrap", 75, () => (st().tickets || 0) >= 10),
  A("tixbig", "Rubbelglück", "Gewinne mindestens 20× den Lospreis.", "crystal", 250, () => (st().ticketBig || 0) >= 1),
  A("dare", "Mutprobe", "Gewinne eine Runde im Risikospiel.", "beacon", 50, () => (st().gambleWins || 0) >= 1),
  A("allin", "Alles oder nichts", "Gewinne 4 Risikorunden am Stück.", "wild", 300, () => (st().gambleChain || 0) >= 4),
  A("up1", "Erster Ausbau", "Kaufe eine Ausbaustufe.", "up_hull", 25, () => (st().upgrades || 0) >= 1),
  A("tier", "Großer Ausbau", "Schließe eine Ausbaustufe ab.", "up_engine", 75, () => (st().tierUps || 0) >= 1),
  A("maxed", "Voll ausgebaut", "Alle 45 Ausbaustufen.", "up_reactor", 1000, () => totalSteps() >= 45 || (state.vehicle | 0) >= 1),
  A("veh2", "Kleinstadt", "Mach aus dem Dorf eine Kleinstadt.", "up_engine", 500, () => (state.vehicle | 0) >= 1),
  A("veh3", "Metropole", "Mach aus der Kleinstadt eine Metropole.", "up_reactor", 2000, () => (state.vehicle | 0) >= 2),
  A("allmax", "Alles ausgebaut", "Bau auch die Metropole komplett aus.", "up_reactor", 5000, () => (state.vehicle | 0) >= 2 && totalSteps() >= 45),
  A("crew", "Volles Rathaus", "Hol alle vier Leute in die Stadt.", "up_scanner", 300, () => (state.crew || []).length >= 4),
  A("captain", "Bürgermeister", "Erreiche Rang 7.", "up_reactor", 200, () => state.level >= 7),
  A("veteran", "Stadtveteran", "Erreiche Rang 15.", "up_reactor", 600, () => state.level >= 15),
  A("exp1", "Erste Aktion", "Schließ eine Aktion ab.", "up_engine", 50, () => (st().expeds || 0) >= 1),
  A("world", "Stadtkenner", "Besuche alle vier Viertel.", "warp", 300, () => (state.visited || []).length >= 4),
  A("coll", "Sammler", "Finde 6 Sammelstücke.", "up_cargo", 200, () => (state.album || []).length >= 6),
  A("museum", "Stadtmuseum", "Finde alle 12 Sammelstücke.", "up_cargo", 800, () => (state.album || []).length >= 12),
  A("explorer", "Spürnase", "Alle 9 Entdeckungen in der Stadt.", "wild", 150, () => (state.found || []).length >= 9),
  A("paint", "Frischer Anstrich", "Ändere Fassadenfarbe oder Banner.", "up_hull", 25, () => (st().paints || 0) >= 1),
  A("phoenix", "Wiederaufbau", "Verliere eine Stadt und mach weiter.", "up_hull", 100, () => (state.shipsLost || 0) >= 1),
  A("loyal", "Treuer Bürgermeister", "Hol dir 7-mal die tägliche Spende.", "crystal", 200, () => (st().daily || 0) >= 7),
  A("dust", "Wappensammler", "Sammle insgesamt 10 Wappen.", "crystal", 150, () => (st().dustTotal || 0) >= 10),
  A("climber", "Höhenluft", "Erreiche auf der Risikoleiter ×12 oder mehr.", "beacon", 150, () => (st().ladderTop || 0) >= 6),
  A("hunter", "Ballonfänger", "Fang 10 Ballons.", "crystal", 120, () => (st().starsShot || 0) >= 10),
  A("booster", "Erlassen", "Nutze deinen ersten Erlass.", "up_scanner", 50, () => (st().boostsUsed || 0) >= 1),
];
'''

PAINTS_NS = r'''const PAINTS = [
  { id: "std", name: "Natur", filter: "none", sw: "linear-gradient(135deg,#e8e2d0,#8a8470)", need: "" },
  { id: "cobalt", name: "Pastell", filter: "saturate(.7) brightness(1.15) hue-rotate(10deg)", sw: "linear-gradient(135deg,#f0d0e0,#c0e0f0)", rank: 2, need: "ab Rang 2" },
  { id: "ruby", name: "Backstein", filter: "sepia(.6) saturate(1.6) hue-rotate(-20deg)", sw: "linear-gradient(135deg,#c86a4a,#7a3a2a)", rank: 4, need: "ab Rang 4" },
  { id: "emerald", name: "Grüne Stadt", filter: "hue-rotate(60deg) saturate(1.2)", sw: "linear-gradient(135deg,#7ed957,#2f8a4a)", rank: 6, need: "ab Rang 6" },
  { id: "gold", name: "Goldene Zeiten", filter: "sepia(1) saturate(2.4) hue-rotate(-10deg) brightness(1.1)", sw: "linear-gradient(135deg,#ffe39a,#b07a1a)", rank: 10, need: "ab Rang 10" },
  { id: "night", name: "Neonnacht", filter: "hue-rotate(200deg) saturate(1.6) brightness(.85)", sw: "linear-gradient(135deg,#ff4fd8,#3a2a8a)", ach: "explorer", need: "Erfolg: Spürnase" },
];
'''
DECALS_NS = r'''const DECALS = [
  { id: "none", name: "Keins", sw: "#1c2a3a", need: "" },
  { id: "stripes", name: "Wimpelkette", sw: "repeating-linear-gradient(90deg,#ff7a59 0 6px,#ffc94a 6px 12px,#4aa8ff 12px 18px)", rank: 3, need: "ab Rang 3" },
  { id: "flames", name: "Graffiti", sw: "linear-gradient(90deg,#ff4fd8,#7ee0c8)", ach: "mega", need: "Erfolg: Wolkenkratzer" },
  { id: "crest", name: "Stadtwappen", sw: "radial-gradient(circle,#ffc94a 30%,#2a5aa8 32%)", rank: 9, need: "ab Rang 9" },
];
'''
DECAL_NS = r'''function decalSVG(g) {
  const d = state.decal || "none", X = cityX(g), x0 = X.res0, x1 = X.res1, y = g.t + 8;
  if (d === "stripes") { let s = `<path d="M${x0},${y} Q${(x0 + x1) / 2},${y + 10} ${x1},${y}" stroke="#ffffff" stroke-width=".6" fill="none"/>`; for (let i = 1; i < 10; i++) { const x = x0 + i * (x1 - x0) / 10, yy = y + Math.sin(i / 10 * Math.PI) * 9; s += `<path d="M${x - 2},${yy} l2,4 l2,-4z" fill="${["#ff7a59", "#ffc94a", "#4aa8ff"][i % 3]}"/>`; } return s; }
  if (d === "flames") return `<path d="M${x0 + 4},${117 - 8} q6,-8 12,-2 q4,-8 10,0 q6,-6 10,2" stroke="#ff4fd8" stroke-width="2.2" fill="none"/><path d="M${x0 + 8},${117 - 4} q8,-4 18,0" stroke="#7ee0c8" stroke-width="1.6" fill="none"/>`;
  if (d === "crest") return `<g transform="translate(${(x0 + x1) / 2 - 6} ${y + 6})"><path d="M0 0 H12 V7 Q12 12 6 14 Q0 12 0 7z" fill="#2a5aa8" stroke="#ffc94a" stroke-width="1"/><path d="M3 9 V5 l3 -2 l3 2 V9z" fill="#ffc94a"/></g>`;
  return "";
}
'''

ALBUM_REPS_NS = [
    ('name: "Quietschente"', 'name: "Gummiente"'), ('name: "Alter Helm"', 'name: "Bauhelm"'), ('name: "Vergilbte Landkarte"', 'name: "Alter Stadtplan"'),
    ('name: "Herz-Anhänger"', 'name: "Liebesschloss"'), ('name: "Gummipinguin"', 'name: "Hafenpinguin"'),
    ('name: "Wüstenglas"', 'name: "Fabrikglas"'), ('name: "Glühende Schraube"', 'name: "Glühbirne"'), ('name: "Feuerfeste Socke"', 'name: "Arbeitshandschuh"'),
    ('name: "Dino-Ei"', 'name: "Goldenes Ei"'), ('name: "Alter Funkturm"', 'name: "Laternenmodell"'), ('name: "Eiskristall"', 'name: "Sternschnuppe"'),
]
RANKS_EF = 'const RANKS = ["Rekrut", "Schrottsammler", "Schrauber", "Mechaniker", "Wrackjäger", "Panzerfahrer", "Kapitän", "Gildenveteran", "Werkmeister", "Legende aus Stahl"];'
RANKS_NS = 'const RANKS = ["Neubürger", "Trümmerräumer", "Bauhelfer", "Polier", "Bauleiter", "Stadtrat", "Bürgermeister", "Stadtveteran", "Oberbürgermeister", "Legende der Skyline"];'

LINES_NS = [
    'const FINDS = { clang: "Klopfende Fassade", rat: "Hausmaus", pilot: "Plaudernder Bürgermeister", boost: "Hupkonzert", reactor: "Stromschlag", scanner: "Radiosendung", duck: "Gummiente im Laden", laser: "Feuerwerk", roll: "Stadtfest-Wackler" };',
    'const SCAN_LINES = ["Radio: Verkehrsfunk. Alles frei, außer der Kreuzung.", "Radio: Wetter heute: Baustaub mit Sonne.", "Radio: Ein Hund sucht sein Herrchen. Oder umgekehrt.", "Radio: Spuren von verlorenen Socken.", "Radio: Die Bäckerei hat Kuchen!"];',
    'const SHIP_A = ["Rosen", "Linden", "Birken", "Sonnen", "Eichen", "Wiesen", "Mühlen", "Brunnen", "Kirsch", "Buchen", "Hafen", "Schloss", "Wald", "Silber", "Gold", "Bären", "Falken", "Hirsch"];',
    'const SHIP_B = ["bach", "feld", "berg", "hausen", "stadt", "dorf", "heim", "tal", "hof", "au", "brück", "burg", "wald", "furt", "stein", "wiese", "kamp", "horst"];',
    'const SHIP_FIX = ["Neuhoffnung", "Sonnenstadt", "Glückshausen", "Waschbärhausen", "Kuchenheim", "Gutenacht", "Zweite Chance", "Halbe Miete", "Schönwetter", "Nimmermüde", "Neu-Paulsdorf", "Lichtenhafen"];',
    '''const PILOT_LINES = [
  ["Ist das ... ein Rathaus oder ein Schutthaufen?", "Bitte nicht klopfen, das hält gerade so.", "Mein Schreibtisch ist ein umgedrehter Eimer.", "Die erste Sitzung findet im Freien statt."],
  ["Die Mauern halten! Meistens.", "Kaffee ist alle. Moral sinkt.", "Klebeband ist auch ein Baustoff.", "Hast du das Radio gehört? Wir sind berühmt. Fast."],
  ["Das fühlt sich schon fast wie eine richtige Stadt an.", "Schöner Ausblick. Schade um den Kaffee.", "Wenn das der Landrat sieht ...", "Weiter so, Bürgermeister!"],
  ["Ich wurde geboren, um diese Stadt zu regieren.", "Hörst du das? Das ist der Klang von Erfolg.", "Legenden parken nicht, sie haben Chauffeure.", "Ich hab mir eine Sonnenbrille gegen das Blitzlicht gekauft."],
];''',
    '''const RADIO = [
  "Funk: Der Markt zahlt heute gut für Wappen.",
  "Funk: Regen im Anmarsch. Planen über die Baustelle.",
  "Funk: Ein Lastwagen hat Ziegel an der Brücke verloren.",
  "Funk: Die Baufirma bietet neue Kräne an. Nur gegen Taler.",
  "Funk: Eine Baugenehmigung ist unterwegs. Absender: Bauamt.",
  "Funk: Enten auf der Straße. Bitte langsam fahren.",
  "Funk: Makler Varn sucht Bauland. Fragt nicht woher.",
  "Funk: Trümmerfeld hinter dem Bahnhof gesichtet. Investoren sind unterwegs.",
  "Funk: Das Bauamt erinnert: Ein starkes Wohnviertel rettet dir beim Notverkauf den Hals.",
];''',
]

HTML_NS = [
    ('<title>Eisenfront</title>', '<title>Neustadt</title>'),
    ('<h1 class="intro-title" id="introTitle" aria-label="Eisenfront">EISENFRONT</h1>', '<h1 class="intro-title" id="introTitle" aria-label="Neustadt">NEUSTADT</h1>'),
    ('<p class="intro-sub">Werkstatt-Slots · Bergen. Reparieren. Durchhalten.</p>', '<p class="intro-sub">Skyline-Walzen · Drehen. Bauen. Wachsen.</p>'),
    ('<button type="button" class="intro-btn" id="introBtn">Anwerfen</button>', '<button type="button" class="intro-btn" id="introBtn">Losbauen</button>'),
    ('          <h1>Eisenfront</h1>\n          <small>Werkstatt-Slots · nur Spielschrauben ·', '          <h1>Neustadt</h1>\n          <small>Aufbau-Slots · nur Spieltaler ·'),
    ('<span id="radioText">Funk: Das Funkgerät knackt. Die Mechanikergilde hört mit.</span>', '<span id="radioText">Funk: Guten Morgen, Neustadt! Das Bauamt hat geöffnet.</span>'),
    ('title="Werkstatthund Rex ein- oder ausblenden"', 'title="Stadtwaschbär Paule ein- oder ausblenden"'),
    ('aria-label="Rex, dein Werkstatthund. Antippen zum Kraulen."', 'aria-label="Paule, dein Stadtwaschbär. Antippen zum Kraulen."'),
    ('<p class="hint">Leertaste fordert Nachschub an. Erneut drücken stoppt sofort.</p>', '<p class="hint">Leertaste baut eine neue Skyline, erneut drücken macht schneller.</p>'),
    ('<h3>Feldküche <span>bezahlt mit Orden · zeitlich begrenzt</span></h3>', '<h3>Bauamt <span>bezahlt mit Wappen · zeitlich begrenzt</span></h3>'),
    ('<h2>Kantine <span>Tagesbonus und Rubbellose</span></h2>', '<h2>Bürgerbüro <span>Tagesbonus und Rubbellose</span></h2>'),
    ('<b>Tägliche Lieferung</b>', '<b>Tägliche Spende</b>'),
    ('data-pv="ship" aria-selected="true">Panzer<i', 'data-pv="ship" aria-selected="true">Stadt<i'),
    ('<h2>Werkhalle<small id="shipName">PZ-7 Rostbeule</small></h2>', '<h2>Stadtbild<small id="shipName">Stadt Neuhoffnung</small></h2>'),
    ('name: "Schrottfund"', 'name: "Fundsache"'), ('name: "Ordensfieber"', 'name: "Wappenfieber"'), ('name: "Tresor-Jackpot"', 'name: "Schatz-Jackpot"'),
    ('name: "Scharfes Fernglas", icon: "up_scanner", color: "#a7c060", cost: 4, min: 3, effect: "Alle Gewinne +25 %"', 'name: "Gutachten", icon: "up_scanner", color: "#7ee0c8", cost: 4, min: 3, effect: "Auszahlungen +25 %"'),
    ('name: "Taubenfutter"', 'name: "Kranverleih"'), ('effect: "Rex springt und Tauben liefern doppelt so oft"', 'effect: "Kran 3× so häufig"'),
    ('name: "Funkverstärker"', 'name: "Eilantrag"'), ('name: "Feldhandbuch"', 'name: "Fortbildung"'), ('name: "Spürnase"', 'name: "Stadtarchiv"'),
    ('{ id: "scrap",   name: "Zahnrad",         w: 42, pay: [3, 12, 30],     color: "#c9ccd1" },', '{ id: "scrap",   name: "Wohnung",         w: 42, pay: [3, 12, 30],     color: "#7ed957" },'),
    ('{ id: "cell",    name: "Kanister",        w: 30, pay: [5, 18, 52],     color: "#b5cc6a" },', '{ id: "cell",    name: "Laden",           w: 30, pay: [5, 18, 52],     color: "#4aa8ff" },'),
    ('{ id: "chip",    name: "Kettenglied",     w: 14, pay: [9, 29, 88],     color: "#a6acb4" },', '{ id: "chip",    name: "Büro",            w: 14, pay: [9, 29, 88],     color: "#6fb8ff" },'),
    ('{ id: "core",    name: "Motorblock",      w: 9,  pay: [15, 52, 175],   color: "#e07a4a" },', '{ id: "core",    name: "Hochhaus",        w: 9,  pay: [15, 52, 175],   color: "#ff7a59" },'),
    ('{ id: "crystal", name: "Orden",           w: 5,  pay: [29, 118, 440],  color: "#e8b04a" },', '{ id: "crystal", name: "Wappen",          w: 5,  pay: [29, 118, 440],  color: "#ffc94a" },'),
    ('{ id: "relic",   name: "Goldbarren",      w: 3,  pay: [49, 175, 735],  color: "#ffd34a" },', '{ id: "relic",   name: "Goldkuppel",      w: 3,  pay: [49, 175, 735],  color: "#ffd34a" },'),
    ('{ id: "beacon",  name: "Depesche",        w: 4,  pay: null, special: "#d9c75a" },', '{ id: "beacon",  name: "Baugenehmigung",  w: 4,  pay: null, special: "#c6f06b" },'),
    ('{ id: "capsule", name: "Nachschubkiste",  w: 6,  pay: null, reels: [0, 2, 4], special: "#e8b04a" },', '{ id: "capsule", name: "Bauplan",         w: 6,  pay: null, reels: [0, 2, 4], special: "#4aa8ff" },'),
    ('{ id: "warp",    name: "Kompass",         w: 6,  pay: null, reels: [1, 2, 3], special: "#e07a4a" },', '{ id: "warp",    name: "Stadtbus",        w: 6,  pay: null, reels: [1, 2, 3], special: "#ff7a59" },'),
    ('const WILD = { id: "wild", name: "Schraubenschlüssel",', 'const WILD = { id: "wild", name: "Kran",'),
]

# Ballon statt Fallschirmkiste (Texte und Grafik der Sternschnuppe)
STAR_NS = [
    ('''  g.innerHTML = `<circle class="hit" r="20"/><path d="M-13 -14 q13 -18 26 0 z" fill="${gold ? "#e8b04a" : "#e8dcb8"}" stroke="${gold ? "#7a5608" : "#8a7a5a"}" stroke-width="1"/><path d="M-13 -14 l11 12 M13 -14 l-11 12 M0 -14 v12" stroke="#c9bfa0" stroke-width=".7"/>
    <g class="core"><rect x="-7" y="-2" width="14" height="11" rx="1.5" fill="${gold ? "#c9952e" : "#5a6a2c"}" stroke="${gold ? "#ffe39a" : "#2a3214"}" stroke-width="1.3"/><path d="M-7 3.5 h14 M-2 -2 v11 M2 -2 v11" stroke="${gold ? "#fff2c4" : "#2a3214"}" stroke-width="1"/></g>`;''',
     '''  g.innerHTML = `<circle class="hit" r="20"/><ellipse cx="0" cy="-12" rx="10" ry="12" fill="${gold ? "#ffd34a" : ["#ff7a59", "#4aa8ff", "#7ed957"][(Math.random() * 3) | 0]}" stroke="rgba(0,0,0,.3)" stroke-width="1"/><ellipse cx="-3" cy="-16" rx="3" ry="4" fill="#ffffff" opacity=".4"/><path d="M0 0 q-2 4 0 8" stroke="#e8e4d4" stroke-width=".8" fill="none"/>
    <g class="core"><path d="M-5 8 H5 V13 Q5 17 0 18 Q-5 17 -5 13z" fill="${gold ? "#ffd34a" : "#2a5aa8"}" stroke="${gold ? "#7a5608" : "#ffc94a"}" stroke-width="1"/></g>`;'''),
    ('st.gold ? "Goldkiste! +3 Orden" : "Abgefangen! +1 Orden"', 'st.gold ? "Goldballon! +3 Wappen" : "Gefangen! +1 Wappen"'),
    ('setTimeout(() => addDust(n, st.gold ? "goldene Fallschirmkiste" : "Fallschirmkiste"), 700);', 'setTimeout(() => addDust(n, st.gold ? "goldener Ballon" : "Ballon"), 700);'),
]

VEHICLES_NS = '''const VEHICLES = [
  { name: "Dorf", rank: 1, cost: 1, color: "#7ed957", desc: "Ein paar Häuser zwischen Trümmern. Hier fängt alles an." },
  { name: "Kleinstadt", acc: "eine Kleinstadt", rank: 8, cost: 4, color: "#4aa8ff", desc: "Kirchturm, zweite Häuserreihe und mehr Platz. Neue Ausbauten kosten mehr, dafür steigen Einsätze bis 250." },
  { name: "Metropole", acc: "eine Metropole", rank: 14, cost: 12, color: "#ff7a59", desc: "Hochhauskulisse, Hängebrücke, Lichter bis zum Horizont. Einsätze bis 1.000." },
];
'''

CHANGELOG_NS = r'''const CHANGELOG = [
  { v: "0.5.0", date: "25.10.2026", title: "Sprachen", items: ["Neue Sprachauswahl oben neben „Ton“ und im Startbildschirm: Deutsch, Englisch, Spanisch, Japanisch, Russisch, Niederländisch und Griechisch. Die Wahl gilt für alle vier Welten.", "Übersetzt sind bisher Knöpfe, Menüs, Überschriften und kurze Hinweise. Regeln, Hilfe und Sprüche folgen.", "Eigenes Symbol im Browser-Tab für jede Welt."] },
  { v: "0.4.0", date: "25.10.2026", title: "Skyline-Walzen und Pixel-Stadt", items: ["Neues Grundspiel: Skyline-Walzen. Sechs Walzen stehen als sechs Hochhäuser nebeneinander, jedes ist bei jedem Dreh 2 bis 7 Felder hoch. Die Gewinnwege ergeben sich aus den Höhen, bis zu 117.649.", "Gewinne: gleiche Symbole auf mindestens 3 Häusern nebeneinander, von links. Der Kran ersetzt jedes Symbol.", "Nachbau: Gewinnfelder verschwinden, Neues rutscht nach, so lange es weiter gewinnt.", "Freibauten: 4 oder mehr Baugenehmigungen bringen 10 Freibauten. Der Multiplikator wächst mit jedem Nachbau bis ×15 und bleibt bis zum Ende.", "3 Stadtbusse starten die Stadtlotterie. Neue Symbole: Baum und Laterne.", "Das Stadtbild ist komplett neu gezeichnet, in Pixeloptik: Häuser, Rathaus, Funkturm, Handel, Energie, Verkehr und auch der Himmel. Alle Ausbaustufen und Stadtstufen sind neu.", "Die Stadtrundfahrt ist wieder raus. Neue Erfolge: Wegebauer, Dauerbaustelle und Skyline."] },
  { v: "0.3.0", date: "25.10.2026", title: "Stadtrundfahrt statt Hochstapler", items: ["Neues Grundspiel: die Stadtrundfahrt. Du würfelst mit zwei Würfeln, der Stadtbus fährt über 20 Felder rund um die Stadt. Bei einem Pasch würfelst du noch einmal.", "Grundstücke: Hält der Bus auf freiem Bauland, kannst du es kaufen und bei jedem weiteren Halt ausbauen (Häuschen, Stadthaus, Wohnblock, Hochhaus). Hält der Bus auf deinem Grundstück, zahlt es Miete. Ein ganzes Viertel zahlt ×1,5.", "Vier Viertel: Gartenweg, Marktviertel, Büromeile und Turmallee, jedes teurer und ertragreicher als das davor.", "Sonderfelder: Busbahnhof mit Rundenbonus, Stadtanzeiger mit Meldungen, Bauamt mit Bauplänen, Baustelle mit Mini-Events, Stadtpark mit Parkkasse, Kiosk und Rathaus mit Freifahrten (Gewinne ×2).", "Auto-Bauen kauft auf Wunsch von selbst, solange genug Taler übrig bleiben.", "Bei Pleite verkauft der Makler zuerst Grundstücke, dann erst Ausbauten der Stadt.", "Das Glücksrad-Bonusspiel heißt jetzt Stadtlotterie. Paule-Boost: Die nächste Fahrt zahlt doppelt.", "Drei neue Erfolge: Grundbesitzer, Viertelchef und Skyline."] },
  { v: "0.2.0", date: "25.10.2026", title: "Mehr Action auf der Baustelle", items: ["Der Kran steht jetzt richtig: neben dem Haus auf dem Boden, der Mast wächst mit, die Last hängt über dem Dach.", "Mini-Events mit Geschicklichkeit: Kran-Timing (im richtigen Moment tippen, bis +3 Etagen), Ziegelregen (goldene Ziegel fangen, Taler sofort) und Tauben-Alarm (alle Tauben verscheuchen, Etage plus Kran-Sicherung).", "Richtfest alle 10 Etagen: Sofortbonus, der auch bei einem Abriss bleibt.", "Bauboom: Fünf Bausteine in Folge, dann bringen die nächsten 3 je eine Etage extra.", "Investor: Ab Etage 5 bietet manchmal jemand 30 % über Wert. Verkaufen oder weiterbauen?", "Balance angepasst, damit die neuen Boni fair bleiben: Die Abrissbirne kommt etwas öfter, der Wert startet etwas höher."] },
  { v: "0.1.0", date: "25.10.2026", title: "Erste Fassung", items: ["Neustadt ist da: Aufbau-Slots, in denen du eine zerstörte Stadt Stück für Stück wieder aufbaust.", "Fünf Ausbaubereiche in je vier sichtbaren Stufen: Wohnviertel, Verkehr, Funkturm, Handel und Energie. Drei Stadtstufen: Dorf, Kleinstadt, Metropole.", "Eigenes Grundspiel „Hochstapler“: Eine kleine Walze setzt Etagen auf dein Hochhaus, der Wert steigt mit jeder Etage. Du entscheidest, wann du auszahlst, bevor die Abrissbirne kommt.", "Kran-Sicherung fängt eine Abrissbirne ab, Baupläne starten die Bauplanauswahl, der Stadtbus die Stadtrundfahrt, Baugenehmigungen bringen Freibauten ab Etage 3.", "Waschbär Paule begleitet dich, Ballons schweben über die Stadt, ein Klick in den Himmel zündet ein Feuerwerk.", "Eigener Look im Stil eines Städtebauspiels, eigene Musik (Stadtpark, Pendlerjazz, Baustellenfunk) und eigene Geräusche.", "Wie alle Welten: nur Spielgeld, eigener Spielstand, über „Welt“ jederzeit wechselbar."] },
'''

# Feinkorrekturen auf Eisenfront-Text (vor der Wortliste)
PHRASES_NS = [
    ('"Panzer verloren"', '"Stadt verloren"'), (">Panzer verloren</h2>", ">Stadt verloren</h2>"),
    ("Keine Schrauben und keine Teile mehr zum Verkaufen. Dein Panzer bleibt endgültig liegen.", "Keine Taler und nichts mehr zum Verkaufen. Deine Stadt liegt in Trümmern."),
    ("Die Mechanikergilde braucht deinen Namen und den Namen deines Panzers.", "Das Bauamt braucht deinen Namen und den Namen deiner Stadt."),
    ("Der Schrotthändler trägt deinen neuen Panzer ins Register ein.", "Das Bauamt trägt deine neue Stadt ins Register ein."),
    ("Dein neuer Panzer braucht einen Namen.", "Deine neue Stadt braucht einen Namen."),
    ('"Neuen Panzer registrieren"', '"Neue Stadt registrieren"'),
    ('`Die ${state.shipName || "Rostbeule"} ist verloren.', '`${state.shipName || "Neuhoffnung"} liegt in Trümmern.'),
    ("Ein Schrotthändler überlässt dir ein neues Wrack", "Das Bauamt überlässt dir neues Bauland"),
    ("Eine starke Panzerung bringt mehr zurück.", "Ein starkes Wohnviertel bringt mehr zurück."),
    ('"Embleme für den Panzer."', '"Banner für die Stadt."'),
    ('"Farben für deinen Panzer"', '"Fassadenfarben für deine Stadt"'),
    ("Fordert mehrmals hintereinander an. Freigeschaltet über den Motor.", "Spielt mehrere Runden hintereinander und zahlt beim Auto-Ziel aus. Freigeschaltet über den Verkehr."),
    ('"Schnellerer Nachschub. Wird vom Motor freigeschaltet."', '"Schnellere Walze. Wird vom Verkehr freigeschaltet."'),
    ("`Freischalten mit Motor Stufe", "`Freischalten mit Verkehr Stufe"), ('"Freischalten mit Motor Stufe 2"', '"Freischalten mit Verkehr Stufe 2"'),
    ('"Die Kanone deines Panzers bestimmt den Höchsteinsatz. Rüste sie in der Werkhalle aus."', '"Die Energie deiner Stadt bestimmt den Höchsteinsatz. Bau sie im Stadtbild aus."'),
    ("Höhere Einsätze schaltet die Kanone frei.", "Höhere Einsätze schaltet die Energie frei."),
    ("· Kanone ausbauen", "· Energie ausbauen"),
    ('const CATS_HELP = { hull: "Panzerung: schützt bei Pleite, du bekommst mehr zurück.", engine: "Motor: schaltet Auto-Schübe und Turbo frei.", scanner: "Funk: erhöht alle Gewinne ein bisschen.", cargo: "Lager: mehr Gewinn in Bonusspielen.", reactor: "Kanone: höhere Einsätze." };',
     'const CATS_HELP = { hull: "Wohnviertel: schützt bei Pleite, du bekommst mehr zurück.", engine: "Verkehr: schaltet Auto-Runden und Turbo frei.", scanner: "Funkturm: erhöht alle Auszahlungen ein bisschen.", cargo: "Handel: mehr Gewinn in Bonusspielen.", reactor: "Energie: höhere Einsätze." };'),
    ('<span id="spinLabel">Anfordern</span>', '<span id="spinLabel">Bauen</span>'),
    ("Einsatz wählen und Nachschub anfordern. Drei Depeschen lösen Freispiele aus.", "Einsatz wählen und bauen. Gleiche Symbole von links auf mindestens 3 Häusern gewinnen."),
    ('["Werkhalle", "Dein Panzer. Klick auf Bauteile oder ins Gelände, da gibt es', '["Stadtbild", "Deine Stadt. Tipp auf Gebäude oder in den Himmel, da gibt es'),
    ("Mit Upgrades wird er vom Wrack zum schweren Brocken.", "Mit jedem Ausbau wird sie vom Trümmerfeld zur Großstadt."),
    ('"Tipp: Klick mal auf die Bauteile deines Panzers oder ins Gelände."', '"Tipp: Tipp mal auf die Gebäude deiner Stadt oder in den Himmel."'),
    ("Tipp: Klick mal auf die Bauteile deines Panzers oder ins Gelände.", "Tipp: Tipp mal auf die Gebäude deiner Stadt oder in den Himmel."),
    ('"Zurück in der Werkhalle!"', '"Aktion abgeschlossen!"'),
    ("Erst wenn dein Panzer von der Expedition zurück ist.", "Erst wenn deine Aktion abgeschlossen ist."),
    ('id="jumpBtn" ${spinning || busy || state.exped ? "disabled" : ""}>Hinfahren</button>', 'id="jumpBtn" ${spinning || busy || state.exped ? "disabled" : ""}>Hinziehen</button>'),
    ('"Klick auf eine freigeschaltete Front, um hinzufahren."', '"Tipp auf ein freigeschaltetes Viertel, um hinzuziehen."'),
    ('aria-label="Frontkarte mit vier Fronten"', 'aria-label="Stadtkarte mit vier Vierteln"'),
    ('"Fronten mit eigenem Wetter, eigenen Farben und eigener Musikstimmung. Neue Fronten schaltest du mit Stufen frei."', '"Viertel mit eigenem Wetter, eigenen Farben und eigener Musikstimmung. Neue Viertel schaltest du mit Rängen frei."'),
    ('"Seltene Funde von den Fronten.', '"Seltene Funde aus den Vierteln.'),
    ("beim Nachschub an der jeweiligen Front auf", "beim Bauen im jeweiligen Viertel auf"),
    ("Manchmal stecken sie im Nachschub.", "Manchmal tauchen sie beim Bauen auf."),
    ('"Funk: Noch eine Depesche! Der Einsatz geht weiter." : "Funk: Depesche erhalten! Sondereinsatz genehmigt."', '"Funk: Noch eine Genehmigung! Weiterbauen." : "Funk: Baugenehmigung erteilt!"'),
    ('tier: retrigger ? "Noch eine Depesche" : "Depesche erhalten"', 'tier: retrigger ? "Noch eine Genehmigung" : "Baugenehmigung"'),
    ("Jeder Schub füllt den Ordensmesser ein wenig", "Jede Runde füllt den Wappenmesser ein wenig"),
    ("Spielt mehrere Runden hintereinander und zahlt beim Auto-Ziel aus.", "Spielt mehrere Runden hintereinander und zahlt beim Auto-Ziel aus."),
    ("Oliv oder Signalrot raten", "Grün oder Rot raten"), ('style="--gc:#a7c060">Oliv</button>', 'style="--gc:#7ed957">Grün</button>'), ('style="--gc:#e0704a">Signalrot</button>', 'style="--gc:#e0704a">Rot</button>'),
    ("Wer hat schon wieder", "Wer hat schon wieder"),
]

WORDS_NS = [
    (r"Schraubenschlüssel", "Kran"), (r"Spielschrauben", "Spieltaler"), (r"Schrauben", "Taler"), (r"\bSchraube\b", "Taler"),
    (r"Ordensmesser", "Wappenmesser"), (r"Ordenssammler", "Wappensammler"), (r"Ordensfieber", "Wappenfieber"), (r"Ordens\b", "Wappens"), (r"(?<![A-Za-zäöü])Orden\b", "Wappen"),
    (r"GOLDTRESOR", "STADTSCHATZ"), (r"Goldtresor", "Stadtschatz"),
    (r"Depeschen", "Baugenehmigungen"), (r"Depesche", "Baugenehmigung"),
    (r"Nachschubkisten", "Baupläne"), (r"Nachschubkiste", "Bauplan"), (r"Kistenbergung", "Bauplanauswahl"),
    (r"Geländefahrt", "Stadtlotterie"), (r"Kartenrad", "Glücksrad"), (r"\bKompasse\b", "Stadtbusse"), (r"\bKompass\b", "Stadtbus"),
    (r"Schraubenschlüssel", "Kran"),
    (r"Freispiele", "Freibauten"), (r"Freispiel\b", "Freibau"), (r"Freispielen", "Freibauten"),
    (r"Auto-Schübe", "Auto-Runden"), (r"Auto-Schub", "Auto-Runde"), (r"Jeder Schub", "Jede Runde"), (r"jeder Schub", "jede Runde"), (r"jedem Schub", "jeder Runde"), (r"pro Schub", "pro Runde"), (r"Neuer Schub", "Neue Runde"), (r"nächste Schub", "nächste Runde"), (r"Nächster Schub", "Nächste Runde"), (r"Schübe\b", "Runden"), (r"Schüben\b", "Runden"), (r"\bSchub\b", "Runde"),
    (r"Werkstatthund", "Stadtwaschbär"), (r"REX-BOOST", "PAULE-BOOST"), (r"Rex-Boost", "Paule-Boost"), (r"\bRex'", "Paules"), (r"\bRex\b", "Paule"),
    (r"Mechanikergilde", "Bauamt"), (r"Schrotthändler", "Makler"), (r"Feldküche", "Bauamt"), (r"Feldration", "Erlass"), (r"Rationen", "Erlasse"), (r"Kantine", "Bürgerbüro"), (r"Tägliche Lieferung", "Tägliche Spende"), (r"tägliche Lieferung", "tägliche Spende"),
    (r"Expeditionen", "Aktionen"), (r"Expedition", "Aktion"),
    (r"Frontkarte", "Stadtkarte"), (r"Fronten", "Viertel"), (r"neue Front\b", "neues Viertel"), (r"\bFront\b", "Viertel"),
    (r"Werkhalle", "Stadtbild"),
    (r"Panzerregister", "Stadtregister"), (r"Panzername", "Stadtname"), (r"Panzerklasse", "Stadtklasse"), (r"Panzerkenner", "Stadtkenner"), (r"Panzerung", "Wohnviertel"),
    (r"deines Panzers", "deiner Stadt"), (r"des Panzers", "der Stadt"), (r"deinen Panzer", "deine Stadt"), (r"Dein Panzer", "Deine Stadt"), (r"dein Panzer", "deine Stadt"), (r"Der Panzer", "Die Stadt"), (r"der Panzer\b", "die Stadt"), (r"den Panzer\b", "die Stadt"), (r"einen Panzer", "eine Stadt"), (r"Verlorene Panzer", "Verlorene Städte"), (r"Panzer-", "Stadt-"), (r"\bPanzer\b", "Stadt"),
    (r"PZ-7", "Stadt"), (r"Rostbeule", "Neuhoffnung"),
    (r"\bWracks\b", "Ruinen"), (r"\bWrack\b", "Ruine"),
    (r"Fahrzeug (\$\{V \+ 1\}) von", r"Stadtstufe \1 von"), (r"Nächstes Fahrzeug", "Nächste Stadtstufe"), (r"Neues Fahrzeug", "Neue Stadtstufe"), (r"Umsteigen auf", "Ausbauen zur"), (r"voll ausgebaut", "voll ausgebaut"),
    (r"Funk: Antenne verbogen. Nur Rauschen.", "Radio: Nur Rauschen. Der Mast ist umgeknickt."),
    (r"EISENFRONT", "NEUSTADT"), (r"Eisenfront", "Neustadt"),
]

COLOR_MAP_NS = [
    ("#a7c060", "#7ee0c8"), ("#6f8fa8", "#4aa8ff"), ("#b8c7cf", "#9ad4ff"), ("#d9c75a", "#c6f06b"), ("#e07a4a", "#ff7a59"),
    ("rgba(167,192,96,", "rgba(126,224,200,"), ("rgba(111,143,168,", "rgba(74,168,255,"), ("rgba(217,199,90,", "rgba(198,240,107,"),
]

POST_NS = [
    (r"Startet einen Runde\. Kostet \$\{bet\(\)\} Taler\. <b>Leertaste</b> geht auch, erneut drücken stoppt sofort\.", "Baut eine neue Skyline (kostet ${bet()} Taler). Während des Drehs macht es schneller. <b>Leertaste</b> geht auch."),
    (r"die gesamte Bergung", "die gesamte Summe"), (r"Wähle eine Kiste\.", "Wähle einen Bauplan."), (r"aria-label=\"Kiste \$\{i \+ 1\} öffnen\"", "aria-label=\"Bauplan ${i + 1} öffnen\""),
    (r'<p class="note">Gewinn = Wert × Einsatz × Wege\..*?</p>', '<p class="note">Taler pro Gewinnweg beim aktuellen Einsatz. Wege = Treffer auf Haus 1 × Treffer auf Haus 2 × …</p>'),
    (r"Gib deinem Stadt einen eigenen Namen\. Das Stadt ist die Gildenregistrierung und bleibt\.", "Gib deiner Stadt einen eigenen Namen."),
    (r"Funk: Die Gilde überschreibt dir", "Funk: Das Bauamt überschreibt dir"),
    (r"Funk: Die ganze Gilde hat deine Mega-Bergung mitgehört!", "Funk: Die ganze Stadt hat deinen Mega-Bau gesehen!"),
    (r"Funk: Die Gilde befördert dich", "Funk: Der Stadtrat befördert dich"),
    (r"Funk: Die Gilde trägt die \$\{v\} ins", "Funk: Das Bauamt trägt ${v} ins"),
    (r"Funk: Die Gilde trägt die \$\{ship\} unter Kapitän", "Funk: Das Bauamt trägt ${ship} unter Bürgermeister"),
    (r"Funk: Die Werft bestätigt", "Funk: Das Bauamt bestätigt"),
    (r"Fordere zum ersten Mal Nachschub an\.", "Bau deine erste Skyline."),
    (r'"Kurs bestimmen"', '"Losfahren"'), (r'"Weiter ins Gelände"', '"Nächste Haltestelle"'),
    (r"zum Beispiel Neustadt im Gelände", "zum Beispiel Neustadt"),
    (r'\["Fallschirmkiste", "[^"]*"\]', '["Ballon", "Schnell antippen, dann fängst du den Ballon. Dran hängt ein Wappen. Goldene Ballons bringen mehr."]'),
    (r"Kisten und Gewinne wachsen mit\.", "Alle Gewinne wachsen mit."),
    (r"Nachschub anfordern", "Bauen"), (r"Nachschub rollt an", "Es wird gebaut"),
    (r"Liniengewinne", "Auszahlungen"), (r"Liniengewinn", "Gewinn"), (r"beim nächsten Runde", "in der nächsten Runde"), (r"\bEin Runde\b", "Eine Runde"), (r"jeder Wappen", "jedes Wappen"), (r"auf den Walzen", "beim Bauen"),
    (r"Bergungsaufträge", "Bauaufträge"), (r"Bergungsauftrag", "Bauauftrag"), (r"Bergungslog", "Baulog"), (r"Bonus-Bergung", "Bonus-Gewinn"), (r"Mega-Bergung", "Mega-Bau"), (r"große Bergungen", "große Bauten"), (r"Große Bergung", "Großer Bau"), (r"große Bergung", "großer Bau"),
    (r"Willkommen an Bord", "Willkommen im Rathaus"), (r"ist an Bord!", "ist jetzt in der Stadt!"), (r"Taler an Bord\.", "Taler in der Stadtkasse."), (r"Fundstück an Bord", "Fundstück in der Stadt"),
    (r"Kapitänsausweis", "Bürgerausweis"), (r"Kapitänsname", "Bürgermeistername"), (r"Kapitän", "Bürgermeister"),
]
