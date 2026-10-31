// Salvage & Grind – Desktop-Hülle (Electron). Liefert die vier Welten über einen kleinen Server auf diesem PC aus (http://localhost),
// damit die Online-Funktionen (Anmeldung bei Firebase) funktionieren. Nichts davon ist von außen erreichbar.
const { app, BrowserWindow, Menu, shell } = require("electron");
const path = require("path"), http = require("http"), fs = require("fs");
const ROOT = path.join(__dirname, "app"), PORT0 = 47821;
const TYPES = { ".html": "text/html; charset=utf-8", ".js": "text/javascript", ".css": "text/css", ".json": "application/json", ".png": "image/png", ".ico": "image/x-icon", ".svg": "image/svg+xml", ".woff2": "font/woff2", ".woff": "font/woff", ".ttf": "font/ttf", ".mp3": "audio/mpeg", ".ogg": "audio/ogg", ".webp": "image/webp", ".jpg": "image/jpeg" };
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
    webPreferences: { backgroundThrottling: false, spellcheck: false },
  });
  win.once("ready-to-show", () => { win.maximize(); win.show(); });
  win.loadURL(ORIGIN + "/index.html").then(() => migrate(win));

  // F11 = Vollbild an/aus, Strg+R = neu laden, Strg+Umschalt+G = Prüfanzeige, Strg+Umschalt+I = Entwicklerwerkzeuge
  win.webContents.on("before-input-event", (e, input) => {
    if (input.type !== "keyDown") return;
    if (input.key === "F11") { win.setFullScreen(!win.isFullScreen()); e.preventDefault(); }
    if (input.control && input.key.toLowerCase() === "r") { win.reload(); e.preventDefault(); }
    if (input.control && input.shift && input.key.toLowerCase() === "i") win.webContents.toggleDevTools();
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
app.on("window-all-closed", () => app.quit());
