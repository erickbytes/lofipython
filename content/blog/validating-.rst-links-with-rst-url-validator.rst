Find Broken Links in Your .rst Documents With rst-url-validator
###############################################################
:date: 2024-03-01 12:56
:author: lofipython
:category: coding, programming, python, writing, .rst, reStructuredtext
:tags: reStructuredtext Format, python rst url validation, how to validate .rst links
:slug: validating-rst-links-with-rst-url-validator
:status: published

The posts on this blog are written in `reStructuredText <https://www.writethedocs.org/guide/writing/reStructuredText/>`__. 
I recently had an idea to write a Python script to check my .rst document url links for broken tags or urls that are not valid. 
When I'm using `Pelican <https://pypi.org/project/pelican/>`__, it hints when a url tag is malformed and gives a line number.
However, it can still be difficult to track down a problematic link when there's an issue in your document.

So I did what any other programmer probably does in 2024, opened up an AI assistant. Bing quickly generated the structure 
of the Python script from my prompt, but like usual it required some tinkering and refinement to make it work.
You can find the complete Python script in the `rst-url-validator Github repo <https://github.com/erickbytes/rst-url-validator>`__.

Bing was also valuable for helping me modify the `regex module <https://docs.python.org/3/howto/regex.html>`__ code 
for rst-url-validator. It is typically very confusing to reason about regex, 
but with AI assistance I can just ask it for regex that does something and 
the AI can generate the code. Coding is getting way easier than it used to be thanks 
to these new advances in large language models.


**Install Python Library Dependencies**

The script uses `requests <https://pypi.org/project/requests/>`__ to send an HTTP request to the url 
and `rich <https://pypi.org/project/rich/>`__ to print color-coded output to the terminal screen. 

.. code:: console

   pip install requests
   pip install rich


**Clone The Github Repo**

.. code:: console

   git clone git@github.com:erickbytes/rst-url-validator.git
   cd rst-url-validator


**Run The CLI Command**

.. code:: console

   python rst-url-validator.py your_file.rst


.. image:: {static}/images/rst-report.png
  :alt: validate .rst document urls with python


It parses each url tag, checks for required characters and sends a `HEAD <https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD>`__ request 
to the url to check if it loads successfully. Some websites return status codes like 403 (permission denied), 301 (redirect), or 404 (page not found). 
If the status code returned is 200, it's safe to say the page loaded. Be aware that some sites like Cloudflare (returns 403) and Amazon (returns 503) do not serve 
any requests and just return an error. In cases like these, you'll need to check pages like this manually in a browser to see if the page loads.

This script helped me find and fix or remove a bunch of broken links on the older posts on this blog. If you're working with .rst documents, give it a try!