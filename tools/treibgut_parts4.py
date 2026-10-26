# Teil 4: rustikales Design und eigene Musik für Treibgut
TG_VERSION_RUSTIC = "0.2.0"

FONT_LINK_OLD = 'family=Fredoka:wght@500;600;700'
FONT_LINK_NEW = 'family=Patua+One&family=Alegreya+Sans:wght@400;500;700;800&family=Courier+Prime:wght@400;700'

ROOT_OLD = """  --f-display: "Fredoka", "Segoe UI", sans-serif;
  --f-body: "Manrope", system-ui, sans-serif;
  --f-mono: "JetBrains Mono", ui-monospace, monospace;"""
ROOT_NEW = """  --f-display: "Patua One", Georgia, serif;
  --f-body: "Alegreya Sans", system-ui, sans-serif;
  --f-mono: "Courier Prime", ui-monospace, monospace;"""

# Grundfarben: wärmer, gedeckter, Holz statt Glas
COLOR_MAP_RUSTIC = [
    ("#4fe3ff", "#5cc8b0"), ("#8b6cff", "#3f86c0"), ("#ff4fd8", "#e0704a"), ("#b49cff", "#8fbfdf"),
    ("#b8ff5c", "#b5d65a"), ("#a48cff", "#d8b27a"), ("#06070f", "#120c07"), ("#0d1022", "#1e140b"),
    ("#141838", "#2a1c10"), ("#0b0d1c", "#1a110a"), ("#e9ecff", "#f3e6c8"), ("#8a90b8", "#b9a684"),
    ("#bff4ff", "#d8f3e8"), ("#ff9ae8", "#f0b08a"), ("#9fb3ff", "#d9b27c"), ("#5dffa8", "#8fe07a"),
    ("#0a0c1a", "#1a110a"), ("#0e1128", "#1c120a"), ("#10132b", "#2a1a0c"), ("#2a2f5c", "#5a3a1a"),
    ("rgba(139,108,255,", "rgba(63,134,192,"), ("rgba(79,227,255,", "rgba(92,200,176,"),
    ("rgba(255,79,216,", "rgba(224,112,74,"), ("rgba(184,255,92,", "rgba(181,214,90,"),
    ("rgba(4,5,12,", "rgba(18,12,7,"), ("rgba(220,225,255,", "rgba(243,230,200,"), ("rgba(6,7,15,", "rgba(18,12,7,"),
    ("rgba(10,12,26,", "rgba(22,14,7,"), ("rgba(93,255,168,", "rgba(143,224,122,"),
]

NAIL = "radial-gradient(circle at {x} {y}, #f1d08a 0 2.2px, #8a6224 2.6px 3.6px, transparent 4px)"
NAILS = ", ".join(NAIL.format(x=x, y=y) for x, y in [("11px", "11px"), ("calc(100% - 11px)", "11px"), ("11px", "calc(100% - 11px)"), ("calc(100% - 11px)", "calc(100% - 11px)")])
ROPE = "repeating-linear-gradient(45deg, #d9b77a 0 5px, #9c7642 5px 8px, #c9a46a 8px 11px)"

RUSTIC_CSS = """
/* ---------- Treibgut: rustikaler Look (Holz, Tau, Messing, Pergament) ---------- */
:root { --ink: #f3e6c8; --ink-soft: #c2ad86; --line: rgba(243,230,200,.14); --glass: rgba(255,240,210,.04); --glass-2: rgba(255,240,210,.08);
  --cyan: #5cc8b0; --violet: #3f86c0; --gold: #e8b04a; --magenta: #e0704a; --lime: #b5d65a; --win: #8fe07a; --lose: #e86a5a;
  --grad: linear-gradient(135deg, #e8b04a, #c9763a); --wood: #3b2614; --wood2: #4a3019; --brass: #d9a84a; }
body { font-synthesis: none;
  background:
    radial-gradient(ellipse 80% 50% at 50% -5%, rgba(255,190,110,.16), transparent 70%),
    radial-gradient(ellipse 60% 50% at 50% 110%, rgba(0,0,0,.6), transparent 70%),
    repeating-linear-gradient(180deg, transparent 0 70px, rgba(0,0,0,.5) 70px 73px, rgba(255,220,170,.05) 73px 74px),
    repeating-linear-gradient(90deg, rgba(255,230,190,.015) 0 2px, rgba(0,0,0,.03) 2px 6px, rgba(255,230,190,.01) 6px 9px),
    linear-gradient(180deg, #2c1b0e, #1c1108); background-color: #1c1108; }
#stars { opacity: .35; }
.aurora i { opacity: .16; }
.glass { backdrop-filter: none; -webkit-backdrop-filter: none; border: 2px solid #6a4622; border-radius: 14px;
  background:
    linear-gradient(180deg, rgba(255,220,170,.06), rgba(0,0,0,.28)),
    repeating-linear-gradient(180deg, transparent 0 46px, rgba(0,0,0,.42) 46px 48px, rgba(255,220,170,.06) 48px 49px),
    repeating-linear-gradient(90deg, rgba(255,230,190,.022) 0 3px, rgba(0,0,0,.035) 3px 8px, rgba(255,230,190,.012) 8px 12px),
    linear-gradient(90deg, #3a2513, #4a301a 45%, #3e2815);
  box-shadow: 0 18px 40px rgba(0,0,0,.6), inset 0 0 0 1px rgba(255,220,170,.07), inset 0 0 50px rgba(0,0,0,.45); }
.glass::after { background: NAILS; opacity: 1; }
.brand h1, .topbar .brand h1 { background: linear-gradient(180deg, #fff1c8 0%, #e8b04a 55%, #a8702a 100%); -webkit-background-clip: text; background-clip: text; color: transparent;
  letter-spacing: .06em; filter: drop-shadow(0 2px 0 #1a0f06); animation: none; font-weight: 400; }
.intro { background: radial-gradient(ellipse at 50% 40%, rgba(255,180,90,.25), transparent 60%), repeating-linear-gradient(180deg, transparent 0 70px, rgba(0,0,0,.5) 70px 73px), linear-gradient(180deg, #2c1b0e, #120b05); }
.intro-title { font-weight: 400; }
.intro-title span { background: linear-gradient(180deg, #fff1c8, #e8b04a 60%, #a8702a); -webkit-background-clip: text; background-clip: text; filter: drop-shadow(0 3px 0 #1a0f06) drop-shadow(0 0 18px rgba(232,176,74,.35)); }
.intro-btn { color: #2a1808; background: linear-gradient(180deg, #f1d08a, #c98e3a); border: 2px solid #7a4e1a; box-shadow: 0 6px 0 #5a3812, 0 10px 30px rgba(0,0,0,.5); animation: fadeIn .6s 1.3s both; font-weight: 400; }
.chip { border-radius: 8px; border: 1.5px solid #8a6436; background: rgba(0,0,0,.28); color: var(--ink-soft); }
.chip[aria-pressed="true"] { color: #fff1c8; border-color: var(--brass); background: rgba(232,176,74,.16); }
.radio { background: linear-gradient(180deg, #efe1bd, #e2cfa3); border: 1px solid #a8885a; color: #3a2a18; border-radius: 4px; box-shadow: 0 2px 0 rgba(0,0,0,.35); }
.radio span, .radio.hot span { color: #3a2a18; }
.radio i { background: #b8322a; box-shadow: 0 0 0 2px #7a1a14; }
.radio.hot i { background: #e0503a; box-shadow: 0 0 0 2px #7a1a14, 0 0 8px #e0503a; }
.rank, .deck, .expcard, .up, .contract, .stepper, .ptabs { background: rgba(20,12,6,.45); border-color: rgba(243,230,200,.12); }
.lvl { color: #2a1808; background: linear-gradient(135deg, #f1d08a, #c98e3a); }
.jackpot { background: linear-gradient(135deg, rgba(232,176,74,.22), rgba(120,70,20,.3)); border: 2px solid #b8862e; }
.jackpot b { color: #fff1c8; text-shadow: 0 2px 0 #1a0f06, 0 0 12px rgba(232,176,74,.5); }
.frame { border: 7px solid transparent; border-radius: 18px; background: linear-gradient(#1c120a, #1c120a) padding-box, ROPE border-box;
  box-shadow: 0 0 0 2px #5a3a1a, 0 12px 30px rgba(0,0,0,.6), inset 0 0 40px rgba(0,0,0,.7); }
.frame.fs { background: linear-gradient(#1c120a, #1c120a) padding-box, ROPE border-box; box-shadow: 0 0 0 2px #5a3a1a, 0 0 26px rgba(181,214,90,.55), inset 0 0 40px rgba(0,0,0,.7); }
.frame::before, .frame::after { border-color: var(--brass); }
.reel { border-radius: 8px; border: 1px solid rgba(243,230,200,.08);
  background: repeating-linear-gradient(90deg, rgba(255,230,190,.02) 0 3px, rgba(0,0,0,.05) 3px 9px), linear-gradient(180deg, #1c120a 0%, #2c1d10 50%, #1c120a 100%); }
.reel::before { background: linear-gradient(180deg, rgba(22,14,7,.92) 0%, transparent 22%, transparent 78%, rgba(22,14,7,.92) 100%); }
.lp span { border-radius: 50%; background: rgba(0,0,0,.3); }
.spinring { background: conic-gradient(from 0deg, #f1d08a, #8a5a1a, #f1d08a, #8a5a1a, #f1d08a); filter: none; }
.spin { background: radial-gradient(circle at 50% 30%, #6a4622 0%, #3a2412 70%); color: #fff1c8; box-shadow: inset 0 2px 0 rgba(255,220,170,.25), inset 0 -6px 14px rgba(0,0,0,.6), 0 0 0 2px #2a1808; font-weight: 400; letter-spacing: .08em; }
.spinwrap::after { box-shadow: 0 0 26px rgba(232,176,74,.5); }
.bbtn { color: #2a1808; border: 2px solid rgba(0,0,0,.35); box-shadow: 0 4px 0 rgba(0,0,0,.35); font-weight: 400; }
.ghost { border: 1.5px solid #8a6436; background: rgba(0,0,0,.25); }
.ticket { background: linear-gradient(180deg, #efe1bd, #dcc89a); color: #3a2a18; border: 1px solid #a8885a; }
.ticket small, .ticket .top { color: #6a5434; }
.ticket b { color: color-mix(in srgb, var(--tc) 70%, #3a2a18); }
.ptabs button[aria-selected="true"] { background: rgba(232,176,74,.18); color: #fff1c8; box-shadow: inset 0 0 0 1.5px var(--brass); }
.bonus-card { border-width: 2px; }
.bip-bubble { background: linear-gradient(180deg, #f6ead0, #e6d3a8); color: #2a1a0a; box-shadow: 0 10px 28px rgba(0,0,0,.5), 0 0 0 1.5px #a8885a; }
.bip-bubble::before { border-right-color: #ecdcb6; }
.bip-bubble b { color: #9a3a1a; }
.banner { background: radial-gradient(ellipse at center, rgba(28,18,9,.92) 0%, rgba(28,18,9,.78) 70%); }
.banner .b-tier, .bonus-card h2, .card h2, .psec h3, .daily b, .ticket b, .boost b, .lab h3 { font-weight: 400; }
.shipview { border: 3px solid #6a4622; box-shadow: inset 0 0 0 2px #2a1808; }
.toast { background: linear-gradient(180deg, #efe1bd, #dcc89a); color: #3a2a18; }
.stat b, .jackpot b, .stepper output b, .float, .banner .b-amt { font-weight: 700; }
.world b { font-weight: 400; }
""".replace("NAILS", NAILS).replace("ROPE", ROPE)

MUSIC_NEW = r'''/* Eigene Treibgut-Musik: Seemannslied (6/8), Lagerfeuer-Gitarre, Inselfest mit Steeldrum. */
function mPluck(f, t, vol, dur = .9) {
  mTone(f, t, dur, { type: "sawtooth", vol: vol * .55, cutoff: 1500, attack: .002, release: dur * .95 });
  mTone(f, t, dur * .7, { type: "triangle", vol: vol * .5, attack: .002, release: dur * .65 });
}
function mAccordion(f, t, dur, vol) { [-7, 7].forEach(d => mTone(f, t, dur, { type: "square", vol, cutoff: 1400, attack: .03, release: .07, detune: d })); }
function mSteel(f, t, vol) {
  mTone(f, t, .45, { type: "sine", vol, attack: .003, release: .42 });
  mTone(f * 2, t, .25, { type: "sine", vol: vol * .4, attack: .003, release: .22 });
  mTone(f * 3.02, t, .14, { type: "sine", vol: vol * .15, attack: .003, release: .12 });
}
function mWood(t, vol, f = 900) { mTone(f, t, .05, { type: "triangle", vol: vol * .8, attack: .001, release: .04 }); }
const TRACKS = [
  { id: "shanty", name: "Seemannslied", bpm: 90,
    step(i, t, mode) {
      // 6/8-Takt mit 12 Schritten: Bass auf 1 und 4, Akkordeon auf den Zwischenschlägen, eigene Melodie in d-Moll
      const PROG = [[62, 65, 69], [60, 64, 67], [62, 65, 69], [57, 61, 64]], ROOT = [38, 36, 38, 33];
      const MEL = [[69, 0, 69, 67, 65, 0], [67, 0, 64, 60, 64, 0], [65, 0, 69, 72, 69, 65], [64, 0, 61, 64, 0, 0],
                   [69, 0, 72, 74, 72, 69], [67, 0, 64, 67, 64, 60], [65, 69, 67, 65, 64, 62], [61, 0, 64, 62, 0, 0]];
      const STEP = this.dur, bar = Math.floor(i / 12) % 4, s = i % 12, ch = PROG[bar], hot = mode !== "base", phrase = Math.floor(i / 48) % 2;
      if (s === 0) mTone(NOTE(ROOT[bar]), t, STEP * 5, { type: "triangle", vol: .11, attack: .005, release: .3 });
      if (s === 6) mTone(NOTE(ROOT[bar] + 7), t, STEP * 5, { type: "triangle", vol: .09, attack: .005, release: .3 });
      if (s === 2 || s === 4 || s === 8 || s === 10) ch.forEach(n => mAccordion(NOTE(n - 12), t, STEP * 1.6, hot ? .013 : .01));
      if (s === 0 || s === 6) mKick(t, hot ? .26 : .17);
      if (s % 2 === 1 && (hot || s === 3 || s === 9)) mNoise(t, .05, hot ? .045 : .03, 5500);
      if (hot && (s === 3 || s === 9)) mWood(t, .03, 900);
      if (s % 2 === 0 && (hot || phrase === 1)) {
        const n = MEL[bar + (phrase ? 4 : 0)][s / 2];
        if (n) mAccordion(NOTE(n + (mode === "bonus" ? 12 : 0)), t, STEP * 1.8, hot ? .02 : .015);
      }
      if (!hot && phrase === 0 && s === 10 && Math.random() < .4) mPluck(NOTE(ch[2] + 12), t, .05, .6);
    } },
  { id: "fire", name: "Lagerfeuer", bpm: 72, gain: 2.2,
    step(i, t, mode) {
      // ruhige Fingerpicking-Gitarre in G-Dur, Meeresrauschen, gepfiffene Töne
      const PROG = [[55, 59, 62, 67], [52, 55, 59, 64], [48, 52, 55, 60], [50, 54, 57, 62]], ROOT = [43, 40, 36, 38];
      const PENTA = [67, 69, 71, 74, 76, 79, 81];
      const STEP = this.dur, bar = Math.floor(i / 16) % 4, s = i % 16, ch = PROG[bar], hot = mode !== "base";
      if (s === 0) { mPluck(NOTE(ROOT[bar]), t, .1, 1.8); mNoise(t, 2.8, .035, 300); }
      if (s === 8) mPluck(NOTE(ROOT[bar] + 7), t, .07, 1.2);
      const pick = [-1, 1, 2, 1, 3, 1, 2, 1];
      if (s % 2 === 0 && pick[(s / 2) % 8] >= 0) mPluck(NOTE(ch[pick[(s / 2) % 8]]), t, hot ? .06 : .05, 1);
      if (hot && s % 2 === 1) mNoise(t, .04, .03, 6500);
      if (hot && (s === 4 || s === 12)) mWood(t, .035, 700);
      const whistle = mode === "bonus" ? .5 : hot ? .3 : .12;
      if ((s === 0 || s === 6 || s === 10) && Math.random() < whistle) mTone(NOTE(PENTA[(Math.random() * PENTA.length) | 0] + 12), t, STEP * 3, { type: "sine", vol: .03, attack: .04, release: .25 });
    } },
  { id: "calypso", name: "Inselfest", bpm: 112,
    step(i, t, mode) {
      // fröhlicher Calypso in C-Dur: Steeldrum, hüpfender Bass, Klanghölzer im 3-2-Rhythmus
      const PROG = [[60, 64, 67], [65, 69, 72], [67, 71, 74], [60, 64, 67]], ROOT = [36, 41, 43, 36];
      const STEP = this.dur, bar = Math.floor(i / 16) % 4, s = i % 16, ch = PROG[bar], hot = mode !== "base";
      const bassPat = [1,0,0,1, 0,0,1,0, 1,0,0,1, 0,0,1,0], bassOff = [0,0,0,7, 0,0,12,0, 0,0,0,7, 0,0,4,0];
      if (bassPat[s]) mTone(NOTE(ROOT[bar] + bassOff[s]), t, STEP * 1.6, { type: "triangle", vol: .12, attack: .005, release: .12 });
      if (s === 0 || s === 8) mKick(t, hot ? .24 : .16);
      if ([0, 3, 6, 10, 12].includes(s) && (hot || bar % 2 === 1)) mWood(t, hot ? .035 : .025);
      if (s % 2 === 1) mNoise(t, .035, hot ? .045 : .028, 7000);
      const steel = [1,0,1,0, 0,1,0,1, 0,0,1,0, 1,0,0,0];
      const seq = [2, 1, 0, 1, 2, 2, 1, 0];
      if (steel[s] && (hot || bar % 2 === 0 || s < 8)) mSteel(NOTE(ch[seq[(i >> 1) % 8] % 3] + 12), t, hot ? .042 : .034);
      if (s === 2 || s === 10) ch.forEach(n => mTone(NOTE(n), t, STEP * .8, { type: "triangle", vol: .018, attack: .004, release: .1 }));
      if (mode === "fs" && s === 14) mSteel(NOTE(ch[2] + 24), t, .04);
    } },
];
'''
