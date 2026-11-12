# -*- coding: utf-8 -*-
"""Building blocks for topic content. Every text is an {"en", "es"} pair made with T(en, es).
build_site.py and build_pdf.py know how to render each block."""


def T(en, es):
    return {"en": en, "es": es}


def pills(*items):
    return list(items)


# ------------------------------------------------------------------------------------------
# Block constructors
# ------------------------------------------------------------------------------------------
def H2(num, en, es):
    return ("h2", num, T(en, es))


def H3(en, es):
    return ("h3", T(en, es))


def P(en, es):
    return ("p", T(en, es))


def E(name_en, name_es, body_en, body_es, pills_=None, tip=None, kind="def"):
    """An entry card. name_* may contain <i> for the Spanish exam term."""
    return ("entry", T(name_en, name_es), T(body_en, body_es), pills_ or [], tip, kind)


def FIG(fn, cap_en, cap_es):
    return ("fig", fn, T(cap_en, cap_es))


def TABLE(head, rows, widths=None, cls=""):
    return ("table", head, rows, widths, cls)


def BOX(kind, title_en, title_es, items):
    """items: list of (en, es) pairs rendered as bullets."""
    return ("box", kind, T(title_en, title_es), [T(a, b) for a, b in items])


def BR():
    return ("pagebreak",)
