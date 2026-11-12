# -*- coding: utf-8 -*-
"""Original SVG diagrams for Topic 7 (EN/ES). No third-party artwork is used. Each function takes the language
("en" or "es") and returns an SVG string. Figures sit on a light background in both themes."""

from svgkit import NAVY, TEAL, RED, SLATE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect, car_h, tick, cross, ASPHALT, VERGE, WHITE  # noqa: F401

MUTED = "#64748b"
GRID = "#e2e8f0"
AMBER = "#f59e0b"
LAMP_RED = "#ef4444"
NIGHT = "#1e293b"
BEAM = "#fef9c3"


def L(lang, en, es):
    return en if lang == "en" else es


def line(x1, y1, x2, y2, color=INK, width=2, dash=None, extra=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{d}{extra}/>'


def glow(cx, cy, r, color, core=None):
    return f'<circle cx="{cx}" cy="{cy}" r="{r * 2}" fill="{color}" opacity=".3"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="{core or color}"/>'


# ---------------------------------------------------------------- D1 the lights at the back of a car
def rear_lights(lang):
    cx, base = 360, 250
    p = [rect(cx - 150, base - 8, 300, 8, "#cbd5e1", 2)]
    p.append(rect(cx - 122, base - 34, 40, 34, "#1f2937", 5) + rect(cx + 82, base - 34, 40, 34, "#1f2937", 5))
    p.append(f'<path d="M{cx - 110} {base - 128} L{cx - 84} {base - 196} L{cx + 84} {base - 196} L{cx + 110} {base - 128} Z" fill="#475569"/>')
    p.append(f'<path d="M{cx - 96} {base - 132} L{cx - 74} {base - 186} L{cx + 74} {base - 186} L{cx + 96} {base - 132} Z" fill="#cbd5e1"/>')
    p.append(rect(cx - 140, base - 132, 280, 106, "#64748b", 16))
    p.append(rect(cx - 24, base - 194, 48, 7, LAMP_RED, 3))
    for sx in (-1, 1):
        x0 = cx + sx * 112
        p.append(rect(x0 - 22, base - 120, 44, 20, "#991b1b", 4) + glow(x0, base - 110, 6, LAMP_RED))
        p.append(rect(x0 - 22, base - 96, 44, 10, AMBER, 3))
    p.append(rect(cx - 96, base - 46, 22, 10, "#f8fafc", 3, ' stroke="#94a3b8" stroke-width="1"'))
    p.append(rect(cx + 74, base - 46, 22, 10, LAMP_RED, 3))
    p.append(rect(cx - 50, base - 80, 100, 24, "#fff", 3, ' stroke="#94a3b8" stroke-width="1"') + rect(cx - 50, base - 80, 12, 24, "#1d4ed8", 2))
    p.append(rect(cx - 10, base - 86, 20, 4, "#fde68a", 2))
    p.append(rect(cx - 132, base - 40, 22, 6, "#b91c1c", 2) + rect(cx + 110, base - 40, 22, 6, "#b91c1c", 2))
    right = L(lang, [("Third brake light (red)", cx + 20, base - 191, 30), ("Position + brake lights (red)", cx + 124, base - 110, 98),
                     ("Indicators (amber)", cx + 124, base - 91, 130), ("Rear fog light (red)", cx + 90, base - 41, 200)],
              [("Tercera luz de freno (roja)", cx + 20, base - 191, 30), ("Posición + freno (rojas)", cx + 124, base - 110, 98),
               ("Intermitentes (amarillo auto)", cx + 124, base - 91, 130), ("Antiniebla trasera (roja)", cx + 90, base - 41, 200)])
    left = L(lang, [("Number-plate light", cx - 6, base - 84, 60), ("Reversing light (white)", cx - 90, base - 41, 186), ("Reflectors (red)", cx - 124, base - 37, 226)],
             [("Luz de la placa", cx - 6, base - 84, 60), ("Marcha atrás (blanca)", cx - 90, base - 41, 186), ("Catadióptricos (rojos)", cx - 124, base - 37, 226)])
    for s_, ax, ay, y in right:
        p.append(line(ax, ay, 524, y - 4, MUTED, 1, "3 3") + f'<circle cx="{ax}" cy="{ay}" r="2.5" fill="{INK}"/>' + txt(530, y, s_, 11.5, 600, INK))
    for s_, ax, ay, y in left:
        p.append(line(ax, ay, 196, y - 4, MUTED, 1, "3 3") + f'<circle cx="{ax}" cy="{ay}" r="2.5" fill="{INK}"/>' + txt(190, y, s_, 11.5, 600, INK, "end"))
    return svg(720, 262, "".join(p), L(lang, "Lights at the back of a car", "Luces de la parte trasera de un turismo"))


# ---------------------------------------------------------------- D2 fog lights by weather
def _icon(kind, cx, cy):
    if kind == "fog":
        return "".join(line(cx - 22, cy - 12 + i * 8, cx + 22, cy - 12 + i * 8, SLATE, 3, extra=' stroke-linecap="round"') for i in range(4))
    cloud = (f'<ellipse cx="{cx}" cy="{cy - 6}" rx="22" ry="11" fill="{"#475569" if kind == "dust" else "#94a3b8"}"/>'
             f'<circle cx="{cx - 9}" cy="{cy - 13}" r="9" fill="{"#475569" if kind == "dust" else "#94a3b8"}"/>'
             f'<circle cx="{cx + 7}" cy="{cy - 15}" r="11" fill="{"#475569" if kind == "dust" else "#94a3b8"}"/>')
    if kind == "rain":
        return cloud + "".join(line(cx - 12 + i * 8, cy + 8, cx - 15 + i * 8, cy + 16, "#1d4ed8", 2) for i in range(4))
    if kind == "snow":
        return cloud + "".join(f'<circle cx="{cx - 12 + i * 8}" cy="{cy + 12 + (i % 2) * 4}" r="2.4" fill="#1d4ed8"/>' for i in range(4))
    if kind == "dust":
        return cloud
    # narrow winding road: warning triangle with a bend
    return (f'<path d="M{cx} {cy - 20} L{cx + 22} {cy + 16} L{cx - 22} {cy + 16} Z" fill="#fff" stroke="#c81e1e" stroke-width="4" stroke-linejoin="round"/>'
            f'<path d="M{cx - 4} {cy + 11} C {cx - 4} {cy + 2} {cx + 6} {cy + 2} {cx + 4} {cy - 4} L{cx + 2} {cy - 9}" fill="none" stroke="{INK}" stroke-width="2.5"/>')


def fog_symbol(cx, cy, color, rear=False):
    """Dashboard-style fog lamp symbol: a lamp with beam lines crossed by a wavy line (simplified)."""
    s = -1 if rear else 1
    lamp = f'<path d="M{cx + s * 2} {cy - 9} A 9 9 0 0 {1 if s > 0 else 0} {cx + s * 2} {cy + 9} Z" fill="none" stroke="{color}" stroke-width="2.2"/>'
    beams = "".join(line(cx - s * 3, cy - 7 + i * 7, cx - s * 12, cy - 7 + i * 7, color, 2) for i in range(3))
    wave = f'<path d="M{cx - s * 7} {cy - 11} q {s * 2} 4 0 7 q {-s * 2} 4 0 7 q {s * 2} 4 0 7" fill="none" stroke="{color}" stroke-width="1.6"/>'
    return lamp + beams + wave


def fog_matrix(lang):
    cols = L(lang, [("fog", ["Fog"], "thick"), ("rain", ["Rain"], "very heavy"), ("snow", ["Snow"], "heavy"), ("dust", ["Dust or", "smoke"], "dense"),
                    ("road", ["Narrow road", "with bends sign"], "")],
             [("fog", ["Niebla"], "espesa"), ("rain", ["Lluvia"], "muy intensa"), ("snow", ["Nevada"], "fuerte"), ("dust", ["Polvo", "o humo"], "densas"),
              ("road", ["Vía estrecha", "con curvas"], "")])
    p = []
    x0, cw = 190, 104
    for i, (kind, name, _) in enumerate(cols):
        cx = x0 + i * cw + cw / 2
        p.append(_icon(kind, cx, 36))
        p.append(lines(cx, 72, name, 11, 700, INK, "middle", 13))
    rows = [(L(lang, "Front fog lights", "Antiniebla delantera"), L(lang, "optional to fit; you MAY use them", "opcional; se PUEDE usar"), "#16a34a"),
            (L(lang, "Rear fog light", "Antiniebla trasera"), L(lang, "compulsory to fit; you MUST use it", "obligatoria; se DEBE usar"), "#f59e0b")]
    for r, (name, sub, col) in enumerate(rows):
        y = 100 + r * 64
        p.append(rect(10, y, 700, 56, "#f8fafc" if r == 0 else "#fff7ed", 6))
        p.append(rect(18, y + 12, 34, 32, "#1f2937", 5) + fog_symbol(35, y + 28, col, rear=(r == 1)))
        p.append(txt(60, y + 25, name, 12.5, 700, INK) + txt(60, y + 42, sub, 10.5, 400, SLATE))
        for i, (kind, _, strong) in enumerate(cols):
            cx = x0 + i * cw + cw / 2
            if r == 1 and kind == "road":
                p.append(cross(cx, y + 24, 11))
            else:
                p.append(tick(cx, y + 22, 11))
                if r == 1 and strong:
                    p.append(txt(cx, y + 48, strong, 10.5, 800, "#b45309", "middle"))
                if r == 0 and kind == "rain":
                    p.append(txt(cx, y + 48, L(lang, "heavy", "intensa"), 10.5, 700, SLATE, "middle"))
    p.append(txt(360, 248, L(lang, "Rear fog light: only when conditions are ESPECIALLY bad, never just for a narrow winding road.",
                                "Antiniebla trasera: solo con condiciones ESPECIALMENTE adversas, nunca solo por una vía estrecha con curvas."), 11.5, 700, TEAL, "middle"))
    return svg(720, 258, "".join(p), L(lang, "When to use fog lights", "Cuándo usar las luces antiniebla"))


# ---------------------------------------------------------------- D3 dazzle when overtaking at night
def _beam(x, y, length, right=True, wide=False):
    s = 1 if right else -1
    h = 14 if wide else 8
    x2 = x + s * length
    return f'<path d="M{x} {y - 4} L{x2} {y - h} L{x2} {y + h} L{x} {y + 4} Z" fill="{BEAM}" opacity=".75"/>'


def overtake_dazzle(lang):
    p = []
    steps = L(lang,
              [("1", "Behind: both on dipped beam", "main beam would dazzle via mirrors"),
               ("2", "Pulling out: still dipped", "you are not yet level with them"),
               ("3", "Level: you may switch to main beam", "now the overtaken driver dips"),
               ("4", "Past: back on the right", "dip again if anyone could be dazzled")],
              [("1", "Detrás: ambos con luz de cruce", "la larga deslumbraría por los espejos"),
               ("2", "Al salir: sigue con luz de cruce", "aún no estás en paralelo"),
               ("3", "En paralelo: puedes poner la larga", "ahora el adelantado pone la de cruce"),
               ("4", "Pasado: vuelves a la derecha", "cruce otra vez si puedes deslumbrar")])
    positions = [((80, 70, False), (200, 70, False)),     # (overtaker x, y, main), (overtaken x, y, main)
                 ((150, 46, False), (210, 70, False)),
                 ((260, 46, True), (262, 70, False)),
                 ((380, 70, False), (230, 70, False))]
    for i, (n, head, sub) in enumerate(steps):
        oy = i * 64
        p.append(rect(10, 30 + oy, 440, 58, NIGHT, 6))
        p.append(line(14, 58 + oy, 446, 58 + oy, "#94a3b8", 1.5, "10 8"))
        (ax, ay, amain), (bx, by, bmain) = positions[i]
        p.append(_beam(bx + 20, by + oy, 90 if bmain else 50, True, bmain) + car_h(bx, by + oy, "#facc15", True, 34, 16))
        p.append(_beam(ax + 20, ay + oy, 130 if amain else 50, True, amain) + car_h(ax, ay + oy, LAMP_RED, True, 34, 16))
        p.append(f'<circle cx="474" cy="{55 + oy}" r="11" fill="{NAVY}"/>' + txt(474, 59 + oy, n, 11.5, 800, "#fff", "middle"))
        p.append(txt(492, 54 + oy, head, 12, 700, INK) + txt(492, 70 + oy, sub, 10.5, 400, SLATE))
    p.append(txt(20, 20, L(lang, "Red car overtakes the yellow one at night", "El coche rojo adelanta al amarillo de noche"), 11.5, 700, SLATE))
    return svg(720, 292, "".join(p), L(lang, "Avoiding dazzle when overtaking", "Evitar deslumbrar al adelantar"))


# ---------------------------------------------------------------- D4 dazzle on bends
def curve_dazzle(lang):
    p = [rect(10, 20, 380, 230, VERGE, 8)]
    # a bend: the road comes up from the bottom and turns right
    p.append('<path d="M120 250 L120 150 Q 120 70 220 70 L390 70" fill="none" stroke="#4b5563" stroke-width="84"/>')
    p.append('<path d="M120 250 L120 150 Q 120 70 220 70 L390 70" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="12 9"/>')
    # car A goes up and enters the bend to the right; its straight beam crosses the oncoming lane
    p.append(f'<path d="M140 180 L118 70 L176 74 Z" fill="{BEAM}" opacity=".85"/>')
    p.append(f'<rect x="130" y="180" width="20" height="36" rx="6" fill="#1d4ed8"/>')
    # car B comes the other way and enters the bend to its left; its beam goes off the road
    p.append(f'<path d="M290 50 L190 22 L200 62 Z" fill="{BEAM}" opacity=".85"/>')
    p.append(f'<rect x="290" y="40" width="36" height="20" rx="6" fill="#b45309"/>')
    p.append(f'<circle cx="140" cy="232" r="11" fill="{NAVY}"/>' + txt(140, 236, "A", 11.5, 800, "#fff", "middle"))
    p.append(f'<circle cx="338" cy="36" r="11" fill="{NAVY}"/>' + txt(338, 40, "B", 11.5, 800, "#fff", "middle"))
    p.append(lines(410, 60, L(lang, ["A’s bend turns right: its headlights", "sweep straight across the oncoming", "lane, so A dips first."],
                                  ["La curva de A gira a la derecha: sus", "faros barren el carril contrario, así", "que A pone primero la luz de cruce."]), 12, 400, INK, "start", 17))
    p.append(lines(410, 150, L(lang, ["B’s bend turns left: its beam goes", "to the outside of the road, so B", "may switch a little later."],
                                   ["La curva de B gira a la izquierda: su", "haz se va al exterior de la vía, así", "que B puede cambiar algo más tarde."]), 12, 400, INK, "start", 17))
    return svg(720, 262, "".join(p), L(lang, "Dazzle on a bend", "Deslumbramiento en las curvas"))


# ---------------------------------------------------------------- D5 if oncoming lights dazzle you
def dazzled_view(lang):
    p = [rect(10, 20, 400, 230, NIGHT, 8)]
    p.append('<path d="M40 250 L190 90 L230 90 L380 250 Z" fill="#374151"/>')
    p.append(line(210, 96, 210, 250, "#e5e7eb", 2, "10 9"))
    p.append(line(226, 92, 356, 250, "#fde68a", 4))           # right edge line, highlighted
    p.append(line(194, 92, 64, 250, "#e5e7eb", 2))
    p.append(glow(185, 104, 6, "#fff7d6", "#ffffff") + glow(203, 104, 6, "#fff7d6", "#ffffff"))
    p.append(f'<path d="M194 104 L60 50 L60 190 Z" fill="#fff7d6" opacity=".18"/>')
    p.append(f'<path d="M150 236 Q 230 210 300 200" fill="none" stroke="#fde68a" stroke-width="2" stroke-dasharray="5 4"/>')
    p.append(f'<path d="M296 194 L306 199 L297 206 Z" fill="#fde68a"/>')
    p.append(txt(320, 190, L(lang, "look here", "mira aquí"), 12, 800, "#fde68a"))
    items = L(lang,
              [("Oncoming lights", ["look to the right, along the line", "between carriageway and shoulder;", "close your left eye"]),
               ("Lights behind you", ["tilt the mirror, or shift", "your position a little"]),
               ("Dazzled anyway", ["slow down, even to a stop,", "without moving onto the shoulder"])],
              [("Luces de frente", ["mira a la derecha, guiándote por", "la línea entre calzada y arcén;", "cierra el ojo izquierdo"]),
               ("Luces por detrás", ["cambia la orientación del espejo", "o cambia un poco de posición"]),
               ("Si te deslumbran", ["reduce, incluso hasta parar,", "sin salirte al arcén"])])
    y = 48
    for head, body in items:
        p.append(txt(430, y, head, 12.5, 700, INK) + lines(430, y + 18, body, 11.5, 400, SLATE, "start", 15))
        y += 30 + 15 * len(body) + 4
    return svg(720, 262, "".join(p), L(lang, "When lights dazzle you", "Cuando te deslumbran"))


# ---------------------------------------------------------------- D6 lights that show where a vehicle is
def presence(lang):
    p = []
    cap = L(lang,
            [("Car, front", "position lights: white"), ("Car, rear", "position lights: red"), ("Trailer, rear", "triangular reflectors: trailers only"),
             ("Wide lorry, rear", "clearance lights: red, over 2.10 m")],
            [("Turismo, delante", "luces de posición: blancas"), ("Turismo, detrás", "luces de posición: rojas"), ("Remolque, detrás", "catadióptricos triangulares: solo remolques"),
             ("Camión ancho, detrás", "luces de gálibo: rojas, más de 2,10 m")])
    for i in range(4):
        ox = 10 + i * 178
        cx = ox + 84
        p.append(rect(ox, 10, 168, 150, NIGHT, 8))
        if i in (0, 1):
            p.append(rect(cx - 56, 70, 112, 50, "#475569", 10) + f'<path d="M{cx - 44} 70 L{cx - 32} 36 L{cx + 32} 36 L{cx + 44} 70 Z" fill="#334155"/>')
            col = "#ffffff" if i == 0 else LAMP_RED
            p.append(glow(cx - 42, 86, 4.5, "#fff7d6" if i == 0 else LAMP_RED, col) + glow(cx + 42, 86, 4.5, "#fff7d6" if i == 0 else LAMP_RED, col))
            p.append(rect(cx - 20, 100, 40, 10, "#e5e7eb", 2))
        elif i == 2:
            p.append(rect(cx - 60, 76, 120, 36, "#475569", 4) + line(cx, 112, cx, 140, "#475569", 4))
            for sx in (-1, 1):
                x = cx + sx * 46
                p.append(f'<path d="M{x} 84 L{x + 8} 98 L{x - 8} 98 Z" fill="#b91c1c" stroke="#fca5a5" stroke-width="1"/>')
                p.append(glow(x, 106, 3.5, LAMP_RED))
        else:
            p.append(rect(cx - 60, 30, 120, 100, "#64748b", 4))
            for x in (cx - 56, cx + 56):
                p.append(glow(x, 34, 4, LAMP_RED))
                p.append(glow(x, 118, 4, LAMP_RED))
            p.append(line(cx - 60, 140, cx + 60, 140, "#fde68a", 1.5) + txt(cx, 154, "&gt; 2,10 m" if lang == "es" else "&gt; 2.10 m", 10.5, 700, "#fde68a", "middle"))
        p.append(txt(cx, 180, cap[i][0], 12, 700, INK, "middle"))
        p.append(txt(cx, 196, cap[i][1], 10.5, 400, SLATE, "middle"))
    return svg(720, 206, "".join(p), L(lang, "Lights and reflectors that show a vehicle is there", "Luces y catadióptricos que indican la presencia"))
