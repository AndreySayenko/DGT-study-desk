# -*- coding: utf-8 -*-
"""Original SVG diagrams for Category A1/A2, Topic 9 (documentation), EN/ES. No third-party artwork is used.
Three figures are specific to riders; two (points and insurance) are shared with Category B, Topic 9."""

from svgkit import NAVY, TEAL, AMBER, RED, SLATE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect, tick, cross
from ..b09.diagrams import L, line, MUTED, LINE, CARD, FREQ
from ..b09.diagrams import points_path, insurance_grid  # noqa: F401  (shared with Topic B9)
from ..b10.diagrams import arrow
from ..b08 import signs as S

GOOD = "#0b7548"


def _n(lang, x):
    """A decimal number with the language's decimal mark."""
    s = f"{x}"
    return s if lang == "en" else s.replace(".", ",")


# ---------------------------------------------------------------- D1 the motorcycle licences, step by step
def licence_ladder(lang):
    steps = [
        ("AM", L(lang, "from 15", "desde 15 años"), L(lang, ["Mopeds", "Light quadricycles"], ["Ciclomotores", "Cuadriciclos ligeros"]), None),
        ("A1", L(lang, "from 16", "desde 16 años"), L(lang, ["≤ 125 cc · ≤ 11 kW", "≤ 0.1 kW/kg", "Trikes ≤ 15 kW"], ["≤ 125 c.c. · ≤ 11 kW", "≤ 0,1 kW/kg", "Triciclos ≤ 15 kW"]),
         L(lang, "includes AM", "incluye el AM")),
        ("A2", L(lang, "from 18", "desde 18 años"), L(lang, ["≤ 35 kW · ≤ 0.2 kW/kg", "if limited: original", "≤ 2 × its power"], ["≤ 35 kW · ≤ 0,2 kW/kg", "si está limitada: original", "≤ 2 × su potencia"]),
         L(lang, "includes A1 and AM", "incluye A1 y AM")),
        ("A", L(lang, "from 20", "desde 20 años"), L(lang, ["Any motorcycle", "Trikes over 15 kW", "only from 21"], ["Cualquier motocicleta", "Triciclos de más de", "15 kW, desde 21"]), None),
    ]
    fills = ["#e0f2fe", "#cde7fb", "#b4daf7", "#9bcbf2"]
    w, bottom = 166, 318
    p = []
    for i, (code, age, spec, inc) in enumerate(steps):
        x, top = 12 + i * 178, 206 - i * 44
        p.append(rect(x, top, w, bottom - top, fills[i], 10))
        p.append(txt(x + 14, top + 30, code, 24, 800, NAVY) + txt(x + w - 12, top + 28, age, 12, 700, INK, "end"))
        p.append(lines(x + 14, top + 54, spec, 11.5, 600, INK, "start", 15))
        if inc:
            p.append(txt(x + 14, bottom - 12, inc, 10.5, 700, SLATE))
    # the only compulsory step: A2 → A
    x2, x3 = 12 + 2 * 178 + w / 2, 12 + 3 * 178 + 30
    p.append(f'<path d="M{x2} 112 Q{x2 + 40} 62 {x3 - 10} 64" fill="none" stroke="{AMBER}" stroke-width="2.5"/>')
    p.append(arrow(x3 - 22, 63, x3 - 2, 66, AMBER, 2.5, 10))
    p.append(lines(x2 - 128, 24, L(lang, ["The only way to A: hold A2 for at", "least 2 years + a training course"], ["Al A solo se llega con el A2: 2 años", "de experiencia + una formación"]),
                   12, 800, AMBER, "start", 15))
    p.append(lines(16, 36, L(lang, ["A1 and A2 can also be taken directly,", "with their own exams."], ["El A1 y el A2 también se obtienen", "directamente, con sus exámenes."]),
                   11, 600, SLATE, "start", 14))
    # B holders
    p.append(rect(12, 330, 696, 38, "#fef3c7", 8))
    p.append(txt(360, 354, L(lang, "B held for more than 3 years: also the A1 motorcycles, in Spain only",
                             "Permiso B con más de 3 años: también las motocicletas del A1, solo en España"), 12, 700, INK, "middle"))
    return svg(720, 376, "".join(p), L(lang, "Motorcycle licences step by step", "Los permisos de moto paso a paso"))


# ---------------------------------------------------------------- D2 does this motorcycle fit the A2?
def a2_power(lang):
    cards = [
        (L(lang, ["35 kW · 190 kg"], ["35 kW · 190 kg"]), f"35 ÷ 190 = {_n(lang, 0.18)} kW/kg", True, L(lang, ["Fits A2"], ["Vale con el A2"])),
        (L(lang, ["35 kW · 150 kg"], ["35 kW · 150 kg"]), f"35 ÷ 150 = {_n(lang, 0.23)} kW/kg", False, L(lang, ["Over 0.2 kW/kg:", "needs A"], ["Más de 0,2 kW/kg:", "exige el A"])),
        (L(lang, ["Limited to 35 kW", "from 60 kW"], ["Limitada a 35 kW", "desde 60 kW"]), "60 ≤ 2 × 35 = 70", True, L(lang, ["Fits A2"], ["Vale con el A2"])),
        (L(lang, ["Limited to 35 kW", "from 95 kW"], ["Limitada a 35 kW", "desde 95 kW"]), "95 > 2 × 35 = 70", False, L(lang, ["Derived from more than", "twice: needs A"], ["Deriva de más del", "doble: exige el A"])),
    ]
    p = []
    for i, (head, calc, ok, verdict) in enumerate(cards):
        x, w = 8 + i * 178, 170
        col = GOOD if ok else RED
        p.append(rect(x, 8, w, 210, CARD, 10, f' stroke="{LINE}" stroke-width="1.5"'))
        p.append(S.at(S.moto(INK), x + w / 2, 46, 1.6))
        p.append(lines(x + w / 2, 92, head, 13, 800, INK, "middle", 16))
        p.append(txt(x + w / 2, 132, calc, 11.5, 600, SLATE, "middle"))
        p.append((tick if ok else cross)(x + 26, 166, 12))
        p.append(lines(x + 44, 162 if len(verdict) > 1 else 170, verdict, 12, 800, col, "start", 15))
    p.append(lines(360, 240, L(lang, ["A2: at most 35 kW and 0.2 kW/kg, and not derived from a motorcycle with more than twice its power."],
                                    ["A2: como máximo 35 kW y 0,2 kW/kg, y no derivada de una motocicleta con más del doble de su potencia."]), 11.5, 700, INK, "middle", 15))
    return svg(720, 252, "".join(p), L(lang, "Which motorcycles the A2 covers", "Qué motocicletas cubre el A2"))


# ---------------------------------------------------------------- D3 the ITV calendar of a motorcycle and a moped
def itv_timeline(lang):
    rows = [
        (L(lang, ["Two-wheel moped"], ["Ciclomotor de dos ruedas"]), 3, L(lang, "1st ITV at 3 years", "1.ª ITV a los 3 años")),
        (L(lang, ["Motorcycle, three-wheeler,", "three-wheel moped, quad"], ["Motocicleta, tres ruedas,", "ciclomotor de tres ruedas, quad"]), 4, L(lang, "1st ITV at 4 years", "1.ª ITV a los 4 años")),
    ]
    x0, x1, top, rh = 222, 700, 40, 62
    sx = (x1 - x0) / 13
    p = []
    names = L(lang, [("none", "exempt"), ("2y", "every 2 years")], [("none", "exento"), ("2y", "cada 2 años")])
    lx = x0
    for k, n in names:
        p.append(rect(lx, 6, 14, 14, FREQ[k][0], 3) + txt(lx + 20, 18, n, 11.5, 600, INK))
        lx += 34 + len(n) * 6.6
    p.append(f'<circle cx="{lx + 6}" cy="13" r="6" fill="{NAVY}"/>' + txt(lx + 18, 18, L(lang, "inspection", "inspección"), 11.5, 600, INK))
    for yr in range(0, 14):
        x = x0 + yr * sx
        p.append(line(round(x, 1), top - 4, round(x, 1), top + rh * 2 - 8, "#e2e8f0", 1))
    for i, (name, first, note) in enumerate(rows):
        y = top + i * rh
        p.append(lines(x0 - 12, y + (20 if len(name) == 1 else 13), name, 11.5, 700, INK, "end", 14))
        xa = x0 + first * sx
        p.append(rect(x0, y + 4, round(xa - x0 - 2, 1), 22, FREQ["none"][0], 5) + rect(round(xa + 2, 1), y + 4, round(x1 - xa - 2, 1), 22, FREQ["2y"][0], 5))
        for yr in range(first, 13, 2):
            p.append(f'<circle cx="{x0 + yr * sx:.1f}" cy="{y + 15}" r="7" fill="{NAVY}" stroke="#fff" stroke-width="2"/>')
        p.append(txt(round(xa, 1), y + 44, note, 11, 700, NAVY, "middle"))
    yb = top + rh * 2 + 2
    for yr in range(0, 14):
        p.append(txt(round(x0 + yr * sx, 1), yb + 4, str(yr) if yr < 13 else "…", 11, 400, MUTED, "middle"))
    p.append(txt((x0 + x1) / 2, yb + 22, L(lang, "Age in years, counted from the first registration", "Antigüedad en años, desde la primera matriculación"), 11.5, 600, SLATE, "middle"))
    p.append(txt(360, yb + 44, L(lang, "You may go up to 30 days early: the next date still counts from the one you were given.",
                                 "Se puede adelantar hasta 30 días: la fecha siguiente se cuenta desde la que tenías."), 11, 600, SLATE, "middle"))
    return svg(720, yb + 52, "".join(p), L(lang, "ITV calendar of motorcycles and mopeds", "Calendario de ITV de motos y ciclomotores"))
