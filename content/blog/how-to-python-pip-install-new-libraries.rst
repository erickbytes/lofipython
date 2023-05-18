How to Install Libraries and Enable the pip Installer in Python
###############################################################
:date: 2018-01-20 17:50
:author: pythonmarketer
:category: coding, programming
:tags: command line, computers, matrix, neo, pip, python, python libraries, software
:slug: how-to-python-pip-install-new-libraries
:status: published

Python comes with a bunch of `standard modules <https://docs.python.org/3/py-modindex.html>`__. My favorites are shutil, glob, datetime, time, os (operating system), re (regular expressions) and webbrowser. The standard library is loaded.

Inevitably, you'll want to install new libraries from Python's rich ecosystem of external modules. Enter pip, Python's handy package manager and people's champion.

This post will teach you some Python history, show how to install pandas, and help you troubleshoot problems if it's not working. You'll find Windows and Linux commands for venv setup (recommended). With pip, you'll feel like Neo when installing new modules. Any skill is at your fingertips. It's like learning kung fu. There's probably a library for that!

.. image:: http://pythonmarketer.files.wordpress.com/2018/01/19c0c-i-know-kung-fu-e1516470914221.png
   :alt: i know kung fu
   :class: alignnone size-full wp-image-1321
   :width: 1277px
   :height: 532px

**First, Some Python Version Caveats + History**

**Python 2 reached end of life on January 1st, 2020**. `Python 2 has officially been sunset <https://www.python.org/doc/sunset-python-2/>`__.

Python comes with pip now, no setup is required. But certain versions such as Python 3.2 or the Python 2.7 that came stock on my improbably still functioning 2008 black Macbook, for example, may not have it installed.

In December 2021, Python 3.6 reached `"end of life phase" <https://devguide.python.org/devcycle/#end-of-life-branches>`__.

Python 3.6 is "now effectively frozen". Read more in `PEP 494 <https://www.python.org/dev/peps/pep-0494/>`__. (Released Oct. 2022)

**TLDR:** use Python 3.7 to 3.11. This blog endorses using the lightning fast Python version `3.11. <https://www.python.org/downloads/release/python-3110/>`__

Enter This in Your Terminal
---------------------------

::

    python -m pip install pandas

Pandas is a super useful library for wrangling spreadsheet data, AKA "tabular" data. If successful, you should see activity that looks similar to the below screenshot, where I am installing `openpyxl <https://openpyxl.readthedocs.io/en/stable/>`__, an additional Python Excel library you'll likely want. You are good to go! This is the part where you get to feel like Neo! See `Installing Python Modules <https://docs.python.org/3/installing/index.html>`__ in the Python Documentation for more detailed instructions.

.. image:: http://pythonmarketer.files.wordpress.com/2018/01/de9d6-neo_pip-e1587604013861.png
   :alt: neo_pip
   :class: alignnone size-full wp-image-1322
   :width: 650px
   :height: 340px

**To view all your installed libraries, enter:**

.. code:: python

   pip list

**Write a "requirements.txt" of installed libraries:**

.. code:: python

   pip freeze > requirements.txt

**You can list your outdated packages with the --outdated argument:**

.. code:: python

   pip list --outdated

**Use pip's -h help command line argument:**

.. code:: python

   pip -h

**View your system and user pip config settings:**

.. code:: python

   pip config debug

**Supplementary Resources**

-  Take a look at this `list of 20 modules <https://pythontips.com/2013/07/30/20-python-libraries-you-cant-live-without/>`__ to get started. Here is another `more comprehensive list of libraries <https://github.com/vinta/awesome-python>`__ you can now install.
-  Swing by the pip documentation `Quickstart <https://pip.pypa.io/en/stable/quickstart/>`__ and `User Guide <https://pip.pypa.io/en/stable/user_guide/>`__ to learn some helpful commands.
-  `PyPI, the Python Package Index <https://pypi.org/search/?q=time+travel>`__ is the official Python package repository.
-  `Why you should use 'python -m pip' <https://snarky.ca/why-you-should-use-python-m-pip/>`__
-  `pip cheat sheet from opensource.com <https://opensource.com/downloads/pip-cheat-sheet?utm_medium=Email&utm_campaign=weekly&sc_cid=7013a000002DAKPAA4>`__

Congrats on figuring out how to install packages with pip, have fun!

Having issues? Try upgrading your pip version.
----------------------------------------------

.. code:: python

   python -m pip install --upgrade pip

Try the ensurepip command.
--------------------------

This command will install and upgrade pip to the newest version. New in Python 3.4:

::

    python -m ensurepip --upgrade

..

   \"The ensurepip ` <https://docs.python.org/3/library/ensurepip.html#module-ensurepip>`__ package provides support for bootstrapping the pip installer into an existing Python installation or virtual environment. This bootstrapping approach reflects the fact that pip is an independent project with its own release cycle, and the latest available stable version is bundled with maintenance and feature releases of the CPython reference interpreter."

   \- `ensurepip Python Documentation <https://docs.python.org/3/library/ensurepip.html>`__

You should follow best practice and `create a virtual environment <https://docs.python.org/3/library/venv.html>`__  before installing libraries. `venv  <https://docs.python.org/3/library/venv.html>`__ or `virtualenv  <https://pythonmarketer.wordpress.com/2018/04/10/creating-isolated-python-environments-with-virtualenv/>`__ will help you out. To create with venv:

::

    python3 -m venv add_env_name_here

After your environment is created, activate it with the first command below, then install a library on Ubuntu Linux:

::

    source add_env_path_here/bin activate
    python -m pip install pandas

Alternatively, on Windows computers:

::

    cd add_env_path_here\scripts & activate
    python -m pip install pandas


**Getting the prefix right can be tricky.**

Since this was written, I moved to Python 3.11. When I first moved from Python 2 to 3 on Windows, I somehow accidentally configured the following behavior: entering **python some_program.py**\  ran a .py file with Python 2. Whereas, entering **py some_program.py**\ ran a .py file with Python 3.

In the install command, the prefix is a reference to your Python executable. You may just need to alter your prefix to call it correctly. Here are some to try in place of "python". Observe what happens when you run these command variations.Good luck!

``python3 -m pip install pandas``

``python3.11 -m pip install pandas``

``py -m pip install pandas``

``pip3 install pandas``

How to Manually Enable the pip Installer
----------------------------------------

**The rest of this post may be useful to you if you are:**

#. Working on legacy Python 2 code or Python 3.3 or lower for which pip is not installed.
#. Seeking to fix a faulty pip install that is not working properly.
#. Curious to know how to manually set up pip.

Assumes Python is already `installed <https://www.python.org/downloads/>`__. If you're running Windows 10, I found it easy to install Python from the `Windows store <https://www.microsoft.com/en-us/p/python-39/9p7qfqmjrfp7?activetab=pivot:overviewtab>`__. Download the `get-pip.py file <https://bootstrap.pypa.io/get-pip.py>`__. Go to the link, right click the page and "Save As" a .py file to download. Then place the file where you want to access it. I placed mine in C:\Python27\Lib\site-packages

You could also download the file with `curl <https://curl.haxx.se/>`__:

::

    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.pyt-pip.py 


If you are not sure where your site-packages folder is, type 
`python -m site <https://stackoverflow.com/questions/122327/how-do-i-find-the-location-of-my-python-site-packages-directory>`__ into command prompt for file path ideas.

**Run the get-pip.py file.**

Using command prompt's cd command with a Windows "&" operator to run the Python file in a Windows command prompt:

::

    cd c:\Python27\Lib\site-packages & python get-pip.py

Or Linux terminal:

::
    
    cd /Python27/Lib/site-packages && python get-pip.py``

You should see some activity in command prompt that shows installation/updating of "setup" and "wheel". When it finishes, you have installed pip.

**Type into command prompt at the same location:**

::

    python -m pip install requests

This should install the Requests module into your Python libraries. Requests is an http module which is highly regarded almost universally by the Python community.

**Thanks for reading! Check out these other posts with pip installed library examples:**

`Fix Grammar and Spelling with language_tool_python and textblob <https://lofipython.com/fix-spelling-and-grammar-with-language_tool_python-and-textblob/>`__

`gooey <https://lofipython.com/gooey-gui-for-python-scripts/>`__ - GUI library

`tweepy <https://lofipython.com/delete-all-your-tweets-with-tweepy-and-the-twitter-api/>`__ - Twitter library

`A Guide to Making HTTP requests <https://lofipython.com/how-to-make-json-requests-with-python/>`__
