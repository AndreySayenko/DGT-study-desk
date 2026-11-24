# -*- coding: utf-8 -*-
"""Original SVG diagrams for Category A1/A2, Topic 1 (definitions and general concepts), EN/ES. No third-party
artwork is used. Three figures are shared with Category B, Topic 1 so both categories show the same picture; the two
below are specific to this topic."""

from svgkit import NAVY, TEAL, AMBER, RED, SLATE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect  # noqa: F401
from ..b09.diagrams import L, line, MUTED, LINE, CARD
from ..b08.signs import at, ped, moped, moto, rider, car_side, standing
from ..b01.diagrams import tree, ladder, masses  # noqa: F401  (shared with Topic B1)

DARK = "#1f2937"
WHEEL = "#334155"


def _chip(cx, y, text, fill, cw=8.6, size=12):
    w = 18 + cw * len(text)
    return rect(cx - w / 2, y, w, 24, fill, 12) + txt(cx, y + 16.5, text, size, 800, "#fff", "middle")


def _wheelchair(c=INK):
    """A person in a wheelchair, centred on (0, 0)."""
    return (f'<circle cx="-2" cy="9" r="10" fill="none" stroke="{c}" stroke-width="2.6"/>'
            f'<circle cx="14" cy="16" r="3" fill="{c}"/>'
            f'<path d="M-8 -2 L6 -2 L12 14" fill="none" stroke="{c}" stroke-width="2.6" stroke-linejoin="round"/>'
            f'<circle cx="-4" cy="-20" r="4.3" fill="{c}"/>'
            f'<path d="M-4 -15 L-5 -2 L8 -2 L10 10" fill="none" stroke="{c}" stroke-width="4" stroke-linejoin="round"/>'
            f'<path d="M-4 -12 L4 -6" stroke="{c}" stroke-width="3"/>')


# ---------------------------------------------------------------- D1 driver or pedestrian?
def who_is_driver(lang):
    P_, D_ = L(lang, "PEDESTRIAN", "PEATÓN"), L(lang, "DRIVER", "CONDUCTOR")
    panels = [
        (at(ped(INK), 0, -2, 1.9), P_, TEAL, L(lang, ["Walking"], ["Caminando"])),
        (at(moped(INK), 12, 8, 1.8) + at(standing(INK), -44, 2, 1.7), P_, TEAL, L(lang, ["Pushing a moped", "or a bicycle on foot"], ["Llevando a pie un", "ciclomotor o una bici"])),
        (at(_wheelchair(INK), 0, 0, 1.75), P_, TEAL, L(lang, ["In a wheelchair,", "at walking pace"], ["En silla de ruedas,", "al paso"])),
        (at(moto(INK), 0, 4, 2.1), D_, NAVY, L(lang, ["Riding a motorcycle", "or a moped"], ["Montado en una moto", "o un ciclomotor"])),
        (at(rider(INK), 0, 6, 2.0), D_, NAVY, L(lang, ["In charge of an animal", "(riding or leading it)"], ["A cargo de un animal", "(montado o guiándolo)"])),
        (at(car_side(INK), 0, 14, 2.0) + rect(-13, -40, 26, 26, "#1d4ed8", 3) + txt(0, -19.5, "L", 20, 900, "#fff", "middle"), D_, NAVY, L(lang, ["Learner on the road: the", "instructor (extra controls)"], ["Vehículo de autoescuela: el", "profesor (mandos adicionales)"])),
    ]
    p = []
    for i, (art, verdict, col, cap) in enumerate(panels):
        cx = 124 + (i % 3) * 236
        y0 = 6 + (i // 3) * 168
        p.append(rect(cx - 112, y0, 224, 160, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'))
        p.append(f'<g transform="translate({cx} {y0 + 52})">{art}</g>')
        p.append(_chip(cx, y0 + 98, verdict, col) + lines(cx, y0 + 138, cap, 11, 600, INK, "middle", 14))
    return svg(720, 340, "".join(p), L(lang, "Driver or pedestrian?", "¿Conductor o peatón?"))


# ---------------------------------------------------------------- D2 wheel layouts of motorcycles and their relatives
def _wheel_v(cx, cy, w=10, h=22):
    return rect(cx - w / 2, cy - h / 2, w, h, WHEEL, 4)


def wheel_layouts(lang):
    panels = [
        ("moto", L(lang, "Motorcycle", "Motocicleta"), L(lang, "2 wheels", "2 ruedas"), NAVY),
        ("sidecar", L(lang, "Motorcycle with sidecar", "Motocicleta con sidecar"), L(lang, "3 asymmetric wheels", "3 ruedas asimétricas"), NAVY),
        ("trike", L(lang, "Three-wheeled vehicle", "Vehículo de tres ruedas"), L(lang, "3 symmetric wheels", "3 ruedas simétricas"), AMBER),
        ("quad", L(lang, "Heavy quadricycle", "Cuatriciclo pesado"), L(lang, "4 wheels", "4 ruedas"), TEAL),
    ]
    p = []
    for i, (k, title, chip, col) in enumerate(panels):
        cx = 92 + i * 179
        p.append(rect(cx - 84, 8, 168, 286, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'))
        p.append(lines(cx, 32, _split(title), 12.5, 800, INK, "middle", 15))
        ay = 62
        ax = cx - 20 if k == "sidecar" else cx
        p.append(line(ax, ay, ax, 236, "#94a3b8", 1.5, "6 4"))  # longitudinal axis
        if k == "moto":
            p.append(_wheel_v(cx, 92) + _wheel_v(cx, 206) + rect(cx - 9, 100, 18, 98, "#64748b", 8) + rect(cx - 22, 104, 44, 5, DARK, 2))
        elif k == "sidecar":
            p.append(_wheel_v(cx - 20, 92) + _wheel_v(cx - 20, 206) + rect(cx - 29, 100, 18, 98, "#64748b", 8) + rect(cx - 42, 104, 44, 5, DARK, 2))
            p.append(rect(cx + 6, 126, 36, 62, "#94a3b8", 14) + _wheel_v(cx + 50, 160) + line(cx - 11, 150, cx + 6, 150, DARK, 3))
        elif k == "trike":
            p.append(_wheel_v(cx, 92) + rect(cx - 9, 100, 18, 70, "#64748b", 8) + rect(cx - 22, 104, 44, 5, DARK, 2))
            p.append(rect(cx - 34, 168, 68, 36, "#94a3b8", 10) + _wheel_v(cx - 42, 194) + _wheel_v(cx + 42, 194))
        else:
            p.append(rect(cx - 30, 96, 60, 110, "#94a3b8", 14) + rect(cx - 22, 104, 44, 5, DARK, 2)
                     + _wheel_v(cx - 38, 112) + _wheel_v(cx + 38, 112) + _wheel_v(cx - 38, 190) + _wheel_v(cx + 38, 190))
        p.append(_chip(cx, 252, chip, col, 6.6, 11.5))
    p.append(lines(360, 314, L(lang, ["The dashed line is the vehicle’s long axis. All four are automóviles: engine over 50 cm³ (combustion) and/or",
                                        "a design speed over 45 km/h. Heavy quadricycle (EU L7e): up to 450 kg in running order (600 kg goods), 15 kW."],
                                       ["La línea discontinua es el eje longitudinal. Los cuatro son automóviles: más de 50 cm³ (combustión) y/o más de",
                                        "45 km/h por construcción. Cuatriciclo pesado (UE L7e): hasta 450 kg en orden de marcha (600 kg mercancías), 15 kW."]), 10.5, 600, SLATE, "middle", 15))
    return svg(720, 340, "".join(p), L(lang, "Two, three or four wheels", "Dos, tres o cuatro ruedas"))


def _split(title):
    words = title.split()
    if len(title) <= 18:
        return [title]
    half = len(words) // 2 + (1 if len(words) % 2 else 0)
    return [" ".join(words[:half]), " ".join(words[half:])]
