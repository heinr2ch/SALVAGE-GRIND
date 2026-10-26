// Salvage & Grind – Desktop-Hülle (Electron). Lädt die vier Welten als lokale Dateien.
const { app, BrowserWindow, Menu, shell } = require("electron");
const path = require("path");

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
  win.loadFile(path.join(__dirname, "app", "index.html"));

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
    if (url.startsWith("file:")) { win.loadURL(url); return { action: "deny" }; }
    shell.openExternal(url); return { action: "deny" };
  });
  win.webContents.on("will-navigate", (e, url) => { if (!url.startsWith("file:")) { e.preventDefault(); shell.openExternal(url); } });
  win.on("page-title-updated", e => e.preventDefault());
}

Menu.setApplicationMenu(null);
app.whenReady().then(createWindow);
app.on("window-all-closed", () => app.quit());
