# -*- coding: utf-8 -*-
"""Original SVG diagrams for Category A1/A2, Topic 10 (accidents and their factors), EN/ES. No third-party artwork
is used. Four figures are drawn for riders; two (alcohol curve, drowsiness clock) are shared with Category B, Topic 10."""

from svgkit import NAVY, TEAL, AMBER, RED, SLATE, INK, svg, txt, lines  # noqa: F401
from ..b02.diagrams import rect, tick, cross, ASPHALT, WHITE
from ..b09.diagrams import L, line, MUTED, LINE, CARD
from ..b10.diagrams import arrow, rot
from ..b10.diagrams import bac_curve, drowsy_clock  # noqa: F401  (shared with Topic B10)
from ..b08 import signs as S

GOOD = "#0b7548"
SKIN = "#f1c9a5"
SHELL = "#facc15"
VISOR = "#1e3a5f"
STEEL = "#94a3b8"
STEEL_D = "#64748b"


# ---------------------------------------------------------------- D1 stopping distance on a motorcycle
def stop_moto(lang):
    xs, xe, xp, gy = 86, 336, 590, 104
    p = [line(30, gy, 700, gy, SLATE, 2)]
    steps = [(xs, L(lang, "1 · Sees the danger", "1 · Ve el peligro")), (xe, L(lang, "2 · Brakes", "2 · Frena")), (xp, L(lang, "3 · Stops", "3 · Se detiene"))]
    for x, lab in steps:
        p.append(txt(x, 20, lab, 12.5, 700, INK, "middle") + line(x, 88, x, 208, MUTED, 1, "4 3"))
        p.append(S.at(S.moto(NAVY), x - 14, gy - 12, 1.25))
    p.append(S.at(S.standing(INK), 652, gy - 21, 1.0))
    p.append(line(xs, 46, xe, 46, AMBER, 2) + line(xs, 40, xs, 52, AMBER, 2) + line(xe, 40, xe, 52, AMBER, 2))
    p.append(txt((xs + xe) / 2, 40, L(lang, "reaction time ≈ 0.75 s", "tiempo de reacción ≈ 0,75 s"), 11, 600, INK, "middle"))
    p.append(rect(xs, 118, xe - xs, 28, TEAL, 4) + txt((xs + xe) / 2, 136.5, L(lang, "Reaction distance", "Distancia de reacción"), 12, 700, "#fff", "middle"))
    p.append(rect(xe + 2, 118, xp - xe - 2, 28, AMBER, 4) + txt((xe + xp) / 2, 136.5, L(lang, "Braking distance", "Distancia de frenado"), 12, 700, "#fff", "middle"))
    p.append(rect(xs, 154, xp - xs, 28, NAVY, 4) + txt((xs + xp) / 2, 172.5, L(lang, "Stopping distance = reaction + braking", "Distancia de detención = reacción + frenado"), 12, 700, "#fff", "middle"))
    p.append(txt(30, 232, L(lang, "Braking distance compared with a dry road", "Distancia de frenado comparada con la calzada seca"), 12, 700, INK))
    unit, bx = 46, 196
    for i, (lab, k) in enumerate([(L(lang, "Dry", "Seca"), 1), (L(lang, "Rain", "Lluvia"), 2), (L(lang, "Snow or ice", "Nieve o hielo"), 10)]):
        y = 246 + i * 24
        p.append(txt(bx - 10, y + 13, lab, 11.5, 600, INK, "end") + rect(bx, y + 2, unit * k, 16, AMBER, 3) + txt(bx + unit * k + 8, y + 14.5, f"×{k}", 12, 800, INK))
    p.append(txt(30, 330, L(lang, "A passenger or a heavy load also makes the braking distance longer.", "Un pasajero o una carga pesada también alargan la distancia de frenado."), 11, 600, SLATE))
    return svg(720, 340, "".join(p), L(lang, "Stopping distance on a motorcycle", "Distancia de detención en moto"))


# ---------------------------------------------------------------- D2 guardrail posts and the motorcyclist protection rail
def _beam(x, y, w):
    return rect(x, y, w, 22, STEEL, 3) + line(x, y + 8, x + w, y + 8, STEEL_D, 1.5) + line(x, y + 14, x + w, y + 14, STEEL_D, 1.5)


def guardrail_posts(lang):
    panels = [
        ("H", L(lang, "“H” profile post", "Poste de perfil en «H»"), False, L(lang, ["Sharp edges: a sliding", "rider can be cut badly"], ["Aristas cortantes: puede", "causar lesiones muy graves"])),
        ("C", L(lang, "“C” profile post", "Poste de perfil en «C»"), True, L(lang, ["Rounded: less", "aggressive on impact"], ["Redondeado: menos", "agresivo en el impacto"])),
        ("SPM", L(lang, "Motorcyclist protection", "Protección para motoristas"), True, L(lang, ["A lower rail covers the posts", "so a fallen rider slides past"], ["Una banda inferior tapa los postes", "y el motorista caído desliza"])),
    ]
    gy = 168
    p = []
    for i, (kind, title, ok, note) in enumerate(panels):
        x, w = 8 + i * 238, 228
        p.append(rect(x, 6, w, 286, CARD, 10, f' stroke="{LINE}" stroke-width="1.5"'))
        p.append(txt(x + w / 2, 28, title, 12.5, 800, INK, "middle"))
        p.append(rect(x + 1, gy, w - 2, 14, ASPHALT, 0))
        p.append(_beam(x + 14, 66, w - 28))
        for px in (x + 48, x + w - 64):
            p.append(rect(px, 76, 16, gy - 76, STEEL_D, 2))
        if kind == "SPM":
            p.append(rect(x + 14, 128, w - 28, 30, "#cbd5e1", 4, f' stroke="{STEEL_D}" stroke-width="1.5"'))
        # cross-section of the post, seen from above
        cx, cy = x + w / 2, 218
        p.append(txt(cx, 192, L(lang, "post seen from above", "poste visto desde arriba"), 10, 600, MUTED, "middle"))
        if kind == "H":
            p.append(f'<path d="M{cx - 14} {cy - 16} L{cx - 14} {cy + 16} M{cx + 14} {cy - 16} L{cx + 14} {cy + 16} M{cx - 14} {cy} L{cx + 14} {cy}" stroke="{INK}" stroke-width="5" fill="none"/>')
        else:
            p.append(f'<path d="M{cx + 14} {cy - 14} Q{cx - 22} {cy - 14} {cx - 18} {cy} Q{cx - 22} {cy + 14} {cx + 14} {cy + 14}" stroke="{INK}" stroke-width="5" fill="none" stroke-linecap="round"/>')
        p.append((tick if ok else cross)(x + 26, 254, 11))
        p.append(lines(x + 44, 250, note, 11, 700, GOOD if ok else RED, "start", 14))
    return svg(720, 298, "".join(p), L(lang, "Guardrail posts and a fallen rider", "Los postes del guardarraíl y el motorista caído"))


# ---------------------------------------------------------------- D3 helmet types
def _helmet(cx, cy, kind):
    """Side view of a head and helmet looking right."""
    out = f'<circle cx="{cx + 4}" cy="{cy + 4}" r="34" fill="{SKIN}"/>'
    dome = f"M{cx - 38} {cy + 26} Q{cx - 50} {cy - 26} {cx - 4} {cy - 40} Q{cx + 38} {cy - 44} {cx + 44} {cy - 4}"
    if kind == "jet":
        out += f'<path d="{dome} L{cx + 42} {cy + 4} L{cx + 16} {cy + 6} Q{cx + 2} {cy + 30} {cx - 14} {cy + 34} Z" fill="{SHELL}" stroke="#a16207" stroke-width="2"/>'
        out += f'<path d="M{cx + 18} {cy - 18} L{cx + 50} {cy - 16} L{cx + 50} {cy + 22} L{cx + 30} {cy + 22} Z" fill="#bfdbfe" opacity="0.55" stroke="#60a5fa" stroke-width="1.5"/>'
        return out
    chin = f"L{cx + 46} {cy + 30} Q{cx + 20} {cy + 46} {cx - 12} {cy + 40} Z"
    if kind == "integral":
        out += f'<path d="{dome} {chin}" fill="{SHELL}" stroke="#a16207" stroke-width="2"/>'
    else:  # modular: chin bar raised, dashed outline where it closes
        out += f'<path d="{dome} L{cx + 42} {cy + 6} L{cx + 16} {cy + 8} Q{cx + 2} {cy + 30} {cx - 14} {cy + 34} Z" fill="{SHELL}" stroke="#a16207" stroke-width="2"/>'
        out += f'<path d="M{cx + 16} {cy + 8} L{cx + 46} {cy + 8} L{cx + 46} {cy + 30} Q{cx + 20} {cy + 46} {cx - 12} {cy + 40}" fill="none" stroke="#a16207" stroke-width="1.5" stroke-dasharray="4 3"/>'
        out += f'<path d="M{cx - 2} {cy - 46} Q{cx + 30} {cy - 62} {cx + 52} {cy - 40} L{cx + 46} {cy - 30} Q{cx + 26} {cy - 48} {cx + 2} {cy - 36} Z" fill="{SHELL}" stroke="#a16207" stroke-width="2"/>'
    out += f'<path d="M{cx + 14} {cy - 16} L{cx + 46} {cy - 14} L{cx + 46} {cy + 8} L{cx + 16} {cy + 8} Z" fill="{VISOR}"/>'
    return out


def helmet_types(lang):
    cards = [
        ("integral", L(lang, "Full-face (integral)", "Integral"), L(lang, ["Covers the head, face", "and chin: the safest"], ["Cubre cabeza, cara", "y barbilla: el más seguro"]), GOOD),
        ("modular", L(lang, "Modular (flip-up)", "Modular"), L(lang, ["The chin bar lifts up;", "ride with it closed"], ["La mentonera se levanta;", "circula con ella cerrada"]), AMBER),
        ("jet", L(lang, "Open-face (jet)", "Jet"), L(lang, ["Does not cover the chin:", "less protection in a fall"], ["No cubre la barbilla:", "menos protección en caída"]), RED),
    ]
    p = []
    for i, (kind, title, note, col) in enumerate(cards):
        x, w = 8 + i * 238, 228
        p.append(rect(x, 6, w, 236, CARD, 10, f' stroke="{LINE}" stroke-width="1.5"'))
        p.append(txt(x + w / 2, 30, title, 13, 800, INK, "middle"))
        p.append(_helmet(x + w / 2 - 6, 116, kind))
        p.append(lines(x + w / 2, 200, note, 11.5, 700, col, "middle", 15))
    p.append(lines(360, 266, L(lang, ["Whatever the type: approved to UNECE R22 (label inside), the right size, fastened —",
                                       "and replaced after a crash or a hard knock, even if you see no damage."],
                                ["Sea del tipo que sea: homologado UNECE R22 (etiqueta interior), de tu talla y abrochado,",
                                 "y sustituido tras un accidente o un golpe fuerte, aunque no se vean daños."]), 11.5, 700, INK, "middle", 15))
    return svg(720, 292, "".join(p), L(lang, "Helmet types", "Tipos de casco"))


# ---------------------------------------------------------------- D4 crossing a low-grip patch upright
def _rear(cx, gy, lean):
    """Motorcycle and rider seen from behind, leaning `lean` degrees (negative = to the left)."""
    body = (rect(cx - 7, gy - 34, 14, 34, "#111827", 6) + rect(cx - 14, gy - 52, 28, 22, "#475569", 6)
            + rect(cx - 9, gy - 44, 18, 6, "#dc2626", 2) + rect(cx - 13, gy - 86, 26, 38, NAVY, 9)
            + f'<circle cx="{cx}" cy="{gy - 98}" r="13" fill="#e5e7eb" stroke="{INK}" stroke-width="1.5"/>'
            + line(cx - 24, gy - 70, cx + 24, gy - 70, "#111827", 4))
    return rot(body, lean, cx, gy) + f'<circle cx="{cx}" cy="{gy}" r="3.5" fill="{AMBER}"/>'


def upright_low_grip(lang):
    gy = 196
    p = [rect(0, gy, 720, 40, ASPHALT)]
    p.append(rect(286, gy + 4, 150, 30, "#e5e7eb", 3) + "".join(rect(296 + k * 26, gy + 8, 14, 22, WHITE, 2) for k in range(5)))
    p.append(txt(361, gy + 54, L(lang, "painted marking, manhole, rails, leaves, gravel…", "marca vial, tapa de alcantarilla, raíles, hojas, gravilla…"), 11, 600, SLATE, "middle"))
    for x, lean in ((120, -22), (361, 0), (600, -22)):
        p.append(_rear(x, gy, lean))
    labs = [(120, L(lang, ["1 · Before it: slow down", "while still on good grip"], ["1 · Antes: reduce la velocidad", "mientras aún hay adherencia"])),
            (361, L(lang, ["2 · On it: upright,", "no braking, no hard throttle"], ["2 · Encima: recta,", "sin frenar ni acelerar fuerte"])),
            (600, L(lang, ["3 · Past it: lean again", "and carry on"], ["3 · Después: vuelve a", "inclinar y continúa"]))]
    for x, lab in labs:
        p.append(lines(x, 22, lab, 11.5, 700, INK, "middle", 15))
    p.append(arrow(190, 70, 290, 70, MUTED, 2, 9) + arrow(432, 70, 532, 70, MUTED, 2, 9))
    return svg(720, gy + 64, "".join(p), L(lang, "Crossing a low-grip patch", "Pasar por una zona de baja adherencia"))
