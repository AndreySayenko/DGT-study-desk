# -*- coding: utf-8 -*-
"""Original SVG diagrams for Category A1/A2, Topic 5 (manoeuvres), EN/ES. No third-party artwork is used. Two
figures are specific to this topic; three are shared with Category B, Topic 5."""

from svgkit import NAVY, TEAL, AMBER, RED, SLATE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect, car_v, tick, cross, ASPHALT, VERGE, WHITE
from ..b09.diagrams import L, line, MUTED, LINE, CARD  # noqa: F401
from ..b12.diagrams import moto_v
from ..b05.diagrams import overtake_cyclist, turn_positions, immobilisations  # noqa: F401  (shared with Topic B5)

MOTO = "#dc2626"
DARK = "#1f2937"
SKIN = "#e7b98f"
INDICATOR = "#f59e0b"
OFF = "#94a3b8"


def _arm(x1, y1, x2, y2, op=1.0):
    o = f' opacity="{op}"' if op < 1 else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{NAVY}" stroke-width="10" stroke-linecap="round"{o}/>'


def _hand(x, y, op=1.0):
    o = f' opacity="{op}"' if op < 1 else ""
    return f'<circle cx="{x}" cy="{y}" r="6" fill="{SKIN}"{o}/>'


def _rider_rear(cx, by, pose, left_on=False, right_on=False, brake=False):
    """A rider on a motorcycle seen from behind; `by` is ground level. pose: 'left', 'right' or 'slow'."""
    p = [rect(cx - 10, by - 48, 20, 48, DARK, 9),                              # rear tyre
         rect(cx - 24, by - 74, 48, 24, "#475569", 9),                         # tail
         rect(cx - 10, by - 66, 20, 8, MOTO if brake else "#7f1d1d", 3)]       # brake light
    if brake:
        p.append(f'<circle cx="{cx}" cy="{by - 62}" r="15" fill="{MOTO}" opacity="0.25"/>')
    for x, on in ((cx - 33, left_on), (cx + 33, right_on)):
        p.append(f'<circle cx="{x}" cy="{by - 62}" r="5.5" fill="{INDICATOR if on else OFF}"/>')
        if on:
            p.append(f'<circle cx="{x}" cy="{by - 62}" r="11" fill="{INDICATOR}" opacity="0.3"/>')
    p.append(line(cx - 36, by - 84, cx + 36, by - 84, DARK, 4))               # handlebar
    p.append(rect(cx - 21, by - 134, 42, 62, NAVY, 15))                        # torso
    p.append(f'<circle cx="{cx}" cy="{by - 148}" r="16" fill="#334155"/>')     # helmet
    p.append(_arm(cx + 17, by - 122, cx + 32, by - 86) + _hand(cx + 32, by - 86))  # right hand on the bar
    sx, sy = cx - 17, by - 122
    if pose == "left":
        p.append(_arm(sx, sy, cx - 86, sy) + _hand(cx - 90, sy))
    elif pose == "right":
        p.append(_arm(sx, sy, cx - 60, sy) + _arm(cx - 60, sy, cx - 60, sy - 44) + _hand(cx - 60, sy - 50))
    else:
        p.append(_arm(sx, sy, cx - 80, sy - 22, 0.35) + _hand(cx - 84, sy - 24, 0.35))
        p.append(_arm(sx, sy, cx - 80, sy + 18) + _hand(cx - 84, sy + 20))
        p.append(f'<path d="M{cx - 100} {sy - 22} L{cx - 100} {sy + 18}" stroke="{SLATE}" stroke-width="2.2"/>'
                 f'<path d="M{cx - 104} {sy - 16} L{cx - 100} {sy - 24} L{cx - 96} {sy - 16} Z M{cx - 104} {sy + 12} L{cx - 100} {sy + 20} L{cx - 96} {sy + 12} Z" fill="{SLATE}"/>')
    return "".join(p)


def rider_arm_signals(lang):
    panels = [
        ("left", L(lang, ["Move or turn left"], ["Desplazamiento o giro", "a la izquierda"]), L(lang, "= left indicator", "= intermitente izquierdo"), dict(left_on=True)),
        ("right", L(lang, ["Move or turn right"], ["Desplazamiento o giro", "a la derecha"]), L(lang, "= right indicator", "= intermitente derecho"), dict(right_on=True)),
        ("slow", L(lang, ["Slow down a lot or stop"], ["Frenar mucho o detenerse"]), L(lang, "= brake light, repeated", "= luz de freno, reiterada"), dict(brake=True)),
    ]
    p = []
    for i, (pose, title, chip, kw) in enumerate(panels):
        cx = 124 + i * 236
        p.append(rect(cx - 112, 6, 224, 300, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'))
        p.append(lines(cx, 30, title, 12.5, 800, INK, "middle", 15))
        p.append(_rider_rear(cx + 18, 248, pose, **kw))
        p.append(line(cx - 96, 249, cx + 96, 249, "#cbd5e1", 2))
        p.append(rect(cx - 96, 264, 192, 26, "#e2e8f0", 13) + txt(cx, 281, chip, 11.5, 700, INK, "middle"))
    p.append(lines(360, 330, L(lang, ["Seen from behind. Left arm, palm extended: horizontal for left, bent upwards for right, moved up and down to slow down.",
                                        "Your course: if the lights and the arm say different things, the arm prevails."],
                                       ["Visto desde atrás. Brazo izquierdo con la palma extendida: horizontal para la izquierda, doblado hacia arriba para la derecha,",
                                        "y moviéndolo de arriba abajo para frenar. Según tu curso, si las luces y el brazo se contradicen, prevalece el brazo."]), 11, 600, SLATE, "middle", 15))
    return svg(720, 352, "".join(p), L(lang, "Arm signals on a motorcycle", "Señales con el brazo en moto"))


# ---------------------------------------------------------------- D2 overtaking rules that concern two-wheelers
def _road_v(x0, x1, top, bot):
    mid = (x0 + x1) / 2
    return (rect(x0, top, x1 - x0, bot - top, ASPHALT) + line(x0 + 4, top, x0 + 4, bot, WHITE, 2.5) + line(x1 - 4, top, x1 - 4, bot, WHITE, 2.5)
            + line(mid, top, mid, bot, WHITE, 2.5, "14 12"))


def two_wheel_overtake(lang):
    p = []
    top, bot = 46, 238
    for i in range(3):
        ox = 8 + i * 238
        p.append(rect(ox, 6, 228, 330, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'))
        p.append(rect(ox + 10, top, 208, bot - top, VERGE, 6))
    # panel 1: a motorcycle overtaking a car out of town, 1.5 m
    cx = 122
    p.append(_road_v(cx - 50, cx + 50, top, bot))
    p.append(car_v(cx + 25, 160, "#64748b"))
    p.append(moto_v(cx - 26, 140, MOTO))
    p.append(f'<path d="M{cx - 18} 150 H{cx + 13}" stroke="{AMBER}" stroke-width="2.6"/><path d="M{cx - 18} 144 V156 M{cx + 13} 144 V156" stroke="{AMBER}" stroke-width="2.6"/>')
    p.append(line(cx - 2, 150, cx - 2, 100, AMBER, 1.6, "3 3"))
    p.append(rect(cx - 32, 78, 64, 22, AMBER, 11) + txt(cx, 93.5, "≥ 1,5 m" if lang == "es" else "≥ 1.5 m", 12, 800, "#fff", "middle"))
    p.append(tick(cx + 82, 66))
    p.append(lines(cx, 262, L(lang, ["Out of town, a two-wheeler", "overtaking anything keeps", "at least 1.5 m to the side"],
                                     ["Fuera de poblado, la moto que", "adelanta a cualquier vehículo", "deja al menos 1,5 m"]), 12, 700, INK, "middle", 16))
    # panel 2: junction — two-wheelers may be overtaken there
    cx = 360
    p.append(rect(cx - 104, 108, 208, 54, ASPHALT))
    p.append(_road_v(cx - 50, cx + 50, top, bot))
    p.append(rect(cx - 46, 112, 92, 46, ASPHALT))
    p.append(moto_v(cx + 25, 128, MOTO))
    p.append(car_v(cx - 25, 150, "#64748b"))
    p.append(tick(cx + 82, 66))
    p.append(lines(cx, 262, L(lang, ["At junctions overtaking is", "forbidden, but two-wheelers", "may be overtaken there"],
                                     ["En las intersecciones se prohíbe", "adelantar, pero a los vehículos", "de dos ruedas sí se les puede"]), 12, 700, INK, "middle", 16))
    # panel 3: level crossing — not even two-wheelers since 1 October 2026
    cx = 598
    p.append(_road_v(cx - 50, cx + 50, top, bot))
    for dy in range(-30, 34, 12):
        p.append(rect(cx - 104, 132 + dy, 208, 5, "#78716c"))
    p.append(line(cx - 104, 120, cx + 104, 120, "#d6d3d1", 3) + line(cx - 104, 154, cx + 104, 154, "#d6d3d1", 3))
    p.append(moto_v(cx + 25, 168, MOTO))
    p.append(car_v(cx - 25, 206, "#64748b"))
    p.append(cross(cx + 82, 66))
    p.append(lines(cx, 262, L(lang, ["Level crossings: no overtaking,", "not even two-wheelers", "(since 1 October 2026)"],
                                     ["Paso a nivel: prohibido", "adelantar, tampoco a los de", "dos ruedas (desde el 1-10-2026)"]), 12, 700, INK, "middle", 16))
    for i, t_ in enumerate(L(lang, ["You overtake", "You are overtaken", "You are overtaken"], ["Adelantas tú", "Te adelantan", "Te adelantan"])):
        p.append(txt(122 + i * 238, 30, t_, 13, 800, INK, "middle"))
    return svg(720, 342, "".join(p), L(lang, "Overtaking rules that concern two-wheelers", "Normas de adelantamiento que afectan a los vehículos de dos ruedas"))
