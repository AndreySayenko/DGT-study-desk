# -*- coding: utf-8 -*-
"""Categories and topics shown on the main screen. Edit, then run `npm run build`.

Each category has 13 topics. A topic without a title here is shown as "Topic N".
A topic can be opened once build_site.py builds its page (BUILT in build_site.py); until then it shows
"Coming soon". To name a topic before it is written, add it to `titles`, for example:

    titles={1: T("Definitions and general concepts", "Definiciones y conceptos generales"),
            2: T("Road signs", "Señales")},
"""

N_TOPICS = 13


def T(en, es):
    return {"en": en, "es": es}


CATEGORIES = [
    dict(id="b", tag="B", name=T("Category B", "Permiso B"), sub=T("Cars", "Turismos"),
         titles={1: T("Definitions and general concepts", "Definiciones y conceptos generales"),
                 2: T("Use of the road", "Uso de las vías"),
                 3: T("Speed", "La velocidad"),
                 4: T("Priority", "La prioridad"),
                 5: T("Manoeuvres", "Las maniobras"),
                 6: T("Carrying people and goods", "Transporte de personas y mercancías"),
                 7: T("Lights", "Las luces"),
                 8: T("Signs and signals", "Las señales"),
                 9: T("Documentation", "Documentación"),
                 10: T("Accidents and their factors", "Los accidentes y sus factores"),
                 11: T("First aid", "Primeros auxilios"),
                 12: T("Driving techniques", "Técnicas de conducción"),
                 13: T("Vehicle maintenance and accessories", "Mantenimiento del vehículo y accesorios")}),
    dict(id="a", tag="A1 · A2", name=T("Category A1 / A2", "Permiso A1 / A2"), sub=T("Motorcycles", "Motocicletas"),
         titles={1: T("Definitions and general concepts", "Definiciones y conceptos generales"),
                 2: T("Use of the road", "Uso de las vías"),
                 3: T("Speed", "La velocidad"),
                 4: T("Priority", "La prioridad"),
                 5: T("Manoeuvres", "Las maniobras"),
                 6: T("Carrying people and goods", "Transporte de personas y mercancías"),
                 7: T("Lights", "Las luces"),
            8: T("Signs and signals", "Las señales"),
            9: T("Documentation", "Documentación"),
            10: T("Accidents and their factors", "Los accidentes y sus factores"),
            11: T("First aid", "Primeros auxilios"),
            12: T("Riding techniques", "Técnicas de conducción"),
            13: T("Maintenance and accessories", "Mantenimiento del vehículo y accesorios")}),
]


def topic_id(cat_id, n):
    """b, 1 -> "b-01". Used in page names (topics/b-01.html) and as the key for saved progress."""
    return f"{cat_id}-{n:02d}"
