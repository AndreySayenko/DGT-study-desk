# -*- coding: utf-8 -*-
"""Original SVG diagrams for Topic 12 (driving techniques), EN/ES. No third-party artwork is used. Each function takes
the language ("en" or "es") and returns an SVG string. The environmental labels are simplified drawings of the DGT's
official designs, made for this site."""
import math

from svgkit import NAVY, TEAL, AMBER, RED, SLATE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect, car_v, car_h, tick, cross, ASPHALT, VERGE, WHITE  # noqa: F401
from ..b09.diagrams import L, line, MUTED, LINE, CARD
from ..b10.diagrams import arrow, rot, badge

DARK = "#1f2937"
SKY = "#bfdbfe"


def card(x, y, w, h, color=NAVY):
    return rect(x, y, w, h, "#fff", 10, f' stroke="{LINE}" stroke-width="1.5"') + rect(x, y, 6, h, color, 3)


def road_v(x0, x1, top, bot, lanes):
    """Vertical road from x0 to x1 with `lanes` lanes and dashed lane lines."""
    out = [rect(x0, top, x1 - x0, bot - top, ASPHALT), rect(x0 + 4, top, 3, bot - top, WHITE), rect(x1 - 7, top, 3, bot - top, WHITE)]
    w = (x1 - x0) / lanes
    for i in range(1, lanes):
        x = x0 + i * w
        out.append("".join(rect(x - 1.5, y, 3, 18, WHITE) for y in range(int(top) + 6, int(bot), 34)))
    return "".join(out)


def moto_v(cx, cy, color=TEAL):
    return rect(cx - 4, cy - 16, 8, 32, DARK, 4) + rect(cx - 7, cy - 6, 14, 14, color, 5) + f'<circle cx="{cx}" cy="{cy - 2}" r="5" fill="#94a3b8"/>'


# ---------------------------------------------------------------- D1 blind spots
def blind_spots(lang):
    x0, x1, top, bot = 150, 420, 10, 330
    lw = (x1 - x0) / 3
    cx, cy = x0 + 1.5 * lw, 120
    p = [rect(0, 0, 720, 340, "#e8f0e3"), road_v(x0, x1, top, bot, 3)]
    # what the mirrors see (behind, fanning out) and the blind spots beside-behind
    p.append(f'<path d="M{cx - 14} {cy + 4} L{cx - 92} {bot} L{cx - 24} {bot} Z" fill="#93c5fd" opacity="0.55"/>')
    p.append(f'<path d="M{cx + 14} {cy + 4} L{cx + 92} {bot} L{cx + 24} {bot} Z" fill="#93c5fd" opacity="0.55"/>')
    p.append(f'<path d="M{cx - 4} {cy + 20} L{cx - 18} {bot} L{cx + 18} {bot} L{cx + 4} {cy + 20} Z" fill="#c4b5fd" opacity="0.55"/>')
    for s in (-1, 1):
        p.append(f'<path d="M{cx + s * 16} {cy - 8} L{cx + s * 16} {cy + 4} L{cx + s * 86} {cy + 150} L{cx + s * 96} {cy + 40} L{cx + s * 96} {cy - 8} Z" fill="{RED}" opacity="0.28"/>')
    p.append(car_v(cx, cy, NAVY))
    p.append(moto_v(cx - lw + 6, cy + 54, TEAL) + car_v(cx + lw, cy + 70, "#b45309"))
    p.append(car_v(cx - lw + 22, cy + 186, "#64748b") + car_v(cx + lw - 22, cy + 192, "#64748b"))
    # labels
    p.append(line(x0 - 4, cy + 40, x0 + 30, cy + 40, RED, 1.2) + lines(x0 - 10, cy + 30, L(lang, ["Blind", "spot"], ["Ángulo", "muerto"]), 12.5, 800, RED, "end", 15))
    p.append(line(x1 - 30, cy + 40, x1 + 4, cy + 40, RED, 1.2) + lines(x1 + 10, cy + 30, L(lang, ["Blind", "spot"], ["Ángulo", "muerto"]), 12.5, 800, RED, "start", 15))
    p.append(lines(x0 - 10, cy + 196, L(lang, ["Seen in the", "door mirror"], ["Se ve por el", "retrovisor exterior"]), 11, 700, "#1d4ed8", "end", 14))
    p.append(lines(x1 + 10, cy + 196, L(lang, ["Seen in the", "door mirror"], ["Se ve por el", "retrovisor exterior"]), 11, 700, "#1d4ed8", "start", 14))
    p.append(rect(cx - 56, bot - 22, 112, 18, "#ede9fe", 4) + txt(cx, bot - 9, L(lang, "interior mirror", "retrovisor interior"), 10, 700, "#5b21b6", "middle"))
    # head turn inset
    hx, hy = 624, 120
    p.append(card(530, 26, 182, 196, AMBER))
    p.append(f'<circle cx="{hx}" cy="{hy}" r="22" fill="#d9b38c"/>' + rect(hx - 32, hy + 18, 64, 26, "#475569", 10))
    p.append(f'<path d="M{hx} {hy} L{hx} {hy - 74} A74 74 0 0 0 {hx - 52.3:.1f} {hy - 52.3:.1f} Z" fill="{AMBER}" opacity="0.25"/>')
    p.append(line(hx, hy, hx, hy - 74, SLATE, 1.5, "4 3") + arrow(hx, hy, hx - 50, hy - 50, AMBER, 2.5, 9))
    p.append(txt(hx - 16, hy - 52, "45°", 13, 800, AMBER, "middle"))
    p.append(lines(546, 182, L(lang, ["Turn your head about", "45° and look directly", "before any sideways move."], ["Gira la cabeza unos 45°", "y mira directamente antes", "de moverte de lado."]), 11, 600, INK, "start", 14))
    return svg(720, 340, "".join(p), L(lang, "Mirror fields and blind spots", "Campo de los retrovisores y ángulos muertos"))


# ---------------------------------------------------------------- D2 the time gap
def time_gap(lang):
    p = []
    rows = [(L(lang, "In town", "En vía urbana"), 2, TEAL), (L(lang, "On the open road", "En carretera"), 3, NAVY),
            (L(lang, "Rain, fog, tiredness, a bad surface, a tailgater…", "Lluvia, niebla, cansancio, mal firme, alguien muy pegado…"), 4, AMBER)]
    unit = 120
    for i, (lab, s, col) in enumerate(rows):
        y = 26 + i * 86
        p.append(txt(20, y + 2, lab, 12.5, 800, INK))
        p.append(rect(20, y + 12, 680, 50, ASPHALT, 6) + "".join(rect(x, y + 35, 18, 3, WHITE) for x in range(30, 700, 36)))
        lead = 70 + s * unit
        p.append(car_h(lead + 26, y + 37, "#64748b") + car_h(64, y + 37, col))
        p.append(line(lead, y + 8, lead, y + 66, "#fde047", 3))
        p.append(arrow(90, y + 52, lead - 4, y + 52, "#fff", 2, 8))
        p.append(txt((90 + lead) / 2, y + 30, L(lang, f"{s} seconds" if s < 4 else "3 + 1 = 4 seconds", f"{s} segundos" if s < 4 else "3 + 1 = 4 segundos"), 13, 800, "#fff", "middle"))
    p.append(lines(20, 286, L(lang, ["How to count it: when the car in front passes a fixed point (a post, a sign), say “one thousand and one,", "one thousand and two…”. If you reach the point before you finish, you are too close."],
                                ["Cómo contarlo: cuando el vehículo de delante pasa por un punto fijo (un poste, una señal), cuenta «mil uno,", "mil dos…». Si llegas al punto antes de terminar, vas demasiado cerca."]), 11, 600, SLATE, "start", 15))
    return svg(720, 320, "".join(p), L(lang, "The safe time gap in front", "La distancia de seguridad en tiempo"))


# ---------------------------------------------------------------- D3 stopping in a queue
def queue_gap(lang):
    p = []
    for k, (title, gap, note, extra) in enumerate([
        (L(lang, "Stopped in traffic", "Detenido en una cola"), "2–3 m", L(lang, ["Leave 2–3 m: you should see the rear", "tyres of the car in front on the road."], ["Deja 2–3 m: debes ver las ruedas", "traseras del de delante sobre el suelo."]), False),
        (L(lang, "Last in the queue", "Último de la cola"), "5–6 m", L(lang, ["Hazard lights if the queue is unexpected;", "5–6 m gap; watch the mirrors, first gear", "ready to move aside, until others stop behind."], ["Luces de emergencia si es imprevista;", "5–6 m; vigila los espejos y ten la 1.ª", "lista para apartarte, hasta que paren detrás."]), True)]):
        ox = 8 + k * 358
        p.append(rect(ox, 8, 346, 270, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"') + txt(ox + 16, 32, title, 13.5, 800, INK))
        p.append(rect(ox + 16, 48, 314, 128, ASPHALT, 6) + "".join(rect(ox + 16, y, 314, 2, WHITE) for y in (50, 172)))
        a, b = ox + 56, (ox + 206 if not extra else ox + 236)
        # side view of two cars (front car ahead on the right)
        p.append(f'<g transform="translate({b + 44} 120) scale(1.6)">' + _car_side("#64748b") + '</g>')
        p.append(f'<g transform="translate({a + 40} 120) scale(1.6)">' + _car_side(TEAL if not extra else AMBER) + '</g>')
        gx0, gx1 = a + 76, b + 8
        p.append(line(gx0, 150, gx1, 150, "#fde047", 2) + line(gx0, 144, gx0, 156, "#fde047", 2) + line(gx1, 144, gx1, 156, "#fde047", 2))
        p.append(txt((gx0 + gx1) / 2, 166, gap, 13, 800, "#fde047", "middle"))
        if not extra:
            p.append(f'<circle cx="{b + 20}" cy="128" r="13" fill="none" stroke="#fde047" stroke-width="2"/>')
        else:
            for hx in (a + 6, a + 74):
                p.append(f'<circle cx="{hx}" cy="110" r="5" fill="#f59e0b"/>')
        p.append(lines(ox + 16, 202, note, 11, 600, INK, "start", 15))
    return svg(720, 286, "".join(p), L(lang, "Leaving space when you stop", "El espacio al detenerse"))


def _car_side(c):
    return (f'<path d="M-24 6 L-24 0 Q-24 -2 -21 -3 L-12 -4 L-6 -11 Q-5 -12 -3 -12 L10 -12 Q12 -12 13 -10 L18 -4 L23 -3 Q26 -2 26 1 L26 6 Z" fill="{c}"/>'
            f'<path d="M-4 -10 L10 -10 L13 -5 L-8 -5 Z" fill="#cbd5e1"/>'
            f'<circle cx="-14" cy="6" r="5.5" fill="{DARK}"/><circle cx="16" cy="6" r="5.5" fill="{DARK}"/><circle cx="-14" cy="6" r="2" fill="#cbd5e1"/><circle cx="16" cy="6" r="2" fill="#cbd5e1"/>')


# ---------------------------------------------------------------- D4 zones of uncertainty
def uncertainty(lang):
    p = [rect(0, 0, 720, 300, "#e8f0e3"), rect(0, 40, 720, 190, ASPHALT), rect(0, 44, 720, 3, WHITE), rect(0, 223, 720, 3, WHITE)]
    p.append("".join(rect(x, 133, 24, 3, WHITE) for x in range(0, 720, 44)))
    p.append(rect(0, 226, 720, 30, "#d1d5db"))
    Z = "#f59e0b"
    # cyclist: wide side-to-side zone
    p.append(f'<ellipse cx="120" cy="190" rx="70" ry="30" fill="{Z}" opacity="0.35"/>' + rect(96, 186, 48, 8, DARK, 4) + f'<circle cx="110" cy="182" r="6" fill="#d9b38c"/>')
    p.append(arrow(120, 168, 120, 156, Z, 2, 7) + arrow(120, 212, 120, 222, Z, 2, 7))
    # parked / moving car: door opening and lane change
    p.append(f'<path d="M260 160 L360 160 L380 120 L240 120 Z" fill="{Z}" opacity="0.30"/>' + car_h(310, 190, "#64748b"))
    p.append(rect(298, 168, 22, 5, "#94a3b8", 2) + arrow(310, 168, 290, 140, Z, 2, 7))
    # adult pedestrian: small zone
    p.append(f'<circle cx="480" cy="240" r="16" fill="{Z}" opacity="0.35"/><circle cx="480" cy="236" r="5" fill="#d9b38c"/>' + rect(476, 241, 8, 10, "#475569", 2))
    # child: unpredictable, partly hidden by a parked car
    p.append(f'<ellipse cx="620" cy="214" rx="48" ry="40" fill="{Z}" opacity="0.35"/>' + car_h(640, 210, "#94a3b8", right=False)
             + f'<circle cx="604" cy="236" r="4" fill="#d9b38c"/>' + rect(601, 240, 6, 7, "#ef4444", 2))
    labels = [(120, L(lang, ["Cyclist: sways sideways,", "more uphill"], ["Ciclista: oscila a los lados,", "más en subida"])),
              (310, L(lang, ["Vehicle: lane change,", "sudden turn, a door opening"], ["Vehículo: cambio de carril,", "giro imprevisto, abrir puerta"])),
              (480, L(lang, ["Adult pedestrian:", "smaller zone"], ["Peatón adulto:", "zona menor"])),
              (624, L(lang, ["Child: unpredictable,", "often hidden"], ["Niño: imprevisible,", "a veces poco visible"]))]
    for x, lab in labels:
        p.append(lines(x, 274, lab, 10.5, 700, INK, "middle", 13))
    p.append(txt(360, 26, L(lang, "Shaded: where each road user may move without warning — keep out of it", "Sombreado: donde cada usuario puede moverse de forma imprevista; evita esa zona"), 11.5, 700, AMBER, "middle"))
    return svg(720, 306, "".join(p), L(lang, "Zones of uncertainty", "Zonas de incertidumbre"))


# ---------------------------------------------------------------- D5 adjusting the mirrors and mirror types
def mirrors(lang):
    p = []
    # interior mirror view: rear window with 3 of its 4 edges visible
    p.append(card(10, 10, 230, 220, NAVY) + txt(28, 34, L(lang, "Interior mirror", "Retrovisor interior"), 13, 800, INK))
    p.append(rect(34, 48, 190, 86, DARK, 30) + rect(44, 56, 170, 70, "#64748b", 18))
    p.append(f'<path d="M66 66 L192 66 L204 134 L54 134 Z" fill="{SKY}"/>' + rect(56, 104, 146, 22, "#9ca3af") + rect(150, 94, 28, 14, "#475569", 3))
    p.append(f'<path d="M54 126 L66 66 L192 66 L204 126" fill="none" stroke="{TEAL}" stroke-width="3"/>' + rect(34, 126, 190, 10, DARK, 0) + tick(206, 58, 8))
    p.append(txt(129, 148, L(lang, "top + both sides visible", "arriba + los dos lados"), 10, 700, TEAL, "middle"))
    p.append(lines(28, 172, L(lang, ["You see at least three of", "the four sides of the rear", "window, with a small eye", "movement."], ["Se ven al menos tres de", "los cuatro lados de la", "luneta trasera, con un", "leve movimiento de ojos."]), 11, 600, INK, "start", 14))
    # exterior mirror: little of own car, 50 % road / 50 % sky
    p.append(card(250, 10, 230, 220, TEAL) + txt(268, 34, L(lang, "Door mirrors", "Retrovisores exteriores"), 13, 800, INK))
    p.append(rect(278, 48, 172, 92, DARK, 16))
    p.append(rect(286, 56, 156, 38, SKY, 8) + rect(286, 94, 156, 38, "#9ca3af", 8) + rect(286, 56, 18, 76, "#64748b", 6))
    p.append(line(286, 94, 442, 94, "#475569", 1.5, "4 3") + tick(424, 74, 9))
    p.append(lines(268, 160, L(lang, ["As little of your own car as", "possible, as much road as", "possible: horizon in the", "middle (50 % road, 50 % sky)."], ["Lo mínimo del lateral del", "vehículo y lo máximo de la", "calzada: horizonte en medio", "(50 % asfalto, 50 % cielo)."]), 11, 600, INK, "start", 14))
    # mirror types
    p.append(card(490, 10, 220, 220, AMBER) + txt(508, 34, L(lang, "Types of mirror", "Tipos de espejos"), 13, 800, INK))
    types = [(L(lang, "Flat", "Plano"), L(lang, "real size (usually the interior one)", "imagen real (normalmente el interior)"), 1.0),
             (L(lang, "Convex", "Convexo"), L(lang, "wider view, but objects look smaller and further away (door mirrors)", "más ángulo, pero empequeñece y aleja (exteriores)"), 0.6),
             (L(lang, "Panoramic", "Panorámico"), L(lang, "wider interior view; doesn’t replace the door mirrors", "interior de más ángulo; no sustituye a los exteriores"), 0.8)]
    for i, (t, d, s) in enumerate(types):
        y = 54 + i * 54
        p.append(rect(508, y - 6, 40, 30, SKY, 6, f' stroke="{SLATE}" stroke-width="1.5"') + rect(528 - 10 * s, y + 9 - 7 * s, 20 * s, 14 * s, "#b45309", 2))
        p.append(txt(558, y + 6, t, 12, 800, INK) + lines(558, y + 20, _wrap(d, 28), 9.5, 500, SLATE, "start", 11.5))
    return svg(720, 240, "".join(p), L(lang, "Adjusting the mirrors", "Reglaje de los espejos"))


def _wrap(s, n):
    out, cur = [], ""
    for w in s.split():
        if len(cur) + len(w) + 1 > n and cur:
            out.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        out.append(cur)
    return out


# ---------------------------------------------------------------- D6 when to change gear
def rev_bands(lang):
    cx, cy, r = 170, 170, 130
    a0, a1, vmax = 210, -30, 7000

    def ang(v):
        return math.radians(a0 + (a1 - a0) * v / vmax)

    def pt(v, rr):
        a = ang(v)
        return cx + rr * math.cos(a), cy - rr * math.sin(a)

    def arc(v1, v2, rr, col, w):
        x1, y1 = pt(v1, rr)
        x2, y2 = pt(v2, rr)
        large = 1 if abs((a0 + (a1 - a0) * v2 / vmax) - (a0 + (a1 - a0) * v1 / vmax)) > 180 else 0
        return f'<path d="M{x1:.1f} {y1:.1f} A{rr} {rr} 0 {large} 1 {x2:.1f} {y2:.1f}" fill="none" stroke="{col}" stroke-width="{w}"/>'
    p = [f'<circle cx="{cx}" cy="{cy}" r="{r + 14}" fill="{DARK}"/>', arc(0, vmax, r - 6, "#374151", 10), arc(5500, vmax, r - 6, RED, 10)]
    p.append(arc(1500, 2000, r - 26, TEAL, 18) + arc(2000, 2500, r - 46, AMBER, 18))
    for v in range(0, vmax + 1, 1000):
        x1, y1 = pt(v, r)
        x2, y2 = pt(v, r - 14)
        tx, ty = pt(v, r - 64)
        p.append(line(round(x1, 1), round(y1, 1), round(x2, 1), round(y2, 1), "#e5e7eb", 2) + txt(round(tx, 1), round(ty + 5, 1), str(v // 1000), 14, 800, "#e5e7eb", "middle"))
    nx, ny = pt(1800, r - 30)
    p.append(line(cx, cy, round(nx, 1), round(ny, 1), "#ef4444", 4) + f'<circle cx="{cx}" cy="{cy}" r="9" fill="#ef4444"/>')
    p.append(txt(cx, cy + 46, "× 1000 rpm", 11, 600, "#9ca3af", "middle"))
    p.append(card(330, 16, 380, 92, TEAL) + txt(350, 42, L(lang, "Diesel: change up at 1,500–2,000 rpm", "Diésel: cambia entre 1.500 y 2.000 rpm"), 13, 800, TEAL)
             + txt(350, 68, L(lang, "Petrol: change up at 2,000–2,500 rpm", "Gasolina: cambia entre 2.000 y 2.500 rpm"), 13, 800, AMBER)
             + txt(350, 92, L(lang, "Lower revs = less fuel and less pollution.", "Menos revoluciones = menos consumo y contaminación."), 11, 600, INK))
    p.append(card(330, 120, 380, 186, NAVY) + txt(350, 146, L(lang, "You can skip gears", "Puedes saltar marchas"), 13, 800, INK))
    for i, (g, v) in enumerate([("3", 30), ("4", 40), ("5", 50)]):
        x = 360 + i * 110
        p.append(rect(x, 162, 70, 70, "#eef2f7", 10) + txt(x + 35, 202, g + L(lang, "rd" if g == "3" else "th", "ª"), 22, 800, NAVY, "middle")
                 + txt(x + 35, 254, L(lang, f"from {v} km/h", f"desde {v} km/h"), 11, 700, INK, "middle"))
    p.append(lines(350, 280, L(lang, ["Example: 3rd to 5th. Shift down as late as possible,", "also skipping gears."], ["Ejemplo: de 3.ª a 5.ª. Reduce lo más tarde posible,", "saltando también marchas."]), 10.5, 600, SLATE, "start", 13))
    return svg(720, 314, "".join(p), L(lang, "When to change gear", "Cuándo cambiar de marcha"))


# ---------------------------------------------------------------- D7 environmental labels
def _label(cx, cy, kind, r=46):
    fills = {"0": ("#1d4ed8", None), "ECO": ("#16a34a", "#1d4ed8"), "C": ("#16a34a", None), "B": ("#facc15", None)}
    a, b = fills[kind]
    out = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{a}" stroke="#fff" stroke-width="3"/>'
    if b:
        out += f'<path d="M{cx} {cy - r} A{r} {r} 0 0 1 {cx} {cy + r} Z" fill="{b}"/>'
    out += f'<circle cx="{cx}" cy="{cy}" r="{r - 10}" fill="none" stroke="#fff" stroke-width="1.5" opacity="0.7"/>'
    tc = INK if kind == "B" else "#fff"
    size = 17 if kind == "ECO" else 34
    out += txt(cx, cy + size * 0.36, kind, size, 900, tc, "middle")
    return out


def eco_labels(lang):
    rows = [
        ("0", L(lang, "Zero emissions — the most efficient", "0 emisiones: los más eficientes"),
         L(lang, ["Battery electric (BEV), extended-range (REEV), plug-in", "hybrids (PHEV) with at least 40 km of electric range,", "and fuel-cell vehicles."],
           ["Eléctricos de batería (BEV), de autonomía extendida (REEV),", "híbridos enchufables (PHEV) con al menos 40 km de", "autonomía y vehículos de pila de combustible."])),
        ("ECO", L(lang, "ECO", "ECO"),
         L(lang, ["Plug-in hybrids under 40 km, non-plug-in hybrids (HEV),", "natural gas (CNG, LNG) or LPG. They must also meet the", "C criteria."],
           ["Enchufables de menos de 40 km, híbridos no enchufables", "(HEV), gas natural (GNC, GNL) o GLP. Deben cumplir", "además los criterios de la C."])),
        ("C", L(lang, "C — latest Euro standards", "C: últimas normas Euro"),
         L(lang, ["Cars and light vans: petrol from January 2006, diesel", "from September 2015. More than 8 seats and heavy", "vehicles: from 2014."],
           ["Turismos y furgonetas ligeras: gasolina desde enero de", "2006, diésel desde septiembre de 2015. Más de 8 plazas", "y pesados: desde 2014."])),
        ("B", L(lang, "B — earlier Euro standards", "B: normas Euro anteriores"),
         L(lang, ["Cars and light vans: petrol from 1 January 2001, diesel", "from 2006. More than 8 seats and heavy vehicles:", "from 2006."],
           ["Turismos y furgonetas ligeras: gasolina desde el 1 de", "enero de 2001, diésel desde 2006. Más de 8 plazas y", "pesados: desde 2006."])),
    ]
    p = []
    for i, (k, t, body) in enumerate(rows):
        y = 10 + i * 92
        p.append(rect(10, y, 700, 84, "#fff" if i % 2 else CARD, 10, f' stroke="{LINE}" stroke-width="1"'))
        p.append(_label(58, y + 42, k, 34))
        p.append(txt(112, y + 24, t, 13.5, 800, INK) + lines(112, y + 44, body, 11, 500, INK, "start", 14))
    y = 10 + 4 * 92
    p.append(rect(10, y, 700, 46, "#fef2f2", 10, f' stroke="#fecaca" stroke-width="1"') + f'<circle cx="58" cy="{y + 23}" r="17" fill="none" stroke="{SLATE}" stroke-width="2" stroke-dasharray="4 3"/>'
             + txt(112, y + 28, L(lang, "No label: the remaining 50 % most polluting vehicles.", "Sin distintivo: el 50 % restante, los más contaminantes."), 12.5, 700, RED))
    return svg(720, y + 54, "".join(p), L(lang, "DGT environmental labels, most to least efficient", "Distintivos ambientales de la DGT, de más a menos eficiente"))
