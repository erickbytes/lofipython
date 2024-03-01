Find Broken Links in Your .rst Documents With rst-url-validator
###############################################################
:date: 2024-03-01 12:56
:author: lofipython
:category: coding, programming, python, writing
:tags: reStructuredtext Format, python rst url validation, how to validate .rst links
:slug: validating-rst-links-with-rst-url-validator
:status: published

The posts on this blog are written in `reStructuredtext <https://www.writethedocs.org/guide/writing/reStructuredText/>`__. 
I recently had an idea to write a Python script to check my broken urls for broken tags or urls that are no valid. 
So I did what any other programmer does in 2024 and opened up an AI assistant. Bing quickly generated the structure 
of the Python script from my prompt, but like usual it required some tinkering and refinement to make it work.

Bing was also valuable for helping me write regex code for rst-url-validator. It is typically very confusing to reason about regex, 
but with AI assistance I can just ask for regex that does something and the AI can generate it. Coding is getting way easier than 
it used to be thanks to these new advances in Large Language Models. You can find the complete Python script in the `rst-url-validator Github repo <https://github.com/erickbytes/rst-url-validator>`__.


**Install Python Library Dependencies**

The script uses requests to validate the link and rich to print color-coded output to the terminal screen. 

.. code:: console

   pip install requests
   pip install rich


**Clone The Github Repo**

.. code:: console

   git clone git@github.com:erickbytes/rst-url-validator.git


**Install Python Library Dependencies**

.. code:: console

   python3.12 rst-url-validator.py your_file.rst


.. image:: {static}/images/rst-report.png
  :alt: validate .rst document urls with python


It parses each url tag, checks for required characters and sends a HEAD request to the url to check if it still loads successfully. 
Some websites return status codes like 403 (permission denied), 301 (redirect), or 404 (page not found). If the status code returned is 200,
it's safe to say the page loaded.

This script helped me find a bunch of broken links on my older post. I used this script to refresh or clean up tons on this blog. 
If you're working with .rst documents, give it a try!