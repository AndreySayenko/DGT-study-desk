# -*- coding: utf-8 -*-
"""Original SVG diagrams for Topic 4 (EN/ES). No third-party artwork is used. Each function takes the language
("en" or "es") and returns an SVG string. Figures sit on a light background in both themes. Road signs are drawn
in simplified form from their official shapes and colours."""

from svgkit import NAVY, TEAL, RED, SLATE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect, car_v, car_h, arrow_v, arrow_h, tick, cross, ASPHALT, VERGE, WHITE  # noqa: F401
from ..b02.diagrams import corridor  # noqa: F401  (reused in section 5)

SIGN_RED = "#c81e1e"
SIGN_BLUE = "#1d4ed8"
DIRT = "#c8a26b"
WATER = "#60a5fa"
GRID_YELLOW = "#facc15"
MUTED = "#64748b"


def L(lang, en, es):
    return en if lang == "en" else es


def line(x1, y1, x2, y2, color=WHITE, width=2, dash=None, extra=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{d}{extra}/>'


def badge(cx, cy, s, fill=NAVY):
    return f'<circle cx="{cx}" cy="{cy}" r="12" fill="{fill}"/>' + txt(cx, cy + 4.5, s, 12, 800, "#fff", "middle")


# ---------------------------------------------------------------- simplified signs
def traffic_light(cx, cy, lit):
    cols = {"red": "#ef4444", "amber": "#f59e0b", "green": "#22c55e"}
    out = [rect(cx - 15, cy - 40, 30, 80, "#1f2937", 7)]
    for i, name in enumerate(("red", "amber", "green")):
        out.append(f'<circle cx="{cx}" cy="{cy - 25 + i * 25}" r="9.5" fill="{cols[name] if name == lit else "#374151"}"/>')
    return "".join(out)


def warn_triangle(cx, cy, kind):
    """Danger sign with a junction symbol: thick bar = the road you are on (with priority)."""
    out = [f'<path d="M{cx} {cy - 36} L{cx + 40} {cy + 32} L{cx - 40} {cy + 32} Z" fill="#fff" stroke="{SIGN_RED}" stroke-width="7" stroke-linejoin="round"/>',
           rect(cx - 4.5, cy - 14, 9, 40, INK)]
    if kind == "cross":
        out.append(rect(cx - 18, cy + 4, 36, 4, INK))
    elif kind == "right":
        out.append(rect(cx, cy + 4, 18, 4, INK))
    elif kind == "merge":
        out.append(line(cx + 17, cy + 25, cx + 3, cy + 7, INK, 4))
    return "".join(out)


def give_way(cx, cy):
    return f'<path d="M{cx - 40} {cy - 32} L{cx + 40} {cy - 32} L{cx} {cy + 36} Z" fill="#fff" stroke="{SIGN_RED}" stroke-width="8" stroke-linejoin="round"/>'


def stop_sign(cx, cy, r=36):
    import math
    pts = " ".join(f"{cx + r * math.cos(math.radians(22.5 + 45 * k)):.1f},{cy + r * math.sin(math.radians(22.5 + 45 * k)):.1f}" for k in range(8))
    pts2 = " ".join(f"{cx + (r - 4) * math.cos(math.radians(22.5 + 45 * k)):.1f},{cy + (r - 4) * math.sin(math.radians(22.5 + 45 * k)):.1f}" for k in range(8))
    return (f'<polygon points="{pts}" fill="{SIGN_RED}"/><polygon points="{pts2}" fill="none" stroke="#fff" stroke-width="1.5"/>'
            + txt(cx, cy + 7, "STOP", 19, 800, "#fff", "middle"))


def priority_road(cx, cy):
    return (f'<path d="M{cx} {cy - 36} L{cx + 36} {cy} L{cx} {cy + 36} L{cx - 36} {cy} Z" fill="#fff" stroke="{INK}" stroke-width="1.5"/>'
            f'<path d="M{cx} {cy - 25} L{cx + 25} {cy} L{cx} {cy + 25} L{cx - 25} {cy} Z" fill="{GRID_YELLOW}"/>')


def roundabout_ahead(cx, cy):
    out = [rect(cx - 48, cy - 32, 96, 64, "#fff", 6, f' stroke="{INK}" stroke-width="2"'),
           f'<circle cx="{cx}" cy="{cy - 2}" r="11" fill="none" stroke="{INK}" stroke-width="4"/>',
           line(cx, cy + 28, cx, cy + 9, INK, 4)]
    for x2, y2, x1, y1 in ((cx - 36, cy - 2, cx - 11, cy - 2), (cx + 36, cy - 2, cx + 11, cy - 2), (cx, cy - 27, cx, cy - 13)):
        out.append(line(x1, y1, x2, y2, INK, 3))
    return "".join(out)


def r6(cx, cy, s=30):
    """Priority over oncoming traffic: blue square, small red arrow down, large white arrow up."""
    return (rect(cx - s, cy - s, 2 * s, 2 * s, SIGN_BLUE, 4, ' stroke="#fff" stroke-width="2"') +
            line(cx - s * 0.35, cy - s * 0.55, cx - s * 0.35, cy + s * 0.35, SIGN_RED, s * 0.16) +
            f'<path d="M{cx - s * 0.6} {cy + s * 0.3} L{cx - s * 0.35} {cy + s * 0.65} L{cx - s * 0.1} {cy + s * 0.3} Z" fill="{SIGN_RED}"/>' +
            line(cx + s * 0.35, cy + s * 0.6, cx + s * 0.35, cy - s * 0.3, "#fff", s * 0.18) +
            f'<path d="M{cx + s * 0.07} {cy - s * 0.25} L{cx + s * 0.35} {cy - s * 0.65} L{cx + s * 0.63} {cy - s * 0.25} Z" fill="#fff"/>')


def r5(cx, cy, r=30):
    """Give way to oncoming traffic: red ring, black arrow down, red arrow up."""
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{SIGN_RED}"/><circle cx="{cx}" cy="{cy}" r="{r * 0.78}" fill="#fff"/>' +
            line(cx - r * 0.3, cy - r * 0.5, cx - r * 0.3, cy + r * 0.3, INK, r * 0.15) +
            f'<path d="M{cx - r * 0.52} {cy + r * 0.22} L{cx - r * 0.3} {cy + r * 0.55} L{cx - r * 0.08} {cy + r * 0.22} Z" fill="{INK}"/>' +
            line(cx + r * 0.3, cy + r * 0.5, cx + r * 0.3, cy - r * 0.3, SIGN_RED, r * 0.15) +
            f'<path d="M{cx + r * 0.08} {cy - r * 0.22} L{cx + r * 0.3} {cy - r * 0.55} L{cx + r * 0.52} {cy - r * 0.22} Z" fill="{SIGN_RED}"/>')


# ---------------------------------------------------------------- D1 signs that give or take away priority
def priority_signs(lang):
    xs = [72, 216, 360, 504, 648]
    p = []
    p.append(txt(360, 16, L(lang, "These give you priority", "Te dan prioridad"), 13, 700, "#0b7548", "middle"))
    row1 = [traffic_light(xs[0], 64, "green"), warn_triangle(xs[1], 66, "cross"), warn_triangle(xs[2], 66, "right"),
            warn_triangle(xs[3], 66, "merge"), priority_road(xs[4], 66)]
    cap1 = L(lang, ["Green light", "P-1 crossroads", "P-1a side road", "P-1c road joining", "R-3 priority road"],
             ["Luz verde", "P-1 intersección", "P-1a vía lateral", "P-1c incorporación", "R-3 calzada prioritaria"])
    p.append(txt(360, 148, L(lang, "These take it away", "Te la quitan"), 13, 700, "#b42318", "middle"))
    row2 = [traffic_light(xs[0], 196, "red"), traffic_light(xs[1], 196, "amber"), stop_sign(xs[2], 198), give_way(xs[3], 198),
            roundabout_ahead(xs[4], 198)]
    cap2 = L(lang, ["Red light", "Amber light", "R-2 STOP", "R-1 give way", "Roundabout ahead"],
             ["Luz roja", "Luz ámbar", "R-2 STOP", "R-1 ceda el paso", "Glorieta próxima"])
    for i in range(5):
        p.append(row1[i])
        p.append(txt(xs[i], 122, cap1[i], 11, 600, INK, "middle"))
        p.append(row2[i])
        p.append(txt(xs[i], 254, cap2[i], 11, 600, INK, "middle"))
    return svg(720, 264, "".join(p), L(lang, "Signs that give or take away priority", "Señales que dan o quitan la prioridad"))


# ---------------------------------------------------------------- D2 unsigned junctions
def _cross_roads(ox, cx, cy, half=32, vertical_dirt=False, only_south=False):
    """Crossroads (or a T with the side road to the south) centred at (cx, cy) inside a 340-wide panel at ox."""
    out = [rect(ox, 30, 340, 270, VERGE, 8)]
    out.append(rect(ox, cy - half, 340, 2 * half, ASPHALT))
    vy1 = cy + half if only_south else 30
    out.append(rect(cx - half, vy1, 2 * half, 300 - vy1, DIRT if vertical_dirt else ASPHALT))
    if vertical_dirt:
        for k in range(8):
            out.append(f'<circle cx="{cx - 20 + (k % 3) * 18}" cy="{cy + half + 14 + k * 11}" r="1.6" fill="#8b6b3d"/>')
    out.append(line(ox + 6, cy, cx - half - 4, cy, WHITE, 2, "12 9"))
    out.append(line(cx + half + 4, cy, ox + 334, cy, WHITE, 2, "12 9"))
    if not vertical_dirt:
        if not only_south:
            out.append(line(cx, 34, cx, cy - half - 4, WHITE, 2, "12 9"))
        out.append(line(cx, cy + half + 4, cx, 296, WHITE, 2, "12 9"))
    return "".join(out)


def right_rule(lang):
    p = []
    # panel A: no signs, chain of "car on my right"
    ox, cx, cy = 10, 180, 160
    p.append(txt(ox + 170, 20, L(lang, "No signs: give way to the right", "Sin señales: cede a la derecha"), 13, 700, INK, "middle"))
    p.append(_cross_roads(ox, cx, cy))
    p.append(car_v(cx + 16, 258, "#1d4ed8", up=True) + arrow_v(cx + 16, 232, 204, WHITE))
    p.append(car_h(70, cy + 16, "#b45309", right=True) + arrow_h(96, 126, cy + 16, WHITE))
    p.append(car_v(cx - 16, 64, "#0f766e", up=False) + arrow_v(cx - 16, 90, 116, WHITE))
    p.append(badge(cx + 46, 258, "1"))
    p.append(badge(70, cy + 46, "2"))
    p.append(badge(cx - 46, 64, "3"))
    p.append(lines(ox + 10, 322, L(lang, ["1 has nobody on its right, so it goes first;", "2 has 1 on its right; 3 has 2 on its right"],
                                     ["1 no tiene a nadie a su derecha y pasa primero;", "2 tiene a 1 a su derecha; 3 tiene a 2 a su derecha"]), 11.5, 400, INK, "start", 15))
    # panel B: paved road beats unpaved road
    ox, cx = 370, 560
    p.append(txt(ox + 170, 20, L(lang, "Exception: paved beats unpaved", "Excepción: pavimentada antes que tierra"), 13, 700, INK, "middle"))
    p.append(_cross_roads(ox, cx, cy, vertical_dirt=True, only_south=True))
    p.append(car_h(450, cy + 16, "#1d4ed8", right=True) + arrow_h(476, 506, cy + 16, WHITE))
    p.append(car_v(cx + 16, 262, "#7c3aed", up=True) + arrow_v(cx + 16, 236, 210, WHITE))
    p.append(badge(450, cy + 46, "1"))
    p.append(badge(cx + 46, 262, "2"))
    p.append(lines(ox + 10, 322, L(lang, ["2 comes from the right, but on an unpaved road:", "the car on the paved road goes first"],
                                     ["2 viene por la derecha, pero por un camino sin pavimentar:", "pasa primero el de la vía pavimentada"]), 11.5, 400, INK, "start", 15))
    return svg(720, 346, "".join(p), L(lang, "Priority at junctions without signs", "Prioridad en intersecciones sin señalizar"))


# ---------------------------------------------------------------- D3 do not block the junction
def blocking_box(lang):
    p = [rect(0, 60, 720, 150, VERGE, 8)]
    top, bot = 100, 164
    vx1, vx2 = 340, 404
    p.append(rect(0, top, 720, bot - top, ASPHALT))
    p.append(rect(vx1, 60, vx2 - vx1, 150, ASPHALT))
    # yellow box grid
    grid = []
    for k in range(-4, 9):
        x = vx1 + k * 16
        grid.append(line(x, top, x + 64, bot, GRID_YELLOW, 2))
        grid.append(line(x + 64, top, x, bot, GRID_YELLOW, 2))
    cid = f"t4box-{lang}"   # one id per language: both language versions sit on the same page
    p.append(f'<clipPath id="{cid}"><rect x="{vx1}" y="{top}" width="{vx2 - vx1}" height="{bot - top}"/></clipPath><g clip-path="url(#{cid})">' + "".join(grid) + "</g>")
    p.append(f'<rect x="{vx1}" y="{top}" width="{vx2 - vx1}" height="{bot - top}" fill="none" stroke="{GRID_YELLOW}" stroke-width="2.5"/>')
    p.append(line(6, 132, vx1 - 22, 132, WHITE, 2, "12 9"))
    p.append(line(vx2 + 4, 132, 714, 132, WHITE, 2, "12 9"))
    p.append(line(vx1 - 12, 134, vx1 - 12, bot, WHITE, 4))   # stop line
    # queue after the junction
    for x in (432, 478, 524, 570, 616, 662, 708):
        p.append(car_h(x, 148, "#94a3b8", right=True))
    # our car waits
    p.append(car_h(vx1 - 40, 148, "#1d4ed8", right=True))
    # ghost car inside the box
    p.append(f'<rect x="{372 - 20}" y="{148 - 10}" width="40" height="20" rx="6" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="4 3"/>')
    # cross traffic
    p.append(car_v(388, 190, "#0f766e", up=True))
    p.append(arrow_v(388, 168, 112, "#ffffff", 2))
    # traffic light
    p.append(rect(vx1 - 30, 66, 12, 30, "#1f2937", 3) + f'<circle cx="{vx1 - 24}" cy="{89}" r="4" fill="#22c55e"/>' +
             f'<circle cx="{vx1 - 24}" cy="{80}" r="4" fill="#374151"/><circle cx="{vx1 - 24}" cy="{71}" r="4" fill="#374151"/>')
    # labels
    p.append(tick(22, 30) + txt(40, 35, L(lang, "Green, but the exit is full: wait before the line", "En verde, pero la salida está llena: espera antes de la línea"), 12, 700, INK))
    p.append(line(150, 42, vx1 - 48, 136, MUTED, 1.2, "4 3"))
    p.append(cross(470, 30) + txt(488, 35, L(lang, "Never stop inside the box", "No te quedes dentro del cuadro"), 12, 700, INK))
    p.append(line(486, 42, 380, 138, MUTED, 1.2, "4 3"))
    p.append(lines(360, 232, L(lang, ["Already stuck inside when your light turns red? Leave the junction without waiting,",
                                       "as long as you do not hinder those who now have a green light."],
                                ["¿Te has quedado dentro y tu semáforo se pone rojo? Sal de la intersección sin esperar,",
                                 "siempre que no entorpezcas a quienes ahora tienen verde."]), 12, 400, INK, "middle", 16))
    return svg(720, 262, "".join(p), L(lang, "Do not enter a junction you may block", "No entrar en una intersección que puedas bloquear"))


# ---------------------------------------------------------------- D4 turning: pedestrians, cyclists and animals go first
def bike(cx, cy, color="#7c3aed"):
    """Cyclist seen from above, travelling right."""
    return (rect(cx - 14, cy - 2.5, 28, 5, "#111827", 2) + f'<circle cx="{cx}" cy="{cy}" r="6" fill="{color}"/>'
            + f'<circle cx="{cx + 2}" cy="{cy}" r="3" fill="#fde68a"/>')


def walker(cx, cy, color=TEAL):
    return f'<circle cx="{cx}" cy="{cy}" r="7" fill="{color}"/><circle cx="{cx}" cy="{cy}" r="3.2" fill="#fde68a"/>'


def vulnerable_turn(lang):
    p = [rect(0, 20, 420, 270, VERGE, 8)]
    top, bot = 60, 124
    sx1, sx2 = 250, 314
    p.append(rect(0, top, 420, bot - top, ASPHALT))
    p.append(rect(sx1, bot, sx2 - sx1, 290 - bot, ASPHALT))
    p.append(rect(0, bot, sx1, 8, "#d6d3d1") + rect(sx2, bot, 420 - sx2, 8, "#d6d3d1"))     # pavements
    p.append(line(6, 92, 414, 92, WHITE, 2, "12 9"))
    p.append(line(282, bot + 30, 282, 286, WHITE, 2, "12 9"))
    # car turning right into the side road
    p.append(car_h(150, 108, "#1d4ed8", right=True))
    p.append(f'<path d="M176 108 Q 266 108 266 160" fill="none" stroke="#fff" stroke-width="2.5" stroke-dasharray="6 4"/>')
    p.append(f'<path d="M260 152 L266 164 L272 152 Z" fill="#fff"/>')
    # cyclist going straight on, close to the car
    p.append(bike(206, 119))
    p.append(arrow_h(224, 246, 119, "#fde68a", 2))
    # pedestrians crossing the mouth of the side road (no crossing)
    p.append(walker(262, 176) + walker(290, 182))
    p.append(arrow_h(300, 326, 182, "#fde68a", 2))
    # an animal crossing further down
    p.append(f'<ellipse cx="300" cy="236" rx="13" ry="7" fill="#7c2d12"/><circle cx="314" cy="232" r="4.5" fill="#7c2d12"/>')
    # labels
    items = L(lang,
              [("1", "Pedestrians crossing the road you turn into", "go first, even with no crossing there"),
               ("2", "A cyclist close by, going straight on", "goes first when you turn right or left"),
               ("3", "Animals crossing the road you turn into", "go first, even with no cañada there")],
              [("1", "Peatones que cruzan la vía en la que entras", "pasan primero, aunque no haya paso"),
               ("2", "Un ciclista próximo que sigue recto", "pasa primero si giras a derecha o izquierda"),
               ("3", "Animales que cruzan la vía en la que entras", "pasan primero, aunque no haya cañada")])
    for i, (n, head, sub) in enumerate(items):
        y = 64 + i * 70
        p.append(badge(446, y - 4, n, TEAL))
        p.append(txt(466, y, head, 12, 700, INK))
        p.append(txt(466, y + 17, sub, 11.5, 400, SLATE))
    p.append(badge(232, 182, "1", TEAL) + badge(196, 140, "2", TEAL) + badge(330, 256, "3", TEAL))
    return svg(720, 300, "".join(p), L(lang, "Turning into another road", "Girar para entrar en otra vía"))


# ---------------------------------------------------------------- D5 narrow bridge with priority signs
def narrowing(lang):
    p = [rect(0, 40, 720, 170, VERGE, 8)]
    p.append(rect(330, 40, 60, 170, WATER))
    p.append(f'<path d="M0 100 H260 L300 112 H420 L460 100 H720 V160 H460 L420 148 H300 L260 160 H0 Z" fill="{ASPHALT}"/>')
    p.append(rect(300, 107, 120, 4, "#d6d3d1") + rect(300, 149, 120, 4, "#d6d3d1"))   # parapets
    p.append(line(6, 130, 250, 130, WHITE, 2, "12 9") + line(470, 130, 714, 130, WHITE, 2, "12 9"))
    p.append(car_h(200, 145, "#1d4ed8", right=True) + arrow_h(226, 262, 145, WHITE))
    p.append(truck_h(560, 115) + arrow_h(520, 486, 115, WHITE))
    p.append(r6(244, 186, 22))
    p.append(r5(482, 70, 22))
    p.append(lines(20, 236, L(lang, ["Blue square (R-6): you have priority", "over oncoming vehicles"],
                                ["Cuadrado azul (R-6): tienes prioridad", "respecto al sentido contrario"]), 12, 700, INK, "start", 16))
    p.append(lines(700, 236, L(lang, ["Red circle (R-5): give way to oncoming traffic;", "if you meet on the bridge, you reverse"],
                                 ["Círculo rojo (R-5): cede al sentido contrario;", "si os encontráis en el puente, retrocedes tú"]), 12, 700, INK, "end", 16))
    p.append(txt(360, 26, L(lang, "No signs: whoever entered first goes first; if in doubt, the vehicle that is harder to manoeuvre",
                            "Sin señales: pasa quien entró primero; en caso de duda, el de mayor dificultad de maniobra"), 12, 400, SLATE, "middle"))
    return svg(720, 272, "".join(p), L(lang, "Priority on a narrow bridge", "Prioridad en un puente estrecho"))


def truck_h(cx, cy, color="#b45309"):
    """Lorry seen from above, travelling left."""
    w, h = 70, 24
    x, y = cx - w / 2, cy - h / 2
    return rect(x, y, w, h, "#cbd5e1", 4, ' stroke="#64748b"') + rect(x, y, 18, h, color, 4)


# ---------------------------------------------------------------- D6 emergency vehicles
def _car_side(cx, base, color):
    return (f'<circle cx="{cx - 48}" cy="{base - 13}" r="13" fill="#1f2937"/><circle cx="{cx + 48}" cy="{base - 13}" r="13" fill="#1f2937"/>'
            f'<path d="M{cx - 46} {base - 46} L{cx - 28} {base - 70} L{cx + 32} {base - 70} L{cx + 52} {base - 46} Z" fill="{color}"/>'
            f'<path d="M{cx - 38} {base - 48} L{cx - 25} {base - 65} L{cx - 2} {base - 65} L{cx - 2} {base - 48} Z" fill="#cbd5e1"/>'
            f'<path d="M{cx + 4} {base - 48} L{cx + 4} {base - 65} L{cx + 29} {base - 65} L{cx + 43} {base - 48} Z" fill="#cbd5e1"/>'
            + rect(cx - 84, base - 48, 168, 34, color, 10))


def _waves(x, y, left=True, color=SLATE):
    s = -1 if left else 1
    return "".join(f'<path d="M{x + s * (6 + 7 * k)} {y - 9 - 4 * k} Q {x + s * (12 + 9 * k)} {y} {x + s * (6 + 7 * k)} {y + 9 + 4 * k}" fill="none" stroke="{color}" stroke-width="2"/>'
                   for k in range(3))


def emergency_signals(lang):
    p = []
    # priority vehicle
    cx, base = 170, 140
    p.append(f'<circle cx="{cx}" cy="{base - 76}" r="20" fill="#93c5fd" opacity=".6"/>')
    p.append(_car_side(cx, base, "#e2e8f0"))
    p.append(rect(cx - 84, base - 34, 168, 7, "#1d4ed8"))
    p.append(rect(cx - 16, base - 80, 32, 9, "#1d4ed8", 3))
    p.append(_waves(cx - 92, base - 34, True, "#1d4ed8"))
    p.append(txt(cx, 26, L(lang, "Priority vehicle on urgent service", "Vehículo prioritario en servicio urgente"), 13, 700, INK, "middle"))
    p.append(lines(cx, 172, L(lang, ["Blue light (V-1), visible at 50 m all round,", "and the siren at the same time.",
                                       "Light alone only if leaving out the siren is no danger."],
                                ["Luz azul (V-1), visible a 50 m en todas direcciones,", "y la sirena a la vez.",
                                 "Solo la luz si omitir la sirena no supone peligro."]), 11.5, 400, INK, "middle", 16))
    # non-priority vehicle in an emergency
    cx = 540
    p.append(_car_side(cx, base, "#64748b"))
    for x in (cx - 84, cx + 78):
        p.append(rect(x, base - 42, 6, 8, "#f59e0b", 2))
        p.append(f'<circle cx="{x + 3}" cy="{base - 38}" r="9" fill="#fcd34d" opacity=".5"/>')
    p.append(_waves(cx + 90, base - 30, False, SLATE))
    p.append(line(cx - 20, base - 54, cx - 46, base - 90, "#d6a77a", 5, extra=' stroke-linecap="round"'))
    p.append(f'<path d="M{cx - 48} {base - 94} q -14 -8 -26 -2 q 2 10 -2 18 q 12 -4 26 2 Z" fill="#fff" stroke="{SLATE}" stroke-width="1.2"/>')
    p.append(txt(cx, 26, L(lang, "Ordinary car forced into an emergency", "Vehículo no prioritario en una urgencia"), 13, 700, INK, "middle"))
    p.append(lines(cx, 172, L(lang, ["Horn on and off + hazard lights,", "or a handkerchief waved from the window.",
                                       "Every traffic rule still applies."],
                                ["Claxon intermitente + luz de emergencia,", "o un pañuelo agitado por la ventanilla.",
                                 "Debe respetar todas las normas."]), 11.5, 400, INK, "middle", 16))
    p.append(line(360, 40, 360, 210, "#e2e8f0", 1.5))
    p.append(txt(360, 238, L(lang, "Everyone else: make way, normally by moving to the right, and stop if necessary.",
                                "Los demás: facilitar el paso, normalmente apartándose a la derecha, y detenerse si es preciso."), 12.5, 700, TEAL, "middle"))
    return svg(720, 250, "".join(p), L(lang, "Vehicles on emergency service", "Vehículos en servicio de urgencia"))
