RSS Is Thriving: Working With RSS Python Tools
##############################################
:date: 2023-09-18 17:14
:author: lofipython
:category: coding, programming, python, XML, RSS, writing
:tags: python RSS tools, RSS aggregator, RSS validation, parsing RSS python, RSS feeds, python RSS readers
:slug: working-with-rss-in-python
:status: published

There have been countless obituaries about RSS on the internet, like when Dan McKinley wrote that `"Google Reader Killed RSS" <https://mcfunley.com/google-reader-killed-rss>`__. For sure, the existence of Google Reader had an impact on other readers gaining a wider audience before it was shut down by Google. This likely did have a suppressive impact on the adoption of RSS.

"Whatever happened to RSS?" is a question that murmurs thorugh the internet. The answer: it's still here and it's not going anywhere. I propose that RSS is not dead, but quietly regaining its strength and is on track to relevancy again. But did it actually fall off?

    **Did you know?** RSS stands for "Really Simple Syndication".    

Some say with the rise of social media and email newsletters, RSS is not worth the time. That's precisely what the social media and search engine giants want so you'll stay in their walled garden platform. Google killed Google Reader because it is not in their interests to support a syndication format that cuts out their search engine middleman role. Nonetheless, we only need to consciously choose to use RSS to bring it back to prominence. Who's with me?!

    "RSS readers have not only survived in the era of social media, 
    but are driving more and more attention back to themselves, as people are realizing the pitfalls"
    
    
    \- Brian Barrett. "It's Time for an RSS Revival". Wired. https://www.wired.com/story/rss-readers-feedly-inoreader-old-reader

You'll often hear the term "aggregator" or "reader" when dealing with RSS, which both mean "tool that collects multiple RSS feeds into single readable format". There are plenty of free RSS reader websites to keep up with new material from your favorite websites. Currently, I use `Feeder <https://feeder.co>`__ to keep up with the blogs I follow. Their free plan allows you to follow up to 200 RSS feeds for free. `Feedly <https://feedly.com>`__ is a commonly suggested RSS reader also. 
 

.. image:: {static}/images/rssicon.png
  :alt: RSS icon


**A Few Benefits of RSS**

- Receive notice when a new post is published by your favorite websites and blogs.

- The personal data of your readers is not collected.

- An RSS subscription is less intrusive compared to blasting into someone's cluttered email inbox. Plus you won't end up in the spam folder.

- Diversify your website's traffic to be less dependent on search engines and social media platforms. 

    To know approximately how much RSS traffic you have, check how many HTTP requests have an XML content type. `This blog post <https://darekkay.com/blog/rss-subscriber-count/>`__ has a good breakdown of this HTTP based approach. Typically, 6% of total HTTP requests on my blog have XML content type, indicating RSS traffic.

Python RSS Tools
----------------

The rest of this post will highlight some practical Python tools and resources for RSS. The libraries used in the below code examples can be installed with `pip <https://pip.pypa.io/en/stable/user_guide/>`__. There are also some standard library Python tools mentioned. Enjoy!

`feedparser <https://github.com/kurtmckee/feedparser>`__: Universal Feed Parser is a Python module for downloading and parsing syndicated feeds

**Parse an RSS feed with feedparser.**

.. code-block:: python

    import feedparser
    
    feed = "https://feedparser.readthedocs.io/en/latest/examples/atom10.xml"
    d = feedparser.parse(feed)
    print(d['feed']['title'])
    print(d.feed.published)

**Detect a malformed RSS feed with feedparser "bozo".**

.. code-block:: python

    import feedparser
    
    # https://feedparser.readthedocs.io/en/latest/bozo.html#detecting-a-non-well-formed-feed
    feed = "http://feedparser.org/tests/illformed/rss/aaa_illformed.xml"
    d = feedparser.parse(feed)
    # d.bozo: An integer, either 1 or 0. Set to 1 if the feed is not well-formed XML, and 0 otherwise.
    print(d.bozo)
    if d.bozo:
        exc = d.bozo_exception
        # Print bozo error message.
        print(exc.getMessage())
        # Print line number where exception occurred.
        print(f"Error at line {exc.getLineNumber()}")
    else:
        print("Feed is well-formed RSS.")
    

`feedvalidator <https://www.feedvalidator.org/>`__ and `W3 RSS Validator <https://validator.w3.org/feed/>`__: check if your feed is valid RSS or Atom. Below shows how you can validate your feed using the webbrowser module with the Python CLI:

.. code-block:: console

    # Validate an RSS feed.    
    python -m webbrowser -t "https://validator.w3.org/feed/check.cgi?url=https://example.com/feeds/all.rss.xml"
    
    
`atoma <https://github.com/NicolasLM/atoma>`__: an Atom, RSS and JSON feed parser

**Parse an RSS feed with atoma.**

.. code-block:: python

   import atoma
   import requests
   
   response = requests.get("https://example.com/feed.atom")
   feed = atoma.parse_atom_bytes(response.content)
   print(feed.title.value)


**Additional RSS Tools, Reads + Resources**

`It's Time for an RSS Revival, Wired <https://www.wired.com/story/rss-readers-feedly-inoreader-old-reader/>`__

`Mozilla Thunderbird <https://en.wikipedia.org/wiki/Mozilla_Thunderbird>`__: an open source RSS client

`Awesome Tech RSS <https://github.com/tuan3w/awesome-tech-rss>`__: a list of tech RSS feeds you can follow

`pelican-planet <https://pypi.org/project/pelican-planet/>`__: a Pelican static site generator plugin that allows generating a page aggregating blog articles from other web sites. The `pelican Python library <https://docs.getpelican.com/en/latest/>`__ also has built-in support for RSS and Atom feed generation.

`Django Syndication Feed Framework <https://docs.djangoproject.com/en/4.2/ref/contrib/syndication/#module-django.contrib.syndication>`__: built-in RSS feed framework for Django websites

`django-yarr <https://github.com/radiac/django-yarr>`__: a lightweight, customisable RSS reader for the Django web framework

`python-feedgen <https://github.com/lkiesow/python-feedgen>`__: generates atom feeds, RSS feeds and podcasts

`A Roadmap to XML Parsers in Python, Real Python <https://realpython.com/python-xml-parser/>`__

`lxml <https://pypi.org/project/lxml/>`__: a Pythonic, mature binding for the libxml2 and libxslt libraries

`xml.sax <https://docs.python.org/3/library/xml.sax.handler.html>`__ API: standard library XML validation option that is based on a Java API

`Python Documentation, XML Processing Modules <https://docs.python.org/3/library/xml.html>`__

`RSSerpent <https://github.com/RSSerpent/RSSerpent>`__: open source software to create RSS feeds for websites without them

`rawdog <http://offog.org/git/rawdog/README>`__: an "RSS aggregator without visions of grandeur"

`RSS2mastodon <https://github.com/ai6yr/rss2mastodon>`__: a quick set of python scripts for auto-posting an RSS or Atom feed to Mastodon

`Craigslist RSS Scraper Python Script <https://github.com/anhqle/craigslist>`__

