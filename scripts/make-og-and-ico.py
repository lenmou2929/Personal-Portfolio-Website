# 生成两件分享/品牌静态资产（2026-09-10 求职信息审计 P4/C3/P5）：
#   1) public/og-image.jpg —— 1200×630 社交分享卡片（微信/QQ 分享名片效果），风格同站点
#      定稿（暖纸底 #F5F3EE / 电话绿 #4E6E5C / 墨色 #1D1B17）
#   2) public/favicon.ico —— 由 favicon.png 转出的多尺寸 ico，消除浏览器默认请求 404
# 用法：python scripts/make-og-and-ico.py（改动文案/配色后重跑即可）
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / 'public'

BG = (245, 243, 238)      # --color-bg 暖纸底
INK = (29, 27, 23)        # --color-ink
INK2 = (111, 106, 95)     # --color-ink-2
ACCENT = (78, 110, 92)    # --color-accent 电话绿

F_YAHEI = r'C:\Windows\Fonts\msyh.ttc'
F_YAHEI_B = r'C:\Windows\Fonts\msyhbd.ttc'
F_MONO = r'C:\Windows\Fonts\consola.ttf'


def font(path, size):
    return ImageFont.truetype(path, size)


# ---------- og-image.jpg ----------
W, H = 1200, 630
img = Image.new('RGB', (W, H), BG)
d = ImageDraw.Draw(img)

d.rectangle([0, 0, 14, H], fill=ACCENT)  # 左缘品牌绿条

d.text((72, 74), 'PORTFOLIO · 2023 — 2026', font=font(F_MONO, 26), fill=ACCENT)
d.text((66, 150), '陈继祖', font=font(F_YAHEI_B, 128), fill=INK)
d.text((72, 330), 'UE5 地编 / 3D 美术 · AI 辅助开发', font=font(F_YAHEI_B, 48), fill=ACCENT)
d.text((72, 412), '影视向 · 产品向 ｜ 14 件作品 ｜ 深圳 · 随时到岗', font=font(F_YAHEI, 30), fill=INK2)

d.line([72, 486, 1128, 486], fill=(220, 215, 204), width=2)  # --color-line
d.text((72, 516), 'portfolio.onboard.wang', font=font(F_MONO, 34), fill=INK2)

img.save(PUBLIC / 'og-image.jpg', quality=88)
print('og-image.jpg', (PUBLIC / 'og-image.jpg').stat().st_size, 'bytes')

# ---------- favicon.ico ----------
src = Image.open(PUBLIC / 'favicon.png').convert('RGBA')
src.save(PUBLIC / 'favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])
print('favicon.ico', (PUBLIC / 'favicon.ico').stat().st_size, 'bytes')
