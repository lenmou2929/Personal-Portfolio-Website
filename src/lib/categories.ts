/** 作品分类（docs/网站/00-网站策划案 §2 站点地图 v2）。
 * 注意：与 src/content.config.ts 里 schema 的 z.enum 保持同一组 key。 */
export const WORK_CATEGORIES = [
	{ key: '3d', label: '3D 美术', en: '3D / LOOKDEV' },
	{ key: 'graphic', label: '平面设计', en: 'GRAPHIC' },
	{ key: 'vibecoding', label: 'Vibecoding', en: 'WEB APP' },
	{ key: 'planning', label: '项目策划', en: 'PLANNING' },
] as const;

export type WorkCategory = (typeof WORK_CATEGORIES)[number]['key'];

export function findCategory(key: string) {
	return WORK_CATEGORIES.find((c) => c.key === key);
}
