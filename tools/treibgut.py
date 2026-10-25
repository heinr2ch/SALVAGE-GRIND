# Erzeugt "Treibgut" (Meeres-Survival mit Floß) aus dem Sternenwrack-Quelltext.
# Aufruf: python3 treibgut.py <sternenwrack.html> <ausgabe.html>
import re, sys

SRC, OUT = sys.argv[1], sys.argv[2]
s = open(SRC, encoding="utf-8").read()

def rep(a, b, cnt=1):
    global s
    n = s.count(a)
    assert n == cnt, (n, a[:100])
    s = s.replace(a, b)

def rep_all(a, b):
    global s
    s = s.replace(a, b)

def block(start, end, new, keep_end=True):
    """Ersetzt alles von start (inklusive) bis end (exklusive, end bleibt erhalten)."""
    global s
    i = s.index(start)
    j = s.index(end, i + len(start))
    assert s.count(start) == 1, ("start mehrfach", start[:60])
    s = s[:i] + new + s[j:]

from treibgut_parts import *   # Inhalte (Grafiken, Texte)

# ---------- 1. Speicher und Codes trennen ----------
s = re.sub(r'(["`])sw-', r'\1tg-', s)
rep_all("SWS1-", "TGS1-"); rep_all("SWK1-", "TGK1-")

# ---------- 3. Schrift ----------
rep('family=Unbounded:wght@500;700;800', 'family=Fredoka:wght@500;600;700')
rep_all('"Unbounded", "Segoe UI"', '"Fredoka", "Segoe UI"')
rep_all('Unbounded, sans-serif', 'Fredoka, sans-serif')

# ---------- 4. Hintergrund, Kopf, Intro ----------
for a, b in CSS_REPS:
    rep(a, b)
rep_all(EMBLEM_OLD, EMBLEM_NEW)
for a, b in HTML_REPS:
    rep(a, b)

# ---------- 5. Symbole ----------
block("const ICONS = {", "\n// Balance ab Beta", ICONS_NEW)
block("ICONS.wild = `", "\n", WILD_NEW)
for a, b in SYMBOL_REPS:
    rep(a, b)

# ---------- 6. Bip wird Koko, der Papagei ----------
block('    <svg viewBox="0 0 80 92" data-mood="normal" id="bipSvg" aria-hidden="true">', "  </button>\n  <button type=\"button\" class=\"bip-help\"", PARROT_SVG)
block("const BIP = {", "const bipState", BIP_NEW)

# ---------- 7. Floß statt Raumschiff ----------
block("const CATS = [", "CATS.forEach(c =>", CATS_NEW)
rep('const CLASS_NAMES = [[1, "Wrack", "#ff6b7a"], [4, "Schrottschlepper", "#ff9a3c"], [8, "Bergungsfrachter", "#ffc94a"], [12, "Sternenkreuzer", "#4fe3ff"], [14, "Flaggschiff", "#b49cff"], [15, "Legende", "#ff4fd8"]];', CLASS_NEW)
block("/* Schiffsgrafik: jede Kategorie", "/* Himmel, Trümmer und Partikel", RAFT_SVG)
block("function sizeSkyObj(o) {", "const mainSky = makeSky(", OCEAN_SKY)
block("function decalSVG(g) {", "function choosePaint(id) {", DECAL_NEW)
block("const PAINTS = [", "const DECALS = [", PAINTS_NEW)
block("const DECALS = [", "const unlockedCos", DECALS_NEW)
block("const DRONE = `", "function sparkAt(", GULL_NEW)

# ---------- 8. Hintergrund: Luftblasen statt Sterne ----------
block("function drawStars(dt) {", "let lastT = performance.now();", BUBBLES)

# ---------- 9. Welt: Inseln, Crew, Album, Erfolge, Expeditionen ----------
block("const SECTORS = [", "const curSector", SECTORS_NEW)
block("const CREW = [", "const hasCrew", CREW_NEW)
block("const EXPED = [", "const sectorIdx", EXPED_NEW)
block("const ACH = [", "function checkAch()", ACH_NEW)
for a, b in ALBUM_REPS:
    rep(a, b)
rep(RANKS_OLD, RANKS_NEW)
for a, b in SECTOR_CSS:
    rep(a, b)

# ---------- 10. Treibfässer statt Sternschnuppen ----------
for a, b in STAR_REPS:
    rep(a, b)

# ---------- 11. Einzelne Texte mit Grammatik ----------
for a, b in PHRASES:
    n = s.count(a)
    assert n >= 1, ("Phrase fehlt", a[:80])
    s = s.replace(a, b)

# ---------- 2. Farben: Weltall-Palette auf Meer-Palette ----------
for a, b in COLOR_MAP:
    s = re.sub(re.escape(a), b, s, flags=re.I)

# ---------- 12. Allgemeine Wortliste (nur in Texten, Groß-/Kleinschreibung beachtet) ----------
for a, b in WORDS:
    s = re.sub(a, b, s)

rep("\n</style>", EXTRA_CSS)

# ---------- 13. Version und Änderungsprotokoll ----------
s = re.sub(r'const GAME_VERSION = "[^"]+";', f'const GAME_VERSION = "{TG_VERSION}";', s)
block("const CHANGELOG = [", "];\n", CHANGELOG_NEW)

open(OUT, "w", encoding="utf-8").write(s)
print("Treibgut erzeugt:", OUT, len(s), "Zeichen")
