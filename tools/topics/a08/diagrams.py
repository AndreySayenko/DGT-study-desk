# -*- coding: utf-8 -*-
"""Original SVG diagrams for Category A1/A2, Topic 8 (signs and signals), EN/ES. No third-party artwork is used.
Three figures are specific to riders; the sign drawings inside them are the simplified ones of Category B, Topic 8."""

import math
import re

from svgkit import NAVY, TEAL, AMBER, RED, SLATE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect, car_h, car_v, tick, cross, ASPHALT, WHITE
from ..b09.diagrams import L, line, MUTED, LINE, CARD
from ..b10.diagrams import arrow, rot
from ..b12.diagrams import moto_v
from ..b08 import signs as S

VERGE_BG = "#e8f0e3"
PAVE = "#cbd5e1"


def _moto(cx, cy, deg, color=TEAL, k=1.35):
    """Motorcycle seen from above at (cx, cy), heading `deg` degrees clockwise from 'up', drawn k times larger."""
    return f'<g transform="translate({cx} {cy}) rotate({deg}) scale({k}) translate({-cx} {-cy})">{moto_v(cx, cy, color)}</g>'


def _sign(code, x, y, px):
    """A sign drawing from the Topic B8 catalogue, placed with its top-left corner at (x, y) and `px` wide."""
    src = S.ICON[code]
    vb = re.search(r'viewBox="0 0 (\d+) (\d+)"', src)
    w, h = int(vb.group(1)), int(vb.group(2))
    inner = re.sub(r"^<svg[^>]*>|</svg>$", "", src)
    return f'<svg x="{x}" y="{y}" width="{px}" height="{round(px * h / w, 1)}" viewBox="0 0 {w} {h}" font-family="{S.FONT}">{inner}</svg>'


# ---------------------------------------------------------------- D1 which no-entry signs stop a motorcycle or a moped
def entry_matrix(lang):
    rows = [
        ("R-100", L(lang, "No vehicles", "Circulación prohibida"),
         L(lang, "Closed to every vehicle, in both directions", "Cerrada a toda clase de vehículos, en ambos sentidos"), False, False),
        ("R-101", L(lang, "No entry", "Entrada prohibida"),
         L(lang, "No entry for any vehicle", "Prohibido el acceso a toda clase de vehículos"), False, False),
        ("R-102", L(lang, "No motor vehicles", "Entrada prohibida a vehículos de motor"),
         L(lang, "A moped is not a “motor vehicle” in the Traffic Law", "El ciclomotor no es «vehículo de motor» en la Ley de Tráfico"), False, True),
        ("R-103", L(lang, "No motor vehicles, except two-wheeled motorcycles", "Prohibida a vehículos de motor, excepto motos de dos ruedas"),
         L(lang, "Two-wheeled motorcycles are the exception", "Las motocicletas de dos ruedas son la excepción"), True, True),
        ("R-104", L(lang, "No motorcycles", "Entrada prohibida a motocicletas"),
         L(lang, "Motorcycles and three-wheelers treated as motorcycles", "Motocicletas y vehículos de tres ruedas asimilados"), False, True),
        ("R-105", L(lang, "No mopeds", "Entrada prohibida a ciclomotores"),
         L(lang, "Mopeds, and vehicles for people with reduced mobility", "Ciclomotores y vehículos para personas de movilidad reducida"), True, False),
    ]
    top, rh = 62, 46
    xm, xp = 556, 656
    p = [rect(8, 6, 704, top - 10, NAVY, 10)]
    p.append(txt(24, 30, L(lang, "The sign you meet head-on", "La señal que encuentras de frente"), 13, 800, "#fff"))
    p.append(txt(24, 47, L(lang, "May you ride past it?", "¿Puedes pasar?"), 11, 600, "#cbd5e1"))
    p.append(S.at(S.moto("#fff", NAVY), xm, 24, 0.8) + txt(xm, 50, L(lang, "Motorcycle", "Motocicleta"), 11.5, 800, "#fff", "middle"))
    p.append(S.at(S.moped("#fff", NAVY), xp, 24, 0.8) + txt(xp, 50, L(lang, "Moped", "Ciclomotor"), 11.5, 800, "#fff", "middle"))
    for k, (code, name, note, moto_ok, moped_ok) in enumerate(rows):
        y = top + k * rh
        p.append(rect(8, y, 704, rh - 4, CARD if k % 2 == 0 else "#fff", 8, f' stroke="{LINE}" stroke-width="1"'))
        p.append(_sign(code, 20, y + 3, 36))
        p.append(txt(70, y + 18, f"{code} · {name}", 12.5, 800, INK))
        p.append(txt(70, y + 34, note, 11, 500, MUTED))
        cy = y + (rh - 4) / 2
        p.append((tick if moto_ok else cross)(xm, cy, 12))
        p.append((tick if moped_ok else cross)(xp, cy, 12))
    yb = top + len(rows) * rh + 14
    p.append(lines(360, yb, L(lang,
                              ["Three-wheelers treated as motorcycles follow the motorcycle column.",
                               "These signs bind only those who meet them head-on, from the point where they stand."],
                              ["Los vehículos de tres ruedas asimilados a motocicletas siguen la columna de la motocicleta.",
                               "Estas señales solo obligan a quien se las encuentra de frente, a partir del lugar en que están."]),
                   10.5, 600, SLATE, "middle", 14))
    return svg(720, yb + 24, "".join(p), L(lang, "No-entry signs for motorcycles and mopeds", "Señales de prohibición de entrada para motocicletas y ciclomotores"))


# ---------------------------------------------------------------- D2 the advanced stop box (avanza-motos)
def advance_box(lang):
    y0, y1 = 100, 260
    mid = (y0 + y1) / 2
    xr, xf = 478, 566
    p = [rect(0, 0, 720, 336, VERGE_BG)]
    p.append(rect(0, y0 - 12, 720, 12, PAVE) + rect(0, y1, 720, 12, PAVE) + rect(0, y0, 720, y1 - y0, ASPHALT))
    p.append(line(0, mid, xr - 8, mid, WHITE, 2.5, "16 12"))
    p.append(f'<rect x="{xr + 3}" y="{y0}" width="{xf - xr - 6}" height="{y1 - y0}" fill="#5eead4" opacity="0.28"/>')
    p.append(rect(xr - 3, y0, 6, y1 - y0, WHITE) + rect(xf - 3, y0, 6, y1 - y0, WHITE))
    for y in range(y0 + 8, y1 - 8, 22):                      # pedestrian crossing beyond the box
        p.append(rect(592, y, 46, 12, WHITE))
    # traffic light on red, beyond the crossing
    p.append(rect(655, 30, 20, 50, "#111827", 5) + line(665, 80, 665, y0 - 12, "#111827", 3)
             + f'<circle cx="665" cy="41" r="6" fill="#ef4444"/><circle cx="665" cy="55" r="6" fill="#3f4652"/><circle cx="665" cy="69" r="6" fill="#3f4652"/>')
    # painted pictogram inside the box, motorcycles waiting in it, cars behind the first line
    p.append(S.at(S.moto(WHITE, ASPHALT), 522, 226, 1.15))
    for cx, cy in ((536, 124), (510, 160), (538, 192)):
        p.append(_moto(cx, cy, 90))
    for cx, cy, c in ((440, 140, "#1d4ed8"), (440, 220, "#b45309"), (378, 140, "#7c3aed"), (374, 220, "#334155")):
        p.append(car_h(cx, cy, c))
    # labels
    p.append(txt(16, 26, L(lang, "Advanced stop box (avanza-motos)", "Zona de espera adelantada (avanza-motos)"), 13.5, 800, INK))
    p.append(lines(16, 46, L(lang, ["Two continuous lines across the road, 4 m apart,", "just before a junction or crossing with traffic lights."],
                                   ["Dos marcas transversales continuas separadas 4 m,", "justo antes de una intersección o paso con semáforo."]), 11.5, 500, SLATE, "start", 15))
    p.append(line(522, y0 - 14, 522, 72, TEAL, 1.5) + txt(522, 64, L(lang, "On red: only the vehicles painted here", "En rojo: solo los vehículos pintados aquí"), 11.5, 800, TEAL, "middle"))
    p.append(line(xr, 282, xf, 282, NAVY, 1.5) + line(xr, 276, xr, 288, NAVY, 1.5) + line(xf, 276, xf, 288, NAVY, 1.5)
             + txt((xr + xf) / 2, 302, "4 m", 12.5, 800, NAVY, "middle"))
    p.append(line(408, y1 + 14, 408, 290, SLATE, 1.5) + txt(408, 306, L(lang, "Everyone else waits behind the first line", "Los demás esperan tras la primera línea"), 11.5, 700, INK, "end"))
    p.append(_sign("S-49", 588, 280, 34) + lines(630, 298, L(lang, ["S-49", "announces it"], ["S-49:", "la anuncia"]), 10.5, 700, SLATE, "start", 13))
    return svg(720, 336, "".join(p), L(lang, "Advanced stop box for motorcycles", "Zona de espera adelantada para motos"))


# ---------------------------------------------------------------- D3 motorcyclist guidance marks in a bend
def _pt(cx, cy, r, deg):
    a = math.radians(deg)
    return round(cx + r * math.cos(a), 1), round(cy + r * math.sin(a), 1)


def _arc(cx, cy, r, a0, a1):
    x0, y0 = _pt(cx, cy, r, a0)
    x1, y1 = _pt(cx, cy, r, a1)
    return f"M{x0} {y0} A{r} {r} 0 {1 if abs(a1 - a0) > 180 else 0} {0 if a1 < a0 else 1} {x1} {y1}"


def _stroke(d, color, w, dash=None, op=None):
    extra = (f' stroke-dasharray="{dash}"' if dash else "") + (f' opacity="{op}"' if op else "")
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}"{extra}/>'


def guide_marks(lang):
    cx, cy, rc = 170, 352, 280                       # left-hand bend: you ride the outer lane, anticlockwise
    p = [rect(0, 0, 720, 330, VERGE_BG)]
    p.append(_stroke(_arc(cx, cy, rc, 10, -150), ASPHALT, 116))
    p.append(_stroke(_arc(cx, cy, rc - 54, 10, -150), WHITE, 2.5) + _stroke(_arc(cx, cy, rc + 54, 10, -150), WHITE, 2.5))
    p.append(_stroke(_arc(cx, cy, rc, 10, -150), WHITE, 3))
    p.append(_stroke(_arc(cx, cy, rc + 12, -8, -112), "#fbbf24", 17, op="0.4"))
    for a in range(-12, -110, -8):
        x, y = _pt(cx, cy, rc + 12, a)
        p.append(f'<circle cx="{x}" cy="{y}" r="4.6" fill="#fff"/>')
    # your line, away from the centre line
    p.append(_stroke(_arc(cx, cy, rc + 36, 8, -110), "#5eead4", 2.2, "7 6"))
    x1, y1 = _pt(cx, cy, rc + 36, -110)
    x2, y2 = _pt(cx, cy, rc + 36, -117)
    p.append(arrow(x1, y1, x2, y2, "#5eead4", 2.2, 9))
    mx, my = _pt(cx, cy, rc + 36, -24)
    p.append(_moto(mx, my, -24, TEAL, 1.5))
    # oncoming car in the inner lane
    ox, oy = _pt(cx, cy, rc - 28, -76)
    p.append(rot(car_v(ox, oy, "#b45309", True, 20, 34), -76 + 180, ox, oy))
    # labels
    p.append(txt(476, 34, L(lang, "Motorcyclist guidance marks", "Marcas de guiado para motoristas"), 13.5, 800, INK))
    p.append(lines(476, 54, L(lang, ["They announce a bend of special risk and", "show the part of the lane that it is", "better not to ride on."],
                                    ["Anuncian una curva de especial riesgo y", "señalan la zona del carril que se", "recomienda evitar pisar."]), 11.5, 500, SLATE, "start", 15))
    kx, ky = _pt(cx, cy, rc + 12, -44)
    p.append(line(kx + 6, ky - 1, 488, 140, AMBER, 1.5) + txt(494, 144, L(lang, "Keep off this strip", "Evita esta franja"), 12, 800, AMBER))
    p.append(line(mx + 14, my, 504, 232, TEAL, 1.5) + lines(510, 230, L(lang, ["Your line: away from", "the centre line"], ["Tu trazada: lejos", "del eje"]), 12, 800, TEAL, "start", 15))
    p.append(line(ox + 2, oy + 20, 236, 246, SLATE, 1.3))
    p.append(lines(186, 262, L(lang, ["Oncoming lane: lean in next to", "the centre line and your body", "hangs over it"],
                                     ["Carril contrario: si te inclinas", "junto al eje, lo invades", "con el cuerpo"]), 11, 600, INK, "start", 14))
    p.append(lines(522, 288, L(lang, ["A recommendation: the usual rules", "of the road stay the same."], ["Es una recomendación: las normas", "de circulación no cambian."]), 10.5, 600, SLATE, "start", 14))
    return svg(720, 330, "".join(p), L(lang, "Motorcyclist guidance marks in a bend", "Marcas de guiado para motoristas en una curva"))
