# -*- coding: utf-8 -*-
"""Question bank for the interactive Topic 6 page (carrying people and goods). In every question the FIRST option is
the correct one (the page shuffles options when it shows them). Ids must be unique and must not start with "ai"."""

BANK = []


def Q(qid, tag, en, es, opts, why_en, why_es):
    BANK.append({
        "id": qid, "tag": tag,
        "q": {"en": en, "es": es},
        "o": [{"en": a, "es": b} for a, b in opts],
        "why": {"en": why_en, "es": why_es},
    })


# tag -> section number, names, recap bullets, typical confusion
TAGS = {
    "people": dict(sec=1, en="Seats, weight and where people sit", es="Plazas, peso y emplazamiento",
        recap=[("Never more people than authorised seats; a child takes a whole seat.", "Nunca más personas que plazas autorizadas; un niño ocupa una plaza."),
               ("Never above the MMA: count people and luggage. Seats and MMA are in the inspection card or registration certificate.",
                "Nunca por encima de la MMA: cuentan personas y equipaje. Plazas y MMA en la tarjeta ITV o el permiso de circulación."),
               ("People only in places fitted for them; in a goods load area only with authorisation.", "Personas solo en los lugares acondicionados; en la zona de carga, solo con autorización."),
               ("The driver keeps control and position, and places people, objects and animals so nothing interferes.", "El conductor mantiene el control y la posición, y coloca personas, objetos y animales sin interferencias.")],
        trap=("Thinking small children do not count as a seat.", "Pensar que los niños pequeños no cuentan como plaza.")),
    "belts": dict(sec=1, en="Seat belts and child seats", es="Cinturón y sistemas de retención",
        recap=[("Everyone wears an approved belt, in town and out of town.", "Todos usan cinturón homologado, en vías urbanas e interurbanas."),
               ("135 cm or less: approved child seat for their height and weight.", "Hasta 135 cm: sistema de retención homologado según talla y peso."),
               ("Up to 9 seats: children in the back, unless no rear seats, rear full of such children, or seats do not fit.", "Hasta 9 plazas: los menores detrás, salvo que no haya asientos traseros, estén ocupados por otros menores o no quepan los sistemas."),
               ("Rear-facing seat in front only with the frontal airbag off. Buses: from over 3 years old to 135 cm.", "Silla a contramarcha delante solo con el airbag desactivado. Autobuses: de más de 3 años a 135 cm.")],
        trap=("Using age instead of height (135 cm).", "Usar la edad en lugar de la estatura (135 cm).")),
    "exempt": dict(sec=1, en="Exemptions from the belt", es="Exenciones del cinturón",
        recap=[("Drivers reversing or parking; holders of a medical exemption certificate (show it on request).", "Conductores que hacen marcha atrás o estacionan; titulares de certificado médico de exención (mostrarlo si se pide)."),
               ("Emergency vehicles on service: only in town. Patient-care ambulance staff treating the patient: any road.", "Vehículos de urgencia en servicio: solo en poblado. Personal de ambulancia atendiendo al paciente: cualquier vía."),
               ("Taxis in town may carry passengers under 135 cm without a child seat, in a rear seat.", "Taxis en ciudad pueden llevar menores de 135 cm sin sistema de retención, en asiento trasero."),
               ("Not exempt: pregnant women; and since October 2026, taxi drivers, delivery drivers and driving instructors.", "No exentos: embarazadas; y desde octubre de 2026, taxistas, repartidores y profesores de autoescuela.")],
        trap=("Thinking pregnant women or taxi drivers in town are exempt.", "Pensar que las embarazadas o los taxistas en ciudad están exentos.")),
    "moto": dict(sec=1, en="Passengers on motorcycles and mopeds", es="Pasajeros en motocicletas y ciclomotores",
        recap=[("At most one passenger (plus sidecar occupant), if the registration certificate allows it.", "Como máximo un pasajero (más el del sidecar), si consta en el permiso de circulación."),
               ("Over 12; over 7 if a parent, guardian or authorised adult rides.", "Mayor de 12 años; mayor de 7 si conduce su padre, madre, tutor o adulto autorizado."),
               ("Behind the rider, never between rider and handlebars.", "Detrás del conductor, nunca entre él y el manillar."),
               ("Astride, feet on the side footrests.", "A horcajadas, con los pies en los reposapiés laterales.")],
        trap=("Seating a small child in front of the rider.", "Sentar a un niño pequeño delante del conductor.")),
    "helmet": dict(sec=1, en="Helmets", es="El casco",
        recap=[("Riders and passengers of motorcycles, three-wheelers, quadricycles, mopeds and quads: approved helmet (UNECE R22), fastened.",
                "Conductores y pasajeros de motos, tres ruedas, cuadriciclos, ciclomotores y quads: casco homologado (R22) abrochado."),
               ("With a protective structure and belts on the inspection card: belt instead of helmet.", "Con estructura de autoprotección y cinturones en la tarjeta ITV: cinturón en lugar de casco."),
               ("Cyclists: compulsory under 16 everywhere, and for everyone on interurban roads.", "Ciclistas: obligatorio a menores de 16 en todas las vías y a todos en interurbanas."),
               ("Cycling for work in town: helmet compulsory.", "Circular en bicicleta por trabajo en ciudad: casco obligatorio.")],
        trap=("Thinking adult cyclists may ride without a helmet on interurban roads.", "Pensar que un ciclista adulto puede ir sin casco por vía interurbana.")),
    "cycles": dict(sec=1, en="Carrying on cycles", es="Transporte en ciclos",
        recap=[("One-person cycles may carry children up to 22 kg in approved extra seats.", "Ciclos de una plaza: menores de hasta 22 kg en asientos adicionales homologados."),
               ("Approved trailers: people, animals up to 15 kg, or load.", "Remolques homologados: personas, animales de hasta 15 kg o carga."),
               ("Out of town, with a trailer: only by day and with good visibility.", "En interurbana, con remolque: solo de día y con buena visibilidad."),
               ("Carrying load or passengers requires an adult rider.", "Para llevar carga o pasajeros, el conductor debe ser mayor de edad.")],
        trap=("Mixing up 22 kg (children) and 15 kg (animals).", "Confundir 22 kg (menores) con 15 kg (animales).")),
    "loading": dict(sec=2, en="Loading and placing the load", es="Carga y descarga y colocación",
        recap=[("Load and unload off the road; if on it, on the side nearest the edge, following stopping and parking rules.", "Cargar y descargar fuera de la vía; si es en ella, por el lado más próximo al borde y respetando parada y estacionamiento."),
               ("Never leave goods on the carriageway, shoulder or pedestrian areas; work quickly, without danger or noise.", "Nunca depositar mercancía en calzada, arcén o zonas peatonales; con rapidez, sin peligro ni ruido."),
               ("The load must not unbalance, hide lights or signals, drag, fall or shift, or cause avoidable dust; cover it if needed.", "La carga no debe desestabilizar, ocultar luces o señales, arrastrar, caer o desplazarse ni producir polvo evitable; cubrirla si hace falta."),
               ("Cars: in the boot, evenly; only light things in the cabin; heavy things on the roof rack are dangerous.", "Turismos: en el maletero, repartida; en el habitáculo solo cosas ligeras; peso en la baca, peligroso.")],
        trap=("Thinking heavy luggage is best on the roof rack.", "Pensar que el equipaje pesado va mejor en la baca.")),
    "dims": dict(sec=2, en="Maximum dimensions", es="Dimensiones máximas",
        recap=[("Length 12 m; buses 13.50 / 15 m; semitrailer 14.04; articulated 16.50; road train 18.75.", "Longitud 12 m; autobuses 13,50 / 15 m; semirremolque 14,04; articulado 16,50; tren de carretera 18,75."),
               ("Width 2.55 m (2.60 refrigerated bodies and prisoner buses).", "Anchura 2,55 m (2,60 isotermos y autobuses de presos)."),
               ("Height 4 m (4.20 urban buses; 4.50 car transporters, cranes, closed containers).", "Altura 4 m (4,20 autobuses urbanos; 4,50 portavehículos, grúas, contenedores cerrados)."),
               ("Over 12 m long: V-6 plate at the rear, centred, or two symmetrical plates.", "Más de 12 m: señal V-6 detrás, centrada, o dos placas simétricas.")],
        trap=("Mixing up 2.55 m (width) and 4 m (height).", "Confundir 2,55 m (anchura) con 4 m (altura).")),
    "overhang": dict(sec=2, en="How far the load may stick out", es="Cuánto puede sobresalir la carga",
        recap=[("Not only for goods: rear only, 10 % divisible or 15 % indivisible; never front or sides.", "No exclusivos de mercancías: solo detrás, 10 % divisible o 15 % indivisible; nunca delante ni a los lados."),
               ("Goods vehicles: as a rule nothing; indivisible load: up to 5 m long ⅓ + ⅓, over 5 m 2 m front and 3 m rear.", "Mercancías: como norma nada; indivisible: hasta 5 m ⅓ + ⅓, más de 5 m 2 m delante y 3 m detrás."),
               ("Sideways: 0.40 m each side, total width ≤ 2.55 m.", "A lo ancho: 0,40 m por lado, anchura total ≤ 2,55 m."),
               ("Under 1 m wide: 0.25 m rear, 0.50 m each side, none in front. Beyond the limits: complementary permit.", "Menos de 1 m de ancho: 0,25 m detrás, 0,50 m a cada lado, nada delante. Por encima: autorización complementaria.")],
        trap=("Swapping 2 m front and 3 m rear.", "Intercambiar 2 m delante y 3 m detrás.")),
    "loadsignal": dict(sec=2, en="Signalling the overhang", es="Señalizar la carga saliente",
        recap=[("Protect the projecting end and signal it.", "Resguardar la extremidad saliente y señalizarla."),
               ("By day: rear 1 or 2 V-20 panels (2 across the whole width, inverted V); front not needed.", "De día: detrás 1 o 2 paneles V-20 (2 si ocupa toda la anchura, en V invertida); delante no hace falta."),
               ("At night or poor visibility: front white light; rear red light plus the panel(s).", "De noche o poca visibilidad: delante luz blanca; detrás luz roja además del panel."),
               ("Side overhang over 0.40 m beyond the position lights: white light and reflector in front, red behind. Vehicles under 1 m wide: no rear signal needed.",
                "Carga lateral a más de 0,40 m de las luces de posición: luz y catadióptrico blancos delante, rojos detrás. Menos de 1 m de ancho: no se señaliza detrás.")],
        trap=("Putting a red light at the front of an overhanging load.", "Poner luz roja en la parte delantera de la carga.")),
    "towing": dict(sec=2, en="Motorcycle trailers and bicycles", es="Remolques de moto y bicicletas",
        recap=[("Motorcycles, three-wheelers and mopeds may tow a trailer of up to 50 % of their unladen mass.", "Motos, tres ruedas y ciclomotores pueden llevar remolque de hasta el 50 % de su masa en vacío."),
               ("Only by day with good visibility, 10 % below their generic out-of-town speeds.", "Solo de día y con buena visibilidad, un 10 % por debajo de sus velocidades genéricas fuera de poblado."),
               ("Never with people in the trailer; in town, local bylaws.", "Nunca con personas en el remolque; en poblado, ordenanzas municipales."),
               ("Bicycles carry load or passengers only with an adult rider, without hiding lights or losing stability.", "Las bicicletas llevan carga o pasajeros solo con conductor mayor de edad, sin tapar luces ni perder estabilidad.")],
        trap=("Using the laden mass, or 10 km/h instead of 10 %.", "Usar la masa cargada, o 10 km/h en lugar del 10 %.")),
    "doors": dict(sec=3, en="Doors", es="Las puertas",
        recap=[("Get in and out on the side nearest the edge of the road.", "Entrar y salir por el lado más cercano al borde de la vía."),
               ("Never drive with doors open.", "Prohibido llevar las puertas abiertas."),
               ("Never open them before the vehicle has fully stopped.", "Prohibido abrirlas antes de la completa inmovilización."),
               ("Check first that nobody is endangered, above all two-wheelers.", "Comprobar antes que no se pone en peligro a nadie, sobre todo a los de dos ruedas.")],
        trap=("Opening the traffic-side door without checking for cyclists.", "Abrir la puerta del lado del tráfico sin mirar si viene un ciclista.")),
    "plates": dict(sec=4, en="Vehicle signals V-1 to V-13", es="Señales V-1 a V-13",
        recap=[("V-1 blue priority (50 m). V-2 amber obstacle (stopped or ≤ 40 km/h). V-3 police not urgent.", "V-1 azul prioritario (50 m). V-2 amarilla obstáculo (parado o ≤ 40 km/h). V-3 policía no urgente."),
               ("V-4 speed limit at the rear. V-5 slow vehicle (can’t exceed 40 by construction). V-6 long (> 12 m).", "V-4 limitación de velocidad detrás. V-5 vehículo lento (no supera 40 por construcción). V-6 largo (> 12 m)."),
               ("V-7 Spanish nationality, V-8 foreign. V-9 public service (SP). V-10 school. V-11 dangerous goods. V-12 test plate.", "V-7 nacionalidad española, V-8 extranjera. V-9 servicio público (SP). V-10 escolar. V-11 mercancías peligrosas. V-12 ensayo."),
               ("V-13 novice: licence under 1 year, rear left.", "V-13 novel: permiso de menos de 1 año, detrás a la izquierda.")],
        trap=("Mixing up V-4 (speed limit) and V-5 (slow vehicle).", "Confundir la V-4 (limitación) con la V-5 (vehículo lento).")),
    "plates2": dict(sec=4, en="Vehicle signals V-14 to V-27", es="Señales V-14 a V-27",
        recap=[("V-14 driving lessons. V-15 disabled driver. V-16 immobilised vehicle or fallen load.", "V-14 aprendizaje. V-15 minusválido. V-16 vehículo inmovilizado o carga caída."),
               ("V-17 taxi free, V-18 taximeter, V-19 ITV badge, V-20 load sticking out behind.", "V-17 taxi libre, V-18 taxímetro, V-19 ITV, V-20 carga saliente detrás."),
               ("V-21 special-transport escort, V-22 cyclist escort, V-23 reflective goods marking, V-24 roadside assistance.", "V-21 acompañamiento de transporte especial, V-22 de ciclistas, V-23 marcado reflectante, V-24 auxilio en vías públicas."),
               ("V-25 environmental label and V-26 shared use: windscreen, lower right. V-27 virtual triangle (voluntary, connected cars).", "V-25 ambiental y V-26 uso compartido: parabrisas, abajo a la derecha. V-27 triángulo virtual (voluntario, vehículos conectados).")],
        trap=("Placing the environmental label on the left of the windscreen.", "Colocar el distintivo ambiental a la izquierda del parabrisas.")),
}


# ---------------------------------------------------------------- 1. people
Q("pp1", "people", "A car has 5 seats. How many people may travel in it, counting a baby?", "Un turismo tiene 5 plazas. ¿Cuántas personas pueden viajar en él, contando un bebé?",
  [("5 in total, baby included", "5 en total, incluido el bebé"), ("5 adults plus the baby", "5 adultos más el bebé"), ("6 if two are children", "6 si dos son niños")],
  "A child occupies a seat like an adult.", "Un niño ocupa una plaza igual que un adulto.")
Q("pp2", "people", "Where can you check a vehicle’s number of seats and its MMA?", "¿Dónde se consulta el número de plazas y la MMA de un vehículo?",
  [("In the inspection card or the registration certificate", "En la tarjeta de inspección técnica o en el permiso de circulación"), ("On the driving licence", "En el permiso de conducción"),
   ("On the insurance policy", "En la póliza del seguro")],
  "Never exceed either of them.", "No se puede superar ninguno de los dos.")
Q("pp3", "people", "When checking you do not exceed the MMA, you must count…", "Para no superar la MMA hay que contar…",
  [("the people and their luggage", "las personas y su equipaje"), ("only the luggage", "solo el equipaje"), ("only the driver", "solo al conductor")],
  "The MMA can never be exceeded.", "La MMA no se puede superar en ningún caso.")
Q("pp4", "people", "May people travel in the load area of a lorry?", "¿Pueden viajar personas en la zona de carga de un camión?",
  [("Only with authorisation and the safety conditions it sets", "Solo con autorización y en las condiciones de seguridad que se fijen"), ("Yes, if seated", "Sí, si van sentadas"),
   ("Yes, on short trips", "Sí, en trayectos cortos")],
  "Otherwise only in places fitted for people.", "Si no, solo en los lugares acondicionados para personas.")
Q("pp5", "people", "A vehicle authorised to carry people and load together must have…", "Un vehículo autorizado a llevar personas y carga a la vez debe tener…",
  [("a protection so the load cannot hit or hinder the occupants", "una protección para que la carga no dañe ni estorbe a los ocupantes"), ("a second driver", "un segundo conductor"),
   ("a V-20 panel", "un panel V-20")],
  "In case the load is thrown forward.", "Por si la carga sale proyectada.")
Q("pp6", "people", "Placing a dog loose on the passenger seat where it can reach you is…", "Llevar un perro suelto en el asiento del acompañante, donde puede alcanzarte, es…",
  [("wrong: nothing may interfere with the driver", "incorrecto: nada debe interferir con el conductor"), ("allowed if it is small", "correcto si es pequeño"), ("allowed in town", "correcto en poblado")],
  "Objects and animals must be properly placed.", "Objetos y animales deben ir colocados adecuadamente.")

# ---------------------------------------------------------------- 1.1 belts
Q("bt1", "belts", "Must rear passengers wear seat belts in town?", "¿Deben llevar cinturón los pasajeros traseros en ciudad?",
  [("Yes, on urban and interurban roads", "Sí, en vías urbanas e interurbanas"), ("No, only out of town", "No, solo fuera de poblado"), ("Only children", "Solo los niños")],
  "Unless the vehicle has no belts fitted.", "Salvo que el vehículo no los tenga instalados.")
Q("bt2", "belts", "A child seat is compulsory for children…", "El sistema de retención infantil es obligatorio para los menores…",
  [("135 cm tall or less", "de estatura igual o inferior a 135 cm"), ("under 12", "de menos de 12 años"), ("under 36 kg only", "de menos de 36 kg solamente")],
  "Suited to their height and weight.", "Adaptado a su talla y peso.")
Q("bt3", "belts", "In a car with 5 seats, where does a 120 cm child normally travel?", "En un turismo de 5 plazas, ¿dónde viaja normalmente un niño de 120 cm?",
  [("In a rear seat, in an approved child seat", "En un asiento trasero, con sistema de retención homologado"), ("In the front, with the belt", "Delante, con el cinturón"), ("Anywhere, with the belt", "En cualquier plaza, con cinturón")],
  "Vehicles up to 9 seats.", "Vehículos de hasta 9 plazas.")
Q("bt4", "belts", "When may a child under 135 cm travel in the front seat of a car?", "¿Cuándo puede un menor de 135 cm ir delante en un turismo?",
  [("When the rear seats are full of such children, missing, or the child seats do not fit", "Si no hay asientos traseros, están ocupados por otros menores así o no caben los sistemas"),
   ("Whenever the parent agrees", "Siempre que lo acepten los padres"), ("On short trips", "En trayectos cortos")],
  "Always in an approved child seat.", "Siempre con sistema de retención homologado.")
Q("bt5", "belts", "A rear-facing child seat in the front passenger seat is allowed…", "Una silla a contramarcha en el asiento del acompañante se permite…",
  [("only if the frontal airbag is switched off", "solo si el airbag frontal está desactivado"), ("always", "siempre"), ("only on motorways", "solo en autopistas")],
  "An inflating airbag would hit the seat.", "El airbag al inflarse golpearía la silla.")
Q("bt6", "belts", "On a coach (more than 9 seats), which children must use a child seat?", "En un autocar (más de 9 plazas), ¿qué menores deben usar sistema de retención?",
  [("Over 3 years old and up to 135 cm", "Los de más de tres años y hasta 135 cm"), ("All under 135 cm, babies included", "Todos los de menos de 135 cm, bebés incluidos"), ("None", "Ninguno")],
  "Without child seats, the belt if it suits their size.", "Si no hay, el cinturón si es adecuado a su talla y peso.")
Q("bt7", "belts", "On a coach, who tells passengers they must wear belts?", "En un autocar, ¿quién informa de la obligación del cinturón?",
  [("The driver, guide or group leader, or audiovisual means and pictograms", "El conductor, el guía o el responsable del grupo, o medios audiovisuales y pictogramas"),
   ("Nobody, it is the passenger’s duty", "Nadie, es cosa del pasajero"), ("Only the police", "Solo la policía")],
  "Signs or pictograms count.", "Valen letreros o pictogramas.")
Q("bt8", "belts", "A child seat is chosen according to…", "El sistema de retención infantil se elige según…",
  [("the child’s height and weight, following the maker’s instructions", "la talla y el peso del niño, según las instrucciones del fabricante"), ("the child’s age only", "solo la edad del niño"),
   ("the car’s brand", "la marca del coche")],
  "It must be approved.", "Debe estar homologado.")

# ---------------------------------------------------------------- 1.2 exemptions
Q("ex1", "exempt", "Are drivers exempt from the seat belt while parking?", "¿Está exento del cinturón el conductor mientras estaciona?",
  [("Yes, while reversing or parking", "Sí, al hacer marcha atrás o estacionar"), ("No, never", "No, nunca"), ("Only at night", "Solo de noche")],
  "Only during those manoeuvres.", "Solo durante esas maniobras.")
Q("ex2", "exempt", "Is a pregnant woman exempt from the seat belt?", "¿Está exenta del cinturón una mujer embarazada?",
  [("No, she must wear it", "No, debe usarlo"), ("Yes, always", "Sí, siempre"), ("Yes, from the sixth month", "Sí, a partir del sexto mes")],
  "Approved accessories can add protection.", "Hay accesorios homologados que aumentan la seguridad.")
Q("ex3", "exempt", "An ambulance on urgent service is on an autovía. Must its driver wear the belt?", "Una ambulancia en servicio urgente circula por una autovía. ¿Debe su conductor usar el cinturón?",
  [("Yes: the exemption for emergency vehicles applies only in town", "Sí: la exención de los vehículos de urgencia es solo en poblado"), ("No, never on service", "No, nunca en servicio"),
   ("Only at night", "Solo de noche")],
  "Staff treating the patient in the back are exempt on any road.", "El personal que atiende al paciente detrás está exento en cualquier vía.")
Q("ex4", "exempt", "A taxi in a city carries a 120 cm child without a child seat. Is it allowed?", "Un taxi en ciudad lleva a un niño de 120 cm sin sistema de retención. ¿Se permite?",
  [("Yes, if the child sits in a rear seat", "Sí, si ocupa un asiento trasero"), ("No, never", "No, nunca"), ("Yes, in the front seat", "Sí, en el asiento delantero")],
  "Only in urban traffic.", "Solo en tráfico urbano.")
Q("ex5", "exempt", "Since October 2026, must a taxi driver in town wear the seat belt?", "Desde octubre de 2026, ¿debe un taxista llevar el cinturón en ciudad?",
  [("Yes, the old exemption no longer exists", "Sí, la antigua exención ya no existe"), ("No, taxis are exempt in town", "No, los taxis están exentos en poblado"), ("Only with passengers", "Solo con pasajeros")],
  "Same for delivery drivers and driving instructors.", "Igual para repartidores y profesores de autoescuela.")
Q("ex6", "exempt", "A person with a medical exemption certificate from another EU country…", "Una persona con certificado médico de exención de otro país de la UE…",
  [("is exempt, and shows it to agents on request", "está exenta y debe mostrarlo a los agentes si lo piden"), ("must get a Spanish one", "debe obtener uno español"), ("is not exempt in Spain", "no está exenta en España")],
  "Certificates from any EU state are valid.", "Valen los de cualquier Estado de la UE.")
Q("ex7", "exempt", "Is a delivery driver making many stops in town exempt from the belt?", "¿Está exento del cinturón un repartidor que hace muchas paradas en ciudad?",
  [("No, not since October 2026", "No, desde octubre de 2026"), ("Yes, always in town", "Sí, siempre en poblado"), ("Yes, below 30 km/h", "Sí, por debajo de 30 km/h")],
  "The 2026 reform removed that exemption.", "La reforma de 2026 suprimió esa exención.")

# ---------------------------------------------------------------- 1.3 motorcycles
Q("mo1", "moto", "How many passengers may a motorcycle without sidecar carry?", "¿Cuántos pasajeros puede llevar una motocicleta sin sidecar?",
  [("One, if its registration certificate allows it", "Uno, si consta en su permiso de circulación"), ("Two", "Dos"), ("One child and one adult", "Un niño y un adulto")],
  "Plus the sidecar occupant, if it has one.", "Más el ocupante del sidecar, si lo tiene.")
Q("mo2", "moto", "Minimum age for a passenger on a motorcycle, as a general rule", "Edad mínima del pasajero de una motocicleta, como norma general",
  [("over 12", "mayor de 12 años"), ("over 7", "mayor de 7 años"), ("over 16", "mayor de 16 años")],
  "Over 7 if a parent, guardian or authorised adult rides.", "Mayor de 7 si conduce su padre, madre, tutor o adulto autorizado.")
Q("mo3", "moto", "Your 9-year-old son may ride behind you on your motorcycle if…", "Tu hijo de 9 años puede ir detrás contigo en tu moto si…",
  [("you, his parent, are riding and the other conditions are met", "conduces tú, su padre o madre, y se cumplen las demás condiciones"), ("never, he is under 12", "nunca, es menor de 12"),
   ("only in town", "solo en poblado")],
  "Exception for over-7s with a parent, guardian or authorised adult.", "Excepción para mayores de 7 con padre, madre, tutor o adulto autorizado.")
Q("mo4", "moto", "Where must a motorcycle passenger sit?", "¿Dónde debe ir el pasajero de una moto?",
  [("Behind the rider", "Detrás del conductor"), ("Between the rider and the handlebars, if small", "Entre el conductor y el manillar, si es pequeño"), ("On the tank", "Sobre el depósito")],
  "Never between rider and handlebars.", "Nunca entre el conductor y el manillar.")
Q("mo5", "moto", "How does a motorcycle passenger sit?", "¿Cómo va sentado el pasajero de una moto?",
  [("Astride, feet on the side footrests", "A horcajadas, con los pies en los reposapiés laterales"), ("Side-saddle", "De lado"), ("Any way, if holding on", "De cualquier forma si va agarrado")],
  "One leg each side.", "Una pierna a cada lado.")
Q("mo6", "moto", "Do these conditions also apply to mopeds?", "¿Se aplican también estas condiciones a los ciclomotores?",
  [("Yes, the same rules", "Sí, las mismas"), ("No, mopeds can’t carry passengers", "No, los ciclomotores no pueden llevar pasajeros"), ("Only the age rule", "Solo la de la edad")],
  "If the registration certificate allows a passenger.", "Si su permiso de circulación admite pasajero.")

# ---------------------------------------------------------------- helmets
Q("hm1", "helmet", "Who must wear a helmet on a moped?", "¿Quién debe llevar casco en un ciclomotor?",
  [("Rider and passenger", "El conductor y el pasajero"), ("Only the rider", "Solo el conductor"), ("Only out of town", "Solo fuera de poblado")],
  "Approved (UNECE R22) and fastened.", "Homologado (R22) y abrochado.")
Q("hm2", "helmet", "A quadricycle has a protective structure and belts listed on its inspection card. Its occupants…", "Un cuadriciclo tiene estructura de autoprotección y cinturones en su tarjeta ITV. Sus ocupantes…",
  [("may skip the helmet but must wear the belt", "están exentos del casco y deben usar el cinturón"), ("must wear both", "deben usar ambos"), ("need neither", "no necesitan ninguno")],
  "It must be stated on the inspection card.", "Debe constar en la tarjeta de inspección técnica.")
Q("hm3", "helmet", "An adult cyclist on an interurban road…", "Un ciclista adulto por una vía interurbana…",
  [("must wear an approved helmet", "debe llevar casco homologado"), ("may ride without a helmet", "puede ir sin casco"), ("needs one only at night", "solo lo necesita de noche")],
  "Compulsory for everyone on interurban roads.", "Obligatorio para todos en vías interurbanas.")
Q("hm4", "helmet", "A 14-year-old cycles in town. Helmet?", "Un chico de 14 años circula en bici por la ciudad. ¿Casco?",
  [("Compulsory: under 16 on any road", "Obligatorio: menores de 16 en cualquier vía"), ("Optional in town", "Opcional en ciudad"), ("Only on cycle lanes", "Solo en carriles bici")],
  "Under-16s wear it everywhere.", "Los menores de 16 lo llevan en todas las vías.")
Q("hm5", "helmet", "A delivery rider working by bicycle in a city…", "Un repartidor que trabaja en bicicleta por la ciudad…",
  [("must wear an approved or certified helmet", "debe llevar casco homologado o certificado"), ("needs no helmet in town", "no necesita casco en ciudad"), ("needs a motorcycle helmet", "necesita casco de moto")],
  "Cycling for work in town.", "Actividad profesional en vías urbanas.")
Q("hm6", "helmet", "The approved motorcycle helmet standard is…", "La norma de homologación del casco de moto es…",
  [("UNECE R22", "Reglamento UNECE R22"), ("EN 1078 only", "solo la EN 1078"), ("there is none", "no existe")],
  "Properly fastened.", "Correctamente abrochado.")

# ---------------------------------------------------------------- cycles
Q("cy1", "cycles", "A one-person bicycle may carry a child in an approved extra seat if the child weighs up to…", "Una bicicleta de una plaza puede llevar a un menor en asiento adicional homologado si pesa hasta…",
  [("22 kg", "22 kg"), ("15 kg", "15 kg"), ("40 kg", "40 kg")],
  "And can sit on their own.", "Y es capaz de sentarse solo.")
Q("cy2", "cycles", "A bicycle trailer may carry animals weighing up to…", "Un remolque de bicicleta puede llevar animales de hasta…",
  [("15 kg", "15 kg"), ("22 kg", "22 kg"), ("50 kg", "50 kg")],
  "Also people or load, with approved trailers.", "También personas o carga, con remolques que cumplan las especificaciones.")
Q("cy3", "cycles", "A bicycle towing a trailer on an interurban road may ride…", "Una bicicleta con remolque por vía interurbana puede circular…",
  [("only by day, with good visibility", "solo de día y sin visibilidad reducida"), ("day or night with lights", "de día o de noche con luces"), ("never", "nunca")],
  "In town there is no such limit.", "En poblado no existe esa limitación.")
Q("cy4", "cycles", "To carry a passenger on a bicycle, the rider must be…", "Para llevar un pasajero en bicicleta, el conductor debe ser…",
  [("an adult (18 or over)", "mayor de edad"), ("over 16", "mayor de 16"), ("over 14", "mayor de 14")],
  "Same for carrying load.", "Igual para llevar carga.")

# ---------------------------------------------------------------- 2.1-2.2 loading
Q("ld1", "loading", "As a general rule, loading and unloading is done…", "Como norma general, la carga y descarga se hace…",
  [("off the road", "fuera de la vía"), ("on the shoulder", "en el arcén"), ("in the right lane with hazard lights", "en el carril derecho con la luz de emergencia")],
  "Exceptionally on the road, following its rules.", "Excepcionalmente en la vía, con sus normas.")
Q("ld2", "loading", "When you must load on the road, you do it…", "Cuando hay que cargar en la vía, se hace…",
  [("on the side nearest the edge of the carriageway", "por el lado más próximo al borde de la calzada"), ("on the traffic side", "por el lado del tráfico"), ("from the middle of the road", "desde el centro de la calzada")],
  "Respecting stopping and parking rules.", "Respetando las normas de parada y estacionamiento.")
Q("ld3", "loading", "May you leave boxes on the pavement while unloading?", "¿Puedes dejar cajas en la acera mientras descargas?",
  [("No, goods may not be left on the carriageway, shoulder or pedestrian areas", "No, no se puede depositar mercancía en calzada, arcén ni zonas peatonales"), ("Yes, briefly", "Sí, un momento"),
   ("Yes, if you stay with them", "Sí, si te quedas con ellas")],
  "Unload quickly, without danger or nuisance.", "Con rapidez, sin peligros ni molestias.")
Q("ld4", "loading", "A load of sand that could blow away must be…", "Una carga de arena que puede volar debe…",
  [("fully and effectively covered", "cubrirse total y eficazmente"), ("wetted", "mojarse"), ("driven slowly", "transportarse despacio")],
  "No avoidable dust or falling material.", "Sin polvo ni caídas evitables.")
Q("ld5", "loading", "Where should luggage go in a car?", "¿Dónde debe ir el equipaje en un turismo?",
  [("In the boot, weight spread evenly", "En el maletero, con el peso repartido uniformemente"), ("On the rear seat", "En el asiento trasero"), ("On the roof rack, heaviest first", "En la baca, lo más pesado")],
  "Only small, light things in the cabin.", "En el habitáculo solo objetos ligeros y pequeños.")
Q("ld6", "loading", "Heavy, bulky luggage on the roof rack…", "Equipaje pesado y voluminoso en la baca…",
  [("can make the car unstable and raise fuel use", "puede comprometer la estabilidad y aumenta el consumo"), ("improves road holding", "mejora la adherencia"), ("is the recommended place", "es el lugar recomendado")],
  "It may even make the car overturn.", "Incluso puede hacerlo volcar.")
Q("ld7", "loading", "The load must not hide…", "La carga no debe ocultar…",
  [("lights, number plates and the driver’s arm signals", "las luces, las placas y las advertencias del conductor"), ("the rear window only", "solo la luna trasera"), ("nothing, if it is tied", "nada, si va atada")],
  "Nor make the vehicle unstable or fall.", "Ni comprometer la estabilidad ni caerse.")

# ---------------------------------------------------------------- 2.3 dimensions
Q("dm1", "dims", "General maximum length of a motor vehicle, load included", "Longitud máxima general de un vehículo de motor, con la carga",
  [("12 m", "12 m"), ("10 m", "10 m"), ("15 m", "15 m")],
  "Buses, semitrailers, articulated vehicles and road trains have their own limits.", "Autobuses, semirremolques, articulados y trenes de carretera tienen límites propios.")
Q("dm2", "dims", "General maximum width of a vehicle, load included", "Anchura máxima general de un vehículo, con la carga",
  [("2.55 m", "2,55 m"), ("2.50 m", "2,50 m"), ("3 m", "3 m")],
  "2.60 m for refrigerated bodies and prisoner buses.", "2,60 m para isotermos y autobuses de presos.")
Q("dm3", "dims", "General maximum height, load included", "Altura máxima general, con la carga",
  [("4 m", "4 m"), ("3.5 m", "3,5 m"), ("4.5 m", "4,5 m")],
  "4.20 urban buses; 4.50 car transporters, cranes and closed containers.", "4,20 autobuses urbanos; 4,50 portavehículos, grúas y contenedores cerrados.")
Q("dm4", "dims", "Maximum length of a road train", "Longitud máxima de un tren de carretera",
  [("18.75 m", "18,75 m"), ("16.50 m", "16,50 m"), ("12 m", "12 m")],
  "Articulated vehicles: 16.50 m.", "Vehículos articulados: 16,50 m.")
Q("dm5", "dims", "Which vehicle must carry the V-6 “long vehicle” plate?", "¿Qué vehículo debe llevar la señal V-6 «Vehículo largo»?",
  [("One longer than 12 m", "El de más de 12 m de longitud"), ("Any lorry", "Cualquier camión"), ("One over 3,500 kg", "El de más de 3.500 kg")],
  "Including combinations.", "Incluidos los conjuntos.")
Q("dm6", "dims", "The V-6 plate is…", "La señal V-6 es…",
  [("yellow reflective with a fluorescent red border", "amarilla reflectante con borde rojo fluorescente"), ("orange with a black border", "naranja con borde negro"), ("red and white striped", "a franjas rojas y blancas")],
  "At the rear, centred, or two symmetrical plates.", "Detrás y centrada, o dos placas simétricas.")
Q("dm7", "dims", "Maximum height of a car transporter", "Altura máxima de un portavehículos",
  [("4.50 m", "4,50 m"), ("4 m", "4 m"), ("5 m", "5 m")],
  "Also crane vehicles and closed-container carriers.", "También vehículos grúa y portacontenedores cerrados.")
Q("dm8", "dims", "Maximum length of a 3-axle bus", "Longitud máxima de un autobús de 3 ejes",
  [("15 m", "15 m"), ("13.50 m", "13,50 m"), ("12 m", "12 m")],
  "2 axles: 13.50 m.", "2 ejes: 13,50 m.")

# ---------------------------------------------------------------- 2.4 overhang
Q("oh1", "overhang", "In a car, a divisible load may stick out at the rear up to…", "En un turismo, una carga divisible puede sobresalir por detrás hasta…",
  [("10 % of the vehicle’s length", "el 10 % de la longitud del vehículo"), ("15 % of its length", "el 15 % de su longitud"), ("1 m", "1 m")],
  "Indivisible: 15 %.", "Indivisible: 15 %.")
Q("oh2", "overhang", "In a car, may a load stick out at the sides?", "En un turismo, ¿puede la carga sobresalir por los laterales?",
  [("No, nor in front", "No, ni por delante"), ("Yes, 0.40 m", "Sí, 0,40 m"), ("Yes, if signalled", "Sí, si se señaliza")],
  "Only at the rear (and on top within the rules).", "Solo por detrás (y por arriba según las normas).")
Q("oh3", "overhang", "A 10 m lorry carries an indivisible load. How far may it stick out?", "Un camión de 10 m lleva carga indivisible. ¿Cuánto puede sobresalir?",
  [("2 m in front and 3 m behind", "2 m por delante y 3 m por detrás"), ("3 m in front and 2 m behind", "3 m por delante y 2 m por detrás"), ("⅓ of its length each end", "⅓ de su longitud por cada extremo")],
  "Vehicles over 5 m long.", "Vehículos de más de 5 m.")
Q("oh4", "overhang", "A 4.5 m van carries indivisible pipes. How far may they stick out?", "Un furgón de 4,5 m lleva tubos indivisibles. ¿Cuánto pueden sobresalir?",
  [("⅓ of its length in front and ⅓ behind", "⅓ de su longitud por delante y otro ⅓ por detrás"), ("2 m in front and 3 m behind", "2 m delante y 3 m detrás"), ("Nothing", "Nada")],
  "Vehicles up to 5 m long.", "Vehículos de hasta 5 m.")
Q("oh5", "overhang", "In a goods vehicle, a divisible load may stick out…", "En un vehículo de mercancías, una carga divisible puede sobresalir…",
  [("nothing beyond the vehicle’s outline", "nada de la proyección en planta"), ("10 % at the rear", "un 10 % por detrás"), ("2 m at the rear", "2 m por detrás")],
  "Only indivisible loads get the exception.", "Solo la carga indivisible tiene la excepción.")
Q("oh6", "overhang", "An indivisible load wider than the lorry may stick out sideways up to…", "Una carga indivisible más ancha que el camión puede sobresalir lateralmente hasta…",
  [("0.40 m each side, total width ≤ 2.55 m", "0,40 m por cada lado, anchura total ≤ 2,55 m"), ("0.50 m each side", "0,50 m por cada lado"), ("1 m in total", "1 m en total")],
  "When its smallest dimension exceeds the vehicle’s width.", "Cuando su dimensión menor supera el ancho del vehículo.")
Q("oh7", "overhang", "On a motorcycle (under 1 m wide), the load may stick out…", "En una moto (menos de 1 m de ancho), la carga puede sobresalir…",
  [("0.25 m behind and 0.50 m each side, never in front", "0,25 m detrás y 0,50 m a cada lado, nunca delante"), ("10 % behind", "un 10 % por detrás"), ("0.50 m in front", "0,50 m por delante")],
  "Each side measured from the centre line.", "A cada lado del eje longitudinal.")
Q("oh8", "overhang", "An indivisible load that inevitably exceeds the limits may travel…", "Una carga indivisible que inevitablemente rebasa los límites puede circular…",
  [("with a complementary movement permit", "con autorización complementaria de circulación"), ("at night only", "solo de noche"), ("never", "nunca")],
  "Following the conditions it sets.", "Con las normas y condiciones que se establezcan.")
Q("oh9", "overhang", "A motorhome is, for overhang purposes…", "Una autocaravana, a efectos de carga saliente, es…",
  [("a vehicle not only for goods: rear overhang 10 % or 15 %", "un vehículo no destinado solo a mercancías: 10 % o 15 % por detrás"), ("a goods vehicle", "un vehículo de mercancías"),
   ("not allowed any overhang", "un vehículo sin carga saliente posible")],
  "Like cars and mixed vehicles.", "Como turismos y mixtos.")

# ---------------------------------------------------------------- 2.5 signalling
Q("ls1", "loadsignal", "By day in clear weather, a load sticking out at the rear is signalled with…", "De día y con tiempo claro, la carga que sobresale por detrás se señaliza con…",
  [("one or two V-20 panels", "uno o dos paneles V-20"), ("a red light", "una luz roja"), ("a red flag", "una bandera roja")],
  "At the front nothing is needed by day.", "Delante, de día, no hace falta.")
Q("ls2", "loadsignal", "At night, a load sticking out at the front is signalled with…", "De noche, la carga que sobresale por delante se señaliza con…",
  [("a white light", "una luz blanca"), ("a red light", "una luz roja"), ("a V-20 panel", "un panel V-20")],
  "At the rear: panel plus a red light.", "Detrás: panel y luz roja.")
Q("ls3", "loadsignal", "At night, the rear end of an overhanging load carries…", "De noche, el extremo trasero de una carga saliente lleva…",
  [("the V-20 panel(s) and a red light", "el panel o paneles V-20 y una luz roja"), ("only a red light", "solo una luz roja"), ("a white light", "una luz blanca")],
  "From sunset to sunrise or in poor visibility.", "Entre la puesta y la salida del sol o con poca visibilidad.")
Q("ls4", "loadsignal", "When are two V-20 panels used?", "¿Cuándo se usan dos paneles V-20?",
  [("When the load sticks out across the whole rear width, one at each end", "Cuando la carga sobresale por toda la anchura trasera, uno en cada extremo"),
   ("Always at night", "Siempre de noche"), ("When it sticks out more than 3 m", "Cuando sobresale más de 3 m")],
  "Their stripes form an inverted V.", "Sus franjas forman una V invertida.")
Q("ls5", "loadsignal", "A load sticks out sideways more than 0.40 m beyond the position lights. It must carry…", "Una carga sobresale lateralmente más de 0,40 m del borde de las luces de posición. Debe llevar…",
  [("white light and reflector to the front, red to the rear, at each side end", "luz y catadióptrico blancos hacia delante y rojos hacia atrás en cada extremo lateral"),
   ("a V-20 panel on each side", "un panel V-20 a cada lado"), ("nothing by day", "nada de día")],
  "On each lateral end.", "En cada una de sus extremidades laterales.")
Q("ls6", "loadsignal", "A motorcycle carries a load sticking out at the rear. Must it be signalled?", "Una moto lleva carga que sobresale por detrás. ¿Debe señalizarse?",
  [("No, vehicles under 1 m wide need not signal it", "No, en vehículos de menos de 1 m de ancho no es necesario"), ("Yes, with a V-20 panel", "Sí, con un panel V-20"), ("Yes, with a red flag", "Sí, con una bandera roja")],
  "Its overhang is already limited to 0.25 m.", "Su carga saliente ya está limitada a 0,25 m.")

# ---------------------------------------------------------------- 2.6 towing
Q("tw1", "towing", "A motorcycle may tow a trailer whose mass is up to…", "Una motocicleta puede arrastrar un remolque cuya masa no supere…",
  [("50 % of the motorcycle’s unladen mass", "el 50 % de la masa en vacío de la moto"), ("its own laden mass", "su masa cargada"), ("100 kg", "100 kg")],
  "Also three-wheelers and mopeds.", "También vehículos de tres ruedas y ciclomotores.")
Q("tw2", "towing", "A moped with a trailer must…", "Un ciclomotor con remolque debe…",
  [("travel by day and 10 % below its generic out-of-town speeds", "circular de día y un 10 % por debajo de sus velocidades genéricas fuera de poblado"), ("travel at 25 km/h", "circular a 25 km/h"),
   ("use the hazard lights", "llevar la luz de emergencia")],
  "And without reduced visibility.", "Y sin visibilidad reducida.")
Q("tw3", "towing", "May a person ride in a motorcycle’s trailer?", "¿Puede viajar una persona en el remolque de una moto?",
  [("No, never", "No, en ningún caso"), ("Yes, a child", "Sí, un niño"), ("Yes, with a helmet", "Sí, con casco")],
  "Only goods.", "Solo carga.")
Q("tw4", "towing", "In town, motorcycle trailers follow…", "En poblado, los remolques de moto se rigen por…",
  [("the local bylaws", "las ordenanzas municipales"), ("the motorway rules", "las normas de autopista"), ("no rules", "ninguna norma")],
  "The conditions above are for interurban roads.", "Las condiciones anteriores son para vías interurbanas.")

# ---------------------------------------------------------------- 3. doors
Q("dr1", "doors", "As a general rule, you get out of the car…", "Como norma general, se sale del vehículo…",
  [("by the door nearest the edge of the road", "por la puerta del lado más cercano al borde de la vía"), ("by the driver’s door", "por la puerta del conductor"), ("by any door", "por cualquier puerta")],
  "Away from the traffic.", "Lejos del tráfico.")
Q("dr2", "doors", "May you open the door before the car has fully stopped?", "¿Se puede abrir la puerta antes de que el vehículo esté completamente parado?",
  [("No", "No"), ("Yes, at low speed", "Sí, a poca velocidad"), ("Yes, the rear doors", "Sí, las traseras")],
  "Driving with doors open is also forbidden.", "También está prohibido llevarlas abiertas.")
Q("dr3", "doors", "Before opening your door on the traffic side, you must check above all for…", "Antes de abrir la puerta del lado del tráfico debes comprobar sobre todo…",
  [("riders of two-wheelers", "a los conductores de vehículos de dos ruedas"), ("pedestrians on the far pavement", "a los peatones de la acera de enfrente"), ("parked cars", "los coches estacionados")],
  "Opening without checking is forbidden.", "Abrir sin comprobar está prohibido.")
Q("dr4", "doors", "Driving with a door open is…", "Circular con una puerta abierta está…",
  [("forbidden", "prohibido"), ("allowed below 20 km/h", "permitido por debajo de 20 km/h"), ("allowed when loading", "permitido al cargar")],
  "Also opening before stopping.", "Igual que abrirla antes de parar.")

# ---------------------------------------------------------------- 4. plates V-1 to V-13
Q("vp1", "plates", "The V-1 signal is…", "La señal V-1 es…",
  [("one or more blue lights, visible all round from 50 m", "una o varias luces azules, visibles en todas direcciones a 50 m"), ("an amber rotating light", "una luz amarilla giratoria"),
   ("a red and white panel", "un panel rojo y blanco")],
  "Priority vehicle on urgent service.", "Vehículo prioritario en servicio urgente.")
Q("vp2", "plates", "An amber rotating light (V-2) on a tractor means…", "Una luz amarilla (V-2) en un tractor indica…",
  [("a vehicle-obstacle: working, stopped, or at 40 km/h or less", "vehículo-obstáculo: trabajando, parado o a 40 km/h como máximo"), ("priority vehicle", "vehículo prioritario"),
   ("a long vehicle", "vehículo largo")],
  "Also special transport, escorts and military columns.", "También transporte especial, acompañamientos y columnas militares.")
Q("vp3", "plates", "The V-5 “slow vehicle” plate is carried by vehicles that…", "La señal V-5 «Vehículo lento» la llevan los vehículos que…",
  [("by construction cannot exceed 40 km/h", "por construcción no pueden superar 40 km/h"), ("have a speed limit set by the authority", "tienen un límite fijado por la autoridad"), ("carry heavy loads", "llevan cargas pesadas")],
  "An orange triangle with a red border.", "Triángulo naranja con borde rojo.")
Q("vp4", "plates", "Where does the V-13 novice-driver plate go?", "¿Dónde se coloca la señal V-13 de conductor novel?",
  [("At the rear left, visible", "En la parte posterior izquierda, visible"), ("On the windscreen", "En el parabrisas"), ("At the rear right", "En la parte posterior derecha")],
  "Licence held for less than one year.", "Permiso con menos de un año de antigüedad.")
Q("vp5", "plates", "Which vehicle carries the V-11 plate?", "¿Qué vehículo lleva la señal V-11?",
  [("One carrying dangerous goods, front and rear", "El que transporta mercancías peligrosas, delante y detrás"), ("A school bus", "Un autobús escolar"), ("A long vehicle", "Un vehículo largo")],
  "Orange plates.", "Placas naranjas.")
Q("vp6", "plates", "The V-9 plate (“SP”) means…", "La señal V-9 («SP») indica…",
  [("public service vehicle", "servicio público"), ("special plate", "placa especial"), ("Spanish plate", "matrícula española")],
  "Front and rear, next to the number plates.", "Delante y detrás, junto a las placas de matrícula.")
Q("vp7", "plates", "Does a car with EU-format plates bearing the E need the V-7 oval in France?", "¿Necesita el óvalo V-7 en Francia un coche con placas de formato UE con la E?",
  [("No", "No"), ("Yes, always", "Sí, siempre"), ("Only on motorways", "Solo en autopistas")],
  "The EU plate already shows the nationality.", "La placa UE ya indica la nacionalidad.")
Q("vp8", "plates", "The V-4 plate is carried at the rear by…", "La señal V-4 la llevan detrás…",
  [("certain drivers, special vehicles and vehicles with a special permit", "determinados conductores, vehículos especiales y vehículos con autorización especial"),
   ("all lorries", "todos los camiones"), ("novice drivers only", "solo los conductores noveles")],
  "It shows a speed they must not exceed.", "Indica una velocidad que no deben superar.")
Q("vp9", "plates", "The V-13 plate measures, on a car…", "La placa V-13 mide, en un turismo…",
  [("19.5 cm high by 15 cm wide", "19,5 cm de alto por 15 cm de ancho"), ("13 cm by 10 cm", "13 cm por 10 cm"), ("30 cm by 20 cm", "30 cm por 20 cm")],
  "13 × 10 cm on motorcycles, three-wheelers and quadricycles.", "13 × 10 cm en motos, tres ruedas y cuadriciclos.")
Q("vp10", "plates", "The V-3 signal identifies…", "La señal V-3 identifica…",
  [("a police vehicle not on urgent service", "un vehículo de policía en servicio no urgente"), ("a police vehicle on urgent service", "un vehículo de policía en servicio urgente"), ("an escort vehicle", "un vehículo de acompañamiento")],
  "Lettering of the force on the sides.", "Rotulación del Cuerpo en los costados.")

# ---------------------------------------------------------------- plates V-14 to V-27
Q("vq1", "plates2", "What does the V-20 panel indicate?", "¿Qué indica el panel V-20?",
  [("The load sticks out at the rear", "Que la carga sobresale por detrás"), ("A slow vehicle", "Un vehículo lento"), ("A vehicle-obstacle", "Un vehículo-obstáculo")],
  "Red and white diagonal stripes.", "Franjas diagonales rojas y blancas.")
Q("vq2", "plates2", "Where does the V-25 environmental label go?", "¿Dónde se coloca el distintivo ambiental V-25?",
  [("Inside the windscreen, lower right corner", "En el ángulo inferior derecho del parabrisas, por dentro"), ("Lower left corner of the windscreen", "En el ángulo inferior izquierdo del parabrisas"),
   ("On the rear window", "En la luna trasera")],
  "If there is no windscreen, somewhere clearly visible.", "Si no hay parabrisas, en sitio bien visible.")
Q("vq3", "plates2", "The V-16 signal indicates…", "La señal V-16 indica…",
  [("a vehicle immobilised on the carriageway, or its load fallen on it", "vehículo inmovilizado en la calzada o carga caída en ella"), ("a vehicle-obstacle at work", "vehículo-obstáculo trabajando"),
   ("a slow vehicle", "vehículo lento")],
  "The connected warning light.", "La baliza luminosa conectada.")
Q("vq4", "plates2", "The V-17 light on a taxi means…", "La luz V-17 de un taxi indica…",
  [("it is free for hire", "que está libre para ser alquilado"), ("the meter is running", "que el taxímetro está en marcha"), ("it is on urgent service", "que está en servicio urgente")],
  "V-18 lights the taximeter.", "La V-18 ilumina el taxímetro.")
Q("vq5", "plates2", "A vehicle escorting a group of cyclists carries…", "Un vehículo que acompaña a un grupo de ciclistas lleva…",
  [("the V-22 sign, possibly with the V-2", "la señal V-22, que puede ir con la V-2"), ("the V-21 sign", "la señal V-21"), ("the V-1 light", "la luz V-1")],
  "The V-21 is for special transport.", "La V-21 es para transporte especial.")
Q("vq6", "plates2", "The V-27 “virtual triangle”…", "El «triángulo virtual» V-27…",
  [("appears on board connected vehicles to warn of a nearby danger; it is voluntary", "aparece a bordo de vehículos conectados para avisar de un peligro próximo; es voluntario"),
   ("replaces the V-16", "sustituye a la V-16"), ("is a sticker on the rear window", "es un adhesivo en la luna trasera")],
  "The danger is reported to the DGT connected-vehicle platform.", "El peligro se comunica a la plataforma de vehículo conectado de la DGT.")
Q("vq7", "plates2", "The V-23 marking is…", "El distintivo V-23 es…",
  [("reflective contour marking on long, heavy goods vehicles", "un marcado reflectante en vehículos de mercancías largos y pesados"), ("the ITV badge", "el distintivo de la ITV"), ("a shared-use badge", "un distintivo de uso compartido")],
  "On the rear and sides.", "En la parte trasera y lateral.")
Q("vq8", "plates2", "How many blind-spot warning stickers (VEH 21/05) does a large vehicle carry?", "¿Cuántas señales de ángulos muertos (VEH 21/05) lleva un vehículo grande?",
  [("Three: one each side and one at the rear right", "Tres: una a cada lado y una detrás a la derecha"), ("Two, at the rear", "Dos, detrás"), ("One, at the front", "Una, delante")],
  "Refuse trucks carry two at the rear. It is voluntary.", "Los de residuos llevan dos detrás. Es voluntaria.")
Q("vq9", "plates2", "The V-15 plate indicates…", "La señal V-15 indica…",
  [("a driver with reduced mobility", "un conductor con movilidad reducida"), ("a vehicle for disabled passengers only", "un vehículo solo para pasajeros con discapacidad"), ("a learner driver", "un conductor en prácticas")],
  "Front and rear.", "Delante y detrás.")
Q("vq10", "plates2", "The V-19 badge shows…", "El distintivo V-19 indica…",
  [("the vehicle passed its ITV and when the next one is due", "que el vehículo ha superado la ITV y la fecha de la próxima"), ("the environmental label", "la etiqueta ambiental"), ("the insurance", "el seguro")],
  "ITV = periodic technical inspection.", "ITV = inspección técnica periódica.")
