// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  vite: {
    plugins: [tailwindcss()],
    build: {
      // CSS 目标降到 Chromium 84 档：压缩器会把媒体查询写成区间语法 (width<=640px)（需 104+），
      // 百度 T7 等老壳内核读不懂就整块丢弃，手机端样式全失效。降档后还原为经典 max-width 写法。
      // 调研与验收见 docs/网站/05-百度App内核兼容调研与修复方案.md（2026-09-10）
      cssTarget: ['chrome84'],
    },
  }
});