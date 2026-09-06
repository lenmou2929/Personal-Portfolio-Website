# -*- coding: utf-8 -*-
"""B 组视频入库管线（2026-09-06 第 20 次会话）。

跟练 5 条 + 圣甲虫成片 → website/public/videos/。
规范：H.264 CRF25 限速 5M（单条 ≤15MB，GitHub <100MB 硬限制）、1440p 归一
1080p、AAC 128k、+faststart；另抽帧做 poster（preload="none" 需要封面）。
后续补视频在 JOBS 增行重跑。
"""
import os
import re
import subprocess

from imageio_ffmpeg import get_ffmpeg_exe

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, 'assets', '原始素材')
DST = os.path.join(ROOT, 'website', 'public', 'videos')
FF = get_ffmpeg_exe()

# (源, 目标名, poster 采样点占全片比例) —— 地铁通道含片头，取后半段
JOBS = [
    ('3D类/学生时期的跟练渲染作品/地铁通道_含片头.mp4', 'practice-subway.mp4', 0.55),
    ('3D类/学生时期的跟练渲染作品/暴风海洋.mp4', 'practice-ocean.mp4', 0.35),
    ('3D类/学生时期的跟练渲染作品/流动森林.mp4', 'practice-forest.mp4', 0.35),
    ('3D类/学生时期的跟练渲染作品/罗马式小建筑.mp4', 'practice-rome.mp4', 0.35),
    ('3D类/学生时期的跟练渲染作品/黑暗小巷视频.mp4', 'practice-alley.mp4', 0.35),
    ('3D类/圣甲虫球体地编项目/圣甲虫球体场景渲染视频.mp4', 'scarab-sphere.mp4', 0.4),
]
MAX_BYTES = 15 * 1024 * 1024


def duration(path: str) -> float:
    r = subprocess.run([FF, '-i', path], capture_output=True, text=True, encoding='utf-8', errors='replace')
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r.stderr)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else 0.0


def encode(src: str, dst: str) -> None:
    """统一压到 1080 级（长边 1920）、CRF25 限速 5M。圣甲虫源码率已达标但仍走同管线，保证 faststart。"""
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    tmp = dst + '.tmp.mp4'
    subprocess.run(
        [
            FF, '-y', '-i', src,
            '-vf', "scale='if(gt(iw,ih),min(1920,iw),-2)':'if(gt(iw,ih),-2,min(1920,ih))'",
            '-c:v', 'libx264', '-crf', '25', '-preset', 'medium',
            '-maxrate', '5M', '-bufsize', '10M',
            '-c:a', 'aac', '-b:a', '128k',
            '-movflags', '+faststart',
            tmp,
        ],
        check=True, capture_output=True,
    )
    os.replace(tmp, dst)


def poster(src: str, dst: str, at: float) -> None:
    total = duration(src)
    ts = min(total * at, max(total - 0.5, 0)) if total else 1.0
    subprocess.run(
        [FF, '-y', '-ss', f'{ts:.2f}', '-i', src, '-frames:v', '1',
         '-vf', "scale='if(gt(iw,ih),min(1280,iw),-2)':'if(gt(iw,ih),-2,min(1280,ih))'",
         '-q:v', '3', dst],
        check=True, capture_output=True,
    )


def main():
    for src_rel, name, at in JOBS:
        src = os.path.join(SRC, src_rel)
        dst_mp4 = os.path.join(DST, name)
        dst_jpg = os.path.join(DST, name.replace('.mp4', '.jpg'))
        if not os.path.exists(src):
            print(f'[缺] {src_rel}')
            continue
        encode(src, dst_mp4)
        poster(src, dst_jpg, at)
        mb = os.path.getsize(dst_mp4) / 1024 / 1024
        flag = ' ⚠️超15MB' if os.path.getsize(dst_mp4) > MAX_BYTES else ''
        print(f'[入] videos/{name}  {mb:.1f}MB{flag}  + {os.path.basename(dst_jpg)} {os.path.getsize(dst_jpg)//1024}KB')


if __name__ == '__main__':
    main()
