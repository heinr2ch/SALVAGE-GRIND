// Salvage & Grind – Desktop-Hülle (Electron). Lädt die vier Welten als lokale Dateien.
const { app, BrowserWindow, Menu, shell } = require("electron");
const path = require("path");

// Musik und Ton dürfen sofort starten
app.commandLine.appendSwitch("autoplay-policy", "no-user-gesture-required");

function createWindow() {
  const win = new BrowserWindow({
    width: 1600, height: 900, minWidth: 1024, minHeight: 640,
    backgroundColor: "#05060d", title: "Salvage & Grind", show: false,
    icon: path.join(__dirname, "app", "icon.ico"),
    webPreferences: { backgroundThrottling: false, spellcheck: false },
  });
  win.once("ready-to-show", () => { win.maximize(); win.show(); });
  win.loadFile(path.join(__dirname, "app", "index.html"));

  // F11 = Vollbild an/aus, Strg+R = neu laden, Strg+Umschalt+I = Entwicklerwerkzeuge (nur zum Testen)
  win.webContents.on("before-input-event", (e, input) => {
    if (input.type !== "keyDown") return;
    if (input.key === "F11") { win.setFullScreen(!win.isFullScreen()); e.preventDefault(); }
    if (input.control && input.key.toLowerCase() === "r") { win.reload(); e.preventDefault(); }
    if (input.control && input.shift && input.key.toLowerCase() === "i") win.webContents.toggleDevTools();
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
