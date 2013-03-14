#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Wood'
SITENAME = u"Wood's Linux Zen"
SITEURL = u'http://localhost'
SITE_SOURCE = u"https://github.com/coldnight/coldnight.github.com"
SITE_TAGLINE = u"分享技术,分享点滴"
FEED_DOMAIN = u"http://localhost"

DISQUS_SITENAME = u"linuxzen"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

THEME = "neat"

DEFAULT_CATEGORY = u"Python"


AUTHOR_SHORTBIO = u"喜欢重复的造轮子"

AUTHOR_EMAIL = u"wh_linux@126.com"

from hashlib import md5
AUTHOR_EMAIL_HASH = md5(AUTHOR_EMAIL).hexdigest()

GITHUB_USERNAME = u'coldnight'

GITHUB_BADGE = False

STATIC_PATHS = ["upload"]
# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10


MD_EXTENSIONS =  (['codehilite','extra', 'fenced_code'])
