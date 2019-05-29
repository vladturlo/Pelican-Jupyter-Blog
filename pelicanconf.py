#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Vlad Turlo'
SITENAME = "Vlad Turlo's Blog"
SITEURL = '/index.html'
SITETITLE = AUTHOR
SITESUBTITLE = 'def my_blog(your_attention): return GreatMood'
SITEDESCRIPTION = 'Just sharing what I have learned ...'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'En'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Main Menu
MAIN_MENU = True
MENUITEMS = (('Archives', '/archives.html'),('Categories', '/categories.html'),('Tags', '/tags.html'),)

#LINKS = (('About', '/about.html'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./pelican-plugins', ]
PLUGINS = ['pelican-ipynb.markup', ]

IGNORE_FILES = [".ipynb_checkpoints"]

THEME = './pelican-themes/Flex'

GITHUB_URL = 'https://github.com/vladturlo'
TWITTER_USERNAME = 'TurloVladyslav'

SOCIAL = (('twitter', 'https://twitter.com/TurloVladyslav'),
          ('facebook', 'https://www.facebook.com/vlad.turlo'),
          ('linkedin', 'https://www.linkedin.com/in/vladturlo/'),
          ('github', 'https://github.com/vladturlo'),
          )

SITELOGO = '/images/face.jpg'
FAVICON = '/images/favicon.ico'

LOAD_CONTENT_CACHE = False
