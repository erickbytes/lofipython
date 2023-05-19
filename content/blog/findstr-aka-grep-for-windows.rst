Findstr, RegEx File Searches for Windows
########################################
:date: 2018-07-15 19:52
:author: pythonmarketer
:category: command prompt, data, python, Windows
:tags: programming, regex
:slug: findstr-aka-grep-for-windows
:status: published

Findstr is the Windows alternative to GREP, which runs on the `Unix operating system <https://www.howtogeek.com/182649/htg-explains-what-is-unix/>`__. Findstr searches files with `regular expressions <https://en.wikipedia.org/wiki/Regular_expression>`__ and seems useful for string matching within files and directories.  It is one of over `280 command prompt commands <https://www.lifewire.com/list-of-command-prompt-commands-4092302>`__. Here's the official `Windows Documentation <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/findstr>`__ and some `Linux vs. Windows Examples. <https://www.mkyong.com/linux/grep-for-windows-findstr-example/>`__

**Update:** Windows announced that `Grep and several other Unix command line tools will be added to Windows 10 <https://hackaday.com/2019/06/10/windows-10-goes-to-shell/>`__. This is a new alternative to findstr.

**This findstr command returns all lines containing an '@' in a text file.**

::

   findstr @ test.txt

.. image:: https://pythonmarketer.files.wordpress.com/2018/07/findstr-emails.png
   :alt: findstr Emails
   :class: alignnone size-full wp-image-1406
   :width: 602px
   :height: 48px

**I was happy to see Findstr's convenient help menu:**

::

   findstr -?

.. image:: https://pythonmarketer.files.wordpress.com/2018/07/findstr_help.png
   :alt: findstr_help
   :class: alignnone size-full wp-image-1408
   :width: 657px
   :height: 603px

Regular expressions are so powerful. It's nice to have this utility within the command prompt. I am hoping to get to know some of the other 280 command prompt commands.

**I've previously explored regex with Python. This Python regex example finds all words in a text file containing '@' symbols:**

.. code-block:: python

   import re

   # read the file to string + regex email search
   with open('test.txt', 'r') as fhand:
       string = fhand.read()
       # this regex returns a python list of emails:
       emails = re.findall('(\S*@\S+)', string) 
       print(emails)

.. image:: https://pythonmarketer.files.wordpress.com/2018/07/findall_python.png
   :alt: findall_python
   :class: alignnone size-full wp-image-1405
   :width: 633px
   :height: 173px

For more command prompt nuggets, check out my more recent post: `Exploring Windows Command Line Tools, Batch Files and Remote Desktop Connection <https://lofipython.com/exploring-windows-command-line-tools-batch-file-automation-and-remote-desktop-connection/>`__.
