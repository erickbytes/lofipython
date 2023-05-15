Title: Creating Isolated Python Environments with Virtualenv
Date: 2018-04-10 00:44
Author: pythonmarketer
Category: coding, programming
Tags: computers, python, virtual machine
Slug: creating-isolated-python-environments-with-virtualenv
Status: published

**Why bother?** Because with [virtualenv](https://virtualenv.pypa.io/en/stable/), we can create multiple Python environments on one computer that each:

1.  *Are capable of running different versions of Python.* Right now I have both Python 2.7 and Python 3.8 installed and am able to create either environment and run code with that version's Python interpreter.
2.  *Isolate dependencies for external libraries.* Once the environment is created, I do not have to worry about different versions of Python libraries conflicting with each other.
3.  *Allow you to have a unique Python environment for different projects.*

**Potential Pitfalls to Avoid with Virtual Environments**

1.  **Know your OS.** The virtualenv commands are slightly different from the Mac, or Linux OS to Windows.
2.  **Be aware of variations within Windows systems.** Some Stack Overflow post commands mention a "Bin" folder, however on my particular version of Windows, the folder was named "Scripts" instead. There was no "Bin" folder that I could locate.
3.  **Choose the right library.** Virtualenv is used commonly. Virtualenvwrapper is a handy tool to make it easier to use. I chose virtualenv as my virtual environment library because I wanted to maintain both Python 2.7 and 3.8 environments. For versions of Python 3.3 and above, check out [venv](https://docs.python.org/3/library/venv.html), an easy to use, stock library and virtual environment generator. I am looking forward to checking both of these out. Virtualenv can be installed with the [pip installer](https://pythonmarketer.wordpress.com/2018/01/20/how-to-python-pip-install-new-libraries/).

Consider upgrading your Python version to the [latest stable release](https://www.google.com/search?client=ubuntu&channel=fs&q=python+latest+stable+release&ie=utf-8&oe=utf-8). [Follow these steps to download and install Python 3.8 in the Ubuntu terminal.](https://linuxize.com/post/how-to-install-python-3-8-on-ubuntu-18-04/)

**Install pip in your new Python version:  
**

    curl -O https://bootstrap.pypa.io/get-pip.py
    python3.8 get-pip.py

**Install Virtalenv on Ubuntu:** `sudo pip3 install virtualenv`

**Create a virtual environment with your new Python version. Enter in terminal or command prompt:** `virtualenv -p python3.8 38env`

**Activate your new virtual environment on Ubuntu:**

    cd Desktop/Projects/Sandbox38/bin && source activate

**Alternatively, activate an env on Windows:**

    cd Desktop\Projects\your_env_name\scripts & activate

[Activation and Deactivation for Mac vs. Windows](https://www.codingforentrepreneurs.com/blog/activate-reactivate-deactivate-your-virtualenv/)

**Now you can now install pandas 1.0 in your virtual environment.**

`python3.8 -m pip install pandas`

**Below are two screenshots of the command prompt and some links that helped me.**

Below, I am creating a 2.7 environment, even though I have Python 3.6 as my system version. Note how many times I messed up before I got it right, thanks to a [Stack Overflow post](https://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv). It took many previous tries but I eventually figured out how to create a Python 2.7 virtualenv, which I named py27_env. I ran the python.exe file inside of the folder where I installed Python 2.7, which I named py27.

To run a program, I entered python some_program.py. I also tested by downloading modules that did not have a version compatible with Python 3.6. It worked and installed the correct Python 2 version in my py27_env environment.

![create_py2_env](https://pythonmarketer.files.wordpress.com/2018/04/create_py2_env.jpg){.alignnone .size-full .wp-image-1378 width="700" height="882"}

Below, I am activating a previously created environment named 14pandas. Then I am installing two external Excel libraries, pandas and xlrd in my environment. The one-liner posted above is a more efficient way to activate a virtualenv.

![virtualenv_Activate](https://pythonmarketer.files.wordpress.com/2018/04/virtualenv_activate.jpg){.alignnone .size-full .wp-image-1379 width="676" height="564"}

[More Reading on venv, pipenv, and virtualenv](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)
