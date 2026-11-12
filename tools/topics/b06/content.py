# -*- coding: utf-8 -*-
"""Topic 6 content (carrying people and goods), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the learner's course (Tema 6: Transporte de personas y mercancías). The wording and
the figures are original; the rules come from the Reglamento General de Circulación (RD 1428/2003, arts. 9–16 and
114–119, and Anexo XI) and the Reglamento General de Vehículos (RD 2822/1998, Anexo IX on dimensions and Anexo XI on
vehicle plates), as amended up to RD 518/2026 (in force 1 October 2026).
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from .diagrams import child_seats, moto_passenger, max_lengths, overhang, overhang_signals, vehicle_plates


def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("Two halves. <b>People</b>: seats, seat belts, child seats (the <b>135 cm</b> line), exemptions, and passengers on motorcycles (<b>12 years</b>, or <b>7</b> with a parent). "
         "<b>Goods</b>: how to load, maximum dimensions, how far a load may stick out and how to signal it.",
         "Dos mitades. <b>Personas</b>: plazas, cinturón, sistemas de retención infantil (la línea de <b>135 cm</b>), exenciones y pasajeros de motocicleta (<b>12 años</b>, o <b>7</b> con su padre o madre). "
         "<b>Mercancías</b>: cómo cargar, dimensiones máximas, cuánto puede sobresalir la carga y cómo se señaliza."),
        ("The last part is the list of <b>V signals</b> carried by vehicles (V-1 to V-27). The exam asks what each one means and where it goes.",
         "La última parte es la lista de <b>señales V</b> de los vehículos (V-1 a V-27). El examen pregunta qué indica cada una y dónde se coloca."),
        ("The sections follow the order of your course’s Topic 6. Spanish exam terms are in <i>italics</i> in the English text, and a glossary closes the topic.",
         "Los apartados siguen el orden del Tema 6 de tu curso. Al final hay un glosario español–inglés."),
    ]))

    # ---------------------------------------------------------------- 1. carrying people
    B.append(H2("1", "Carrying people", "Transporte de personas"))
    B.append(TABLE(
        [T("Rule", "Norma"), T("Detail", "Detalle")],
        [
            [T("<b>How</b>", "<b>Cómo</b>"), T("Loading a vehicle or carrying people, goods or things in any way other than the regulated one is <b>forbidden</b>.",
                                                "Se <b>prohíbe</b> cargar los vehículos o transportar personas, mercancías o cosas de forma distinta a la reglamentaria.")],
            [T("<b>How many</b>", "<b>Cuántos</b>"), T("Never <b>more people than authorised seats</b>. A <b>child takes a seat</b> just like an adult.",
                                                       "Nunca <b>más personas que plazas autorizadas</b>. <b>Un niño ocupa una plaza</b> igual que un adulto.")],
            [T("<b>Weight</b>", "<b>Peso</b>"), T("Never above the vehicle’s <b>MMA</b>: count the people and their luggage.", "En ningún caso se supera la <b>MMA</b>: hay que contar el peso de las personas y su equipaje.")],
            [T("<b>Where to check</b>", "<b>Dónde se consulta</b>"), T("Seats and MMA are in the <b>vehicle inspection card</b> (<i>tarjeta de inspección técnica</i>) or the <b>registration certificate</b> (<i>permiso de circulación</i>).",
                                                                        "Las plazas y la MMA figuran en la <b>tarjeta de inspección técnica</b> o en el <b>permiso de circulación</b>.")],
            [T("<b>Where people sit</b>", "<b>Emplazamiento</b>"),
             T("Only in the places made and fitted for them. In goods vehicles, people may travel in the <b>load area</b> only with <b>authorisation</b> and the safety conditions it sets. "
               "Vehicles allowed to carry <b>people and load together</b> need a <b>protection</b> so the load cannot hinder or hurt the occupants if it is thrown forward.",
               "Solo en el lugar destinado y acondicionado para ellas. En vehículos de mercancías pueden viajar personas en la <b>zona de carga</b> solo con <b>autorización</b> y en las condiciones de seguridad que fije. "
               "Los vehículos autorizados a llevar <b>personas y carga a la vez</b> necesitan una <b>protección</b> para que la carga no estorbe ni dañe a los ocupantes si sale proyectada.")],
        ],
        widths=["22%", "78%"],
    ))
    B.append(P(
        "The <b>driver</b> must always be able to <b>control the vehicle</b>, keep the right <b>driving position</b>, make sure <b>passengers</b> keep theirs, "
        "and place <b>objects and animals</b> so that <b>nothing gets between the driver and them</b>.",
        "El <b>conductor</b> debe estar en todo momento en condiciones de <b>controlar su vehículo</b>, mantener la <b>posición adecuada</b>, cuidar de que la mantengan los <b>pasajeros</b> "
        "y colocar adecuadamente los <b>objetos y animales</b> para que <b>no haya interferencia</b> entre él y cualquiera de ellos."))

    B.append(H3("1.1 Seat belts and child seats", "1.1 Obligaciones de los ocupantes"))
    B.append(P(
        "The <b>driver and every occupant</b> wear an approved <b>seat belt</b>, properly fastened, on <b>urban and interurban</b> roads alike (unless the vehicle has none fitted). "
        "Children <b>135 cm tall or less</b> must use an <b>approved child seat</b> (<i>sistema de retención infantil</i>, SRI) suited to their <b>height and weight</b>, following the maker’s instructions.",
        "El <b>conductor y los ocupantes</b> usan, debidamente abrochado, el <b>cinturón de seguridad</b> homologado, tanto en vías <b>urbanas como interurbanas</b> (salvo que el vehículo no lo tenga instalado). "
        "Los menores de <b>estatura igual o inferior a 135 cm</b> deben usar <b>sistemas de retención infantil homologados</b> adaptados a su <b>talla y peso</b>, según las instrucciones del fabricante."))
    B.append(FIG(child_seats, "Under 135 cm: child seat in the back. A rear-facing seat in front is only allowed with the frontal airbag switched off.",
                 "Menos de 135 cm: sistema de retención detrás. Una silla a contramarcha delante solo se permite con el airbag frontal desactivado."))
    B.append(TABLE(
        [T("Vehicles up to 9 seats (driver included)", "Vehículos de hasta 9 plazas (incluido el conductor)")],
        [
            [T("Children up to 135 cm travel in the <b>rear seats</b>, except when: the vehicle <b>has no rear seats</b>; all rear seats are <b>taken by other such children</b>; "
               "or <b>not all the child seats fit</b> in the back.",
               "Los menores de hasta 135 cm van en los <b>asientos traseros</b>, salvo que: el vehículo <b>no tenga asientos traseros</b>; todos estén <b>ocupados por otros menores de las mismas características</b>; "
               "o <b>no sea posible instalar</b> detrás todos los sistemas.")],
            [T("If they sit in front and there is a <b>frontal airbag</b>, a <b>rear-facing</b> child seat is allowed <b>only with the airbag switched off</b>.",
               "Si ocupan los asientos delanteros y hay <b>airbag frontal</b>, solo pueden usar sistemas <b>orientados hacia atrás</b> si el <b>airbag está desactivado</b>.")],
        ],
    ))
    B.append(BOX("key", "Vehicles for people with more than 9 seats", "Vehículos de personas de más de nueve plazas", [
        ("Passengers are <b>told</b> they must wear belts or child seats, by the driver, the guide or the group leader, by audiovisual means, notices or pictograms.",
         "Se <b>informa</b> a los pasajeros de la obligación de llevar el cinturón o el sistema de retención: el conductor, el guía o el responsable del grupo, por medios audiovisuales, letreros o pictogramas."),
        ("Children <b>over 3</b> and up to <b>135 cm</b> use approved child seats suited to their size; <b>under-3s are excluded</b>. Without such seats, they use the <b>seat belt</b> if it suits their size.",
         "Los menores <b>de más de tres años</b> y hasta <b>135 cm</b> usan sistemas homologados adaptados a su talla y peso (<b>excluidos los menores de tres años</b>). Si no los hay, el <b>cinturón</b>, si es adecuado a su talla y peso."),
    ]))

    B.append(H3("1.2 Exemptions", "1.2 Exenciones"))
    B.append(TABLE(
        [T("Not required to wear a belt or restraint", "No están obligados al cinturón o sistema de retención")],
        [
            [T("Drivers while <b>reversing or parking</b>.", "Los conductores que hagan <b>marcha atrás o estacionen</b>.")],
            [T("People with a <b>medical exemption certificate</b> (serious medical reasons or disability) from any EU state; they show it to agents on request.",
               "Las personas con <b>certificado de exención por razones médicas graves o discapacidad</b> de cualquier Estado de la UE; deben mostrarlo a los agentes si lo piden.")],
            [T("Drivers and passengers of <b>emergency vehicles on service, in town</b> (out of town they must wear it).",
               "Conductores y pasajeros de <b>vehículos en servicio de urgencia, en poblado</b> (en autopistas, autovías y convencionales es obligatorio).")],
            [T("Passengers of <b>medical-care ambulances</b> on urgent service who sit in the patient area to <b>treat the patient</b> on the way, on <b>any road</b>.",
               "Los pasajeros de <b>ambulancias asistenciales</b> en servicio de urgencia que ocupen el habitáculo del paciente para <b>prestarle asistencia</b> en ruta, en <b>todo tipo de vías</b>.")],
            [T("<b>Taxis</b> in urban traffic may carry passengers <b>under 135 cm without a child seat</b>, as long as they sit in a <b>rear seat</b>.",
               "Los <b>taxis</b> en tráfico urbano pueden llevar a personas de <b>menos de 135 cm sin sistema de retención</b>, siempre que ocupen un <b>asiento trasero</b>.")],
        ],
    ))
    B.append(BOX("trap", "Who is not exempt", "Quién no está exento", [
        ("<b>Pregnant women</b> must wear the seat belt; approved accessories can add protection for mother and baby.",
         "Las <b>embarazadas</b> deben usar el cinturón; existen accesorios homologados que aumentan la seguridad de la madre y el bebé."),
        ("<b>Since 1 October 2026</b> the old in-town exemptions for <b>taxi drivers</b>, drivers making <b>deliveries</b> and <b>driving instructors</b> are gone: they wear the belt too.",
         "<b>Desde el 1 de octubre de 2026</b> desaparecen las antiguas exenciones en poblado para <b>taxistas</b>, conductores de <b>reparto</b> y <b>profesores de autoescuela</b>: también llevan cinturón."),
    ]))

    B.append(H3("1.3 Motorcycles, mopeds and cycles", "1.3 Motocicletas, ciclomotores y ciclos"))
    B.append(FIG(moto_passenger, "Besides the rider (and the sidecar passenger, if any), at most one passenger, and only on these conditions.",
                 "Además del conductor (y del ocupante del sidecar, en su caso), como máximo un pasajero, y solo con estas condiciones."))
    B.append(E(
        "Cycles", "Ciclos",
        "Cycles built for <b>one person</b> may carry children <b>up to 22 kg</b> who can sit on their own, in <b>extra seats</b> that meet the technical specifications. "
        "Approved <b>trailers</b> or similar may carry people, <b>animals up to 15 kg</b> or load; on <b>interurban roads</b>, only <b>by day</b> and with good visibility. "
        "The cyclist must be an <b>adult</b> to carry load or passengers.",
        "Los ciclos que por construcción solo pueden llevar <b>una persona</b> pueden transportar menores de <b>hasta 22 kg</b>, capaces de sentarse solos, en <b>asientos adicionales</b> que cumplan las especificaciones técnicas. "
        "Pueden usar <b>remolques</b> u otros elementos homologados para personas, <b>animales de hasta 15 kg</b> o carga; en <b>vía interurbana</b>, solo <b>de día</b> y sin visibilidad reducida. "
        "Para llevar carga o pasajeros, el conductor debe ser <b>mayor de edad</b>.",
        pills_=[T("children ≤ 22 kg", "menores ≤ 22 kg"), T("animals ≤ 15 kg", "animales ≤ 15 kg")]))
    B.append(BOX("key", "The helmet", "El casco", [
        ("An approved helmet (<b>UNECE R22</b>), properly fastened, for <b>riders and passengers</b> of motorcycles (with or without sidecar), three-wheelers and quadricycles, mopeds and special <b>quads</b>.",
         "Casco homologado (<b>Reglamento UNECE R22</b>) correctamente abrochado para <b>conductores y pasajeros</b> de motocicletas (con o sin sidecar), vehículos de tres ruedas y cuadriciclos, ciclomotores y vehículos especiales tipo <b>quad</b>."),
        ("Since <b>1 October 2026</b> they also need <b>protective gloves</b> on interurban roads and <b>closed shoes</b> on every road (Topic 10).",
         "Desde el <b>1 de octubre de 2026</b> necesitan además <b>guantes de protección</b> en vías interurbanas y <b>calzado cerrado</b> en todas las vías (Tema 10)."),
        ("If the vehicle has a <b>protective structure</b> and seat belts, and its inspection card says so, occupants wear the <b>seat belt instead</b> of the helmet (and of the gloves and shoes).",
         "Si el vehículo tiene <b>estructura de autoprotección</b> y cinturones, y así consta en su tarjeta ITV, sus ocupantes quedan exentos del casco (y de guantes y calzado) y deben usar el <b>cinturón</b>."),
        ("<b>Cyclists</b>: compulsory for <b>under-16s</b> everywhere and for <b>everyone on interurban roads</b>; also for anyone cycling <b>for work</b> in town.",
         "<b>Ciclistas</b>: obligatorio para los <b>menores de 16 años</b> en todas las vías y para <b>todos en vías interurbanas</b>; también para quien circula en bicicleta por su <b>actividad profesional</b> en vías urbanas."),
    ]))

    # ---------------------------------------------------------------- 2. carrying goods
    B.append(H2("2", "Carrying goods", "Transporte de mercancías"))
    B.append(H3("2.1 Loading and unloading", "2.1 Operaciones de carga y descarga"))
    B.append(P(
        "As a rule, load and unload <b>off the road</b>. When it must be done on the road: on the side <b>nearest the edge</b>, respecting the <b>stopping and parking</b> rules (and local hours and places in towns), "
        "<b>never leaving goods</b> on the carriageway, shoulder or pedestrian areas, and <b>quickly</b>, avoiding danger, noise and nuisance.",
        "Como norma general, la carga y descarga se hace <b>fuera de la vía</b>. Si es imprescindible hacerla en ella: por el lado <b>más próximo al borde</b> de la calzada, respetando las normas de <b>parada y estacionamiento</b> (y en poblado, las de horas y lugares), "
        "<b>sin depositar mercancía</b> en la calzada, el arcén ni zonas peatonales, y <b>con rapidez</b>, evitando peligros, ruidos y molestias."))
    B.append(H3("2.2 How to place the load", "2.2 Cómo se coloca la carga"))
    B.append(TABLE(
        [T("The load and its fastenings must not…", "La carga y sus accesorios no pueden…"), T("In a car", "En un turismo")],
        [
            [T("Make the vehicle <b>unstable</b> · <b>hide lights</b>, plates or badges and the driver’s arm signals · <b>drag, fall or shift</b> dangerously · "
               "cause avoidable <b>noise or dust</b> (dusty or loose loads must be <b>fully covered</b>).",
               "<b>Comprometer la estabilidad</b> · <b>ocultar los dispositivos luminosos</b>, placas o distintivos y las advertencias del conductor · <b>arrastrar, caer o desplazarse</b> peligrosamente · "
               "producir <b>ruido, polvo</b> u otras molestias evitables (si produce polvo o puede caer, debe <b>cubrirse total y eficazmente</b>)."),
             T("In the <b>boot</b>, weight spread <b>evenly</b>. In the cabin only <b>small, light</b> things (they can fly and hurt someone). "
               "Heavy, bulky things on the <b>roof rack</b> can make the car unstable, even <b>overturn</b> it, and raise fuel use.",
               "En el <b>maletero</b>, con el peso repartido <b>uniformemente</b>. En el habitáculo, solo objetos de <b>poco peso y volumen</b> (pueden salir despedidos). "
               "Objetos pesados y voluminosos en la <b>baca</b> comprometen la estabilidad, pueden hacerlo <b>volcar</b> y aumentan el consumo.")],
        ],
        widths=["55%", "45%"],
    ))
    B.append(H3("2.3 Maximum dimensions, load included", "2.3 Dimensiones máximas con la carga"))
    B.append(P("The vehicle and its load may <b>never exceed</b> the dimensions set for the <b>vehicle</b> or for the <b>road</b> it is on.",
               "La longitud, anchura y altura del vehículo y su carga <b>en ningún caso exceden</b> las fijadas para el <b>vehículo</b> o para la <b>vía</b> por la que circula."))
    B.append(FIG(max_lengths, "Maximum lengths. Anything over 12 m carries the V-6 “long vehicle” plate at the rear.",
                 "Longitudes máximas. Todo lo que supere 12 m lleva detrás la señal V-6 «Vehículo largo»."))
    B.append(TABLE(
        [T("Dimension", "Dimensión"), T("General", "General"), T("Exceptions", "Excepciones")],
        [
            [T("<b>Length</b>", "<b>Longitud</b>"), T("<b>12 m</b> (motor vehicles and trailers)", "<b>12 m</b> (vehículos de motor y remolques)"),
             T("Buses 13.50 m (2 axles) / 15 m (3+) · semitrailers 14.04 m · articulated 16.50 m · road trains 18.75 m",
               "Autobuses 13,50 m (2 ejes) / 15 m (3 o más) · semirremolques 14,04 m · articulados 16,50 m · trenes de carretera 18,75 m")],
            [T("<b>Width</b>", "<b>Anchura</b>"), T("<b>2.55 m</b>", "<b>2,55 m</b>"),
             T("2.60 m: refrigerated (isothermal) bodies and buses for moving prisoners", "2,60 m: superestructuras isotermas y autobuses para el traslado de presos")],
            [T("<b>Height</b>", "<b>Altura</b>"), T("<b>4 m</b>", "<b>4 m</b>"),
             T("4.20 m urban buses · 4.50 m car transporters, crane vehicles and closed-container carriers", "4,20 m autobuses urbanos · 4,50 m portavehículos, vehículos grúa y transporte de contenedores cerrados")],
        ],
        widths=["16%", "28%", "56%"],
        cls="small",
    ))
    B.append(E(
        "V-6 “Long vehicle”", "V-6 «Vehículo largo»",
        "A vehicle or combination <b>longer than 12 m</b> carries the V-6: a <b>yellow reflective</b> rectangle with a <b>fluorescent red</b> border, at the <b>rear, centred</b>, "
        "or two plates placed symmetrically on both sides, as close to the edges as possible.",
        "Los vehículos o conjuntos de <b>más de 12 m</b> llevan la V-6: placa rectangular de fondo <b>amarillo reflectante</b> y borde <b>rojo fluorescente</b>, en la <b>parte posterior y centrada</b>, "
        "o dos placas simétricas a ambos lados del eje, lo más cerca posible de los bordes.",
        tip=("Road signs can also limit length, width and height: red circles with the figure in metres.",
             "La vía también puede limitar la longitud, anchura y altura: señales circulares rojas con la cifra en metros.")))
    B.append(H3("2.4 How far the load may stick out", "2.4 Cuánto puede sobresalir la carga"))
    B.append(FIG(overhang, "The rules depend on whether the vehicle is made only for goods.",
                 "Las normas dependen de si el vehículo está destinado exclusivamente al transporte de mercancías."))
    B.append(TABLE(
        [T("Vehicle", "Vehículo"), T("Overhang allowed", "Puede sobresalir")],
        [
            [T("<b>Not only for goods</b> (cars, mixed vehicles, motorhomes…)", "<b>No destinados solo a mercancías</b> (turismos, mixtos, autocaravanas…)"),
             T("At the <b>rear</b>: up to <b>10 %</b> of the vehicle’s length if the load is <b>divisible</b>, <b>15 %</b> if <b>indivisible</b>. On top if the rules are met. <b>Never in front or at the sides.</b>",
               "Por <b>detrás</b>: hasta el <b>10 %</b> de la longitud del vehículo si la carga es <b>divisible</b>, el <b>15 %</b> si es <b>indivisible</b>. Por arriba si se cumplen las normas. <b>Nunca por delante ni por los laterales.</b>")],
            [T("<b>Only for goods</b> (lorries, vans…)", "<b>Destinados solo a mercancías</b> (camiones, furgones…)"),
             T("As a rule, <b>nothing</b> beyond the vehicle’s outline. Exceptionally, a well-stowed <b>indivisible</b> load (beams, posts, pipes): "
               "vehicle <b>up to 5 m</b>: <b>⅓</b> of its length in front and ⅓ behind; <b>over 5 m</b>: <b>2 m in front, 3 m behind</b>. "
               "Sideways, if the load’s smallest side is wider than the vehicle: <b>0.40 m each side</b>, total width ≤ <b>2.55 m</b>.",
               "Como norma, <b>nada</b> fuera de la proyección en planta. Excepcionalmente, carga <b>indivisible</b> bien estibada (vigas, postes, tubos): "
               "vehículos de <b>hasta 5 m</b>: <b>⅓</b> de su longitud delante y otro ⅓ detrás; de <b>más de 5 m</b>: <b>2 m delante y 3 m detrás</b>. "
               "A lo ancho, si la dimensión menor de la carga supera el ancho del vehículo: <b>0,40 m por cada lado</b>, anchura total ≤ <b>2,55 m</b>.")],
            [T("<b>Under 1 m wide</b> (motorcycles, mopeds…)", "<b>De menos de 1 m de ancho</b> (motos, ciclomotores…)"),
             T("<b>0.25 m</b> at the rear, <b>0.50 m</b> each side of the centre line, <b>nothing in front</b>.", "<b>0,25 m</b> por detrás, <b>0,50 m</b> a cada lado del eje longitudinal, <b>nada por delante</b>.")],
        ],
        widths=["30%", "70%"],
        cls="small",
    ))
    B.append(P("An indivisible load that <b>inevitably</b> exceeds these limits needs a <b>complementary permit</b> and must follow its conditions.",
               "Las cargas indivisibles que <b>inevitablemente</b> rebasen estos límites necesitan una <b>autorización complementaria</b> de circulación y cumplir sus condiciones."))
    B.append(H3("2.5 Signalling a load that sticks out", "2.5 Señalizar la carga que sobresale"))
    B.append(P("Take precautions so it cannot hurt or endanger anyone: <b>protect the end</b> that sticks out to soften any knock, and <b>signal it</b>:",
               "Hay que evitar daños o peligros: <b>resguardar la extremidad saliente</b> para aminorar roces o choques y <b>señalizarla</b>:"))
    B.append(FIG(overhang_signals, "The V-20 panel always marks the rear end; at night a white light goes in front and a red light behind.",
                 "El panel V-20 marca siempre el extremo trasero; de noche se añade una luz blanca delante y una roja detrás."))
    B.append(TABLE(
        [T("When", "Cuándo"), T("Front", "Delante"), T("Rear", "Detrás")],
        [
            [T("<b>By day</b>, clear weather", "<b>De día</b> y con tiempo claro"), T("Not needed", "No es necesario"),
             T("<b>1 or 2 V-20 panels</b>; 2 when the load fills the whole rear width, one at each end, stripes forming an inverted V", "<b>1 o 2 paneles V-20</b>; 2 si la carga ocupa toda la anchura trasera, uno en cada extremo, con franjas en V invertida")],
            [T("<b>Sunset to sunrise</b>, or poor visibility", "<b>Entre la puesta y la salida del sol</b> o con poca visibilidad"), T("A <b>white light</b>", "Una <b>luz blanca</b>"),
             T("The panel(s) <b>plus a red light</b>", "El panel o paneles <b>y una luz roja</b>")],
            [T("Load sticking out <b>sideways</b> more than <b>0.40 m</b> beyond the position lights", "Carga que sobresale <b>lateralmente</b> más de <b>0,40 m</b> del borde de las luces de posición"),
             T("White light + white reflector", "Luz blanca + catadióptrico blanco"), T("Red light + red reflector", "Luz roja + catadióptrico rojo")],
        ],
        widths=["34%", "24%", "42%"],
        cls="small",
    ))
    B.append(P("Vehicles <b>under 1 m wide</b> do not need to signal a load sticking out at the rear.",
               "En los vehículos de <b>anchura inferior a 1 m</b> no es necesario señalizar la carga que sobresale por detrás."))
    B.append(H3("2.6 Special cases", "2.6 Casos especiales"))
    B.append(E(
        "Motorcycles, three-wheelers and mopeds towing", "Motocicletas, vehículos de tres ruedas y ciclomotores con remolque",
        "They may tow a trailer or semitrailer weighing <b>no more than 50 %</b> of the towing vehicle’s <b>unladen</b> mass, if: they travel <b>by day</b> with good visibility; "
        "their speed is <b>10 % lower</b> than their generic out-of-town limits; and <b>nobody rides</b> in the trailer. In towns, local bylaws apply.",
        "Pueden arrastrar un remolque o semirremolque cuya masa <b>no supere el 50 %</b> de la <b>masa en vacío</b> del vehículo tractor, si: circulan <b>de día</b> y sin visibilidad reducida; "
        "reducen un <b>10 %</b> las velocidades genéricas fuera de poblado; y <b>no transportan personas</b> en el remolque. En poblado, lo que digan las ordenanzas municipales.",
        pills_=[T("≤ 50 % unladen mass", "≤ 50 % de la masa en vacío"), T("−10 % speed", "−10 % de velocidad")]))
    B.append(E(
        "Bicycles and other cycles", "Bicicletas y demás ciclos",
        "May carry load and passengers <b>if the rider is an adult</b>, placed so they cannot drag, fall or shift, make the cycle unstable, or hide its lights and reflectors.",
        "Pueden transportar carga y pasajeros <b>si el conductor es mayor de edad</b>, de forma que no puedan arrastrar, caer o desplazarse, comprometer la estabilidad ni ocultar el alumbrado o la señalización."))

    # ---------------------------------------------------------------- 3. doors
    B.append(H2("3", "Doors", "Las puertas"))
    B.append(P(
        "As a rule, get in and out by the door on the side <b>nearest the edge of the road</b>. It is <b>forbidden</b> to drive with doors <b>open</b>, to open them <b>before the vehicle has fully stopped</b>, "
        "and to open them or get out <b>without first checking</b> that it endangers or hinders nobody, above all <b>riders of two-wheelers</b>.",
        "Como norma general, se entra y se sale por la puerta del lado <b>más cercano al borde de la vía</b>. Se <b>prohíbe</b> llevar las puertas <b>abiertas</b>, abrirlas <b>antes de la completa inmovilización</b> "
        "y abrirlas o apearse <b>sin asegurarse</b> de que no hay peligro ni entorpecimiento para otros usuarios, especialmente los <b>conductores de vehículos de dos ruedas</b>.",
        ))

    # ---------------------------------------------------------------- 4. vehicle signals
    B.append(H2("4", "Signals on vehicles", "Señales en los vehículos"))
    B.append(P("These plates, lights and badges tell other road users something about the vehicle, its service, its load or its driver, so they can take precautions.",
               "Estas señales informan a los demás de circunstancias del vehículo, del servicio que presta, de su carga o de su conductor, para que adopten las precauciones necesarias."))
    B.append(FIG(vehicle_plates, "Simplified drawings of ten of the plates and badges.", "Dibujos simplificados de diez de las señales."))
    B.append(TABLE(
        [T("Signal", "Señal"), T("What it means · where it goes", "Qué indica · dónde se coloca")],
        [
            [T("<b>V-1</b> Priority vehicle", "<b>V-1</b> Vehículo prioritario"), T("Police, fire, civil protection and rescue, or medical assistance on <b>urgent service</b>. One or more <b>blue</b> lights visible all round from <b>50 m</b>.",
                                                                                  "Policía, extinción de incendios, protección civil y salvamento o asistencia sanitaria en <b>servicio urgente</b>. Luz o luces <b>azules</b> visibles en todas direcciones a <b>50 m</b>.")],
            [T("<b>V-2</b> Vehicle-obstacle", "<b>V-2</b> Vehículo-obstáculo en la vía"), T("<b>Amber</b> light(s): a vehicle working on or by the road, <b>stopped or parked</b> or going at <b>≤ 40 km/h</b>; also special transport and its escorts, escorts of sports events, cycling marches and military columns. May add red-and-white reflective contour strips.",
                                                                                        "Luz o luces <b>amarillo auto</b>: vehículo que presta un servicio o trabajo, <b>parado o estacionado</b> o a <b>≤ 40 km/h</b>; también transporte especial y acompañamientos, pruebas deportivas, marchas ciclistas y columnas militares. Puede añadir distintivos de franjas rojas y blancas.")],
            [T("<b>V-3</b> Police, non-urgent", "<b>V-3</b> Policía en servicio no urgente"), T("Name of the force on the sides; may have reflective contour lines and position lights in the V-1 colour, and a lit sign.",
                                                                                            "Rotulación del Cuerpo en los costados; puede llevar líneas reflectantes y alumbrado del color de la V-1 y un cartel iluminado.")],
            [T("<b>V-4</b> Speed limit", "<b>V-4</b> Limitación de velocidad"), T("The vehicle may not exceed the figure in km/h. At the <b>rear</b>: certain drivers, special vehicles and combinations, vehicles with a special permit.",
                                                                                 "El vehículo no debe superar la cifra en km/h. En la <b>parte trasera</b>: determinados conductores, vehículos especiales y sus conjuntos, vehículos con autorización especial.")],
            [T("<b>V-5</b> Slow vehicle", "<b>V-5</b> Vehículo lento"), T("By construction it <b>cannot exceed 40 km/h</b> (orange triangle with red border).", "Por construcción <b>no puede superar 40 km/h</b> (triángulo naranja de borde rojo).")],
            [T("<b>V-6</b> Long vehicle", "<b>V-6</b> Vehículo largo"), T("Longer than <b>12 m</b>.", "Longitud superior a <b>12 m</b>.")],
            [T("<b>V-7</b> Spanish nationality", "<b>V-7</b> Nacionalidad española"), T("Registered in Spain. Not needed in other EU states with EU plates bearing the E.", "Matriculado en España. No hace falta en otros Estados de la UE con placas de la UE con la E.")],
            [T("<b>V-8</b> Foreign nationality", "<b>V-8</b> Nacionalidad extranjera"), T("Registered abroad; compulsory in Spain unless the plates show the EU flag and the country letters.", "Matriculado en el extranjero; obligatorio en España salvo placas con la bandera de la UE y las siglas del Estado.")],
            [T("<b>V-9</b> Public service", "<b>V-9</b> Servicio público"), T("“SP”, front and rear, next to the number plates.", "«SP», delante y detrás, junto a las placas de matrícula.")],
            [T("<b>V-10</b> School transport", "<b>V-10</b> Transporte escolar"), T("Front and rear.", "Delante y detrás.")],
            [T("<b>V-11</b> Dangerous goods", "<b>V-11</b> Mercancías peligrosas"), T("Orange plate, front and rear.", "Placa naranja, delante y detrás.")],
            [T("<b>V-12</b> Test or research plate", "<b>V-12</b> Placa de ensayo o investigación"), T("Front and rear.", "Delante y detrás.")],
            [T("<b>V-13</b> Novice driver", "<b>V-13</b> Conductor novel"), T("Licence held for <b>less than a year</b>. At the <b>rear left</b>, visible. 19.5 × 15 cm (13 × 10 cm on motorcycles, reduced-mobility vehicles, three-wheelers and quadricycles).",
                                                                            "Permiso con <b>menos de un año</b> de antigüedad. En la <b>parte posterior izquierda</b>, visible. 19,5 × 15 cm (13 × 10 cm en motos, vehículos de movilidad reducida, tres ruedas y cuadriciclos).")],
            [T("<b>V-14</b> Driving lessons", "<b>V-14</b> Aprendizaje de la conducción"), T("The vehicle is being used for <b>lessons or driving tests</b>.", "El vehículo circula en función del <b>aprendizaje o de las pruebas</b> de aptitud.")],
            [T("<b>V-15</b> Disabled driver", "<b>V-15</b> Minusválido"), T("Driver with reduced mobility who may benefit from the facilities granted. Front and rear.", "Conductor con movilidad reducida que puede beneficiarse de las facilidades concedidas. Delante y detrás.")],
            [T("<b>V-16</b> Warning device", "<b>V-16</b> Preseñalización de peligro"), T("The vehicle is <b>immobilised on the carriageway</b>, or its load has fallen onto it.", "El vehículo está <b>inmovilizado en la calzada</b> o su carga ha caído en ella.")],
            [T("<b>V-17</b> “LIBRE” light", "<b>V-17</b> Alumbrado de LIBRE"), T("A taxi <b>available for hire</b>.", "Taxi <b>en condiciones de ser alquilado</b>.")],
            [T("<b>V-18</b> Taximeter light", "<b>V-18</b> Alumbrado de taxímetro"), T("Lights up the meter once the fare is running.", "Ilumina el taxímetro al producirse la bajada de bandera.")],
            [T("<b>V-19</b> ITV badge", "<b>V-19</b> Distintivo de ITV"), T("Passed the periodic <b>inspection</b>; shows when the next one is due.", "Ha superado la <b>inspección técnica periódica</b>; indica la fecha de la próxima.")],
            [T("<b>V-20</b> Overhanging load panel", "<b>V-20</b> Panel de carga que sobresale"), T("The load sticks out <b>at the rear</b>.", "La carga <b>sobresale por detrás</b>.")],
            [T("<b>V-21</b> Special-transport escort sign", "<b>V-21</b> Cartel de acompañamiento de transporte especial"), T("A special vehicle or special transport is <b>close by</b> (“ESPECIAL”).", "Circulación <b>próxima</b> de un vehículo especial o en régimen de transporte especial («ESPECIAL»).")],
            [T("<b>V-22</b> Cyclist escort sign", "<b>V-22</b> Cartel de acompañamiento de ciclistas"), T("<b>Cyclists</b> close by. Carried at all times by vehicles escorting cyclists; may be combined with the V-2.",
                                                                                                         "Circulación próxima de <b>ciclistas</b>. La llevan siempre los vehículos que solo acompañan a ciclistas; puede ir con la V-2 formando un conjunto.")],
            [T("<b>V-23</b> Goods vehicle marking", "<b>V-23</b> Distintivo de vehículos de mercancías"), T("<b>Reflective</b> contour marking on the rear and sides of long, heavy vehicles and their trailers.", "Marcado <b>reflectante</b> en la parte trasera y lateral de vehículos largos y pesados y sus remolques.")],
            [T("<b>V-24</b> Roadside assistance", "<b>V-24</b> Vehículo de auxilio en vías públicas"), T("Plate at the front or rear of the recovery vehicle; may optionally use a special acoustic signal.", "Placa en la parte frontal o posterior del vehículo de auxilio; opcionalmente, señal acústica especial.")],
            [T("<b>V-25</b> Environmental label", "<b>V-25</b> Distintivo ambiental"), T("<b>0 emisiones, ECO, C or B</b>. Lower <b>right</b> corner of the windscreen, inside; if none, somewhere clearly visible.", "<b>0 emisiones, ECO, C o B</b>. Ángulo inferior <b>derecho</b> del parabrisas, por dentro; si no hay parabrisas, en sitio bien visible.")],
            [T("<b>V-26</b> Shared-use badge", "<b>V-26</b> Distintivo de uso compartido"), T("Self-drive rental car used one after another by many users within a set zone. Same place as the V-25.", "Vehículo de alquiler sin conductor de uso concatenado por usuarios indeterminados en una zona delimitada. Mismo lugar que la V-25.")],
            [T("<b>V-27</b> Virtual triangle", "<b>V-27</b> Triángulo virtual"), T("Appears on the <b>dashboard</b> of <b>connected</b> vehicles to warn of a nearby danger reported to the DGT platform. <b>Voluntary</b>.",
                                                                               "Aparece en el sistema de a bordo de vehículos <b>conectados</b> para advertir de un peligro próximo comunicado a la plataforma de la DGT. <b>Voluntaria</b>.")],
            [T("<b>VEH 21/05</b> Blind-spot sticker", "<b>VEH 21/05</b> Advertencia de ángulos muertos"), T("<b>Voluntary</b> stickers warning vulnerable users of the blind spots of large vehicles: <b>three</b> per vehicle (one each side within the first metre, one at the rear right; refuse trucks: two at the rear).",
                                                                                                    "Señal adhesiva <b>voluntaria</b> que advierte a los usuarios vulnerables de los ángulos muertos de vehículos grandes: <b>tres</b> por vehículo (una a cada lado en el primer metro y una detrás a la derecha; camiones de residuos: dos detrás).")],
        ],
        widths=["30%", "70%"],
        cls="small",
    ))

    # ---------------------------------------------------------------- 5. traps
    B.append(H2("5", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("A child counts as a <b>full seat</b>; the people and luggage count towards the <b>MMA</b>.", "Un niño ocupa <b>una plaza</b> completa; las personas y el equipaje cuentan para la <b>MMA</b>."),
        ("The line is <b>135 cm</b> of height, not age. In buses (more than 9 seats) the rule starts <b>over 3 years old</b>.", "La línea son <b>135 cm</b> de estatura, no la edad. En autobuses (más de 9 plazas) la norma empieza en los <b>mayores de tres años</b>."),
        ("Rear-facing child seat in front only with the <b>airbag off</b>.", "Silla a contramarcha delante solo con el <b>airbag desactivado</b>."),
        ("Emergency vehicles are exempt from the belt <b>in town only</b>; patient-care ambulance staff on <b>any road</b>.", "Los vehículos de urgencia están exentos del cinturón <b>solo en poblado</b>; el personal sanitario de la ambulancia, en <b>cualquier vía</b>."),
        ("Pregnant women are <b>not</b> exempt. Taxi drivers, delivery drivers and instructors no longer are either.", "Las embarazadas <b>no</b> están exentas. Taxistas, repartidores y profesores de autoescuela tampoco ya."),
        ("Motorcycle passenger: <b>over 12</b>, or <b>over 7</b> with a parent, guardian or authorised adult riding; never between rider and handlebars.",
         "Pasajero de moto: <b>mayor de 12 años</b>, o <b>mayor de 7</b> si conduce su padre, madre, tutor o adulto autorizado; nunca entre el conductor y el manillar."),
        ("Cycles: children <b>≤ 22 kg</b> in extra seats; animals <b>≤ 15 kg</b> in trailers; out of town only by day.", "Ciclos: menores <b>≤ 22 kg</b> en asientos adicionales; animales <b>≤ 15 kg</b> en remolque; en interurbana, solo de día."),
        ("Cars: rear overhang <b>10 %</b> (divisible) or <b>15 %</b> (indivisible), never in front.", "Turismos: por detrás <b>10 %</b> (divisible) o <b>15 %</b> (indivisible), nunca por delante."),
        ("Goods vehicles over 5 m: <b>2 m in front, 3 m behind</b> (indivisible load only). Up to 5 m: <b>⅓ and ⅓</b>.", "Vehículos de mercancías de más de 5 m: <b>2 m delante, 3 m detrás</b> (solo carga indivisible). Hasta 5 m: <b>⅓ y ⅓</b>."),
        ("Overhang by day: rear panel only; at night add a <b>white light in front</b> and a <b>red light behind</b>.", "Carga saliente de día: solo el panel detrás; de noche, además <b>luz blanca delante</b> y <b>luz roja detrás</b>."),
        ("Motorcycle trailer: <b>≤ 50 % of the unladen mass</b>, by day, <b>−10 %</b> speed, nobody in it.", "Remolque de moto: <b>≤ 50 % de la masa en vacío</b>, de día, <b>−10 %</b> de velocidad y sin personas."),
        ("V-2 is <b>amber</b> (working vehicle, ≤ 40 km/h); V-1 is <b>blue</b> (priority).", "La V-2 es <b>amarilla</b> (vehículo trabajando, ≤ 40 km/h); la V-1 es <b>azul</b> (prioritario)."),
        ("V-5 = <b>can’t exceed 40 km/h by construction</b>; V-4 = a speed limit for this vehicle or driver.", "V-5 = <b>no puede superar 40 km/h por construcción</b>; V-4 = límite de velocidad de ese vehículo o conductor."),
        ("V-13 novice: rear <b>left</b>. V-25 label: windscreen lower <b>right</b>.", "V-13 novel: detrás a la <b>izquierda</b>. V-25: parabrisas, ángulo inferior <b>derecho</b>."),
        ("Get out on the side <b>nearest the kerb</b>; check for cyclists and motorcyclists before opening the door.", "Se sale por el lado <b>más cercano al borde</b>; comprobar ciclistas y motoristas antes de abrir la puerta."),
    ]))

    # ---------------------------------------------------------------- 6. key numbers
    B.append(H2("6", "Key numbers on one page", "Números clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Number", "Cifra")],
        [
            [T("Child seat needed", "Sistema de retención obligatorio"), T("height ≤ 135 cm", "estatura ≤ 135 cm")],
            [T("Rear seat rule", "Regla del asiento trasero"), T("vehicles up to 9 seats (driver included)", "vehículos de hasta 9 plazas (con el conductor)")],
            [T("Buses with more than 9 seats", "Autobuses de más de 9 plazas"), T("child seat from over 3 years to 135 cm", "sistema de retención de más de 3 años a 135 cm")],
            [T("Motorcycle passenger", "Pasajero de moto"), T("over 12 (over 7 with a parent or authorised adult)", "mayor de 12 (mayor de 7 con padre, madre o adulto autorizado)")],
            [T("Cycles", "Ciclos"), T("children ≤ 22 kg · animals ≤ 15 kg · adult rider", "menores ≤ 22 kg · animales ≤ 15 kg · conductor mayor de edad")],
            [T("Cyclist helmet", "Casco del ciclista"), T("under 16 everywhere; everyone on interurban roads", "menores de 16 en todas las vías; todos en interurbanas")],
            [T("Length", "Longitud"), T("12 m · bus 13.50 / 15 · semitrailer 14.04 · articulated 16.50 · road train 18.75", "12 m · autobús 13,50 / 15 · semirremolque 14,04 · articulado 16,50 · tren de carretera 18,75")],
            [T("Width / height", "Anchura / altura"), T("2.55 m (2.60) / 4 m (4.20, 4.50)", "2,55 m (2,60) / 4 m (4,20, 4,50)")],
            [T("Long vehicle plate V-6", "Señal V-6"), T("over 12 m", "más de 12 m")],
            [T("Overhang, cars", "Carga saliente, turismos"), T("rear 10 % divisible / 15 % indivisible", "detrás 10 % divisible / 15 % indivisible")],
            [T("Overhang, goods vehicles (indivisible)", "Carga saliente, mercancías (indivisible)"), T("≤ 5 m: ⅓ + ⅓ · &gt; 5 m: 2 m front + 3 m rear · 0.40 m each side, ≤ 2.55 m total", "≤ 5 m: ⅓ + ⅓ · &gt; 5 m: 2 m delante + 3 m detrás · 0,40 m por lado, ≤ 2,55 m en total")],
            [T("Overhang, vehicles under 1 m wide", "Carga saliente, vehículos de menos de 1 m"), T("0.25 m rear · 0.50 m each side · 0 front", "0,25 m detrás · 0,50 m a cada lado · 0 delante")],
            [T("Side overhang needing lights", "Carga lateral que exige luces"), T("more than 0.40 m beyond the position lights", "más de 0,40 m del borde de las luces de posición")],
            [T("Motorcycle trailer", "Remolque de moto"), T("≤ 50 % unladen mass · −10 % speed", "≤ 50 % de la masa en vacío · −10 % de velocidad")],
            [T("V-1 light / V-2 light", "Luz V-1 / luz V-2"), T("blue, visible at 50 m / amber, ≤ 40 km/h", "azul, visible a 50 m / amarillo auto, ≤ 40 km/h")],
            [T("V-13 novice plate", "Placa V-13"), T("licence &lt; 1 year · 19.5 × 15 cm (13 × 10 cm)", "permiso &lt; 1 año · 19,5 × 15 cm (13 × 10 cm)")],
        ],
        widths=["38%", "62%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
# The PDF self-test reuses twelve questions from the page's question bank. The correct option is placed in
# turn at A, B and C so the answer key is not always the same letter.
QUIZ_IDS = ["pp2", "bt2", "bt5", "ex3", "mo2", "hm4", "ld3", "dm2", "oh3", "ls2", "dr1", "vp4"]


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
    ("Reglamento General de Circulación (RD 1428/2003): carrying people and goods, seat belts and helmets — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2003-23514"),
    ("Reglamento General de Vehículos (RD 2822/1998): maximum dimensions and the V signals (Anexo XI) — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-1999-1826"),
    ("Real Decreto 518/2026 (reform of the Reglamento, in force 1 October 2026)", "https://www.boe.es/eli/es/rd/2026/06/24/518"),
    ("La Moncloa, 30-09-2026: the reform comes into force (seat belts for taxis, goods vehicles and driving schools; cyclist helmets)",
     "https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/interior/paginas/2026/300926-reforma-reglamento-circulacion.aspx"),
    ("Motor16: the seat-belt exemptions removed from 1 October 2026", "https://www.motor16.com/las-ultimas-noticias/cinturon-obligatorio-sin-exenciones-taxistas/"),
]

GLOSSARY = [
    ("plaza · masa máxima autorizada (MMA)", "seat · maximum authorised mass"),
    ("tarjeta de inspección técnica · permiso de circulación", "vehicle inspection card · registration certificate"),
    ("cinturón de seguridad", "seat belt"),
    ("sistema de retención infantil (SRI)", "child restraint (child seat)"),
    ("orientado hacia atrás (a contramarcha)", "rear-facing"),
    ("airbag frontal desactivado", "frontal airbag switched off"),
    ("certificado de exención", "exemption certificate"),
    ("ambulancia asistencial", "patient-care ambulance"),
    ("embarazada", "pregnant woman"),
    ("a horcajadas · reposapiés", "astride · footrests"),
    ("casco homologado", "approved helmet"),
    ("estructura de autoprotección", "roll-over protection structure"),
    ("carga y descarga", "loading and unloading"),
    ("maletero · baca", "boot · roof rack"),
    ("carga divisible · indivisible", "divisible · indivisible load"),
    ("proyección en planta", "outline seen from above"),
    ("estibar", "to stow (secure a load)"),
    ("isotermo", "refrigerated / insulated body"),
    ("semirremolque · vehículo articulado · tren de carretera", "semitrailer · articulated vehicle · road train"),
    ("portavehículos · vehículo grúa", "car transporter · crane vehicle"),
    ("autorización complementaria de circulación", "special movement permit"),
    ("extremidad saliente", "projecting end"),
    ("catadióptrico", "reflector"),
    ("masa en vacío", "unladen mass"),
    ("apearse", "to get out (of a vehicle)"),
    ("conductor novel", "novice driver"),
    ("bajada de bandera", "start of the taxi fare"),
    ("distintivo ambiental", "environmental label"),
    ("ángulo muerto", "blind spot"),
]
