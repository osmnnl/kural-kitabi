#!/usr/bin/env python3
"""Local render-check via headless Google Chrome (wkhtmltoimage replacement).

Pipeline: build.py writes _check.html (literal colors, all assets base64). Chrome
renders it at 280mm=1058px width; each page is 1058px tall + 22px gap, so page N
sits at y0=(N-1)*1080. This screenshots the full stack then crops requested pages.

Usage:
  python3 render_check.py <total_pages_built> <page_to_crop> [more pages...]
  e.g.  python3 build.py 1 2 ... 17   &&   python3 render_check.py 17 17
Outputs: /tmp/r.png (full stack), /tmp/r_pNN.png (per cropped page).
Chrome reads CSS var() fine, but we point at _check.html to match the documented flow.
"""
import subprocess, sys, pathlib
from PIL import Image

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ROOT = pathlib.Path(__file__).resolve().parent
CHECK = ROOT / "_check.html"
PAGE_H, GAP = 1058, 22          # px per page at 96dpi (280mm) + page-wrap bottom margin
STRIDE = PAGE_H + GAP           # 1080

def main():
    total = int(sys.argv[1])
    crops = [int(a) for a in sys.argv[2:]] or [total]
    height = total * STRIDE + 140
    full = "/tmp/r.png"
    subprocess.run([
        CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", "--default-background-color=00000000",
        f"--window-size=1058,{height}", f"--screenshot={full}",
        "--virtual-time-budget=6000", CHECK.as_uri(),
    ], check=True, capture_output=True)
    im = Image.open(full)
    print("rendered", full, im.size)
    for n in crops:
        y0 = (n - 1) * STRIDE
        box = (0, y0, min(1058, im.width), min(y0 + PAGE_H, im.height))
        out = f"/tmp/r_p{n:02d}.png"
        im.crop(box).save(out)
        print("cropped page", n, "->", out, box)

if __name__ == "__main__":
    main()
