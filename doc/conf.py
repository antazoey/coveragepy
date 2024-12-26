# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/nedbat/coveragepy/blob/master/NOTICE.txt

"""Sphinx configuration."""

# coverage.py documentation build configuration file, created by
# sphinx-quickstart on Wed May 13 22:18:33 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import atexit
import os
import re
import sys
import tempfile

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# on_rtd is whether we are on readthedocs.org
on_rtd = os.getenv('READTHEDOCS') == 'True'

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.restbuilder',
    'sphinx.ext.napoleon',
    'sphinx_code_tabs',
    'sphinx_rtd_theme',
]

autodoc_typehints = "description"

# Add any paths that contain templates here, relative to this directory.
templates_path = []

# The suffix of source filenames.
source_suffix = {'.rst': 'restructuredtext'}

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Coverage.py'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# @@@ editable
copyright = "2009–2024, Ned Batchelder" # pylint: disable=redefined-builtin
# The short X.Y.Z version.
version = "7.6.10"
# The full version, including alpha/beta/rc tags.
release = "7.6.10"
# The date of release, in "monthname day, year" format.
release_date = "December 26, 2024"
# @@@ end

rst_epilog = f"""
.. |release_date| replace:: {release_date}
.. |coverage-equals-release| replace:: coverage=={release}
.. |doc-url| replace:: https://coverage.readthedocs.io/en/{release}
.. |br| raw:: html

  <br/>

"""

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_patterns = ["_build", "help/*"]

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

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

nitpick_ignore = [
    ("py:class", "DefaultValue"),
    ("py:class", "FilePath"),
    ("py:class", "types.FrameType"),
    ("py:class", "TWarnFn"),
    ("py:class", "TDebugCtl"),
]

nitpick_ignore_regex = [
    (r"py:class", r"coverage\..*\..*"),
]

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}
#html_style = "neds.css"
#html_add_permalinks = ""

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = ['_templates']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'media/sleepy-snake-circle-150.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_use_modindex = False

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = '.htm'

# Output file base name for HTML help builder.
htmlhelp_basename = 'coveragepydoc'

# -- Spelling ---

if any("spell" in arg for arg in sys.argv):
    # sphinxcontrib.spelling needs the native "enchant" library, which often is
    # missing, so only use the extension if we are specifically spell-checking.
    extensions += ['sphinxcontrib.spelling']
    names_file = tempfile.NamedTemporaryFile(mode='w', prefix="coverage_names_", suffix=".txt")
    with open("../CONTRIBUTORS.txt") as contributors:
        names = set(re.split(r"[^\w']", contributors.read()))
        names = [n for n in names if len(n) >= 2 and n[0].isupper()]
        names_file.write("\n".join(names))
        names_file.flush()
    atexit.register(os.remove, names_file.name)

    spelling_word_list_filename = ['dict.txt', names_file.name]
    spelling_show_suggestions = False


# Regexes for URLs that linkcheck should skip.
linkcheck_ignore = [
    # We have lots of links to GitHub, and they start refusing to serve them to linkcheck,
    # so don't bother checking them.
    r"https://github.com/nedbat/coveragepy/(issues|pull)/\d+",
    # When publishing a new version, the docs will refer to the version before
    # the docs have been published.  So don't check those links.
    fr"https://coverage.readthedocs.io/en/{release}$",
]

# https://github.com/executablebooks/sphinx-tabs/pull/54
sphinx_tabs_valid_builders = ['linkcheck']

# When auto-doc'ing a class, only write the class' docstring into the class docs,
# don't automatically include the __init__ docstring.
autoclass_content = "class"

prerelease = bool(max(release).isalpha())

def setup(app):
    """Configure Sphinx"""
    app.add_css_file('coverage.css')
    app.add_config_value('prerelease', False, 'env')
    print("** Prerelease = %r" % prerelease)
