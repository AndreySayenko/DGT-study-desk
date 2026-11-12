# -*- coding: utf-8 -*-
"""Original SVG diagrams for Category A1/A2, Topic 12 (riding techniques), EN/ES. No third-party artwork is used.
Five figures are drawn for this topic; the controls figure is shared with Category B, Topic 10."""
import math

from svgkit import NAVY, TEAL, AMBER, RED, SLATE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect, car_v, tick, cross, ASPHALT, WHITE
from ..b09.diagrams import L, line, MUTED, LINE, CARD
from ..b10.diagrams import arrow, badge
from ..b10.diagrams import moto_controls  # noqa: F401  (shared with Topic B10)
from ..b12.diagrams import moto_v, road_v, card
from ..b08 import signs as S

GOOD = "#0b7548"
GRASS = "#e8f0e3"


def _moto(cx, cy, deg, color=NAVY, k=1.5):
    """Motorcycle seen from above at (cx, cy), heading `deg` degrees clockwise from 'up', drawn k times larger."""
    return f'<g transform="translate({cx} {cy}) rotate({deg}) scale({k}) translate({-cx} {-cy})">{moto_v(cx, cy, color)}</g>'


# ---------------------------------------------------------------- D1 mirrors and blind spots on a motorcycle
def mirrors_moto(lang):
    x0, x1, top, bot = 120, 390, 10, 330
    lw = (x1 - x0) / 3
    cx, cy = x0 + 1.5 * lw, 110
    p = [rect(0, 0, 720, 340, GRASS), road_v(x0, x1, top, bot, 3)]
    for s in (-1, 1):
        p.append(f'<path d="M{cx + s * 14} {cy + 2} L{cx + s * 92} {bot} L{cx + s * 24} {bot} Z" fill="#93c5fd" opacity="0.55"/>')
        p.append(f'<path d="M{cx + s * 16} {cy - 10} L{cx + s * 16} {cy + 2} L{cx + s * 86} {cy + 150} L{cx + s * 96} {cy + 40} L{cx + s * 96} {cy - 10} Z" fill="{RED}" opacity="0.28"/>')
    p.append(_moto(cx, cy, 0, NAVY, 1.6))
    for s in (-1, 1):
        p.append(f'<circle cx="{cx + s * 13}" cy="{cy - 12}" r="3.5" fill="#e5e7eb" stroke="{INK}" stroke-width="1.2"/>')
    p.append(car_v(cx - lw + 4, cy + 62, "#b45309") + car_v(cx + lw - 20, cy + 196, "#64748b"))
    p.append(line(x0 - 4, cy + 40, x0 + 26, cy + 40, RED, 1.2) + lines(x0 - 10, cy + 30, L(lang, ["Blind", "spot"], ["Ángulo", "muerto"]), 12.5, 800, RED, "end", 15))
    p.append(line(x1 - 26, cy + 40, x1 + 4, cy + 40, RED, 1.2) + lines(x1 + 10, cy + 30, L(lang, ["Blind", "spot"], ["Ángulo", "muerto"]), 12.5, 800, RED, "start", 15))
    p.append(lines(x0 - 10, cy + 196, L(lang, ["Seen in the", "left mirror"], ["Se ve por el", "espejo izquierdo"]), 11, 700, "#1d4ed8", "end", 14))
    p.append(lines(x1 + 10, cy + 196, L(lang, ["Seen in the", "right mirror"], ["Se ve por el", "espejo derecho"]), 11, 700, "#1d4ed8", "start", 14))
    # what the law asks
    p.append(card(470, 14, 242, 248, NAVY))
    p.append(txt(486, 38, L(lang, "Compulsory mirrors", "Retrovisores obligatorios"), 13, 800, INK))
    rows = [
        (L(lang, ["Two-wheel moped"], ["Ciclomotor de dos ruedas"]), True, False),
        (L(lang, ["Motorcycle, top speed", "up to 100 km/h"], ["Moto de velocidad", "máxima hasta 100 km/h"]), True, False),
        (L(lang, ["Motorcycle, top speed", "over 100 km/h"], ["Moto de velocidad", "máxima de más de 100 km/h"]), True, True),
    ]
    p.append(txt(640, 60, L(lang, "left", "izq."), 10.5, 700, MUTED, "middle") + txt(686, 60, L(lang, "right", "dcha."), 10.5, 700, MUTED, "middle"))
    for i, (name, left, right) in enumerate(rows):
        y = 72 + i * 50
        p.append(lines(486, y + 16 if len(name) == 1 else y + 10, name, 11, 600, INK, "start", 14))
        p.append(tick(640, y + 16, 10))
        p.append(tick(686, y + 16, 10) if right else txt(686, y + 20, L(lang, "optional", "opcional"), 9.5, 700, MUTED, "middle"))
    p.append(lines(486, 232, L(lang, ["Turn your head and look before", "any sideways move."], ["Gira la cabeza y mira antes", "de cualquier desplazamiento lateral."]), 11, 700, AMBER, "start", 14))
    return svg(720, 340, "".join(p), L(lang, "Mirrors and blind spots on a motorcycle", "Retrovisores y ángulos muertos en moto"))


# ---------------------------------------------------------------- D2 riding a bend
def curve_moto(lang):
    ccx, ccy, R = 300, 52, 188
    road = f"M20 {ccy + R} L{ccx} {ccy + R} A{R} {R} 0 0 0 {ccx + R} {ccy} L{ccx + R} -10"
    p = [rect(0, 0, 720, 320, GRASS), f'<path d="{road}" fill="none" stroke="{ASPHALT}" stroke-width="58"/>',
         f'<path d="{road}" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="12 10"/>']
    p.append(line(ccx, ccy + R - 30, ccx, ccy + R + 30, "#fde047", 3) + line(ccx + R - 30, ccy, ccx + R + 30, ccy, "#fde047", 3))
    # the rider's line, in the middle of the own lane, away from the centre line
    a = math.radians(45)
    p.append(_moto(150, ccy + R + 15, 90, NAVY))
    mx, my = ccx + (R - 15) * math.cos(a), ccy + (R - 15) * math.sin(a)
    p.append(_moto(round(mx, 1), round(my, 1), 45, NAVY))
    p.append(_moto(ccx + R + 15, 92, 0, NAVY))
    # where to look: the exit
    p.append(f'<path d="M{mx:.1f} {my:.1f} L{ccx + R + 15} {ccy - 6}" stroke="{TEAL}" stroke-width="2" stroke-dasharray="6 5" fill="none"/>')
    p.append(f'<circle cx="{ccx + R + 15}" cy="{ccy - 6}" r="6" fill="none" stroke="{TEAL}" stroke-width="2.5"/>')
    # centrifugal force outwards
    ox, oy = ccx + (R + 34) * math.cos(a), ccy + (R + 34) * math.sin(a)
    p.append(arrow(ox, oy, ox + 42, oy + 42, RED, 3, 11))
    p.append(lines(ox + 50, oy + 28, L(lang, ["Centrifugal force pushes you out:", "more weight, more speed or a", "tighter bend, more force"],
                                       ["La fuerza centrífuga te empuja fuera:", "más peso, más velocidad o curva", "más cerrada, más fuerza"]), 11, 600, INK, "start", 14))
    p.append(badge(150, ccy + R - 50, 1) + lines(166, ccy + R - 52, L(lang, ["Before: brake upright, on the", "straight; choose your line"], ["Antes: frena recto, en la", "recta; elige la trayectoria"]), 11.5, 600, INK, "start", 14))
    p.append(badge(200, 70, 2) + lines(216, 74, L(lang, ["During: gentle,", "progressive throttle;", "look at the exit;", "leaning takes more", "width: keep off", "the centre line"],
                                                    ["Durante: acelera", "suave y progresivo;", "mira a la salida;", "inclinada ocupa", "más anchura: no", "invadas el contrario"]), 11.5, 600, INK, "start", 14))
    p.append(badge(ccx + R + 50, 30, 3) + lines(ccx + R + 66, 28, L(lang, ["Exit: accelerate", "and bring the", "motorcycle upright"], ["Salida: acelera", "y endereza", "la moto"]), 11.5, 600, INK, "start", 14))
    return svg(720, 300, "".join(p), L(lang, "Riding a bend", "Cómo tomar una curva en moto"))


# ---------------------------------------------------------------- D3 emergency braking
def braking_moto(lang):
    cx, cy, k = 200, 150, 5.2
    gy = cy + 8 * k + 6.5 * k
    p = [rect(8, 8, 400, 290, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'), line(20, gy, 396, gy, "#94a3b8", 2)]
    p.append(S.at(S.moto(NAVY), cx, cy, k))
    p.append(arrow(cx - 40, cy - 84, cx + 70, cy - 84, AMBER, 3.5, 12))
    p.append(txt(cx + 15, cy - 94, L(lang, "weight moves forward", "el peso se desplaza adelante"), 11.5, 800, AMBER, "middle"))
    rx, fx = cx - 14 * k, cx + 14 * k
    for x, share, lab, col in ((rx, "30–40 %", L(lang, "rear brake", "freno trasero"), "#93c5fd"), (fx, "60–70 %", L(lang, "front brake", "freno delantero"), NAVY)):
        p.append(rect(x - 46, gy + 12, 92, 28, col, 6) + txt(x, gy + 31, share, 13, 800, "#fff" if col == NAVY else INK, "middle"))
        p.append(txt(x, gy + 56, lab, 11, 700, INK, "middle"))
    p.append(txt(208, 30, L(lang, "Share of the braking in an emergency", "Reparto de la frenada de emergencia"), 12.5, 800, INK, "middle"))
    steps = [
        (L(lang, "Brake upright", "Frena recto"), L(lang, ["before leaning, or once the", "motorcycle is upright"], ["antes de inclinar la moto", "o con ella ya derecha"])),
        (L(lang, "Both brakes, clutch in", "Los dos frenos y desembraga"), L(lang, ["hard use of both, only in an", "emergency"], ["uso intensivo de ambos, solo", "en una emergencia"])),
        (L(lang, "Rigid body", "Cuerpo rígido"), L(lang, ["arms straight, knees against", "the tank, heels on the footrests"], ["brazos estirados, rodillas al", "depósito, talones en reposapiés"])),
        (L(lang, "A wheel locks?", "¿Se bloquea una rueda?"), L(lang, ["release that brake at once and", "brake again"], ["suelta ese freno enseguida y", "vuelve a frenar"])),
    ]
    for i, (title, body) in enumerate(steps):
        y = 8 + i * 74
        p.append(card(420, y, 292, 66, NAVY) + badge(442, y + 22, i + 1) + txt(460, y + 27, title, 12.5, 800, INK) + lines(442, y + 46, body, 10.5, 500, INK, "start", 13))
    p.append(lines(208, 318, L(lang, ["The rear wheel loses grip and can lock and skid;", "with a passenger it locks less, so the rear brake can work harder."],
                                     ["La rueda trasera pierde agarre y puede bloquearse y derrapar;", "con pasajero se bloquea menos y el freno trasero puede trabajar más."]), 10.5, 600, SLATE, "middle", 13))
    return svg(720, 340, "".join(p), L(lang, "Emergency braking on a motorcycle", "Frenada de emergencia en moto"))


# ---------------------------------------------------------------- D4 riding in a group
def group_ride(lang):
    top, mid, bot = 96, 146, 196
    p = [rect(0, 0, 720, 290, GRASS), rect(0, top, 720, bot - top, ASPHALT)]
    p.append(rect(0, top + 3, 720, 3, WHITE) + rect(0, bot - 6, 720, 3, WHITE) + "".join(rect(x, mid - 1.5, 24, 3, WHITE) for x in range(0, 720, 44)))
    lead = [(640, 160, TEAL), (590, 182, TEAL), (540, 160, TEAL)]
    rear = [(370, 160, NAVY), (320, 182, NAVY), (270, 160, NAVY), (220, 182, NAVY)]
    for x, y, c in lead + rear:
        p.append(_moto(x, y, 90, c, 1.35))
    p.append(arrow(668, 120, 712, 120, WHITE, 2.5, 9))
    p.append(line(400, 214, 512, 214, AMBER, 2) + line(400, 206, 400, 222, AMBER, 2) + line(512, 206, 512, 222, AMBER, 2))
    p.append(txt(456, 238, L(lang, "gap between subgroups", "separación entre subgrupos"), 11, 800, AMBER, "middle"))
    p.append(lines(590, 30, L(lang, ["Front subgroup: the least", "experienced riders and the", "least powerful motorcycles"], ["Subgrupo de cabeza: los", "menos experimentados y las", "motos de menos potencia"]), 11, 700, TEAL, "middle", 14))
    p.append(lines(296, 30, L(lang, ["Subgroups of three or four,", "in single file, slightly offset", "so each rider sees ahead"], ["Subgrupos de tres o cuatro,", "en hilera, algo desviados para", "ver hacia delante"]), 11, 700, INK, "middle", 14))
    p.append(cross(40, 252, 10) + txt(58, 256, L(lang, "Never side by side", "Nunca en paralelo"), 11.5, 800, RED))
    p.append(tick(250, 252, 10) + txt(268, 256, L(lang, "Each rider is responsible for their own riding", "La responsabilidad es de cada conductor"), 11.5, 800, GOOD))
    return svg(720, 276, "".join(p), L(lang, "Riding in a group", "Conducción en grupo"))


# ---------------------------------------------------------------- D5 where the luggage goes
def luggage_moto(lang):
    cx, cy, k = 250, 140, 5
    gy = cy + 8 * k + 6.5 * k
    p = [rect(8, 8, 704, 300, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'), line(20, gy, 480, gy, "#94a3b8", 2)]
    p.append(S.at(S.moto("#334155"), cx, cy, k))
    # tank bag (front rack), top case (rear rack), side case (pannier)
    p.append(rect(cx + 30, cy - 34, 30, 16, GOOD, 4))
    p.append(rect(cx - 94, cy - 40, 46, 32, AMBER, 6) + rect(cx - 50, cy - 10, 14, 4, "#334155", 1))
    p.append(f'<rect x="{cx - 104}" y="{cy - 6}" width="56" height="44" rx="6" fill="#1d4ed8" opacity="0.85"/>')
    p.append(line(cx + 45, cy - 36, cx + 70, cy - 82, GOOD, 1.5) + line(cx - 71, cy - 42, cx - 71, cy - 92, AMBER, 1.5) + line(cx - 100, cy + 30, cx - 150, gy + 8, "#1d4ed8", 1.5))
    p.append(lines(cx + 74, cy - 98, L(lang, ["Front rack (on the tank):", "heavy items"], ["Portaequipajes delantero", "(depósito): objetos pesados"]), 11, 800, GOOD, "start", 13))
    p.append(lines(cx - 70, cy - 108, L(lang, ["Rear rack (top case):", "light items only"], ["Portaequipajes trasero", "(baúl): solo objetos ligeros"]), 11, 800, AMBER, "middle", 13))
    p.append(lines(cx - 150, gy + 24, L(lang, ["Side cases: the same", "weight on each side,", "heaviest at the bottom"], ["Maletas laterales: el mismo", "peso a cada lado, lo más", "pesado en el fondo"]), 11, 800, "#1d4ed8", "middle", 13))
    rules = L(lang, [
        "Only what you need, without",
        "exceeding the maximum mass.",
        "",
        "Keep the weight low and close",
        "to the centre of gravity.",
        "",
        "Strap down everything that has",
        "no fixing: nothing may move or fall.",
        "",
        "Nothing near the handlebar, wheels,",
        "suspension, pedals or transmission.",
        "",
        "Adjust the suspension for the load.",
    ], [
        "Solo lo necesario, sin superar",
        "la masa máxima autorizada.",
        "",
        "El peso bajo y cerca del",
        "centro de gravedad.",
        "",
        "Amarra todo lo que no tenga",
        "anclaje: nada puede moverse ni caer.",
        "",
        "Nada cerca del manillar, ruedas,",
        "suspensión, pedales ni transmisión.",
        "",
        "Ajusta la amortiguación a la carga.",
    ])
    p.append(rect(492, 22, 208, 272, "#fff", 10, f' stroke="{LINE}" stroke-width="1.5"') + lines(506, 48, rules, 11, 600, INK, "start", 16))
    p.append(txt(250, 292, L(lang, "Heavy items in the top case make the motorcycle wobble (fluctuation).", "Los objetos pesados en el baúl provocan fluctuación."), 11, 700, RED, "middle"))
    return svg(720, 316, "".join(p), L(lang, "Where to carry luggage on a motorcycle", "Dónde llevar el equipaje en moto"))
