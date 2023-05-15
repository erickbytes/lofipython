Launch the Browser with a Windows Batch File
############################################
:date: 2021-12-06 21:15
:author: pythonmarketer
:category: coding, productivity, programming, Scripts
:tags: automation, command line, scripting, Windows
:slug: can-you-script-it
:status: published

Can it be scripted? Ask yourself this question about everything you do. Every application opened, website viewed and task you knock out in the course of a day might be worth writing a script to automate. As an example, here is a `Windows batch file <https://en.wikipedia.org/wiki/Batch_file>`__ that opens 3 websites I visit frequently:

**Open Websites.bat**

*Save below 3 lines as a ".bat" file and double click it to launch the websites in a browser.*

.. code:: wp-block-code

   (start "Netflix" "https://www.netflix.com/browse"
   start "Twitter" "https://twitter.com/home"
   start "Gmail" "https://mail.google.com/")

Anything and everything is subject to automation. You can use `Windows Scripting <https://pythonmarketer.com/2020/05/06/exploring-windows-command-line-tools-batch-file-automation-and-remote-desktop-connection/>`__, Python, R, other programming languages or `RPA <https://pythonmarketer.com/2021/08/15/how-to-open-firefox-with-webbrowser-on-ubuntu-linux/>`__. Keep your eyes peeled for time you could be saving. One script like this might save (a few seconds everyday) **x** (every day for the rest of your life). Or more. Sometimes, I find myself piddling away at something I don't really need to be struggling to remember. Consider writing a script for it!
