/* 手机视口分步滚动截图（视觉审查用）：模拟真人滚动，每屏一张
   用法：node scripts/mobile-shots.mjs [baseURL] —— 默认 http://localhost:4321 */
import puppeteer from 'puppeteer-core';
import { mkdirSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const base = process.argv[2] || 'http://localhost:4321';
const vw = Number(process.argv[3]) || 412; // 视口宽，桌面对照传 1440
const tag = process.argv[4] || 'm'; // 文件名后缀
const pages = [
  ['home', '/'],
  ['works-3d', '/works/3d/'],
  ['works-vibecoding', '/works/vibecoding/'],
  ['works-graphic', '/works/graphic/'],
  ['about', '/about/'],
  ['contact', '/contact/'],
];

rmSync(`shots/${tag}`, { recursive: true, force: true });
mkdirSync(`shots/${tag}`, { recursive: true });
const browser = await puppeteer.launch({
  executablePath: 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  headless: 'new',
  args: [
    '--no-sandbox',
    '--hide-scrollbars',
    `--user-data-dir=${join(tmpdir(), 'edge-shots-profile')}`,
    '--edge-skip-compat-layer-relaunch',
    '--disable-features=msEdgeMode',
  ],
});
const page = await browser.newPage();
await page.setViewport({ width: vw, height: vw > 700 ? 900 : Math.round((vw * 15) / 8), deviceScaleFactor: 1.5 }); // 手机=8:15（用户 2026-09-09）；桌面=1440×900

for (const [name, path] of pages) {
  try {
    await page.goto(base + path, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await new Promise((r) => setTimeout(r, 2000));
    // 首屏先截一张（手机提示浮层可见），再关掉浮层继续分步滚动
    await page.screenshot({ path: `shots/${tag}/${name}-s00.png` });
    await page.evaluate(() => document.querySelector('#m-notice .mn-ok')?.click());
    await new Promise((r) => setTimeout(r, 500));
    // 分步滚动：每步 85% 视口高，到底后回顶
    let step = 1;
    await page.evaluate(() => window.scrollTo(0, 0));
    while (true) {
      await page.screenshot({ path: `shots/${tag}/${name}-s${String(step).padStart(2, '0')}.png` });
      const atEnd = await page.evaluate(() => {
        const next = Math.round(scrollY + innerHeight * 0.85);
        if (next >= document.documentElement.scrollHeight - innerHeight + 4) {
          scrollTo(0, document.documentElement.scrollHeight);
          return true;
        }
        scrollTo(0, next);
        return false;
      });
      await new Promise((r) => setTimeout(r, 1100)); // 等 scrub/入场动画跟上
      step++;
      if (step > 14 || atEnd) break;
    }
    console.log('shot:', name, `${step} 屏`);
  } catch (e) {
    console.log('FAIL:', name, e.message.slice(0, 80));
  }
}
await browser.close();
console.log('all done');
