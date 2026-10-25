# Sternenwrack · Entwicklungsnotizen

Stand: **Beta 0.11.0** (25.10.2026). Diese Datei dient als Übergabe für neue Claude-Sitzungen.

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
