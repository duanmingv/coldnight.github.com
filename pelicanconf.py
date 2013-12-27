#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'cold'
SITENAME = u"cold's world"
SITEURL = u'http://www.linuxzen.com'
SITE_SOURCE = u"https://github.com/coldnight/coldnight.github.com"
SITE_TAGLINE = u"木秀于林"
FEED_DOMAIN = SITEURL
FEED_ATOM = None
FEED_ALL_ATOM = u"feeds/all.atom.xml"

DISQUS_SITENAME = u"linuxzen"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

THEME = "tuxlite_tbs"

DEFAULT_CATEGORY = u"Python"

ARCHIVES_URL = "archives.html"

GITHUB_URL = u"https://github.com/coldnight/coldnight.github.com"

FLOW_CONTENT = u"""<script src="http://s96.cnzz.com/stat.php?id=3767683&web_id=3767683&show=pic" language="JavaScript"></script>"""

STATIC_PATHS = [u"static/upload",
                "extra/robots.txt",
                "extra/bdsitemap.txt",
                "extra/googledbee14f7be5461f0.html",
                "extra/404.html",
                ]
# STATIC_SAVE_AS = "static/upload/"
EXTRA_PATH_METADATA = {
    "extra/robots.txt":{"path":"robots.txt"},
    "extra/bdsitemap.txt": {"path": "bdsitemap.txt"},
    "extra/googledbee14f7be5461f0.html": {"path":"googledbee14f7be5461f0.html"},
    "extra/404.html": {"path":"404.html"},
}
# Blogroll
LINKS =  (('eleven', 'http://eleveni386.7axu.com'),
          (u'小邪兽_deepin',"http://neteue.com"),
          (u'Frantic1048', "http://frantic1048.com/"),
          (u"晓风'Blog", "http://www.dongxf.com/"),
          )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

MD_EXTENSIONS =  (['codehilite(css_class=highlight)', 'extra',
                   'fenced_code', 'tables', 'sane_lists'])

PLUGIN_PATH = u"pelican-plugins"
PLUGINS = ['sitemap']#, 'gzip_cache']

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
