# -*- coding: utf-8 -*-
"""B 组素材图片入库管线（2026-09-06 第 20 次会话）。

规范（docs/网站/04-素材格式清单 核对版）：原始素材 → 长边 ≤1920px、sRGB、
JPG（质量 86）、LANCZOS 缩放，输出至 website/public/works/。
后续用户补交素材时在 MAPPINGS 增行重跑即可。
"""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, 'assets', '原始素材')
DST = os.path.join(ROOT, 'website', 'public', 'works')
MAX_EDGE = 1920
QUALITY = 86

# 源（相对 assets/原始素材）→ 目标（相对 website/public/works）
MAPPINGS = {
    # ---- 平面类 → graphic/ ----
    '平面类/包装设计/隅野包装设计_画板 1.png': 'graphic/yuye-cover.jpg',
    **{
        f'平面类/包装设计/隅野包装设计-{n:02d}.png': f'graphic/yuye-{n:02d}.jpg'
        for n in range(2, 14)
    },
    '平面类/海报类/SunLing海报.jpg': 'graphic/poster-sunling.jpg',
    '平面类/海报类/彩云海报（优）.jpg': 'graphic/poster-caiyun.jpg',
    '平面类/海报类/焦虑海报（优）.jpg': 'graphic/poster-jiaolv.jpg',
    '平面类/海报类/银河海报（优）.jpg': 'graphic/poster-yinhe.jpg',
    '平面类/翔驰易拉宝/易拉宝一.png': 'graphic/rollup-01.jpg',
    '平面类/翔驰易拉宝/易拉宝二.png': 'graphic/rollup-02.jpg',
    '平面类/翔驰易拉宝/易拉宝三.png': 'graphic/rollup-03.jpg',
    '平面类/翔驰易拉宝/易拉宝四.png': 'graphic/rollup-04.jpg',
    '平面类/logo&字体设计/Logo&字体合集_1.png': 'graphic/logo-set-1.jpg',
    '平面类/logo&字体设计/Logo&字体合集_2.png': 'graphic/logo-set-2.jpg',
    '平面类/logo&字体设计/logo排列.jpg': 'graphic/logo-grid.jpg',
    # Wine bottle spatula Logo（废）.jpg —— 用户已标废，不上站
    '平面类/logo&字体设计/Len mou 白.png': 'graphic/logo-lenmou-w.jpg',
    '平面类/logo&字体设计/len mou 黑.png': 'graphic/logo-lenmou-b.jpg',
    '平面类/OnBoard（我的vibecoding类别作品中的3D预览器品牌）/OnBoard品牌logo排版.png': 'graphic/onboard-brand.jpg',
    # ---- 3D 类：座机四视角（正面已有 phone-front.jpg）----
    '3D类/老式电话机/老式电话渲染图/老式电话背面细节图.png': 'phone-back.jpg',
    '3D类/老式电话机/老式电话渲染图/老式电话左侧面细节图.png': 'phone-left.jpg',
    '3D类/老式电话机/老式电话渲染图/老式电话右侧面细节图.png': 'phone-right.jpg',
    # ---- 3D 类：Metahuman 图集 + AI 辅助过程 ----
    '3D类/Metahuman服装角色流程/UE5中角色全身截图（用于生成AI做参考）.png': 'meta-fullbody.jpg',
    '3D类/Metahuman服装角色流程/上衣渲染图.png': 'meta-top-render.jpg',
    '3D类/Metahuman服装角色流程/上衣高模.png': 'meta-top-high.jpg',
    '3D类/Metahuman服装角色流程/上衣低模.png': 'meta-top-low.jpg',
    '3D类/Metahuman服装角色流程/上衣低模拓扑线图.png': 'meta-top-wire.jpg',
    '3D类/Metahuman服装角色流程/法线烘培结果.png': 'meta-bake.jpg',
    '3D类/Metahuman服装角色流程/AI辅助角色制作流程/01-即梦AI角色头部形象生成截图.png': 'meta-ai-01.jpg',
    '3D类/Metahuman服装角色流程/AI辅助角色制作流程/02-Hyper3D生成头部高模与基本贴图截图.png': 'meta-ai-02.jpg',
    '3D类/Metahuman服装角色流程/AI生成角色着装图.png': 'meta-ai-03.jpg',
    '3D类/Metahuman服装角色流程/AI生成上衣拆分图.png': 'meta-ai-04.jpg',
    # ---- 3D 类：圣甲虫过程（成品渲染图已有 scarab-sphere.jpg）----
    **{
        f'3D类/圣甲虫球体地编项目/圣甲虫球体UE5场景搭建步骤图/BuZ.{i}.jpeg': f'scarab-step-{i + 1}.jpg'
        for i in range(6)
    },
    '3D类/圣甲虫球体地编项目/材质、布料制作图/军用帐篷MD白膜展示.png': 'scarab-tent-md.jpg',
    '3D类/圣甲虫球体地编项目/材质、布料制作图/圣甲虫球体材质球节点及材质展示.png': 'scarab-nodes.jpg',
    # ---- 3D 类：Blender 渲染练习（原创条目）----
    '3D类/Blender渲染图/余晖废墟渲染图.png': 'blender-ruins.jpg',
    '3D类/Blender渲染图/医院一楼.png': 'blender-hospital-1.jpg',
    '3D类/Blender渲染图/医院空房.jpg': 'blender-hospital-2.jpg',
    '3D类/Blender渲染图/地球.png': 'blender-earth.jpg',
    '3D类/Blender渲染图/极客薯片产品渲染图.png': 'blender-chips.jpg',
    # ---- 3D 类：跟练练习集图集（黑暗小巷静帧，与跟练视频同作品）----
    '3D类/Blender渲染图/黑暗小巷_横屏.jpg': 'alley-h.jpg',
    '3D类/Blender渲染图/黑暗小巷_竖屏冷色调.png': 'alley-cold.jpg',
    '3D类/Blender渲染图/黑暗小巷_竖屏暖色调.png': 'alley-warm.jpg',
}


def process(src: str, dst: str) -> tuple:
    im = Image.open(src)
    im = im.convert('RGB')  # sRGB 输出，去掉 alpha/调色板
    w, h = im.size
    if max(w, h) > MAX_EDGE:
        scale = MAX_EDGE / max(w, h)
        im = im.resize((round(w * scale), round(h * scale)), Image.LANCZOS)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    im.save(dst, 'JPEG', quality=QUALITY, optimize=True, progressive=True)
    return im.size, os.path.getsize(dst)


def main():
    total_in = total_out = 0
    for src_rel, dst_rel in MAPPINGS.items():
        src = os.path.join(SRC, src_rel)
        dst = os.path.join(DST, dst_rel)
        if not os.path.exists(src):
            print(f'[缺] {src_rel}')
            continue
        (w, h), size = process(src, dst)
        total_in += os.path.getsize(src)
        total_out += size
        print(f'[入] {dst_rel}  {w}x{h}  {size // 1024}KB')
    print(f'-- 合计 {len(MAPPINGS)} 张：{total_in // 1024 // 1024}MB → {total_out // 1024 // 1024}MB --')


if __name__ == '__main__':
    main()
