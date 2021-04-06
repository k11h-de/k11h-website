#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from datetime import datetime

AUTHOR = 'Karsten'
SITENAME = 'k11h DevOps'
SITETITLE = "k11h DevOps"
SITESUBTITLE = "professional devops services"
SITEURL = ''
SITELOGO = SITEURL + "/images/logo.png"
THEME = "/home/k11h/pelican-themes/Flex"
PATH = 'content'
COPYRIGHT_YEAR = datetime.now().year
ROBOTS = "index, follow"
TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Xing', 'https://www.xing.com/profile/Karsten_Brusch/cv'),
        ('github', 'https://github.com/k11h-de'))

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# THEME
THEME_COLOR = 'light'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

PYGMENTS_STYLE = 'emacs'
PYGMENTS_STYLE_DARK = 'monokai'

USE_LESS = True
PAGE_ORDER_BY = "menu_item"