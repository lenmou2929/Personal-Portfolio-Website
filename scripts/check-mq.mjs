// 构建后断言：产物 CSS 不得含媒体查询区间写法（width<= / width>=）。
// 区间写法需 Chromium 104+，百度 T7 等老壳内核读到即整块丢弃，手机端样式全部失效。
// 防回归：将来升级 Astro/Vite/Tailwind 若改写行为回潮，构建在此失败而不是悄悄上线。
import { readdirSync, readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';

const bad = [];

function walk(dir) {
	for (const name of readdirSync(dir)) {
		const p = join(dir, name);
		if (statSync(p).isDirectory()) {
			walk(p);
		} else if (p.endsWith('.css')) {
			const hits = readFileSync(p, 'utf8').match(/width<=|width>=|width</g);
			if (hits) bad.push(`${p}：${hits.length} 处`);
		}
	}
}

walk('dist');

if (bad.length) {
	console.error('✗ 检测到区间写法媒体查询（老内核整块丢弃，手机样式会失效）：');
	console.error(bad.join('\n'));
	process.exit(1);
}
console.log('✓ CSS 媒体查询语法检查通过：无区间写法（width<= / width>=）');
