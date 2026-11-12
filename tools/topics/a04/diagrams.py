# -*- coding: utf-8 -*-
"""Original SVG diagrams for Category A1/A2, Topic 4 (priority), EN/ES. No third-party artwork is used. Two figures
are specific to this topic; the others are shared with Category B, Topic 4."""

from svgkit import NAVY, TEAL, AMBER, RED, SLATE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect, car_h, ASPHALT, VERGE, WHITE
from ..b09.diagrams import L, line, MUTED, LINE, CARD  # noqa: F401
from ..b10.diagrams import arrow, rot, badge
from ..b12.diagrams import moto_v
from ..b04.diagrams import priority_signs, right_rule, blocking_box, vulnerable_turn, narrowing, emergency_signals, corridor  # noqa: F401  (shared with Topic B4)

MOTO = "#dc2626"
MOTO_BG = "#fee2e2"
BAR_BG = "#e2e8f0"


# ---------------------------------------------------------------- D1 order of priority in a narrow stretch
def narrow_order(lang):
    rows = {
        "en": ["Special vehicles and special transport over the set masses or dimensions",
               "Vehicle combinations (except those in 4)",
               "Animal-drawn vehicles",
               "Cars towing a trailer up to 750 kg MMA, motorhomes",
               "Buses",
               "Lorries, tractor units and large vans",
               "Cars, car-derived vans, adaptable mixed vehicles",
               "Special vehicles within the limits, quadricycles, light quadricycles",
               "Three-wheeled vehicles, motorcycles with sidecar, three-wheeled mopeds",
               "Motorcycles, two-wheeled mopeds, bicycles"],
        "es": ["Especiales y transporte especial que exceden masas o dimensiones",
               "Conjuntos de vehículos (salvo los del punto 4)",
               "Vehículos de tracción animal",
               "Turismos con remolque de hasta 750 kg de MMA, autocaravanas",
               "Autobuses",
               "Camiones, tractocamiones y furgones",
               "Turismos, derivados de turismo, mixtos adaptables",
               "Especiales que no exceden los límites, cuadriciclos y cuadriciclos ligeros",
               "Vehículos de tres ruedas, motos con sidecar, ciclomotores de tres ruedas",
               "Motocicletas, ciclomotores de dos ruedas y bicicletas"],
    }[lang]
    p = [txt(48, 20, L(lang, "▲ Goes first: harder to manoeuvre", "▲ Pasa primero: mayor dificultad de maniobra"), 12, 800, INK)]
    top, rh = 30, 27
    for i, label in enumerate(rows):
        y = top + i * rh
        moto = i >= 8
        w = 660 - i * 24
        p.append(rect(48, y, w, rh - 5, MOTO_BG if moto else BAR_BG, 6, f' stroke="{MOTO}" stroke-width="1.5"' if moto else ""))
        p.append(badge(28, y + (rh - 5) / 2, i + 1, MOTO if moto else NAVY))
        p.append(txt(58, y + 15.5, label, 11.5, 800 if moto else 600, INK))
    yb = top + 10 * rh
    p.append(txt(48, yb + 14, L(lang, "▼ Gives way and reverses", "▼ Cede el paso y retrocede"), 12, 800, INK))
    p.append(txt(712, yb - 4 - rh, L(lang, "your family of vehicles", "tu familia de vehículos"), 11, 800, MOTO, "end"))
    p.append(lines(48, yb + 38, L(lang, ["Same type, or a type not on the list: the one that would have to reverse further goes first;",
                                         "if that is equal, the one with the greater width, length or MMA."],
                                        ["Mismo tipo o tipo no enumerado: pasa el que tuviera que dar marcha atrás mayor distancia;",
                                         "si es igual, el de mayor anchura, longitud o masa máxima autorizada."]), 11, 600, SLATE, "start", 15))
    return svg(720, yb + 66, "".join(p), L(lang, "Order of priority in a narrow stretch without signs", "Orden de preferencia en un estrechamiento sin señalizar"))


# ---------------------------------------------------------------- D2 police order to stop (forward red light)
def _police(cx, cy, flash=True, ghost=False):
    op = ' opacity="0.45"' if ghost else ""
    out = car_h(cx, cy, "#1e3a8a") + rect(cx - 5, cy - 7, 8, 14, "#60a5fa", 2)
    if flash:
        out += f'<circle cx="{cx - 1}" cy="{cy}" r="11" fill="#60a5fa" opacity="0.35"/>'
        for dy in (-7, 0, 7):
            out += line(cx + 24, cy + dy * 0.4, cx + 40, cy + dy * 1.6, RED, 2.6)
        out += f'<circle cx="{cx + 21}" cy="{cy}" r="3.4" fill="{RED}"/>'
    return f"<g{op}>{out}</g>"


def police_stop(lang):
    p = [txt(360, 20, L(lang, "Police signal to stop (since July 2025)", "Orden de detención de la policía (desde julio de 2025)"), 13, 800, INK, "middle")]
    p.append(rect(0, 32, 720, 26, VERGE))
    p.append(rect(0, 58, 720, 106, ASPHALT))
    p.append(line(0, 111, 720, 111, WHITE, 2.4, "18 14"))
    p.append(line(0, 164, 720, 164, WHITE, 3))
    p.append(rect(0, 167, 720, 30, "#9ca3af"))
    p.append(rect(0, 197, 720, 18, VERGE))
    # moving: police behind the motorcycle in the right-hand lane
    p.append(_police(150, 138))
    p.append(rot(moto_v(262, 138, MOTO), 90, 262, 138))
    p.append(f'<path d="M286 138 C 480 138, 520 182, 584 182" fill="none" stroke="#fde68a" stroke-width="2.6" stroke-dasharray="7 5"/>')
    p.append(arrow(576, 182, 592, 182, "#fde68a", 2.6))
    # stopped: motorcycle on the right, police behind it
    p.append(rot(moto_v(614, 182, MOTO), 90, 614, 182))
    p.append(_police(470, 182, flash=False, ghost=True))
    p.append(badge(614, 152, 2, RED))
    p.append(badge(150, 106, 1, NAVY))
    steps = L(lang, [("1", "Police behind you: blue light and siren, plus a red light flashing forward."),
                     ("2", "Stop on the right, in front of the police vehicle, where you create no extra risk."),
                     ("3", "Stay there and follow the agent’s instructions (loudspeaker or other clear means).")],
                    [("1", "Policía detrás: luz azul y sirena, y además una luz roja intermitente hacia delante."),
                     ("2", "Detente a la derecha, delante del vehículo policial, donde no generes más riesgo."),
                     ("3", "Permanece en tu sitio y sigue las instrucciones del agente (megafonía u otro medio).")])
    for i, (n, s) in enumerate(steps):
        y = 236 + i * 24
        p.append(badge(30, y - 4, n, RED if n == "2" else NAVY))
        p.append(txt(48, y + 0.5, s, 12, 600, INK))
    return svg(720, 300, "".join(p), L(lang, "Police signal to stop", "Orden de detención de la policía"))
