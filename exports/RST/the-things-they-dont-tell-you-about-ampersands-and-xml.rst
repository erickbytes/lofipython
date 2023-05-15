The Things They Don't Tell You About Ampersands and XML
#######################################################
:date: 2022-07-06 12:49
:author: pythonmarketer
:category: APIs, coding, Google, programming
:tags: data, learning, problem solving, XML
:slug: the-things-they-dont-tell-you-about-ampersands-and-xml
:status: published

**In an XML document, you need to escape any ampersands in your text as** ``&amp;``

I began a new coding project. Sure, there's documentation for the API that solves my problem. I find out it uses XML. `Extensible Markup Language <https://en.wikipedia.org/wiki/XML>`__, a classic API format. Cool. I craft a beautiful script that works at first. Hallelujah!

Later on, I realize it doesn't work as well as I believed. It turns out, if I want a server to accept my XML document, `escaping certain characters <https://www.ibm.com/docs/en/was-liberty/base?topic=manually-xml-escape-characters>`__ might be required. The documentation didn't mention this. It was my first time using XML, how would I know?

I noticed a script only worked for a handful of requests. It failed for most, returning a `400 status code <https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400>`__. Suspecting the issue was likely in my payload, I studied the data of the request bodies that failed compared to the others that succeeded. All of the payload bodies that failed contained text with an ampersand.

Suspecting it might be an XML + ampersand related issue, I google `this Stack Overflow post <https://stackoverflow.com/questions/1328538/how-do-i-escape-ampersands-in-xml-so-they-are-rendered-as-entities-in-html>`__ which explains the ampersand escaping situation. There are a handful of characters that must be escaped. Otherwise, you might not be able to connect to the server.

These are the things they often don't tell you. Those little details you must sometimes realize for yourself, unless someone bothers to mention it or write it down. Now you know something that cost me an hour or two of tinkering to realize!

.. figure:: https://pythonmarketer.files.wordpress.com/2022/07/xml-example-2.png?w=453
   :alt: `Image Source <https://github.com/sichkar-valentyn/XML_files_in_Python/blob/master/example.xml>`__
   :figclass: wp-image-7060
   :width: 453px
   :height: 521px

   `Image Source <https://github.com/sichkar-valentyn/XML_files_in_Python/blob/master/example.xml>`__

Wanna read more on HTTP? Check out my guide on `making HTTP requests with Python <https://pythonmarketer.com/2020/05/18/how-to-make-json-requests-with-python/>`__ to read more about HTTP requests.
