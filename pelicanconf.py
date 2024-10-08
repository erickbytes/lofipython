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
    ["Collaborate", "https://lofipython.com/contact"]
]
# ["Support Lo-Fi Python", "https://www.paypal.com/donate/?hosted_button_id=DSN3VYA899D9C"]
# ["Github", "https://github.com/erickbytes/lofipython"]
DEFAULT_PAGINATION = 10
THEME = "blue-penguin-dark"
GITHUB_URL = "https://github.com/erickbytes/lofipython.com"
STATIC_PATHS = ["blog", "theme", "static", "extra", "images"]
ARTICLE_PATHS = ["blog", "theme", "static", "extra", "images"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}
PYGMENTS_RST_OPTIONS = {"linenos": "table"}
ARTICLE_EXCLUDES = ["blog/drafts"]
PLUGIN_PATHS = ['home/erickbytes/lofipython']
# PLUGINS = ['pelican_webmention']
# DARK_LIGHT_SWITCHING_OFF = False
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# SITEDESCRIPTION = ""
# LOAD_CONTENT_CACHE = False
