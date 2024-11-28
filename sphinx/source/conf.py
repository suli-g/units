# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
from nt import environ
import sys
import os
import dotenv
import django

sys.path.insert(0, os.path.abspath("../.."))

dotenv.load_dotenv("../..")
django.setup()

project = "Units"
copyright = "2024, Sulaiman Gafoor"
author = "Sulaiman Gafoor"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinxcontrib_django",
]


templates_path = ["_templates"]
exclude_patterns = ["doc_utils", "migrations"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_baseurl = environ.get("GITHUB_PAGES_URL")
html_static_path = ["_static"]
django_show_db_tables = True
django_show_db_tables_abstract = True
