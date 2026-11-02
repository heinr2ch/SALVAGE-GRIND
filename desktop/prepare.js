// Kopiert die fünf Welten nach desktop/app, baut die Schriften lokal ein und stellt die Welt-Links auf lokale Dateien um.
const fs = require("fs"), path = require("path");
const ROOT = path.join(__dirname, ".."), APP = path.join(__dirname, "app");
// Demo (SG_DEMO=1): nur Sternenwrack, nur das erste Fahrzeug. Steam-/Discord-IDs kommen aus Umgebungsvariablen (GitHub-Variablen).
const DEMO = process.env.SG_DEMO === "1";
const WORLDS = DEMO ? [""] : ["", "treibgut/", "eisenfront/", "neustadt/", "neonkueste/"];
const STEAM = path.join(__dirname, "steam");
const appId = (DEMO ? process.env.SG_STEAM_DEMO_APPID : process.env.SG_STEAM_APPID) || "";
const mainId = process.env.SG_STEAM_APPID || "";
for (const f of ["steam_appid.txt", "discord_appid.txt", "build.json"]) fs.rmSync(path.join(STEAM, f), { force: true });
if (/^\d+$/.test(appId)) fs.writeFileSync(path.join(STEAM, "steam_appid.txt"), appId);
if (/^\d{10,25}$/.test(process.env.SG_DISCORD_APPID || "")) fs.writeFileSync(path.join(STEAM, "discord_appid.txt"), process.env.SG_DISCORD_APPID);
const store = /^\d+$/.test(mainId) && mainId !== "480" ? "https://store.steampowered.com/app/" + mainId + "/" : "";
fs.writeFileSync(path.join(STEAM, "build.json"), JSON.stringify({ demo: DEMO, store }));
console.log(DEMO ? "DEMO-Ausgabe" : "Vollversion", "· Steam", appId || "aus", "· Discord", process.env.SG_DISCORD_APPID ? "an" : "aus");
const SITE = /https:\/\/heinr2ch\.github\.io\/(?:SALVAGE-GRIND|salvage-grind|STERNENWRACK|salvage-and-grind)\/((?:treibgut|eisenfront|neustadt|neonkueste)\/)?/g;

fs.rmSync(APP, { recursive: true, force: true });
fs.mkdirSync(path.join(APP, "fonts"), { recursive: true });

// Schriften und Firebase liegen schon lokal im Repo (fonts/, vendor/), siehe tools/vendor/fetch.js
fs.rmSync(path.join(APP, "fonts"), { recursive: true, force: true });
fs.cpSync(path.join(ROOT, "fonts"), path.join(APP, "fonts"), { recursive: true });
fs.cpSync(path.join(ROOT, "vendor"), path.join(APP, "vendor"), { recursive: true });
fs.cpSync(path.join(ROOT, "media"), path.join(APP, "media"), { recursive: true });   // Intro-Video und Entwicklerlogo
for (const f of ["THIRD_PARTY_NOTICES.md"]) if (fs.existsSync(path.join(ROOT, f))) fs.copyFileSync(path.join(ROOT, f), path.join(APP, f));

// Closed Beta (tools/seal.py): Welten liegen verschlüsselt als spiel.bin neben einer Startseite mit Key-Abfrage; die Demo kommt offen aus demo.html
const SEALED = fs.existsSync(path.join(ROOT, "spiel.bin"));
for (const w of WORLDS) {
  const up = w ? "../" : "./";
  if (SEALED && !DEMO) {
    fs.mkdirSync(path.join(APP, w), { recursive: true });
    for (const f of ["index.html", "spiel.bin"]) fs.copyFileSync(path.join(ROOT, w, f), path.join(APP, w, f));
    console.log("Welt", w || "sternenwrack/", "verschlüsselt", Math.round(fs.statSync(path.join(ROOT, w, "spiel.bin")).size / 1024) + " KB");
    continue;
  }
  let s = fs.readFileSync(path.join(ROOT, w, SEALED && DEMO && !w ? "demo.html" : "index.html"), "utf8");
  if (SEALED && DEMO) s = s.replace('<script>window.SG_DEMO = 1; window.SG_STORE = "";</script>', "");
  const before = s.length;
  if (/fonts\.googleapis\.com|gstatic\.com/.test(s)) throw new Error("Noch Google-Abruf in " + (w || "sternenwrack"));
  s = s.replace(SITE, (m, sub) => up + (sub || "") + "index.html");
  s = s.replace('/github\\.io$/.test(location.hostname) ? "_self" : "_blank"', '"_self"');
  if (DEMO) s = s.replace("<head>", `<head><script>window.SG_DEMO = 1; window.SG_STORE = ${JSON.stringify(store)};</script>`);
  fs.mkdirSync(path.join(APP, w), { recursive: true });
  fs.writeFileSync(path.join(APP, w, "index.html"), s);
  console.log("Welt", w || "sternenwrack/", Math.round(before / 1024) + " KB");
}
fs.copyFileSync(path.join(__dirname, "build", "icon.ico"), path.join(APP, "icon.ico"));
// Version des Installers = Version von Sternenwrack
const ver = (fs.readFileSync(path.join(ROOT, "index.html"), "utf8").match(/GAME_VERSION = "([^"]+)"/) || [])[1];
if (ver) { const pj = path.join(__dirname, "package.json"), j = JSON.parse(fs.readFileSync(pj, "utf8")); if (j.version !== ver) { j.version = ver; fs.writeFileSync(pj, JSON.stringify(j, null, 2) + "\n"); } console.log("Version", ver); }
console.log("Schriften:", fs.readdirSync(path.join(APP, "fonts", "files")).length, "Dateien");
// Einstellungen für den Installer-Bau (builder.json): Vollversion oder Demo mit eigenem Namen, eigener Kennung und eigenem Speicherordner
const pkg = JSON.parse(fs.readFileSync(path.join(__dirname, "package.json"), "utf8")), cfg = JSON.parse(JSON.stringify(pkg.build));
if (DEMO) {
  cfg.appId += ".demo"; cfg.productName = pkg.productName + " Demo";
  cfg.extraMetadata = { name: pkg.name + "-demo", productName: pkg.productName + " Demo" };
  for (const k of ["win", "mac", "linux"]) if (cfg[k] && cfg[k].artifactName) cfg[k].artifactName = cfg[k].artifactName.replace("Salvage-and-Grind", "Salvage-and-Grind-Demo");
  if (cfg.linux) { cfg.linux.executableName += "-demo"; cfg.linux.desktop = Object.assign({}, cfg.linux.desktop, { Name: pkg.productName + " Demo" }); }
  if (cfg.nsis) cfg.nsis.shortcutName += " Demo";
}
fs.writeFileSync(path.join(__dirname, "builder.json"), JSON.stringify(cfg, null, 2));
