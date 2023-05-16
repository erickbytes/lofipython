How to Upgrade Requests in the Bash Console
###########################################
:date: 2022-01-23 14:41
:author: pythonmarketer
:category: coding, python
:tags: bash, pip, python install, pythonanywhere
:slug: how-to-upgrade-requests-in-the-pythonanywhere-bash-console
:status: published

This command can be used to upgrade your Python `requests library <https://docs.python-requests.org/en/latest/>`__ with `pip <https://pythonmarketer.com/2018/01/20/how-to-python-pip-install-new-libraries/>`__, Python's package manager. It is tailored for a PythonAnywhere environment. I suppose this command works on any `Bash console <https://www.gnu.org/software/bash/>`__, but if you're running your app with pythonanywhere, you can find the bash console here:

.. code-block:: python

   https://www.pythonanywhere.com/user/your_username/consoles/

.. figure:: https://pythonmarketer.files.wordpress.com/2022/01/python-anywhere-bash-highlight-2.png?w=1024
   :alt: 
   :figclass: wp-image-6771

**Install requests with this command:**

::
   python3.8 -m pip install requests --upgrade --user

Substitute in whatever your Python version is. This command upgrades the requests library on a PythonAnywhere app. If any libraries depend on a specific version of requests, a warning appears like this one I saw for the `python-unsplash <https://github.com/yakupadakli/python-unsplash>`__ library.

   ERROR: python-unsplash 1.1.0 has requirement requests==2.20.0, but you'll have requests 2.27.1 which is incompatible.

.. figure:: https://pythonmarketer.files.wordpress.com/2022/01/requests-upgrade-full-install.png?w=1024
   :alt: 
   :figclass: wp-image-6777
