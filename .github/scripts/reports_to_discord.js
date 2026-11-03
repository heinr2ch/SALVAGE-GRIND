// Holt neue Feedback-/Fehlermeldungen aus Firebase und schickt sie in einen Discord-Kanal. Danach werden sie in Firebase gelöscht.
// Fehler gehen nach #🐞┃report (Secret DISCORD_WEBHOOK_REPORT), Ideen und Lob nach #💡┃feedback (DISCORD_WEBHOOK_FEEDBACK).
// Dazu FIREBASE_DB_SECRET. Fehlt etwas, passiert nichts.
// Rang KIneArbyte auf FreiSpieleDC: wird bei jeder Meldung erwähnt, damit Heinrich und Snemelc benachrichtigt werden
const ROLE = "1566422081443332146";
const DB = "https://salvage-grind-default-rtdb.europe-west1.firebasedatabase.app";
const { DISCORD_WEBHOOK_REPORT: H_REP, DISCORD_WEBHOOK_FEEDBACK: H_FB, FIREBASE_DB_SECRET: SEC } = process.env;
// WATCH_MIN > 0: bleibt so viele Minuten wach und schaut alle 5 Sekunden nach neuen Meldungen (fast sofort in Discord)
const WATCH = (+process.env.WATCH_MIN || 0) * 60000, T0 = Date.now(), sleep = ms => new Promise(r => setTimeout(r, ms));
async function once() {
  const r = await fetch(`${DB}/reports.json?auth=${encodeURIComponent(SEC)}`); if (!r.ok) throw new Error("Firebase " + r.status);
  const all = await r.json() || {}; const ids = Object.keys(all).sort((a, b) => (all[a].t || 0) - (all[b].t || 0));
  if (ids.length) console.log(new Date().toISOString(), ids.length, "neue Meldungen");
  const KIND = { bug: ["🐞 Fehler", 0xff5a6a], idea: ["💡 Idee", 0xffc94a], love: ["❤️ Lob", 0x8fe9a8], player: ["🚩 Gemeldeter Spieler/Inhalt (DSA)", 0xff2d55] };
  for (const id of ids.slice(0, 25)) {
    const x = all[id] || {}, [title, color] = KIND[x.k] || KIND.bug;
    const body = { username: "Salvage & Grind", avatar_url: "https://raw.githubusercontent.com/heinr2ch/SALVAGE-GRIND/main/desktop/build/icon.png", content: `<@&${ROLE}>`, allowed_mentions: { roles: [ROLE] }, embeds: [{ title: `${title} · ${x.w || "?"} · ${x.v || "?"}`, description: String(x.m || "").slice(0, 3800), color,
      fields: [{ name: "Spieler", value: String(x.n || "unbekannt").slice(0, 60), inline: true }, { name: "Gerät", value: String(x.d || "-").slice(0, 900) }],
      timestamp: x.t ? new Date(x.t).toISOString() : undefined }] };
    const HOOK = (x.k === "idea" || x.k === "love" ? H_FB : H_REP) || H_REP || H_FB;
    const p = await fetch(HOOK, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
    if (p.status === 429) { await new Promise(res => setTimeout(res, 3000)); continue; }
    if (!p.ok) { console.log("Discord", p.status, await p.text()); continue; }
    await fetch(`${DB}/reportsLog/${id}.json?auth=${encodeURIComponent(SEC)}`, { method: "PUT", body: JSON.stringify(x) });   // Verlauf fürs Dashboard
    await fetch(`${DB}/reports/${id}.json?auth=${encodeURIComponent(SEC)}`, { method: "DELETE" });
    await new Promise(res => setTimeout(res, 700));
  }
}
(async () => {
  if (!(H_REP || H_FB) || !SEC) { console.log("Secrets fehlen, nichts zu tun."); return; }
  do { try { await once(); } catch (e) { console.error(e.message); } if (WATCH) await sleep(5000); } while (WATCH && Date.now() - T0 < WATCH);
})().catch(e => { console.error(e); process.exit(1); });
