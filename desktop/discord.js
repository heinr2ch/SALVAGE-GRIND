// Discord „Spielt gerade“ (Rich Presence) ohne Zusatzpaket: spricht direkt mit der laufenden Discord-App über deren lokale Schnittstelle.
// Läuft nur, wenn eine Discord-Application-ID hinterlegt ist (discord_appid.txt). Ohne Discord passiert einfach nichts.
const net = require("net"), path = require("path"), os = require("os");
function pipePaths() {
  if (process.platform === "win32") return [...Array(10)].map((_, i) => `\\\\?\\pipe\\discord-ipc-${i}`);
  const base = process.env.XDG_RUNTIME_DIR || process.env.TMPDIR || process.env.TMP || process.env.TEMP || "/tmp";
  const dirs = [base, path.join(base, "app/com.discordapp.Discord"), path.join(base, "snap.discord"), path.join(base, ".flatpak/com.discordapp.Discord/xdg-run")];
  const out = []; for (const d of dirs) for (let i = 0; i < 10; i++) out.push(path.join(d, `discord-ipc-${i}`)); return out;
}
const frame = (op, obj) => { const j = Buffer.from(JSON.stringify(obj), "utf8"), h = Buffer.alloc(8); h.writeUInt32LE(op, 0); h.writeUInt32LE(j.length, 4); return Buffer.concat([h, j]); };
function create(clientId) {
  let sock = null, ready = false, last = null, timer = 0, start = Date.now();
  const tryConnect = (list, i = 0) => {
    if (i >= list.length) { schedule(); return; }
    const s = net.createConnection(list[i]);
    s.once("error", () => { s.destroy(); tryConnect(list, i + 1); });
    s.once("connect", () => {
      sock = s; s.write(frame(0, { v: 1, client_id: clientId }));
      s.on("data", () => { if (!ready) { ready = true; if (last) send(last); } });
      s.on("close", () => { sock = null; ready = false; schedule(); });
      s.on("error", () => {});
    });
  };
  const schedule = () => { clearTimeout(timer); timer = setTimeout(() => tryConnect(pipePaths()), 30000); };
  const send = a => { if (!sock || !ready) return; try { sock.write(frame(1, { cmd: "SET_ACTIVITY", args: { pid: process.pid, activity: a }, nonce: String(Date.now()) + Math.random() })); } catch (e) {} };
  tryConnect(pipePaths());
  return {
    set(p) {
      const a = { details: p.world ? `Welt: ${p.world}` : "Im Hauptmenü", state: p.credits != null ? `${p.credits} ${p.cur || "Credits"}${p.level ? ` · Rang ${p.level}` : ""}` : undefined,
        timestamps: { start }, assets: { large_image: "logo", large_text: "Salvage & Grind" + (p.demo ? " (Demo)" : "") } };
      if (p.store) a.buttons = [{ label: "Auf Steam ansehen", url: p.store }];
      last = a; send(a);
    },
    stop() { clearTimeout(timer); try { sock && sock.destroy(); } catch (e) {} },
  };
}
module.exports = { create };
