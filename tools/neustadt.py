# Erzeugt "Neustadt" (Städte wieder aufbauen, Grundspiel Hochstapler) aus der fertigen Eisenfront-Datei.
# Aufruf: python3 neustadt.py <eisenfront_src.html> <ausgabe.html>
# Reihenfolge der Welten: Sternenwrack → treibgut.py → eisenfront.py → neustadt.py
import re, sys

SRC, OUT = sys.argv[1], sys.argv[2]
s = open(SRC, encoding="utf-8").read()
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
    assert s.count(start) == 1, ("start", start[:60], s.count(start))
    i = s.index(start); j = s.index(end, i + len(start))
    s = s[:i] + new + s[j:]

def const_def(new):
    global s
    name = re.match(r"const (\w+)", new).group(1)
    pat = (r"const %s = \[[\s\S]*?\n\];" % name) if new.rstrip().endswith("\n];") else (r"const %s = [^\n]*;" % name)
    s, n = re.subn(pat, lambda m: new.rstrip(), s, count=1)
    assert n == 1, ("const", name)

from eisenfront_parts1 import EMBLEM_EF
from eisenfront_parts2 import CLASS_EF
from neustadt_parts1 import *
from neustadt_parts2 import *
from neustadt_parts3 import *
from neustadt_parts4 import *

# 1. Speicher und Codes
s = re.sub(r'(["`])ef-', r'\1ns-', s)
s = s.replace("EFS1-", "NSS1-").replace("EFK1-", "NSK1-")

# 2. Schrift
rep(FONT_EF, FONT_NS)
for a, b in ROOT_FONTS_NS: rep(a, b)
s = s.replace("'Black Ops One', sans-serif", "'Rubik', sans-serif").replace("Black Ops One", "Rubik")

# 3. Emblem, Kopf, Symbole
s = s.replace(EMBLEM_EF, EMBLEM_NS)
for a, b in HTML_NS: rep(a, b)
block("const ICONS = {", "\n// Balance ab Beta", ICONS_NS)
block("ICONS.wild = `", "\n", WILD_NS)

# 4. Paule, der Waschbär
block('    <svg viewBox="0 0 80 92" data-mood="normal" id="bipSvg" aria-hidden="true">', "  </button>\n  <button type=\"button\" class=\"bip-help\"", RACCOON_SVG)
block("const BIP = {", "const bipState", BIP_NS)

# 5. Stadtbild, Himmel, Hintergrund
block("const CATS = [", "CATS.forEach(c =>", CATS_NS)
rep(CLASS_EF, CLASS_NS)
block("/* Panzergrafik", "/* Himmel, Trümmer", CITY_SVG + "\n")
block("function sizeSkyObj(o) {", "const mainSky = makeSky(", CITY_SKY)
block("function drawStars(dt) {", "let lastT = performance.now();", CITY_BG + "\n")
block("function decalSVG(g) {", "function choosePaint(id) {", DECAL_NS)
block("const PAINTS = [", "const DECALS = [", PAINTS_NS)
block("const DECALS = [", "const unlockedCos", DECALS_NS)
block('    const part = zone ? zone.dataset.part : "space";', "/* ---------- Rubbellose", CLICK_NS)

# 6. Welt
block("const SECTORS = [", "const curSector", SECTORS_NS)
block("const CREW = [", "const hasCrew", CREW_NS)
block("const EXPED = [", "const sectorIdx", EXPED_NS)
block("const ACH = [", "function checkAch()", ACH_NS)
for a, b in ALBUM_REPS_NS: rep(a, b)
rep(RANKS_EF, RANKS_NS)
for a, b in SECTOR_CSS_NS: rep(a, b)
for b in LINES_NS: const_def(b)
for a, b in STAR_NS + STARPOS_NS: rep(a, b)

# 7. Texte mit Grammatik
PHRASES_NS.append(("Noch ein Wrack, aber ein großes.", "Noch eine Baustelle, aber eine große."))
PHRASES_NS.append(('"Startet als Wrack · Wirkung baut auf dem alten auf · teurere, stärkere Teile"', '"Startet als Baustelle · Wirkung baut auf der alten auf · teurere, stärkere Ausbauten"'))
for a, b in PHRASES_NS:
    if a not in s: MISSING.append(a); continue
    s = s.replace(a, b)

# 8. Eigenes Grundspiel: Hochstapler
for a, b in TOWER_HTML: rep(a, b)
block("/* ===================== Eisenfront: Rex sammelt", "/* ---------- Eisenfront: Werkstatt-Geräusche", TOWER_JS + "\n")

# 9. Look, Musik, Geräusche
block("/* ---------- Eisenfront: Werkstatt-Look", "</style>", CITY_CSS + TOWER_CSS + "\n")
block("/* Eigene Eisenfront-Musik", "TRACKS.forEach(tr =>", MUSIC_NS)
block("/* ---------- Eisenfront: Werkstatt-Geräusche", "\ncolFill(colBoard(false), false);", SFX_NS)
rep("\ncolFill(colBoard(false), false);\n", "\ntwReelIdle(); twDraw(true); twUi();\n")

for a, b in COLOR_MAP_NS:
    s = re.sub(re.escape(a), b, s, flags=re.I)

# 10. Wortliste
for a, b in WORDS_NS:
    s = re.sub(a, b, s)

for a, b in POST_NS:
    s, n = re.subn(a, b, s)
    if not n: MISSING.append('POST ' + a)

# 11. Fahrzeuge werden Stadtstufen, Version, Protokoll
s = re.sub(r"const VEHICLES = \[\n.*?\n\];\n", lambda m: VEHICLES_NS, s, count=1, flags=re.S)
s = re.sub(r'const GAME_VERSION = "[^"]+";', 'const GAME_VERSION = "0.1.0";', s)
block("const CHANGELOG = [", "];\n", CHANGELOG_NS)

# 12. Welten
s = WORLDS_RE.sub(lambda m: WORLDS_ORIG, s, count=1)
rep('const WORLD_ID = "eisenfront";', 'const WORLD_ID = "neustadt";')

open(OUT, "w", encoding="utf-8").write(s)
print("Neustadt erzeugt:", OUT, len(s), "Zeichen")
for m in MISSING: print("FEHLT:", m[:110])
