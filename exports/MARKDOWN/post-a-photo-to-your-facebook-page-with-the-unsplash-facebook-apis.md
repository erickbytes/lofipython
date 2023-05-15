Title: Post an Unsplash Photo to Facebook Pages with Python
Date: 2020-10-04 15:13
Author: pythonmarketer
Category: APIs, coding, programming
Tags: Facebook API, python, social media, Unsplash
Slug: post-a-photo-to-your-facebook-page-with-the-unsplash-facebook-apis
Status: published

`<!-- wp:paragraph -->`{=html}

My goal was to automate posting positive photos and quotes to my Facebook page, "[Positive Thoughts Daily](https://www.facebook.com/positivedailythought)", with the Unsplash and Facebook APIs. Here's how I did it!

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

This implementation relies on [my own collection of photos on Unsplash](https://unsplash.com/@erickbytes/likes). I will manually select which photos I like to get added to my collection. Then my app will take the new photos and post one a day for me.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:quote -->`{=html}

> Side note: the free version of the Unsplash API is capped at 50 requests per week, which was enough for me.

`<!-- /wp:quote -->`{=html}

`<!-- wp:heading {"level":3} -->`{=html}

### Setting Up The Facebook API

`<!-- /wp:heading -->`{=html}

`<!-- wp:list {"ordered":true} -->`{=html}

1.  Sign up for a Facebook [developer account](https://developers.facebook.com/)
2.  Create a new Facebook app
3.  Add "page_manage_posts" and "pages_read_user_content" permissions to your app in the [Graph API Explorer](https://developers.facebook.com/tools/explorer)
4.  Get a "short lived" user access token from the Graph API explorer (optional: fetch a "long lived" user access token, which lasts up to 60 days)
5.  Use your user access token to a fetch your page's access token

`<!-- /wp:list -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Optional: fetch long lived access token with curl**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
curl -i -X GET "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token& client_id={app-id}& client_secret={app-secret}& fb_exchange_token={short-lived-user-access-token}"
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Fetch your Facebook page's access token**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
curl -i -X GET "https://graph.facebook.com/{your-user-id}/accounts?access_token={user-access-token}
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:heading {"level":3} -->`{=html}

### Setting up Unsplash

`<!-- /wp:heading -->`{=html}

`<!-- wp:list {"ordered":true} -->`{=html}

1.  Sign up for an [Unsplash developer account](https://unsplash.com/documentation)
2.  Install the python-unsplash library. In the terminal enter:

`<!-- /wp:list -->`{=html}

`<!-- wp:code -->`{=html}

``` wp-block-code
python -m pip install python-unsplash
```

`<!-- /wp:code -->`{=html}

`<!-- wp:paragraph -->`{=html}

3\. Decide what photo you want to post. This example fetches a random photo from my [Unsplash collection](https://unsplash.com/collections/66610223/positive-thoughts-daily). You can also fetch any photo at random, or pass in a query to get a certain type of photo.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:syntaxhighlighter/code -->`{=html}

``` wp-block-syntaxhighlighter-code
from unsplash.api import Api
from unsplash.auth import Auth
import requests
"""
Python-Unsplash library Github: 
https://github.com/yakupadakli/python-unsplash
"""
client_id = "add_your_client_id"
client_secret = "add_your_client_secret"
redirect_uri = "add_your_redirect_uri"
code = ""
auth = Auth(client_id, client_secret, redirect_uri, code=code)
api = Api(auth)
# returns a python list containing a class
image = api.photo.random(collections=66610223) # my collection id
image_id = image[0].id
"""
Use image_id to get random photo's 
download link from a collection.
"""
url = f"https://api.unsplash.com/photos/{image_id}/download?client_id={client_id}"
r = requests.get(url)
print(r.text)
image = r.json()
download_link = image['url']
```

`<!-- /wp:syntaxhighlighter/code -->`{=html}

`<!-- wp:heading {"level":3} -->`{=html}

### Posting the Unsplash Image to Facebook

`<!-- /wp:heading -->`{=html}

`<!-- wp:syntaxhighlighter/code -->`{=html}

``` wp-block-syntaxhighlighter-code
"""Use download link and post to page with Facebook API."""
page_id = "add_page_id_from_about_section"
url = f"https://graph.facebook.com/{page_id}/photos?access_token={page_access_token}&url={download_link}"
r = requests.post(url)
post_ids = r.json()
print(post_ids)
```

`<!-- /wp:syntaxhighlighter/code -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Post Project Reflections**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

This was my first time working with the Facebook API. Honestly, it's a little crazy trying to balance all the token types in your head. There are about 5 different types of tokens that are used for different things! Ultimately I was able to figure out how to to post a photo. So there is a bit of a learning curve. It's a good challenge to build your API skills. The Unsplash API requires no [Oauth](https://en.wikipedia.org/wiki/OAuth) tokens and is easier to pick up.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

My Facebook page posts are now triggered by page loads on this [website](https://positivethoughts.pythonanywhere.com/)! I am using a [MySQL database](https://pythonmarketer.wordpress.com/2020/05/25/essential-mysql-terminal-commands-and-connecting-to-mysql-with-flask-pandas-and-pythonanywhere/) to track which images I post to make sure I don't duplicate any posts and to make sure I only post once every 24 hours. Ah, I love the smell of fresh automation in the morning. 😀

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Supplementary Links**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:list -->`{=html}

-   [FB API "Getting Started"](https://developers.facebook.com/docs/pages/getting-started)
-   [FB API "Explorer"](https://developers.facebook.com/tools/explorer)
-   [FB Permissions Reference](https://developers.facebook.com/docs/permissions/reference)
-   [Debugging Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/debugging-and-error-handling/)
-   [FB API Publishing](https://developers.facebook.com/docs/pages/publishing/)
-   [A Guide to Tackling APIs](https://pythonmarketer.wordpress.com/2020/05/18/how-to-make-json-requests-with-python/), written by me!

`<!-- /wp:list -->`{=html}
