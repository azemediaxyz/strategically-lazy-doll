#!/usr/bin/env python3
"""Put a meme line on an image: 1080x1350 (4:5), white text, thin black outline.

Usage:
  python3 overlay.py image.jpg "My line here" -o meme.jpg
  python3 overlay.py image.jpg "First line\\nsecond line" --position top --font Inter-SemiBold.ttf

Needs Pillow (pip install pillow). Put \\n where you want a line break;
otherwise the text wraps by itself and avoids leaving one word alone on a line.
"""
import argparse
import os
import sys

from PIL import Image, ImageDraw, ImageFont, ImageOps

W, H = 1080, 1350
FONT_CANDIDATES = [
    "Inter-SemiBold.ttf", "Inter-SemiBold.otf",
    "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf",
    "/usr/share/fonts/truetype/inter/Inter-SemiBold.ttf",
    "/Library/Fonts/Inter-SemiBold.ttf",
    os.path.expanduser("~/Library/Fonts/Inter-SemiBold.ttf"),
    "C:/Windows/Fonts/Inter-SemiBold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/Library/Fonts/Arial Bold.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
]


def load_font(path, size):
    for p in ([path] if path else []) + FONT_CANDIDATES:
        try:
            return ImageFont.truetype(p, size)
        except OSError:
            continue
    sys.exit("No usable font found. Pass one with --font path/to/font.ttf")


def wrap_para(draw, para, font, max_w):
    lines, cur = [], ""
    for w in para.split():
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=font) <= max_w:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    lines.append(cur)
    # no orphan: if the last line is one word, pull a word down from the line above
    if len(lines) >= 2 and len(lines[-1].split()) == 1 and len(lines[-2].split()) > 2:
        prev = lines[-2].split()
        cand = prev[-1] + " " + lines[-1]
        if draw.textlength(cand, font=font) <= max_w:
            lines[-2], lines[-1] = " ".join(prev[:-1]), cand
    return lines


def wrap(draw, text, font, max_w):
    """Returns (lines, has_orphan). Each manual \n starts a new line."""
    lines, orphan = [], False
    for para in text.split("\n"):
        pl = wrap_para(draw, para, font, max_w)
        if len(pl) >= 2 and len(pl[-1].split()) == 1:
            orphan = True
        lines += pl
    return lines, orphan


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("image")
    ap.add_argument("text")
    ap.add_argument("-o", "--output", default="meme.jpg")
    ap.add_argument("--position", choices=["bottom", "top"], default="bottom")
    ap.add_argument("--font", default=None)
    ap.add_argument("--size", type=int, default=0, help="font size in px (default: fit automatically)")
    a = ap.parse_args()

    img = ImageOps.fit(Image.open(a.image).convert("RGB"), (W, H), Image.LANCZOS)
    draw = ImageDraw.Draw(img)
    text = a.text.replace("\\n", "\n")
    max_w = int(W * 0.86)

    # biggest size (68 down to 40) that fits in 5 lines / 38% of the height,
    # preferring one with no word left alone on a line
    def fits(size):
        font = load_font(a.font, size)
        lines, orphan = wrap(draw, text, font, max_w)
        line_h = int(size * 1.25)
        return font, lines, orphan, line_h, len(lines) <= 5 and line_h * len(lines) <= H * 0.38

    sizes = [a.size] if a.size else list(range(68, 38, -2))
    tried = [(s_,) + fits(s_) for s_ in sizes]
    ok = [t for t in tried if t[5]]
    size, font, lines, orphan, line_h, _ = next((t for t in ok if not t[3]), ok[0] if ok else tried[-1])

    block_h = line_h * len(lines)
    y = int(H * 0.06) if a.position == "top" else H - block_h - int(H * 0.07)
    stroke = max(2, size // 22)
    for line in lines:
        x = (W - draw.textlength(line, font=font)) / 2
        draw.text((x, y), line, font=font, fill="white", stroke_width=stroke, stroke_fill="black")
        y += line_h

    img.save(a.output, quality=92)
    print(f"Saved {a.output} ({W}x{H}, {size}px, {len(lines)} lines)")


if __name__ == "__main__":
    main()
