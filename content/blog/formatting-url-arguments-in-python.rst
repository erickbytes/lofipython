Formatting URL Arguments in Python
##################################
:date: 2023-10-25 15:42
:author: lofipython
:category: http, urls, python, requests
:tags: url formatting, working with urls in APIs, python http url formatting, python url parameters, format python url arguments
:slug: formatting-url-arguments-in-python
:status: published

When I first started working with APIs, I had a bad habit of passing URL arguments
as one long ugly string. Anything longer than 79 characters violates PEP-8.
It's also hard to read and can be difficult to edit the code in your text editor if the URL is trailing off the screen.
In this post, you'll find some alternatives to the primitive "long ugly string" approach.

  **Did you know?** URL stands for "uniform resource locator".

Below are two ways to neatly format your URLs so that they have parameters.
Both involve using a Python dictionary. The requests API allows you to pass
a dictionary or list of tuples to its params argument. Alternatively, if you want
to see the full URL as a string, there's a sleek way to format URL arguments
with urllib's `urlencode function <https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlencode>`__.

.. image:: {static}/images/url-structure.png
  :alt: a visual breakdown of a url with parameters

source: `Geeks for Geeks <https://www.geeksforgeeks.org/how-to-handle-missing-parameters-in-url-with-flask/>`__

**Pass a dictionary to the requests params argument to include URL arguments.**

  You often want to send some sort of data in the URL’s query string.
  If you were constructing the URL by hand, this data would be given as key/value pairs
  in the URL after a question mark, e.g. httpbin.org/get?key=val.
  Requests allows you to provide these arguments as a dictionary of strings, using the params keyword argument.
  \- requests documentation, `Passing Parameters in URLs <https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls>`__


.. code-block:: python

  import requests

  payload = {
      "email": "example@example.com",
      "message": "This email is not real.",
      "status": "inactive"
  }
  r = requests.get("https://httpbin.org/get", params=payload)
  print(r.text)



**Use urllib's urlencode function to dynamically construct URL from a dictionary.**

.. code-block:: python

  import requests
  from urllib.parse import urlencode

  payload = {
      "email": "example@example.com",
      "message": "This email is not real.",
      "status": "inactive"
  }
  # Returns str of URL encoded parameters.
  url_parameters = urlencode(payload)
  # >>> url_parameters
  # "email=example%40example.com&message=This+email+is+not+real.&status=inactive"
  url = f"https://httpbin.org/get?{url_parameters}"
  r = requests.get(url)
  print(r.text)


**Arguments can be a good thing.**

This seemingly basic HTTP formatting was something that took me too long to realize.
I hope it helps you keep your URLs tidy and your HTTP requests more readable.

**Read More About URL Parameters**

`Passing Parameters in URLS, requests Documentation <https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls>`__

`urllib Examples, Python Documentation <https://docs.python.org/3/library/urllib.request.html#urllib-examples>`__

`requests API Documentation Reference <https://requests.readthedocs.io/en/latest/api/#requests.request>`__

`Stack Overflow, Python Dictionary to URL Parameters <https://stackoverflow.com/questions/1233539/python-dictionary-to-url-parameters>`__
