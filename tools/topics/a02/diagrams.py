# -*- coding: utf-8 -*-
"""Original SVG diagrams for Category A1/A2, Topic 2 (use of the road), EN/ES. No third-party artwork is used.
Two figures are shared with Category B, Topic 2; the two below are specific to this topic."""
import math

from svgkit import NAVY, TEAL, AMBER, RED, SLATE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect, car_v, car_h, tick, cross, ASPHALT, VERGE, WHITE
from ..b02.diagrams import lane_choice, distances  # noqa: F401  (shared with Topic B2)
from ..b09.diagrams import L, line, MUTED, LINE, CARD
from ..b10.diagrams import arrow, rot
from ..b12.diagrams import moto_v

MOTO = "#dc2626"


def _road_v(x0, x1, top, bot, centre="dash"):
    out = [rect(x0, top, x1 - x0, bot - top, ASPHALT), rect(x0 + 3, top, 3, bot - top, WHITE), rect(x1 - 6, top, 3, bot - top, WHITE)]
    cx = (x0 + x1) / 2
    if centre == "dash":
        out.append("".join(rect(cx - 1.5, y, 3, 16, WHITE) for y in range(int(top) + 6, int(bot), 30)))
    return "".join(out)


# ---------------------------------------------------------------- D1 which side of islands and roundabouts
def island_sides(lang):
    p = []
    titles = [L(lang, "Island between two directions", "Isleta entre dos sentidos"), L(lang, "Island on a one-way road", "Isleta en sentido único"),
              L(lang, "Roundabout", "Glorieta")]
    for i, t in enumerate(titles):
        ox = 8 + i * 238
        p.append(rect(ox, 8, 226, 330, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"') + txt(ox + 113, 32, t, 12.5, 800, INK, "middle"))
    # a) two-way road
    x0, x1 = 54, 176
    p.append(rect(18, 44, 206, 236, VERGE) + _road_v(x0, x1, 44, 280))
    p.append(rect(105, 132, 22, 64, "#e5e7eb", 11, ' stroke="#9ca3af"') + rect(108, 150, 16, 28, "#16a34a", 8))
    p.append(car_v(84, 112, "#64748b", up=False) + arrow(84, 140, 84, 250, "#fca5a5", 3, 9))
    p.append(moto_v(148, 246, MOTO) + arrow(148, 222, 148, 70, "#fde68a", 3, 10))
    p.append(tick(198, 108, 10))
    p.append(lines(121, 298, L(lang, ["Keep it on your left: pass on", "the right-hand part of the road"], ["Déjala a la izquierda: circula", "por la parte derecha"]), 11, 600, INK, "middle", 14))
    # b) one-way road
    o = 238
    x0, x1 = o + 54, o + 176
    p.append(rect(o + 18, 44, 206, 236, VERGE) + _road_v(x0, x1, 44, 280))
    p.append(rect(o + 105, 132, 22, 64, "#e5e7eb", 11, ' stroke="#9ca3af"') + rect(o + 108, 150, 16, 28, "#16a34a", 8))
    p.append(moto_v(o + 84, 246, MOTO) + arrow(o + 84, 222, o + 84, 70, "#fde68a", 3, 10))
    p.append(moto_v(o + 148, 246, MOTO) + arrow(o + 148, 222, o + 148, 70, "#fde68a", 3, 10))
    p.append(tick(o + 28, 108, 10) + tick(o + 198, 108, 10))
    p.append(lines(o + 121, 298, L(lang, ["Either side"], ["Por cualquiera de los dos lados"]), 11, 600, INK, "middle", 14))
    # c) roundabout
    o = 476
    cx, cy = o + 113, 150
    p.append(rect(o + 18, 44, 190, 236, VERGE))
    p.append(rect(cx - 22, 44, 44, 236, ASPHALT) + rect(o + 18, cy - 22, 190, 44, ASPHALT))
    p.append(f'<circle cx="{cx}" cy="{cy}" r="78" fill="{ASPHALT}"/><circle cx="{cx}" cy="{cy}" r="40" fill="#16a34a" stroke="#fff" stroke-width="2"/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="59" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="8 7"/>')
    # anticlockwise travel (centre on the left), motorcycle on the outer lane
    r = 69
    pts = []
    for k in range(0, 31):
        a = math.radians(100 - k * 8)
        pts.append(f"{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}")
    p.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#fde68a" stroke-width="3"/>')
    a_end = math.radians(100 - 30 * 8)
    ex, ey = cx + r * math.cos(a_end), cy + r * math.sin(a_end)
    a_prev = math.radians(100 - 29 * 8)
    px, py = cx + r * math.cos(a_prev), cy + r * math.sin(a_prev)
    p.append(arrow(px, py, ex, ey, "#fde68a", 3, 10))
    p.append(f'<g transform="translate({cx + r * math.cos(math.radians(100)):.1f} {cy + r * math.sin(math.radians(100)):.1f}) rotate(10)">{moto_v(0, 0, MOTO)}</g>')
    p.append(lines(o + 113, 298, L(lang, ["Centre on your left. Interurban:", "outer lane; urban: the lane for", "your exit"], ["Centro a la izquierda. Interurbana:", "carril exterior; urbana: el que", "convenga a tu destino"]), 10.5, 600, INK, "middle", 13.5))
    return svg(720, 346, "".join(p), L(lang, "Islands and roundabouts: which side", "Isletas y glorietas: por qué lado"))


# ---------------------------------------------------------------- D2 motorcycles on the hard shoulder in a jam
def moto_shoulder(lang):
    top, mid, edge, sh = 60, 122, 184, 226
    p = [rect(0, 0, 720, top, VERGE), rect(0, top, 720, edge - top, ASPHALT), rect(0, edge, 720, sh - edge, "#9ca3af"), rect(0, sh, 720, 40, VERGE)]
    p.append(rect(0, top + 3, 720, 3, WHITE) + rect(0, edge - 4, 720, 3, WHITE))
    p.append("".join(rect(x, mid - 1.5, 24, 3, WHITE) for x in range(0, 720, 44)))
    # stopped queue in both lanes
    for x in range(40, 700, 70):
        p.append(car_h(x, (top + mid) / 2 + 2, "#64748b") + car_h(x + 22, (mid + edge) / 2, "#94a3b8"))
    # motorcycles in single file on the shoulder
    for x in (210, 300):
        p.append(f'<g transform="translate({x} {(edge + sh) / 2}) rotate(90)">{moto_v(0, 0, MOTO)}</g>')
    p.append(arrow(330, (edge + sh) / 2, 400, (edge + sh) / 2, "#fff", 2.5, 9))
    p.append(rect(410, edge + 8, 70, 26, "#fff", 13, f' stroke="{RED}" stroke-width="3"') + txt(445, edge + 26, "≤ 30", 13, 900, INK, "middle"))
    # signed stretch bracket
    p.append(line(150, sh + 12, 640, sh + 12, NAVY, 2) + line(150, sh + 4, 150, sh + 20, NAVY, 2) + line(640, sh + 4, 640, sh + 20, NAVY, 2))
    p.append(txt(395, sh + 32, L(lang, "signed stretch (fixed signs and road markings)", "tramo señalizado (señales fijas y marcas viales)"), 11, 700, NAVY, "middle"))
    # forbidden: weaving between the lanes
    p.append(f'<g transform="translate(560 {mid}) rotate(90)">{moto_v(0, 0, "#6b7280")}</g>' + cross(560, mid - 26, 11))
    p.append(txt(560, 50, L(lang, "zigzagging between vehicles: prohibited", "zigzaguear entre vehículos: prohibido"), 11, 700, RED, "middle"))
    conds = [L(lang, "Only where signed", "Solo tramos señalizados"), L(lang, "Traffic stopped by congestion", "Tráfico detenido por congestión"),
             L(lang, "30 km/h at most", "Máximo 30 km/h"), L(lang, "Single file, extreme care", "En columna de a uno")]
    for i, c in enumerate(conds):
        x = 10 + i * 178
        p.append(rect(x, 290, 170, 34, "#eef2f7", 8) + txt(x + 85, 312, c, 11.5, 700, NAVY, "middle"))
    p.append(txt(360, 344, L(lang, "Don’t endanger the drivers who must use the shoulder; leave it if needed.", "No pongas en riesgo a quienes deben circular por el arcén; abandónalo si es preciso."), 11, 600, SLATE, "middle"))
    return svg(720, 354, "".join(p), L(lang, "Motorcycles on the hard shoulder in a traffic jam", "Motocicletas por el arcén en un atasco"))


# ---------------------------------------------------------------- D3 which lane on a motorcycle
def lanes_moto(lang):
    panels = [
        (2, "two", L(lang, ["Two-way,", "two lanes"], ["Doble sentido,", "dos carriles"]), L(lang, ["The right-hand lane"], ["El carril derecho"])),
        (3, "two", L(lang, ["Two-way, three lanes", "(broken lines)"], ["Doble sentido, tres", "carriles (discontinuas)"]), L(lang, ["Right lane; centre only to", "overtake or turn left"], ["Derecho; el central solo para", "adelantar o girar a la izq."])),
        (3, "out", L(lang, ["One-way,", "out of town"], ["Sentido único,", "fuera de poblado"]), L(lang, ["The rightmost lane; the", "others to overtake"], ["El de más a la derecha; el", "resto para adelantar"])),
        (3, "town", L(lang, ["One-way, in town,", "marked lanes"], ["Sentido único, en", "poblado, con marcas"]), L(lang, ["The lane that best suits", "your destination"], ["El que mejor convenga", "a tu destino"])),
    ]
    p = []
    for i, (n, kind, title, rule) in enumerate(panels):
        ox = 6 + i * 178
        p.append(rect(ox, 6, 170, 330, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"') + lines(ox + 85, 28, title, 11.5, 800, INK, "middle", 14))
        x0, x1 = ox + 26, ox + 144
        top, bot = 62, 262
        p.append(rect(x0, top, x1 - x0, bot - top, ASPHALT) + rect(x0 + 2, top, 3, bot - top, WHITE) + rect(x1 - 5, top, 3, bot - top, WHITE))
        w = (x1 - x0) / n
        for k in range(1, n):
            x = x0 + k * w
            p.append("".join(rect(x - 1.5, y, 3, 14, WHITE) for y in range(top + 6, bot, 26)))
        lane = lambda k: x0 + w * (k + 0.5)  # noqa: E731
        if kind == "two":
            p.append(car_v(lane(0), 100, "#64748b", up=False) + arrow(lane(0), 128, lane(0), 168, "#fff", 2, 7))
            p.append(moto_v(lane(n - 1), 226, MOTO) + arrow(lane(n - 1), 204, lane(n - 1), 150, "#fde68a", 2.5, 8))
            if n == 3:
                p.append(f'<path d="M{lane(2)} 200 C {lane(2)} 180 {lane(1)} 180 {lane(1)} 150" fill="none" stroke="#fde68a" stroke-width="2" stroke-dasharray="5 4"/>')
                p.append(cross(lane(0), 222, 9))
            p.append(tick(x1 + 12, 226, 9))
        elif kind == "out":
            for k in range(n):
                p.append(arrow(lane(k), bot - 8, lane(k), bot - 30, "#fff", 2, 7))
            p.append(moto_v(lane(n - 1), 190, MOTO) + tick(x1 + 12, 190, 9))
            p.append(car_v(lane(1), 120, "#94a3b8"))
        else:
            for k in range(n):
                p.append(arrow(lane(k), bot - 8, lane(k), bot - 30, "#fff", 2, 7))
            p.append(moto_v(lane(0), 170, MOTO) + f'<path d="M{lane(0)} 152 L{lane(0)} 120 L{lane(0) - 16} 120" fill="none" stroke="#fde68a" stroke-width="2.5"/>')
            p.append(moto_v(lane(2), 200, MOTO) + f'<path d="M{lane(2)} 182 L{lane(2)} 110" fill="none" stroke="#fde68a" stroke-width="2.5"/>')
            p.append(tick(x1 + 12, 150, 9))
        p.append(lines(ox + 85, 290, rule, 11, 600, INK, "middle", 14))
    p.append(txt(360, 354, L(lang, "Autopistas and autovías through urban land: rightmost lane, the rest to overtake. Never on pavements.",
                              "Autopistas y autovías por suelo urbano: el de más a la derecha y el resto para adelantar. Nunca por aceras."), 11, 600, SLATE, "middle"))
    return svg(720, 364, "".join(p), L(lang, "Which lane to use on a motorcycle", "Qué carril usar en moto"))
