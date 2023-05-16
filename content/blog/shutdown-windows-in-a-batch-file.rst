"Shutdown" a Windows Computer by Double-clicking a Batch File
#############################################################
:date: 2023-02-21 18:28
:author: pythonmarketer
:category: automation, coding, Windows
:tags: windows automation, windows batch files
:slug: shutdown-windows-in-a-batch-file
:status: published

Here is a quick and easy way to automate turning off your computer. This saves me about 15 seconds to manually click the start menu and restart buttons. It worked for me on an old, laggy HP computer running the Windows 10 operating system. Now, I can double-click a batch file on my Desktop and walk away while it struggles.

Batch files are executable via:

-  double-clicking them
-  right-clicking and selecting "Run"
-  entering the batch file name in command prompt, ex: "shut down CPU.bat" if the current working directory is in the same folder as the batch file

Open a blank Notepad document and save as **shut down CPU.bat** with this text:

::
   cmd /c shutdown -s

.. figure:: https://pythonmarketer.files.wordpress.com/2023/02/screenshot_20230221-225405-494.png?w=681
   :alt: Source: `Microsoft shutdown documentation <https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown>`__
   :figclass: wp-image-7432

   Source: `Microsoft shutdown documentation <https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown>`__

When this batch file runs, it will trigger a pop-up window warning that your computer is about to shut down. For my slow, slogging computer it shut off about 20 seconds later. This may also trigger queued automatic updates to install, which happened when I used the above command.

.. figure:: https://pythonmarketer.files.wordpress.com/2023/02/image_editor_output_image1037058739-1677025419090.png?w=687
   :alt: `Source: Stack Overflow <https://stackoverflow.com/questions/162304/how-do-i-shutdown-restart-or-log-off-windows-via-a-bat-file>`__
   :figclass: wp-image-7423

   `Source: Stack Overflow <https://stackoverflow.com/questions/162304/how-do-i-shutdown-restart-or-log-off-windows-via-a-bat-file>`__
