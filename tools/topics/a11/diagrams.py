# -*- coding: utf-8 -*-
"""Original SVG diagrams for Category A1/A2, Topic 11 (first aid), EN/ES. No third-party artwork is used. Two figures
are drawn for riders; the others (PAS, 112, assessment, airway, recovery position, CPR, bleeding, shock) come with the
blocks taken from Category B, Topic 11."""

from svgkit import NAVY, TEAL, AMBER, RED, SLATE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect, car_h, tick, cross, ASPHALT, VERGE, WHITE
from ..b09.diagrams import L, line, LINE, CARD
from ..b10.diagrams import arrow, rot, badge
from ..b11.diagrams import limb, poly, head, _standing, SKIN, CLOTH, VEST, DARK
from ..b12.diagrams import moto_v

GOOD = "#0b7548"
SHELL = "#facc15"
VISOR = "#1e3a5f"


# ---------------------------------------------------------------- D0 the PAS rule, rider's wording
def pas_moto(lang):
    steps = [
        (TEAL, L(lang, "1 · PROTECT", "1 · PROTEGER"),
         L(lang, ["Yourself: stop somewhere safe,", "off the carriageway, engine off;", "vest on to walk on the road.", "The scene: vehicles off the", "road, engine off, no smoking.", "The victims: don’t move them", "unless there is danger."],
           ["A ti: para en un lugar seguro,", "fuera de la calzada, motor", "parado; chaleco para caminar.", "El lugar: vehículos fuera de", "la calzada, motor parado, no", "fumar. A las víctimas: no", "moverlas salvo peligro."])),
        (AMBER, L(lang, "2 · ALERT", "2 · AVISAR"),
         L(lang, ["Call 112: free, works without", "credit, the same in the whole", "EU, answered in your language.", "Say where, how many are hurt", "and how, what happened, and", "who you are."],
           ["Llama al 112: gratuito, sin", "saldo, común en toda la UE,", "te atienden en tu idioma.", "Di dónde, cuántos heridos y", "cómo están, qué ha pasado y", "quién eres."])),
        (RED, L(lang, "3 · HELP", "3 · SOCORRER"),
         L(lang, ["Only if you know how; if not,", "wait for the medical team.", "Stay calm, worst cases first.", "Loosen tight clothing, cover", "them, nothing to eat or drink,", "don’t remove the helmet,", "stay with them."],
           ["Solo si sabes hacerlo; si no,", "espera a los sanitarios.", "Calma, primero los más graves.", "Afloja la ropa, abrígales, nada", "de comer ni beber, no quites", "el casco, acompáñales."])),
    ]
    p = []
    for i, (col, title, body) in enumerate(steps):
        x = 14 + i * 238
        p.append(rect(x, 10, 216, 46, col, 10) + txt(x + 108, 40, title, 17, 800, "#fff", "middle"))
        p.append(rect(x, 64, 216, 132, "#fff", 10, f' stroke="{LINE}" stroke-width="1.5"') + lines(x + 12, 86, body, 11, 500, INK, "start", 15))
        if i < 2:
            p.append(arrow(x + 218, 33, x + 236, 33, SLATE, 3, 9))
    return svg(720, 204, "".join(p), L(lang, "The PAS rule: protect, alert, help", "La regla PAS: proteger, avisar, socorrer"))


# ---------------------------------------------------------------- D1 protecting yourself and the scene, on a motorcycle
def protect_moto(lang):
    top, mid, edge, sh = 40, 100, 160, 196
    p = [rect(0, 0, 720, top, VERGE), rect(0, top, 720, edge - top, ASPHALT), rect(0, edge, 720, sh - edge, "#9ca3af"), rect(0, sh, 720, 64, VERGE)]
    p.append(rect(0, top + 3, 720, 3, WHITE) + rect(0, edge - 3, 720, 3, WHITE))
    for x in range(0, 720, 44):
        p.append(rect(x, mid - 1.5, 24, 3, WHITE))
    p.append(rect(0, sh + 4, 720, 4, "#d1d5db") + "".join(rect(x, sh + 2, 4, 12, "#6b7280") for x in range(10, 720, 60)))
    p.append(car_h(80, 130, "#cbd5e1") + car_h(640, 70, "#cbd5e1", right=False))
    # your motorcycle on the shoulder, hazard lights if fitted, an optional V-16 on it
    mx, my = 170, 178
    p.append(f'<g transform="translate({mx} {my}) rotate(90) scale(1.5) translate({-mx} {-my})">{moto_v(mx, my, NAVY)}</g>')
    for hx, hy in ((146, 172), (146, 184), (194, 172), (194, 184)):
        p.append(f'<circle cx="{hx}" cy="{hy}" r="3.5" fill="#f59e0b"/>')
    p.append(f'<circle cx="166" cy="178" r="12" fill="#f59e0b" opacity="0.3"/><circle cx="166" cy="178" r="5" fill="#f59e0b" stroke="#fff" stroke-width="1.5"/>')
    p.append(f'<g transform="translate(470 178) rotate(-8)">{car_h(0, 0, "#b45309")}</g>')
    p.append(_standing(320, 252))
    for x, y, n in ((170, 158, 1), (320, 178, 2), (470, 156, 3)):
        p.append(badge(x, y - 2, n))
    notes = [
        L(lang, "Motorcycle off the carriageway, engine off; hazard lights if it has them. A V-16 is optional on a motorcycle.", "Moto fuera de la calzada, motor parado; luces de emergencia si las tiene. La V-16 es opcional en moto."),
        L(lang, "The vest your motorcycle must carry: put it on to walk on an interurban road; wait behind the barrier.", "El chaleco que debe llevar la moto: póntelo para caminar por una interurbana; espera tras la barrera."),
        L(lang, "Crashed vehicles off the carriageway if they block it: engine off. No smoking.", "Vehículos accidentados fuera de la calzada si obstaculizan: motor parado. No fumar."),
    ]
    for i, n in enumerate(notes):
        y = 284 + i * 22
        p.append(badge(24, y - 4, i + 1, NAVY, 9) + txt(40, y, n, 11.5, 600, INK))
    return svg(720, 346, "".join(p), L(lang, "Protecting yourself and the scene on a motorcycle", "Protegerse y proteger el lugar en moto"))


# ---------------------------------------------------------------- D2 removing a rider's helmet, two people
def _kneeling(cx, base, facing=1, arms=None):
    """A kneeling rescuer seen from the side; `arms` is a list of (x, y) hand positions."""
    hip = (cx, base - 30)
    out = limb(cx, base - 30, cx - 26 * facing, base - 4, 11, DARK) + limb(cx - 26 * facing, base - 4, cx - 2 * facing, base - 4, 10, DARK)
    out += rect(cx - 11, base - 82, 22, 54, VEST, 8) + rect(cx - 11, base - 62, 22, 3, "#cbd5e1", 0)
    out += head(cx + 4 * facing, base - 96, 11)
    for hx, hy in arms or []:
        out += poly([(cx + 4 * facing, base - 74), ((cx + hx) / 2, (base - 70 + hy) / 2 - 4), (hx, hy)], 7, VEST)
    return out


def helmet_off(lang):
    g = 222
    p = [rect(8, 8, 448, 256, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'), line(20, g, 444, g, "#94a3b8", 2)]
    # casualty on the back, head to the left, wearing a helmet
    p.append(rect(228, g - 44, 200, 40, CLOTH, 14) + limb(232, g - 26, 210, g - 26, 14, SKIN))
    hx, hy = 186, g - 30
    p.append(f'<circle cx="{hx}" cy="{hy}" r="27" fill="{SHELL}" stroke="#a16207" stroke-width="2"/>')
    p.append(f'<path d="M{hx + 6} {hy - 24} A27 27 0 0 1 {hx + 26} {hy - 4} L{hx + 12} {hy - 2} Z" fill="{VISOR}"/>')
    p.append(arrow(150, hy, 104, hy, AMBER, 3, 11))
    # rescuer 1 at the head, rescuer 2 at the side holding neck and jaw
    p.append(_kneeling(70, g, 1, [(162, hy - 14), (162, hy + 14)]))
    p.append(_kneeling(276, g - 2, -1, [(212, g - 16), (204, g - 6)]))
    p.append(badge(70, 30, 1) + badge(276, 30, 2))
    p.append(lines(88, 26, L(lang, ["Opens the strap, spreads the", "sides and slides the helmet", "off along the body’s line"], ["Abre el cierre, separa los", "laterales y saca el casco en", "la línea del cuerpo"]), 10.5, 700, INK, "start", 13))
    p.append(lines(294, 26, L(lang, ["Holds the neck and jaw", "still: head, neck and", "trunk stay in line"], ["Sujeta cuello y mandíbula:", "cabeza, cuello y tronco", "se mantienen alineados"]), 10.5, 700, INK, "start", 13))
    # when to take it off
    cards = [
        (GOOD, True, L(lang, "Leave it on", "No lo quites"),
         L(lang, ["Check breathing and the pulse in", "the neck (carotid) with the", "helmet on: open the visor."], ["Comprueba la respiración y el", "pulso carotídeo con el casco", "puesto: abre la pantalla."])),
        (AMBER, False, L(lang, "Only if essential", "Solo si es imprescindible"),
         L(lang, ["For example, to do CPR. At least", "two people who know the", "technique, as in the drawing."], ["Por ejemplo, para hacer la RCP.", "Mínimo dos personas que", "conozcan la técnica, como aquí."])),
    ]
    for i, (col, ok, title, body) in enumerate(cards):
        y = 8 + i * 132
        p.append(rect(468, y, 244, 124, "#fff", 10, f' stroke="{col}" stroke-width="2"'))
        p.append((tick if ok else cross)(490, y + 24, 11) if ok else badge(490, y + 24, "!", AMBER, 11))
        p.append(txt(510, y + 29, title, 13, 800, col) + lines(484, y + 58, body, 11, 600, INK, "start", 15))
    return svg(720, 272, "".join(p), L(lang, "An injured rider’s helmet", "El casco del motorista herido"))
