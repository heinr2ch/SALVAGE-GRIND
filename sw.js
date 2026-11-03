// Salvage & Grind – Service Worker für die Browser-App. Speichert nichts zwischen, damit immer die aktuelle Version läuft.
self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", e => e.waitUntil(self.clients.claim()));
self.addEventListener("fetch", e => { if (e.request.mode === "navigate") e.respondWith(fetch(e.request).catch(() => new Response("<meta charset=utf-8><body style='background:#0d1022;color:#fff;font-family:system-ui;padding:40px'>Keine Internetverbindung. Salvage &amp; Grind braucht Internet – bitte später nochmal öffnen.", { headers: { "Content-Type": "text/html; charset=utf-8" } }))); });
