// 简历网站冒烟测试。
// 三层防线：
//   1. 源码层——关键页面存在、作品内容集合字段合法（与 src/content.config.ts 的 zod schema 对齐）
//   2. 产物层——dist 构建产物存在、页面内链无死链（需先 npm run build）
//   3. 兼容层——产物 CSS 无区间写法媒体查询（与 scripts/check-mq.mjs 同源逻辑，防止有人绕过 build 脚本）
import { readdirSync, readFileSync, existsSync } from 'node:fs';
import { join, dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { describe, it, expect } from 'vitest';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const pagesDir = join(root, 'src', 'pages');
const contentDir = join(root, 'src', 'content', 'works');
const distDir = join(root, 'dist');

const CATEGORY_KEYS = ['3d', 'vibecoding', 'graphic'];
const KEY_PAGES = [
	'index.astro',
	'about.astro',
	'contact.astro',
	'404.astro',
	'works/[category]/index.astro',
	'en/index.astro',
	'en/about.astro',
	'en/contact.astro',
];

describe('源码层：关键页面', () => {
	for (const rel of KEY_PAGES) {
		it(`页面存在且非空：${rel}`, () => {
			const p = join(pagesDir, ...rel.split('/'));
			expect(existsSync(p), `缺页面 src/pages/${rel}`).toBe(true);
			const src = readFileSync(p, 'utf8');
			expect(src.trim().length).toBeGreaterThan(0);
		});
	}
});

describe('源码层：作品内容集合（work collection）', () => {
	const walk = (dir) =>
		readdirSync(dir, { withFileTypes: true }).flatMap((e) =>
			e.isDirectory() ? walk(join(dir, e.name)) : e.name.endsWith('.md') ? [join(dir, e.name)] : [],
		);

	const files = existsSync(contentDir) ? walk(contentDir) : [];

	it('作品目录下存在 .md 内容文件', () => {
		expect(files.length).toBeGreaterThan(0);
	});

	for (const file of files) {
		const rel = file.slice(root.length + 1);
		it(`frontmatter 字段合法：${rel}`, () => {
			const fm = readFileSync(file, 'utf8').split('---')[1] ?? '';
			const pick = (key) => fm.match(new RegExp(`^${key}:\\s*(.+)$`, 'm'))?.[1]?.trim();

			expect(pick('title'), '缺 title').toBeTruthy();
			expect(CATEGORY_KEYS).toContain(pick('category'));
			expect(['S', 'A', 'B']).toContain(pick('level') ?? 'A');
			expect(pick('date'), '缺 date').toBeTruthy();
			expect(pick('cover'), '缺 cover').toBeTruthy();
			expect(pick('attribution'), '缺诚实标注 attribution').toBeTruthy();
			// 注：attribution_source 来源标注不做强制检查（2026-09-10 用户拍板）：
			// 跟练类作品已在视频片尾标注来源，性质角标（attribution）本身即满足诚实展示要求。
		});
	}
});

describe('源码层：壳内核图片拦截防护', () => {
	it('作品卡封面图 pointer-events:none（百度等壳内核点图弹自家预览，抢在卡片 click 之前）', () => {
		const src = readFileSync(join(root, 'src', 'components', 'WorkCard.astro'), 'utf8');
		expect(src).toMatch(/\.ph\s+img\s*{[^}]*pointer-events:\s*none/s);
	});
});

describe('源码层：作品条灯箱（图片放大查看 + 左右切换）', () => {
	const src = () => readFileSync(join(root, 'src', 'components', 'CategoryView.astro'), 'utf8');

	it('灯箱 DOM 存在（img-lightbox + 大图 + 关闭/左右按钮）', () => {
		expect(src()).toMatch(/id="img-lightbox"/);
		expect(src()).toMatch(/class="lb-img"/);
		expect(src()).toMatch(/lb-close/);
		expect(src()).toMatch(/lb-prev/);
		expect(src()).toMatch(/lb-next/);
	});

	it('作品条内图片 pointer-events:none（灯箱委托容器点击，兼防壳内核拦截）', () => {
		expect(src()).toMatch(/\.wp-media img,\s*\n\s*\.wp-gallery img,\s*\n\s*\.wp-process img\s*{[^}]*pointer-events:\s*none/s);
	});

	it('灯箱逻辑完整：从点击图开始、循环切换、背景关闭、ESC 分流不误关作品条', () => {
		const s = src();
		expect(s).toMatch(/lbOpen\(list,\s*Math\.max\(0,\s*list\.indexOf\(img\)\)\)/);
		expect(s).toMatch(/lbIdx = \(lbIdx \+ d \+ lbList\.length\) % lbList\.length/);
		expect(s).toMatch(/e\.target === lightbox\) lbClose/);
		// ESC 分流：单一监听器——灯箱可见时 ESC 归灯箱并 return（防同帧连执误关作品条），否则才 close()
		expect(s).toMatch(
			/if \(!lightbox\.hasAttribute\('hidden'\)\) \{[^}]*lbClose\(\);[^}]*return;[\s\S]*?if \(e\.key === 'Escape'\) close\(\);/,
		);
	});
});

const distReady = existsSync(join(distDir, 'index.html'));

describe.skipIf(!distReady)('产物层：dist 死链检查（先 npm run build）', () => {
	const htmlFiles = [];
	const walk = (dir) =>
		readdirSync(dir, { withFileTypes: true }).flatMap((e) => {
			const p = join(dir, e.name);
			return e.isDirectory() ? walk(p) : p.endsWith('.html') ? (htmlFiles.push(p), []) : [];
		});
	walk(distDir);

	it('构建产物包含关键页面', () => {
		expect(existsSync(join(distDir, 'index.html'))).toBe(true);
		expect(existsSync(join(distDir, 'about', 'index.html'))).toBe(true);
		expect(existsSync(join(distDir, 'en', 'index.html'))).toBe(true);
	});

	it('站内链接无死链（首页/关于/联系/作品索引 + 英文版）', () => {
		const broken = [];
		for (const file of htmlFiles) {
			if (!/\\(index|about|contact|404)(\\index\.html)?$/.test(file) && !/en\\/.test(file)) continue;
			const html = readFileSync(file, 'utf8');
			const hrefs = [...html.matchAll(/href="(\/[^"#][^"]*)"/g)].map((m) => m[1]);
			for (const href of new Set(hrefs)) {
				const path = href.split('?')[0].split('#')[0];
				const target = join(distDir, decodeURIComponent(path), 'index.html');
				const asFile = join(distDir, decodeURIComponent(path));
				if (!existsSync(target) && !existsSync(asFile)) broken.push(`${file} -> ${href}`);
			}
		}
		expect(broken, `死链：\n${broken.join('\n')}`).toEqual([]);
	});
});

describe.skipIf(!distReady)('兼容层：老内核媒体查询', () => {
	it('dist CSS 无区间写法（width<= / width>=）', () => {
		const bad = [];
		const walk = (dir) =>
			readdirSync(dir, { withFileTypes: true }).flatMap((e) => {
				const p = join(dir, e.name);
				if (e.isDirectory()) return walk(p);
				if (p.endsWith('.css')) {
					const hits = readFileSync(p, 'utf8').match(/width<=|width>=|width</g);
					if (hits) bad.push(`${p}：${hits.length} 处`);
				}
				return [];
			});
		walk(distDir);
		expect(bad, bad.join('\n')).toEqual([]);
	});
});
