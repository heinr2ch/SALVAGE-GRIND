// Kopiert die vier Welten nach desktop/app, baut die Schriften lokal ein und stellt die Welt-Links auf lokale Dateien um.
const fs = require("fs"), path = require("path");
const ROOT = path.join(__dirname, ".."), APP = path.join(__dirname, "app");
const WORLDS = ["", "treibgut/", "eisenfront/", "neustadt/"];
const SITE = /https:\/\/heinr2ch\.github\.io\/(?:SALVAGE-GRIND|salvage-grind|STERNENWRACK|salvage-and-grind)\/((?:treibgut|eisenfront|neustadt)\/)?/g;

fs.rmSync(APP, { recursive: true, force: true });
fs.mkdirSync(path.join(APP, "fonts"), { recursive: true });

// Schriften: nur die Schnitte, die das Spiel nutzt (alle Sprachen über unicode-range)
const FONTS = [["unbounded", [500, 700, 800]], ["manrope", [400, 600, 700]], ["jetbrains-mono", [500, 700]]];
let css = "";
for (const [fam, weights] of FONTS) {
  const pkg = path.join(__dirname, "node_modules", "@fontsource", fam);
  for (const w of weights) {
    const src = fs.readFileSync(path.join(pkg, w + ".css"), "utf8");
    css += src.replace(/url\(\.\/files\/([^)]+)\)/g, (m, f) => {
      if (f.endsWith(".woff2")) fs.copyFileSync(path.join(pkg, "files", f), path.join(APP, "fonts", f));
      return `url(./${f})`;
    }).replace(/,\s*url\(\.\/[^)]+\.woff\)\s*format\('woff'\)/g, "") + "\n";
  }
}
// Familiennamen wie bei Google Fonts
css = css.replace(/font-family: '([^']+)'/g, (m, f) => `font-family: '${f === "JetBrains Mono" ? "JetBrains Mono" : f}'`);
fs.writeFileSync(path.join(APP, "fonts", "fonts.css"), css);

for (const w of WORLDS) {
  const up = w ? "../" : "./";
  let s = fs.readFileSync(path.join(ROOT, w, "index.html"), "utf8");
  const before = s.length;
  s = s.replace(/<link rel="preconnect" href="https:\/\/fonts\.googleapis\.com">\s*/g, "")
       .replace(/<link rel="preconnect" href="https:\/\/fonts\.gstatic\.com"[^>]*>\s*/g, "")
       .replace(/<link rel="stylesheet" href="https:\/\/fonts\.googleapis\.com[^"]*">/g, `<link rel="stylesheet" href="${up}fonts/fonts.css">`);
  if (!s.includes("fonts/fonts.css")) throw new Error("Schrift-Link nicht gefunden: " + w);
  s = s.replace(SITE, (m, sub) => up + (sub || "") + "index.html");
  s = s.replace('/github\\.io$/.test(location.hostname) ? "_self" : "_blank"', '"_self"');
  fs.mkdirSync(path.join(APP, w), { recursive: true });
  fs.writeFileSync(path.join(APP, w, "index.html"), s);
  console.log("Welt", w || "sternenwrack/", Math.round(before / 1024) + " KB");
}
fs.copyFileSync(path.join(__dirname, "build", "icon.ico"), path.join(APP, "icon.ico"));
// Version des Installers = Version von Sternenwrack
const ver = (fs.readFileSync(path.join(ROOT, "index.html"), "utf8").match(/GAME_VERSION = "([^"]+)"/) || [])[1];
if (ver) { const pj = path.join(__dirname, "package.json"), j = JSON.parse(fs.readFileSync(pj, "utf8")); if (j.version !== ver) { j.version = ver; fs.writeFileSync(pj, JSON.stringify(j, null, 2) + "\n"); } console.log("Version", ver); }
console.log("Schriften:", fs.readdirSync(path.join(APP, "fonts")).length - 1, "Dateien");
