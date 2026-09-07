import type { WorkCategory } from './categories';

/** 分类卡配图单一来源（首页分类卡 + 分类页底部互推卡共用）。
 * 2026-09-06 用户指定：地编/3D=圣甲虫渲染图、Vibecoding=官方分类展示图。 */
export const CATEGORY_IMAGES: Record<WorkCategory, string> = {
	'3d': '/works/scarab-sphere.jpg',
	vibecoding: '/works/vibecoding-cat.jpg',
	graphic: '/works/galaxy-poster.jpg',
};
