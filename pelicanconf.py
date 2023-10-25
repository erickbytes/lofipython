AUTHOR = "@erickbytes"
SITENAME = "Lo-Fi Python"
SITEURL = "https://lofipython.com"
PATH = "content"
TIMEZONE = "America/Chicago"
DEFAULT_LANG = "en"
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
    ["Github", "https://github.com/erickbytes/lofipython"],
]
DEFAULT_PAGINATION = 10
THEME = "blue-penguin-dark"
GITHUB_URL = "https://github.com/erickbytes/lofipython.com"
STATIC_PATHS = ["blog", "theme", "static", "extra"]
ARTICLE_PATHS = ["blog", "theme", "static", "extra"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}
PYGMENTS_RST_OPTIONS = {"linenos": "table"}
ARTICLE_EXCLUDES = ["blog/drafts"]
# DARK_LIGHT_SWITCHING_OFF = False
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# SITEDESCRIPTION = ""
# LOAD_CONTENT_CACHE = False
