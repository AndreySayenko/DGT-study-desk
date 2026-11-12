# -*- coding: utf-8 -*-
"""Helpers for the original SVG diagrams (no third-party artwork). Colours are fixed: figures sit on a light
"paper" background in both themes."""

FONT = "Inter, 'DejaVu Sans', Arial, sans-serif"
NAVY = "#12355b"
TEAL = "#0f766e"
AMBER = "#b45309"
RED = "#b42318"
SLATE = "#475569"
BLUE = "#1d4ed8"
INK = "#0f172a"


def svg(w, h, inner, title=""):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" role="img" aria-label="{title}" '
        f'style="font-family:{FONT};">{inner}</svg>'
    )


def txt(x, y, s, size=12, weight=400, fill=INK, anchor="start", italic=False):
    st = ' font-style="italic"' if italic else ""
    return (
        f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" '
        f'fill="{fill}" text-anchor="{anchor}"{st}>{s}</text>'
    )


def lines(x, y, arr, size=11, weight=400, fill=INK, anchor="start", lh=14):
    out = []
    for i, s in enumerate(arr):
        out.append(txt(x, y + i * lh, s, size, weight, fill, anchor))
    return "".join(out)


def box(x, y, w, h, fill, title, sub=None, tcolor="#fff", scolor=None, stroke=None, size=12.5):
    sc = f' stroke="{stroke}" stroke-width="1.5"' if stroke else ""
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{fill}"{sc}/>']
    cx = x + w / 2
    if isinstance(title, str):
        title = [title]
    if sub:
        base = y + h / 2 - 3 - (len(title) - 1) * 7
        out.append(lines(cx, base, title, size, 700, tcolor, "middle", 14))
        out.append(txt(cx, y + h - 9, sub, 10, 400, scolor or tcolor, "middle"))
    else:
        base = y + h / 2 + 4 - (len(title) - 1) * 7
        out.append(lines(cx, base, title, size, 700, tcolor, "middle", 14))
    return "".join(out)
