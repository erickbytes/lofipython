Title: Phone Number Cleaning Regex + pandas Series Example
Date: 2021-12-31 14:19
Author: pythonmarketer
Category: coding, pandas, programming, python
Tags: data cleaning, regex
Slug: phone-number-cleaning-regex-pandas-series-example
Status: published

`<!-- wp:paragraph -->`{=html}

This is a solution I worked out recently to strip phone numbers into a uniform format. To install [pandas with pip](https://pandas.pydata.org/docs/getting_started/install.html), enter in command prompt:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
python -m pip install pandas 
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:paragraph -->`{=html}

The pandas library has regex built in and it's pretty neat! Behold the power of pandas and a [regular expression](https://en.wikipedia.org/wiki/Regular_expression) to do trivial telephone tidying:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:image {"id":6382,"width":767,"height":150,"sizeSlug":"large","linkDestination":"none"} -->`{=html}

![](https://pythonmarketer.files.wordpress.com/2021/12/pandas-example-7-3.41.12-pm.png?w=561){.wp-image-6382 width="767" height="150"}

`<!-- /wp:image -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
import pandas as pd
s = pd.Series(data=["(010) 001-1010"], name="Phone", dtype="str")
# remove parentheses, hyphens and spaces with pandas + regex
s = s.str.replace(pat="\(|\)|-| ", repl="", regex=True)
print(s)
# resulting number: "0100011010"
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Regex is cool.**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

Grasping the intricacies of what this code is doing feels elegant when you connect the dots.. or pipes. The replace is done via a pandas [str accessor](https://pandas.pydata.org/pandas-docs/stable/reference/series.html#api-series-str). In the pat string, the parentheses are escaped with slashes and separated by pipes "\|". They act as an [or operator](https://realpython.com/python-or-operator/), succinctly chaining multiple characters together for matching and in this case replacing them with nothing. Pretty nifty. If you read the [pandas docs](https://pandas.pydata.org/docs/), you'll find regex is accessible in different parts of the API. Dive in, it's some of my favorite documentation to snoop. There is so much you can do with pandas. This example demonstrates how its flexible functions get the job done efficiently.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Further Reading:**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[pandas.Series documentation](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[pandas str.replace documentation](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.replace.html)

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[Source of the famous “Now you have two problems” quote](http://regex.info/blog/2006-09-15/247)

`<!-- /wp:paragraph -->`{=html}
