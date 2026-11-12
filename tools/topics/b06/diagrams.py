# -*- coding: utf-8 -*-
"""Original SVG diagrams for Topic 6 (EN/ES). No third-party artwork is used. Each function takes the language
("en" or "es") and returns an SVG string. Figures sit on a light background in both themes. Vehicle plates are
drawn in simplified form from their official shapes and colours."""

from svgkit import NAVY, TEAL, RED, SLATE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect, tick, cross, ASPHALT, VERGE, WHITE  # noqa: F401

MUTED = "#64748b"
GRID = "#e2e8f0"
LOAD = "#92400e"
SIGN_RED = "#c81e1e"


def L(lang, en, es):
    return en if lang == "en" else es


def line(x1, y1, x2, y2, color=INK, width=2, dash=None, extra=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{d}{extra}/>'


def dim(x1, x2, y, label, color=INK):
    """Horizontal dimension arrow with a label above it."""
    return (line(x1 + 5, y, x2 - 5, y, color, 1.5) +
            f'<path d="M{x1} {y} L{x1 + 7} {y - 4} L{x1 + 7} {y + 4} Z" fill="{color}"/>' +
            f'<path d="M{x2} {y} L{x2 - 7} {y - 4} L{x2 - 7} {y + 4} Z" fill="{color}"/>' +
            txt((x1 + x2) / 2, y - 6, label, 11, 700, color, "middle"))


# ---------------------------------------------------------------- D1 child seats
def _cabin(cx, airbag=None):
    out = [rect(cx - 55, 22, 110, 196, "#e2e8f0", 28, f' stroke="{SLATE}" stroke-width="1.5"'),
           rect(cx - 44, 50, 88, 16, "#bfdbfe", 6),
           line(cx - 46, 76, cx + 46, 76, "#94a3b8", 2),
           f'<circle cx="{cx - 24}" cy="{88}" r="9" fill="none" stroke="{INK}" stroke-width="2.5"/>',
           rect(cx - 44, 100, 36, 40, "#94a3b8", 7), rect(cx + 8, 100, 36, 40, "#94a3b8", 7),
           rect(cx - 46, 160, 92, 40, "#94a3b8", 7),
           line(cx - 15, 162, cx - 15, 198, "#cbd5e1", 1.5), line(cx + 15, 162, cx + 15, 198, "#cbd5e1", 1.5)]
    if airbag:
        on = airbag == "on"
        out.append(rect(cx + 8, 66, 36, 14, "#dc2626" if on else "#16a34a", 3) +
                   txt(cx + 26, 77, "ON" if on else "OFF", 9.5, 800, "#fff", "middle"))
    return "".join(out)


def _child_seat(cx, cy, rear_facing=False):
    """Child seat seen from above. The curved back of the shell is behind the child; the child faces the open side."""
    d = -1 if rear_facing else 1
    shell = (f'<path d="M{cx - 15} {cy - 15 * d} L{cx - 15} {cy + 13 * d} Q {cx} {cy + 20 * d} {cx + 15} {cy + 13 * d} L{cx + 15} {cy - 15 * d}" '
             f'fill="none" stroke="{TEAL}" stroke-width="6" stroke-linejoin="round"/>')
    return shell + f'<circle cx="{cx}" cy="{cy + 4 * d}" r="6" fill="#fde68a" stroke="#b45309" stroke-width="1.2"/>'


def child_seats(lang):
    p = []
    panels = [
        (None, (0, 180, False), True, L(lang, ["Under 135 cm: approved child seat", "for their height and weight,", "in a rear seat"],
                                         ["Menos de 135 cm: sistema homologado", "para su talla y peso,", "en un asiento trasero"])),
        ("on", (26, 120, True), False, L(lang, ["Rear-facing seat in front", "with the frontal airbag ON:", "never"],
                                          ["Silla a contramarcha delante", "con el airbag frontal ACTIVADO:", "nunca"])),
        ("off", (26, 120, True), True, L(lang, ["Rear-facing seat in front: only", "with the airbag OFF, and only when", "the rear seats cannot be used"],
                                          ["Silla a contramarcha delante: solo", "con el airbag DESACTIVADO y si no", "se pueden usar los traseros"])),
    ]
    for i, (airbag, (dx, cy, rf), ok, cap) in enumerate(panels):
        cx = 120 + i * 240
        p.append(_cabin(cx, airbag))
        p.append(_child_seat(cx + dx, cy, rf))
        p.append(tick(cx + 74, 40, 13) if ok else cross(cx + 74, 40, 13))
        p.append(lines(cx, 240, cap, 11.5, 400, INK, "middle", 15))
        if i:
            p.append(line(i * 240, 20, i * 240, 280, GRID, 1.2))
    return svg(720, 290, "".join(p), L(lang, "Child seats", "Sistemas de retención infantil"))


# ---------------------------------------------------------------- D2 motorcycle passenger
def moto_passenger(lang):
    p = [rect(60, 206, 330, 6, "#cbd5e1", 2)]
    # motorcycle seen from the side, travelling right
    for wx in (120, 320):
        p.append(f'<circle cx="{wx}" cy="176" r="30" fill="#1f2937"/><circle cx="{wx}" cy="176" r="12" fill="#9ca3af"/>')
    p.append(line(120, 176, 160, 132, "#334155", 7, extra=' stroke-linecap="round"'))
    p.append(rect(190, 136, 66, 34, "#334155", 6))
    p.append(line(160, 132, 296, 116, "#334155", 7, extra=' stroke-linecap="round"'))
    p.append('<path d="M140 124 L244 124 L256 110 L294 106 L300 118 L276 130 L140 132 Z" fill="#111827"/>')
    p.append(line(298, 110, 320, 176, "#475569", 6) + line(292, 102, 318, 94, INK, 4))
    p.append(rect(262, 162, 22, 6, "#64748b", 2) + rect(196, 162, 22, 6, "#64748b", 2))
    # rider
    p.append(line(262, 120, 276, 76, "#1d4ed8", 16, extra=' stroke-linecap="round"'))
    p.append(line(276, 84, 312, 98, "#1d4ed8", 7, extra=' stroke-linecap="round"'))
    p.append(line(262, 122, 288, 140, "#1e3a8a", 9, extra=' stroke-linecap="round"') + line(288, 140, 274, 164, "#1e3a8a", 8, extra=' stroke-linecap="round"'))
    p.append(f'<circle cx="280" cy="58" r="14" fill="#e2e8f0" stroke="{INK}" stroke-width="2"/>' + rect(282, 52, 12, 8, "#475569", 3))
    # passenger behind, astride, feet on the footrests
    p.append(line(206, 120, 220, 80, "#0f766e", 15, extra=' stroke-linecap="round"'))
    p.append(line(220, 88, 258, 104, "#0f766e", 6, extra=' stroke-linecap="round"'))
    p.append(line(206, 122, 228, 142, "#115e59", 9, extra=' stroke-linecap="round"') + line(228, 142, 208, 164, "#115e59", 8, extra=' stroke-linecap="round"'))
    p.append(f'<circle cx="224" cy="62" r="13" fill="#e2e8f0" stroke="{INK}" stroke-width="2"/>' + rect(226, 57, 11, 7, "#475569", 3))
    items = L(lang,
              ["Shown on the registration certificate", "One passenger, over 12 (over 7 if the rider is",
               "  their parent, guardian or an authorised adult)", "Behind the rider, never in front of them",
               "Astride, feet on the side footrests", "Both wear an approved helmet, fastened"],
              ["Que conste en el permiso de circulación", "Un pasajero mayor de 12 años (de 7 si conduce",
               "  su padre, madre, tutor o adulto autorizado)", "Detrás del conductor, nunca delante",
               "A horcajadas, pies en los reposapiés laterales", "Ambos con casco homologado y abrochado"])
    y = 44
    for k, s in enumerate(items):
        if not s.startswith("  "):
            p.append(tick(426, y - 4, 8))
        p.append(txt(442, y, s.strip(), 11.5, 400, INK))
        y += 22 if k != 1 else 16
    return svg(720, 220, "".join(p), L(lang, "Carrying a passenger on a motorcycle or moped", "Pasajero en motocicleta o ciclomotor"))


# ---------------------------------------------------------------- D3 maximum lengths
def max_lengths(lang):
    rows = L(lang,
             [("Most vehicles and trailers", 12), ("Bus, 2 axles", 13.5), ("Semitrailer", 14.04), ("Bus, 3 or more axles", 15),
              ("Articulated vehicle", 16.5), ("Road train", 18.75)],
             [("Casi todos los vehículos y remolques", 12), ("Autobús de 2 ejes", 13.5), ("Semirremolque", 14.04), ("Autobús de 3 o más ejes", 15),
              ("Vehículo articulado", 16.5), ("Tren de carretera", 18.75)])
    gx0, gx1 = 240, 660
    k = (gx1 - gx0) / 20

    def X(v):
        return round(gx0 + v * k, 1)

    p = []
    top = 30
    for v in (0, 5, 10, 15, 20):
        p.append(line(X(v), top - 8, X(v), top + 6 * 30 - 6, GRID, 1))
        p.append(txt(X(v), top + 6 * 30 + 8, f"{v} m", 10.5, 400, MUTED, "middle"))
    for i, (name, v) in enumerate(rows):
        y = top + i * 30
        p.append(txt(gx0 - 10, y + 13, name, 12, 600, INK, "end"))
        p.append(rect(X(0), y, X(v) - X(0), 18, NAVY, 4))
        p.append(txt(X(v) + 6, y + 14, (f"{v:g}" if lang == "en" else f"{v:g}".replace(".", ",")) + " m", 11.5, 700, INK))
    p.append(line(X(12), top - 14, X(12), top + 6 * 30 - 4, SIGN_RED, 1.8, "5 4"))
    p.append(rect(X(12) - 30, 2, 60, 16, "#fff") + txt(X(12), 14, L(lang, "&gt; 12 m: V-6", "&gt; 12 m: V-6"), 11, 700, SIGN_RED, "middle"))
    return svg(720, top + 6 * 30 + 16, "".join(p), L(lang, "Maximum length including the load", "Longitud máxima con la carga"))


# ---------------------------------------------------------------- D4 how far the load may stick out
def _truck(x, y, length, cab=True):
    out = [rect(x, y, length, 30, "#cbd5e1", 3, ' stroke="#64748b" stroke-width="1"')]
    if cab:
        out.append(rect(x + length - 34, y - 14, 34, 44, "#1d4ed8", 4) + rect(x + length - 20, y - 8, 14, 14, "#bfdbfe", 2))
    out.append(f'<circle cx="{x + 22}" cy="{y + 34}" r="9" fill="#1f2937"/><circle cx="{x + length - 18}" cy="{y + 34}" r="9" fill="#1f2937"/>')
    return "".join(out)


def _car_side(x, y, length):
    return (f'<path d="M{x} {y + 22} L{x + 6} {y + 6} L{x + length * 0.28} {y + 4} L{x + length * 0.42} {y - 12} L{x + length * 0.78} {y - 12} '
            f'L{x + length * 0.9} {y + 4} L{x + length} {y + 8} L{x + length} {y + 26} L{x} {y + 26} Z" fill="#1d4ed8"/>'
            f'<circle cx="{x + 18}" cy="{y + 28}" r="8" fill="#1f2937"/><circle cx="{x + length - 18}" cy="{y + 28}" r="8" fill="#1f2937"/>')


def overhang(lang):
    p = []
    # row 1: car (not a goods vehicle): rear only
    y = 40
    p.append(txt(20, 22, L(lang, "Cars, mixed vehicles, motorhomes (not goods vehicles)", "Turismos, mixtos, autocaravanas (no destinados solo a mercancías)"), 12.5, 700, INK))
    p.append(_car_side(150, y, 150))
    p.append(rect(80, y - 4, 210, 5, LOAD, 2))
    p.append(dim(80, 150, y + 52, L(lang, "rear only", "solo detrás")))
    p.append(lines(330, y + 4, L(lang, ["Divisible load: up to 10 % of the vehicle’s length", "Indivisible load: up to 15 %", "Never in front or at the sides"],
                                   ["Carga divisible: hasta el 10 % de la longitud", "Carga indivisible: hasta el 15 %", "Nunca por delante ni por los lados"]), 11.5, 400, INK, "start", 16))
    # row 2: goods vehicle up to 5 m
    y = 140
    p.append(txt(20, 122, L(lang, "Goods vehicles, indivisible load (beams, posts, pipes)", "Vehículos de mercancías, carga indivisible (vigas, postes, tubos)"), 12.5, 700, INK))
    p.append(_truck(130, y, 120))
    p.append(rect(90, y - 6, 200, 6, LOAD, 2))
    p.append(dim(90, 130, y + 58, "⅓") + dim(250, 290, y + 58, "⅓"))
    p.append(lines(330, y + 8, L(lang, ["Vehicle up to 5 m long:", "⅓ of its length at the rear and ⅓ in front"],
                                   ["Vehículo de hasta 5 m:", "⅓ de su longitud detrás y otro ⅓ delante"]), 11.5, 400, INK, "start", 16))
    # row 3: goods vehicle over 5 m
    y = 220
    p.append(_truck(130, y, 150))
    p.append(rect(70, y - 6, 250, 6, LOAD, 2))
    p.append(dim(70, 130, y + 58, L(lang, "3 m rear", "3 m detrás")) + dim(280, 320, y + 58, L(lang, "2 m", "2 m")))
    p.append(lines(330, y + 8, L(lang, ["Vehicle over 5 m long:", "3 m at the rear, 2 m in front"],
                                   ["Vehículo de más de 5 m:", "3 m detrás, 2 m delante"]), 11.5, 400, INK, "start", 16))
    p.append(lines(20, 316, L(lang, ["Sideways (indivisible load wider than the vehicle): up to 0.40 m each side, total width ≤ 2.55 m.",
                                      "Vehicles under 1 m wide (motorcycles, mopeds): 0.25 m at the rear, 0.50 m each side of the axis, nothing in front."],
                               ["A lo ancho (carga indivisible más ancha que el vehículo): hasta 0,40 m por cada lado, anchura total ≤ 2,55 m.",
                                "Vehículos de menos de 1 m de ancho (motos, ciclomotores): 0,25 m detrás, 0,50 m a cada lado del eje, nada delante."]), 11.5, 700, TEAL, "start", 17))
    return svg(720, 346, "".join(p), L(lang, "How far the load may stick out", "Cuánto puede sobresalir la carga"))


# ---------------------------------------------------------------- D5 signalling a load that sticks out
def v20(x, y, s=26, lang="en"):
    """V-20 panel: square with red and white diagonal stripes."""
    cid = f"t6v20-{lang}-{int(x)}-{int(y)}"
    stripes = "".join(f'<path d="M{x + i * s / 2.5 - s} {y + s} L{x + i * s / 2.5} {y}" stroke="{SIGN_RED}" stroke-width="{s / 5.5:.1f}"/>' for i in range(0, 7))
    return (f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{s}" height="{s}"/></clipPath>' + rect(x, y, s, s, "#fff") +
            f'<g clip-path="url(#{cid})">{stripes}</g>' + f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="none" stroke="{SIGN_RED}" stroke-width="1.5"/>')


def overhang_signals(lang):
    p = []
    for i, night in enumerate((False, True)):
        ox = 10 + i * 360
        p.append(rect(ox, 30, 340, 150, "#1e293b" if night else "#e0f2fe", 8))
        p.append(rect(ox, 150, 340, 30, "#334155" if night else "#9ca3af"))
        tx = ox + 70
        p.append(_truck(tx, 110, 170))
        p.append(f'<path d="M{ox + 30} 106 L{ox + 290} 84" stroke="{LOAD}" stroke-width="6" stroke-linecap="round"/>')
        p.append(v20(ox + 18, 108, 24, lang))
        if night:
            p.append(f'<circle cx="{ox + 292}" cy="84" r="8" fill="#fff" opacity=".35"/><circle cx="{ox + 292}" cy="84" r="4.5" fill="#fff"/>')
            p.append(f'<circle cx="{ox + 30}" cy="106" r="8" fill="#ef4444" opacity=".35"/><circle cx="{ox + 30}" cy="106" r="4.5" fill="#ef4444"/>')
        p.append(txt(ox + 170, 22, L(lang, "Night or poor visibility" if night else "By day, clear weather", "De noche o con poca visibilidad" if night else "De día y con buena visibilidad"),
                     13, 700, INK, "middle"))
        cap = (L(lang, ["Rear: V-20 panel(s) + a red light", "Front: a white light"], ["Detrás: panel(es) V-20 + luz roja", "Delante: luz blanca"]) if night else
               L(lang, ["Rear: one or two V-20 panels", "Front: nothing needed"], ["Detrás: uno o dos paneles V-20", "Delante: no es necesario"]))
        p.append(lines(ox + 170, 202, cap, 11.5, 400, INK, "middle", 16))
    p.append(txt(360, 248, L(lang, "Two panels when the load spans the whole rear width: one at each end, stripes forming an inverted V.",
                                "Dos paneles si la carga ocupa todo el ancho trasero: uno en cada extremo, con las franjas en V invertida."), 11.5, 700, TEAL, "middle"))
    return svg(720, 258, "".join(p), L(lang, "Signalling a load that sticks out", "Señalizar la carga que sobresale"))


# ---------------------------------------------------------------- D6 some vehicle plates
def _plate(kind, cx, cy, lang="en"):
    if kind == "V-4":
        return (f'<circle cx="{cx}" cy="{cy}" r="26" fill="#fff" stroke="{INK}" stroke-width="2.5"/>' + txt(cx, cy + 9, "40", 24, 800, INK, "middle"))
    if kind == "V-5":
        return f'<path d="M{cx} {cy - 28} L{cx + 30} {cy + 24} L{cx - 30} {cy + 24} Z" fill="#f97316" stroke="{SIGN_RED}" stroke-width="5" stroke-linejoin="round"/>'
    if kind == "V-6":
        return rect(cx - 40, cy - 15, 80, 30, "#facc15", 2, f' stroke="{SIGN_RED}" stroke-width="5"')
    if kind == "V-10":
        return (rect(cx - 26, cy - 26, 52, 52, "#facc15", 3, f' stroke="{INK}" stroke-width="3"') +
                f'<circle cx="{cx - 9}" cy="{cy - 12}" r="5" fill="{INK}"/><circle cx="{cx + 10}" cy="{cy - 9}" r="4" fill="{INK}"/>' +
                rect(cx - 15, cy - 6, 12, 22, INK, 3) + rect(cx + 5, cy - 4, 10, 18, INK, 3))
    if kind == "V-11":
        return rect(cx - 36, cy - 20, 72, 40, "#f97316", 2, f' stroke="{INK}" stroke-width="2.5"') + line(cx - 36, cy, cx + 36, cy, INK, 2)
    if kind == "V-13":
        return rect(cx - 22, cy - 28, 44, 56, "#16a34a", 3) + txt(cx, cy + 15, "L", 38, 800, "#fff", "middle")
    if kind == "V-14":
        return (rect(cx - 24, cy - 28, 48, 56, "#1e3a8a", 3, ' stroke="#fff" stroke-width="1"') + txt(cx, cy + 8, "L", 32, 800, "#fff", "middle") +
                rect(cx - 24, cy + 14, 48, 14, "#fff") + txt(cx, cy + 25, "PRÁCTICAS", 8, 800, SIGN_RED, "middle"))
    if kind == "V-15":
        return (rect(cx - 26, cy - 26, 52, 52, "#1d4ed8", 4) + f'<circle cx="{cx - 2}" cy="{cy - 14}" r="4.5" fill="#fff"/>' +
                f'<path d="M{cx - 2} {cy - 8} L{cx - 2} {cy + 4} L{cx + 10} {cy + 4} L{cx + 14} {cy + 14}" stroke="#fff" stroke-width="3.5" fill="none" stroke-linecap="round"/>' +
                f'<path d="M{cx - 9} {cy - 1} A 11 11 0 1 0 {cx + 7} {cy + 12}" stroke="#fff" stroke-width="3" fill="none"/>')
    if kind == "V-20":
        return v20(cx - 26, cy - 26, 52, lang)
    if kind == "V-25":
        cols = [("#1d4ed8", "0"), ("#0d9488", "ECO"), ("#16a34a", "C"), ("#facc15", "B")]
        out = []
        for j, (c, s) in enumerate(cols):
            x = cx - 15 + (j % 2) * 30
            y = cy - 14 + (j // 2) * 28
            out.append(f'<circle cx="{x}" cy="{y}" r="13" fill="{c}"/>' + txt(x, y + 4, s, 8.5 if s == "ECO" else 11, 800, INK if c == "#facc15" else "#fff", "middle"))
        return "".join(out)
    return ""


def vehicle_plates(lang):
    items = L(lang,
              [("V-4", "Speed limit"), ("V-5", "Slow vehicle (≤ 40)"), ("V-6", "Long vehicle (&gt; 12 m)"), ("V-10", "School transport"), ("V-11", "Dangerous goods"),
               ("V-13", "Novice driver"), ("V-14", "Learner driver"), ("V-15", "Disabled driver"), ("V-20", "Load sticks out"), ("V-25", "Environmental label")],
              [("V-4", "Limitación de velocidad"), ("V-5", "Vehículo lento (≤ 40)"), ("V-6", "Vehículo largo (&gt; 12 m)"), ("V-10", "Transporte escolar"), ("V-11", "Mercancías peligrosas"),
               ("V-13", "Conductor novel"), ("V-14", "Aprendizaje"), ("V-15", "Minusválido"), ("V-20", "Carga que sobresale"), ("V-25", "Distintivo ambiental")])
    p = []
    for i, (code, name) in enumerate(items):
        cx = 72 + (i % 5) * 144
        cy = 52 + (i // 5) * 130
        p.append(_plate(code, cx, cy, lang))
        p.append(txt(cx, cy + 50, code, 12, 800, INK, "middle"))
        p.append(txt(cx, cy + 66, name, 11, 400, SLATE, "middle"))
    return svg(720, 270, "".join(p), L(lang, "Some vehicle plates and badges", "Algunas señales en los vehículos"))
