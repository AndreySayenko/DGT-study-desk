# -*- coding: utf-8 -*-
"""Original SVG diagrams for Topic 11 (first aid), EN/ES. No third-party artwork is used. Each function takes the
language ("en" or "es") and returns an SVG string. People are drawn as simple pictograms."""
import math

from svgkit import NAVY, TEAL, AMBER, RED, SLATE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect, car_h, tick, cross, ASPHALT, VERGE, WHITE  # noqa: F401
from ..b09.diagrams import L, line, MUTED, LINE, CARD
from ..b10.diagrams import arrow, rot, badge

SKIN = "#d9b38c"
CLOTH = "#64748b"
VEST = "#d9f99d"
DARK = "#1f2937"
BLOOD = "#b91c1c"


def limb(x1, y1, x2, y2, w=10, c=CLOTH):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>'


def poly(pts, w=10, c=CLOTH):
    return f'<polyline points="{" ".join(f"{x},{y}" for x, y in pts)}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'


def head(cx, cy, r=12, c=SKIN):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}"/>'


def card(x, y, w, h, color=NAVY):
    return rect(x, y, w, h, "#fff", 10, f' stroke="{LINE}" stroke-width="1.5"') + rect(x, y, 6, h, color, 3)


# ---------------------------------------------------------------- D1 the PAS rule
def pas_rule(lang):
    steps = [
        (TEAL, L(lang, "1 · PROTECT", "1 · PROTEGER"),
         L(lang, ["Yourself: stop somewhere safe,", "V-16 on the roof, vest on", "before getting out.", "The scene: vehicles off the", "road, engine off, no smoking.", "The victims: don’t move them", "unless there is danger."],
           ["A ti: para en un lugar seguro,", "V-16 en el techo, chaleco", "antes de bajar.", "El lugar: vehículos fuera de", "la calzada, motor parado, no", "fumar. A las víctimas: no", "moverlas salvo peligro."])),
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


# ---------------------------------------------------------------- D2 calling 112
def call_112(lang):
    p = [rect(30, 14, 130, 214, DARK, 22) + rect(40, 34, 110, 168, "#fee2e2", 6) + rect(80, 22, 30, 5, "#4b5563", 2) + f'<circle cx="95" cy="214" r="7" fill="#4b5563"/>']
    p.append(txt(95, 112, "112", 38, 800, RED, "middle") + f'<path d="M78 140 q-4 14 10 24 l6 -6 -8 -8 q-3 2 -4 -2 l4 -8 -8 -6 z" fill="{RED}"/>'
             + txt(112, 160, L(lang, "call", "llama"), 12, 700, RED, "middle"))
    p.append(lines(95, 246, L(lang, ["free · no credit needed", "whole EU · your language"], ["gratuito · sin saldo", "toda la UE · tu idioma"]), 10.5, 600, SLATE, "middle", 13))
    cards = [
        (L(lang, "WHERE", "DÓNDE"), L(lang, ["The exact place: road,", "kilometre, direction."], ["El lugar exacto: vía,", "kilómetro, sentido."])),
        (L(lang, "WHO IS HURT", "QUIÉN ESTÁ HERIDO"), L(lang, ["How many injured and", "what state they are in."], ["Número de heridos y", "su estado."])),
        (L(lang, "WHAT HAPPENED", "QUÉ HA PASADO"), L(lang, ["Vehicles involved, fire risk,", "dangerous goods…"], ["Vehículos implicados, riesgo", "de incendio, mercancías peligrosas…"])),
        (L(lang, "WHO YOU ARE", "QUIÉN ERES"), L(lang, ["Name, surname, ID number", "and a contact phone."], ["Nombre, apellidos, DNI", "y teléfono de contacto."])),
    ]
    for i, (t, b) in enumerate(cards):
        x, y = 196 + (i % 2) * 262, 22 + (i // 2) * 118
        p.append(card(x, y, 246, 104, AMBER) + txt(x + 20, y + 30, t, 14, 800, INK) + lines(x + 20, y + 54, b, 11.5, 500, INK, "start", 16))
    return svg(720, 266, "".join(p), L(lang, "What to tell 112", "Qué decir al 112"))


# ---------------------------------------------------------------- D3 protecting the scene
def _standing(cx, base, vest=True):
    return (head(cx, base - 62, 9) + limb(cx - 5, base - 26, cx - 7, base, 7, DARK) + limb(cx + 5, base - 26, cx + 7, base, 7, DARK)
            + rect(cx - 10, base - 52, 20, 30, VEST if vest else CLOTH, 6) + rect(cx - 10, base - 40, 20, 3, "#cbd5e1", 0)
            + limb(cx - 12, base - 48, cx - 16, base - 28, 6, VEST if vest else CLOTH) + limb(cx + 12, base - 48, cx + 22, base - 62, 6, VEST if vest else CLOTH)
            + rect(cx + 18, base - 72, 7, 11, DARK, 2))


def protect_scene(lang):
    top, mid, edge, sh = 40, 100, 160, 196
    p = [rect(0, 0, 720, top, VERGE), rect(0, top, 720, edge - top, ASPHALT), rect(0, edge, 720, sh - edge, "#9ca3af"), rect(0, sh, 720, 64, VERGE)]
    p.append(rect(0, top + 3, 720, 3, WHITE) + rect(0, edge - 3, 720, 3, WHITE))
    for x in range(0, 720, 44):
        p.append(rect(x, mid - 1.5, 24, 3, WHITE))
    p.append(rect(0, sh + 4, 720, 4, "#d1d5db") + "".join(rect(x, sh + 2, 4, 12, "#6b7280") for x in range(10, 720, 60)))
    # traffic in the lanes
    p.append(car_h(80, 130, "#cbd5e1") + car_h(640, 70, "#cbd5e1", right=False))
    # your car on the shoulder: hazard lights and the V-16 on the roof
    p.append(car_h(170, 178, NAVY))
    for (hx, hy) in ((151, 169), (151, 187), (189, 169), (189, 187)):
        p.append(f'<circle cx="{hx}" cy="{hy}" r="4" fill="#f59e0b"/>')
    p.append(f'<circle cx="174" cy="178" r="13" fill="#f59e0b" opacity="0.35"/><circle cx="174" cy="178" r="6" fill="#f59e0b" stroke="#fff" stroke-width="1.5"/>')
    # accident car moved onto the shoulder
    p.append(f'<g transform="translate(470 178) rotate(-8)">{car_h(0, 0, "#b45309")}</g>')
    # person behind the barrier
    p.append(_standing(320, 252))
    marks = [(174, 158, 1), (320, 178, 2), (470, 156, 3)]
    for x, y, n in marks:
        p.append(badge(x, y - 2, n))
    notes = [
        L(lang, "Your car off the carriageway: hazard lights, and the V-16 on the roof from inside, window down.", "Tu coche fuera de la calzada: luces de emergencia y la V-16 en el techo desde dentro, bajando la ventanilla."),
        L(lang, "Vest on before getting out; walk and wait off the carriageway, behind the barrier.", "Chaleco antes de bajar; camina y espera fuera de la calzada, tras la barrera."),
        L(lang, "Crashed vehicles off the carriageway if they block it: handbrake on, engine off. No smoking.", "Vehículos accidentados fuera de la calzada si obstaculizan: freno de mano y motor parado. No fumar."),
    ]
    for i, n in enumerate(notes):
        y = 284 + i * 22
        p.append(badge(24, y - 4, i + 1, NAVY, 9) + txt(40, y, n, 11.5, 600, INK))
    return svg(720, 346, "".join(p), L(lang, "Protecting yourself and the scene", "Protegerse y proteger el lugar"))


# ---------------------------------------------------------------- D4 initial assessment, step by step
def triage_flow(lang):
    p = []

    def bx(x, y, w, h, fill, t, sub, tcol="#fff", scol=None):
        out = rect(x, y, w, h, fill, 10, ' stroke="#cbd5e1" stroke-width="1.5"' if fill == "#fff" else "")
        out += txt(x + 12, y + 20, t, 12.5, 800, tcol)
        out += lines(x + 12, y + 37, sub, 11, 500, scol or tcol, "start", 14)
        return out
    p.append(rect(14, 8, 692, 34, "#eef2f7", 8) + txt(360, 30, L(lang, "Several injured? Check them all before helping any: 10–15 seconds each.", "¿Varios heridos? Valóralos a todos antes de socorrer a ninguno: 10–15 segundos cada uno."), 12, 700, NAVY, "middle"))
    p.append(bx(220, 58, 280, 58, NAVY, L(lang, "Does the person respond?", "¿Responde?"), L(lang, ["Ask a simple question loudly; pinch the", "back of the hand."], ["Pregunta algo sencillo en voz alta;", "pellizca el dorso de la mano."])))
    p.append(bx(14, 152, 226, 112, TEAL, L(lang, "YES — conscious", "SÍ: consciente"),
                L(lang, ["Check breathing and that there is", "no bleeding or serious wound.", "Keep watching them (still,", "covered) and go on to the next."], ["Comprueba que respira y que no", "hay hemorragias ni heridas graves.", "Vigílale (quieto, tapado) y", "pasa al siguiente herido."])))
    p.append(arrow(226, 112, 160, 150, SLATE, 2.5, 9) + txt(170, 124, L(lang, "yes", "sí"), 12, 800, TEAL))
    p.append(bx(272, 152, 434, 58, "#fff", L(lang, "NO — unconscious: ABC", "NO: inconsciente → regla ABC"),
                L(lang, ["A · Airway: head-tilt, chin-lift; remove anything in the mouth."], ["A · Vía aérea: maniobra frente-mentón; saca lo que obstruya."]), INK, INK))
    p.append(arrow(420, 116, 470, 150, SLATE, 2.5, 9) + txt(452, 130, "no", 12, 800, RED))
    p.append(bx(272, 226, 434, 44, "#fff", L(lang, "B · Is the person breathing? See · feel · hear", "B · ¿Respira? Ver · sentir · oír"), [], INK, INK))
    p.append(arrow(490, 210, 490, 224, SLATE, 2.5, 8))
    p.append(bx(272, 290, 206, 74, TEAL, L(lang, "Breathing", "Respira"), L(lang, ["Recovery position (PLS);", "check the breathing", "every 2–3 minutes."], ["Posición lateral de", "seguridad (PLS); revisa", "cada 2–3 minutos."])))
    p.append(bx(500, 290, 206, 74, RED, L(lang, "Not breathing", "No respira"), L(lang, ["C · cardio-respiratory", "arrest: start CPR now", "(30 compressions : 2)."], ["C · parada cardio-", "respiratoria: RCP ya", "(30 compresiones : 2)."])))
    p.append(arrow(380, 270, 380, 288, SLATE, 2.5, 8) + arrow(600, 270, 600, 288, SLATE, 2.5, 8))
    p.append(txt(392, 284, L(lang, "yes", "sí"), 11.5, 800, TEAL) + txt(612, 284, "no", 11.5, 800, RED))
    return svg(720, 372, "".join(p), L(lang, "Initial assessment of the injured", "Valoración inicial de los heridos"))


# ---------------------------------------------------------------- D5 opening the airway and checking breathing
def airway(lang):
    g = 214
    p = [rect(10, 10, 400, 236, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'), line(24, g, 396, g, SLATE, 2)]
    # body lying on its back, head on the left, chin tilted up
    p.append(rect(214, g - 50, 178, 50, CLOTH, 16) + rect(186, g - 44, 40, 30, SKIN, 8))
    p.append(f'<path d="M150 {g - 4} C 112 {g - 4} 98 {g - 40} 108 {g - 66} C 114 {g - 80} 124 {g - 86} 134 {g - 88} L 142 {g - 92} L 150 {g - 106} '
             f'L 158 {g - 94} L 166 {g - 92} L 170 {g - 88} L 184 {g - 86} C 196 {g - 82} 202 {g - 70} 204 {g - 56} L 212 {g - 40} L 204 {g - 8} Z" fill="{SKIN}"/>')
    p.append(f'<path d="M150 {g - 4} C 112 {g - 4} 98 {g - 40} 108 {g - 66} C 112 {g - 74} 116 {g - 78} 120 {g - 80} C 112 {g - 50} 124 {g - 22} 150 {g - 12} Z" fill="#6b4f3a"/>')
    p.append(f'<ellipse cx="164" cy="{g - 50}" rx="7" ry="10" fill="#c79a6e"/><circle cx="144" cy="{g - 80}" r="3" fill="{INK}"/>')
    p.append(f'<path d="M 170 {g - 86} C 180 {g - 74} 190 {g - 60} 204 {g - 44}" fill="none" stroke="#7dd3fc" stroke-width="6" stroke-linecap="round"/>')
    # rescuer's hands: one on the forehead pushing back, two fingers lifting the chin
    p.append(rot(rect(104, g - 104, 50, 18, "#c79a6e", 8), -28, 129, g - 95) + arrow(104, g - 112, 82, g - 92, NAVY, 2.5, 9))
    p.append(limb(192, g - 70, 214, g - 96, 7, "#c79a6e") + arrow(226, g - 74, 214, g - 108, NAVY, 2.5, 9))
    p.append(lines(24, 32, L(lang, ["1 · Hand on the forehead:", "tilt the head back"], ["1 · Una mano en la frente:", "empuja hacia atrás"]), 11.5, 700, INK, "start", 14))
    p.append(lines(244, 32, L(lang, ["2 · Fingers under the chin:", "lift it"], ["2 · Dedos bajo el mentón:", "elévalo"]), 11.5, 700, INK, "start", 14))
    p.append(txt(210, 236, L(lang, "The tongue moves forward and the airway opens", "La lengua se separa y se abre la vía aérea"), 11, 600, "#0369a1", "middle"))
    # checking breathing
    p.append(txt(434, 34, L(lang, "B · Is the person breathing?", "B · ¿Respira?"), 14, 800, INK))
    rows = [
        (L(lang, "SEE", "VER"), L(lang, ["the chest or belly rise", "with each breath"], ["si el pecho o el abdomen", "se mueven al respirar"])),
        (L(lang, "FEEL", "SENTIR"), L(lang, ["the air from the mouth or", "nose on your cheek"], ["el aire de la boca o la", "nariz en tu mejilla"])),
        (L(lang, "HEAR", "OÍR"), L(lang, ["the air going in and out", "of the mouth and nose"], ["la entrada y salida de aire", "por la boca y la nariz"])),
    ]
    for i, (t, b) in enumerate(rows):
        y = 52 + i * 64
        p.append(card(430, y, 280, 54, NAVY) + txt(448, y + 33, t, 15, 800, NAVY) + lines(524, y + 23, b, 11, 500, INK, "start", 14))
    p.append(lines(434, 252, L(lang, ["Noisy, snoring breathing: airway partly blocked.", "Irregular, gasping: possible serious brain damage."], ["Ruidosa, con ronquidos: vía aérea obstruida en parte.", "Irregular o entrecortada: posible daño cerebral grave."]), 10.5, 600, RED, "start", 14))
    return svg(720, 282, "".join(p), L(lang, "Opening the airway and checking breathing", "Abrir la vía aérea y comprobar la respiración"))


# ---------------------------------------------------------------- D6 recovery position (PLS) in three steps
def recovery_position(lang):
    p = []
    caps = [L(lang, ["1 · Raise the arm nearest", "to you (the head will", "rest on it)."], ["1 · Sube el brazo más", "cercano a ti (ahí apoyará", "la cabeza)."]),
            L(lang, ["2 · Bend the far arm and the", "far leg; roll the person", "towards you, all in one go."], ["2 · Dobla el brazo más alejado", "y la pierna del mismo lado;", "gíralo hacia ti a la vez."]),
            L(lang, ["3 · On their side, top leg", "bent, head resting on the", "raised arm."], ["3 · De lado, con la pierna", "flexionada y la cabeza sobre", "el brazo que subiste."])]
    for i in range(3):
        ox = 8 + i * 238
        p.append(rect(ox, 8, 226, 252, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'))
        p.append(txt(ox + 113, 164, L(lang, "you are here ↓", "tú, aquí ↓"), 10, 600, MUTED, "middle"))
        p.append(lines(ox + 14, 196, caps[i], 11, 600, INK, "start", 15))
    ARM = "#a5b4c8"
    # 1 · on the back, near arm raised past the head
    o = 8
    p.append(limb(o + 66, 98, o + 150, 98, 26) + limb(o + 150, 90, o + 208, 86, 10, DARK) + limb(o + 150, 106, o + 208, 112, 10, DARK)
             + limb(o + 72, 84, o + 140, 80, 8, ARM) + limb(o + 74, 114, o + 14, 118, 8, ARM) + head(o + 46, 98, 14))
    p.append(f'<circle cx="{o + 14}" cy="118" r="9" fill="none" stroke="{TEAL}" stroke-width="2.5"/>')
    # 2 · far arm across the chest, far knee bent, roll arrow
    o = 246
    p.append(limb(o + 66, 98, o + 150, 98, 26) + limb(o + 150, 106, o + 208, 112, 10, DARK) + poly([(o + 150, 90), (o + 176, 66), (o + 200, 84)], 10, DARK)
             + poly([(o + 72, 84), (o + 104, 86), (o + 86, 106)], 8, ARM) + limb(o + 74, 114, o + 14, 118, 8, ARM) + head(o + 46, 98, 14))
    p.append(f'<path d="M{o + 96} 56 C {o + 136} 50 {o + 146} 118 {o + 116} 140" fill="none" stroke="{TEAL}" stroke-width="2.5"/>'
             + arrow(o + 124, 132, o + 112, 144, TEAL, 2.5, 9))
    # 3 · lying on the side
    o = 484
    p.append(limb(o + 22, 114, o + 84, 112, 8, ARM) + head(o + 44, 98, 14) + limb(o + 62, 100, o + 146, 96, 26)
             + limb(o + 146, 90, o + 208, 84, 10, DARK) + poly([(o + 146, 104), (o + 172, 132), (o + 204, 124)], 10, DARK)
             + poly([(o + 74, 90), (o + 94, 72), (o + 66, 74)], 8, ARM))
    return svg(720, 268, "".join(p), L(lang, "The recovery position in three steps", "La posición lateral de seguridad en tres pasos"))


# ---------------------------------------------------------------- D7 CPR
def cpr(lang):
    g = 230
    p = [rect(10, 10, 384, 260, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'), line(24, g, 380, g, SLATE, 2)]
    p.append(rect(116, g - 50, 240, 50, CLOTH, 18) + head(92, g - 24, 22))
    # rescuer: straight arms from the shoulders, hands on the centre of the chest
    p.append(head(230, 44, 14) + rect(204, 60, 52, 34, "#475569", 10))
    p.append(limb(214, 86, 222, g - 58, 9, "#475569") + limb(246, 86, 238, g - 58, 9, "#475569"))
    p.append(rect(212, g - 62, 36, 12, "#c79a6e", 5))
    p.append(arrow(200, g - 66, 200, g - 40, RED, 2.5, 8) + arrow(200, g - 40, 200, g - 66, RED, 2.5, 8))
    p.append(lines(190, g - 104, L(lang, ["Push down", "4–5 cm (course);", "5–6 cm (current", "guidelines)"], ["Hundir", "4–5 cm (curso);", "5–6 cm (guías", "actuales)"]), 10.5, 700, RED, "end", 13))
    p.append(lines(24, 32, L(lang, ["Heel of the hand on the", "centre of the chest, the", "other on top, fingers", "interlaced."], ["Talón de la mano en el", "centro del pecho, el de", "la otra encima, dedos", "entrelazados."]), 11, 600, INK, "start", 14))
    p.append(lines(276, 32, L(lang, ["Arms straight:", "push with your", "body weight."], ["Brazos rectos:", "empuja con el", "peso del cuerpo."]), 11, 600, INK, "start", 14))
    p.append(txt(200, 256, L(lang, "On a flat, hard surface, face up. Let the chest come back up each time.", "Boca arriba, en superficie plana y dura. Deja que el pecho vuelva a subir."), 10.5, 600, SLATE, "middle"))
    # the cycle
    cx, cy, r = 540, 112, 70
    p.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{LINE}" stroke-width="10"/>')
    p.append(f'<path d="M{cx - r} {cy} A{r} {r} 0 0 1 {cx + r} {cy}" fill="none" stroke="{NAVY}" stroke-width="10"/>' + arrow(cx + r, cy - 4, cx + r, cy + 14, NAVY, 3, 14))
    p.append(f'<path d="M{cx + r} {cy + 2} A{r} {r} 0 0 1 {cx - r} {cy + 2}" fill="none" stroke="{TEAL}" stroke-width="10"/>' + arrow(cx - r, cy + 4, cx - r, cy - 14, TEAL, 3, 14))
    p.append(txt(cx, cy - r - 14, L(lang, "30 compressions", "30 compresiones"), 13.5, 800, NAVY, "middle") + txt(cx, cy + r + 24, L(lang, "2 breaths", "2 ventilaciones"), 13.5, 800, TEAL, "middle"))
    p.append(lines(cx, cy - 6, L(lang, ["repeat until", "help arrives or", "the person reacts"], ["repetir hasta que", "llegue la ayuda o", "el herido reaccione"]), 10.5, 600, INK, "middle", 13))
    p.append(lines(414, 228, L(lang, ["About 100 a minute (guidelines: 100–120); swap rescuers", "every 1–2 min. Children: 5 breaths first, then 30 : 2,", "with one hand — two fingers for a baby."],
                                ["Unas 100 por minuto (guías: 100–120); turnarse cada", "1–2 min. Niños: 5 ventilaciones iniciales y luego 30 : 2,", "con una mano; con dos dedos en bebés."]), 10.5, 600, INK, "start", 14))
    return svg(720, 280, "".join(p), L(lang, "Cardiopulmonary resuscitation", "Reanimación cardiopulmonar"))


# ---------------------------------------------------------------- D8 external bleeding
def bleeding(lang):
    cx = 150
    p = [rect(10, 10, 300, 330, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"')]
    p.append(head(cx, 44, 18) + rect(cx - 6, 60, 12, 10, SKIN, 3) + rect(cx - 30, 68, 60, 100, CLOTH, 14))
    p.append(limb(cx - 28, 78, cx - 50, 160, 13) + limb(cx - 50, 160, cx - 56, 196, 10, SKIN))
    p.append(limb(cx + 28, 78, cx + 50, 160, 13) + limb(cx + 50, 160, cx + 58, 194, 10, SKIN))
    p.append(limb(cx - 16, 166, cx - 22, 312, 16, DARK) + limb(cx + 16, 166, cx + 22, 312, 16, DARK))
    # arm wound with gauze, armpit point; leg wound with tourniquet above, groin point
    p.append(rect(cx + 44, 140, 18, 16, "#fff", 3, f' stroke="{BLOOD}" stroke-width="1.5"') + f'<circle cx="{cx + 53}" cy="148" r="4" fill="{BLOOD}"/>')
    p.append(f'<circle cx="{cx + 30}" cy="84" r="7" fill="none" stroke="{NAVY}" stroke-width="3"/>')
    p.append(f'<circle cx="{cx - 21}" cy="270" r="5" fill="{BLOOD}"/>' + rect(cx - 33, 218, 24, 8, AMBER, 2))
    p.append(f'<circle cx="{cx - 14}" cy="174" r="7" fill="none" stroke="{NAVY}" stroke-width="3"/>')
    p.append(line(cx + 38, 84, 236, 70, NAVY, 1.2) + lines(240, 64, L(lang, ["armpit"], ["axila"]), 11, 700, NAVY, "start", 13))
    p.append(line(cx + 64, 148, 236, 148, BLOOD, 1.2) + lines(240, 144, L(lang, ["wound +", "gauze"], ["herida +", "gasa"]), 11, 700, BLOOD, "start", 13))
    p.append(line(cx - 22, 174, 44, 200, NAVY, 1.2) + lines(24, 212, L(lang, ["groin"], ["ingle"]), 11, 700, NAVY, "start", 13))
    p.append(line(cx - 34, 222, 44, 252, AMBER, 1.2) + lines(24, 264, L(lang, ["tourniquet", "+ time"], ["torniquete", "+ hora"]), 11, 700, AMBER, "start", 13))
    steps = [
        (1, NAVY, L(lang, ["Press hard on the wound with gauze or a", "clean cloth. If it soaks through, put more", "on top — never take the first one off."],
                    ["Presiona sobre la herida con una gasa o un", "trozo de tela limpia. Si se empapa, pon otra", "encima sin retirar la anterior."])),
        (2, NAVY, L(lang, ["Still bleeding? Your course: raise the limb", "and keep pressing in the armpit (arm) or", "the groin (leg), where the main artery runs."],
                    ["¿Sigue sangrando? Tu curso: eleva el miembro", "y presiona en la axila (brazo) o en la ingle", "(pierna), donde pasa la arteria."])),
        (3, AMBER, L(lang, ["Last resort (amputation, very serious", "bleeding): a tourniquet above the wound.", "Don’t loosen it, leave it visible, write", "down the time for the medical team."],
                     ["Último recurso (amputación, hemorragia muy", "grave): torniquete por encima de la herida.", "No aflojarlo, dejarlo visible y anotar la", "hora para los sanitarios."])),
    ]
    y = 34
    for n, col, body in steps:
        h = 24 + 15 * len(body)
        p.append(card(326, y, 384, h, col) + badge(348, y + 22, n, col) + lines(368, y + 26, body, 11, 500, INK, "start", 15))
        y += h + 12
    return svg(720, 350, "".join(p), L(lang, "Controlling external bleeding", "Cómo contener una hemorragia externa"))


# ---------------------------------------------------------------- D9 shock
def shock(lang):
    g = 170
    p = [rect(10, 10, 360, 196, CARD, 12, f' stroke="{LINE}" stroke-width="1.5"'), line(24, g, 356, g, SLATE, 2)]
    p.append(rect(258, g - 46, 70, 46, "#cbd5e1", 6))
    p.append(head(54, g - 16, 16) + limb(72, g - 16, 186, g - 18, 26) + limb(186, g - 20, 300, g - 56, 12, DARK) + limb(186, g - 12, 300, g - 48, 12, DARK))
    p.append(rect(90, g - 40, 90, 14, "#93c5fd", 6, ' opacity="0.9"'))
    p.append(arrow(320, g - 64, 320, g - 96, NAVY, 2.5, 9) + lines(206, 40, L(lang, ["Legs raised: the head", "lower than the body"], ["Piernas elevadas: la cabeza", "más baja que el cuerpo"]), 11.5, 700, INK, "start", 15))
    p.append(lines(24, 40, L(lang, ["Light cover —", "don’t make them sweat"], ["Abrigo ligero,", "sin hacerle sudar"]), 11, 600, "#0369a1", "start", 14))
    p.append(txt(190, 194, L(lang, "Loosen tight clothing. Nothing to drink.", "Aflojar la ropa que oprima. No dar bebidas."), 11, 600, SLATE, "middle"))
    p.append(card(386, 14, 324, 190, RED) + txt(406, 42, L(lang, "Signs of shock", "Síntomas del shock"), 14, 800, RED))
    signs = L(lang, ["Cold sweat", "Pale skin", "Confusion, restlessness", "Fast, shallow breathing", "Fast, weak pulse"],
              ["Sudor frío", "Piel pálida", "Confusión, inquietud", "Respiración rápida y superficial", "Pulso rápido y débil"])
    for i, s in enumerate(signs):
        p.append(f'<circle cx="412" cy="{66 + i * 26}" r="4" fill="{RED}"/>' + txt(424, 70 + i * 26, s, 12, 600, INK))
    p.append(txt(406, 196, L(lang, "Cause: a major loss of blood.", "Causa: una pérdida importante de sangre."), 10.5, 600, MUTED))
    return svg(720, 214, "".join(p), L(lang, "Shock and the anti-shock position", "El shock y la posición antishock"))
