# -*- coding: utf-8 -*-
"""Question bank for the interactive Category A1/A2, Topic 6 page (carrying people and goods). In every question the
FIRST option is the correct one (the page shuffles options when it shows them). Ids must be unique and must not start
with "ai"."""

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
    "people": dict(sec=1, en="Carrying a passenger", es="Llevar pasajero",
        recap=[("No more people than seats, and never over the MMA.", "No más personas que plazas y nunca por encima de la MMA."),
               ("One passenger, if the registration document allows it.", "Un pasajero, si consta en el permiso o licencia de circulación."),
               ("Over 12; over 7 with father, mother, guardian or authorised adult.", "Mayor de 12; mayor de 7 con padre, madre, tutor o adulto autorizado."),
               ("Behind the rider, astride, feet on the footrests; never in front.", "Detrás del conductor, a horcajadas, pies en los reposapiés; nunca delante.")],
        trap=("Putting a small child between the rider and the handlebar.", "Llevar a un niño pequeño entre el conductor y el manillar.")),
    "equip": dict(sec=1, en="Helmet, gloves, shoes, vest", es="Casco, guantes, calzado y chaleco",
        recap=[("Helmet UNECE R22, fastened, every road (rider and passenger).", "Casco UNECE R22 abrochado en todas las vías (conductor y pasajero)."),
               ("Gloves on interurban roads; closed shoes on every road (since 1-10-2026).", "Guantes en interurbanas; calzado cerrado en todas (desde el 1-10-2026)."),
               ("Protective structure + belts on the ITV card: seat belt instead.", "Estructura de autoprotección y cinturones en la ITV: cinturón en su lugar."),
               ("Vest: carried on every motorcycle; worn when off the bike on interurban roads; professionals always.", "Chaleco: en toda moto; puesto al bajarse en interurbana; profesionales siempre.")],
        trap=("Thinking gloves are compulsory in town.", "Pensar que los guantes son obligatorios en ciudad.")),
    "load": dict(sec=2, en="Placing the load", es="Colocar la carga",
        recap=[("Must not compromise stability.", "No comprometer la estabilidad."),
               ("Must not hide lights, plates or arm signals.", "No ocultar luces, placas ni las señales con el brazo."),
               ("Must not drag, fall or shift; no avoidable noise or dust (cover it).", "No arrastrar, caer ni desplazarse; sin ruido ni polvo evitables (cubrirla)."),
               ("On a motorcycle: central rack or two side cases fixed to the frame.", "En moto: portaequipajes central o dos maletas laterales fijadas al chasis.")],
        trap=("Thinking a load may cover the rear light if it is short.", "Pensar que la carga puede tapar la luz trasera si es poco tiempo.")),
    "overhang": dict(sec=2, en="Overhang and signalling", es="Carga que sobresale",
        recap=[("Under 1 m wide: 0.25 m rear, 0.50 m each side of the axis, nothing in front.", "Menos de 1 m de ancho: 0,25 m detrás, 0,50 m a cada lado del eje, nada delante."),
               ("Other vehicles not only for goods: 10 % divisible, 15 % indivisible (rear).", "Otros no exclusivos de mercancías: 10 % divisible, 15 % indivisible (detrás)."),
               ("Protect the end; V-20 at the rear; plus a red light at night.", "Resguardar el extremo; V-20 detrás; de noche, además luz roja."),
               ("Under 1 m wide: no need to signal the rear overhang.", "Menos de 1 m de ancho: no hace falta señalizar lo que sobresale detrás.")],
        trap=("Putting a V-20 on a motorcycle top case that sticks out 20 cm.", "Poner una V-20 en el baúl de una moto que sobresale 20 cm.")),
    "trailer": dict(sec=2, en="Towing a trailer", es="Remolque",
        recap=[("Motorcycles, three-wheelers and mopeds (not bicycles since 2026).", "Motos, tres ruedas y ciclomotores (no las bicicletas desde 2026)."),
               ("Trailer ≤ 50 % of the towing vehicle’s unladen mass.", "Remolque ≤ 50 % de la masa en vacío del tractor."),
               ("By day, good visibility, nobody in the trailer.", "De día, buena visibilidad, sin personas en el remolque."),
               ("Generic out-of-town speeds −10 %; in town, bylaws.", "Velocidades genéricas fuera de poblado −10 %; en poblado, ordenanzas.")],
        trap=("Using the MMA instead of the unladen mass for the 50 %.", "Usar la MMA en vez de la masa en vacío para el 50 %.")),
    "plates": dict(sec=3, en="Signs on vehicles", es="Señales en los vehículos",
        recap=[("V-1 blue: priority vehicle on urgent service. V-2 amber: obstacle or work vehicle ≤ 40 km/h.", "V-1 azul: prioritario en servicio urgente. V-2 amarillo auto: obstáculo o de trabajo a ≤ 40 km/h."),
               ("V-6 over 12 m. V-13 novice (< 1 year): on a motorcycle, anywhere visible at the rear. V-19 ITV. V-20 rear overhang.", "V-6 más de 12 m. V-13 novel (< 1 año): en moto, en un sitio visible de la parte posterior. V-19 ITV. V-20 carga que sobresale."),
               ("V-16: vehicle or load on the carriageway; triangles invalid since 2026; not compulsory on motorcycles.", "V-16: vehículo o carga en la calzada; triángulos sin validez desde 2026; no obligatoria en moto."),
               ("V-25 environmental label (voluntary on motorcycles); V-26 shared use; VEH 21/05 blind spots, voluntary.", "V-25 ambiental (voluntario en moto); V-26 uso compartido; VEH 21/05 ángulos muertos, voluntaria.")],
        trap=("Confusing the V-1 (blue) with the V-2 (amber).", "Confundir la V-1 (azul) con la V-2 (amarillo auto).")),
}

# ---------------------------------------------------------------- people
Q("pp1", "people", "How many passengers may a motorcycle without sidecar carry?", "¿Cuántos pasajeros puede llevar una motocicleta sin sidecar?",
  [("One, if the registration document allows it", "Uno, si consta en el permiso de circulación"), ("Two", "Dos"), ("None", "Ninguno")],
  "Besides the rider.", "Además del conductor.")
Q("pp2", "people", "Minimum age of a passenger on a motorcycle, as a rule:", "Edad mínima del pasajero de una moto, como norma general:",
  [("Over 12", "Mayor de 12 años"), ("Over 7", "Mayor de 7 años"), ("Over 16", "Mayor de 16 años")],
  "Exceptionally over 7.", "Excepcionalmente, mayor de 7.")
Q("pp3", "people", "An 8-year-old may ride as a passenger on a motorcycle if the rider is…", "Un niño de 8 años puede ir de pasajero en moto si conduce…",
  [("their father, mother, guardian or an adult they authorise", "su padre, madre, tutor o un adulto autorizado por ellos"), ("any adult", "cualquier adulto"), ("nobody: they must be over 12", "nadie: debe tener más de 12")],
  "With an approved helmet and meeting the other conditions.", "Con casco homologado y el resto de condiciones.")
Q("pp4", "people", "Where must the passenger sit?", "¿Dónde debe ir el pasajero?",
  [("On the seat behind the rider", "En el asiento detrás del conductor"), ("Between the rider and the handlebar, if a child", "Entre el conductor y el manillar, si es un niño"), ("Wherever there is room", "Donde haya sitio")],
  "Never in an intermediate position.", "Nunca en lugar intermedio.")
Q("pp5", "people", "How must the passenger sit?", "¿Cómo debe ir sentado el pasajero?",
  [("Astride, with feet on the side footrests", "A horcajadas, con los pies en los reposapiés laterales"), ("Side-saddle", "De lado"), ("However is comfortable", "Como le resulte cómodo")],
  "One leg each side.", "Una pierna a cada lado.")
Q("pp6", "people", "Where can you check how many seats your motorcycle has?", "¿Dónde puedes consultar el número de plazas de tu moto?",
  [("On the inspection card or the registration certificate", "En la tarjeta ITV o en el permiso de circulación"), ("On the driving licence", "En el permiso de conducción"), ("On the insurance policy", "En la póliza del seguro")],
  "Also the MMA.", "También la MMA.")
Q("pp7", "people", "Besides the rider, a motorcycle with sidecar may carry…", "Además del conductor, una moto con sidecar puede llevar…",
  [("the sidecar occupant and one passenger", "al ocupante del sidecar y a un pasajero"), ("only the sidecar occupant", "solo al ocupante del sidecar"), ("two passengers on the seat", "dos pasajeros en el asiento")],
  "If the documents allow it.", "Si consta en la documentación.")
Q("pp8", "people", "With a passenger and luggage, which limit must you never exceed?", "Con pasajero y equipaje, ¿qué límite no puedes superar nunca?",
  [("The MMA", "La MMA"), ("The tare", "La tara"), ("The mass in running order", "La masa en orden de marcha")],
  "People count towards the mass.", "Las personas cuentan en la masa.")

# ---------------------------------------------------------------- equipment
Q("eq1", "equip", "Since October 2026, riding a motorcycle on an interurban road, you and your passenger must wear…", "Desde octubre de 2026, en moto por vía interurbana, tú y tu pasajero debéis llevar…",
  [("helmet, protective gloves and closed shoes", "casco, guantes de protección y calzado cerrado"), ("only the helmet", "solo el casco"), ("helmet and vest", "casco y chaleco")],
  "Gloves on interurban roads; helmet and shoes on every road.", "Guantes en interurbanas; casco y calzado en todas.")
Q("eq2", "equip", "In town, on a motorcycle, are protective gloves compulsory?", "En ciudad, en moto, ¿son obligatorios los guantes de protección?",
  [("No, only on interurban roads", "No, solo en vías interurbanas"), ("Yes, always", "Sí, siempre"), ("Only for the passenger", "Solo para el pasajero")],
  "Recommended anyway.", "Recomendables de todos modos.")
Q("eq3", "equip", "Closed shoes covering the whole foot are compulsory on a motorcycle…", "El calzado cerrado que cubra todo el pie es obligatorio en moto…",
  [("on every road", "en todas las vías"), ("only on interurban roads", "solo en vías interurbanas"), ("only for the rider", "solo para el conductor")],
  "Since 1 October 2026.", "Desde el 1 de octubre de 2026.")
Q("eq4", "equip", "The motorcycle helmet must be approved according to…", "El casco de moto debe estar homologado según…",
  [("UNECE Regulation R22", "el Reglamento UNECE R22"), ("UNECE R44", "el Reglamento UNECE R44"), ("No standard is required", "No se exige norma")],
  "And properly fastened.", "Y correctamente abrochado.")
Q("eq5", "equip", "A quadricycle with a protective structure and seat belts, as stated on its ITV card. Its occupants…", "Un cuadriciclo con estructura de autoprotección y cinturones, según su tarjeta ITV. Sus ocupantes…",
  [("wear the seat belt instead of the helmet", "usan el cinturón en lugar del casco"), ("wear helmet and belt", "usan casco y cinturón"), ("need neither", "no necesitan ninguno")],
  "Also exempt from gloves and closed shoes.", "También quedan exentos de guantes y calzado.")
Q("eq6", "equip", "Until when may moped users keep wearing certified (not approved) helmets?", "¿Hasta cuándo pueden usarse en ciclomotor cascos certificados (no homologados)?",
  [("1 October 2027", "Hasta el 1 de octubre de 2027"), ("Indefinitely", "Indefinidamente"), ("1 January 2026", "Hasta el 1 de enero de 2026")],
  "A one-year transitional period.", "Un periodo transitorio de un año.")
Q("eq7", "equip", "Your motorcycle breaks down on an interurban road and you get off onto the shoulder. You must…", "Tu moto se avería en vía interurbana y te bajas al arcén. Debes…",
  [("wear the high-visibility vest", "ponerte el chaleco de alta visibilidad"), ("place two triangles", "colocar dos triángulos"), ("take off the helmet", "quitarte el casco")],
  "Every motorcycle must carry one since October 2026.", "Toda moto debe llevarlo desde octubre de 2026.")
Q("eq8", "equip", "A delivery rider working on a motorcycle in town must wear the vest…", "Un repartidor que trabaja en moto en ciudad debe llevar el chaleco…",
  [("at all times, on every road", "siempre, en todas las vías"), ("only on interurban roads", "solo en interurbanas"), ("only at night", "solo de noche")],
  "Riders who work on the vehicle.", "Quien circula por su actividad profesional.")
Q("eq9", "equip", "Must the passenger also wear the helmet?", "¿Debe llevar casco también el pasajero?",
  [("Yes, approved and fastened", "Sí, homologado y abrochado"), ("Only out of town", "Solo fuera de poblado"), ("Only if under 18", "Solo si es menor de 18")],
  "Rider and passenger.", "Conductor y pasajero.")

# ---------------------------------------------------------------- load
Q("ld1", "load", "Where should a load go on a two-wheeled motorcycle?", "¿Dónde debe ir la carga en una moto de dos ruedas?",
  [("On the central rear rack or in two side cases fixed to the frame", "En el portaequipajes central o en dos maletas laterales fijadas al chasis"), ("On the fuel tank", "Sobre el depósito"), ("Held by the passenger", "Sujeta por el pasajero")],
  "Well placed and secured.", "Bien colocada y sujeta.")
Q("ld2", "load", "A load must never…", "La carga nunca debe…",
  [("hide the lights or the number plate", "ocultar las luces ni la placa de matrícula"), ("be in a top case", "ir en un baúl"), ("weigh more than 5 kg", "pesar más de 5 kg")],
  "Nor the rider’s arm signals.", "Ni las advertencias con el brazo.")
Q("ld3", "load", "A load that makes dust or may fall must be…", "Una carga que produce polvo o puede caer debe…",
  [("fully and effectively covered", "cubrirse total y eficazmente"), ("carried only at night", "llevarse solo de noche"), ("signalled with a V-20", "señalizarse con la V-20")],
  "To avoid dangers and nuisance.", "Para evitar peligros y molestias.")
Q("ld4", "load", "Which of these is a load placement rule?", "¿Cuál de estas es una norma de colocación de la carga?",
  [("It must not compromise the vehicle’s stability", "No debe comprometer la estabilidad del vehículo"), ("It must be on the left side", "Debe ir en el lado izquierdo"), ("It must be red", "Debe ser de color rojo")],
  "Nor drag, fall or shift.", "Ni arrastrar, caer o desplazarse.")
Q("ld5", "load", "Badly loaded side cases make the motorcycle lean to one side. This breaks the rule that the load must not…", "Unas maletas mal cargadas hacen que la moto se incline a un lado. Esto incumple que la carga no debe…",
  [("compromise stability", "comprometer la estabilidad"), ("make noise", "producir ruido"), ("hide the lights", "ocultar las luces")],
  "Balance the load on both sides.", "Reparte la carga en ambos lados.")

# ---------------------------------------------------------------- overhang
Q("oh1", "overhang", "On a vehicle less than 1 m wide, the load may stick out at the rear…", "En un vehículo de menos de 1 m de ancho, la carga puede sobresalir por detrás…",
  [("0.25 m", "0,25 m"), ("0.50 m", "0,50 m"), ("1 m", "1 m")],
  "And nothing at the front.", "Y nada por delante.")
Q("oh2", "overhang", "On a motorcycle, how far may a load stick out sideways?", "En una moto, ¿cuánto puede sobresalir la carga lateralmente?",
  [("0.50 m each side of its long axis", "0,50 m a cada lado de su eje longitudinal"), ("0.25 m each side", "0,25 m a cada lado"), ("It may not stick out sideways", "No puede sobresalir lateralmente")],
  "So the total width stays within 1 m.", "La anchura total no supera 1 m.")
Q("oh3", "overhang", "On a motorcycle, may the load stick out at the front?", "En una moto, ¿puede sobresalir la carga por delante?",
  [("No", "No"), ("Up to 0.25 m", "Hasta 0,25 m"), ("Up to 0.50 m", "Hasta 0,50 m")],
  "Never at the front.", "Nunca por la parte delantera.")
Q("oh4", "overhang", "Your top case sticks out 0.20 m behind the motorcycle. Must you signal it with a V-20?", "Tu baúl sobresale 0,20 m por detrás de la moto. ¿Debes señalizarlo con la V-20?",
  [("No, vehicles under 1 m wide don’t need to", "No, los vehículos de menos de 1 m de ancho no lo necesitan"), ("Yes, always", "Sí, siempre"), ("Only at night", "Solo de noche")],
  "It is within the 0.25 m allowed.", "Está dentro de los 0,25 m permitidos.")
Q("oh5", "overhang", "On a car (not a goods vehicle), a divisible load may stick out at the rear up to…", "En un turismo (no de mercancías), una carga divisible puede sobresalir por detrás hasta…",
  [("10 % of its length", "el 10 % de su longitud"), ("15 % of its length", "el 15 % de su longitud"), ("1 m", "1 m")],
  "Indivisible: 15 %.", "Indivisible: 15 %.")
Q("oh6", "overhang", "A load sticking out at the rear, at night, on a vehicle where it must be signalled, carries…", "Una carga que sobresale por detrás, de noche, en un vehículo que debe señalizarla, lleva…",
  [("the V-20 panel and a red light", "el panel V-20 y una luz roja"), ("only the V-20 panel", "solo el panel V-20"), ("a white light", "una luz blanca")],
  "By day, the panel alone.", "De día, solo el panel.")
Q("oh7", "overhang", "Besides signalling it, the end of a load that sticks out must be…", "Además de señalizarla, el extremo de una carga que sobresale debe…",
  [("protected to soften any rub or knock", "ir resguardado para aminorar los efectos de un roce o choque"), ("painted red", "pintarse de rojo"), ("tied with rope only", "atarse solo con cuerda")],
  "To avoid harm to others.", "Para evitar daños a los demás.")

# ---------------------------------------------------------------- trailer
Q("tr1", "trailer", "May a motorcycle tow a trailer?", "¿Puede una motocicleta arrastrar un remolque?",
  [("Yes, under certain conditions", "Sí, con ciertas condiciones"), ("No, never", "No, nunca"), ("Only in town", "Solo en poblado")],
  "Mass, daytime, speed and no people.", "Masa, de día, velocidad y sin personas.")
Q("tr2", "trailer", "The trailer of a motorcycle may weigh at most…", "El remolque de una moto puede pesar como máximo…",
  [("50 % of the motorcycle’s unladen mass", "el 50 % de la masa en vacío de la moto"), ("50 % of its MMA", "el 50 % de su MMA"), ("750 kg", "750 kg")],
  "Unladen mass of the towing vehicle.", "Masa en vacío del vehículo tractor.")
Q("tr3", "trailer", "A motorcycle towing a trailer out of town must…", "Una moto con remolque fuera de poblado debe…",
  [("reduce its generic speeds by 10 %", "reducir un 10 % sus velocidades genéricas"), ("reduce them by 10 km/h", "reducirlas 10 km/h"), ("keep the same speeds", "mantener las mismas velocidades")],
  "Per cent, not km/h.", "Por ciento, no km/h.")
Q("tr4", "trailer", "May a child travel in the trailer of a motorcycle?", "¿Puede viajar un niño en el remolque de una moto?",
  [("No, never", "No, nunca"), ("Yes, with a helmet", "Sí, con casco"), ("Yes, in town", "Sí, en poblado")],
  "Never people in the towed vehicle.", "Nunca personas en el vehículo remolcado.")
Q("tr5", "trailer", "At night, may a moped tow a trailer?", "De noche, ¿puede un ciclomotor arrastrar un remolque?",
  [("No, only by day with good visibility", "No, solo de día y con buena visibilidad"), ("Yes, with the lights on", "Sí, con las luces encendidas"), ("Yes, in town", "Sí, en poblado")],
  "In town, local bylaws apply.", "En poblado, las ordenanzas municipales.")
Q("tr6", "trailer", "Since October 2026, which of these is NOT covered by the motorcycle trailer rule (−10 %, 50 %)?", "Desde octubre de 2026, ¿cuál NO está en la norma de remolque de las motos (−10 %, 50 %)?",
  [("Bicycles", "Las bicicletas"), ("Mopeds", "Los ciclomotores"), ("Three-wheeled vehicles", "Los vehículos de tres ruedas")],
  "Bicycles have their own trailer rules now. Your course still lists cycles.", "Las bicicletas tienen ahora sus propias normas. Tu curso aún incluye los ciclos.")

# ---------------------------------------------------------------- plates
Q("vp1", "plates", "The V-1 sign (priority vehicle) consists of…", "La señal V-1 (vehículo prioritario) consiste en…",
  [("one or more blue lights", "una o varias luces azules"), ("one or more amber lights", "una o varias luces amarillo auto"), ("a red flashing light", "una luz roja intermitente")],
  "Police, fire, civil protection, ambulance on urgent service.", "Policía, bomberos, protección civil, asistencia sanitaria en servicio urgente.")
Q("vp2", "plates", "An amber rotating light (V-2) on a vehicle working at the roadside means…", "Una luz giratoria amarillo auto (V-2) en un vehículo trabajando junto a la vía indica…",
  [("a vehicle-obstacle: stopped, parked or going at no more than 40 km/h", "vehículo-obstáculo: parado, estacionado o a no más de 40 km/h"), ("a priority vehicle", "un vehículo prioritario"), ("a long vehicle", "un vehículo largo")],
  "Also special transport and escorts.", "También transporte especial y acompañamiento.")
Q("vp3", "plates", "The V-6 sign is carried by vehicles or combinations longer than…", "La señal V-6 la llevan los vehículos o conjuntos de más de…",
  [("12 m", "12 m"), ("10 m", "10 m"), ("18.75 m", "18,75 m")],
  "Long vehicle.", "Vehículo largo.")
Q("vp4", "plates", "On a motorcycle, the V-13 (novice) sign goes…", "En una moto, la señal V-13 (novel) va…",
  [("somewhere visible at the rear", "en un sitio visible de la parte posterior"), ("at the front", "en la parte delantera"), ("on the helmet", "en el casco")],
  "On a car it goes at the rear left; on a motorcycle it is enough to place it somewhere visible at the rear, in a smaller size (10 × 13 cm).", "En un turismo va detrás a la izquierda; en moto basta colocarla en un sitio visible de la parte posterior, en tamaño reducido (10 × 13 cm).")
Q("vp5", "plates", "The V-13 means the driver’s licence is…", "La señal V-13 indica que el permiso del conductor tiene…",
  [("less than one year old", "menos de un año de antigüedad"), ("less than two years old", "menos de dos años"), ("a learner’s permit", "un permiso de aprendizaje")],
  "Novice driver.", "Conductor novel.")
Q("vp6", "plates", "Since 1 January 2026, are warning triangles still valid instead of the V-16?", "Desde el 1 de enero de 2026, ¿siguen valiendo los triángulos en lugar de la V-16?",
  [("No, only the connected V-16", "No, solo la V-16 conectada"), ("Yes, as an alternative", "Sí, como alternativa"), ("Yes, on motorways", "Sí, en autopistas")],
  "The V-16 is not compulsory on motorcycles.", "La V-16 no es obligatoria en motos.")
Q("vp7", "plates", "The V-16 tells others that…", "La V-16 indica que…",
  [("the vehicle is immobilised on the carriageway or its load is on it", "el vehículo está inmovilizado en la calzada o su carga está sobre ella"), ("the vehicle is slow", "el vehículo es lento"), ("the driver is a novice", "el conductor es novel")],
  "Warning device.", "Dispositivo de preseñalización de peligro.")
Q("vp8", "plates", "Is it compulsory to display the environmental label (V-25) on a motorcycle?", "¿Es obligatorio colocar el distintivo ambiental (V-25) en una moto?",
  [("No, it is recommended on the screen or another visible place", "No, se recomienda en la cúpula o en otro lugar visible"), ("Yes, on the number plate", "Sí, en la placa de matrícula"), ("Yes, on the helmet", "Sí, en el casco")],
  "A recommendation, not an obligation.", "Es una recomendación, no una obligación.")
Q("vp9", "plates", "The V-19 badge shows that…", "El distintivo V-19 indica que…",
  [("the vehicle passed its periodic inspection, and when the next is due", "el vehículo ha superado la ITV y la fecha de la próxima"), ("the vehicle is insured", "el vehículo está asegurado"), ("the vehicle is for hire", "el vehículo es de alquiler")],
  "ITV badge.", "Distintivo de ITV.")
Q("vp10", "plates", "The V-26 badge identifies…", "El distintivo V-26 identifica…",
  [("a shared-use vehicle (car sharing)", "un vehículo de uso compartido"), ("a taxi", "un taxi"), ("a school bus", "un autobús escolar")],
  "Self-drive rental used by many users in a set zone.", "Alquiler sin conductor de uso concatenado en una zona delimitada.")
Q("vp11", "plates", "The VEH 21/05 blind-spot sticker is…", "La señal adhesiva VEH 21/05 de ángulos muertos es…",
  [("voluntary, to warn vulnerable users such as motorcyclists", "voluntaria, para advertir a usuarios vulnerables como los motoristas"), ("compulsory on all lorries", "obligatoria en todos los camiones"), ("compulsory on motorcycles", "obligatoria en las motos")],
  "Three per vehicle.", "Tres por vehículo.")
Q("vp12", "plates", "A red-and-white striped square panel at the rear of a load is the…", "Un panel cuadrado con franjas rojas y blancas en el extremo de una carga es la…",
  [("V-20", "V-20"), ("V-2", "V-2"), ("V-6", "V-6")],
  "Load that sticks out.", "Carga que sobresale.")

# ---------------------------------------------------------------- more practice
Q("pp9", "people", "May a moped carry a passenger?", "¿Puede un ciclomotor llevar pasajero?",
  [("Yes, with the same conditions as a motorcycle, if its licence allows it", "Sí, con las mismas condiciones que la moto, si consta en su licencia"), ("No, never", "No, nunca"), ("Only children", "Solo niños")],
  "Over 12, behind the rider, astride, helmet.", "Mayor de 12, detrás, a horcajadas, con casco.")
Q("pp10", "people", "Your motorcycle’s documents allow only one seat. May you carry a passenger?", "La documentación de tu moto solo admite una plaza. ¿Puedes llevar pasajero?",
  [("No", "No"), ("Yes, if the passenger is light", "Sí, si el pasajero pesa poco"), ("Yes, in town", "Sí, en poblado")],
  "It must be stated on the registration document.", "Debe constar en el permiso de circulación.")
Q("pp11", "people", "May the passenger carry a small child between themselves and the rider?", "¿Puede el pasajero llevar a un niño pequeño entre él y el conductor?",
  [("No: at most one passenger", "No: como máximo un pasajero"), ("Yes, if under 7", "Sí, si es menor de 7"), ("Yes, with a helmet", "Sí, con casco")],
  "Besides the rider and the sidecar occupant, one passenger only.", "Además del conductor y del ocupante del sidecar, solo un pasajero.")
Q("eq10", "equip", "Must the passenger also wear gloves on an interurban road?", "¿Debe llevar guantes también el pasajero en vía interurbana?",
  [("Yes, riders and passengers", "Sí, conductores y pasajeros"), ("No, only the rider", "No, solo el conductor"), ("Only at night", "Solo de noche")],
  "Since 1 October 2026.", "Desde el 1 de octubre de 2026.")
Q("eq11", "equip", "Who must wear a helmet among these?", "¿Quién debe llevar casco entre estos?",
  [("The rider of a quad approved as a special vehicle", "El conductor de un quad homologado como vehículo especial"), ("A car driver", "El conductor de un turismo"), ("A bus passenger", "Un pasajero de autobús")],
  "Motorcycles, three-wheelers, quadricycles, mopeds and quads.", "Motos, tres ruedas, cuadriciclos, ciclomotores y quads.")
Q("eq12", "equip", "A helmet worn but unfastened…", "Un casco puesto pero sin abrochar…",
  [("does not meet the rule: it must be properly fastened", "no cumple la norma: debe ir correctamente abrochado"), ("is enough in town", "basta en ciudad"), ("is enough below 30 km/h", "basta por debajo de 30 km/h")],
  "An unfastened helmet can come off in a fall.", "Un casco sin abrochar puede salir despedido en una caída.")
Q("ld6", "load", "At night, a bag on your rack hides the rear light. This is…", "De noche, una bolsa en tu portaequipajes tapa la luz trasera. Esto está…",
  [("forbidden", "prohibido"), ("allowed if the bag is small", "permitido si la bolsa es pequeña"), ("allowed in town", "permitido en poblado")],
  "The load must not hide lights or plates.", "La carga no debe ocultar luces ni placas.")
Q("oh8", "overhang", "On a vehicle less than 1 m wide, the total width including the load may not exceed…", "En un vehículo de menos de 1 m de ancho, la anchura total con la carga no puede superar…",
  [("1 m", "1 m"), ("1.5 m", "1,5 m"), ("0.75 m", "0,75 m")],
  "0.50 m each side of the axis.", "0,50 m a cada lado del eje.")
Q("oh9", "overhang", "On a car, an indivisible load may stick out at the rear up to…", "En un turismo, una carga indivisible puede sobresalir por detrás hasta…",
  [("15 % of its length", "el 15 % de su longitud"), ("10 % of its length", "el 10 % de su longitud"), ("25 % of its length", "el 25 % de su longitud")],
  "Divisible: 10 %.", "Divisible: 10 %.")
Q("tr7", "trailer", "In town, the rules for a moped towing a trailer are set by…", "En poblado, las normas del ciclomotor con remolque las fijan…",
  [("the municipal bylaws", "las ordenanzas municipales"), ("the DGT, for each street", "la DGT, calle a calle"), ("nobody: they are banned", "nadie: están prohibidos")],
  "Out of town: the −10 % rule.", "Fuera de poblado: la regla del −10 %.")
Q("vp13", "plates", "The V-2 may also be used by…", "La V-2 también la pueden usar…",
  [("escort vehicles of cycling marches and sports events", "los vehículos de acompañamiento de marchas ciclistas y pruebas deportivas"), ("taxis", "los taxis"), ("novice drivers", "los conductores noveles")],
  "Also special transport and military columns.", "También transporte especial y columnas militares.")
Q("vp14", "plates", "On a car with a windscreen, the V-25 environmental label goes…", "En un turismo con parabrisas, el distintivo ambiental V-25 va…",
  [("in the lower right corner, on the inside", "en el ángulo inferior derecho, por dentro"), ("on the number plate", "en la placa de matrícula"), ("on the rear window", "en la luna trasera")],
  "Without a windscreen, somewhere clearly visible.", "Sin parabrisas, en sitio bien visible.")
Q("vp15", "plates", "How many VEH 21/05 blind-spot stickers does a vehicle carry?", "¿Cuántas señales VEH 21/05 de ángulos muertos lleva un vehículo?",
  [("Three: one each side and one at the rear right", "Tres: una a cada lado y una detrás a la derecha"), ("One at the rear", "Una detrás"), ("Four, one per corner", "Cuatro, una por esquina")],
  "Refuse trucks: two at the rear.", "Vehículos de residuos: dos detrás.")
