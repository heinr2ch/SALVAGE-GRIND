# Versionssprung für alle vier Welten auf einmal: python3 tools/bump.py "Titel" "Punkt 1" "Punkt 2" ...
# Liest die aktuellen Versionen, erhöht PATCH (oder MINOR mit --minor) und trägt alles an allen Stellen ein.
import json, re, sys
args = sys.argv[1:]; minor = "--minor" in args; major = "--major" in args; args = [a for a in args if a not in ("--minor", "--major")]
title, items = args[0], args[1:]
import datetime; D = datetime.date.today().strftime("%d.%m.%Y")
def nxt(v):
    a, b, c = map(int, v.split("."))
    if major: return "1.0.0"
    return f"{a}.{b + 1}.0" if minor else f"{a}.{b}.{c + 1}"
def rd(p): return open(p, encoding="utf-8").read()
def wr(p, s): open(p, "w", encoding="utf-8").write(s)
entry = lambda v: '  { v: "%s", date: "%s", title: "%s", items: %s },\n' % (v, D, title, json.dumps(items, ensure_ascii=False))
W = [  # Welt, Datei mit Version, Muster, Datei mit Protokoll, Protokoll-Anker, CHANGELOG.md, README-Abschnitt
    ("sw", "index.html", r'const GAME_VERSION = "([\d.]+)";', "index.html", "const CHANGELOG = [\n", "CHANGELOG.md", "# Sternenwrack"),
    ("tg", "tools/treibgut_parts5.py", r'TG_VERSION_NET = "([\d.]+)"', "tools/treibgut_parts3.py", "CHANGELOG_NEW = r'''const CHANGELOG = [\n", "treibgut/CHANGELOG.md", "### Treibgut"),
    ("ef", "tools/eisenfront.py", r'const GAME_VERSION = "([\d.]+)";', "tools/eisenfront_parts2.py", "CHANGELOG_EF = r'''const CHANGELOG = [\n", "eisenfront/CHANGELOG.md", "### Eisenfront"),
    ("ns", "tools/neustadt.py", r'const GAME_VERSION = "([\d.]+)";', "tools/neustadt_parts2.py", "CHANGELOG_NS = r'''const CHANGELOG = [\n", "neustadt/CHANGELOG.md", "### Neustadt"),
]
readme = rd("README.md")
for w, vf, pat, cf, anchor, md, sec in W:
    s = rd(vf); old = re.search(pat, s).group(1); new = nxt(old)
    s = s.replace(re.search(pat, s).group(0), re.search(pat, s).group(0).replace(old, new), 1); wr(vf, s)
    s = rd(cf); assert s.count(anchor) == 1, cf; wr(cf, s.replace(anchor, anchor + entry(new)))
    s = rd(md); i = s.index("\n## Beta"); wr(md, s[:i] + f"\n## Beta {new} · {title} · {D}\n" + "".join(f"- {x}\n" for x in items) + s[i:])
    i = readme.index(sec); j = readme.index("**Aktuelle Version: Beta ", i); k = readme.index("**", j + 2)
    readme = readme[:j] + f"**Aktuelle Version: Beta {new}" + readme[k:]
    print(w, old, "→", new)
wr("README.md", readme)
