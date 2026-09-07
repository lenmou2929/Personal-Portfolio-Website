/** 英文文案单一来源（2026-09-08 第 20 次会话，内页 EN 上线）。
 * 结构：UI_EN = 内页界面串；WORK_EN = 作品条目标题/摘要（键=条目 id）；
 * ATTR_EN = 诚实标注角标；CAPTION_EN = 图注/视频说明（键=素材路径）；
 * TOOL_EN = 中文工具名映射；CAT_EN = 分类名；LEADS_EN = 分类页导语。
 * CN 页面不 import 本文件；EN 页面查不到的键一律回退中文原文。 */

export const ATTR_EN: Record<string, string> = {
	原创: 'ORIGINAL',
	参考还原: 'REFERENCE',
	教程跟做: 'TUTORIAL',
	基于案例二创: 'DERIVATIVE',
};

export const CAT_EN: Record<string, string> = {
	'3d': 'Environment Art / 3D',
	vibecoding: 'Vibecoding',
	graphic: 'Graphic Design',
};

export const TOOL_EN: Record<string, string> = {
	即梦AI: 'Jimeng AI',
};

export const WORK_EN: Record<string, { t: string; s: string }> = {
	'scarab-sphere': {
		t: 'Scarab Sphere — The Dig Site',
		s: 'Cinematic environment short: hand-sculpted terrain, procedural sphere materials, a military tent simulated in Marvelous Designer, graded in After Effects.',
	},
	'metahuman-costume': {
		t: 'Metahuman — Costume Character',
		s: 'Hero character for my original game Flight 404: AI-assisted concept and high-poly, integrated into UE5 Metahuman, with manual retopology and normal baking.',
	},
	onboard: {
		t: 'OnBoard — 3D Snowboard Previewer',
		s: 'Web-based 3D snowboard preview tool (self-built, AI-assisted): material editing, decal system, HDRI environments and bake export — live at onboard.wang.',
	},
	bitsugar: {
		t: 'BitSugar — Fuse-Bead Pattern Studio',
		s: 'Free public web tool, live in production. Domain, DNS, deployment and search-engine submission all done independently; open-sourced on GitHub.',
	},
	'telephone-pbr': {
		t: 'Vintage Telephone — PBR',
		s: 'Full-pipeline PBR product render: modeling, UVs, Substance Painter texturing, Cycles renders. Also the live hero of the 3D category page.',
	},
	'shilian-game': {
		t: 'Lost Signal — Playable Game Demo',
		s: 'A playable UE5 blueprint game demo (full playthrough): gameplay heavily reworked and extended from a tutorial case — not a replica.',
	},
	'blender-renders': {
		t: 'Blender Render Studies',
		s: 'Freestyle Blender renders: scene building, lighting and mood — rooftop ruins at dusk, abandoned hospital, earth, and a product shot.',
	},
	'practice-renders': {
		t: 'Tutorial Practice Reels',
		s: 'Render exercises from my student years following tutorials: subway passage, storm ocean, flowing forest, Romanesque building, dark alley.',
	},
	'logo-type': {
		t: 'Logo & Type Design',
		s: 'Logo and lettering collection: personal brand "lenmou" in black & white, mark arrangements, and the identity for my own 3D previewer OnBoard.',
	},
	'student-posters': {
		t: 'Poster Collection',
		s: 'Four posters from my student years: theme pieces and event visuals — galaxy, anxiety, Caiyun, SunLing.',
	},
	'xiangchi-rollup': {
		t: 'Xiangchi Sports — In-Store Roll-up Banners',
		s: 'Commercial work from my internship at Xiangchi Sports: roll-up banner designs for offline stores, from brand rules to print production.',
	},
	'yuye-packaging': {
		t: 'Yuye WanderBrew — Packaging Design',
		s: 'Full packaging design for the instant-coffee brand "Yuye WanderBrew": key visual, can and box structure, and shelf display.',
	},
};

export const CAPTION_EN: Record<string, string> = {
	'/works/meta-ai-01.jpg': '1/10 · Jimeng AI — character head concept',
	'/works/meta-ai-02.jpg': '2/10 · Hyper3D — head high-poly & base textures',
	'/works/meta-fullbody.jpg': '3/10 · Full body in UE5 (reference for AI generation)',
	'/works/meta-ai-04.jpg': '4/10 · AI-generated outfit reference',
	'/works/meta-ai-05.jpg': '5/10 · AI-generated figure extraction (garment only)',
	'/works/meta-ai-06.jpg': '6/10 · AI-generated jacket split (modeling reference)',
	'/works/meta-ai-07.jpg': '7/10 · AI-generated pants split (modeling reference)',
	'/works/meta-ai-08.jpg': '8/10 · AI-generated shoes split (modeling reference)',
	'/works/meta-ai-09.jpg': '9/10 · Hyper3D — garment high-poly',
	'/works/meta-ai-10.jpg': '10/10 · Remaining steps in Blender (shading & assembly)',
	'/videos/practice-subway.mp4': 'Subway Passage',
	'/videos/practice-ocean.mp4': 'Storm Ocean',
	'/videos/practice-forest.mp4': 'Flowing Forest',
	'/videos/practice-rome.mp4': 'Romanesque Building',
	'/videos/practice-alley.mp4': 'Dark Alley',
	'/works/scarab-step-1.jpg': 'UE5 scene building 1/6',
	'/works/scarab-step-2.jpg': 'UE5 scene building 2/6',
	'/works/scarab-step-3.jpg': 'UE5 scene building 3/6',
	'/works/scarab-step-4.jpg': 'UE5 scene building 4/6',
	'/works/scarab-step-5.jpg': 'UE5 scene building 5/6',
	'/works/scarab-step-6.jpg': 'UE5 scene building 6/6',
	'/works/scarab-tent-md.jpg': 'Military tent — Marvelous Designer blockout',
	'/works/scarab-nodes.jpg': 'Sphere material nodes & material showcase',
};

export const LEADS_EN: Record<string, string> = {
	'3d': 'UE5 environment art and the full Blender pipeline — scene building, lookdev, lighting and rendering; film and product tracks side by side.',
	vibecoding: 'Live web products built with AI-assisted development — requirements, coding and deployment done independently; the demos are the works themselves.',
	graphic: 'Graphic design foundation — branding, packaging, posters and offline materials; the bedrock of all layout work.',
};

export const UI_EN = {
	newWindow: 'Open in new tab ↗',
	activate: 'Click to interact',
	loadFail: 'Embed failed to load — ',
	live: 'LIVE — Online',
	bitsugarDesc:
		'Fuse-bead pattern tool (free & public): domain, DNS, deployment and search-engine submission all done independently; open-sourced on GitHub.',
	onboardDesc:
		'3D snowboard previewer "OnBoard" (self-built, AI-assisted): swap materials, add decals, adjust HDRI lighting and bake the final texture — right in the browser.',
	works: 'Works',
	empty: 'Works coming soon — being reviewed and uploaded.',
	moreCats: 'Keep browsing',
	moreCatsSub: 'the other two categories',
	process: 'Production Process',
	hint3d: 'SCROLL — scroll to pick up the receiver · move mouse to look around',
};
