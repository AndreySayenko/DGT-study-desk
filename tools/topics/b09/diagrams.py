# -*- coding: utf-8 -*-
"""Original SVG diagrams for Topic 9 (EN/ES). No third-party artwork is used. Each function takes the language
("en" or "es") and returns an SVG string. Figures sit on a light background in both themes."""

from svgkit import NAVY, TEAL, RED, SLATE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect, tick, cross  # noqa: F401

MUTED = "#64748b"
LINE = "#cbd5e1"
CARD = "#f8fafc"
EU = "#1d4ed8"
# sequential ramp for "how often": none → every 2 years → every year → every 6 months
FREQ = {"none": ("#e5e7eb", INK), "2y": ("#93c5fd", INK), "1y": ("#3b82f6", "#fff"), "6m": ("#1e3a8a", "#fff")}


def L(lang, en, es):
    return en if lang == "en" else es


def line(x1, y1, x2, y2, color=INK, width=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{d}/>'


# ---------------------------------------------------------------- D1 minimum ages for each licence
def licence_ages(lang):
    x0, step, ay = 50, 88, 232
    p = [line(x0 - 20, ay, x0 + step * 7 + 26, ay, SLATE, 2)]
    for i, age in enumerate(range(14, 22)):
        x = x0 + i * step
        p.append(line(x, ay - 6, x, ay + 6, SLATE, 2) + txt(x, ay + 24, str(age), 14, 700, INK, "middle"))
    p.append(txt(x0 + step * 3.5, ay + 44, L(lang, "Minimum age (years)", "Edad mínima (años)"), 11.5, 600, SLATE, "middle"))
    chips = {
        14: [("LCM", L(lang, ["reduced", "mobility"], ["movilidad", "reducida"]), TEAL)],
        15: [("AM", L(lang, ["mopeds,", "light quads"], ["ciclomotores,", "cuadric. ligeros"]), TEAL)],
        16: [("A1", L(lang, ["≤ 125 cc,", "≤ 11 kW"], ["≤ 125 c.c.,", "≤ 11 kW"]), NAVY), ("LVA", L(lang, ["farm", "vehicles"], ["vehículos", "agrícolas"]), TEAL)],
        18: [("B", L(lang, ["cars", "≤ 3,500 kg"], ["turismos", "≤ 3.500 kg"]), NAVY), ("A2", L(lang, ["motorcycles", "≤ 35 kW"], ["motos", "≤ 35 kW"]), NAVY),
             ("B+E", L(lang, ["trailer", "≤ 3,500 kg"], ["remolque", "≤ 3.500 kg"]), NAVY)],
        20: [("A", L(lang, ["after 2 years", "with A2"], ["tras 2 años", "con A2"]), NAVY)],
        21: [(L(lang, "Trikes", "Triciclos"), L(lang, ["over 15 kW", "(A or B)"], ["de más de 15", "kW (A o B)"]), RED)],
    }
    for age, cs in chips.items():
        x = x0 + (age - 14) * step
        for j, (code, sub, col) in enumerate(cs):
            y = ay - 62 - j * 60
            p.append(rect(x - 42, y, 84, 52, "#fff", 8, f' stroke="{col}" stroke-width="2"'))
            p.append(txt(x, y + 18, code, 14, 800, col, "middle") + lines(x, y + 32, sub, 9.5, 600, SLATE, "middle", 11))
    return svg(720, ay + 52, "".join(p), L(lang, "Minimum age for each licence", "Edad mínima de cada permiso o licencia"))


# ---------------------------------------------------------------- D2 where the number plates and the L plate go
def _plate(cx, cy, text, w=74, h=18, fill="#fff", fg=INK, eu=True):
    out = rect(cx - w / 2, cy - h / 2, w, h, fill, 3, ' stroke="#334155" stroke-width="1.2"')
    if eu:
        out += rect(cx - w / 2, cy - h / 2, 10, h, EU, 2) + txt(cx - w / 2 + 5, cy + 4, "E", 7, 700, "#fff", "middle")
    return out + txt(cx + (4 if eu else 0), cy + 4.5, text, 10.5, 700, fg, "middle")


def _lplate(cx, cy, s=26):
    return rect(cx - s / 2, cy - s / 2, s, s, "#16a34a", 3, ' stroke="#fff" stroke-width="1.5"') + \
        f'<path d="M{cx - 5} {cy - 8} L{cx - 5} {cy + 7} L{cx + 7} {cy + 7}" stroke="#fff" stroke-width="3.6" fill="none"/>'


def plates(lang):
    p = []
    for i in range(4):
        p.append(rect(6 + i * 179, 6, 170, 232, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'))
    # a. car seen from behind with the L plate
    cx = 91
    p.append(rect(cx - 64, 92, 128, 70, "#64748b", 14) + f'<path d="M{cx - 50} 94 L{cx - 38} 52 L{cx + 38} 52 L{cx + 50} 94 Z" fill="#475569"/>'
             + f'<path d="M{cx - 40} 92 L{cx - 31} 60 L{cx + 31} 60 L{cx + 40} 92 Z" fill="#cbd5e1"/>' + rect(cx - 58, 160, 22, 18, "#1f2937", 4) + rect(cx + 36, 160, 22, 18, "#1f2937", 4)
             + rect(cx - 62, 104, 22, 12, "#ef4444", 3) + rect(cx + 40, 104, 22, 12, "#ef4444", 3))
    p.append(_plate(cx, 138, "1234 BCD") + _lplate(cx - 38, 76))
    # b. motorcycle from behind
    cx = 270
    p.append(rect(cx - 9, 120, 18, 58, "#1f2937", 8) + rect(cx - 24, 70, 48, 34, "#334155", 10) + f'<circle cx="{cx}" cy="58" r="14" fill="#94a3b8"/>'
             + rect(cx - 40, 78, 80, 6, "#334155", 3) + rect(cx - 6, 104, 12, 8, "#ef4444", 2))
    p.append(_plate(cx, 124, "1234 BCD", 60, 16))
    # c. light trailer
    cx = 449
    p.append(rect(cx - 62, 86, 124, 62, "#e2e8f0", 4, ' stroke="#64748b" stroke-width="1.5"') + rect(cx - 70, 146, 140, 8, "#475569", 2)
             + rect(cx - 64, 154, 18, 22, "#1f2937", 4) + rect(cx + 46, 154, 18, 22, "#1f2937", 4))
    p.append(_plate(cx, 128, "1234 BCD"))
    # d. heavy trailer: copy of the towing vehicle's plate on the right, red trailer plate in the middle
    cx = 628
    p.append(rect(cx - 64, 62, 128, 86, "#e2e8f0", 4, ' stroke="#64748b" stroke-width="1.5"') + rect(cx - 72, 146, 144, 8, "#475569", 2)
             + rect(cx - 66, 154, 18, 22, "#1f2937", 4) + rect(cx + 48, 154, 18, 22, "#1f2937", 4))
    p.append(_plate(cx, 100, "R 1234 BBB", 74, 18, "#dc2626", INK, eu=False) + _plate(cx + 26, 132, "1234 BCD", 64, 16))
    caps = L(lang, [["Car: front and rear plates.", "Novice: V-13 “L” at the", "rear LEFT, for 1 year"], ["Motorcycle, moped,", "self-propelled special", "vehicle: one rear plate"],
                    ["Trailer up to 750 kg:", "one plate, the towing", "vehicle’s, centre or left"], ["Trailer over 750 kg: the", "towing vehicle’s plate on the", "right + its own RED plate"]],
             [["Turismo: placa delantera y", "trasera. Novel: V-13 «L»", "detrás a la IZQUIERDA, 1 año"], ["Moto, ciclomotor, vehículo", "especial autopropulsado:", "una placa detrás"],
              ["Remolque hasta 750 kg:", "una placa, la del tractor,", "en el centro o a la izquierda"], ["Remolque de más de 750 kg:", "la del tractor a la derecha", "+ su placa ROJA propia"]])
    for i, c in enumerate(caps):
        p.append(lines(91 + i * 179, 198, c, 11, 600, INK, "middle", 14))
    return svg(720, 244, "".join(p), L(lang, "Where the plates go", "Colocación de las placas"))


# ---------------------------------------------------------------- D3 ITV: how often each vehicle is inspected, by age
def itv_chart(lang):
    rows = L(lang, [
        ("Two-wheel mopeds", [(0, 3, "none"), (3, 14, "2y")]),
        ("Motorcycles, 3-wheel mopeds, quads", [(0, 4, "none"), (4, 14, "2y")]),
        ("Private cars, motorhomes", [(0, 4, "none"), (4, 10, "2y"), (10, 14, "1y")]),
        ("Goods vehicles ≤ 3.5 t (vans)", [(0, 2, "none"), (2, 6, "2y"), (6, 10, "1y"), (10, 14, "6m")]),
        ("Towed caravans 750 kg–3.5 t", [(0, 6, "none"), (6, 14, "2y")]),
        (["Trailers > 750 kg (not caravans),", "goods vehicles > 3.5 t"], [(0, 10, "1y"), (10, 14, "6m")]),
    ], [
        ("Ciclomotores de dos ruedas", [(0, 3, "none"), (3, 14, "2y")]),
        ("Motos, ciclomotores 3 ruedas, quads", [(0, 4, "none"), (4, 14, "2y")]),
        ("Turismos privados, autocaravanas", [(0, 4, "none"), (4, 10, "2y"), (10, 14, "1y")]),
        ("Mercancías ≤ 3,5 t (furgonetas)", [(0, 2, "none"), (2, 6, "2y"), (6, 10, "1y"), (10, 14, "6m")]),
        ("Caravanas remolcadas 750 kg–3,5 t", [(0, 6, "none"), (6, 14, "2y")]),
        (["Remolques > 750 kg (no caravanas),", "mercancías > 3,5 t"], [(0, 10, "1y"), (10, 14, "6m")]),
    ])
    names = L(lang, {"none": "exempt", "2y": "every 2 years", "1y": "every year", "6m": "every 6 months"},
              {"none": "exento", "2y": "cada 2 años", "1y": "cada año", "6m": "cada 6 meses"})
    short = L(lang, {"none": "exempt", "2y": "2 years", "1y": "1 year", "6m": "6 months"}, {"none": "exento", "2y": "2 años", "1y": "1 año", "6m": "6 meses"})
    x0, x1, top, rh = 236, 704, 54, 34
    sx = (x1 - x0) / 14
    p = []
    # legend in one row above the plot
    lx = x0
    for k in ("none", "2y", "1y", "6m"):
        p.append(rect(lx, 14, 14, 14, FREQ[k][0], 3) + txt(lx + 20, 26, names[k], 11.5, 600, INK))
        lx += 26 + len(names[k]) * 6.6
    for yr in range(0, 15, 2):
        x = x0 + yr * sx
        p.append(line(x, top - 6, x, top + rh * len(rows) - 4, "#e2e8f0", 1))
    for i, (name, segs) in enumerate(rows):
        y = top + i * rh
        p.append(lines(x0 - 10, y + 13, name, 11, 600, INK, "end", 12) if isinstance(name, list) else txt(x0 - 10, y + 19, name, 11.5, 600, INK, "end"))
        for a, b, k in segs:
            xa, xb = x0 + a * sx + 1, x0 + b * sx - 1
            p.append(rect(round(xa, 1), y + 2, round(xb - xa, 1), rh - 10, FREQ[k][0], 4))
            if xb - xa > 46:
                p.append(txt(round((xa + xb) / 2, 1), y + 19, short[k], 10.5, 700, FREQ[k][1], "middle"))
    yb = top + rh * len(rows) + 8
    for yr in range(0, 15, 2):
        p.append(txt(round(x0 + yr * sx, 1), yb + 6, str(yr) if yr < 14 else "…", 11, 400, MUTED, "middle"))
    p.append(txt((x0 + x1) / 2, yb + 24, L(lang, "Age of the vehicle in years (from its first registration)", "Antigüedad del vehículo en años (desde su matriculación)"), 11.5, 600, SLATE, "middle"))
    return svg(720, yb + 32, "".join(p), L(lang, "How often each vehicle passes the ITV", "Frecuencia de la ITV según el vehículo"))


# ---------------------------------------------------------------- D4 what the compulsory insurance pays for
def insurance_grid(lang):
    cols = L(lang, [["The guilty", "driver"], ["Policyholder, insured,", "owner and relatives*"], ["Other people"]],
             [["El conductor", "culpable"], ["Tomador, asegurado,", "propietario y parientes*"], ["Otras personas"]])
    rows = L(lang, ["Personal injury", "Damage to property"], ["Daños personales", "Daños materiales"])
    marks = [[False, True, True], [False, False, True]]
    x0, cw, y0, rh = 190, 176, 70, 54
    p = [rect(x0 + i * cw, 10, cw - 6, 52, "#e0f2fe", 8) for i in range(3)]
    for i, c in enumerate(cols):
        p.append(lines(x0 + i * cw + (cw - 6) / 2, 32 - (len(c) - 1) * 7, c, 12, 700, INK, "middle", 15))
    for r, name in enumerate(rows):
        y = y0 + r * rh
        p.append(rect(10, y, 172, rh - 6, "#f1f5f9", 8) + txt(96, y + rh / 2 + 1, name, 12.5, 700, INK, "middle"))
        for c in range(3):
            p.append(rect(x0 + c * cw, y, cw - 6, rh - 6, "#fff", 8, f' stroke="{LINE}" stroke-width="1.2"'))
            cx, cy = x0 + c * cw + (cw - 6) / 2, y + (rh - 6) / 2
            p.append(tick(cx - 30, cy, 12) + txt(cx - 12, cy + 4.5, L(lang, "covered", "cubiertos"), 12, 700, "#0b7548") if marks[r][c]
                     else cross(cx - 38, cy, 12) + txt(cx - 20, cy + 4.5, L(lang, "not covered", "no cubiertos"), 12, 700, RED))
    p.append(txt(360, 190, L(lang, "* Spouse and relatives up to the third degree of blood or marriage, of any of them.",
                             "* Cónyuge y parientes hasta el tercer grado de consanguinidad o afinidad de cualquiera de ellos."), 11, 400, MUTED, "middle"))
    return svg(720, 198, "".join(p), L(lang, "What the compulsory insurance of the guilty driver covers", "Qué cubre el seguro obligatorio del conductor culpable"))


# ---------------------------------------------------------------- D5 points over the years for a new driver with a clean record
def points_path(lang):
    x0, x1, y0, y1 = 70, 690, 220, 44
    sx = (x1 - x0) / 9
    sy = (y0 - y1) / 9          # points 7..16
    Y = lambda v: y0 - (v - 7) * sy  # noqa: E731
    X = lambda t: x0 + t * sx  # noqa: E731
    p = []
    for v in (8, 12, 14, 15):
        p.append(line(x0, round(Y(v), 1), x1, round(Y(v), 1), "#e2e8f0", 1) + txt(x0 - 10, round(Y(v), 1) + 4, str(v), 12, 700, SLATE, "end"))
    pts = [(0, 8), (2, 8), (2, 12), (5, 12), (5, 14), (8, 14), (8, 15), (9, 15)]
    d = "M" + " L".join(f"{X(t):.1f} {Y(v):.1f}" for t, v in pts)
    p.append(f'<path d="{d}" fill="none" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>')
    for t, v in ((0, 8), (2, 12), (5, 14), (8, 15)):
        p.append(f'<circle cx="{X(t):.1f}" cy="{Y(v):.1f}" r="5" fill="{NAVY}" stroke="#fff" stroke-width="2"/>')
    notes = L(lang, [(1, 8, "8 points: licence less than 2 years old"), (3.5, 12, "12 after 2 years"), (6.5, 14, "+2 after 3 clean years"), (8.4, 15, "+1 → max 15")],
              [(1, 8, "8 puntos: permiso de menos de 2 años"), (3.5, 12, "12 a los 2 años"), (6.5, 14, "+2 tras 3 años sin sanción"), (8.4, 15, "+1 → máx. 15")])
    for t, v, s in notes:
        if v == 8:
            p.append(txt(round(X(0), 1) + 8, round(Y(v), 1) + 20, s, 11.5, 700, INK, "start"))
        else:
            p.append(txt(round(X(t), 1), round(Y(v), 1) - 10, s, 11.5, 700, INK, "middle"))
    for t in range(0, 10):
        p.append(txt(round(X(t), 1), y0 + 18, str(t), 11, 400, MUTED, "middle"))
    p.append(txt((x0 + x1) / 2, y0 + 36, L(lang, "Years with the licence, without firm sanctions that take away points", "Años con el permiso, sin sanciones firmes con pérdida de puntos"), 11.5, 600, SLATE, "middle"))
    p.append(txt(x0 - 10, 18, L(lang, "points", "puntos"), 11.5, 600, SLATE, "end"))
    return svg(720, y0 + 44, "".join(p), L(lang, "Points of a new driver with a clean record", "Puntos de un conductor novel sin sanciones"))
