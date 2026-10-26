# Neustadt Teil 4: Look (Städtebau-Oberfläche), Musik, Geräusche, Klicks ins Stadtbild

FONT_EF = 'family=Black+Ops+One&family=Barlow:wght@400;500;600;700;800&family=Courier+Prime:wght@400;700'
FONT_NS = 'family=Rubik:wght@500;600;700;800&family=Nunito+Sans:wght@400;600;700;800&family=IBM+Plex+Mono:wght@500;700'
ROOT_FONTS_NS = [
    ('--f-display: "Black Ops One", Impact, sans-serif;', '--f-display: "Rubik", system-ui, sans-serif;'),
    ('--f-body: "Barlow", system-ui, sans-serif;', '--f-body: "Nunito Sans", system-ui, sans-serif;'),
    ('--f-mono: "Courier Prime", ui-monospace, monospace;', '--f-mono: "IBM Plex Mono", ui-monospace, monospace;'),
]

CITY_CSS = r'''/* ---------- Neustadt: Städtebau-Oberfläche (Planungstisch, Zonenfarben, klare Kacheln) ---------- */
:root { --bg: #0e1a26; --ink: #eef4f8; --ink-soft: #9ab0c0; --line: rgba(200,225,240,.12); --glass: rgba(200,225,240,.04); --glass-2: rgba(200,225,240,.08);
  --cyan: #7ee0c8; --violet: #4aa8ff; --gold: #ffc94a; --magenta: #ff7a59; --lime: #c6f06b; --win: #7ed957; --lose: #ff6b7a;
  --grad: linear-gradient(135deg, #7ee0c8, #4aa8ff); --r: 16px; }
body { font-synthesis: none;
  background:
    radial-gradient(ellipse 80% 50% at 50% -10%, rgba(126,224,200,.12), transparent 70%),
    radial-gradient(ellipse 60% 50% at 100% 100%, rgba(74,168,255,.12), transparent 70%),
    linear-gradient(rgba(126,224,200,.05) 1px, transparent 1px) 0 0 / 40px 40px,
    linear-gradient(90deg, rgba(126,224,200,.05) 1px, transparent 1px) 0 0 / 40px 40px,
    linear-gradient(180deg, #12222f, #0b141d); background-color: #0b141d; }
#stars { opacity: .8; }
.aurora i { opacity: .08; }
.glass { border: 1px solid rgba(200,225,240,.12); border-radius: 18px; backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
  background: linear-gradient(180deg, rgba(30,52,70,.82), rgba(18,32,44,.88));
  box-shadow: 0 18px 44px rgba(0,0,0,.45), inset 0 1px 0 rgba(255,255,255,.08); }
.glass::after { display: none; }
.brand h1, .topbar .brand h1 { background: linear-gradient(180deg, #ffffff 10%, #7ee0c8 100%); -webkit-background-clip: text; background-clip: text; color: transparent;
  letter-spacing: .04em; filter: none; animation: none; font-weight: 800; }
.intro { background: radial-gradient(ellipse at 50% 30%, rgba(126,224,200,.2), transparent 60%), linear-gradient(180deg, #1c3a5a, #0b141d); }
.intro-title { font-weight: 800; letter-spacing: .06em; }
.intro-title span { background: linear-gradient(180deg, #ffffff, #7ee0c8 70%, #4aa8ff); -webkit-background-clip: text; background-clip: text; filter: drop-shadow(0 3px 0 rgba(0,0,0,.4)) drop-shadow(0 0 22px rgba(126,224,200,.35)); }
.intro-btn { color: #0c1a14; background: linear-gradient(180deg, #8ff0c8, #3fd0a0); border: 0; border-radius: 99px; box-shadow: 0 5px 0 #1f8a64, 0 10px 30px rgba(63,208,160,.3); animation: fadeIn .6s 1.3s both; font-weight: 800; }
.chip { border-radius: 99px; border: 1px solid rgba(200,225,240,.16); background: rgba(255,255,255,.04); color: var(--ink-soft); }
.chip[aria-pressed="true"] { color: #ffffff; border-color: #7ee0c8; background: rgba(126,224,200,.14); }
.radio { background: rgba(8,16,26,.55); border: 1px solid rgba(126,224,200,.25); color: #cfe8f0; border-radius: 99px; font-family: var(--f-body); font-weight: 600; }
.radio span, .radio.hot span { color: #cfe8f0; }
.radio i { background: #7ed957; box-shadow: 0 0 0 2px rgba(126,217,87,.3); }
.radio.hot i { background: #ffc94a; box-shadow: 0 0 0 2px rgba(255,201,74,.3), 0 0 8px #ffc94a; }
.rank, .deck, .expcard, .up, .contract, .stepper, .ptabs { background: rgba(8,16,26,.45); border-color: rgba(200,225,240,.1); }
.lvl { color: #0c1a14; background: linear-gradient(135deg, #8ff0c8, #3fd0a0); }
.jackpot { background: linear-gradient(135deg, rgba(255,201,74,.16), rgba(255,122,89,.12)); border: 1px solid rgba(255,201,74,.4); border-radius: 14px; }
.jackpot b { color: #fff4d0; text-shadow: 0 0 12px rgba(255,201,74,.45); }
.frame { border: 1px solid rgba(200,225,240,.14); border-radius: 18px; background: linear-gradient(180deg, rgba(20,38,54,.95), rgba(12,24,34,.95)); box-shadow: 0 12px 30px rgba(0,0,0,.45); padding: 12px; }
.frame.fs { background: linear-gradient(180deg, rgba(30,54,40,.95), rgba(12,24,20,.95)); box-shadow: 0 0 0 2px rgba(198,240,107,.5), 0 0 26px rgba(198,240,107,.25); }
.frame::before, .frame::after { display: none; }
.spinring { background: conic-gradient(from 0deg, #7ee0c8, #4aa8ff, #ffc94a, #ff7a59, #7ed957, #7ee0c8); filter: none; }
.spin { background: radial-gradient(circle at 50% 30%, #2a4a64 0%, #12222f 70%); color: #ffffff; font-weight: 800; letter-spacing: .06em; }
.spinwrap::after { box-shadow: 0 0 26px rgba(126,224,200,.4); }
.bbtn { color: #0c1a14; border: 0; border-radius: 99px; box-shadow: 0 3px 0 rgba(0,0,0,.35); font-weight: 800; }
.ghost { border: 1px solid rgba(200,225,240,.18); background: rgba(255,255,255,.03); border-radius: 99px; }
.ticket { background: linear-gradient(180deg, #f4f8fa, #dce8ee); color: #12222f; border: 0; }
.ticket small, .ticket .top { color: #4a6070; }
.ticket b { color: color-mix(in srgb, var(--tc) 60%, #12222f); }
.ptabs button[aria-selected="true"] { background: rgba(126,224,200,.16); color: #ffffff; box-shadow: inset 0 0 0 1.5px #7ee0c8; }
.bip-bubble { background: #ffffff; color: #12222f; box-shadow: 0 10px 28px rgba(0,0,0,.4); }
.bip-bubble::before { border-right-color: #ffffff; }
.bip-bubble b { color: #1f8a64; }
.banner { background: radial-gradient(ellipse at center, rgba(10,20,30,.9) 0%, rgba(10,20,30,.75) 70%); }
.shipview { border: 1px solid rgba(200,225,240,.16); border-radius: 14px; }
.toast { background: #ffffff; color: #12222f; pointer-events: none; }
.up { border-radius: 14px; }
.up .buy { border-radius: 12px; }
.netfloat { position: absolute; z-index: 7; transform: translate(-50%, -50%); pointer-events: none; white-space: nowrap;
  font: 700 clamp(1rem, 3.6vw, 1.5rem) var(--f-mono); color: #ffffff; text-shadow: 0 2px 0 rgba(0,0,0,.5), 0 0 14px var(--fc, #7ee0c8); animation: netFloat 1.1s ease-out forwards; }
.netfloat small { display: block; text-align: center; font-size: .62em; color: var(--fc, #7ee0c8); }
@keyframes netFloat { 0% { opacity: 0; transform: translate(-50%, -30%) scale(.6); } 20% { opacity: 1; transform: translate(-50%, -50%) scale(1.12); } 100% { opacity: 0; transform: translate(-50%, -140%) scale(1); } }
.casc { position: absolute; z-index: 6; top: 8px; left: 50%; transform: translateX(-50%); padding: 4px 12px; border-radius: 99px; pointer-events: none; background: #7ee0c8; color: #0c1a14; font: 700 .78rem var(--f-body); }
.sail { transform-box: fill-box; transform-origin: 0% 50%; animation: flagWave 1.8s ease-in-out infinite; }
@keyframes flagWave { 0%, 100% { transform: skewY(-6deg) scaleX(.92); } 50% { transform: skewY(6deg) scaleX(1.06); } }
@media (prefers-reduced-motion: reduce) { .sail { animation: none; } }
'''

MUSIC_NS = r'''/* Eigene Neustadt-Musik: Stadtpark (Lo-Fi), Pendlerjazz (Bossa), Baustellenfunk. */
function mKeys(f, t, dur, vol) { mTone(f, t, dur, { type: "triangle", vol, attack: .006, release: dur * .8 }); mTone(f * 2, t, dur * .5, { type: "sine", vol: vol * .3, attack: .006, release: dur * .45 }); }
function mVinyl(t, dur) { mNoise(t, dur, .006, 3000); }
function mHat(t, vol) { mNoise(t, .04, vol, 8000); }
function mSnr(t, vol) { mNoise(t, .13, vol, 1600); mTone(200, t, .05, { type: "triangle", vol: vol * .6, attack: .001, release: .04 }); }
function mHammer(t, vol) { mTone(1800, t, .05, { type: "square", vol: vol * .4, cutoff: 3000, attack: .001, release: .04 }); mNoise(t, .03, vol, 3500); }
const TRACKS = [
  { id: "park", name: "Stadtpark", bpm: 84,
    step(i, t, mode) {
      // Lo-Fi: weiche Septakkorde, wackliger Beat, Plattenknistern
      const PROG = [[57, 60, 64, 67], [53, 57, 60, 64], [55, 59, 62, 65], [52, 55, 59, 62]], ROOT = [45, 41, 43, 40];
      const STEP = this.dur, bar = Math.floor(i / 16) % 4, s = i % 16, ch = PROG[bar], hot = mode !== "base";
      if (s === 0) { ch.forEach((n, k) => mKeys(NOTE(n), t + k * .012, STEP * 7, .022)); mVinyl(t, STEP * 16); }
      if (s === 8) ch.slice(1).forEach(n => mKeys(NOTE(n), t, STEP * 5, .016));
      if (s === 0 || s === 7 || s === 10) mTone(NOTE(ROOT[bar]), t, STEP * 2.4, { type: "sine", vol: .14, attack: .01, release: .2 });
      if (s === 0 || s === 10) mKick(t, hot ? .22 : .16);
      if (s === 4 || s === 12) mSnr(t + .012, hot ? .05 : .035);
      if (s % 2 === 0) mHat(t + (s % 4 ? .02 : 0), hot ? .03 : .018);
      if ((hot || bar % 2) && (s === 3 || s === 11 || s === 14) && Math.random() < .6) mKeys(NOTE(ch[(Math.random() * 4) | 0] + 12 + (mode === "bonus" ? 12 : 0)), t, STEP * 2, .02);
    } },
  { id: "jazz", name: "Pendlerjazz", bpm: 112,
    step(i, t, mode) {
      // Bossa nova: synkopierter Bass, Rimshot, sanfte Akkorde
      const PROG = [[62, 65, 69, 72], [55, 59, 62, 65], [60, 64, 67, 71], [57, 60, 64, 67]], ROOT = [38, 43, 36, 45];
      const STEP = this.dur, bar = Math.floor(i / 16) % 4, s = i % 16, ch = PROG[bar], hot = mode !== "base";
      if (s === 0 || s === 6 || s === 8 || s === 14) mTone(NOTE(ROOT[bar] + (s >= 8 ? 7 : 0)), t, STEP * 1.8, { type: "triangle", vol: .12, attack: .005, release: .12 });
      if ([0, 3, 6, 10, 12].includes(s) && (hot || bar % 2 === 1)) mTone(800, t, .03, { type: "triangle", vol: hot ? .022 : .016, attack: .001, release: .025 });
      if (s % 2 === 1) mHat(t, hot ? .022 : .014);
      if ([2, 5, 9, 13].includes(s)) ch.forEach(n => mKeys(NOTE(n), t, STEP * 1.2, .013));
      const MEL = [74, 72, 69, 72, 71, 67, 69, 64];
      if ((hot || bar >= 2) && s % 4 === 0) mTone(NOTE(MEL[(i >> 2) % 8] + (mode === "bonus" ? 12 : 0)), t, STEP * 3, { type: "sine", vol: .03, attack: .03, release: .25 });
    } },
  { id: "funk", name: "Baustellenfunk", bpm: 104,
    step(i, t, mode) {
      // Funk: slappender Bass, Hammer als Percussion, Bläser-Stöße
      const ROOT = [40, 40, 43, 38], BASS = [0, 0, 12, 0, 10, 0, 7, 0, 0, 12, 0, 10, 7, 0, 5, 3];
      const STEP = this.dur, bar = Math.floor(i / 16) % 4, s = i % 16, hot = mode !== "base";
      if (BASS[s] !== 0 || s === 0) mTone(NOTE(ROOT[bar] + BASS[s]), t, STEP * .9, { type: "sawtooth", vol: .06, cutoff: 700, attack: .002, release: .06 });
      if (s === 0 || s === 6 || s === 10) mKick(t, hot ? .25 : .18);
      if (s === 4 || s === 12) mSnr(t, hot ? .06 : .045);
      if (s % 2 === 1) mHat(t, .02);
      if (s === 7 || s === 15) mHammer(t, hot ? .06 : .04);
      if ((hot || bar === 3) && (s === 2 || s === 3)) [64, 67, 71].forEach(n => mTone(NOTE(n + (mode === "bonus" ? 12 : 0)), t, STEP * .8, { type: "sawtooth", vol: .014, cutoff: 1800, attack: .01, release: .06 }));
    } },
];
'''

SFX_NS = r'''/* ---------- Neustadt: Stadt-Geräusche (Bauklötze, Kasse, Hupe, Glockenspiel) ---------- */
function lnoise(dur, vol = .3, at = 0, lp = 1200) {
  const c = audio(); if (!c) return;
  const t = c.currentTime + at;
  const buf = c.createBuffer(1, Math.max(1, Math.floor(c.sampleRate * dur)), c.sampleRate);
  const d = buf.getChannelData(0); for (let i = 0; i < d.length; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / d.length, 2);
  const s = c.createBufferSource(), f = c.createBiquadFilter(), g = c.createGain();
  f.type = "lowpass"; f.frequency.value = lp; g.gain.value = vol;
  s.buffer = buf; s.connect(f); f.connect(g); g.connect(master); s.start(t);
}
const block = (f = 420, at = 0, vol = .16) => { tone(f, .08, { type: "triangle", vol, at, slide: .8 }); lnoise(.04, vol * .6, at, 2400); };
const chime = (f, at = 0, vol = .1) => { tone(f, .6, { type: "sine", vol, at }); tone(f * 3, .2, { type: "sine", vol: vol * .2, at }); };
const till = (at = 0) => { tone(2400, .06, { type: "square", vol: .03, at }); chime(1760, at + .06, .08); chime(2349, at + .12, .07); };
const thud = (at = 0, vol = .3) => { tone(80, .3, { type: "sine", vol, at, slide: .5 }); lnoise(.25, vol * .7, at, 500); };
Object.assign(sfx, {
  start() { tone(520, .05, { type: "triangle", vol: .06 }); },
  tick() {},
  stop() { block(380, 0, .14); },
  slam() { block(300, 0, .2); },
  scatter(n) { [784, 988, 1175].forEach((f, i) => chime(f * Math.pow(1.06, n), i * .08, .09)); },
  tease() {},
  coin(i) { [880, 1109, 1319].slice(0, 1 + Math.min(2, i)).forEach((f, k) => block(f, k * .05, .1)); },
  small() { till(0); },
  fanfare(level) {
    const runs = [[523, 659, 784, 1047], [392, 523, 659, 784, 1047, 1319], [392, 523, 659, 784, 1047, 1319, 1568]][level];
    runs.forEach((f, i) => chime(f, i * .08, .09)); till(runs.length * .08);
  },
  fs() { [659, 784, 988, 1319].forEach((f, i) => chime(f, i * .1, .1)); tone(1320, .2, { type: "square", vol: .03, at: .45 }); },
  click() { tone(1100, .03, { type: "sine", vol: .05 }); },
  feature(kind) { if (kind === 0) { [988, 1319].forEach((f, i) => chime(f, i * .08, .09)); } else { tone(392, .18, { type: "square", vol: .05, cutoff: 1500 }); tone(330, .25, { type: "square", vol: .05, at: .2, cutoff: 1500 }); } },
  bonusStart() { [523, 659, 784, 1047, 1319].forEach((f, i) => chime(f, i * .08, .1)); },
  pick(n) { block(600 + n * 40, 0, .1); },
  alarm() { tone(660, .25, { type: "square", vol: .05, slide: .7, cutoff: 1800 }); tone(660, .25, { type: "square", vol: .05, at: .3, slide: .7, cutoff: 1800 }); },
  mult() { [784, 988, 1175, 1568].forEach((f, i) => chime(f, i * .06, .08)); },
  wheelTick() { tone(1500, .02, { type: "square", vol: .03 }); },
  upgrade() { [0, .09, .18].forEach((t, i) => block(500 + i * 120, t, .12)); },
  bigUpgrade() { [0, .08, .16, .24].forEach((t, i) => block(400 + i * 100, t, .13)); [523, 659, 784, 1047, 1319].forEach((f, i) => chime(f, .45 + i * .07, .09)); },
  scrap() { thud(0, .35); lnoise(.7, .25, .05, 900); [0, .12, .26].forEach(t => block(200 + Math.random() * 100, t, .12)); },
  lost() { tone(330, 1.4, { type: "sine", vol: .1, slide: .5 }); thud(.2, .3); lnoise(1.2, .2, .2, 700); },
  clang() { block(240, 0, .2); block(320, .06, .12); },
  squeak(p = 1) { tone(1300 * p, .1, { vol: .12, slide: 1.5 }); tone(1800 * p, .08, { vol: .08, at: .09, slide: .7 }); },
  blips() { [880, 1046, 784].forEach((f, i) => tone(f, .08, { type: "sine", vol: .05, at: i * .08 })); },
  cough() { tone(440, .12, { type: "square", vol: .05, cutoff: 1400 }); tone(440, .2, { type: "square", vol: .05, at: .16, cutoff: 1400 }); },
  boost() { tone(330, .15, { type: "square", vol: .05, cutoff: 1400 }); tone(440, .3, { type: "square", vol: .05, at: .15, cutoff: 1400 }); },
  zap() { lnoise(.25, .2, 0, 4000); tone(120, .3, { type: "sawtooth", vol: .05 }); },
  sonar() { [523, 659, 784].forEach((f, i) => chime(f, i * .12, .07)); },
  creak() { tone(200 + Math.random() * 60, .2, { type: "sawtooth", vol: .04, slide: 1.3, cutoff: 900 }); },
  pew() { tone(300, .5, { type: "sawtooth", vol: .04, slide: 4, cutoff: 2000 }); },
  roll() { [523, 659, 784, 1047].forEach((f, i) => chime(f, i * .07, .1)); },
  ticket() { lnoise(.15, .1, 0, 4000); chime(1319, .1, .07); },
  streakUp(n) { [523, 659, 784, 988, 1175].slice(0, Math.min(5, n + 1)).forEach((f, i) => chime(f * (1 + n * .04), i * .05, .08)); },
  streakBreak() { block(200, 0, .2); },
  mission() { till(0); chime(1568, .2, .08); },
  rankUp() { [523, 659, 784, 1047, 1319].forEach((f, i) => chime(f, i * .08, .1)); till(.5); },
  jackpot() { [0, .3, .6].forEach(t => till(t)); [392, 523, 659, 784, 1047, 1319, 1568].forEach((f, i) => chime(f, 1 + i * .08, .1)); },
  dust() { [1568, 2093, 2637].forEach((f, i) => tone(f, .3, { type: "sine", vol: .06, at: i * .06 })); },
  powerUp() { [659, 784, 988, 1319].forEach((f, i) => chime(f, i * .07, .09)); },
  boostSpin() { [784, 1047, 1319].forEach((f, i) => chime(f, i * .05, .08)); },
  jump() { [392, 523, 659, 784].forEach((f, i) => chime(f, i * .1, .09)); tone(220, .5, { type: "square", vol: .03, at: .5, cutoff: 1200 }); },
  droneIn() { [0, .1, .2].forEach(t => tone(900 + Math.random() * 200, .05, { type: "sine", vol: .04, at: t })); },
  laser(dur) { lnoise(dur, .03, 0, 3000); },
  shatter() { thud(0, .3); lnoise(.4, .22, 0, 1500); },
  crystal() { chime(1319, 0, .09); chime(1760, .06, .07); },
  levelUp() { [523, 784, 1047].forEach((f, i) => chime(f, i * .1, .1)); },
});
function skySparks(sky, x, y, n) {
  const [sx, sy] = toSky(sky, x, y);
  const cols = ["rgba(255,122,89,1)", "rgba(126,224,200,1)", "rgba(255,201,74,1)", "rgba(74,168,255,1)", "rgba(255,79,216,1)"];
  for (let i = 0; i < n; i++) { const a = Math.random() * 6.28, v = 1 + Math.random() * 2.5; sky.parts.push({ x: sx, y: sy, vx: Math.cos(a) * v, vy: Math.sin(a) * v - .5, r: 1.2, life: 1, kind: "spark", col: cols[i % cols.length] }); }
}
'''

CLICK_NS = r'''    const part = zone ? zone.dataset.part : "space";
    const A = partAnchors(state.ship);
    if (part === "hull") {
      sfx.clang(); skySparks(sky, p.x, p.y, 6);
      discover("clang");
      if (H === 0 && Math.random() < .45) {
        const [mx, my] = A.hull, rat = document.createElementNS("http://www.w3.org/2000/svg", "g");
        rat.innerHTML = `<g class="peek"><ellipse cx="${mx}" cy="${my + 18}" rx="6" ry="4.5" fill="#8a8f9c"/><circle cx="${mx - 4}" cy="${my + 14.5}" r="2.4" fill="#8a8f9c"/><circle cx="${mx + 4}" cy="${my + 14.5}" r="2.4" fill="#8a8f9c"/><circle cx="${mx - 2}" cy="${my + 17.5}" r=".9" fill="#111"/><circle cx="${mx + 2}" cy="${my + 17.5}" r=".9" fill="#111"/></g>`;
        fxG.appendChild(rat); setTimeout(() => rat.remove(), 1900);
        setTimeout(() => { sfx.squeak(1.6); bubbleAt(svg, view, mx, my + 8, "Hey! Ich wohne hier!"); }, 350);
        discover("rat");
      } else bubbleAt(svg, view, p.x, p.y - 4, H === 0 ? "Bröckel. Da fiel was ab." : ["Ding-dong! Niemand zu Hause.", "Hier wohnt Familie Müller. Und ein Wellensittich.", "Klopf, klopf. Wer baut da?"][(Math.random() * 3) | 0]);
      return;
    }
    if (part === "cockpit") {
      sfx.blips(); const lines = PILOT_LINES[H], X = cityX(g);
      bubbleAt(svg, view, X.hall, g.t - 4, lines[(Math.random() * lines.length) | 0]); discover("pilot"); return;
    }
    if (part === "engine") {
      sfx.cough(); bubbleAt(svg, view, p.x, 108, E === 0 ? "*holper holper*" : E === 3 ? "*schwusch*" : "*tuut tuut*");
      const ship = groupEl.querySelector(".ship"); if (ship) { ship.classList.add("boost"); setTimeout(() => ship.classList.remove("boost"), 1800); }
      discover("boost"); return;
    }
    if (part === "reactor") {
      sfx.zap();
      const [rx, ry] = A.reactor;
      skySparks(sky, rx, ry, R === 0 ? 18 : 8);
      bubbleAt(svg, view, rx + 10, ry - 10, R === 0 ? "Bitte nicht anfassen! Wirklich nicht!" : ["Strom für alle!", "Grüne Energie, gute Laune.", "Läuft wie geschmiert."][R % 3]);
      discover("reactor"); return;
    }
    if (part === "scanner") {
      sfx.sonar(); const [tx, ty] = A.scanner;
      const c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      c.setAttribute("cx", tx); c.setAttribute("cy", ty); c.setAttribute("r", 8); c.setAttribute("fill", "none"); c.setAttribute("stroke", "#4aa8ff"); c.setAttribute("stroke-width", .8); c.setAttribute("class", "sonar");
      fxG.appendChild(c); setTimeout(() => c.remove(), 1700);
      setTimeout(() => bubbleAt(svg, view, tx, ty - 6, S === 0 ? "Radio: Nur Rauschen. Der Mast ist umgeknickt." : SCAN_LINES[(Math.random() * SCAN_LINES.length) | 0]), 500);
      discover("scanner"); return;
    }
    if (part === "cargo") {
      sfx.creak(); const [cx, cy] = A.cargo;
      const roll = Math.random(), kind = roll < .35 ? "duck" : roll < .65 ? "sock" : "box";
      if (C === 0 && kind !== "duck") { bubbleAt(svg, view, cx, cy, "Der Stand ist umgekippt. Nur Krümel."); return; }
      setTimeout(() => { floatItem(fxG, cx, 118, kind); if (kind === "duck") { sfx.squeak(1); bubbleAt(svg, view, cx, cy, "Quietsch! Sonderangebot!"); discover("duck"); } else bubbleAt(svg, view, cx, cy, kind === "sock" ? "Eine einzelne Socke. Im Angebot." : "Lieferung angekommen!"); }, 250);
      return;
    }
    // Klick in den Himmel: Feuerwerk über der Stadt
    sfx.pew();
    const fl = document.createElementNS("http://www.w3.org/2000/svg", "g"), col = ["#ff7a59", "#7ee0c8", "#ffc94a", "#4aa8ff", "#ff4fd8"][(Math.random() * 5) | 0];
    fl.innerHTML = `<path d="M${p.x},118 L${p.x},${p.y}" stroke="${col}" stroke-width="1" stroke-dasharray="2 3" opacity=".6"><animate attributeName="opacity" from=".8" to="0" dur=".9s" fill="freeze"/></path>${Array.from({ length: 12 }, (_, i) => { const a = i / 12 * 6.28; return `<line x1="${p.x}" y1="${p.y}" x2="${p.x}" y2="${p.y}" stroke="${col}" stroke-width="1.4" stroke-linecap="round"><animate attributeName="x2" from="${p.x}" to="${(p.x + Math.cos(a) * 16).toFixed(1)}" dur=".5s" begin=".25s" fill="freeze"/><animate attributeName="y2" from="${p.y}" to="${(p.y + Math.sin(a) * 16).toFixed(1)}" dur=".5s" begin=".25s" fill="freeze"/></line>`; }).join("")}`;
    fxG.appendChild(fl);
    setTimeout(() => { sfx.dust(); skySparks(sky, p.x, p.y, 16); }, 260);
    let o = 1; const fade = () => { o -= .02; fl.setAttribute("opacity", o); if (o > 0) requestAnimationFrame(fade); else fl.remove(); }; setTimeout(() => requestAnimationFrame(fade), 700);
    discover("laser");
  });
}

'''

STARPOS_NS = [
    ('const x0 = VB.x + VB.w * (.55 + Math.random() * .4), y0 = VB.y - 14, x1 = x0 - 60 - Math.random() * 80, y1 = 112 + Math.random() * 14;',
     'const x0 = VB.x + VB.w + 20, y0 = 20 + Math.random() * 40, x1 = VB.x - 25, y1 = y0 - 10 + Math.random() * 20;'),
    ('st.x = x0 + (x1 - x0) * k + Math.sin(k * 9) * 6; st.y = y0 + (y1 - y0) * k;', 'st.x = x0 + (x1 - x0) * k; st.y = y0 + (y1 - y0) * k + Math.sin(k * 7) * 5;'),
]
