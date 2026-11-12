# -*- coding: utf-8 -*-
"""Original SVG diagrams for Topic 2 (EN/ES). No third-party artwork is used."""

from svgkit import NAVY, TEAL, RED, SLATE, INK, svg, txt, lines  # noqa: F401

ASPHALT = "#4b5563"
SHOULDER = "#9ca3af"
VERGE = "#86a96b"
WHITE = "#ffffff"
GOOD = "#0b7548"
CAR = ["#1d4ed8", "#b45309", "#0f766e", "#7c3aed", "#be123c", "#334155"]


def rect(x, y, w, h, fill, rx=0, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{extra}/>'


def hline(x1, x2, y, dash=False, color=WHITE, width=2):
    d = ' stroke-dasharray="14 10"' if dash else ""
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color}" stroke-width="{width}"{d}/>'


def vline(x, y1, y2, dash=False, color=WHITE, width=2):
    d = ' stroke-dasharray="14 10"' if dash else ""
    return f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{color}" stroke-width="{width}"{d}/>'


def car_v(cx, cy, color, up=True, w=22, h=38):
    """Car seen from above, travelling up (or down)."""
    x, y = cx - w / 2, cy - h / 2
    wy = y + 6 if up else y + h - 14
    return (rect(x, y, w, h, color, 6) +
            rect(x + 3, wy, w - 6, 8, "#cbd5e1", 2))


def truck_v(cx, cy, color, up=True, dashed=False):
    w, h = 26, 64
    x, y = cx - w / 2, cy - h / 2
    if dashed:
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="none" stroke="{color}" stroke-width="2" stroke-dasharray="5 4"/>'
    cab = y if up else y + h - 16
    return rect(x, y, w, h, "#cbd5e1", 4, ' stroke="#64748b"') + rect(x, cab, w, 16, color, 4)


def car_h(cx, cy, color, right=True, w=40, h=20):
    """Car seen from above, travelling right (or left)."""
    x, y = cx - w / 2, cy - h / 2
    wx = x + w - 14 if right else x + 6
    return rect(x, y, w, h, color, 6) + rect(wx, y + 3, 8, h - 6, "#cbd5e1", 2)


def arrow_v(x, y1, y2, color=WHITE, width=2.5):
    """Arrow from y1 to y2 (head at y2)."""
    d = -1 if y2 < y1 else 1
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2 - d * 6}" stroke="{color}" stroke-width="{width}"/>'
            f'<path d="M{x - 6} {y2 - d * 8} L{x} {y2} L{x + 6} {y2 - d * 8} Z" fill="{color}"/>')


def arrow_h(x1, x2, y, color=WHITE, width=2.5):
    d = 1 if x2 > x1 else -1
    return (f'<line x1="{x1}" y1="{y}" x2="{x2 - d * 6}" y2="{y}" stroke="{color}" stroke-width="{width}"/>'
            f'<path d="M{x2 - d * 8} {y - 6} L{x2} {y} L{x2 - d * 8} {y + 6} Z" fill="{color}"/>')


def tick(cx, cy, r=11):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{GOOD}"/>'
            f'<path d="M{cx - 5} {cy} L{cx - 1.5} {cy + 4} L{cx + 5.5} {cy - 4.5}" stroke="#fff" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')


def cross(cx, cy, r=11):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{RED}"/>'
            f'<path d="M{cx - 4.5} {cy - 4.5} L{cx + 4.5} {cy + 4.5} M{cx + 4.5} {cy - 4.5} L{cx - 4.5} {cy + 4.5}" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>')


def bracket_v(x, y1, y2, side="left", color=NAVY):
    """Vertical bracket; its arms point towards the road."""
    a = 8 if side == "left" else -8
    return f'<path d="M{x + a} {y1} H{x} V{y2} H{x + a}" stroke="{color}" stroke-width="2" fill="none"/>'


# ---------------------------------------------------------------- D1 parts of the road
def road_parts(lang):
    T = {
        "en": dict(sh="HARD SHOULDER", lane="LANE", med="MEDIAN", calz=["Carriageway", "(calzada)"], plat=["Road platform", "(plataforma)"],
                   plat_n=["= carriageway", "+ both shoulders"], carril=["Lane", "(carril)"], calz_n=["= the lanes"]),
        "es": dict(sh="ARCÉN", lane="CARRIL", med="MEDIANA", calz=["Calzada"], plat=["Plataforma"],
                   plat_n=["= calzada", "+ sus dos arcenes"], carril=["Carril"], calz_n=["= los carriles"]),
    }[lang]
    x0, x1 = 160, 560
    rows = [  # (y, h, kind)
        (20, 14, "verge"), (34, 22, "sh"), (56, 40, "lane"), (96, 40, "lane"), (136, 16, "sh"),
        (152, 32, "med"), (184, 16, "sh"), (200, 40, "lane"), (240, 40, "lane"), (280, 22, "sh"), (302, 14, "verge"),
    ]
    fill = {"verge": VERGE, "sh": SHOULDER, "lane": ASPHALT, "med": VERGE}
    p = [rect(x0, y, x1 - x0, h, fill[k]) for y, h, k in rows]
    # edge lines (solid) and lane lines (broken)
    for y in (56, 136, 200, 280):
        p.append(hline(x0, x1, y))
    p.append(hline(x0, x1, 96, dash=True))
    p.append(hline(x0, x1, 240, dash=True))
    # crash barrier on the median
    p.append(hline(x0, x1, 168, color="#e5e7eb", width=3))
    for x in range(x0 + 10, x1, 40):
        p.append(rect(x, 164, 4, 8, "#e5e7eb"))
    # labels painted on the surface
    p.append(txt(x0 + 12, 49, T["sh"], 10.5, 700, WHITE))
    p.append(txt(x0 + 12, 296, T["sh"], 10.5, 700, WHITE))
    p.append(txt(x1 - 12, 186 - 3, T["med"], 10.5, 700, "#1f3b17", "end"))
    p.append(txt(x0 + 12, 81, T["lane"], 11, 700, WHITE))
    p.append(txt(x0 + 12, 265, T["lane"], 11, 700, WHITE))
    # traffic
    p.append(car_h(420, 76, CAR[0], right=False) + car_h(300, 116, CAR[1], right=False))
    p.append(car_h(330, 220, CAR[2]) + car_h(470, 260, CAR[3]))
    # left: carriageway bracket (top) and lane bracket (bottom)
    p.append(bracket_v(148, 56, 136, "left"))
    p.append(lines(140, 92 - (len(T["calz"]) - 1) * 7, T["calz"], 12, 700, NAVY, "end", 14))
    p.append(lines(140, 92 + len(T["calz"]) * 14 - 4, T["calz_n"], 10.5, 400, SLATE, "end", 13))
    p.append(bracket_v(148, 240, 280, "left"))
    p.append(lines(140, 260 - (len(T["carril"]) - 1) * 7 + 4, T["carril"], 12, 700, NAVY, "end", 14))
    # right: platform bracket (bottom carriageway + its shoulders)
    p.append(bracket_v(572, 184, 302, "right"))
    p.append(lines(582, 232, T["plat"], 12, 700, NAVY, "start", 14))
    p.append(lines(582, 232 + len(T["plat"]) * 14 + 2, T["plat_n"], 10.5, 400, SLATE, "start", 13))
    return svg(720, 324, "".join(p), "Parts of the road" if lang == "en" else "Partes de la vía")


# ---------------------------------------------------------------- D2 lane choice
def lane_choice(lang):
    T = {
        "en": dict(
            a=["Two-way, two lanes"], b=["Two-way, three lanes", "(broken lines)"], c=["One way, 3+ lanes, out of town:", "trucks &gt; 3,500 kg, combos &gt; 7 m"],
            a_n=["Keep to the right-hand lane"], b_n=["Right lane. Centre: only to", "overtake or turn left. Left: never"],
            c_n=["Right lane; exceptionally the", "next one; never the others"],
        ),
        "es": dict(
            a=["Doble sentido, dos carriles"], b=["Doble sentido, tres carriles", "(líneas discontinuas)"], c=["Sentido único, 3 o más carriles,", "interurbana: pesados y conjuntos &gt; 7 m"],
            a_n=["Por el carril derecho"], b_n=["Carril derecho. Central: solo para", "adelantar o girar a la izq. Izquierdo: nunca"],
            c_n=["El derecho; excepcionalmente el", "contiguo; nunca los restantes"],
        ),
    }[lang]
    p = []
    top, bot = 56, 286
    lw = 46

    def road(xc, n, dashes):
        x = xc - n * lw / 2
        out = [rect(x - 10, top, n * lw + 20, bot - top, SHOULDER), rect(x, top, n * lw, bot - top, ASPHALT)]
        out.append(vline(x, top, bot) + vline(x + n * lw, top, bot))
        for i in range(1, n):
            out.append(vline(x + i * lw, top, bot, dash=dashes[i - 1]))
        return x, "".join(out)

    def heading(xc, arr):
        return lines(xc, 18, arr, 12, 700, NAVY, "middle", 15)

    def note(xc, arr):
        return lines(xc, bot + 20, arr, 10.5, 400, INK, "middle", 13)

    # panel A
    xa = 120
    x, r = road(xa, 2, [True])
    p.append(r + heading(xa, T["a"]) + note(xa, T["a_n"]))
    p.append(car_v(x + lw * 1.5, 220, CAR[0], up=True) + car_v(x + lw * 0.5, 110, CAR[5], up=False))
    p.append(arrow_v(x + lw * 1.5, 190, 160) + arrow_v(x + lw * 0.5, 140, 170))
    p.append(tick(x + lw * 2 + 26, 220))
    # panel B
    xb = 360
    x, r = road(xb, 3, [True, True])
    p.append(r + heading(xb, T["b"]) + note(xb, T["b_n"]))
    p.append(car_v(x + lw * 2.5, 236, CAR[0], up=True) + tick(x + lw * 3 + 26, 236))
    p.append(car_v(x + lw * 1.5, 170, CAR[1], up=True))
    p.append(f'<path d="M{x + lw * 2.5} 200 C {x + lw * 2.5} 180, {x + lw * 1.5} 200, {x + lw * 1.5} 194" stroke="{WHITE}" stroke-width="2" fill="none" stroke-dasharray="4 3"/>')
    p.append(car_v(x + lw * 0.5, 96, CAR[5], up=False) + arrow_v(x + lw * 0.5, 126, 150))
    p.append(cross(x + lw * 0.5, 210))
    # panel C
    xc = 600
    x, r = road(xc, 3, [True, True])
    p.append(r + heading(xc, T["c"]) + note(xc, T["c_n"]))
    p.append(truck_v(x + lw * 2.5, 226, NAVY) + tick(x + lw * 3 + 26, 226))
    p.append(truck_v(x + lw * 1.5, 150, NAVY, dashed=True))
    p.append(cross(x + lw * 0.5, 110))
    for i in range(3):
        p.append(arrow_v(x + lw * (i + 0.5), 280, 264, color="#e5e7eb", width=2))
    return svg(720, 330, "".join(p), "Which lane to use" if lang == "en" else "Qué carril usar")


# ---------------------------------------------------------------- D3 emergency corridor
def corridor(lang):
    T = {
        "en": dict(a="Two lanes: gap in the centre", b="Three or more lanes: between the left lane and the next",
                   gap="EMERGENCY CORRIDOR"),
        "es": dict(a="Dos carriles: hueco en el centro", b="Tres o más: entre el carril izquierdo y su contiguo",
                   gap="CARRIL DE EMERGENCIA"),
    }[lang]
    p = []
    top, bot = 34, 284
    lw = 50

    def road(x, n):
        out = [rect(x - 12, top, n * lw + 24, bot - top, SHOULDER), rect(x, top, n * lw, bot - top, ASPHALT),
               vline(x, top, bot), vline(x + n * lw, top, bot)]
        for i in range(1, n):
            out.append(vline(x + i * lw, top, bot, dash=True, color="#9ca3af"))
        return "".join(out)

    def ambulance(cx, cy):
        return (rect(cx - 12, cy - 22, 24, 44, WHITE, 5, f' stroke="{RED}" stroke-width="1.5"') +
                rect(cx - 2.5, cy - 9, 5, 18, RED) + rect(cx - 9, cy - 2.5, 18, 5, RED) +
                rect(cx - 12, cy - 22, 24, 6, "#2563eb", 3))

    # panel A: two lanes
    xa = 110
    p.append(road(xa, 2))
    p.append(txt(xa + lw, 22, T["a"], 12, 700, NAVY, "middle"))
    for i, y in enumerate((80, 132, 184, 236)):
        p.append(car_v(xa + 15, y, CAR[i % 6]) + car_v(xa + 2 * lw - 15, y, CAR[(i + 3) % 6]))
    p.append(f'<rect x="{xa + 30}" y="{top}" width="{2 * lw - 60}" height="{bot - top}" fill="#fde68a" opacity=".35"/>')
    p.append(ambulance(xa + lw, 250) + arrow_v(xa + lw, 222, 190, color=RED))
    # panel B: three lanes
    xb = 420
    p.append(road(xb, 3))
    p.append(txt(xb + 1.5 * lw, 22, T["b"], 12, 700, NAVY, "middle"))
    for i, y in enumerate((80, 132, 184, 236)):
        p.append(car_v(xb + 15, y, CAR[i % 6]))
        p.append(car_v(xb + lw + 30, y, CAR[(i + 2) % 6]) + car_v(xb + 2 * lw + 34, y, CAR[(i + 4) % 6]))
    p.append(f'<rect x="{xb + 30}" y="{top}" width="{lw - 12}" height="{bot - top}" fill="#fde68a" opacity=".35"/>')
    p.append(ambulance(xb + 49, 250) + arrow_v(xb + 49, 222, 190, color=RED))
    # one label between the panels, pointing into both gaps (between the rows of cars)
    mid, y = (xa + 2 * lw + xb) / 2, 158
    p.append(txt(mid, y + 4, T["gap"], 10.5, 700, RED, "middle"))
    p.append(f'<line x1="{mid - 78}" y1="{y}" x2="{xa + lw + 4}" y2="{y}" stroke="{RED}" stroke-width="1.5"/>')
    p.append(f'<circle cx="{xa + lw}" cy="{y}" r="3.5" fill="{RED}"/>')
    p.append(f'<line x1="{mid + 78}" y1="{y}" x2="{xb + 45}" y2="{y}" stroke="{RED}" stroke-width="1.5"/>')
    p.append(f'<circle cx="{xb + 49}" cy="{y}" r="3.5" fill="{RED}"/>')
    return svg(720, 300, "".join(p), "Emergency corridor" if lang == "en" else "Carril de emergencia")


# ---------------------------------------------------------------- D4 safety distances
def distances(lang):
    T = {
        "en": dict(
            r=[(["Out of town:", "MMA &gt; 3,500 kg or", "longer than 10 m"], 50, "≥ 50 m"),
               (["Tunnels and underpasses"], 100, "≥ 100 m or 4 s · 2 chevrons"),
               (["Tunnels: MMA &gt; 3,500 kg"], 150, "≥ 150 m or 6 s · 3 chevrons")],
            note="Elsewhere: enough space to stop without hitting the vehicle in front. Chevrons painted on the lane: keep at least two.",
        ),
        "es": dict(
            r=[(["Fuera de poblado:", "MMA &gt; 3.500 kg o más", "de 10 m de longitud"], 50, "≥ 50 m"),
               (["Túneles y pasos inferiores"], 100, "≥ 100 m o 4 s · 2 galones"),
               (["Túneles: MMA &gt; 3.500 kg"], 150, "≥ 150 m o 6 s · 3 galones")],
            note="En los demás casos: espacio para detenerse sin chocar con el de delante. Galones pintados en el carril: al menos dos.",
        ),
    }[lang]
    x0, sc = 230, 2.8
    X = lambda m: x0 + m * sc
    p = []
    top, rh = 30, 62
    colors = [TEAL, "#1d4ed8", NAVY]
    for i, (label, m, value) in enumerate(T["r"]):
        y = top + i * rh
        p.append(lines(8, y + 24 - (len(label) - 1) * 7, label, 11.5, 700, INK, "start", 14))
        p.append(car_h(x0 - 24, y + 24, CAR[5]))
        p.append(car_h(X(m) + 24, y + 24, colors[i]))
        p.append(rect(x0, y + 18, m * sc, 12, colors[i], 3, ' opacity=".25"'))
        p.append(f'<line x1="{x0}" y1="{y + 24}" x2="{X(m)}" y2="{y + 24}" stroke="{colors[i]}" stroke-width="2.5"/>')
        p.append(txt(x0 + 6, y + 13, value, 11.5, 700, colors[i]))
    ay = top + 3 * rh + 4
    p.append(f'<line x1="{x0}" y1="{ay}" x2="{X(150)}" y2="{ay}" stroke="{SLATE}" stroke-width="1.5"/>')
    for m in (0, 50, 100, 150):
        p.append(f'<line x1="{X(m)}" y1="{ay - 4}" x2="{X(m)}" y2="{ay + 4}" stroke="{SLATE}" stroke-width="1.5"/>')
        p.append(txt(X(m), ay + 18, f"{m} m" if m == 150 else str(m), 10.5, 400, SLATE, "middle"))
    p.append(txt(8, ay + 44, T["note"], 10.5, 400, SLATE))
    return svg(720, 270, "".join(p), "Minimum distances" if lang == "en" else "Distancias mínimas")


# ---------------------------------------------------------------- D5 traffic levels
def levels(lang):
    T = {
        "en": [("White", "Normal", "flowing", "&gt; 90 %"), ("Green", "Conditioned", "heavy traffic", "75 – 90 %"),
               ("Yellow", "Discontinuous", "occasional queues", "25 – 75 %"), ("Red", "Saturated", "frequent long stops", "&lt; 25 %"),
               ("Black", "Interrupted", "road closed, flooded…", "")],
        "es": [("Blanco", "Normal", "circulación fluida", "&gt; 90 %"), ("Verde", "Condicionada", "circulación intensa", "75 – 90 %"),
               ("Amarillo", "Discontinua", "retenciones esporádicas", "25 – 75 %"), ("Rojo", "Saturada", "detenciones frecuentes", "&lt; 25 %"),
               ("Negro", "Interrumpida", "carretera cortada…", "")],
    }[lang]
    fills = ["#ffffff", "#15803d", "#facc15", "#dc2626", "#111827"]
    p = []
    for i, (col, name, sub, pct) in enumerate(T):
        cx = 72 + i * 144
        p.append(f'<circle cx="{cx}" cy="52" r="34" fill="{fills[i]}" stroke="#64748b" stroke-width="2"/>')
        if pct:
            p.append(txt(cx, 57, pct, 13, 800, "#111827" if i in (0, 2) else "#ffffff", "middle"))
        p.append(txt(cx, 108, col, 11, 700, SLATE, "middle"))
        p.append(txt(cx, 125, name, 12.5, 700, INK, "middle"))
        p.append(txt(cx, 141, sub, 10.5, 400, SLATE, "middle"))
    return svg(720, 156, "".join(p), "Traffic level colours" if lang == "en" else "Colores del nivel de circulación")


# ---------------------------------------------------------------- D6 pedestrians on a road without pavement
def walkers(lang):
    T = {
        "en": dict(l=["Left-hand shoulder,", "facing the traffic", "(in single file)"], r=["Pushing a bicycle, moped", "or VMP, or a group led", "by someone: on the right"],
                   none="No usable pedestrian zone"),
        "es": dict(l=["Arcén izquierdo,", "de cara al tráfico", "(unos detrás de otros)"], r=["Empujando una bicicleta,", "ciclomotor o VMP, o un grupo", "dirigido: por la derecha"],
                   none="Sin zona peatonal practicable"),
    }[lang]
    p = []
    top, bot = 30, 262
    xl, xr = 260, 460          # outer edges of the shoulders
    sh = 32
    p.append(rect(xl, top, xr - xl, bot - top, SHOULDER))
    p.append(rect(xl + sh, top, xr - xl - 2 * sh, bot - top, ASPHALT))
    p.append(vline(xl + sh, top, bot) + vline(xr - sh, top, bot) + vline((xl + xr) / 2, top, bot, dash=True))
    p.append(txt((xl + xr) / 2, 20, T["none"], 12, 700, NAVY, "middle"))

    def person(cx, cy, color=INK):
        return (f'<circle cx="{cx}" cy="{cy - 14}" r="5" fill="{color}"/>'
                f'<path d="M{cx} {cy - 8} V{cy + 6} M{cx} {cy + 6} L{cx - 5} {cy + 16} M{cx} {cy + 6} L{cx + 5} {cy + 16} M{cx - 6} {cy - 2} H{cx + 6}" stroke="{color}" stroke-width="2.4" stroke-linecap="round" fill="none"/>')

    def bike(cx, cy):
        return (f'<circle cx="{cx}" cy="{cy - 16}" r="7" fill="none" stroke="{TEAL}" stroke-width="2.2"/>'
                f'<circle cx="{cx}" cy="{cy + 16}" r="7" fill="none" stroke="{TEAL}" stroke-width="2.2"/>'
                f'<path d="M{cx} {cy - 16} L{cx} {cy + 16}" stroke="{TEAL}" stroke-width="2.4"/>')

    # left shoulder: pedestrians walking up, facing traffic coming down the left lane
    p.append(person(xl + sh / 2, 150) + person(xl + sh / 2, 196))
    p.append(arrow_v(xl + sh / 2, 120, 92, color=NAVY))
    p.append(car_v(xl + sh + 34, 82, CAR[1], up=False) + arrow_v(xl + sh + 34, 108, 134))
    # right shoulder: person pushing a bike, walking up with the traffic
    p.append(bike(xr - sh / 2 + 2, 150) + person(xr - sh / 2 - 9, 186, INK))
    p.append(arrow_v(xr - sh / 2, 122, 96, color=NAVY))
    p.append(car_v(xr - sh - 34, 236, CAR[0], up=True) + arrow_v(xr - sh - 34, 212, 188))
    # captions
    p.append(lines(xl - 16, 140, T["l"], 12, 700, INK, "end", 15))
    p.append(lines(xr + 16, 140, T["r"], 12, 700, INK, "start", 15))
    return svg(720, 272, "".join(p), "Where pedestrians walk" if lang == "en" else "Por dónde circulan los peatones")
