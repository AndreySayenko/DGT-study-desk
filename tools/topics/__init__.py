# -*- coding: utf-8 -*-
"""Written topics. Each is a package here (b01, b02, ...) that provides:

  META       titles and intro text for the page and the PDF, per language, plus the PDF file name
  blocks()   the study text, as blocks from blocks.py
  quiz()     the PDF self-test: [(question, [A, B, C], index of the correct option, explanation)]
  SOURCES    [(title, url)]
  GLOSSARY   [(spanish term, english term)]
  BANK, TAGS the questions for the page's tests and the section recaps (see b01/bank.py)

To publish a new topic: add its package, list it in BUILT, and run `npm run build`.
The main screen then shows it as ready instead of "Coming soon"."""
import importlib

# topic id (as in catalog.py) -> package name
BUILT = {
    "b-01": "b01",
    "b-02": "b02",
    "b-03": "b03",
    "b-04": "b04",
    "b-05": "b05",
    "b-06": "b06",
    "b-07": "b07",
    "b-08": "b08",
    "b-09": "b09",
    "b-10": "b10",
    "b-11": "b11",
    "b-12": "b12",
    "b-13": "b13",
    "a-01": "a01",
    "a-02": "a02",
    "a-03": "a03",
    "a-04": "a04",
    "a-05": "a05",
    "a-06": "a06",
    "a-07": "a07",
    "a-08": "a08",
    "a-09": "a09",
    "a-10": "a10",
    "a-11": "a11",
    "a-12": "a12",
    "a-13": "a13",
}


def load(tid):
    return importlib.import_module(f"topics.{BUILT[tid]}")
