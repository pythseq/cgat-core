#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# CGATCore documentation build configuration file, created by
# sphinx-quickstart on Sat Mar  3 13:24:26 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.extend(os.path.abspath('../CGATCore'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.imgmath',
              'sphinx.ext.ifconfig',
              'sphinx.ext.inheritance_diagram',
              'sphinxcontrib.programoutput',
              'sphinx.ext.intersphinx',
              'sphinx.ext.napoleon',
              'CGATReport.report_directive']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'CGATCore'
copyright = '2018, CGAT Developers'
author = 'CGAT Developers'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
#'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}

# Included at the end of each rst file
rst_epilog = '''
.. _CGAT Training Programme: http://www.cgat.org
.. _CGAT Pipeline Collection: https://www.cgat.org/downloads/public/CGATPipelines/documentation/
.. _CGAT Code Collection: https://www.cgat.org/downloads/public/cgat/documentation/
.. _pysam: https://github.com/pysam-developers/pysam
.. _samtools: http://samtools.sourceforge.net/
.. _htslib: http://www.htslib.org/
.. _tabix: http://samtools.sourceforge.net/tabix.shtml/
.. _Galaxy: https://main.g2.bx.psu.edu/
.. _cython: http://cython.org/
.. _python: http://python.org/
.. _ipython: http://ipython.org/
.. _pyximport: http://www.prescod.net/pyximport/
.. _sphinx: http://sphinx-doc.org/
.. _ruffus: http://www.ruffus.org.uk/
.. _cgatreport: https://github.com/AndreasHeger/CGATReport/
.. _sqlite: http://www.sqlite.org/
.. _make: http://www.gnu.org/software/make
.. _UCSC: http://genome.ucsc.edu
.. _ENSEMBL: http://www.ensembl.org
.. _GO: http://www.geneontology.org
.. _gwascatalog: http://www.genome.gov/gwastudies/
.. _distlid: http://distild.jensenlab.org/
.. _mysql: https://mariadb.org/
.. _postgres: http://www.postgresql.org/
.. _bedtools: http://bedtools.readthedocs.org/en/latest/
.. _UCSC Tools: http://genome.ucsc.edu/admin/git.html
.. _git: http://git-scm.com/
.. _sge: http://wiki.gridengine.info/wiki/index.php/Main_Page
.. _alignlib: https://github.com/AndreasHeger/alignlib
.. _iGenomes: https://support.illumina.com/sequencing/sequencing_software/igenome.html
'''
# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'CGATCoredoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'CGATCore.tex', 'CGATCore Documentation',
     'CGAT Developers', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'cgatcore', 'CGATCore Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'CGATCore', 'CGATCore Documentation',
     author, 'CGATCore', 'One line description of project.',
     'Miscellaneous'),
]



