# -*- coding: utf-8 -*-
"""Original SVG diagrams for Topic 1 (EN/ES). No third-party artwork is used."""

from svgkit import FONT, NAVY, TEAL, AMBER, RED, SLATE, BLUE, INK, svg, txt, lines, box  # noqa: F401


# ---------------------------------------------------------------- D1 tree
def tree(lang):
    T = {
        "en": dict(
            root=["ROAD", "USERS"],
            ped="Pedestrians",
            pedn=["on foot · pushing a pram · walking beside", "a bike or moped · wheelchair users"],
            ani="Animals",
            anin=["ridden, herded or pulling a vehicle"],
            veh="Vehicles",
            nm="Without motor",
            nms="cycles, trailers, caravans",
            nc="Not counted as motor",
            ncs="EPAC, mopeds, VMP, trams",
            mo="Motor vehicles",
            mos="engine-propelled",
            au="Automóviles",
            aus="cars, buses, trucks",
            ve="Special vehicles",
            ves="tractors, cranes…",
        ),
        "es": dict(
            root=["USUARIOS", "DE LA VÍA"],
            ped="Peatones",
            pedn=["a pie · empujando un cochecito · llevando", "a mano una bici o ciclomotor · sillas de ruedas"],
            ani="Animales",
            anin=["montados, conducidos o tirando de un vehículo"],
            veh="Vehículos",
            nm="Sin motor",
            nms="ciclos, remolques, caravanas",
            nc="No considerados de motor",
            ncs="EPAC, ciclomotores, VMP, tranvía",
            mo="De motor",
            mos="propulsados por motor",
            au="Automóviles",
            aus="turismos, autobuses…",
            ve="Vehículos especiales",
            ves="tractores, grúas…",
        ),
    }[lang]
    p = []
    p.append(box(8, 205, 118, 64, NAVY, T["root"]))
    p.append(f'<path d="M126 237 H143 M143 43 V313 M143 43 H160 M143 118 H160 M143 313 H160" stroke="{SLATE}" stroke-width="1.6" fill="none"/>')
    p.append(box(160, 20, 150, 46, TEAL, T["ped"]))
    p.append(lines(325, 40, T["pedn"], 10.5, 400, SLATE))
    p.append(box(160, 95, 150, 46, TEAL, T["ani"]))
    p.append(lines(325, 122, T["anin"], 10.5, 400, SLATE))
    p.append(box(160, 290, 150, 46, NAVY, T["veh"]))
    p.append(f'<path d="M310 313 H330 M330 210 V370 M330 210 H350 M330 290 H350 M330 370 H350" stroke="{SLATE}" stroke-width="1.6" fill="none"/>')
    p.append(box(350, 185, 190, 50, "#dbeafe", T["nm"], T["nms"], tcolor=NAVY, scolor=SLATE, stroke="#93c5fd"))
    p.append(box(350, 265, 190, 50, "#fef3c7", T["nc"], T["ncs"], tcolor="#7c2d12", scolor=SLATE, stroke="#fcd34d"))
    p.append(box(350, 345, 190, 50, AMBER, T["mo"], T["mos"], tcolor="#fff", scolor="#ffedd5"))
    p.append(f'<path d="M540 370 H558 M555 342 V407 M555 342 H570 M555 407 H570" stroke="{SLATE}" stroke-width="1.6" fill="none"/>')
    p.append(box(570, 320, 145, 44, "#ffedd5", T["au"], T["aus"], tcolor="#7c2d12", scolor=SLATE, stroke="#fb923c", size=12))
    p.append(box(570, 385, 145, 44, "#ffedd5", T["ve"], T["ves"], tcolor="#7c2d12", scolor=SLATE, stroke="#fb923c", size=12))
    return svg(720, 440, "".join(p), "Classification of road users")


# ---------------------------------------------------------------- D2 speed ladder
def ladder(lang):
    T = {
        "en": dict(
            axis="design / cut-off speed (km/h)",
            r=[
                ("Personal mobility", "vehicle (VMP)", "6 – 25 km/h design speed · electric only"),
                ("Pedal-assist bicycle", "(EPAC)", "assistance cuts out before 25 km/h · ≤ 250 W"),
                ("Ciclo de motor", "(EU class L1e-A)", "assistance cuts out at ≤ 25 km/h · ≤ 1,000 W"),
                ("Moped · light", "quadricycle", "≤ 45 km/h by construction · 50 cm³ (4 kW)"),
                ("Motorcycle and", "other motor vehicles", ["&gt; 45 km/h", "and/or &gt; 50 cm³"]),
            ],
        ),
        "es": dict(
            axis="velocidad de diseño / de corte (km/h)",
            r=[
                ("Vehículo de movilidad", "personal (VMP)", "6 – 25 km/h de velocidad de diseño · solo eléctrico"),
                ("Bicicleta de pedaleo", "asistido (EPAC)", "la asistencia se corta antes de 25 km/h · ≤ 250 W"),
                ("Ciclo de motor", "(clase UE L1e-A)", "la asistencia se corta a ≤ 25 km/h · ≤ 1.000 W"),
                ("Ciclomotor ·", "cuatriciclo ligero", "≤ 45 km/h por construcción · 50 cm³ (4 kW)"),
                ("Motocicleta y", "resto de automóviles", ["&gt; 45 km/h", "y/o &gt; 50 cm³"]),
            ],
        ),
    }[lang]
    x0, sc = 190, 8  # 0 km/h at x=190; 8 px per km/h
    X = lambda v: x0 + v * sc
    p = []
    for v in (6, 25, 45):
        p.append(f'<line x1="{X(v)}" y1="30" x2="{X(v)}" y2="{46+5*50}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 4"/>')
        p.append(txt(X(v), 24, str(v), 12, 700, NAVY, "middle"))
    colors = [TEAL, BLUE, "#4f46e5", AMBER, RED]
    ends = [(6, 25), (0, 25), (0, 25), (0, 45), (45, 60)]
    top, rh = 46, 50
    for i, (n1, n2, note) in enumerate(T["r"]):
        y = top + i * rh
        p.append(txt(8, y + 17, n1, 11.5, 700, INK))
        p.append(txt(8, y + 31, n2, 11, 400, SLATE))
        a, b = ends[i]
        p.append(f'<rect x="{X(a)}" y="{y+6}" width="{(b-a)*sc}" height="30" rx="6" fill="{colors[i]}"/>')
        if i == 4:
            p.append(f'<path d="M{X(60)} {y+6} L{X(60)+22} {y+21} L{X(60)} {y+36} Z" fill="{colors[i]}"/>')
            p.append(lines(X(45) + 8, y + 18, note, 10.5, 700, "#fff", "start", 13))
        elif i == 3:
            p.append(txt(X(0) + 10, y + 26, note, 11, 600, "#fff"))
        else:
            p.append(txt(X(b) + 10, y + 26, note, 11, 500, INK))
    p.append(f'<line x1="{x0}" y1="{top+5*rh+4}" x2="{X(60)+22}" y2="{top+5*rh+4}" stroke="{SLATE}" stroke-width="1.5"/>')
    p.append(txt(x0, top + 5 * rh + 22, "0", 10.5, 400, SLATE, "middle"))
    p.append(txt(x0 + 520, top + 5 * rh + 22, T["axis"], 10.5, 400, SLATE, "end"))
    return svg(720, 330, "".join(p), "Speed and power ladder of light vehicles")


# ---------------------------------------------------------------- D3 masses
def masses(lang):
    T = {
        "en": dict(
            names=[("Tara", "unladen mass"), ("Masa en orden de marcha", "running-order mass"), ("Masa en carga", "loaded mass")],
            seg1=["vehicle + fixed", "equipment + normal", "supplies"],
            seg2="+ driver 75 kg",
            seg3=["+ passengers", "+ luggage / cargo"],
            mma="MMA: maximum authorised mass (never exceed)",
            ax=("Axle mass", ["weight resting on the road", "through one axle's wheels"]),
            co=("Combination MMA", ["maximum mass of the motor", "vehicle + its trailer, loaded"]),
        ),
        "es": dict(
            names=[("Tara", "masa en vacío"), ("Masa en orden de marcha", "tara + conductor"), ("Masa en carga", "vehículo + pasajeros y carga")],
            seg1=["vehículo + equipo", "fijo + dotación", "normal"],
            seg2="+ conductor 75 kg",
            seg3=["+ pasajeros", "+ equipaje / carga"],
            mma="MMA: masa máxima autorizada (no se puede superar)",
            ax=("Masa por eje", ["la que gravita sobre el suelo", "por las ruedas de un eje"]),
            co=("MMA del conjunto", ["masa máxima del vehículo de", "motor con carga + su remolque"]),
        ),
    }[lang]
    p = []
    base = 270
    cols = [40, 200, 360]
    w = 120
    c_tara, c_drv, c_load = "#1e3a5f", "#3b82f6", "#bfdbfe"
    # tara
    p.append(f'<rect x="{cols[0]}" y="{base-110}" width="{w}" height="110" fill="{c_tara}" rx="4"/>')
    p.append(lines(cols[0] + w / 2, base - 70, T["seg1"], 10.5, 500, "#fff", "middle", 14))
    # running order
    p.append(f'<rect x="{cols[1]}" y="{base-110}" width="{w}" height="110" fill="{c_tara}" rx="4"/>')
    p.append(f'<rect x="{cols[1]}" y="{base-132}" width="{w}" height="22" fill="{c_drv}" rx="4"/>')
    p.append(txt(cols[1] + w / 2, base - 117, T["seg2"], 10.5, 700, "#fff", "middle"))
    p.append(lines(cols[1] + w / 2, base - 70, T["seg1"], 10.5, 500, "#fff", "middle", 14))
    # loaded
    p.append(f'<rect x="{cols[2]}" y="{base-110}" width="{w}" height="110" fill="{c_tara}" rx="4"/>')
    p.append(f'<rect x="{cols[2]}" y="{base-132}" width="{w}" height="22" fill="{c_drv}" rx="4"/>')
    p.append(txt(cols[2] + w / 2, base - 117, T["seg2"], 10.5, 700, "#fff", "middle"))
    p.append(f'<rect x="{cols[2]}" y="{base-217}" width="{w}" height="85" fill="{c_load}" rx="4" stroke="{c_drv}"/>')
    p.append(lines(cols[2] + w / 2, base - 70, T["seg1"], 10.5, 500, "#fff", "middle", 14))
    p.append(lines(cols[2] + w / 2, base - 178, T["seg3"], 11, 600, NAVY, "middle", 15))
    # MMA line
    p.append(f'<line x1="20" y1="{base-232}" x2="500" y2="{base-232}" stroke="{RED}" stroke-width="2" stroke-dasharray="7 5"/>')
    p.append(txt(20, base - 240, T["mma"], 11, 700, RED))
    # baseline + labels
    p.append(f'<line x1="20" y1="{base}" x2="500" y2="{base}" stroke="{SLATE}" stroke-width="1.5"/>')
    for i, (a, b) in enumerate(T["names"]):
        p.append(txt(cols[i] + w / 2, base + 18, a, 11.5, 700, INK, "middle"))
        p.append(txt(cols[i] + w / 2, base + 33, b, 10, 400, SLATE, "middle"))
    # side notes
    p.append(f'<rect x="525" y="60" width="185" height="62" rx="8" fill="#f1f5f9" stroke="#cbd5e1"/>')
    p.append(txt(535, 80, T["ax"][0], 11.5, 700, NAVY))
    p.append(lines(535, 96, T["ax"][1], 10, 400, SLATE, "start", 13))
    p.append(f'<rect x="525" y="140" width="185" height="62" rx="8" fill="#f1f5f9" stroke="#cbd5e1"/>')
    p.append(txt(535, 160, T["co"][0], 11.5, 700, NAVY))
    p.append(lines(535, 176, T["co"][1], 10, 400, SLATE, "start", 13))
    return svg(720, 320, "".join(p), "How vehicle masses build up")


# ---------------------------------------------------------------- D4 categories
def categories(lang):
    T = {
        "en": dict(
            fam=["N · goods", "O · trailers", "M · passengers"],
            m2="M2: &gt; 8 seats + driver, ≤ 5 t",
            m3="M3: &gt; 8 seats + driver, &gt; 5 t",
            m1="M1: up to 8 seats besides the driver, any mass",
            unit="maximum authorised mass (tonnes)",
        ),
        "es": dict(
            fam=["N · mercancías", "O · remolques", "M · personas"],
            m2="M2: &gt; 8 plazas + conductor, ≤ 5 t",
            m3="M3: &gt; 8 plazas + conductor, &gt; 5 t",
            m1="M1: hasta 8 plazas además del conductor, cualquier masa",
            unit="masa máxima autorizada (toneladas)",
        ),
    }[lang]
    x0, sc = 120, 600 / 14.0
    X = lambda t: x0 + t * sc
    p = []

    def seg(x1, x2, y, fill, label, arrow=False, tc="#fff"):
        out = f'<rect x="{x1}" y="{y}" width="{x2-x1}" height="34" fill="{fill}" stroke="#fff" stroke-width="2"/>'
        if arrow:
            out += f'<path d="M{x2} {y} L{x2+18} {y+17} L{x2} {y+34} Z" fill="{fill}"/>'
        out += txt((x1 + x2) / 2, y + 22, label, 11.5, 700, tc, "middle")
        return out

    # N
    y = 40
    p.append(txt(8, y + 22, T["fam"][0], 12, 700, AMBER))
    p.append(seg(X(0), X(3.5), y, "#d97706", "N1 ≤ 3.5 t"))
    p.append(seg(X(3.5), X(12), y, "#b45309", "N2: &gt; 3.5 t up to 12 t"))
    p.append(seg(X(12), X(14), y, "#78350f", "N3", True))
    # O
    y = 100
    p.append(txt(8, y + 22, T["fam"][1], 12, 700, TEAL))
    p.append(seg(X(0), X(0.75), y, "#14b8a6", "O1"))
    p.append(seg(X(0.75), X(3.5), y, "#0d9488", "O2"))
    p.append(seg(X(3.5), X(10), y, "#0f766e", "O3: &gt; 3.5 t up to 10 t"))
    p.append(seg(X(10), X(14), y, "#115e59", "O4 &gt; 10 t", True))
    # M
    y = 160
    p.append(txt(8, y + 22, T["fam"][2], 12, 700, BLUE))
    p.append(seg(X(0), X(5), y, "#3b82f6", T["m2"]))
    p.append(seg(X(5), X(14), y, "#1d4ed8", T["m3"], True))
    p.append(txt(x0, y + 56, T["m1"], 11, 500, NAVY))
    # labels above bars for tiny O1/O2 clarity
    p.append(txt(X(0.375), 94, "≤ 0.75", 9.5, 600, TEAL, "middle"))
    p.append(txt(X(2.125), 94, "0.75 – 3.5", 9.5, 600, TEAL, "middle"))
    # axis
    ay = 250
    p.append(f'<line x1="{X(0)}" y1="{ay}" x2="{X(14)+18}" y2="{ay}" stroke="{SLATE}" stroke-width="1.5"/>')
    for t in (0, 0.75, 3.5, 5, 10, 12):
        p.append(f'<line x1="{X(t)}" y1="{ay-4}" x2="{X(t)}" y2="{ay+4}" stroke="{SLATE}" stroke-width="1.5"/>')
        p.append(txt(X(t), ay + 18, ("%g" % t), 10.5, 600, SLATE, "middle"))
    p.append(txt(716, ay + 36, T["unit"], 10.5, 400, SLATE, "end"))   # inside the 720 canvas
    return svg(720, 300, "".join(p), "Vehicle categories M, N and O by mass")


# ---------------------------------------------------------------- D5 coupling
def coupling(lang):
    T = {
        "en": dict(
            t1="Road train (tren de carretera) = motor vehicle HITCHED to a trailer",
            n1="the trailer carries its own weight on its own axles",
            t2="Articulated vehicle = tractor unit COUPLED to a semi-trailer",
            n2="part of the semi-trailer's weight rests on the tractor",
        ),
        "es": dict(
            t1="Tren de carretera = vehículo de motor ENGANCHADO a un remolque",
            n1="el remolque soporta su propio peso con sus propios ejes",
            t2="Vehículo articulado = tractocamión ACOPLADO a un semirremolque",
            n2="parte del peso del semirremolque descansa sobre el tractocamión",
        ),
    }[lang]
    p = []

    def wheel(cx, cy):
        return (f'<circle cx="{cx}" cy="{cy}" r="12" fill="#1f2937"/>'
                f'<circle cx="{cx}" cy="{cy}" r="4.5" fill="#cbd5e1"/>')

    # --- top: road train
    p.append(txt(10, 22, T["t1"], 12.5, 700, NAVY))
    p.append(txt(10, 38, T["n1"], 10.5, 400, SLATE))
    y = 55
    p.append(f'<rect x="40" y="{y+22}" width="52" height="46" rx="7" fill="{NAVY}"/>')
    p.append(f'<rect x="98" y="{y+10}" width="120" height="58" rx="4" fill="#94a3b8"/>')
    p.append(wheel(66, y + 74) + wheel(150, y + 74) + wheel(190, y + 74))
    p.append(f'<line x1="218" y1="{y+60}" x2="262" y2="{y+60}" stroke="{RED}" stroke-width="5"/>')
    p.append(f'<circle cx="218" cy="{y+60}" r="5" fill="{RED}"/>')
    p.append(f'<rect x="262" y="{y+10}" width="250" height="58" rx="4" fill="#cbd5e1" stroke="#94a3b8"/>')
    p.append(wheel(300, y + 74) + wheel(470, y + 74) + wheel(498, y + 74))
    p.append(txt(387, y + 44, "REMOLQUE" if lang == "es" else "TRAILER", 12, 700, SLATE, "middle"))
    # --- bottom: articulated
    y2 = 222
    p.append(txt(10, 180, T["t2"], 12.5, 700, NAVY))
    p.append(txt(10, 196, T["n2"], 10.5, 400, SLATE))
    p.append(f'<rect x="40" y="{y2+22}" width="52" height="46" rx="7" fill="{NAVY}"/>')
    p.append(f'<rect x="92" y="{y2+52}" width="86" height="16" fill="#475569"/>')
    p.append(wheel(66, y2 + 74) + wheel(128, y2 + 74) + wheel(156, y2 + 74))
    p.append(f'<rect x="108" y="{y2+4}" width="404" height="52" rx="4" fill="#cbd5e1" stroke="#94a3b8"/>')
    p.append(wheel(450, y2 + 74) + wheel(478, y2 + 74) + wheel(506, y2 + 74))
    p.append(txt(330, y2 + 36, "SEMIRREMOLQUE" if lang == "es" else "SEMI-TRAILER", 12, 700, SLATE, "middle"))
    p.append(f'<circle cx="140" cy="{y2+57}" r="5" fill="{RED}"/>')
    p.append(f'<path d="M140 {y2-18} V{y2+44}" stroke="{RED}" stroke-width="2.5" fill="none"/>')
    p.append(f'<path d="M133 {y2+36} L140 {y2+47} L147 {y2+36} Z" fill="{RED}"/>')
    return svg(720, 328, "".join(p), "Trailer versus semi-trailer")
