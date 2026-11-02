// Brücke zur Seite: Steam-Erfolge, Steam-Name, „Spielt gerade“ für Steam und Discord. Sonst nichts.
const { contextBridge, ipcRenderer } = require("electron");
const on = ipcRenderer.sendSync("steam:ready");
if (on) contextBridge.exposeInMainWorld("sgSteam", { activate: id => ipcRenderer.send("steam:ach", String(id)), friends: () => ipcRenderer.send("steam:friends") });
const info = ipcRenderer.sendSync("desk:info") || {};
contextBridge.exposeInMainWorld("sgDesk", {
  info: () => info,
  presence: p => ipcRenderer.send("desk:presence", p),
  updCheck: () => ipcRenderer.invoke("upd:check"),
  updInstall: url => ipcRenderer.invoke("upd:install", String(url)),
  updPage: url => ipcRenderer.send("upd:page", String(url)),
  onUpdProgress: fn => ipcRenderer.on("upd:progress", (e, p) => fn(+p || 0)),
});
