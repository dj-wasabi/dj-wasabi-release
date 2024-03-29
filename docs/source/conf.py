# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx_adc_theme

html_theme = "sphinx_adc_theme"
html_theme_path = [sphinx_adc_theme.get_html_theme_path()]

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../../lib'))
# currentPath = os.path.dirname(os.path.realpath(__file__))
# libraryDir = os.path.join(currentPath, "../lib")
# sys.path.append(libraryDir)


# -- Project information -----------------------------------------------------

project = 'djWasabi'
copyright = '2021, Werner Dijkerman'
author = 'Werner Dijkerman'

# The full version, including alpha/beta/rc tags
release = '0.4.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']

# extensions = [
# ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
# html_theme = 'bootstrap-astropy'

# html_theme_options = {
#     'logotext1': 'djWasabi',  # white,  semi-bold
#     'logotext2': '',  # orange, light
#     'logotext3': ':docs',   # white,  light
#     'astropy_project_menubar': False
# }


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
