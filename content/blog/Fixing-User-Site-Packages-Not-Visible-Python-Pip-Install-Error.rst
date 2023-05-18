How to Fix Pip Install Site-Packages --user Error
#################################################
:date: 2023-05-17 20:35
:author: pythonmarketer
:category: coding, python
:tags: pip, python install, troubleshooting error
:slug: fix-python-pip-user-install-error
:status: published


| While running Python 3.11 today, out of the blue I saw this error attempting to pip install a package in my virtual environment:
|

::

    ERROR: Cannot perform a '--user' install. User site-packages are not visible in this virtualenv.


I found a `Github thread <https://github.com/microsoft/vscode-python/issues/14327>`_ that fixed the problem! You need to update your pyvenv.cfg in order to resolve this conflict.

Here is the how to fix your Python environment from Github user `jawalahe <https://github.com/microsoft/vscode-python/issues/14327#issuecomment-757408341>`_ :

1. Go to the pyvenv.cfg file in the Virtual environment folder
2. Set include-system-site-packages to true and save the change.

After completing this, my pip installs worked again and no longer returned the error.