#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from hashlib import md5

AUTHOR = u'Wood.D'
SITENAME = u"Wood.D's Record"
SITEURL = u'http://www.linuxzen.com'
SITE_SOURCE = u"https://github.com/coldnight/coldnight.github.com"
SITE_TAGLINE = u"木秀于林"
FEED_DOMAIN = u"http://www.linuxzen.com"

DISQUS_SITENAME = u"linuxzen"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

THEME = "neat"

DEFAULT_CATEGORY = u"Python"


AUTHOR_SHORTBIO = u"喜欢Linux和Python,用Vim编写程序,曾长时间使用cold这个id,"\
        u"现使用Wood.D作为以后长期id,现在维护一个gtalk群,有兴趣的可以加入,"\
        u"使用xmpp帐号添加:clubot@vim-cn.com`"

AUTHOR_EMAIL = u"wh_linux@126.com"

AUTHOR_EMAIL_HASH = md5(AUTHOR_EMAIL).hexdigest()

GITHUB_USERNAME = u'coldnight'

GITHUB_BADGE = False

STATIC_PATHS = [u"upload", ]
# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('eleven', 'eleveni386.7axu.com'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10


MD_EXTENSIONS =  (['codehilite','extra', 'fenced_code'])

FILES_TO_COPY = (
    ("404.html", "404.html"),
)
