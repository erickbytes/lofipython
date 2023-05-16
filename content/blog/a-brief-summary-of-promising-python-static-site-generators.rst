8 Promising Python Static Site Generators
#########################################
:date: 2021-07-28 23:31
:author: pythonmarketer
:category: coding, programming, web development
:tags: creating your own blog, python, static site generator
:slug: a-brief-summary-of-promising-python-static-site-generators
:status: published

A static site generator creates static HTML and markdown files to serve as a website. They're commonly used to host blogs but not exclusively. I recently researched my options to roll a static site in Python. I'm assessing a few of them as a potential future self-hosted blogging solution for this Wordpress blog. Or maybe I'll spin up a new one!

   **Why Statics?**

   Most "modern" websites are *dynamic* in the sense that the contents of the site live in a database, and are converted into presentation-ready HTML only when a user wants to see the page. That's great. However, it presents some minor issues that static site generators try to solve.

   In a static site, the whole site, every page, *everything*, is created before the first user even sees it and uploaded to the server as a simple folder full of HTML files (and images, CSS, etc).

   The Nikola Handbook - https://getnikola.com/handbook.html#why-static

Static Site Generator Python Libraries
--------------------------------------

*listed in largest to smallest order by # of Github project stars*

**Pelican** \| `Github - 11K Stars <https://github.com/getpelican/pelican>`__

Seems to be the front running static site generator in Python's ecosystem. It contains a convenient pelican-importer tool to import existing content from WordPress, Dotclear, or RSS feeds. Enjoying the modular nature of the `pelican-plugins <https://github.com/pelican-plugins>`__ and `pelican-themes <https://github.com/getpelican/pelican-themes>`__!

**Lektor** \| `Github - 3.5K Stars <https://github.com/lektor/lektor>`__

Intriguing CMS project touting a "Python API", `plugins for tools like Webpack <https://www.getlektor.com/plugins/>`__ and talented maintainers including the author of Flask.

**Cactus** \| `Github - 3.5K stars <https://github.com/eudicots/Cactus>`__

"Simple but powerful `static website generator <http://mickgardner.com/2011/04/27/An-Introduction-To-Static-Site-Generators.html>`__ using Python and the `Django template system <http://docs.djangoproject.com/en/dev/topics/templates/>`__... typical users would be designers that are tech-savvy, want to use templates, but don't like to mess with setting up django or S3." (Mac OS) `Demo Video <https://vimeo.com/46999791>`__

**Nikola** \| `Github - 2.2K stars <https://github.com/getnikola/nikola>`__

Viable option to host your site with the informative `Nikola Handbook <https://getnikola.com/handbook.html#why-static>`__ walking you through each step. `Plugins <https://plugins.getnikola.com/>`__ for `Jupyter Notebooks <https://plugins.getnikola.com/v7/notebook_shortcode/>`__, `post processing filters <https://getnikola.com/handbook.html#post-processing-filters>`__, a `Wordpress importer <https://getnikola.com/handbook.html#importing-your-wordpress-site-into-nikola>`__ command line tool and about `40 ready to go themes <https://themes.getnikola.com/>`__ to find the perfect style.

**Makesite** \| `Github - 1.6K Stars <https://github.com/sunainapai/makesite>`__

Offers less configuration, using only a single makesite.py file.

**Hyde** \| `Github - 1.6K stars <https://github.com/hyde/hyde>`__

Port from `Jekyll <https://jekyllrb.com/>`__, a `Ruby <https://www.ruby-lang.org/en/>`__ static site generator. It has since formed its own "evil twin" identity.

**Mynt** \| `Github - 400 stars <https://github.com/Anomareh/mynt>`__

"Designed to give you all the features of a CMS with none of the often rigid implementations of those features."

**Staticjinja** \| `Github - 250 Stars <https://github.com/staticjinja/staticjinja>`__

"Minimalist Python library for building static websites with Jinja."

Additional Resources
--------------------

-  `PyLadies.com <http://PyLadies.com>`__, `created with Mynt <https://pyladies.com/>`__
-  FullStackPython.com, `created with Pelican <https://github.com/mattmakai/fullstackpython.com>`__
-  GetLektor.com, `created with Lektor <https://github.com/lektor/lektor-website>`__
-  `Hugo <https://github.com/gohugoio/hugo>`__, a Go static site generator
-  `How to Build a Low-tech Website? <https://solar.lowtechmagazine.com/2018/09/how-to-build-a-lowtech-website.html>`__ (featuring Pelican)
-  One convenient way to serve your static files up on the web is with a `CDN <https://www.cloudflare.com/learning/cdn/what-is-a-cdn/#:~:text=A%20content%20delivery%20network%20(CDN,stylesheets%2C%20images%2C%20and%20videos.>`__ like `Cloudflare Pages <https://developers.cloudflare.com/pages/framework-guides/deploy-anything/>`__.
-  You can research more projects on `Jamstack <https://jamstack.org/generators/>`__, a site I found helpful for finding these libraries.

**Update**! I launched a Pelican blog about investing with Cloudflare pages. It's my first live static blog. Read more about it `here <https://lofipython/launching-a-live-static-blog-via-pelican-github-and-cloudflare-pages/>`__.
