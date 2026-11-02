// Salvage & Grind – Desktop-Hülle (Electron). Liefert die fünf Welten über einen kleinen Server auf diesem PC aus (http://localhost),
// damit die Online-Funktionen (Anmeldung bei Firebase) funktionieren. Nichts davon ist von außen erreichbar.
const { app, BrowserWindow, Menu, shell, ipcMain } = require("electron");
const path = require("path"), http = require("http"), fs = require("fs");
const ROOT = path.join(__dirname, "app"), PORT0 = 47821;
const TYPES = { ".html": "text/html; charset=utf-8", ".js": "text/javascript", ".css": "text/css", ".json": "application/json", ".png": "image/png", ".ico": "image/x-icon", ".svg": "image/svg+xml", ".woff2": "font/woff2", ".woff": "font/woff", ".ttf": "font/ttf", ".mp3": "audio/mpeg", ".ogg": "audio/ogg", ".webp": "image/webp", ".jpg": "image/jpeg", ".mp4": "video/mp4", ".webm": "video/webm" };
let ORIGIN = "";
function serve(port) {
  return new Promise((ok, fail) => {
    const srv = http.createServer((req, res) => {
      let u = decodeURIComponent((req.url || "/").split("?")[0]);
      if (u.endsWith("/")) u += "index.html";
      const f = path.normalize(path.join(ROOT, u));
      if (!f.startsWith(ROOT)) { res.writeHead(403); return res.end(); }
      fs.readFile(f, (err, data) => {
        if (err) { res.writeHead(404); return res.end("404"); }
        res.writeHead(200, { "Content-Type": TYPES[path.extname(f).toLowerCase()] || "application/octet-stream", "Cache-Control": "no-cache" });
        res.end(data);
      });
    });
    srv.once("error", fail);
    srv.listen(port, "127.0.0.1", () => ok(port));
  });
}
async function startServer() {
  for (let p = PORT0; p < PORT0 + 10; p++) { try { await serve(p); ORIGIN = "http://localhost:" + p; return; } catch (e) {} }
  throw new Error("Kein freier Port");
}
// Einmalig: alte Spielstände aus der Dateiversion (file://) übernehmen
async function migrate(win) {
  const mark = path.join(app.getPath("userData"), "migrated-v1");
  if (fs.existsSync(mark)) return;
  try {
    const old = new BrowserWindow({ show: false, webPreferences: { backgroundThrottling: false } });
    await old.loadFile(path.join(__dirname, "migrate.html"));
    const data = await old.webContents.executeJavaScript("JSON.stringify(Object.assign({}, localStorage))");
    old.destroy();
    await win.webContents.executeJavaScript(`(() => { const d = ${data}; let n = 0; for (const k in d) if (localStorage.getItem(k) === null) { localStorage.setItem(k, d[k]); n++; } return n; })()`).then(n => { if (n) win.reload(); });
  } catch (e) {}
  try { fs.writeFileSync(mark, "1"); } catch (e) {}
}
const local = url => url.startsWith(ORIGIN + "/");
// Einstellungen neben dem Programm (resources) oder im Entwicklungsordner: steam_appid.txt, discord_appid.txt, build.json
const cfgFile = n => [path.join(process.resourcesPath || "", n), path.join(__dirname, n), path.join(__dirname, "steam", n)].find(f => { try { return fs.existsSync(f); } catch (e) { return false; } });
const cfgText = n => { const f = cfgFile(n); try { return f ? fs.readFileSync(f, "utf8").trim() : ""; } catch (e) { return ""; } };
const BUILD = (() => { try { return JSON.parse(cfgText("build.json") || "{}"); } catch (e) { return {}; } })();   // { demo: true, store: "https://store.steampowered.com/app/…" }
const DEV = !app.isPackaged;

// Steam (optional): nur aktiv, wenn steamworks.js installiert ist und eine steam_appid.txt vorhanden ist
let steam = null, steamLib = null;
try {
  const appId = parseInt(cfgText("steam_appid.txt"), 10);
  if (appId) { steamLib = require("steamworks.js"); steam = steamLib.init(appId); try { steamLib.electronEnableSteamOverlay(); } catch (e) {} }
} catch (e) { steam = null; }
const steamInfo = () => { if (!steam) return null; try { return { name: steam.localplayer.getName(), id: String(steam.localplayer.getSteamId().steamId64) }; } catch (e) { return null; } };
ipcMain.on("steam:ready", e => { e.returnValue = !!steam; });
ipcMain.on("desk:info", e => { e.returnValue = { steam: steamInfo(), demo: !!BUILD.demo, store: BUILD.store || "", platform: process.platform }; });
// Erfolg-Kennung im Spiel → API-Name in Steamworks: ACH_<KENNUNG IN GROSSBUCHSTABEN>
ipcMain.on("steam:ach", (e, id) => { try { if (steam) steam.achievement.activate("ACH_" + String(id).toUpperCase().replace(/[^A-Z0-9]/g, "_")); } catch (er) {} });
ipcMain.on("steam:friends", () => { try { if (steam) steam.overlay.activateDialog(steamLib.overlay.Dialog.Friends); } catch (er) {} });

// Einfache Updates für die Version ohne Steam (Steam aktualisiert selbst): neueste Version auf GitHub nachsehen, Installer laden und starten
const https = require("https"), os = require("os");
const REPO = "heinr2ch/SALVAGE-GRIND";
const vnum = v => String(v || "").replace(/^[^\d]*/, "").split(/[.-]/).slice(0, 3).map(x => parseInt(x, 10) || 0);
const newer = (a, b) => { const x = vnum(a), y = vnum(b); for (let i = 0; i < 3; i++) { if (x[i] !== y[i]) return x[i] > y[i]; } return false; };
function getJSON(url) {
  return new Promise((ok, fail) => https.get(url, { headers: { "User-Agent": "SalvageGrind-Updater", Accept: "application/vnd.github+json" } }, r => {
    if (r.statusCode >= 300 && r.statusCode < 400 && r.headers.location) { r.resume(); return getJSON(r.headers.location).then(ok, fail); }
    let d = ""; r.on("data", c => d += c); r.on("end", () => { try { ok(JSON.parse(d)); } catch (e) { fail(e); } });
  }).on("error", fail));
}
ipcMain.handle("upd:check", async () => {
  if (steam || process.env.SG_SMOKE) return { ok: false, why: "steam" };
  try {
    const list = await getJSON(`https://api.github.com/repos/${REPO}/releases?per_page=10`);
    const rel = (Array.isArray(list) ? list : []).find(r => !r.draft && /^desktop-v/.test(r.tag_name)); if (!rel) return { ok: false };
    const latest = rel.tag_name.replace(/^desktop-v/, ""), cur = app.getVersion();
    const want = process.platform === "win32" ? (BUILD.demo ? /Demo-Setup-.*\.exe$/ : /^Salvage-and-Grind-Setup-.*\.exe$/) : null;
    const asset = want ? (rel.assets || []).find(a => want.test(a.name)) : null;
    return { ok: true, current: cur, latest, newer: newer(latest, cur), url: asset ? asset.browser_download_url : "", size: asset ? asset.size : 0, page: rel.html_url };
  } catch (e) { return { ok: false, why: String(e.message || e) }; }
});
ipcMain.handle("upd:install", async (e, url) => {
  if (!/^https:\/\/github\.com\/heinr2ch\/SALVAGE-GRIND\/releases\/download\//.test(String(url))) return { ok: false, why: "url" };
  const file = path.join(os.tmpdir(), path.basename(url));
  const send = p => { try { e.sender.send("upd:progress", p); } catch (er) {} };
  const dl = (u, n = 0) => new Promise((ok, fail) => https.get(u, { headers: { "User-Agent": "SalvageGrind-Updater" } }, r => {
    if (r.statusCode >= 300 && r.statusCode < 400 && r.headers.location && n < 5) { r.resume(); return dl(r.headers.location, n + 1).then(ok, fail); }
    if (r.statusCode !== 200) { r.resume(); return fail(new Error("HTTP " + r.statusCode)); }
    const total = +r.headers["content-length"] || 0; let got = 0; const out = fs.createWriteStream(file);
    r.on("data", c => { got += c.length; if (total) send(got / total); }); r.pipe(out); out.on("finish", () => out.close(ok)); out.on("error", fail);
  }).on("error", fail));
  try { await dl(url); send(1); const err = await shell.openPath(file); if (err) return { ok: false, why: err }; setTimeout(() => app.quit(), 1500); return { ok: true }; }
  catch (er) { return { ok: false, why: String(er.message || er) }; }
});
ipcMain.on("upd:page", (e, url) => { if (/^https:\/\/github\.com\/heinr2ch\//.test(String(url))) shell.openExternal(url); });

// Discord „Spielt gerade“: Application-ID aus discord_appid.txt
let discord = null;
try { const did = cfgText("discord_appid.txt"); if (/^\d{10,25}$/.test(did)) discord = require("./discord").create(did); } catch (e) { discord = null; }

// Was gerade gespielt wird: Steam-Freundesliste (Rich Presence) und Discord zeigen Welt und Credits
let lastP = "";
ipcMain.on("desk:presence", (e, p) => {
  if (!p || typeof p !== "object") return;
  const clean = { world: String(p.world || "").slice(0, 40), credits: Number.isFinite(+p.credits) ? Math.floor(+p.credits).toLocaleString("de-DE") : null, cur: String(p.cur || "Credits").slice(0, 20), level: +p.level || 0, demo: !!BUILD.demo, store: BUILD.store || "" };
  const key = JSON.stringify(clean); if (key === lastP) return; lastP = key;
  try { if (steam) { const lp = steam.localplayer; lp.setRichPresence("world", clean.world); lp.setRichPresence("credits", clean.credits || "0"); lp.setRichPresence("cur", clean.cur); lp.setRichPresence("steam_display", clean.world ? "#Status" : "#Menu"); } } catch (er) {}
  try { if (discord) discord.set(clean); } catch (er) {}
});

// Musik und Ton dürfen sofort starten
app.commandLine.appendSwitch("autoplay-policy", "no-user-gesture-required");
// Grafikkarte immer nutzen, auch wenn der Treiber auf Electrons Sperrliste steht, und die starke Grafikkarte bevorzugen
app.commandLine.appendSwitch("ignore-gpu-blocklist");
app.commandLine.appendSwitch("enable-gpu-rasterization");
app.commandLine.appendSwitch("enable-zero-copy");
app.commandLine.appendSwitch("force_high_performance_gpu");

// Prüfanzeige (Strg+Umschalt+G): zeigt, ob die Grafikkarte zeichnet, und die Bilder pro Sekunde
const DIAG = (gpu) => `(() => {
  let el = document.getElementById("sgDiag");
  if (el) { el.remove(); cancelAnimationFrame(window.__sgRaf); return; }
  el = document.createElement("div"); el.id = "sgDiag";
  el.style.cssText = "position:fixed;left:12px;bottom:12px;z-index:99999;font:600 13px/1.5 monospace;color:#fff;background:rgba(0,0,0,.82);border:1px solid rgba(255,255,255,.25);border-radius:10px;padding:10px 14px;pointer-events:none;white-space:pre";
  document.body.appendChild(el);
  const g = ${JSON.stringify(gpu)}, ok = v => /enabled/.test(v || "") ? "an" : "AUS (" + v + ")";
  const head = "Grafikkarte zeichnet: " + ok(g.gpu_compositing) + "\\nRasterung per Grafikkarte: " + ok(g.rasterization) + "\\nCanvas: " + ok(g["2d_canvas"]) + "\\nFenster: " + innerWidth + " × " + innerHeight + " (Faktor " + devicePixelRatio + ")";
  let n = 0, t0 = performance.now(), worst = 0, last = t0;
  const tick = now => { n++; worst = Math.max(worst, now - last); last = now;
    if (now - t0 >= 1000) { el.textContent = head + "\\nBilder pro Sekunde: " + Math.round(n * 1000 / (now - t0)) + "  (längste Pause " + Math.round(worst) + " ms)"; n = 0; t0 = now; worst = 0; }
    window.__sgRaf = requestAnimationFrame(tick); };
  el.textContent = head; window.__sgRaf = requestAnimationFrame(tick);
})()`;

function createWindow() {
  const win = new BrowserWindow({
    width: 1600, height: 900, minWidth: 1024, minHeight: 640,
    backgroundColor: "#05060d", title: "Salvage & Grind", show: false,
    icon: path.join(__dirname, "app", "icon.ico"),
    webPreferences: { backgroundThrottling: false, spellcheck: false, preload: path.join(__dirname, "preload.js"), contextIsolation: true, devTools: DEV },
  });
  // Kein Browser-Gefühl: kein Kontextmenü, kein Zoomen per Strg+Mausrad
  win.webContents.on("context-menu", e => e.preventDefault());
  win.webContents.setVisualZoomLevelLimits(1, 1).catch(() => {});
  win.once("ready-to-show", () => { win.maximize(); win.show(); });
  win.loadURL(ORIGIN + "/index.html").then(() => migrate(win));
  // Selbsttest beim Bauen (SG_SMOKE=1): Seite laden, prüfen, ob das Spiel läuft, dann beenden
  if (process.env.SG_SMOKE === "1") win.webContents.once("did-finish-load", () => setTimeout(async () => {
    let r = "fehlt"; try { r = await win.webContents.executeJavaScript(`JSON.stringify({ spiel: typeof state === "object" || !!window.SG_GATE, tor: !!window.SG_GATE, version: typeof GAME_VERSION === "string" ? GAME_VERSION : null, demo: !!window.SG_DEMO, desk: !!window.sgDesk, schrift: document.fonts.check("16px Unbounded") })`); } catch (e) { r = "Fehler " + e.message; }
    console.log("SMOKE " + r); try { if (process.env.SG_SMOKE_OUT) fs.writeFileSync(process.env.SG_SMOKE_OUT, "SMOKE " + r); } catch (e) {} app.exit(/"spiel":true/.test(r) ? 0 : 1);
  }, 6000));

  // F11 = Vollbild an/aus, Strg+Umschalt+G = Prüfanzeige; nur beim Entwickeln: Strg+R = neu laden, Strg+Umschalt+I = Entwicklerwerkzeuge
  win.webContents.on("before-input-event", (e, input) => {
    if (input.type !== "keyDown") return;
    if (input.key === "F11") { win.setFullScreen(!win.isFullScreen()); e.preventDefault(); }
    const k = input.key.toLowerCase();
    if (input.control && (k === "r" || k === "f5" || k === "+" || k === "-" || k === "=" || k === "0")) { if (DEV && k === "r") win.reload(); e.preventDefault(); }
    if (k === "f5" || (input.control && input.shift && (k === "i" || k === "j" || k === "c")) || k === "f12") { if (DEV && k === "i") win.webContents.toggleDevTools(); e.preventDefault(); }
    if (input.control && input.shift && input.key.toLowerCase() === "g") { win.webContents.executeJavaScript(DIAG(app.getGPUFeatureStatus())).catch(() => {}); e.preventDefault(); }
  });
  // Links nach außen (z. B. GitHub) im normalen Browser öffnen, Welten im Spielfenster
  win.webContents.setWindowOpenHandler(({ url }) => {
    if (local(url)) { win.loadURL(url); return { action: "deny" }; }
    shell.openExternal(url); return { action: "deny" };
  });
  win.webContents.on("will-navigate", (e, url) => { if (!local(url)) { e.preventDefault(); shell.openExternal(url); } });
  win.on("page-title-updated", e => e.preventDefault());
}

Menu.setApplicationMenu(null);
app.whenReady().then(startServer).then(createWindow);
app.on("window-all-closed", () => { try { discord && discord.stop(); } catch (e) {} app.quit(); });
