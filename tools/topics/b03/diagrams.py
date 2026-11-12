# -*- coding: utf-8 -*-
"""Original SVG diagrams for Topic 3 (EN/ES). No third-party artwork is used. Each function takes the language
("en" or "es") and returns an SVG string. Figures sit on a light background in both themes."""

from svgkit import NAVY, TEAL, RED, SLATE, INK, svg, txt, lines  # noqa: F401

# The speed-range chart uses two series colours checked for colour-blind separation (blue / amber).
MOTORWAY = "#1d4ed8"
OTHER = "#b45309"
GRID = "#e2e8f0"
MUTED = "#64748b"
ASPHALT = "#4b5563"
PAVING = "#d6d3d1"
KERB = "#e5e7eb"
MEDIAN = "#86a96b"
WHITE = "#ffffff"
SIGN_RED = "#c81e1e"
SIGN_BLUE = "#1e3a8a"


def L(lang, en, es):
    return en if lang == "en" else es


def rect(x, y, w, h, fill, rx=0, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{extra}/>'


def line(x1, y1, x2, y2, color=WHITE, width=2, dash=None, extra=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{d}{extra}/>'


def _num(cx, cy, r, n, fill):
    n = str(n)
    size = r * (0.86 if len(n) < 3 else 0.68)
    return txt(cx, round(cy + size * 0.36, 1), n, round(size, 1), 800, fill, "middle")


def max_sign(cx, cy, r, n):
    """Maximum-speed sign: white disc, red ring, black figure."""
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{SIGN_RED}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{round(r * 0.78, 1)}" fill="#fff"/>' + _num(cx, cy, r, n, INK))


def min_sign(cx, cy, r, n):
    """Minimum-speed sign: blue disc, white figure."""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{SIGN_BLUE}"/>' + _num(cx, cy, r, n, "#fff")


def v4_disc(cx, cy, r, n):
    """V-4 plate: white disc with a black rim and black figure."""
    w = max(1.2, r * 0.07)
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="{INK}" stroke-width="{round(w, 1)}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{round(r * 0.84, 1)}" fill="none" stroke="{INK}" stroke-width="{round(w / 2, 1)}"/>'
            + _num(cx, cy, r, n, INK))


# ---------------------------------------------------------------- D1 speed concepts on one scale
def speed_band(lang):
    x0, x1 = 30, 690
    k = (x1 - x0) / 140

    def X(v):
        return round(x0 + v * k, 1)

    p = [txt(360, 18, L(lang, "A car on a motorway or dual carriageway", "Un turismo en autopista o autovía"), 13, 700, INK, "middle")]
    # signs over the two limits
    p.append(min_sign(X(60), 50, 16, 60))
    p.append(txt(X(60) + 22, 54, L(lang, "minimum", "mínima"), 11, 700, SLATE))
    p.append(max_sign(X(120), 50, 16, 120))
    p.append(txt(X(120) - 22, 54, L(lang, "maximum", "máxima"), 11, 700, SLATE, "end"))
    # the three zones
    y, h = 74, 30
    p.append(rect(X(0), y, X(60) - X(0) - 1, h, "#fde7c7", 4))
    p.append(rect(X(60) + 1, y, X(120) - X(60) - 2, h, "#d1fae5", 4))
    p.append(rect(X(120) + 1, y, X(140) - X(120) - 1, h, "#fecaca", 4))
    p.append(txt((X(0) + X(60)) / 2, y + 19, L(lang, "Abnormally low", "Anormalmente reducida"), 12, 700, "#92400e", "middle"))
    p.append(txt((X(60) + X(120)) / 2, y + 19, L(lang, "Allowed: choose the adequate speed", "Permitido: elige la velocidad adecuada"), 12, 700, "#065f46", "middle"))
    p.append(txt((X(120) + X(140)) / 2, y + 19, L(lang, "Speeding", "Exceso"), 12, 700, "#991b1b", "middle"))
    for v in (0, 60, 120, 140):
        p.append(txt(X(v), y + h + 15, f"{v}" + (" km/h" if v == 140 else ""), 10.5, 400, MUTED, "end" if v == 140 else ("start" if v == 0 else "middle")))
    # snow example at 100 km/h
    sx = X(100)
    p.append(f'<path d="M{sx - 6} {y + h + 2} L{sx + 6} {y + h + 2} L{sx} {y + h - 6} Z" fill="{INK}"/>')
    p.append(line(sx, y + h + 2, sx, y + h + 34, INK, 1.5, "3 3"))
    p.append(lines(sx, y + h + 50, L(lang, ["Heavy snow at 100 km/h: inside the limits,", "but too fast for the conditions: velocidad excesiva"],
                                       ["Con mucha nieve a 100 km/h: dentro de los límites,", "pero demasiado rápido: velocidad excesiva"]), 11.5, 400, INK, "middle", 15))
    p.append(lines(X(30), y + h + 50, L(lang, ["Below 60 km/h without a reason:", "you hold up the traffic behind"],
                                          ["Por debajo de 60 km/h sin motivo:", "entorpeces a los que vienen detrás"]), 11.5, 400, INK, "middle", 15))
    return svg(720, 176, "".join(p), L(lang, "Speed concepts on one scale", "Conceptos de velocidad en una escala"))


# ---------------------------------------------------------------- D2 generic limits out of town as ranges
def limits_ranges(lang):
    gx0, gx1 = 270, 690
    k = (gx1 - gx0) / 130

    def X(v):
        return round(gx0 + v * k, 1)

    rows = {
        "en": [("Cars and motorcycles", "+ motorhomes ≤ 3,500 kg, pick-ups", (60, 120), (45, 90)),
               ("Buses", "+ car-derived vans, adaptable mixed", (60, 100), (45, 90)),
               ("Lorries, vans and the rest", "+ motorhomes &gt; 3,500 kg, with trailer", (60, 90), (40, 80))],
        "es": [("Turismos y motocicletas", "+ autocaravanas ≤ 3.500 kg, pick-up", (60, 120), (45, 90)),
               ("Autobuses", "+ derivados de turismo, mixtos adaptables", (60, 100), (45, 90)),
               ("Camiones, furgonetas y resto", "+ autocaravanas &gt; 3.500 kg, con remolque", (60, 90), (40, 80))],
    }[lang]
    p = []
    # legend
    lg = [(MOTORWAY, L(lang, "Autopista and autovía", "Autopista y autovía")),
          (OTHER, L(lang, "Vía para automóviles and carretera convencional", "Vía para automóviles y carretera convencional"))]
    lx = 20
    for col, name in lg:
        p.append(rect(lx, 9, 14, 10, col, 2))
        p.append(txt(lx + 20, 18, name, 11.5, 600, INK))
        lx += 34 + len(name) * 6.4
    top = 36
    rh = 66
    # grid
    for v in (0, 30, 60, 90, 120):
        p.append(line(X(v), top, X(v), top + rh * 3 - 6, GRID, 1))
        p.append(txt(X(v), top + rh * 3 + 10, f"{v}" + (" km/h" if v == 120 else ""), 10.5, 400, MUTED, "middle"))
    for i, (name, sub, mw, cv) in enumerate(rows):
        y = top + i * rh
        p.append(txt(20, y + 24, name, 12.5, 700, INK))
        p.append(txt(20, y + 40, sub, 10.5, 400, SLATE))
        for j, ((lo, hi), col) in enumerate(((mw, MOTORWAY), (cv, OTHER))):
            by = y + 8 + j * 24
            p.append(rect(X(lo), by, X(hi) - X(lo), 14, col, 4))
            p.append(txt(X(lo) - 6, by + 11, f"{lo}", 11, 700, INK, "end"))
            p.append(txt(X(hi) + 6, by + 11, f"{hi}", 11, 700, INK))
    return svg(720, top + rh * 3 + 18, "".join(p), L(lang, "Generic minimum and maximum speeds out of town", "Velocidades mínimas y máximas genéricas fuera de poblado"))


# ---------------------------------------------------------------- D3 urban limits
def _street(kind, cx, y):
    """A tiny street seen from above, 112 x 40."""
    x, w, h = cx - 56, 112, 40
    out = []
    if kind == "platform":
        out.append(rect(x, y, w, h, PAVING, 4))
        for i in range(7):
            out.append(rect(x + 8 + i * 15, y + 4, 9, 3, "#a8a29e", 1))
            out.append(rect(x + 8 + i * 15, y + h - 7, 9, 3, "#a8a29e", 1))
        out.append(rect(cx - 10, y + 14, 26, 13, "#1d4ed8", 3))
        out.append(f'<circle cx="{cx - 30}" cy="{y + 20}" r="4.5" fill="{TEAL}"/>')
        out.append(f'<circle cx="{cx + 34}" cy="{y + 24}" r="4.5" fill="{TEAL}"/>')
        return "".join(out)
    if kind == "motorway":
        out.append(rect(x, y, w, 16, ASPHALT, 3))
        out.append(rect(x, y + 16, w, 8, MEDIAN))
        out.append(rect(x, y + 24, w, 16, ASPHALT, 3))
        out.append(line(x + 4, y + 8, x + w - 4, y + 8, WHITE, 1.5, "8 6"))
        out.append(line(x + 4, y + 32, x + w - 4, y + 32, WHITE, 1.5, "8 6"))
        return "".join(out)
    out.append(rect(x, y, w, h, KERB, 3))
    out.append(rect(x, y + 5, w, h - 10, ASPHALT))
    mid = y + h / 2
    if kind == "two":
        out.append(line(x, mid - 1.5, x + w, mid - 1.5, WHITE, 1.2))
        out.append(line(x, mid + 1.5, x + w, mid + 1.5, WHITE, 1.2))
        out.append(line(x + 4, y + 12.5, x + w - 4, y + 12.5, WHITE, 1.2, "6 5"))
        out.append(line(x + 4, y + h - 12.5, x + w - 4, y + h - 12.5, WHITE, 1.2, "6 5"))
    else:
        out.append(line(x + 4, mid, x + w - 4, mid, WHITE, 1.5, "8 6"))
    if kind == "travesia":
        out.append(rect(cx + 16, y - 9, 36, 15, "#fff", 2, f' stroke="{SIGN_RED}" stroke-width="2"'))
        out.append(rect(cx + 21, y - 4, 26, 2.5, INK))
        out.append(rect(cx + 24, y + 0.5, 20, 2, INK))
    return "".join(out)


def urban_limits(lang):
    cards = {
        "en": [("platform", ["Single platform", "(road and pavement level)"], [20]),
               ("one", ["One lane", "per direction"], [30]),
               ("two", ["Two or more lanes", "per direction"], [50]),
               ("travesia", ["Travesía", "(main road through town)"], [50]),
               ("motorway", ["Urban autopista", "or autovía"], [80, 60])],
        "es": [("platform", ["Plataforma única", "de calzada y acera"], [20]),
               ("one", ["Un único carril", "por sentido"], [30]),
               ("two", ["Dos o más carriles", "por sentido"], [50]),
               ("travesia", ["Travesía", ""], [50]),
               ("motorway", ["Autopista y autovía", "dentro de poblado"], [80, 60])],
    }[lang]
    p = []
    for i, (kind, label, nums) in enumerate(cards):
        x = 10 + i * 142
        cx = x + 66
        p.append(rect(x, 6, 132, 162, "#f8fafc", 10, f' stroke="{GRID}" stroke-width="1.5"'))
        p.append(_street(kind, cx, 22))
        if len(nums) == 1:
            p.append(max_sign(cx, 96, 22, nums[0]))
        else:
            p.append(max_sign(cx - 25, 96, 21, nums[0]))
            p.append(min_sign(cx + 25, 96, 21, nums[1]))
        p.append(lines(cx, 140, [s for s in label if s], 11.5, 700, INK, "middle", 15))
    return svg(720, 174, "".join(p), L(lang, "Generic speed limits in built-up areas", "Límites genéricos de velocidad en poblado"))


# ---------------------------------------------------------------- D4 pedestrian risk by impact speed
def pedestrian_risk(lang):
    gx0, gx1 = 130, 590
    k = (gx1 - gx0) / 100

    def X(v):
        return round(gx0 + v * k, 1)

    rows = [("30 km/h", 10, 15, "10–15 %"),
            ("50 km/h", 50, 80, "50–80 %"),
            ("80 km/h", 100, 100, L(lang, "almost 100 %", "casi 100 %"))]
    p = [txt(20, 18, L(lang, "Chance that a pedestrian hit by a car dies", "Probabilidad de que muera un peatón atropellado"), 13, 700, INK)]
    top = 34
    for v in (0, 25, 50, 75, 100):
        p.append(line(X(v), top, X(v), top + 3 * 40 - 8, GRID, 1))
        p.append(txt(X(v), top + 3 * 40 + 6, f"{v} %", 10.5, 400, MUTED, "middle"))
    for i, (sp, lo, hi, lab) in enumerate(rows):
        y = top + i * 40 + 4
        p.append(txt(20, y + 15, sp, 12.5, 700, INK))
        if hi > lo:
            p.append(rect(X(0), y, X(hi) - X(0), 22, "#f4b4ae", 4))
        p.append(rect(X(0), y, X(lo) - X(0), 22, RED, 4))
        p.append(txt(X(hi) + 8, y + 15, lab, 12, 700, INK))
    p.append(rect(20, top + 3 * 40 + 20, 12, 10, RED, 2))
    p.append(rect(32, top + 3 * 40 + 20, 12, 10, "#f4b4ae", 2))
    p.append(txt(52, top + 3 * 40 + 29, L(lang, "Dark: lower estimate · light: higher estimate. Figures differ between studies; the trend does not.",
                                          "Oscuro: estimación baja · claro: estimación alta. Las cifras varían según el estudio; la tendencia no."), 10.5, 400, SLATE))
    return svg(720, top + 3 * 40 + 40, "".join(p), L(lang, "Pedestrian death risk by impact speed", "Riesgo de muerte del peatón según la velocidad"))


# ---------------------------------------------------------------- vehicle seen from behind
def _car_rear(cx, base, lit=False, arm=False, plate=True):
    """A car seen from behind, 150 wide, wheels on y = base. Returns SVG."""
    g = []
    if lit:
        for sx in (-60, 60):
            g.append(f'<circle cx="{sx}" cy="-52" r="20" fill="#fca5a5" opacity=".55"/>')
            g.append(f'<path d="M{sx - 26} -74 A 34 34 0 0 1 {sx + 26} -74" fill="none" stroke="#ef4444" stroke-width="2" opacity=".7"/>')
    g.append(rect(-62, -16, 22, 16, "#1f2937", 3))
    g.append(rect(40, -16, 22, 16, "#1f2937", 3))
    g.append('<path d="M-58 -66 L-44 -104 L44 -104 L58 -66 Z" fill="#475569"/>')
    g.append('<path d="M-50 -70 L-39 -98 L39 -98 L50 -70 Z" fill="#cbd5e1"/>')
    g.append(rect(-75, -68, 150, 54, "#64748b", 10))
    light = "#ef4444" if lit else "#991b1b"
    g.append(rect(-71, -58, 22, 11, light, 3))
    g.append(rect(49, -58, 22, 11, light, 3))
    if plate:
        g.append(rect(-24, -36, 48, 12, "#fff", 2, ' stroke="#94a3b8" stroke-width="1"'))
    if arm:
        skin = "#d6a77a"
        g.append(line(-46, -84, -100, -104, skin, 6, extra=' stroke-linecap="round" opacity=".35"'))
        g.append(line(-46, -84, -100, -64, skin, 6, extra=' stroke-linecap="round" opacity=".35"'))
        g.append(line(-46, -84, -104, -84, skin, 7, extra=' stroke-linecap="round"'))
        g.append(line(-120, -108, -120, -60, INK, 1.8))
        g.append('<path d="M-125 -102 L-120 -110 L-115 -102 Z" fill="#0f172a"/>')
        g.append('<path d="M-125 -66 L-120 -58 L-115 -66 Z" fill="#0f172a"/>')
    return f'<g transform="translate({cx} {base})">' + "".join(g) + "</g>"


# ---------------------------------------------------------------- D5 the V-4 plate
def v4_sign(lang):
    p = [f'<g transform="translate(0 -8)">' + _car_rear(150, 160) + "</g>"]
    p.append(v4_disc(196, 124, 10, 80))
    p.append(line(207, 121, 298, 90, MUTED, 1.2, "4 3"))
    p.append(v4_disc(350, 80, 50, 80))
    p.append(txt(350, 152, L(lang, "Plate V-4", "Señal V-4"), 12.5, 700, INK, "middle"))
    body = L(lang,
             ["Shows the speed this vehicle", "must not exceed. Carried at the rear,", "always visible, when the limit is set:",
              "• for the driver (personal circumstances)", "• for the vehicle (its features or its load)"],
             ["Indica la velocidad que el vehículo", "no debe rebasar. Va en la parte posterior,", "siempre visible, cuando el límite se fija:",
              "• al conductor (circunstancias personales)", "• al vehículo (características o carga)"])
    p.append(lines(438, 52, body, 12, 400, INK, "start", 18))
    return svg(720, 170, "".join(p), L(lang, "V-4 speed-limitation plate", "Señal V-4 de limitación de velocidad"))


# ---------------------------------------------------------------- D6 how to warn before slowing down
def slow_down(lang):
    p = []
    # 1. mirror
    p.append(rect(48, 34, 150, 74, "#bfdbfe", 34, f' stroke="{SLATE}" stroke-width="5"'))
    p.append('<path d="M92 104 L114 46 L132 46 L154 104 Z" fill="#9ca3af"/>')
    p.append(rect(112, 60, 22, 14, "#b45309", 3))
    p.append(rect(116, 62, 14, 4, "#fde68a", 1))
    # 2. brake lights
    p.append(_car_rear(368, 120, lit=True))
    # 3. arm signal
    p.append(_car_rear(616, 120, arm=True))
    steps = L(lang,
              [("1", "Check the mirrors", "distance and speed of those behind"),
               ("2", "Warn: brake lights", "press the pedal several times"),
               ("3", "… or the arm", "up and down, short and quick")],
              [("1", "Mira los espejos", "distancia y velocidad de los de detrás"),
               ("2", "Avisa: luces de freno", "pisa el pedal varias veces"),
               ("3", "… o el brazo", "de arriba abajo, corto y rápido")])
    for i, (n, head, sub) in enumerate(steps):
        cx = (123, 368, 600)[i]
        p.append(f'<circle cx="{cx - 4 - len(head) * 3.6}" cy="{144}" r="10" fill="{NAVY}"/>')
        p.append(txt(cx - 4 - len(head) * 3.6, 148, n, 11.5, 800, "#fff", "middle"))
        p.append(txt(cx + 10, 149, head, 12.5, 700, INK, "middle"))
        p.append(txt(cx, 167, sub, 11, 400, SLATE, "middle"))
    p.append(txt(360, 198, L(lang, "Then slow down smoothly, never abruptly (unless the danger is imminent).",
                                "Después reduce sin brusquedades (salvo peligro inminente)."), 12, 700, TEAL, "middle"))
    return svg(720, 208, "".join(p), L(lang, "Warning before slowing down", "Advertir antes de reducir la velocidad"))
