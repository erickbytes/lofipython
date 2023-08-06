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

#. Sign up for a `Twitter Developer account <https://developer.twitter.com/>`__ and create an app. I named mine "tweetcleanr".

#. Find your app under "Projects & Apps". Edit your app's permissions to "**Read + Write + Direct Messages**".

#. After you update your permissions, select the "Keys and tokens" tab. Then regenerate new API keys. Then paste them in the below script.


.. code:: console

   pip install api


.. image:: {static}/blog/images/example.png
  :alt: create value with an API


.. code-block:: python

   from api import stuff

   if __name__ == "__main__":
       value = stuff.apply()
       print(value)



**Challenge Complete**

It's great when stuff just works. And it only cost me about 1 hour to complete. 



**Supplementary Reading**

`Tweepy Documentation Tutorial <http://docs.tweepy.org/en/latest/getting_started.html>`__

`Twitter's API Tutorials <https://developer.twitter.com/en/docs/tutorials>`__

`Twitter Postman Tutorial <https://developer.twitter.com/en/docs/tutorials/postman-getting-started>`__
