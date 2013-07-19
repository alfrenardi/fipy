# -*- coding: utf-8 -*-
#
# FiPy documentation build configuration file, created by
# sphinx-quickstart on Sat Aug 29 21:50:21 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(os.path.abspath('sphinxext'))
sys.path.append(os.path.abspath('tutorial'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 
              'sphinx.ext.doctest', 
              'sphinx.ext.intersphinx', 
              'sphinx.ext.todo', 
              'sphinx.ext.coverage', 
              'sphinx.ext.pngmath', 
              'sphinx.ext.ifconfig',
              'sphinx.ext.autosummary',
              'numpydoc',
              'bibstuff.sphinxext.bibref',
              'sphinxcontrib.traclinks',
              'redirecting_html']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.txt'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'documentation/contents'

# General information about the project.
project = u'FiPy'
copyright = u'2004-2012, Jonathan E. Guyer, Daniel Wheeler & James A. Warren'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#

import fipy

# The short X.Y version.
version = fipy.__version__
# The full version, including alpha/beta/rc tags.
release = fipy.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
unused_docs = ['documentation/RESOURCES',
               'documentation/TODOLIST', 
               'documentation/VERSION']

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_patterns = ['fipy/generated/modules.txt',
                    'fipy/generated/__init__.txt',
                    'build', 
                    'dist',
                    'FiPy.egg-info', 
                    'documentation/_build', 
                    'documentation/tutorial/package/generated/modules.txt',
                    'documentation/sphinxext',
                    'documentation/sphinxext/bibtex/bibstuff/examples/*.txt',
                    '**/.svn',
                    '**/.git']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

autoclass_content = "both"

autosummary_generate = ['examples/diffusion/index.txt',
                        'examples/convection/index.txt',
                        'examples/phase/index.txt',
                        'examples/levelSet/index.txt',
                        'examples/cahnHilliard/index.txt',
                        'examples/flow/index.txt',
                        'examples/reactiveWetting/index.txt',
                        'examples/updating/index.txt']
                        
autodoc_member_order = 'alphabetical'

traclinks_base_url = 'http://matforge.org/fipy'
                        
# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'nist'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}
html_sidebars = {'index': ['indexsidebar.html', 'searchbox.html', 'contact.html'],
                 '**': ['localtoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html', 'contact.html']}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {
    'index': 'index.html',
}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'FiPydoc'

# -- Options for LaTeX output --------------------------------------------------

common_preamble = r"""
    \usepackage[amssymb]{SIunits}
    \usepackage{changepage}

    \DeclareMathOperator{\erf}{erf}
    \providecommand{\abs}[1]{\lvert#1\rvert}
    """

latex_elements = {
    'fncychap': r"""
    \usepackage[PetersLenny]{fncychap}
    """,
    'preamble': common_preamble + r"""

    \makeatletter
    \renewcommand{\maketitle}{%
      \begin{titlepage}%
        \let\footnotesize\small
        \let\footnoterule\relax
        \ifsphinxpdfoutput
          \begingroup
          % This \def is required to deal with multi-line authors; it
          % changes \\ to ', ' (comma-space), making it pass muster for
          % generating document info in the PDF file.
          \def\\{, }
          \pdfinfo{
            /Author (\@author)
            /Title (\@title)
          }
          \endgroup
        \fi
        \changepage{1in}{}{1in}{0.5in}{}{-0.5in}{}{}{}
        \begin{flushright}%
          \fipylogo\par%
          \vskip 3em%
          {\rm\Huge\py@HeaderFamily \@title \par}%
          {\em\LARGE\py@HeaderFamily \py@release\releaseinfo \par}
          \vfill
          {\large\py@HeaderFamily \@author \par}
          \vfill
          {\py@authoraddress \par}
          \vfill
          {%\large
           \@date \par
           \vfill
           \vfill
           \vfill
           \vfill
           \vfill
           \vfill
           \includegraphics[trim=5 2 5 5,scale=1.]{nistident_flright_vec}\par
          }%
        \end{flushright}%\par
        \@thanks
      \end{titlepage}%
      \clearpage%
      \changepage{}{}{}{}{}{}{}{}{}
      \vspace*{\fill}
      \input LICENSE
      \rule{\textwidth}{0.1pt}
      \input DISCLAIMER
      \clearpage
      \setcounter{footnote}{0}%
      \let\thanks\relax\let\maketitle\relax
      %\gdef\@thanks{}\gdef\@author{}\gdef\@title{}
    }
    \makeatother

    \definecolor{redish}{rgb}{0.894,0.122,0.122}
    \definecolor{bluish}{rgb}{0.216,0.188,0.533}
    
    \authoraddress{Materials Science and Engineering Division \\
    and the Center for Theoretical and Computational Materials Science \\
    Material Measurement Laboratory}
    
    \newcommand{\fipylogo}{\scalebox{10}{\rotatebox{4}{\textcolor{redish}{\( \varphi \)}}\kern-.70em\raisebox{-.15em}{\textcolor{bluish}{\( \pi\)}}}}
    
    \ChNameVar{\fontsize{14}{16}\usefont{OT1}{phv}{m}{n}\selectfont} 
    \ChNumVar{\fontsize{60}{62}\usefont{OT1}{ptm}{m}{n}\selectfont} 
    \ChTitleVar{\Huge\bfseries\rm}
    \ChRuleWidth{1pt}
    """
}

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('documentation/manual', 'fipy.tex', 'FiPy Manual',
   r'Jonathan E. Guyer \\ Daniel Wheeler \\ James A. Warren', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = True

latex_additional_files = ['figures/nistident_flright_vec.pdf']

# Documents to append as an appendix to all manuals.
# latex_appendices = ['documentation/refs.bib_cited']

# If false, no module index is generated.
#latex_use_modindex = True

pngmath_latex_preamble = common_preamble

# refer to Python, NumPy, SciPy, matplotlib
intersphinx_mapping = {
    'python': ('http://docs.python.org/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None),
    'scipy': ('http://docs.scipy.org/doc/scipy/reference/', None),
    'matplotlib': ('http://matplotlib.sourceforge.net/', None)}
# intersphinx_mapping = {'http://docs.python.org/': None,
#                        'http://docs.scipy.org/doc/numpy/': None,
#                        'http://docs.scipy.org/doc/scipy/reference/': None,
#                        'http://matplotlib.sourceforge.net/': None}

def skip_numpy_not_numerix(app, what, name, obj, skip, options):
    import types
    if ((type(obj) in [types.FunctionType, 
                       types.BuiltinFunctionType,
                       types.ClassType, 
                       types.TypeType]) 
        and not (obj.__module__.startswith("fipy")
                 or obj.__module__.startswith("package"))):
            skip = True
    return skip
    
def setup(app):
    app.connect('autodoc-skip-member', skip_numpy_not_numerix)

    
    
