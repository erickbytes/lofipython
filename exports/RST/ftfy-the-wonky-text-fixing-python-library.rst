ftfy, The Wonky Text Fixing Python Library
##########################################
:date: 2022-01-06 11:44
:author: pythonmarketer
:category: coding, programming
:tags: ftfy, python, text cleaning
:slug: ftfy-the-wonky-text-fixing-python-library
:status: published

Every Python programmer has undoubtedly come across some crazy characters. The `ftfy library "Fixes Text For You" <https://ftfy.readthedocs.io/en/latest/>`__ and acts like a swiss army knife when you've got questionable characters breaking your script. In my case, an HTTP request was failing because of weird cryptic letters hiding in the data when it was only supposed to be an apostrophe. This library fixed my text and made it appear flawless. I really like ftfy because it solves a common problem, fixing "`mojibake <https://en.wikipedia.org/wiki/Mojibake#:~:text=Mojibake%20(%E6%96%87%E5%AD%97%E5%8C%96%E3%81%91%3B%20IPA%3A,from%20a%20different%20writing%20system.>`__" or mangled characters. It's a good tool to have when you see these types of issues!

`Install with pip <https://pypi.org/project/ftfy/>`__:

.. code:: wp-block-preformatted

   pip install ftfy

.. figure:: https://pythonmarketer.files.wordpress.com/2022/01/ftfy-example-1.png?w=819
   :alt: source: `ftfy documentation <https://ftfy.readthedocs.io/en/latest/avoid.html>`__
   :figclass: wp-image-6448

   source: `ftfy documentation <https://ftfy.readthedocs.io/en/latest/avoid.html>`__

See also: `Python Unicode How To <https://docs.python.org/3/howto/unicode.html>`__
