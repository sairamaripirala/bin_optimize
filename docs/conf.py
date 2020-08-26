import os
import sys

import sphinx_material

sys.path.insert(0, os.path.abspath('../'))
html_theme = 'sphinx_material'
html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()
html_sidebars = {
    '**': ['globaltoc.html', 'searchbox.html']
}
html_theme_options = {
    'base_url': 'http://bin-optimize.readthedocs.io',
    'repo_url': 'https://github.com/saripirala/bin-optimize/',
    'repo_name': 'bin-optimize',
    'html_minify': True,
    'css_minify': True,
    'nav_title': 'bin-optimize',
    'globaltoc_depth': 2,
    'theme_color': '0000aa',
    'logo_icon': '&#x2286',
    'color_primary': 'grey',
    'color_accent': 'blue',
    'version_dropdown': False
}
html_css_files = [
    'css/custom.css'
]


project = 'bin-optimize'
copyright = '2020, Sairam Aripirala'
author = 'Sairam Aripirala'

extensions = extensions = [
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx_material'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
