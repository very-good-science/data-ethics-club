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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "Data Ethics Club"
copyright = "2024, Data Ethics Club Community"
author = "Data Ethics Club"

# The full version, including alpha/beta/rc tags
# release = " "


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser", 
    "sphinx_design",
    "ablog",
]

myst_enable_extensions = [
    "colon_fence",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- ABlog Options -------------------------------------------------

# Where should the root page of the blog be?
blog_path = "write_ups/write-ups"

# How many paragraphs of the post to show in a preview
post_auto_excerpt = 0

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
html_baseurl = "dataethicsclub.com"

html_theme_options = {
    "search_bar_text": "Search this site...",
    "show_prev_next": True,
    "footer_items": ["license-footer", "sphinx-version"],
    "use_edit_page_button": True,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/very-good-science/data-ethics-club",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Mailing List",
            "url": "https://www.jiscmail.ac.uk/cgi-bin/webadmin?SUBED1=DATAETHICSCLUB&A=1",
            "icon": "fa-regular fa-envelope",
        },
        {
            "name": "DEC Paper",
            "url": "https://doi.org/10.1016/j.patter.2022.100537",
            "icon": "fa-brands fa-readme",
        }
    ],
    "logo": {
        "text": "Data Ethics Club",
    },
}

html_context = {
    "github_user": "very-good-science",
    "github_repo": "data-ethics-club",
    "github_version": "main",
    "doc_path": "/site/",
}    



html_sidebars = {
    # Removes the left-hand Section Navigation from the following pages
    "index": [],
    "reading-list": [],
    "mailing-list": [],
    # Add blog sidebars
    # ref: https://ablog.readthedocs.io/en/stable/manual/ablog-configuration-options.html#sidebars
    "write_ups/*": [
        'ablog/postcard.html',
        'ablog/recentposts.html',
        "ablog/categories.html",
        "ablog/tagcloud.html",
        "ablog/authors.html",
        "ablog/archives.html",
        ]
}

html_favicon = "_static/favicon.png"
html_logo = "_static/logo.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = [
    'custom.css',
]
