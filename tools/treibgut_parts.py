# Inhalte für das Treibgut-Thema (Meer, Floß, Inseln)
from treibgut_parts2 import *
from treibgut_parts3 import *

TG_VERSION = "0.1.0"

COLOR_MAP = [
    ("#4fe3ff", "#3fe0c5"), ("#8b6cff", "#2f8fff"), ("#ff4fd8", "#ff7a59"), ("#b49cff", "#7fc8ff"),
    ("#b8ff5c", "#c6f06b"), ("#a48cff", "#d8b27a"), ("#06070f", "#03111a"), ("#0d1022", "#06202b"),
    ("#141838", "#0c2a35"), ("#0b0d1c", "#071a22"), ("#e9ecff", "#e8f7f5"), ("#8a90b8", "#86a9ae"),
    ("#bff4ff", "#c8fff2"), ("#ff9ae8", "#ffb59a"), ("#9fb3ff", "#d9b27c"),
    ("rgba(139,108,255,", "rgba(47,143,255,"), ("rgba(79,227,255,", "rgba(63,224,197,"),
    ("rgba(255,79,216,", "rgba(255,122,89,"), ("rgba(184,255,92,", "rgba(198,240,107,"),
    ("rgba(4,5,12,", "rgba(2,12,18,"), ("rgba(220,225,255,", "rgba(220,245,255,"),
]
COL = dict(COLOR_MAP)

CSS_REPS = [
    ("""    radial-gradient(ellipse 60% 50% at 15% 0%, rgba(139,108,255,.22), transparent 70%),
    radial-gradient(ellipse 50% 40% at 90% 30%, rgba(79,227,255,.12), transparent 70%),
    radial-gradient(ellipse 70% 50% at 50% 110%, rgba(255,79,216,.10), transparent 70%),
    var(--bg);""",
     """    radial-gradient(ellipse 70% 45% at 50% -8%, rgba(255,198,120,.20), transparent 70%),
    radial-gradient(ellipse 55% 45% at 10% 25%, rgba(63,224,197,.16), transparent 70%),
    radial-gradient(ellipse 60% 45% at 92% 40%, rgba(47,143,255,.16), transparent 70%),
    linear-gradient(180deg, #082a3a 0%, #04161f 45%, #020c12 100%);"""),
    ("/* Layout: Sternenfeld im Hintergrund.", "/* Treibgut-Thema (aus Sternenwrack erzeugt). Layout: Meer mit Luftblasen im Hintergrund."),
    (".emblem { width: 46px; height: 46px; flex: none; overflow: visible; filter: drop-shadow(0 0 10px rgba(139,108,255,.5)); }",
     ".emblem { width: 46px; height: 46px; flex: none; overflow: visible; filter: drop-shadow(0 0 10px rgba(63,224,197,.5)); }"),
]

EMBLEM_OLD = """          <path d="M18 41 L28 20 L35 30 L41 24 L46 42 Z" fill="#141838" stroke="url(#emb)" stroke-width="2.6" stroke-linejoin="round"/>
          <path d="M28 20 L31 36 L46 42" fill="none" stroke="url(#emb)" stroke-width="1.3" opacity=".6"/>"""
EMBLEM_NEW = """          <path d="M31 36 V15" stroke="#e8d3a2" stroke-width="2.2" stroke-linecap="round"/>
          <path d="M32.5 16 Q44 24 43 33 H32.5 Z" fill="url(#emb)" stroke="#e8f7f5" stroke-width="1" stroke-linejoin="round"/>
          <path d="M29.5 19 Q22 26 23 33 H29.5 Z" fill="#e8f7f5" opacity=".85"/>
          <rect x="19" y="35" width="26" height="5" rx="2" fill="#7a4f2a" stroke="#e8d3a2" stroke-width="1.4"/>
          <path d="M13 44 q4.75 -3 9.5 0 t9.5 0 t9.5 0 t9.5 0" stroke="url(#emb)" stroke-width="2.4" fill="none" stroke-linecap="round"/>"""

HTML_REPS = [
    ('<h1 class="intro-title" id="introTitle" aria-label="Sternenwrack">STERNENWRACK</h1>', '<h1 class="intro-title" id="introTitle" aria-label="Treibgut">TREIBGUT</h1>'),
    ('<p class="intro-sub">Salvage Slots · Bergen. Ausbauen. Überleben.</p>', '<p class="intro-sub">Survival Slots · Fischen. Bauen. Überleben.</p>'),
    ('<button type="button" class="intro-btn" id="introBtn">Andocken</button>', '<button type="button" class="intro-btn" id="introBtn">Ablegen</button>'),
    ('<title>Sternenwrack</title>', '<title>Treibgut</title>'),
    ('          <h1>Sternenwrack</h1>\n          <small>Salvage Slots · nur Spielcredits ·', '          <h1>Treibgut</h1>\n          <small>Survival Slots · nur Spielmuscheln ·'),
    ('<span id="radioText">Funk: Verbindung zur Bergungsgilde steht.</span>', '<span id="radioText">Funk: Das Funkgerät knistert. Die Strandgilde hört mit.</span>'),
    ('title="Bordroboter Bip ein- oder ausblenden">', 'title="Papagei Koko ein- oder ausblenden">'),
    ('<svg viewBox="0 0 16 16" aria-hidden="true"><rect x="2.5" y="4" width="11" height="9" rx="3.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M8 4V1.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><circle cx="6" cy="8.5" r="1.1" fill="currentColor"/><circle cx="10" cy="8.5" r="1.1" fill="currentColor"/></svg>Bip',
     '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 2.5a4.5 4.5 0 0 0-4.5 4.5c0 3 2 5.5 4.5 7 2.5-1.5 4.5-4 4.5-7A4.5 4.5 0 0 0 8 2.5z" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M8 7.5l2.5 1.5L8 10.5z" fill="currentColor"/><circle cx="6.5" cy="6.5" r="1" fill="currentColor"/></svg>Koko'),
    ('<button type="button" class="bip-bot" id="bipBot" aria-label="Bip, dein Bordroboter. Antippen zum Streicheln.">', '<button type="button" class="bip-bot" id="bipBot" aria-label="Koko, dein Bordpapagei. Antippen zum Kraulen.">'),
    ('aria-label="Hilfemodus: Bip erklärt, worüber du mit der Maus fährst (Taste H)"', 'aria-label="Hilfemodus: Koko erklärt, worüber du mit der Maus fährst (Taste H)"'),
    ('<p class="hint">Leertaste startet. Während des Scans erneut drücken stoppt sofort.</p>', '<p class="hint">Leertaste wirft das Netz aus. Erneut drücken holt es sofort ein.</p>'),
    ('<h3>Boost-Labor <span>bezahlt mit Sternenstaub · zeitlich begrenzt</span></h3>', '<h3>Kräuterhütte <span>bezahlt mit Bernstein · zeitlich begrenzt</span></h3>'),
    ('<h2>Bordzentrale <span>Tagesbonus und Rubbellose</span></h2>', '<h2>Strandhütte <span>Tagesbonus und Rubbellose</span></h2>'),
    ('<b>Tägliche Bergung</b><small id="dailyTxt">', '<b>Tägliche Strandsuche</b><small id="dailyTxt">'),
    ('data-pv="ship" aria-selected="true">Schiff<i', 'data-pv="ship" aria-selected="true">Floß<i'),
    ('data-pv="log" aria-selected="false">Bordbuch<i', 'data-pv="log" aria-selected="false">Logbuch<i'),
    ('<h2>Hangar<small id="shipName">KSV-7 Rostkrähe</small></h2>', '<h2>Lagune<small id="shipName">SOS-7 Salzbrise</small></h2>'),
]

ICONS_NEW = r'''const ICONS = {
  scrap: `<svg viewBox="0 0 40 40"><rect x="4" y="15" width="31" height="11" rx="5.5" fill="#7a4f2a" stroke="#d9b27c" stroke-width="2"/><ellipse cx="31" cy="20.5" rx="3.4" ry="4.6" fill="#d9b27c"/><ellipse cx="31" cy="20.5" rx="1.5" ry="2.2" fill="#7a4f2a"/><path d="M8 19 h13 M10 23 h14" stroke="#4e2f15" stroke-width="1.4" stroke-linecap="round"/><path d="M15 15 l-3 -6" stroke="#4e2f15" stroke-width="1.8" stroke-linecap="round"/><path d="M12 9 q-5 -1 -6 3 q4 1 6 -3z" fill="#6fd17f"/></svg>`,
  cell: `<svg viewBox="0 0 40 40"><path d="M7 34 Q10 12 34 5 Q31 27 7 34 Z" fill="#1d5a2f" stroke="#6fe08a" stroke-width="2" stroke-linejoin="round"/><path d="M7 34 Q19 21 32 7" stroke="#6fe08a" stroke-width="1.6" fill="none"/><path d="M13 27 l-3 -6 M17 23 l-2 -8 M21 19 l0 -8 M16 27 l7 1 M20 23 l8 0 M24 18 l7 -2" stroke="#6fe08a" stroke-width="1.3" stroke-linecap="round"/></svg>`,
  chip: `<svg viewBox="0 0 40 40"><circle cx="19" cy="19" r="14" fill="#5a4120" stroke="#e0b878" stroke-width="2"/><circle cx="19" cy="19" r="9.5" fill="none" stroke="#e0b878" stroke-width="2"/><circle cx="19" cy="19" r="5" fill="none" stroke="#e0b878" stroke-width="2"/><circle cx="19" cy="19" r="1.6" fill="#e0b878"/><path d="M19 5.5 l2.5 3.5 M26 8 l.5 4 M31 13 l-3 2.5 M33 20 l-4 .3" stroke="#a07a3e" stroke-width="1.3"/><path d="M31 27 q5 4 3 10" stroke="#e0b878" stroke-width="2.6" fill="none" stroke-linecap="round"/></svg>`,
  core: `<svg viewBox="0 0 40 40"><path d="M5 20 Q14 8 26 13 L35 6 L33 20 L35 34 L26 27 Q14 32 5 20 Z" fill="#1d3a5a" stroke="#7fc8ff" stroke-width="2" stroke-linejoin="round"/><circle cx="11.5" cy="18.5" r="2" fill="#ffffff"/><circle cx="11.5" cy="18.5" r=".9" fill="#071a22"/><path d="M16 14.5 q3.5 5.5 0 11 M20.5 13.5 q3.5 6.5 0 13" stroke="#bfe4ff" stroke-width="1.4" fill="none"/><path d="M7 22.5 q2.5 1.2 5 0" stroke="#bfe4ff" stroke-width="1.2" fill="none"/><path d="M24 25 l3 4" stroke="#bfe4ff" stroke-width="1.2"/></svg>`,
  crystal: `<svg viewBox="0 0 40 40"><path d="M20 3 C30 12 34 19 34 25 a14 14 0 0 1 -28 0 C6 19 10 12 20 3 Z" fill="#8a4706" stroke="#ffb347" stroke-width="2"/><path d="M20 9 C27 16 29 20 29 25 a9 9 0 0 1 -9 9" stroke="#ffe0a3" stroke-width="1.8" fill="none" opacity=".8"/><ellipse cx="14.5" cy="22" rx="2.6" ry="4.2" fill="#ffffff" opacity=".5"/><path d="M17 27 l3 -2.4 l2.5 3 l2 -1.5" stroke="#3a1e02" stroke-width="1.2" fill="none" stroke-linecap="round"/></svg>`,
  relic: `<svg viewBox="0 0 40 40"><circle cx="20" cy="20" r="15.5" fill="#8a5a08" stroke="#ffd34a" stroke-width="2.2"/><circle cx="20" cy="20" r="11" fill="none" stroke="#ffe39a" stroke-width="1.3" stroke-dasharray="2 2"/><path d="M13.5 22 q6.5 -13 13 0 v3 h-13z" fill="#ffd34a"/><circle cx="17.3" cy="19" r="1.5" fill="#8a5a08"/><circle cx="22.7" cy="19" r="1.5" fill="#8a5a08"/><path d="M16 25 v2 M18.7 25 v2 M21.3 25 v2 M24 25 v2" stroke="#8a5a08" stroke-width="1"/><path d="M9 9 l3 3 M31 9 l-3 3" stroke="#ffe39a" stroke-width="1.4" stroke-linecap="round"/></svg>`,
  beacon: `<svg viewBox="0 0 40 40"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#0d2a14" stroke="#c6f06b" stroke-width="2"/><g transform="rotate(-28 20 16)"><rect x="14.5" y="10" width="11" height="17" rx="4" fill="#2f7a46" stroke="#c6f06b" stroke-width="1.7"/><rect x="17" y="5.5" width="6" height="5.5" rx="1.4" fill="#2f7a46" stroke="#c6f06b" stroke-width="1.5"/><rect x="16.6" y="3.4" width="6.8" height="3" rx="1" fill="#b07a4a"/><rect x="17" y="13.5" width="6" height="10" rx="1" fill="#f4e6c0"/><path d="M18.2 16.5 h3.6 M18.2 19 h2.8 M18.2 21.5 h3.2" stroke="#b07a4a" stroke-width=".9"/></g><path d="M5 25 q3 -2 6 0 t6 0" stroke="#7fc8ff" stroke-width="1.4" fill="none" opacity=".8"/>${band("FREE", "#c6f06b", "#0d2a14")}</svg>`,
  capsule: `<svg viewBox="0 0 40 40"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#2e2104" stroke="#ffc94a" stroke-width="2"/><path d="M8 11 h24 v14 h-24z" fill="#9a6a32" stroke="#ffc94a" stroke-width="1.6" stroke-linejoin="round"/><path d="M8 11 l4 -4 h24 l-4 4 M32 11 l4 -4 v14 l-4 4" fill="#c08a48" stroke="#ffc94a" stroke-width="1.4" stroke-linejoin="round"/><path d="M8 18 h24 M14 11 v14 M26 11 v14" stroke="#5a3a14" stroke-width="1.4"/><circle cx="20" cy="18" r="2" fill="#ffc94a"/><path d="M4 27 q3 -2 6 0 t6 0 t6 0 t6 0 t6 0" stroke="#7fc8ff" stroke-width="1.3" fill="none" opacity=".8"/>${band("BONUS", "#ffc94a", "#2e2104")}</svg>`,
  warp: `<svg viewBox="0 0 40 40"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#082a3a" stroke="#ff7a59" stroke-width="2"/><circle cx="20" cy="16.5" r="12" fill="#0d3d55"/><path d="M20 14a2.5 2.5 0 1 1-2.5 2.5a5 5 0 0 1 5-5a7.5 7.5 0 1 1-7.5 7.5a10 10 0 0 1 10-10" fill="none" stroke="#7fdcff" stroke-width="2.2" stroke-linecap="round"/><circle cx="20" cy="16.5" r="1.8" fill="#fff"/><path d="M28 6 q2 2 4 0 M7 22 q2 2 4 0" stroke="#ffffff" stroke-width="1" fill="none"/>${band("BONUS", "#ff7a59", "#082a3a")}</svg>`,
};
'''

WILD_NEW = r'''ICONS.wild = `<svg viewBox="0 0 40 40"><rect x="1.5" y="1.5" width="37" height="37" rx="9" fill="#071a22" stroke="url(#wildG)" stroke-width="2.4"/><circle cx="20" cy="16" r="11" fill="none" stroke="#ffffff" stroke-width="6"/><path d="M20 5 a11 11 0 0 1 7.8 3.2 l-4.2 4.2 a5 5 0 0 0 -3.6 -1.4z M31 16 a11 11 0 0 1 -3.2 7.8 l-4.2 -4.2 a5 5 0 0 0 1.4 -3.6z M20 27 a11 11 0 0 1 -7.8 -3.2 l4.2 -4.2 a5 5 0 0 0 3.6 1.4z M9 16 a11 11 0 0 1 3.2 -7.8 l4.2 4.2 a5 5 0 0 0 -1.4 3.6z" fill="#ff5a4a"/><circle cx="20" cy="16" r="11" fill="none" stroke="#071a22" stroke-width=".8" opacity=".4"/><path d="M6 6 l1 2.4 2.4 1 -2.4 1 -1 2.4 -1 -2.4 -2.4 -1 2.4 -1z" fill="#ffffff"/>${band("WILD", "url(#wildG)", "#071a22")}</svg>`;'''

SYMBOL_REPS = [
    ('{ id: "scrap",   name: "Schrott",         w: 42, pay: [3, 12, 30],     color: "#b9c3dc" },', '{ id: "scrap",   name: "Treibholz",       w: 42, pay: [3, 12, 30],     color: "#d9b27c" },'),
    ('{ id: "cell",    name: "Energiezelle",    w: 30, pay: [5, 18, 52],     color: "#5dffa8" },', '{ id: "cell",    name: "Palmblatt",       w: 30, pay: [5, 18, 52],     color: "#6fe08a" },'),
    ('{ id: "chip",    name: "Datenkern",       w: 14, pay: [9, 29, 88],     color: "#a48cff" },', '{ id: "chip",    name: "Tau",             w: 14, pay: [9, 29, 88],     color: "#e0b878" },'),
    ('{ id: "core",    name: "Reaktorkern",     w: 9,  pay: [15, 52, 175],   color: "#ff9a3c" },', '{ id: "core",    name: "Thunfisch",       w: 9,  pay: [15, 52, 175],   color: "#7fc8ff" },'),
    ('{ id: "crystal", name: "Sternenkristall", w: 5,  pay: [29, 118, 440],  color: "#4fe3ff" },', '{ id: "crystal", name: "Bernstein",       w: 5,  pay: [29, 118, 440],  color: "#ffb347" },'),
    ('{ id: "relic",   name: "Fremdartefakt",   w: 3,  pay: [49, 175, 735],  color: "#ff6b9a" },', '{ id: "relic",   name: "Piratenmünze",    w: 3,  pay: [49, 175, 735],  color: "#ffd34a" },'),
    ('{ id: "beacon",  name: "Notsignal",       w: 4,  pay: null, special: "#b8ff5c" },', '{ id: "beacon",  name: "Flaschenpost",    w: 4,  pay: null, special: "#c6f06b" },'),
    ('{ id: "capsule", name: "Frachtkapsel",    w: 6,  pay: null, reels: [0, 2, 4], special: "#ffc94a" },', '{ id: "capsule", name: "Treibkiste",      w: 6,  pay: null, reels: [0, 2, 4], special: "#ffc94a" },'),
    ('{ id: "warp",    name: "Sprungkern",      w: 6,  pay: null, reels: [1, 2, 3], special: "#ff4fd8" },', '{ id: "warp",    name: "Strudel",         w: 6,  pay: null, reels: [1, 2, 3], special: "#ff7a59" },'),
    ('const WILD = { id: "wild", name: "Wild-Kristall",', 'const WILD = { id: "wild", name: "Rettungsring",'),
]
