Troubleshooting Tracebacks to Resurrect a Python Web2py App
###########################################################
:date: 2024-04-07 20:53
:author: lofipython
:category: coding, programming, python, web2py, apps
:tags: troubleshooting web2py app, updating old Python code, maintaining python code
:slug: troubleshooting-tracebacks-to-resurrect-a-web2py-app
:status: published

Back in 2016, I `built a web2py app <https://lofipython.com/askkevinparker-com-my-first-web-app-other-notes>`__ 
as my first web application. It accepts a prompt from the user and 
primitively attempts to match that text to a line of Kevin Parker's lyrics.

I didn't look at the app's code for many years. I just needed to log into PythonAnywhere every 3 months 
and hit a button to keep it running on their free plan. Until I decided to update it recently. 

Tame Impala released a new album and lots of additional tracks to import to the app.
Just need to update the database with new music. No big deal easy peasy, right? Wrong! 

Part of the problem was that I didn't remember where the important code like the controller default.py 
and HTML files were after not seeing it for 3+ years. It took me some time to remember the folder 
structure of a web2py project also.

**web2py Python Errors Solved**

I installed web2py locally with the help of a `DigitalOcean blog post <https://www.digitalocean.com/community/tutorials/how-to-use-the-web2py-framework-to-quickly-build-your-python-app>`__.
After I failed to push a new version of the app to production, for some reasons it was in a broken state.
Python version issues popped up and required some heady navigation. Enjoy these gritty details 
of the tracebacks that transpired.

.. code:: console

   ModuleNotFoundError: No module named 'formatter'


.. image:: {static}/images/ModuleNotFoundError-no-module-named-formatter.png
  :alt: formatter module missing in Python WSGI app

This error popped up in my app's WSGI error logs. I researched the `formatter module <https://pypi.org/project/formatter/>`__. 
I believe this was caused by attempting to run Python code compiled to a .w2p file
on Python 3.11 on a Python 3.10 interpreter. However, I didn't know how to solve it until after I saw the next error.

.. code:: console
   
   SystemError: compiled code is incompatible

.. image:: {static}/images/SystemError-compiled-code-is-incompatible-cause.png
  :alt: incompatible python interpreter and compiled python code

Once I read this error, I consulted Bing about it. One of the options that Bing suggested was 
that my Python code had incompatible versions. This was caused by a mismatch between my development 
and production Python versions.

**Installing Python 3.10 in Development Environment**

I compiled the updated web2py app in Python 3.11 on my Chromebook. My PythonAnywhere environment was 
running Python 3.10. Therefore, I need to build the development version in Python 3.10 to match the 
production environment on PythonAnywhere. I then entered a handful of commands and waited for Python 3.10 
to compile in my Ubuntu development environment. 

After compiling the development version and importing it to PythonAnywhere, the app shows a different error!
Since I was using a .w2p file to import the app to my dev environment and back to production, 
it contained old Python web2py code written in earlier Python versions with a few more bugs that surfaced.

.. code:: console
   
   SyntaxError: multiple exception types must be parenthesized


.. image:: {static}/images/SyntaxError-exception-types-must-be-parenthesized.png
  :alt: exception types must be parenthesized in Python

This error showed up in my appadmin.py. At some point this unparenthensized syntax was phased out of Python. 
The fix is add parentheses to the exception statements:

*Incorrect*

.. code-block:: python

   except Exception, e:
      
*Correct*

.. code-block:: python

   except (Exception, e):


.. code:: console

   unable to parse csv file: iterator should return strings, not bytes (the file should be opened in text mode)
   

In order to import the new Tame Impala songs to the SQLlite database, web2py provides a 
GUI interface in its admin panel or the DAL (Database Abstraction Layer). 
I chose to use the GUI. In the GUI, you can either manually enter each song or use its csv import widget. 
To save time, I imported via the csv widget. However, this error slowed me down. 
It stemmed from the need for TextIOWrapper to convert the csv data to a required format.

.. image:: {static}/images/unable-to-parse-csv-fix.png
  :alt: unable to parse csv Python fix with TextIOWrapper

The solution I found was to use the 
`fix suggested by AnooshaAviligonda <https://github.com/web2py/web2py/issues/2148#issuecomment-616036400>`__.
In web2py/gluon/packages/dal/pydal/objects.py, I swapped in this code:

.. code-block:: python
   
   csv_reader = csv.reader(TextIOWrapper(utf8_data,encoding), dialect=dialect, **kwargs)


After adding the above code to my web2py app's object.py file, the csv importer was functional again. 
I successfully imported the new songs to my app and brought the code forward into future Python versions. 
Keeping up with this project over the years shows how maintaining an app across different Python versions 
can cause unexpected bugs. After some tough Python tracebacks conquered, the app is now functional, 
updated with all Tame Impala's new music and live on the web again!

**Check out my Tame Impala web2py app here:** 

`tameimpala.pythonanywhere.com/tameimpala <http://tameimpala.pythonanywhere.com/tameimpala>`__.