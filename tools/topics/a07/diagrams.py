# -*- coding: utf-8 -*-
"""Original SVG diagrams for Category A1/A2, Topic 7 (lights), EN/ES. No third-party artwork is used. Two figures are
specific to this topic; four are shared with Category B, Topic 7."""

from svgkit import NAVY, TEAL, AMBER, RED, SLATE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect
from ..b09.diagrams import L, line, MUTED, LINE, CARD  # noqa: F401
from ..b08.signs import at, moto
from ..b07.diagrams import fog_matrix, overtake_dazzle, curve_dazzle, dazzled_view  # noqa: F401  (shared with Topic B7)

DARK = "#1f2937"
BODY = "#475569"
AMBER_L = "#f59e0b"
RED_L = "#dc2626"
WARM = "#fef9c3"


def fog_matrix_moto(lang):
    """Topic B7's fog-light matrix, with the rear fog light shown as optional equipment, as it is on a motorcycle."""
    return fog_matrix(lang, moto=True)


def _callout(x1, y1, x2, y2, label, anchor):
    tx = x2 - 6 if anchor == "end" else x2 + 6
    return (line(x1, y1, x2, y2, SLATE, 1.3) + f'<circle cx="{x1}" cy="{y1}" r="2.4" fill="{SLATE}"/>'
            + lines(tx, y2 + 4, label, 11, 700, INK, anchor, 13))


def _dashed(shape):
    return shape.replace("/>", ' stroke-dasharray="3 2" stroke-width="2"/>', 1)


# ---------------------------------------------------------------- D1 a motorcycle’s lights, front and rear
def _num(cx, cy, n):
    return f'<circle cx="{cx}" cy="{cy}" r="9" fill="{NAVY}"/>' + txt(cx, cy + 4, str(n), 11, 800, "#fff", "middle")


def moto_lights(lang):
    p = []
    for ox, title in ((8, L(lang, "Front", "Delante")), (368, L(lang, "Rear", "Detrás"))):
        p.append(rect(ox, 6, 344, 340, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'))
        p.append(txt(ox + 172, 28, title, 13, 800, INK, "middle"))
    # front view
    cx = 180
    p.append(rect(cx - 11, 150, 22, 62, DARK, 9))
    p.append(line(cx - 16, 104, cx - 9, 160, "#64748b", 5) + line(cx + 16, 104, cx + 9, 160, "#64748b", 5))
    p.append(line(cx - 80, 66, cx + 80, 66, DARK, 5))
    for s_ in (-1, 1):
        p.append(line(cx + s_ * 64, 66, cx + s_ * 70, 46, DARK, 2.5) + f'<circle cx="{cx + s_ * 72}" cy="42" r="7" fill="#94a3b8"/>')
        p.append(rect(cx + s_ * 54 - 9, 84, 18, 9, AMBER_L, 4))
    p.append(f'<circle cx="{cx}" cy="98" r="34" fill="{WARM}" opacity="0.5"/><circle cx="{cx}" cy="98" r="26" fill="#334155"/><circle cx="{cx}" cy="98" r="19" fill="{WARM}"/>')
    p.append(rect(cx - 10, 129, 20, 6, "#fff", 3, ' stroke="#94a3b8" stroke-width="1"'))
    for s_ in (-1, 1):
        p.append(_dashed(f'<circle cx="{cx + s_ * 30}" cy="150" r="8" fill="#fff" stroke="{SLATE}"/>'))
    p.append(_num(cx + 42, 76, 1) + _num(cx - 28, 132, 2) + _num(cx - 54, 106, 3) + _num(cx + 52, 160, 4))
    front = L(lang, ["Dipped and main beam (white): 1 or 2", "Position light: white", "Indicators: amber", "Fog lights: optional, white or selective yellow"],
                    ["Cruce y carretera (blancas): 1 o 2", "Luz de posición: blanca", "Intermitentes: amarillo auto", "Antiniebla: opcional, blanca o amarillo selectivo"])
    for k, t_ in enumerate(front):
        y = 236 + k * 24
        p.append(_num(30, y - 4, k + 1) + txt(46, y, t_, 11.5, 600, INK))
    # rear view
    cx = 540
    p.append(rect(cx - 13, 166, 26, 46, DARK, 9))
    p.append(rect(cx - 42, 58, 84, 54, BODY, 12))
    p.append(f'<rect x="{cx - 34}" y="62" width="68" height="20" rx="6" fill="{RED_L}" opacity="0.25"/>' + rect(cx - 26, 66, 52, 12, RED_L, 4))
    for s_ in (-1, 1):
        p.append(line(cx + s_ * 40, 90, cx + s_ * 56, 90, DARK, 3) + rect(cx + s_ * 62 - 9, 85, 18, 9, AMBER_L, 4))
    p.append(_dashed(f'<rect x="{cx - 34}" y="92" width="14" height="10" rx="3" fill="#fecaca" stroke="{RED_L}"/>'))
    p.append(_dashed(f'<rect x="{cx + 20}" y="92" width="14" height="10" rx="3" fill="#fff" stroke="{SLATE}"/>'))
    p.append(rect(cx - 8, 113, 16, 5, "#fde68a", 2))
    p.append(rect(cx - 30, 119, 60, 32, "#fff", 3, f' stroke="{INK}" stroke-width="1.5"') + rect(cx - 30, 119, 9, 32, "#1d4ed8", 2))
    p.append(rect(cx - 15, 155, 30, 8, "#b91c1c", 3))
    p.append(_num(cx + 46, 66, 1) + _num(cx - 76, 72, 2) + _num(cx + 44, 120, 3) + _num(cx - 30, 168, 4) + _num(cx, 97, 5))
    rear = L(lang, ["Position and brake light: red", "Indicators: amber", "Plate light: on with the position lights", "Rear reflector: red, not triangular (compulsory)", "Rear fog (red), reversing (white): optional"],
                   ["Posición y freno: rojas", "Intermitentes: amarillo auto", "Luz de matrícula: con la de posición", "Catadióptrico: rojo, no triangular (obligatorio)", "Antiniebla (roja) y marcha atrás (blanca): opcionales"])
    for k, t_ in enumerate(rear):
        y = 236 + k * 22
        p.append(_num(390, y - 4, k + 1) + txt(406, y, t_, 11.5 if lang == "en" else 11, 600, INK))
    p.append(lines(360, 364, L(lang, ["Solid: compulsory · dashed outline: optional.", "Hazard lights (all indicators at once) are optional on motorcycles; side reflectors (amber) too."],
                                       ["Trazo continuo: obligatorio · discontinuo: opcional.", "La luz de emergencia (todos los intermitentes a la vez) es opcional en moto; también los catadióptricos laterales."]),
                   10.5, 600, SLATE, "middle", 14))
    return svg(720, 388, "".join(p), L(lang, "A motorcycle’s lights", "Las luces de la motocicleta"))


# ---------------------------------------------------------------- D2 a passenger or a load tilts the beam upwards
def _road(ox, w, gy):
    return rect(ox, gy, w, 22, "#4b5563") + line(ox, gy + 11, ox + w, gy + 11, "#fff", 2, "12 10")


def beam_tilt(lang):
    p = []
    gy = 196
    for ox, title in ((8, L(lang, "Rider alone: beam on the road", "Solo el conductor: haz hacia la vía")),
                      (368, L(lang, "Passenger or load behind: beam rises", "Pasajero o carga detrás: el haz sube"))):
        p.append(rect(ox, 6, 344, 290, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'))
        p.append(txt(ox + 172, 30, title, 12.5, 800, INK, "middle"))
        p.append(rect(ox + 1, 60, 342, gy - 60, "#0f172a", 0))
        p.append(_road(ox + 1, 342, gy))
    # panel 1
    p.append(f'<path d="M108 168 L340 {gy} L340 {gy - 22} Z" fill="{WARM}" opacity="0.55"/>')
    p.append(at(moto("#e5e7eb"), 82, 172, 2.4))
    p.append(lines(180, 244, L(lang, ["The light reaches the road ahead", "without dazzling anyone"], ["La luz alumbra la vía por delante", "sin deslumbrar a nadie"]), 11.5, 700, INK, "middle", 15))
    # panel 2: rear sinks under the weight, the beam points up
    p.append(f'<path d="M468 160 L702 92 L702 130 Z" fill="{WARM}" opacity="0.55"/>')
    p.append(f'<g transform="rotate(-6 412 192)">' + at(moto("#e5e7eb"), 442, 172, 2.4) + rect(400, 140, 22, 18, "#b45309", 4) + "</g>")
    p.append(rect(650, 150, 46, 20, "#64748b", 6) + rect(652, 154, 10, 12, "#cbd5e1", 2))
    p.append(f'<circle cx="657" cy="146" r="10" fill="#fde047" opacity="0.8"/>')
    p.append(lines(540, 244, L(lang, ["The rear sinks, the beam points higher and can", "dazzle oncoming drivers: adjust the headlight"],
                                     ["La parte trasera baja, el haz apunta más alto y puede", "deslumbrar a los que vienen: regula el faro"]), 11.5, 700, INK, "middle", 15))
    return svg(720, 302, "".join(p), L(lang, "Headlight aim with a passenger or load", "Reglaje del faro con pasajero o carga"))
