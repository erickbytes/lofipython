Title: Yoast SEO API Python Example With requests + pandas
Date: 2021-09-06 14:12
Author: pythonmarketer
Category: APIs, coding, HTTP, programming, python
Tags: Python Wordpress Blog SEO, SEO, Yoast API
Slug: yoast-api-python-example-with-requests-pandas
Status: published

`<!-- wp:paragraph -->`{=html}

Lately I've been checking out the [Yoast SEO plug-in](https://yoast.com/wordpress/plugins/seo/) and their [REST API](https://developer.yoast.com/customization/apis/rest-api). The API returns all of the SEO metadata, meta tags, schema.org data, etc. for your Wordpress blog posts. Here's a Yoast API Python example script to fetch post metadata via requests and pandas:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:syntaxhighlighter/code -->`{=html}

``` wp-block-syntaxhighlighter-code
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
```

`<!-- /wp:syntaxhighlighter/code -->`{=html}

`<!-- wp:paragraph -->`{=html}

**What this script is doing:**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:list {"ordered":true} -->`{=html}

1.  Read a list of my blog posts from Github into a [pandas dataframe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html).
2.  Use [pandas .apply](https://pandas.pydata.org/docs/reference/api/pandas.Series.apply.html) to fetch the metadata for each post url.
3.  Deserialize + normalize the JSON response.
4.  Convert to a pandas dataframe and store in a pandas Series named 'metadata'.
5.  Merge the series and write the metadata to a csv file.

`<!-- /wp:list -->`{=html}

`<!-- wp:paragraph -->`{=html}

**The Payoff**:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

You'll end up with blobs of JSON formatted metadata to sift through or wrangle to your liking! Check out the [Yoast documentation](https://developer.yoast.com/) if you're interested in finding out more about their APIs.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**New to APIs?**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

It's ok if so, we all were once. Check out my [guide to making HTTP requests with Python](https://pythonmarketer.wordpress.com/2020/05/18/how-to-make-json-requests-with-python/) if you want to see more API examples.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:image {"id":5922,"width":640,"height":451,"sizeSlug":"full","linkDestination":"none","className":"is-style-rounded","noBottomMargin":true,"noTopMargin":true} -->`{=html}

![](https://pythonmarketer.files.wordpress.com/2021/10/e5f7c-image.png "SEO Overview"){.wp-image-5922 width="640" height="451"}

`<!-- /wp:image -->`{=html}
