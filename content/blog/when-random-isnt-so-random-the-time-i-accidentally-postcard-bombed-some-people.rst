Assessing The Marketing Effects of Randomization Failure
########################################################
:date: 2020-05-09 04:06
:author: pythonmarketer
:category: coding, Marketing, pandas, programming, python, work
:tags: business, mistakes, random
:slug: when-random-isnt-so-random-the-time-i-accidentally-postcard-bombed-some-people
:status: published

**Preface**

I always enjoy reading when technical people share their stories of the times things went a little haywire. Times when, despite their best intentions, a solution didn't work as planned and it ends in unpleasant or catastrophic failure. I had an experience like this recently, so here's my "oops" story. Fortunately, I think this falls closer to the unpleasant end of the spectrum.

**Finding A Solution**

My employer needed a way to create postcard contact lists to mail 500,000 people each month. About 2 years in with the company, the old postcard system was breaking down and no one knew how to fix it. The guy who built it left the company. I never knew him and he didn't leave behind much help for anyone to fix his creation.

For my team, it was easier to create the contacts lists by drawing contact data out of our CRM with `requests <https://requests.readthedocs.io/en/master/>`__ and formatting the data with `pandas <https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html>`__. So that's what I did to help us deliver the postcards. (Let's set aside the debate on the strategic value of postcards.)

Things were going smooth for a few months. The new system was creating the lists and nothing appeared to change. The system is still in use today we are more reliable than the old system in its partially degraded state. But there were some growing pains.

**The Moment of** `Ely <https://twitter.com/jamesorharry/status/1100717726547562503>`__

   ELY (n.) The first, tiniest inkling you get that something, somewhere, has gone terribly wrong. [Douglas Adams, The Meaning of Liff]

We began to hear murmurs of the same contacts getting mailed each month from our senders. The script was supposed to draw a certain allocation of contacts at random for each sender. I knew I used ```df.sample(n=1)`` <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html>`__ from pandas to randomize the contact pool. The contacts were definitely getting randomized.

Then one day while making a change requested by our stakeholders, I noticed some code I had written that looked sort of like this:

.. code:: python

   def remove_duplicates(df):
       """Remove duplicates and randomize the order of the rows."""
       original = df.copy(deep=True)
       df = format_for_duplicate_removal(df)
       df = df.drop_duplicates().sample(n=1)
       deduped_contacts = original[original.index.isin(df.index)]
       return deduped_contacts

**The idea of this function was to:**

-  create a throwaway copy of the original dataframe with ``df.copy()``
-  format the throwaway for better duplicate removal
-  ``drop_duplicates()`` and randomize the dataframe's order of the rows with ``df.sample(n=1)``
-  return those rows from the original dataframe, preserving original data but in randomized order

**Discovering The Error**

Looks great, right? Can you spot my error? Here's where I went wrong: I needed to randomize the data that gets returned. But instead, I randomized the throwaway dataframe. I never once altered the order of the original table. I did remove the duplicates, but the row order of the original dataframe never changed.

**Assessing the Damage**

It took me a few months after I wrote the code to realize. That was enough time for a small fraction of our customers to get postcard bombed.

Suppose you have two postcard campaigns every month. Both campaigns are drawing from the same contact source data. Both lists are created by the same script with nearly the same logic. That's ok if you randomize the contact order or the list is static. But if you don't randomize them and it's supposed to be a "random" draw campaign, that means you'll likely end up sending to the same people in both campaigns. That's exactly what happened. I accidentally postcard bombed 'em.

Thankfully, only a small percent of our "senders" were opted into both campaigns. What does that mean for those senders? Their contacts got `NFL blitzed <https://www.youtube.com/watch?v=SSPewc--3yY>`__ for 3 months straight. Instead of getting 1 or maybe 2 postcards a month if they're really lucky, they received 2 a month, each month until I caught the error. We bombarded about 3,000 lucky potential customers each month during that time. Some of them let us know they thought it was excessive.

   The opposite of love is not hate, it's indifference. - Elie Wiesel

**Sidebar On Analog Marketing**

I think postcards are still relevant as a Marketing tool in 2020. From an environmental perspective, I prefer going digital. Some people let us know when we mail them that they feel the same way and then we stop mailing them. But I think there's something tangible about real things you can hold in your hands. Postcards also tend to get a reaction, even if it's not a good one. Sometimes that reaction is an email stating, "DON'T EVER MAIL ME AGAIN!!!" 😆

**For the record, I changed my mistake to this:**

.. code:: python

   def remove_duplicates(df):
       """Remove duplicates and randomize the order of the rows."""
       original = df.copy(deep=True)
       df = format_for_duplicate_removal(df)
       df = df.drop_duplicates()
       deduped_contacts = original[original.index.isin(df.index)]
       randomized_contacts = deduped_contacts.sample(n=1)
       return randomized_contacts

**Or maybe something like this would be better, for clearer separation of actions:**

.. code:: python

   def remove_duplicates(df):
       """Remove duplicates while preserving original data."""
       original = df.copy(deep=True)
       df = format_for_duplicate_removal(df)
       df = df.drop_duplicates()
       deduped_contacts = original[original.index.isin(df.index)]
       return deduped_contacts

   def randomize_contacts(df):
       """Randomize the order of the rows."""
       randomized_contacts = df.sample(n=1)
       return randomized_contacts

**In Conclusion: Mistakes Happen.**

Sometimes they have interesting consequences when you make them at a certain scale. Maybe I could have written some tests to prevent this. Maybe I should have reviewed my code a couple more times. Sometimes, we're asked to do work that stretches our mental capacity and time to the limit.

Additionally, it's almost always a better choice to use an existing system, rather than writing your own. But in this case, my team was put in a situation where we needed to deliver because some else's software wasn't doing the job. I did my best to fill that need. And we're still using this way to send postcards today.

I wish this failure didn't happen for the sake of everyone involved, but `to err is human <https://en.wikipedia.org/wiki/An_Essay_on_Criticism>`__, right? Live and learn.
