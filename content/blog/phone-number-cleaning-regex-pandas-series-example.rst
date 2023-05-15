Phone Number Cleaning Regex + pandas Series Example
###################################################
:date: 2021-12-31 14:19
:author: pythonmarketer
:category: coding, pandas, programming, python
:tags: data cleaning, regex
:slug: phone-number-cleaning-regex-pandas-series-example
:status: published

This is a solution I worked out recently to strip phone numbers into a uniform format. To install `pandas with pip <https://pandas.pydata.org/docs/getting_started/install.html>`__, enter in command prompt:

.. code:: wp-block-preformatted

   python -m pip install pandas 

The pandas library has regex built in and it's pretty neat! Behold the power of pandas and a `regular expression <https://en.wikipedia.org/wiki/Regular_expression>`__ to do trivial telephone tidying:

.. figure:: https://pythonmarketer.files.wordpress.com/2021/12/pandas-example-7-3.41.12-pm.png?w=561
   :alt: 
   :figclass: wp-image-6382
   :width: 767px
   :height: 150px

.. code:: wp-block-preformatted

   import pandas as pd
   s = pd.Series(data=["(010) 001-1010"], name="Phone", dtype="str")
   # remove parentheses, hyphens and spaces with pandas + regex
   s = s.str.replace(pat="\(|\)|-| ", repl="", regex=True)
   print(s)
   # resulting number: "0100011010"

**Regex is cool.**

Grasping the intricacies of what this code is doing feels elegant when you connect the dots.. or pipes. The replace is done via a pandas `str accessor <https://pandas.pydata.org/pandas-docs/stable/reference/series.html#api-series-str>`__. In the pat string, the parentheses are escaped with slashes and separated by pipes "|". They act as an `or operator <https://realpython.com/python-or-operator/>`__, succinctly chaining multiple characters together for matching and in this case replacing them with nothing. Pretty nifty. If you read the `pandas docs <https://pandas.pydata.org/docs/>`__, you'll find regex is accessible in different parts of the API. Dive in, it's some of my favorite documentation to snoop. There is so much you can do with pandas. This example demonstrates how its flexible functions get the job done efficiently.

**Further Reading:**

`pandas.Series documentation <https://pandas.pydata.org/docs/reference/api/pandas.Series.html>`__

`pandas str.replace documentation <https://pandas.pydata.org/docs/reference/api/pandas.Series.str.replace.html>`__

`Source of the famous “Now you have two problems” quote <http://regex.info/blog/2006-09-15/247>`__
