Delete All Your Tweets with Tweepy and the Twitter API
######################################################
:date: 2020-09-13 21:07
:author: pythonmarketer
:category: coding, programming, python
:tags: api, tweepy, tweets, twitter
:slug: delete-all-your-tweets-with-tweepy-and-the-twitter-api
:status: published

You may want to `download an archive <https://help.twitter.com/en/managing-your-account/how-to-download-your-twitter-archive>`__ of your tweets before deleting them. I did this and it took about a day to get my archive download.

**How To Purge Your Tweet History with Python**

#. Per the `Tweepy library documentation <http://docs.tweepy.org/en/latest/install.html>`__, install tweepy with `pip <https://pythonmarketer.wordpress.com/2018/01/20/how-to-python-pip-install-new-libraries/>`__. It worked fine in my python 3.8 `virtual environment <https://docs.python.org/3/library/venv.html>`__.

.. code:: wp-block-code

   pip install tweepy

2. Sign up for a `Twitter Developer account <https://developer.twitter.com/>`__ and create an app. I named mine "tweetcleanr".

3. Find your app under "Projects & Apps". Edit your app's permissions to "**Read + Write + Direct Messages**".

4. After you update your permissions, select the "Keys and tokens" tab. Then regenerate new API keys. Then paste them in the below script.

.. figure:: https://pythonmarketer.files.wordpress.com/2020/09/twitter-dev.png?w=1024
   :alt: 
   :figclass: wp-image-4350

5. Save the below script as a python file. In command prompt or terminal, run python **delete_tweets.py** or whatever you want to name it!

6. You'll be asked to go to a link and enter an authorization code. Then you'll see your tweets being deleted like pictured below.

**delete_tweets.py**

I found this `Github Gist <https://gist.github.com/davej/113241>`__ via Google and updated the print and input statements to Python 3. I also added the `traceback module <https://docs.python.org/3/library/traceback.html>`__ in case you need to debug it. Initially, I received an error telling me to complete step 3 above. I didn't see the error message at first, until adding ``traceback.print_exc()`` like you see below.

.. code:: wp-block-syntaxhighlighter-code

   import tweepy
   import traceback

   """
   Delete All Your Tweets - Github Gist by davej
   Credit: https://gist.github.com/davej/113241
   Ported to Python 3 by Python Marketer: pythonmarketer.com/2020/09/13/delete-all-your-tweets-with-tweepy-and-the-twitter-api/
   """
   CONSUMER_KEY = "get_from_dev_portal"
   CONSUMER_SECRET = "get_from_dev_portal"


   def oauth_login(consumer_key, consumer_secret):
       """Authenticate with twitter using OAuth"""

       auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
       auth_url = auth.get_authorization_url()

       verify_code = input(
           "Authenticate at %s and then enter you verification code here > " % auth_url
       )
       auth.get_access_token(verify_code)

       return tweepy.API(auth)


   def batch_delete(api):
       print(
           "You are about to delete all tweets from the account @%s."
           % api.verify_credentials().screen_name
       )
       print("Does this sound ok? There is no undo! Type yes to carry out this action.")
       do_delete = input("> ")
       if do_delete.lower() == "yes":
           for status in tweepy.Cursor(api.user_timeline).items():
               try:
                   api.destroy_status(status.id)
                   print("Deleted:", status.id)
               except Exception:
                   traceback.print_exc()
                   print("Failed to delete:", status.id)


   if __name__ == "__main__":
       api = oauth_login(CONSUMER_KEY, CONSUMER_SECRET)
       print("Authenticated as: %s" % api.me().screen_name)

       batch_delete(api)

.. figure:: https://pythonmarketer.files.wordpress.com/2020/09/terminaltweepy.png?w=755
   :alt: 
   :figclass: wp-image-4325

**✅** **Twitter Cleanse Complete**

Twitter has a really slick developer dashboard. Its API combined with the tweepy library got the job done for me. It's great when stuff just works. And it only cost me about 1 hour to complete. Time to start a clean slate. Here's to looking forward.

**Supplementary Reading**

`Tweepy Documentation Tutorial <http://docs.tweepy.org/en/latest/getting_started.html>`__

`Twitter's API Tutorials <https://developer.twitter.com/en/docs/tutorials>`__

`Twitter Postman Tutorial <https://developer.twitter.com/en/docs/tutorials/postman-getting-started>`__
