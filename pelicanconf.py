#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Angadh'
SITENAME = 'SpaceH'
SITEURL = ''

PATH = 'content'
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images']
ARTICLE_PATHS = ['articles']
HEADER_IMAGE = "HOWLER_Pic.jpeg"
PROFILE_PICTURE = "HOWLER_Pic.jpeg"
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

THEME = 'theme/solid_theme'

PLUGIN_PATHS = ['/Users/inertialframe/blog-plugins',
               ]
PLUGINS = ['pelican_javascript',
           'simple_footnotes',
           'obsidian']

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Angadh Nanjangud', 'https://www.sems.qmul.ac.uk/staff/a.nanjangud'),
         ('Twitter', 'https://twitter.com/1spaceman_spiff'),
         ('LinkedIn', 'https://www.sems.qmul.ac.uk/staff/a.nanjangud'))

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

CONTACTS = [
    ("Twitter", "twitter", "https://twitter.com/1spaceman_spiff"),
    #("Facebook", "facebook-f", "https://facebook.com/theanalogfox"),
    #("Instagram", "instagram", "https://www.instagram.com/theanalogfox/"),
    ("Email", "envelope", "info@theanalogfox.com"),
]

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
