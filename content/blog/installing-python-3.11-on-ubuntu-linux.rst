How to Install Python 3.11 or 3.12 on a Linux Computer
######################################################
:date: 2023-08-13 22:45
:author: lofipython
:category: coding, programming, python
:tags: install python linux, installing Python 3.11, installing python 3.12, how to build Python 3.11 + 3.12
:slug: installing-python-3.11-on-ubuntu-linux
:status: published

Below are the steps I followed to install both Python 3.11 and Python 3.12 in my Ubuntu Linux shell.
Make sure to adjust your Python version to match 3.11 or 3.12 in all commands.

I downloaded the .tgz file from Python.org, not sure initially how to build Python from it.
Once I unpacked the compressed files, I saw the build instructions in the README.rst
to build a functional Python 3.11 on my Ubuntu computer. Here's how to install the speedier Python versionss 3.11 or 3.12.


**How to Install Python 3.11 or 3.12**

Install Linux build libraries.

.. code:: console

  sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev


I followed this step posted on `this blog <https://aruljohn.com/blog/install-python/>`_.
If you don't do this, you'll see an error about C not being found when running the ./configure command.

**Install sqllite Libraries (Django Requirement)**

.. code:: console

  sudo apt install sqlite3 libsqlite3-dev


Use curl to download the Python gzip file.

.. code:: console

   curl https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz --output Python-3.11.0.tgz


.. image:: {static}/images/curl-python-install-command.png
  :alt: download Python with curl


Unpack gzip file to folder.

.. code:: console

   tar -xvzf Python-3.11.0.tgz


Change directory, read the README + find build commands.

.. code:: console

   cd Python-3.11.0
   cat README.rst

Build Python.

.. code:: console

    # Build Python on Unix, Linux, BSD, macOS, and Cygwin:
    ./configure --enable-optimizations
    make
    make test
    sudo make install


**Building Python on Various Platforms**


    This will install Python as ``python3``.

    You can pass many options to the configure script; run ``./configure --help``
    to find out more.  On macOS case-insensitive file systems and on Cygwin,
    the executable is called ``python.exe``; elsewhere it's just ``python``.

    Building a complete Python installation requires the use of various
    additional third-party libraries, depending on your build platform and
    configure options.  Not all standard library modules are buildable or
    useable on all platforms.  Refer to the
    `Install dependencies <https://devguide.python.org/setup/#install-dependencies>`_
    section of the Developer Guide for current detailed information on
    dependencies for various Linux distributions and macOS.

    On macOS, there are additional configure and build options related
    to macOS framework and universal builds.  Refer to `Mac/README.rst
    <https://github.com/python/cpython/blob/main/Mac/README.rst>`_.

    On Windows, see `PCbuild/readme.txt <https://github.com/python/cpython/blob/main/PCbuild/readme.txt>`_.

    \- Python 3.11 Linux README.rst
