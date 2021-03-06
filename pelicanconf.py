#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


# Site basic information
AUTHOR = u'O. A. Rodríguez'
SITENAME = u'Gatomontez'
SITEURL = 'http://gatomontez.com'
SITEDESCRIPTION = u'Manuales, tutoriales y recursos sobre programación.'

# Date
TIMEZONE = 'America/Mexico_City'
DATE_FORMATS = {
    'en': u'%A %d %B %Y',
    'es': u'%A, %d de %B, %Y'
}
# Languaje
DEFAULT_LANG = u'es'
DEFAULT_CATEGORY = u'sin-categoria'

# For Windows:
# See http://msdn.microsoft.com/en-us/library/39cwe7zf%28vs.71%29.aspx
# See http://msdn.microsoft.com/en-us/library/cdax410z%28VS.71%29.aspx
LOCALE = ('esm', 'es_MX', 'es', 'en_US' 'us')

# Articles
ARTICLE_URL = u'articulo/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = u'articulo/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_LANG_URL = u'articulo/{lang}/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_LANG_SAVE_AS = u'articulo/{lang}/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Pages
PAGE_URL = u'{slug}/'
PAGE_SAVE_AS = u'{slug}/index.html'
PAGE_LANG_URL = u'{lang}/{slug}/'
PAGE_LANG_SAVE_AS = u'{lang}/{slug}/index.html'

# Categories
CATEGORY_URL = u'categoria/{slug}/'
CATEGORY_SAVE_AS = u'categoria/{slug}/index.html'

# Tags
TAG_URL = u'tema/{slug}/'
TAG_SAVE_AS = u'tema/{slug}/index.html'

# Author
AUTHOR_URL = u'autor/{slug}/'
AUTHOR_SAVE_AS = u'autor/{slug}/index.html'

ARCHIVES_SAVE_AS = u'archivo/index.html'
AUTHORS_SAVE_AS = u'autores/index.html'
CATEGORIES_SAVE_AS = u'categorias/index.html'
TAGS_SAVE_AS = u'temas/index.html'

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'smarty']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('IPython', 'http://ipython.org/'),
    ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (
    ('facebook', 'http://www.facebook.com/gatomontezweb'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme
THEME = u'./themes/gmzblue'
THEME_STATIC_DIR = u'theme'

# Static files go here
STATIC_PATHS = [
    'images',
    'pictures',
    '.htaccess',
    'humans.txt',
    'robots.txt',
    'favicon.ico'
]

# Summary
SUMMARY_MAX_LENGTH = 30

# Plugins
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['gravatar']

# Gravatar
AUTHOR_EMAIL = 'oarodriguez@live.com.mx'
GRAVATAR_URL = 'https://www.gravatar.com/avatar/'

# Disqus
DISQUS_SITENAME = "gatomontez"

# Base layout params
LEFT_COLUMN_WIDTH = 4
RIGHT_COLUMN_WIDTH = 8

# Copyright message
# COPYRIGHT_MESSAGE = u'&copy; 2014, {sitename}, by {author}'.format(
#     sitename=SITENAME, author=AUTHOR)
