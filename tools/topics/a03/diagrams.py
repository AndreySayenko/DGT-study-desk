# -*- coding: utf-8 -*-
"""Original SVG diagrams for Category A1/A2, Topic 3 (speed), EN/ES. No third-party artwork is used. Two figures
are specific to this topic; three are shared with Category B, Topic 3 (the speed scale is relabelled for a
motorcycle)."""

from svgkit import NAVY, TEAL, AMBER, RED, SLATE, INK, svg, txt, lines  # noqa: F401
from ..b03.diagrams import L, rect, line, max_sign, MOTORWAY, OTHER, GRID, MUTED
from ..b03.diagrams import speed_band, urban_limits, pedestrian_risk  # noqa: F401  (shared with Topic B3)
from ..b08.signs import at, moto

CARD = "#f8fafc"
LINE = "#cbd5e1"


# ---------------------------------------------------------------- D1 the speed scale, for a motorcycle
def moto_speed_band(lang):
    out = speed_band(lang)
    return (out.replace("A car on a motorway or dual carriageway", "A motorcycle on an autopista or autovía")
               .replace("Un turismo en autopista o autovía", "Una motocicleta en autopista o autovía"))


# ---------------------------------------------------------------- D2 generic limits out of town for the A family
def moto_limits(lang):
    gx0, gx1 = 300, 690
    k = (gx1 - gx0) / 130

    def X(v):
        return round(gx0 + v * k, 1)

    rows = {
        "en": [(["Motorcycle"], "+ three-wheelers treated as motorcycles", (60, 120), (45, 90)),
               (["Three-wheeled vehicle,", "heavy quadricycle"], "", (60, 70), (35, 70)),
               (["Moped, cycle,", "light quadricycle"], "", "bicycles only, on autovías: up to 45", "up to 45")],
        "es": [(["Motocicleta"], "+ tres ruedas asimilados a motocicletas", (60, 120), (45, 90)),
               (["Vehículo de tres ruedas,", "cuatriciclo pesado"], "", (60, 70), (35, 70)),
               (["Ciclomotor, ciclo,", "cuatriciclo ligero"], "", "solo bicicletas y solo en autovías: hasta 45", "hasta 45")],
    }[lang]
    p = []
    lg = [(MOTORWAY, L(lang, "Autopista and autovía", "Autopista y autovía")),
          (OTHER, L(lang, "Vía para automóviles and carretera convencional", "Vía para automóviles y carretera convencional"))]
    lx = 20
    for col, name in lg:
        p.append(rect(lx, 9, 14, 10, col, 2))
        p.append(txt(lx + 20, 18, name, 11.5, 600, INK))
        lx += 34 + len(name) * 6.4
    top, rh = 36, 70
    for v in (0, 30, 60, 90, 120):
        p.append(line(X(v), top, X(v), top + rh * 3 - 6, GRID, 1))
        p.append(txt(X(v), top + rh * 3 + 10, f"{v}" + (" km/h" if v == 120 else ""), 10.5, 400, MUTED, "middle"))
    for i, (name, sub, mw, cv) in enumerate(rows):
        y = top + i * rh
        p.append(lines(20, y + 22, name, 12.5, 700, INK, "start", 15))
        if sub:
            p.append(txt(20, y + 40, sub, 10.5, 400, SLATE))
        for j, (rng, col) in enumerate(((mw, MOTORWAY), (cv, OTHER))):
            by = y + 10 + j * 26
            if isinstance(rng, tuple):
                lo, hi = rng
                p.append(rect(X(lo), by, X(hi) - X(lo), 14, col, 4))
                p.append(txt(X(lo) - 6, by + 11, f"{lo}", 11, 700, INK, "end"))
                p.append(txt(X(hi) + 6, by + 11, f"{hi}", 11, 700, INK))
            else:
                p.append(rect(X(0), by, X(45) - X(0), 14, "none", 4, f' stroke="{col}" stroke-width="2" stroke-dasharray="5 3"'))
                p.append(txt(X(45) + 8, by + 11, rng, 11, 600, INK))
    p.append(lines(20, top + rh * 3 + 34, L(lang, ["Mopeds and light quadricycles: never on autopistas, autovías or vías para automóviles.", "Bicycles: on autovías only on the shoulder (riders over 14)."],
                                            ["Ciclomotores y cuatriciclos ligeros: nunca por autopistas, autovías ni vías para automóviles.", "Bicicletas: en autovías, solo por el arcén (mayores de 14 años)."]),
                   10.5, 600, SLATE, "start", 14))
    return svg(720, top + rh * 3 + 58, "".join(p), L(lang, "Generic speeds out of town for the motorcycle family", "Velocidades genéricas fuera de poblado de la familia de la moto"))


# ---------------------------------------------------------------- D3 towing a trailer: − 10 %
def _trailer(x, y):
    """A small single-axle trailer seen from the side, hitch on the right, at (x, y) = hitch point."""
    return (rect(x - 74, y - 30, 50, 26, "#64748b", 4) + rect(x - 74, y - 34, 50, 6, "#475569", 2)
            + line(x - 24, y - 10, x, y - 4, "#334155", 3)
            + f'<circle cx="{x - 49}" cy="{y + 2}" r="9" fill="none" stroke="#334155" stroke-width="3"/>')


def trailer_rule(lang):
    p = [rect(10, 8, 300, 248, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"')]
    p.append(txt(160, 32, L(lang, "Allowed only if…", "Solo se permite si…"), 13, 800, INK, "middle"))
    p.append(line(30, 128, 290, 128, "#94a3b8", 2))
    p.append(_trailer(150, 116))
    p.append(at(moto(INK), 196, 106, 2.1))
    conds = L(lang, ["trailer ≤ 50 % of the bike’s unladen mass", "by day, with good visibility", "nobody rides in the trailer", "in town: local bylaws"],
                    ["remolque ≤ 50 % de la masa en vacío", "de día y con buena visibilidad", "nadie viaja en el remolque", "en poblado: ordenanzas municipales"])
    for i, c in enumerate(conds):
        cy = 150 + i * 25
        p.append(rect(28, cy, 264, 20, "#e2e8f0", 10) + txt(160, cy + 14, c, 11, 700, INK, "middle"))
    # right: the numbers
    p.append(rect(326, 8, 384, 248, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'))
    p.append(txt(518, 32, L(lang, "Maximum speed − 10 %", "Velocidad máxima − 10 %"), 13, 800, INK, "middle"))
    rows = [
        (L(lang, ["Motorcycle", "autopista, autovía"], ["Motocicleta", "autopista, autovía"]), 120, L(lang, "108", "108")),
        (L(lang, ["Motorcycle", "carretera convencional"], ["Motocicleta", "carretera convencional"]), 90, L(lang, "81", "81")),
        (L(lang, ["Three-wheeled vehicle", "(70 km/h limit)"], ["Vehículo de tres ruedas", "(límite de 70 km/h)"]), 70, L(lang, "63", "63")),
        (L(lang, ["Moped"], ["Ciclomotor"]), 45, L(lang, "40.5", "40,5")),
    ]
    for i, (name, was, now) in enumerate(rows):
        cy = 70 + i * 48
        p.append(lines(344, cy - (4 if len(name) == 2 else -4), name, 11.5, 700, INK, "start", 14))
        p.append(max_sign(560, cy, 17, was))
        p.append(f'<path d="M584 {cy} L612 {cy}" stroke="{SLATE}" stroke-width="2.4"/><path d="M612 {cy - 5} L620 {cy} L612 {cy + 5} Z" fill="{SLATE}"/>')
        p.append(f'<text x="632" y="{cy + 6}" font-size="17" font-weight="800" fill="{RED}">{now}<tspan font-size="11" font-weight="600" fill="{SLATE}"> km/h</tspan></text>')
    p.append(lines(518, 252 - 12, L(lang, ["Per cent, not km/h. The minimum speed does not change."], ["Por ciento, no km/h. La velocidad mínima no cambia."]), 10.5, 600, SLATE, "middle", 13))
    return svg(720, 264, "".join(p), L(lang, "Towing a trailer with a motorcycle", "Remolque arrastrado por una motocicleta"))
