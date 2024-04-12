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
primitively attempts to match that text to a line of Kevin Parker's lyrics written for the band Tame Impala.

I didn't look at the app's code for many years. I just needed to log into `PythonAnywhere <https://pythonanywhere.com>`__ 
every 3 months and hit a button to keep it running on their free plan. Until I decided to update it recently. 

Tame Impala released a new album and lots of additional tracks to import to the app.
Just need to update the database with new music. No big deal, right?

Part of the problem with updating the app was that I didn't remember where the important code 
like the controller default.py and relevant HTML files were after not seeing it for 5+ years. 
It took some time to remember the folder structure of a web2py project. Since it was my first 
project ever, documentation was nonexistent. I could have saved myself a lot of grief if I'd wrote 
down some notes when I made the app.

web2py is relatively easy to grasp for Python developers. One thing I like is that 
once it is installed, the development server is easily started by running the web2py.py file:


.. code:: console

   cd web2py
   python3.10 web2py.py


**web2py Python Errors Solved**

I installed web2py locally with the help of a `DigitalOcean blog post <https://www.digitalocean.com/community/tutorials/how-to-use-the-web2py-framework-to-quickly-build-your-python-app>`__.
After I failed to push a new version of the app to production, for some reasons it was in a broken state.
Python version issues surfaced, requiring some heady navigation. Enjoy these gritty details 
of the tracebacks that transpired.

------------



.. code:: console

   ModuleNotFoundError: No module named 'formatter'


.. image:: {static}/images/ModuleNotFoundError-no-module-named-formatter.png
  :alt: formatter module missing in Python WSGI app

This error showed up in my app's WSGI error logs. Initially, I researched and attempted to install 
the `formatter module <https://pypi.org/project/formatter/>`__. I believe this was caused by attempting 
to run Python code compiled to a .w2p file on Python 3.11 on a Python 3.10 interpreter. However, I didn't 
know how to solve it until after I saw the next error.

------------



.. code:: console
   
   SystemError: compiled code is incompatible

.. image:: {static}/images/SystemError-compiled-code-is-incompatible-cause.png
  :alt: incompatible python interpreter and compiled python code

After reading this error, I consulted Bing about it. One of the options that Bing suggested was 
that my Python code had incompatible versions. This was caused by a mismatch between my development 
and production Python versions.


**Installing Python 3.10 in Development Environment**

Originally, I compiled the updated web2py app in Python 3.11 on my Chromebook. My PythonAnywhere environment was 
running `Python 3.10 <https://www.python.org/downloads/release/python-3105/>`__. Therefore, I need to build the 
development code in Python 3.10 to match the production environment on PythonAnywhere. 
I entered a handful of commands from Bing Copilot to build Python 3.10 on my Ubuntu development environment:

.. code:: console

   sudo apt-get install build-essential
   sudo apt-get install zlib1g-dev
   sudo apt-get install libsqlite3-dev
   wget https://www.python.org/ftp/python/3.10.5/Python-3.10.5.tgz
   cd Python-3.10.5.tgz
   tar zxvf Python-3.10.5.tgz
   ./configure --enable-optimizations --enable-loadable-sqlite-extensions
   make && sudo make install

The lesson I took away is to consider your production environment's Python version before you begin working on a project. 
In most cases, you'll want to match that version in your development environment to avoid errors like this.

After compiling the new development Python 3.10 version, I exported the app to a new .w2p file.
Next, I imported the .w2p file containing the updated app to PythonAnywhere in the admin interface app importer.

After syncing my development and production environment versions, the app showed a different error. 
Progress! 

Since I was using a .w2p file from 5+ years ago, it contained old Python web2py code written in 
earlier Python versions with a few more bugs. Despite these version inconveniences, I was happy to see the 
"compiled code is incompatible" and "formatter module missing" errors stopped.
One problem solved, two more discovered in its wake, am I right?


------------



.. code:: console
   
   SyntaxError: multiple exception types must be parenthesized


.. image:: {static}/images/SyntaxError-exception-types-must-be-parenthesized.png
  :alt: exception types must be parenthesized in Python

This error showed up in my appadmin.py. At some point this unparenthesized syntax was phased out of Python. 
The fix is add parentheses to the exception statements:

*Incorrect*

.. code-block:: python

   except Exception, e:
      
*Correct*

.. code-block:: python

   except (Exception, e):


------------



.. code:: console

   unable to parse csv file: iterator should return strings, not bytes (the file should be opened in text mode)
   

In order to import the new Tame Impala songs to the SQLlite database, web2py provides a 
GUI interface in its admin panel or the DAL (Database Abstraction Layer). 
I chose to use the GUI. In the GUI, you can either manually enter each song or use its csv import widget. 
To save time, I imported via the csv widget. However, this error slowed me down. 
It stemmed from the need for TextIOWrapper to convert the csv data to a required format.

.. image:: {static}/images/unable-to-parse-csv-web2py.png
  :alt: unable to parse csv error importing to web2py SQLlite

The solution I found was to use the 
`fix suggested by AnooshaAviligonda <https://github.com/web2py/web2py/issues/2148#issuecomment-616036400>`__.
In web2py/gluon/packages/dal/pydal/objects.py, I swapped in this code:

.. code-block:: python
   
   csv_reader = csv.reader(TextIOWrapper(utf8_data,encoding), dialect=dialect, **kwargs)


.. image:: {static}/images/unable-to-parse-csv-fix.png
  :alt: unable to parse csv Python fix with TextIOWrapper


After adding the above code to my web2py app's objects.py file, the csv importer completed my 
new Tame Impala songs database import. Also, I was able to export an app from my development environment 
and deploy it into PythonAnywhere via the admin interface. Mission accomplished.

I imported the new songs to my app and brought the code forward into future Python versions. 
Keeping up with this project over the years shows how maintaining an app across different Python versions 
can cause unexpected challenges. With these Python tracebacks conquered, the app is back on the web. 
Now with all of Tame Impala's new lyrics!

**Check out my Tame Impala web2py app here:** 

`tameimpala.pythonanywhere.com/tameimpala <http://tameimpala.pythonanywhere.com/tameimpala>`__