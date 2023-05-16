Organize Your Emails in Bulk With Gmail Search Operators + Python Libraries
###########################################################################
:date: 2021-02-07 11:17
:author: pythonmarketer
:category: productivity, python
:tags: email, gmail, IMAP, smtp
:slug: using-gmails-search-operators-to-organize-your-emails-in-bulk
:status: published

After 12 years with Gmail as my primary email inbox, I wanted to clear out old "Promotions" emails. This can be done with some clever use of Gmail's search syntax shown below.

I wanted to preserve my "Starred" emails, but delete old emails to free up space. I was able to delete 58,000 "Promotions" emails! I wrote this post because I feel it might save you a little time figuring it out yourself. I also included brief details on possible Python tools for Gmail and IMAP below if you are considering scripting your contact management.

I didn't need Python in the end after reading some `Gmail search operator examples <https://support.google.com/mail/answer/7190?hl=en>`__. For example, adding a hypen before a search in Gmail acts similar to a `"bitwise" or unary operator (~) <https://en.wikipedia.org/wiki/Bitwise_operation#NOT>`__ in Python. It excludes or inverses the criteria in a search rather than including it. I was able to use this to exclude my starred emails. You can also add a filter for "has attachment". I used that to star any emails with attachments, then delete the rest and excluded "starred" emails.

**Gmail search syntax to get "Promotions" minus "Starred" emails and filter on a date range**:

``category:promotions -is:starred after:2019/12/31 before:2021/1/1``

**Selecting "all" emails in your search**

.. figure:: https://pythonmarketer.files.wordpress.com/2021/02/select-all-in-search.jpg?w=588
   :alt: Filtering Gmail Emails
   :figclass: wp-image-5251

**Once, you've selected "All" from the checkbox dropdown, click "Select all conversations that match this search".** Now you can apply actions such as "add a star" or "delete" them by clicking the (⋮) vertical ellipses menu:

.. figure:: https://pythonmarketer.files.wordpress.com/2021/02/gmail-filter-steps.jpg?w=1024
   :alt: Gmail Filter Steps
   :figclass: wp-image-5258

**To Python or not?**

I also considered Python tools for interfacing with gmail to accomplish this. There doesn't seem to be an easy way to group emails by "Category" in the `Gmail API <https://developers.google.com/gmail/api/quickstart/python>`__ or IMAP. IMAP is shorthand for `Internet Message Access Protocol <https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol>`__.

`imaplib <https://docs.python.org/3/library/imaplib.html>`__ is an "IMAP4 protocol client" in the Python standard library. Usually python's `smtplib <https://docs.python.org/3/library/smtplib.html>`__ is the first library that comes up for email. Don't forget about imaplib! It might be more suitable for searching based on text in your emails or `creating labeled segments yourself, then applying actions to them <https://superuser.com/questions/719677/how-to-use-gmail-tabs-with-imap>`__.

**Additional Gmail + Python Resources**

`G <https://support.google.com/mail/answer/7190?hl=en>`__\ `mail search operators <https://support.google.com/mail/answer/7190?hl=en>`__

`imaplib <https://docs.python.org/3/library/imaplib.html>`__ - python standard library interface to email accounts [`Stack Overflow example <https://stackoverflow.com/questions/3180891/imap-how-to-delete-messages>`__]

`enabling IMAP in your gmail <https://support.google.com/mail/answer/7126229?hl=en>`__

`Gmail API Python Quickstart <https://developers.google.com/gmail/api/quickstart/python>`__

`Gmail python library <https://github.com/charlierguo/gmail>`__ - There are also pythonic wrappers to the Gmail API like this one.

`imaplib - Python Module of the Week <https://pymotw.com/2/imaplib/>`__

`Use Google Like a Pro <https://markodenic.com/use-google-like-a-pro/>`__
