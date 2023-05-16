pymarketer: an HTTP + Spreadsheet Wrangling Python package
##########################################################
:date: 2023-01-08 19:52
:author: pythonmarketer
:category: coding, excel, HTTP
:tags: problem solving, programming, python, software
:slug: pymarketer-http-spreadsheet-operations-python-package
:status: published

Typically, this blog reviews the other Python libraries in its vast ecosystem. This time, it's my own package I made for fun, pymarketer. This was created in a single day and can be installed from the `Github repo <https://github.com/erickbytes/pymarketer>`__. Have a go at `my most read post <https://pythonmarketer.com/2018/01/20/how-to-python-pip-install-new-libraries/>`__ if you need help with pip.

**Install with pip from source**\ `Github repo <https://github.com/erickbytes/pymarketer>`__\ **:**

.. code:: python

   python -m pip install git+https://github.com/erickbytes/pymarketer.git

The pymarketer package helps you do things like:

-  merging all the tabs of an Excel file into one CSV
-  generate HTTP code
-  make a word cloud image
-  splitting a CSV
-  merging CSVs

**Generating a Word Cloud with the pymarketer Package (via**\ `wordcloud <http://amueller.github.io/word_cloud/index.html>`__\ **)**

.. code-block:: python

   import pandas as pd
   import pymarketer as pm

   xl = "Chicago Breweries.xlsx"
   df = pd.read_excel(xl)
   # Make a wordcloud from a pandas dataframe.
   wordcloud = pm.word_cloud(df)
   wordcloud.to_file("Text Word Cloud Visualization.jpg")

.. figure:: https://pythonmarketer.files.wordpress.com/2023/01/text-word-cloud-visualization.jpg?w=400
   :alt: 
   :figclass: wp-image-7362
   :width: 400px
   :height: 200px

This package relied on several Python libraries to complete:

-  chardet
-  `pandas <https://pandas.pydata.org/>`__
-  `numpy <https://numpy.org/doc/stable/reference/generated/numpy.array_split.html>`__
-  wordcloud
-  `ftfy <https://ftfy.readthedocs.io/en/latest/>`__

I'll likely expand on this in the future. Anyone who wrangles data might be able to apply this package to good profit. At minimum, you might find it interesting to take a look at the project's `\__init__.py <https://github.com/erickbytes/pymarketer/blob/main/pymarketer/__init__.py>`__ to see how some of the functions are implemented.

**Additional Resources**

-  `How to Make an Internal Python Package <https://changhsinlee.com/python-package/>`__
-  `pymarketer Github Examples <https://github.com/erickbytes/pymarketer/blob/main/pymarketer_examples.py>`__
