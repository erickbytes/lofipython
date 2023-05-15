AUTHOR = "@erickbytes"
SITENAME = "Lo-fi Python"
SITEURL = "https://lofipython.com"

PATH = "content"

TIMEZONE = "America/Chicago"

DEFAULT_LANG = "en"
# Site Logo
SITELOGO = "images/python-powered-h-140x182.png"

# Feed generation is usually not desired when developing
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_ATOM = "feeds/all.atom.xml"
TAG_FEED_ATOM = "feeds/{slug}.tag.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"
MENUITEMS = [
    ["RSS", "feeds/all.rss.xml"],
    ["Atom", "feeds/all.atom.xml"],
    ["Github", "https://github.com/erickbytes/divbull"],
]

DEFAULT_PAGINATION = 10

THEME = "blue-penguin-dark"
GITHUB_URL = "https://github.com/erickbytes/pythonmarketer.com"
STATIC_PATHS = ["images", "blog", "theme", "static"]
ARTICLE_PATHS = ["images", "blog", "theme", "static"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}
# DARK_LIGHT_SWITCHING_OFF = False
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}
# HTML metadata
# SITEDESCRIPTION = ""
LOAD_CONTENT_CACHE = False