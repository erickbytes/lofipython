Post an Unsplash Photo to Facebook Pages with Python
####################################################
:date: 2020-10-04 15:13
:author: pythonmarketer
:category: APIs, coding, programming
:tags: Facebook API, python, social media, Unsplash
:slug: post-a-photo-to-your-facebook-page-with-the-unsplash-facebook-apis
:status: published

My goal was to automate posting positive photos and quotes to my Facebook page, "`Positive Thoughts Daily <https://www.facebook.com/positivedailythought>`__", with the Unsplash and Facebook APIs. Here's how I did it!

This implementation relies on `my own collection of photos on Unsplash <https://unsplash.com/@erickbytes/likes>`__. I will manually select which photos I like to get added to my collection. Then my app will take the new photos and post one a day for me.

   Side note: the free version of the Unsplash API is capped at 50 requests per week, which was enough for me.

Setting Up The Facebook API
~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Sign up for a Facebook `developer account <https://developers.facebook.com/>`__
#. Create a new Facebook app
#. Add "page_manage_posts" and "pages_read_user_content" permissions to your app in the `Graph API Explorer <https://developers.facebook.com/tools/explorer>`__
#. Get a "short lived" user access token from the Graph API explorer (optional: fetch a "long lived" user access token, which lasts up to 60 days)
#. Use your user access token to a fetch your page's access token

**Optional: fetch long lived access token with curl**

.. code:: python

   curl -i -X GET "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token& client_id={app-id}& client_secret={app-secret}& fb_exchange_token={short-lived-user-access-token}"

**Fetch your Facebook page's access token**

.. code:: python

   curl -i -X GET "https://graph.facebook.com/{your-user-id}/accounts?access_token={user-access-token}

Setting up Unsplash
~~~~~~~~~~~~~~~~~~~

#. Sign up for an `Unsplash developer account <https://unsplash.com/documentation>`__
#. Install the python-unsplash library. In the terminal enter:

.. code:: python

   python -m pip install python-unsplash

3. Decide what photo you want to post. This example fetches a random photo from my `Unsplash collection <https://unsplash.com/collections/66610223/positive-thoughts-daily>`__. You can also fetch any photo at random, or pass in a query to get a certain type of photo.

.. code-block:: python

   from unsplash.api import Api
   from unsplash.auth import Auth
   import requests
   """Python-Unsplash library Github: 
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
   # Use image_id to get random photo's download link from a collection.
   url = f"https://api.unsplash.com/photos/{image_id}/download?client_id={client_id}"
   r = requests.get(url)
   print(r.text)
   image = r.json()
   download_link = image['url']

Posting the Unsplash Image to Facebook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   """Use download link and post to page with Facebook API."""
   page_id = "add_page_id_from_about_section"
   url = f"https://graph.facebook.com/{page_id}/photos?access_token={page_access_token}&url={download_link}"
   r = requests.post(url)
   post_ids = r.json()
   print(post_ids)

**Post Project Reflections**

This was my first time working with the Facebook API. Honestly, it's a little crazy trying to balance all the token types in your head. There are about 5 different types of tokens that are used for different things! Ultimately I was able to figure out how to to post a photo. So there is a bit of a learning curve. It's a good challenge to build your API skills. The Unsplash API requires no `Oauth <https://en.wikipedia.org/wiki/OAuth>`__ tokens and is easier to pick up.

My Facebook page posts are now triggered by page loads on this `website <https://positivethoughts.pythonanywhere.com/>`__! I am using a `MySQL database <https://pythonmarketer.wordpress.com/2020/05/25/essential-mysql-terminal-commands-and-connecting-to-mysql-with-flask-pandas-and-pythonanywhere/>`__ to track which images I post to make sure I don't duplicate any posts and to make sure I only post once every 24 hours. Ah, I love the smell of fresh automation in the morning. 😀

**Supplementary Links**

-  `FB API "Getting Started" <https://developers.facebook.com/docs/pages/getting-started>`__
-  `FB API "Explorer" <https://developers.facebook.com/tools/explorer>`__
-  `FB Permissions Reference <https://developers.facebook.com/docs/permissions/reference>`__
-  `Debugging Tokens <https://developers.facebook.com/docs/facebook-login/access-tokens/debugging-and-error-handling/>`__
-  `FB API Publishing <https://developers.facebook.com/docs/pages/publishing/>`__
-  `A Guide to Tackling APIs <https://pythonmarketer.wordpress.com/2020/05/18/how-to-make-json-requests-with-python/>`__, written by me!
