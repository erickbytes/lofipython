Opening Firefox Via the webbrowser Module + RPA Tools
#####################################################
:date: 2021-08-15 23:13
:author: pythonmarketer
:category: automation, coding, gui, programming, python
:tags: Firefox, RPA
:slug: how-to-open-firefox-with-webbrowser-on-ubuntu-linux
:status: published

webbrowser is a convenient Python standard library module. It opened my Firefox browser on my Ubuntu Linux operating system running on a Chromebook. This code is adapted from a `Python Examples blog post <https://pythonexamples.org/python-open-url-in-firefox-browser/>`__. Below is a list of other browsers you can open with webbrowser. At the bottom of this post, you'll find more tools to interact with browsers and GUIs programmatically.

.. code-block:: python

   import webbrowser
   firefox_sh = '/usr/lib/firefox/firefox.sh'
   webbrowser.register('firefox',
       None,
       webbrowser.BackgroundBrowser(firefox_sh))
   url = 'https://lofipython.com'
   webbrowser.get('firefox').open_new_tab(url)
   print(webbrowser._browsers)

.. raw:: html

   <figure class="wp-block-table is-style-regular">

====================== ==================================
Type Name              Class Name
====================== ==================================
``'mozilla'``          ``Mozilla('mozilla')``
``'firefox'``          ``Mozilla('mozilla')``
``'netscape'``         ``Mozilla('netscape')``
``'galeon'``           ``Galeon('galeon')``
``'epiphany'``         ``Galeon('epiphany')``
``'skipstone'``        ``BackgroundBrowser('skipstone')``
``'kfmclient'``        ``Konqueror()``
``'konqueror'``        ``Konqueror()``
``'kfm'``              ``Konqueror()``
``'mosaic'``           ``BackgroundBrowser('mosaic')``
``'opera'``            ``Opera()``
``'grail'``            ``Grail()``
``'links'``            ``GenericBrowser('links')``
``'elinks'``           ``Elinks('elinks')``
``'lynx'``             ``GenericBrowser('lynx')``
``'w3m'``              ``GenericBrowser('w3m')``
``'windows-default'``  ``WindowsDefault``
``'macosx'``           ``MacOSX('default')``
``'safari'``           ``MacOSX('safari')``
``'google-chrome'``    ``Chrome('google-chrome')``
``'chrome'``           ``Chrome('chrome')``
``'chromium'``         ``Chromium('chromium')``
``'chromium-browser'`` ``Chromium('chromium-browser')``
====================== ==================================

.. raw:: html

   <figcaption>

`webbrowser docs <https://docs.python.org/3/library/webbrowser.html#webbrowser.get>`__

.. raw:: html

   </figcaption>

.. raw:: html

   </figure>

**Check out these other browser\gui automation tools:**

-  `pyautogui <https://pyautogui.readthedocs.io/en/latest/>`__
-  `Selenium <https://www.selenium.dev/selenium/docs/api/py/>`__
-  `RPA for Python <https://github.com/tebelorg/RPA-Python>`__
-  `robotframework <https://github.com/robotframework/robotframework>`__
-  `TagUI <https://github.com/kelaberetiv/TagUI>`__
-  `Sikuli <https://github.com/RaiMan/SikuliX1>`__
-  `Open RPA <https://github.com/open-rpa/openrpa>`__
-  `Power Automate <https://flow.microsoft.com/en-us/blog/automate-tasks-with-power-automate-desktop-for-windows-10-no-additional-cost/>`__
-  `CasperJS <https://www.casperjs.org/>`__
-  `PhantomJS <https://github.com/ariya/phantomjs>`__
-  `SlimerJS <https://slimerjs.org/>`__

*see* *also:* `Robot Process Automation <https://en.wikipedia.org/wiki/Robotic_process_automation>`__, `Things You Can Do With a Browser in 2020 <https://github.com/luruke/browser-2020>`__
