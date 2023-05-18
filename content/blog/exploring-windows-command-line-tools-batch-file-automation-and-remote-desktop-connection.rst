Script Windows Like A Pro: Command Line, Batch Files, Remote Desktop Connection and pywin32
###########################################################################################
:date: 2020-05-06 14:11
:author: pythonmarketer
:category: automation, command prompt, Scripts, Windows
:tags: command line, remote computer, scripting, shell
:slug: exploring-windows-command-line-tools-batch-file-automation-and-remote-desktop-connection
:status: published

Here are a few useful corners of the vast array of Windows scripting tools.

Helpful Windows Command Line Documentation
------------------------------------------

-  `Windows command line Documentation Syntax <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/command-line-syntax-key>`__
-  `Command-line reference A-Z <https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb490890%28v%3dtechnet.10%29>`__
-  `Command shell overview <https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb490954%28v%3dtechnet.10%29>`__
-  `Using command redirection operators <https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb490982%28v%3dtechnet.10%29>`__
-  `About Windows Remote Management <https://docs.microsoft.com/en-us/windows/win32/winrm/about-windows-remote-management>`__

A Few General Windows Commands
------------------------------

Use  `find <https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb490906(v=technet.10)>`__ 
to look in a text file to count the lines matching a string:

::

   find /C "FAIL" < "Test_Results.txt"
   # returns: 0 if no match or # of lines found, e.g. 2,50,100

I wrote a post on `findstr <https://pythonmarketer.wordpress.com/2018/07/15/findstr-aka-grep-for-windows/>`__, which offers similar functionality.

**clip:** pipe commands `into the clipboard <https://www.hanselman.com/blog/ForgottenButAwesomeWindowsCommandPromptFeatures.aspx>`__.

**If:** `If <https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb490920(v=technet.10)>`__ Statements based on if files exist.

**List ip address-related info:**

::

   ipconfig 

**Check system bit (usually 64-bit or 32-bit):**

::

   wmic os getosarchitecture

Automate Windows Scripts with Batch Files
-----------------------------------------

Batch files can be run from command prompt or by double-clicking them. Here's an example of text in a batch file that activates a python virtual environment. Swap in your username and environment if you've created it.

::

   cmd /k "cd C:\Users\your_username\PythonEnv\Scripts & activate & cd .. & dir"

#. Save above as a .bat file.
#. This uses `cmd <https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb490880%28v%3dtechnet.10%29>`__ to open a new command prompt in a Windows batch file.
#. `cd  <https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb490875(v=technet.10)>`__\ into my python virtual env then activate it by running a batch file.
#. Then call dir to print directory contents.

`Set <https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb490998(v=technet.10)>`__\  a custom system 'last_name' variable to be recalled later.

::

   set /p last_name=Enter a last name:
   echo %last_name%
   pause

Here we print it out with `echo <https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb490897(v=technet.10)>`__. Then `pause <https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb490965(v=technet.10)>`__.

**Line continuation in batch files:** Use ^ to continue your batch file scripts on a new line.

System Assessment Tools: powercfg and sfc
-----------------------------------------

**Display system stats:**

::

   systeminfo

**Use powercfg to assess power, sleep and system states**

::

   powercfg /SLEEPSTUDY

Use sfc to perform a system file check:

::

   # scan and repair
   sfc /SCANNOW
   # scan, but do not repair:
   sfc /VERIFYONLY

Accessing a Remote Computer From the Command Line
-------------------------------------------------

You may want to `ping <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/ping>`__ a remote computer to see if it's running. Add your ip address instead of the below 1s and 0s:

::

   ping 01.10.10.01

**Log into your Remote Desktop with**\ `mstsc <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/mstsc>`__\ **:**

#. Run Remote Desktop Connection, save an RDP file from Windows Desktop Client.
#. You may need to `adjust your credentials on your local machine. <https://serverfault.com/questions/396722/your-system-administrator-does-not-allow-the-use-of-saved-credentials-to-log-on>`__
#. Finally, trigger login to an active window from command prompt:

::

   mstsc RDP_File_Name.rdp

`WinRM <https://docs.microsoft.com/en-us/windows/win32/winrm/portal>`__ and WinRS can allow terminal access to your Remote Desktop. You may need to set your wifi network to private. To configure winrm:

::

   winrm quickconfig

**Log into a remote computer with**\ `winrs <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/winrs>`__\ ** and run ipconfig:**

::

   winrs -r:https://myserver.com -t:600 -u:administrator -p:$%fgh7 ipconfig

Check Out Python's `pywin32 <https://github.com/mhammond/pywin32>`__ Module
---------------------------------------------------------------------------

This module is extremely useful for scripting out Windows applications. For example, I've made good use of its interfaces to Outlook and `Task Scheduler <https://pythonmarketer.wordpress.com/2018/11/25/automated-python-with-windows-task-scheduler/>`__. Install with `pip <http://pythonmarketer.wordpress.com/2018/01/20/how-to-python-pip-install-new-libraries/>`__:

::

   python -m pip install pywin32

**Here's an example to send an Outlook email:**

.. code-block:: python

   import win32com.client

   outlook = win32com.client.Dispatch('outlook.application')
   mail = outlook.CreateItem(0)
   mail.To = 'someone@example.com'
   mail.CC = 'name@example.com'
   mail.Subject = 'Moneyball Review'
   mail.Body = """Moneyball is an inspiring movie, based on real events.
               Brad Pitt, Jonah Hill and Philip Seymour Hoffmann gave great performances.
               The trade deadline scene is delightful. Wow.
               Chris Pratt as Hatteberg too. What a solid film.
               Money isn't everything. Playing ball is.
               """
   mail.Attachments.Add('Baseball_Analysis.csv')
   mail.Send()
