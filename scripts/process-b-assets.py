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
    # 「Len mou 白.png」白底白 logo 上站呈全白（2026-09-06 用户确认移除），不再入库
    '平面类/logo&字体设计/len mou 黑.png': 'graphic/logo-lenmou-b.jpg',
    '平面类/OnBoard（我的vibecoding类别作品中的3D预览器品牌）/OnBoard品牌logo排版.png': 'graphic/onboard-brand.jpg',
    # ---- vibecoding：BitSugar / OnBoard 实机截图（尾缀定序；比特糖 -1 即封面）----
    'vibecoding/BitSugar · 比特糖/比特糖网站截图展示-1.png': 'bitsugar-cover.jpg',
    'vibecoding/BitSugar · 比特糖/比特糖网站截图展示-英文版-2.png': 'bitsugar-en.jpg',
    'vibecoding/BitSugar · 比特糖/首页下方的图纸预览界面截图-3.png': 'bitsugar-preview.jpg',
    'vibecoding/BitSugar · 比特糖/拼豆绘制界面截图-4.png': 'bitsugar-paint.jpg',
    'vibecoding/BitSugar · 比特糖/vibecoding分类展示图.png': 'vibecoding-cat.jpg',
    'vibecoding/OnBoard · 上板/01-默认界面截图.png': 'onboard-01.jpg',
    'vibecoding/OnBoard · 上板/02-贴花效果截图.png': 'onboard-02.jpg',
    'vibecoding/OnBoard · 上板/03-弹窗设置截图.png': 'onboard-03.jpg',
    'vibecoding/OnBoard · 上板/04-整体效果截图.png': 'onboard-04.jpg',
    # ---- 3D 类：座机四视角（正面已有 phone-front.jpg）----
    '3D类/老式电话机/老式电话渲染图/老式电话背面细节图.png': 'phone-back.jpg',
    '3D类/老式电话机/老式电话渲染图/老式电话左侧面细节图.png': 'phone-left.jpg',
    '3D类/老式电话机/老式电话渲染图/老式电话右侧面细节图.png': 'phone-right.jpg',
    # ---- 3D 类：UE5 悬崖植被地编（2026-09-09 新增，-1 为封面）----
    '3D类/UE5影视地编作品-悬崖/悬崖边-1.png': 'cliff-cover.jpg',
    '3D类/UE5影视地编作品-悬崖/远处山林-2.png': 'cliff-forest-far.jpg',
    # ---- 3D 类：AI 生成前期场景概念图（2026-09-09 新增，AI 生成图为封面）----
    '3D类/AI生成前期场景概念图/AI概念图_Short_1.1.png': 'ai-concept-cover.jpg',
    '3D类/AI生成前期场景概念图/Blender白膜ID_Short_1.1.png': 'ai-concept-whitebox.jpg',
    # ---- 3D 类：Metahuman 图集 + AI 辅助过程（过程图按用户尾缀 -1..-8 定序）----
    '3D类/Metahuman服装角色流程/UE5中角色全身截图（用于生成AI做参考）-3.png': 'meta-fullbody.jpg',
    '3D类/Metahuman服装角色流程/Metahuman卡片封面.png': 'meta-card.jpg',
    '3D类/Metahuman服装角色流程/上衣渲染图.png': 'meta-top-render.jpg',
    '3D类/Metahuman服装角色流程/上衣高模.png': 'meta-top-high.jpg',
    '3D类/Metahuman服装角色流程/上衣低模.png': 'meta-top-low.jpg',
    '3D类/Metahuman服装角色流程/上衣低模拓扑线图.png': 'meta-top-wire.jpg',
    '3D类/Metahuman服装角色流程/上衣法线烘培结果.png': 'meta-bake.jpg',
    '3D类/Metahuman服装角色流程/裤子渲染图.png': 'meta-pants-render.jpg',
    '3D类/Metahuman服装角色流程/裤子高模.png': 'meta-pants-high.jpg',
    '3D类/Metahuman服装角色流程/裤子低模.png': 'meta-pants-low.jpg',
    '3D类/Metahuman服装角色流程/裤子低模拓扑线图.png': 'meta-pants-wire.jpg',
    '3D类/Metahuman服装角色流程/裤子法线烘培结果.png': 'meta-pants-bake.jpg',
    '3D类/Metahuman服装角色流程/皮鞋渲染图.png': 'meta-shoes-render.jpg',
    '3D类/Metahuman服装角色流程/皮鞋高模.png': 'meta-shoes-high.jpg',
    '3D类/Metahuman服装角色流程/皮鞋低模.png': 'meta-shoes-low.jpg',
    '3D类/Metahuman服装角色流程/皮鞋低模拓扑线图.png': 'meta-shoes-wire.jpg',
    '3D类/Metahuman服装角色流程/皮鞋法线烘培结果.png': 'meta-shoes-bake.jpg',
    '3D类/Metahuman服装角色流程/即梦AI角色头部形象生成截图-1.png': 'meta-ai-01.jpg',
    '3D类/Metahuman服装角色流程/02-Hyper3D生成头部高模与基本贴图截图-2.png': 'meta-ai-02.jpg',
    # 过程第 3 步（UE5 全身参考）与图集 meta-fullbody 同源同图，直接复用不另存
    '3D类/Metahuman服装角色流程/AI生成角色着装图-4.png': 'meta-ai-04.jpg',
    '3D类/Metahuman服装角色流程/AI生成去除角色图-5.png': 'meta-ai-05.jpg',
    '3D类/Metahuman服装角色流程/AI生成上衣拆分图-6.png': 'meta-ai-06.jpg',
    '3D类/Metahuman服装角色流程/AI生成裤子拆分图-7.png': 'meta-ai-07.jpg',
    '3D类/Metahuman服装角色流程/AI生成皮鞋拆分图-8.png': 'meta-ai-08.jpg',
    '3D类/Metahuman服装角色流程/AI生成高模-9.png': 'meta-ai-09.jpg',
    '3D类/Metahuman服装角色流程/在Blender中完成剩余操作-10.png': 'meta-ai-10.jpg',
    # ---- 3D 类：失联游戏场景截图（尾缀定序）----
    **{
        f'3D类/失联游戏全流程演示（玩法内容在教程之上进行了大改）/游戏场景-{n}.png': f'shilian-scene-{n:02d}.jpg'
        for n in range(1, 12)
    },
    '3D类/失联游戏全流程演示（玩法内容在教程之上进行了大改）/失联全流程卡片封面.png': 'shilian-card.jpg',
    # ---- 3D 类：圣甲虫过程（成品渲染图已有 scarab-sphere.jpg）----
    **{
        f'3D类/圣甲虫球体地编项目/圣甲虫球体UE5场景搭建步骤图/BuZ.{i}.jpeg': f'scarab-step-{i + 1}.jpg'
        for i in range(6)
    },
    '3D类/圣甲虫球体地编项目/材质、布料制作图/军用帐篷MD白膜展示.png': 'scarab-tent-md.jpg',
    '3D类/圣甲虫球体地编项目/材质、布料制作图/圣甲虫球体材质球节点及材质展示.png': 'scarab-nodes.jpg',
    # ---- 3D 类：Blender 渲染练习（原创条目）----
    '3D类/Blender渲染图/余晖废墟渲染图.png': 'blender-ruins.jpg',
    '3D类/失联游戏全流程演示（玩法内容在教程之上进行了大改）/失联全流程卡片封面.png': 'shilian-card.jpg',
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
    recompress_heavy()


def recompress_heavy(threshold_kb: int = 350, quality: int = 82) -> None:
    """后处理：works/ 下超阈值的 JPG 二次压缩（q82），进一步压加载体积。"""
    saved = 0
    count = 0
    for root, _dirs, files in os.walk(DST):
        for f in files:
            if not f.lower().endswith('.jpg'):
                continue
            p = os.path.join(root, f)
            if os.path.getsize(p) <= threshold_kb * 1024:
                continue
            before = os.path.getsize(p)
            im = Image.open(p)
            im.save(p, 'JPEG', quality=quality, optimize=True, progressive=True)
            after = os.path.getsize(p)
            if after < before:
                saved += before - after
                count += 1
                print(f'[压] {os.path.relpath(p, DST)}  {before // 1024}KB → {after // 1024}KB')
    print(f'-- 二次压缩 {count} 张，省 {saved // 1024}KB --')


if __name__ == '__main__':
    main()
