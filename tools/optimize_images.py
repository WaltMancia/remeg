#!/usr/bin/env python3
"""Convierte fotografías a WebP optimizado para la web.

Uso:  python3 tools/optimize_images.py ruta/foto.jpg [otra.png ...]
Genera site/assets/<nombre>.webp (máx. 820 px de lado largo, calidad 70).
Requiere: pip install pillow
"""
import sys
from pathlib import Path
from PIL import Image

OUT = Path(__file__).resolve().parent.parent / "site" / "assets"

for arg in sys.argv[1:]:
    src = Path(arg)
    img = Image.open(src).convert("RGB")
    img.thumbnail((820, 820))
    dest = OUT / f"{src.stem}.webp"
    img.save(dest, "WEBP", quality=70)
    print(f"{src.name} -> {dest.relative_to(OUT.parent.parent)} {img.size} {dest.stat().st_size // 1024} KB")
    print("   Recuerde usar width/height reales y un alt descriptivo en index.html.")
