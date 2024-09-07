Should You Block LLMs and Bots From Your Blog?
##############################################
:date: 2024-09-07 14:42
:author: lofipython
:category: bots, blogging, internet
:tags: robots.txt policy, LLMs, internet ethics
:slug: should-you-block-llms-and-bots-from-your-blog
:status: published

**Bots and robots.txt**

Bots are crawling the internet. They make up a large chunk of all web traffic.
On my blogs, I've always used the robots.txt to say to bots, "scrape away!" like this:

::

   User-agent: *
   Disallow:

Some websites use a robots.txt to say, "don't scrape our content". 
We can ask crawlers to restrict from crawling, but this more less is an honor system.
For this blog, I always welcomed all real traffic, but had activated "Bot Fight Mode" to 
to protect against some of the bots.

**Cloudflare Rolls Out New AI Blocker Configuration**

I noticed in my Cloudflare Pages dashboard that a new setting has become available to me on the free plan.

.. image:: {static}/images/cloudflare-LLM-blocker.png
  :alt: toggle cloudflare AI bot blocker

.. raw:: html

    <center><em>Block AI Bots Configuration on Cloudflare Pages</em></center>

I now have another level of security available if I want to use it. I'd already enabled "Bot Fight Mode" on my Cloudflare Pages blogs.
For now, I'm choosing to keep my blogs open to all traffic, including AIs while excluding some bots. Anyone who publishes
to the open internet will have to assess their willingness to open up their site and trust that it will come back to them 
in some way.

   You can block artificial intelligence (AI) bots, crawlers, and scrapers from scraping 
   your website content and training large language models (LLM) to recreate it without 
   your permission. When you enable this feature via a pre-configured managed rule, 
   Cloudflare can detect and block AI bots from your website.

   /- `AI Bots <https://developers.cloudflare.com/bots/concepts/bot/#ai-bots>`__

In 2024, I am re-thinking if allowing Google, Bing and Twitter to crawl my stuff is still the best position. 
In order for this system to work, there needs to be proof of references to my original writing.

.. image:: {static}/images/top-blog-crawlers.png
  :alt: most frequently crawling search engines
  :width: 500px

.. raw:: html

    <center><em>Crawler Traffic on lofipython.com, Oct. - Sept. 2024</em></center>

If an LLM is just a remix of all the data it consumes, how do we trace the origin of its results?
And how does that get attributed back? It seemed more easy to tell with Google's link based search results.
But even then, there was a lack of transparency. It's still that way today. I appreciate Cloudflare is putting 
this choice to block or not block AIs in the hands of website makers.

The point of this post was not to answer the question, but instead reflect on the nuances of web creators 
and their relationship with big tech. Everyone will have to decide for themselves if they think it's worth it.
In this case, we're likely "paid in exposure". Big tech will distill the value of what we write to inquiring 
humans, but will website creators lose out on this exchange? Are we cutting off a channel of distribution if we 
push back against LLMs scooping up our data? Right now there seems to be more questions than answers. We'll see. 