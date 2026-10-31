# Veröffentlicht den Stand aus "experimente" als Testversion unter <seite>/beta/ (liegt im Ordner beta/ auf main).
# Testversion hat eigene Spielstände (Präfix "beta:"), ein Beta-Schild und Welt-Links innerhalb von /beta/.
# Aufruf (im experimente-Checkout): python3 tools/beta.py <pfad-zum-main-checkout>
import os, sys, subprocess

SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DST = os.path.abspath(sys.argv[1])
WORLDS = ["", "treibgut/", "eisenfront/", "neustadt/"]

STORE = ('<script>/*BETA*/(function(){try{var P="beta:",S=Storage.prototype,g=S.getItem,s=S.setItem,r=S.removeItem;'
         'S.getItem=function(k){return g.call(this,P+k)};S.setItem=function(k,v){return s.call(this,P+k,v)};'
         'S.removeItem=function(k){return r.call(this,P+k)};}catch(e){}})();</script>')
BADGE = ('<div aria-hidden="true" style="position:fixed;top:6px;left:50%;transform:translateX(-50%);z-index:2147483000;'
         'pointer-events:none;font:800 11px/1 system-ui,sans-serif;letter-spacing:.12em;color:#1a1200;background:#ffc94a;'
         'padding:5px 12px;border-radius:99px;box-shadow:0 2px 10px rgba(0,0,0,.5)">BETA-TEST · eigene Spielstände</div>')

rev = subprocess.run(["git", "-C", SRC, "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
for w in WORLDS:
    s = open(os.path.join(SRC, w, "index.html"), encoding="utf-8").read()
    old = '(seg ? seg + "/" : "") + sub'
    assert s.count(old) == 1, "Welt-Link nicht gefunden: " + (w or "sternenwrack")
    s = s.replace(old, '(seg ? seg + "/" : "") + "beta/" + sub')
    s = s.replace("<head>", "<head>" + STORE, 1)
    s = s.replace("<title>", "<title>[BETA] ", 1).replace('document.title = COLLECTION + " · "', 'document.title = "[BETA] " + COLLECTION + " · "')
    i = s.rfind("</body>"); s = s[:i] + BADGE + s[i:] if i >= 0 else s + BADGE
    out = os.path.join(DST, "beta", w); os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(s)
open(os.path.join(DST, "beta", "STAND.txt"), "w").write("Testversion aus Zweig experimente, Stand " + rev + "\n")
print("Beta geschrieben, Stand", rev)
