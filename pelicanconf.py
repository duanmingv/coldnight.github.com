#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from hashlib import md5

AUTHOR = u'cold'
SITENAME = u"cold's world"
SITEURL = u'http://www.linuxzen.com'
SITE_SOURCE = u"https://github.com/coldnight/coldnight.github.com"
SITE_TAGLINE = u"木秀于林"
FEED_DOMAIN = u"http://www.linuxzen.com"
FEED_ATOM = u"feeds/all.atom.xml"

DISQUS_SITENAME = u"linuxzen"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

THEME = "tuxlite_tbs"

DEFAULT_CATEGORY = u"Python"


AUTHOR_SHORTBIO = u"喜欢Linux和Python,用Vim编写程序,"\
        u"现在维护一个gtalk群,有兴趣的可以加入,"\
        u"使用xmpp帐号添加:clubot@vim-cn.com`"

AUTHOR_EMAIL = u"wh_linux@126.com"

AUTHOR_EMAIL_HASH = md5(AUTHOR_EMAIL).hexdigest()

GITHUB_USERNAME = u'coldnight'

GITHUB_BADGE = False

GITHUB_URL = u"https://github.com/coldnight/coldnight.github.com"

STATIC_PATHS = [u"upload", ]
# Blogroll
LINKS =  (('eleven', 'http://eleveni386.7axu.com'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10


MD_EXTENSIONS =  (['codehilite','extra', 'fenced_code'])

FILES_TO_COPY = (
    ("extra/404.html", "404.html"),
    ("extra/googledbee14f7be5461f0.html", "googledbee14f7be5461f0.html"),
    ("extra/robots.txt", "robots.txt"),
    ("extra/bdsitemap.txt", "bdsitemap.txt"),
)


PLUGINS = ['pelican.plugins.sitemap',]

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}
