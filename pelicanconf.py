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

# different layout for pages and blog
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'
INDEX_SAVE_AS = 'blog/index.html'
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_LANG_URL = 'blog/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = 'blog/{slug}-{lang}.html'
CATEGORY_SAVE_AS = ''
ARCHIVES_SAVE_AS = 'blog/archives.html'
TAGS_SAVE_AS = 'blog/tags.html'
TAG_URL = 'blog/tag/{slug}.html'
TAG_SAVE_AS = 'blog/tag/{slug}.html'
AUTHOR_SAVE_AS = ''

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
    ('blog', '/blog/index.html'),
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
