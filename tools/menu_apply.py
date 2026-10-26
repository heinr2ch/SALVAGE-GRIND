# Setzt MENU_CSS und MENU_JS aus tools/menu_parts.py in index.html ein (zwischen Markern, mehrfach ausführbar).
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from menu_parts import MENU_CSS, MENU_JS
p = sys.argv[1] if len(sys.argv) > 1 else "index.html"
s = open(p, encoding="utf-8").read()
def put(s, start, end, body, anchor):
    blk = start + body + end
    if start in s:
        return re.sub(re.escape(start) + r".*?" + re.escape(end), lambda m: blk, s, count=1, flags=re.S)
    assert s.count(anchor) >= 1, anchor
    i = s.index(anchor)
    return s[:i] + blk + "\n" + s[i:]
s = put(s, "/*MENU-CSS-START*/", "/*MENU-CSS-END*/", MENU_CSS, "/* ---------- Handy: kompakt")
s = put(s, "/*MENU-JS-START*/", "/*MENU-JS-END*/", MENU_JS, "/* ---------- Start-Knopf: Feedback beim Drücken")
open(p, "w", encoding="utf-8").write(s)
print("Menü eingesetzt:", p)
