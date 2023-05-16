Yoast SEO API Python Example With requests + pandas
###################################################
:date: 2021-09-06 14:12
:author: pythonmarketer
:category: APIs, coding, HTTP, programming, python
:tags: Python Wordpress Blog SEO, SEO, Yoast API
:slug: yoast-api-python-example-with-requests-pandas
:status: published

Lately I've been checking out the `Yoast SEO plug-in <https://yoast.com/wordpress/plugins/seo/>`__ and their `REST API <https://developer.yoast.com/customization/apis/rest-api>`__. The API returns all of the SEO metadata, meta tags, schema.org data, etc. for your Wordpress blog posts. Here's a Yoast API Python example script to fetch post metadata via requests and pandas:

.. code-block:: python

   import pandas as pd
   import requests

   def fetch_metadata(post_url):
       """Returns the Yoast API response as pandas dataframe."""
       url = f'https://atomic-temporary-107329037.wpcomstaging.com/wp-json/yoast/v1/get_head?url={post_url}'
       r = requests.get(url)
       print(r.text)
       print(r.status_code)
       response_dict = r.json()
       metadata_df = pd.json_normalize(response_dict['json'])
       return metadata_df

   url = 'https://github.com/erickbytes/Python-Marketer-Reader-Analytics/blob/master/dataset/2020_pythonmarketer.com_post_views.xlsx?raw=true.xlsx'
   posts = pd.read_excel(url)
   # update url domain with pandas .str accessor
   posts.url = posts.url.str.replace(pat='.wordpress', repl='', regex=False)
   posts['metadata'] = posts.url.apply(fetch_metadata)
   metadata_df = pd.concat(list(posts['results']))
   metadata_df.to_csv('Wordpress Blog Post Yoast API Metadata.csv', index=False)

**What this script is doing:**

#. Read a list of my blog posts from Github into a `pandas dataframe <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html>`__.
#. Use `pandas .apply <https://pandas.pydata.org/docs/reference/api/pandas.Series.apply.html>`__ to fetch the metadata for each post url.
#. Deserialize + normalize the JSON response.
#. Convert to a pandas dataframe and store in a pandas Series named 'metadata'.
#. Merge the series and write the metadata to a csv file.

**The Payoff**:

You'll end up with blobs of JSON formatted metadata to sift through or wrangle to your liking! Check out the `Yoast documentation <https://developer.yoast.com/>`__ if you're interested in finding out more about their APIs.

**New to APIs?**

It's ok if so, we all were once. Check out my `guide to making HTTP requests with Python <https://lofipython.com/how-to-make-json-requests-with-python/>`__ if you want to see more API examples.

.. figure:: https://pythonmarketer.files.wordpress.com/2021/10/e5f7c-image.png
   :alt: SEO Overview
   :figclass: wp-image-5922
   :width: 640px
   :height: 451px
