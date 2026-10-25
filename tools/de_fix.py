# Kleine Grammatik-Korrekturen am deutschen Text, die durch die Wortersetzung entstehen.
# Läuft am Ende jedes Welt-Skripts, vor dem Einsetzen der Sprachdaten.
FIX = {
    "tg": [("füllt sich bei Würfe ohne", "füllt sich bei Würfen ohne")],
    "ef": [("füllt sich bei Würfe ohne", "füllt sich bei Schüben ohne"), ("füllt sich bei Schübe ohne", "füllt sich bei Schüben ohne")],
    "ns": [
        ("in der Stadtbild", "im Stadtbild"), ("In der Bauamt", "Im Bauamt"),
        ("Der nächste Runde gewinnt", "Die nächste Runde gewinnt"), ("der nächste Runde gewinnt", "die nächste Runde gewinnt"),
        ("Neues Ruine, neues Glück. Bau es", "Neue Ruine, neues Glück. Bau sie"),
        ("ein neues Ruine", "eine neue Ruine"), ("Neues Ruine", "Neue Ruine"),
        ("Freibautenn", "Freibauten"), ("feste Kran ", "feste Kräne "), ("feste Kran.", "feste Kräne."), ("Jeder sichtbare Wappen", "Jedes sichtbare Wappen"),
        ('} Freibau${fsLeft === 1 ? "" : "e"}', '} Freibau${fsLeft === 1 ? "" : "ten"}'),
    ],
}
def de_fix(s, world):
    for a, b in FIX.get(world, []):
        s = s.replace(a, b)
    return s
