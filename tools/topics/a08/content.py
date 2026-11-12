# -*- coding: utf-8 -*-
"""Category A1/A2, Topic 8 content (signs and signals), bilingual. Every text is a (EN, ES) pair.

The A1/A2 course's Tema 8 (Las señales) teaches the same catalogue of signs, in the same order, as the Category B
course. A sign means the same whatever you ride, so this page takes the catalogue (general rules, agents, beaconing,
traffic lights, vertical signs and road markings) from Category B, Topic 8 — one source of truth for every sign — and
adds what singles out motorcycles and mopeds: the no-entry signs that stop one and not the other, the carriageway and
lane signs that sort two-wheelers, the advanced stop box and the guidance marks in bends. Those additions are marked
"On two wheels" inside the catalogue and collected in section 9.

The rules come from the Reglamento General de Circulación (RD 1428/2003, Título IV and Anexo I) with the official sign
catalogue approved by RD 465/2025 (in force 1 July 2025) and the reform made by RD 518/2026 (in force 1 October 2026),
and from the definitions of the Ley sobre Tráfico (RDL 6/2015, Anexo I), as they stand in November 2026.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from ..b08 import content as B8
from ..b08.signs import ICON
from .diagrams import entry_matrix, advance_box, guide_marks


# ------------------------------------------------------------------------------------------ helpers
def _h3(B, start):
    for i, b in enumerate(B):
        if b[0] == "h3" and b[1]["en"].startswith(start):
            return i
    raise KeyError(f"Topic B8 has no heading starting with {start!r}")


def _after_table(B, start, new):
    """Insert the blocks `new` after the first table of the subsection whose English title starts with `start`."""
    i = _h3(B, start)
    for j in range(i + 1, len(B)):
        if B[j][0] in ("h2", "h3"):
            break
        if B[j][0] == "table":
            B[j + 1:j + 1] = new
            return
    raise KeyError(f"No table under {start!r}")


def _row(code, en, es, moto_en, moto_es, moped_en, moped_es, icon=None):
    """A row of the section 9 table: the drawing with its code and a short name under it, then the two verdicts."""
    ic = ICON[icon or code]
    head = f"<b>{B8.nw(code)}</b><br>" if code[:2] in ("R-", "S-") else ""
    cell = '<div style="text-align:center;font-size:.9em;line-height:1.3">%s%s</div>'
    return [T(ic + cell % (head, en), ic + cell % (head, es)), T(moto_en, moto_es), T(moped_en, moped_es)]


TWO = ("On two wheels", "Sobre dos ruedas")


def blocks():
    src = B8.blocks()
    assert src[0][0] == "box", "Topic B8 should open with its ‘what this topic is about’ box"
    end = next(i for i, b in enumerate(src) if b[0] == "h2" and b[1] == "9")
    B = src[1:end]
    closing = src[end:]
    traps_b8 = next(b for b in closing if b[0] == "box")
    numbers_b8 = next(b for b in closing if b[0] == "table")

    # ---------------------------------------------------------------- how to use
    intro = ("box", "key", T("What this topic is really about", "De qué va realmente este tema"), list(src[0][3][:2]) + [
        T("A sign means the same whatever you ride, so sections <b>1 to 8</b> are the <b>same catalogue</b> as Category B, Topic 8, in the order of your A1/A2 course "
          "(its section 5, vertical signs, is split here into <b>5 warning</b>, <b>6 regulatory</b> and <b>7 indication</b> signs; its section 6, road markings, is section <b>8</b>). "
          "The sign drawings are our own simplified versions of the official catalogue (RD 465/2025, in force since 1 July 2025).",
          "Una señal significa lo mismo conduzcas lo que conduzcas, así que los apartados <b>1 a 8</b> son el <b>mismo catálogo</b> que el Tema 8 del permiso B, en el orden de tu curso A1/A2 "
          "(su apartado 5, señales verticales, se divide aquí en <b>5 advertencia</b>, <b>6 reglamentación</b> y <b>7 indicación</b>; su apartado 6, marcas viales, es aquí el <b>8</b>). "
          "Los dibujos de las señales son versiones simplificadas propias del catálogo oficial (RD 465/2025, vigente desde el 1 de julio de 2025)."),
        T("What changes on a motorcycle or a moped is flagged <b>“On two wheels”</b> and collected in <b>section 9</b>: which no-entry signs stop a motorcycle and which stop a moped, "
          "the carriageway and lane signs that sort two-wheelers, the <b>advanced stop box</b> and the <b>guidance marks</b> in bends. If you already know the Category B page, go straight there. "
          "Spanish exam terms are in <i>italics</i>, and a glossary closes the topic.",
          "Lo que cambia en moto o en ciclomotor va marcado como <b>«Sobre dos ruedas»</b> y reunido en el <b>apartado 9</b>: qué señales de prohibición de entrada detienen a una motocicleta y cuáles a un ciclomotor, "
          "las señales de calzada y de carril que distinguen a los vehículos de dos ruedas, la <b>zona de espera adelantada</b> (avanza-motos) y las <b>marcas de guiado</b> en curvas. Si ya conoces la página del permiso B, ve directamente allí. "
          "Al final hay un glosario español–inglés."),
    ])
    B.insert(0, intro)

    # ---------------------------------------------------------------- 6.3 no-entry signs
    _after_table(B, "6.3 ", [
        FIG(entry_matrix, "Read the pictogram, not the red ring: a moped is not a “motor vehicle” in law, so only R-100, R-101 and R-105 stop it; a motorcycle is stopped by R-100, R-101, R-102 and R-104.",
            "Fíjate en el pictograma, no en el borde rojo: el ciclomotor no es «vehículo de motor» en la ley, así que solo lo detienen la R-100, la R-101 y la R-105; a la motocicleta la detienen la R-100, la R-101, la R-102 y la R-104."),
        BOX("trap", f"{TWO[0]}: motor vehicle, motorcycle or moped?", f"{TWO[1]}: ¿vehículo de motor, motocicleta o ciclomotor?", [
            ("The Traffic Law’s definition of <b>motor vehicle</b> (<i>vehículo de motor</i>) <b>leaves out mopeds</b>. So <b>R-102</b> and <b>R-103</b>, which ban “motor vehicles”, do not stop a moped; the sign that stops it is <b>R-105</b>.",
             "La definición de <b>vehículo de motor</b> de la Ley de Tráfico <b>excluye a los ciclomotores</b>. Por eso la <b>R-102</b> y la <b>R-103</b>, que prohíben «vehículos de motor», no detienen a un ciclomotor; la señal que lo detiene es la <b>R-105</b>."),
            ("<b>R-102</b> (car above motorcycle) stops <b>every motorcycle</b>. <b>R-103</b> (car only) lets through <b>two-wheeled motorcycles</b> and three-wheelers treated as motorcycles. "
             "<b>R-104</b> (motorcycle only) stops exactly those two.",
             "La <b>R-102</b> (turismo sobre motocicleta) detiene a <b>todas las motocicletas</b>. La <b>R-103</b> (solo turismo) deja pasar a las <b>motocicletas de dos ruedas</b> y a los vehículos de tres ruedas asimilados. "
             "La <b>R-104</b> (solo motocicleta) detiene precisamente a esos dos."),
            ("<b>R-100</b> and <b>R-101</b> stop everybody, whatever you ride: R-100 closes the road to vehicles <b>in both directions</b>; R-101 forbids <b>entry</b> to every vehicle.",
             "La <b>R-100</b> y la <b>R-101</b> detienen a todos, conduzcas lo que conduzcas: la R-100 cierra la vía a los vehículos <b>en ambos sentidos</b>; la R-101 prohíbe el <b>acceso</b> a toda clase de vehículos."),
        ]),
    ])

    # ---------------------------------------------------------------- 6.5 other prohibitions
    _after_table(B, "6.5 ", [
        BOX("key", f"{TWO[0]}: overtaking and parking signs", f"{TWO[1]}: señales de adelantamiento y de estacionamiento", [
            ("<b>R-305</b> bans overtaking <b>motor vehicles</b> — cars, lorries and motorcycles alike — whenever the manoeuvre means <b>using the side of the road for oncoming traffic</b>. It binds you on a motorcycle exactly as it binds a car. "
             "What it does not ban is an overtake made <b>without leaving your side</b>; the general overtaking rules of Topic 5 still apply to it.",
             "La <b>R-305</b> prohíbe adelantar a los <b>vehículos de motor</b> —turismos, camiones y motocicletas por igual— cuando la maniobra <b>implique invadir la zona del sentido contrario</b>. Te obliga en moto igual que a un turismo. "
             "Lo que no prohíbe es el adelantamiento hecho <b>sin salir de tu sentido</b>; a ese se le siguen aplicando las normas generales del Tema 5."),
            ("<b>R-306</b> concerns only <b>lorries over 3,500 kg</b>. The stopping and parking signs (<b>R-307</b>, <b>R-308</b> and their variants) apply to a motorcycle or a moped just as to any other vehicle.",
             "La <b>R-306</b> solo afecta a los <b>camiones de más de 3.500 kg</b>. Las señales de parada y estacionamiento (<b>R-307</b>, <b>R-308</b> y sus variantes) se aplican a una motocicleta o a un ciclomotor igual que a cualquier otro vehículo."),
        ]),
    ])

    # ---------------------------------------------------------------- 6.6 obligation signs
    _after_table(B, "6.6 ", [
        BOX("key", f"{TWO[0]}: the blue signs that sort two-wheelers", f"{TWO[1]}: las señales azules que distinguen a los vehículos de dos ruedas", [
            ("<b>R-404</b> (white car) obliges automobiles to use that carriageway, <b>except two-wheeled motorcycles</b> and three-wheelers treated as motorcycles. The sign that obliges <b>you</b> is <b>R-405</b> (white motorcycle).",
             "La <b>R-404</b> (turismo blanco) obliga a los automóviles a circular por esa calzada, <b>excepto a las motocicletas de dos ruedas</b> y a los vehículos de tres ruedas asimilados. La señal que te obliga <b>a ti</b> es la <b>R-405</b> (motocicleta blanca)."),
            ("<b>R-407b</b> (white moped) marks a track <b>reserved and compulsory for mopeds</b>: on a moped you <b>must</b> use it; on a motorcycle you <b>may not</b>, because it is forbidden to every other user. "
             "The same goes for the tracks for cycles and VMP (<b>R-407a</b>, <b>R-420</b>, <b>R-421</b>): they are closed to motorcycles and mopeds.",
             "La <b>R-407b</b> (ciclomotor blanco) señala una vía <b>reservada y obligatoria para ciclomotores</b>: en ciclomotor <b>debes</b> usarla; en motocicleta <b>no puedes</b>, porque está prohibida a los demás usuarios. "
             "Lo mismo ocurre con las vías para ciclos y VMP (<b>R-407a</b>, <b>R-420</b>, <b>R-421</b>): están cerradas a motocicletas y ciclomotores."),
            ("<b>R-413</b> makes dipped beam compulsory for everyone on that stretch. A motorcycle already rides with it <b>by day and by night</b> and keeps it on after the sign that ends the obligation, <b>S-24</b> (Topic 7).",
             "La <b>R-413</b> obliga a todos a llevar la luz de cruce en ese tramo. La motocicleta ya la lleva <b>de día y de noche</b> y la mantiene encendida tras la señal que pone fin a la obligación, la <b>S-24</b> (Tema 7)."),
        ]),
    ])

    # ---------------------------------------------------------------- 7.1 general indications
    _after_table(B, "7.1 ", [
        BOX("key", f"{TWO[0]}: zones and waiting areas", f"{TWO[1]}: zonas y áreas de espera", [
            ("<b>S-49</b> announces an <b>advanced stop box</b>. Its motorcycle pictogram stands for <b>motorcycles, three-wheelers treated as motorcycles and mopeds</b>; a bicycle pictogram stands for cycles. "
             "The marking itself is drawn in section 8.4.",
             "La <b>S-49</b> anuncia una <b>zona de espera adelantada</b>. Su pictograma de motocicleta representa a <b>motocicletas, vehículos de tres ruedas asimilados y ciclomotores</b>; el de bicicleta, a los ciclos. "
             "La marca vial está dibujada en el apartado 8.4."),
            ("<b>S-1</b> and <b>S-1a</b>: a motorcycle may use motorways and autovías; a <b>moped may not</b> (Topic 2).",
             "<b>S-1</b> y <b>S-1a</b>: la motocicleta puede circular por autopistas y autovías; el <b>ciclomotor no</b> (Tema 2)."),
            ("In the zones signed <b>S-28</b> (10 km/h) and <b>S-47</b> (20 km/h) the limit binds you too, pedestrians may use the whole zone and you may park only in the marked places.",
             "En las zonas señalizadas con <b>S-28</b> (10 km/h) y <b>S-47</b> (20 km/h) el límite también te obliga, los peatones pueden usar toda la zona y solo puedes estacionar en los lugares designados."),
        ]),
    ])

    # ---------------------------------------------------------------- 7.2 lane signs
    _after_table(B, "7.2 ", [
        BOX("key", f"{TWO[0]}: reserved lanes", f"{TWO[1]}: carriles reservados", [
            ("A lane signed <b>S-51</b> is only for the vehicles <b>drawn on the sign</b>. You may ride in a bus or taxi lane <b>only when the motorcycle pictogram is on it</b>.",
             "Un carril señalizado con <b>S-51</b> es solo para los vehículos <b>dibujados en la señal</b>. Solo puedes circular por un carril bus o taxi <b>si figura el pictograma de la motocicleta</b>."),
            ("Without the pictogram you are like any other vehicle: where the lane’s line is <b>broken</b> you may enter it only for a manoeuvre that is <b>not stopping, parking, turning round or overtaking</b>, "
             "and always giving preference to the vehicles the lane is for.",
             "Sin el pictograma eres un vehículo más: donde la marca del carril es <b>discontinua</b> solo puedes entrar para una maniobra que <b>no sea parar, estacionar, cambiar de sentido o adelantar</b>, "
             "dejando siempre preferencia a los vehículos autorizados."),
            ("In a high-occupancy lane (<b>VAO</b>) the figure on the sign is the number of people a car needs; motorcycles are among the vehicles admitted to VAO lanes (Topic 2).",
             "En un carril de alta ocupación (<b>VAO</b>) la cifra de la señal es el número de personas que necesita un turismo; las motocicletas están entre los vehículos admitidos en los carriles VAO (Tema 2)."),
        ]),
    ])

    # ---------------------------------------------------------------- 8.4 other white markings
    _after_table(B, "8.4 Other", [
        FIG(advance_box, "On red, the box between the two lines is only for the vehicles painted in it; everyone else stops at the first line they reach.",
            "Con el semáforo en rojo, el espacio entre las dos líneas es solo para los vehículos pintados en él; los demás se detienen ante la primera línea que encuentran."),
        BOX("key", f"{TWO[0]}: the advanced stop box and the hatched area", f"{TWO[1]}: el avanza-motos y el cebreado", [
            ("The <b>avanza-motos</b> is the space between <b>two continuous lines across the road, 4 metres apart</b>, just before a junction or a pedestrian crossing <b>controlled by traffic lights</b>. "
             "While the light is <b>red</b> only the vehicles shown by its pictograms may occupy it: motorcycles, mopeds, cycles or VMP, as painted.",
             "El <b>avanza-motos</b> es el espacio entre <b>dos marcas transversales continuas separadas 4 metros</b>, justo antes de una intersección o un paso de peatones <b>regulados por semáforo</b>. "
             "Con el semáforo en <b>rojo</b> solo pueden ocuparlo los vehículos de sus pictogramas: motocicletas, ciclomotores, ciclos o VMP, según lo pintado."),
            ("A box painted <b>only with a bicycle</b> is an avanza-bici: it is not for you. Look at the pictogram before you roll forward.",
             "Un espacio pintado <b>solo con una bicicleta</b> es un avanza-bici: no es para ti. Mira el pictograma antes de adelantarte."),
            ("<b>Hatched area</b> (<i>cebreado</i>): nobody may enter it <b>except those obliged to use the shoulder</b>. A moped is one of them; a <b>motorcycle is not</b>, so on a motorcycle you stay out.",
             "<b>Cebreado</b>: nadie debe entrar <b>excepto los obligados a circular por el arcén</b>. El ciclomotor es uno de ellos; la <b>motocicleta no</b>, así que en moto no se entra."),
        ]),
    ])

    # ---------------------------------------------------------------- 8.4.1 markings that calm traffic
    _after_table(B, "8.4.1 ", [
        FIG(guide_marks, "The marks announce a bend of special risk and show the strip of the lane it is better not to ride on. Keeping away from the centre line keeps your leaning body out of the oncoming lane.",
            "Las marcas anuncian una curva de especial riesgo y señalan la franja del carril que se recomienda no pisar. Alejarte del eje evita que tu cuerpo, al inclinarte, invada el carril contrario."),
    ])

    # ---------------------------------------------------------------- 9. on two wheels
    B.append(H2("9", "On two wheels: what singles out motorcycles and mopeds", "Sobre dos ruedas: lo que distingue a motocicletas y ciclomotores"))
    B.append(P(
        "Almost every sign binds a rider exactly as it binds a car driver. The few that tell two-wheelers apart do it with a <b>pictogram</b>, and the law treats three vehicles differently: "
        "the <b>motorcycle</b> (a motor vehicle and an automobile), the <b>three-wheeler treated as a motorcycle</b> (follows the motorcycle) and the <b>moped</b> (<i>ciclomotor</i>), which is <b>not a motor vehicle</b> in the Traffic Law.",
        "Casi todas las señales obligan al motorista igual que al conductor de un turismo. Las pocas que distinguen a los vehículos de dos ruedas lo hacen con un <b>pictograma</b>, y la ley trata de forma distinta a tres vehículos: "
        "la <b>motocicleta</b> (vehículo de motor y automóvil), el <b>vehículo de tres ruedas asimilado a motocicleta</b> (sigue a la motocicleta) y el <b>ciclomotor</b>, que <b>no es vehículo de motor</b> en la Ley de Tráfico."))
    B.append(TABLE(
        [T("Sign or marking", "Señal o marca"), T("On a motorcycle", "En motocicleta"), T("On a moped", "En ciclomotor")],
        [
            _row("R-102", "No motor vehicles", "Prohibida a vehículos de motor",
                 "<b>No entry.</b>", "<b>No puedes entrar.</b>",
                 "<b>You may enter</b>: a moped is not a motor vehicle.", "<b>Puedes entrar</b>: el ciclomotor no es vehículo de motor."),
            _row("R-103", "No motor vehicles, except two-wheeled motorcycles", "Prohibida a vehículos de motor, excepto motos de dos ruedas",
                 "<b>You may enter</b> (two wheels, or a three-wheeler treated as a motorcycle).", "<b>Puedes entrar</b> (dos ruedas, o tres ruedas asimilado a motocicleta).",
                 "<b>You may enter.</b>", "<b>Puedes entrar.</b>"),
            _row("R-104", "No motorcycles", "Prohibida a motocicletas",
                 "<b>No entry</b>, nor for three-wheelers treated as motorcycles.", "<b>No puedes entrar</b>, tampoco los tres ruedas asimilados.",
                 "<b>You may enter.</b>", "<b>Puedes entrar.</b>"),
            _row("R-105", "No mopeds", "Prohibida a ciclomotores",
                 "<b>You may enter.</b>", "<b>Puedes entrar.</b>",
                 "<b>No entry</b> (nor for vehicles for people with reduced mobility).", "<b>No puedes entrar</b> (tampoco los vehículos para personas de movilidad reducida)."),
            _row("R-404", "Carriageway for automobiles", "Calzada para automóviles",
                 "<b>Not obliged</b>: two-wheeled motorcycles are the exception.", "<b>No te obliga</b>: las motocicletas de dos ruedas son la excepción.",
                 "It is addressed to automobiles, and a moped is not one.", "Se dirige a los automóviles, y el ciclomotor no lo es."),
            _row("R-405", "Carriageway for motorcycles", "Calzada para motocicletas",
                 "<b>You must use it</b> (also three-wheelers treated as motorcycles).", "<b>Debes circular por ella</b> (también los tres ruedas asimilados).",
                 "It is addressed to motorcycles.", "Se dirige a las motocicletas."),
            _row("R-407b", "Moped track", "Vía para ciclomotores",
                 "<b>You may not use it.</b>", "<b>No puedes usarla.</b>",
                 "<b>You must use it.</b>", "<b>Debes usarla.</b>"),
            _row("S-1 · S-1a", "Motorway, autovía", "Autopista, autovía",
                 "<b>Allowed.</b>", "<b>Permitido.</b>",
                 "<b>Forbidden</b> (Topic 2).", "<b>Prohibido</b> (Tema 2).", icon="S-1"),
            _row("S-51", "Reserved lane", "Carril reservado",
                 "Only if the <b>motorcycle is drawn</b> on the sign.", "Solo si en la señal figura la <b>motocicleta</b>.",
                 "Only if the sign admits mopeds.", "Solo si la señal admite ciclomotores.", icon="S-51a"),
            _row("S-49", "Advanced stop box", "Avanza moto o bici",
                 "On red, you may wait in the box when the <b>motorcycle</b> is painted in it.", "En rojo, puedes esperar en la zona si lleva pintada la <b>motocicleta</b>.",
                 "The same: the motorcycle pictogram also stands for mopeds.", "Igual: el pictograma de motocicleta representa también al ciclomotor."),
            _row("mk-hatch", "Hatched area", "Cebreado",
                 "<b>Stay out.</b>", "<b>No se entra.</b>",
                 "You may enter, as a vehicle <b>obliged to use the shoulder</b>.", "Puedes entrar, como vehículo <b>obligado a circular por el arcén</b>."),
            _row("S-891", "Side gap: 1.5 m", "Distancia lateral: 1,5 m",
                 "Leave <b>at least 1.5 m</b> when you overtake a cycle or a moped.", "Deja <b>al menos 1,5 m</b> al adelantar a un ciclo o a un ciclomotor.",
                 "It reminds those who overtake <b>you</b> of the 1.5 m they owe you.", "Recuerda a quien <b>te</b> adelanta los 1,5 m que debe dejarte."),
        ],
        widths=["26%", "37%", "37%"], cls="small",
    ))
    B.append(BOX("key", "Made with riders in mind", "Pensado para quien va en moto", [
        ("<b>Motorcyclist guidance marks</b> (section 8.4.1) announce a bend of special risk and the strip of the lane it is better not to ride on. They also address cyclists, and they recommend: they create no new prohibition.",
         "Las <b>marcas de guiado para motoristas</b> (apartado 8.4.1) anuncian una curva de especial riesgo y la franja del carril que se recomienda no pisar. Se dirigen también a los ciclistas y son una recomendación: no crean una prohibición nueva."),
        ("<b>Motorcyclist protection systems</b> (section 3.3) are restraint barriers designed specifically to protect riders of two-wheelers.",
         "Los <b>sistemas de protección para motoristas</b> (apartado 3.3) son barreras de contención diseñadas específicamente para proteger a los vehículos de dos ruedas."),
        ("The warning signs that matter most on two wheels are the ones about <b>grip and balance</b>: <b>P-19</b> slippery road, <b>P-28</b> loose chippings, <b>P-29</b> crosswind (it never says from which side), "
         "<b>P-15</b> uneven road and <b>P-34</b> ice or snow.",
         "Las señales de peligro que más importan sobre dos ruedas son las de <b>adherencia y equilibrio</b>: <b>P-19</b> pavimento deslizante, <b>P-28</b> proyección de gravilla, <b>P-29</b> viento transversal (nunca indica de qué lado), "
         "<b>P-15</b> perfil irregular y <b>P-34</b> hielo o nieve."),
        ("Riding tip, not a sign rule: <b>painted markings</b> (crossings, arrows, hatching) grip less than bare asphalt, above all when wet. Cross them upright, without braking or accelerating hard.",
         "Consejo de conducción, no norma de señalización: las <b>marcas pintadas</b> (pasos, flechas, cebreados) agarran menos que el asfalto, sobre todo mojadas. Písalas con la moto recta, sin frenar ni acelerar con fuerza."),
    ]))

    # ---------------------------------------------------------------- 10. traps
    B.append(H2("10", "Classic exam traps", "Trampas clásicas del examen"))
    rider_traps = [
        T("<b>R-102</b> stops a motorcycle but <b>not a moped</b>; <b>R-103</b> lets two-wheeled motorcycles through; <b>R-104</b> stops motorcycles; <b>R-105</b> stops mopeds and vehicles for <b>reduced mobility</b>.",
          "La <b>R-102</b> detiene a la motocicleta pero <b>no al ciclomotor</b>; la <b>R-103</b> deja pasar a las motocicletas de dos ruedas; la <b>R-104</b> detiene a las motocicletas; la <b>R-105</b>, a ciclomotores y vehículos para <b>movilidad reducida</b>."),
        T("<b>R-404</b> (car on blue) does <b>not</b> oblige a two-wheeled motorcycle; <b>R-405</b> does. <b>R-407b</b> is compulsory for mopeds and closed to motorcycles.",
          "La <b>R-404</b> (turismo sobre azul) <b>no</b> obliga a la motocicleta de dos ruedas; la <b>R-405</b> sí. La <b>R-407b</b> es obligatoria para ciclomotores y está cerrada a las motocicletas."),
        T("Advanced stop box: <b>two continuous lines 4 m apart</b>, only <b>on red</b>, only the vehicles <b>painted in it</b>. In S-49 the motorcycle pictogram also covers three-wheelers and mopeds.",
          "Avanza-motos: <b>dos líneas continuas separadas 4 m</b>, solo <b>en rojo</b>, solo los vehículos <b>pintados</b>. En la S-49 el pictograma de motocicleta incluye también tres ruedas asimilados y ciclomotores."),
        T("A bus lane (<b>S-51</b>) is yours only if the <b>motorcycle is drawn</b> on the sign. A hatched area is for those <b>obliged to use the shoulder</b>: a moped yes, a motorcycle no.",
          "Un carril bus (<b>S-51</b>) solo es tuyo si en la señal figura la <b>motocicleta</b>. El cebreado es para los <b>obligados a circular por el arcén</b>: el ciclomotor sí, la motocicleta no."),
        T("<b>R-305</b> binds a motorcycle like any other vehicle: no overtaking motor vehicles if you must <b>use the oncoming side</b>.",
          "La <b>R-305</b> obliga a la motocicleta como a cualquier vehículo: no se adelanta a vehículos de motor si hay que <b>invadir el sentido contrario</b>."),
    ]
    shared = [it for it in traps_b8[3] if not it["en"].startswith("R-103 lets")]
    assert len(shared) == len(traps_b8[3]) - 1
    B.append(("box", "trap", T("Read twice", "Lee dos veces"), rider_traps + shared))

    # ---------------------------------------------------------------- 11. numbers
    B.append(H2("11", "Key numbers on one page", "Números clave en una página"))
    B.append(numbers_b8)
    return B


# ------------------------------------------------------------------------------------------
# The PDF self-test reuses twelve questions from the page's question bank. The correct option is placed in
# turn at A, B and C so the answer key is not always the same letter.
QUIZ_IDS = ["or2", "ag2", "av3", "li3", "wn4", "pr2", "ne2", "ne5", "ob2", "in6", "mo2", "tw4"]


def quiz():
    from .bank import BANK
    by_id = {q["id"]: q for q in BANK}
    out = []
    for i, qid in enumerate(QUIZ_IDS):
        q = by_id[qid]
        opts = [T(o["en"], o["es"]) for o in q["o"]]
        k = i % 3
        order = opts[1:]
        order.insert(k, opts[0])
        out.append((T(q["q"]["en"], q["q"]["es"]), order, k, T(q["why"]["en"], q["why"]["es"])))
    return out


SOURCES = list(B8.SOURCES)

GLOSSARY = list(B8.GLOSSARY) + [
    ("vehículo de motor · ciclomotor", "motor vehicle · moped (not a motor vehicle in the Traffic Law)"),
    ("vehículo de tres ruedas asimilado a motocicleta", "three-wheeler treated as a motorcycle"),
    ("calzada obligatoria · vía reservada", "compulsory carriageway · reserved track"),
    ("carril reservado · carril VAO", "reserved lane · high-occupancy lane"),
    ("marcas de guiado para motoristas", "motorcyclist guidance marks"),
    ("sistema de protección para motoristas", "motorcyclist protection system"),
]
