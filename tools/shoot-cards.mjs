import { chromium } from 'playwright';
import fs from 'fs';
const spec = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const exe = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
const b = await chromium.launch(fs.existsSync(exe) ? { executablePath: exe } : {});
const c = await b.newContext({ viewport: { width: 1200, height: 630 },
                               deviceScaleFactor: 1 });
let n = 0;
for (const s of spec) {
  const p = await c.newPage();
  await p.setContent(s.html, { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  await p.screenshot({ path: s.out });
  await p.close();
  n++;
}
await b.close();
console.log(`${n} share cards rendered`);
