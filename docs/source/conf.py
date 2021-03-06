# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
#from importlib.machinery import SOURCE_SUFFIXES
import os
import sys
import mock
mock_modules = ['supervisor','board','pwmio','digitalio','busio','analogio']
for mod_name in mock_modules:
   sys.modules[mod_name] = mock.Mock()

sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../../Teensy'))
sys.path.insert(0, os.path.abspath('../../Teensy/Containers'))
sys.path.insert(0, os.path.abspath('../../Onion'))

import pid_object
import shift_object
import output_obj
import input_obj
import ltc2984
import uart_object
import settings_handler



# -- Project information -----------------------------------------------------

project = 'Loop Controller and Remote I/O'
copyright = '2022, Chris Heyden'
author = 'Chris Heyden'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        'sphinx.ext.autodoc',
        'myst_parser',
        'sphinx.ext.autosummary',
        'sphinx.ext.autosectionlabel'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

#SOURCE_SUFFIXES = ['.rst', '.md']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
