#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mt Taka'
SITENAME = 'D3C blog'
SITEURL = ''
DEFAULT_DATE_FORMAT = '%Y/%m/%d(%a)'

# markdown extention
MARKDOWN = {
    'extension_configs' : {
        'markdown.extensions.codehilite' : {'css_class': 'highlight'},
        'markdown.extensions.tables' : {},
        'markdown.extensions.fenced_code' : {},
        'linkify': {},
        'del_ins': {},
        'nl2br': {}
    }
}

# Plugin
PLUGIN_PATHS = ['../pelican-plugins', ]
PLUGINS = ['i18n_subsites', 'liquid_tags.notebook', 'tag_cloud', ]
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n'],}

# Themes
THEME = '../pelican-themes/pelican-bootstrap3'

# pelican-boostrap3 Setting
## Google Analytics
#GOOGLE_ANALYTICS_UNIVERSAL = "UA-124570016-1"
#GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = "UA-124570016-1"
## 各記事のヘッダー
SHOW_ARTICLE_CATEGORY = False
SHOW_DATE_MODIFIED = True
##ヘッダーのパンくずにカテゴリ表示
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

## Pygments Style
PYGMENTS_STYLE = 'autumn'

## サイドバー
ABOUT_ME = "著者の解説。このブログは技術習得のための学習記録が中心になるかと思う。"
DISPLAY_ARCHIVE_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 5

## ソーシャルボタン
ADDTHIS_PROFILE = "ra-5b8116442bd6e8ad"



PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
