Title: Organize Your Emails in Bulk With Gmail Search Operators + Python Libraries
Date: 2021-02-07 11:17
Author: pythonmarketer
Category: productivity, python
Tags: email, gmail, IMAP, smtp
Slug: using-gmails-search-operators-to-organize-your-emails-in-bulk
Status: published

`<!-- wp:paragraph -->`{=html}

After 12 years with Gmail as my primary email inbox, I wanted to clear out old "Promotions" emails. This can be done with some clever use of Gmail's search syntax shown below.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

I wanted to preserve my "Starred" emails, but delete old emails to free up space. I was able to delete 58,000 "Promotions" emails! I wrote this post because I feel it might save you a little time figuring it out yourself. I also included brief details on possible Python tools for Gmail and IMAP below if you are considering scripting your contact management.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

I didn't need Python in the end after reading some [Gmail search operator examples](https://support.google.com/mail/answer/7190?hl=en). For example, adding a hypen before a search in Gmail acts similar to a ["bitwise" or unary operator (\~)](https://en.wikipedia.org/wiki/Bitwise_operation#NOT) in Python. It excludes or inverses the criteria in a search rather than including it. I was able to use this to exclude my starred emails. You can also add a filter for "has attachment". I used that to star any emails with attachments, then delete the rest and excluded "starred" emails.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Gmail search syntax to get "Promotions" minus "Starred" emails and filter on a date range**:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

`category:promotions -is:starred after:2019/12/31 before:2021/1/1`

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Selecting "all" emails in your search**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:image {"id":5251,"sizeSlug":"large","linkDestination":"none"} -->`{=html}

![](https://pythonmarketer.files.wordpress.com/2021/02/select-all-in-search.jpg?w=588){.wp-image-5251}

`<!-- /wp:image -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Once, you've selected "All" from the checkbox dropdown, click "Select all conversations that match this search".** Now you can apply actions such as "add a star" or "delete" them by clicking the (⋮) vertical ellipses menu:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:image {"id":5258,"sizeSlug":"large","linkDestination":"none"} -->`{=html}

![](https://pythonmarketer.files.wordpress.com/2021/02/gmail-filter-steps.jpg?w=1024){.wp-image-5258}

`<!-- /wp:image -->`{=html}

`<!-- wp:paragraph -->`{=html}

**To Python or not?**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

I also considered Python tools for interfacing with gmail to accomplish this. There doesn't seem to be an easy way to group emails by "Category" in the [Gmail API](https://developers.google.com/gmail/api/quickstart/python) or IMAP. IMAP is shorthand for [Internet Message Access Protocol](https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol).

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[imaplib](https://docs.python.org/3/library/imaplib.html) is an "IMAP4 protocol client" in the Python standard library. Usually python's [smtplib](https://docs.python.org/3/library/smtplib.html) is the first library that comes up for email. Don't forget about imaplib! It might be more suitable for searching based on text in your emails or [creating labeled segments yourself, then applying actions to them](https://superuser.com/questions/719677/how-to-use-gmail-tabs-with-imap).

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Additional Gmail + Python Resources**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[G](https://support.google.com/mail/answer/7190?hl=en)[mail search operators](https://support.google.com/mail/answer/7190?hl=en)

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[imaplib](https://docs.python.org/3/library/imaplib.html) - python standard library interface to email accounts \[[Stack Overflow example](https://stackoverflow.com/questions/3180891/imap-how-to-delete-messages)\]

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[enabling IMAP in your gmail](https://support.google.com/mail/answer/7126229?hl=en)

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[Gmail API Python Quickstart](https://developers.google.com/gmail/api/quickstart/python)

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[Gmail python library](https://github.com/charlierguo/gmail) - There are also pythonic wrappers to the Gmail API like this one.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[imaplib - Python Module of the Week](https://pymotw.com/2/imaplib/)

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[Use Google Like a Pro](https://markodenic.com/use-google-like-a-pro/)

`<!-- /wp:paragraph -->`{=html}
