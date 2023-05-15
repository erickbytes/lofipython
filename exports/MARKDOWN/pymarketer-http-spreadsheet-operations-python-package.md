Title: pymarketer: an HTTP + Spreadsheet Wrangling Python package
Date: 2023-01-08 19:52
Author: pythonmarketer
Category: coding, excel, HTTP
Tags: problem solving, programming, python, software
Slug: pymarketer-http-spreadsheet-operations-python-package
Status: published

`<!-- wp:paragraph -->`{=html}

Typically, this blog reviews the other Python libraries in its vast ecosystem. This time, it's my own package I made for fun, pymarketer. This was created in a single day and can be installed from the [Github repo](https://github.com/erickbytes/pymarketer). Have a go at [my most read post](https://pythonmarketer.com/2018/01/20/how-to-python-pip-install-new-libraries/) if you need help with pip.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Install with pip from source [Github repo](https://github.com/erickbytes/pymarketer):**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:code -->`{=html}

``` wp-block-code
python -m pip install git+https://github.com/erickbytes/pymarketer.git
```

`<!-- /wp:code -->`{=html}

`<!-- wp:paragraph -->`{=html}

The pymarketer package helps you do things like:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:list -->`{=html}

-   merging all the tabs of an Excel file into one CSV
-   generate HTTP code
-   make a word cloud image
-   splitting a CSV
-   merging CSVs

`<!-- /wp:list -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Generating a Word Cloud with the pymarketer Package (via [wordcloud](http://amueller.github.io/word_cloud/index.html))**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:syntaxhighlighter/code {"language":"python"} -->`{=html}

``` wp-block-syntaxhighlighter-code
import pandas as pd
import pymarketer as pm

xl = "Chicago Breweries.xlsx"
df = pd.read_excel(xl)
# Make a wordcloud from a pandas dataframe.
wordcloud = pm.word_cloud(df)
wordcloud.to_file("Text Word Cloud Visualization.jpg")
```

`<!-- /wp:syntaxhighlighter/code -->`{=html}

`<!-- wp:image {"id":7362,"width":400,"height":200,"sizeSlug":"large","linkDestination":"none"} -->`{=html}

![](https://pythonmarketer.files.wordpress.com/2023/01/text-word-cloud-visualization.jpg?w=400){.wp-image-7362 width="400" height="200"}

`<!-- /wp:image -->`{=html}

`<!-- wp:paragraph -->`{=html}

This package relied on several Python libraries to complete:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:list -->`{=html}

-   chardet
-   [pandas](https://pandas.pydata.org/)
-   [numpy](https://numpy.org/doc/stable/reference/generated/numpy.array_split.html)
-   wordcloud
-   [ftfy](https://ftfy.readthedocs.io/en/latest/)

`<!-- /wp:list -->`{=html}

`<!-- wp:paragraph -->`{=html}

I'll likely expand on this in the future. Anyone who wrangles data might be able to apply this package to good profit. At minimum, you might find it interesting to take a look at the project's [\_\_init\_\_.py](https://github.com/erickbytes/pymarketer/blob/main/pymarketer/__init__.py) to see how some of the functions are implemented.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Additional Resources**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:list -->`{=html}

-   [How to Make an Internal Python Package](https://changhsinlee.com/python-package/)
-   [pymarketer Github Examples](https://github.com/erickbytes/pymarketer/blob/main/pymarketer_examples.py)

`<!-- /wp:list -->`{=html}
