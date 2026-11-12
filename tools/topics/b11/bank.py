# -*- coding: utf-8 -*-
"""Question bank for the interactive Topic 11 page (first aid). In every question the FIRST option is the correct one
(the page shuffles options when it shows them). Ids must be unique and must not start with "ai"."""

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
        recap=[("Involved users and anyone who knows about an accident must help or call for help, avoid danger and work with the agents.", "Los implicados y quien tenga conocimiento deben auxiliar o pedir auxilio, evitar peligros y colaborar con los agentes."),
               ("Not helping is the crime of failure to help (art. 195); a driver who causes a serious accident and leaves commits art. 382 bis.", "No auxiliar es omisión del deber de socorro (art. 195); el conductor que causa un accidente grave y se va comete el art. 382 bis."),
               ("Non-involved users may drive on if agents are already there or their help is clearly not needed.", "Los no implicados pueden seguir si ya están los agentes o su ayuda claramente no hace falta."),
               ("Deaths or serious injuries: don’t change the scene or evidence (unless it endangers someone), call the agents and stay. Give your details if asked.", "Muertos o heridos graves: no alterar el lugar ni las pruebas (salvo peligro), avisar a los agentes y quedarse. Dar los datos si los piden.")],
        trap=("Thinking only the drivers involved must help.", "Pensar que solo deben ayudar los conductores implicados.")),
    "protect": dict(sec=2, en="PAS: protect", es="PAS: proteger",
        recap=[("PAS: Protect, Alert, Help — in that order.", "PAS: Proteger, Avisar, Socorrer, en ese orden."),
               ("Protect yourself: stop safely, V-16 on the roof from inside, hazard lights, vest on before getting out, stay off the carriageway.", "Autoprotegerse: parar en lugar seguro, V-16 en el techo desde dentro, luces de emergencia, chaleco antes de bajar, no andar por la calzada."),
               ("Protect the scene: vehicles off the carriageway, handbrake, engine off, no smoking; fire: extinguisher at the base, never water.", "Proteger el lugar: vehículos fuera de la calzada, freno de mano, motor parado, no fumar; fuego: extintor en la base, nunca agua."),
               ("Protect the victims: don’t move them or remove a helmet unless essential (two people, head–neck–trunk still).", "Proteger a las víctimas: no moverlas ni quitar el casco salvo que sea imprescindible (dos personas, eje cabeza-cuello-tronco inmóvil).")],
        trap=("Getting out first and putting the vest on afterwards.", "Bajar primero y ponerse el chaleco después.")),
    "alert": dict(sec=2, en="PAS: alert", es="PAS: avisar",
        recap=[("Call 112: free, no credit needed, the same in the whole EU, answered in your language.", "Llamar al 112: gratuito, sin saldo, común en toda la UE, atienden en tu idioma."),
               ("Say the exact place, number and state of the injured, what happened (vehicles, fire, dangerous goods) and who you are.", "Decir el lugar exacto, número y estado de los heridos, qué ha pasado (vehículos, incendio, mercancías peligrosas) y quién eres."),
               ("No need to alert or stay only if injuries are clearly minor, safety is restored and nobody asks.", "No hace falta avisar ni quedarse solo si las heridas son leves, la seguridad está restablecida y nadie lo pide."),
               ("All three conditions must be met.", "Deben cumplirse las tres condiciones.")],
        trap=("Thinking you can leave as soon as nobody seems badly hurt.", "Pensar que te puedes ir en cuanto nadie parece grave.")),
    "help": dict(sec=2, en="PAS: help", es="PAS: socorrer",
        recap=[("Only help if you know how; otherwise wait for the medical team.", "Solo socorrer si se sabe; si no, esperar a los sanitarios."),
               ("Keep calm; worst cases first (unconscious, breathing problems); treat them inside the vehicle if needed.", "Calma; primero los más graves (inconscientes, dificultad respiratoria); atenderlos en el vehículo si hace falta."),
               ("Loosen clothing, cover them even in summer, nothing to eat, drink or medicines, don’t touch wounds or burns.", "Aflojar la ropa, taparlos incluso en verano, ni comida ni bebida ni medicamentos, no tocar heridas ni quemaduras."),
               ("The golden hour: the first hour after the accident, when most deaths happen.", "La hora de oro: la primera hora tras el accidente, cuando se produce la mayoría de los fallecidos.")],
        trap=("Giving an injured person water.", "Dar agua a un herido.")),
    "assess": dict(sec=3, en="Initial assessment and ABC", es="Valoración inicial y ABC",
        recap=[("Check consciousness, breathing and circulation; with several injured, assess all first, 10–15 s each.", "Comprobar consciencia, respiración y circulación; con varios heridos, valorar a todos primero, 10–15 s cada uno."),
               ("Conscious: answers simple questions or reacts to a pinch. Unconscious: no response → ABC.", "Consciente: contesta o reacciona a un pellizco. Inconsciente: no responde → ABC."),
               ("A: head-tilt, chin-lift; hooked finger to remove an object. B: see, feel, hear.", "A: maniobra frente-mentón; dedo en gancho para sacar objetos. B: ver, sentir, oír."),
               ("Snoring breathing: airway partly blocked; irregular: possible brain damage. No breathing/pulse: CPR.", "Respiración con ronquidos: vía aérea obstruida en parte; irregular: posible daño cerebral. Sin respiración o pulso: RCP.")],
        trap=("Helping the first injured person you see before checking the others.", "Atender al primer herido sin valorar antes a los demás.")),
    "recovery": dict(sec=4, en="Breathing casualties and the recovery position", es="Heridos que respiran y PLS",
        recap=[("Conscious and breathing: check for serious injuries, go on to others, keep watching.", "Consciente que respira: comprobar lesiones graves, pasar a otros, sin dejar de vigilarlo."),
               ("Unconscious and breathing: recovery position if you must leave them or they vomit or bleed from mouth or nose.", "Inconsciente que respira: PLS si hay que dejarlo solo o vomita o sangra por boca o nariz."),
               ("Bleeding ear: lie on that ear. Check breathing every 2–3 minutes.", "Sangra por un oído: sobre ese lado. Comprobar la respiración cada 2–3 minutos."),
               ("PLS: raise the near arm, bend the far arm and leg, roll in one go — best with two people.", "PLS: subir el brazo cercano, doblar el brazo y la pierna alejados, girar a la vez; mejor entre dos.")],
        trap=("Laying someone with a bleeding ear on the other side.", "Colocar sobre el otro lado a quien sangra por un oído.")),
    "cpr": dict(sec=4, en="CPR", es="RCP",
        recap=[("Unconscious and not breathing: start CPR at once, face up on a hard flat surface.", "Inconsciente que no respira: RCP inmediata, boca arriba sobre superficie plana y dura."),
               ("Heel of the hand on the centre of the chest, arms straight, 4–5 cm (course), 30 compressions; swap every 1–2 min.", "Talón de la mano en el centro del pecho, brazos rectos, 4–5 cm (curso), 30 compresiones; turnarse cada 1–2 min."),
               ("Breaths: head-tilt, pinch the nose, blow for 1 second, watch the chest rise; two breaths; 30 : 2 at about 100 a minute.", "Ventilaciones: frente-mentón, pinzar la nariz, soplar 1 segundo, ver subir el pecho; dos insuflaciones; 30 : 2 a unas 100 por minuto."),
               ("Children: 5 breaths first, then 30 : 2, one hand or two fingers.", "Niños: 5 ventilaciones iniciales y luego 30 : 2, con una mano o dos dedos.")],
        trap=("Bending the arms during compressions.", "Doblar los brazos al comprimir.")),
    "bleed": dict(sec=4, en="Bleeding", es="Hemorragias",
        recap=[("External: press on the wound with gauze or clean cloth; if soaked, add more on top.", "Externa: presionar con gasa o tela limpia; si se empapa, poner otra encima."),
               ("Course: then raise the limb and press the armpit (arm) or groin (leg).", "Curso: después elevar el miembro y presionar la axila (brazo) o la ingle (pierna)."),
               ("Tourniquet: last resort above the wound; keep it on, visible, note the time.", "Torniquete: último recurso por encima de la herida; mantenerlo, visible, anotar la hora."),
               ("Blood from ear, nose or mouth: don’t plug it. Ear → PLS on that ear; lung → half-sitting if conscious.", "Sangre por oído, nariz o boca: no taponar. Oído → PLS sobre ese oído; pulmón → semisentado si está consciente.")],
        trap=("Removing a soaked gauze to put a clean one.", "Quitar la gasa empapada para poner una limpia.")),
    "shock": dict(sec=4, en="Shock", es="Shock",
        recap=[("Shock can follow a major loss of blood.", "El shock puede deberse a una pérdida importante de sangre."),
               ("Signs: cold sweat, pale skin, confusion, restlessness, fast shallow breathing, fast weak pulse.", "Síntomas: sudor frío, palidez, confusión, inquietud, respiración rápida y superficial, pulso rápido y débil."),
               ("Anti-shock position: head lower than the body (legs raised).", "Posición antishock: la cabeza más baja que el cuerpo (piernas elevadas)."),
               ("Loosen clothing, cover lightly without making them sweat, no drinks.", "Aflojar la ropa, tapar ligeramente sin hacer sudar, no dar bebidas.")],
        trap=("Giving a person in shock something to drink.", "Dar de beber a una persona en shock.")),
    "injury": dict(sec=5, en="Fractures, wounds, burns, fire", es="Fracturas, heridas, quemaduras, fuego",
        recap=[("Fractures: don’t set them; immobilise both ends; open ones: cover and stop the bleeding.", "Fracturas: no reducirlas; inmovilizar los dos extremos; abiertas: tapar y contener la hemorragia."),
               ("Wounds: sterile dressings, don’t explore, don’t pull out embedded objects; organs out: damp cloths.", "Heridas: apósitos estériles, no explorar, no retirar objetos clavados; vísceras: paños húmedos."),
               ("Burns: don’t touch, don’t remove stuck clothing, don’t burst blisters; cold water, damp sterile dressings, separately; raise the part.", "Quemaduras: no tocar, no quitar la ropa pegada, no pinchar ampollas; agua fría, apósitos húmedos, por separado; elevar."),
               ("Vehicle fire: injured out first, extinguisher at the base, sand or blankets, never water. Person on fire: blanket or roll.", "Fuego en el vehículo: primero sacar a los heridos, extintor en la base, arena o mantas, nunca agua. Persona en llamas: manta o rodar.")],
        trap=("Pulling out an object stuck in a wound.", "Sacar un objeto clavado en una herida.")),
    "transport": dict(sec=6, en="Moving the injured and first-aid kit", es="Traslado y botiquín",
        recap=[("Wait for the ambulance. A private car only exceptionally.", "Esperar a la ambulancia. Coche particular solo excepcionalmente."),
               ("Exceptions: no way to call for help, or worsening with help over 30 min late (uncontrolled bleeding, shock, tourniquet).", "Excepciones: no se puede pedir ayuda, o empeora y la ayuda tarda más de 30 min (hemorragia, shock, torniquete)."),
               ("Keep the head–neck–trunk aligned, suitable position, go with them; horn and hazard lights or a handkerchief; follow the rules.", "Eje cabeza-cuello-tronco alineado, posición adecuada, acompañarlo; claxon y luces de emergencia o pañuelo; respetar las normas."),
               ("A first-aid kit is not compulsory, but recommended.", "El botiquín no es obligatorio, pero sí recomendable.")],
        trap=("Thinking a first-aid kit is compulsory in a car.", "Pensar que el botiquín es obligatorio en un turismo.")),
}

# ---------------------------------------------------------------- 1. duty
Q("du1", "duty", "Who must help at a road accident?", "¿Quién está obligado a ayudar en un accidente de tráfico?",
  [("Those involved and anyone who knows about it", "Los implicados y quien tenga conocimiento de él"), ("Only the drivers involved", "Solo los conductores implicados"), ("Only the police", "Solo la policía")],
  "Even users who are not involved.", "Incluso los usuarios no implicados.")
Q("du2", "duty", "Not helping the victims of an accident when you could is…", "No auxiliar a las víctimas de un accidente pudiendo hacerlo es…",
  [("a crime of failure to help", "un delito de omisión del deber de socorro"), ("a minor offence", "una infracción leve"), ("allowed if you are in a hurry", "permitido si tienes prisa")],
  "Código Penal, art. 195.", "Código Penal, art. 195.")
Q("du3", "duty", "A user not involved in an accident may drive on when…", "Un usuario no implicado puede continuar la marcha cuando…",
  [("the agents are already there", "ya se han personado los agentes"), ("they have an appointment", "tiene una cita"), ("it is raining", "está lloviendo")],
  "Or when their help is clearly not needed.", "O cuando claramente no sea necesaria su colaboración.")
Q("du4", "duty", "If there are deaths or serious injuries you must…", "Si hay muertos o heridos graves hay que…",
  [("avoid changing the scene and the evidence, call the agents and stay", "evitar alterar el lugar y las pruebas, avisar a los agentes y quedarse"), ("move the vehicles to clean the road", "mover los vehículos para limpiar la vía"), ("leave once you have called", "irse tras llamar")],
  "Unless leaving things as they are endangers someone.", "Salvo que no hacerlo perjudique la seguridad.")
Q("du5", "duty", "If the agents ask, a person involved in an accident must…", "Si lo piden los agentes, un implicado en un accidente debe…",
  [("show their documents, explain what happened and take the alcohol and drug tests", "mostrar su documentación, explicar lo ocurrido y someterse a las pruebas de alcohol y drogas"), ("only give their name", "dar solo su nombre"), ("nothing", "nada")],
  "Working with the authorities.", "Colaborar con la Autoridad.")
Q("du6", "duty", "A driver who causes an accident with seriously injured people and deliberately leaves without any risk to stay commits…", "El conductor que causa un accidente con heridos graves y se marcha voluntariamente sin riesgo para quedarse comete…",
  [("the crime of leaving the scene of an accident", "el delito de abandono del lugar del accidente"), ("no offence if they call later", "ninguna infracción si llama después"), ("only an administrative offence", "solo una infracción administrativa")],
  "Art. 382 bis: prison and a driving ban.", "Art. 382 bis: prisión y privación del permiso.")
Q("du7", "duty", "Someone involved in an accident asks for your details. You must give…", "Un implicado en un accidente te pide tus datos. Debes facilitar…",
  [("your identity and your vehicle’s details", "tu identidad y los datos del vehículo"), ("only your phone number", "solo tu teléfono"), ("nothing", "nada")],
  "Name, ID, plate…", "Nombre, DNI, matrícula…")
Q("du8", "duty", "With only minor damage, the sensible thing is to…", "Si solo hay pequeños daños materiales, lo acertado es…",
  [("agree and fill in the accident report form off the road", "llegar a un acuerdo y rellenar el parte amistoso fuera de la vía"), ("block the road until the police arrive", "bloquear la vía hasta que llegue la policía"), ("argue on the carriageway", "discutir en la calzada")],
  "Tell the insurers as soon as possible.", "Comunicarlo a las aseguradoras cuanto antes.")
Q("du9", "duty", "Where should you fill in the accident report form?", "¿Dónde se debe rellenar el parte amistoso?",
  [("Somewhere safe, off the road", "En un lugar seguro, fuera de la vía"), ("On the carriageway, next to the cars", "En la calzada, junto a los coches"), ("On the hard shoulder of a motorway", "En el arcén de la autopista")],
  "Don’t create new risks.", "Para no crear nuevos riesgos.")
Q("du10", "duty", "If you can’t help yourself, to avoid failing in your duty you must…", "Si no puedes socorrer tú mismo, para no incumplir tu deber debes…",
  [("urgently call for help", "pedir auxilio con urgencia"), ("leave", "marcharte"), ("wait for someone else to call", "esperar a que llame otro")],
  "Failing to call is punished the same way.", "No pedirlo se castiga igual.")

# ---------------------------------------------------------------- 2. protect
Q("pa1", "protect", "What is the right order at an accident?", "¿Cuál es el orden correcto ante un accidente?",
  [("Protect, alert, help", "Proteger, avisar, socorrer"), ("Help, alert, protect", "Socorrer, avisar, proteger"), ("Alert, help, protect", "Avisar, socorrer, proteger")],
  "The PAS rule.", "La regla PAS.")
Q("pa2", "protect", "The first thing to protect is…", "Lo primero que hay que proteger es…",
  [("yourself", "a uno mismo"), ("the vehicles", "los vehículos"), ("the evidence", "las pruebas")],
  "Then the scene, then the victims.", "Después el lugar y después las víctimas.")
Q("pr1", "protect", "When do you put the reflective vest on?", "¿Cuándo hay que ponerse el chaleco reflectante?",
  [("Before getting out of the vehicle", "Antes de salir del vehículo"), ("Once you reach the injured", "Al llegar junto a los heridos"), ("Only at night", "Solo de noche")],
  "Even on roads where it isn’t compulsory.", "Aunque no sea obligatorio en esa vía.")
Q("pr2", "protect", "How do you place the V-16 warning light?", "¿Cómo se coloca la señal V-16?",
  [("On the roof, from inside, with the window down, before getting out", "En el techo, desde dentro, bajando la ventanilla, antes de salir"), ("50 m behind the car, walking", "A 50 m detrás del coche, andando"), ("Inside the boot", "En el maletero")],
  "Plus the hazard lights.", "Además de las luces de emergencia.")
Q("pr3", "protect", "To put out a vehicle fire you should use…", "Para apagar el fuego de un vehículo hay que usar…",
  [("an extinguisher at the base of the flames, or sand or blankets — never water", "el extintor en la base de las llamas, o arena o mantas, nunca agua"), ("plenty of water", "mucha agua"), ("the extinguisher at the top of the flames", "el extintor en lo alto de las llamas")],
  "Get the injured out first.", "Primero, sacar a los heridos.")
Q("pr4", "protect", "Crashed vehicles that block the road should be…", "Los vehículos accidentados que obstaculizan la vía se deben…",
  [("moved off the carriageway, with the handbrake on and engine off", "colocar fuera de la calzada, con freno de mano y motor parado"), ("left exactly where they are, always", "dejar siempre donde están"), ("left with the engine running", "dejar con el motor en marcha")],
  "On the shoulder or central reservation — but with deaths or serious injuries, don’t alter evidence unless there is a danger.", "En el arcén o la mediana; con muertos o heridos graves, no alterar pruebas salvo peligro.")
Q("pr5", "protect", "At an accident scene, smoking is…", "En el lugar de un accidente, fumar…",
  [("to be avoided: it is a fire risk", "debe evitarse: hay riesgo de incendio"), ("fine outside the car", "está bien fuera del coche"), ("recommended to calm down", "se recomienda para calmarse")],
  "Fuel may have spilled.", "Puede haber combustible derramado.")
Q("pr6", "protect", "May you move an injured person?", "¿Se puede mover a un herido?",
  [("Only if essential because of a danger, keeping the head–neck–trunk still", "Solo si es imprescindible por un peligro, inmovilizando el eje cabeza-cuello-tronco"), ("Yes, to make them comfortable", "Sí, para ponerlo cómodo"), ("Yes, always to the shoulder", "Sí, siempre al arcén")],
  "A spinal injury can be made worse.", "Se puede agravar una lesión de columna.")
Q("pr7", "protect", "Should you remove an injured motorcyclist’s helmet?", "¿Hay que quitar el casco a un motorista herido?",
  [("No, unless essential and you know how — at least two people", "No, salvo que sea imprescindible y se sepa hacerlo, mínimo dos personas"), ("Yes, always, so they can breathe", "Sí, siempre, para que respire"), ("Yes, one person is enough", "Sí, basta una persona")],
  "Moving the neck can cause serious injury.", "Mover el cuello puede causar lesiones graves.")
Q("pr8", "protect", "After stopping at an accident, you should…", "Tras detenerte en un accidente, debes…",
  [("avoid walking on the carriageway", "evitar circular por la calzada"), ("stand in the middle of the road to stop traffic", "ponerte en medio de la calzada para parar el tráfico"), ("cross between moving cars", "cruzar entre los coches")],
  "Walk and wait off the road.", "Caminar y esperar fuera de la calzada.")

# ---------------------------------------------------------------- 2. alert
Q("al1", "alert", "The emergency number is…", "El teléfono de emergencias es…",
  [("112", "el 112"), ("091", "el 091"), ("061 only", "solo el 061")],
  "The same in the whole European Union.", "Común en toda la Unión Europea.")
Q("al2", "alert", "Calling 112…", "Llamar al 112…",
  [("is free and works even without credit", "es gratuito y funciona incluso sin saldo"), ("costs money", "cuesta dinero"), ("only works in Spain", "solo funciona en España")],
  "And they answer in the caller’s language.", "Y atienden en el idioma de quien llama.")
Q("al3", "alert", "Which information is NOT needed when you call 112?", "¿Qué información NO es necesaria al llamar al 112?",
  [("Your insurance policy number", "El número de tu póliza de seguro"), ("The exact place", "El lugar exacto"), ("The number and state of the injured", "El número y estado de los heridos")],
  "Also what happened and your identity and phone.", "También qué ha ocurrido y tu identidad y teléfono.")
Q("al4", "alert", "When calling 112 you should mention, if there is any…", "Al llamar al 112 hay que mencionar, si lo hay…",
  [("a fire risk or dangerous goods", "riesgo de incendio o mercancías peligrosas"), ("the colour of the cars", "el color de los coches"), ("the weather forecast", "la previsión del tiempo")],
  "The characteristics of the accident.", "Las características del accidente.")
Q("al5", "alert", "You need not alert or stay at an accident only if…", "No es necesario avisar ni permanecer en un accidente solo si…",
  [("injuries are clearly minor, safety is restored and nobody involved asks you to", "las heridas son leves, la seguridad está restablecida y ningún implicado lo solicita"), ("you are late", "llegas tarde"), ("it is night", "es de noche")],
  "All three conditions.", "Las tres condiciones.")
Q("al6", "alert", "There is a slightly injured person, the road is clear, but they ask you to stay. You must…", "Hay un herido leve, la vía está despejada, pero te pide que te quedes. Debes…",
  [("stay", "quedarte"), ("leave, since injuries are minor", "irte, porque es leve"), ("only leave your number", "solo dejar tu teléfono")],
  "One of the three conditions fails.", "No se cumple una de las tres condiciones.")
Q("al7", "alert", "When you call 112 you must give…", "Al llamar al 112 debes dar…",
  [("your name, surname, ID and a contact phone", "tu nombre, apellidos, DNI y un teléfono de contacto"), ("nothing about yourself", "nada sobre ti"), ("only your number plate", "solo tu matrícula")],
  "So they can call you back.", "Para poder volver a llamarte.")

# ---------------------------------------------------------------- 2. help
Q("hp1", "help", "If you don’t know how to help an injured person, you should…", "Si no sabes cómo socorrer a un herido, debes…",
  [("wait for the medical team", "esperar a la ayuda sanitaria"), ("try anyway", "intentarlo de todas formas"), ("take them to hospital in your car", "llevarlo al hospital en tu coche")],
  "Wrong help can make things worse.", "Una ayuda inadecuada puede empeorar el resultado.")
Q("hp2", "help", "Who should you help first?", "¿A quién hay que atender primero?",
  [("The most serious: the unconscious and those with breathing problems", "A los más graves: inconscientes y con dificultad respiratoria"), ("Whoever shouts the most", "Al que más grita"), ("The nearest", "Al más cercano")],
  "Order by seriousness.", "Orden según la gravedad.")
Q("hp3", "help", "An injured person asks for water. You should…", "Un herido te pide agua. Debes…",
  [("not give it: no food, drink or medicines", "no dársela: ni bebida, ni alimento, ni medicamentos"), ("give a little", "darle un poco"), ("give water with sugar", "darle agua con azúcar")],
  "They may need surgery.", "Puede necesitar una operación.")
Q("hp4", "help", "Injured people should be covered…", "A los heridos hay que taparlos…",
  [("so they don’t lose body heat, even in summer", "para que no pierdan temperatura, incluso en verano"), ("only in winter", "solo en invierno"), ("never", "nunca")],
  "Without making them sweat.", "Sin hacerles sudar.")
Q("hp5", "help", "With an injured person’s clothing, you should…", "Con la ropa del herido, hay que…",
  [("loosen what presses on the neck and airway", "aflojar la que oprima el cuello y las vías respiratorias"), ("take it all off", "quitársela entera"), ("not touch it", "no tocarla")],
  "To help them breathe.", "Para facilitar la respiración.")
Q("hp6", "help", "On wounds and burns you should…", "Sobre heridas y quemaduras hay que…",
  [("not touch them or put creams on them", "no tocarlas ni aplicar pomadas"), ("apply ointment", "aplicar pomada"), ("clean them with alcohol", "limpiarlas con alcohol")],
  "Risk of infection and worse injury.", "Riesgo de infección y de empeorar.")
Q("hp7", "help", "The ‘golden hour’ is…", "La «hora de oro» es…",
  [("the hour right after an accident, when most deaths happen", "la hora inmediatamente posterior al accidente, cuando hay más fallecidos"), ("the hour before the accident", "la hora anterior al accidente"), ("rush hour", "la hora punta")],
  "What is done then is crucial.", "Lo que se hace entonces es fundamental.")
Q("hp8", "help", "Why should you stay with the victims?", "¿Por qué hay que acompañar a las víctimas?",
  [("To calm them and watch their state", "Para transmitir tranquilidad y vigilar su estado"), ("To question them", "Para interrogarlas"), ("It is not needed", "No hace falta")],
  "Keep calm yourself too.", "Y mantener uno mismo la calma.")
Q("hp9", "help", "An injured person trapped in a car with no danger around should be treated…", "A un herido atrapado en su coche sin peligro alrededor hay que atenderlo…",
  [("inside the vehicle, without moving them", "dentro del vehículo, sin moverlo"), ("after pulling them out quickly", "tras sacarlo rápidamente"), ("only once on the shoulder", "solo una vez en el arcén")],
  "Move only if there is a danger.", "Mover solo si hay peligro.")

# ---------------------------------------------------------------- 3. assessment and ABC
Q("as1", "assess", "The initial assessment checks…", "La valoración inicial comprueba…",
  [("consciousness, breathing and circulation", "la consciencia, la respiración y la circulación"), ("only wounds", "solo las heridas"), ("only fractures", "solo las fracturas")],
  "The vital signs.", "Los signos vitales.")
Q("as2", "assess", "With several injured people, before helping any you should…", "Con varios heridos, antes de socorrer a ninguno hay que…",
  [("assess them all, 10–15 seconds each", "valorarlos a todos, 10–15 segundos cada uno"), ("help the first one you reach", "atender al primero que encuentres"), ("wait for the ambulance", "esperar a la ambulancia")],
  "Then help the most serious first.", "Después, atender primero al más grave.")
Q("as3", "assess", "An injured person is conscious when they…", "Un herido está consciente cuando…",
  [("answer simple questions or react to a pinch", "contesta a preguntas sencillas o reacciona a un pellizco"), ("have their eyes open", "tiene los ojos abiertos"), ("breathe", "respira")],
  "Ask loudly; pinch the back of the hand.", "Preguntar en voz alta; pellizco en el dorso de la mano.")
Q("as4", "assess", "If an injured person doesn’t respond to any stimulus you apply…", "Si un herido no responde a ningún estímulo se aplica…",
  [("the ABC rule", "la regla ABC"), ("the PAS rule", "la regla PAS"), ("the anti-shock position", "la posición antishock")],
  "Airway, breathing, circulation.", "Vía aérea, boca, circulación.")
Q("as5", "assess", "The head-tilt, chin-lift is used to…", "La maniobra frente-mentón sirve para…",
  [("open the airway", "abrir las vías respiratorias"), ("stop bleeding", "detener una hemorragia"), ("check the pulse", "tomar el pulso")],
  "One hand on the forehead, the other lifts the chin.", "Una mano en la frente y la otra eleva el mentón.")
Q("as6", "assess", "In an unconscious person, a common cause of a blocked airway is…", "En un inconsciente, una causa habitual de obstrucción es…",
  [("the tongue falling back", "la caída de la lengua"), ("the seat belt", "el cinturón"), ("the cold", "el frío")],
  "Also sweets, gum or other objects.", "También caramelos, chicles u otros objetos.")
Q("as7", "assess", "To remove an object from the mouth you use…", "Para sacar un objeto de la boca se usa…",
  [("the index finger, bent like a hook", "el dedo índice doblado en forma de gancho"), ("tweezers", "unas pinzas"), ("a sip of water", "un sorbo de agua")],
  "After opening the airway.", "Tras abrir la vía aérea.")
Q("as8", "assess", "To check breathing you…", "Para comprobar la respiración hay que…",
  [("see the chest move, feel the air, hear it", "ver el pecho moverse, sentir el aire y oírlo"), ("look at the eyes", "mirar los ojos"), ("ask them to cough", "pedirle que tosa")],
  "See, feel and hear.", "Ver, sentir y oír.")
Q("as9", "assess", "Noisy, snoring breathing suggests…", "Una respiración ruidosa o con ronquidos indica…",
  [("a partly blocked airway", "vías aéreas parcialmente obstruidas"), ("a broken leg", "una pierna rota"), ("that all is well", "que todo va bien")],
  "Irregular breathing: possible brain damage.", "Irregular: posible daño cerebral.")
Q("as10", "assess", "Irregular, gasping or shallow breathing may mean…", "Una respiración irregular, entrecortada o superficial puede indicar…",
  [("serious brain damage", "un daño cerebral grave"), ("a stomach injury", "una lesión de estómago"), ("normal sleep", "sueño normal")],
  "Watch them closely.", "Vigilarle de cerca.")
Q("as11", "assess", "A person who isn’t breathing and/or has no pulse is in…", "Una persona que no respira y/o no tiene pulso está en…",
  [("cardio-respiratory arrest", "parada cardio-respiratoria"), ("shock", "estado de shock"), ("a fainting fit", "un desmayo")],
  "Start CPR urgently.", "Hay que hacer la RCP urgentemente.")

# ---------------------------------------------------------------- 4. recovery position
Q("rp1", "recovery", "With a conscious injured person who breathes, you…", "Con un herido consciente que respira…",
  [("check for serious injuries and go on to others, still watching them", "compruebas que no tiene lesiones graves y pasas a otros, sin dejar de vigilarlo"), ("put them in the recovery position", "lo pones en PLS"), ("start CPR", "empiezas la RCP")],
  "They might get worse.", "Puede empeorar.")
Q("rp2", "recovery", "An unconscious person who breathes is put in the recovery position if…", "A un inconsciente que respira se le pone en PLS si…",
  [("you must leave them alone or they vomit or bleed from mouth or nose", "hay que dejarle solo o vomita o sangra por boca o nariz"), ("they are cold", "tiene frío"), ("they wake up", "despierta")],
  "So they don’t choke.", "Para que no se asfixie.")
Q("rp3", "recovery", "An unconscious person bleeds from an ear. Lay them…", "Un inconsciente sangra por un oído. Se le coloca…",
  [("on the side of the bleeding ear", "sobre el lado del oído que sangra"), ("on the other side", "sobre el otro lado"), ("face up", "boca arriba")],
  "Cover the ear without plugging it.", "Cubrir el oído sin taponar.")
Q("rp4", "recovery", "In the recovery position, check the breathing every…", "En la PLS, la respiración se comprueba cada…",
  [("2–3 minutes", "2–3 minutos"), ("15 minutes", "15 minutos"), ("half an hour", "media hora")],
  "They could go into cardiac arrest.", "Podría entrar en parada cardíaca.")
Q("rp5", "recovery", "The first step of the recovery position is…", "El primer paso de la PLS es…",
  [("raising the arm nearest to you", "subir el brazo del herido más cercano"), ("rolling the person", "voltear al herido"), ("bending both legs", "doblar las dos piernas")],
  "The head will rest on that arm.", "Sobre ese brazo apoyará la cabeza.")
Q("rp6", "recovery", "In the second step you bend…", "En el segundo paso se doblan…",
  [("the far arm and the leg on the same side", "el brazo más alejado y la pierna del mismo lado"), ("both arms", "los dos brazos"), ("the neck", "el cuello")],
  "Then roll the person towards you.", "Después se le gira hacia ti.")
Q("rp7", "recovery", "When rolling into the recovery position, a helper should make sure that…", "Al girar al herido a la PLS, el ayudante debe asegurar que…",
  [("the head and neck turn together with the trunk", "la cabeza-cuello gire a la vez que el tronco"), ("the head turns first", "la cabeza gire primero"), ("the legs stay still", "las piernas no se muevan")],
  "Best done by two people.", "Mejor entre dos personas.")
Q("rp8", "recovery", "In the final recovery position, the head rests…", "En la PLS final, la cabeza queda apoyada…",
  [("on the arm moved in the first step", "sobre el brazo que se movió en el primer paso"), ("on the ground, face down", "en el suelo, boca abajo"), ("on a high cushion", "sobre un cojín alto")],
  "With the top leg bent.", "Con la pierna flexionada.")

# ---------------------------------------------------------------- 4. CPR
Q("cp1", "cpr", "An unconscious person who does not breathe needs…", "Un herido inconsciente que no respira necesita…",
  [("CPR immediately", "RCP inmediatamente"), ("the recovery position", "la posición lateral de seguridad"), ("to be given water", "que le den agua")],
  "Compressions and breaths.", "Compresiones y ventilaciones.")
Q("cp2", "cpr", "For CPR the person must be…", "Para la RCP el herido debe estar…",
  [("face up on a flat, hard surface", "boca arriba sobre una superficie plana y dura"), ("on a soft mattress", "sobre un colchón blando"), ("on their side", "de lado")],
  "Kneel next to their chest.", "El auxiliador, arrodillado junto al pecho.")
Q("cp3", "cpr", "Where do you place your hands for chest compressions?", "¿Dónde se colocan las manos para las compresiones?",
  [("Heel of the hand in the centre of the chest, the other on top", "Talón de la mano en el centro del pecho y la otra encima"), ("On the belly", "Sobre el abdomen"), ("On the left side of the chest", "En el lado izquierdo del pecho")],
  "Fingers interlaced.", "Entrelazando los dedos.")
Q("cp4", "cpr", "During compressions your arms should be…", "Durante las compresiones los brazos deben estar…",
  [("straight, using your body weight", "rectos, dejando caer el peso del cuerpo"), ("bent", "doblados"), ("relaxed", "relajados")],
  "Without losing contact between compressions.", "Sin perder el contacto entre compresiones.")
Q("cp5", "cpr", "According to your course, how far should the chest go down?", "Según tu curso, ¿cuánto hay que hundir el pecho?",
  [("About 4–5 cm", "Unos 4–5 cm"), ("1 cm", "1 cm"), ("10 cm", "10 cm")],
  "Current European guidelines: 5–6 cm.", "Las guías europeas actuales: 5–6 cm.")
Q("cp6", "cpr", "For an adult, CPR is done in cycles of…", "En un adulto, la RCP se hace en ciclos de…",
  [("30 compressions and 2 breaths", "30 compresiones y 2 ventilaciones"), ("15 compressions and 1 breath", "15 compresiones y 1 ventilación"), ("5 compressions and 5 breaths", "5 compresiones y 5 ventilaciones")],
  "At about 100 compressions a minute.", "A unas 100 compresiones por minuto.")
Q("cp7", "cpr", "With two rescuers doing CPR, they should swap every…", "Con dos auxiliadores haciendo RCP, deben turnarse cada…",
  [("1–2 minutes", "1 o 2 minutos"), ("10 minutes", "10 minutos"), ("30 seconds", "30 segundos")],
  "So the compressions stay effective.", "Para que las compresiones sigan siendo eficaces.")
Q("cp8", "cpr", "Each rescue breath should last about…", "Cada insuflación debe durar aproximadamente…",
  [("1 second", "1 segundo"), ("5 seconds", "5 segundos"), ("10 seconds", "10 segundos")],
  "Watch the chest rise.", "Observar cómo se eleva el pecho.")
Q("cp9", "cpr", "During a mouth-to-mouth breath you must…", "Durante el boca a boca hay que…",
  [("keep the airway open and pinch the nose", "mantener abierta la vía aérea y pinzar la nariz"), ("press on the chest", "presionar el pecho"), ("turn the head to the side", "girar la cabeza de lado")],
  "With the hand on the forehead.", "Con la mano que está en la frente.")
Q("cp10", "cpr", "The chest doesn’t rise with your breath. You should check…", "El pecho no se eleva al insuflar. Hay que comprobar…",
  [("your technique and that the airway isn’t blocked", "la técnica y que la vía aérea no esté obstruida"), ("the pulse in the wrist", "el pulso en la muñeca"), ("nothing, keep going faster", "nada, seguir más deprisa")],
  "Then repeat.", "Y repetir.")
Q("cp11", "cpr", "CPR on a child starts with…", "La RCP en un niño empieza con…",
  [("5 breaths, then 30 : 2", "5 ventilaciones y luego 30 : 2"), ("30 compressions", "30 compresiones"), ("only compressions", "solo compresiones")],
  "Mouth to mouth-and-nose.", "Boca a boca-nariz.")
Q("cp12", "cpr", "On a baby, chest compressions are done with…", "En un bebé, las compresiones se hacen con…",
  [("two fingers", "dos dedos"), ("both hands", "las dos manos"), ("the fist", "el puño")],
  "To avoid too much force.", "Para no ejercer demasiada fuerza.")
Q("cp13", "cpr", "How long do you continue CPR?", "¿Hasta cuándo se continúa la RCP?",
  [("Until help arrives or the person reacts", "Hasta que llegue la ayuda sanitaria o el herido reaccione"), ("For 2 minutes", "Durante 2 minutos"), ("Until you count to 100", "Hasta contar 100")],
  "Swapping rescuers if possible.", "Turnándose si es posible.")
Q("cp14", "cpr", "Current European guidelines say that someone not trained in rescue breaths should…", "Las guías europeas actuales dicen que quien no tiene formación en ventilaciones debe…",
  [("give chest compressions only", "hacer solo compresiones"), ("do nothing", "no hacer nada"), ("only give breaths", "hacer solo ventilaciones")],
  "The 112 operator will guide you.", "El operador del 112 te guiará.")

# ---------------------------------------------------------------- 4. bleeding
Q("bl1", "bleed", "The first thing to do with external bleeding is…", "Lo primero ante una hemorragia externa es…",
  [("press directly on the wound with gauze or clean cloth", "presionar directamente sobre la herida con una gasa o tela limpia"), ("apply a tourniquet", "hacer un torniquete"), ("wash the wound", "lavar la herida")],
  "Firm, direct pressure.", "Presión directa y firme.")
Q("bl2", "bleed", "The gauze is soaked with blood. You should…", "La gasa se empapa de sangre. Hay que…",
  [("put another one on top without removing the first", "poner otra encima sin retirar la anterior"), ("remove it and put a clean one", "retirarla y poner una limpia"), ("stop pressing", "dejar de presionar")],
  "Removing it reopens the wound.", "Retirarla reabre la herida.")
Q("bl3", "bleed", "According to your course, to control bleeding from an arm after pressing on the wound you…", "Según tu curso, para contener una hemorragia en el brazo tras presionar la herida se…",
  [("raise the arm and press in the armpit", "eleva el brazo y se presiona en el hueco de la axila"), ("lower the arm and press the wrist", "baja el brazo y se presiona la muñeca"), ("press the neck", "presiona el cuello")],
  "Where the main artery runs.", "Donde está la arteria.")
Q("bl4", "bleed", "According to your course, for bleeding in a leg you press…", "Según tu curso, en una hemorragia de la pierna se presiona…",
  [("in the fold of the groin, with the leg raised", "en el pliegue de la ingle, con la pierna elevada"), ("on the knee", "en la rodilla"), ("on the ankle", "en el tobillo")],
  "Where the artery runs.", "Donde está la arteria.")
Q("bl5", "bleed", "A tourniquet is…", "El torniquete es…",
  [("a last resort, placed above the wound", "un último recurso, colocado por encima de la herida"), ("the first thing to do", "lo primero que hay que hacer"), ("placed below the wound", "colocado por debajo de la herida")],
  "Your course: very dangerous, avoid it if possible.", "Tu curso: muy peligroso, evitar si es posible.")
Q("bl6", "bleed", "After applying a tourniquet you must…", "Tras hacer un torniquete hay que…",
  [("leave it on and visible, and note the time", "mantenerlo, visible, y anotar la hora"), ("loosen it every 5 minutes", "aflojarlo cada 5 minutos"), ("cover it with a blanket", "taparlo con una manta")],
  "For the medical team.", "Para los sanitarios.")
Q("bl7", "bleed", "A tourniquet is needed in case of…", "El torniquete es necesario en caso de…",
  [("amputation or very serious bleeding", "amputación o hemorragias muy graves"), ("a small cut", "un corte pequeño"), ("a nosebleed", "una hemorragia nasal")],
  "Only then.", "Solo entonces.")
Q("bl8", "bleed", "Blood coming out of the ear may mean…", "La salida de sangre por el oído puede indicar…",
  [("a fracture of the base of the skull", "una fractura de la base del cráneo"), ("a cold", "un resfriado"), ("nothing serious", "nada grave")],
  "Cover without plugging; lie on that ear.", "Cubrir sin taponar; tumbar sobre ese oído.")
Q("bl9", "bleed", "Internal bleeding that shows through an opening must…", "Las hemorragias internas exteriorizadas…",
  [("not be stopped or plugged", "no deben cortarse ni taponarse"), ("be plugged firmly", "deben taponarse con fuerza"), ("be treated with a tourniquet", "se tratan con torniquete")],
  "They are extremely serious.", "Son de extrema gravedad.")
Q("bl10", "bleed", "A conscious person bleeds from the nose after a crash. Keep their head…", "Un herido consciente sangra por la nariz tras un golpe. Su cabeza debe estar…",
  [("straight or tilted forward", "recta o hacia delante"), ("tilted back", "hacia atrás"), ("lower than the body", "más baja que el cuerpo")],
  "Unconscious: recovery position.", "Inconsciente: posición lateral de seguridad.")
Q("bl11", "bleed", "A conscious person coughs up blood (lung injury). Place them…", "Un herido consciente sangra por la boca al toser (pulmón). Se le coloca…",
  [("half-sitting", "semisentado"), ("face down", "boca abajo"), ("with the legs raised", "con las piernas elevadas")],
  "Unconscious: recovery position.", "Si está inconsciente, PLS.")
Q("bl12", "bleed", "Someone vomits blood (possible stomach injury). Place them…", "Alguien vomita sangre (posible lesión de estómago). Se le coloca…",
  [("in the recovery position", "en posición lateral de seguridad"), ("half-sitting with the head back", "semisentado con la cabeza atrás"), ("face up", "boca arriba")],
  "So they don’t choke.", "Para que no se asfixie.")

# ---------------------------------------------------------------- 4. shock
Q("sh1", "shock", "Shock can be caused by…", "El estado de shock puede deberse a…",
  [("a major loss of blood", "una pérdida importante de sangre"), ("eating too much", "comer demasiado"), ("the cold only", "solo el frío")],
  "Watch for its signs.", "Hay que vigilar sus síntomas.")
Q("sh2", "shock", "Which is a sign of shock?", "¿Cuál es un síntoma de shock?",
  [("Cold sweat and pale skin", "Sudor frío y piel pálida"), ("Red, hot skin", "Piel roja y caliente"), ("Slow, deep breathing", "Respiración lenta y profunda")],
  "Also a fast, weak pulse and fast, shallow breathing.", "También pulso rápido y débil y respiración rápida y superficial.")
Q("sh3", "shock", "In shock the pulse is usually…", "En el shock, el pulso suele ser…",
  [("fast and weak", "rápido y débil"), ("slow and strong", "lento y fuerte"), ("normal", "normal")],
  "And the breathing fast and shallow.", "Y la respiración rápida y superficial.")
Q("sh4", "shock", "The anti-shock position is…", "La posición antishock consiste en…",
  [("lying down with the head lower than the body", "tumbado con la cabeza más baja que el resto del cuerpo"), ("sitting up", "sentado"), ("lying on the side", "de lado")],
  "Legs raised.", "Piernas elevadas.")
Q("sh5", "shock", "A person in shock should be covered…", "A una persona en shock hay que taparla…",
  [("lightly, without making them sweat", "ligeramente, sin hacerle sudar"), ("with several blankets", "con varias mantas"), ("not at all", "nada")],
  "And no drinks.", "Y no darle bebidas.")
Q("sh6", "shock", "May you give a person in shock something to drink?", "¿Se puede dar de beber a una persona en shock?",
  [("No", "No"), ("Yes, water", "Sí, agua"), ("Yes, something hot", "Sí, algo caliente")],
  "Never give food or drink to the injured.", "Nunca dar bebida ni comida a los heridos.")

# ---------------------------------------------------------------- 5. injuries
Q("ij1", "injury", "A limb is visibly deformed after a crash. You should…", "Una extremidad está deformada tras un accidente. Debes…",
  [("not try to set the bone, and immobilise it", "no intentar recolocar el hueso, e inmovilizarla"), ("pull it straight", "estirarla"), ("massage it", "darle un masaje")],
  "Hold both ends.", "Sujetando los dos extremos.")
Q("ij2", "injury", "To immobilise a fracture you hold…", "Para inmovilizar una fractura se sujetan…",
  [("both ends", "los dos extremos"), ("only the end nearest the body", "solo el extremo más cercano al cuerpo"), ("nothing", "nada")],
  "Open fractures: cover and stop the bleeding.", "Abiertas: tapar y contener la hemorragia.")
Q("ij3", "injury", "Wounds should be covered with…", "Las heridas se cubren con…",
  [("sterile dressings", "apósitos estériles"), ("cotton wool", "algodón"), ("the person’s clothes", "la ropa del herido")],
  "Don’t handle or explore them.", "Sin manipular ni explorar.")
Q("ij4", "injury", "There is an object stuck in a wound. You should…", "Hay un objeto clavado en una herida. Debes…",
  [("leave it, dress around it and immobilise it all together", "dejarlo, fijarlo con un vendaje e inmovilizar en bloque"), ("pull it out carefully", "sacarlo con cuidado"), ("push it in further", "introducirlo más")],
  "Removing it can worsen the injury and bleeding.", "Retirarlo puede aumentar la lesión y la hemorragia.")
Q("ij5", "injury", "If internal organs come out of a wound, you should…", "Si hay salida de vísceras, hay que…",
  [("lay the person down and cover the organs with damp cloths, without touching them", "tumbar al herido y cubrir los órganos con paños húmedos, sin tocarlos"), ("push them back in", "introducirlas de nuevo"), ("cover them with dry cotton wool", "cubrirlas con algodón seco")],
  "Don’t move the person otherwise.", "Sin mover más al herido.")
Q("ij6", "injury", "On a burn you should apply…", "Sobre una quemadura hay que aplicar…",
  [("cold water and damp sterile dressings", "agua fría y apósitos estériles húmedos"), ("cream or ointment", "pomada"), ("oil", "aceite")],
  "No creams.", "Sin pomadas.")
Q("ij7", "injury", "Clothing stuck to a burn should…", "La ropa pegada a una quemadura…",
  [("not be removed", "no se debe quitar"), ("be pulled off quickly", "se arranca rápidamente"), ("be cut and pulled off", "se corta y se arranca")],
  "And don’t burst blisters.", "Y no pinchar las ampollas.")
Q("ij8", "injury", "Blisters from a burn should…", "Las ampollas de una quemadura…",
  [("be left alone — not burst or cut", "no se manipulan: ni pinchar ni cortar"), ("be burst", "se pinchan"), ("be cut off", "se cortan")],
  "Risk of infection.", "Riesgo de infección.")
Q("ij9", "injury", "Burns on different parts of the body should be bandaged…", "Las quemaduras en distintas zonas se vendan…",
  [("separately", "por separado"), ("together", "juntas"), ("never", "nunca")],
  "Raise the burnt area.", "Y elevar la zona quemada.")
Q("ij10", "injury", "Someone has burns on the face. Watch especially for…", "Alguien tiene quemaduras en la cara. Hay que vigilar especialmente…",
  [("breathing problems", "problemas respiratorios"), ("a broken leg", "una pierna rota"), ("hearing", "la audición")],
  "And possible shock.", "Y un posible shock.")
Q("ij11", "injury", "A person’s clothes catch fire. You should…", "La ropa de una persona se incendia. Hay que…",
  [("cover them with a blanket or roll them on the ground", "cubrirla con una manta o hacerla rodar por el suelo"), ("make them run", "hacerla correr"), ("aim the extinguisher at the face", "apuntar el extintor a la cara")],
  "Never aim an extinguisher at the face.", "Nunca apuntar el extintor a la cara.")
Q("ij12", "injury", "Raising a burnt limb…", "Elevar una extremidad quemada…",
  [("reduces pain and swelling", "disminuye el dolor y la hinchazón"), ("makes the burn worse", "empeora la quemadura"), ("is forbidden", "está prohibido")],
  "Keep watching for shock.", "Vigilar un posible shock.")

# ---------------------------------------------------------------- 6–7. transport and kit
Q("tr1", "transport", "To take the injured to hospital you should…", "Para trasladar a los heridos hay que…",
  [("wait for the ambulance", "esperar a la ambulancia"), ("use the first car available", "usar el primer coche disponible"), ("call a taxi", "llamar a un taxi")],
  "A private car only exceptionally.", "Un coche particular solo excepcionalmente.")
Q("tr2", "transport", "You may use a private car to move an injured person when…", "Se puede usar un coche particular para trasladar a un herido cuando…",
  [("help can’t be requested at all, or it is very late and they get worse", "no se puede pedir ayuda, o se retrasa mucho y el herido empeora"), ("they are slightly hurt", "está levemente herido"), ("it is faster", "es más rápido")],
  "And they can travel immobilised in a suitable position.", "Y puede ir inmovilizado en una posición adecuada.")
Q("tr3", "transport", "‘Help is late’ means, according to your course, more than…", "«La ayuda se retrasa» significa, según tu curso, más de…",
  [("30 minutes since it was called", "30 minutos desde que se solicitó"), ("5 minutes", "5 minutos"), ("2 hours", "2 horas")],
  "With uncontrolled bleeding, worsening shock or a tourniquet.", "Con hemorragia que no se contiene, shock en aumento o torniquete.")
Q("tr4", "transport", "When carrying an injured person in a private car you must keep…", "Al trasladar a un herido en coche particular hay que mantener…",
  [("the head–neck–trunk aligned", "alineado el eje cabeza-cuello-tronco"), ("the windows closed", "las ventanillas cerradas"), ("the radio on", "la radio encendida")],
  "And go with them to watch their state.", "Y acompañarlo para vigilar su estado.")
Q("tr5", "transport", "A private car on an urgent run warns other drivers…", "Un coche particular en servicio de urgencia advierte a los demás…",
  [("with the horn and hazard lights, or by waving a handkerchief", "con el claxon y las luces de emergencia, o agitando un pañuelo"), ("by ignoring traffic lights", "saltándose los semáforos"), ("by driving on the shoulder", "circulando por el arcén")],
  "And it must follow the traffic rules.", "Y debe respetar las normas de circulación.")
Q("tr6", "transport", "A private car taking an injured person to hospital…", "Un coche particular que lleva a un herido al hospital…",
  [("must still respect the traffic rules", "debe respetar las normas de circulación"), ("may exceed the speed limits", "puede superar los límites de velocidad"), ("is a priority vehicle", "es un vehículo prioritario")],
  "It is not a priority vehicle.", "No es un vehículo prioritario.")
Q("tr7", "transport", "A first-aid kit in a car is…", "El botiquín en un turismo es…",
  [("not compulsory, but recommended", "no obligatorio, pero sí recomendable"), ("compulsory", "obligatorio"), ("forbidden", "prohibido")],
  "Keep it usable.", "Que esté en condiciones de uso.")
Q("tr8", "transport", "Which item is useful in a car first-aid kit?", "¿Qué elemento es útil en un botiquín del coche?",
  [("Sterile dressings and gloves", "Apósitos estériles y guantes"), ("Sleeping pills", "Somníferos"), ("Ointment for burns", "Pomada para quemaduras")],
  "Also bandages, gauze, tape, scissors, disinfectant…", "También vendas, gasas, esparadrapo, tijeras, desinfectante…")
