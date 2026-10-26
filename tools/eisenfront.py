# Erzeugt "Eisenfront" (Werkstatt mit Panzer) aus der fertigen Treibgut-Datei.
# Aufruf: python3 eisenfront.py <treibgut_src.html> <ausgabe.html>
import re, sys

SRC, OUT = sys.argv[1], sys.argv[2]
s = open(SRC, encoding="utf-8").read()
from i18n import strip as i18n_strip, inject as i18n_inject
s = i18n_strip(s)  # Sprachdaten der Vorstufe raus, sonst stören sie die Ankertexte
WORLDS_RE = re.compile(r"const WORLDS = \[.*?\n\];\n", re.S)
WORLDS_ORIG = WORLDS_RE.search(s).group(0)
MISSING = []

def rep(a, b, cnt=1):
    global s
    n = s.count(a)
    assert n == cnt, (n, a[:100])
    s = s.replace(a, b)

def block(start, end, new):
    global s
    assert s.count(start) == 1, ("start", start[:60])
    i = s.index(start); j = s.index(end, i + len(start))
    s = s[:i] + new + s[j:]

def const_def(new):
    """Ersetzt die Definition einer Konstante komplett (einzeilig oder als Liste bis \\n];)."""
    global s
    name = re.match(r"const (\w+)", new).group(1)
    pat = (r"const %s = \[[\s\S]*?\n\];" % name) if new.rstrip().endswith("\n];") else (r"const %s = [^\n]*;" % name)
    s, n = re.subn(pat, lambda m: new.rstrip(), s, count=1)
    assert n == 1, ("const", name)

from eisenfront_parts1 import *
from eisenfront_parts2 import *
from eisenfront_parts3 import *
from eisenfront_parts4 import *
from eisenfront_parts5 import *

# 1. Speicher und Codes
s = re.sub(r'(["`])tg-', r'\1ef-', s)
s = s.replace("TGS1-", "EFS1-").replace("TGK1-", "EFK1-")

# 2. Schrift
rep(FONT_TG, FONT_EF)
for a, b in ROOT_FONTS: rep(a, b)

# 3. Emblem, Kopf, Symbole
s = s.replace(EMBLEM_TG, EMBLEM_EF)
for a, b in HTML_EF: rep(a, b)
block("const ICONS = {", "\n// Balance ab Beta", ICONS_EF)
block("ICONS.wild = `", "\n", WILD_EF)

# 4. Rex und Brieftaube
block('    <svg viewBox="0 0 80 92" data-mood="normal" id="bipSvg" aria-hidden="true">', "  </button>\n  <button type=\"button\" class=\"bip-help\"", DOG_SVG)
block("const BIP = {", "const bipState", BIP_EF)
block("const DRONE = `", "function sparkAt(", PIGEON + "\n")

# 5. Panzer, Gelände, Hintergrund
block("const CATS = [", "CATS.forEach(c =>", CATS_EF)
rep(CLASS_TG, CLASS_EF)
block("/* Floßgrafik", "/* Himmel, Trümmer", TANK_SVG + VEH_EF + "\n")
block("function sizeSkyObj(o) {", "const mainSky = makeSky(", FIELD_SKY)
block("function drawStars(dt) {", "let lastT = performance.now();", EMBERS + "\n")
block("function decalSVG(g) {", "function choosePaint(id) {", DECAL_EF)
block("const PAINTS = [", "const DECALS = [", PAINTS_EF)
block("const DECALS = [", "const unlockedCos", DECALS_EF)
rep(HOOK_TG, HOOK_EF)
rep(COUGH_TG, COUGH_EF)

# 6. Welt
block("const SECTORS = [", "const curSector", SECTORS_EF)
block("const CREW = [", "const hasCrew", CREW_EF)
block("const EXPED = [", "const sectorIdx", EXPED_EF)
block("const ACH = [", "function checkAch()", ACH_EF)
for a, b in ACH_EF_REPS: rep(a, b)
for a, b in ALBUM_REPS_EF:
    if a != b: rep(a, b)
rep(RANKS_TG, RANKS_EF)
for a, b in SECTOR_CSS_EF: rep(a, b)
for a, b in LINES_REPS:
    if a != b: const_def(b)
for a, b in STAR_EF: rep(a, b)
for a, b in MAP_REPS: rep(a, b)
rep('fills: ["#2a0f3a", "#3c1652"]', 'fills: ["#2e3424", "#3e4630"]')
rep('fills: ["#3e0d44", "#58145e"]', 'fills: ["#3a3a26", "#4e4e32"]')
rep('fills: ["#520a40", "#76105c"]', 'fills: ["#4a3420", "#64462a"]')

# 7. Texte mit Grammatik
for a, b in PHRASES_EF:
    if a not in s: MISSING.append(a); continue
    s = s.replace(a, b)

# 7b. Eigenes Grundspiel: Rex sammelt (ersetzt das Fangnetz)
for a, b in COL_HTML: rep(a, b)
block("/* ===================== Treibgut: Fangnetz-Kaskaden statt Walzen", "/* ---------- Treibgut: rustikale Geräusche", 'const fmtF = f => String(f).replace(".", ",");\n' + COL_JS + "\n")
rep("\nnetFill(netNewBoard(), false);\n", "\ncolFill(colBoard(false), false);\n")

# 8. Look, Musik, Geräusche
block("/* ---------- Treibgut: rustikaler Look", "/* ---------- Treibgut: Segel und Wellen", MILITARY_CSS + "\n")
block("/* ---------- Treibgut: Segel und Wellen", "/* ---------- Treibgut: Fangnetz", MOTION_EF)
rep(NETGRID_TG, NETGRID_EF)
for a, b in NET_CSS_REPS: rep(a, b)
block("/* Eigene Treibgut-Musik", "TRACKS.forEach(tr =>", MUSIC_EF)
block("/* ---------- Treibgut: rustikale Geräusche", "\ncolFill(colBoard(false), false);", SFX_EF)

for a, b in COLOR_MAP_EF:
    s = re.sub(re.escape(a), b, s, flags=re.I)

rep("\n</style>", "\n" + COL_CSS + DARK_CSS + "</style>")

rep('effect: "Hilfsmöwe 4× so oft"', 'effect: "Rex springt und Tauben liefern doppelt so oft"')

# 9. Wortliste
for a, b in WORDS_EF:
    s = re.sub(a, b, s)
POST_FIX = [
    ('<b id="rankTitle">Schiffbrüchiger</b>', '<b id="rankTitle">Rekrut</b>'),
    ("Strandfund (20), Ordenfieber (100) und Piraten-Jackpot (500)", "Schrottfund (20), Ordensfieber (100) und Tresor-Jackpot (500)"),
    ('"Netz leer. Neuer Schub?"', '"Lager leer. Neuer Schub?"'),
    ("`Fange ${m.goal} Sätze mit", "`Verbaue ${m.goal} Sätze mit"),
    ('"Fange einen Satz aus 8 oder mehr"', '"Verbaue einen Satz aus 8 oder mehr"'),
    ("Ordenfieber", "Ordensfieber"),
    ("Layout: Meer mit Luftblasen im Hintergrund.", "Layout: Werkhalle mit Funken im Hintergrund."),
]
POST_FIX += [
    ("Kostet ${bet()} Schrauben (5 Linien × ${lineBet()}). <b>Leertaste</b> geht auch, erneut drücken stoppt die Walzen sofort.", "Kostet ${bet()} Schrauben. <b>Leertaste</b> geht auch, erneut drücken stoppt sofort."),
    ("`Einsatz pro Linie: <b>${lineBet()}</b>, also ${bet()} Schrauben pro Schub.", "`Einsatz: <b>${bet()}</b> Schrauben pro Schub. Kisten und Gewinne wachsen mit."),
    ("Liniengewinne +", "Alle Gewinne +"),
]
for a, b in POST_FIX:
    if a not in s: MISSING.append("POST " + a); continue
    s = s.replace(a, b)
s = s.replace("'Patua One', serif", "'Black Ops One', sans-serif").replace("Patua One", "Black Ops One")
s = s.replace("/* ---------- Treibgut: Fangnetz", "/* ---------- Eisenfront: Ersatzteillager (Fangnetz-Engine)")

s = re.sub(r"const VEHICLES = \[\n.*?\n\];\n", lambda m: VEHICLES_EF, s, count=1, flags=re.S)

# 10. Version und Protokoll
s = re.sub(r'const GAME_VERSION = "[^"]+";', 'const GAME_VERSION = "0.6.1";', s)
block("const CHANGELOG = [", "];\n", CHANGELOG_EF)

# 11. Welten
s = WORLDS_RE.sub(lambda m: WORLDS_ORIG, s, count=1)
rep('const WORLD_ID = "treibgut";', 'const WORLD_ID = "eisenfront";')

from favicons import set_favicon
from de_fix import de_fix
s = de_fix(s, "ef")
s, _n = i18n_inject(s); print("Sprachdaten:", _n, "Einträge")
s = set_favicon(s, "ef")
open(OUT, "w", encoding="utf-8").write(s)
print("Eisenfront erzeugt:", OUT, len(s), "Zeichen")
for m in MISSING: print("FEHLT:", m[:110])
