#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from datetime import datetime

AUTHOR = 'Karsten'
SITENAME = 'k11h DevOps'
SITETITLE = "k11h DevOps"
SITESUBTITLE = "professional devops services"
SITEURL = ''
SITELOGO = "/images/logo.png"
FAVICON = '/images/favicon.ico'
THEME = "theme"
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
USE_GOOGLE_FONTS = False
STATIC_PATHS = ['extra', 'images' ] 
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}
USE_FOLDER_AS_CATEGORY = True
LINKS = (
    ('---',' '),
    ('articles', '/archives.html'),
    ('tags', '/tags.html')
)
# # Social widget
SOCIAL = (
    ("github", "https://github.com/k11h-de"),
    ("xing", "https://www.xing.com/profile/Karsten_Brusch/cv"),
    ("amazon", "https://www.amazon.de/hz/wishlist/ls/16BKUO7S8QAYB"),
    ("rss", "/feeds/all.atom.xml"),
    ("git-alt", "https://github.com/k11h-de/k11h-website"),
)

DEFAULT_PAGINATION = 5
DISABLE_URL_HASH = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# THEME
THEME_COLOR = 'dark'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True

PAGE_ORDER_BY = "menu_item"

CUSTOM_CSS = "/extra/custom.css"
