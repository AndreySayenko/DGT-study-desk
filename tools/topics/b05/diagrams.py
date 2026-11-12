# -*- coding: utf-8 -*-
"""Original SVG diagrams for Topic 5 (EN/ES). No third-party artwork is used. Each function takes the language
("en" or "es") and returns an SVG string. Figures sit on a light background in both themes."""

from svgkit import NAVY, TEAL, RED, SLATE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect, car_v, car_h, arrow_v, arrow_h, tick, cross, ASPHALT, SHOULDER, VERGE, WHITE  # noqa: F401

AMBER_ON = "#f59e0b"
AMBER_OFF = "#92400e"
SKIN = "#d6a77a"
MUTED = "#64748b"
KERB = "#d6d3d1"
VEST = "#d9f99d"


def L(lang, en, es):
    return en if lang == "en" else es


def line(x1, y1, x2, y2, color=WHITE, width=2, dash=None, extra=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{d}{extra}/>'


def badge(cx, cy, s, fill=NAVY, r=11):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>' + txt(cx, cy + 4, s, 11.5, 800, "#fff", "middle")


# ---------------------------------------------------------------- D1 lights and arm signals
def _car_rear(signal):
    """Car seen from behind, centred on x = 0, wheels on y = 0, 150 wide. signal: left | right | reverse | slow."""
    g = []
    if signal == "slow":
        for sx in (-60, 60):
            g.append(f'<circle cx="{sx}" cy="-53" r="17" fill="#fca5a5" opacity=".55"/>')
    g.append(rect(-62, -16, 22, 16, "#1f2937", 3) + rect(40, -16, 22, 16, "#1f2937", 3))
    g.append('<path d="M-58 -66 L-44 -104 L44 -104 L58 -66 Z" fill="#475569"/>')
    g.append('<path d="M-50 -70 L-39 -98 L39 -98 L50 -70 Z" fill="#cbd5e1"/>')
    g.append(rect(-75, -68, 150, 54, "#64748b", 10))
    tail = "#ef4444" if signal == "slow" else "#991b1b"
    g.append(rect(-71, -60, 22, 9, tail, 2) + rect(49, -60, 22, 9, tail, 2))
    g.append(rect(-71, -49, 22, 5, AMBER_ON if signal == "left" else AMBER_OFF, 1.5))
    g.append(rect(49, -49, 22, 5, AMBER_ON if signal == "right" else AMBER_OFF, 1.5))
    rev = "#ffffff" if signal == "reverse" else "#94a3b8"
    g.append(rect(-44, -32, 14, 6, rev, 1.5, ' stroke="#475569" stroke-width=".8"') + rect(30, -32, 14, 6, rev, 1.5, ' stroke="#475569" stroke-width=".8"'))
    if signal == "left":
        g.append(f'<circle cx="-60" cy="-47" r="12" fill="{AMBER_ON}" opacity=".35"/>')
    if signal == "right":
        g.append(f'<circle cx="60" cy="-47" r="12" fill="{AMBER_ON}" opacity=".35"/>')
    if signal == "reverse":
        g.append('<circle cx="-37" cy="-29" r="10" fill="#e0f2fe" opacity=".7"/><circle cx="37" cy="-29" r="10" fill="#e0f2fe" opacity=".7"/>')
    g.append(rect(-24, -38, 48, 12, "#fff", 2, ' stroke="#94a3b8" stroke-width="1"'))
    # driver's arm out of the left window (left as seen from behind)
    sh = (-46, -84)
    if signal == "left":
        g.append(line(*sh, -112, -84, SKIN, 7, extra=' stroke-linecap="round"') + f'<ellipse cx="-118" cy="-84" rx="7" ry="4" fill="{SKIN}"/>')
    elif signal == "right":
        g.append(line(*sh, -86, -84, SKIN, 7, extra=' stroke-linecap="round"') + line(-86, -84, -86, -122, SKIN, 7, extra=' stroke-linecap="round"'))
        g.append(f'<ellipse cx="-86" cy="-129" rx="4.5" ry="8" fill="{SKIN}"/>')
    elif signal == "reverse":
        g.append(line(*sh, -112, -84, SKIN, 7, extra=' stroke-linecap="round"') + f'<ellipse cx="-117" cy="-84" rx="4" ry="8.5" fill="{SKIN}"/>')
    elif signal == "slow":
        for y2, op in ((-108, ".35"), (-60, ".35"), (-84, "1")):
            g.append(line(*sh, -108, y2, SKIN, 6, extra=f' stroke-linecap="round" opacity="{op}"'))
        g.append(line(-124, -112, -124, -56, INK, 1.8))
        g.append('<path d="M-129 -106 L-124 -114 L-119 -106 Z" fill="#0f172a"/><path d="M-129 -62 L-124 -54 L-119 -62 Z" fill="#0f172a"/>')
    return "".join(g)


def arm_signals(lang):
    rows = L(lang,
             [("Left", "left indicator", "arm straight out"), ("Right", "right indicator", "forearm up, palm open"),
              ("Reversing", "reversing lights", "arm out, palm back"), ("Slowing sharply", "brake lights", "arm up and down")],
             [("Izquierda", "intermitente izquierdo", "brazo horizontal"), ("Derecha", "intermitente derecho", "antebrazo hacia arriba"),
              ("Marcha atrás", "luz de marcha atrás", "brazo, palma hacia atrás"), ("Frenar mucho", "luces de freno", "brazo de arriba abajo")])
    p = []
    for i, sig in enumerate(("left", "right", "reverse", "slow")):
        cx = 180 * i + 110
        p.append(f'<g transform="translate({cx} 150) scale(0.72)">' + _car_rear(sig) + "</g>")
        head, light, arm = rows[i]
        p.append(txt(cx - 20, 176, head, 12.5, 700, INK, "middle"))
        p.append(txt(cx - 20, 193, L(lang, "Light: ", "Luz: ") + light, 10.5, 400, SLATE, "middle"))
        p.append(txt(cx - 20, 208, L(lang, "Arm: ", "Brazo: ") + arm, 10.5, 400, SLATE, "middle"))
        if i:
            p.append(line(180 * i, 30, 180 * i, 210, "#e2e8f0", 1.2))
    p.append(txt(360, 236, L(lang, "If the lights and the arm say different things, the arm signal prevails.",
                                "Si las luces y el brazo dicen cosas distintas, prevalece la señal del brazo."), 12.5, 700, TEAL, "middle"))
    return svg(720, 246, "".join(p), L(lang, "Light and arm signals", "Señales luminosas y con el brazo"))


# ---------------------------------------------------------------- D2 the three kinds of immobilisation
def immobilisations(lang):
    cards = L(lang,
              [("Detention", "detención", ["Imposed, not chosen:", "emergency, traffic needs,", "a rule, agent, sign or light.", "Not a manoeuvre."], "#b42318"),
               ("Stop", "parada", ["Chosen, for less than", "2 minutes, and the driver", "does not abandon the", "vehicle."], "#b45309"),
               ("Parking", "estacionamiento", ["Chosen, and it is", "neither a detention", "nor a stop."], NAVY)],
              [("Detención", "", ["Impuesta, no voluntaria:", "emergencia, circulación,", "una norma, agente, señal", "o semáforo. No es maniobra."], "#b42318"),
               ("Parada", "", ["Voluntaria, durante menos", "de 2 minutos y sin que el", "conductor abandone", "el vehículo."], "#b45309"),
               ("Estacionamiento", "", ["Voluntaria, y no es", "ni detención ni parada."], NAVY)])
    p = []
    for i, (name, term, body, col) in enumerate(cards):
        x = 10 + i * 238
        cx = x + 110
        p.append(rect(x, 8, 220, 176, "#f8fafc", 10, f' stroke="{col}" stroke-width="2"'))
        if i == 0:
            p.append(rect(cx - 11, 22, 22, 50, "#1f2937", 5) + f'<circle cx="{cx}" cy="34" r="6.5" fill="#ef4444"/><circle cx="{cx}" cy="49" r="6.5" fill="#374151"/><circle cx="{cx}" cy="64" r="6.5" fill="#374151"/>')
        elif i == 1:
            p.append(f'<circle cx="{cx}" cy="47" r="25" fill="#fff" stroke="{col}" stroke-width="3"/>' + line(cx, 47, cx, 30, INK, 3) + line(cx, 47, cx + 11, 53, INK, 3)
                     + txt(cx + 46, 53, "&lt; 2 min", 13, 800, col, "middle"))
        else:
            p.append(rect(cx - 25, 22, 50, 50, "#1d4ed8", 6) + txt(cx, 59, "P", 34, 800, "#fff", "middle"))
        p.append(txt(cx, 98, name + (f" (<tspan font-style='italic'>{term}</tspan>)" if term else ""), 13, 700, INK, "middle"))
        p.append(lines(cx, 118, body, 11.5, 400, SLATE, "middle", 15))
    return svg(720, 192, "".join(p), L(lang, "Detention, stop and parking", "Detención, parada y estacionamiento"))


# ---------------------------------------------------------------- D3 overtaking a cyclist
def bike(cx, cy):
    return (rect(cx - 14, cy - 2.5, 28, 5, "#111827", 2) + f'<circle cx="{cx}" cy="{cy}" r="6" fill="#7c3aed"/>'
            + f'<circle cx="{cx + 2}" cy="{cy}" r="3" fill="#fde68a"/>')


def ghost_h(cx, cy):
    return f'<rect x="{cx - 20}" y="{cy - 10}" width="40" height="20" rx="6" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="4 3"/>'


def overtake_cyclist(lang):
    top, mid, bot = 60, 110, 160
    p = [rect(0, 40, 720, 140, VERGE, 8), rect(0, top, 720, bot - top, ASPHALT), rect(0, bot, 720, 12, SHOULDER)]
    p.append(line(6, mid, 714, mid, WHITE, 2, "14 10"))
    p.append(line(0, bot, 720, bot, WHITE, 2))
    p.append(bike(420, 146) + arrow_h(438, 462, 146, "#fde68a", 2))
    p.append(ghost_h(150, 135))
    p.append(car_h(410, 84, "#1d4ed8", right=True))
    p.append(ghost_h(650, 135))
    p.append(f'<path d="M172 132 C 230 132 250 86 300 86" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="6 4"/>')
    p.append(f'<path d="M520 86 C 570 86 590 132 626 132" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="6 4"/>')
    # lateral gap
    p.append(line(470, 95, 470, 140, "#fde68a", 2) + line(464, 95, 476, 95, "#fde68a", 2) + line(464, 140, 476, 140, "#fde68a", 2))
    p.append(rect(480, 106, 62, 22, "#fde68a", 5) + txt(511, 121, "≥ 1,5 m" if lang == "es" else "≥ 1.5 m", 12, 800, INK, "middle"))
    p.append(badge(150, 112, "1") + badge(410, 62, "2") + badge(650, 112, "3"))
    steps = L(lang,
              [("1", "Look and signal", ["check there is room to pass", "and room to come back"]),
               ("2", "Pass with a wide gap", ["≥ 1.5 m; out of town, also", "20 km/h below the limit"]),
               ("3", "Back to the right", ["gradually, once you see", "the cyclist in the mirror"])],
              [("1", "Mira y señaliza", ["comprueba que hay espacio", "para pasar y para volver"]),
               ("2", "Pasa con margen", ["≥ 1,5 m; fuera de poblado,", "además 20 km/h menos"]),
               ("3", "Vuelve a la derecha", ["de forma gradual, al ver", "al ciclista en el espejo"])])
    for i, (n, head, sub) in enumerate(steps):
        x = 10 + i * 238
        p.append(badge(x + 11, 208, n) + txt(x + 28, 212, head, 12, 700, INK) + lines(x + 28, 228, sub, 10.5, 400, SLATE, "start", 14))
    p.append(txt(360, 26, L(lang, "Overtaking a cyclist: move partly or fully into the next lane (a full lane change if there are 2+ lanes your way)",
                            "Adelantar a un ciclista: ocupar parcial o totalmente el carril contiguo (cambio completo si hay 2 o más en tu sentido)"), 11.5, 400, SLATE, "middle"))
    return svg(720, 252, "".join(p), L(lang, "Overtaking a cyclist", "Adelantar a un ciclista"))


# ---------------------------------------------------------------- D4 where to position before turning
def _turn_panel(ox, kind, lang):
    out = [rect(ox, 20, 170, 190, VERGE, 8)]
    x1, x2 = ox + 45, ox + 125
    out.append(rect(ox, 40, 170, 56, ASPHALT))
    out.append(rect(x1, 96, x2 - x1, 114, ASPHALT))
    out.append(line(ox + 4, 68, x1 - 4, 68, WHITE, 1.5, "8 6") + line(x2 + 4, 68, ox + 166, 68, WHITE, 1.5, "8 6"))
    cy = 172
    if kind == "right":
        out.append(line(ox + 85, 100, ox + 85, 208, WHITE, 1.5, "8 6"))
        cx = ox + 112
        path = f"M{cx} {cy - 22} C {cx} 110 {cx + 4} 84 {ox + 160} 84"
    elif kind == "oneway":
        out.append(line(ox + 85, 100, ox + 85, 208, WHITE, 1.5, "8 6"))
        out.append(arrow_v(ox + 100, 204, 186, "#cbd5e1", 2))
        cx = ox + 58
        path = f"M{cx} {cy - 22} C {cx} 100 {cx - 4} 56 {ox + 10} 56"
    elif kind == "marked":
        out.append(line(ox + 85, 100, ox + 85, 208, WHITE, 2.5))
        cx = ox + 98
        path = f"M{cx} {cy - 22} C {cx} 100 {cx - 10} 56 {ox + 10} 56"
    else:   # three lanes, broken lines: centre lane
        w = (x2 - x1) / 3
        out.append(line(x1 + w, 100, x1 + w, 208, WHITE, 1.5, "8 6") + line(x1 + 2 * w, 100, x1 + 2 * w, 208, WHITE, 1.5, "8 6"))
        cx = round(x1 + 1.5 * w, 1)
        path = f"M{cx} {cy - 22} C {cx} 100 {cx - 10} 56 {ox + 10} 56"
    out.append(f'<path d="{path}" fill="none" stroke="#fde68a" stroke-width="2.5"/>')
    out.append(car_v(cx, cy, "#1d4ed8", up=True))
    return "".join(out)


def turn_positions(lang):
    kinds = ["right", "oneway", "marked", "three"]
    caps = L(lang,
             [("Turning right", "keep close to the right edge"), ("Left, one-way road", "keep close to the left edge"),
              ("Left, two-way, marked", "keep next to the centre line"), ("Left, 3 lanes, broken lines", "move into the centre lane")],
             [("Giro a la derecha", "ceñirse al borde derecho"), ("Izquierda, sentido único", "ceñirse al borde izquierdo"),
              ("Izquierda, doble sentido", "ceñirse a la marca central"), ("Izquierda, 3 carriles", "colocarse en el carril central")])
    p = []
    for i, k in enumerate(kinds):
        ox = 6 + i * 179
        p.append(_turn_panel(ox, k, lang))
        p.append(txt(ox + 85, 230, caps[i][0], 12, 700, INK, "middle"))
        p.append(txt(ox + 85, 246, caps[i][1], 11, 400, SLATE, "middle"))
    return svg(720, 256, "".join(p), L(lang, "Where to position before turning", "Dónde colocarse antes de girar"))


# ---------------------------------------------------------------- D5 parking on a slope
def _parked(cx, cy, wheel_angle):
    """Car seen from above facing right, kerb below it; front wheels turned by wheel_angle (negative = away from kerb)."""
    out = []
    for wx, ang in ((cx - 34, 0), (cx + 30, wheel_angle)):
        for wy in (cy - 23, cy + 23):
            out.append(f'<rect x="{wx - 9}" y="{wy - 4}" width="18" height="8" rx="2" fill="#111827" transform="rotate({ang} {wx} {wy})"/>')
    out.append(rect(cx - 52, cy - 21, 104, 42, "#1d4ed8", 9) + rect(cx + 16, cy - 16, 16, 32, "#cbd5e1", 3))
    return "".join(out)


def park_slope(lang):
    p = []
    for i, (up, ang) in enumerate(((True, -28), (False, 28))):
        ox = 10 + i * 355
        p.append(rect(ox, 30, 340, 120, ASPHALT, 8) + rect(ox, 150, 340, 14, KERB))
        p.append(_parked(ox + 170, 118, ang))
        lab = L(lang, "uphill" if up else "downhill", "cuesta arriba" if up else "cuesta abajo")
        if up:
            p.append(f'<path d="M{ox + 20} 60 L{ox + 120} 44" stroke="#fde68a" stroke-width="2.5"/><path d="M{ox + 112} 39 L{ox + 124} 43 L{ox + 115} 51 Z" fill="#fde68a"/>')
        else:
            p.append(f'<path d="M{ox + 20} 44 L{ox + 120} 60" stroke="#fde68a" stroke-width="2.5"/><path d="M{ox + 115} 53 L{ox + 124} 61 L{ox + 112} 65 Z" fill="#fde68a"/>')
        p.append(txt(ox + 134, 56, lab, 12, 700, "#fde68a"))
        title = L(lang, "Facing uphill", "Cuesta arriba") if up else L(lang, "Facing downhill", "Cuesta abajo")
        gear = L(lang, "1st gear engaged", "primera velocidad") if up else L(lang, "reverse gear engaged", "marcha atrás")
        wheels = (L(lang, "front wheels towards the centre of the road", "ruedas hacia el centro de la calzada") if up else
                  L(lang, "front wheels towards the kerb", "ruedas hacia el bordillo"))
        p.append(txt(ox + 170, 20, title, 13, 700, INK, "middle"))
        p.append(lines(ox + 170, 184, [gear, wheels], 11.5, 400, INK, "middle", 16))
    p.append(lines(360, 230, L(lang, ["Always: engine off, parking brake on. Automatic gearbox: P.",
                                       "The kerb trick is compulsory for vehicles over 3,500 kg, buses and combinations, unless they use proper chocks."],
                                ["Siempre: motor apagado y freno de estacionamiento. Cambio automático: P.",
                                 "Más de 3.500 kg, autobuses y conjuntos: calzos adecuados o una rueda directriz contra el bordillo."]), 11.5, 700, TEAL, "middle", 16))
    return svg(720, 256, "".join(p), L(lang, "Parking on a slope", "Estacionar en pendiente"))


# ---------------------------------------------------------------- D6 broken down on an interurban road
def breakdown(lang):
    p = [rect(0, 20, 720, 210, VERGE, 8)]
    p.append(rect(0, 40, 720, 104, ASPHALT) + rect(0, 144, 720, 26, SHOULDER))
    p.append(line(6, 92, 714, 92, WHITE, 2, "14 10") + line(0, 144, 720, 144, WHITE, 2))
    p.append(rect(0, 178, 720, 5, "#94a3b8"))     # safety barrier
    for x in range(10, 720, 40):
        p.append(rect(x, 176, 4, 9, "#64748b"))
    p.append(car_h(120, 118, "#94a3b8", right=True) + arrow_h(146, 186, 118, WHITE))
    # broken-down car on the shoulder with hazard lights and V-16 on the roof
    cx, cy = 380, 157
    p.append(rect(cx - 30, cy - 13, 60, 26, "#475569", 6) + rect(cx + 10, cy - 9, 10, 18, "#cbd5e1", 2))
    for dx in (-30, 30):
        for dy in (-13, 13):
            p.append(f'<circle cx="{cx + dx}" cy="{cy + dy}" r="5" fill="{AMBER_ON}"/>')
    for k in range(8):
        import math
        a = math.radians(k * 45)
        p.append(line(cx - 6 + 10 * math.cos(a), cy + 10 * math.sin(a), cx - 6 + 19 * math.cos(a), cy + 19 * math.sin(a), "#facc15", 2))
    p.append(f'<circle cx="{cx - 6}" cy="{cy}" r="6.5" fill="#facc15" stroke="#92400e" stroke-width="1.5"/>')
    # occupants behind the barrier, wearing vests
    for x in (440, 462, 484):
        p.append(f'<circle cx="{x}" cy="204" r="8" fill="{VEST}" stroke="#65a30d" stroke-width="2"/>')
    p.append(f'<path d="M398 166 C 410 190 420 200 432 204" fill="none" stroke="#fde68a" stroke-width="2" stroke-dasharray="4 3"/>')
    items = L(lang,
              [("1", "Hazard lights on"), ("2", "V-16 light on the roof (360°, connected)"), ("3", "Vest on before stepping onto road or shoulder"),
               ("4", "Get out away from traffic; wait behind the barrier")],
              [("1", "Luz de emergencia"), ("2", "V-16 en el techo (360°, conectada)"), ("3", "Chaleco antes de pisar la calzada o el arcén"),
               ("4", "Salir lejos del tráfico; esperar tras la barrera")])
    p.append(badge(380, 132, "1", TEAL) + badge(352, 132, "2", TEAL) + badge(512, 204, "3", TEAL) + badge(420, 182, "4", TEAL))
    for i, (n, s) in enumerate(items):
        x = 10 + (i % 2) * 360
        y = 252 + (i // 2) * 22
        p.append(badge(x + 11, y - 4, n, TEAL) + txt(x + 28, y, s, 11.5, 600, INK))
    p.append(txt(360, 12, L(lang, "The warning triangle no longer replaces the V-16; it may be used as well.",
                            "El triángulo ya no sustituye a la V-16; puede colocarse además."), 11.5, 400, SLATE, "middle"))
    return svg(720, 284, "".join(p), L(lang, "Broken down on an interurban road", "Avería en una vía interurbana"))
