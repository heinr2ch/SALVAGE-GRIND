# Tab-Symbole (Favicons) je Welt. Werden von den Welt-Skripten nach dem <title> gesetzt.
# Aufruf für Sternenwrack selbst: python3 tools/favicons.py index.html sw
import re, sys, urllib.parse

FAVICONS = {
    # Sternenwrack: Raumschiff vor Stern auf Nachtblau
    "sw": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#0d1022"/><path d="M24 6l1.2 3 3 1.2-3 1.2L24 14.4l-1.2-3-3-1.2 3-1.2z" fill="#ffd34a"/><path d="M5 20l9-6 10 3-4 6H9z" fill="#7ee0c8"/><path d="M14 14l-2 9h8z" fill="#9b7bff"/><circle cx="17" cy="18" r="1.8" fill="#0d1022"/><path d="M5 20l-2 2 6 1z" fill="#ff5fd2"/></svg>',
    # Treibgut: Floß mit Segel auf Wellen
    "tg": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#0e4a5e"/><circle cx="24" cy="8" r="3.4" fill="#ffd27a"/><path d="M15 6v15" stroke="#7a5230" stroke-width="2"/><path d="M16 7l8 11h-8z" fill="#f2e6c8"/><rect x="7" y="20" width="18" height="4" rx="1" fill="#b07a44"/><path d="M2 27q3-2.5 6 0t6 0 6 0 6 0 6 0" stroke="#7ee0f0" stroke-width="2" fill="none"/></svg>',
    # Eisenfront: Zahnrad mit Panzerkette auf Oliv
    "ef": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#2a2a1e"/><g fill="#c9a24a"><circle cx="16" cy="14" r="7"/><rect x="14.5" y="4" width="3" height="4"/><rect x="14.5" y="20" width="3" height="4"/><rect x="6" y="12.5" width="4" height="3"/><rect x="22" y="12.5" width="4" height="3"/></g><circle cx="16" cy="14" r="3" fill="#2a2a1e"/><rect x="5" y="24" width="22" height="5" rx="2.5" fill="#6f7a52"/><g fill="#2a2a1e"><circle cx="9" cy="26.5" r="1.3"/><circle cx="16" cy="26.5" r="1.3"/><circle cx="23" cy="26.5" r="1.3"/></g></svg>',
    # Neustadt: Pixel-Skyline auf Türkis
    "ns": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" shape-rendering="crispEdges"><rect width="32" height="32" rx="8" fill="#123a4a" shape-rendering="auto"/><rect x="4" y="16" width="6" height="12" fill="#7ee0c8"/><rect x="11" y="8" width="8" height="20" fill="#4aa8ff"/><rect x="14" y="4" width="2" height="4" fill="#ff4b5c"/><rect x="20" y="13" width="8" height="15" fill="#ffc94a"/><g fill="#fff4c8"><rect x="13" y="11" width="2" height="2"/><rect x="16" y="11" width="2" height="2"/><rect x="13" y="16" width="2" height="2"/><rect x="16" y="20" width="2" height="2"/><rect x="22" y="16" width="2" height="2"/><rect x="25" y="20" width="2" height="2"/><rect x="6" y="19" width="2" height="2"/></g><rect x="2" y="28" width="28" height="2" fill="#3a3d46"/></svg>',
}

def favicon_tag(world):
    return '<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%s">' % urllib.parse.quote(FAVICONS[world].replace('"', "'"), safe=" =:/',.-")

def set_favicon(s, world):
    tag = favicon_tag(world)
    if re.search(r'<link rel="icon"[^>]*>', s):
        return re.sub(r'<link rel="icon"[^>]*>', lambda m: tag, s, count=1)
    i = s.index("</title>") + len("</title>")
    return s[:i] + tag + s[i:]

if __name__ == "__main__":
    p, w = sys.argv[1], sys.argv[2]
    s = open(p, encoding="utf-8").read()
    open(p, "w", encoding="utf-8").write(set_favicon(s, w))
    print("Favicon gesetzt:", p, w)
