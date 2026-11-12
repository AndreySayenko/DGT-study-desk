# -*- coding: utf-8 -*-
"""Small, original drawings of Spanish traffic signs, lights, devices and road markings for Topic 8's tables.

Each icon is a standalone inline SVG (no ids, no external artwork), simplified from the official designs in the
Catálogo oficial de señales de circulación (RD 465/2025). ICON maps a code such as "P-1" or "R-101" to its SVG.
Pictograms are drawn centred on (0, 0) and placed with at()."""
import math

RED = "#d7191f"
BLUE = "#1447c8"
YEL = "#ffd200"
K = "#111111"
W = "#ffffff"
GREEN = "#0b7a3b"
ORANGE = "#f08a00"
BROWN = "#7b4a22"
GRAY = "#8a8f98"
ASPH = "#4b5563"
FONT = "Arial, 'Liberation Sans', 'DejaVu Sans', sans-serif"

ICON = {}


def ico(inner, w=100, h=100, px=48, label=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{round(px * w / 100)}" height="{round(px * h / 100)}" '
            f'role="img" aria-label="{label}" style="display:block;margin:2px auto;font-family:{FONT}">{inner}</svg>')


def add(code, inner, w=100, h=100, px=48):
    ICON[code] = ico(inner, w, h, px, code)


def t(x, y, s, size, fill=K, weight=700, anchor="middle", extra=""):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{extra}>{s}</text>'


def at(inner, x, y, s=1.0, rot=0, fx=False):
    tr = f"translate({x} {y})"
    if rot:
        tr += f" rotate({rot})"
    if s != 1 or fx:
        tr += f" scale({-s if fx else s} {s})"
    return f'<g transform="{tr}">{inner}</g>'


def ln(x1, y1, x2, y2, c=K, w=2, cap="round", extra=""):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}" stroke-linecap="{cap}"{extra}/>'


def pth(d, c=K, w=None, fill=None, join="round", cap="round"):
    if w is None:
        return f'<path d="{d}" fill="{fill or c}"/>'
    return f'<path d="{d}" fill="{fill or "none"}" stroke="{c}" stroke-width="{w}" stroke-linejoin="{join}" stroke-linecap="{cap}"/>'


def rc(x, y, w, h, fill, rx=0, stroke=None, sw=1):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{s}/>'


def ci(cx, cy, r, fill, stroke=None, sw=1):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{s}/>'


def head(x2, y2, fx, fy, c, hl, hw):
    dx, dy = x2 - fx, y2 - fy
    L = math.hypot(dx, dy) or 1
    ux, uy = dx / L, dy / L
    bx, by = x2 - ux * hl, y2 - uy * hl
    px, py = -uy, ux
    return f'<path d="M{x2:.1f} {y2:.1f} L{bx + px * hw:.1f} {by + py * hw:.1f} L{bx - px * hw:.1f} {by - py * hw:.1f} Z" fill="{c}"/>'


def arr(pts, c=K, w=6, hl=None, hw=None):
    """Polyline arrow through pts [(x, y), ...]; the head sits on the last point."""
    hl = hl or w * 2.1
    hw = hw or w * 1.6
    (fx, fy), (x2, y2) = pts[-2], pts[-1]
    L = math.hypot(x2 - fx, y2 - fy) or 1
    ex, ey = x2 - (x2 - fx) / L * (hl * 0.8), y2 - (y2 - fy) / L * (hl * 0.8)
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts[:-1] + [(ex, ey)])
    return pth(d, c, w, cap="butt") + head(x2, y2, fx, fy, c, hl, hw)


def carr(d, end, ctrl, c=K, w=6, hl=None, hw=None):
    """Curved arrow: path d must stop short of `end`; the head points from `ctrl` to `end`."""
    hl = hl or w * 2.1
    hw = hw or w * 1.6
    return pth(d, c, w, cap="butt") + head(end[0], end[1], ctrl[0], ctrl[1], c, hl, hw)


# ------------------------------------------------------------------------------------------ sign frames
def warn(inner, bg=W):
    return f'<path d="M50 10 L93 87 L7 87 Z" fill="{bg}" stroke="{RED}" stroke-width="9" stroke-linejoin="round"/>' + inner


def prohib(inner="", bg=W):
    return ci(50, 50, 42, bg, RED, 12) + inner


def oblig(inner=""):
    return ci(50, 50, 46, BLUE, W, 2.5) + inner


def bar_red():
    """Red diagonal of prohibition signs such as 'no right turn' (top left to bottom right)."""
    return ln(22, 22, 78, 78, RED, 8, "butt")


def stripes(n=5, gap=4.4, r=43, c=K, w=1.5):
    out = []
    for i in range(n):
        d = (i - (n - 1) / 2) * gap
        h = math.sqrt(r * r - d * d)
        cx, cy = 50 + 0.7071 * d, 50 + 0.7071 * d
        out.append(ln(round(cx - 0.7071 * h, 1), round(cy + 0.7071 * h, 1), round(cx + 0.7071 * h, 1), round(cy - 0.7071 * h, 1), c, w, "butt"))
    return "".join(out)


def endsig(inner="", n=5):
    return ci(50, 50, 45, W, K, 2.5) + inner + stripes(n)


def end_blue(inner):
    return oblig(inner) + ln(19, 81, 81, 19, RED, 9, "butt")


def brect(inner, w=100, h=130, fill=BLUE, edge=W):
    return rc(2, 2, w - 4, h - 4, fill, 7, edge, 2.5) + inner


def end_rect(w=100, h=130):
    return ln(8, h - 8, w - 8, 8, RED, 9, "butt")


def wrect(inner, w=100, h=60, sw=4):
    return rc(3, 3, w - 6, h - 6, W, 8, K, sw) + inner


# ------------------------------------------------------------------------------------------ pictograms (centred on 0,0)
def car_front(c=K, bg=W):
    return (pth("M-13 -4 L-9 -13 Q-8 -15 -5 -15 L5 -15 Q8 -15 9 -13 L13 -4 Z", c) + rc(-20, -5, 40, 13, c, 3)
            + pth("M-10 -5 L-7 -12 L7 -12 L10 -5 Z", bg) + rc(-18, 7, 8, 8, c, 1.5) + rc(10, 7, 8, 8, c, 1.5)
            + ci(-13, 1.5, 2.6, bg) + ci(13, 1.5, 2.6, bg))


def car_side(c=K, bg=W):
    return (pth("M-20 6 L-20 1 Q-20 -1 -17 -1.5 L-10 -2.5 L-5 -8 Q-4 -9 -2 -9 L9 -9 Q11 -9 12 -7.5 L16 -2.5 L20 -1.5 Q22 -1 22 1 L22 6 Z", c)
            + pth("M-3.5 -7.5 L8.5 -7.5 L11 -3 L-6.5 -3 Z", bg) + ln(2.5, -7.5, 2.5, -3, c, 1.5)
            + ci(-11, 6, 4.5, c) + ci(13, 6, 4.5, c) + ci(-11, 6, 1.7, bg) + ci(13, 6, 1.7, bg))


def truck(c=K, bg=W, load=""):
    out = (rc(-22, -12, 29, 17, c, 1) + pth("M8 -7 L16 -7 L21 -1 L21 5 L8 5 Z", c) + pth("M10 -5 L15 -5 L18.5 -1 L10 -1 Z", bg)
           + rc(-22, 4, 43, 3, c) + "".join(ci(x, 8, 3.8, c) + ci(x, 8, 1.4, bg) for x in (-15, -7, 14)))
    if load:
        out += t(-7.5, -0.5, load, 9.5, bg)
    return out


def moto(c=K, bg=W):
    return (ci(-14, 8, 6.5, "none", c, 2.6) + ci(14, 8, 6.5, "none", c, 2.6) + pth("M-14 8 L-6 1 L6 1 L14 8", c, 2.4)
            + pth("M-8 0 L8 0 L11 -4 L-2 -4 Z", c) + ln(14, 8, 10, -6, c, 2.6) + ci(1, -11.5, 3.6, c)
            + pth("M0 -8 L-4 -1", c, 4.2) + pth("M0 -7 L9 -5", c, 2.6) + pth("M-4 -1 L3 2 L2 7", c, 3))


def moped(c=K, bg=W):
    return (ci(-13, 7, 6, "none", c, 2.4) + ci(13, 7, 6, "none", c, 2.4) + pth("M-20 5 A8 8 0 0 1 -5 1", c, 2.2)
            + pth("M-17 -1 L-4 -1 L1 6 L-9 6 Z", c) + rc(-16, -6, 11, 3.5, c, 1.5) + ln(13, 7, 9, -11, c, 2.4)
            + ln(6, -11, 12, -11, c, 2.4) + ln(0, 5, 9, -3, c, 3))


def bike(c=K, bg=W):
    return (ci(-13, 5, 7.5, "none", c, 2.3) + ci(13, 5, 7.5, "none", c, 2.3)
            + pth("M-13 5 L-5 -5 L8 -5 L13 5 M-5 -5 L0 5 L8 -5 M-13 5 L0 5", c, 2.3)
            + ln(-8, -8, -2, -8, c, 2.6) + ln(-5, -8, -5, -5, c, 2) + pth("M8 -5 L6 -10 L11 -10", c, 2.3))


def cyclist(c=K, bg=W):
    return at(bike(c, bg) + ci(1, -21, 3.6, c) + pth("M0 -17 L-5 -9", c, 4) + pth("M0 -16 L7 -10", c, 2.4) + pth("M-5 -9 L0 -2 L0 4", c, 2.8), 0, 6)


def ped(c=K, bg=W):
    return (ci(2, -17, 4.3, c) + pth("M1 -11 L-1 3", c, 5.5) + pth("M-1 3 L-7 20 M-1 3 L6 11 L8 20", c, 4.2)
            + pth("M1 -9 L-6 0 M1 -9 L7 -1", c, 3.4))


def standing(c=K, bg=W):
    return (ci(0, -17, 4.3, c) + rc(-5, -11, 10, 14, c, 3) + rc(-5, 2, 4, 18, c, 1.5) + rc(1, 2, 4, 18, c, 1.5)
            + rc(-8, -10, 3, 13, c, 1.5) + rc(5, -10, 3, 13, c, 1.5))


def horse(c=K, bg=W):
    return (rc(-15, -4, 24, 9, c, 4) + pth("M5 -3 L11 -15 L15 -14 L11 -2 Z", c) + pth("M11 -15 L19 -12 L18 -9 L13 -10 Z", c)
            + pth("M-12 4 L-13 15 M-8 4 L-8 15 M3 4 L4 15 M7 4 L9 15", c, 2.4) + pth("M-15 -2 Q-20 1 -19 9", c, 2))


def rider(c=K, bg=W):
    return horse(c, bg) + ci(-3, -17, 3.2, c) + pth("M-3 -14 L-3 -5", c, 3.6) + pth("M-3 -5 L0 1", c, 2.6) + pth("M-3 -11 L6 -8", c, 2)


def cart(c=K, bg=W):
    return (at(horse(c, bg), 10, 0, 0.8) + rc(-25, -9, 17, 7, c, 1) + ci(-17, 3, 5.5, "none", c, 2.2) + ln(-8, -6, 0, -2, c, 2)
            + ci(-18, -14, 2.6, c) + ln(-18, -12, -18, -9, c, 3))


def tractor(c=K, bg=W):
    return (ci(-10, 6, 9, c) + ci(-10, 6, 3.2, bg) + ci(14, 10, 5.5, c) + ci(14, 10, 2, bg) + rc(-3, -2, 22, 8, c, 1.5)
            + pth("M-16 -2 L-14 -15 L-2 -15 L-2 -2", c, 2.6) + rc(-10, -6, 6, 3, c) + ln(12, -2, 12, -10, c, 2))


def handcart(c=K, bg=W):
    return (ci(-14, 6, 5.5, "none", c, 2.2) + ln(-24, 0, -4, 0, c, 3) + ln(-4, 0, 5, -4, c, 2.2) + at(ped(c, bg), 13, 0, 0.75, 12))


def vmp(c=K, bg=W):
    return (ci(-10, 13, 4.5, "none", c, 2.2) + ci(10, 13, 4.5, "none", c, 2.2) + ln(-10, 11, 6, 11, c, 3) + ln(9, 12, 5, -14, c, 2.6)
            + ln(1, -14, 9, -14, c, 2.6) + pth("M12 -6 L17 -6 M14.5 -6 L14.5 -1 M13 -9 L13 -6 M16 -9 L16 -6", c, 1.4))


def tram(c=K, bg=W):
    return (rc(-20, -6, 40, 15, c, 3) + "".join(rc(x, -3, 7, 5, bg, 1) for x in (-17, -8, 1, 10))
            + pth("M-6 -6 L0 -13 L6 -6", c, 1.6) + ln(-8, -13, 8, -13, c, 1.6) + ci(-12, 10, 2.4, c) + ci(12, 10, 2.4, c) + ln(-22, 13.5, 22, 13.5, c, 1.6))


def train(c=K, bg=W):
    return (rc(-12, -17, 24, 28, c, 6) + rc(-8, -12, 16, 9, bg, 2) + ci(-6, 4, 2.2, bg) + ci(6, 4, 2.2, bg)
            + pth("M-12 10 L-15 16 L15 16 L12 10 Z", c))


def bus(c=K, bg=W):
    return (rc(-25, -9, 50, 15, c, 2) + "".join(rc(-22 + i * 7.5, -7, 6, 6, bg, 1) for i in range(6))
            + ci(-15, 7, 3.4, c) + ci(15, 7, 3.4, c) + ci(-15, 7, 1.3, bg) + ci(15, 7, 1.3, bg))


def plane(c=K):
    return pth("M-18 0 L-6 -2 L2 -14 L6 -14 L2 -2 L14 -2 L18 -8 L20 -8 L18 0 L20 8 L18 8 L14 2 L2 2 L6 14 L2 14 L-6 2 Z", c)


def cow(c=K, bg=W):
    return (rc(-16, -7, 28, 13, c, 4) + pth("M12 -7 L21 -5 L21 1 L14 2 Z", c) + pth("M14 -7 L13 -11 M18 -6 L19 -10", c, 1.6)
            + pth("M-13 5 L-13 14 M-9 5 L-9 14 M5 5 L5 14 M9 5 L9 14", c, 2.6) + pth("M-16 -5 Q-21 -2 -20 6", c, 1.6))


def deer(c=K, bg=W):
    return (f'<ellipse cx="0" cy="0" rx="13" ry="5" transform="rotate(14)" fill="{c}"/>'
            + pth("M-9 -3 L-15 -12 L-12 -14 L-6 -5 Z", c) + f'<ellipse cx="-17" cy="-13" rx="4.5" ry="2.6" transform="rotate(-15 -17 -13)" fill="{c}"/>'
            + pth("M-15 -15 L-14 -21 M-14.5 -18 L-11 -20 M-17 -15 L-20 -20", c, 1.5)
            + pth("M-8 1 L-17 2 L-15 8 M-6 3 L-12 8 L-10 12", c, 2.2) + pth("M9 3 L21 8 M8 4 L17 13", c, 2.2) + pth("M12 0 L16 -4", c, 2))


def boar(c=K, bg=W):
    return (pth("M-12 -6 Q0 -12 14 -5 Q18 0 14 6 L-10 6 Q-15 3 -12 -6 Z", c) + pth("M-12 -6 L-21 0 L-21 3 L-12 5 Z", c)
            + pth("M-10 -7 L-8 -11 L-6 -7 Z", c) + pth("M-8 5 L-8 11 M-3 6 L-3 11 M8 6 L8 11 M12 5 L12 11", c, 2.6)
            + pth("M-18 1 L-16 -1", bg, 1) + pth("M14 -3 L18 -6", c, 1.4))


def lamp(c=W):
    """Dipped-beam headlamp (as on R-413 and S-24)."""
    return pth("M2 -12 Q14 -12 14 0 Q14 12 2 12 Z", c) + "".join(ln(-16, -9 + i * 6, -3, -6 + i * 6, c, 2.6) for i in range(4))


def snowflake(c=K, r=13, w=2.2):
    out = []
    for a in (0, 60, 120):
        rad = math.radians(a)
        dx, dy = math.cos(rad) * r, math.sin(rad) * r
        out.append(ln(round(-dx, 1), round(-dy, 1), round(dx, 1), round(dy, 1), c, w))
        for s in (1, -1):
            bx, by = s * dx * 0.6, s * dy * 0.6
            for b in (35, -35):
                rb = math.radians(a + (0 if s > 0 else 180) + 180 + b)
                out.append(ln(round(bx, 1), round(by, 1), round(bx + math.cos(rb) * -4.5, 1), round(by + math.sin(rb) * -4.5, 1), c, w * 0.75))
    return "".join(out)


def zebra(c=K, y=0, n=5, w=4, gap=3.4, h=7):
    x0 = -(n * w + (n - 1) * gap) / 2
    return "".join(rc(round(x0 + i * (w + gap), 1), y, w, h, c) for i in range(n))


def blank_icon(code, text):
    add(code, rc(4, 4, 92, 92, "#f1f5f9", 8, "#94a3b8", 2) + t(50, 57, text, 18, "#475569"))


# ------------------------------------------------------------------------------------------ P: danger warning signs
def P(code, inner, bg=W):
    add(code, warn(inner, bg), 100, 96)


def junction(stub):
    """P-1 family: thick priority road with a pointed top, thinner side roads."""
    road = pth("M45.5 84 L45.5 42 L50 34 L54.5 42 L54.5 84 Z", K)
    sides = {
        "both": pth("M33 61 L67 61", K, 6, cap="butt"), "right": pth("M50 61 L67 61", K, 6, cap="butt"), "left": pth("M33 61 L50 61", K, 6, cap="butt"),
        "mr": pth("M64 80 L51 63", K, 6, cap="butt"), "ml": pth("M36 80 L49 63", K, 6, cap="butt"),
        "stag": pth("M34 54 L50 54 M50 70 L66 70", K, 6, cap="butt"),
    }
    return sides[stub] + road


P("P-1", junction("both"))
P("P-1a", junction("right"))
P("P-1b", junction("left"))
P("P-1c", junction("mr"))
P("P-1d", junction("ml"))
P("P-1e", junction("stag"))
P("P-2", pth("M37 47 L63 75 M63 47 L37 75", K, 8, cap="butt"))
P("P-3", ci(50, 45, 6, RED) + ci(50, 60, 6, ORANGE) + ci(50, 75, 6, "#10a34a"))
P("P-4", "".join(carr(f"M{50 + 13 * math.cos(math.radians(a)):.1f} {62 + 13 * math.sin(math.radians(a)):.1f} A13 13 0 0 0 "
                      f"{50 + 13 * math.cos(math.radians(a - 80)):.1f} {62 + 13 * math.sin(math.radians(a - 80)):.1f}",
                      (50 + 13 * math.cos(math.radians(a - 100)), 62 + 13 * math.sin(math.radians(a - 100))),
                      (50 + 13 * math.cos(math.radians(a - 80)) + 6 * math.sin(math.radians(a - 80)), 62 + 13 * math.sin(math.radians(a - 80)) - 6 * math.cos(math.radians(a - 80))),
                      K, 4.5, 6, 5.5) for a in (90, 210, 330)))
P("P-5", rc(26, 72, 16, 8, K) + rc(58, 72, 16, 8, K) + pth("M40 70 L68 52", K, 6) + pth("M30 80 Q36 76 42 80 Q48 84 54 80 Q60 76 66 80", K, 1.8))
P("P-6", at(tram(), 50, 66, 0.95))
P("P-7", pth("M34 52 L34 80 M42 52 L42 80 M58 52 L58 80 M66 52 L66 80", K, 4, cap="butt") + rc(30, 58, 40, 5, K) + rc(30, 69, 40, 5, K))
P("P-8", at(train(), 50, 64, 0.95))
P("P-12", at(plane(), 50, 64, 1.1))
P("P-13a", carr("M44 84 L44 62 Q44 50 55 49", (62, 49), (55, 49), K, 7, 9, 7))
P("P-13b", carr("M56 84 L56 62 Q56 50 45 49", (38, 49), (45, 49), K, 7, 9, 7))
P("P-14a", carr("M45 85 L45 76 Q45 70 52 66 Q58 62 57 56 L50 48", (45, 43), (50, 48), K, 6.5, 8, 6.5))
P("P-14b", carr("M55 85 L55 76 Q55 70 48 66 Q42 62 43 56 L50 48", (55, 43), (50, 48), K, 6.5, 8, 6.5))
P("P-15", pth("M26 80 L26 74 Q32 64 38 74 Q44 69 50 74 Q56 64 62 74 Q68 69 74 74 L74 80 Z", K))
P("P-15a", pth("M27 80 L27 75 L38 75 Q50 60 62 75 L73 75 L73 80 Z", K))
P("P-15b", pth("M27 80 L27 67 L38 67 Q50 82 62 67 L73 67 L73 80 Z", K))
P("P-16a", pth("M24 54 L77 81 L24 81 Z", K) + t(42, 58, "10%", 10.5, K, 800, extra=' transform="rotate(27 42 58)"')
     + arr([(31, 70), (52, 80)], W, 2.6, 6, 4))
P("P-16b", pth("M23 81 L76 54 L76 81 Z", K) + t(58, 58, "10%", 10.5, K, 800, extra=' transform="rotate(-27 58 58)"')
     + arr([(48, 80), (69, 70)], W, 2.6, 6, 4))
P("P-17", pth("M37 84 L37 68 L44 58 L44 42", K, 6) + pth("M63 84 L63 68 L56 58 L56 42", K, 6))
P("P-17a", pth("M40 84 L40 42", K, 6) + pth("M62 84 L62 68 L54 58 L54 42", K, 6))
P("P-17b", pth("M60 84 L60 42", K, 6) + pth("M38 84 L38 68 L46 58 L46 42", K, 6))
P("P-18", ci(44, 49, 4.6, K) + pth("M43 54 L52 66 L46 78 M52 66 L60 79", K, 5) + pth("M45 57 L36 72", K, 3) + pth("M47 59 L58 63", K, 3)
     + ln(33, 76, 39, 64, K, 2.4) + pth("M28 79 L33 74 L38 79 Z", K) + pth("M57 82 Q66 66 76 82 Z", K), YEL)
P("P-19", at(car_side(), 50, 56, 0.75, -18) + pth("M34 82 Q40 72 46 78 Q52 84 58 74 M48 84 Q54 74 60 80 Q66 86 70 76", K, 2.4))
P("P-20a", at(ped(), 51, 58, 0.85) + at(zebra(K, 0, 6, 4.5, 3), 50, 76))
P("P-20b", at(ped(), 51, 63, 1.0))
P("P-20c", at(ped(), 40, 58, 0.7) + at(cyclist(), 60, 58, 0.55) + at(zebra(K, 0, 7, 4, 2.6), 50, 75))
P("P-21a", at(ped(), 42, 66, 0.72) + at(ped(), 58, 60, 0.8) + rc(37, 61, 5, 6, K, 1) + rc(53, 54, 5, 6, K, 1))
P("P-21b", at(standing(), 42, 65, 0.85) + at(standing(), 58, 65, 0.85) + ln(35, 58, 33, 82, K, 1.8) + ln(65, 58, 67, 82, K, 1.8))
P("P-22a", at(cyclist(), 50, 58, 0.75) + "".join(rc(30 + i * 7, 74, 4, 4, K) for i in range(6)) + "".join(rc(30 + i * 7, 80, 4, 4, K) for i in range(6)))
P("P-22b", at(cyclist(), 50, 63, 0.9))
P("P-23", at(cow(), 50, 66, 1.0))
P("P-24", at(deer(), 50, 64, 1.05))
P("P-24a", at(boar(), 50, 66, 1.05))
P("P-25", arr([(42, 44), (42, 80)], K, 5, 8, 6) + arr([(58, 80), (58, 44)], K, 5, 8, 6))
P("P-26", pth("M52 42 L76 82 L46 82 Z", K) + ci(40, 58, 3, K) + ci(36, 67, 2.6, K) + ci(42, 72, 3.4, K) + ci(33, 77, 2.4, K))
P("P-27", rc(24, 60, 22, 16, K) + at(car_side(), 56, 60, 0.6, 40) + pth("M26 82 Q31 78 36 82 Q41 86 46 82 Q51 78 56 82 Q61 86 66 82 Q71 78 76 82", K, 2))
P("P-28", at(car_side(), 54, 70, 0.75) + ci(35, 64, 2, K) + ci(30, 70, 2.4, K) + ci(37, 74, 1.8, K) + ci(29, 78, 2, K) + rc(24, 81, 52, 2.5, K))
P("P-29", ln(32, 46, 32, 84, K, 3) + pth("M32 49 L70 55 L70 62 L32 61 Z", K) + pth("M41 51 L41 61 M51 52 L51 61 M61 54 L61 62", W, 4, cap="butt"))
P("P-30", pth("M24 66 L50 66 L50 80 L76 80 L76 84 L24 84 Z", K) + at(car_front(), 46, 56, 0.6, 12))
P("P-31", at(car_front(), 41, 52, 0.55) + at(car_front(), 58, 60, 0.6) + at(car_front(), 45, 72, 0.7))
P("P-32", at(car_side(), 50, 66, 0.75, 72))
P("P-33", "".join(ln(28, 56 + i * 5, 46, 56 + i * 5, K, 2) for i in range(5)) + at(car_side(), 58, 72, 0.6))
P("P-34", at(snowflake(), 50, 64, 1.05))
P("P-35", at(car_front(), 39, 74, 0.5) + at(car_front(), 61, 74, 0.5)
     + carr("M41 64 Q41 54 56 46", (60, 42), (56, 46), K, 3, 5, 4.5) + carr("M59 64 Q59 54 44 46", (40, 42), (44, 46), K, 3, 5, 4.5))
P("P-50", rc(46, 40, 8, 26, K, 2) + ci(50, 75, 4.6, K))

# not triangles: countdown beacons (P-9/P-10) and level-crossing crosses (P-11)
for code, n in (("P-10a", 3), ("P-10b", 2), ("P-10c", 1)):
    inner = rc(22, 4, 20, 92, W, 2, "#9ca3af", 1.5) + rc(58, 4, 20, 92, W, 2, "#9ca3af", 1.5)
    for i in range(n):
        y = 10 + i * 14
        inner += pth(f"M23 {y} L41 {y + 8} L41 {y + 14} L23 {y + 6} Z", RED) + pth(f"M77 {y} L59 {y + 8} L59 {y + 14} L77 {y + 6} Z", RED)
    add(code, inner)
ICON["P-9/10"] = ICON["P-10a"]


def andrew(extra=""):
    one = '<rect x="-46" y="-8" width="92" height="16" rx="3" fill="#fff" stroke="' + RED + '" stroke-width="5"/>'
    return at(one, 50, 44, 1, 28) + at(one, 50, 44, 1, -28) + extra


add("P-11", andrew(), 100, 90)
add("P-11a", andrew(pth("M18 82 L50 66 L82 82", RED, 5) + pth("M18 82 L50 66 L82 82", W, 1.5)), 100, 90)


# ------------------------------------------------------------------------------------------ R: regulatory signs
def octagon(r=46):
    pts = " ".join(f"{50 + r * math.cos(math.radians(22.5 + 45 * i)):.1f},{50 + r * math.sin(math.radians(22.5 + 45 * i)):.1f}" for i in range(8))
    return f'<polygon points="{pts}" fill="{RED}" stroke="{W}" stroke-width="3"/>'


add("R-1", pth("M8 12 L92 12 L50 90 Z", RED, 10, W))
add("R-2", f'<polygon points="{" ".join(f"{50 + 48 * math.cos(math.radians(22.5 + 45 * i)):.1f},{50 + 48 * math.sin(math.radians(22.5 + 45 * i)):.1f}" for i in range(8))}" fill="#9ca3af"/>'
    + octagon() + t(50, 59, "STOP", 25, W, 800))
add("R-3", pth("M50 3 L97 50 L50 97 L3 50 Z", K, 2, W) + pth("M50 21 L79 50 L50 79 L21 50 Z", YEL))
add("R-4", pth("M50 3 L97 50 L50 97 L3 50 Z", K, 2, W) + pth("M50 21 L79 50 L50 79 L21 50 Z", YEL) + ln(26, 74, 74, 26, K, 10, "butt"))
add("R-5", prohib(arr([(40, 26), (40, 74)], K, 6, 11, 8) + arr([(60, 74), (60, 26)], RED, 6, 11, 8)))
add("R-6", rc(4, 4, 92, 92, BLUE, 6, W, 2.5) + arr([(36, 24), (36, 76)], RED, 6, 11, 8) + arr([(62, 78), (62, 20)], W, 8, 14, 11))

# 5.2.2 no entry
add("R-100", prohib())
add("R-101", ci(50, 50, 46, RED) + rc(18, 42, 64, 16, W))
add("R-102", prohib(at(car_front(), 50, 31, 0.7) + rc(10, 45, 80, 10, RED) + at(moto(), 50, 69, 0.62)))
add("R-103", prohib(at(car_front(), 50, 50, 1.1)))
add("R-104", prohib(at(moto(), 50, 52, 1.1)))
add("R-105", prohib(at(moped(), 50, 52, 1.1)))
add("R-106", prohib(at(truck(), 50, 51, 1.05)))
add("R-107", prohib(at(truck(K, W, "5,5t"), 50, 51, 1.05)))
add("R-108", prohib(rc(34, 30, 32, 34, K, 2) + rc(38, 34, 24, 22, ORANGE) + rc(32, 62, 36, 5, K) + ci(38, 70, 4, K) + ci(62, 70, 4, K)))
add("R-109", prohib(at(car_front(), 50, 60, 0.95) + pth("M36 40 L41 31 L44 37 L50 27 L54 36 L59 30 L63 40 Z", ORANGE) + ci(50, 37, 3, RED)))
add("R-110", prohib(f'<ellipse cx="50" cy="39" rx="21" ry="10" fill="{ORANGE}"/>' + rc(27, 48, 46, 4, K) + ci(36, 56, 3.4, K) + ci(64, 56, 3.4, K)
                    + pth("M25 66 Q31 62 37 66 Q43 70 50 66 Q57 62 63 66 Q69 70 75 66", K, 2) + pth("M28 73 Q34 69 40 73 Q46 77 52 73 Q58 69 64 73 Q70 77 73 73", K, 2)))
add("R-111", prohib(at(tractor(), 50, 50, 1.05)))
add("R-112", prohib(rc(18, 44, 18, 12, K, 2) + ln(36, 52, 44, 52, K, 2.4) + rc(44, 38, 36, 15, K, 1) + t(62, 50, "2t", 10, W) + ci(24, 58, 4, K) + ci(62, 57, 4, K)))
add("R-113", prohib(at(cart(), 50, 52, 1.05)))
add("R-114", prohib(at(bike(), 50, 52, 1.15)))
add("R-115", prohib(at(handcart(), 52, 52, 1.1)))
add("R-116", prohib(at(ped(), 50, 51, 1.15)))
add("R-117", prohib(at(rider(), 50, 53, 1.05)))
add("R-118", prohib(at(vmp(), 50, 50, 1.2)))
add("R-119", prohib(at(vmp(), 50, 31, 0.6) + rc(10, 45, 80, 10, RED) + at(bike(), 50, 68, 0.75)))
add("R-120", prohib(at(car_front(), 42, 52, 0.95) + "".join(ci(64 + (i % 3) * 5, 44 + (i // 3) * 5, 1.6, K) for i in range(9))))

# 5.2.3 restriction
add("R-200", prohib(rc(22, 45, 56, 10, K)))
add("R-201", prohib(t(50, 60, "5,5t", 27, K, 800)))
add("R-202", prohib(t(50, 40, "2,4t", 17, K, 800) + arr([(50, 44), (50, 56)], K, 2.4, 5, 4) + ln(30, 64, 70, 64, K, 3) + ci(33, 64, 5, K) + ci(67, 64, 5, K)))
add("R-203", prohib(at(truck(), 50, 42, 0.95) + arr([(42, 64), (22, 64)], K, 2, 6, 4) + arr([(58, 64), (78, 64)], K, 2, 6, 4) + t(50, 68, "10m", 11, K, 800)))
add("R-204", prohib(t(48, 63, "2", 34, K, 800) + t(61, 63, ",5", 14, K, 800) + t(61, 41, "m", 11, K, 800)
                    + pth("M14 50 L26 42 L26 58 Z", K) + pth("M86 50 L74 42 L74 58 Z", K)))
add("R-205", prohib(t(50, 61, "4,5m", 24, K, 800) + pth("M50 22 L42 12 L58 12 Z", K) + pth("M50 78 L42 88 L58 88 Z", K)))

# 5.2.4 other prohibitions
add("R-300", prohib(t(50, 46, "70 m", 17, K, 800) + at(car_front(), 32, 61, 0.45) + at(car_front(), 68, 61, 0.45)))
add("R-301", prohib(t(50, 63, "40", 38, K, 800)))
add("R-302", prohib(arr([(42, 78), (42, 46), (66, 46)], K, 8, 13, 10) + bar_red()))
add("R-303", prohib(arr([(58, 78), (58, 46), (34, 46)], K, 8, 13, 10) + bar_red()))
add("R-304", prohib(carr("M60 78 L60 44 Q60 30 48 30 Q37 30 37 44 L37 56", (37, 66), (37, 56), K, 7, 11, 9) + bar_red()))
add("R-305", prohib(at(car_front(RED), 34, 50, 0.72) + at(car_front(), 66, 50, 0.72)))
add("R-306", prohib(rc(18, 38, 28, 22, RED, 2) + rc(19, 60, 7, 6, RED, 1) + rc(38, 60, 7, 6, RED, 1) + at(car_front(), 68, 50, 0.72)))
x_red = ln(22, 22, 78, 78, RED, 8, "butt") + ln(78, 22, 22, 78, RED, 8, "butt")
add("R-307", ci(50, 50, 42, BLUE, RED, 12) + x_red)
add("R-307a", ci(50, 50, 42, BLUE, RED, 12) + x_red + arr([(32, 50), (16, 50)], W, 3.4, 7, 5) + arr([(68, 50), (84, 50)], W, 3.4, 7, 5))
add("R-307b", ci(50, 50, 42, BLUE, RED, 12) + x_red + arr([(66, 50), (84, 50)], W, 3.4, 7, 5))
add("R-307c", ci(50, 50, 42, BLUE, RED, 12) + x_red + arr([(34, 50), (16, 50)], W, 3.4, 7, 5))
one = ln(22, 22, 78, 78, RED, 8, "butt")
add("R-308", ci(50, 50, 42, BLUE, RED, 12) + one)
add("R-308c", ci(50, 50, 42, BLUE, RED, 12) + one + t(54, 34, "1-15", 12, W, 800))
add("R-308d", ci(50, 50, 42, BLUE, RED, 12) + one + t(46, 74, "16-31", 12, W, 800))
add("R-308e", rc(4, 4, 92, 92, W, 8, K, 4) + ci(50, 42, 27, BLUE, RED, 8) + ln(32, 24, 68, 60, RED, 6, "butt") + t(50, 89, "VADO", 15, RED, 800))
add("R-308f", ci(50, 50, 42, BLUE, RED, 12) + one + arr([(48, 30), (70, 30)], W, 3.4, 7, 5) + arr([(52, 70), (30, 70)], W, 3.4, 7, 5))
add("R-308g", ci(50, 50, 42, BLUE, RED, 12) + one + arr([(48, 30), (70, 30)], W, 3.4, 7, 5))
add("R-308h", ci(50, 50, 42, BLUE, RED, 12) + one + arr([(52, 70), (30, 70)], W, 3.4, 7, 5))
add("R-309", rc(4, 4, 92, 92, W, 8, K, 4) + ci(50, 50, 27, BLUE, RED, 8) + ln(32, 32, 68, 68, RED, 6, "butt"))
add("R-310", prohib(pth("M26 44 L40 44 L64 34 L64 66 L40 56 L26 56 Z", K) + rc(64, 44, 10, 12, K, 2) + bar_red()))

# 5.2.5 obligation
add("R-400a", oblig(arr([(22, 50), (80, 50)], W, 11, 22, 17)))
add("R-400b", oblig(arr([(78, 50), (20, 50)], W, 11, 22, 17)))
add("R-400c", oblig(arr([(50, 82), (50, 18)], W, 11, 22, 17)))
add("R-400d", oblig(carr("M42 80 L42 52 Q42 38 56 38 L62 38", (78, 38), (62, 38), W, 8, 16, 12)))
add("R-400e", oblig(carr("M58 80 L58 52 Q58 38 44 38 L38 38", (22, 38), (38, 38), W, 8, 16, 12)))
add("R-401a", oblig(arr([(26, 26), (74, 74)], W, 10, 20, 15)))
add("R-401b", oblig(arr([(74, 26), (26, 74)], W, 10, 20, 15)))
add("R-401c", oblig(arr([(50, 30), (24, 66)], W, 7, 15, 11) + arr([(50, 30), (76, 66)], W, 7, 15, 11)))
add("R-402", oblig("".join(carr(f"M{50 + 26 * math.cos(math.radians(a)):.1f} {50 + 26 * math.sin(math.radians(a)):.1f} A26 26 0 0 0 "
                                  f"{50 + 26 * math.cos(math.radians(a - 75)):.1f} {50 + 26 * math.sin(math.radians(a - 75)):.1f}",
                                  (50 + 26 * math.cos(math.radians(a - 100)), 50 + 26 * math.sin(math.radians(a - 100))),
                                  (50 + 26 * math.cos(math.radians(a - 75)) + 8 * math.sin(math.radians(a - 75)), 50 + 26 * math.sin(math.radians(a - 75)) - 8 * math.cos(math.radians(a - 75))),
                                  W, 7, 12, 10) for a in (100, 220, 340))))
add("R-403a", oblig(arr([(42, 84), (42, 18)], W, 7, 14, 10) + carr("M42 66 Q42 50 58 50", (78, 50), (58, 50), W, 7, 14, 10)))
add("R-403b", oblig(arr([(58, 84), (58, 18)], W, 7, 14, 10) + carr("M58 66 Q58 50 42 50", (22, 50), (42, 50), W, 7, 14, 10)))
add("R-403c", oblig(pth("M50 84 L50 56", W, 7, cap="butt") + carr("M50 58 Q50 44 36 44", (20, 44), (36, 44), W, 7, 14, 10)
                    + carr("M50 58 Q50 44 64 44", (80, 44), (64, 44), W, 7, 14, 10)))
add("R-404", oblig(at(car_front(W, BLUE), 50, 50, 1.25)))
add("R-405", oblig(at(moto(W, BLUE), 50, 52, 1.2)))
add("R-406", oblig(at(truck(W, BLUE), 50, 51, 1.15)))
add("R-407a", oblig(at(bike(W, BLUE), 50, 52, 1.3)))
add("R-407b", oblig(at(moped(W, BLUE), 50, 52, 1.2)))
add("R-408", oblig(at(cart(W, BLUE), 50, 52, 1.15)))
add("R-409", oblig(at(rider(W, BLUE), 50, 53, 1.15)))
add("R-410", oblig(at(ped(W, BLUE), 50, 51, 1.3)))
add("R-411", oblig(t(50, 64, "40", 42, W, 800)))
add("R-412", oblig(rc(34, 18, 32, 64, W, 14) + rc(40, 26, 20, 48, BLUE, 9) + pth("M34 30 L66 46 M34 46 L66 30 M34 54 L66 70 M34 70 L66 54", W, 2.4)))
add("R-412b", oblig(rc(24, 22, 26, 56, W, 11) + "".join(ln(27, 30 + i * 7, 47, 30 + i * 7, BLUE, 2) for i in range(7))
                     + pth("M56 70 L66 44 L76 70 Z", W) + at(snowflake(BLUE, 6, 1.4), 66, 60)))
add("R-413", oblig(at(lamp(), 52, 50, 1.6)))
add("R-414", oblig(rc(34, 26, 32, 36, W, 2) + rc(38, 30, 24, 24, ORANGE) + rc(32, 62, 36, 5, W) + ci(38, 71, 4, W) + ci(62, 71, 4, W)))
add("R-415", oblig(f'<ellipse cx="50" cy="38" rx="21" ry="10" fill="{ORANGE}"/>' + rc(27, 47, 46, 4, W) + ci(36, 55, 3.4, W) + ci(64, 55, 3.4, W)
                   + pth("M25 66 Q31 62 37 66 Q43 70 50 66 Q57 62 63 66 Q69 70 75 66", W, 2.2)))
add("R-416", oblig(at(car_front(W, BLUE), 50, 62, 1.0) + pth("M36 41 L41 32 L44 38 L50 28 L54 37 L59 31 L63 41 Z", ORANGE) + ci(50, 38, 3, RED)))
add("R-417", oblig(ci(46, 22, 7, W) + pth("M42 32 L38 58 L60 58 L66 78", W, 7) + pth("M36 30 L58 56", K, 3.5) + pth("M58 34 L64 26", W, 2.4)))
add("R-418", oblig(rc(26, 24, 48, 10, W) + rc(32, 34, 12, 44, W) + rc(56, 34, 12, 44, W)))
add("R-419", oblig(at(tractor(W, BLUE), 50, 51, 1.2)))
add("R-420", oblig(at(vmp(W, BLUE), 50, 50, 1.35)))
add("R-421", oblig(at(vmp(W, BLUE), 50, 32, 0.75) + at(bike(W, BLUE), 50, 66, 0.95)))
add("R-422", oblig(at(standing(W, BLUE), 58, 52, 1.3) + ln(36, 36, 36, 82, W, 3) + ln(30, 36, 42, 36, W, 3) + ci(36, 76, 6, "none", W, 2.4)))

# 5.2.6 end of prohibition or restriction
add("R-500", endsig("", 6))
add("R-501", endsig(t(50, 64, "70", 40, K, 800)))
add("R-502", endsig(at(car_front(), 33, 50, 0.72) + at(car_front(), 67, 50, 0.72)))
add("R-503", endsig(rc(16, 38, 28, 22, K, 2) + rc(17, 60, 7, 6, K, 1) + rc(36, 60, 7, 6, K, 1) + at(car_front(), 67, 50, 0.72)))
add("R-504", rc(4, 4, 92, 92, W, 6, K, 4) + ci(50, 50, 28, "none", GRAY, 9) + ln(30, 30, 70, 70, GRAY, 8, "butt") + ln(10, 90, 90, 10, K, 8, "butt"))
for code, pic in (("R-505", at(bike(W, BLUE), 50, 52, 1.3)), ("R-506", t(50, 64, "40", 42, W, 800)), ("R-507", at(car_front(W, BLUE), 50, 50, 1.25)),
                  ("R-508", at(moto(W, BLUE), 50, 52, 1.2)), ("R-509", at(truck(W, BLUE), 50, 51, 1.15)), ("R-510", at(moped(W, BLUE), 50, 52, 1.2)),
                  ("R-511", at(cart(W, BLUE), 50, 52, 1.15)), ("R-512", at(rider(W, BLUE), 50, 53, 1.15)), ("R-513", at(ped(W, BLUE), 50, 51, 1.3)),
                  ("R-514", at(tractor(W, BLUE), 50, 51, 1.2)), ("R-515", at(vmp(W, BLUE), 50, 50, 1.35)),
                  ("R-516", at(vmp(W, BLUE), 50, 32, 0.75) + at(bike(W, BLUE), 50, 66, 0.95))):
    add(code, end_blue(pic))


# ------------------------------------------------------------------------------------------ S: indication signs
def V(code, inner, end=False, fill=BLUE, edge=W):
    """Vertical rectangular sign (100 x 130)."""
    add(code, brect(inner, 100, 130, fill, edge) + (end_rect(100, 130) if end else ""), 100, 130)


def SQ(code, inner, end=False, fill=BLUE, edge=W):
    add(code, brect(inner, 100, 100, fill, edge) + (end_rect(100, 100) if end else ""), 100, 100)


def WD(code, inner, w=160, h=70, end=False, fill=BLUE, edge=W, px=48):
    add(code, brect(inner, w, h, fill, edge) + (end_rect(w, h) if end else ""), w, h, px)


def motorway(c=W):
    return (pth("M14 118 L40 34 L46 34 L38 118 Z", c) + pth("M86 118 L60 34 L54 34 L62 118 Z", c) + rc(18, 30, 64, 7, c)
            + pth("M47 118 L49 50 L51 50 L53 118 Z", c))


def autovia(c=W, label="AUTOVÍA"):
    lines_ = "".join(ln(50 + dx * 3, 118, 50 + dx * 0.6, 42, c, 2.6 if abs(dx) > 9 else 1.8) for dx in (-14, -9, -4, 4, 9, 14))
    return t(50, 26, label, 15, c, 800) + lines_


V("S-1", motorway())
V("S-2", motorway(), end=True)
V("S-1a", autovia())
V("S-2a", autovia(), end=True)
V("S-3", at(car_front(W, BLUE), 50, 65, 1.3))
V("S-4", at(car_front(W, BLUE), 50, 65, 1.3), end=True)
multi = t(50, 24, "MULTI-", 15, K, 800) + t(50, 40, "CARRIL", 15, K, 800) + f'<ellipse cx="50" cy="66" rx="24" ry="5" fill="none" stroke="{K}" stroke-width="2.5"/>' \
    + "".join(ln(50 + dx * 3, 120, 50 + dx * 0.8, 72, K, 2) for dx in (-12, -4, 4, 12))
V("S-1b", multi, fill=W, edge=K)
V("S-2b", multi, end=True, fill=W, edge=K)
dos1 = (t(50, 22, "CARRETERA", 12, K, 800) + t(50, 37, "2+1", 13, K, 800) + ln(22, 122, 40, 46, K, 2.4) + ln(78, 122, 60, 46, K, 2.4)
        + pth("M38 122 Q40 96 50 84 Q58 72 52 46", K, 2) + pth("M62 122 Q60 98 52 86", K, 2, cap="butt"))
V("S-1c", dos1, fill=W, edge=K)
V("S-2c", dos1, end=True, fill=W, edge=K)
V("S-5", rc(18, 14, 64, 56, W, 3) + pth("M28 66 L28 42 Q28 24 50 24 Q72 24 72 42 L72 66 Z", K) + pth("M36 66 L36 46 Q36 34 50 34 Q64 34 64 46 L64 66 Z", "#cbd5e1")
  + "".join(rc(25 + i * 9, 18, 6, 3, K) for i in range(6)))
SQ("S-7", t(50, 69, "70", 50, W, 800))
SQ("S-8", t(50, 69, "70", 50, W, 800), end=True)
WD("S-9", t(80, 50, "70-90", 40, W, 800), 160, 70)
WD("S-10", t(80, 50, "70-90", 40, W, 800), 160, 70, end=True)
SQ("S-11", arr([(50, 88), (50, 12)], W, 16, 30, 24))
WD("S-11a", arr([(54, 64), (54, 8)], W, 7, 14, 10) + arr([(106, 64), (106, 8)], W, 7, 14, 10), 160, 70)
WD("S-12", arr([(16, 35), (146, 35)], W, 9, 22, 16), 160, 70)


def crossing_sq(pic):
    return pth("M50 12 L90 86 L10 86 Z", W) + pic


SQ("S-13", crossing_sq(at(ped(), 52, 52, 0.95) + at(zebra(K, 0, 7, 5, 4), 50, 76)))
SQ("S-45", crossing_sq(at(cyclist(), 50, 56, 0.8) + "".join(rc(22 + i * 8, 78, 5, 4, K) for i in range(8))))
SQ("S-46", crossing_sq(at(ped(), 40, 58, 0.7) + at(cyclist(), 61, 58, 0.55) + at(zebra(K, 0, 7, 5, 3.6), 50, 76)))
stairs_up = pth("M14 118 L14 104 L32 104 L32 90 L50 90 L50 76 L68 76 L68 62 L86 62 L86 118 Z", W)
V("S-14a", stairs_up + at(ped(W, BLUE), 44, 52, 1.1))
V("S-14b", at(stairs_up, 100, 0, 1, fx=True) + at(ped(W, BLUE), 56, 60, 1.1))
dead_end = rc(44, 46, 12, 74, W) + rc(22, 30, 56, 16, RED, 0, W, 3)
V("S-15a", dead_end)
V("S-15e", dead_end + at(ped(W, BLUE), 32, 16, 0.5) + at(bike(W, BLUE), 64, 16, 0.6))
V("S-16", ln(30, 122, 70, 10, W, 9, "butt") + pth("M55 70 L74 30 L82 30 L82 120 L66 120 Z", W)
  + "".join(ci(70 + (i % 3) * 4.5, 40 + (i // 3) * 7, 1.6, "#94a3b8") for i in range(33)))
SQ("S-17", t(50, 80, "P", 80, W, 800))
SQ("S-17a", t(44, 74, "P", 66, W, 800) + rc(56, 66, 14, 14, W) + pth("M60 73 L66 73 M63 70 L63 76", GREEN, 3) + ci(81, 73, 7, "none", W, 2) + ln(81, 73, 81, 68, W, 1.6))
SQ("S-18", t(50, 62, "TAXI", 32, W, 800))
V("S-19", rc(14, 14, 72, 46, W, 3) + at(bus(), 50, 38, 1.2))
V("S-20", rc(14, 14, 72, 46, W, 3) + at(tram(), 50, 38, 1.35))
add("S-21", rc(2, 2, 156, 26, BLUE, 4, W, 2) + t(80, 21, "PAJARES", 15, W, 800) + rc(2, 30, 156, 22, BLUE, 4, W, 2) + rc(14, 34, 132, 14, W, 2) + t(80, 46, "CON RESTRICCIÓN", 11, K, 800)
    + rc(2, 54, 156, 22, BLUE, 4, W, 2) + rc(40, 58, 106, 14, W, 2) + t(93, 70, "CERRADO", 11, K, 800) + at(truck(W, BLUE), 21, 65, 0.4)
    + rc(2, 78, 156, 22, BLUE, 4, W, 2) + rc(40, 82, 106, 14, W, 2) + t(93, 94, "CADENAS", 11, K, 800) + at(car_front(W, BLUE), 21, 89, 0.4), 160, 102)
SQ("S-22", carr("M60 76 L60 38 Q60 20 42 20 Q26 20 26 38 L26 48", (26, 60), (26, 48), W, 8, 15, 11) + t(50, 92, "150 m", 15, W, 800))
SQ("S-25", arr([(50, 74), (50, 14)], W, 9, 15, 11) + carr("M50 74 L50 92 M50 60 L66 50 L42 92", (40, 96), (42, 92), W, 6, 10, 8))
SQ("S-23", rc(36, 6, 28, 28, W) + pth("M50 11 L50 29 M41 20 L59 20", RED, 7, cap="butt") + pth("M16 82 L16 50 M16 70 L84 70 L84 84 M16 62 L80 56", W, 4))
WD("S-24", at(lamp(), 60, 35, 1.5) + t(120, 50, "?", 44, W, 800), 160, 70)
add("S-26", "".join(rc(2 + i * 34, 2, 30, 66, BLUE, 3, W, 2) + t(17 + i * 34, 16, str(300 - i * 100), 10, W, 800)
                    + "".join(pth(f"M{6 + i * 34} {30 + j * 12} L{28 + i * 34} {22 + j * 12} L{28 + i * 34} {28 + j * 12} L{6 + i * 34} {36 + j * 12} Z", W) for j in range(3 - i))
                    for i in range(3)), 106, 70)
SQ("S-32", rc(26, 22, 48, 10, W) + rc(32, 32, 12, 46, W) + rc(56, 32, 12, 46, W))
SQ("S-34", pth("M30 6 L30 94", W, 6, cap="butt") + pth("M52 6 L52 26 L72 40 L72 62 L52 76 L52 94", W, 6) + pth("M41 10 L41 22 M41 38 L41 50 M41 66 L41 78", W, 4, cap="butt"))
V("S-34a", pth("M30 6 L30 124", W, 6, cap="butt") + pth("M52 6 L52 36 L72 50 L72 80 L52 94 L52 124", W, 6) + t(62, 60, "S", 11, W, 800) + t(62, 72, "O", 11, W, 800) + t(62, 84, "S", 11, W, 800))
WD("S-27", t(80, 30, "SOS", 26, W, 800) + arr([(130, 52), (30, 52)], W, 6, 14, 10), 160, 70)
play = at(ped(W, BLUE), 22, 44, 0.9) + at(car_front(W, BLUE), 58, 22, 0.55) + pth("M90 14 L104 4 L118 14 L118 30 L90 30 Z", W) + rc(100, 20, 7, 10, BLUE) + at(ped(W, BLUE), 64, 52, 0.55, -10) + ci(46, 56, 3, W) + pth("M118 34 Q100 52 112 64", W, 6)
WD("S-28", play, 130, 70)
WD("S-29", play, 130, 70, end=True)
coex = at(car_front(W, BLUE), 28, 22, 0.6) + at(cyclist(W, BLUE), 70, 22, 0.5) + at(standing(W, BLUE), 24, 66, 1.05) + at(standing(W, BLUE), 40, 76, 0.6) + ci(70, 70, 17, W, RED, 5) + t(70, 77, "20", 18, K, 800)
SQ("S-47", coex)
SQ("S-48", coex, end=True)
pedzone = at(standing(W, BLUE), 70, 52, 1.35) + at(ped(W, BLUE), 46, 52, 1.2) + rc(14, 60, 16, 12, W, 3) + ci(17, 76, 3, W) + ci(27, 76, 3, W) + ln(30, 60, 36, 50, W, 2.4)
SQ("S-30a", pedzone)
SQ("S-31a", pedzone, end=True)
SQ("S-33", at(standing(W, GREEN), 38, 30, 0.95) + at(standing(W, GREEN), 54, 36, 0.6) + at(bike(W, GREEN), 50, 74, 1.4), fill=GREEN)
SQ("S-35", at(bike(W, BLUE), 50, 52, 1.6))
SQ("S-36", at(bike(W, BLUE), 50, 52, 1.6), end=True)
SQ("S-37", at(vmp(W, BLUE), 50, 50, 1.7))
SQ("S-39", at(vmp(W, BLUE), 50, 50, 1.7), end=True)
SQ("S-38", at(vmp(W, BLUE), 50, 28, 0.9) + at(bike(W, BLUE), 50, 70, 1.2))
SQ("S-40", at(vmp(W, BLUE), 50, 28, 0.9) + at(bike(W, BLUE), 50, 70, 1.2), end=True)
split = ln(62, 4, 62, 96, W, 3) + at(bike(W, BLUE), 32, 52, 1.1) + at(ped(W, BLUE), 80, 52, 0.9)
SQ("S-41", split)
SQ("S-42", split, end=True)
split3 = ln(62, 4, 62, 96, W, 3) + at(vmp(W, BLUE), 32, 30, 0.75) + at(bike(W, BLUE), 32, 72, 0.95) + at(ped(W, BLUE), 80, 52, 0.9)
SQ("S-43", split3)
SQ("S-44", split3, end=True)
V("S-49", at(moto(W, BLUE), 30, 22, 0.75) + at(bike(W, BLUE), 70, 22, 0.75) + rc(4, 44, 92, 5, W) + arr([(50, 118), (50, 62)], W, 8, 16, 12))

# 5.3.2 lanes (lane-arrow signs)
def lane_sign(code, n, spec, extra="", w=None):
    w = w or (28 + 26 * n)
    xs = [w / 2 + (i - (n - 1) / 2) * 26 for i in range(n)]
    out = []
    for i, kind in enumerate(spec):
        x = xs[i]
        if kind == "u":
            out.append(arr([(x, 90), (x, 12)], W, 5, 11, 8))
        elif kind == "d":
            out.append(arr([(x, 10), (x, 88)], W, 5, 11, 8))
        elif kind == "endL":          # this lane ends, merging into the lane on its left
            out.append(pth(f"M{x} 90 L{x} 62 L{xs[i - 1] + 4} 40", W, 5))
        elif kind == "endR":
            out.append(pth(f"M{x} 90 L{x} 62 L{xs[i + 1] - 4} 40", W, 5))
        elif kind == "newR":          # a new lane opens on the right
            out.append(pth(f"M{xs[i - 1] + 3} 66 L{x} 46", W, 5) + arr([(x, 47), (x, 12)], W, 5, 11, 8))
        elif kind == "bifR":
            out.append(carr(f"M{x} 90 L{x} 56 Q{x} 42 {x + 8} 30", (x + 13, 14), (x + 8, 30), W, 5, 11, 8))
        elif kind == "bifL":
            out.append(carr(f"M{x} 90 L{x} 56 Q{x} 42 {x - 8} 30", (x - 13, 14), (x - 8, 30), W, 5, 11, 8))
        elif kind == "dashL":         # dashed lane joining from the left
            out.append(pth(f"M{x - 20} 92 Q{x} 70 {x} 46", W, 5, cap="butt").replace("/>", ' stroke-dasharray="6 5"/>') + arr([(x, 47), (x, 12)], W, 5, 11, 8))
        elif kind == "dashR":
            out.append(pth(f"M{x + 20} 92 Q{x} 70 {x} 46", W, 5, cap="butt").replace("/>", ' stroke-dasharray="6 5"/>') + arr([(x, 47), (x, 12)], W, 5, 11, 8))
        elif kind == "bike":
            out.append(arr([(x, 90), (x, 12)], W, 5, 11, 8) + ci(x, 54, 11, BLUE, W, 2.4) + at(bike(W, BLUE), x, 54, 0.42))
        elif kind == "bikeD":
            out.append(arr([(x, 10), (x, 88)], W, 5, 11, 8) + ci(x, 48, 11, BLUE, W, 2.4) + at(bike(W, BLUE), x, 48, 0.42))
        elif kind == "v70":
            out.append(arr([(x, 90), (x, 12)], W, 5, 11, 8) + ci(x, 50, 10, BLUE, W, 2.4) + t(x, 54.5, "70", 11, W, 800))
    add(code, brect("".join(out) + extra, w, 100), w, 100)


lane_sign("S-50d", 3, ["d", "v70", "u"])
lane_sign("S-50e", 3, ["v70", "v70", "u"])
lane_sign("S-52", 2, ["u", "endL"])
lane_sign("S-52a", 3, ["d", "u", "endL"])
lane_sign("S-53", 2, ["u", "newR"])
lane_sign("S-53b", 3, ["u", "u", "newR"])
lane_sign("S-60a", 2, ["bifL", "u"])
lane_sign("S-60b", 2, ["u", "bifR"])
lane_sign("S-61a", 3, ["bifL", "u", "u"])
lane_sign("S-61b", 3, ["u", "u", "bifR"])
lane_sign("S-61c", 3, ["d", "u", "bifR"])
lane_sign("S-62a", 4, ["bifL", "u", "u", "u"])
lane_sign("S-62b", 4, ["u", "u", "u", "bifR"])
lane_sign("S-63a", 4, ["bifL", "bifL", "bifR", "bifR"])
lane_sign("S-63c", 4, ["bifL", "bifL", "u", "u"])
lane_sign("S-63d", 4, ["u", "u", "bifR", "bifR"])
lane_sign("S-64a", 3, ["u", "u", "bike"])
lane_sign("S-66", 2, ["bikeD", "u"])
lane_sign("S-68", 3, ["d", "d", "u"])
lane_sign("S-70a", 2, ["dashL", "u"])
lane_sign("S-70b", 2, ["u", "dashR"])
lane_sign("S-73a", 3, ["dashL", "dashL", "u"])
SQ("S-51a", at(bus(W, BLUE), 50, 22, 1.4) + at(moto(W, BLUE), 50, 52, 0.75) + t(50, 88, "TAXI", 20, W, 800))
SQ("S-51b", pth("M24 66 L24 40 Q24 28 36 26 L64 26 Q76 28 76 40 L76 66 Z", W) + ci(40, 36, 5, BLUE) + ci(60, 36, 5, BLUE) + t(50, 60, "2+", 20, K, 800)
   + pth("M14 92 L24 66 M86 92 L76 66", W, 3) + arr([(50, 94), (50, 72)], W, 4, 9, 7))

# 5.3.3 services: blue vertical sign with a white square
def SV(code, pic):
    V(code, rc(14, 12, 72, 64, W, 2) + pic)


SV("S-100", pth("M50 20 L50 68 M26 44 L74 44", RED, 14, cap="butt"))
V("S-101", rc(14, 12, 72, 54, W, 2) + pth("M50 18 L50 60 M29 39 L71 39", RED, 12, cap="butt") + t(50, 98, "S.O.S.", 18, W, 800))
SV("S-102", t(50, 58, "itv", 32, K, 800))
SV("S-103", rc(46, 30, 8, 40, K) + pth("M36 20 L64 20 L64 30 L56 30 L56 24 L44 24 L44 30 L36 30 Z", K))
SV("S-104", pth("M38 22 Q30 22 30 32 L30 58 Q30 68 38 68 L46 68 L46 58 L40 58 L40 32 L46 32 L46 22 Z", K))


def pump(x, y, s=1, c=K):
    return at(rc(-10, -18, 20, 36, c, 2) + rc(-6, -14, 12, 9, W) + pth("M10 -8 L16 -4 L16 12 L20 12", c, 2.4), x, y, s)


SV("S-105", pump(48, 46, 1.1))
SV("S-105b", pump(42, 48, 0.9) + t(66, 32, "GLP", 13, BLUE, 800))
SV("S-105c", pump(48, 50, 0.9) + t(50, 26, "GLP", 14, BLUE, 800))
ev = rc(-9, -16, 18, 32, "#16a34a", 2) + t(0, -2, "E", 11, W, 800) + t(0, 11, "V", 11, W, 800)
SV("S-105d", pump(36, 46, 0.85) + at(ev, 64, 48))
SV("S-105e", at(ev, 50, 44, 1.3))
SV("S-105f", pump(32, 48, 0.75) + at(ev, 64, 50, 0.9) + t(32, 26, "GLP", 11, BLUE, 800))
V("S-106", rc(20, 10, 60, 40, W, 2) + rc(46, 16, 8, 26, K) + pth("M38 14 L62 14 L62 20 L56 20 L56 17 L44 17 L44 20 L38 20 Z", K)
  + rc(20, 56, 60, 40, W, 2) + pump(50, 76, 0.85))
SV("S-107", pth("M50 22 L76 66 L24 66 Z", K) + pth("M50 40 L58 66 L42 66 Z", W))
SV("S-108", rc(54, 24, 10, 42, K) + rc(30, 30, 26, 8, K) + rc(30, 30, 8, 18, K) + rc(26, 62, 44, 6, K))
SV("S-109", rc(28, 30, 44, 30, K, 3) + ci(50, 45, 10, W) + ci(50, 45, 6, K) + rc(36, 24, 12, 7, K))
SV("S-110", rc(24, 34, 52, 14, K) + rc(24, 28, 6, 30, K) + rc(70, 40, 6, 18, K) + rc(32, 28, 12, 6, K, 3))
SV("S-111", pth("M38 22 L62 66 M62 22 L38 66", K, 5))
SV("S-112", pth("M30 34 L64 34 L60 56 L34 56 Z", K) + pth("M64 38 Q74 40 62 50", K, 3) + rc(24, 58, 52, 4, K, 2))


def caravan(c=K, bg=W):
    return rc(-18, -12, 32, 22, c, 5) + rc(-12, -7, 9, 7, bg, 1) + rc(2, -7, 8, 7, bg, 1) + ci(-4, 11, 4, c) + ln(14, 6, 22, 6, c, 2)


SV("S-113", at(caravan(), 48, 46, 1.1))
SV("S-114", pth("M38 18 L50 42 L26 42 Z", K) + pth("M38 30 L52 56 L24 56 Z", K) + rc(36, 56, 4, 10, K) + rc(48, 50, 26, 4, K) + pth("M54 54 L52 66 M68 54 L70 66", K, 3))
SV("S-115", at(ped(), 40, 46, 0.95) + at(ped(), 62, 46, 0.95) + ln(30, 34, 26, 66, K, 2))
SV("S-116", pth("M50 16 L64 38 L36 38 Z", K) + at(caravan(), 48, 56, 0.85))
SV("S-117", pth("M30 20 L42 46 L18 46 Z", K) + rc(28, 46, 4, 18, K) + pth("M54 40 L68 28 L82 40 L82 64 L54 64 Z", K) + rc(64, 50, 8, 14, W))
SV("S-118", t(50, 66, "i", 50, K, 800, extra=' font-style="italic" font-family="Georgia, serif"'))
V("S-119", rc(14, 12, 72, 54, W, 2) + pth("M28 46 Q44 32 64 42 L72 36 L72 52 L64 46 Q44 58 28 46 Z", K) + pth("M50 18 L50 30 Q50 36 46 34", K, 2) + t(50, 98, "COTO", 18, W, 800))
SV("S-120", at(deer(), 40, 50, 0.95, fx=True) + pth("M62 22 Q76 18 78 32 Q78 42 66 42 Z", K) + rc(66, 40, 4, 26, K))
SV("S-121", rc(24, 58, 52, 8, K) + rc(28, 30, 44, 10, K) + rc(30, 40, 8, 18, K) + rc(62, 40, 8, 18, K) + pth("M38 58 L38 46 Q50 36 62 46 L62 58 Z", K) + rc(24, 24, 52, 6, K))
SV("S-122", "")
V("S-123", pth("M50 14 A28 28 0 0 0 50 70 Z", "#16a34a") + t(64, 74, "P", 64, W, 800) + at(standing(W, BLUE), 30, 92, 0.8) + rc(10, 108, 80, 8, "#16a34a"))
SV("S-124", rc(20, 34, 22, 22, BLUE) + t(31, 52, "P", 18, W, 800) + t(48, 52, "+", 16, K, 800) + at(train(), 66, 46, 0.6))
SV("S-125", rc(20, 34, 22, 22, BLUE) + t(31, 52, "P", 18, W, 800) + t(48, 52, "+", 16, K, 800) + ci(68, 45, 11, "none", K, 3) + t(68, 50, "M", 12, K, 800))
SV("S-126", rc(20, 34, 22, 22, BLUE) + t(31, 52, "P", 18, W, 800) + t(48, 52, "+", 16, K, 800) + at(bus(), 68, 46, 0.42))
SV("S-128", at(caravan(), 46, 34, 1.0) + pth("M40 52 L60 52 L56 64 L44 64 Z", K) + pth("M30 68 Q36 64 42 68 Q48 72 54 68 Q60 64 66 68", K, 2))
V("S-129", t(50, 66, "P", 70, W, 800) + at(snowflake(W, 16, 3), 50, 98))

# 5.3.4 orientation: road identification, location, confirmation, urban modules
def plate(code, text, fill, fg=W, w=150):
    add(code, rc(2, 2, w - 4, 56, fill, 4, "#cbd5e1" if fill == W else None, 1.5) + t(w / 2, 45, text, 40, fg, 800), w, 60, 52)


plate("S-400", "E-90", GREEN)
plate("S-410", "A-30", BLUE)
plate("S-410a", "AP-6", BLUE)
plate("S-420", "N-401", RED, w=170)
plate("S-430", "EX-100", ORANGE, K, 190)
plate("S-440", "ZA-320", BROWN, W, 190)
plate("S-450", "CC-30", YEL, K, 170)
add("S-500", rc(4, 4, 152, 46, W, 8, K, 3) + pth("M20 46 L20 30 L26 22 L32 30 L32 46 M40 46 L40 20 L46 12 L52 20 L52 46 M60 46 L60 28 L74 28 L74 46 M84 46 L84 34 L96 34 L96 46", K, 4)
    + ci(132, 24, 14, W, RED, 4) + t(132, 29, "40", 13, K, 800) + rc(4, 54, 152, 34, W, 8, RED, 4) + t(80, 78, "PUERTO LOPE", 18, K, 800), 160, 92, 60)
add("S-510", rc(4, 4, 152, 46, W, 8, K, 3) + t(80, 34, "PUERTO LOPE", 18, K, 800) + ln(16, 44, 144, 10, RED, 5, "butt"), 160, 54, 60)
add("S-520", rc(4, 4, 152, 40, BROWN, 8, W, 3) + t(80, 31, "Ebro", 20, W, 800), 160, 48, 52)
add("S-540", rc(4, 4, 152, 60, GREEN, 8, W, 3) + t(80, 26, "PROVINCIA DE", 13, W, 800) + t(80, 52, "LUGO", 22, W, 800), 160, 68, 56)
add("S-570", rc(4, 4, 92, 36, BLUE, 6, W, 3) + t(50, 32, "A-67", 26, W, 800) + rc(4, 44, 92, 72, BLUE, 6, W, 3) + t(50, 68, "km", 20, W, 800) + t(50, 104, "144", 32, W, 800), 100, 120, 44)
add("S-572", rc(4, 4, 92, 36, RED, 6, W, 3) + t(50, 32, "N-204", 22, W, 800) + rc(4, 44, 92, 72, W, 6, RED, 4) + t(50, 68, "km", 20, K, 800) + t(50, 104, "43", 32, K, 800), 100, 120, 44)
add("S-574", rc(30, 2, 40, 136, RED, 3) + t(50, 22, "N-4", 12, W, 800) + t(50, 40, "km", 10, W, 800) + t(50, 56, "510", 15, W, 800), 100, 140, 40)
add("S-600", rc(4, 4, 172, 92, W, 8, K, 4) + rc(64, 12, 52, 20, RED, 2) + t(90, 28, "N-420", 14, W, 800) + t(14, 56, "ALCAÑIZ", 16, K, 800, "start") + t(166, 56, "13", 16, K, 800, "end")
    + t(14, 84, "TERUEL", 22, K, 800, "start") + t(166, 84, "157", 22, K, 800, "end"), 180, 100, 54)
add("S-602", rc(4, 4, 172, 92, BLUE, 8, W, 3) + rc(64, 12, 52, 20, BLUE, 2, W, 2) + t(90, 28, "A-64", 14, W, 800) + t(14, 56, "Pola de Siero", 15, W, 800, "start")
    + t(166, 56, "18", 16, W, 800, "end") + t(14, 84, "Oviedo", 22, W, 800, "start") + t(166, 84, "37", 22, W, 800, "end"), 180, 100, 54)


def module(code, fill, fg, small, big, extra=""):
    add(code, rc(3, 3, 194, 44, fill, 5, "#64748b" if fill in (W, YEL) else W, 2) + t(12, 18, small, 10, fg, 700, "start") + t(12, 38, big, 17, fg, 800, "start")
        + arr([(160, 25), (188, 25)], fg, 4, 9, 7) + extra, 200, 50, 48)


module("S-700", GREEN, W, "calle", "Sierpes")
module("S-710", YEL, K, "estación de", "Chamartín")
module("S-720", ORANGE, K, "estadio", "Las Gaunas")
module("S-730", BROWN, W, "parque del", "Oeste")
module("S-740", W, K, "teatro", "Campoamor")
module("S-750", W, K, "zona", "industrial")
module("S-760", BLUE, W, "", "Valencia  A-3")
module("S-770", W, K, "", "N-401  TOLEDO")

# 5.3.5 complementary panels (white, black border)
def PNL(code, inner, w=160, h=60, px=56):
    add(code, wrect(inner, w, h), w, h, px)


PNL("S-800", t(80, 42, "1000 m", 28, K, 800))
PNL("S-810", t(80, 42, "800 m", 26, K, 800) + pth("M22 42 L30 24 L38 42 Z", K) + pth("M122 42 L130 24 L138 42 Z", K))
PNL("S-820", t(80, 28, "10 m", 18, K, 800) + arr([(50, 44), (110, 44)], K, 4, 10, 7))
PNL("S-821", t(80, 28, "10 m", 18, K, 800) + arr([(110, 44), (50, 44)], K, 4, 10, 7))
PNL("S-830", ln(80, 6, 80, 54, K, 3) + t(42, 28, "10 m", 16, K, 800) + t(120, 28, "25 m", 16, K, 800) + arr([(64, 44), (20, 44)], K, 3.4, 9, 6) + arr([(96, 44), (140, 44)], K, 3.4, 9, 6))
PNL("S-840", t(80, 41, "STOP 150 m", 22, K, 800))
PNL("S-850", pth("M70 54 L70 34 L50 14", K, 9, cap="butt") + pth("M90 34 L70 34", K, 3, cap="butt") + pth("M70 14 L70 34", K, 3, cap="butt"), 140, 60, 50)
PNL("S-860", "")
PNL("S-870a", arr([(66, 46), (94, 16)], K, 7, 16, 12))
PNL("S-870b", arr([(94, 46), (66, 16)], K, 7, 16, 12))
PNL("S-880a", at(truck(), 80, 30, 1.2))
PNL("S-880b", rc(38, 22, 22, 12, K, 2) + ln(60, 30, 70, 30, K, 2.4) + rc(70, 16, 50, 18, K, 1) + ci(46, 38, 4, K) + ci(90, 37, 4, K) + ci(100, 37, 4, K))
PNL("S-880c", at(bus(), 80, 30, 1.4))
PNL("S-880d", at(bike(), 80, 30, 1.2))
PNL("S-880e", at(vmp(), 80, 30, 1.05))
PNL("S-880f", at(vmp(), 58, 30, 0.95) + at(bike(), 100, 30, 1.0))
add("S-890a", rc(3, 3, 154, 54, K, 8, "#64748b", 2) + at(snowflake(W, 16, 3), 56, 30) + at(snowflake(W, 16, 3), 104, 30), 160, 60, 56)
PNL("S-890b", pth("M96 16 Q100 6 112 10 Q124 6 128 18 Q138 20 134 30 L92 30 Q84 26 96 16 Z", K) + "".join(ln(80 - i * 9, 30 + (i % 2) * 4, 74 - i * 9, 44 + (i % 2) * 4, K, 2.4) for i in range(5)))
PNL("S-890c", "".join(ln(28, 16 + i * 6, 70, 16 + i * 6, K, 2.4) for i in range(6)) + at(car_side(), 102, 34, 0.9))
PNL("S-891", at(car_front(), 34, 30, 0.75) + t(84, 26, "1,5 m", 14, K, 800) + arr([(84, 38), (60, 38)], K, 2.4, 7, 5) + arr([(84, 38), (108, 38)], K, 2.4, 7, 5)
    + at(cyclist(), 124, 30, 0.5) + at(cyclist(), 142, 30, 0.5))
PNL("S-892", rc(50, 8, 70, 4, K) + ln(84, 12, 84, 18, K, 3) + at(rc(-22, -9, 44, 18, K, 3) + ci(-22, 0, 7, K), 84, 32, 1, 18))

# 5.3.6 other signs
add("S-900", rc(4, 4, 92, 122, W, 8, RED, 6) + pth("M50 22 Q30 22 32 40 Q24 52 40 56 L48 56 L48 86 L54 86 L54 56 L62 56 Q76 52 68 40 Q70 22 50 22 Z", K)
    + ln(26, 100, 64, 76, K, 3) + pth("M62 74 Q70 66 66 80 Q74 82 62 88 Q54 82 62 74 Z", RED) + t(50, 116, "PELIGRO DE INCENDIO", 7, K, 800), 100, 130)
add("S-910", rc(4, 4, 92, 122, W, 6, BLUE, 8) + rc(38, 34, 24, 76, RED, 6) + rc(42, 24, 10, 12, RED) + pth("M52 28 L66 22", RED, 4), 100, 130)
stars = "".join(t(round(50 + 30 * math.cos(math.radians(30 * i))), round(54 + 30 * math.sin(math.radians(30 * i))), "★", 12, YEL, 400) for i in range(12))
SQ("S-920", stars + t(50, 55, "ESPAÑA", 14, W, 800))
add("S-930", brect(stars + t(50, 55, "PORTUGAL", 11, W, 800), 100, 100) + rc(2, 100, 96, 28, W, 4, "#94a3b8", 2) + t(50, 121, "1 km", 18, K, 800), 100, 130)
add("S-940", "".join(rc(2, 2 + i * 32, 136, 30, BLUE, 3, W, 2) + ci(116, 17 + i * 32, 11, W, RED, 3.5) + t(116, 21 + i * 32, v, 11, K, 800)
                     + t(14, 22 + i * 32, lab, 11, W, 700, "start") for i, (v, lab) in enumerate((("30", "poblado"), ("50", "poblado"), ("90", "carretera"), ("120", "autopista/autovía")))), 140, 132)
V("S-950", rc(14, 12, 72, 64, W, 2) + t(50, 40, "Radio", 16, K, 700) + t(50, 62, "DRS", 16, K, 800) + t(50, 108, "94,6", 24, W, 800))
add("S-960", rc(4, 4, 92, 92, W, 6, BLUE, 8) + pth("M30 26 Q22 34 32 48 L50 66 Q64 78 72 70 L66 62 L58 66 L36 44 L40 36 Z", K) + t(50, 88, "S.O.S.", 13, K, 800))
add("S-970", rc(4, 4, 132, 92, W, 6, BLUE, 8) + rc(22, 26, 18, 56, RED, 5) + rc(26, 18, 8, 10, RED)
    + at(pth("M30 26 Q22 34 32 48 L50 66 Q64 78 72 70 L66 62 L58 66 L36 44 L40 36 Z", K), 44, 0, 0.9) + t(90, 88, "S.O.S.", 12, K, 800), 140, 100)
runner = ci(36, 22, 7, W) + pth("M34 32 L28 56 L40 66 L38 84 M28 56 L14 70 M34 34 L48 46 L58 40 M34 36 L22 44 L14 40", W, 7)
SQ("S-980", runner + rc(68, 14, 22, 72, W), fill="#16a34a")
SQ("S-980a", runner + rc(76, 14, 14, 72, W) + arr([(54, 64), (72, 64)], W, 4, 9, 7), fill="#16a34a")
add("S-990a", rc(2, 2, 150, 96, "#16a34a", 8, W, 2) + at(runner, 6, 2, 0.55) + arr([(48, 28), (82, 28)], W, 4, 9, 7) + rc(92, 10, 12, 44, W) + pth("M120 2 L156 50 L120 98 Z", "#16a34a")
    + t(48, 86, "100m", 26, W, 800), 160, 100, 56)


def radar(c=K):
    return ci(0, 0, 6, c) + "".join(f'<path d="M{6 + i * 6} -10 Q{12 + i * 6} 0 {6 + i * 6} 10" fill="none" stroke="{c}" stroke-width="2.4"/>' for i in range(3))


def vehicles3(c=K, bg=W):
    return at(car_side(c, bg), 0, -16, 0.6) + at(truck(c, bg), 2, 0, 0.62) + at(moto(c, bg), 6, 18, 0.5)


add("S-991a", wrect(at(radar(), 40, 46) + at(vehicles3(), 96, 46), 140, 90, 4), 140, 90, 56)
add("S-991b", brect(at(radar(W), 40, 46) + at(vehicles3(W, BLUE), 96, 46), 140, 90), 140, 90, 56)
add("S-991c", wrect(rc(18, 14, 22, 62, K, 4) + ci(29, 26, 7, RED) + ci(29, 45, 7, "none", W, 1.5) + ci(29, 64, 7, "none", W, 1.5) + at(radar(), 50, 46, 0.8)
                    + at(vehicles3(), 100, 46), 140, 90, 4), 140, 90, 56)
add("S-991d", wrect(f'<g transform="translate(6 23) scale(.45)">{octagon()}{t(50, 59, "STOP", 25, W, 800)}</g>' + at(radar(), 58, 46, 0.8) + at(vehicles3(), 104, 46), 140, 90, 4), 140, 90, 56)
add("S-991e", wrect(f'<g transform="translate(6 23) scale(.45)">{prohib(t(50, 46, "70 m", 17, K, 800))}</g>' + at(radar(), 58, 46, 0.8) + at(vehicles3(), 104, 46), 140, 90, 4), 140, 90, 56)
add("S-991g", rc(3, 3, 134, 84, YEL, 6, K, 2) + pth("M14 26 L52 26 M22 34 L46 34 Q52 34 50 42 L22 42 Q16 36 22 34 Z M32 26 L32 34", K, 3) + rc(18, 56, 22, 6, K, 2) + pth("M14 52 L22 56 M44 52 L36 56", K, 2)
    + at(radar(), 64, 46, 0.8) + at(vehicles3(), 108, 46), 140, 90, 56)


def gap_sign(fill, fg, top="PRECAUCIÓN", mid="COLISIONES", bottom="POR ALCANCES"):
    return (rc(3, 3, 114, 46, fill, 6, fg if fill == W else W, 2.5) + t(60, 18, top, 10, fg, 800) + t(60, 30, mid, 10, fg, 800) + t(60, 42, bottom, 10, fg, 800)
            + rc(3, 52, 114, 58, fill, 6, fg if fill == W else W, 2.5) + t(60, 68, "distancia mínima", 11, fg, 800) + t(60, 80, "entre vehículos", 11, fg, 800)
            + at(car_side(fg, fill), 28, 96, 0.55, fx=True) + t(60, 101, "&lt; &lt;", 14, fg, 800) + at(car_side(fg, fill), 92, 96, 0.55, fx=True))


add("S-992a", gap_sign(W, K), 120, 114, 50)
add("S-992c", gap_sign(BLUE, W), 120, 114, 50)
add("S-992e", rc(3, 3, 114, 46, BLUE, 6, W, 2.5) + t(60, 22, "PRECAUCIÓN", 10, W, 800) + t(60, 36, "CON NIEBLA", 10, W, 800)
    + rc(3, 52, 114, 58, BLUE, 6, W, 2.5) + t(60, 68, "distancia mínima", 11, W, 800) + t(60, 80, "entre vehículos", 11, W, 800)
    + at(car_side(W, BLUE), 26, 96, 0.5, fx=True) + rc(52, 90, 5, 10, ORANGE) + rc(64, 90, 5, 10, RED) + at(car_side(W, BLUE), 94, 96, 0.5, fx=True), 120, 114, 50)
add("S-993", rc(3, 3, 154, 104, YEL, 8, K, 2) + t(80, 26, "ATENCIÓN", 18, RED, 800) + ci(30, 50, 13, W, RED, 3) + t(30, 55, "120", 11, K, 800)
    + ci(124, 48, 13, W, RED, 3) + t(124, 53, "40", 12, K, 800) + pth("M10 96 L150 64 L150 100 L10 100 Z", K) + at(car_side(BLUE, W), 44, 82, 0.6, -13)
    + at(truck(BLUE, W), 112, 66, 0.75, -13), 160, 110, 60)


# ------------------------------------------------------------------------------------------ agents, devices and beaconing
def flag(code, color):
    add(code, ln(30, 10, 30, 92, "#6b7280", 4) + pth("M32 12 L80 20 L80 52 L32 46 Z", color, 1.5, color), 100, 100, 44)


flag("ag-red", RED)
flag("ag-yellow", YEL)
flag("ag-green", "#16a34a")
add("ag-arm", at(moto("#334155"), 32, 60, 1.6) + pth("M36 40 L74 72", "#334155", 6) + rc(70, 68, 10, 8, W, 2, "#334155", 2), 100, 100, 44)
add("ag-light", rc(14, 40, 72, 44, "#e5e7eb", 10, "#64748b", 2) + rc(26, 26, 48, 16, "#1e40af", 5) + ci(38, 34, 6, RED) + ci(62, 34, 6, RED)
    + "".join(ln(50, 22, 50 + 26 * math.cos(math.radians(a)), 22 + 26 * math.sin(math.radians(a)), RED, 2) for a in (-150, -120, -60, -30)), 100, 100, 44)
add("ag-paddle", ln(50, 60, 50, 96, "#6b7280", 5) + f'<g transform="translate(14 0) scale(.72)">{octagon()}{t(50, 59, "STOP", 25, W, 800)}</g>', 100, 100, 44)
add("ag-school", ln(50, 60, 50, 96, "#6b7280", 5) + f'<g transform="translate(14 0) scale(.72)">{prohib(at(ped(), 50, 52, 1.0))}</g>', 100, 100, 44)
add("vms", rc(4, 14, 152, 62, "#111827", 6) + "".join(t(80, 38 + i * 18, s_, 13, "#f59e0b", 700) for i, s_ in enumerate(("RIESGO DE", "INCENDIO"))), 160, 90, 64)
add("dev-barrier", ln(26, 40, 22, 90, "#475569", 4) + ln(74, 40, 78, 90, "#475569", 4) + rc(10, 26, 80, 18, W, 2, "#94a3b8", 1.5)
    + "".join(rc(14 + i * 16, 26, 8, 18, RED) for i in range(5)), 100, 100, 44)
add("dev-boom", rc(10, 40, 14, 50, "#475569", 2) + "".join(rc(24 + i * 14, 44, 7, 8, RED) + rc(31 + i * 14, 44, 7, 8, W) for i in range(5)) + rc(24, 44, 70, 8, "none", 0, "#94a3b8", 1), 100, 100, 44)
add("dev-panel", rc(6, 26, 88, 40, W, 2, "#94a3b8", 1.5) + "".join(pth(f"M{14 + i * 20} 30 L{26 + i * 20} 46 L{14 + i * 20} 62 L{22 + i * 20} 62 L{34 + i * 20} 46 L{22 + i * 20} 30 Z", RED) for i in range(4))
    + ln(30, 66, 26, 90, "#475569", 3) + ln(70, 66, 74, 90, "#475569", 3), 100, 100, 44)
add("dev-cones", "".join(pth(f"M{x} 22 L{x + 12} 82 L{x - 12} 82 Z", "#f97316") + pth(f"M{x - 4} 42 L{x + 4} 42 L{x + 6} 52 L{x - 6} 52 Z", W) + rc(x - 16, 82, 32, 6, K, 1) for x in (30, 72)), 100, 100, 44)
add("dev-redlight", rc(10, 66, 80, 14, W, 2, "#94a3b8", 1) + "".join(rc(14 + i * 26, 66, 12, 14, RED) for i in range(3))
    + "".join(rc(x - 10, 30, 20, 34, "#facc15", 3) + ci(x, 34, 11, RED, "#7f1d1d", 1.5) for x in (26, 74)), 100, 100, 44)
add("dev-yellow", "".join(pth(f"M{x} 40 L{x + 7} 88 L{x - 7} 88 Z", "#f97316") + rc(x - 2, 26, 4, 14, "#64748b") + ci(x, 24, 6, "#facc15", "#a16207", 1.5) for x in (20, 50, 80)), 100, 100, 44)
add("dev-vertice", pth("M20 90 L20 40 Q50 18 80 40 L80 90 Z", "#0f766e") + pth("M30 60 L46 50 L46 70 Z", W) + pth("M70 60 L54 50 L54 70 Z", W), 100, 100, 44)
add("dev-arista", pth("M36 92 L36 14 L64 22 L64 92 Z", W, 1.5, W).replace('fill="#ffffff"', 'fill="#ffffff" stroke="#94a3b8"') + pth("M36 30 L64 38 L64 56 L36 48 Z", K) + rc(44, 36, 12, 14, ORANGE), 100, 100, 44)
add("dev-chevrons", rc(6, 22, 88, 52, "#1e3a8a", 3) + "".join(pth(f"M{30 + i * 22} 30 L{16 + i * 22} 48 L{30 + i * 22} 66 L{40 + i * 22} 66 L{26 + i * 22} 48 L{40 + i * 22} 30 Z", W) for i in range(3))
    + ln(50, 74, 50, 94, "#64748b", 4), 100, 100, 44)
add("dev-catseye", rc(0, 0, 100, 100, "#1f2937") + "".join(ci(20 + i * 18, 80 - i * 14 + (i * i), 3.2, "#fde68a") for i in range(5)) + ln(6, 96, 90, 30, "#9ca3af", 2, extra=' stroke-dasharray="4 8"'), 100, 100, 44)
add("dev-guardrail-refl", rc(6, 40, 88, 14, "#cbd5e1", 3, "#64748b", 1.5) + rc(6, 54, 88, 6, "#94a3b8") + ln(20, 60, 20, 92, "#64748b", 4) + ln(80, 60, 80, 92, "#64748b", 4)
    + rc(44, 36, 12, 22, ORANGE, 2), 100, 100, 44)
add("dev-flat", rc(32, 6, 36, 88, W, 3, "#94a3b8", 1.5) + "".join(pth(f"M32 {18 + i * 20} L68 {6 + i * 20} L68 {16 + i * 20} L32 {28 + i * 20} Z", "#1e3a8a") for i in range(4)), 100, 100, 44)
add("dev-cyl", "".join(rc(x, 26, 14, 62, "#0f766e", 7) + rc(x, 38, 14, 5, W) + rc(x, 50, 14, 5, W) for x in (14, 43, 72)), 100, 100, 44)
add("dev-fogbox", rc(30, 10, 40, 60, "#6b7280", 4) + "".join(ci(40 + (i % 3) * 10, 22 + (i // 3) * 6, 2.4, RED) for i in range(6))
    + "".join(ci(40 + (i % 3) * 10, 46 + (i // 3) * 6, 2.4, "#f59e0b") for i in range(6)) + ln(50, 70, 50, 94, "#6b7280", 4), 100, 100, 44)
add("dev-snowpole", "".join("".join(rc(x, 8 + j * 14, 6, 7, RED if j % 2 == 0 else W, 0, "#94a3b8", 0.6) for j in range(6)) for x in (30, 64)) + rc(0, 92, 100, 8, "#e2e8f0"), 100, 100, 44)
add("dev-rumble", rc(0, 0, 100, 100, ASPH) + rc(26, 0, 10, 100, W) + "".join(rc(44, 6 + i * 9, 30, 4, "#d1d5db") for i in range(10)), 100, 100, 44)
add("dev-windsock", ln(26, 14, 26, 92, "#64748b", 3) + pth("M26 16 L84 26 L84 40 L26 38 Z", RED) + pth("M46 20 L46 40 M64 23 L64 40", W, 8, cap="butt"), 100, 100, 44)
add("dev-gantry", "".join(rc(x, 16, 7, 78, W, 0, "#94a3b8", 1) for x in (8, 85)) + rc(8, 12, 84, 7, W, 0, "#94a3b8", 1)
    + "".join(rc(8 + i * 14, 12, 7, 7, RED) for i in range(6)) + "".join(rc(8, 24 + i * 14, 7, 7, RED) + rc(85, 24 + i * 14, 7, 7, RED) for i in range(5))
    + ci(50, 30, 8, W, RED, 3) + t(50, 33.5, "2,5", 7, K, 800), 100, 100, 44)
add("dev-studs", rc(0, 0, 100, 100, ASPH) + ln(52, 0, 52, 100, W, 3, extra=' stroke-dasharray="12 10"') + "".join(ci(36, 12 + i * 19, 4, c) for i, c in enumerate(("#22c55e", "#22c55e", "#f59e0b", RED, RED))), 100, 100, 44)
add("dev-rail", rc(4, 34, 92, 12, "#cbd5e1", 3, "#64748b", 1.5) + rc(4, 46, 92, 4, "#94a3b8") + "".join(ln(x, 50, x, 92, "#64748b", 4) for x in (16, 50, 84)), 100, 100, 44)
add("dev-pretil", rc(4, 24, 92, 8, "#2563eb", 2) + rc(4, 44, 92, 6, "#2563eb", 2) + "".join(rc(x, 24, 6, 50, "#2563eb") for x in (12, 47, 82)) + rc(0, 74, 100, 20, "#94a3b8"), 100, 100, 44)
add("dev-moto", rc(4, 26, 92, 12, "#cbd5e1", 3, "#64748b", 1.5) + rc(4, 62, 92, 12, "#cbd5e1", 3, "#64748b", 1.5) + "".join(ln(x, 38, x, 62, "#64748b", 4) for x in (16, 50, 84)) + rc(0, 74, 100, 20, ASPH), 100, 100, 44)
add("dev-atten", rc(14, 30, 72, 56, K, 4) + "".join(pth(f"M{20 + i * 22} 30 L{34 + i * 22} 58 L{20 + i * 22} 86 L{30 + i * 22} 86 L{44 + i * 22} 58 L{30 + i * 22} 30 Z", "#facc15") for i in range(3))
    + rc(4, 20, 92, 10, "#cbd5e1", 3, "#64748b", 1), 100, 100, 44)


# ------------------------------------------------------------------------------------------ traffic lights
OFF = "#3f4652"


def housing(lamps, w=36, h=96, x=32, y=2):
    out = rc(x, y, w, h, "#111827", 8)
    n = len(lamps)
    for i, lp in enumerate(lamps):
        cy = y + h * (i + 0.5) / n
        out += ci(x + w / 2, cy, w * 0.36, OFF) + (lp(x + w / 2, cy, w * 0.36) if lp else "")
    return out


def lit(color):
    return lambda cx, cy, r: ci(cx, cy, r, color)


def rays(cx, cy, r, color):
    return "".join(ln(round(cx + math.cos(math.radians(a)) * (r + 4), 1), round(cy + math.sin(math.radians(a)) * (r + 4), 1),
                      round(cx + math.cos(math.radians(a)) * (r + 10), 1), round(cy + math.sin(math.radians(a)) * (r + 10), 1), color, 2.4) for a in (0, 45, 135, 180, 225, 315))


def TL(code, inner, w=100, h=100):
    add(code, inner, w, h, 44)


TL("tl-ped-green", housing([None, lambda x, y, r: at(ped("#22c55e"), x, y, 0.45)]))
TL("tl-ped-flash", housing([None, lambda x, y, r: at(ped("#22c55e"), x, y, 0.45) + rays(x, y, r, "#22c55e")]))
TL("tl-ped-red", housing([lambda x, y, r: at(standing("#ef4444"), x, y, 0.45), None]))
TL("tl-green", housing([None, None, lit("#22c55e")]))
TL("tl-amber", housing([None, lit("#f59e0b"), None]))
TL("tl-red", housing([lit("#ef4444"), None, None]))
TL("tl-flash-red", rc(14, 30, 72, 36, "#111827", 8) + ci(32, 48, 13, "#ef4444") + ci(68, 48, 13, OFF) + rays(32, 48, 13, "#ef4444") + ln(50, 66, 50, 96, "#64748b", 4))
TL("tl-flash-amber", housing([None, lambda x, y, r: ci(x, y, r, "#f59e0b") + rays(x, y, r, "#f59e0b"), None]))
TL("tl-arrow-green", housing([lit("#ef4444"), None, lambda x, y, r: arr([(x - 8, y), (x + 9, y)], "#22c55e", 3.4, 7, 5)]))
TL("tl-arrow-black", housing([lambda x, y, r: ci(x, y, r, "#ef4444") + arr([(x, y + 7), (x, y - 5), (x + 9, y - 5)], K, 3, 6, 4.5), None, None]))
TL("tl-lane-x", rc(14, 14, 72, 72, "#111827", 6) + pth("M28 28 L72 72 M72 28 L28 72", "#ef4444", 4))
TL("tl-lane-diag", rc(14, 14, 72, 72, "#111827", 6) + arr([(30, 30), (68, 68)], "#facc15", 4.5, 12, 9))
TL("tl-lane-down", rc(14, 14, 72, 72, "#111827", 6) + arr([(50, 24), (50, 76)], "#22c55e", 4.5, 12, 9))


def bar(kind):
    def f(x, y, r):
        d = {"h": (x - 9, y, x + 9, y), "v": (x, y - 9, x, y + 9), "l": (x - 7, y - 7, x + 7, y + 7), "r": (x + 7, y - 7, x - 7, y + 7)}[kind]
        return ln(*d, W, 5, "butt")
    return f


TL("tl-bus-h", housing([bar("h"), None, None]))
TL("tl-bus-v", housing([None, None, bar("v")]))
TL("tl-bus-l", housing([None, None, bar("l")]))
TL("tl-bus-r", housing([None, None, bar("r")]))
TL("tl-bus-flash", housing([None, lambda x, y, r: bar("v")(x, y, r) + rays(x, y, r, W), None]))
TL("tl-cycle", housing([lambda x, y, r: at(bike("#ef4444"), x, y, 0.42), lambda x, y, r: at(bike("#f59e0b"), x, y, 0.42), lambda x, y, r: at(bike("#22c55e"), x, y, 0.42)]))


# ------------------------------------------------------------------------------------------ road markings (seen from above, traffic going up)
def MK(code, inner, bg=ASPH):
    add(code, rc(0, 0, 120, 80, bg, 6) + inner, 120, 80, 62)


def vdash(x, w=3, dash="12 9", c=W, y1=0, y2=80):
    return ln(x, y1, x, y2, c, w, "butt", f' stroke-dasharray="{dash}"')


MK("mk-cont", ln(60, 0, 60, 80, W, 3, "butt"))
MK("mk-double", ln(57, 0, 57, 80, W, 3, "butt") + ln(63, 0, 63, 80, W, 3, "butt"))
MK("mk-wide", ln(70, 0, 70, 80, W, 7, "butt") + t(96, 50, "BUS", 13, W, 800))
MK("mk-dash", vdash(60))
MK("mk-dash-short", vdash(60, 3, "12 4"))
MK("mk-dash-wide", vdash(70, 7, "12 9") + t(96, 50, "BUS", 13, W, 800))
MK("mk-cont-dash", ln(57, 0, 57, 80, W, 3, "butt") + vdash(63))
MK("mk-reversible", vdash(42) + vdash(48) + vdash(72) + vdash(78) + arr([(60, 64), (60, 16)], "#e5e7eb", 3, 8, 6) + arr([(60, 16), (60, 64)], "#e5e7eb", 3, 8, 6))
MK("mk-guide", pth("M40 80 Q40 40 0 36", W, 2.5).replace("/>", ' stroke-dasharray="5 4"/>') + pth("M80 80 Q80 40 120 30", W, 2.5).replace("/>", ' stroke-dasharray="5 4"/>')
   + pth("M60 80 L60 0", W, 2.5).replace("/>", ' stroke-dasharray="5 4"/>'))
MK("mk-stop", ln(10, 22, 110, 22, W, 6, "butt") + t(60, 62, "STOP", 26, W, 800))
MK("mk-yield", ln(10, 22, 110, 22, W, 5, "butt", ' stroke-dasharray="10 6"') + pth("M44 36 L76 36 L60 74 Z", W, 3.5) )
MK("mk-zebra", "".join(rc(14 + i * 14, 12, 8, 56, W) for i in range(7)))
MK("mk-cycle", "".join(rc(8 + i * 14, 20, 8, 8, W) + rc(8 + i * 14, 52, 8, 8, W) for i in range(8)))
MK("mk-hump", rc(0, 22, 120, 38, "#374151") + "".join(pth(f"M{8 + i * 36} 58 L{26 + i * 36} 26 L{44 + i * 36} 58 Z", W) for i in range(3)))
MK("mk-yield-tri", pth("M42 8 L78 8 L60 76 Z", W, 4))
MK("mk-stop-word", t(60, 54, "STOP", 32, W, 800))
MK("mk-speed", f'<ellipse cx="60" cy="40" rx="34" ry="30" fill="none" stroke="{W}" stroke-width="6"/>' + t(60, 52, "30", 32, W, 800))
MK("mk-reserved", at(bike(W, ASPH), 40, 44, 1.2) + at(vmp(W, ASPH), 86, 40, 0.95) + vdash(110, 3, "8 6"))
MK("mk-lane-arrows", vdash(40) + vdash(80) + arr([(20, 72), (20, 14)], W, 4, 10, 7) + carr("M60 72 L60 40 Q60 28 50 24", (40, 20), (50, 24), W, 4, 10, 7) + arr([(100, 72), (100, 14)], W, 4, 10, 7))
MK("mk-exit", ln(30, 0, 30, 80, W, 3, "butt") + vdash(80) + arr([(56, 74), (56, 18)], W, 4, 10, 7) + arr([(64, 60), (98, 22)], W, 4, 10, 7))
MK("mk-endlane", vdash(60) + carr("M86 76 L86 52 Q86 40 70 34", (56, 28), (70, 34), W, 5, 12, 9))
MK("mk-return", ln(60, 0, 60, 34, W, 3, "butt") + vdash(60, 3, "8 6", W, 34, 80) + carr("M50 76 Q50 50 64 40", (74, 36), (64, 40), W, 4, 10, 7) + arr([(80, 74), (80, 30)], "#e5e7eb", 2, 6, 4))
MK("mk-rbt-arrows", "".join(at(a, x, 40) for a, x in ((arr([(0, 28), (0, -24)], W, 3.4, 8, 6), 22), (carr("M0 28 L0 0 Q0 -14 -10 -18", (-18, -22), (-10, -18), W, 3.4, 8, 6), 52),
                                                         (carr("M0 28 L0 -4 Q0 -16 10 -18", (18, -22), (10, -18), W, 3.4, 8, 6), 84))))
MK("mk-minirbt", ci(60, 40, 18, "none", W, 4) + carr("M28 54 Q20 36 34 20", (42, 14), (34, 20), W, 3, 8, 6) + carr("M92 26 Q100 44 86 60", (78, 66), (86, 60), W, 3, 8, 6))
MK("mk-bifurcation", pth("M30 76 L60 20 L90 76 L74 76 L60 48 L46 76 Z", W) + ln(10, 0, 10, 80, W, 3) + ln(110, 0, 110, 80, W, 3))
MK("mk-pn", ln(42, 16, 78, 64, W, 6, "butt") + ln(78, 16, 42, 64, W, 6, "butt") + t(24, 52, "P", 26, W, 800) + t(96, 52, "N", 26, W, 800))
MK("mk-bus", t(60, 54, "BUS", 30, W, 800) + vdash(110, 3, "8 6"))
MK("mk-res-start", ln(110, 0, 110, 80, W, 3) + "".join(ln(110, 20 + i * 18, 30 + i * 12, 8 + i * 18, W, 5, "butt") for i in range(4)))
MK("mk-cycleway", rc(14, 0, 92, 80, "#b4472f") + ln(14, 0, 14, 80, W, 4) + ln(106, 0, 106, 80, W, 4) + at(bike(W, "#b4472f"), 60, 42, 1.5))
MK("mk-park-line", rc(0, 0, 12, 80, "#cbd5e1") + "".join(ln(12, y, 40, y, W, 2.5) for y in (4, 40, 76)) + ln(40, 4, 40, 76, W, 2.5) + rc(16, 46, 20, 26, "#1d4ed8", 5) + rc(16, 8, 20, 28, "#b45309", 5))
MK("mk-park-battery", ln(0, 10, 120, 10, "#cbd5e1", 4) + "".join(ln(x, 10, x, 60, W, 2.5) for x in (20, 50, 80, 110)) + at(car_front(), 35, 38, 0.6) + at(car_front(), 65, 38, 0.6))
MK("mk-park-diag", ln(0, 10, 120, 10, "#cbd5e1", 4) + "".join(ln(x, 10, x - 26, 62, W, 2.5) for x in (40, 70, 100, 130)))
MK("mk-hatch", pth("M20 70 L60 10 L100 70 Z", W, 3) + "".join(ln(36 + i * 10, 64, 52 + i * 10, 40, W, 3, "butt") for i in range(5)))
MK("mk-edge", ln(14, 0, 14, 80, W, 4, "butt") + ln(106, 0, 106, 80, W, 4, "butt") + vdash(60) + rc(0, 0, 10, 80, "#9ca3af") + rc(110, 0, 10, 80, "#9ca3af"))
MK("mk-orient", t(60, 34, "M-50", 22, W, 800) + t(60, 66, "SOLO", 22, W, 800))
MK("mk-chevrons", "".join(pth(f"M40 {y + 10} L60 {y} L80 {y + 10}", W, 5, cap="butt") for y in (10, 40)) + vdash(10) + vdash(110))
MK("mk-avanza", ln(10, 16, 110, 16, W, 4, "butt") + ln(10, 66, 110, 66, W, 4, "butt") + at(moto(W, ASPH), 38, 42, 0.8) + at(bike(W, ASPH), 84, 42, 0.8))
MK("mk-dragon", ln(60, 0, 60, 80, W, 3, "butt") + "".join(pth(f"M10 {y} L30 {y} L20 {y + 10} Z", W) + pth(f"M90 {y} L110 {y} L100 {y + 10} Z", W) for y in (6, 30, 54)))
MK("mk-broken-edge", pth("M14 0 L26 10 L14 20 L26 30 L14 40 L26 50 L14 60 L26 70 L14 80", W, 3) + pth("M106 0 L94 10 L106 20 L94 30 L106 40 L94 50 L106 60 L94 70 L106 80", W, 3) + vdash(60))
MK("mk-damero", "".join(rc(10 + c_ * 10, 10 + r_ * 10, 10, 10, W) for r_ in range(6) for c_ in range(10) if (r_ + c_) % 2 == 0))
MK("mk-moto-guide", pth("M30 80 Q36 30 90 0", W, 3) + "".join(ln(34 + i * 6, 70 - i * 15, 58 + i * 10, 74 - i * 17, W, 3, "butt") for i in range(4)))
MK("mk-zbe", t(60, 54, "ZBE", 32, W, 800))
MK("mk-y-zigzag", ln(108, 0, 108, 80, "#cbd5e1", 4) + pth("M96 4 L70 14 L96 24 L70 34 L96 44 L70 54 L96 64 L70 74", "#facc15", 3))
MK("mk-y-cont", rc(104, 0, 16, 80, "#cbd5e1") + ln(102, 0, 102, 80, "#facc15", 5, "butt"))
MK("mk-y-dash", rc(104, 0, 16, 80, "#cbd5e1") + ln(102, 0, 102, 80, "#facc15", 5, "butt", ' stroke-dasharray="12 9"'))
def diag_grid(x0, y0, x1, y1, step, c, w):
    """Criss-cross diagonals clipped to the box (x0, y0)-(x1, y1), without clipPath ids."""
    out = []
    for sgn in (1, -1):
        k = -(x1 - x0) - (y1 - y0)
        while k <= (x1 - x0) + (y1 - y0):
            pts = []
            # line: (y - y0) = sgn * (x - x0) + k  -> clip against the four sides
            for x in (x0, x1):
                y = y0 + sgn * (x - x0) + k
                if y0 <= y <= y1:
                    pts.append((x, y))
            for y in (y0, y1):
                x = x0 + (y - y0 - k) * sgn
                if x0 <= x <= x1:
                    pts.append((x, y))
            pts = sorted(set((round(a, 1), round(b, 1)) for a, b in pts))
            if len(pts) >= 2:
                out.append(ln(pts[0][0], pts[0][1], pts[-1][0], pts[-1][1], c, w, "butt"))
            k += step
    return "".join(out)


MK("mk-y-grid", diag_grid(16, 8, 104, 72, 14, "#facc15", 2) + rc(16, 8, 88, 64, "none", 0, "#facc15", 3))
MK("mk-redwhite", "".join(rc(10 + c_ * 10, 16 + r_ * 12, 10, 12, RED if (r_ + c_) % 2 else W) for r_ in range(4) for c_ in range(10)))
MK("mk-blue", ln(10, 0, 10, 80, "#cbd5e1", 4) + "".join(ln(34, y, 54, y, "#38bdf8", 4) for y in (6, 74)) + ln(54, 6, 54, 74, "#38bdf8", 4, "butt", ' stroke-dasharray="10 6"'))
