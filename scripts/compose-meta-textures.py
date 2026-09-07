# -*- coding: utf-8 -*-
"""Metahuman 上衣材质贴图五合一拼图（2026-09-07 第 20 次会话）。

上排 3 张（BaseColor / Normal / Roughness）+ 下排 2 张居中（Metallic / IOR），
画布 1920×1080 深底（#101214，同作品条内底色），输出 public/works/meta-textures.jpg，
与上衣渲染图（16:9）在图集首行并排等高。改组合/顺序后重跑本脚本。
"""
import os

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, 'assets', '原始素材', '3D类', 'Metahuman服装角色流程', '上衣材质贴图')
DST = os.path.join(ROOT, 'website', 'public', 'works', 'meta-textures.jpg')

CANVAS_W, CANVAS_H = 1920, 1080
CELL = 540  # 两排 540 正好 1080 高；上排 3 张居中，下排 2 张居中
BG = (16, 18, 20)  # #101214
ROW1 = ['T_Clothes_Color.png', 'T_Clothes_Normal.png', 'T_Clothes_Rough.png']
ROW2 = ['T_Clothes_Metal.png', 'T_Clothes_IOR.png']


def paste_cell(canvas: Image.Image, path: str, x: int, y: int) -> None:
    im = Image.open(path).convert('RGB')
    im.thumbnail((CELL, CELL), Image.LANCZOS)  # 源为正方形 → 缩至 540×540
    canvas.paste(im, (x + (CELL - im.width) // 2, y + (CELL - im.height) // 2))


def main():
    canvas = Image.new('RGB', (CANVAS_W, CANVAS_H), BG)
    for row, names in ((0, ROW1), (1, ROW2)):
        total = len(names) * CELL
        x0 = (CANVAS_W - total) // 2
        for k, name in enumerate(names):
            paste_cell(canvas, os.path.join(SRC, name), x0 + k * CELL, row * CELL)
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    canvas.save(DST, 'JPEG', quality=86, optimize=True, progressive=True)
    print('[拼] works/meta-textures.jpg', canvas.size, os.path.getsize(DST) // 1024, 'KB')


if __name__ == '__main__':
    main()
