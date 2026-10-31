# Sprachdaten: liest tools/i18n/ui_*.tsv (Spalten de, en, es, ja, ru, nl, el; "#" steht für eine Zahl)
# und setzt pro Welt nur die Einträge ein, deren deutscher Text in der Datei vorkommt.
# Aufruf für Sternenwrack: python3 tools/i18n.py index.html
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BLOCK = re.compile(r"/\*I18N-START\*/.*?/\*I18N-END\*/", re.S)

def load():
    d, bad = {}, []
    for f in sorted(glob.glob(os.path.join(HERE, "i18n", "ui_*.tsv"))):
        for line in open(f, encoding="utf-8"):
            line = line.rstrip("\n")
            if not line or line.startswith("#de"): continue
            p = line.split("\t")
            if len(p) != 7: bad.append((f, line[:60])); continue
            n = p[0].count("#")
            if any(x.count("#") != n for x in p[1:]): bad.append((f, p[0])); continue
            d[p[0]] = p[1:]
    # Teil 2 und 3: nummerierte Übersetzungen (Spalte 1 = Nummer in pX_keys.json); "§" steht für beliebigen Text
    sig = lambda t: (t.count("#"), t.count("§"), t.count("{C}"), t.count("{S}"), sorted(re.findall(r"</?[a-z]+", t)))
    for part in ("p2", "p3", "p4", "p5"):
        kf = os.path.join(HERE, "i18n", part + "_keys.json")
        if not os.path.exists(kf): continue
        keys = json.load(open(kf, encoding="utf-8"))
        for f in sorted(glob.glob(os.path.join(HERE, "i18n", part + "_*.tsv"))):
            for line in open(f, encoding="utf-8"):
                line = line.rstrip("\n")
                if not line or line.startswith("#"): continue
                p = line.split("\t")
                if len(p) != 7 or not p[0].isdigit() or int(p[0]) >= len(keys): bad.append((f, line[:50])); continue
                k = keys[int(p[0])]
                if any(sig(x) != sig(k) for x in p[1:]): bad.append((f, part + " Nr. " + p[0] + " passt nicht")); continue
                d[k] = p[1:]
    return d, bad

def strip(s):
    return BLOCK.sub("/*I18N-START*/{}/*I18N-END*/", s)

def inject(s):
    d, bad = load()
    for b in bad: print("I18N übersprungen:", b)
    body = strip(s)
    pick = {}
    for k, v in d.items():
        words = [w for w in re.findall(r"[A-Za-zÄÖÜäöüß]{4,}", k)]
        if all(w in body for w in words): pick[k] = v
    js = json.dumps(pick, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return BLOCK.sub(lambda m: "/*I18N-START*/" + js + "/*I18N-END*/", body, count=1), len(pick)

if __name__ == "__main__":
    p = sys.argv[1]
    s, n = inject(open(p, encoding="utf-8").read())
    open(p, "w", encoding="utf-8").write(s)
    print("Sprachdaten eingesetzt:", p, n, "Einträge")
