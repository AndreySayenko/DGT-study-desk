# -*- coding: utf-8 -*-
"""Question bank for the interactive Category A1/A2, Topic 11 page (first aid). In every question the FIRST option is
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
    "duty": dict(sec=1, en="The duty to help", es="Deber de ayudar",
        recap=[("Involved users, and those who know of the accident, must help or call for help.", "Los implicados, y quienes tengan conocimiento del accidente, deben auxiliar o pedir auxilio."),
               ("Not helping is a crime: failure to help (omisión del deber de socorro).", "No prestar auxilio es delito: omisión del deber de socorro."),
               ("Non-involved users may go on if agents are there or help is clearly not needed.", "Los no implicados pueden seguir si ya están los agentes o su ayuda claramente no hace falta."),
               ("Deaths or serious injuries: don’t change the evidence, call the agents and stay.", "Muertos o heridos graves: no alterar las pruebas, avisar a los agentes y permanecer.")],
        trap=("Driving on because you were not involved, when nobody has helped yet.", "Seguir la marcha porque no estabas implicado, cuando nadie ha ayudado todavía.")),
    "protect": dict(sec=2, en="PAS: protect", es="PAS: proteger",
        recap=[("Order: protect yourself, the scene, the victims.", "Orden: autoprotegerse, proteger el lugar, proteger a las víctimas."),
               ("Motorcycle off the carriageway, engine off; V-16 optional; hazard lights if fitted.", "Moto fuera de la calzada, motor parado; V-16 opcional; luces de emergencia si las tiene."),
               ("Vest (compulsory equipment since 1-10-2026) on before walking on an interurban road.", "Chaleco (obligatorio desde el 1-10-2026) puesto antes de caminar por una interurbana."),
               ("Fire: extinguisher at the base, or sand or blankets, never water.", "Fuego: extintor en la base, o arena o mantas, nunca agua.")],
        trap=("Thinking the vest is only advisable on a motorcycle.", "Pensar que en moto el chaleco solo es recomendable.")),
    "alert": dict(sec=2, en="PAS: alert", es="PAS: avisar",
        recap=[("112: free, works without credit, the same in the whole EU.", "112: gratuito, funciona sin saldo y es común en toda la UE."),
               ("Say where, how many injured and in what state, what happened, and who you are.", "Decir dónde, cuántos heridos y cómo están, qué ha pasado y quién eres."),
               ("No need to alert or stay only if injuries are clearly minor, safety is restored and nobody asks.", "No hace falta avisar ni quedarse solo si las heridas son leves, la seguridad está restablecida y nadie lo pide."),
               ("Give your name and vehicle details to those involved who ask.", "Dar tus datos y los del vehículo a los implicados que los pidan.")],
        trap=("Leaving because the injuries look minor though someone asks you to stay.", "Marcharse porque las heridas parecen leves aunque alguien pide que te quedes.")),
    "help": dict(sec=2, en="PAS: help", es="PAS: socorrer",
        recap=[("Only as far as you know how; if unsure, wait for the medical team.", "Solo en la medida en que sepas; si dudas, espera a la ayuda sanitaria."),
               ("Keep calm; seriousness decides the order; don’t move them unless essential.", "Calma; el orden lo marca la gravedad; no moverlos salvo que sea imprescindible."),
               ("Loosen tight clothing, cover them even in summer.", "Aflojar la ropa que oprima, taparlos incluso en verano."),
               ("Never food, drink or medicines; don’t touch wounds or burns.", "Nunca comida, bebida ni medicamentos; no tocar heridas ni quemaduras.")],
        trap=("Giving water to a thirsty injured person.", "Dar agua a un herido que tiene sed.")),
    "assess": dict(sec=3, en="Initial assessment and ABC", es="Valoración inicial y ABC",
        recap=[("Assess all the injured first, 10–15 seconds each.", "Valorar a todos los heridos primero, 10–15 segundos cada uno."),
               ("Conscious: answers or reacts to pain. Unconscious: apply ABC.", "Consciente: contesta o reacciona al dolor. Inconsciente: regla ABC."),
               ("A: head-tilt, chin-lift; B: see, feel, hear; C: no breathing or pulse → CPR.", "A: frente-mentón; B: ver, sentir, oír; C: sin respiración o pulso → RCP."),
               ("Noisy breathing: airway partly blocked; irregular: possible brain damage.", "Respiración ruidosa: vía parcialmente obstruida; irregular: posible daño cerebral.")],
        trap=("Starting to treat the first injured person before looking at the others.", "Empezar a atender al primer herido antes de valorar a los demás.")),
    "helmet": dict(sec=3, en="The injured rider’s helmet", es="El casco del motorista herido",
        recap=[("Leave the helmet on: possible neck or spine injury.", "No quitar el casco: posible lesión en cuello o columna."),
               ("Check breathing and the carotid pulse with the helmet on.", "Comprobar respiración y pulso carotídeo con el casco puesto."),
               ("Off only if essential, for example for CPR.", "Quitarlo solo si es imprescindible, por ejemplo para la RCP."),
               ("At least two people who know how; neck–head–trunk kept in line.", "Mínimo dos personas que sepan; eje cuello-cabeza-tronco alineado.")],
        trap=("Taking the helmet off a conscious rider “so they can breathe better”.", "Quitar el casco a un motorista consciente «para que respire mejor».")),
    "recovery": dict(sec=4, en="Breathing casualties and the recovery position", es="Heridos que respiran y PLS",
        recap=[("Conscious and breathing: check for serious injuries and keep watching.", "Consciente que respira: descartar lesiones graves y seguir vigilándolo."),
               ("Unconscious and breathing: recovery position if left alone or vomiting or bleeding from mouth or nose.", "Inconsciente que respira: PLS si se le deja solo o vomita o sangra por boca o nariz."),
               ("Bleeding from an ear: lie them on that ear.", "Sangra por un oído: sobre ese lado."),
               ("Check breathing every 2–3 minutes.", "Comprobar la respiración cada 2–3 minutos.")],
        trap=("Putting someone with a bleeding ear on the other side.", "Colocar sobre el otro lado a quien sangra por un oído.")),
    "cpr": dict(sec=4, en="CPR", es="RCP",
        recap=[("Unconscious and not breathing: CPR at once, on a hard, flat surface.", "Inconsciente que no respira: RCP inmediata, sobre superficie dura y plana."),
               ("Heels of the hands in the centre of the chest, arms straight; 30 compressions, 2 breaths.", "Talones de las manos en el centro del pecho, brazos rectos; 30 compresiones y 2 ventilaciones."),
               ("Course: 4–5 cm, about 100 a minute; ERC 2025: 5–6 cm, 100–120.", "Curso: 4–5 cm, unas 100 por minuto; ERC 2025: 5–6 cm, 100–120."),
               ("Children: 5 breaths first; babies: two fingers.", "Niños: 5 ventilaciones iniciales; bebés: dos dedos.")],
        trap=("Bending the arms during the compressions.", "Doblar los brazos durante las compresiones.")),
    "bleed": dict(sec=4, en="Bleeding and shock", es="Hemorragias y shock",
        recap=[("Press on the wound; a soaked gauze stays, another goes on top.", "Presionar sobre la herida; la gasa empapada se queda y se pone otra encima."),
               ("Course: raise the limb and press the armpit or groin; tourniquet last.", "Curso: elevar el miembro y presionar en axila o ingle; torniquete al final."),
               ("Tourniquet: don’t loosen, visible, note the time.", "Torniquete: no aflojar, visible y anotar la hora."),
               ("Shock: cold sweat, pale, fast weak pulse; anti-shock position, covered, nothing to drink.", "Shock: sudor frío, palidez, pulso rápido y débil; posición antishock, tapado, sin bebidas.")],
        trap=("Removing the soaked gauze to put a clean one.", "Quitar la gasa empapada para poner una limpia.")),
    "injury": dict(sec=5, en="Fractures, wounds, burns, fire", es="Fracturas, heridas, quemaduras, fuego",
        recap=[("Fractures: don’t set them; immobilise both ends.", "Fracturas: no reducirlas; inmovilizar los dos extremos."),
               ("Wounds: sterile dressing; embedded objects stay in.", "Heridas: apósito estéril; los objetos clavados no se retiran."),
               ("Burns: cold water, damp sterile dressings, no creams, don’t burst blisters.", "Quemaduras: agua fría, apósitos estériles húmedos, sin pomadas, sin pinchar ampollas."),
               ("Person on fire: blanket or roll; extinguisher never at the face.", "Persona en llamas: manta o rodar; extintor nunca a la cara.")],
        trap=("Pulling out an object embedded in a wound.", "Sacar un objeto clavado en una herida.")),
    "transport": dict(sec=6, en="Moving the injured and the first-aid kit", es="Traslado y botiquín",
        recap=[("Wait for the ambulance.", "Esperar a la ambulancia."),
               ("Private vehicle only exceptionally: no way to call, or help over 30 minutes late and getting worse.", "Vehículo particular solo excepcionalmente: sin forma de avisar, o la ayuda tarda más de 30 minutos y empeora."),
               ("Keep the head–neck–trunk line; go with the injured; warn others, keep the rules.", "Eje cabeza-cuello-tronco; acompañar al herido; advertir a los demás y respetar las normas."),
               ("A first-aid kit is recommended, not compulsory.", "El botiquín es recomendable, no obligatorio.")],
        trap=("Thinking a non-priority vehicle carrying an injured person may ignore the rules.", "Pensar que un vehículo no prioritario con un herido puede saltarse las normas.")),
}

# ---------------------------------------------------------------- 1 duty
Q("du1", "duty", "Who must help, or call for help, at a road accident?", "¿Quién debe auxiliar, o pedir auxilio, en un accidente de tráfico?",
  [("Those involved, and those who know about it even if not involved", "Los implicados, y quienes tengan conocimiento de él aunque no estén implicados"), ("Only those involved", "Solo los implicados"), ("Only the agents and the medical services", "Solo los agentes y los sanitarios")],
  "Users involved in an accident, or who know about it, must help or ask for help.", "Los usuarios implicados, o que tengan conocimiento del accidente, deben auxiliar o solicitar auxilio.")
Q("du2", "duty", "What is failing to help a seriously injured person who needs it?", "¿Qué es no ayudar a un herido grave que lo necesita?",
  [("A crime: failure to help (omisión del deber de socorro)", "Un delito: omisión del deber de socorro"), ("A minor administrative offence", "Una infracción administrativa leve"), ("Nothing, if you were not involved", "Nada, si no estabas implicado")],
  "The Código Penal punishes not helping a person in serious danger when you could do so without risk.", "El Código Penal castiga no socorrer a una persona en peligro grave pudiendo hacerlo sin riesgo.")
Q("du3", "duty", "You come across an accident on your motorcycle and the Guardia Civil are already dealing with it. Must you stop?", "Encuentras en moto un accidente y la Guardia Civil ya lo está atendiendo. ¿Debes parar?",
  [("No: non-involved users may carry on if the agents are already there", "No: los no implicados pueden seguir si ya están los agentes"), ("Yes, always", "Sí, siempre"), ("Yes, to give your details", "Sí, para dar tus datos")],
  "Non-involved users need not act when the authorities are there or their help is clearly not needed.", "Los no implicados no están obligados si ya se ha personado la Autoridad o claramente no hace falta su colaboración.")
Q("du4", "duty", "In an accident with someone seriously injured, what must you avoid?", "En un accidente con un herido grave, ¿qué debes evitar?",
  [("Changing the state of things, the marks or other evidence, unless safety requires it", "Modificar el estado de las cosas, las huellas u otras pruebas, salvo que lo exija la seguridad"), ("Calling 112", "Llamar al 112"), ("Staying at the scene", "Permanecer en el lugar")],
  "The evidence helps establish responsibility; you must call the agents and stay.", "Las pruebas ayudan a determinar la responsabilidad; hay que avisar a los agentes y permanecer.")
Q("du5", "duty", "The agents ask you, as a witness, how the accident happened. Must you collaborate?", "Los agentes te piden, como testigo, que expliques cómo ocurrió el accidente. ¿Debes colaborar?",
  [("Yes: help clarify the facts and collaborate with the authority", "Sí: hay que esclarecer los hechos y colaborar con la Autoridad"), ("No, only those involved", "No, solo los implicados"), ("Only if they are local police", "Solo si son policía local")],
  "Those obliged to help must also avoid dangers, restore safety, clarify the facts and collaborate.", "Los obligados deben además evitar peligros, restablecer la seguridad, esclarecer los hechos y colaborar.")
Q("du6", "duty", "After a crash with only minor damage, what is the sensible thing to do?", "Tras un choque solo con pequeños daños materiales, ¿qué es lo acertado?",
  [("Agree with the other party and fill in the accident report form somewhere safe, off the road", "Llegar a un acuerdo y rellenar el parte amistoso en un lugar seguro fuera de la vía"),
   ("Fill in the form in the middle of the carriageway", "Rellenar el parte en mitad de la calzada"), ("Leave without exchanging details", "Marcharse sin intercambiar datos")],
  "Give your identity and vehicle details to those involved who ask, and tell the insurers as soon as possible.", "Hay que dar la identidad y los datos del vehículo a los implicados que lo soliciten y comunicarlo a las aseguradoras cuanto antes.")
Q("du7", "duty", "Someone involved in the accident asks for your details. What must you give?", "Un implicado en el accidente te pide tus datos. ¿Qué debes darle?",
  [("Your identity (name, ID) and your vehicle’s (number plate)", "Tu identidad (nombre, DNI) y la del vehículo (matrícula)"), ("Only your phone number", "Solo tu teléfono"), ("Nothing: only the agents may ask", "Nada: solo pueden pedirlos los agentes")],
  "If you must help, give your details to those involved who ask for them.", "Si estás obligado a prestar ayuda, debes comunicar tus datos a los implicados que lo soliciten.")

# ---------------------------------------------------------------- 2.1 protect
Q("pr1", "protect", "What is the first step of the PAS rule?", "¿Cuál es el primer paso de la regla PAS?",
  [("Protect", "Proteger"), ("Alert", "Avisar"), ("Help", "Socorrer")],
  "Protect, alert, help — first protect, so there are no new victims.", "Proteger, avisar, socorrer: primero proteger, para que no haya nuevas víctimas.")
Q("pr2", "protect", "Within “protect”, what comes first?", "Dentro de «proteger», ¿qué va primero?",
  [("Protecting yourself", "Autoprotegerse"), ("Protecting the victims", "Proteger a las víctimas"), ("Calling 112", "Llamar al 112")],
  "Protect yourself, then the scene, then the victims.", "Autoprotegerse, después el lugar y después a las víctimas.")
Q("pr3", "protect", "Where should you leave your motorcycle when you stop to help?", "¿Dónde debes dejar tu moto al parar a ayudar?",
  [("Somewhere safe, off the carriageway if possible, with the engine off", "En un lugar seguro, fuera de la calzada si es posible, con el motor parado"), ("Next to the casualty, on the carriageway", "Junto al herido, en la calzada"), ("Across the lane, to stop traffic", "Atravesada en el carril, para cortar el tráfico")],
  "Stop somewhere safe without blocking traffic, following the rules.", "Detenerse en un lugar seguro, sin obstaculizar y cumpliendo las normas.")
Q("pr4", "protect", "Since 1 October 2026, what does the law say about the reflective vest on a motorcycle?", "Desde el 1 de octubre de 2026, ¿qué dice la norma sobre el chaleco reflectante en moto?",
  [("The motorcycle must carry it, and you wear it when you get off on the carriageway or shoulder of an interurban road", "La moto debe llevarlo, y te lo pones al bajarte en la calzada o el arcén de una interurbana"),
   ("It is only recommended", "Solo es recomendable"), ("It is compulsory only at night", "Solo es obligatorio de noche")],
  "The reform added the vest to the motorcycle’s compulsory equipment.", "La reforma añadió el chaleco a la dotación obligatoria de la motocicleta.")
Q("pr5", "protect", "Is the V-16 warning light compulsory on a motorcycle?", "¿Es obligatoria la luz V-16 en una motocicleta?",
  [("No: recommended, not compulsory", "No: recomendable, no obligatoria"), ("Yes, since 2026", "Sí, desde 2026"), ("Only on motorcycles over 125 cc", "Solo en motos de más de 125 c.c.")],
  "It is compulsory for cars, vans, buses and lorries.", "Es obligatoria en turismos, furgonetas, autobuses y camiones.")
Q("pr6", "protect", "If you carry a V-16, where does your course say to put it on the motorcycle?", "Si llevas una V-16, ¿dónde dice tu curso que hay que colocarla en la moto?",
  [("By hand, on the most visible metal part, before walking away", "Con la mano, sobre la parte metálica más visible, antes de alejarte"), ("On the ground 50 m behind", "En el suelo, 50 m por detrás"), ("Inside the top case", "Dentro del baúl")],
  "The V-16 is placed before leaving the vehicle; it replaced the triangles for cars.", "La V-16 se coloca antes de abandonar el vehículo; sustituyó a los triángulos en los coches.")
Q("pr7", "protect", "A car involved in the accident blocks a lane. What should be done with it?", "Un coche implicado en el accidente obstaculiza un carril. ¿Qué hay que hacer con él?",
  [("Move it off the carriageway if possible, immobilised and with the engine off", "Retirarlo de la calzada si es posible, inmovilizado y con el motor parado"), ("Leave it as it is, always", "Dejarlo siempre como está"), ("Push it into the oncoming lane", "Empujarlo al carril contrario")],
  "Vehicles or load that are an obstacle go to the shoulder or central reservation.", "Los vehículos o la carga que sean un obstáculo se colocan en el arcén o la mediana.")
Q("pr8", "protect", "A crashed vehicle catches fire. How do you fight it?", "Un vehículo accidentado se incendia. ¿Cómo lo apagas?",
  [("Extinguisher at the base of the flames, or sand or blankets — never water", "Extintor sobre la base de las llamas, o arena o mantas, nunca agua"), ("Water on the flames", "Agua sobre las llamas"), ("Extinguisher at the top of the flames", "Extintor a la parte alta de las llamas")],
  "Get the injured out first; never use water.", "Primero sacar a los heridos; nunca usar agua.")
Q("pr9", "protect", "May you smoke while helping at an accident scene?", "¿Puedes fumar mientras ayudas en un accidente?",
  [("No: it is one of the risks to avoid", "No: es uno de los riesgos que hay que evitar"), ("Yes, away from the injured", "Sí, lejos de los heridos"), ("Yes, if there is no fuel spilt", "Sí, si no hay combustible derramado")],
  "Assess other possible risks: don’t smoke.", "Evaluar otros posibles riesgos: no fumar.")

# ---------------------------------------------------------------- 2.2 alert
Q("al1", "alert", "Which number do you call for the emergency services?", "¿Qué número marcas para los servicios de emergencia?",
  [("112", "112"), ("091", "091"), ("060", "060")],
  "112 is free, works without credit and is the same in the whole EU.", "El 112 es gratuito, funciona sin saldo y es común en toda la UE.")
Q("al2", "alert", "Which information should you give 112?", "¿Qué información debes dar al 112?",
  [("Exact place, number and state of the injured, what happened, and your identity and phone", "Lugar exacto, número y estado de los heridos, características del accidente, y tu identidad y teléfono"),
   ("Only the number plates", "Solo las matrículas"), ("Only your name", "Solo tu nombre")],
  "Also mention fire risk or dangerous goods.", "También el riesgo de incendio o las mercancías peligrosas.")
Q("al3", "alert", "Your phone has no credit. Can you call 112?", "Tu móvil no tiene saldo. ¿Puedes llamar al 112?",
  [("Yes: the call is free even without credit", "Sí: es gratuito incluso sin saldo"), ("No", "No"), ("Only from a landline", "Solo desde un fijo")],
  "112 can be called without credit, anywhere in the EU.", "Al 112 se puede llamar sin saldo, en cualquier país de la UE.")
Q("al4", "alert", "When is it not necessary to alert or to stay at the scene?", "¿Cuándo no es necesario avisar ni permanecer en el lugar?",
  [("When there are only clearly minor injuries, safety is restored and nobody involved asks you to", "Si solo hay heridas claramente leves, la seguridad está restablecida y ningún implicado lo solicita"),
   ("When you are in a hurry", "Cuando tienes prisa"), ("When there are no witnesses", "Cuando no hay testigos")],
  "All three conditions must be met.", "Deben cumplirse las tres condiciones.")
Q("al5", "alert", "There are only minor injuries and the road is clear, but one of the people involved asks you to stay. What do you do?", "Solo hay heridas leves y la vía está despejada, pero un implicado te pide que te quedes. ¿Qué haces?",
  [("Stay", "Quedarme"), ("Leave: the injuries are minor", "Marcharme: las heridas son leves"), ("Leave my phone number and go", "Dejar mi teléfono y marcharme")],
  "If any person involved asks, the exception no longer applies.", "Si algún implicado lo solicita, ya no se aplica la excepción.")

# ---------------------------------------------------------------- 2.3 help
Q("hp1", "help", "You are not sure how to help an injured person. What should you do?", "No estás seguro de cómo ayudar a un herido. ¿Qué debes hacer?",
  [("Wait for the medical team: wrong help can make things worse", "Esperar a la ayuda sanitaria: una ayuda inadecuada puede empeorar el resultado"), ("Try anything, it’s better than nothing", "Intentar cualquier cosa, mejor que nada"), ("Move the person to a more comfortable place", "Llevar al herido a un sitio más cómodo")],
  "Be honest about whether you know how to act.", "Hay que ser consciente de si se sabe cómo actuar.")
Q("hp2", "help", "An injured person is cold and asks for something to drink. What do you do?", "Un herido tiene frío y pide algo de beber. ¿Qué haces?",
  [("Cover them, but give nothing to drink", "Taparlo, pero no darle de beber"), ("Give water but don’t cover them", "Darle agua pero no taparlo"), ("Give a hot drink", "Darle una bebida caliente")],
  "Cover them so they don’t lose heat; never food, drink or medicines.", "Taparlos para que no pierdan temperatura; nunca bebida, alimento ni medicamentos.")
Q("hp3", "help", "It is summer. Should you cover an injured person?", "Es verano. ¿Debes tapar a un herido?",
  [("Yes: even in summer, so they don’t lose body heat", "Sí: incluso en verano, para que no pierda temperatura"), ("No, never in summer", "No, nunca en verano"), ("Only if they are unconscious", "Solo si está inconsciente")],
  "Covering the injured is recommended even in summer.", "Se recomienda tapar a los heridos incluso en verano.")
Q("hp4", "help", "What should you do with clothing that presses on the neck of the injured?", "¿Qué haces con la ropa que oprime el cuello del herido?",
  [("Loosen it", "Aflojarla"), ("Leave it", "Dejarla como está"), ("Tighten it to support the neck", "Apretarla para sujetar el cuello")],
  "Loosen clothes that press on the neck and airway.", "Hay que aflojar las prendas que opriman el cuello y las vías respiratorias.")
Q("hp5", "help", "Several people are injured. Who do you look after first?", "Hay varios heridos. ¿A quién atiendes primero?",
  [("According to seriousness: the unconscious and those with breathing problems", "Según la gravedad: inconscientes y con dificultades respiratorias"), ("Whoever shouts most", "A quien más grita"), ("The one closest to you", "Al más cercano")],
  "Set an order of preference by seriousness.", "Establecer un orden de preferencia en función de la gravedad.")
Q("hp6", "help", "What is the “golden hour”?", "¿Qué es la «hora de oro»?",
  [("The hour right after the accident, when most deaths happen", "La hora inmediatamente posterior al accidente, cuando se producen más muertes"), ("The time the ambulance takes to arrive", "El tiempo que tarda la ambulancia"), ("The hour of the day with most accidents", "La hora del día con más accidentes")],
  "What is done in that hour is crucial.", "La actuación en esa hora es fundamental.")
Q("hp7", "help", "A casualty has a burn on the arm. May you put cream on it?", "Un herido tiene una quemadura en el brazo. ¿Puedes ponerle una pomada?",
  [("No: don’t touch wounds or burns or put creams on them", "No: no tocar heridas ni quemaduras ni aplicar pomadas"), ("Yes, any burn cream", "Sí, cualquier crema para quemaduras"), ("Yes, if it is small", "Sí, si es pequeña")],
  "Cold water and damp sterile dressings, no creams.", "Agua fría y apósitos estériles húmedos, sin pomadas.")

# ---------------------------------------------------------------- 3 assessment
Q("as1", "assess", "There are three injured people. What do you do first?", "Hay tres heridos. ¿Qué haces primero?",
  [("Assess all three, 10–15 seconds each, before helping any", "Valorar a los tres, 10–15 segundos cada uno, antes de socorrer a ninguno"), ("Fully treat the first one you reach", "Atender por completo al primero que encuentres"), ("Call 112 and leave", "Llamar al 112 y marcharte")],
  "Assess the state of all before starting to help any.", "Hay que valorar el estado de todos antes de comenzar a socorrer a ninguno.")
Q("as2", "assess", "How do you know an injured person is conscious?", "¿Cómo sabes que un herido está consciente?",
  [("They answer simple questions asked loudly, or react to a pinch", "Contesta a preguntas sencillas en tono alto o reacciona a un pellizco"), ("Their eyes are open", "Tiene los ojos abiertos"), ("They are breathing", "Respira")],
  "Conscious: responds to questions or to painful stimuli.", "Consciente: contesta a preguntas sencillas o responde a estímulos dolorosos.")
Q("as3", "assess", "What does the initial assessment check?", "¿Qué comprueba la valoración inicial?",
  [("Consciousness, breathing and circulation", "Consciencia, respiración y circulación"), ("Fractures and wounds", "Fracturas y heridas"), ("Name and age", "Nombre y edad")],
  "It checks the vital signs.", "Comprueba los signos vitales.")
Q("as4", "assess", "What is the head-tilt, chin-lift for?", "¿Para qué sirve la maniobra frente-mentón?",
  [("To open the airway", "Para abrir las vías respiratorias"), ("To check the pulse", "Para tomar el pulso"), ("To stop bleeding from the nose", "Para cortar la hemorragia nasal")],
  "One hand on the forehead pushing back, the other lifting the chin; the tongue moves away.", "Una mano en la frente empuja hacia atrás y la otra eleva el mentón; la lengua se separa.")
Q("as5", "assess", "How do you check that an unconscious person is breathing?", "¿Cómo compruebas que un inconsciente respira?",
  [("See the chest move, feel the air on your cheek, hear it go in and out", "Ver si se mueve el pecho, sentir el aire en la mejilla, oír la entrada y salida de aire"), ("With a mirror", "Con un espejo"), ("By pinching their arm", "Pellizcándole el brazo")],
  "B: see, feel and hear.", "B: ver, sentir y oír.")
Q("as6", "assess", "The person breathes noisily, with snoring. What does it suggest?", "El herido respira de forma ruidosa, con ronquidos. ¿Qué indica?",
  [("The airway is partly blocked", "Vías aéreas parcialmente obstruidas"), ("Possible serious brain damage", "Posible daño cerebral grave"), ("That they are asleep", "Que está dormido")],
  "Irregular or gasping breathing suggests possible serious brain damage.", "La respiración irregular o entrecortada indica posible daño cerebral grave.")
Q("as7", "assess", "An injured person does not breathe and has no pulse. What is it, and what do you do?", "Un herido no respira y no tiene pulso. ¿Qué le ocurre y qué haces?",
  [("Cardio-respiratory arrest: start CPR urgently", "Parada cardiorrespiratoria: RCP urgentemente"), ("Shock: raise the legs", "Shock: elevarle las piernas"), ("Fainting: wait for them to wake", "Desmayo: esperar a que despierte")],
  "C — circulation: no breathing and/or no pulse means cardio-respiratory arrest.", "C — circulación: sin respiración y/o sin pulso, parada cardiorrespiratoria.")
Q("as8", "assess", "What may block the airway of an unconscious person?", "¿Qué puede obstruir la vía aérea de un inconsciente?",
  [("The tongue falling back, a sweet, chewing gum or another object", "La caída de la lengua, un caramelo, un chicle u otro objeto"), ("The helmet visor", "La pantalla del casco"), ("Tight shoes", "Un calzado ajustado")],
  "If needed, the object is removed with a hooked index finger.", "Si hace falta, se saca con el dedo índice doblado en gancho.")

# ---------------------------------------------------------------- 3.2 helmet
Q("hm1", "helmet", "A rider lies on the road after a fall, conscious and breathing. Should you take the helmet off?", "Un motorista está en el suelo tras una caída, consciente y respirando. ¿Debes quitarle el casco?",
  [("No: leave it on", "No: dejárselo puesto"), ("Yes, so they can breathe better", "Sí, para que respire mejor"), ("Yes, to see the face", "Sí, para verle la cara")],
  "There may be a neck or spine injury; only remove it if essential.", "Puede haber una lesión de cuello o columna; solo se quita si es imprescindible.")
Q("hm2", "helmet", "How do you check the pulse and breathing of an injured rider?", "¿Cómo compruebas el pulso y la respiración de un motorista herido?",
  [("Carotid pulse in the neck and breathing, without removing the helmet", "Pulso carotídeo en el cuello y respiración, sin retirar el casco"), ("Remove the helmet first", "Quitarle primero el casco"), ("Pulse at the ankle", "El pulso en el tobillo")],
  "Only if CPR is essential is the helmet removed.", "Solo si es imprescindible hacer la RCP se retira el casco.")
Q("hm3", "helmet", "When may a rider’s helmet be removed?", "¿Cuándo se puede retirar el casco a un motorista?",
  [("Only when essential, for example to do CPR", "Solo cuando sea imprescindible, por ejemplo para hacer la RCP"), ("Always, to check the head", "Siempre, para revisar la cabeza"), ("Whenever the rider asks", "Siempre que el motorista lo pida")],
  "And only by people who know the technique.", "Y solo por quienes conozcan la técnica.")
Q("hm4", "helmet", "How many people does it take, at least, to remove an injured rider’s helmet?", "¿Cuántas personas hacen falta, como mínimo, para quitar el casco a un motorista herido?",
  [("Two", "Dos"), ("One", "Una"), ("Four", "Cuatro")],
  "At least two people who know the technique, to avoid injuring the cervical spine.", "Mínimo dos personas que conozcan la técnica, para evitar lesiones en la columna cervical.")
Q("hm5", "helmet", "While one person slides the helmet off, what does the other do?", "Mientras una persona saca el casco, ¿qué hace la otra?",
  [("Holds the neck and jaw so that head, neck and trunk stay in line", "Sujeta el cuello y la mandíbula para que cabeza, cuello y tronco sigan alineados"), ("Lifts the casualty’s legs", "Levanta las piernas del herido"), ("Calls 112", "Llama al 112")],
  "The neck–head–trunk line is kept still before moving the person.", "Se inmoviliza el eje cuello-cabeza-tronco antes de moverlo.")
Q("hm6", "helmet", "What is the main risk of removing a rider’s helmet badly?", "¿Cuál es el principal riesgo de quitar mal el casco a un motorista?",
  [("Injuring the cervical spine", "Lesionar la columna cervical"), ("Breaking the visor", "Romper la pantalla"), ("Making the person cold", "Que el herido coja frío")],
  "A possible neck injury can become much worse.", "Una posible lesión cervical puede agravarse mucho.")

# ---------------------------------------------------------------- 4.1–4.2 breathing casualties
Q("rp1", "recovery", "An injured person is conscious and breathing, without serious injuries. What do you do?", "Un herido está consciente, respira y no tiene lesiones graves. ¿Qué haces?",
  [("Go on to the others, without stopping watching them", "Pasar a los demás heridos, sin abandonar su vigilancia"), ("Put them in the recovery position", "Ponerle en posición lateral de seguridad"), ("Start CPR", "Hacerle la RCP")],
  "Keep an eye on them in case they get worse.", "Hay que vigilarlo por si empeorase su estado.")
Q("rp2", "recovery", "When do you put an unconscious person who breathes in the recovery position?", "¿Cuándo pones en posición lateral de seguridad a un inconsciente que respira?",
  [("If you must leave them alone, or they vomit or bleed from the mouth or nose", "Si hay que dejarle solo, o vomita o sangra por la boca o la nariz"), ("Never", "Nunca"), ("Only if they have a fracture", "Solo si tiene una fractura")],
  "It stops them choking.", "Evita que se asfixie.")
Q("rp3", "recovery", "An unconscious person who breathes is bleeding from the left ear. On which side do you lay them?", "Un inconsciente que respira sangra por el oído izquierdo. ¿Sobre qué lado lo colocas?",
  [("On the left, the bleeding ear", "Sobre el izquierdo, el del oído que sangra"), ("On the right", "Sobre el derecho"), ("Face up", "Boca arriba")],
  "Recovery position on the side of the bleeding ear, which is covered without plugging it.", "Posición lateral sobre el oído que sangra, que se cubre sin taponar.")
Q("rp4", "recovery", "How often should you check the breathing of someone in the recovery position?", "¿Cada cuánto debes comprobar la respiración de alguien en posición lateral de seguridad?",
  [("Every 2–3 minutes", "Cada 2–3 minutos"), ("Every 15 minutes", "Cada 15 minutos"), ("Once is enough", "Basta con una vez")],
  "If they stop breathing they may go into cardiac arrest.", "Si deja de respirar puede entrar en parada cardíaca.")
Q("rp5", "recovery", "In the recovery position, where does the casualty’s head end up?", "En la posición lateral de seguridad, ¿dónde queda apoyada la cabeza?",
  [("On the arm that was raised first, the one nearest the rescuer", "Sobre el brazo que se subió primero, el más cercano al auxiliador"), ("On the ground, face down", "En el suelo, boca abajo"), ("On a rolled-up jacket", "Sobre una chaqueta enrollada")],
  "The leg ends bent, the head on the arm moved in the first step.", "Queda con la pierna flexionada y la cabeza sobre el brazo que se movió primero.")
Q("rp6", "recovery", "How many people should turn a casualty into the recovery position, ideally?", "¿Cuántas personas deben girar al herido a la posición lateral, idealmente?",
  [("Two, so head and neck turn with the trunk", "Dos, para que cabeza y cuello giren con el tronco"), ("One, always", "Una, siempre"), ("Four", "Cuatro")],
  "It is advisable to do it with two people whenever possible.", "Es aconsejable realizarla entre dos personas siempre que sea posible.")

# ---------------------------------------------------------------- 4.3 CPR
Q("cp1", "cpr", "An unconscious person is not breathing. What do you do?", "Un inconsciente no respira. ¿Qué haces?",
  [("Start CPR immediately", "Iniciar inmediatamente la RCP"), ("Put them in the recovery position", "Ponerle en posición lateral"), ("Wait for the ambulance without touching them", "Esperar a la ambulancia sin tocarle")],
  "Unconscious and not breathing: cardiopulmonary resuscitation at once.", "Inconsciente que no respira: reanimación cardiopulmonar inmediata.")
Q("cp2", "cpr", "What is the CPR cycle for an adult?", "¿Cuál es el ciclo de RCP en un adulto?",
  [("30 compressions then 2 breaths", "30 compresiones seguidas de 2 ventilaciones"), ("15 compressions then 2 breaths", "15 compresiones seguidas de 2 ventilaciones"), ("5 compressions then 1 breath", "5 compresiones seguidas de 1 ventilación")],
  "Repeat until help arrives or the person reacts.", "Repetir hasta que llegue la ayuda o el herido reaccione.")
Q("cp3", "cpr", "Where do you put your hands for chest compressions?", "¿Dónde colocas las manos para las compresiones?",
  [("Heel of one hand in the centre of the chest, the other on top, fingers interlaced", "Talón de una mano en el centro del pecho y la otra encima, dedos entrelazados"), ("On the stomach", "Sobre el estómago"), ("On the left side of the chest", "En el lado izquierdo del pecho")],
  "Arms straight, body weight pressing down.", "Brazos rectos y el peso del cuerpo hacia abajo.")
Q("cp4", "cpr", "According to your course, how deep should the compressions be in an adult?", "Según tu curso, ¿cuánto se hunde el pecho en las compresiones de un adulto?",
  [("About 4–5 cm", "Unos 4–5 cm"), ("About 1–2 cm", "Unos 1–2 cm"), ("About 10 cm", "Unos 10 cm")],
  "The 2025 European guidelines say 5–6 cm; for the exam, give the course’s figure.", "Las guías europeas de 2025 dicen 5–6 cm; en el examen, la cifra del curso.")
Q("cp5", "cpr", "At what rate should compressions be given, according to your course?", "¿A qué ritmo se hacen las compresiones, según tu curso?",
  [("About 100 a minute", "Unas 100 por minuto"), ("About 30 a minute", "Unas 30 por minuto"), ("About 200 a minute", "Unas 200 por minuto")],
  "Current European guidelines: 100–120 a minute.", "Guías europeas actuales: 100–120 por minuto.")
Q("cp6", "cpr", "How do you start CPR on a child?", "¿Cómo se empieza la RCP en un niño?",
  [("With 5 breaths, then cycles of 30 compressions and 2 breaths", "Con 5 ventilaciones y después ciclos de 30 compresiones y 2 ventilaciones"), ("With 30 compressions, like an adult", "Con 30 compresiones, como un adulto"), ("With 2 breaths only", "Solo con 2 ventilaciones")],
  "Mouth to mouth-and-nose; compressions with less force (one hand, or two fingers on a baby).", "Boca a boca-nariz; compresiones con menos fuerza (una mano, o dos dedos en un bebé).")
Q("cp7", "cpr", "Two rescuers are doing CPR. How often should they swap?", "Dos auxiliadores hacen la RCP. ¿Cada cuánto se turnan?",
  [("Every 1–2 minutes", "Cada 1 o 2 minutos"), ("Every 10 minutes", "Cada 10 minutos"), ("They shouldn’t swap", "No deben turnarse")],
  "At least two rescuers taking turns is recommended.", "Se recomienda al menos dos auxiliadores que se turnen.")
Q("cp8", "cpr", "How long should each rescue breath last?", "¿Cuánto debe durar cada insuflación?",
  [("About one second, watching the chest rise", "Un segundo, observando cómo se eleva el pecho"), ("Five seconds", "Cinco segundos"), ("As long as you can", "Todo lo que puedas")],
  "If the chest doesn’t rise, check the technique and that the airway is clear.", "Si el pecho no se eleva, comprobar la técnica y que la vía no está obstruida.")
Q("cp9", "cpr", "While giving the rescue breaths, what do you do with the casualty’s nose?", "Durante las insuflaciones, ¿qué haces con la nariz del herido?",
  [("Pinch it with the thumb and index finger of the hand on the forehead", "Pinzarla con el pulgar y el índice de la mano que está en la frente"), ("Nothing", "Nada"), ("Cover it with the other hand’s palm", "Taparla con la palma de la otra mano")],
  "The airway is kept open with the head-tilt, chin-lift.", "La vía aérea se mantiene abierta con la maniobra frente-mentón.")
Q("cp10", "cpr", "On what surface should a casualty lie for CPR?", "¿Sobre qué superficie debe estar el herido para la RCP?",
  [("Face up on a flat, hard surface", "Boca arriba sobre una superficie plana y dura"), ("On a soft mattress", "Sobre un colchón blando"), ("Sitting against a wall", "Sentado contra una pared")],
  "The rescuer kneels next to the chest.", "El auxiliador se arrodilla junto al pecho.")

# ---------------------------------------------------------------- 4.4–4.5 bleeding and shock
Q("bl1", "bleed", "What is the first thing to do with external bleeding?", "¿Qué es lo primero ante una hemorragia externa?",
  [("Press directly on the wound with gauze or clean cloth", "Presionar directamente sobre la herida con una gasa o tela limpia"), ("Apply a tourniquet", "Hacer un torniquete"), ("Wash the wound with water", "Lavar la herida con agua")],
  "Direct pressure is the first step in your course and in the European guidelines.", "La presión directa es el primer paso en tu curso y en las guías europeas.")
Q("bl2", "bleed", "The gauze on a wound is soaked with blood. What do you do?", "La gasa de una herida se ha empapado de sangre. ¿Qué haces?",
  [("Put another gauze on top without removing the first", "Poner otra gasa encima sin retirar la anterior"), ("Replace it with a clean one", "Cambiarla por una limpia"), ("Remove it and leave the wound in the air", "Quitarla y dejar la herida al aire")],
  "Removing it would reopen the wound.", "Retirarla volvería a abrir la herida.")
Q("bl3", "bleed", "According to your course, where do you press for bleeding from the arm that won’t stop?", "Según tu curso, ¿dónde presionas si la hemorragia del brazo no se contiene?",
  [("In the hollow of the armpit, raising the arm", "En el hueco de la axila, elevando el brazo"), ("On the wrist", "En la muñeca"), ("On the neck", "En el cuello")],
  "For the leg, press in the groin. Current European guidance no longer recommends pressure points.", "En la pierna, en la ingle. La guía europea actual ya no recomienda los puntos de compresión.")
Q("bl4", "bleed", "When may a tourniquet be used, according to your course?", "¿Cuándo se puede hacer un torniquete, según tu curso?",
  [("As a last resort, for amputation or very serious bleeding", "Como último recurso, en amputaciones o hemorragias muy graves"), ("For any wound that bleeds", "En cualquier herida que sangre"), ("Never", "Nunca")],
  "It is very dangerous and should be avoided if possible.", "Es muy peligroso y debe evitarse si es posible.")
Q("bl5", "bleed", "After applying a tourniquet, what must you do?", "Tras hacer un torniquete, ¿qué debes hacer?",
  [("Leave it on and visible, and note the time it was applied", "Mantenerlo visible y anotar la hora en que se hizo"), ("Loosen it every 10 minutes", "Aflojarlo cada 10 minutos"), ("Cover it with a blanket", "Taparlo con una manta")],
  "The medical team needs to know when it was put on.", "Los sanitarios necesitan saber cuándo se colocó.")
Q("bl6", "bleed", "A casualty bleeds from the nose and is conscious. How do you position the head?", "Un herido consciente sangra por la nariz. ¿Cómo le colocas la cabeza?",
  [("Straight or tilted forward", "Recta o hacia delante"), ("Tilted back", "Hacia atrás"), ("Face down on the ground", "Boca abajo en el suelo")],
  "If unconscious, recovery position.", "Si está inconsciente, posición lateral de seguridad.")
Q("bl7", "bleed", "Blood comes from an ear after a fall. What may it indicate, and what do you do?", "Sale sangre por un oído tras una caída. ¿Qué puede indicar y qué haces?",
  [("A fracture of the base of the skull; cover it with gauze without plugging it", "Una fractura de la base del cráneo; cubrir con una gasa sin taponar"), ("A small cut; plug it with cotton", "Un corte pequeño; taponar con algodón"), ("Nothing serious; clean it", "Nada grave; limpiarlo")],
  "Internal bleeding that shows must never be plugged.", "Las hemorragias internas exteriorizadas no se taponan.")
Q("bl8", "bleed", "A conscious casualty coughs up blood. How do you position them?", "Un herido consciente sangra al toser. ¿Cómo lo colocas?",
  [("Half-sitting", "Semisentado"), ("Lying flat on the back", "Tumbado boca arriba"), ("Standing", "De pie")],
  "Possible lung injury; if unconscious, recovery position.", "Posible lesión de pulmón; si está inconsciente, posición lateral de seguridad.")
Q("sh1", "bleed", "Which are signs of shock?", "¿Cuáles son síntomas de shock?",
  [("Cold sweat, pale skin, confusion, fast shallow breathing, fast weak pulse", "Sudoración fría, piel pálida, confusión, respiración rápida y superficial, pulso rápido y débil"), ("Red face and slow pulse", "Cara roja y pulso lento"), ("Deep, calm breathing", "Respiración profunda y tranquila")],
  "Shock can follow a major loss of blood.", "El shock puede producirse por una pérdida importante de sangre.")
Q("sh2", "bleed", "How do you place a casualty in shock?", "¿Cómo colocas a un herido en shock?",
  [("In the anti-shock position: head lower than the rest of the body", "En posición antishock: la cabeza más baja que el resto del cuerpo"), ("Sitting up", "Sentado"), ("On the side", "De lado")],
  "Loosen tight clothing, cover lightly and give nothing to drink.", "Aflojar la ropa, taparlo ligeramente y no darle bebidas.")

# ---------------------------------------------------------------- 5 fractures, wounds, burns, fire
Q("ij1", "injury", "A rider’s leg is clearly deformed and painful. What do you do?", "La pierna de un motorista está claramente deformada y le duele. ¿Qué haces?",
  [("Don’t try to set it: immobilise it, holding both ends", "No reducirla: inmovilizarla sujetando los dos extremos"), ("Pull it straight", "Estirarla para enderezarla"), ("Make them walk to test it", "Hacerle caminar para comprobarlo")],
  "Never put the bone back in place.", "No hay que tratar de recolocar el hueso.")
Q("ij2", "injury", "A piece of metal is embedded in a wound. What do you do?", "Hay un trozo de metal clavado en una herida. ¿Qué haces?",
  [("Leave it in, dress around it and immobilise it all together", "Dejarlo, tapar la herida con el objeto y fijarlo con un vendaje"), ("Pull it out at once", "Sacarlo enseguida"), ("Push it in further", "Empujarlo hacia dentro")],
  "Removing it can worsen the injury and the bleeding.", "Retirarlo puede aumentar la lesión y la hemorragia.")
Q("ij3", "injury", "What should you cover a wound with?", "¿Con qué debes cubrir una herida?",
  [("Sterile dressings", "Con apósitos estériles"), ("Cotton wool", "Con algodón"), ("Nothing, leave it in the air", "Con nada, al aire")],
  "Don’t handle or explore wounds, unless to stop bleeding.", "No manipular ni explorar las heridas, salvo para contener una hemorragia.")
Q("ij4", "injury", "How do you treat a burn?", "¿Cómo tratas una quemadura?",
  [("Cold water, then cover with damp sterile dressings", "Agua fría y cubrirla con apósitos estériles húmedos"), ("Burst the blisters and apply cream", "Pinchar las ampollas y poner crema"), ("Remove the clothing stuck to it", "Quitar la ropa pegada")],
  "No creams, don’t touch, don’t burst blisters, don’t remove stuck clothing.", "Sin pomadas, sin tocar, sin pinchar ampollas, sin quitar la ropa pegada.")
Q("ij5", "injury", "A person’s clothing is on fire. What do you do?", "La ropa de una persona está ardiendo. ¿Qué haces?",
  [("Cover them with a blanket or make them roll on the ground", "Cubrirla con una manta o hacerla rodar por el suelo"), ("Make them run to put it out", "Hacerla correr para apagarlo"), ("Aim the extinguisher at the face", "Apuntar el extintor a la cara")],
  "With an extinguisher, never aim at the face.", "Con extintor, no apuntar nunca a la cara.")
Q("ij6", "injury", "Several areas of the body are burnt. How do you bandage them?", "Hay varias zonas del cuerpo quemadas. ¿Cómo las vendas?",
  [("Separately, never together", "Por separado, nunca juntas"), ("All together in one bandage", "Todas juntas con una venda"), ("You don’t bandage burns", "Las quemaduras no se vendan")],
  "Raise the burnt part to reduce pain and swelling.", "Elevar la zona quemada disminuye el dolor y la hinchazón.")

# ---------------------------------------------------------------- 6 transport and kit
Q("tr1", "transport", "How should an injured person be taken to hospital, as a rule?", "Por norma, ¿cómo se traslada a un herido al hospital?",
  [("Wait for the ambulance", "Esperar a la ambulancia"), ("In the first car that stops", "En el primer coche que pare"), ("On the back of a motorcycle", "De pasajero en una moto")],
  "A private vehicle only exceptionally.", "En vehículo particular solo excepcionalmente.")
Q("tr2", "transport", "When may a casualty be taken in a private vehicle?", "¿Cuándo se puede trasladar a un herido en un vehículo particular?",
  [("Only if help can’t be called, or it is over 30 minutes late and the casualty is getting seriously worse", "Solo si no se puede pedir ayuda, o tarda más de 30 minutos y el herido empeora gravemente"),
   ("Whenever it is faster", "Siempre que sea más rápido"), ("Never", "Nunca")],
  "For example: bleeding that can’t be controlled, signs of shock increasing, or a tourniquet.", "Por ejemplo: hemorragia que no se contiene, signos de shock en aumento o un torniquete.")
Q("tr3", "transport", "A private car carries an injured person urgently. How must it behave?", "Un coche particular traslada urgentemente a un herido. ¿Cómo debe circular?",
  [("Warn others (horn and hazard lights, or a handkerchief) and follow the traffic rules", "Advertir a los demás (claxon y luces de emergencia, o un pañuelo) y respetar las normas"),
   ("It may run red lights", "Puede saltarse los semáforos"), ("It may exceed the speed limits", "Puede superar los límites de velocidad")],
  "A non-priority vehicle on an urgent run still follows the rules.", "Un vehículo no prioritario en servicio de urgencia sigue respetando las normas.")
Q("tr4", "transport", "Is a first-aid kit compulsory on a motorcycle?", "¿Es obligatorio llevar botiquín en la moto?",
  [("No: recommended and useful, not compulsory", "No: recomendable y útil, no obligatorio"), ("Yes, since 2026", "Sí, desde 2026"), ("Only on trips abroad", "Solo en viajes al extranjero")],
  "Keep it usable: gloves, bandages, gauze, sterile dressings, tape, scissors…", "Que esté en condiciones de uso: guantes, vendas, gasas, apósitos estériles, esparadrapo, tijeras…")
Q("tr5", "transport", "Transporting an injured person in a private vehicle, what must you keep?", "Al trasladar a un herido en un vehículo particular, ¿qué debes mantener?",
  [("The head–neck–trunk line straight, and someone with them to watch", "El eje cabeza-cuello-tronco alineado, y alguien que le acompañe vigilándolo"), ("The person sitting up", "Al herido sentado"), ("The windows closed", "Las ventanillas cerradas")],
  "Use a vehicle that allows the right position for their state.", "Usar un vehículo que permita la posición adecuada a su estado.")
