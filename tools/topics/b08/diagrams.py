# -*- coding: utf-8 -*-
"""Original SVG figures for Topic 8 (EN/ES). No third-party artwork is used. Each function takes the language
("en" or "es") and returns an SVG string. The small sign icons used in the tables live in signs.py."""
import re

from svgkit import NAVY, TEAL, RED, SLATE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect, car_v, tick, cross, ASPHALT, VERGE, WHITE  # noqa: F401
from .signs import ICON

MUTED = "#64748b"
LINE = "#cbd5e1"
CARD = "#f8fafc"
VEST = "#d9f99d"


def L(lang, en, es):
    return en if lang == "en" else es


def emb(code, x, y, w):
    """Place one of the table icons inside a figure."""
    s = ICON[code]
    m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', s)
    vw, vh = float(m.group(1)), float(m.group(2))
    inner = s[s.index(">") + 1: s.rindex("</svg>")]
    return f'<svg x="{x}" y="{y}" width="{w}" height="{w * vh / vw:.1f}" viewBox="0 0 {vw:g} {vh:g}">{inner}</svg>'


def line(x1, y1, x2, y2, color=INK, width=2, dash=None, cap="round"):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" stroke-linecap="{cap}"{d}/>'


def path(d, color=INK, width=2.5, fill="none", dash=None):
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"{ds}/>'


def ahead(x, y, dx, dy, color, s=7):
    """Arrow head at (x, y) pointing along (dx, dy) (unit-ish)."""
    import math
    L_ = math.hypot(dx, dy) or 1
    ux, uy = dx / L_, dy / L_
    bx, by = x - ux * s * 1.4, y - uy * s * 1.4
    return f'<path d="M{x:.1f} {y:.1f} L{bx - uy * s:.1f} {by + ux * s:.1f} L{bx + uy * s:.1f} {by - ux * s:.1f} Z" fill="{color}"/>'


# ---------------------------------------------------------------- D1 order of priority between signals
def agent_icon(x, y, s=1.0):
    g = (f'<circle cx="0" cy="-30" r="6" fill="#f1c27d"/><rect x="-7" y="-39" width="14" height="5" rx="2" fill="#1e3a8a"/>'
         f'<rect x="-8" y="-23" width="16" height="24" rx="4" fill="{VEST}" stroke="#65a30d" stroke-width="1.2"/>'
         f'<line x1="-4" y1="1" x2="-5" y2="22" stroke="#1e3a8a" stroke-width="5" stroke-linecap="round"/>'
         f'<line x1="4" y1="1" x2="5" y2="22" stroke="#1e3a8a" stroke-width="5" stroke-linecap="round"/>'
         f'<line x1="7" y1="-20" x2="9" y2="-48" stroke="{VEST}" stroke-width="4.5" stroke-linecap="round"/>'
         f'<line x1="-7" y1="-20" x2="-11" y2="0" stroke="{VEST}" stroke-width="4.5" stroke-linecap="round"/>')
    return f'<g transform="translate({x} {y}) scale({s})">{g}</g>'


def priority_order(lang):
    names = L(lang, [["Agents"], ["Temporary signs", "and beaconing"], ["Traffic lights"], ["Vertical signs"], ["Road markings"]],
              [["Agentes"], ["Señalización", "circunstancial y", "balizamiento"], ["Semáforos"], ["Señales verticales"], ["Marcas viales"]])
    p = []
    for i in range(5):
        x = 8 + i * 142
        p.append(rect(x, 10, 126, 176, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'))
        p.append(f'<circle cx="{x + 22}" cy="32" r="14" fill="{NAVY}"/>' + txt(x + 22, 37, f"{i + 1}º", 12, 700, "#fff", "middle"))
        icon = [agent_icon(x + 63, 96, 1.1), emb("dev-panel", x + 30, 50, 56) + emb("dev-cones", x + 58, 66, 44),
                emb("tl-red", x + 38, 52, 54), emb("R-2", x + 36, 52, 56), emb("mk-yield-tri", x + 22, 60, 84)][i]
        p.append(icon)
        p.append(lines(x + 63, 136 + (0 if len(names[i]) < 3 else -6), names[i], 12, 700, INK, "middle", 14))
        if i < 4:
            p.append(f'<path d="M{x + 129} 92 L{x + 139} 98 L{x + 129} 104 Z" fill="{MUTED}"/>')
    p.append(txt(360, 204, L(lang, "Higher first: obey the first that applies, even against a later one",
                             "Primero el de más arriba: se obedece el primero que exista, aunque contradiga a uno posterior"), 11.5, 600, MUTED, "middle"))
    return svg(720, 212, "".join(p), L(lang, "Order of priority between kinds of signal", "Orden de prioridad entre tipos de señales"))


# ---------------------------------------------------------------- D2 which sign applies to you, by its side
def _junction(ox, signs, apply, lang):
    """One T-junction panel. signs: list of (side, code). apply: dict move -> code or None."""
    cx = ox + 115
    p = [rect(ox, 20, 230, 200, VERGE, 10), rect(ox, 46, 230, 56, ASPHALT), rect(cx - 30, 46, 60, 174, ASPHALT)]
    p.append(line(ox, 74, cx - 30, 74, WHITE, 2, "10 8") + line(cx + 30, 74, ox + 230, 74, WHITE, 2, "10 8"))
    p.append(line(cx, 102, cx, 220, WHITE, 2, "10 8") + line(cx, 108, cx + 30, 108, WHITE, 3, cap="butt"))
    for side, code in signs:
        sx = cx + 34 if side == "right" else cx - 58
        p.append(line(sx + 13, 128, sx + 13, 146, "#475569", 3) + emb(code, sx, 104, 27))
    p.append(car_v(cx + 15, 190, "#1d4ed8"))
    cols = {}
    for mv, code in apply.items():
        cols[mv] = NAVY if code else "#94a3b8"
    # straight
    p.append(path(f"M{cx + 15} 168 L{cx + 15} 36", cols["straight"], 3, dash=None if apply["straight"] else "6 5") + ahead(cx + 15, 30, 0, -1, cols["straight"], 5))
    # left turn
    p.append(path(f"M{cx + 15} 166 L{cx + 15} 112 Q{cx + 15} 60 {cx - 40} 60 L{ox + 18} 60", cols["left"], 3, dash=None if apply["left"] else "6 5") + ahead(ox + 12, 60, -1, 0, cols["left"], 5))
    # right turn
    p.append(path(f"M{cx + 15} 166 L{cx + 15} 120 Q{cx + 15} 90 {cx + 50} 90 L{ox + 212} 90", cols["right"], 3, dash=None if apply["right"] else "6 5") + ahead(ox + 218, 90, 1, 0, cols["right"], 5))
    # which sign governs each move
    for mv, (tx, ty) in {"straight": (cx + 24, 22), "left": (ox + 8, 22), "right": (ox + 198, 106)}.items():
        code = apply[mv]
        p.append(rect(tx - 3, ty - 3, 26, 26, "#fff", 6, f' stroke="{NAVY if code else "#94a3b8"}" stroke-width="1.5"'))
        p.append(emb(code, tx, ty, 20) if code else txt(tx + 10, ty + 15, "—", 14, 700, "#94a3b8", "middle"))
    return "".join(p)


def sign_sides(lang):
    p = [_junction(4, [("right", "R-2")], {"straight": "R-2", "left": "R-2", "right": "R-2"}, lang),
         _junction(245, [("left", "R-2")], {"straight": "R-2", "left": "R-2", "right": None}, lang),
         _junction(486, [("left", "R-2"), ("right", "R-1")], {"straight": "R-2", "left": "R-2", "right": "R-1"}, lang)]
    caps = L(lang, [["Sign on the right:", "everyone obeys it"], ["Sign on the left only:", "straight on and left turns"], ["Different signs: left one for", "straight on and left,", "right one for turning right"]],
             [["Señal a la derecha:", "la obedecen todos"], ["Señal solo a la izquierda:", "de frente y giro a la izquierda"], ["Señales distintas: la izquierda,", "de frente y giro a la izquierda;", "la derecha, giro a la derecha"]])
    for i, c in enumerate(caps):
        p.append(lines(119 + i * 241, 240, c, 12, 700, INK, "middle", 15))
    p.append(txt(360, 298, L(lang, "Label at each arrow = the sign that governs that move; grey dashed = that sign does not affect it.",
                             "La etiqueta de cada flecha es la señal que rige ese movimiento; gris discontinuo = esa señal no le afecta."), 11.5, 400, MUTED, "middle"))
    return svg(720, 306, "".join(p), L(lang, "Which sign applies to you, by its side of the road", "Qué señal te afecta según el lado en que está"))


# ---------------------------------------------------------------- D3 agents' arm signals
def officer(x, y, arms, extra=""):
    """Front view of a traffic officer. arms: list of (x2, y2) hand points relative to the shoulders."""
    p = [f'<circle cx="{x}" cy="{y - 58}" r="9" fill="#f1c27d"/>', rect(x - 10, y - 71, 20, 6, "#1e3a8a", 2), rect(x - 13, y - 66, 26, 3, "#1e3a8a", 1),
         rect(x - 14, y - 47, 28, 40, VEST, 6, ' stroke="#65a30d" stroke-width="1.4"'), rect(x - 14, y - 30, 28, 4, "#e2e8f0"),
         line(x - 6, y - 8, x - 8, y + 30, "#1e3a8a", 8), line(x + 6, y - 8, x + 8, y + 30, "#1e3a8a", 8)]
    for sx, (hx, hy) in zip((-12, 12), arms):
        p.append(line(x + sx, y - 42, x + hx, y + hy, VEST, 7))
        p.append(f'<circle cx="{x + hx}" cy="{y + hy}" r="4" fill="#f1c27d"/>')
    return "".join(p) + extra


def agent_arms(lang):
    p = []
    for i in range(4):
        p.append(rect(4 + i * 179, 6, 173, 270, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'))
    # a. arm raised vertically
    p.append(officer(90, 150, [(-22, -8), (14, -112)]))
    # b. plan view: arms along the E-W axis
    bx, by = 269, 112
    p.append(rect(bx - 80, by - 22, 160, 44, ASPHALT) + rect(bx - 22, by - 92, 44, 184, ASPHALT))
    p.append(f'<circle cx="{bx}" cy="{by}" r="8" fill="{VEST}" stroke="#65a30d" stroke-width="1.5"/>' + line(bx - 26, by, bx + 26, by, VEST, 5))
    p.append(car_v(bx + 11, by + 66, "#1d4ed8") + car_v(bx - 11, by - 66, "#b45309", up=False))
    p.append(f'<g transform="rotate(90 {bx - 62} {by + 10})">{car_v(bx - 62, by + 10, "#0f766e", up=False)}</g>')
    p.append(cross(bx + 34, by + 66, 9) + cross(bx - 34, by - 66, 9) + tick(bx - 62, by - 12, 9))
    # c. swinging red or amber light
    p.append(officer(448, 150, [(-22, -8), (34, -40)]))
    p.append(f'<circle cx="485" cy="104" r="7" fill="#ef4444"/><circle cx="485" cy="104" r="13" fill="#ef4444" opacity=".25"/>')
    p.append(path("M470 78 Q490 66 506 82", "#f59e0b", 3) + ahead(508, 85, 0.5, 1, "#f59e0b", 5))
    # d. arm extended moving up and down
    p.append(officer(612, 150, [(-22, -8), (52, -46)]))
    p.append(path("M670 70 L670 128", "#f59e0b", 3) + ahead(670, 64, 0, -1, "#f59e0b", 5) + ahead(670, 134, 0, 1, "#f59e0b", 5))
    caps = L(lang, [
        ["Arm raised vertically", "STOP: everyone coming", "towards the agent"],
        ["Arm(s) out sideways", "STOP: traffic crossing", "the line of the arms"],
        ["Swinging red/amber light", "STOP: the users the", "light is aimed at"],
        ["Arm out, moving up/down", "SLOW DOWN: drivers who", "come at right angles to it"]],
        [
        ["Brazo levantado vertical", "DETENERSE: todos los que", "se acerquen al agente"],
        ["Brazo(s) extendido(s)", "DETENERSE: los que corten", "la dirección de los brazos"],
        ["Balanceo de luz roja/amarilla", "DETENERSE: aquellos a", "quienes se dirija la luz"],
        ["Brazo extendido arriba/abajo", "REDUCIR: los que se acerquen", "perpendiculares al brazo"]])
    for i, c in enumerate(caps):
        cx = 90 + i * 179
        p.append(txt(cx, 222, c[0], 12, 700, NAVY, "middle") + lines(cx, 240, c[1:], 11.5, 600, INK, "middle", 15))
    return svg(720, 282, "".join(p), L(lang, "Agents' arm signals", "Señales de los agentes con los brazos"))


# ---------------------------------------------------------------- D4 colours of exit signs on a motorway
def _panel(x, y, w, h, fill, rows, fg=None):
    fg = fg or ("#fff" if fill != "#fff" else INK)
    st = ' stroke="#111" stroke-width="1.5"' if fill == "#fff" else ' stroke="#fff" stroke-width="2"'
    out = [rect(x, y, w, h, fill, 6, st)]
    for (s, size, anchor, dx, dy) in rows:
        tx = x + (w / 2 if anchor == "middle" else dx)
        out.append(txt(tx, y + dy, s, size, 700, fg, anchor))
    return "".join(out)


def exit_glyph(x, y, color):
    """Simplified 'exit' pictogram: a road with a branch peeling off to the right."""
    return (line(x, y + 14, x, y, color, 3, cap="butt") + line(x + 5, y + 14, x + 12, y + 2, color, 3, cap="butt")
            + ahead(x + 14, y - 1, 0.6, -1, color, 3.5))


def darrow(x, y, dx, dy, color, size=12):
    """Small drawn arrow from (x, y) along (dx, dy)."""
    return line(x, y, x + dx * size * 0.7, y + dy * size * 0.7, color, 2.6, cap="butt") + ahead(x + dx * size, y + dy * size, dx, dy, color, 3.6)


def exit_colours(lang):
    BLUE = "#1447c8"
    p = []
    heads = L(lang, ["Exit to a motorway or autovía", "Exit to a conventional road"], ["Salida hacia autopista o autovía", "Salida hacia carretera convencional"])
    for col, to_conv in enumerate((False, True)):
        ox = 6 + col * 362
        p.append(rect(ox, 6, 348, 262, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'))
        p.append(txt(ox + 174, 28, heads[col], 13, 700, NAVY, "middle"))
        rows = L(lang, [("At the exit: immediate exit sign", False), ("About 500 m before: pre-signposting", True)],
                 [("En la salida: cartel de salida inmediata", False), ("Unos 500 m antes: preseñalización", True)])
        for r, (label, presig) in enumerate(rows):
            y = 50 + r * 108
            p.append(txt(ox + 14, y, label, 11.5, 700, INK))
            p.append(_panel(ox + 14, y + 8, 132, 76, BLUE, [("A-6", 11, "middle", 0, 22), ("A Coruña", 15, "middle", 0, 46)]))
            p.append(darrow(ox + 44, y + 64, 0, 1, "#fff", 12) + darrow(ox + 116, y + 64, 0, 1, "#fff", 12))
            fill = "#fff" if (to_conv and not presig) else BLUE
            fg = INK if fill == "#fff" else "#fff"
            p.append(_panel(ox + 154, y + 8, 180, 30, fill, [("20", 14, "start", 140, 21)] + ([("500 m", 13, "start", 12, 21)] if presig else [])))
            p.append(exit_glyph(ox + 154 + (96 if presig else 60), y + 15, fg))
            p.append(_panel(ox + 154, y + 42, 180, 42, fill, [("Las Rozas", 16, "start", 22, 28)]))
            p.append(darrow(ox + 154 + 140, y + 52, 0.7, 0.7, fg, 18))
    p.append(txt(360, 288, L(lang, "Confirmation signs: colour of the road you are on · Pre-signposting: colour of the road the exit leads to, except a lower-category road",
                             "Confirmación: color de la vía por la que circulas · Preseñalización: color de la vía de destino, salvo si es de inferior categoría"), 11, 600, MUTED, "middle"))
    p.append(txt(360, 304, L(lang, "Immediate exit sign: always the colour of the road the exit leads to",
                             "Cartel de salida inmediata: siempre del color de la vía hacia la que se dirige la salida"), 11, 600, MUTED, "middle"))
    return svg(720, 312, "".join(p), L(lang, "Colours of exit signs on a motorway", "Colores de los carteles de salida en autopista"))
