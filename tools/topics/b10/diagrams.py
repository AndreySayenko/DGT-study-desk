# -*- coding: utf-8 -*-
"""Original SVG diagrams for Topic 10 (accidents and their factors), EN/ES. No third-party artwork is used.
Each function takes the language ("en" or "es") and returns an SVG string. Figures sit on a light background in
both themes."""
import math

from svgkit import NAVY, TEAL, AMBER, RED, SLATE, BLUE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect, car_h, tick, cross, ASPHALT, VERGE, WHITE  # noqa: F401
from ..b08.signs import at, car_side, standing
from ..b09.diagrams import L, line, MUTED, LINE, CARD

DARK = "#1f2937"
SKIN = "#d9b38c"
CLOTH = "#94a3b8"
SEAT = "#cbd5e1"


def arrow(x1, y1, x2, y2, color=INK, w=2.5, head=9):
    a = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - head * math.cos(a), y2 - head * math.sin(a)
    px, py, hw = -math.sin(a), math.cos(a), head * 0.55
    pts = "%.1f,%.1f %.1f,%.1f %.1f,%.1f" % (x2, y2, bx + px * hw, by + py * hw, bx - px * hw, by - py * hw)
    return line(round(x1, 1), round(y1, 1), round(bx, 1), round(by, 1), color, w) + f'<polygon points="{pts}" fill="{color}"/>'


def rot(inner, a, cx, cy):
    return f'<g transform="rotate({a} {cx} {cy})">{inner}</g>'


def badge(cx, cy, n, color=NAVY, r=10):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>' + txt(cx, cy + 4.2, str(n), 12, 800, "#fff", "middle")


def wheel(cx, cy, turn=0, r=12, color=INK):
    """Steering wheel seen from the driver's seat; the red dot marks the top, so a turn shows."""
    inner = (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="{color}" stroke-width="3"/>'
             + line(cx - r, cy, cx + r, cy, color, 2.5) + line(cx, cy, cx, cy + r, color, 2.5)
             + f'<circle cx="{cx}" cy="{cy}" r="3.2" fill="{color}"/><circle cx="{cx}" cy="{cy - r}" r="3" fill="{RED}"/>')
    return rot(inner, turn, cx, cy) if turn else inner


def car_top(cx, cy, color=NAVY, slide=None):
    """Car seen from above, nose up, with its four wheels; slide='front'/'rear' paints that axle red."""
    w, h = 26, 46
    out = []
    for sx in (-1, 1):
        for axle, wy in (("front", cy - h / 2 + 7), ("rear", cy + h / 2 - 17)):
            col = RED if slide == axle else DARK
            out.append(rect(cx + sx * (w / 2 + 1) - 3.5, wy, 7, 11, col, 2))
    out.append(rect(cx - w / 2, cy - h / 2, w, h, color, 7) + rect(cx - w / 2 + 4, cy - h / 2 + 8, w - 8, 9, "#cbd5e1", 2)
               + rect(cx - w / 2 + 4, cy + h / 2 - 12, w - 8, 6, "#cbd5e1", 2))
    return "".join(out)


# ---------------------------------------------------------------- D1 the three factors
def risk_factors(lang):
    x0, x1, top, rh = 222, 668, 26, 50
    X = lambda v: x0 + (x1 - x0) * v / 100  # noqa: E731
    rows = [(L(lang, "Human factor", "Factor humano"), L(lang, "the driver", "el conductor"), 70, 90),
            (L(lang, "Road and surroundings", "Vía y entorno"), L(lang, "road, weather", "vía, climatología"), 10, 35),
            (L(lang, "Vehicle", "Vehículo"), L(lang, "tyres, brakes, lights…", "neumáticos, frenos, luces…"), 4, 13)]
    bottom = top + rh * len(rows)
    p = []
    for v in (0, 25, 50, 75, 100):
        p.append(line(X(v), top - 8, X(v), bottom, LINE, 1) + txt(X(v), bottom + 18, f"{v} %", 11, 500, MUTED, "middle"))
    for i, (name, sub, lo, hi) in enumerate(rows):
        cy = top + i * rh + rh / 2
        p.append(txt(x0 - 14, cy - 1, name, 13, 700, INK, "end") + txt(x0 - 14, cy + 14, sub, 10.5, 400, MUTED, "end"))
        p.append(rect(X(lo), cy - 11, X(hi) - X(lo), 22, NAVY, 4))
        p.append(txt(X(hi) + 8, cy + 4.5, f"{lo}–{hi} %", 12.5, 700, INK))
    p.append(txt((x0 + x1) / 2, bottom + 38, L(lang, "Share of accidents in which each factor is involved (ranges; one accident can have several)",
                                                "Porcentaje de accidentes en los que interviene cada factor (intervalos; un accidente puede tener varios)"), 11, 600, SLATE, "middle"))
    return svg(720, bottom + 48, "".join(p), L(lang, "The three accident factors", "Los tres factores de los accidentes"))


# ---------------------------------------------------------------- D2 reaction, braking and stopping distance
def stopping_distance(lang):
    xs, xe, xp, gy = 70, 330, 590, 104
    p = [line(30, gy, 700, gy, SLATE, 2)]
    steps = [(xs, L(lang, "1 · Sees the danger", "1 · Ve el peligro")), (xe, L(lang, "2 · Presses the brake", "2 · Pisa el freno")), (xp, L(lang, "3 · Stops", "3 · Se detiene"))]
    for x, lab in steps:
        p.append(txt(x, 20, lab, 12.5, 700, INK, "middle") + line(x, 88, x, 208, MUTED, 1, "4 3"))
        p.append(at(car_side(NAVY, "#fff"), x - 32, gy - 11, 1.45))
    p.append(at(standing(INK), 652, gy - 21, 1.0))
    p.append(line(xs, 46, xe, 46, AMBER, 2) + line(xs, 40, xs, 52, AMBER, 2) + line(xe, 40, xe, 52, AMBER, 2))
    p.append(txt((xs + xe) / 2, 40, L(lang, "reaction time ≈ 0.75 s", "tiempo de reacción ≈ 0,75 s"), 11, 600, INK, "middle"))
    p.append(rect(xs, 118, xe - xs, 28, TEAL, 4) + txt((xs + xe) / 2, 136.5, L(lang, "Reaction distance", "Distancia de reacción"), 12, 700, "#fff", "middle"))
    p.append(rect(xe + 2, 118, xp - xe - 2, 28, AMBER, 4) + txt((xe + xp) / 2, 136.5, L(lang, "Braking distance", "Distancia de frenado"), 12, 700, "#fff", "middle"))
    p.append(rect(xs, 154, xp - xs, 28, NAVY, 4) + txt((xs + xp) / 2, 172.5, L(lang, "Stopping distance = reaction + braking", "Distancia de detención = reacción + frenado"), 12, 700, "#fff", "middle"))
    # lower panel: how the braking distance grows with the surface
    p.append(txt(30, 232, L(lang, "Braking distance compared with a dry road", "Distancia de frenado comparada con la calzada seca"), 12, 700, INK))
    unit, bx = 46, 196
    for i, (lab, k) in enumerate([(L(lang, "Dry", "Seca"), 1), (L(lang, "Rain", "Lluvia"), 2), (L(lang, "Snow or ice", "Nieve o hielo"), 10)]):
        y = 246 + i * 24
        p.append(txt(bx - 10, y + 13, lab, 11.5, 600, INK, "end") + rect(bx, y + 2, unit * k, 16, AMBER, 3) + txt(bx + unit * k + 8, y + 14.5, f"×{k}", 12, 800, INK))
    return svg(720, 322, "".join(p), L(lang, "Reaction, braking and stopping distance", "Distancia de reacción, de frenado y de detención"))


# ---------------------------------------------------------------- D3 when drowsiness strikes, and the rest rule
def drowsy_clock(lang):
    cx, cy, r = 186, 146, 100
    pt = lambda h, rr: (cx + rr * math.cos(math.radians(h * 15 - 90)), cy + rr * math.sin(math.radians(h * 15 - 90)))  # noqa: E731
    p = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{CARD}" stroke="{LINE}" stroke-width="2"/>']
    # night (21–7 h) as a soft inner band, for orientation
    a1, a2 = pt(21, r - 50), pt(7, r - 50)
    p.append(f'<path d="M{a1[0]:.1f} {a1[1]:.1f} A{r - 50} {r - 50} 0 0 1 {a2[0]:.1f} {a2[1]:.1f}" fill="none" stroke="#dbe3ef" stroke-width="10"/>')
    for h in range(24):
        o, i = pt(h, r - 2), pt(h, r - (12 if h % 3 == 0 else 7))
        p.append(line(round(o[0], 1), round(o[1], 1), round(i[0], 1), round(i[1], 1), SLATE, 2 if h % 3 == 0 else 1))
        if h % 3 == 0:
            q = pt(h, r - 25)
            p.append(txt(round(q[0], 1), round(q[1] + 4.5, 1), str(h), 12, 700, INK, "middle"))
    for h1, h2 in ((3, 5), (14, 16)):
        s, e = pt(h1, r + 9), pt(h2, r + 9)
        p.append(f'<path d="M{s[0]:.1f} {s[1]:.1f} A{r + 9} {r + 9} 0 0 1 {e[0]:.1f} {e[1]:.1f}" fill="none" stroke="{RED}" stroke-width="12" stroke-linecap="butt"/>')
    p.append(txt(cx, cy + 4, "24 h", 15, 800, INK, "middle") + txt(cx, cy - 58, L(lang, "night", "noche"), 9.5, 600, MUTED, "middle"))
    q = pt(4, r + 26)
    p.append(txt(q[0] - 4, q[1] - 6, L(lang, "3–5 h", "3–5 h"), 13, 800, RED) + txt(q[0] - 4, q[1] + 8, L(lang, "early hours", "madrugada"), 10.5, 600, INK))
    q = pt(15, r + 24)
    p.append(txt(q[0] + 4, q[1] + 12, "14–16 h", 13, 800, RED, "end") + lines(q[0] + 4, q[1] + 26, L(lang, ["early", "afternoon"], ["primeras horas", "de la tarde"]), 10.5, 600, INK, "end", 13))
    cards = [
        ("2 h · 200 km", L(lang, ["Stop at least this often —", "sooner if you notice tiredness."], ["Para como mínimo con esta frecuencia;", "antes si notas cansancio."])),
        ("20–30 min", L(lang, ["Rest: stretch your legs, get fresh air;", "sleep if you need to."], ["Descansa: estira las piernas, toma el aire;", "duerme si lo necesitas."])),
        ("7–9 h", L(lang, ["of good, deep sleep before a trip.", "Sleeping badly is as risky as too little."], ["de sueño profundo antes del viaje. Dormir", "mal es tan peligroso como dormir poco."])),
    ]
    for i, (big, sub) in enumerate(cards):
        y = 28 + i * 84
        p.append(rect(392, y, 316, 72, "#fff", 10, f' stroke="{LINE}" stroke-width="1.5"') + rect(392, y, 6, 72, NAVY, 3))
        p.append(txt(412, y + 26, big, 19, 800, NAVY) + lines(412, y + 45, sub, 11, 500, INK, "start", 14))
    return svg(720, 298, "".join(p), L(lang, "Drowsiness peaks and the rest rule", "Horas de más somnolencia y la regla del descanso"))


# ---------------------------------------------------------------- D4 rumble strips (GSLF)
def rumble_strips(lang):
    top, bot = 72, 196
    p = [rect(0, 44, 720, top - 44, VERGE), rect(0, bot, 720, 26, VERGE), rect(0, top, 720, bot - top, ASPHALT)]
    p.append(rect(0, top + 3, 720, 3, WHITE) + rect(0, bot - 6, 720, 3, WHITE))
    mid = (top + bot) / 2
    p.append(rect(0, mid - 8, 720, 3, WHITE) + rect(0, mid + 5, 720, 3, WHITE))
    for x in range(6, 720, 10):
        p.append(rect(x, mid - 4, 5, 8, DARK, 1))          # milled strips between the two centre lines
        p.append(rect(x, bot - 16, 5, 9, DARK, 1))         # milled strips along the edge line
        p.append(rect(x, top + 7, 5, 9, DARK, 1))
    # car drifting to the edge, and car drifting over the centre
    p.append(f'<g transform="translate(236 168) rotate(9)">{car_h(0, 0, NAVY)}</g>')
    p.append(arrow(150, 154, 210, 162, "#fff", 2, 7))
    p.append(f'<g transform="translate(520 120) rotate(-9)">{car_h(0, 0, TEAL)}</g>')
    p.append(arrow(436, 150, 494, 130, "#fff", 2, 7))
    for (vx, vy) in ((262, 186), (548, 112)):
        p.append(f'<path d="M{vx} {vy - 10} l5 4 -5 4 5 4 -5 4" stroke="#fde047" stroke-width="2" fill="none"/>'
                 f'<path d="M{vx + 8} {vy - 10} l5 4 -5 4 5 4 -5 4" stroke="#fde047" stroke-width="2" fill="none"/>')
    p.append(txt(360, 20, L(lang, "Centre strips (separating the two directions): a noise and vibration warn you before you cross into oncoming traffic",
                             "Guías en el eje (separación de sentidos): ruido y vibración avisan antes de invadir el sentido contrario"), 11.5, 600, INK, "middle"))
    p.append(line(560, 26, 560, mid - 10, INK, 1.2))
    p.append(txt(360, 244, L(lang, "Edge strips (road edge): they warn you before you run off the road",
                              "Guías en el borde de la calzada: avisan antes de salirte de la vía"), 11.5, 600, INK, "middle"))
    p.append(line(150, 232, 150, bot - 8, INK, 1.2))
    return svg(720, 254, "".join(p), L(lang, "Rumble strips (GSLF) seen from above", "Guías sonoras (GSLF) vistas desde arriba"))


# ---------------------------------------------------------------- D5 blood alcohol over time (illustration)
def bac_curve(lang):
    x0, x1, yb, yt = 70, 560, 236, 36
    X = lambda t: x0 + (x1 - x0) * t / 6  # noqa: E731
    Y = lambda c: yb - (yb - yt) * c  # noqa: E731

    def curve(D, ka, beta):
        return lambda t: max(0.0, D * (1 - math.exp(-ka * t)) - beta * t)
    empty, food = curve(1.0, 4.0, 0.2), curve(0.85, 1.5, 0.2)

    def path(f):
        pts, t = [], 0.0
        while t <= 6.0:
            v = f(t)
            pts.append("%.1f,%.1f" % (X(t), Y(v)))
            if t > 1 and v <= 0:
                break
            t += 0.05
        return "M" + " L".join(pts)
    p = [rect(X(0.5), yt - 6, X(1.5) - X(0.5), yb - yt + 6, "#e8eef7", 0)]
    p.append(txt((X(0.5) + X(1.5)) / 2, yt + 8, "30–90 min", 10.5, 700, NAVY, "middle"))
    p.append(line(x0, yb, x1, yb, SLATE, 1.5) + line(x0, yt - 6, x0, yb, SLATE, 1.5))
    for h in range(7):
        p.append(line(X(h), yb, X(h), yb + 5, SLATE, 1.5) + txt(X(h), yb + 19, f"{h} h", 11, 500, MUTED, "middle"))
    p.append(txt((x0 + x1) / 2, yb + 38, L(lang, "Time since drinking", "Tiempo desde que se bebe"), 11, 600, SLATE, "middle"))
    p.append(f'<text x="24" y="{(yb + yt) / 2}" font-size="11" font-weight="600" fill="{SLATE}" text-anchor="middle" transform="rotate(-90 24 {(yb + yt) / 2})">'
             + L(lang, "Blood alcohol (illustration)", "Tasa de alcohol (ilustración)") + "</text>")
    p.append(f'<path d="{path(food)}" fill="none" stroke="{TEAL}" stroke-width="2.5" stroke-linejoin="round"/>')
    p.append(f'<path d="{path(empty)}" fill="none" stroke="{NAVY}" stroke-width="2.5" stroke-linejoin="round"/>')
    t1 = 5 / 60
    p.append(f'<circle cx="{X(t1):.1f}" cy="{Y(empty(t1)):.1f}" r="4" fill="{NAVY}" stroke="#fff" stroke-width="1.5"/>')
    p.append(line(50, Y(empty(t1)), X(t1) - 4, Y(empty(t1)), NAVY, 1.2) + badge(46, Y(empty(t1)), 1))
    p.append(badge((X(0.5) + X(1.5)) / 2, yt - 18, 2))
    p.append(badge(X(3) + 14, Y(empty(3)) - 18, 3))
    # legend and notes in a right-hand column
    lx = 584
    p.append(line(lx, 46, lx + 22, 46, NAVY, 3) + txt(lx + 30, 50, L(lang, "empty stomach", "en ayunas"), 11.5, 600, INK))
    p.append(line(lx, 68, lx + 22, 68, TEAL, 3) + txt(lx + 30, 72, L(lang, "with food", "con comida"), 11.5, 600, INK))
    notes = [L(lang, ["In the blood about", "5 min after drinking"], ["En sangre a los", "5 min de beber"]),
             L(lang, ["Highest level", "30–90 min after"], ["Máximo entre 30 y", "90 min después"]),
             L(lang, ["Then falls very slowly:", "several hours"], ["Después baja muy", "despacio: varias horas"])]
    for i, n in enumerate(notes):
        y = 110 + i * 52
        p.append(badge(lx + 9, y, i + 1) + lines(lx + 25, y + 4, n, 11, 500, INK, "start", 14))
    return svg(720, 286, "".join(p), L(lang, "How blood alcohol rises and falls", "Cómo sube y baja la tasa de alcohol"))


# ---------------------------------------------------------------- D6 reading the tyre sidewall
def tyre_code(lang):
    p = [rect(16, 14, 688, 104, DARK, 20)]
    p.append(f'<path d="M30 30 Q360 6 690 30" fill="none" stroke="#374151" stroke-width="2"/><path d="M30 104 Q360 128 690 104" fill="none" stroke="#374151" stroke-width="2"/>')
    toks = [("225", 110, 1), ("/", 158, 0), ("70", 196, 2), ("R", 262, 1), ("16", 308, 2), ("110", 392, 1), ("S", 448, 2)]
    for s, x, _ in toks:
        p.append(txt(x, 82, s, 38, 800, "#fff", "middle"))
    p.append(txt(560, 58, "TUBELESS", 13, 700, "#d1d5db", "middle") + txt(540, 92, "DOT", 13, 700, "#d1d5db", "middle") + txt(620, 92, "3221", 28, 800, "#fff", "middle"))
    labs = {
        "225": L(lang, ["width", "225 mm"], ["anchura", "225 mm"]),
        "70": L(lang, ["profile: sidewall", "= 70 % of the width"], ["perfil: flanco =", "70 % de la anchura"]),
        "R": L(lang, ["radial", "structure"], ["estructura", "radial"]),
        "16": L(lang, ["rim diameter", "16 inches"], ["diámetro llanta", "16 pulgadas"]),
        "110": L(lang, ["load index", "110 = 1,060 kg"], ["índice de carga", "110 = 1.060 kg"]),
        "S": L(lang, ["speed symbol", "S = 180 km/h"], ["código velocidad", "S = 180 km/h"]),
        "3221": L(lang, ["made in week 32", "of 2021"], ["fabricado semana", "32 de 2021"]),
    }
    rowy = {1: 148, 2: 198}
    for s, x, row in toks + [("3221", 620, 1)]:
        if not row:
            continue
        y = rowy[row]
        p.append(line(x, 96, x, y - 12, SLATE, 1.3) + f'<circle cx="{x}" cy="96" r="3" fill="{SLATE}"/>')
        p.append(lines(x, y, labs[s], 11.5, 600, INK, "middle", 14))
    return svg(720, 230, "".join(p), L(lang, "How to read a tyre's markings", "Cómo leer las inscripciones del neumático"))


# ---------------------------------------------------------------- D7 tyre pressure and where it wears
def tyre_pressure(lang):
    g = 168
    shapes = {
        "ok": lambda c: f"M{c - 56} {g - 92} L{c + 56} {g - 92} Q{c + 62} {g - 92} {c + 62} {g - 80} L{c + 62} {g - 8} Q{c + 62} {g} {c + 54} {g} L{c - 54} {g} Q{c - 62} {g} {c - 62} {g - 8} L{c - 62} {g - 80} Q{c - 62} {g - 92} {c - 56} {g - 92} Z",
        "high": lambda c: f"M{c - 54} {g - 96} L{c + 54} {g - 96} C{c + 66} {g - 70} {c + 56} {g - 10} {c + 22} {g} L{c - 22} {g} C{c - 56} {g - 10} {c - 66} {g - 70} {c - 54} {g - 96} Z",
        "low": lambda c: f"M{c - 54} {g - 86} L{c + 54} {g - 86} C{c + 74} {g - 56} {c + 76} {g - 6} {c + 58} {g} L{c + 30} {g} Q{c} {g - 14} {c - 30} {g} L{c - 58} {g} C{c - 76} {g - 6} {c - 74} {g - 56} {c - 54} {g - 86} Z",
    }
    contact = {"ok": [(-54, 54)], "high": [(-22, 22)], "low": [(-58, -30), (30, 58)]}
    panels = [
        ("ok", L(lang, "Correct pressure", "Presión correcta"), L(lang, ["The whole tread touches the road:", "even wear, best grip."], ["Apoya toda la banda de rodadura:", "desgaste uniforme, máxima adherencia."])),
        ("high", L(lang, "Too high", "Presión excesiva"), L(lang, ["Only the centre touches: less grip,", "the centre wears, bumps reach", "the suspension."], ["Solo apoya el centro: menos adherencia,", "se desgasta el centro, la suspensión", "sufre los baches."])),
        ("low", L(lang, "Too low", "Presión escasa"), L(lang, ["The edges carry the load: they wear,", "the tyre overheats (blow-out risk),", "aquaplaning, more fuel."], ["Apoyan los bordes: se desgastan, se", "calienta (riesgo de reventón),", "aquaplaning, más consumo."])),
    ]
    p = []
    for i, (k, title, note) in enumerate(panels):
        c = 122 + i * 238
        p.append(rect(c - 114, 6, 228, 274, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'))
        p.append((tick if k == "ok" else cross)(c - 86, 28, 10) + txt(c - 70, 33, title, 13.5, 800, INK))
        p.append(line(c - 96, g, c + 96, g, SLATE, 2))
        p.append(f'<path d="{shapes[k](c)}" fill="{DARK}"/>')
        rim_y = g - (96 if k == "high" else 86 if k == "low" else 92)
        p.append(rect(c - 40, rim_y - 14, 80, 16, "#94a3b8", 3))
        for a, b in contact[k]:
            p.append(rect(c + a, g + 3, b - a, 7, TEAL if k == "ok" else RED, 2))
        p.append(lines(c - 98, g + 32, note, 10.8, 500, INK, "start", 14))
    return svg(720, 286, "".join(p), L(lang, "Tyre pressure and tyre wear", "Presión de inflado y desgaste del neumático"))


# ---------------------------------------------------------------- D8 motorcycle controls (top view)
def moto_controls(lang):
    cx = 360
    R, Lc = NAVY, TEAL
    p = [rect(cx - 10, 14, 20, 58, DARK, 9), rect(cx - 10, 236, 20, 58, DARK, 9)]
    p.append(f'<ellipse cx="{cx}" cy="150" rx="40" ry="62" fill="#94a3b8"/>' + rect(cx - 24, 176, 48, 66, "#475569", 14))
    p.append(line(cx - 92, 86, cx + 92, 86, "#334155", 7) + rect(cx - 110, 80, 30, 12, DARK, 5) + rect(cx + 80, 80, 30, 12, DARK, 5))
    p.append(line(cx - 106, 74, cx - 70, 70, "#334155", 4) + line(cx + 106, 74, cx + 70, 70, "#334155", 4))
    p.append(line(cx - 44, 210, cx - 62, 210, "#334155", 6) + line(cx + 44, 210, cx + 62, 210, "#334155", 6))
    p.append(line(cx - 58, 210, cx - 70, 192, "#334155", 4) + line(cx + 58, 210, cx + 70, 192, "#334155", 4))
    p.append(txt(cx + 20, 30, L(lang, "front", "delante"), 10.5, 600, MUTED))
    marks = [  # (x, y, colour, label lines, label anchor x, label y)
        (cx - 88, 72, Lc, L(lang, ["LEFT HAND", "clutch lever"], ["MANO IZQUIERDA", "maneta de embrague"]), 30, 64),
        (cx - 70, 192, Lc, L(lang, ["LEFT FOOT", "gear lever"], ["PIE IZQUIERDO", "selector de marchas"]), 30, 186),
        (cx + 88, 72, R, L(lang, ["RIGHT HAND", "front brake lever"], ["MANO DERECHA", "maneta del freno delantero"]), 690, 50),
        (cx + 95, 86, R, L(lang, ["RIGHT HAND", "throttle (twist grip)"], ["MANO DERECHA", "acelerador (puño)"]), 690, 108),
        (cx + 70, 192, R, L(lang, ["RIGHT FOOT", "rear brake pedal"], ["PIE DERECHO", "pedal del freno trasero"]), 690, 186),
    ]
    for x, y, col, lab, lx, ly in marks:
        p.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{col}" stroke="#fff" stroke-width="2"/>')
        if lx < cx:
            p.append(line(lx + 128, ly + 4, x - 8, y, col, 1.3) + lines(lx, ly, lab, 11.5, 700, INK, "start", 15))
        else:
            p.append(line(lx - 150, ly + 4, x + 8, y, col, 1.3) + lines(lx, ly, lab, 11.5, 700, INK, "end", 15))
    p.append(f'<circle cx="40" cy="262" r="7" fill="{Lc}"/>' + txt(54, 266, L(lang, "Left side: clutch and gears", "Lado izquierdo: embrague y marchas"), 12, 700, INK))
    p.append(f'<circle cx="452" cy="262" r="7" fill="{R}"/>' + txt(466, 266, L(lang, "Right side: throttle and both brakes", "Lado derecho: acelerador y frenos"), 12, 700, INK))
    return svg(720, 300, "".join(p), L(lang, "Motorcycle controls seen from above", "Mandos de la motocicleta vistos desde arriba"))


# ---------------------------------------------------------------- D9 wearing the seat belt
def _person_front(cx):
    return (rect(cx - 60, 40, 120, 212, SEAT, 18) + rect(cx - 30, 10, 60, 36, SEAT, 10)
            + rect(cx - 8, 76, 16, 18, SKIN, 3) + f'<circle cx="{cx}" cy="58" r="22" fill="{SKIN}"/>'
            + f'<path d="M{cx - 50} 104 Q{cx - 50} 92 {cx - 38} 92 L{cx + 38} 92 Q{cx + 50} 92 {cx + 50} 104 L{cx + 40} 196 L{cx - 40} 196 Z" fill="{CLOTH}"/>'
            + rect(cx - 62, 98, 13, 100, CLOTH, 6) + rect(cx + 49, 98, 13, 100, CLOTH, 6)
            + rect(cx - 44, 194, 88, 46, "#475569", 8))


def seatbelt(lang):
    p = []
    for i, ok in enumerate((True, False)):
        cx = 118 + i * 360
        p.append(rect(cx - 106, 4, 344, 282, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'))
        p.append(_person_front(cx))
        if ok:
            p.append(line(cx + 28, 92, cx - 36, 206, DARK, 9) + line(cx - 46, 208, cx + 46, 208, DARK, 9) + rect(cx - 44, 201, 14, 14, "#d1d5db", 2))
            notes = [(cx + 28, 98, L(lang, ["Over the collarbone,", "across the middle", "of the chest"], ["Sobre la clavícula,", "por el centro", "del pecho"])),
                     (cx + 40, 208, L(lang, ["Low, over the hip", "bones, below the", "belly"], ["Baja, sobre los", "huesos de la cadera,", "bajo el abdomen"]))]
            head = (tick(cx - 72, 24, 11), L(lang, "Correct", "Correcto"))
        else:
            p.append(line(cx + 9, 84, cx - 36, 178, DARK, 9) + line(cx - 46, 172, cx + 46, 172, DARK, 9) + rect(cx - 44, 165, 14, 14, "#d1d5db", 2))
            p.append(f'<circle cx="{cx + 10}" cy="86" r="14" fill="none" stroke="{RED}" stroke-width="2.5"/><circle cx="{cx + 20}" cy="172" r="14" fill="none" stroke="{RED}" stroke-width="2.5"/>')
            notes = [(cx + 24, 86, L(lang, ["Against the neck"], ["Contra el cuello"])),
                     (cx + 34, 172, L(lang, ["Over the belly:", "the body can slide", "under it (submarining)"], ["Sobre el abdomen:", "el cuerpo se desliza", "por debajo (efecto", "submarino)"]))]
            head = (cross(cx - 72, 24, 11), L(lang, "Wrong", "Incorrecto"))
        p.append(head[0] + txt(cx - 56, 29, head[1], 13.5, 800, INK))
        for x, y, lab in notes:
            p.append(line(x, y, cx + 84, y, INK, 1.2) + lines(cx + 90, y - 2, lab, 11, 600, INK, "start", 13.5))
    return svg(720, 292, "".join(p), L(lang, "How to wear the seat belt", "Cómo colocar el cinturón de seguridad"))


# ---------------------------------------------------------------- D10 adjusting the head restraint
def headrest(lang):
    hx, hy = 250, 112
    p = [rect(312, 172, 64, 116, SEAT, 16), line(328, 158, 328, 176, "#64748b", 4), line(360, 158, 360, 176, "#64748b", 4)]
    p.append(rect(318, 66, 50, 92, "#94a3b8", 16))
    p.append(f'<path d="M{hx - 30} 180 L{hx + 46} 180 L{hx + 60} 288 L{hx - 52} 288 Z" fill="{CLOTH}"/>' + rect(hx - 12, 150, 26, 34, SKIN, 4))
    p.append(f'<ellipse cx="{hx}" cy="{hy}" rx="46" ry="46" fill="{SKIN}"/>'
             + f'<path d="M{hx - 42} {hy - 8} L{hx - 56} {hy + 10} L{hx - 42} {hy + 14} Z" fill="{SKIN}"/>'
             + f'<ellipse cx="{hx + 6}" cy="{hy + 6}" rx="6" ry="10" fill="#c79a6e"/><circle cx="{hx - 22}" cy="{hy - 4}" r="3.6" fill="{INK}"/>'
             + f'<path d="M{hx - 44} {hy - 22} Q{hx - 30} {hy - 52} {hx + 2} {hy - 48} Q{hx + 40} {hy - 44} {hx + 46} {hy - 4} Q{hx + 30} {hy - 30} {hx - 44} {hy - 22} Z" fill="#6b4f3a"/>')
    rows = [(66, L(lang, ["Top of the head restraint level", "with the top of the head"], ["Parte superior del reposacabezas a la", "altura de la parte superior de la cabeza"])),
            (hy - 4, L(lang, ["Middle of the head restraint", "at eye level"], ["Parte central del reposacabezas", "a la altura de los ojos"])),
            (150, L(lang, ["Gap between the back of the head", "and the head restraint: 4 cm at most"], ["Distancia entre la cabeza y el", "reposacabezas: no más de 4 cm"]))]
    for i, (y, lab) in enumerate(rows):
        if i < 2:
            p.append(line(180, y, 430, y, NAVY, 1.5, "6 4"))
        p.append(badge(450, y, i + 1) + lines(468, y - 3, lab, 11.5, 600, INK, "start", 14))
    p.append(arrow(307, 132, 297, 132, RED, 2, 6) + arrow(307, 132, 317, 132, RED, 2, 6))
    p.append(line(307, 136, 307, 150, RED, 1.2) + line(307, 150, 436, 150, RED, 1.2, "3 3"))
    return svg(720, 292, "".join(p), L(lang, "How to adjust the head restraint", "Cómo regular el reposacabezas"))


# ---------------------------------------------------------------- D11 driving through a bend
def curve_technique(lang):
    ccx, ccy, R = 300, 52, 188
    road = f"M20 {ccy + R} L{ccx} {ccy + R} A{R} {R} 0 0 0 {ccx + R} {ccy} L{ccx + R} -10"
    p = [rect(0, 0, 720, 320, "#e8f0e3"), f'<path d="{road}" fill="none" stroke="{ASPHALT}" stroke-width="58"/>',
         f'<path d="{road}" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="12 10"/>']
    # zone limits
    p.append(line(ccx, ccy + R - 30, ccx, ccy + R + 30, "#fde047", 3) + line(ccx + R - 30, ccy, ccx + R + 30, ccy, "#fde047", 3))
    p.append(car_h(150, ccy + R + 13, NAVY))
    a = math.radians(45)
    mx, my = ccx + (R - 13) * math.cos(a), ccy + (R - 13) * math.sin(a)
    p.append(f'<g transform="translate({mx:.1f} {my:.1f}) rotate(-45)">{car_h(0, 0, NAVY)}</g>')
    p.append(f'<g transform="translate({ccx + R + 13} 90) rotate(-90)">{car_h(0, 0, NAVY)}</g>')
    # centrifugal force on the outside of the bend
    ox, oy = ccx + (R + 34) * math.cos(a), ccy + (R + 34) * math.sin(a)
    p.append(arrow(ox, oy, ox + 46, oy + 46, RED, 3, 11))
    p.append(lines(ox + 54, oy + 30, L(lang, ["Centrifugal force pushes", "you out of the bend: more", "with speed (×4 if you double", "it), a tighter bend, more weight"],
                                       ["La fuerza centrífuga te empuja", "hacia fuera: crece con la velocidad", "(×4 si la duplicas), la curva más", "cerrada y el peso"]), 11, 600, INK, "start", 14))
    p.append(badge(150, ccy + R - 50, 1) + lines(166, ccy + R - 52, L(lang, ["Before: brake and shift down", "on the straight — not in the bend"], ["Antes: frena y reduce en la recta,", "no dentro de la curva"]), 11.5, 600, INK, "start", 14))
    p.append(badge(304, 96, 2) + lines(320, 100, L(lang, ["During: keep a", "gentle, steady", "throttle; brake", "only softly"], ["Durante: acelera", "suave y progresivo;", "si frenas, con", "suavidad"]), 11.5, 600, INK, "start", 14))
    p.append(badge(ccx + R + 50, 30, 3) + lines(ccx + R + 66, 28, L(lang, ["Exit: speed up,", "longer gears, straighten", "the wheel gently"], ["Salida: acelera,", "marchas más largas,", "endereza con suavidad"]), 11.5, 600, INK, "start", 14))
    return svg(720, 300, "".join(p), L(lang, "Driving through a bend", "Cómo conducir en una curva"))


# ---------------------------------------------------------------- D12 skids: front or rear axle
def skid(lang):
    p = []
    panels = [
        ("front", L(lang, "Front wheels slide (understeer)", "Derrapa el eje delantero (subviraje)"),
         L(lang, ["The car goes straight on instead of turning.", "Straighten the steering a little and", "let the front tyres grip again."],
           ["El coche sigue recto en lugar de girar.", "Endereza un poco la dirección para", "que las ruedas delanteras recuperen agarre."])),
        ("rear", L(lang, "Rear wheels slide (oversteer)", "Derrapa el eje trasero (sobreviraje)"),
         L(lang, ["The rear swings out of the bend.", "Turn the wheel towards the same side", "the rear is sliding (countersteer)."],
           ["La parte trasera se va hacia fuera.", "Gira el volante hacia el mismo lado", "del derrape (contravolante)."])),
    ]
    for i, (k, title, note) in enumerate(panels):
        ox = i * 362
        p.append(rect(ox + 4, 4, 350, 316, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'))
        p.append(txt(ox + 20, 28, title, 13, 800, INK))
        road = f"M{ox + 230} 244 C{ox + 230} 156 {ox + 170} 90 {ox + 40} 78"
        p.append(f'<path d="{road}" fill="none" stroke="{ASPHALT}" stroke-width="64"/><path d="{road}" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="10 9"/>')
        p.append(f'<path d="M{ox + 222} 212 C{ox + 220} 156 {ox + 170} 110 {ox + 80} 96" fill="none" stroke="{TEAL}" stroke-width="2.5" stroke-dasharray="6 5"/>')
        if k == "front":
            p.append(car_top(ox + 222, 210, NAVY, "front") + arrow(ox + 222, 182, ox + 242, 70, RED, 3, 11))
            p.append(wheel(ox + 300, 120, 0) + txt(ox + 300, 150, L(lang, "straighten", "endereza"), 10.5, 700, INK, "middle"))
        else:
            p.append(rot(car_top(ox + 214, 204, NAVY, "rear"), -38, ox + 214, 204) + arrow(ox + 228, 228, ox + 272, 240, RED, 3, 11))
            p.append(wheel(ox + 300, 120, 35) + txt(ox + 300, 150, L(lang, "steer right", "gira a la dcha."), 10.5, 700, INK, "middle"))
        p.append(lines(ox + 20, 270, note, 11, 500, INK, "start", 14))
    return svg(720, 324, "".join(p), L(lang, "What to do in a skid", "Cómo actuar en un derrape"))


# ---------------------------------------------------------------- D13 crosswind and the screen effect
def crosswind(lang):
    top, bot = 90, 206
    lane = (top + bot) / 2
    p = [rect(0, 72, 720, top - 72, "#9ca3af"), rect(0, top, 720, bot - top, ASPHALT), rect(0, bot, 720, 30, VERGE)]
    p.append(rect(0, top + 3, 720, 3, WHITE) + rect(0, bot - 6, 720, 3, WHITE))
    for x in range(0, 720, 40):
        p.append(rect(x, lane - 1.5, 22, 3, WHITE))
    tx0, tx1 = 290, 452
    p.append(rect(tx0, lane + 10, tx1 - tx0 - 26, 40, "#e5e7eb", 4, ' stroke="#64748b"') + rect(tx1 - 26, lane + 12, 26, 36, "#b45309", 5, ' stroke="#fff" stroke-width="1.5"') + rect(tx1 - 10, lane + 16, 6, 28, "#cbd5e1", 2))
    for x in range(30, 720, 44):
        sheltered = tx0 - 6 < x < tx1 + 6
        y2 = bot + 4 if sheltered else top + 20
        p.append(arrow(x, 262, x, y2, BLUE, 2, 8))
    p.append(f'<rect x="{tx0}" y="{top + 8}" width="{tx1 - tx0}" height="{lane - top - 12}" fill="#93c5fd" opacity="0.22"/>')
    for x in (120, 370, 620):
        p.append(car_h(x, (top + lane) / 2 + 2, NAVY))
    caps = [(120, 20, L(lang, ["Wind from the right: hold", "the wheel firmly, turned", "slightly into the wind"], ["Viento desde la derecha:", "volante firme y un poco", "girado contra el viento"])),
            (370, 0, L(lang, ["Alongside the lorry it", "shields you (screen effect):", "straighten the wheel"], ["Junto al camión, este hace", "de pantalla: endereza", "el volante"])),
            (620, 20, L(lang, ["Past the lorry the wind", "hits again: correct", "to the right"], ["Al dejar atrás el camión", "vuelve el viento: corrige", "hacia la derecha"]))]
    for x, turn, lab in caps:
        p.append(wheel(x - 92, 24, turn) + lines(x - 74, 16, lab, 10.8, 600, INK, "start", 13.5))
    p.append(txt(14, 286, L(lang, "Crosswind blowing from the driver's right to left (from below in this drawing)", "Viento lateral de derecha a izquierda del conductor (desde abajo en el dibujo)"), 11, 600, BLUE))
    return svg(720, 294, "".join(p), L(lang, "Crosswind and the screen effect", "Viento lateral y efecto pantalla"))
