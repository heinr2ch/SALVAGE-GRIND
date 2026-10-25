# Sternenwrack · Entwicklungsnotizen

Stand: Sternenwrack **Beta 0.13.1**, Treibgut 0.5.1, Eisenfront 0.4.1, Neustadt 0.5.1 (25.10.2026). Diese Datei dient als Übergabe für neue Claude-Sitzungen.

## Was das Spiel ist
- Browser-Spielautomat mit Sci-Fi-Thema „Bergung im All“. **Nur Spielgeld (Credits), kein echtes Geld.**
- Komplett eigene Grafiken (SVG inline), keine fremden Assets (Warframe-Assets wurden bewusst abgelehnt).
- Eine einzige Datei: `index.html` mit HTML, CSS und JS inline. Kein Build-System, keine Abhängigkeiten außer Google Fonts.
- Gehostet über GitHub Pages: https://heinr2ch.github.io/STERNENWRACK/ (Repo `heinr2ch/STERNENWRACK`, Branch `main`, Root). Jeder Push auf `main` deployt automatisch (1–2 Minuten).
- Dezentes Branding „heinr2ch“ (Intro, Fußzeile, Werftstempel am Schiff).

## Arbeitsweise mit dem Nutzer
- Der Nutzer (heinr2ch) schreibt auf Deutsch, oft per Spracheingabe. Antworten auf Deutsch, knapp, ohne Fachjargon.
- Jede Änderung: testen, direkt nach GitHub pushen, **erst nach erfolgreichem Pages-Deploy** „ist live“ melden.
  Deploy prüfen: `gh api repos/heinr2ch/STERNENWRACK/actions/runs --jq '.workflow_runs[0] | .status + " " + (.conclusion // "-") + " " + .head_sha[0:7]'`
- **Versionierung (feste Anweisung):** Schema „Beta 0.MINOR.PATCH“. Neue Features erhöhen MINOR, Korrekturen und kleine Komfortfunktionen PATCH. Nie 1.0 erreichen, ohne dass der Nutzer es sagt. Der Nutzer korrigiert bei Bedarf (z. B. Hilfemodus war für ihn nur ein PATCH).
  Bei jedem Update ändern: `GAME_VERSION`, das `CHANGELOG`-Array im Spiel (neuester Eintrag oben), `CHANGELOG.md`, Versionszeile in `README.md`.
- Commit-Identität: `user.name=heinr2ch`, `user.email=heinr2ch@users.noreply.github.com`. Tags lassen sich nicht pushen, daher keine Tags.
- Größere Balance-Änderungen vorher per Node-Simulation prüfen und dem Nutzer kurz die Zahlen nennen.
- Vor größeren Patches Backup anlegen. Änderungen am besten per Python-Skript mit exakten Ankertexten (Ersetzung mit Zählprüfung), danach `node --check` auf das extrahierte Script.
- Test mit Playwright (headless Chromium): Intro klicken, **danach Benennungsdialog bestätigen (`#namingBtn`)**, sonst blockiert er Scans. Externe Hosts per `page.route` abbrechen. Auf `pageerror` achten. Achtung: `page.evaluate` auf eine Funktion, die ein nie aufgelöstes Promise zurückgibt (z. B. `openNaming`), hängt, also in `{ }` einpacken.

## Aufbau der Datei (wichtige Teile)
- Theme-Tokens: `--cyan --violet --magenta --gold --lime`, Fonts Unbounded / Inter / JetBrains Mono (`--f-display --f-body --f-mono`).
- `state` (Spielstand) mit `serialize()` / `applySave()` / `freshState()` / `afterLoad()`. `SAVE_KEYS` für Zahlenfelder.
  Speichern: Artifact-Datenbank, wenn vorhanden, sonst `localStorage` (`sw-save`). Export/Import als Code (`SWS1-…`).
- Walzen: 5×3, 5 Linien (`LINES`), `SYMBOLS` mit Gewichten `w` und Auszahlung `pay` (Vielfache des Linieneinsatzes), `REEL_SETS`, `pick()`, `pick3()`, `evaluate(grid)`.
  Einsatz: `lineBet()` pro Linie, `bet()` = 5 × Linieneinsatz. `LINE_BETS = [1,2,5,10,20]`, der Reaktor begrenzt.
- Ablauf: `spin(auto)`, danach `finish(grid, free)` mit Gewinnberechnung, Feiern, Bonusspielen und Freispielen.
- Sound: Web Audio synthetisch (`sfx`-Objekt, `tone()`, `noise()`). Musik: prozedural, 3 Titel (`TRACKS`), interaktiv.
- Partikel: `burst`, `burstAt`, `sparkAt` (Canvas `#fx`). Hangar-Himmel: `makeSky/drawSky/skySparks`, `VB = {x:10,y:20,w:360,h:190}`.
- Schiff: `shipSVG()` mit Stufen je Kategorie (`CATS`: hull, engine, scanner, cargo, reactor; je 9 Schritte, `tierOfCat`), Lackierung, Abzeichen, Klick-Gimmicks in `bindShipFx`.
- Hilfsfunktionen: `toast`, `radio` (Funkzeile), `addLog`, `bump`/`st()` (Statistik), `checkAch()`, `pvDot`, `saveGame`, `render()`, `escapeHTML`, `fmtTime`.

## Features (Stand 0.9.0)
- **Symbole:** Schrott, Energiezelle, Datenkern, Reaktorkern, Sternenkristall, Fremdartefakt. Dazu Notsignal (Scatter, Freispiele), Frachtkapsel (Walze 1/3/5, Kapselbergung als Pick-Spiel), Sprungkern (Walze 2/3/4, Hyperraumsprung mit Glücksrad), Wild-Kristall (nur durch den Laser).
- **Bergungslaser:** Bei knappem Fehlschlag schießt eine Drohne ein Symbol weg und setzt ein Wild (`LASER_P = 0.055`, `findLaserTarget`, `laserStrike`).
- **Freispiele (neu in 0.9.0):** 3/4/5 Notsignale ergeben 8/12/20 Freispiele. Multiplikator `fsMult` startet bei ×2 und steigt pro Gewinn bis ×5. Kristalldrohne (`crystalDrone`, 30 %) setzt feste Wild-Kristalle auf Walze 2–4 (`fsSticky`, max. 3, Overlay `.lockwild` via `renderSticky`). Retrigger behält Multiplikator und Kristalle.
- **Strähne:** Gewinnserien bis ×1,5 (`STREAK_MULT`).
- **Sternenschatz (Jackpot):** wächst pro Scan (`JP_FEED`), Chance `bet()/JP_DIV`.
- **Bip-Boost:** Nach 12 Scans ohne Gewinn (`BOOST_AT`) garantiert Bip einen Gewinn.
- **Signal-Risiko:** Gewinn verdoppeln per Farbwahl, 50:50, bis ×32.
- **Risikoleiter (0.10.0):** `playLadder`, Sprossen `LADDER` ×1 bis ×100. Chance = alter/neuer Wert (fair), 1 oder 2 Sprossen pro Sprung, Licht mit Stopp-Knopf (`#rStop`, Leertaste). Gipfel +2 Staub.
- **Hangar:** Schiff vom Wrack zum Kreuzer aufrüsten, sichtbar animiert. Bei Pleite Notverkauf von Teilen, ohne Teile ist das Schiff verloren und es gibt ein neues Wrack.
- **Schiffsregister (0.8.2):** Benennungsdialog `#naming` (`openNaming("start"|"lost")`). Kapitänsname (`state.captain`) und Schiffsname mit festem Präfix „KSV-7“ (`state.shipName`, `state.shipNamed`). Zufallsvorschläge mit Würfel. Nach Schiffsverlust neu taufen.
- **Sternenstaub (0.8.0):** Zweitwährung `state.dust`, Messer `dustMeter` (+2 pro Scan, +8 pro sichtbarem Sternenkristall, 100 ergeben 1 Staub). Extra für große Gewinne, Bonusspiele, Jackpot (+5) und starke Freispiele.
- **Boost-Labor (0.8.0):** `BOOSTS` (scanner, drones, signal, guild, treasure) für 3–8 Staub, 2–5 Minuten Echtzeit, `state.boosts = {id: endTs}`, stapelbar und verlängerbar. Chips mit Countdown über den Walzen (`renderBoostBar` aktualisiert nur noch die Zeit, damit nichts neu ploppt).
- **Sternschnuppen (0.9.0):** Fliegen alle 35–75 s durch das Hangarfenster (`spawnStar`, `#starLayer`). Abschießen per Klick gibt +1 Staub, goldene +3.
- **Bip (Bordroboter):** Kontextsprüche (`BIP`-Objekt, `bip(kind, prio)`), Glücksladung, streichelbar, ausblendbar.
  **Hilfemodus (0.8.1):** „?“-Knopf oder Taste H. Bip erklärt alles, worüber man mit der Maus fährt (`HELP_RULES`). Bei neuen UI-Elementen bitte eine Regel ergänzen.
- **Weitere Features:** Aufträge (`MISSION_TYPES`), Ränge/XP, Crew, Lackierungen, Abzeichen, Sternenkarte mit Sektoren, Erfolge (`ACH`, Helfer `A(...)`), Fund-Album, Expeditionen (Echtzeit), tägliche Bergung, 3 Rubbellose mit Mausrubbeln, Bordbuch (Statistik, Verlauf, Freunde-Codes und Bestenliste, Export/Import, Lautstärke, Neustart, „Was ist neu“, Regeln).

## Balance (Stand 0.9.0)
- Gewichte: Schrott 42, Zelle 30, Chip 14, Kern 9, Kristall 5, Artefakt 3, Notsignal 4, Kapsel/Sprungkern je 6.
- Auszahlungen (3/4/5 gleiche): Schrott 3/12/30, Zelle 5/18/52, Chip 9/29/88, Kern 15/52/175, Kristall 29/118/440, Artefakt 49/175/735.
- Trefferquote etwa 31 % der Scans. Freispiele etwa alle 110 Scans, im Mittel 34× Einsatz (Durchschnitt 52×).
- Die Auszahlung liegt bewusst über dem Einsatz (etwa 125 %), weil der Nutzer „mehr Gewinn“ wollte. Bei Beschwerden über zu schnelle Credits: `FS_MULT_MAX` oder `FS_WILD_P` senken.

## Bekannte Stolpersteine
- Die CSS-Klasse `.bonus` ist das Vollbild-Overlay. Keine anderen Elemente so nennen (früherer Bug mit `msg bonus`).
- Die Leertaste startet einen Scan, außer in Eingabefeldern.
- Elemente, die per `setInterval` aktualisiert werden, nicht komplett per `innerHTML` neu bauen, sonst laufen Einblend-Animationen immer wieder neu.

## Weitere Stile (Themes)
- Weitere Stile werden **nicht von Hand kopiert**, sondern per Skript aus dem Sternenwrack-Quelltext erzeugt. So bekommen sie neue Features automatisch.
- **Treibgut** (Meer, Floß, Inseln) liegt unter `treibgut/index.html`, live unter https://heinr2ch.github.io/STERNENWRACK/treibgut/. Eigene Version (Start Beta 0.1.0), eigenes `treibgut/CHANGELOG.md`.
- Erzeugen: `python3 tools/treibgut.py <sternenwrack-quelltext.html> <ausgabe.html>` (Quelltext = Artifact-Fassung ohne `<html>/<head>`), danach wie üblich in die Standalone-Hülle packen.
  Die Inhalte liegen in `tools/treibgut_parts*.py`: Farben (`COLOR_MAP`), Symbole, Papagei-SVG, Floß-Grafik (`RAFT_SVG`), Meer-Szene (`OCEAN_SKY`), Inseln, Crew, Erfolge, Texte (`PHRASES` exakt, `WORDS` als Regex).
- Das Skript bricht ab, wenn ein Ankertext fehlt. Nach Sternenwrack-Änderungen also neu laufen lassen und fehlende Anker in den Parts anpassen.
- Getrennte Speicherschlüssel (`tg-` statt `sw-`, Codes `TGS1-`/`TGK1-`), damit sich die Spielstände auf derselben Domain nicht mischen.
- WORDS-Ersetzungen nie auf Bezeichner im Code loslassen (z. B. `countCredits`), daher Lookbehind `(?<![A-Za-z])`.
- **Welten (Sternenwrack 0.11.0):** `WORLD_ID` und `WORLDS` (Name, Text, URL, Vorschaubild). Knopf „Welt“ (`#worldBtn`, Dialog `#worlds`) und Links im Intro. Das Treibgut-Skript lässt `WORLDS` unverändert und tauscht nur `WORLD_ID`. Ein neuer Stil braucht einen Eintrag in `WORLDS`.
- **Treibgut 0.2.0:** rustikaler Look als CSS-Block `RUSTIC_CSS` am Ende, Schriften Patua One, Alegreya Sans und Courier Prime, eigene Musik `MUSIC_NEW` (Seemannslied, Lagerfeuer, Inselfest) in `tools/treibgut_parts4.py`.
- **Treibgut 0.3.0 – Fangnetz:** eigenes Grundspiel (Cluster-Kaskaden 6×5) in `tools/treibgut_parts5.py` (`NET_JS`). Es überschreibt per späterer Funktionsdeklaration `spin`, `finish`, `quickStop`, `press`, `evaluate`, `buildInfo`, `renderSticky`, `gainDustFromSpin` und wird **vor** dem `start()`-Aufruf eingefügt (sonst Konstanten in der TDZ). Balance: `tools/sim/fangnetz.js` (Gewichte `NET_W`, Auszahlungen `NET_PAY` × Einsatz, Nachfang ×1/×2/×3/×5, Freispiele ×2 bis ×10). Ergebnis: Treffer ~50 %, Freispiele ~1/114, Gesamt ~119 %.
- Rustikale Geräusche in `SFX_JS` (überschreibt Einträge von `sfx`), Wurfhaken statt Laser (`HOOK_*`), ruhigeres Meer (`SKY_SLOW`).
- **Eisenfront** (Werkstatt, Panzer, Fronten) liegt unter `eisenfront/index.html`. Es wird aus der **fertigen Treibgut-Datei** erzeugt, erbt also Fangnetz-Engine, Hilfemodus usw.: `python3 tools/eisenfront.py <treibgut_src.html> <ausgabe.html>`.
  Reihenfolge: Sternenwrack-Quelltext → `treibgut.py` → `eisenfront.py`. Inhalte in `tools/eisenfront_parts1.py` (Symbole, Hund Rex, Brieftaube, Panzer `TANK_SVG`, Gelände `FIELD_SKY`), `parts2` (Texte, Fronten, Crew, Erfolge, `PHRASES_EF`, `WORDS_EF`), `parts3` (Werkstatt-CSS, Musik, Geräusche). Speicher `ef-`, Codes `EFS1-`/`EFK1-`, `WORLD_ID = "eisenfront"`.
  Fehlende Phrasen werden nur gemeldet (`FEHLT:`), Blöcke und `rep` brechen ab.
- **Eisenfront 0.2.0 – Rex sammelt:** eigenes Grundspiel (Sammler-Slot, 5×3, 243 Wege) in `tools/eisenfront_parts4.py` (`COL_JS`). Es ersetzt den Fangnetz-Block aus Treibgut komplett und nutzt dieselbe Kachel-Fläche `#netGrid`. Kisten (`CASH_SYM`, Wert × Einsatz) holt Rex (`REX_SYM`) ein; Rex springt rein (`COL_JUMP`), Brieftaube bringt Kisten (`COL_DROP`). Freispiele: Rex-Zähler je 4 → +10 FS und Sammler `COL_LEV` ×1/×2/×3/×10. Balance: `tools/sim/rexsammelt.js`, Ergebnis Treffer ~47 %, Freispiele ~1/205, Gesamt ~114 %. Düsterer Look als `DARK_CSS`.
- **Fahrzeugklassen (SW 0.12.0, TG 0.4.0, EF 0.3.0):** `VEHICLES` (Name, Mindestrang, Kostenfaktor 1/4/12, Farbe, Text) und `state.vehicle` (0–2, in `SAVE_KEYS`). Umsteigen über `#vehCard` / `switchVehicle()`, wenn `totalSteps() >= 45` und `state.level >= rank`. Teile starten bei 0; Wirkungen rechnen mit `effStep(id) = Klasse × 9 + Stufe` (`catEffect`, `hullPct`, `MAXLINE` je Klasse, `LINE_BETS` bis 200 = Einsatz 1.000). Grafik: `vehicleSVG()` legt `vehLayers()` (pro Welt eigene Zusatzteile) um `shipSVG()`. Treibgut/Eisenfront ersetzen `VEHICLES` und `vehLayers` (`tools/treibgut_parts6.py`, `tools/eisenfront_parts5.py`).
- **Handy (≤ 600 px):** Block `/* ---------- Handy: kompakt` am Ende des CSS: feste Kontrollleiste `.deck` unten (die `.machine` verliert dafür `backdrop-filter`, sonst klebt `position: fixed` am Paneel), Knopfzeile waagerecht scrollbar, Zeilennummern aus. Zoom: `touch-action: manipulation`, `gesturestart` abgefangen, `maximum-scale=1` in der Hülle.
- **Neustadt** (Städtebau) liegt unter `neustadt/index.html` und wird aus der fertigen Eisenfront-Datei erzeugt: `python3 tools/neustadt.py <eisenfront_src.html> <ausgabe.html>`. Reihenfolge: Sternenwrack → `treibgut.py` → `eisenfront.py` → `neustadt.py`.
  Inhalte: `neustadt_parts1.py` (Symbole, Waschbär Paule, Stadtbild `CITY_SVG` mit `vehLayers` für Dorf/Kleinstadt/Metropole, Himmel `CITY_SKY`), `parts2` (Texte, Viertel, Wortliste `WORDS_NS`, Nachkorrekturen `POST_NS`), `parts3` (Grundspiel), `parts4` (Look, Musik, Geräusche, Klicks ins Stadtbild). Speicher `ns-`, Codes `NSS1-`/`NSK1-`.
  Erzeugen der ganzen Kette: Sternenwrack-Quelltext = `index.html` ab `<title>` bis vor `</body></html>`; die Hülle davor/danach wird für die anderen Welten wiederverwendet (Titel tauschen die Skripte selbst).
- **Neustadt 0.1/0.2 (Hochstapler):** frühere Grundspiele, seit 0.3.0 ersetzt. Alte Fassung im Git-Verlauf (`tools/neustadt_parts3.py` vor 0.3.0, Simulation `tools/sim/hochstapler.js`).
- **Neustadt 0.3.0 (Stadtrundfahrt, Brettspiel):** in 0.4.0 wieder ersetzt, Code im Git-Verlauf (Commit 8965bff, `tools/neustadt_parts3.py`), Simulation `tools/sim/stadtrundfahrt.js`.
- **Neustadt 0.4.0 – Skyline-Walzen:** `tools/neustadt_parts3.py` (`SKY_HTML`, `SKY_CSS`, `SKY_JS`), ersetzt den Rex-Block aus Eisenfront. Überschreibt `spin`, `press`, `quickStop`, `evaluate`, `finish`, `buildInfo`, `render` (umhüllt).
  - 6 Walzen (`skCols`, `skGrid[r]` von unten nach oben), Höhe je Dreh nach `SK_HW` (2 bis 7), Wege = Produkt der Treffer je Walze (`skEvaluate`). Symbole `SK_W`, Auszahlung `SK_PAY × SK_SCALE × Einsatz` je Weg. Neue Symbole `tree` (Baum) und `lamp` (Laterne) mit eigenen `ICONS`.
  - Kran (`wild`) nur Walze 2 bis 5. Nachbau (`skCascade`): Gewinnfelder raus, Rest rutscht, oben neu. Freibauten: 4+ `beacon` → 10 (+2 je weitere), in Freibauten 3+ → +5. Multiplikator `skM` +1 pro Nachbau bis 15, gilt nur in Freibauten. 3+ `warp` → Stadtlotterie (Glücksrad).
  - Zellgröße per `--skc` (`skSize`), Positionen über `bottom: calc(var(--skc) * Reihe)`. Dächer in Pixeloptik je Höhe (`skRoof`).
  - Erlasse wirken wie früher: `drones` Kran ×3, `signal` Baugenehmigung ×2,5. Paule-Boost: würfelt die Skyline neu, bis sie gewinnt.
  - Balance: `tools/sim/skyline.js`, Auszahlung ~113 %, Treffer ~54 % (viele kleine), Freibauten ~1/124 mit im Mittel ~60×.
- **Neustadt 0.4.0 – Pixel-Stadt:** `CITY_SVG` in `tools/neustadt_parts1.py` neu: alles als Rechtecke auf 2er-Raster (`pr`, `pxHouse`, `pxLights`), gleiche Schnittstellen (`GEO`, `cityX`, `partAnchors`, `shipSVG`, `vehLayers`, Klickzonen `data-part`). `GY` ist jetzt 116. Der Himmel (`sizeSkyObj`) malt in 1/3 Auflösung, `#sky` mit `image-rendering: pixelated`.
- **Sprachen (SW 0.13.0, TG 0.5.0, EF 0.4.0, NS 0.5.0):** Laufzeit-Übersetzung in der Sternenwrack-Quelle (`LANGS`, `I18N`, `trText`, `trTree`, `MutationObserver` `trObs`, `setLang`). Wahl `#langSel` (oben) und `#introLang` (Start), gespeichert als `welten-lang` (gilt für alle Welten, absichtlich ohne `sw-`-Präfix). Jeder Textknoten und `title`/`aria-label`/`placeholder` wird mit dem Wörterbuch verglichen, Zahlen werden dabei zu `#`. Was fehlt, bleibt Deutsch.
  - Daten: `tools/i18n/ui_*.tsv` (Spalten de, en, es, ja, ru, nl, el; `#` in allen Spalten gleich oft). `tools/i18n.py` setzt sie zwischen `/*I18N-START*/` und `/*I18N-END*/` ein, nur Einträge, deren Wörter (ab 4 Buchstaben) in der Welt vorkommen. Sternenwrack: `python3 tools/i18n.py index.html` nach jeder Textänderung. Die Welt-Skripte entfernen die Daten der Vorstufe am Anfang (sonst stören sie die Ankertexte) und setzen ihre eigenen am Ende ein.
  - Fehlende Texte finden: per Playwright sichtbare Textknoten prüfen, die nicht übersetzt wurden (`trState.get(n)`: `src === out`). Stand: Bedienung übersetzt; Regeln, Hilfe-Blasen, Sprüche der Begleiter, Funkzeilen und Protokoll noch Deutsch.
- **Tab-Symbole:** `tools/favicons.py` (`FAVICONS` je Welt, SVG als data-URL). Sternenwrack: `python3 tools/favicons.py index.html sw`, die Welt-Skripte setzen ihres am Ende.
- **Start-Knopf (SW 0.13.1 usw.):** CSS-Block `Start-Knopf mit Feedback` direkt nach `.spin.stop`, JS-Block `Start-Knopf: Feedback` vor `window.claude?.hot?.snapshot`. Klassen am `#spinwrap`: `pressed` (Einfedern + `.sp-ripple`), `go` (Lichtbogen `.sp-arc`, drehendes Symbol), `won` (über umhülltes `celebrateWin`), `nope` (Kopfschütteln, wenn der Knopf gesperrt ist). Zähler `#spBadge` zeigt Auto-Drehs bzw. Freispiele. Farbe über `--sp-glow` (Standard `--cyan`, in Freispielen `--lime`), also passt er sich jeder Welt an.
- **Versionen für alle Welten auf einmal:** `python3 tools/bump.py "Titel" "Punkt 1" ...` (PATCH) bzw. mit `--minor`. Trägt Version, Protokoll im Spiel, CHANGELOG.md und README ein. Danach Welten neu erzeugen.
- **Sprachen Teil 2 (in Arbeit):** `trFull` übersetzt ganze HTML-Texte (Sprechblasen in `bip`, Hilfe in `helpShow`, Funk in `radio`), Namen werden dabei zu `{C}`/`{S}`. `trRich` übersetzt Absätze mit Fettdruck als Ganzes. Texte gesammelt in `tools/i18n/p2_keys.json` (nummeriert).
