# Eisenfront Teil 3: Look (Stahl, Oliv, Nieten, Warnstreifen), Musik und Geräusche

FONT_TG = 'family=Patua+One&family=Alegreya+Sans:wght@400;500;700;800&family=Courier+Prime:wght@400;700'
FONT_EF = 'family=Black+Ops+One&family=Barlow:wght@400;500;600;700;800&family=Courier+Prime:wght@400;700'
ROOT_FONTS = [
    ('--f-display: "Patua One", Georgia, serif;', '--f-display: "Black Ops One", Impact, sans-serif;'),
    ('--f-body: "Alegreya Sans", system-ui, sans-serif;', '--f-body: "Barlow", system-ui, sans-serif;'),
]

MILITARY_CSS = r'''/* ---------- Eisenfront: Werkstatt-Look (Stahlblech, Oliv, Nieten, Warnstreifen, Khakizettel) ---------- */
:root { --ink: #e8e4d4; --ink-soft: #a9a894; --line: rgba(232,228,212,.13); --glass: rgba(232,228,212,.035); --glass-2: rgba(232,228,212,.07);
  --cyan: #a7c060; --violet: #6f8fa8; --gold: #e8b04a; --magenta: #e07a4a; --lime: #d9c75a; --win: #a7e07a; --lose: #e86a5a;
  --grad: linear-gradient(135deg, #c9d68a, #6f7f3a); --steel: #4a4f55; --steel2: #5c6268; --olive: #4f5a2c; --brass: #c9a24a; }
body { font-synthesis: none;
  background:
    radial-gradient(ellipse 80% 50% at 50% -5%, rgba(255,200,120,.12), transparent 70%),
    radial-gradient(ellipse 60% 50% at 50% 110%, rgba(0,0,0,.6), transparent 70%),
    repeating-linear-gradient(90deg, transparent 0 119px, rgba(0,0,0,.45) 119px 121px, rgba(255,255,255,.04) 121px 122px),
    repeating-linear-gradient(0deg, transparent 0 79px, rgba(0,0,0,.35) 79px 81px),
    radial-gradient(circle at 50% 50%, rgba(255,255,255,.02) 0 1px, transparent 1.5px) 0 0 / 7px 7px,
    linear-gradient(180deg, #262a24, #16181a); background-color: #16181a; }
#stars { opacity: .5; }
.aurora i { opacity: .1; }
.glass { backdrop-filter: none; -webkit-backdrop-filter: none; border: 2px solid #20242a; border-radius: 10px;
  background:
    linear-gradient(180deg, rgba(255,255,255,.05), rgba(0,0,0,.25)),
    radial-gradient(ellipse at 20% 0%, rgba(255,255,255,.05), transparent 60%),
    repeating-linear-gradient(115deg, rgba(255,255,255,.012) 0 2px, rgba(0,0,0,.02) 2px 5px),
    linear-gradient(180deg, #3b4038, #2e322e);
  box-shadow: 0 18px 40px rgba(0,0,0,.6), inset 0 1px 0 rgba(255,255,255,.08), inset 0 0 0 1px rgba(0,0,0,.4), inset 0 0 40px rgba(0,0,0,.35); }
.glass::after { background: radial-gradient(circle at 10px 10px, #b8bec4 0 1.8px, #2a2e32 2.2px 3.2px, transparent 3.6px), radial-gradient(circle at calc(100% - 10px) 10px, #b8bec4 0 1.8px, #2a2e32 2.2px 3.2px, transparent 3.6px), radial-gradient(circle at 10px calc(100% - 10px), #b8bec4 0 1.8px, #2a2e32 2.2px 3.2px, transparent 3.6px), radial-gradient(circle at calc(100% - 10px) calc(100% - 10px), #b8bec4 0 1.8px, #2a2e32 2.2px 3.2px, transparent 3.6px); opacity: 1; }
.brand h1, .topbar .brand h1 { background: linear-gradient(180deg, #f4f0dc 0%, #c9d68a 50%, #6f7f3a 100%); -webkit-background-clip: text; background-clip: text; color: transparent;
  letter-spacing: .08em; filter: drop-shadow(0 2px 0 #0a0c08); animation: none; font-weight: 400; }
.intro { background: radial-gradient(ellipse at 50% 40%, rgba(255,190,100,.18), transparent 60%), repeating-linear-gradient(90deg, transparent 0 119px, rgba(0,0,0,.45) 119px 121px), linear-gradient(180deg, #262a24, #0e100e); }
.intro-title { font-weight: 400; letter-spacing: .06em; }
.intro-title span { background: linear-gradient(180deg, #f4f0dc, #c9d68a 55%, #6f7f3a); -webkit-background-clip: text; background-clip: text; filter: drop-shadow(0 3px 0 #0a0c08) drop-shadow(0 0 18px rgba(167,192,96,.3)); }
.intro-btn { color: #1a1c10; background: repeating-linear-gradient(-45deg, #e8b04a 0 12px, #d9a03a 12px 24px); border: 2px solid #3a3010; box-shadow: 0 6px 0 #2a2410, 0 10px 30px rgba(0,0,0,.5); animation: fadeIn .6s 1.3s both; font-weight: 400; letter-spacing: .1em; }
.chip { border-radius: 6px; border: 1.5px solid #5c6268; background: rgba(0,0,0,.3); color: var(--ink-soft); }
.chip[aria-pressed="true"] { color: #f4f0dc; border-color: #a7c060; background: rgba(167,192,96,.15); }
.radio { background: linear-gradient(180deg, #d8cfa8, #c8bd92); border: 1px solid #8a8058; color: #2a2818; border-radius: 3px; box-shadow: 0 2px 0 rgba(0,0,0,.35); font-family: var(--f-mono); }
.radio span, .radio.hot span { color: #2a2818; }
.radio i { background: #a33a2a; box-shadow: 0 0 0 2px #5a1a10; }
.radio.hot i { background: #e0503a; box-shadow: 0 0 0 2px #5a1a10, 0 0 8px #e0503a; }
.rank, .deck, .expcard, .up, .contract, .stepper, .ptabs { background: rgba(10,12,10,.4); border-color: rgba(232,228,212,.1); }
.lvl { color: #1a1c10; background: linear-gradient(135deg, #c9d68a, #6f7f3a); }
.jackpot { background: linear-gradient(135deg, rgba(232,176,74,.18), rgba(60,50,20,.3)); border: 2px solid #8a7a3a; }
.jackpot b { color: #f4f0dc; text-shadow: 0 2px 0 #0a0c08, 0 0 12px rgba(232,176,74,.45); }
.frame { border: 8px solid transparent; border-radius: 12px; background: linear-gradient(#141614, #141614) padding-box, repeating-linear-gradient(-45deg, #e8b04a 0 10px, #1e2018 10px 20px) border-box;
  box-shadow: 0 0 0 2px #0a0c0a, 0 12px 30px rgba(0,0,0,.6), inset 0 0 40px rgba(0,0,0,.7); }
.frame.fs { background: linear-gradient(#141614, #141614) padding-box, repeating-linear-gradient(-45deg, #d9c75a 0 10px, #1e2018 10px 20px) border-box; box-shadow: 0 0 0 2px #0a0c0a, 0 0 26px rgba(217,199,90,.5), inset 0 0 40px rgba(0,0,0,.7); }
.frame::before, .frame::after { border-color: #b8bec4; }
.reel { border-radius: 6px; border: 1px solid rgba(232,228,212,.07); background: linear-gradient(180deg, #1a1c1a, #2a2e2c 50%, #1a1c1a); }
.reel::before { background: linear-gradient(180deg, rgba(16,18,16,.92) 0%, transparent 22%, transparent 78%, rgba(16,18,16,.92) 100%); }
.lp span { border-radius: 3px; background: rgba(0,0,0,.3); }
.spinring { background: conic-gradient(from 0deg, #e8b04a 0 12.5%, #1e2018 0 25%, #e8b04a 0 37.5%, #1e2018 0 50%, #e8b04a 0 62.5%, #1e2018 0 75%, #e8b04a 0 87.5%, #1e2018 0); filter: none; }
.spin { background: radial-gradient(circle at 50% 30%, #6a7a3a 0%, #3a4420 70%); color: #f4f0dc; box-shadow: inset 0 2px 0 rgba(255,255,255,.18), inset 0 -6px 14px rgba(0,0,0,.6), 0 0 0 2px #14160c; font-weight: 400; letter-spacing: .08em; }
.spinwrap::after { box-shadow: 0 0 26px rgba(167,192,96,.45); }
.bbtn { color: #1a1c10; border: 2px solid rgba(0,0,0,.4); box-shadow: 0 4px 0 rgba(0,0,0,.4); font-weight: 600; border-radius: 6px; }
.ghost { border: 1.5px solid #5c6268; background: rgba(0,0,0,.25); }
.ticket { background: linear-gradient(180deg, #d8cfa8, #c4b98c); color: #2a2818; border: 1px solid #8a8058; }
.ticket small, .ticket .top { color: #5a5434; }
.ticket b { color: color-mix(in srgb, var(--tc) 65%, #2a2818); }
.ptabs button[aria-selected="true"] { background: rgba(167,192,96,.16); color: #f4f0dc; box-shadow: inset 0 0 0 1.5px #a7c060; }
.bonus-card { border-width: 2px; }
.bip-bubble { background: linear-gradient(180deg, #e4dcba, #d2c79e); color: #1e1c10; box-shadow: 0 10px 28px rgba(0,0,0,.5), 0 0 0 1.5px #8a8058; }
.bip-bubble::before { border-right-color: #dcd3b0; }
.bip-bubble b { color: #7a2a1a; }
.banner { background: radial-gradient(ellipse at center, rgba(18,20,16,.92) 0%, rgba(18,20,16,.78) 70%); }
.banner .b-tier, .bonus-card h2, .card h2, .psec h3, .daily b, .ticket b, .boost b, .lab h3 { font-weight: 400; letter-spacing: .04em; }
.shipview { border: 3px solid #3a3e42; box-shadow: inset 0 0 0 2px #0e100e; }
.toast { background: linear-gradient(180deg, #d8cfa8, #c4b98c); color: #2a2818; }
.stat b, .jackpot b, .stepper output b, .float, .banner .b-amt { font-weight: 700; }
.world b { font-weight: 400; }
'''

MOTION_EF = r'''/* ---------- Eisenfront: Ketten und Wimpel ---------- */
.sail { transform-box: fill-box; transform-origin: 0% 50%; animation: flagWave 1.6s ease-in-out infinite; }
@keyframes flagWave { 0%, 100% { transform: skewY(-6deg) scaleX(.92); } 50% { transform: skewY(6deg) scaleX(1.06); } }
.tracks { animation: trackRoll 1.4s linear infinite; }
@keyframes trackRoll { to { stroke-dashoffset: -10; } }
.ship.boost .tracks { animation-duration: .35s; }
.toast { pointer-events: none; }
@media (prefers-reduced-motion: reduce) { .sail, .tracks { animation: none; } }

'''

NETGRID_TG = '''    radial-gradient(ellipse at 50% 120%, rgba(63,134,192,.35), transparent 70%),
    linear-gradient(180deg, #13303a, #0c1f26 60%, #081419); }
.netgrid::after { content: ""; position: absolute; inset: 0; pointer-events: none; background: repeating-linear-gradient(45deg, transparent 0 14px, rgba(255,255,255,.025) 14px 15px), repeating-linear-gradient(-45deg, transparent 0 14px, rgba(255,255,255,.025) 14px 15px); }'''
NETGRID_EF = '''    radial-gradient(ellipse at 50% -20%, rgba(255,220,150,.14), transparent 65%),
    linear-gradient(180deg, #2c302c, #232623 60%, #1a1c1a); }
.netgrid::after { content: ""; position: absolute; inset: 0; pointer-events: none;
  background: radial-gradient(circle, rgba(0,0,0,.35) 0 1.6px, transparent 2px) 0 0 / 14px 14px, repeating-linear-gradient(115deg, rgba(255,255,255,.012) 0 2px, rgba(0,0,0,.02) 2px 6px); }'''
NET_CSS_REPS = [
    ('background: linear-gradient(180deg, #f1d08a, #c98e3a); color: #2a1808; border: 2px solid #7a4e1a; font: 700 .78rem var(--f-body);',
     'background: repeating-linear-gradient(-45deg, #e8b04a 0 8px, #d9a03a 8px 16px); color: #1a1c10; border: 2px solid #3a3010; font: 700 .78rem var(--f-body);'),
    ('color: #fff1c8; text-shadow: 0 2px 0 #1a0f06, 0 0 14px var(--fc, #8fe07a);', 'color: #f4f0dc; text-shadow: 0 2px 0 #0a0c08, 0 0 14px var(--fc, #a7e07a);'),
    ('.swarmdemo i.on { background: #7fc8ff; box-shadow: 0 0 8px #7fc8ff; }', '.swarmdemo i.on { background: #e07a4a; box-shadow: 0 0 8px #e07a4a; }'),
]

MAP_REPS = [
    ('stars += `<path d="M${x},${y} q3,-3 6,0 t6,0" stroke="#bfeee6" stroke-width="1" fill="none" opacity="${.15 + (i % 4) * .07}"/>`; }',
     'if (i < 12) stars += `<path d="M0,${i * 20 + 6} H400 M${i * 36},0 V230" stroke="#c9d68a" stroke-width=".6" opacity=".12"/>`; stars += `<path d="M${x - 4},${y} q4,-4 8,0 q4,4 8,0" stroke="#8a9a5a" stroke-width="1" fill="none" opacity="${.12 + (i % 4) * .05}"/>`; }'),
    ('fill="${ok ? "#d9c08a" : "#5a6a6a"}" opacity="${ok ? .55 : .3}"', 'fill="${ok ? "#7a8a4a" : "#4a4e4a"}" opacity="${ok ? .5 : .3}"'),
    ('<g class="mapship"><path d="M${x.x - 6},${x.y - 26} l12 5 l-12 5 l3 -5z" fill="#ffffff"/></g>', '<g class="mapship"><path d="M${x.x},${x.y - 22} v-12" stroke="#e8e4d4" stroke-width="1.4"/><path d="M${x.x},${x.y - 34} l10 3 l-10 3z" fill="#e07a4a"/></g>'),
    ('font-family="Manrope, sans-serif" font-weight="700" font-size="10" fill="${ok ? "#f3e6c8" : "#6b7099"}"', 'font-family="Barlow, sans-serif" font-weight="700" font-size="10" fill="${ok ? "#e8e4d4" : "#6b6f66"}"'),
]

MUSIC_EF = r'''/* Eigene Eisenfront-Musik: Werkstattmarsch, Mundharmonika-Blues, Werkhalle mit Amboss. */
function mBrass(f, t, dur, vol) {
  mTone(f, t, dur, { type: "sawtooth", vol: vol * .6, cutoff: 1300, attack: .03, release: .08 });
  mTone(f, t, dur, { type: "square", vol: vol * .3, cutoff: 900, attack: .04, release: .08, detune: 6 });
}
function mHarp(f, t, dur, vol) { [-9, 9].forEach(d => mTone(f, t, dur, { type: "square", vol, cutoff: 2200, attack: .04, release: .1, detune: d })); mNoise(t, dur * .6, vol * .4, 3000); }
function mSnare(t, vol) { mNoise(t, .12, vol, 1800); mTone(190, t, .06, { type: "triangle", vol: vol * .7, attack: .001, release: .05 }); }
function mAnvil(f, t, vol) {
  mTone(f, t, .9, { type: "sine", vol, attack: .001, release: .85 });
  mTone(f * 2.42, t, .5, { type: "sine", vol: vol * .45, attack: .001, release: .45 });
  mTone(f * 4.1, t, .2, { type: "sine", vol: vol * .2, attack: .001, release: .18 });
  mNoise(t, .03, vol * .8, 4000);
}
const TRACKS = [
  { id: "march", name: "Werkstattmarsch", bpm: 112,
    step(i, t, mode) {
      // gerader 2/4-Marsch in B-Dur: Tuba auf 1 und 3, Trommelwirbel, Blechbläser-Melodie
      const PROG = [[58, 62, 65], [63, 67, 70], [65, 69, 72], [58, 62, 65]], ROOT = [34, 39, 41, 34];
      const MEL = [[70, 0, 70, 72, 74, 0, 70, 0], [75, 0, 74, 72, 70, 0, 67, 0], [72, 0, 72, 74, 77, 0, 72, 0], [70, 72, 74, 72, 70, 0, 0, 0]];
      const STEP = this.dur, bar = Math.floor(i / 16) % 4, s = i % 16, ch = PROG[bar], hot = mode !== "base", phrase = Math.floor(i / 64) % 2;
      if (s === 0 || s === 8) mTone(NOTE(ROOT[bar]), t, STEP * 3, { type: "triangle", vol: .13, attack: .005, release: .2 });
      if (s === 4 || s === 12) mTone(NOTE(ROOT[bar] + 7), t, STEP * 3, { type: "triangle", vol: .1, attack: .005, release: .2 });
      if (s === 4 || s === 12) ch.forEach(n => mBrass(NOTE(n - 12), t, STEP * 1.4, hot ? .014 : .01));
      if (s === 0 || s === 8) mKick(t, hot ? .24 : .16);
      if (s === 4 || s === 12) mSnare(t, hot ? .07 : .05);
      if (hot && s % 2 === 1) mSnare(t, .025);
      if (!hot && (s === 14 || s === 15)) mSnare(t, .02);
      if (s % 2 === 0 && (hot || phrase === 1)) { const n = MEL[bar][s / 2]; if (n) mBrass(NOTE(n + (mode === "bonus" ? 12 : 0)), t, STEP * 1.8, hot ? .022 : .016); }
      if (mode === "fs" && s === 0 && bar === 0) mBell(NOTE(82), t, .03);
    } },
  { id: "harp", name: "Mundharmonika", bpm: 76,
    step(i, t, mode) {
      // langsamer Blues in E: gezupfter Bass, Besen auf der Snare, klagende Mundharmonika
      const PROG = [[52, 56, 59], [57, 61, 64], [52, 56, 59], [59, 63, 66]], ROOT = [40, 45, 40, 47];
      const BLUES = [64, 67, 69, 70, 71, 74, 76];
      const STEP = this.dur, bar = Math.floor(i / 16) % 4, s = i % 16, ch = PROG[bar], hot = mode !== "base";
      const bassPat = [0, 4, 7, 9, 10, 9, 7, 4];
      if (s % 2 === 0) mTone(NOTE(ROOT[bar] + bassPat[s / 2]), t, STEP * 1.8, { type: "triangle", vol: .1, attack: .004, release: .15 });
      if (s === 4 || s === 12) mNoise(t, .2, hot ? .05 : .035, 2500);
      if (s % 4 === 2) mNoise(t, .06, .02, 6000);
      if (s === 0 || s === 8) mKick(t, hot ? .2 : .13);
      if (s === 0 || s === 6) ch.forEach(n => mTone(NOTE(n), t, STEP * 3, { type: "triangle", vol: .016, attack: .02, release: .3 }));
      const p = mode === "bonus" ? .55 : hot ? .4 : .22;
      if ((s === 0 || s === 3 || s === 6 || s === 10 || s === 12) && Math.random() < p) mHarp(NOTE(BLUES[(Math.random() * BLUES.length) | 0]), t, STEP * (2 + (Math.random() * 3 | 0)), .012);
    } },
  { id: "forge", name: "Werkhalle", bpm: 120,
    step(i, t, mode) {
      // stampfende Werkhalle in a-Moll: Amboss-Schläge, zischender Dampf, tiefer Maschinenbass
      const PROG = [[57, 60, 64], [53, 57, 60], [55, 59, 62], [52, 56, 59]], ROOT = [33, 29, 31, 28];
      const STEP = this.dur, bar = Math.floor(i / 16) % 4, s = i % 16, ch = PROG[bar], hot = mode !== "base";
      if (s % 4 === 0) mKick(t, hot ? .28 : .2);
      if ([0, 3, 6, 8, 11, 14].includes(s)) mTone(NOTE(ROOT[bar] + (s === 6 || s === 14 ? 12 : 0)), t, STEP * 1.5, { type: "sawtooth", vol: .05, cutoff: 420, attack: .004, release: .08 });
      if (s === 4 || s === 12) mAnvil(NOTE(ch[0] + 12), t, hot ? .05 : .04);
      if (hot && (s === 7 || s === 15)) mAnvil(NOTE(ch[2] + 12), t, .03);
      if (s === 10) mNoise(t, .35, hot ? .05 : .03, 5000);
      if (s % 2 === 1) mNoise(t, .03, hot ? .04 : .024, 7500);
      const seq = [0, 2, 1, 2];
      if ((hot || bar % 2 === 1) && s % 4 === 2) mTone(NOTE(ch[seq[(i >> 2) % 4]] + 12 + (mode === "bonus" ? 12 : 0)), t, STEP * 1.6, { type: "square", vol: .016, cutoff: 1800, attack: .005, release: .1 });
    } },
];
'''

SFX_EF = r'''/* ---------- Eisenfront: Werkstatt-Geräusche (Blech, Ratsche, Druckluft, Amboss) ---------- */
function lnoise(dur, vol = .3, at = 0, lp = 1200) {
  const c = audio(); if (!c) return;
  const t = c.currentTime + at;
  const buf = c.createBuffer(1, Math.max(1, Math.floor(c.sampleRate * dur)), c.sampleRate);
  const d = buf.getChannelData(0); for (let i = 0; i < d.length; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / d.length, 2);
  const s = c.createBufferSource(), f = c.createBiquadFilter(), g = c.createGain();
  f.type = "lowpass"; f.frequency.value = lp; g.gain.value = vol;
  s.buffer = buf; s.connect(f); f.connect(g); g.connect(master); s.start(t);
}
const clank = (f = 320, at = 0, vol = .14) => { tone(f, .4, { type: "triangle", vol, at }); tone(f * 2.7, .18, { type: "sine", vol: vol * .4, at }); lnoise(.04, vol * .8, at, 4000); };
const anvil = (f = 880, at = 0, vol = .12) => { tone(f, 1.1, { type: "sine", vol, at }); tone(f * 2.42, .5, { type: "sine", vol: vol * .4, at }); tone(f * 4.1, .2, { type: "sine", vol: vol * .2, at }); };
const ratchet = (n = 5, at = 0, vol = .12) => { for (let k = 0; k < n; k++) { tone(1800, .02, { type: "square", vol: vol * .5, at: at + k * .045 }); lnoise(.02, vol * .4, at + k * .045, 5000); } };
const hiss = (at = 0, vol = .15, dur = .4) => { noise(dur, vol, at, 3500); };
const thud = (at = 0, vol = .3) => { tone(90, .25, { type: "sine", vol, at, slide: .5 }); lnoise(.12, vol * .6, at, 500); };
Object.assign(sfx, {
  start() { ratchet(4, 0, .1); hiss(.12, .06, .25); },
  tick() {},
  stop() { clank(260, 0, .12); },
  slam() { thud(0, .3); clank(180, .02, .14); },
  scatter(n) { [880, 1175].forEach((f, i) => anvil(f * Math.pow(1.06, n), i * .07, .08)); },
  tease() {},
  coin(i) { [1568, 2093, 2637].slice(0, 2 + (i > 1 ? 1 : 0)).forEach((f, k) => tone(f, .1, { type: "square", vol: .03, at: k * .05 })); lnoise(.05, .06, 0, 5000); },
  small() { clank(523, 0, .1); clank(659, .08, .09); },
  fanfare(level) {
    const runs = [[523, 659, 784, 1047], [392, 523, 659, 784, 1047, 1319], [392, 523, 659, 784, 1047, 1319, 1568]][level];
    runs.forEach((f, i) => clank(f, i * .08, .1));
    anvil(1047, runs.length * .08, .1 + level * .02);
    if (level >= 1) hiss(runs.length * .08, .12, .5);
  },
  fs() { [0, .18, .36].forEach(t => tone(523, .14, { type: "square", vol: .05, at: t })); tone(784, .6, { type: "square", vol: .05, at: .56 }); thud(.56, .2); },
  click() { tone(1400, .03, { type: "square", vol: .04 }); lnoise(.02, .05, 0, 4000); },
  feature(kind) { if (kind === 0) { clank(200, 0, .2); clank(240, .08, .16); } else { hiss(0, .15, .6); tone(140, .6, { type: "sawtooth", vol: .05, slide: 1.4 }); } },
  bonusStart() { thud(0, .25); [523, 659, 784, 1047].forEach((f, i) => clank(f, .4 + i * .08, .1)); },
  pick(n) { ratchet(2, 0, .08); clank(440 + n * 30, .08, .1); },
  alarm() { [0, .28].forEach(t => tone(660, .22, { type: "square", vol: .06, at: t, slide: .75 })); thud(0, .25); },
  mult() { [784, 988, 1175, 1568].forEach((f, i) => clank(f, i * .06, .09)); },
  wheelTick() { tone(1600, .02, { type: "square", vol: .04 }); },
  upgrade() { ratchet(6, 0, .12); clank(300, .3, .14); },
  bigUpgrade() { ratchet(8, 0, .12); [0, .45, .7].forEach((t, i) => anvil(660 + i * 110, t, .1)); hiss(.9, .12, .5); },
  scrap() { thud(0, .35); lnoise(.5, .25, 0, 700); clank(150, .1, .15); },
  lost() { tone(110, 1.8, { type: "sawtooth", vol: .06, slide: .5 }); hiss(0, .1, 1.4); [0, .35, .6].forEach(t => thud(t, .15)); },
  clang() { clank(170, 0, .3); clank(240, .06, .18); },
  squeak(p = 1) { tone(1100 * p, .12, { vol: .12, slide: 1.5 }); tone(1600 * p, .1, { vol: .09, at: .1, slide: .7 }); },
  blips() { [880, 660, 990].forEach((f, i) => tone(f, .08, { type: "square", vol: .03, at: i * .09 })); },
  cough() { [0, .09, .17, .3].forEach(t => thud(t, .14)); lnoise(.6, .12, 0, 800); },
  boost() { tone(55, 1.4, { type: "sawtooth", vol: .08, slide: 2.2 }); lnoise(1.4, .18, 0, 500); },
  zap() { hiss(0, .12, .3); [0, .07, .15].forEach(t => clank(1200, t, .05)); },
  sonar() { tone(1200, .5, { type: "square", vol: .03 }); tone(1200, .5, { type: "square", vol: .03, at: .6 }); },
  creak() { tone(140 + Math.random() * 40, .3, { type: "sawtooth", vol: .05, slide: 1.3 }); },
  pew() { tone(300, .35, { type: "sawtooth", vol: .05, slide: 3 }); hiss(0, .08, .3); },
  roll() { ratchet(6, 0, .1); [523, 659, 784, 1047].forEach((f, i) => clank(f, .4 + i * .06, .09)); },
  ticket() { lnoise(.15, .1, 0, 4000); clank(1047, .1, .06); },
  streakUp(n) { [523, 659, 784, 988, 1175].slice(0, Math.min(5, n + 1)).forEach((f, i) => clank(f * (1 + n * .04), i * .05, .08)); },
  streakBreak() { thud(0, .25); },
  mission() { anvil(1047, 0, .09); clank(1319, .15, .07); },
  rankUp() { [523, 659, 784, 1047].forEach((f, i) => tone(f, .18, { type: "square", vol: .04, at: i * .12 })); tone(1047, .7, { type: "square", vol: .045, at: .5 }); anvil(784, .5, .1); },
  jackpot() { thud(0, .35); [0, .35, .7, 1.05].forEach(t => anvil(880, t, .13)); [392, 523, 659, 784, 1047, 1319, 1568].forEach((f, i) => clank(f, 1.2 + i * .08, .1)); },
  dust() { [1568, 2093, 2637].forEach((f, i) => tone(f, .3, { type: "sine", vol: .06, at: i * .06 })); },
  powerUp() { ratchet(5, 0, .1); [659, 784, 988, 1319].forEach((f, i) => clank(f, .4 + i * .07, .09)); },
  boostSpin() { [784, 1047, 1319].forEach((f, i) => clank(f, i * .05, .08)); },
  jump() { tone(45, 1.6, { type: "sawtooth", vol: .09, slide: 2.4 }); lnoise(1.6, .22, 0, 600); anvil(660, 1.2, .08); },
  droneIn() { [0, .12, .24, .36].forEach(t => lnoise(.08, .08, t, 1500)); tone(900, .1, { type: "sine", vol: .04, at: .45, slide: 1.3 }); },
  laser(dur) { hiss(0, .05, dur); },
  shatter() { clank(140, 0, .25); lnoise(.4, .22, 0, 1500); },
  crystal() { clank(1319, 0, .08); [1568, 2093].forEach((f, i) => tone(f, .4, { type: "triangle", vol: .06, at: .05 + i * .05 })); },
  levelUp() { [523, 784, 1047].forEach((f, i) => clank(f, i * .1, .1)); },
});
function skySparks(sky, x, y, n) {
  const [sx, sy] = toSky(sky, x, y);
  for (let i = 0; i < n; i++) sky.parts.push({ x: sx, y: sy, vx: (Math.random() - .5) * 4, vy: -1 - Math.random() * 2.5, r: 1.3, life: 1, kind: "spark" });
}
'''
