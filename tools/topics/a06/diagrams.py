# -*- coding: utf-8 -*-
"""Original SVG diagrams for Category A1/A2, Topic 6 (carrying people and goods), EN/ES. No third-party artwork is
used. Two figures are specific to this topic; one is shared with Category B, Topic 6 and one with A1/A2, Topic 3."""

from svgkit import NAVY, TEAL, AMBER, RED, SLATE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect, tick, cross
from ..b09.diagrams import L, line, MUTED, LINE, CARD  # noqa: F401
from ..b06.diagrams import _plate, v20, moto_passenger  # noqa: F401  (moto_passenger shared with Topic B6)
from ..a03.diagrams import trailer_rule  # noqa: F401  (shared with A1/A2 Topic 3)

DARK = "#1f2937"
BODY = "#475569"
LOAD = "#b45309"
SIGN_RED = "#c81e1e"


# ---------------------------------------------------------------- D1 the load on a motorcycle
def _moto_top(cx, cy, s=1.0):
    """A motorcycle seen from above, front at the top, centred on (cx, cy). About 30 x 150 at s = 1."""
    def R(x, y, w, h, c, r=4):
        return rect(round(cx + x * s, 1), round(cy + y * s, 1), round(w * s, 1), round(h * s, 1), c, r * s)
    return (R(-6, -75, 12, 34, DARK, 6) + R(-6, 41, 12, 34, DARK, 6) + R(-11, -48, 22, 94, BODY, 9)
            + R(-30, -52, 60, 5, DARK, 2) + R(-9, -14, 18, 40, "#334155", 7))


def _dim_h(x1, x2, y, label, color=AMBER):
    return (f'<path d="M{x1} {y} H{x2}" stroke="{color}" stroke-width="2"/><path d="M{x1} {y - 6} V{y + 6} M{x2} {y - 6} V{y + 6}" stroke="{color}" stroke-width="2"/>'
            + txt((x1 + x2) / 2, y - 9, label, 11.5, 800, color, "middle"))


def _dim_v(x, y1, y2, label, color=AMBER, side="right"):
    tx = x + 10 if side == "right" else x - 10
    return (f'<path d="M{x} {y1} V{y2}" stroke="{color}" stroke-width="2"/><path d="M{x - 6} {y1} H{x + 6} M{x - 6} {y2} H{x + 6}" stroke="{color}" stroke-width="2"/>'
            + txt(tx, (y1 + y2) / 2 + 4, label, 11.5, 800, color, "start" if side == "right" else "end"))


def moto_load(lang):
    p = []
    # panel 1: where the load goes
    p.append(rect(8, 6, 300, 330, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'))
    p.append(txt(158, 30, L(lang, "Where the load goes", "Dónde va la carga"), 13, 800, INK, "middle"))
    cx, cy = 158, 168
    p.append(_moto_top(cx, cy, 1.25))
    p.append(rect(cx - 22, cy + 34, 44, 40, LOAD, 6))                                  # top case on the central rack
    p.append(rect(cx - 40, cy + 18, 16, 46, LOAD, 5) + rect(cx + 24, cy + 18, 16, 46, LOAD, 5))   # side cases
    p.append(txt(cx, cy + 59, L(lang, "rack", "baúl"), 10, 800, "#fff", "middle"))
    p.append(lines(cx, 280, L(lang, ["On the central rear rack (top case)", "or in two side cases, one each side,", "fixed to the frame"],
                                    ["En el portaequipajes central (baúl)", "o en dos maletas laterales, una a cada", "lado, fijadas al chasis"]), 11.5, 700, INK, "middle", 15))
    # panel 2: how far it may stick out
    p.append(rect(320, 6, 392, 330, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'))
    p.append(txt(516, 30, L(lang, "Vehicles under 1 m wide: how far it may stick out", "Menos de 1 m de ancho: cuánto puede sobresalir"), 13, 800, INK, "middle"))
    cx, cy = 500, 150
    k = 120  # px per metre for the load
    rear = cy + 94
    p.append(f'<rect x="{cx - 0.5 * k}" y="{cy + 20}" width="{k}" height="{rear + 0.25 * k - cy - 20}" fill="none" stroke="{TEAL}" stroke-width="2" stroke-dasharray="6 4"/>')
    p.append(_moto_top(cx, cy, 1.25))
    p.append(rect(cx - 46, cy + 62, 92, rear + 18 - cy - 62, LOAD, 5))
    p.append(line(cx, 54, cx, 304, "#94a3b8", 1.4, "4 4") + txt(cx - 8, 58, L(lang, "axis", "eje"), 10.5, 700, SLATE, "end"))
    p.append(_dim_h(cx, cx + 0.5 * k, rear + 58, "≤ 0,50 m" if lang == "es" else "≤ 0.50 m"))
    p.append(_dim_h(cx - 0.5 * k, cx, rear + 58, "≤ 0,50 m" if lang == "es" else "≤ 0.50 m"))
    p.append(line(cx + 10, rear, cx + 0.5 * k + 26, rear, "#94a3b8", 1.2, "3 3"))
    p.append(_dim_v(cx + 0.5 * k + 20, rear, rear + 0.25 * k, "≤ 0,25 m" if lang == "es" else "≤ 0.25 m"))
    p.append(txt(cx + 0.5 * k + 30, rear - 6, L(lang, "end of the bike", "fin de la moto"), 10, 700, SLATE))
    p.append(cross(cx + 0.5 * k + 40, cy - 70) + txt(cx + 0.5 * k + 56, cy - 66, L(lang, "front: nothing", "delante: nada"), 11.5, 800, RED))
    p.append(lines(516, 326, L(lang, ["Side: 0.50 m each side of the axis (1 m in total). No V-20 panel needed."],
                                     ["Lateral: 0,50 m a cada lado del eje (1 m en total). No hace falta panel V-20."]), 11, 700, TEAL, "middle", 14))
    return svg(720, 342, "".join(p), L(lang, "Carrying a load on a motorcycle", "La carga en la motocicleta"))


# ---------------------------------------------------------------- D2 the vehicle signs in your course
def _beacon(cx, cy, color, glow):
    return (f'<circle cx="{cx}" cy="{cy - 6}" r="24" fill="{glow}" opacity="0.35"/>'
            + f'<path d="M{cx - 16} {cy + 6} L{cx - 16} {cy - 10} Q{cx} {cy - 30} {cx + 16} {cy - 10} L{cx + 16} {cy + 6} Z" fill="{color}"/>'
            + rect(cx - 22, cy + 6, 44, 10, DARK, 3))


def _sign(kind, cx, cy, lang):
    if kind == "V-1":
        return (f'<ellipse cx="{cx}" cy="{cy}" rx="44" ry="20" fill="#93c5fd" opacity="0.4"/>' + rect(cx - 38, cy - 9, 76, 18, "#1e3a8a", 9)
                + rect(cx - 32, cy - 6, 26, 12, "#3b82f6", 5) + rect(cx + 6, cy - 6, 26, 12, "#3b82f6", 5))
    if kind == "V-2":
        return _beacon(cx, cy, "#f59e0b", "#fde68a")
    if kind == "V-16":
        return (f'<circle cx="{cx}" cy="{cy - 8}" r="22" fill="#fde68a" opacity="0.45"/>' + f'<ellipse cx="{cx}" cy="{cy + 8}" rx="24" ry="9" fill="{DARK}"/>'
                + rect(cx - 20, cy - 4, 40, 12, "#e5e7eb", 5) + f'<ellipse cx="{cx}" cy="{cy - 6}" rx="13" ry="6" fill="#f59e0b"/>')
    if kind == "V-19":
        return (rect(cx - 26, cy - 26, 52, 52, "#fef3c7", 3, f' stroke="{INK}" stroke-width="1.5"') + txt(cx, cy + 10, "27", 26, 900, INK, "middle")
                + rect(cx - 26, cy - 26, 12, 12, "#16a34a") + rect(cx + 14, cy + 14, 12, 12, "#dc2626"))
    if kind == "V-26":
        return (f'<circle cx="{cx}" cy="{cy}" r="27" fill="#1d4ed8"/>' + rect(cx - 15, cy + 2, 30, 12, "#fff", 4)
                + "".join(f'<circle cx="{cx + dx}" cy="{cy - 12}" r="4" fill="#fff"/>' + rect(cx + dx - 3, cy - 8, 6, 9, "#fff", 2) for dx in (-11, 0, 11)))
    if kind == "VEH":
        return (f'<path d="M{cx} {cy - 30} L{cx + 32} {cy + 24} L{cx - 32} {cy + 24} Z" fill="#facc15" stroke="{SIGN_RED}" stroke-width="5" stroke-linejoin="round"/>'
                + rect(cx - 18, cy - 2, 20, 16, INK, 2) + rect(cx + 2, cy + 3, 9, 11, INK, 2)
                + f'<circle cx="{cx + 16}" cy="{cy + 14}" r="4" fill="none" stroke="{SIGN_RED}" stroke-width="2"/>')
    return _plate(kind, cx, cy, lang)


def moto_plates(lang):
    items = L(lang,
              [("V-1", "Priority vehicle (blue)"), ("V-2", "Vehicle-obstacle (amber)"), ("V-6", "Long vehicle (&gt; 12 m)"), ("V-13", "Novice (&lt; 1 year)"), ("V-16", "Warning light"),
               ("V-19", "ITV badge"), ("V-20", "Load sticks out"), ("V-25", "Environmental label"), ("V-26", "Shared use"), ("VEH", "Blind-spot sticker")],
              [("V-1", "Prioritario (azul)"), ("V-2", "Vehículo-obstáculo (amarillo)"), ("V-6", "Vehículo largo (&gt; 12 m)"), ("V-13", "Novel (&lt; 1 año)"), ("V-16", "Preseñalización"),
               ("V-19", "Distintivo ITV"), ("V-20", "Carga que sobresale"), ("V-25", "Distintivo ambiental"), ("V-26", "Uso compartido"), ("VEH", "Ángulos muertos")])
    p = []
    for i, (code, name) in enumerate(items):
        cx = 72 + (i % 5) * 144
        cy = 52 + (i // 5) * 130
        p.append(_sign(code, cx, cy, lang))
        p.append(txt(cx, cy + 50, "VEH 21/05" if code == "VEH" else code, 12, 800, INK, "middle"))
        p.append(txt(cx, cy + 66, name, 11, 400, SLATE, "middle"))
    return svg(720, 270, "".join(p), L(lang, "The vehicle signs in your course", "Las señales en los vehículos de tu curso"))
