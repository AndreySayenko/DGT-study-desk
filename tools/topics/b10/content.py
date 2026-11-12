# -*- coding: utf-8 -*-
"""Topic 10 content (accidents and their factors), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the learner's course (Tema 10: Los accidentes y sus factores). The wording and the
figures are original; the rules come from the Ley sobre Tráfico (RDL 6/2015), the Reglamento General de Circulación
(RD 1428/2003) as amended by RD 518/2026 (vulnerable road users, in force since 1 October 2026), the Reglamento General
de Vehículos and the DGT instruction COND 2024/12 on driver-assistance systems (ADAS) in the driving test, as they
stand in November 2026.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from .diagrams import (risk_factors, stopping_distance, drowsy_clock, rumble_strips, bac_curve, tyre_code, tyre_pressure,
                       moto_controls, seatbelt, headrest, curve_technique, skid, crosswind)
from ..b08.signs import ico, warn, at, car_side

NW = '<span style="white-space:nowrap">%s</span>'
PICTO = ico(warn(at(car_side(), 50, 63, 1.25)), 100, 100, 64, "Conducción: ver prospecto")


def rows(pairs):
    """[(en, es), ...] -> one-column table rows."""
    return [[T(a, b)] for a, b in pairs]


def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("Why accidents happen and how to avoid them: who runs the most risk (<b>vulnerable road users</b> and <b>young drivers</b>), and the three <b>factors</b> — the <b>driver</b> (70–90 %), "
         "the <b>road and its surroundings</b> (10–35 %) and the <b>vehicle</b> (4–13 %).",
         "Por qué ocurren los accidentes y cómo evitarlos: quién corre más riesgo (<b>usuarios vulnerables</b> y <b>conductores jóvenes</b>) y los tres <b>factores</b>: el <b>conductor</b> (70–90 %), "
         "la <b>vía y su entorno</b> (10–35 %) y el <b>vehículo</b> (4–13 %)."),
        ("The exam loves <b>numbers</b>: reaction time <b>0.75 s</b>, a break every <b>2 h or 200 km</b> for <b>20–30 min</b>, alcohol <b>0.25 / 0.15 / 0 mg/l</b>, tread <b>1.6 mm</b>, "
         "child seats up to <b>135 cm</b>, head-restraint gap <b>4 cm</b>, airbag <b>25 cm</b>, braking distance <b>×2</b> in rain and <b>×10</b> on ice.",
         "El examen pregunta sobre todo <b>cifras</b>: tiempo de reacción <b>0,75 s</b>, descanso cada <b>2 h o 200 km</b> de <b>20–30 min</b>, alcohol <b>0,25 / 0,15 / 0 mg/l</b>, dibujo <b>1,6 mm</b>, "
         "sillitas hasta <b>135 cm</b>, reposacabezas a <b>4 cm</b>, airbag a <b>25 cm</b>, distancia de frenado <b>×2</b> con lluvia y <b>×10</b> con hielo."),
        ("It includes the rules in force since <b>1 October 2026</b> (RD 518/2026): e-scooter riders must be <b>15</b> and wear a <b>helmet</b>; every cyclist wears a helmet <b>out of town</b>; "
         "motorcyclists need <b>gloves</b> out of town and <b>closed shoes</b>; delivery riders wear a <b>vest</b> at all times.",
         "Incluye las normas vigentes desde el <b>1 de octubre de 2026</b> (RD 518/2026): patinetes desde los <b>15 años</b> y con <b>casco</b>; todos los ciclistas con casco en <b>interurbanas</b>; "
         "motoristas con <b>guantes</b> en interurbanas y <b>calzado cerrado</b>; repartidores con <b>chaleco</b> siempre."),
        ("The sections follow the order of your course’s Topic 10. Spanish exam terms are in <i>italics</i> in the English text, and a glossary closes the topic.",
         "Los apartados siguen el orden del Tema 10 de tu curso. Al final hay un glosario español–inglés."),
    ]))

    # ---------------------------------------------------------------- 1. social impact
    B.append(H2("1", "The social impact of accidents", "Impacto social"))
    B.append(P(
        "According to the World Health Organization (<b>WHO</b>), road accidents are a <b>serious, priority public-health problem</b> all over the world, and in Spain they are "
        "<b>one of the main causes of death and injury</b>. Besides the human side, they bring other <b>major costs</b> that all citizens bear, directly or indirectly — "
        "<b>each death affects about 100 people</b> on average.",
        "Según la Organización Mundial de la Salud (<b>OMS</b>), los accidentes de circulación son un <b>problema grave y prioritario de salud pública</b> en todo el mundo, y en España son "
        "<b>una de las principales causas de muerte y lesiones</b>. Además del aspecto humano, tienen <b>otros costes muy importantes</b> que asumen todos los ciudadanos, de forma directa o indirecta: "
        "<b>cada víctima mortal afecta a una media de 100 personas</b>."))
    B.append(TABLE(
        [T("Cost", "Coste"), T("What it includes", "Qué incluye")],
        [
            [T("<b>Human</b>", "<b>Humanos</b>"), T("Years of life and of working capacity lost; physical and psychological suffering of the victim, family and friends.", "Pérdida de años potenciales de vida y de capacidad productiva; sufrimiento físico y psicológico de la víctima, familiares y amigos.")],
            [T("<b>Material</b>", "<b>Materiales</b>"), T("Damage to vehicles, load, the road, its surroundings and the environment.", "Daños a los vehículos, la carga, la vía, el entorno y el medio ambiente.")],
            [T("<b>Health</b>", "<b>Sanitarios</b>"), T("First aid, care and treatment of the injured, rehabilitation and adaptations for those hurt.", "Primeros auxilios, atención y tratamiento de heridos, rehabilitación y adaptaciones para los accidentados.")],
            [T("<b>Administrative</b>", "<b>Administrativos</b>"), T("Police and fire services, insurance and other services; legal costs.", "Policía y bomberos, seguros y servicios; costes legales.")],
        ],
        widths=["24%", "76%"],
    ))
    B.append(P(
        "People are rarely well informed about the real size of the problem and tend to underestimate it. Cutting accidents and their consequences takes a <b>responsible attitude</b>, "
        "good <b>road-safety knowledge</b> and driving with the <b>greatest safety</b> at all times.",
        "La población no suele tener demasiada información sobre la magnitud real del problema y puede no valorarlo adecuadamente. Para reducir los accidentes y sus consecuencias hace falta una "
        "<b>actitud responsable</b>, <b>conocimientos adecuados de seguridad vial</b> y conducir siempre con la <b>máxima seguridad</b>."))
    B.append(H3("1.1 Accidents can be avoided", "1.1 Los accidentes son evitables"))
    B.append(P(
        "<b>Most accidents can be avoided.</b> They are not chance or bad luck: they are <b>predictable events</b> caused by circumstances that make them more likely — the <b>risk factors</b>. "
        "The key is to avoid them, <b>especially the ones that depend on the driver</b>.",
        "<b>La mayoría de los accidentes se pueden evitar.</b> No se deben a la casualidad ni al azar: son <b>sucesos predecibles</b> debidos a circunstancias que aumentan su probabilidad, los "
        "<b>factores de riesgo</b>. La clave es evitarlos, <b>especialmente los que dependen del propio conductor</b>."))
    B.append(TABLE(
        [T("Risk factors that depend on…", "Factores de riesgo que dependen…"), T("How to avoid them", "Cómo evitarlos")],
        [
            [T("<b>The driver</b> (the most important)", "<b>Del conductor</b> (los más importantes)"), T("Unsuitable speed, distractions, fatigue, sleep, illness, medicines, alcohol, drugs…", "Velocidad inadecuada, distracciones, fatiga, sueño, enfermedades, fármacos, alcohol, drogas…")],
            [T("<b>The vehicle</b>", "<b>Del vehículo</b>"), T("Invest in safety, follow the <b>manufacturer’s maintenance</b>, pass the <b>ITV</b>: avoid mechanical failures.", "Invertir en seguridad, hacer los <b>mantenimientos del fabricante</b>, pasar la <b>ITV</b>: evitar fallos mecánicos.")],
            [T("<b>The road and its surroundings</b>", "<b>De la vía y su entorno</b>"), T("Adapt your <b>speed</b> to the circumstances, keep the <b>safety distance</b>, take the <b>weather</b> into account.", "Adecuar la <b>velocidad</b> a las circunstancias, mantener la <b>distancia de seguridad</b>, tener en cuenta la <b>climatología</b>.")],
        ],
        widths=["34%", "66%"],
    ))

    # ---------------------------------------------------------------- 2. where and when
    B.append(H2("2", "Where and when accidents happen", "Dónde y cuándo se producen"))
    B.append(TABLE(
        [T("The most dangerous places", "Lugares más peligrosos")],
        rows([
            ("<b>Accidents with victims</b> (dead and injured): <b>more on urban roads</b>. <b>Deaths</b>: <b>more on interurban roads</b> (<i>carreteras</i>), because speeds are higher.",
             "<b>Accidentes con víctimas</b> (muertos y heridos): <b>más en vías urbanas</b>. <b>Víctimas mortales</b>: <b>más en carretera</b>, porque se circula a mayor velocidad."),
            ("Most accidents on interurban roads happen on <b>straight stretches with good visibility</b>, by <b>running off the road</b> — single-vehicle accidents, where it is easier to get distracted.",
             "La mayoría de los accidentes en carretera se producen en <b>rectas con buena visibilidad</b>, por <b>salidas de la vía</b>: accidentes en solitario, donde es más fácil distraerse."),
            ("<b>Autovías and autopistas</b> are the <b>safest</b> roads: separate carriageways, no intersections, a gentler layout.",
             "Las <b>autovías y autopistas</b> se consideran <b>más seguras</b>: sentidos separados, sin intersecciones, trazado menos sinuoso."),
        ]),
    ))
    B.append(TABLE(
        [T("The most dangerous times", "Momentos más peligrosos")],
        rows([
            ("<b>Going to and leaving work</b>, especially <b>at the end of the working day in the afternoon</b>.", "<b>Horas de entrada o salida del trabajo</b>, especialmente <b>al terminar la jornada por la tarde</b>."),
            ("<b>Holidays, public holidays and weekends</b>, especially <b>in the early hours</b> (<i>madrugada</i>).", "<b>Vacaciones, festivos y fines de semana</b>, especialmente <b>de madrugada</b>."),
        ]),
    ))
    B.append(BOX("key", "Vans: the key figures", "Furgonetas: principales cifras de siniestralidad", [
        ("Most van accidents happen between <b>7:00 and 23:59</b>; the worst hour is <b>15:00–16:00</b>. The worst day is <b>Friday</b>, then <b>Monday</b>.",
         "La mayoría se producen entre las <b>7:00 y las 23:59</b>; la hora de más siniestralidad es de <b>15:00 a 16:00</b>. El peor día es el <b>viernes</b>, seguido del <b>lunes</b>."),
        ("<b>More accidents on urban roads</b>, but <b>more deaths on interurban roads</b>.", "<b>Más accidentes en vías urbanas</b>, pero <b>más víctimas mortales en interurbanas</b>."),
        ("Most common factor: <b>driver distraction</b>, then not keeping the <b>safety distance</b> and <b>unsuitable speed</b>.", "Factor más habitual: <b>distracciones del conductor</b>, seguido de no respetar la <b>distancia de seguridad</b> y la <b>velocidad inadecuada</b>."),
        ("Most common type: on interurban roads, <b>rear-end and multiple collisions</b>; in towns, <b>side and front-side collisions</b>.", "Tipo más habitual: en interurbanas, <b>colisiones traseras y múltiples</b>; en urbanas, <b>laterales y frontolaterales</b>."),
    ]))

    # ---------------------------------------------------------------- 3. vulnerable groups
    B.append(H2("3", "Vulnerable groups", "Grupos vulnerables"))
    B.append(P(
        "<b>Vulnerable road users</b> are those who, because of <b>how they travel</b> or their <b>age and physical condition</b>, are more exposed and have a much higher risk of <b>serious or fatal injuries</b> "
        "in an accident. Since October 2026 the Reglamento General de Circulación defines them: <b>pedestrians</b> (above all people with disabilities, children, older people and people with reduced mobility), "
        "<b>cyclists</b>, <b>VMP riders</b> (e-scooters and other personal mobility vehicles) and <b>motorcyclists and moped riders and their passengers</b>. Your course also covers <b>older drivers</b>.",
        "Los <b>usuarios vulnerables</b> son aquellos que, <b>por el medio en el que se desplazan</b> o <b>por su edad y condición física</b>, tienen mayor exposición y un riesgo mucho más alto de <b>lesiones graves o mortales</b> "
        "en un accidente. Desde octubre de 2026 el Reglamento General de Circulación los define: <b>peatones</b> (sobre todo personas con discapacidad, menores, mayores y personas con movilidad reducida), "
        "<b>ciclistas</b>, <b>conductores de VMP</b> y <b>conductores y pasajeros de motocicletas y ciclomotores</b>. Tu curso incluye además a los <b>conductores mayores</b>."))

    B.append(H3("3.1.1 Older drivers", "3.1.1 Los conductores mayores"))
    B.append(P("Their main problem is the <b>decline of physical and mental abilities</b>:", "Su principal problema es el <b>deterioro de las capacidades psicofísicas</b>:"))
    B.append(TABLE(
        [T("Problem", "Problema")],
        rows([
            ("<b>Narrower field of vision</b>, especially at night, and more easily <b>dazzled</b>.", "<b>Reducción del campo visual</b>, sobre todo de noche, y más <b>deslumbramientos</b>."),
            ("<b>Hearing loss</b>: harder to tell where sounds come from.", "<b>Pérdida de audición</b>: más difícil localizar la procedencia de los sonidos."),
            ("<b>Slower response in complex situations</b> (intersections, joining and leaving fast roads): a <b>longer reaction time</b>.", "<b>Respuesta más lenta ante situaciones complejas</b> (intersecciones, incorporaciones y salidas de vías rápidas): <b>aumenta el tiempo de reacción</b>."),
            ("<b>Medicines</b> that may affect driving; <b>less ability to keep attention</b>; <b>less strength</b> to brake and <b>worse handling</b> of the steering wheel.",
             "<b>Medicamentos</b> que pueden afectar a la conducción; <b>menor capacidad para mantener la atención</b>; <b>menos fuerza</b> al frenar y <b>peor manejo</b> del volante."),
        ]),
    ))
    B.append(BOX("key", "Remember", "Recuerda", [("Be <b>respectful and patient</b> with older people, especially in complex situations.", "Hay que ser <b>respetuosos y tolerantes</b> con las personas mayores, especialmente en las situaciones complejas.")]))

    B.append(H3("3.1.2 Pedestrians", "3.1.2 Los peatones"))
    B.append(P(
        "Pedestrians have <b>more accidents in towns</b>, but on <b>interurban roads</b> the injuries can be very <b>serious</b> and death is more likely, because of the speeds. In towns the chance of dying when hit is lower, "
        "but there are many more pedestrians hit, and <b>more than half of the pedestrians killed die in towns</b>. Their movements are hard to predict: they have a <b>larger zone of uncertainty</b> than other road users.",
        "Los peatones sufren <b>más accidentes en las ciudades</b>, pero en <b>carretera</b> las lesiones pueden ser <b>muy graves</b> y es mayor la probabilidad de muerte, por las altas velocidades. En zona urbana la probabilidad de morir atropellado es menor, "
        "pero hay más atropellos, y <b>más de la mitad de los atropellados fallecidos lo son en ciudad</b>. Sus movimientos son difíciles de prever: tienen una <b>zona de incertidumbre mayor</b> que el resto de usuarios."))
    B.append(TABLE(
        [T("Who", "Quién"), T("Most common offences", "Infracciones más habituales")],
        [
            [T("<b>Pedestrians</b>", "<b>Peatones</b>"),
             T("Bursting onto the road or crossing incorrectly; standing or walking on the carriageway or shoulder improperly; not using crossings or crossing diagonally; ignoring traffic lights; not respecting priority; getting in or out of a vehicle without watching the traffic.",
               "Irrumpir o cruzar la vía incorrectamente; situarse mal en la calzada o el arcén, o marchar por la calzada de forma antirreglamentaria; no usar los pasos para peatones o cruzar en diagonal; no respetar los semáforos; no respetar la prioridad; subir o bajar de un vehículo sin atender al tráfico.")],
            [T("<b>Drivers</b>, putting pedestrians at risk", "<b>Conductores</b>, poniendo en riesgo a los peatones"),
             T("Not giving way to pedestrians; parking on the pavement or on crossings; not slowing down at crossings; ignoring traffic lights (amber or red).",
               "No respetar la prioridad de los peatones; estacionar sobre la acera o los pasos para peatones; no moderar la velocidad en los pasos; no cumplir los semáforos (ámbar o rojo).")],
        ],
        widths=["22%", "78%"],
    ))
    B.append(P(
        "<b>Older pedestrians</b> have <b>more accidents when they are alone</b> than when they are looking after children, so take extra care with them. Their main problems:",
        "Las <b>personas mayores</b> tienen <b>más accidentes cuando van solas</b> que cuando acompañan a niños a su cargo, por lo que hay que extremar la precaución con ellas. Sus principales problemas:"))
    B.append(TABLE(
        [T("Older pedestrians", "Los mayores como peatones")],
        rows([
            ("<b>Noise</b> stops them hearing vehicles; it is hard for them to judge <b>vehicle speed</b> and see <b>traffic-light colours</b> (especially on very wide roads).",
             "El <b>exceso de ruido</b> les impide oír los vehículos; les cuesta apreciar la <b>velocidad de los vehículos</b> y los <b>colores de los semáforos</b> (sobre todo en calzadas muy anchas)."),
            ("<b>Few crossings</b> in some areas and <b>poor lighting</b> on some roads.", "Los <b>pocos pasos para peatones</b> de algunas zonas y la <b>mala iluminación</b> de algunas vías."),
            ("They need <b>more time to cross</b> wide streets; <b>high kerbs</b> and <b>obstacles</b> on pavements (planters, badly parked cars, bollards); getting <b>disoriented</b> in unfamiliar streets.",
             "Necesitan <b>más tiempo para cruzar</b> las calles anchas; la altura de los <b>bordillos</b> y los <b>obstáculos</b> en las aceras (maceteros, coches mal aparcados, bolardos); <b>problemas de orientación</b> en calles que no conocen."),
        ]),
    ))
    B.append(P(
        "<b>Children</b>, being shorter, usually take the impact on the <b>head or vital organs</b>. Most child pedestrians are hit <b>when school ends</b>. The main causes:",
        "Los <b>niños</b>, por su menor estatura, suelen recibir el impacto en la <b>cabeza o en partes vitales</b>. La mayoría de los atropellos a niños se producen <b>al finalizar la jornada escolar</b>. Sus causas principales:"))
    B.append(TABLE(
        [T("Children as pedestrians", "Los niños como peatones")],
        rows([
            ("<b>Hearing</b>: under <b>7</b>, they cannot tell where the noise of an approaching vehicle comes from.", "<b>Audición</b>: los menores de <b>siete años</b> no distinguen de dónde viene el ruido de un vehículo."),
            ("<b>Limited field of vision</b>: up to <b>40 % less</b> than adults when walking between parked cars — and drivers find it harder to see them.",
             "<b>Campo visual limitado</b>: hasta un <b>40 % menos</b> que los adultos cuando caminan entre coches aparcados; y a los conductores les cuesta más verlos."),
            ("<b>Poor attention control</b>: easily distracted, they may run out at any moment.", "<b>Bajo control de la atención</b>: se distraen con facilidad y pueden echar a correr en cualquier momento."),
            ("They confuse <b>“seeing” with “being seen”</b>: if they see a car, they think the driver has seen them too.", "Confunden <b>«ver» con «ser visto»</b>: si ven un coche, creen que el conductor también les ha visto."),
            ("They <b>don’t know the traffic rules</b> and <b>cannot judge distances and speeds</b> or recognise real danger.", "<b>Desconocen las normas</b> y <b>no calculan distancias ni velocidades</b>, ni identifican el peligro real."),
        ]),
    ))
    B.append(BOX("key", "Avoiding hitting pedestrians: extra attention and slow down…", "Para evitar atropellos: extreme la atención y reduzca la velocidad…", [
        ("…near a <b>stopped bus</b>, above all a <b>school bus</b>; when <b>leaving a garage</b> (ramps); when a vehicle <b>stops in front</b> (its occupants may get out without looking).",
         "…al acercarse a un <b>autobús parado</b>, sobre todo de <b>transporte escolar</b>; al <b>salir de un garaje</b> (rampas); cuando un vehículo <b>se detiene delante</b> (los ocupantes pueden bajar sin fijarse)."),
        ("…when pedestrians are <b>talking on the phone</b>; on roads near <b>towns and leisure areas</b>, especially in summer; in <b>bad weather</b> (pedestrians take more risks on rainy days).",
         "…cuando los peatones van <b>hablando por el móvil</b>; en carreteras <b>próximas a poblaciones y lugares de ocio</b>, sobre todo en verano; con <b>meteorología adversa</b> (en días de lluvia se arriesgan más)."),
        ("…near <b>crossings, school zones, crowds</b> and <b>people with disabilities</b>; and be careful when <b>reversing</b>.", "…en <b>pasos para peatones, zonas escolares, aglomeraciones</b> y ante <b>personas con discapacidad</b>; y cuidado con la <b>marcha atrás</b>."),
        ("<b>Don’t</b> wave pedestrians across; <b>don’t</b> park on the pavement (it forces them onto the road); <b>don’t</b> modify the outside of the car, especially the front — it is designed to reduce injuries to pedestrians.",
         "<b>No</b> haga señales para que crucen; <b>no</b> aparque sobre la acera (obliga al peatón a invadir la calzada); <b>no</b> modifique las partes exteriores del vehículo, sobre todo las delanteras: están diseñadas para reducir las lesiones."),
    ]))
    B.append(P(
        "Pedestrians walking on the carriageway or shoulder of an <b>interurban road</b> at night or in poor visibility must wear at least one <b>luminous or reflective element visible from 150 m</b>.",
        "Los peatones que transiten por la calzada o el arcén de una <b>vía interurbana</b> de noche o con poca visibilidad deben llevar al menos un <b>elemento luminoso o reflectante visible a 150 m</b>."))

    B.append(H3("3.1.3 Cyclists", "3.1.3 Los ciclistas"))
    B.append(P(
        "Most cyclist accidents come from <b>offences by cyclists and by other drivers</b> (distraction, wrong turns, unsuitable speed, not giving way at intersections…). They happen mostly at <b>weekends</b>, especially in good weather; "
        "on <b>conventional roads</b>, above all on straights and at intersections; and mostly as <b>head-on or front-side collisions</b> with another vehicle, followed by rear-end and side impacts.",
        "Las causas más frecuentes son las <b>infracciones de los ciclistas y de los demás conductores</b> (distracciones, giros incorrectos, velocidad inadecuada, no respetar la prioridad…). Ocurren sobre todo en <b>fin de semana</b>, especialmente con buen tiempo; "
        "en <b>carreteras convencionales</b>, sobre todo en rectas e intersecciones; y la mayoría por <b>choque frontal o frontolateral</b> con otro vehículo, seguido de alcances y choques laterales."))
    B.append(TABLE(
        [T("Rule", "Norma"), T("What it says", "Qué dice")],
        [
            [T("<b>Where to ride</b>", "<b>Por dónde</b>"), T("On the <b>carriageway</b> if there is no bike lane. Where there is one, its use is preferred, and the authority can make it compulsory with signs.", "Por la <b>calzada</b> si no hay carril bici. Si lo hay, su uso es preferente, y la autoridad puede hacerlo obligatorio mediante señalización.")],
            [T("<b>Pavements</b>", "<b>Aceras</b>"), T("<b>Not allowed</b>, except <b>children under 12</b> where the town council allows it, <b>accompanied by an adult on foot</b>.", "<b>Prohibidas</b>, salvo <b>menores de 12 años</b> si lo permite la autoridad municipal, <b>acompañados de un adulto a pie</b>.")],
            [T("<b>In town</b>", "<b>En vía urbana</b>"), T("Cyclists ride preferably in the <b>centre of the lane</b>. Motor vehicles keep at least <b>5 m</b> behind a cyclist in the same lane.", "Circulan preferentemente por el <b>centro del carril</b>. Los vehículos a motor dejan al menos <b>5 m</b> con el ciclista que les precede en el mismo carril.")],
            [T("<b>Overtaking a cyclist</b>", "<b>Adelantar a un ciclista</b>"),
             T("Don’t start or continue if it endangers cyclists coming the other way (even on the shoulder). Leave at least <b>1.5 m</b> sideways — more with large vehicles, on slopes, in wind or if the cyclist carries a passenger. "
               "Out of town, slow to at least <b>20 km/h below the limit</b>; with more than one lane in your direction, <b>change lane completely</b>.",
               "No iniciarlo ni continuarlo si pone en peligro a ciclistas que vienen de frente (aunque vayan por el arcén). Dejar al menos <b>1,5 m</b> de separación lateral, más con vehículos grandes, cuestas, viento o si el ciclista lleva pasajero. "
               "En interurbanas, reducir la velocidad al menos <b>20 km/h por debajo del límite</b>; con más de un carril por sentido, <b>cambiar completamente de carril</b>.")],
            [T("<b>Helmet</b>", "<b>Casco</b>"),
             T("<b>Compulsory on interurban roads</b> for every cyclist (the old exceptions were removed in October 2026); on <b>all roads</b> for <b>under-16s</b> and for those who <b>work on a bicycle</b> (couriers, delivery riders).",
               "<b>Obligatorio en vías interurbanas</b> para todos (se suprimieron las exenciones en octubre de 2026); en <b>todo tipo de vías</b> para <b>menores de 16 años</b> y para quienes <b>trabajan en bicicleta</b> (repartidores).")],
            [T("<b>Being seen</b>", "<b>Visibilidad</b>"),
             T("On interurban roads, between sunset and sunrise or in poor visibility: at least one <b>luminous or reflective element visible from 150 m</b>. Those who work on a bicycle wear a <b>high-visibility vest at all times</b>.",
               "En vía interurbana, entre el ocaso y la salida del sol o con poca visibilidad: al menos un <b>elemento luminoso o reflectante visible a 150 m</b>. Quienes trabajan en bicicleta llevan <b>chaleco de alta visibilidad en todo momento</b>.")],
        ],
        widths=["22%", "78%"],
    ))
    B.append(BOX("key", "Take extra care…", "Extreme la precaución…", [
        ("…in <b>single-lane town streets limited to 30 km/h or less</b> where signs allow <b>bicycles in both directions</b>: move to your right to let them pass; if that is impossible, vehicles going in the street’s own direction have priority.",
         "…en <b>vías urbanas de un carril limitadas a 30 km/h o menos</b> donde, con señalización, se permite a las <b>bicicletas circular en ambos sentidos</b>: orillarse a la derecha; si no es posible, tienen prioridad los que circulan en el sentido propio de la vía."),
        ("…near <b>parked vehicles or obstacles</b> (cyclists may swerve suddenly), in <b>housing estates, leisure areas</b> and places with many cyclists, especially in <b>summer and on holidays</b>, and in <b>bad weather or poor visibility</b> (sudden moves and falls).",
         "…con <b>vehículos estacionados u obstáculos</b> (pueden desplazarse bruscamente), en <b>urbanizaciones, zonas de ocio</b> y lugares con muchos ciclistas, sobre todo en <b>verano y festivos</b>, y con <b>mal tiempo o mala visibilidad</b> (movimientos bruscos y caídas)."),
        ("<b>Avoid using the horn</b> near cyclists (it startles them). If you ride, <b>wear a helmet</b>: the most serious injuries are to the head.", "<b>Evite las señales acústicas</b> cerca de ciclistas (susto). Si va en bici, <b>póngase el casco</b>: las lesiones más graves son en la cabeza."),
    ]))

    B.append(H3("3.1.4 Moped and motorcycle riders", "3.1.4 Los conductores de ciclomotores y motocicletas"))
    B.append(TABLE(
        [T("What to know", "Lo que hay que saber")],
        rows([
            ("Mopeds and motorcycles are used <b>more and more</b>. They are <b>less visible, less stable and more fragile</b> than other vehicles, and their accidents are <b>easily fatal</b>; "
             "<b>not wearing a helmet</b> is one of the main reasons for the high death rate.",
             "Se usan <b>cada vez más</b>. Son <b>menos visibles, menos estables y más frágiles</b> que el resto de vehículos, y sus accidentes son <b>fácilmente letales</b>; "
             "la <b>no utilización del casco</b> es uno de los principales motivos de la alta mortalidad."),
            ("Most frequent causes: <b>offences</b> by riders and by others — <b>distractions, not giving way, invading the opposite lane</b>. Most common accident: a <b>head-on or front-side collision when overtaking</b>, especially in towns.",
             "Causas más frecuentes: <b>infracciones</b> de sus conductores y de los demás: <b>distracciones, no respetar la prioridad o invadir el sentido contrario</b>. Accidente más común: <b>colisión frontal o frontolateral al adelantar</b>, sobre todo en vías urbanas."),
            ("<b>Posture</b>: relaxed and comfortable, not leaning forward more than needed to reach the handlebar; hold it <b>gently but firmly</b> (no tension), <b>arms slightly bent</b>.",
             "<b>Postura</b>: suelta y cómoda, sin inclinarse más de lo necesario para llegar al manillar; agarrarlo con <b>suavidad y firmeza</b> (sin agarrotamiento), <b>brazos ligeramente flexionados</b>."),
            ("An <b>inexperienced passenger</b> makes an accident more likely, especially in bends. With a passenger, braking shifts the centre of gravity (it can unbalance the bike), the <b>rear wheel is harder to lock</b> and the <b>stopping distance is longer</b>.",
             "La <b>falta de experiencia del pasajero</b> aumenta la probabilidad de accidente, sobre todo en curvas. Con pasajero, al frenar se desplaza el centro de gravedad (desequilibrio), es <b>más difícil que se bloquee la rueda trasera</b> y la <b>distancia de detención es mayor</b>."),
            ("Riding <b>very slowly in a bend</b> with the handlebar turned: <b>don’t use the front brake</b> (you may fall).", "Circulando <b>muy despacio en curva</b> con el manillar girado: <b>no accionar el freno delantero</b> (posible caída)."),
        ]),
    ))
    B.append(TABLE(
        [T("Protective equipment (since 1 October 2026)", "Equipamiento de protección (desde el 1 de octubre de 2026)"), T("Rider and passenger", "Conductor y pasajero")],
        [
            [T("<b>Helmet</b> approved to UNECE R22, fastened", "<b>Casco</b> homologado (UNECE R22), abrochado"), T("All roads. Moped users may keep using <b>certified</b> (not approved) helmets until 1 October 2027.", "En todo tipo de vías. En ciclomotor se pueden seguir usando cascos <b>certificados</b> hasta el 1 de octubre de 2027.")],
            [T("<b>Protective gloves</b>", "<b>Guantes de protección</b>"), T("<b>Interurban roads</b>.", "En <b>vías interurbanas</b>.")],
            [T("<b>Closed footwear</b> covering the whole foot", "<b>Calzado cerrado</b> que cubra todo el pie"), T("<b>All roads</b> (no sandals or flip-flops).", "En <b>todo tipo de vías</b> (nada de sandalias ni chanclas).")],
            [T("<b>High-visibility vest</b>", "<b>Chaleco de alta visibilidad</b>"),
             T("A motorcycle must <b>carry</b> one; wear it when you get off and stand on the carriageway or shoulder of an interurban road. Those who <b>work</b> on a motorcycle or moped wear it <b>at all times</b>. Otherwise it is <b>recommended</b> while riding.",
               "La motocicleta debe <b>llevarlo</b>; se usa al bajar y ocupar la calzada o el arcén de una interurbana. Quienes <b>trabajan</b> en moto o ciclomotor lo llevan <b>siempre</b>. Si no, es <b>recomendable</b> al circular.")],
        ],
        widths=["38%", "62%"],
    ))
    B.append(P(
        "Not wearing gloves, closed shoes or (for riders who work on the bike) the vest is a <b>serious offence</b>: <b>200 €</b>. Your course repeats in this list the <b>150 m reflective element</b>; in the law that element is for <b>cyclists and VMP riders</b>.",
        "No llevar guantes, calzado cerrado o (los profesionales) el chaleco es infracción <b>grave</b>: <b>200 €</b>. Tu curso repite aquí el <b>elemento reflectante visible a 150 m</b>; en la norma ese elemento es para <b>ciclistas y conductores de VMP</b>."))
    B.append(BOX("key", "If you ride a moped or motorcycle", "Si conduces un ciclomotor o una moto", [
        ("<b>Be visible</b> (don’t surprise anyone); respect <b>priority at intersections</b>; keep the <b>safety distance</b> and <b>avoid riding alongside</b> other vehicles.", "<b>Sé visible</b> (no sorprender); respeta la <b>prioridad en las intersecciones</b>; mantén la <b>distancia de seguridad</b> y <b>evita circular en paralelo</b> con otros vehículos."),
        ("Extra care in <b>bad weather or poor visibility</b> (sudden moves and falls). A reflective vest while riding is <b>recommended, not compulsory</b>.", "Extrema la precaución con <b>mal tiempo o mala visibilidad</b> (movimientos bruscos y caídas). El chaleco al circular es <b>recomendable, no obligatorio</b>."),
        ("If you must use the <b>opposite lane</b>, make sure nothing is coming.", "Si tienes que usar el <b>carril contrario</b>, asegúrate de que no viene nadie."),
    ]))
    B.append(BOX("trap", "If you fall off", "En caso de caída", [("Try to <b>slide along the ground as relaxed as possible</b> until you stop.", "Hay que procurar <b>deslizarse por el suelo lo más relajadamente posible</b> hasta quedar detenido.")]))

    B.append(H3("3.1.5 E-scooters and other personal mobility vehicles (VMP)", "3.1.5 Patinetes eléctricos y otros VMP"))
    B.append(P(
        "E-scooters have become the fashionable urban vehicle — and a <b>particularly vulnerable</b> one in an accident. The rules:",
        "Se han convertido en el vehículo de movilidad urbana de moda, y son <b>especialmente vulnerables</b> en caso de accidente. Las normas:"))
    B.append(TABLE(
        [T("Topic", "Aspecto"), T("Rule", "Norma")],
        [
            [T("<b>Who</b>", "<b>Quién</b>"), T("Minimum age <b>15</b>. <b>Rider only</b>: no passengers.", "Edad mínima <b>15 años</b>. <b>Solo el conductor</b>: no se permite acompañante.")],
            [T("<b>Helmet</b>", "<b>Casco</b>"), T("<b>Compulsory</b>, approved or certified, properly fastened.", "<b>Obligatorio</b>, homologado o certificado, bien abrochado.")],
            [T("<b>Being seen</b>", "<b>Visibilidad</b>"), T("Between sunset and sunrise or in poor visibility: a <b>luminous or reflective element visible from 150 m</b> (a reflective vest). Those who work on a VMP wear the vest <b>at all times</b>.",
                                                              "Entre el ocaso y la salida del sol o con poca visibilidad: <b>elemento luminoso o reflectante visible a 150 m</b> (chaleco reflectante). Quienes trabajan en VMP lo llevan <b>siempre</b>.")],
            [T("<b>Signals</b>", "<b>Señales</b>"), T("<b>Always use your arm</b> to warn of manoeuvres.", "<b>Utilizar siempre el brazo</b> para advertir de las maniobras.")],
            [T("<b>Speed and position</b>", "<b>Velocidad y posición</b>"), T("Maximum <b>25 km/h</b>. Preferably in the <b>centre of the lane</b>; motor vehicles keep at least <b>5 m</b> behind.", "Máximo <b>25 km/h</b>. Preferentemente por el <b>centro del carril</b>; los vehículos a motor dejan al menos <b>5 m</b>.")],
            [T("<b>Equipment</b>", "<b>Equipamiento</b>"),
             T("Electric motor (environmental label <b>CERO</b>, no sticker needed). <b>Two independent brakes</b> (they may share one control). <b>White</b> front light, <b>red</b> rear light, brake light (separate or combined). "
               "Reflectors: <b>white</b> front, <b>white or amber</b> sides, <b>red</b> rear. A <b>bell</b>. Lights <b>always on</b>, day and night (the daytime rule applies from <b>1 October 2027</b>).",
               "Motor eléctrico (distintivo <b>CERO</b>, exento de llevarlo). <b>Dos frenos independientes</b> (pueden accionarse con el mismo mando). Luz delantera <b>blanca</b>, trasera <b>roja</b> y de freno (diferenciada o combinada). "
               "Catadióptricos: <b>blanco</b> delante, <b>blanco o amarillo auto</b> en los laterales, <b>rojo</b> detrás. <b>Timbre</b>. Alumbrado <b>siempre encendido</b>, de día y de noche (lo diurno, desde el <b>1 de octubre de 2027</b>).")],
            [T("<b>Where they may not ride</b>", "<b>Por dónde no</b>"),
             T("<b>Pavements</b>, <b>autopistas and autovías</b> (even inside towns), <b>travesías</b>, <b>interurban roads</b> and <b>urban tunnels</b> — except segregated bike lanes, cycle tracks and paths, and roads closed to motor vehicles, unless signs forbid it.",
               "<b>Aceras</b>, <b>autopistas y autovías</b> (aunque discurran por poblado), <b>travesías</b>, <b>vías interurbanas</b> y <b>túneles urbanos</b>, salvo carriles bici segregados, aceras-bici, pistas-bici, sendas ciclables y vías cerradas a vehículos de motor, si la señalización no lo prohíbe.")],
            [T("<b>In town</b>", "<b>En ciudad</b>"), T("Both directions allowed in single-lane streets limited to <b>30 km/h or less</b>, if signed (same as bicycles). Town bylaws set where they may ride (bike lanes, 30 or 20 km/h streets).",
                                                         "Se puede permitir en ambos sentidos en vías de un carril limitadas a <b>30 km/h o menos</b>, con señalización (igual que las bicis). Las ordenanzas municipales regulan por dónde (carriles bici, calles a 30 o 20 km/h).")],
            [T("<b>General rules</b>", "<b>Normas comunes</b>"), T("All the general rules and bans apply: <b>alcohol, drugs, phone…</b> People with <b>reduced mobility</b> riding a VMP <b>at walking pace</b> count as <b>pedestrians</b>.",
                                                                    "Les afectan todas las normas y prohibiciones comunes: <b>alcohol, drogas, móvil…</b> Las personas con <b>movilidad reducida</b> en VMP <b>al paso de persona</b> se consideran <b>peatones</b>.")],
        ],
        widths=["22%", "78%"],
        cls="small",
    ))
    B.append(BOX("key", "Other things a VMP needs before it can be ridden", "Otras obligaciones para poder circular", [
        ("Registered in the DGT’s <b>national register of light personal vehicles</b>, with the <b>identification label</b> (in its holder, visible) and the <b>manufacturer’s plate</b> (serial number).",
         "Inscrito en el <b>Registro Nacional de Vehículos Personales Ligeros</b> de la DGT, con la <b>etiqueta identificativa</b> (en el portaidentificador, visible) y la <b>placa de marcaje del fabricante</b> (número de serie)."),
        ("A <b>circulation certificate</b> (it meets the technical requirements) and <b>compulsory third-party insurance</b> (since January 2026).", "<b>Certificado de circulación</b> (cumple los requisitos técnicos) y <b>seguro obligatorio de responsabilidad civil</b> (desde enero de 2026)."),
        ("VMP sold before <b>22 January 2024</b> may be used without the certificate until <b>21 January 2027</b>; from 22 January 2027 only certified ones. They must still be <b>registered and insured</b>.",
         "Los VMP comercializados antes del <b>22 de enero de 2024</b> pueden circular sin certificado hasta el <b>21 de enero de 2027</b>; desde el 22 de enero de 2027, solo los certificados. Deben estar igualmente <b>inscritos y asegurados</b>."),
    ]))

    B.append(H3("3.2 The risk group: young drivers", "3.2 Grupo de riesgo: conductores jóvenes"))
    B.append(P(
        "Young drivers are <b>not vulnerable users</b>, but they are an important <b>risk group</b> because of their high accident rate. Road accidents are the <b>main cause of injury and death for people aged 15 to 29</b> "
        "(almost <b>35 %</b> of road deaths). The risk rises <b>from 14–15</b>, the age of the first moped riders.",
        "Los conductores jóvenes <b>no se consideran usuarios vulnerables</b>, pero forman un <b>grupo de riesgo</b> importante por su alta siniestralidad. Los accidentes son la <b>principal causa de lesiones y muerte entre los 15 y los 29 años</b> "
        "(casi el <b>35 %</b> de las víctimas mortales). Aumenta <b>a partir de los 14–15 años</b>, cuando aparecen los primeros conductores de ciclomotores."))
    B.append(TABLE(
        [T("Question", "Pregunta"), T("Answer", "Respuesta")],
        [
            [T("<b>When</b>", "<b>Cuándo</b>"), T("Going out for fun, with <b>alcohol</b> and <b>several occupants</b>; <b>at night and in the early hours</b>; in and around big cities; commuting; <b>weekends, Christmas and summer</b>.",
                                                   "En situaciones de <b>diversión, alcohol y varios ocupantes</b>; <b>noches y madrugadas</b>; grandes ciudades y alrededores; trayectos de ida y vuelta al trabajo; <b>fines de semana, Navidad y verano</b>.")],
            [T("<b>Why</b>", "<b>Por qué</b>"), T("<b>Lack of experience</b>, <b>speeding</b>, <b>breaking rules</b>, <b>alcohol and drugs</b>.", "<b>Falta de experiencia</b>, <b>exceso de velocidad</b>, <b>incumplimiento de normas</b>, <b>alcohol y drogas</b>.")],
            [T("<b>What pushes them to take risks</b>", "<b>Qué les hace asumir más riesgos</b>"),
             T("Advertising that encourages risk; <b>lower perception of risk</b>; accepting unnecessary risks (to prove themselves, competitiveness); not seeing driving as dangerous; showing off in a group (they risk more with friends); "
               "<b>overestimating their skill</b> while having less control; thinking that <b>mistakes are always made by others</b>.",
               "La publicidad que incita al riesgo; <b>menor percepción del riesgo</b>; aceptar riesgos innecesarios (autoafirmación, competitividad); no perciben la conducción como peligrosa; exhibicionismo en grupo (arriesgan más acompañados); "
               "<b>sobrevaloran su capacidad</b> teniendo menos control; piensan que <b>los errores siempre los cometen los demás</b>.")],
        ],
        widths=["24%", "76%"],
    ))

    # ---------------------------------------------------------------- 4. factors
    B.append(H2("4", "The factors involved", "Factores que intervienen"))
    B.append(P("Accidents can be prevented by tackling <b>every risk factor</b>. There are three:", "Los accidentes se pueden evitar previniendo <b>todos los factores de riesgo</b>. Son tres:"))
    B.append(FIG(risk_factors, "The driver is involved in most accidents; the road comes second and the vehicle last. The ranges add up to more than 100 % because an accident usually has several causes.",
                 "El conductor interviene en la mayoría de los accidentes; la vía es el segundo factor y el vehículo el último. Los intervalos suman más del 100 % porque un accidente suele tener varias causas."))

    B.append(H3("4.1 The human factor", "4.1 Factor humano"))
    B.append(P(
        "The human factor is the <b>main cause</b> of accidents (<b>70–90 %</b>): most are due to <b>unsuitable behaviour by the driver</b>. You must adapt your behaviour to what driving demands (your state, speed, the road, the weather, "
        "traffic density, distractions, rules and signs). Your ability depends on your <b>training</b> and your <b>experience</b>.",
        "El factor humano es el <b>principal responsable</b> de los accidentes (<b>70–90 %</b>): la mayoría se deben a <b>comportamientos inadecuados del conductor</b>. Hay que adaptar el comportamiento al nivel exigido (estado del conductor, velocidad, vía, climatología, "
        "densidad de circulación, distracciones, normas y señales). La capacidad depende de la <b>formación</b> y de la <b>experiencia</b>."))
    B.append(BOX("key", "The driver’s most frequent causes of accidents", "Causas de accidentes más frecuentes por el conductor", [
        ("<b>Distraction or lack of attention</b>; not keeping the <b>safety distance</b>; <b>excessive or unsuitable speed</b>.", "<b>Distracciones o falta de atención</b>; no mantener la <b>distancia de seguridad</b>; <b>velocidad excesiva</b> o inadecuada."),
        ("Not giving way; <b>wrong turns</b>; <b>illegal overtaking</b>; improper use of the carriageway.", "No respetar la preferencia de paso; <b>giros incorrectos</b>; <b>adelantamientos antirreglamentarios</b>; uso indebido de la calzada."),
    ]))

    B.append(H3("4.1.1 Speed", "4.1.1 La velocidad"))
    B.append(TABLE(
        [T("Speed and the driver", "Relación velocidad y conductor")],
        rows([
            ("As speed rises, the <b>field of vision narrows</b> — the <b>tunnel effect</b> (<i>efecto túnel</i>): only the centre of the road is seen sharply, and the sides go by too fast to be taken in. Especially dangerous at <b>intersections</b> and with <b>sideways movements</b>.",
             "Al aumentar la velocidad <b>disminuye el campo visual</b>: el <b>efecto túnel</b>. Solo se percibe con nitidez el centro de la vía y las imágenes laterales pasan demasiado rápido. Es especialmente peligroso en las <b>intersecciones</b> y en los <b>desplazamientos laterales</b>."),
            ("<b>Less ability to see and analyse</b> what is going on (more serious mistakes): <b>anticipation and reaction get worse</b>. And <b>injuries are more serious</b>.",
             "<b>Menor capacidad para ver y analizar</b> lo que ocurre (errores más graves): <b>disminuye la capacidad de anticipación y de reacción</b>. Y las <b>lesiones son más graves</b>."),
            ("Driving fast for a long time on wide, good roads makes you <b>feel slower than you really are</b> (take care when entering towns); it raises <b>tension</b>, brings <b>fatigue</b> sooner and makes you more <b>hostile or aggressive</b>.",
             "Conducir mucho tiempo deprisa por vías amplias da la <b>sensación de ir más despacio de lo que se va</b> (cuidado en los accesos a las ciudades); aumenta la <b>tensión</b>, adelanta la <b>fatiga</b> y los comportamientos <b>hostiles o agresivos</b>."),
        ]),
    ))
    B.append(BOX("key", "Remember", "Recuerda", [("<b>90 %</b> of the information needed to drive is <b>visual</b>.", "El <b>90 %</b> de la información necesaria para conducir es de <b>carácter visual</b>.")]))
    B.append(FIG(stopping_distance, "From seeing the danger to stopping: the car first travels the reaction distance without slowing down, then the braking distance. Rain doubles the braking distance; snow or ice multiplies it by ten.",
                 "Desde que se ve el peligro hasta que se para: primero se recorre la distancia de reacción sin frenar, después la de frenado. La lluvia duplica la distancia de frenado; la nieve o el hielo la multiplican por diez."))
    B.append(TABLE(
        [T("Term", "Concepto"), T("Meaning", "Significado")],
        [
            [T("<b>Reaction time</b>", "<b>Tiempo de reacción</b>"),
             T("From <b>perceiving a stimulus</b> to <b>responding</b>. Normally between half a second and one second — <b>typically 0.75 s</b>. It grows with <b>age</b>, <b>fatigue</b> and drowsiness, <b>alcohol, drugs</b> and some <b>medicines</b>, mood, illness, stress, and <b>heat</b> or too much heating.",
               "Desde que el conductor <b>percibe un estímulo</b> hasta que <b>responde</b>. Normalmente entre medio y un segundo, <b>habitual 0,75 s</b>. Aumenta con la <b>edad</b>, la <b>fatiga</b> y la somnolencia, el <b>alcohol, las drogas</b> y algunos <b>medicamentos</b>, el estado de ánimo, enfermedades, estrés, y el <b>calor</b> o exceso de calefacción.")],
            [T("<b>Reaction distance</b>", "<b>Distancia de reacción</b>"),
             T("What the vehicle travels <b>during the reaction time</b>. It depends on how fast the driver reacts and on the <b>speed</b>: more speed or a longer reaction time means more distance.",
               "Lo que recorre el vehículo <b>durante el tiempo de reacción</b>. Depende de lo rápido que reaccione el conductor y de la <b>velocidad</b>: más velocidad o más tiempo de reacción, más distancia.")],
            [T("<b>Braking distance</b>", "<b>Distancia de frenado</b>"),
             T("From <b>pressing the brake</b> to <b>stopping</b>. It depends on the <b>speed</b>, the vehicle’s <b>mass</b> and load (a passenger on a motorcycle makes it longer), the driving <b>technique</b>, the vehicle’s <b>condition</b> (tyres, brakes, suspension), "
               "the <b>road surface</b> and grip, and the <b>weather</b> (rain <b>×2</b>, snow or ice <b>×10</b>).",
               "Desde que se <b>acciona el freno</b> hasta que el vehículo <b>se detiene</b>. Depende de la <b>velocidad</b>, la <b>masa</b> del vehículo y la carga (un pasajero en la moto la aumenta), la <b>técnica</b> de conducción, el <b>estado del vehículo</b> (neumáticos, frenos, suspensión), "
               "el <b>estado de la vía</b> y la adherencia, y la <b>meteorología</b> (lluvia <b>×2</b>, nieve o hielo <b>×10</b>).")],
            [T("<b>Stopping distance</b> (<i>parada técnica</i>)", "<b>Distancia de detención</b> (parada técnica)"),
             T("From <b>seeing the obstacle</b> to stopping: <b>reaction distance + braking distance</b>.", "Desde que se <b>ve el obstáculo</b> hasta que se detiene: <b>distancia de reacción + distancia de frenado</b>.")],
        ],
        widths=["24%", "76%"],
    ))
    B.append(P(
        "Quick maths: <b>km/h ÷ 3.6 = metres per second</b>. At 90 km/h you cover 25 m every second, so in a typical 0.75 s reaction time the car travels about <b>19 m before you even touch the brake</b>; at 50 km/h, about 10 m.",
        "Cálculo rápido: <b>km/h ÷ 3,6 = metros por segundo</b>. A 90 km/h se recorren 25 m cada segundo, así que en un tiempo de reacción de 0,75 s el coche avanza unos <b>19 m antes de tocar el freno</b>; a 50 km/h, unos 10 m."))
    B.append(BOX("key", "To avoid an accident", "Para evitar un accidente", [
        ("Drive at a speed at which your <b>stopping distance is shorter than the distance to the obstacle</b>.", "Hay que llevar una velocidad tal que la <b>distancia de detención sea menor que la distancia al obstáculo</b>."),
        ("How well a driver responds also depends on the <b>training</b> they have had.", "La capacidad de respuesta del conductor también depende de la <b>formación</b> recibida."),
    ]))

    B.append(H3("4.1.2 Fatigue and sleep", "4.1.2 Fatiga y sueño"))
    B.append(P(
        "<b>Fatigue</b>, together with sleep, is one of the main causes of accidents, especially among <b>professional drivers</b>. It harms perception, attention, movement, behaviour and decision-making.",
        "La <b>fatiga</b>, junto con el sueño, es una de las principales causas de accidente, especialmente entre los <b>conductores profesionales</b>. Altera la percepción, la atención, la movilidad, el comportamiento y la toma de decisiones."))
    B.append(TABLE(
        [T("Main effects of fatigue", "Principales efectos de la fatiga")],
        rows([
            ("<b>Muscle stiffness</b> (shifting in the seat, cramps, yawning, back or neck ache); <b>slow, imprecise movements</b>; <b>blurred vision</b> and worse hearing.",
             "<b>Agarrotamiento muscular</b> (más movimientos en el asiento, calambres, bostezos, molestias en espalda o nuca); <b>lentitud y falta de precisión</b>; <b>visión borrosa</b> y menos sensibilidad auditiva."),
            ("<b>Behaviour changes</b>: hostile, irritable, more risks. <b>Less attention and concentration</b> (you lose the sense of speed).", "<b>Cambios de comportamiento</b>: conductas hostiles, irritación, más riesgos. <b>Menos atención y concentración</b> (pérdida de sensación de velocidad)."),
            ("<b>Slower reactions</b> (longer reaction time); <b>fewer steering corrections</b> and more errors; <b>more passive, automatic driving</b>.", "<b>Menor capacidad de reacción</b> (aumenta el tiempo de reacción); <b>menos correcciones de la trayectoria</b> y más errores; <b>conducción más pasiva y automatizada</b>."),
        ]),
    ))
    B.append(TABLE(
        [T("Fatigue comes from…", "La fatiga se debe…"), T("Circumstances", "Circunstancias")],
        [
            [T("<b>The driver</b>", "<b>Al conductor</b>"),
             T("Little experience; <b>driving for long periods without proper breaks</b> (the main cause); bad posture; high speed for a long time; driving sleepy, after alcohol or ill (even a cold); changes in your normal driving habits; stress.",
               "Poca experiencia; <b>conducir largos periodos sin descansar</b> o descansando mal (principal causa); posturas inadecuadas; velocidad excesiva mucho tiempo; conducir con sueño, alcohol o enfermo (incluso resfriado); cambios en los hábitos de conducción; estrés.")],
            [T("<b>The road</b>", "<b>A la vía y entorno</b>"), T("Heavy traffic, jams and hold-ups; a poor road surface; unfamiliar roads; bad weather.", "Mucho tráfico, congestiones y retenciones; firme en mal estado; vías poco conocidas; climatología adversa.")],
            [T("<b>The vehicle</b>", "<b>Al vehículo</b>"),
             T("Poor condition (suspension, steering, lighting); poor ventilation or <b>high temperature</b> — recommended <b>20–23 °C</b>, without blowing air at your eyes; an unergonomic seat or interior.",
               "Mal estado (suspensión, dirección, iluminación); mala ventilación o <b>temperatura elevada</b> (recomendada <b>20–23 °C</b>, sin dirigir el aire a los ojos); asiento o interior poco ergonómico.")],
        ],
        widths=["22%", "78%"],
    ))
    B.append(P(
        "<b>Sleep</b> is one of the biggest dangers. It usually comes with fatigue (each brings on the other) and causes <b>15–30 % of accidents</b>, usually serious ones. <b>You don’t need to fall asleep</b> to crash: the risks of drowsiness start "
        "much earlier, and these accidents happen <b>by day as well as by night</b>.",
        "El <b>sueño</b> es uno de los mayores peligros. Suele aparecer junto con la fatiga (una lleva a la otra) y causa <b>entre el 15 y el 30 % de los accidentes</b>, que suelen ser graves. <b>No hace falta llegar a dormirse</b>: los riesgos de la somnolencia "
        "aparecen mucho antes, y estos accidentes ocurren <b>tanto de día como de noche</b>."))
    B.append(TABLE(
        [T("Why drowsiness raises the risk", "Por qué la somnolencia aumenta el riesgo")],
        rows([
            ("<b>Longer reaction time</b>; <b>more distractions</b> (especially on monotonous roads with little traffic); slower decisions with more mistakes.", "<b>Aumenta el tiempo de reacción</b>; <b>más distracciones</b> (sobre todo en entornos monótonos y con poco tráfico); decisiones más lentas y con más errores."),
            ("Slower, less precise, automatic movements; <b>microsleeps</b> — a few seconds asleep without realising it.", "Movimientos más lentos, imprecisos y automatizados; <b>microsueños</b>: unos segundos dormido sin darse cuenta."),
            ("Worse perception (tired eyes, blurred vision, more dazzle); behaviour changes (restlessness, hostility, more risk, <b>speeding to arrive sooner</b>).", "Peor percepción (fatiga ocular, visión borrosa, más deslumbramiento); cambios de comportamiento (inquietud, hostilidad, más riesgo, <b>acelerar para llegar antes</b>)."),
        ]),
    ))
    B.append(FIG(drowsy_clock, "Drowsiness peaks in the early hours (3–5 h) and early afternoon (14–16 h). Plan breaks: at least every 2 hours or 200 km, for 20–30 minutes.",
                 "La somnolencia aprieta de madrugada (3–5 h) y a primera hora de la tarde (14–16 h). Planifica las paradas: como mínimo cada 2 horas o 200 km, de 20 a 30 minutos."))
    B.append(TABLE(
        [T("Tips against drowsiness", "Consejos para evitar la somnolencia")],
        rows([
            ("<b>Time of day</b>: take care in the <b>early hours (3–5 h)</b> and the <b>early afternoon (14–16 h)</b>. Avoid driving when you would normally be asleep; extra care with <b>shift work</b>.",
             "<b>Momento del día</b>: atención en la <b>madrugada (de 3 a 5)</b> y en las <b>primeras horas de la tarde (de 14 a 16)</b>. Evita conducir en tus horas habituales de sueño; precaución con los <b>turnos cambiantes</b>."),
            ("<b>Sleep quality and quantity</b>: sleeping badly is as dangerous as sleeping too little; <b>7–9 hours</b> of deep sleep is right.", "<b>Calidad y cantidad del sueño</b>: dormir mal es tan peligroso como dormir poco; <b>7–9 horas</b> de sueño profundo es lo adecuado."),
            ("<b>Monotony</b>: driving at night on an empty motorway brings on sleep. <b>Heavy meals</b> sedate; <b>high temperatures</b> cause sleepiness.", "<b>Monotonía</b>: conducir de noche por autovía sin tráfico favorece el sueño. Las <b>comidas copiosas</b> tienen efecto sedante; las <b>altas temperaturas</b> provocan sueño."),
            ("<b>Sedatives and stimulants</b>: alcohol and medicines bring on sleep; tea or coffee have a <b>rebound effect</b> — sleep comes suddenly when they wear off.", "<b>Sedantes y estimulantes</b>: el alcohol y los medicamentos favorecen el sueño; el té o el café tienen <b>efecto rebote</b>: el sueño aparece de golpe cuando pasa su efecto."),
            ("<b>Individual differences and sleep disorders</b>: insomnia can bring daytime sleepiness; <b>narcolepsy</b> legally prevents getting a licence.", "<b>Diferencias individuales y trastornos del sueño</b>: el insomnio puede causar somnolencia diurna; la <b>narcolepsia</b> impide legalmente obtener el permiso."),
        ]),
    ))
    B.append(BOX("key", "Reducing the risk from fatigue or sleep", "Reducir el riesgo por fatiga o sueño", [
        ("Watch for the first <b>signs of tiredness or sleep</b>; if they appear, the best thing is to <b>stop and rest in a suitable place</b>.", "Atención a los primeros <b>síntomas de fatiga o sueño</b>; si aparecen, lo mejor es <b>parar a descansar en un lugar adecuado</b>."),
        ("Stop <b>at least every 2 hours or 200 km</b> (more often if tired), for <b>20–30 minutes</b>: stretch your legs, get some air and, if needed, <b>sleep</b>.", "Parar <b>como mínimo cada 2 horas o 200 km</b> (más a menudo si hay cansancio), <b>20–30 minutos</b>: estirar las piernas, tomar el aire y, si hace falta, <b>dormir</b>."),
    ]))
    B.append(P(
        "<b>Rumble strips</b> (<i>guías sonoras longitudinales fresadas</i>, GSLF) are bands milled into the asphalt that warn the driver, by <b>noise and vibration</b>, of an <b>unintended lane departure</b>. "
        "They give extra time to correct the path before leaving the road or crossing into oncoming traffic, and add safety without big changes to the road.",
        "Las <b>guías sonoras longitudinales fresadas</b> (GSLF) son bandas fresadas en el asfalto que alertan al conductor, mediante <b>sonido y vibración</b>, del <b>abandono involuntario de su carril</b>. "
        "Dan un tiempo añadido para corregir la trayectoria antes de salirse de la vía o invadir el sentido contrario, y aportan seguridad sin modificar sustancialmente la infraestructura."))
    B.append(FIG(rumble_strips, "Rumble strips on the centre line separate the two directions; strips at the road edge warn you before you run off the road. A sign may announce them (“guías sonoras en eje”).",
                 "Las guías en el eje separan los sentidos; las del borde de la calzada avisan antes de salirse de la vía. Una señal puede anunciarlas («guías sonoras en eje»)."))

    B.append(H3("4.1.3 Illness and medicines", "4.1.3 Enfermedades y medicamentos"))
    B.append(P(
        "Illness and medicines can affect the <b>basic abilities needed to drive safely</b> (especially mental illness and neurological disorders). Drivers with a <b>chronic illness</b> should: know the illness and the <b>side effects of their medicines</b>; "
        "recognise the <b>first symptoms</b> of a crisis and know what to do; avoid what <b>triggers</b> a crisis; <b>never drink alcohol while taking medicines</b>; and <b>ask their doctor</b> when in doubt.",
        "Las enfermedades y los medicamentos pueden afectar a las <b>capacidades básicas para conducir con seguridad</b> (sobre todo las enfermedades mentales y los trastornos neurológicos). Quien padezca una <b>enfermedad crónica</b> debe: conocer la enfermedad y los "
        "<b>efectos secundarios de los medicamentos</b>; reconocer los <b>primeros síntomas</b> de una crisis y saber actuar; evitar lo que la <b>desencadena</b>; <b>no tomar alcohol con medicamentos</b>; y <b>consultar al médico</b> en caso de duda."))
    B.append(TABLE(
        [T("Condition", "Situación"), T("Effects on driving", "Efectos en la conducción"), T("Advice", "Consejos")],
        [
            [T("<b>Allergies</b>", "<b>Alergias</b>"),
             T("Cold-like symptoms: <b>misjudged distances</b>, <b>less concentration</b>, especially in a sneezing fit. <b>Antihistamines</b> can cause <b>strong drowsiness</b>, especially <b>first-generation</b> ones; newer ones (third generation) are safer, but <b>never with alcohol or drugs</b>.",
               "Síntomas parecidos al resfriado: <b>errores al calcular distancias</b> y <b>menos concentración</b>, sobre todo en una crisis de estornudos. Los <b>antihistamínicos</b> pueden provocar <b>gran somnolencia</b>, sobre todo los de <b>primera generación</b>; los de tercera son más seguros, pero <b>nunca con alcohol o drogas</b>."),
             T("Keep the <b>windows closed</b>; <b>air conditioning not too strong</b>; clean interior and vents; no alcohol when on medication; no very long trips; <b>sunglasses</b>; avoid driving at dawn and in damp areas; <b>don’t self-medicate</b>.",
               "<b>No abrir las ventanillas</b>; <b>aire acondicionado no muy fuerte</b>; habitáculo y conductos limpios; sin alcohol si se medica; no hacer viajes muy largos; <b>gafas de sol</b>; evitar el amanecer y las zonas húmedas; <b>no automedicarse</b>.")],
            [T("<b>Stress</b>", "<b>Estrés</b>"),
             T("More <b>aggression, hostility and competitiveness</b>; more <b>reckless</b>, more risk accepted; tendency to <b>ignore signs and rules</b>; slower decisions, more errors; more distractions; fatigue sooner.",
               "Más <b>agresividad, hostilidad y competitividad</b>; más <b>imprudencia</b> y aceptación del riesgo; tendencia a <b>no respetar señales y normas</b>; decisiones más lentas y más errores; más distracciones; antes aparece la fatiga."),
             T("Seek <b>specialist help</b>; don’t drive unless strictly necessary (especially in the worst phase, or if on medication).", "<b>Buscar ayuda especializada</b>; no conducir salvo que sea estrictamente necesario (sobre todo en la fase más crítica o si se está medicado).")],
            [T("<b>Depression</b>", "<b>Depresión</b>"),
             T("<b>More distractions</b> (absorbed in thoughts); you miss information from the surroundings; more sensitive to <b>drowsiness and fatigue</b>; irritability and anxiety; <b>psychotropic drugs</b> can seriously impair driving. "
               "The law forbids driving <b>under the effects</b> of certain psychotropics (antidepressants, anxiolytics, sedatives, hypnotics, antipsychotics).",
               "<b>Más distracciones</b> (atención centrada en sus pensamientos); pierde información del entorno; más sensible a la <b>somnolencia y la fatiga</b>; irritabilidad y ansiedad; los <b>psicofármacos</b> pueden alterar gravemente la conducción. "
               "La normativa prohíbe conducir <b>bajo los efectos</b> de determinados psicofármacos (antidepresivos, ansiolíticos, sedantes, hipnóticos, antipsicóticos)."),
             T("See a <b>specialist before driving</b>; don’t self-medicate or take alcohol or other drugs; avoid driving in the <b>most acute phase</b>; avoid night, monotonous or very long drives.", "Consultar a un <b>especialista antes de conducir</b>; no automedicarse ni tomar alcohol u otras drogas; evitar conducir en la <b>fase más aguda</b>; evitar la noche, la monotonía y los trayectos largos.")],
        ],
        widths=["14%", "48%", "38%"],
        cls="small",
    ))
    B.append(TABLE(
        [T("Medicines: not everyone reacts the same", "Medicamentos: no todos reaccionan igual")],
        rows([
            ("Ask your <b>doctor or pharmacist</b> about the risks; follow the doses and times prescribed; <b>never self-medicate</b> or mix with <b>alcohol</b>.", "Consultar los riesgos al <b>médico o al farmacéutico</b>; seguir la pauta de horas y dosis; <b>no automedicarse</b> ni mezclar con <b>alcohol</b>."),
            ("Read the <b>leaflet</b> to see whether it affects driving — <b>alternative or natural remedies</b> can have negative effects too.", "Consultar el <b>prospecto</b> por si afecta a la conducción; las <b>medicinas alternativas o naturales</b> también pueden tener efectos negativos."),
            ("Try not to drive, or be very careful, at the <b>start of any treatment</b>; don’t mix medicines (unless the doctor says so); careful with <b>coffee</b> and other substances that change their effect.",
             "Intentar no conducir, o ser muy prudente, al <b>inicio de cualquier tratamiento</b>; no mezclar medicamentos (salvo indicación médica); cuidado con el <b>café</b> y otras sustancias que alteran sus efectos."),
        ]),
    ))
    B.append(TABLE(
        [T("Pictogram", "Pictograma"), T("What it means", "Qué significa")],
        [[T(PICTO, PICTO), T("<b>“Driving: see the leaflet”</b> (<i>Conducción: ver prospecto</i>). It appears on the box of some medicines and <b>warns — it does not forbid</b> — that you should read the leaflet, which describes all the side effects that can affect a driver.",
                            "<b>«Conducción: ver prospecto»</b>. Aparece en la caja de algunos medicamentos y <b>advierte (no prohíbe)</b> que es recomendable leer el prospecto, donde se describen todos los efectos adversos que pueden afectar al conductor.")]],
        widths=["20%", "80%"],
    ))

    B.append(H3("4.1.4 Heat", "4.1.4 Calor"))
    B.append(TABLE(
        [T("Effects of heat on the driver", "Efectos del calor"), T("How to avoid the risk", "Cómo evitar los riesgos")],
        [[T("<b>Longer reaction time</b>; <b>more mistakes</b>; more <b>fatigue</b>, sleepiness and distraction; more <b>hostility and aggression</b> towards others.",
            "<b>Aumenta el tiempo de reacción</b>; se cometen <b>más errores</b>; más <b>fatiga</b>, sueño y distracciones; más <b>hostilidad y agresividad</b>."),
          T("<b>More stops</b> (20–30 min every 2 h or 200 km); avoid <b>parking in the sun</b>; drink <b>water or juice</b>, avoid hot, heavy meals and take care after eating; light, pale clothes and good <b>sunglasses</b>; air conditioning at <b>20–23 °C</b>.",
            "<b>Más paradas</b> (20–30 min cada 2 h o 200 km); evitar <b>estacionar al sol</b>; beber <b>agua o zumos</b>, evitar comidas calientes y pesadas y extremar la precaución después de comer; ropa clara y ligera y <b>gafas de sol</b> adecuadas; climatización a <b>20–23 °C</b>.")]],
        widths=["44%", "56%"],
    ))

    B.append(H3("4.1.5 Distractions", "4.1.5 Distracciones"))
    B.append(P(
        "Distractions are the risk factor that has <b>grown the most</b> in the last decade — behind <b>one in three fatal accidents</b>. Especially among <b>young drivers (18–25)</b> and <b>over-70s</b>; when the driver has company (talking, arguing, noisy children); "
        "in summer, at weekends and on leisure trips; and on the open road, especially <b>autopistas and autovías</b> (monotony). To drive safely, <b>give all your attention to driving</b>.",
        "Las distracciones son el <b>factor de riesgo que más ha aumentado</b> en la última década: causa <b>uno de cada tres accidentes mortales</b>. Sobre todo en <b>jóvenes de 18 a 25 años</b> y <b>mayores de 70</b>; cuando el conductor va acompañado (conversando, discutiendo, niños alborotados); "
        "en verano, fines de semana y trayectos de ocio; y en carretera, sobre todo en <b>autopista y autovía</b> (monotonía). Para conducir con seguridad hay que <b>centrar toda la atención en la conducción</b>."))
    B.append(TABLE(
        [T("Using the mobile phone — held in the hand or even hands-free", "El móvil al volante, en la mano o incluso con manos libres")],
        rows([
            ("<b>Attention drops</b>. The most dangerous moments: <b>answering</b>, <b>dialling or texting</b>, talking, and <b>hanging up</b> or putting the phone down.", "<b>Se reduce la atención</b>. Momentos más peligrosos: al <b>recibir la llamada</b>, <b>marcar o escribir</b>, mientras se habla y al <b>colgar</b> o dejar el teléfono."),
            ("<b>More offences</b>: after a minute and a half, <b>40 % of signs</b> go unnoticed. Distances are misjudged (the safety distance shrinks).", "<b>Más infracciones</b>: al minuto y medio se deja de percibir el <b>40 % de las señales</b>. Se calculan peor las distancias (se reduce la de seguridad)."),
            ("<b>Worse speed control</b>: sudden changes; after a minute and a half the average speed <b>drops 12 %</b>.", "<b>Peor control de la velocidad</b>: cambios bruscos; al minuto y medio la velocidad media <b>baja un 12 %</b>."),
            ("<b>Swerving</b> and poor handling — the <b>most frequent phone accident is running off the road</b>; disorientation and bad decisions. It is like driving with <b>1 g/l of alcohol in the blood</b>.",
             "<b>Desviaciones de la trayectoria</b> y problemas de maniobrabilidad: el <b>accidente más frecuente por el móvil es la salida de la vía</b>; desorientación y decisiones erróneas. Es similar a conducir con <b>1 g/l de alcohol en sangre</b>."),
        ]),
    ))
    B.append(BOX("trap", "Phone rules", "Normas con el móvil", [
        ("<b>Using the phone by hand while driving is prohibited — even when stopped at traffic lights.</b> Holding it in your hand: <b>6 points and 200 €</b>.", "<b>Prohibido utilizar manualmente el móvil durante la conducción, incluso detenido en un semáforo.</b> Sujetándolo con la mano: <b>6 puntos y 200 €</b>."),
        ("With <b>hands-free</b>, tell the caller you are driving and <b>don’t talk for more than a minute</b>. Better still, don’t use it: stop somewhere safe. Take care also because a ringing phone, like any noise, can <b>startle</b> you.",
         "Con <b>manos libres</b>, indica que conduces y <b>no hables más de un minuto</b>. Mejor no usarlo: detente en un lugar seguro. Ojo también porque el sonido del teléfono, como cualquier ruido, puede <b>sorprender</b>."),
    ]))
    B.append(TABLE(
        [T("Sat-navs (GPS)", "Navegadores GPS")],
        rows([
            ("<b>Plan the trip before setting off</b> and programme speed limits if possible (choose the safest route); follow the <b>voice instructions</b> rather than the screen.", "<b>Planificar el viaje antes de iniciarlo</b> y programar los límites si es posible (itinerario más seguro); seguir las <b>instrucciones de voz</b> y no mirar la pantalla."),
            ("Watch the signs, the road and the traffic: even if the sat-nav suggests a route, <b>your own judgement always comes first</b>.", "Fijarse en la señalización, la vía y el tráfico: aunque el navegador aconseje un camino, <b>el juicio del conductor debe prevalecer siempre</b>."),
            ("A portable unit needs a <b>proper mount</b> (so it can’t fall), placed where it <b>doesn’t block your view</b> or make you look away — and <b>never near the airbag</b>; route the cables away from the wheel and gear lever. "
             "Your main speed reference is the <b>speedometer</b>.",
             "Si es portátil: <b>soporte adecuado</b> (que no se caiga), a una altura que <b>no entorpezca la visión</b> ni obligue a apartar la vista, y <b>nunca cerca del airbag</b>; cables que no estorben al volante ni al cambio. "
             "La principal fuente de velocidad es el <b>velocímetro</b>."),
        ]),
    ))
    B.append(TABLE(
        [T("Smoking", "Fumar")],
        rows([
            ("Lighting up and smoking takes <b>one hand off the controls</b> and distracts; smokers tend to rate traffic situations as less dangerous and <b>take more risks</b>.", "Al encender y fumar se <b>pierde maniobrabilidad</b> con una mano y el conductor se distrae; tienden a ver las situaciones como menos peligrosas y a <b>asumir más riesgos</b>."),
            ("The <b>carbon monoxide</b> (CO) in smoke <b>lowers attention</b>; smoke causes <b>vision problems</b>; and smoking brings medical problems, mainly cardiovascular.", "El <b>monóxido de carbono</b> (CO) del tabaco <b>disminuye la atención</b>; crea <b>problemas de visión</b>; y conlleva problemas médicos, sobre todo cardiovasculares."),
        ]),
    ))
    B.append(BOX("key", "Smoking at the wheel", "Fumar al volante", [
        ("It is <b>recommended not to smoke</b> while driving, but it is <b>not prohibited</b>. Throwing a cigarette end out of the window is: it can start a fire (6 points, Topic 9).",
         "Se <b>recomienda no fumar</b> al conducir, aunque <b>no está prohibido</b>. Lo que sí está prohibido es tirar la colilla por la ventanilla: puede provocar un incendio (6 puntos, Tema 9)."),
    ]))

    B.append(H3("4.1.6 Alcohol", "4.1.6 Alcohol"))
    B.append(P(
        "Alcohol makes an accident <b>more likely</b> and its injuries <b>more serious</b>. It is a <b>depressant of the central nervous system</b>, although at first it has a <b>euphoric phase</b>.",
        "El alcohol <b>aumenta la posibilidad de tener un accidente</b> y la <b>gravedad de las lesiones</b>. Es un <b>depresor del sistema nervioso central</b>, aunque al principio tiene una <b>fase euforizante</b>."))
    B.append(TABLE(
        [T("What alcohol changes", "Alteraciones"), T("How", "Cómo")],
        [
            [T("<b>Behaviour</b>", "<b>Comportamiento</b>"), T("<b>False sense of safety and control</b>; less prudent; more offences; impulsive and aggressive responses.", "<b>Falsa sensación de seguridad y control</b>; menos prudente; más infracciones; respuestas impulsivas y agresivas.")],
            [T("<b>Perception</b>", "<b>Percepción</b>"), T("Perceives worse, <b>misjudges distances</b>, more sensitive to <b>dazzle</b>, and may suffer <b>tunnel vision</b>.", "Percibe peor, <b>calcula mal las distancias</b>, más sensible a los <b>deslumbramientos</b> y puede sufrir <b>visión túnel</b>.")],
            [T("<b>Attention</b>", "<b>Atención</b>"), T("More distractions.", "Más distracciones.")],
            [T("<b>Psychomotor skills</b>", "<b>Psicomotricidad</b>"), T("Less precision and coordination.", "Disminuye la precisión y la coordinación.")],
        ],
        widths=["24%", "76%"],
    ))
    B.append(P(
        "The <b>blood alcohol level</b> (<i>tasa de alcoholemia</i>) is the amount of alcohol in the blood. The <b>only truly safe level is 0.0 g/l</b>: below the legal limit you can still crash because of alcohol.",
        "La <b>tasa de alcoholemia</b> es la cantidad de alcohol en la sangre. La <b>única tasa realmente segura es 0,0 g/l</b>: aunque se conduzca por debajo de la máxima permitida, es posible tener un accidente por el alcohol."))
    B.append(TABLE(
        [T("Driver", "Conductor"), T("Exhaled air", "Aire espirado"), T("Blood", "Sangre")],
        [
            [T("<b>General</b> (after the first 2 years of the licence), <b>including cyclists and VMP riders</b>", "<b>En general</b> (pasados los 2 primeros años de permiso), <b>incluidos ciclistas y VMP</b>"), T("<b>0.25 mg/l</b>", "<b>0,25 mg/l</b>"), T("<b>0.5 g/l</b>", "<b>0,5 g/l</b>")],
            [T("Any driver in the <b>first two years</b> of their licence; <b>professional drivers</b>", "Cualquier conductor en los <b>dos primeros años</b> de permiso o licencia; <b>conductores profesionales</b>"), T("<b>0.15 mg/l</b>", "<b>0,15 mg/l</b>"), T("<b>0.3 g/l</b>", "<b>0,3 g/l</b>")],
            [T("Drivers <b>under 18</b> (any vehicle, bicycles and mopeds included)", "Conductores <b>menores de edad</b> (cualquier vehículo, también bici y ciclomotor)"), T("<b>0.0 mg/l</b>", "<b>0,0 mg/l</b>"), T("<b>0.0 g/l</b>", "<b>0,0 g/l</b>")],
        ],
        widths=["56%", "22%", "22%"],
    ))
    B.append(BOX("trap", "You can’t fool the breathalyser", "No se puede engañar al etilómetro", [
        ("There are <b>no tricks</b>: exercise, chewing gum or sweets, coffee, oil, smoking, mouth sprays, a short nap or lots of water — <b>none of them works</b>.", "<b>No hay trucos</b>: hacer ejercicio, chicles o caramelos, café, aceite, fumar, sprays bucales, dormir un poco o beber mucha agua: <b>nada funciona</b>."),
    ]))
    B.append(FIG(bac_curve, "Blood alcohol over time (illustration, no real figures): it appears within minutes, peaks 30–90 minutes after drinking and then falls very slowly. Food in the stomach makes it rise more slowly and lower.",
                 "La tasa de alcohol a lo largo del tiempo (ilustración, sin cifras reales): aparece en pocos minutos, alcanza el máximo entre 30 y 90 minutos después de beber y luego baja muy despacio. Con comida en el estómago sube más despacio y menos."))
    B.append(TABLE(
        [T("Effects depend on", "Dependen de"), T("How", "Cómo")],
        [
            [T("<b>The driver</b>", "<b>Características del conductor</b>"),
             T("<b>Weight</b> (more effect on slim people); <b>sex</b> (more effect on women); <b>age</b> (more on under-18s and over-65s); <b>circumstances</b> (fatigue, sleep, stress, illness); "
               "<b>experience</b> — the effects are greater on inexperienced drivers, which is why their limit is lower.",
               "<b>Peso</b> (afecta más a las personas delgadas); <b>sexo</b> (más a las mujeres); <b>edad</b> (más a menores de 18 y mayores de 65); <b>circunstancias</b> (fatiga, sueño, estrés, enfermedades); "
               "<b>experiencia</b>: los efectos son mayores en los conductores con poca experiencia, por eso su tasa es más reducida.")],
            [T("<b>How it is drunk</b>", "<b>Forma de ingestión</b>"),
             T("<b>Quantity</b> — the most important factor. <b>Time</b>: in the blood after <b>5 minutes</b>, highest level after <b>30–90 minutes</b>, then disappears very slowly over several hours. "
               "<b>Speed</b>: drinking fast raises it more. <b>Time of day</b>: eliminated more slowly while asleep. <b>Type</b>: <b>fermented</b> drinks (beer, wine) are absorbed <b>more slowly</b> than <b>distilled</b> ones (gin, rum, whisky, vodka); "
               "<b>fizzy or hot</b> drinks act faster. <b>Empty stomach</b>: alcohol passes into the blood faster (higher level).",
               "<b>Cantidad</b>: el factor más importante. <b>Tiempo</b>: en sangre a los <b>5 minutos</b>, pico entre <b>30 y 90 minutos</b>, y después desaparece muy lentamente, varias horas. "
               "<b>Rapidez</b>: beber deprisa afecta más. <b>Hora</b>: se elimina más despacio durante el sueño. <b>Tipo</b>: las <b>fermentadas</b> (cerveza, vino) se absorben <b>más lentamente</b> que las <b>destiladas</b> (ginebra, ron, whisky, vodka); "
               "las <b>gaseosas o calientes</b>, más rápido. <b>En ayunas</b>: pasa antes a la sangre (mayor tasa).")],
        ],
        widths=["22%", "78%"],
    ))
    B.append(BOX("key", "Remember", "Recuerda", [("The effects of alcohol are <b>not always the same</b>: two people who drink the same <b>need not reach the same level</b>.", "Los efectos del alcohol <b>no son siempre los mismos</b>: dos personas que beben lo mismo <b>no tienen por qué alcanzar la misma tasa</b>.")]))

    B.append(H3("4.1.7 Drugs", "4.1.7 Drogas"))
    B.append(P(
        "Driving on public roads is <b>prohibited</b> for any driver — <b>cyclists and VMP riders included</b> — with <b>drugs</b> in their body (narcotics, psychotropics, stimulants, or medicines and similar substances that alter the physical or mental state). "
        "The exception is substances taken <b>on prescription for treatment</b>, <b>as long as they don’t affect driving</b>. Many of the most serious accidents are linked to drugs, and mixed with alcohol their effects become <b>unpredictable</b>.",
        "Está <b>prohibido</b> circular a los conductores de vehículos, <b>incluso ciclistas o VMP</b>, que hayan ingerido o incorporado <b>drogas</b> (estupefacientes, psicotrópicos, estimulantes, y medicamentos u otras sustancias análogas que alteren el estado físico o mental). "
        "Quedan excluidas las sustancias usadas <b>bajo prescripción médica y con finalidad terapéutica</b>, <b>siempre que no afecten a la conducción</b>. Gran parte de los accidentes más graves están relacionados con las drogas, y mezcladas con alcohol sus efectos son <b>imprevisibles</b>."))
    B.append(TABLE(
        [T("Drug", "Droga"), T("Effects on the driver", "Efectos en el conductor")],
        [
            [T("<b>Cannabis</b>", "<b>Cannabis</b>"), T("Distorted perception of surroundings, <b>time and space</b>; loss of concentration; <b>longer reaction time</b>; drowsiness.", "Altera la percepción del entorno, el <b>tiempo y el espacio</b>; pérdida de concentración; <b>aumenta el tiempo de reacción</b>; somnolencia.")],
            [T("<b>Cocaine</b>", "<b>Cocaína</b>"), T("<b>Aggressive, impulsive, competitive</b> behaviour; <b>overestimating your abilities</b>; distorted perception; less concentration.", "Conductas <b>agresivas, impulsivas y competitivas</b>; <b>sobrevaloración de las capacidades</b>; altera la percepción; reduce la concentración.")],
            [T("<b>Ecstasy</b> (MDMA)", "<b>Éxtasis</b> (MDMA)"), T("Optical illusions and blurred vision; more <b>sensitive to dazzle</b>; depression and anxiety; less concentration; physical and mental <b>exhaustion</b> when it wears off (<b>flashbacks</b> hours later).",
                                                                  "Ilusiones ópticas y visión borrosa; mayor <b>sensibilidad al deslumbramiento</b>; depresión y ansiedad; menos concentración; <b>agotamiento</b> físico y mental al pasar el efecto (<b>flashbacks</b> horas después).")],
            [T("<b>LSD</b>", "<b>LSD</b>"), T("Strong <b>distortions of reality and hallucinations</b>; emotional changes (aggression, anxiety, panic); effects can last <b>10–12 hours</b> (flashbacks possible).", "Fuertes <b>distorsiones de la realidad y alucinaciones</b>; alteraciones emocionales (agresividad, ansiedad, pánico); los efectos pueden durar <b>10 o 12 horas</b> (flashbacks).")],
            [T("<b>Amphetamines</b>", "<b>Anfetaminas</b>"), T("Impulsive and violent behaviour; overestimating abilities (<b>false security</b>); repetitive movements; they <b>hide fatigue and sleepiness</b> — and sleep comes back with a <b>rebound effect</b>.",
                                                                 "Comportamientos impulsivos y violentos; sobrevaloración (<b>falsa seguridad</b>); movimientos repetitivos y estereotipados; <b>disminuyen la sensación de fatiga y sueño</b>, que reaparece con <b>efecto rebote</b>.")],
        ],
        widths=["18%", "82%"],
    ))

    B.append(H3("4.1.8 Alcohol, drugs and the law", "4.1.8 Tratamiento legal del alcohol y las drogas"))
    B.append(TABLE(
        [T("Step", "Paso"), T("Rule", "Norma")],
        [
            [T("<b>Who can be tested</b>", "<b>Quién está obligado</b>"),
             T("Traffic agents can test for alcohol or drugs: any <b>road user</b> directly involved as possibly responsible in an <b>accident</b>, or who has committed an <b>offence</b>; and any <b>driver</b> (cyclists and VMP included) involved in an accident, "
               "with <b>obvious symptoms</b>, who has committed an offence or who is simply stopped at a <b>preventive check</b>.",
               "Los agentes pueden someter a las pruebas: a cualquier <b>usuario de la vía</b> implicado directamente como posible responsable en un <b>accidente</b> o que haya cometido una <b>infracción</b>; y a cualquier <b>conductor</b> (incluidos ciclistas y VMP) implicado en un accidente, "
               "con <b>síntomas evidentes</b>, que haya cometido una infracción o simplemente requerido en un <b>control preventivo</b>.")],
            [T("<b>Type of test</b>", "<b>Tipo de prueba</b>"),
             T("<b>Alcohol</b>: exhaled air, with approved <b>breathalysers</b> (<i>etilómetros</i>). <b>Drugs</b>: a <b>saliva test</b> with an approved device, then a <b>lab analysis</b>. "
               "At the person’s request or by court order, <b>contrast tests</b> can be done — preferably a <b>blood</b> test, or urine or similar.",
               "<b>Alcohol</b>: aire espirado con <b>etilómetros</b> autorizados. <b>Drogas</b>: <b>prueba salival</b> con un dispositivo autorizado y posterior <b>análisis</b>. "
               "A petición del interesado o por orden judicial se pueden repetir las pruebas <b>de contraste</b>: preferentemente <b>análisis de sangre</b>, orina u otros.")],
            [T("<b>If the result is over the limit</b> (or there are obvious symptoms, even below it)", "<b>Si supera la tasa</b> (o hay síntomas evidentes, aun sin superarla)"),
             T("The agent explains: a <b>second, similar test</b> follows, at least <b>10 minutes</b> after the first (the person, companions or witnesses may check the time); you may make any <b>statements</b>; and you have the <b>right to a contrast analysis</b> "
               "(blood, urine or other), <b>paid in advance</b> by you — charged to you if positive, <b>refunded if negative</b>.",
               "El agente informa: habrá una <b>segunda prueba similar</b>, con al menos <b>10 minutos</b> entre ambas (lo puede controlar el examinado, sus acompañantes o testigos); puede formular las <b>alegaciones</b> que quiera; y tiene <b>derecho a contrastar</b> con análisis "
               "(sangre, orina u otros), <b>abonado previamente</b> por el interesado: a su cargo si es positivo, <b>devuelto si es negativo</b>.")],
            [T("<b>Immobilising the vehicle</b>", "<b>Inmovilización del vehículo</b>"),
             T("If the result is <b>positive</b> (unless another properly licensed person can drive), or if the driver <b>refuses the tests</b>. It ends when the cause disappears (unless a court orders otherwise) or another driver takes over. "
               "The costs of immobilising, towing and storage are paid by the <b>driver</b> or whoever is legally responsible.",
               "Si el resultado es <b>positivo</b> (salvo que pueda conducir otra persona habilitada) o si el conductor <b>se niega a las pruebas</b>. Termina cuando desaparece la causa (salvo orden judicial) o se sustituye al conductor. "
               "Los gastos de inmovilización, traslado y depósito corren a cargo del <b>conductor</b> o de quien deba responder por él.")],
        ],
        widths=["24%", "76%"],
    ))
    B.append(TABLE(
        [T("Result", "Resultado"), T("Fine", "Multa"), T("Points", "Puntos")],
        [
            [T("Alcohol over the limit, up to <b>twice</b> it (0.25–0.50 mg/l; new and professional drivers 0.15–0.30)", "Alcohol por encima de la tasa, hasta el <b>doble</b> (0,25–0,50 mg/l; noveles y profesionales 0,15–0,30)"), T("500 €", "500 €"), T("4", "4")],
            [T("Alcohol over <b>twice</b> the limit (over 0.50 mg/l; new and professional drivers over 0.30)", "Alcohol por encima del <b>doble</b> (más de 0,50 mg/l; noveles y profesionales más de 0,30)"), T("1,000 €", "1.000 €"), T("6", "6")],
            [T("<b>Drugs</b> in the body", "<b>Drogas</b> en el organismo"), T("1,000 €", "1.000 €"), T("6", "6")],
        ],
        widths=["64%", "18%", "18%"],
    ))
    B.append(P(
        "In <b>serious cases</b> it becomes a <b>crime</b> and can mean <b>prison</b>: over <b>0.60 mg/l</b> in air (1.2 g/l in blood), driving under the influence of drugs, or <b>refusing the tests</b> (Topic 9).",
        "En los <b>casos graves</b> es <b>delito</b> y puede acarrear <b>penas de prisión</b>: más de <b>0,60 mg/l</b> en aire (1,2 g/l en sangre), conducir bajo la influencia de drogas o <b>negarse a las pruebas</b> (Tema 9)."))

    # ---------------------------------------------------------------- 4.2 vehicle
    B.append(H3("4.2 The vehicle factor", "4.2 Factor vehículo"))
    B.append(P(
        "Modern vehicles have <b>safety devices</b> that make an accident less likely or less serious, but <b>cannot prevent it completely</b>; some even have automated driving. The <b>driver’s role is essential</b> for them to work: "
        "<b>maintain the vehicle properly</b> even if it is little used, especially near the beach (salt corrosion). The vehicle factor is involved in <b>4–13 %</b> of accidents.",
        "Los vehículos actuales incorporan <b>dispositivos de seguridad</b> que reducen la posibilidad o las consecuencias de un accidente, pero <b>no los impiden por completo</b>; algunos incluso tienen conducción automatizada. El <b>papel del conductor es fundamental</b>: "
        "hay que <b>realizar el mantenimiento adecuado</b> aunque el vehículo no se mueva mucho, sobre todo en zonas de playa (corrosión por la salinidad). El factor vehículo está implicado en el <b>4–13 %</b> de los accidentes."))
    B.append(BOX("key", "The vehicle’s most frequent causes of accidents", "Causas de accidentes más frecuentes por el vehículo", [
        ("Failure of the <b>tyres</b> (<b>the most frequent</b>), the <b>brakes</b>, the <b>lights</b> or the <b>steering</b>; <b>too much load</b> or badly spread load.", "Fallo en los <b>neumáticos</b> (<b>el más frecuente</b>), los <b>frenos</b>, las <b>luces</b> o la <b>dirección</b>; <b>exceso de carga</b> o mala distribución."),
    ]))

    B.append(H3("4.2.1 The driving position", "4.2.1 Puesto del conductor"))
    B.append(TABLE(
        [T("Before starting the engine, adjust…", "Antes de arrancar, regular…"), T("So that…", "Para…")],
        [
            [T("<b>The seat</b>", "<b>El asiento</b>"), T("You can <b>press the pedals all the way down</b> without moving your body forward, with your <b>legs slightly bent</b>.", "Poder <b>pisar a fondo los pedales</b> sin desplazar el cuerpo hacia delante, con las <b>piernas ligeramente flexionadas</b>.")],
            [T("<b>The backrest and the steering wheel</b>", "<b>El respaldo y el volante</b>"), T("Both hands reach the <b>top of the wheel</b> without your back leaving the backrest; in the normal position your <b>arms are slightly bent</b>.", "Llegar a la <b>parte superior del volante</b> con ambas manos sin separar la espalda del respaldo; en posición normal, los <b>brazos ligeramente flexionados</b>.")],
            [T("<b>Seat and wheel height</b>", "<b>Altura del asiento y del volante</b>"), T("You <b>see the road over the wheel</b>.", "<b>Ver la vía por encima del volante</b>.")],
            [T("Then…", "Después…"), T("Head restraint, mirrors and seat belt.", "Reposacabezas, espejos retrovisores y cinturón.")],
        ],
        widths=["34%", "66%"],
    ))
    B.append(BOX("trap", "The most frequent wrong settings", "Reglajes incorrectos más frecuentes", [
        ("<b>Too close to the wheel</b>: fatigue, less mobility (forced, slower movements) and <b>danger from the airbag</b>.", "<b>Demasiado cerca del volante</b>: fatiga, menos movilidad (movimientos forzados y lentos) y <b>peligro por el airbag</b>."),
        ("<b>Too far from the wheel</b>: you can’t act quickly and effectively, and the <b>passive safety devices don’t work properly</b>.", "<b>Demasiado lejos del volante</b>: impide actuar con rapidez y eficacia, y los <b>dispositivos de seguridad pasiva no actúan correctamente</b>."),
    ]))

    B.append(H3("4.2.2 The controls", "4.2.2 Mandos del vehículo"))
    B.append(TABLE(
        [T("Car control", "Mando del turismo"), T("Use", "Uso")],
        [
            [T("<b>Steering wheel</b> (hands)", "<b>Volante</b> (manos)"), T("Steers the front wheels. <b>Both hands on the outside</b>, firm but not tense, at <b>“ten to two” or “quarter to three”</b>. <b>Don’t cross your hands</b> to turn.", "Dirige las ruedas directrices. <b>Con las dos manos por el exterior</b>, firme sin agarrotamiento, en la posición de las <b>2 menos 10 o las 3 menos cuarto</b>. Para girar, <b>no cruzar las manos</b>.")],
            [T("<b>Gear lever</b> (hand)", "<b>Palanca de cambios</b> (mano)"), T("Choose the right gear: <b>low gears</b> give <b>more force but less speed</b>; high gears, less force but more speed.", "Seleccionar la marcha adecuada: las <b>marchas cortas</b> tienen <b>más fuerza pero menos velocidad</b>; las largas, menos fuerza y más velocidad.")],
            [T("<b>Handbrake</b> (hand)", "<b>Freno de mano</b> (mano)"), T("Keeps the vehicle <b>immobilised</b>.", "Asegura la <b>inmovilización</b>.")],
            [T("<b>Clutch</b> (<b>left foot</b>)", "<b>Embrague</b> (<b>pie izquierdo</b>)"), T("<b>Released</b> (engaged): the gearbox receives the engine’s turn and, in gear, sends it to the driving wheels. <b>Pressed</b> (disengaged): it stops receiving it, so you can change gear.",
                                                                                      "<b>Sin pisar</b> (embragado): el cambio recibe el giro del motor y, con marcha metida, lo manda a las ruedas motrices. <b>Pisado</b> (desembragado): deja de recibirlo y se puede cambiar de marcha.")],
            [T("<b>Service brake</b> (<b>right foot</b>)", "<b>Freno de servicio</b> (<b>pie derecho</b>)"), T("Slows down or stops the vehicle safely and smoothly.", "Disminuye la velocidad o detiene el vehículo con seguridad y suavidad.")],
            [T("<b>Accelerator</b> (<b>right foot</b>)", "<b>Acelerador</b> (<b>pie derecho</b>)"), T("Raises the engine speed (rpm, revolutions per minute).", "Aumenta la velocidad de giro del motor (rpm).")],
        ],
        widths=["30%", "70%"],
    ))
    B.append(FIG(moto_controls, "The usual motorcycle layout: right hand — throttle and front brake; left hand — clutch; right foot — rear brake; left foot — gear lever.",
                 "La disposición más común en la moto: mano derecha, acelerador y freno delantero; mano izquierda, embrague; pie derecho, freno trasero; pie izquierdo, selector de marchas."))

    # ---------------------------------------------------------------- 4.2.3 active safety
    B.append(H3("4.2.3 Active safety: tyres", "4.2.3 Seguridad activa: neumáticos"))
    B.append(P(
        "<b>Active safety</b> tries to <b>prevent an accident from happening</b>. Its main elements: <b>wheels, brakes, suspension, steering and lights</b>. The wheels are the <b>only part touching the ground</b>, so they need the most attention: "
        "they are the <b>main cause of accidents from mechanical failure</b>. A wheel is the <b>rim</b>, the <b>tyre</b> and, in some, an <b>inner tube</b>.",
        "La <b>seguridad activa</b> trata de <b>evitar que se produzca un accidente</b>. Sus elementos principales: <b>ruedas, frenos, suspensión, dirección y luces</b>. Las ruedas son el <b>único elemento en contacto con el suelo</b> y necesitan más supervisión: "
        "son la <b>principal causa de accidente por fallo mecánico</b>. La rueda la forman la <b>llanta</b>, el <b>neumático</b> y, en su caso, la <b>cámara de aire</b>."))
    B.append(TABLE(
        [T("Part of the tyre", "Parte del neumático"), T("What it is", "Qué es")],
        [
            [T("<b>Tread</b>", "<b>Banda de rodadura</b>"), T("The part in contact with the ground; its <b>grooves</b> give grip and clear the water on the road.", "Zona de contacto con el suelo; sus <b>canales y ranuras</b> dan agarre y evacuan el agua de la calzada.")],
            [T("<b>Shoulders</b>", "<b>Hombros</b>"), T("Join the tread and the sidewall.", "Unión entre banda de rodadura y flanco.")],
            [T("<b>Carcass</b>", "<b>Carcasa</b>"), T("Internal structure that bears the <b>weight and the pressure</b>.", "Estructura interna que aguanta el <b>peso y la presión</b> de inflado.")],
            [T("<b>Beads</b>", "<b>Talones</b>"), T("Join the tyre to the rim.", "Unión del neumático y la llanta.")],
            [T("<b>Sidewalls</b>", "<b>Flancos</b>"), T("The sides of the tyre.", "Los costados laterales.")],
        ],
        widths=["28%", "72%"],
    ))
    B.append(FIG(tyre_code, "Reading 225/70 R16 110S: width, profile, radial structure, rim size, load index and speed symbol; DOT 3221 is the manufacturing date.",
                 "Cómo leer 225/70 R16 110S: anchura, perfil, estructura radial, llanta, índice de carga y código de velocidad; DOT 3221 es la fecha de fabricación."))
    B.append(TABLE(
        [T("Marking", "Inscripción"), T("Meaning", "Significado")],
        [
            [T("<b>225</b>", "<b>225</b>"), T("Nominal <b>width</b> in millimetres.", "<b>Anchura</b> nominal en milímetros.")],
            [T("<b>70</b>", "<b>70</b>"), T("<b>Profile</b>: the sidewall height is 70 % of the width.", "<b>Perfil</b>: la altura del flanco es el 70 % de la anchura.")],
            [T("<b>R</b>", "<b>R</b>"), T("<b>Radial</b> structure.", "Estructura <b>radial</b>.")],
            [T("<b>16</b>", "<b>16</b>"), T("Rim diameter in <b>inches</b>.", "Diámetro interior (llanta) en <b>pulgadas</b>.")],
            [T("<b>110</b>", "<b>110</b>"), T("<b>Load index</b>: maximum load per tyre (110 = 1,060 kg).", "<b>Índice de carga</b> máxima por neumático (110 = 1.060 kg).")],
            [T("<b>S</b>", "<b>S</b>"), T("<b>Speed symbol</b>: maximum speed (S = 180 km/h).", "<b>Código de velocidad</b> máxima (S = 180 km/h).")],
            [T("<b>TUBELESS</b>", "<b>TUBELESS</b>"), T("Tyre <b>without an inner tube</b>.", "Neumático <b>sin cámara</b>.")],
            [T("<b>DOT 3221</b>", "<b>DOT 3221</b>"), T("Manufacturing date: <b>week 32 of 2021</b>.", "Fecha de fabricación: <b>semana 32 de 2021</b>.")],
            [T("<b>M+S</b> (M&amp;S, MS)", "<b>M+S</b> (M&amp;S, MS)"), T("Tyres with better grip in <b>mud (M) and snow (S)</b>.", "Neumáticos para mejorar el agarre en <b>barro («M») y nieve («S»)</b>.")],
        ],
        widths=["22%", "78%"],
    ))
    B.append(BOX("trap", "Changing load index or speed code", "Cambiar el índice de carga o el código de velocidad", [
        ("You may fit tyres whose load index and speed code are <b>equal to or higher than</b> the manufacturer’s. Fitting <b>lower</b> ones is <b>prohibited</b>.", "Se pueden montar neumáticos con índice de carga y código de velocidad <b>iguales o superiores</b> a los del fabricante. Montarlos <b>inferiores</b> está <b>prohibido</b>."),
    ]))
    B.append(TABLE(
        [T("Type of tyre", "Tipo de neumático"), T("Feature", "Característica")],
        [
            [T("<b>Tubeless</b>", "<b>Sin cámara</b> (tubeless)"), T("The air is held between the rim and the tyre; <b>safer in a puncture</b> — it loses air slowly.", "El aire está entre la llanta y la cubierta; <b>más seguro en un pinchazo</b>: pierde el aire lentamente.")],
            [T("<b>With inner tube</b>", "<b>Con cámara</b>"), T("The air is in a tube inside; <b>less safe</b>.", "El aire está en una cámara interior; <b>menos seguro</b>.")],
            [T("<b>Radial</b>", "<b>Radial</b>"), T("The carcass has rubberised cords and wires laid out <b>like radii</b>.", "La carcasa tiene cuerdas engomadas y alambres colocados <b>en forma de radios</b>.")],
        ],
        widths=["28%", "72%"],
    ))
    B.append(TABLE(
        [T("The EU tyre label", "La etiqueta europea de neumáticos")],
        rows([
            ("Gives buyers fuller information to <b>compare tyres before buying</b>.", "Ofrece al consumidor información más completa para <b>elegir el neumático al comprarlo</b>."),
            ("<b>Top</b>: a <b>QR code</b> (more information in the EU product database), brand or trade name, tyre type identifier, size with load and speed indexes, class, and the classes for <b>fuel efficiency</b> and <b>wet grip</b> (A to E).",
             "<b>Parte superior</b>: <b>código QR</b> (información en la base de datos de la UE), nombre comercial o marca, identificación del neumático, dimensión con índices de carga y velocidad, clase y las clases de <b>eficiencia en consumo</b> y <b>adherencia en mojado</b> (de A a E)."),
            ("<b>Bottom</b>: the external <b>rolling noise</b> (decibels and class) and two pictograms showing whether its grip meets the standards for <b>snow</b> (3PMSF) and <b>ice</b>.", "<b>Parte inferior</b>: el <b>ruido de rodadura</b> exterior (decibelios y clase) y dos pictogramas que indican si su adherencia cumple los valores para <b>nieve</b> (3PMSF) y <b>hielo</b>."),
        ]),
    ))
    B.append(TABLE(
        [T("Tyre pressure", "Presión de inflado")],
        rows([
            ("Check it regularly — <b>about every 15 days</b> — with <b>cold tyres</b> and a gauge in good condition. If you check with <b>hot</b> tyres, <b>don’t let air out</b>: the manufacturer allows for the rise.",
             "Comprobarla periódicamente, <b>cada 15 días aproximadamente</b>, con los <b>neumáticos fríos</b> y un manómetro en buen estado. Si se comprueba con los neumáticos <b>calientes</b>, <b>no hay que quitar el aumento</b>: el fabricante lo prevé."),
            ("Use the <b>pressure recommended by the manufacturer</b> (by load and type of road). The <b>spare wheel</b> goes at the <b>highest</b> recommended pressure. <b>Don’t change the pressure between winter and summer</b>.",
             "Llevar la <b>presión recomendada por el fabricante</b> (según carga y vía). La <b>rueda de repuesto</b>, a la <b>más alta</b> de las recomendadas. <b>No variar la presión en invierno o verano</b>."),
        ]),
    ))
    B.append(FIG(tyre_pressure, "Too much pressure: only the centre touches and wears. Too little: the edges carry the load, wear and overheat.",
                 "Con exceso de presión solo apoya y se desgasta el centro; con poca presión apoyan los bordes, que se desgastan y se calientan."))
    B.append(TABLE(
        [T("Wrong pressure", "Presión incorrecta"), T("Consequences", "Consecuencias")],
        [
            [T("<b>Too low</b>", "<b>Inferior</b> a la necesaria"), T("Sidewalls deform and <b>overheat</b>; wear on the <b>edges</b> (risk of a <b>blow-out</b>); <b>less grip</b> (aquaplaning); <b>more fuel</b> (more rolling resistance).", "Los flancos se deforman y se <b>calientan</b>; desgaste por los <b>bordes</b> (peligro de <b>reventón</b>); <b>menos adherencia</b> (aquaplaning); <b>más consumo</b> (más resistencia a la rodadura).")],
            [T("<b>Too high</b>", "<b>Superior</b> a la necesaria"), T("Smaller contact area (<b>less grip</b>); wear in the <b>centre</b> of the tread; bumps are not absorbed and the <b>suspension suffers</b>.", "Menor zona de contacto (<b>menos adherencia</b>); desgaste por el <b>centro</b>; no absorbe bien las irregularidades y se <b>deteriora la suspensión</b>.")],
            [T("<b>Unequal on the same axle</b> (<b>the most dangerous</b>)", "<b>Descompensada en el mismo eje</b> (<b>lo más peligroso</b>)"), T("The car <b>pulls to one side</b> on a straight road; less stability; uneven braking.", "Se <b>desvía hacia un lado</b> en recta; menos estabilidad; frenada más irregular.")],
        ],
        widths=["30%", "70%"],
    ))
    B.append(TABLE(
        [T("Changing tyres", "Cambio de neumáticos")],
        rows([
            ("Change them when the tread depth reaches <b>1.6 mm</b> (<b>2 mm recommended</b>), when they have <b>cuts, cracks or bulges</b>, or when they have <b>expired</b> (recommended after <b>5 years</b> from manufacture).",
             "Hay que cambiarlos cuando el dibujo llega a <b>1,6 mm</b> (<b>recomendable a los 2 mm</b>), si tienen <b>cortes, grietas o bultos</b>, o si están <b>caducados</b> (recomendable a los <b>5 años</b> de su fabricación)."),
            ("New tyres should be the <b>same on all wheels</b>, or at least the <b>same on each axle</b>.", "Los neumáticos nuevos deben ser <b>iguales en todas las ruedas</b> o, al menos, <b>iguales en cada eje</b>."),
            ("<b>Wider</b> tyres use more fuel and <b>reduce safety</b> (they harm the brakes, suspension and steering).", "Los neumáticos <b>más anchos</b> consumen más y <b>disminuyen la seguridad</b> (perjudican frenos, suspensión y dirección)."),
        ]),
    ))
    B.append(TABLE(
        [T("Changing a wheel, step by step", "Cambiar una rueda, paso a paso")],
        rows([
            ("<b>1.</b> Find a <b>suitable place</b> and immobilise the vehicle properly.", "<b>1.</b> Buscar un <b>lugar adecuado</b> e inmovilizar bien el vehículo."),
            ("<b>2.</b> Signal it: <b>hazard lights + the V-16 warning light</b>. <b>Put the vest on before getting out</b>.", "<b>2.</b> Señalizarlo: <b>luz de emergencia + dispositivo luminoso V-16</b>. <b>Ponerse el chaleco antes de salir</b>."),
            ("<b>3.</b> Chock the vehicle and place the jack — <b>never get under a car held up by the jack</b>.", "<b>3.</b> Calzar el vehículo y colocar el gato: <b>nunca situarse debajo con el vehículo levantado</b>."),
            ("<b>4.</b> <b>Loosen the nuts before lifting</b> the car with the jack.", "<b>4.</b> <b>Aflojar las tuercas antes de levantar</b> el vehículo con el gato."),
            ("<b>5.</b> Change the wheel and <b>tighten the nuts with the car on the ground</b>.", "<b>5.</b> Cambiar la rueda y <b>apretar las tuercas con el vehículo en el suelo</b>."),
            ("<b>6.</b> Check the nuts after <b>20–30 km</b> (again after 150–250 km is recommended). With a <b>temporary spare</b>, keep to its limits (for example <b>80 km/h</b> and <b>200 km</b>).",
             "<b>6.</b> Comprobar el apriete a los <b>20–30 km</b> (recomendable repetir a los 150–250 km). Con una <b>rueda de uso temporal</b>, respetar sus límites (por ejemplo <b>80 km/h</b> y <b>200 km</b>)."),
        ]),
    ))
    B.append(BOX("trap", "A blow-out", "Reventón", [
        ("Stay <b>calm</b>, <b>hold the wheel firmly</b> and correct any swerve (keep your line).", "Mantener la <b>calma</b>, <b>sujetar el volante con fuerza</b> y corregir las desviaciones (mantener la trayectoria)."),
        ("<b>Don’t take your foot off the accelerator suddenly</b>, and <b>brake as little as possible</b>, very gently.", "<b>No soltar bruscamente el acelerador</b> y <b>frenar lo mínimo posible</b>, con mucha suavidad."),
    ]))
    B.append(TABLE(
        [T("Other tyre care", "Otros mantenimientos"), T("Causes of faster wear", "Causas de mayor desgaste")],
        [[T("Inspect the tyres and <b>remove stones</b> stuck in the grooves; put the tyres in <b>best condition on the rear axle</b>; <b>balance</b> the wheels at a workshop if the steering wheel <b>vibrates</b> at certain speeds (after hitting kerbs…).",
            "Inspeccionar el neumático y <b>retirar la gravilla</b> de las ranuras; colocar los neumáticos en <b>mejor estado en el eje trasero</b>; <b>equilibrar</b> las ruedas en el taller si el volante <b>vibra</b> a ciertas velocidades (golpes contra el bordillo…)."),
          T("Wrong pressure; aggressive driving; high speed and too much load; heat (more in summer); unbalanced wheels; worn brakes or shock absorbers; the road surface and <b>chains</b> (take them off when not needed).",
            "Presión incorrecta; conducción agresiva; velocidad elevada y carga excesiva; temperatura (más en verano); ruedas desequilibradas; mal estado de frenos o amortiguadores; tipo de firme y <b>cadenas</b> (quitarlas cuando no hagan falta).")]],
        widths=["54%", "46%"],
    ))

    B.append(H3("4.2.3 Active safety: brakes", "4.2.3 Seguridad activa: frenos"))
    B.append(P(
        "Brakes <b>slow the vehicle down, stop it or keep it still</b>. How well it brakes depends on the <b>pressure on the pedal</b>, the vehicle’s <b>condition</b> (brakes, tyres, suspension), the <b>load</b>, the <b>speed</b> and the <b>road</b>.",
        "Los frenos sirven para <b>reducir la velocidad, detener o inmovilizar</b> el vehículo. La eficacia depende de la <b>presión sobre el pedal</b>, el <b>estado del vehículo</b> (frenos, neumáticos, suspensión), la <b>carga</b>, la <b>velocidad</b> y la <b>vía</b>."))
    B.append(BOX("key", "Servo brake", "Servofreno", [
        ("It multiplies the force the driver applies, so braking takes less effort — but it <b>only works with the engine running</b>. With the engine off you must press much harder.",
         "Multiplica la fuerza del conductor y le exige menos esfuerzo, pero <b>solo funciona con el motor en marcha</b>. Con el motor parado hay que pisar con mucha más fuerza."),
    ]))
    B.append(TABLE(
        [T("Braking system", "Sistema de frenado"), T("What it does", "Qué hace")],
        [
            [T("<b>Service brake</b> (foot brake)", "<b>Freno de servicio</b> (de pie)"), T("Slows and stops the vehicle; acts on <b>all the wheels</b>.", "Reduce la velocidad y detiene el vehículo; actúa sobre <b>todas las ruedas</b>.")],
            [T("<b>Emergency brake</b> (<i>freno de socorro</i>)", "<b>Freno de socorro</b>"), T("The last part of the foot brake’s travel; stops the vehicle <b>if the service brake fails</b>. Acts on at least <b>one wheel on each side</b>.", "Es el último recorrido del freno de pie; frena <b>si falla el de servicio</b>. Actúa, al menos, sobre <b>una rueda de cada lado</b>.")],
            [T("<b>Parking brake</b> (handbrake)", "<b>Freno de estacionamiento</b> (de mano)"), T("Keeps the vehicle still, even with nobody in it. Usually acts on the <b>rear wheels</b> (by hand or electric).", "Garantiza la inmovilización, incluso sin conductor. Actúa generalmente sobre las <b>ruedas traseras</b> (de mano o eléctrico).")],
            [T("<b>Engine brake</b>", "<b>Freno motor</b>"), T("Using the engine to slow down: <b>lift off the accelerator</b> or <b>shift down</b> (especially on long downhill stretches).", "Usar el motor como freno: <b>levantar el pie del acelerador</b> o <b>reducir a marchas cortas</b> (sobre todo en pendientes largas).")],
        ],
        widths=["32%", "68%"],
    ))
    B.append(BOX("key", "Why use the engine brake", "Ventajas del freno motor", [
        ("You <b>don’t surprise</b> drivers behind with sudden stops (fewer rear-end crashes); <b>less brake wear</b> and no <b>fading</b>; <b>less fuel and pollution</b> (fuel use drops to zero).",
         "<b>No sorprende</b> a los de detrás con detenciones bruscas (menos alcances); <b>menos desgaste de frenos</b> y evita el <b>fading</b>; <b>menos consumo y contaminación</b> (el consumo es nulo)."),
    ]))
    B.append(TABLE(
        [T("Braking normally", "Cómo frenar en condiciones normales")],
        rows([
            ("Brake <b>as early as possible</b> (use the engine brake; avoid sudden braking after checking it is safe); brake <b>smoothly and progressively</b>; <b>don’t overuse</b> the brakes.",
             "Frenar con la <b>máxima antelación</b> (freno motor; evitar frenazos bruscos, comprobando antes que no hay riesgo); frenar <b>suave y progresivamente</b>; <b>no abusar</b> de los frenos."),
            ("Adapt braking to the <b>surface and its grip</b> (especially with low grip and without ABS).", "Adaptar el freno al <b>pavimento y su adherencia</b> (sobre todo con poca adherencia y sin ABS)."),
            ("On <b>long descents</b>, use the <b>engine brake</b> and <b>low gears</b> (don’t ride the clutch). Overusing the brakes causes <b>fading</b> — they lose effect as they overheat. An overloaded vehicle brakes worse.",
             "En <b>descensos prolongados</b>, <b>freno motor</b> y <b>marchas cortas</b> (sin llevar el embrague pisado). Abusar de los frenos provoca <b>fading</b>: pierden eficacia por el calentamiento. Sin sobrecarga se frena mejor."),
        ]),
    ))
    B.append(BOX("trap", "Emergency braking", "Frenada de emergencia", [
        ("<b>1. Press the brake as hard as you can.</b> <b>Without ABS</b>: if the wheels lock, ease off and press hard again. <b>With ABS</b>: <b>keep pressing hard</b> even if the pedal vibrates.",
         "<b>1. Pisar a fondo el freno.</b> <b>Sin ABS</b>: si se bloquean las ruedas, reducir la presión y volver a pisar a fondo. <b>Con ABS</b>: <b>seguir pisando a fondo</b> aunque vibre el pedal."),
        ("<b>2.</b> Press the <b>clutch just before the vehicle stops</b>.", "<b>2.</b> Pisar el <b>embrague justo antes de que el vehículo se detenga</b>."),
    ]))
    B.append(TABLE(
        [T("System", "Sistema"), T("What it does", "Funciones")],
        [
            [T("<b>ABS</b> (anti-lock braking)", "<b>ABS</b> (antibloqueo)"), T("<b>Prevents the wheels from locking</b>, adapts braking to the grip and <b>lets you keep steering</b>.", "<b>Impide el bloqueo de las ruedas</b>, adapta la frenada a la adherencia y <b>permite controlar la dirección</b>.")],
            [T("<b>BAS</b> (brake assist)", "<b>BAS</b> (asistencia a la frenada)"), T("Detects <b>emergency braking</b> and raises the braking pressure on all wheels, <b>without locking them</b>.", "Detecta si es una <b>frenada de emergencia</b> y aumenta la presión en todas las ruedas, <b>sin bloquearlas</b>.")],
        ],
        widths=["30%", "70%"],
    ))
    B.append(TABLE(
        [T("If the brakes fail", "Si fallan los frenos")],
        rows([
            ("<b>1.</b> <b>Pump</b> the pedal (press and release). If you think they have overheated, release the pedal and let them cool.", "<b>1.</b> <b>Pisar y soltar</b> el pedal (bombeando). Si se cree que es por sobrecalentamiento, soltar el pedal y dejar que se ventilen."),
            ("<b>2.</b> Move to the right or onto the shoulder and <b>shift down</b> (engine brake).", "<b>2.</b> Arrimarse a la derecha o salir al arcén y <b>reducir a marchas cortas</b> (freno motor)."),
            ("<b>3.</b> Use the <b>handbrake gently</b> and progressively.", "<b>3.</b> Usar el <b>freno de mano con suavidad</b> y progresivamente."),
            ("<b>4.</b> Look for an <b>emergency escape lane</b> (<i>lecho de frenado</i>), an <b>uphill slope</b>, or <b>scrape along the side</b> to slow down by friction.", "<b>4.</b> Buscar un <b>lecho de frenado de emergencia</b>, una <b>pendiente ascendente</b> o <b>rozar lateralmente</b> para frenar por rozamiento."),
        ]),
    ))
    B.append(TABLE(
        [T("Symptom", "Síntoma"), T("Likely cause", "Causa probable"), T("What to do", "Qué hacer")],
        [
            [T("You must press <b>harder than usual</b> (a metallic noise if very worn)", "Hay que <b>pisar más fuerte de lo normal</b> (ruido metálico si están muy gastadas)"), T("<b>Worn pads or shoes</b>", "<b>Desgaste de pastillas</b> o zapatas"), T("Workshop: replace them", "Taller: sustituirlas")],
            [T("<b>Soft, spongy</b> pedal", "Pedal <b>blando y esponjoso</b>"), T("<b>Air in the hydraulic circuit</b>", "<b>Aire en el circuito hidráulico</b>"), T("Workshop: bleed the system", "Taller: purgar el sistema")],
            [T("Pedal goes <b>almost to the floor</b>", "<b>Recorrido excesivo</b>, casi hasta el fondo"), T("<b>Loss of brake fluid</b>", "<b>Pérdida de líquido de frenos</b>"), T("Workshop: fix the leak and refill between min and max", "Taller: reparar la fuga y rellenar entre mínimo y máximo")],
            [T("Car <b>pulls to one side</b> when braking", "Se <b>desvía hacia un lado</b> al frenar"), T("<b>Different pressures</b> on the same axle, uneven brake wear, bad adjustment or blocked brake hoses", "<b>Presión de inflado diferente</b> en el mismo eje, desgaste desigual, mal reglaje o latiguillos obstruidos"), T("Check the tyre pressure; if that doesn’t fix it, workshop", "Comprobar la presión; si no se soluciona, taller")],
            [T("Less effect after a <b>puddle or a car wash</b>", "Menos eficacia tras un <b>charco o lavar el coche</b>"), T("<b>Too much moisture</b>", "<b>Humedad excesiva</b>"), T("Press the brakes <b>several times</b> to dry them by friction", "Pisar <b>varias veces</b> para secarlos por rozamiento")],
        ],
        widths=["34%", "36%", "30%"],
        cls="small",
    ))
    B.append(P(
        "To maintain the brakes, check the <b>brake fluid level</b> (between the min and max marks), replace the fluid, keep the hoses clean (no cracks or leaks) and change pads and discs as the manufacturer says. "
        "<b>Bad brakes are the first reason vehicles fail the ITV.</b>",
        "Para mantener los frenos hay que comprobar el <b>nivel del líquido de frenos</b> (entre las marcas de máximo y mínimo), sustituirlo, mantener limpios los latiguillos (sin grietas ni fugas) y cambiar pastillas y discos según el fabricante. "
        "<b>El mal estado de los frenos es la primera causa por la que los vehículos no superan la ITV.</b>"))
    B.append(TABLE(
        [T("Brake type", "Tipo de freno"), T("How it works", "Cómo funciona")],
        [
            [T("<b>Disc brake</b>", "<b>Freno de disco</b>"), T("The disc turns with the wheel; the <b>pads</b> squeeze it. <b>The most used</b>: shorter braking distance, less risk of locking, better cooled (<b>less fading</b>).", "El disco gira con la rueda y las <b>pastillas</b> lo comprimen. Es <b>el más utilizado</b>: reduce la distancia de frenado, menos riesgo de bloqueo y mejor refrigerado (<b>menos fading</b>).")],
            [T("<b>Drum brake</b>", "<b>Freno de tambor</b>"), T("The drum turns with the wheel; the <b>shoes</b> expand against it.", "El tambor gira con la rueda y las <b>zapatas</b> se expanden contra él.")],
        ],
        widths=["24%", "76%"],
    ))

    B.append(H3("4.2.3 Active safety: suspension, steering, lights and other systems", "4.2.3 Seguridad activa: suspensión, dirección, luces y otros sistemas"))
    B.append(P(
        "The <b>suspension</b> joins the wheels to the rest of the vehicle, <b>absorbs bumps</b> and <b>controls body roll</b> so it doesn’t affect stability. <b>Smart suspension</b> lets you choose: <b>hard</b> for bends or fast driving (you feel the bumps more), "
        "<b>soft</b> for good roads and motorways (more comfortable). The <b>steering</b> lets the driver <b>direct the vehicle</b>: <b>power steering</b> reduces the effort; <b>speed-sensitive</b> power steering stiffens with speed for better control.",
        "La <b>suspensión</b> une las ruedas al resto del vehículo, <b>absorbe las irregularidades</b> y <b>compensa el balanceo</b> para que no afecte a la estabilidad. La <b>suspensión inteligente</b> permite elegir: <b>dura</b> para curvas o conducción rápida (se notan más los baches) "
        "y <b>blanda</b> para buen pavimento, autopista y autovía (más cómoda). La <b>dirección</b> permite <b>orientar la trayectoria</b>: la <b>asistida</b> reduce la fuerza necesaria; la <b>asistida progresiva</b> se endurece con la velocidad para un mejor control."))
    B.append(TABLE(
        [T("Symptom", "Síntoma"), T("Likely cause", "Causa probable"), T("Solution", "Solución")],
        [
            [T("Bounces too much over bumps", "Rebota demasiado en los baches"), T("Worn <b>shock absorbers</b> or tyres <b>over-inflated</b>", "<b>Amortiguadores</b> en mal estado o <b>exceso de presión</b>"), T("Check pressures or replace the shock absorbers", "Comprobar la presión o sustituir amortiguadores")],
            [T("Leans too much (braking, bends)", "Se inclina demasiado (al frenar, en curvas)"), T("Worn <b>shock absorbers</b> or tyres <b>under-inflated</b>", "<b>Amortiguadores</b> en mal estado o <b>poca presión</b>"), T("Check pressures or replace the shock absorbers", "Comprobar la presión o sustituir amortiguadores")],
            [T("Bounces when braking and needs <b>more distance to stop</b>", "Al frenar rebota y <b>aumenta la distancia de frenado</b>"), T("Worn <b>shock absorbers</b>", "<b>Amortiguadores</b> en mal estado"), T("Replace them", "Sustituirlos")],
            [T("<b>Heavy</b> steering", "Dirección <b>dura</b>"), T("Tyres <b>under-inflated</b> or <b>wrong alignment</b>", "<b>Poca presión</b> o <b>alineación incorrecta</b>"), T("Check pressures or workshop", "Comprobar la presión o taller")],
            [T("Steering has <b>play</b> (the wheel doesn’t respond at once)", "Dirección con <b>holgura</b> (el volante no responde al momento)"), T("A <b>worn part</b>", "Algún <b>elemento desgastado</b>"), T("Workshop", "Taller")],
            [T("Pulls to one side <b>when you let go of the wheel</b>", "Se desvía <b>al soltar el volante</b>"), T("Different pressures on the same axle or wrong alignment", "Presión diferente en el mismo eje o alineado incorrecto"), T("Check pressures or workshop", "Comprobar la presión o taller")],
        ],
        widths=["36%", "36%", "28%"],
        cls="small",
    ))
    B.append(P(
        "For the steering, check the <b>power-steering fluid level</b> (between min and max), keep it <b>aligned</b> and avoid hitting kerbs and potholes.",
        "Para la dirección: comprobar el <b>nivel del líquido de la dirección asistida</b> (entre mínimo y máximo), mantenerla <b>alineada</b> y evitar golpes con bordillos y baches."))
    B.append(TABLE(
        [T("Lights: to see, be seen and signal", "Luces: para ver, ser vistos y señalizar"), T("What to know", "Qué saber")],
        [
            [T("<b>Xenon and bi-xenon</b>", "<b>Xenón y bixenón</b>"), T("Close to daylight; a <b>wider lit area</b> and less eye strain.", "Similar a la luz natural; <b>zona iluminada más amplia</b> y menos fatiga ocular.")],
            [T("<b>LED</b>", "<b>LED</b>"), T("Lights up to <b>three times further</b> than xenon, with a whiter light.", "Ilumina hasta <b>tres veces más</b> distancia que el xenón, y es una luz más clara.")],
            [T("<b>Daytime running lights</b>", "<b>Luces de día</b> (diurnas)"), T("Make the vehicle <b>more visible</b> in all circumstances.", "Aumentan la <b>visibilidad del vehículo</b> en todas las circunstancias.")],
            [T("<b>Adaptive lights</b>", "<b>Luces adaptativas</b>"), T("Turn with the steering, lighting <b>bends and intersections</b>.", "Se orientan con la dirección: mejor visibilidad en <b>curvas e intersecciones</b>.")],
            [T("<b>Maintenance</b>", "<b>Mantenimiento</b>"),
             T("Check that they <b>work and are clean</b> (dirt or damage can deflect the beam and dazzle); check the <b>fuses</b> if a light fails. Check the <b>aim</b>, especially <b>after loading or unloading</b>: "
               "aimed <b>too low</b>, you see obstacles later; <b>too high</b>, it lights the road worse and <b>dazzles</b> others.",
               "Comprobar su <b>funcionamiento y estado</b> (suciedad o daños pueden desviar el haz y deslumbrar); revisar los <b>fusibles</b> si una luz no funciona. Comprobar el <b>reglaje</b>, sobre todo <b>después de cargar o descargar</b>: "
               "<b>bajo</b>, se ven más tarde los obstáculos; <b>alto</b>, ilumina peor la calzada y <b>deslumbra</b>.")],
        ],
        widths=["26%", "74%"],
    ))
    B.append(TABLE(
        [T("Other active-safety systems", "Otros sistemas de seguridad activa"), T("What it does", "Qué hace")],
        [
            [T("<b>ESP</b> (electronic stability control)", "<b>ESP</b> (control electrónico de estabilidad)"), T("<b>Corrects a skid before it happens</b>, braking individual wheels and adjusting the engine’s power.", "<b>Corrige el derrape antes de que se produzca</b>, actuando sobre los frenos de cada rueda y sobre la tracción.")],
            [T("<b>Traction control</b>", "<b>Control de tracción</b>"), T("Detects a <b>driving wheel spinning</b> faster than it should (slippery ground, bends) and cuts engine power and/or brakes.", "Detecta si una <b>rueda motriz gira más rápido</b> de lo debido (suelo deslizante, curva) y actúa sobre la potencia y/o los frenos.")],
            [T("<b>Speed limiter / cruise control</b>", "<b>Limitador de velocidad</b>"), T("Helps keep the chosen speed: some <b>stop you exceeding</b> a set speed; others <b>hold it</b> without touching the pedals; some also keep the distance to the vehicle ahead.",
                                                                                                    "Ayuda a <b>mantener la velocidad</b>: algunos <b>impiden superar</b> una velocidad fijada; otros la <b>mantienen</b> sin pisar los pedales; otros guardan además la distancia con el de delante.")],
        ],
        widths=["32%", "68%"],
    ))

    # ---------------------------------------------------------------- 4.2.4 passive safety
    B.append(H3("4.2.4 Passive safety", "4.2.4 Seguridad pasiva"))
    B.append(P(
        "<b>Passive safety</b> reduces the <b>consequences</b> of an accident: it prevents or reduces injuries. Main elements: <b>chassis and body</b>, <b>glass</b>, <b>seat belts</b>, <b>child restraints</b>, <b>airbags</b>, <b>head restraints</b> and <b>motorcyclists’ equipment</b>.",
        "La <b>seguridad pasiva</b> reduce las <b>consecuencias</b> de un accidente: evita o reduce las lesiones. Elementos principales: <b>chasis y carrocería</b>, <b>cristales</b>, <b>cinturón</b>, <b>sistemas de retención infantil</b>, <b>airbags</b>, <b>reposacabezas</b> y el <b>equipamiento del motorista</b>."))
    B.append(TABLE(
        [T("Body and chassis", "Carrocería y chasis")],
        rows([
            ("They carry every part of the car and <b>protect the occupants</b> by <b>absorbing as much of the crash energy as possible</b>.", "Soportan todos los elementos del vehículo y <b>protegen a los ocupantes</b> <b>absorbiendo la máxima energía</b> del choque."),
            ("The <b>central cell</b> (chassis and passenger compartment) stays <b>rigid</b>; the rest (body) <b>deforms progressively</b> and absorbs the impact — a <b>programmed deformation</b> (crumple zones).",
             "La <b>estructura central</b> (chasis y habitáculo) se mantiene <b>rígida</b>; el resto (carrocería) <b>se deforma progresivamente</b> y absorbe la energía: <b>deformación programada</b>."),
            ("<b>Don’t modify the bodywork</b>: a pedestrian who is hit could be hurt more. A strong body does <b>not replace</b> seat belts, head restraints or airbags — they complement each other.",
             "<b>No se debe modificar la carrocería</b>: en un atropello el peatón puede sufrir más. Una carrocería resistente <b>no sustituye</b> al cinturón, el reposacabezas o el airbag: son complementarios."),
        ]),
    ))
    B.append(TABLE(
        [T("Glass", "Cristal"), T("When it breaks", "Al romperse"), T("Usually used in", "Se usa en")],
        [
            [T("<b>Laminated</b>", "<b>Laminado</b>"), T("Cracks into <b>long pieces that stay joined</b>: you can still see, and it doesn’t injure the occupants.", "Se resquebraja en <b>fragmentos largos que siguen unidos</b>: mantiene la visibilidad y evita lesiones."), T("The <b>windscreen</b>", "El <b>parabrisas</b>")],
            [T("<b>Tempered</b>", "<b>Templado</b>"), T("Breaks into <b>small pieces</b> that block the view and can <b>come loose and hurt</b> the occupants.", "Se fragmenta en <b>pequeños trozos</b> que impiden la visibilidad y pueden <b>desprenderse y dañar</b> a los ocupantes."), T("<b>Rear and side windows</b>", "<b>Luneta trasera y laterales</b>")],
        ],
        widths=["18%", "56%", "26%"],
    ))
    B.append(P("To avoid a windscreen broken by flying gravel, <b>keep more distance</b> from the vehicle ahead.", "Para evitar la rotura del parabrisas por proyección de gravilla, hay que <b>aumentar la separación</b> con el vehículo de delante."))
    B.append(P(
        "The <b>seat belt</b> holds the body in a crash or rollover, so occupants don’t hit the inside or get <b>thrown out</b>. It <b>almost halves the risk of dying</b>, especially together with the <b>airbag</b> — they <b>complement</b> each other, neither replaces the other. "
        "Some belts have a <b>load limiter</b> that eases the pressure on chest and pelvis when the force is very high.",
        "El <b>cinturón</b> retiene y protege el cuerpo en un choque o vuelco, evitando que los ocupantes se golpeen o <b>salgan despedidos</b>. <b>Reduce casi a la mitad la probabilidad de morir</b>, sobre todo junto con el <b>airbag</b>: se <b>complementan</b>, no se sustituyen. "
        "Algunos tienen un sistema que <b>limita la presión</b> sobre pecho y pelvis cuando la fuerza es excesiva."))
    B.append(BOX("trap", "After a serious crash", "Después de un fuerte accidente", [
        ("It is recommended to <b>replace the seat belt</b>: the webbing and the <b>pyrotechnic pretensioners</b> (they fire when the impact is detected) may have lost their effect, and the anchorages may be damaged.",
         "Es recomendable <b>cambiar el cinturón</b>: el trenzado y los <b>pretensores pirotécnicos</b> (se disparan al detectar el impacto) pueden haber perdido eficacia y los anclajes pueden estar dañados."),
    ]))
    B.append(FIG(seatbelt, "The diagonal strap crosses the collarbone and the middle of the chest; the lap strap sits low on the hip bones. Over the belly, the body can slide under it.",
                 "La banda torácica cruza la clavícula y el centro del pecho; la abdominal va baja, sobre los huesos de la cadera. Sobre el abdomen, el cuerpo puede deslizarse por debajo."))
    B.append(TABLE(
        [T("Wearing the belt correctly", "Colocación correcta")],
        rows([
            ("In perfect condition, properly anchored, <b>fastened and snug</b> (neither loose nor too tight).", "En perfectas condiciones, bien anclado, <b>abrochado y ajustado</b> (ni muy flojo ni muy fuerte)."),
            ("<b>Diagonal strap</b>: <b>over the collarbone</b> (between shoulder and neck), across the middle of the chest. <b>Lap strap</b>: over the <b>hip bones</b> (pelvis) and <b>below the belly</b> — badly placed, it can cause serious injuries.",
             "<b>Cinta torácica</b>: <b>sobre la clavícula</b> (entre hombro y cuello), por el centro del pecho. <b>Cinta abdominal</b>: por los <b>huesos de la cadera</b> (pelvis) y <b>por debajo del abdomen</b>; mal colocada puede provocar graves lesiones."),
            ("Sit <b>upright</b> (backrest not too reclined); avoid <b>bulky clothes</b> (coats, thick jumpers); <b>belt clips are prohibited</b> (they slacken it); don’t sit on <b>cushions or towels</b> — "
             "the <b>submarining effect</b>: in a crash the body slides under the lap strap.",
             "<b>Postura correcta</b> (respaldo no muy inclinado); evitar <b>prendas gruesas</b> (abrigos, jerséis voluminosos); <b>prohibido usar pinzas</b> (reducen la tensión); no sentarse sobre <b>cojines o toallas</b>: "
             "<b>efecto submarino</b>, el cuerpo se desliza por debajo de la banda abdominal."),
        ]),
    ))
    B.append(P(
        "<b>Children</b> (under 18) <b>135 cm tall or less</b> must use an <b>approved child restraint</b> suited to their size and weight (a child seat), following the maker’s instructions. <b>Never carry them in your arms.</b>",
        "Los <b>menores de edad</b> de estatura <b>igual o inferior a 135 cm</b> deben usar <b>sistemas de retención infantil homologados</b> adaptados a su talla y peso (sillitas), según las instrucciones del fabricante. <b>Nunca en brazos.</b>"))
    B.append(TABLE(
        [T("Child restraints: recommendations", "Sistemas de retención infantil: recomendaciones")],
        rows([
            ("The <b>safest position</b> is generally <b>facing backwards</b> — keep the child rear-facing <b>as long as possible</b>. The <b>rear centre seat</b> is the safest (least affected by side impacts).",
             "La <b>colocación más segura</b> es, en general, <b>en sentido contrario a la marcha</b>, el mayor tiempo posible. El <b>asiento trasero central</b> es el más seguro (menos afectado por impactos laterales)."),
            ("<b>ISOFIX</b>: simpler, correct and firm fitting. Lets the child travel <b>rear-facing at least until 15 months or 83 cm</b> (some up to 105 cm); some rotate <b>360°</b> to make it easier to seat the child.",
             "<b>ISOFIX</b>: montaje más sencillo, correcto y firme. Permite viajar <b>de espaldas a la marcha al menos hasta los 15 meses o 83 cm</b> (algunos hasta 105 cm); algunos giran <b>360°</b> para colocar al niño."),
            ("<b>i-Size</b>: the newest seats, chosen by the child’s <b>height</b>; they add a <b>top tether</b> or a <b>support leg</b>, and work <b>together with ISOFIX</b>.", "<b>i-Size</b>: lo más moderno, por <b>estatura</b> del niño; incluye <b>fijación superior</b> (top tether) o <b>pata de apoyo</b>, y <b>se complementa con ISOFIX</b>."),
        ]),
    ))
    B.append(BOX("trap", "Never…", "Nunca…", [
        ("…fit a <b>rear-facing child seat</b> on a <b>front seat with an airbag</b> unless the airbag has been <b>switched off</b>.", "…utilizar sillitas <b>orientadas hacia atrás</b> en asientos delanteros <b>con airbag</b>, salvo que se haya <b>desactivado</b>."),
    ]))
    B.append(P(
        "An <b>airbag</b> is a bag that inflates <b>automatically</b> in a <b>violent deceleration</b>, so occupants don’t hit the wheel, windscreen or windows. There are <b>front, side, knee and curtain</b> airbags, and even <b>pedestrian</b> airbags "
        "(sensors in the front bumper fire a bag under the bonnet, by the windscreen); some <b>motorcycles</b> have them too.",
        "El <b>airbag</b> es una bolsa que se infla <b>automáticamente</b> ante una <b>deceleración violenta</b>, para evitar el impacto de los ocupantes contra el volante, el parabrisas o las ventanillas. Los hay <b>frontales, laterales, de rodilla, de cortinilla</b> e incluso <b>para peatones</b> "
        "(sensores en el paragolpes despliegan una bolsa bajo el capó, junto al parabrisas); algunas <b>motocicletas</b> también los llevan."))
    B.append(TABLE(
        [T("Airbag recommendations", "Recomendaciones con el airbag")],
        rows([
            ("Sit about <b>25 cm from the airbag</b> — <b>never less than 10 cm</b>: it inflates at about <b>300 km/h</b>.", "Colocar el asiento a <b>25 cm del airbag</b>, <b>nunca a menos de 10 cm</b>: se infla a unos <b>300 km/h</b>."),
            ("<b>Always with the seat belt</b> (they complement each other). Proper posture — <b>no feet on the dashboard</b>.", "<b>Siempre con el cinturón</b> (son complementarios). Posición adecuada: <b>no poner las piernas en el salpicadero</b>."),
            ("<b>Switch off the passenger airbag</b> for a rear-facing child seat. <b>No objects</b> (sat-nav or others) near an airbag.", "<b>Desconectar el airbag del acompañante</b> si se coloca una sillita hacia atrás. <b>No colocar objetos</b> (navegador u otros) cerca del airbag."),
        ]),
    ))
    B.append(P(
        "The <b>head restraint</b> prevents or reduces <b>neck injuries</b> (<b>whiplash</b>, <i>latigazo cervical</i>) from the sudden movement of the head <b>backwards (hyperextension) and then forwards (hyperflexion)</b>, above all in <b>rear-end crashes</b>. "
        "Use one in every seat (<b>compulsory in the front seats</b>) and adjust it.",
        "El <b>reposacabezas</b> evita o reduce las <b>lesiones cervicales</b> (<b>latigazo cervical</b>) por el movimiento brusco del cuello <b>hacia atrás (hiperextensión) y luego hacia delante (hiperflexión)</b>, sobre todo en <b>impactos por alcance</b>. "
        "Hay que usarlo en todos los asientos (<b>obligatorio en los delanteros</b>) y regularlo."))
    B.append(FIG(headrest, "Top of the head restraint level with the top of the head, its middle at eye level, and no more than 4 cm behind the head.",
                 "Parte superior a la altura de la parte superior de la cabeza, parte central a la altura de los ojos y no más de 4 cm por detrás de la cabeza."))
    B.append(P(
        "There are <b>passive</b> and <b>active</b> head restraints; active ones move to the head automatically in a crash and are <b>more effective</b>. Note: your course writes the two neck movements the other way round — bending back is <b>hyperextension</b>, bending forward is <b>hyperflexion</b>.",
        "Hay reposacabezas <b>pasivos</b> y <b>activos</b>; los activos se acoplan a la cabeza automáticamente y son <b>más eficaces</b>. Ojo: tu curso cambia el orden de los movimientos; hacia atrás es <b>hiperextensión</b> y hacia delante, <b>hiperflexión</b>."))
    B.append(TABLE(
        [T("Helmet", "Casco"), T("Protection", "Protección")],
        [
            [T("<b>Full-face</b> (<i>integral</i>)", "<b>Integral</b>"), T("Covers the <b>whole head and face</b> — the <b>recommended</b> one.", "Cubre <b>toda la cabeza y la cara</b>: el <b>recomendable</b>.")],
            [T("<b>Modular</b>", "<b>Modular</b>"), T("The lower front (chin bar) <b>lifts up</b>.", "Permite <b>levantar la parte inferior</b>.")],
            [T("<b>Open-face</b> (<i>jet</i>)", "<b>Jet</b>"), T("Does <b>not cover the chin</b>.", "<b>No cubre la barbilla</b>.")],
        ],
        widths=["28%", "72%"],
    ))
    B.append(P(
        "The helmet <b>absorbs much of the impact energy</b>, greatly reducing fatal injuries, and protects head and face from <b>abrasion</b> on the road. <b>Not wearing one is the main cause of death</b> in motorcycle and moped accidents. It is <b>compulsory for rider and passenger</b>.",
        "El casco <b>absorbe gran parte de la energía</b> del impacto, reduce mucho las lesiones mortales y protege cabeza y cara de la <b>abrasión</b>. <b>No usarlo es la principal causa de mortalidad</b> en los accidentes de moto y ciclomotor. Es <b>obligatorio para conductor y pasajero</b>."))
    B.append(TABLE(
        [T("Choosing a helmet", "Requisitos para elegir un casco")],
        rows([
            ("<b>Approved</b> to <b>UNECE Regulation 22</b> (label inside): it has passed the safety tests. <b>Integral</b> type recommended; the right <b>size</b> (snug); strong <b>material</b>.", "<b>Homologado</b> conforme al <b>Reglamento UNECE R22</b> (etiqueta interior): ha superado las pruebas de seguridad. Tipo <b>integral</b> recomendable; <b>tamaño</b> ajustado; <b>material</b> resistente."),
            ("<b>Straps and fasteners</b> properly done up so it can’t fly off; <b>light, bright, reflective colours</b> (more visible).", "<b>Cierres y correas</b> bien abrochados para que no salga despedido; <b>colores claros, brillantes y reflectantes</b> (más visibles)."),
            ("Visor in perfect condition, preferably <b>anti-fog</b> (glasses if the helmet has no visor); good <b>ventilation</b> (less fogging).", "Pantalla en perfecto estado, mejor <b>antivaho</b> (gafas si no lleva pantalla); buena <b>ventilación</b> (menos vaho)."),
        ]),
    ))
    B.append(BOX("trap", "Replace the helmet", "Sustituir el casco", [("Replace (throw away) the helmet <b>after an accident or any hard knock</b>.", "El casco se debe <b>sustituir (desechar) después de un accidente o de un fuerte golpe</b>.")]))
    B.append(TABLE(
        [T("Rider’s equipment", "Equipamiento motorista"), T("What to know", "Qué saber")],
        [
            [T("<b>Suit or jacket</b>", "<b>Traje o chaqueta</b>"), T("Preferably <b>leather</b> or another <b>abrasion-resistant</b> material, with protection (back, knees, elbows); <b>bright</b> or reflective colours.", "Preferiblemente de <b>piel</b> u otro material <b>resistente a la abrasión</b>, con protecciones (espalda, rodillas, codos); colores <b>llamativos</b> o reflectantes.")],
            [T("<b>Closed footwear</b>", "<b>Calzado cerrado</b>"), T("Covers the whole foot; <b>compulsory on all roads</b> since October 2026. High boots, snug, with a heel are best; no sandals or flip-flops.", "Que cubra todo el pie; <b>obligatorio en todo tipo de vías</b> desde octubre de 2026. Mejor de caña alta, ajustado y con tacón; nada de sandalias ni chanclas.")],
            [T("<b>Gloves</b>", "<b>Guantes</b>"), T("<b>Compulsory on interurban roads</b>. They protect from cold, keep your hands sensitive for good control and protect them in a fall.", "<b>Obligatorios en vías interurbanas</b>. Protegen del frío, mantienen la sensibilidad para controlar el vehículo y protegen en una caída.")],
            [T("<b>Reflective vest</b>", "<b>Chaleco reflectante</b>"), T("Recommended while riding; part of the motorcycle’s <b>compulsory equipment</b>, worn when you get off onto the carriageway or shoulder of an interurban road.", "Recomendable al circular; forma parte de la <b>dotación obligatoria</b> de la moto y se usa al bajar y ocupar la calzada o el arcén de las interurbanas.")],
        ],
        widths=["26%", "74%"],
    ))

    # ---------------------------------------------------------------- 4.2.5 ADAS
    B.append(H3("4.2.5 Driver-assistance systems (ADAS)", "4.2.5 Sistemas ADAS"))
    B.append(P(
        "<b>ADAS</b> (<i>Advanced Driver Assistance Systems</i>; <i>sistemas avanzados de asistencia a la conducción</i>) are systems that <b>help the driver</b>, making driving and decisions safer for them and for others. "
        "In general they <b>collect information through cameras and sensors</b> and <b>warn the driver</b> or even <b>act on the controls</b>. Most can be <b>switched off by the driver</b>, temporarily or permanently.",
        "Los <b>ADAS</b> (<i>Advanced Driver Assistance Systems</i>) son sistemas que <b>ayudan al conductor</b> y <b>aumentan la seguridad</b> para él y para los demás, facilitando la conducción y las decisiones. "
        "En general <b>recogen información con cámaras y sensores</b> y <b>emiten avisos</b> o incluso <b>actúan sobre los mandos</b>. La mayoría pueden ser <b>desconectados por el conductor</b>, temporal o permanentemente."))
    B.append(BOX("trap", "Two warnings", "Dos advertencias", [
        ("The <b>driver keeps an active role</b>: however many systems the car has, keep <b>full attention and control</b> and <b>don’t take more risks</b> trusting that they will act for you.",
         "El <b>conductor tiene un papel activo</b>: por muchos sistemas que lleve el vehículo, hay que mantener <b>total atención y control</b> y <b>no asumir más riesgos</b> confiando en que actuarán por nosotros."),
        ("In some cars, ADAS <b>lose their calibration when the battery is disconnected</b> (it depends on the make and model), as happens with the steering-angle sensors.", "En algunos casos los ADAS <b>pierden la calibración al desconectar la batería</b> (depende del modelo y fabricante), como sucede con los sensores del ángulo de dirección."),
    ]))
    B.append(BOX("key", "Compulsory in new cars", "Obligatorios en los coches nuevos", [
        ("Under EU Regulation 2019/2144, every <b>new vehicle registered since 6 July 2024</b> must have a set of ADAS — for cars, among others: <b>ISA</b>, <b>drowsiness warning</b>, <b>emergency braking (AEB)</b>, <b>lane keeping</b>, "
         "<b>reversing detection</b>, <b>tyre-pressure monitoring</b>, the <b>emergency stop signal</b> and the <b>event data recorder</b>. Pedestrian and cyclist AEB is required in new cars registered from <b>6 July 2026</b>.",
         "Según el Reglamento (UE) 2019/2144, todo <b>vehículo nuevo matriculado desde el 6 de julio de 2024</b> debe incorporar un conjunto de ADAS; en turismos, entre otros: <b>ISA</b>, <b>advertencia de somnolencia</b>, <b>frenado de emergencia (AEB)</b>, <b>mantenimiento de carril</b>, "
         "<b>detector de marcha atrás</b>, <b>control de presión de neumáticos</b>, <b>aviso de frenada de emergencia</b> y <b>registrador de datos</b>. El AEB ante peatones y ciclistas se exige a los matriculados desde el <b>6 de julio de 2026</b>."),
    ]))
    B.append(TABLE(
        [T("Main ADAS", "Principales ADAS"), T("What it does", "Qué hace")],
        [
            [T("<b>ISA</b> — intelligent speed assistance", "<b>ISA</b>: asistente de velocidad inteligente"),
             T("Combines <b>adaptive cruise control</b> and <b>traffic-sign recognition</b>: a camera behind the rear-view mirror reads the signs and the system keeps a <b>suitable speed</b> by <b>reducing engine revs — it never brakes</b>. Switched on or off by the driver.",
               "Une el <b>control de crucero adaptativo</b> y el <b>reconocimiento de señales</b>: una cámara en el retrovisor lee las señales y el sistema mantiene la <b>velocidad adecuada</b> <b>reduciendo las revoluciones, nunca frena</b>. Se activa o desactiva manualmente.")],
            [T("<b>ACC</b> — adaptive cruise control", "<b>ACC</b>: control de crucero adaptativo"),
             T("Cruise control keeps a set speed and <b>switches off when you brake</b>; the adaptive version also <b>keeps the safety distance</b> to the vehicle ahead automatically.", "El control de crucero mantiene una velocidad fijada y <b>se desconecta al pisar el freno</b>; el adaptativo además <b>mantiene la distancia de seguridad</b> automáticamente.")],
            [T("<b>Emergency braking warning</b> (your course: EBD)", "<b>Aviso de frenada de emergencia</b> (EBD en tu curso)"),
             T("In hard braking the <b>brake lights flash quickly</b> to warn those behind (in EU rules, the emergency stop signal). Your course also describes another system with the same initials: <b>electronic brake-force distribution</b>, which shares the braking force between the wheels.",
               "En una frenada fuerte, las <b>luces de freno parpadean rápidamente</b> para avisar a los de detrás. Tu curso describe además otro sistema con las mismas siglas: el <b>reparto electrónico de la frenada</b>, que distribuye la fuerza de frenado entre las ruedas.")],
            [T("<b>AEB / AEBS</b> — automatic emergency braking", "<b>AEB / AEBS</b>: frenado automático de emergencia"),
             T("A front radar detects imminent danger; if the driver ignores the warnings (sound and light), <b>the car brakes by itself</b> to avoid or reduce the collision. In town and out of town.", "Un radar frontal detecta peligros inminentes; si el conductor ignora los avisos (visuales y acústicos), <b>el vehículo frena solo</b> para evitar o mitigar la colisión. Urbano e interurbano.")],
            [T("<b>LDW</b> — lane departure warning (and <b>LKA / ELKS</b>)", "<b>LDW</b>: alerta de cambio de carril (y <b>LKA / ELKS</b>)"),
             T("Cameras read the lane lines and <b>warn</b> (sound, light or <b>vibration</b> in the wheel or seat) of an <b>unintended</b> drift. It stays off if you <b>signal</b> or steer evasively; usually active from <b>60–80 km/h</b>. "
               "Lane keeping (LKA / ELKS) goes further: it <b>corrects the steering</b> or brakes the wheels on the other side.",
               "Cámaras leen las líneas y <b>avisan</b> (sonido, luz o <b>vibración</b> en volante o asiento) si el cambio de trayectoria es <b>involuntario</b>. Permanece desactivado si se pone el <b>intermitente</b> o se esquiva; suele activarse a partir de <b>60–80 km/h</b>. "
               "El mantenimiento de carril (LKA / ELKS) va más allá: <b>corrige la dirección</b> o frena las ruedas opuestas.")],
            [T("<b>RCTA</b> — rear cross-traffic alert", "<b>RCTA</b>: alerta de tráfico cruzado"),
             T("When <b>reversing out</b> of a space, warns of people, objects or vehicles crossing behind (up to <b>30 m</b>); some brake by themselves below <b>15 km/h</b>. Still check the mirrors and look directly.",
               "Al <b>salir marcha atrás</b>, avisa de personas, objetos o vehículos que cruzan por detrás (hasta <b>30 m</b>); algunos frenan solos por debajo de <b>15 km/h</b>. Hay que seguir mirando los espejos y directamente.")],
            [T("<b>Rear camera</b> and <b>360° system</b>", "<b>Cámara trasera</b> y <b>sistema 360°</b>"),
             T("Show the area behind or a virtual <b>bird’s-eye view</b>, with guide lines or red arrows marking danger. They switch on when you <b>engage reverse</b> or press a button.", "Muestran la parte trasera o una <b>imagen cenital virtual</b>, con líneas guía o flechas rojas de peligro. Se activan al <b>meter la marcha atrás</b> o con un botón.")],
            [T("<b>Parking assist</b>", "<b>Asistencia de estacionamiento</b>"), T("Ultrasonic sensors find a big enough space; the system <b>steers</b> (sometimes brakes) to park — and helps you leave.", "Sensores de ultrasonidos buscan un hueco suficiente; el sistema <b>controla la dirección</b> (a veces el freno) para aparcar, y ayuda a salir.")],
            [T("<b>DDAW / DDR-ADR</b> — drowsiness and distraction warning", "<b>DDAW / DDR-ADR</b>: somnolencia y distracción"), T("Checks whether the driver is <b>alert and taking part</b> (some watch eyes and head) and advises stopping to rest.", "Evalúa si el conductor <b>participa activamente</b> (algunos vigilan ojos y cabeza) y aconseja detenerse a descansar.")],
            [T("<b>Alcolock interface</b>", "<b>Interfaz para alcoholímetro antiarranque</b>"), T("A standard connection to fit a breathalyser that <b>stops the engine starting</b> if the driver is over the limit. Your course: compulsory in professional and public-transport vehicles.", "Interfaz normalizada para instalar un alcoholímetro que <b>impide arrancar</b> si se supera la tasa. Según tu curso, obligatorio en vehículos profesionales y de transporte público.")],
            [T("<b>Hill holder</b>, <b>Start-Stop</b>, <b>head-up display</b>", "<b>Hill holder</b>, <b>Start-Stop</b>, <b>head-up display</b>"),
             T("Hill holder: <b>stops the car rolling back</b> when you lift off the brake on a slope. Start-Stop: <b>stops the engine at idle</b> and restarts it when you press the clutch (less fuel and emissions). HUD: <b>projects data</b> into your line of sight.",
               "Hill holder: <b>impide que el coche vaya hacia atrás</b> al soltar el freno en pendiente. Start-Stop: <b>apaga el motor al ralentí</b> y lo enciende al pisar el embrague (menos emisiones y consumo). HUD: <b>proyecta información</b> en la línea visual.")],
            [T("<b>Automatic lights and wipers</b>", "<b>Alumbrado y limpiaparabrisas automáticos</b>"), T("A sensor detects darkness or rain. Also <b>automatic high beam</b>, <b>cornering lights</b> and <b>adaptive lighting</b> (shapes the beam so others are not dazzled).", "Un sensor detecta poca visibilidad o lluvia. También <b>luz de carretera automática</b>, <b>iluminación en curva</b> e <b>iluminación adaptativa</b> (ajusta el haz sin deslumbrar).")],
            [T("<b>Seat-belt reminder</b>, <b>TPM</b>, <b>sign recognition</b>, <b>night vision</b>", "<b>Alerta de cinturón</b>, <b>TPM</b>, <b>reconocimiento de señales</b>, <b>visión nocturna</b>"),
             T("Belt warning for front and rear seats; <b>tyre-pressure monitoring</b> while driving; a camera reads speed-limit and no-overtaking signs (gives priority to the last one; falls back on map data); "
               "<b>infrared</b> images of pedestrians or animals beyond the headlights.",
               "Aviso de cinturón en plazas delanteras y traseras; <b>control de presión de neumáticos</b> en marcha; una cámara lee las señales de velocidad o prohibido adelantar (da relevancia a la última; si no, datos de navegación); "
               "imágenes por <b>infrarrojos</b> de peatones o animales fuera del alcance de los faros.")],
            [T("<b>EDR</b> — event data recorder (“black box”)", "<b>EDR</b>: registrador de datos (caja negra)"), T("Records key data just before, during and after a collision (speed, braking, position, safety systems, eCall). <b>It cannot be switched off.</b>", "Registra datos críticos poco antes, durante y justo después de una colisión (velocidad, frenada, posición, sistemas de seguridad, eCall). <b>No se puede desactivar.</b>")],
        ],
        widths=["30%", "70%"],
        cls="small",
    ))
    B.append(BOX("key", "ADAS aftermarket", "ADAS aftermarket", [
        ("A car already registered without ADAS can have one fitted by an <b>ADAS aftermarket</b> maker, as long as it is a <b>warning system</b> that <b>does not act on the car’s driving controls</b>.",
         "Un automóvil ya matriculado sin ADAS puede instalar uno de un fabricante <b>ADAS Aftermarket</b>, siempre que sea un <b>sistema de aviso</b> que <b>no actúe sobre los sistemas de conducción</b>."),
    ]))
    B.append(TABLE(
        [T("Other ADAS", "Otros sistemas ADAS"), T("What it does", "Qué hace")],
        [
            [T("<b>FCW</b> — forward collision warning", "<b>FCW</b>: advertencia de colisión frontal"), T("Detects pedestrians, cyclists and vehicles, moving or still; <b>warns</b> if you are too close and in a critical moment can help stop the car.", "Detecta peatones, ciclistas y vehículos, en movimiento o parados; <b>avisa</b> si no se guarda la distancia y, en una situación crítica, puede ayudar a detener el vehículo.")],
            [T("<b>BSM</b> — blind-spot monitor", "<b>BSM</b>: aviso de ángulo muerto"), T("Warns (sound, a light near the door mirror, or vibration) of vehicles coming up in the next lanes; some act on steering or brakes, but <b>the driver stays in full control</b>.", "Avisa (sonido, luz junto al retrovisor exterior o vibración) de vehículos que se aproximan por los carriles contiguos; algunos actúan sobre dirección o frenos, pero <b>el conductor tiene el control absoluto</b>.")],
            [T("<b>Exit warning</b>", "<b>Advertencia de salida del vehículo</b>"), T("Rear sensors warn occupants of <b>cyclists or vehicles coming from behind</b> before they open a door.", "Los sensores traseros avisan a los ocupantes de <b>ciclistas o vehículos que vienen por detrás</b>.")],
            [T("<b>eCall</b>", "<b>eCall</b>"), T("When the airbags go off it <b>calls 112</b> automatically (or by pressing <b>SOS</b>); operators answer in the caller’s language anywhere in Europe. It cuts response time.", "Al saltar los airbags <b>llama al 112</b> automáticamente (o pulsando <b>SOS</b>); los operadores responden en el idioma de quien llama en cualquier país europeo. Reduce el tiempo de respuesta.")],
            [T("<b>Evasive steering assist</b>", "<b>Asistente de esquiva</b>"), T("From <b>30 km/h</b>, works out an escape path and helps the steering — <b>only while the driver is steering</b>.", "A partir de <b>30 km/h</b> calcula una vía de escape y ayuda con la dirección, <b>siempre que el conductor esté maniobrando</b>.")],
            [T("<b>Turn assist</b>", "<b>Asistente de giro</b>"), T("Turning <b>left</b> with the indicator on, up to <b>10 km/h</b>, it brakes if an oncoming vehicle is coming.", "Al girar a la <b>izquierda</b> con el intermitente, hasta <b>10 km/h</b>, frena si viene un vehículo de frente.")],
            [T("<b>Pre-crash safety</b>, <b>adaptive suspension and steering</b>, <b>predictive efficiency</b>", "<b>Sistema preventivo</b>, <b>control de suspensión y dirección</b>, <b>asistente predictivo de eficiencia</b>"),
             T("Before an unavoidable crash (even from behind): tightens the belts, closes the windows, moves the seats. Adapts suspension and steering (sport or comfort). Uses the route to slow down or change gear efficiently.",
               "Ante una colisión inminente (incluso trasera): tensa los cinturones, cierra las ventanillas, mueve los asientos. Adapta suspensión y dirección (deportividad o confort). Usa los datos de la ruta para reducir la velocidad o cambiar de marcha con eficiencia.")],
        ],
        widths=["32%", "68%"],
        cls="small",
    ))
    B.append(P(
        "<b>ADAS in the driving test.</b> The DGT’s instruction <b>COND 2024/12</b> lists the systems allowed in the practical test. <b>Any system not listed must be switched off.</b> "
        "Your course prints the same heading over both lists; in the instruction the second group is <b>“allowed, and graded”</b>: if one of those systems warns or steps in, the examiner judges what happened.",
        "<b>Los ADAS en el examen práctico.</b> La instrucción de la DGT <b>COND 2024/12</b> recoge los sistemas admitidos. <b>Los no recogidos deben desactivarse.</b> "
        "Tu curso pone el mismo título a las dos listas; en la instrucción el segundo grupo es <b>«admitidos y calificación»</b>: si uno de esos sistemas avisa o interviene, el examinador valora lo ocurrido."))
    B.append(TABLE(
        [T("Group", "Grupo"), T("Systems", "Sistemas")],
        [
            [T("<b>Allowed, no effect on the grade</b>", "<b>Admitidos sin incidencia en la calificación</b>"),
             T("Start-Stop; hill holder; reversing detection (REV); rear camera, 360° camera and parking sensors (<b>not full self-parking</b>, which is not allowed); emergency braking warning; speed limiter (SLI); event data recorder (EDR); "
               "sign recognition (TSR, passive only); <b>ISA with its automatic speed control (SCF) switched off</b> — your course says the speed-limit warning (SLWF) too.",
               "Start-Stop; ayuda de salida en pendiente; detector de marcha atrás (REV); cámara de marcha atrás, 360° y sensores (<b>no la ayuda de estacionamiento total</b>, que no está permitida); aviso de frenada de emergencia; limitador (SLI); registrador (EDR); "
               "reconocimiento de señales (TSR, solo pasivo); <b>ISA con el control automático de velocidad (SCF) desactivado</b>; tu curso añade el aviso de límite (SLWF).")],
            [T("<b>Allowed, and graded</b> if they act", "<b>Admitidos y calificación</b> si actúan"),
             T("Tyre-pressure monitoring (TPM); automatic lights and wipers (if they don’t switch on when needed, you must do it); <b>AEB</b> and pedestrian/cyclist AEB (an intervention counts <b>like the instructor stepping in</b>); "
               "pedestrian and cyclist collision warning (VIS-DET); RCTA; drowsiness and distraction warnings (DDR-DAD, DDR-ADR); blind-spot information (BSIS); lane keeping (LKA); lane departure warning (LDW).",
               "Control de presión (TPM); alumbrado y limpiaparabrisas automáticos (si no se activan cuando hace falta, hay que hacerlo manualmente); <b>AEB</b> y AEB ante peatones y ciclistas (su intervención se valora <b>como la del profesor</b>); "
               "advertencia de colisión con peatones y ciclistas (VIS-DET); RCTA; somnolencia y distracciones (DDR-DAD, DDR-ADR); ángulos muertos (BSIS); mantenimiento de carril (LKA); abandono de carril (LDW).")],
        ],
        widths=["28%", "72%"],
        cls="small",
    ))

    # ---------------------------------------------------------------- 4.3 road
    B.append(H3("4.3 The road and its surroundings", "4.3 Factor vía y su entorno"))
    B.append(P(
        "So that driving doesn’t become dangerous, <b>adapt the way you drive to the road</b> (surface, layout…) and to the <b>weather</b> (rain, snow, fog…). The road factor is involved in <b>10–35 %</b> of accidents.",
        "Para que la conducción no se vuelva peligrosa hay que <b>adaptarla a las condiciones de la vía</b> (pavimento, trazado…) y de la <b>climatología</b> (lluvia, nieve, niebla…). El factor vía está implicado en el <b>10–35 %</b> de los accidentes."))
    B.append(TABLE(
        [T("Grip", "Adherencia"), T("Depends on the road’s condition, the type of surface and the vehicle’s condition", "Depende del estado de la calzada, el tipo de firme y el estado del vehículo")],
        [
            [T("<b>Good grip</b>", "<b>Buena adherencia</b>"), T("Asphalt, rigid and <b>rough</b> surfaces (not shiny), especially <b>dry and clean</b>.", "Asfalto, pavimentos rígidos y <b>rugosos</b> (sin brillos), sobre todo con la calzada <b>seca y limpia</b>.")],
            [T("<b>Poor grip</b>", "<b>Mala adherencia</b>"), T("Smooth surfaces or <b>cobbles</b>; a <b>wet</b> road, gravel, leaves, snow, or some very slippery <b>road markings</b>.", "Pavimentos lisos o de <b>adoquines</b>; calzada <b>húmeda</b>, con gravilla, hojas, nieve o algunas <b>marcas viales</b> muy resbaladizas.")],
        ],
        widths=["22%", "78%"],
    ))
    B.append(BOX("key", "Bicycles, mopeds and motorcycles", "Ciclos, ciclomotores y motocicletas", [
        ("In bad weather, watch for <b>road markings</b> — they are very slippery. <b>Slow down before reaching them</b>, keep the vehicle <b>upright</b> while crossing and <b>don’t brake on them</b>.",
         "Con condiciones adversas, atención a las <b>marcas viales</b>: son muy resbaladizas. <b>Disminuir la velocidad antes de llegar</b>, mantener el vehículo en <b>posición vertical</b> al pasar y <b>no frenar sobre ellas</b>."),
    ]))
    B.append(TABLE(
        [T("Forces in a bend", "Fuerzas en las curvas"), T("What it does", "Qué hace")],
        [
            [T("<b>Centrifugal force</b>", "<b>Fuerza centrífuga</b>"),
             T("<b>The most dangerous</b>: it <b>pushes the vehicle to the outside</b> of the bend, along a straight line. It grows with a <b>tighter bend</b> (smaller radius), <b>more speed</b> and <b>more weight</b> (vehicle and load). "
               "Speed counts most: <b>double the speed, four times the force</b>.",
               "<b>La más peligrosa</b>: <b>empuja el vehículo hacia el exterior</b> de la curva, siguiendo una línea recta. Aumenta con un <b>radio menor</b> (curva más cerrada), <b>más velocidad</b> y <b>más peso</b> (vehículo y carga). "
               "La velocidad es lo que más influye: <b>al doble de velocidad, cuatro veces más fuerza</b>.")],
            [T("<b>Centripetal force</b>", "<b>Fuerza centrípeta</b>"), T("The result of <b>what the driver does</b> to take the bend (turning the wheel, driving technique).", "Es la consecuencia de las <b>acciones del conductor</b> para trazar la curva (girar el volante, técnicas de conducción).")],
        ],
        widths=["24%", "76%"],
    ))
    B.append(FIG(curve_technique, "Before the bend, slow down on the straight; inside it, keep a gentle, steady throttle; on the way out, accelerate and straighten the wheel.",
                 "Antes de la curva, reduce en la recta; dentro, acelera suave y progresivamente; a la salida, acelera y endereza el volante."))
    B.append(P(
        "A <b>skid</b> happens when the <b>wheels lose grip</b> and the vehicle slides sideways, especially in bends. <b>Causes</b>: <b>sudden use</b> of the accelerator, brake or steering; <b>too much speed</b> together with a vehicle in poor condition "
        "(worn or under-inflated tyres, damaged suspension, worn brakes) or a slippery surface.",
        "El <b>derrape</b> se produce cuando las <b>ruedas pierden adherencia</b> y el vehículo se desvía hacia un lado, sobre todo en curvas. <b>Causas</b>: <b>uso brusco</b> del acelerador, el freno o el volante; <b>velocidad excesiva</b> junto con mal estado del vehículo "
        "(neumáticos gastados o con poca presión, suspensión dañada, frenos gastados) o pavimento deslizante."))
    B.append(TABLE(
        [T("Skid", "Derrape"), T("What to do", "Cómo actuar")],
        [
            [T("Caused by <b>too much braking</b>", "Por <b>exceso de frenada</b>"), T("<b>Release the brake.</b>", "<b>Soltar el freno.</b>")],
            [T("<b>Front axle</b> slides", "Derrapa el <b>eje delantero</b>"), T("<b>Straighten the steering.</b>", "<b>Enderezar la dirección.</b>")],
            [T("<b>Rear axle</b> slides", "Derrapa el <b>eje trasero</b>"), T("<b>Turn the wheel towards the same side as the skid.</b>", "<b>Girar el volante hacia el mismo lado del derrape.</b>")],
        ],
        widths=["34%", "66%"],
    ))
    B.append(FIG(skid, "Front wheels sliding: the car goes straight on — straighten the steering. Rear wheels sliding: the rear swings out — steer towards the same side.",
                 "Si derrapan las ruedas delanteras, el coche sigue recto: endereza la dirección. Si derrapan las traseras, la parte trasera se va hacia fuera: gira hacia el mismo lado."))
    B.append(BOX("key", "Avoiding skids", "Cómo evitar el derrape", [
        ("<b>Moderate your speed</b>, <b>increase the safety distance</b> (to avoid surprises) and use the accelerator, brake and steering <b>smoothly</b>.", "<b>Moderar la velocidad</b>, <b>aumentar la distancia de seguridad</b> (evitar imprevistos) y usar acelerador, freno y volante con <b>suavidad</b>."),
    ]))

    B.append(H3("4.3.2 Weather", "4.3.2 Climatología"))
    B.append(TABLE(
        [T("Weather", "Meteorología"), T("To see and be seen", "Para mejorar la visibilidad"), T("For grip", "Para mejorar la adherencia")],
        [
            [T("<b>Rain</b> — most dangerous with the <b>first drops</b>", "<b>Lluvia</b>: más peligrosa al caer las <b>primeras gotas</b>"),
             T("<b>Compulsory lights</b> (high beams can dazzle off the water); wipers and <b>demister</b>; extra care overtaking or following <b>large vehicles</b> (more distance).",
               "<b>Alumbrado obligatorio</b> (las largas pueden deslumbrar por el reflejo del agua); limpiaparabrisas y <b>antivaho</b>; precaución al adelantar o seguir a <b>vehículos grandes</b> (más distancia)."),
             T("<b>Brake early and gently</b> (braking distance can <b>double</b>); watch dips and flooding; <b>wet brakes</b> lose effect — dry them with short presses; <b>slow down</b> (aquaplaning). "
               "<b>Small puddles</b>: between the wheels or with all of them, slowly if only one side; <b>large puddles</b>: very slowly, in first gear if needed.",
               "<b>Frenar con antelación y suavidad</b> (la distancia de frenado puede <b>duplicarse</b>); atención a badenes y zonas inundables; los <b>frenos mojados</b> pierden eficacia: secarlos con pequeñas pulsaciones; <b>reducir la velocidad</b> (aquaplaning). "
               "<b>Charcos pequeños</b>: entre las ruedas o con todas, despacio si es con las de un lado; <b>grandes</b>: muy despacio, incluso en primera.")],
            [T("<b>Snow</b> — most dangerous with the <b>first flakes</b> and when it <b>hardens</b>", "<b>Nieve</b>: más peligrosa con los <b>primeros copos</b> y cuando se <b>endurece</b>"),
             T("<b>Clear snow off all the glass</b> before setting off; compulsory lights; wipers (stop to clear them if needed); <b>sunglasses</b> by day (glare from the snow).",
               "<b>Retirar la nieve de los cristales</b> antes de salir; alumbrado obligatorio; limpiaparabrisas (parar a limpiarlos si hace falta); <b>gafas de sol</b> de día (reflejo del sol en la nieve)."),
             T("Move off gently, in <b>second gear</b>, wheels straight; smooth driving, no braking or sudden moves; <b>more distance</b>, low speed, the <b>highest gear possible</b>. Uphill: long gears, slow and steady; downhill: <b>low gears</b> (engine brake). "
               "<b>Thick</b> snow: drive in other vehicles’ <b>ruts</b>; <b>thin</b> snow: where there are <b>no ruts</b>. <b>Chains</b> (at least on the driving wheels) or snow tyres. On hard snow or ice: don’t brake or accelerate.",
               "Arrancar suave, en <b>segunda</b>, con las ruedas rectas; suavidad, sin frenar ni movimientos bruscos; <b>más distancia</b>, velocidad reducida, la <b>marcha más alta posible</b>. Subiendo: largas, lento y sostenido; bajando: <b>cortas</b> (freno motor). "
               "Capa <b>gruesa</b>: por las <b>rodaduras</b> de otros; capa <b>fina</b>: donde <b>no haya rodaduras</b>. <b>Cadenas</b> (al menos en las ruedas motrices) o neumáticos de nieve. Sobre nieve dura o hielo: ni frenar ni acelerar.")],
            [T("<b>Ice</b> — <b>the most dangerous</b>: grip almost nil, stopping distance <b>×10</b>", "<b>Hielo</b>: <b>lo más peligroso</b>, adherencia casi nula, detención <b>×10</b>"),
             T("<b>Clear the ice</b> off the glass before setting off (scraper, heating aimed at it, rear-window heater).", "<b>Retirar el hielo</b> de los cristales antes de salir (rascador, calefacción orientada, luneta térmica)."),
             T("<b>Chains</b> (driving wheels) or special tyres (winter, snow or <b>studded</b>); <b>smooth driving</b> — no sudden acceleration, braking or steering; the <b>highest gear possible</b>.",
               "<b>Cadenas</b> (ruedas motrices) o neumáticos especiales (invierno, nieve o <b>clavos</b>); <b>suavidad</b>: sin acelerones, frenazos ni volantazos; la <b>marcha más alta posible</b>.")],
            [T("<b>Fog</b> — also dust clouds and smoke", "<b>Niebla</b>: también nubes de polvo y humo"),
             T("Compulsory lights; follow the <b>road markings</b> and other vehicles’ lights; keep the car <b>ventilated</b> and the demister on.", "Alumbrado obligatorio; guiarse por las <b>marcas viales</b> y las luces de otros vehículos; habitáculo <b>ventilado</b> y antivaho."),
             T("<b>Slow down</b> to match the visibility; <b>more distance</b> (pile-ups); <b>avoid overtaking</b>; stop somewhere safe if visibility is <b>almost nil</b>.", "<b>Reducir la velocidad</b> según la visibilidad; <b>más distancia</b> (choques en cadena); <b>evitar adelantar</b>; inmovilizar en un lugar seguro si la visibilidad es <b>casi nula</b>.")],
        ],
        widths=["20%", "34%", "46%"],
        cls="small",
    ))
    B.append(BOX("key", "Aquaplaning and ice", "Aquaplaning y hielo", [
        ("<b>Aquaplaning</b>: at <b>too high a speed</b> the tread <b>can’t clear the water</b> and the tyre floats on it — the car <b>ignores the steering and brakes</b>. Worst with <b>worn tyres</b> and on <b>two-wheelers</b>.",
         "<b>Aquaplaning</b>: a <b>velocidad excesiva</b> el dibujo <b>no puede desalojar el agua</b> y el neumático se desliza sobre ella: el vehículo <b>no obedece a la dirección ni al freno</b>. Peor con <b>neumáticos gastados</b> y en <b>vehículos de dos ruedas</b>."),
        ("<b>Ice is common</b> when it is <b>near or below 0 °C</b>, <b>at night or at dawn</b>, and in <b>damp, shady places</b> (bridges, underpasses, ditches, tree-lined stretches) and dips.",
         "<b>El hielo es frecuente</b> con temperaturas <b>cercanas o inferiores a 0 °C</b>, <b>de noche o al amanecer</b>, y en <b>lugares húmedos y sombríos</b> (puentes, pasos inferiores, cunetas, zonas con árboles) y badenes."),
        ("If <b>snow is forecast</b>: a <b>full tank</b>, warm clothes (even blankets), water and food, a torch, and a <b>charged phone</b> with charger.", "Si hay <b>previsión de nevada</b>: <b>depósito lleno</b>, ropa de abrigo (incluso mantas), agua y comida, linterna y <b>móvil cargado</b> con cargador."),
    ]))
    B.append(BOX("trap", "Snow rules", "Normas con nieve", [
        ("On <b>autopistas and autovías</b>, when snow makes driving difficult, <b>overtaking is prohibited</b> and you must use the <b>right-hand lane</b> (also the next one where there are three or more lanes), leaving the left lanes free for <b>emergency vehicles and snowploughs</b>.",
         "En <b>autopistas y autovías</b>, cuando la nieve dificulte la circulación, está <b>prohibido adelantar</b> y es obligatorio circular por el <b>carril de la derecha</b> (también su contiguo en tramos de tres o más carriles), dejando libres los de la izquierda para <b>emergencias y quitanieves</b>."),
        ("Traffic authorities and agents can <b>make chains compulsory</b> — a <b>snow spray does not count</b>. If you don’t comply, you are <b>fined and the vehicle is immobilised</b>.",
         "Las autoridades y agentes pueden <b>obligar a usar cadenas</b> (<b>no sustituibles por sprays</b> para nieve). Si no se cumple, se <b>sanciona y se inmoviliza el vehículo</b>."),
    ]))
    B.append(P(
        "<b>Wind</b> is dangerous when it blows <b>from the side</b> or in <b>gusts</b>. The most affected: <b>bicycles, mopeds, motorcycles</b> and <b>bulky vehicles</b> (vans, lorries, trailers). <b>Slow down</b>, <b>hold the wheel firmly</b> turned slightly <b>into the wind</b>, "
        "and watch for the <b>screen effect</b> (buildings, tunnels, bulky vehicles that suddenly block the wind).",
        "El <b>viento</b> es peligroso cuando sopla <b>transversalmente</b> o a <b>ráfagas</b>. Los más afectados: <b>bicicletas, ciclomotores, motocicletas</b> y <b>vehículos voluminosos</b> (furgonetas, camiones, remolques). <b>Reducir la velocidad</b>, <b>sujetar el volante con firmeza</b> girando contra el viento "
        "y extremar la precaución con el <b>efecto pantalla</b> (edificios, túneles, vehículos voluminosos que tapan el viento de golpe)."))
    B.append(FIG(crosswind, "Strong wind from the right: steer slightly right; alongside the lorry, which shields you, straighten; once past it, correct to the right again.",
                 "Viento fuerte de derecha a izquierda: volante un poco a la derecha; junto al camión, que hace de pantalla, endereza; al dejarlo atrás, vuelve a corregir a la derecha."))
    B.append(TABLE(
        [T("Sun", "Sol")],
        rows([
            ("The sun can <b>dazzle</b>. Choose a <b>good departure time</b> (avoid sunrise and sunset); wear <b>sunglasses</b> — but <b>never at night or in tunnels</b>; use the <b>sun visor</b>; keep the <b>windows clean</b>.",
             "El sol puede <b>deslumbrar</b>. Elegir una <b>hora de salida adecuada</b> (evitar la salida y la puesta de sol); <b>gafas de sol</b>, pero <b>nunca de noche ni en túneles</b>; orientar el <b>parasol</b>; mantener los <b>cristales limpios</b>."),
        ]),
    ))

    # ---------------------------------------------------------------- 5. traps
    B.append(H2("5", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("More <b>accidents</b> in towns, more <b>deaths</b> on interurban roads. Most interurban accidents: <b>straight roads with good visibility</b>, running off the road.", "Más <b>accidentes</b> en ciudad, más <b>muertos</b> en carretera. La mayoría en carretera: <b>rectas con buena visibilidad</b>, salidas de la vía."),
        ("Young drivers are a <b>risk group</b>, <b>not</b> vulnerable users. Older pedestrians have more accidents <b>alone</b> than with children.", "Los jóvenes son <b>grupo de riesgo</b>, <b>no</b> usuarios vulnerables. Los peatones mayores tienen más accidentes <b>solos</b> que con niños."),
        ("Behind a cyclist in town: <b>5 m</b>. Overtaking: <b>1.5 m</b> and, out of town, <b>20 km/h below the limit</b>. Children under 12 on the pavement only with an <b>adult on foot</b> and if the town allows it.",
         "Detrás de un ciclista en ciudad: <b>5 m</b>. Al adelantar: <b>1,5 m</b> y, en interurbana, <b>20 km/h menos del límite</b>. Menores de 12 en la acera solo con un <b>adulto a pie</b> y si el ayuntamiento lo permite."),
        ("VMP: <b>15</b> years, helmet, <b>25 km/h</b>, <b>no passenger</b>, never on pavements, interurban roads, travesías or autovías.", "VMP: <b>15</b> años, casco, <b>25 km/h</b>, <b>sin acompañante</b>, nunca por aceras, interurbanas, travesías ni autovías."),
        ("Reaction time <b>0.75 s</b>; stopping distance = <b>reaction + braking</b>. Rain <b>×2</b>, ice <b>×10</b> (braking distance).", "Tiempo de reacción <b>0,75 s</b>; detención = <b>reacción + frenado</b>. Lluvia <b>×2</b>, hielo <b>×10</b>."),
        ("You can crash from drowsiness <b>without falling asleep</b>. Coffee has a <b>rebound effect</b>.", "Se puede tener un accidente por somnolencia <b>sin llegar a dormirse</b>. El café tiene <b>efecto rebote</b>."),
        ("The medicine pictogram <b>warns</b>, it does <b>not forbid</b>. Smoking while driving is <b>not prohibited</b>.", "El pictograma de los medicamentos <b>advierte</b>, <b>no prohíbe</b>. Fumar conduciendo <b>no está prohibido</b>."),
        ("Phone: the <b>most dangerous moments</b> are answering, dialling, talking and hanging up; the most frequent accident is <b>running off the road</b>. Even at a red light, <b>no hands</b>.",
         "Móvil: los <b>momentos más peligrosos</b> son recibir, marcar, hablar y colgar; el accidente más frecuente es la <b>salida de vía</b>. Ni en un semáforo en rojo se puede <b>usar con la mano</b>."),
        ("Alcohol: <b>fermented</b> drinks absorb <b>more slowly</b> than distilled; an empty stomach and fizzy drinks <b>speed it up</b>; quantity matters most. Under-18 drivers: <b>0.0</b>.", "Alcohol: las <b>fermentadas</b> se absorben <b>más despacio</b> que las destiladas; en ayunas y con gas, <b>más rápido</b>; lo que más influye es la cantidad. Menores: <b>0,0</b>."),
        ("Second breath test: at least <b>10 minutes</b> later. Contrast blood test: <b>you pay first</b>, refunded if negative.", "Segunda prueba: al menos <b>10 minutos</b> después. Análisis de contraste: <b>lo pagas antes</b>, se devuelve si es negativo."),
        ("Clutch <b>released = engaged</b>. Motorcycle: <b>right hand</b> throttle and front brake, <b>left foot</b> gears.", "Embrague <b>sin pisar = embragado</b>. Moto: <b>mano derecha</b> acelerador y freno delantero, <b>pie izquierdo</b> marchas."),
        ("Pressure: check <b>cold</b>, every <b>15 days</b>; spare at the <b>highest</b> pressure; unequal on one axle is <b>the most dangerous</b>. Tread <b>1.6 mm</b>. Best tyres on the <b>rear</b> axle.",
         "Presión: en <b>frío</b>, cada <b>15 días</b>; repuesto a la <b>más alta</b>; descompensada en un eje es <b>lo más peligroso</b>. Dibujo <b>1,6 mm</b>. Los mejores neumáticos, <b>detrás</b>."),
        ("Emergency braking <b>with ABS</b>: keep pressing hard <b>even if the pedal vibrates</b>. Servo brake works <b>only with the engine running</b>.", "Frenada de emergencia <b>con ABS</b>: seguir pisando a fondo <b>aunque vibre el pedal</b>. El servofreno solo funciona <b>con el motor en marcha</b>."),
        ("Rear-axle skid: steer <b>towards</b> the skid. Front-axle skid: <b>straighten</b>.", "Derrape trasero: girar <b>hacia el mismo lado</b>. Delantero: <b>enderezar</b>."),
        ("Thick snow: <b>in the ruts</b>; thin snow: <b>where there are none</b>. Snow on motorways: <b>no overtaking</b>, right-hand lane.", "Nieve gruesa: <b>por las rodaduras</b>; fina: <b>donde no haya</b>. Nieve en autovía: <b>prohibido adelantar</b>, carril derecho."),
    ]))

    # ---------------------------------------------------------------- 6. numbers
    B.append(H2("6", "Key numbers on one page", "Números clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Number", "Cifra")],
        [
            [T("Factors: human / road / vehicle", "Factores: humano / vía / vehículo"), T("70–90 % / 10–35 % / 4–13 %", "70–90 % / 10–35 % / 4–13 %")],
            [T("People affected by each road death", "Personas afectadas por cada víctima mortal"), T("about 100", "unas 100")],
            [T("Vans: worst hour / worst day", "Furgonetas: peor hora / peor día"), T("15:00–16:00 / Friday", "15:00–16:00 / viernes")],
            [T("Young drivers: age band where accidents are the main cause of death", "Jóvenes: franja en que los accidentes son la principal causa de muerte"), T("15–29 (almost 35 % of deaths)", "15–29 (casi el 35 % de los fallecidos)")],
            [T("Behind a cyclist or VMP in town / overtaking gap", "Tras un ciclista o VMP en ciudad / separación al adelantar"), T("5 m / 1.5 m", "5 m / 1,5 m")],
            [T("Reflective element for cyclists, VMP and pedestrians", "Elemento reflectante de ciclistas, VMP y peatones"), T("visible at 150 m", "visible a 150 m")],
            [T("VMP: minimum age / top speed", "VMP: edad mínima / velocidad máxima"), T("15 / 25 km/h", "15 / 25 km/h")],
            [T("Reaction time", "Tiempo de reacción"), T("0.5–1 s (typical 0.75 s)", "0,5–1 s (habitual 0,75 s)")],
            [T("Visual share of driving information", "Información visual al conducir"), T("90 %", "90 %")],
            [T("Rest", "Descanso"), T("every 2 h or 200 km, 20–30 min; sleep 7–9 h", "cada 2 h o 200 km, 20–30 min; dormir 7–9 h")],
            [T("Peak drowsiness", "Horas de más somnolencia"), T("3–5 h and 14–16 h", "3–5 h y 14–16 h")],
            [T("Car temperature", "Temperatura del habitáculo"), T("20–23 °C", "20–23 °C")],
            [T("Phone in the hand", "Móvil en la mano"), T("6 points, 200 €", "6 puntos, 200 €")],
            [T("Alcohol in air: general / new and professional / under 18", "Alcohol en aire: general / noveles y profesionales / menores"), T("0.25 / 0.15 / 0.0 mg/l", "0,25 / 0,15 / 0,0 mg/l")],
            [T("Alcohol peak / time between breath tests", "Pico de alcohol / tiempo entre pruebas"), T("30–90 min / 10 min", "30–90 min / 10 min")],
            [T("Tread depth / tyre check / tyre age", "Dibujo / revisar presión / antigüedad"), T("1.6 mm (2 recommended) / 15 days / 5 years", "1,6 mm (recomendable 2) / 15 días / 5 años")],
            [T("Child restraints / ISOFIX rear-facing", "Retención infantil / ISOFIX de espaldas"), T("up to 135 cm / at least 15 months or 83 cm", "hasta 135 cm / al menos 15 meses u 83 cm")],
            [T("Airbag distance / inflation speed", "Distancia al airbag / velocidad de inflado"), T("25 cm (never under 10) / 300 km/h", "25 cm (nunca menos de 10) / 300 km/h")],
            [T("Head restraint gap", "Distancia al reposacabezas"), T("4 cm at most", "4 cm como máximo")],
            [T("RCTA range / brakes below", "RCTA alcance / frena por debajo de"), T("30 m / 15 km/h", "30 m / 15 km/h")],
        ],
        widths=["56%", "44%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
# The PDF self-test reuses twelve questions from the page's question bank. The correct option is placed in
# turn at A, B and C so the answer key is not always the same letter.
QUIZ_IDS = ["wh2", "pd4", "cy3", "vm2", "sp3", "ft4", "ph2", "al3", "ty4", "br3", "ps5", "wx4"]


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


SOURCES = [
    ("Real Decreto 518/2026, de 24 de junio: Reglamento General de Circulación — protection of vulnerable road users (BOE 26-06-2026; in force 1-10-2026)", "https://www.boe.es/boe/dias/2026/06/26/pdfs/BOE-A-2026-13889.pdf"),
    ("DGT / Ministerio del Interior press release, 23-06-2026: the reform for vulnerable road users", "https://www.dgt.es/comunicacion/notas-de-prensa/20260623-RD-usuarios-vulnerables"),
    ("Reglamento General de Circulación (RD 1428/2003) — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2003-23514"),
    ("Ley sobre Tráfico, Circulación de Vehículos a Motor y Seguridad Vial (RDL 6/2015), art. 14: alcohol and drugs (0.0 for under-18 drivers)", "https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722"),
    ("DGT, Instrucción COND 2024/12: ADAS in the driving test (in force 16-09-2024)",
     "https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/muevete-con-seguridad/normas-de-trafico/C-conductores/Instruccion-COND2024-12-Adas-en-pruebas-de-aptitud-Actualizacion.pdf"),
    ("DGT: from 22-01-2027 only certified VMP may be used (uncertified models sold before 22-01-2024 until then)", "https://www.dgt.es/comunicacion/notas-de-prensa/dgt-recuerda-que-a-partir-de-22-de-enero-los-vmp-que-se-comercialicen-deberan-estar-certificados-para-su-uso"),
    ("Regulation (EU) 2019/2144 on vehicle general safety (compulsory ADAS)", "https://eur-lex.europa.eu/eli/reg/2019/2144/oj"),
]

GLOSSARY = [
    ("siniestralidad", "accident rate"),
    ("factor de riesgo", "risk factor"),
    ("usuario vulnerable", "vulnerable road user"),
    ("atropello", "pedestrian being hit by a vehicle"),
    ("salida de la vía", "running off the road"),
    ("colisión frontolateral · alcance", "front-side collision · rear-end collision"),
    ("vehículo de movilidad personal (VMP)", "personal mobility vehicle (e-scooter)"),
    ("elemento luminoso o reflectante", "luminous or reflective item"),
    ("efecto túnel", "tunnel vision"),
    ("tiempo / distancia de reacción", "reaction time / distance"),
    ("distancia de frenado · de detención", "braking distance · stopping distance"),
    ("microsueño · somnolencia", "microsleep · drowsiness"),
    ("guías sonoras (GSLF)", "rumble strips"),
    ("prospecto", "patient information leaflet"),
    ("tasa de alcoholemia", "blood alcohol level"),
    ("etilómetro · prueba salival", "breathalyser · saliva drug test"),
    ("inmovilización del vehículo", "immobilising (impounding) the vehicle"),
    ("embragado / desembragado", "clutch engaged (released) / disengaged (pressed)"),
    ("banda de rodadura · flanco · talón", "tread · sidewall · bead"),
    ("índice de carga · código de velocidad", "load index · speed symbol"),
    ("reventón · pinchazo", "blow-out · puncture"),
    ("freno de socorro · freno motor", "emergency brake · engine braking"),
    ("fading", "brake fade"),
    ("lecho de frenado", "emergency escape lane"),
    ("amortiguador", "shock absorber"),
    ("deformación programada", "crumple zones"),
    ("cristal laminado / templado", "laminated / toughened glass"),
    ("efecto submarino", "submarining"),
    ("sistema de retención infantil (SRI)", "child restraint (child seat)"),
    ("latigazo cervical", "whiplash"),
    ("adherencia", "grip"),
    ("fuerza centrífuga / centrípeta", "centrifugal / centripetal force"),
    ("derrape · subviraje · sobreviraje", "skid · understeer · oversteer"),
    ("aquaplaning", "aquaplaning"),
    ("rodadura (en la nieve)", "rut (in snow)"),
    ("efecto pantalla", "screen (shielding) effect"),
]
