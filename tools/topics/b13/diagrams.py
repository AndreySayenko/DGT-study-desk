# -*- coding: utf-8 -*-
"""Original SVG diagrams for Topic 13 (vehicle maintenance and accessories), EN/ES. No third-party artwork is used.
Each function takes the language ("en" or "es") and returns an SVG string. Figures sit on a light background in both
themes."""
import math

from svgkit import NAVY, TEAL, AMBER, RED, SLATE, BLUE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect, tick, cross  # noqa: F401
from ..b09.diagrams import L, line, MUTED, LINE, CARD
from ..b10.diagrams import arrow, badge

DARK = "#1f2937"
METAL = "#9ca3af"
OIL = "#b45309"
COOL_HOT = "#dc2626"
COOL_COLD = "#2563eb"
YEL = "#facc15"


def card(x, y, w, h, color=NAVY):
    return rect(x, y, w, h, "#fff", 10, f' stroke="{LINE}" stroke-width="1.5"') + rect(x, y, 6, h, color, 3)


def circ(cx, cy, r, fill, extra=""):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{extra}/>'


# ---------------------------------------------------------------- D1 what the exhaust smoke tells you
def exhaust_smoke(lang):
    panels = [
        ("white", L(lang, "White", "Blanco"), "#e5e7eb", 0.85,
         L(lang, ["Starting in cold weather: it is", "water vapour. Not a fault."], ["Al arrancar con frío: es vapor", "de agua. No es avería."])),
        ("blue", L(lang, "Bluish white", "Blanco azulado"), "#a5b4fc", 0.8,
         L(lang, ["The engine is burning too", "much oil."], ["El motor consume demasiado", "aceite."])),
        ("black", L(lang, "Black", "Negro"), "#374151", 0.85,
         L(lang, ["Too much fuel or too little air:", "more fuel use and pollution."], ["Exceso de carburante o falta de", "aire: más consumo y contaminación."])),
    ]
    p = []
    for i, (k, title, col, op, note) in enumerate(panels):
        ox = 8 + i * 238
        p.append(rect(ox, 8, 226, 214, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"') + txt(ox + 16, 34, title, 14, 800, INK))
        p.append(rect(ox + 14, 108, 96, 14, METAL, 4) + rect(ox + 104, 104, 12, 22, "#6b7280", 3))
        rnd = [(0, 0, 12), (18, -8, 15), (40, -2, 18), (64, -14, 20), (88, -4, 22), (70, 12, 16), (30, 12, 13)]
        for dx, dy, r in rnd:
            p.append(circ(ox + 132 + dx * 0.9, 114 + dy, r, col, f' opacity="{op}"'))
        if k == "white":
            p.append(tick(ox + 200, 32, 10))
        else:
            p.append(cross(ox + 200, 32, 10))
        p.append(lines(ox + 16, 170, note, 11, 600, INK, "start", 15))
    p.append(txt(14, 244, L(lang, "White smoke that goes on once the engine is warm is not water vapour: have it checked (possible coolant leak).",
                             "Si el humo blanco sigue con el motor ya caliente, no es vapor: revísalo (posible fuga de refrigerante)."), 11, 600, SLATE))
    return svg(720, 254, "".join(p), L(lang, "What the exhaust smoke tells you", "Lo que indica el humo del escape"))


# ---------------------------------------------------------------- D2 where things are: a maintenance map
def maintenance_map(lang):
    body = ("M36 196 L36 160 Q38 142 66 138 L150 128 L214 82 Q224 74 240 74 L384 74 Q402 74 414 86 L462 130 "
            "L506 138 Q522 142 522 160 L522 196 Z")
    p = [f'<path d="{body}" fill="#e2e8f0" stroke="#64748b" stroke-width="2"/>',
         f'<path d="M222 86 L298 86 L298 128 L176 128 Z M310 86 L380 86 Q394 86 402 96 L430 128 L310 128 Z" fill="#cbd5e1"/>',
         line(36, 214, 522, 214, SLATE, 1.5)]
    for wx in (150, 420):
        p.append(circ(wx, 198, 30, DARK) + circ(wx, 198, 12, METAL))
    # exhaust line under the car with catalyst and silencer
    p.append(line(176, 206, 508, 206, "#6b7280", 5) + rect(232, 198, 40, 16, "#b45309", 5) + rect(452, 197, 54, 18, "#475569", 6))
    p.append(rect(330, 182, 60, 18, "#94a3b8", 4))  # fuel tank
    items = [  # (x, y, number, colour)
        (60, 150, 1, COOL_COLD),   # radiator / expansion tank
        (88, 140, 2, RED),         # battery
        (122, 132, 3, TEAL),       # air filter
        (150, 140, 4, RED),        # spark plugs
        (176, 152, 5, OIL),        # dipstick and oil filler
        (120, 176, 6, RED),        # alternator and belt
        (156, 190, 7, OIL),        # sump drain plug
        (252, 190, 8, SLATE),      # catalytic converter
        (360, 176, 9, TEAL),       # fuel filter / tank
        (480, 188, 10, SLATE),     # silencer
    ]
    for x, y, n, c in items:
        p.append(badge(x, y, n, c, 10))
    p.append(txt(92, 46, L(lang, "front", "delante"), 11, 700, MUTED) + arrow(84, 42, 44, 42, MUTED, 1.5, 7))
    car = "".join(p)
    p = [f'<g transform="translate(-6 8) scale(0.94)">{car}</g>']
    legend = [
        (COOL_COLD, L(lang, "Cooling", "Refrigeración"), [(1, L(lang, "Radiator and expansion tank", "Radiador y vaso de expansión"))]),
        (RED, L(lang, "Electrical", "Sistema eléctrico"), [(2, L(lang, "Battery", "Batería")), (4, L(lang, "Spark plugs (petrol)", "Bujías (gasolina)")), (6, L(lang, "Alternator and belt", "Alternador y correa"))]),
        (TEAL, L(lang, "Fuel and air", "Alimentación"), [(3, L(lang, "Air filter", "Filtro de aire")), (9, L(lang, "Fuel filter and tank", "Filtro y depósito de combustible"))]),
        (OIL, L(lang, "Lubrication", "Lubricación"), [(5, L(lang, "Dipstick and oil filler", "Varilla y tapón de llenado")), (7, L(lang, "Sump drain plug", "Tapón de vaciado del cárter"))]),
        (SLATE, L(lang, "Exhaust", "Escape"), [(8, L(lang, "Catalytic converter", "Catalizador")), (10, L(lang, "Silencer", "Silenciador"))]),
    ]
    y = 22
    for col, title, its in legend:
        p.append(rect(510, y - 11, 8, 8 + 17 * len(its), col, 3) + txt(526, y, title, 12, 800, INK))
        for n, t in its:
            y += 17
            p.append(txt(530, y, f"{n} · {t}", 10.5, 500, INK))
        y += 22
    return svg(720, 290, "".join(p), L(lang, "Where the parts you maintain are", "Dónde están las piezas que se mantienen"))


# ---------------------------------------------------------------- D3 checking and changing the oil; SAE grades
def oil(lang):
    p = [card(10, 10, 200, 268, OIL), txt(28, 34, L(lang, "The dipstick", "La varilla"), 13.5, 800, INK)]
    sx = 110
    p.append(f'<circle cx="{sx}" cy="62" r="13" fill="none" stroke="{YEL}" stroke-width="6"/>' + rect(sx - 3, 74, 6, 150, METAL, 2))
    p.append(rect(sx - 6, 196, 12, 54, METAL, 3) + rect(sx - 6, 214, 12, 36, OIL, 3))
    for y, lab in ((204, "MAX"), (238, "MIN")):
        p.append(line(sx - 14, y, sx + 14, y, INK, 2) + txt(sx + 20, y + 4, lab, 11, 800, INK))
    p.append(tick(sx - 40, 224, 9) + lines(28, 262, L(lang, ["Level between MIN and MAX"], ["Nivel entre MIN y MAX"]), 10.5, 700, OIL, "start", 13))
    p.append(card(222, 10, 268, 268, NAVY))
    rows = [
        (L(lang, "Check the level", "Comprobar el nivel"), L(lang, ["Engine stopped and cold, car on", "level ground. Pull out, wipe, put", "back, pull out again and read.", "Top up as the maker says."],
                                                            ["Motor parado y frío, coche en", "llano. Sacar, limpiar, volver a", "meter, sacar de nuevo y leer.", "Añadir según el fabricante."])),
        (L(lang, "Change the oil", "Cambiar el aceite"), L(lang, ["Engine warm (more fluid), level", "ground. Drain from the sump plug,", "refill through the cap on top.", "Change the oil filter too."],
                                                         ["Motor caliente (más fluido), en", "llano. Vaciar por el tapón del cárter", "y rellenar por el tapón de arriba.", "Cambiar también el filtro."])),
    ]
    y = 36
    for t, b in rows:
        p.append(txt(240, y, t, 13, 800, NAVY) + lines(240, y + 20, b, 11, 500, INK, "start", 15))
        y += 122
    p.append(line(240, 148, 474, 148, LINE, 1))
    p.append(card(502, 10, 208, 268, AMBER) + txt(520, 34, L(lang, "Multigrade oil", "Aceite multigrado"), 13.5, 800, INK))
    p.append(txt(606, 84, "SAE 10W-60", 22, 900, INK, "middle"))
    p.append(line(560, 94, 560, 116, TEAL, 2) + line(640, 94, 640, 140, COOL_HOT, 2))
    p.append(lines(526, 132, L(lang, ["10W: winter", "(W) — fluid", "in the cold"], ["10W: invierno", "(W): fluido", "en frío"]), 10.5, 700, TEAL, "start", 13))
    p.append(lines(626, 156, L(lang, ["60: when hot", "(summer) —", "more viscous"], ["60: en caliente", "(verano): más", "viscoso"]), 10.5, 700, COOL_HOT, "start", 13))
    p.append(lines(520, 222, L(lang, ["Low number = fluid;", "high number = viscous."], ["Número bajo = fluido;", "número alto = viscoso."]), 10.5, 600, SLATE, "start", 14))
    return svg(720, 288, "".join(p), L(lang, "Checking and changing the engine oil", "Comprobar y cambiar el aceite del motor"))


# ---------------------------------------------------------------- D4 the cooling circuit
def cooling(lang):
    p = [card(10, 10, 450, 250, COOL_COLD)]
    # radiator with fins and fan
    p.append(rect(36, 60, 70, 150, "#cbd5e1", 6, ' stroke="#64748b" stroke-width="1.5"') + "".join(line(40, y, 102, y, "#94a3b8", 1.5) for y in range(68, 206, 9)))
    p.append(circ(126, 135, 26, "none", ' stroke="#64748b" stroke-width="2"') + "".join(
        f'<ellipse cx="{126 + 13 * math.cos(math.radians(a)):.1f}" cy="{135 + 13 * math.sin(math.radians(a)):.1f}" rx="12" ry="5" fill="#94a3b8" transform="rotate({a} {126 + 13 * math.cos(math.radians(a)):.1f} {135 + 13 * math.sin(math.radians(a)):.1f})"/>'
        for a in (0, 90, 180, 270)))
    # engine block
    p.append(rect(250, 86, 150, 110, "#94a3b8", 10) + "".join(circ(284 + i * 28, 120, 10, "#cbd5e1") for i in range(4)))
    p.append(txt(325, 172, L(lang, "engine", "motor"), 12, 800, INK, "middle"))
    # hot out (top), cooled back (bottom)
    p.append(f'<path d="M250 100 L200 100 L200 66 L106 66" fill="none" stroke="{COOL_HOT}" stroke-width="6"/>' + arrow(150, 66, 112, 66, COOL_HOT, 3, 10))
    p.append(f'<path d="M106 204 L200 204 L200 180 L250 180" fill="none" stroke="{COOL_COLD}" stroke-width="6"/>' + arrow(206, 180, 246, 180, COOL_COLD, 3, 10))
    p.append(txt(152, 56, L(lang, "hot coolant", "refrigerante caliente"), 11, 700, COOL_HOT, "middle") + txt(152, 228, L(lang, "cooled coolant", "refrigerante enfriado"), 11, 700, COOL_COLD, "middle"))
    p.append(txt(72, 46, L(lang, "radiator", "radiador"), 11, 700, INK, "middle") + txt(126, 176, L(lang, "fan", "ventilador"), 10, 600, MUTED, "middle"))
    # expansion tank
    tx = 360
    p.append(line(tx + 20, 74, tx + 20, 86, "#64748b", 4) + rect(tx, 26, 70, 50, "#f8fafc", 14, ' stroke="#64748b" stroke-width="2"') + rect(tx, 46, 70, 30, "#fbcfe8", 12))
    p.append(rect(tx + 22, 16, 26, 12, COOL_COLD, 3) + txt(tx + 35, 96, L(lang, "expansion tank", "vaso de expansión"), 10, 700, INK, "middle"))
    for y, lab in ((38, "MAX"), (62, "MIN")):
        p.append(line(tx + 70, y, tx + 82, y, INK, 2) + txt(tx + 86, y + 4, lab, 10, 800, INK))
    p.append(card(472, 10, 238, 250, COOL_COLD) + txt(490, 34, L(lang, "Looking after it", "Mantenimiento"), 13.5, 800, INK))
    notes = L(lang, ["Check the level with the engine", "cold: between MIN and MAX on", "the expansion tank. Your course:", "top up with distilled water.", "Change the coolant as the maker", "says (about every 2 years).", "Watch for leaks; antifreeze for", "very low temperatures."],
              ["Comprueba el nivel con el motor", "frío: entre MIN y MAX del vaso", "de expansión. Tu curso: rellenar", "con agua destilada.", "Cambia el refrigerante según el", "fabricante (unos 2 años).", "Vigila las fugas; anticongelante", "para temperaturas muy bajas."])
    p.append(lines(490, 58, notes, 11, 500, INK, "start", 15))
    p.append(rect(484, 196, 214, 52, "#fef2f2", 8, ' stroke="#fecaca" stroke-width="1"') + cross(504, 222, 10)
             + lines(522, 218, L(lang, ["Never open the tank with", "the engine hot."], ["Nunca abras el vaso con el", "motor caliente."]), 11.5, 800, RED, "start", 15))
    return svg(720, 270, "".join(p), L(lang, "The cooling circuit", "El circuito de refrigeración"))


# ---------------------------------------------------------------- D5 battery, charging and red warning lights
def battery_icon(cx, cy, s=1.0, col=RED):
    w, h = 44 * s, 28 * s
    return (rect(cx - w / 2, cy - h / 2, w, h, "none", 3, f' stroke="{col}" stroke-width="{3 * s}"') + rect(cx - w / 2 + 6 * s, cy - h / 2 - 5 * s, 8 * s, 5 * s, col)
            + rect(cx + w / 2 - 14 * s, cy - h / 2 - 5 * s, 8 * s, 5 * s, col) + line(cx - 14 * s, cy, cx - 6 * s, cy, col, 2.5 * s)
            + line(cx + 6 * s, cy, cx + 14 * s, cy, col, 2.5 * s) + line(cx + 10 * s, cy - 4 * s, cx + 10 * s, cy + 4 * s, col, 2.5 * s))


def oil_icon(cx, cy, s=1.0, col=RED):
    return (f'<path d="M{cx - 22 * s} {cy - 4 * s} L{cx - 8 * s} {cy - 4 * s} L{cx - 4 * s} {cy - 10 * s} L{cx + 8 * s} {cy - 10 * s} L{cx + 12 * s} {cy - 4 * s} '
            f'L{cx + 24 * s} {cy - 10 * s} L{cx + 14 * s} {cy + 10 * s} L{cx - 18 * s} {cy + 10 * s} Z" fill="none" stroke="{col}" stroke-width="{3 * s}" stroke-linejoin="round"/>'
            + line(cx - 22 * s, cy - 4 * s, cx - 28 * s, cy - 10 * s, col, 3 * s) + f'<path d="M{cx + 28 * s} {cy - 2 * s} q-3 6 0 8 q3 -2 0 -8 z" fill="{col}"/>')


def battery(lang):
    p = [card(10, 10, 300, 262, RED), txt(28, 34, L(lang, "The battery", "La batería"), 13.5, 800, INK)]
    bx, by, bw, bh = 40, 66, 230, 108
    p.append(rect(bx, by, bw, bh, "#374151", 8))
    for i in range(6):
        cx0 = bx + 8 + i * 37
        p.append(rect(cx0, by + 26, 32, bh - 34, "#bfdbfe", 3))
        p.append("".join(rect(cx0 + 5 + j * 8, by + 40, 4, bh - 56, "#6b7280", 1) for j in range(3)))
    p.append(line(bx + 4, by + 34, bx + bw - 4, by + 34, COOL_COLD, 1.5, "4 3"))
    p.append(rect(bx + 30, by - 14, 22, 14, RED, 3) + txt(bx + 41, by - 18, "+", 15, 900, RED, "middle"))
    p.append(rect(bx + bw - 52, by - 14, 22, 14, DARK, 3) + txt(bx + bw - 41, by - 18, "−", 15, 900, INK, "middle"))
    p.append(lines(28, 216, L(lang, ["Six cells: lead plates in distilled", "water and sulphuric acid (electrolyte).", "The liquid must cover the plates:", "top up with distilled water only."],
                              ["Seis vasos: placas de plomo en agua", "destilada con ácido sulfúrico (electrolito).", "El líquido debe cubrir las placas:", "añadir solo agua destilada."]), 10.5, 600, INK, "start", 14))
    p.append(txt(bx + bw - 6, by + bh + 18, L(lang, "terminals: tight, clean, greased", "bornes: apretados, limpios, engrasados"), 10, 700, MUTED, "end"))
    # charging: crankshaft pulley, alternator, belt
    p.append(card(322, 10, 388, 128, NAVY) + txt(340, 34, L(lang, "Charging: the alternator", "Carga: el alternador"), 13.5, 800, INK))
    p.append(circ(380, 92, 26, "#64748b") + circ(460, 74, 16, "#94a3b8") + circ(460, 74, 6, "#475569") + circ(380, 92, 8, "#475569"))
    p.append(f'<path d="M366 68 L452 60 M396 114 L470 86" stroke="{DARK}" stroke-width="4"/>')
    p.append(txt(380, 130, L(lang, "engine", "motor"), 10, 600, MUTED, "middle") + txt(460, 52, L(lang, "alternator", "alternador"), 10, 600, MUTED, "middle"))
    p.append(lines(500, 60, L(lang, ["Driven by a belt; it", "recharges the battery and", "powers the electrics while", "the engine runs."], ["Movido por una correa;", "recarga la batería y da", "energía con el motor en", "marcha."]), 10.5, 600, INK, "start", 14))
    # warning lights
    p.append(card(322, 148, 388, 124, RED) + txt(340, 172, L(lang, "Red warning lights", "Testigos rojos"), 13.5, 800, INK))
    p.append(rect(342, 184, 64, 46, DARK, 8) + battery_icon(374, 210, 0.8, "#ef4444"))
    p.append(lines(414, 196, L(lang, ["Charge light on: alternator fault —", "broken belt or worn brushes."], ["Testigo de carga: alternador averiado,", "correa rota o escobillas gastadas."]), 10.5, 600, INK, "start", 13))
    p.append(rect(342, 234, 64, 32, DARK, 8) + oil_icon(374, 250, 0.6, "#ef4444"))
    p.append(lines(414, 246, L(lang, ["Oil pressure light on: pressure too", "low — stop the engine quickly."], ["Presión de aceite: por debajo del", "mínimo; parar el motor rápidamente."]), 10.5, 600, INK, "start", 13))
    return svg(720, 282, "".join(p), L(lang, "Battery, charging and warning lights", "Batería, carga y testigos"))


# ---------------------------------------------------------------- D6 which wheels are driven
def _car_top(cx, cy, mode):
    w, h = 104, 196
    x, y = cx - w / 2, cy - h / 2
    out = [rect(x, y, w, h, "#e2e8f0", 30, ' stroke="#64748b" stroke-width="2"'), rect(x + 14, y + 52, w - 28, 30, "#cbd5e1", 6), rect(x + 14, y + 130, w - 28, 22, "#cbd5e1", 6)]
    front = [(x - 8, y + 30), (x + w - 6, y + 30)]
    rear = [(x - 8, y + h - 66), (x + w - 6, y + h - 66)]
    driven = {"fwd": front, "rwd": rear, "awd": front + rear}[mode]
    for wx, wy in front + rear:
        out.append(rect(wx, wy, 14, 36, RED if (wx, wy) in driven else DARK, 4))
    out.append(rect(cx - 26, y + 14, 52, 34, RED, 6) + txt(cx, y + 36, "M", 14, 900, "#fff", "middle"))
    fy, ry = y + 48, y + h - 48
    if mode in ("fwd", "awd"):
        out.append(line(x + 4, y + 48, x + w - 4, y + 48, RED, 4))
    if mode in ("rwd", "awd"):
        out.append(line(cx, y + 48, cx, ry, RED, 4) + line(x + 4, ry, x + w - 4, ry, RED, 4) + circ(cx, ry, 7, RED))
    if mode == "awd":
        out.append(circ(cx, fy, 6, RED))
    return "".join(out)


def drivetrain(lang):
    cols = [
        ("fwd", L(lang, "Front-wheel drive", "Tracción delantera"), L(lang, ["The front wheels pull:", "a “traction” vehicle"], ["Tiran las ruedas delanteras:", "vehículo de «tracción»"])),
        ("rwd", L(lang, "Rear-wheel drive", "Tracción trasera"), L(lang, ["The rear wheels push:", "a “propulsion” vehicle"], ["Empujan las traseras:", "vehículo de «propulsión»"])),
        ("awd", L(lang, "Four-wheel drive (4×4)", "Tracción total (4×4)"), L(lang, ["All four wheels are driven", "(integral or total traction)"], ["Las cuatro ruedas son", "motrices (tracción integral)"])),
    ]
    p = []
    for i, (m, t, sub) in enumerate(cols):
        cx = 124 + i * 236
        p.append(rect(cx - 112, 8, 224, 312, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"') + txt(cx, 32, t, 13.5, 800, INK, "middle"))
        p.append(_car_top(cx, 152, m) + lines(cx, 280, sub, 11, 600, INK, "middle", 15))
    p.append(txt(360, 338, L(lang, "M = engine · red wheels = driving wheels · red lines = the transmission (shaft and differential)",
                              "M = motor · ruedas rojas = ruedas motrices · líneas rojas = transmisión (árbol y diferencial)"), 11, 600, SLATE, "middle"))
    return svg(720, 348, "".join(p), L(lang, "Which wheels are driven", "Qué ruedas son motrices"))


# ---------------------------------------------------------------- D7 compulsory equipment
def _v16(cx, cy):
    return (f'<path d="M{cx - 22} {cy + 8} Q{cx - 22} {cy - 18} {cx} {cy - 20} Q{cx + 22} {cy - 18} {cx + 22} {cy + 8} Z" fill="#fde68a" stroke="#d97706" stroke-width="1.5"/>'
            + rect(cx - 25, cy + 6, 50, 8, "#f97316", 3) + circ(cx, cy - 6, 6, "#fbbf24"))


def _vest(cx, cy):
    return (f'<path d="M{cx - 20} {cy - 22} L{cx - 8} {cy - 22} L{cx} {cy - 10} L{cx + 8} {cy - 22} L{cx + 20} {cy - 22} L{cx + 24} {cy + 22} L{cx - 24} {cy + 22} Z" fill="#d9f99d" stroke="#65a30d" stroke-width="1.5"/>'
            + rect(cx - 23, cy + 2, 46, 5, "#cbd5e1") + rect(cx - 22, cy + 12, 44, 5, "#cbd5e1"))


def _wheel(cx, cy):
    return circ(cx, cy, 22, DARK) + circ(cx, cy, 11, METAL) + circ(cx, cy, 3, DARK)


def _extinguisher(cx, cy):
    return (rect(cx - 10, cy - 18, 20, 42, "#dc2626", 8) + rect(cx - 6, cy - 26, 12, 9, DARK, 2) + f'<path d="M{cx + 6} {cy - 22} q14 0 16 14" fill="none" stroke="{DARK}" stroke-width="3"/>'
            + rect(cx - 7, cy - 4, 14, 10, "#fff", 2))


def equipment(lang):
    cols = [
        (L(lang, ["Cars, vans and mixed vehicles", "up to 3,500 kg"], ["Turismos, mixtos y mercancías", "hasta 3.500 kg"]), NAVY,
         [(_v16, L(lang, ["V-16 warning light", "(connected)"], ["Señal V-16", "(conectada)"])), (_vest, L(lang, ["High-visibility", "vest (certified)"], ["Chaleco de alta", "visibilidad", "(certificado)"])),
          (_wheel, L(lang, ["Spare or temporary", "wheel + tools, or a", "puncture-repair kit"], ["Rueda de repuesto o", "temporal + herramientas,", "o kit reparapinchazos"]))]),
        (L(lang, ["Buses, heavy vehicles over", "3,500 kg and combinations"], ["Autobuses, pesados de más de", "3.500 kg y conjuntos"]), AMBER,
         [(_v16, L(lang, ["V-16 warning light"], ["Señal V-16"])), (_vest, L(lang, ["High-visibility", "vest"], ["Chaleco de alta", "visibilidad"])),
          (_extinguisher, L(lang, ["Approved fire", "extinguisher, ready", "to use"], ["Extintor homologado,", "en condiciones", "de uso"]))]),
        (L(lang, ["Motorcycles", "(since 1 October 2026)"], ["Motocicletas", "(desde el 1 de octubre de 2026)"]), TEAL,
         [(_vest, L(lang, ["High-visibility", "vest"], ["Chaleco de alta", "visibilidad"]))]),
    ]
    p = []
    for i, (head, col, its) in enumerate(cols):
        ox = 8 + i * 238
        p.append(rect(ox, 8, 226, 318, "#fff", 12, f' stroke="{LINE}" stroke-width="1.5"') + rect(ox, 8, 226, 52, col, 12) + rect(ox, 46, 226, 14, col))
        p.append(lines(ox + 113, 30, head, 12, 800, "#fff", "middle", 15))
        for j, (icon, lab) in enumerate(its):
            y = 102 + j * 76
            p.append(icon(ox + 44, y) + lines(ox + 82, y + 4 - 7 * (len(lab) - 1), lab, 11, 600, INK, "start", 14))
    p.append(lines(484 + 16, 196, L(lang, ["The V-16 is recommended,", "not compulsory, on a", "motorcycle. Riders who", "work on it wear the vest", "at all times."], ["La V-16 es recomendable,", "no obligatoria, en la moto.", "Quienes trabajan en ella", "llevan el chaleco siempre."]), 10.5, 600, SLATE, "start", 14))
    return svg(720, 334, "".join(p), L(lang, "Compulsory equipment by vehicle", "Dotación obligatoria según el vehículo"))
