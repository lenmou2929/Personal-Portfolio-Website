/** 作品分类（docs/网站/00-网站策划案 §2 站点地图 v2）。
 * 2026-09-06 用户调整：策划分类移除、3D 改名「地编/3D」、顺序 3D → Vibecoding → 平面
 * （README 决策表）。no = 页面 kicker 编号（与首页分类卡顺序一致）。
 * 注意：与 src/content.config.ts 里 schema 的 z.enum 保持同一组 key。 */
export const WORK_CATEGORIES = [
	{ key: '3d', no: '01', label: '地编/3D', en: '3D / LOOKDEV' },
	{ key: 'vibecoding', no: '02', label: 'Vibecoding', en: 'WEB APP' },
	{ key: 'graphic', no: '03', label: '平面设计', en: 'GRAPHIC' },
] as const;

export type WorkCategory = (typeof WORK_CATEGORIES)[number]['key'];

export function findCategory(key: string) {
	return WORK_CATEGORIES.find((c) => c.key === key);
}
