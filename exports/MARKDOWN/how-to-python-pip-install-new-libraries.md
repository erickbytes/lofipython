Title: How to Install Libraries and Enable the pip Installer in Python
Date: 2018-01-20 17:50
Author: pythonmarketer
Category: coding, programming
Tags: command line, computers, matrix, neo, pip, python, python libraries, software
Slug: how-to-python-pip-install-new-libraries
Status: published

Python comes with a bunch of [standard modules](https://docs.python.org/3/py-modindex.html). My favorites are shutil, glob, datetime, time, os (operating system), re (regular expressions) and webbrowser. The standard library is loaded.

Inevitably, you'll want to install new libraries from Python's rich ecosystem of external modules. Enter pip, Python's handy package manager and people's champion.

This post will teach you some Python history, show how to install pandas, and help you troubleshoot problems if it's not working. You'll find Windows and Linux commands for venv setup (recommended). With pip, you'll feel like Neo when installing new modules. Any skill is at your fingertips. It's like learning kung fu. There's probably a library for that!

![i know kung fu](http://pythonmarketer.files.wordpress.com/2018/01/19c0c-i-know-kung-fu-e1516470914221.png){.alignnone .size-full .wp-image-1321 width="1277" height="532"}

## First, Some Python Version Caveats + History** **

**Python 2 reached end of life on January 1st, 2020**. [Python 2 has officially been sunset](https://www.python.org/doc/sunset-python-2/).

Python comes with pip now, no setup is required. But certain versions such as Python 3.2 or the Python 2.7 that came stock on my improbably still functioning 2008 black Macbook, for example, may not have it installed.

**In December 2021, Python 3.6 reached ["end of life phase"](https://devguide.python.org/devcycle/#end-of-life-branches).**

Python 3.6 is "now effectively frozen". Read more in [PEP 494](https://www.python.org/dev/peps/pep-0494/). (Released Oct. 2022)

**TLDR:** use Python 3.7 to 3.11. This blog endorses using the lightning fast Python version [3.11.](https://www.python.org/downloads/release/python-3110/)

## Enter This in Your Terminal

`python -m pip install pandas`

Pandas is a super useful library for wrangling spreadsheet data, AKA "tabular" data. If successful, you should see activity that looks similar to the below screenshot, where I am installing [openpyxl](https://openpyxl.readthedocs.io/en/stable/), an additional Python Excel library you'll likely want. You are good to go! This is the part where you get to feel like Neo! See [Installing Python Modules](https://docs.python.org/3/installing/index.html) in the Python Documentation for more detailed instructions.

![neo_pip](http://pythonmarketer.files.wordpress.com/2018/01/de9d6-neo_pip-e1587604013861.png){.alignnone .size-full .wp-image-1322 style="color: var(--color-text);font-size: 1rem" width="650" height="340"}

**To view all your installed libraries, enter:**

    pip list

**Write a "requirements.txt" of installed libraries:**

    pip freeze > requirements.txt

**You can list your outdated packages with the --outdated argument:**

    pip list --outdated

**Use pip's -h help command line argument:**

    pip -h

**Supplementary Resources**

-   Take a look at this [list of 20 modules](https://pythontips.com/2013/07/30/20-python-libraries-you-cant-live-without/) to get started. Here is another [more comprehensive list of libraries](https://github.com/vinta/awesome-python) you can now install.
-   Swing by the pip documentation [Quickstart](https://pip.pypa.io/en/stable/quickstart/) and [User Guide](https://pip.pypa.io/en/stable/user_guide/) to learn some helpful commands.
-   [PyPI, the Python Package Index](https://pypi.org/search/?q=time+travel) is the official Python package repository.
-   [Why you should use 'python -m pip'](https://snarky.ca/why-you-should-use-python-m-pip/)
-   [pip cheat sheet from opensource.com](https://opensource.com/downloads/pip-cheat-sheet?utm_medium=Email&utm_campaign=weekly&sc_cid=7013a000002DAKPAA4)

Congrats on figuring out how to install packages with pip, have fun!

## Having issues? Try upgrading your pip version.

    python -m pip install --upgrade pip

## Try the ensurepip command.

This command will install and upgrade pip to the newest version. New in Python 3.4:

::: {.highlight-python3 .notranslate}
::: highlight
::: {.highlight-python3 .notranslate}
::: highlight
    python -m ensurepip --upgrade
:::
:::
:::
:::

> "The [`ensurepip`{.xref .py .py-mod .docutils .literal .notranslate}](https://docs.python.org/3/library/ensurepip.html#module-ensurepip "ensurepip: Bootstrapping the "pip" installer into an existing Python installation or virtual environment."){.reference .internal} package provides support for bootstrapping the `pip`{.docutils .literal .notranslate} installer into an existing Python installation or virtual environment. This bootstrapping approach reflects the fact that `pip`{.docutils .literal .notranslate} is an independent project with its own release cycle, and the latest available stable version is bundled with maintenance and feature releases of the CPython reference interpreter."
>
> \- [ensurepip Python Documentation](https://docs.python.org/3/library/ensurepip.html)

**You should follow best practice and** [create a virtual environment](https://docs.python.org/3/library/venv.html) **before installing libraries. [venv](https://docs.python.org/3/library/venv.html) or [virtualenv](https://pythonmarketer.wordpress.com/2018/04/10/creating-isolated-python-environments-with-virtualenv/) will help you out. To create with venv:**

`python3 -m venv add_env_name_here`

After your environment is created, activate it with the first command below, then install a library on Ubuntu Linux:

1.  `cd add_env_path_here/bin & source activate`
2.  `python -m pip install pandas`

Alternatively, on Windows computers:

1.  `cd add_env_path_here\scripts & activate`
2.  `python -m pip install pandas`

**Know your OS.**

If you're interested in installing pip on Linux, [try here](https://www.tecmint.com/install-pip-in-linux/). For Mac, [try here](https://www.shellhacks.com/python-install-pip-mac-ubuntu-centos/). Windows, Mac and Linux sometimes use different prefixes (e.g. python, py, python3) to run a python script. Which leads me to my next point...

**Getting the prefix right can be tricky.**

Since this was written, I moved to Python 3.8. When I first moved from Python 2 to 3 on Windows, I somehow accidentally configured the following behavior: entering **python some_program.py**[ ran a .py file with Python 2. Whereas, entering]{style="color: var(--color-text)"} **py some_program.py**[ ran a .py file with Python 3. ]{style="color: var(--color-text)"}

[In the install command, the prefix is a reference to your Python executable. You may just need to alter your prefix to call it correctly. Here are some to try in place of "python". Observe what happens when you run these command variations. ]{style="color: var(--color-text)"}Good luck!

`python3 -m pip install pandas`

`python3.11 -m pip install pandas`

`py -m pip install pandas`

`pip3 install pandas`

## How to Manually Enable the pip Installer

**The rest of this post may be useful to you if you are:  
**

1.  Working on legacy Python 2 code or Python 3.3 or lower for which pip is not installed.
2.  Seeking to fix a faulty pip install that is not working properly.
3.  Curious to know how to manually set up pip.

*Assumes Python is already [installed](https://www.python.org/downloads/). If you're running Windows 10, I found it easy to install Python from the [Windows store](https://www.microsoft.com/en-us/p/python-39/9p7qfqmjrfp7?activetab=pivot:overviewtab).*

**Download the [get-pip.py file](https://bootstrap.pypa.io/get-pip.py).**

Go to the link, right click the page and "Save As" a .py file to download. Then place the file where you want to access it. I placed mine in C:\\Python27\\Lib\\site-packages

You could also download the file with [curl](https://curl.haxx.se/):

`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.pyt-pip.py`[ ]{style="color: var(--color-text)"}

> [If you are not sure where your site-packages folder is, type ]{style="color: var(--color-text)"}**[`python -m site`](https://stackoverflow.com/questions/122327/how-do-i-find-the-location-of-my-python-site-packages-directory)**[ into command prompt for file pat]{style="color: var(--color-text)"}h ideas.

**Run the get-pip.py file.**

Using command prompt's cd command with a Windows "&" operator to run the Python file in a Windows command prompt:

`cd c:\Python27\Lib\site-packages & python get-pip.py`

Or Linux terminal:

`cd /Python27/Lib/site-packages && python get-pip.py`

[You should see some activity in command prompt that shows installation/updating of "setup" and "wheel". When it finishes, you have installed pip.]{style="color: var(--color-text)"}

**Type into command prompt at the same location:**

`python -m pip install requests`[  ]{style="color: var(--color-text)"}

[This should install the Requests module into your Python libraries. Requests is an http module which is highly regarded almost universally by the Python community.]{style="color: var(--color-text)"}

**Thanks for reading! Check out these other posts with pip installed library examples:**

[Fix Grammar and Spelling with language_tool_python and textblob](https://pythonmarketer.com/2022/01/30/fix-spelling-and-grammar-with-language_tool_python-and-textblob/)

[gooey](http://pythonmarketer.wordpress.com/2018/08/25/gooey-gui-for-python-scripts/) - GUI library

[tweepy](http://pythonmarketer.wordpress.com/2020/09/13/delete-all-your-tweets-with-tweepy-and-the-twitter-api/) - Twitter library

[A Guide to Making HTTP requests](https://pythonmarketer.com/2020/05/18/how-to-make-json-requests-with-python/)

[Plotting Datasets Using Jupyter, Pandas and Matplotlib](http://pythonmarketer.wordpress.com/2019/04/12/datasets-plotting-using-jupyter-pandas-and-matplotlib/)
