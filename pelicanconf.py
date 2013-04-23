#!/usr/bin/env python
# -*- coding: utf-8 -*- #

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

ARCHIVES_URL = "archives.html"

GITHUB_URL = u"https://github.com/coldnight/coldnight.github.com"

FLOW_CONTENT = u"""<script src="http://s96.cnzz.com/stat.php?id=3767683&web_id=3767683&show=pic" language="JavaScript"></script>"""

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

PLUGIN_PATH = u"pelican-plugins"
PLUGINS = ['sitemap', 'gzip_cache']

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

DESCRIPTION = u"博主一个爱好开源技术的人, 对Python比较熟悉,"\
        u"也喜欢用Python捣腾一些东西, 本博主要分享一些开源技术,"\
        u"其中包括但不限于Linux/Python/Vim."

KEYWORDS = u"Python, Linux, vim, 开源"
