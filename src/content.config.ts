import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

/**
 * 作品 collection（字段 = docs/网站/00-网站策划案 §3 详情页数据模板）。
 * 诚实标注是项目红线（docs/公共/00-AI协作规范 §2）：教程跟做/参考还原必须如实标注。
 */
export const collections = {
	work: defineCollection({
		loader: glob({ base: './src/content/works', pattern: '**/*.md' }),
		schema: z.object({
			title: z.string(),
			/** 分类 key（与 src/lib/categories.ts 一致）：3d / vibecoding / graphic（2026-09-06 策划分类移除） */
			category: z.enum(['3d', 'vibecoding', 'graphic']),
			/** 作品分级（03-作品集规划）：S 精选 / A 完整 / B 简历附表 */
			level: z.enum(['S', 'A', 'B']).default('A'),
			/** 策展排序：同日期同级内小者在前（缺省排后）；用户手动调序入口 */
			order: z.number().optional(),
			cover: z.string(),
			cover_alt: z.string().default(''),
			date: z.coerce.date(),
			tools: z.array(z.string()).default([]),
			/** 诚实标注：原创 / 参考还原 / 教程跟做；来源写 attribution_source */
			attribution: z.enum(['原创', '参考还原', '教程跟做']),
			attribution_source: z.string().optional(),
			summary: z.string(),
			video: z.string().optional(),
			/** 多视频（如跟练练习集）：面板逐条渲染；poster=抽帧封面（preload="none" 需要封面图） */
			videos: z
				.array(
					z.object({
						src: z.string(),
						poster: z.string().optional(),
						caption: z.string().optional(),
					}),
				)
				.default([]),
			gallery: z.array(z.string()).default([]),
			process: z.array(z.object({ img: z.string(), caption: z.string() })).default([]),
			links: z.array(z.object({ label: z.string(), url: z.string() })).default([]),
			/** glb 地址（public/models/，可选，详情页 model-viewer 用） */
			model3d: z.string().optional(),
			draft: z.boolean().default(false),
		}),
	}),
};
