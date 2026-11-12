# -*- coding: utf-8 -*-
"""Original SVG diagrams for Category A1/A2, Topic 13 (maintenance and accessories), EN/ES. No third-party artwork is
used. Four figures are drawn for motorcycles; the exhaust-smoke figure is shared with Category B, Topic 13."""

from svgkit import NAVY, TEAL, AMBER, RED, SLATE, BLUE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect, tick, cross
from ..b09.diagrams import L, line, MUTED, LINE, CARD
from ..b10.diagrams import arrow, badge
from ..b13.diagrams import exhaust_smoke  # noqa: F401  (shared with Topic B13)
from ..b13.diagrams import card, circ, METAL, OIL, YEL

DARK = "#1f2937"
FRAME = "#334155"
TYRE = "#111827"
GOOD = "#0b7548"


# ---------------------------------------------------------------- D1 the motorcycle's systems
def moto_systems(lang):
    gy, r = 290, 52
    rx, fx, ay = 150, 440, 290 - 52
    p = [rect(8, 8, 704, 300, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'), line(30, gy, 500, gy, "#94a3b8", 2)]
    for x in (rx, fx):
        p.append(circ(x, ay, r, "none", f' stroke="{TYRE}" stroke-width="12"') + circ(x, ay, 8, METAL))
    p.append(line(395, 110, fx, ay, "#64748b", 7))                                     # fork
    p.append(line(380, 92, 410, 84, DARK, 5) + line(395, 92, 395, 112, DARK, 5))      # handlebar and steering head
    p.append(line(392, 116, 286, 200, FRAME, 6) + line(392, 112, 220, 138, FRAME, 6))  # frame
    p.append(line(288, 206, rx, ay, FRAME, 7))                                        # swingarm
    p.append(line(232, 140, 252, 204, "#f59e0b", 5))                                  # rear shock
    p.append(f'<path d="M300 116 L388 108 L380 152 L304 152 Z" fill="{NAVY}"/>')      # tank
    p.append(f'<path d="M196 136 L300 124 L300 138 L200 146 Z" fill="{DARK}"/>')      # seat
    p.append(rect(268, 160, 92, 68, "#94a3b8", 8) + "".join(line(276, y, 352, y, "#cbd5e1", 2) for y in range(170, 224, 9)))  # engine
    p.append(rect(372, 152, 14, 56, "#475569", 3))                                    # radiator
    p.append(rect(222, 150, 28, 18, RED, 3))                                          # battery
    p.append(rect(304, 146, 36, 12, "#a3e635", 3))                                    # air filter
    p.append(rect(310, 154, 6, 10, "#fde047", 1))                                     # spark plug
    p.append(circ(290, 214, 9, "none", f' stroke="{DARK}" stroke-width="3"') + circ(rx, ay, 20, "none", f' stroke="{DARK}" stroke-width="3"'))
    p.append(line(290, 205, rx, ay - 20, DARK, 2.5) + line(290, 223, rx, ay + 20, DARK, 2.5))   # chain
    marks = [(1, 340, 98), (2, 314, 196), (3, 214, 252), (4, 352, 132), (5, 350, 220), (6, 392, 210), (7, 236, 178), (8, 420, 78), (9, 456, 168)]
    for n, x, y in marks:
        p.append(badge(x, y, n, NAVY, 10))
    legend = L(lang, [
        ("Chassis (frame)", "steel or aluminium: strong and light"),
        ("Engine", "two-stroke or four-stroke"),
        ("Transmission", "clutch, gearbox, chain, shaft or belt"),
        ("Fuel supply", "tank, air filter, injection or carburettor"),
        ("Lubrication", "oil between the moving parts"),
        ("Cooling", "air (fins) or liquid (radiator)"),
        ("Electrical", "battery, starter, ignition, spark plug"),
        ("Steering", "handlebar, steering-head bearings"),
        ("Suspension", "fork, swingarm, shock absorbers"),
    ], [
        ("Chasis o bastidor", "acero o aluminio: resistente y ligero"),
        ("Motor", "de dos o de cuatro tiempos"),
        ("Transmisión", "embrague, cambio, cadena o cardan"),
        ("Alimentación", "depósito, filtro, inyección o carburador"),
        ("Lubricación", "aceite entre las piezas móviles"),
        ("Refrigeración", "por aire (aletas) o por líquido (radiador)"),
        ("Eléctrico", "batería, arranque, encendido, bujía"),
        ("Dirección", "manillar, rodamientos de la tija"),
        ("Suspensión", "horquilla, basculante, amortiguadores"),
    ])
    for i, (name, sub) in enumerate(legend):
        y = 30 + i * 30
        p.append(badge(522, y, i + 1, NAVY, 9) + txt(538, y + 1, name, 11.5, 800, INK) + txt(538, y + 14, sub, 9.5, 500, SLATE))
    return svg(720, 316, "".join(p), L(lang, "The systems of a motorcycle", "Los sistemas de una motocicleta"))


# ---------------------------------------------------------------- D2 two-stroke and four-stroke
def _cyl(cx, top, piston_low, arrow_in=False, arrow_out=False, spark=False):
    """A cylinder seen in section: walls, piston at the top or bottom, optional intake/exhaust arrows and spark."""
    h = 84
    out = rect(cx - 22, top, 4, h, "#64748b", 1) + rect(cx + 18, top, 4, h, "#64748b", 1) + rect(cx - 22, top - 4, 44, 6, "#64748b", 1)
    py = top + (54 if piston_low else 14)
    out += rect(cx - 17, py, 34, 20, "#94a3b8", 3) + line(cx, py + 20, cx, top + h + 8, "#64748b", 4)
    if spark:
        out += f'<path d="M{cx} {top + 2} l-6 10 h5 l-4 9 l10 -12 h-5 l4 -7 z" fill="#facc15" stroke="#a16207" stroke-width="0.8"/>'
    if arrow_in:
        out += arrow(cx - 46, top + 2, cx - 12, top + 10, TEAL, 2.5, 8)
    if arrow_out:
        out += arrow(cx + 12, top + 10, cx + 46, top + 2, "#6b7280", 2.5, 8)
    return out


def strokes(lang):
    p = []
    p.append(card(8, 8, 270, 260, AMBER) + txt(26, 34, L(lang, "Two-stroke", "Dos tiempos"), 15, 800, INK))
    p.append(_cyl(80, 66, False, arrow_in=True) + _cyl(200, 66, True, arrow_out=True, spark=True))
    p.append(lines(80, 178, L(lang, ["Up: intake", "and compression"], ["Sube: admisión", "y compresión"]), 10.5, 700, INK, "middle", 13))
    p.append(lines(200, 178, L(lang, ["Down: explosion", "and exhaust"], ["Baja: explosión", "y escape"]), 10.5, 700, INK, "middle", 13))
    p.append(lines(26, 222, L(lang, ["The four phases in two piston strokes.", "Oil: mixed into the petrol (or a separate", "oil tank and pump). It burns with the fuel."],
                                    ["Las cuatro fases en dos movimientos del pistón.", "Aceite: mezclado con la gasolina (o en un", "depósito aparte con bomba); se quema con ella."]), 10.5, 600, OIL, "start", 13))
    p.append(card(290, 8, 422, 260, NAVY) + txt(308, 34, L(lang, "Four-stroke", "Cuatro tiempos"), 15, 800, INK))
    names = L(lang, ["1 Intake", "2 Compression", "3 Explosion", "4 Exhaust"], ["1 Admisión", "2 Compresión", "3 Explosión", "4 Escape"])
    specs = [(True, True, False, False), (False, False, False, False), (True, False, False, True), (False, False, True, False)]
    for i, (low, ain, aout, spark) in enumerate(specs):
        cx = 350 + i * 100
        p.append(_cyl(cx, 66, low, arrow_in=ain, arrow_out=aout, spark=spark) + txt(cx, 186, names[i], 10.5, 700, INK, "middle"))
    p.append(lines(308, 222, L(lang, ["One phase per piston stroke: four strokes, two turns of the crankshaft.", "Oil: in the crankcase, kept between MIN and MAX; it does not go", "into the fuel mixture (air and petrol)."],
                                     ["Una fase por cada movimiento del pistón: cuatro, dos vueltas del cigüeñal.", "Aceite: en el cárter, entre MIN y MAX; no va en la mezcla", "de combustible (aire y gasolina)."]), 10.5, 600, NAVY, "start", 13))
    return svg(720, 276, "".join(p), L(lang, "Two-stroke and four-stroke engines", "Motores de dos y de cuatro tiempos"))


# ---------------------------------------------------------------- D3 checking and changing the oil on a motorcycle
def oil_moto(lang):
    p = [card(8, 8, 210, 270, OIL), txt(26, 34, L(lang, "Dipstick or sight glass", "Varilla o mirilla"), 13, 800, INK)]
    sx = 66
    p.append(f'<circle cx="{sx}" cy="62" r="11" fill="none" stroke="{YEL}" stroke-width="5"/>' + rect(sx - 3, 72, 6, 120, METAL, 2))
    p.append(rect(sx - 6, 170, 12, 48, METAL, 3) + rect(sx - 6, 186, 12, 32, OIL, 3))
    for y, lab in ((178, "MAX"), (208, "MIN")):
        p.append(line(sx - 12, y, sx + 12, y, INK, 2) + txt(sx + 16, y + 4, lab, 10, 800, INK))
    gx, gy = 138, 150
    p.append(circ(gx, gy, 30, "#e5e7eb", f' stroke="{DARK}" stroke-width="4"') + f'<path d="M{gx - 26} {gy + 4} A26 26 0 0 0 {gx + 26} {gy + 4} Z" fill="{OIL}" opacity="0.85"/>')
    for y, lab in ((gy - 12, "MAX"), (gy + 16, "MIN")):
        p.append(line(gx + 32, y, gx + 42, y, INK, 2) + txt(gx + 46, y + 4, lab, 9, 800, INK))
    p.append(tick(36, 248, 9) + txt(52, 252, L(lang, "Level between MIN and MAX", "Nivel entre MIN y MAX"), 10.5, 700, OIL))
    p.append(card(230, 8, 300, 270, NAVY))
    rows = [
        (L(lang, "Check (four-stroke)", "Comprobar (cuatro tiempos)"), L(lang, ["Regularly, engine stopped and cold,", "motorcycle upright and level (on the", "centre stand). Read the dipstick or", "sight glass; top up as the maker says."],
                                                                          ["Periódicamente, motor parado y frío,", "moto vertical y en llano (sobre el", "caballete). Lee la varilla o la mirilla;", "añade según el fabricante."])),
        (L(lang, "Change", "Cambiar"), L(lang, ["With the engine warm, motorcycle", "upright. Change the filter as the", "manufacturer says."], ["Con el motor caliente y la moto", "vertical. Cambia el filtro según", "indique el fabricante."])),
    ]
    y = 34
    for t, b in rows:
        p.append(txt(248, y, t, 13, 800, NAVY) + lines(248, y + 20, b, 11, 500, INK, "start", 15))
        y += 120
    p.append(line(248, 140, 514, 140, LINE, 1))
    p.append(card(542, 8, 170, 270, RED) + txt(560, 34, L(lang, "Used oil", "Aceite usado"), 13, 800, INK))
    p.append(lines(560, 60, L(lang, ["Highly polluting:", "never on the ground", "or down the drain.", "", "Take it to a", "recycling or", "collection point."], ["Muy contaminante:", "nunca al suelo ni", "a la alcantarilla.", "", "Llévalo a un", "punto de reciclaje", "o recogida."]), 11, 600, INK, "start", 15))
    p.append(cross(578, 196, 10) + txt(594, 200, L(lang, "drain", "alcantarilla"), 10.5, 700, RED) + tick(578, 228, 10) + txt(594, 232, L(lang, "collection", "recogida"), 10.5, 700, GOOD))
    return svg(720, 286, "".join(p), L(lang, "Checking and changing the oil on a motorcycle", "Comprobar y cambiar el aceite de la moto"))


# ---------------------------------------------------------------- D4 the chain: slack, tension and grease
def chain_care(lang):
    p = [rect(8, 8, 420, 270, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"')]
    fx, fy, fr = 340, 120, 18
    rx, ry, rr = 110, 130, 48
    p.append(circ(rx, ry, rr, "none", f' stroke="{DARK}" stroke-width="5"') + circ(rx, ry, 8, METAL) + circ(fx, fy, fr, "none", f' stroke="{DARK}" stroke-width="5"') + circ(fx, fy, 5, METAL))
    p.append(line(rx, ry - rr, fx, fy - fr, DARK, 4))
    mx = (rx + fx) / 2
    sag = 16
    p.append(f'<path d="M{rx} {ry + rr} Q{mx} {(ry + rr + fy + fr) / 2 + 2 * sag} {fx} {fy + fr}" fill="none" stroke="{DARK}" stroke-width="4"/>')
    base = (ry + rr + fy + fr) / 2
    p.append(f'<path d="M{rx} {ry + rr} L{fx} {fy + fr}" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5 4"/>')
    p.append(line(mx, base - 6, mx, base + sag + 6, AMBER, 2) + arrow(mx, base + sag + 8, mx, base - 4, AMBER, 2, 7) + arrow(mx, base - 4, mx, base + sag + 8, AMBER, 2, 7))
    p.append(lines(mx + 10, base + 40, L(lang, ["Slack: the up-and-down play", "in the middle of the lower run"], ["Holgura: el juego arriba y abajo", "en el centro del tramo inferior"]), 11, 800, AMBER, "middle", 14))
    p.append(txt(rx, 32, L(lang, "rear sprocket", "corona"), 10.5, 700, MUTED, "middle") + txt(fx, 32, L(lang, "front sprocket", "piñón"), 10.5, 700, MUTED, "middle"))
    p.append(lines(24, 248, L(lang, ["Measure with the wheel on the ground, as the owner’s manual says:", "usually about 20–30 mm. Your course writes “2 to 3 mm”."],
                                    ["Mídela con la rueda en el suelo, como diga el manual:", "lo habitual es unos 20–30 mm. Tu curso escribe «2 y 3 mm»."]), 10.5, 600, SLATE, "start", 14))
    p.append(card(440, 8, 272, 270, TEAL) + txt(458, 34, L(lang, "After riding in the rain, grease:", "Tras circular con lluvia, engrasa:"), 12, 800, INK))
    items = L(lang, ["The chain (and re-tension it)", "Starter and throttle cables", "Clutch and brake levers", "Rear-brake and gear pedals", "Ends of the clutch, rear-brake,", "   speedometer and rev-counter cables", "Centre stand and side stand"],
                    ["La cadena (y tensarla)", "Cables del estárter y del acelerador", "Manetas de embrague y frenos", "Pedales del freno trasero y del cambio", "Extremos de los cables de embrague,", "   freno trasero, velocímetro y tacómetro", "Caballete central y apoyo lateral"])
    y = 36
    for it in items:
        cont = it.startswith("   ")
        y += 15 if cont else 30
        if not cont:
            p.append(circ(464, y - 4, 4, TEAL))
        p.append(txt(476, y, it.strip(), 11, 600, INK))
    return svg(720, 286, "".join(p), L(lang, "Looking after the chain", "El cuidado de la cadena"))
