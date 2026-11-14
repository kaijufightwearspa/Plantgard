// Prueba de humo de la calculadora en un navegador real (Playwright + Chromium).
// Uso:  node tests/smoke.mjs                 → sirve web/ en local
//       node tests/smoke.mjs https://...     → prueba la versión publicada
import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const { chromium } = require("playwright");
const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), "../web");
const fallos = [];
const check = (ok, msg) => { console.log(`${ok ? "ok  " : "FALLA"} ${msg}`); if (!ok) fallos.push(msg); };

let base = process.argv[2], server;
if (!base) {
  server = http.createServer((req, res) => {
    const u = req.url.split("?")[0];
    const f = path.join(root, u === "/" ? "index.html" : u);
    if (!f.startsWith(root) || !fs.existsSync(f)) { res.statusCode = 404; return res.end(); }
    res.setHeader("Content-Type", f.endsWith(".js") ? "text/javascript" : "text/html; charset=utf-8");
    res.end(fs.readFileSync(f));
  }).listen(0);
  base = `http://localhost:${server.address().port}`;
}

const browser = await chromium.launch();
try {
  for (const [ancho, tema] of [[1200, "light"], [390, "dark"]]) {
    const page = await browser.newPage({ viewport: { width: ancho, height: 900 }, colorScheme: tema });
    const errores = [];
    page.on("pageerror", (e) => errores.push(e.message));
    page.on("console", (m) => m.type() === "error" && errores.push(m.text()));
    await page.goto(base + "/");
    await page.waitForSelector("#tbody tr");
    const tabla = await page.locator("#tbody").innerText();
    check(tabla.includes("10.199") && tabla.includes("84.055") && tabla.includes("272.561"), `${ancho}px: VAN de control`);
    check((await page.locator("#k-umbral").innerText()).includes("6,6"), `${ancho}px: umbral 6,6 %`);
    check(!(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth)), `${ancho}px: sin desborde horizontal`);
    check((await page.locator("#flujos").innerText()).includes("56.280"), `${ancho}px: flujo año a año (escenario base)`);
    await page.fill("#perdida", "100");
    check(await page.locator("#errors").isVisible(), `${ancho}px: avisa pérdida imposible`);
    await page.click("#reset");
    check(!(await page.locator("#errors").isVisible()), `${ancho}px: "Volver al ejemplo" restablece`);
    check(errores.length === 0, `${ancho}px: sin errores de consola ${errores.join(" | ")}`);
    await page.close();
  }
  const p = await browser.newPage();
  await p.goto(base + "/?embed=1");
  check(!(await p.locator(".page-head").isVisible()), "modo insertado oculta el título");
  const r = await p.request.get(base + "/docs/PlantGuard_Pro_Base_Conocimiento_v2.0.md");
  check(r.status() === 404, "docs/ no se publica");
} finally {
  await browser.close();
  server?.close();
}
if (fallos.length) { console.error(`\n${fallos.length} prueba(s) fallaron`); process.exit(1); }
console.log("\nTodo OK");
