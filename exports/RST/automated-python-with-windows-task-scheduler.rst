Automated Python With Windows Task Scheduler
############################################
:date: 2018-11-25 19:44
:author: pythonmarketer
:category: automation, productivity, programming, python, Windows
:tags: coding, organization
:slug: automated-python-with-windows-task-scheduler
:status: published

**So you want to run your Python scripts automatically, but how?**

I had heard of several popular scheduling libraries in Python like `celery <http://www.celeryproject.org/>`__, `Invoke <https://www.pyinvoke.org/>`__, and `schedule <https://github.com/dbader/schedule>`__. One of my requirements is to run the python file "in the background", not in command prompt or an open window.

Enter Windows Task Scheduler, the de facto scheduler on Windows 7 computers. I have  scheduled a few scripts and it is working like a charm. In this post, I will schedule an example script to clean up my desktop at the beginning of each day. I have a habit of accumulating many Excel files there throughout the workday. This example automatically moves them into a folder.

Other Windows scheduling alternatives worth mentioning include `creating a Windows service <http://thepythoncorner.com/dev/how-to-create-a-windows-service-in-python/>`__, or using `schtasks <https://docs.microsoft.com/en-us/windows/win32/taskschd/schtasks>`__ if you prefer the command line.

**Here's how to schedule a Python script to run:**

1. Search for Windows Task Scheduler in the start menu. Then select "Task Scheduler Library" to see all of the tasks Windows is running automatically.

2. In the right toolbar, select "Create Basic Task" and give it a name and description. Note: I selected "Configure for: Windows 7, Windows Server 2008 R2".

.. image:: https://pythonmarketer.files.wordpress.com/2018/11/general.png
   :alt: general
   :class: wp-image-1577 alignright
   :width: 481px
   :height: 361px

3. Set the time and frequency that the program will run in the "Triggers" tab.

4. Under the "Actions" tab, select "Start a Program" from the dropdown. Under "Program/Script", enter the path to your Python.exe file. I set mine to a Python executable located within my `virtual environment <https://pythonmarketer.wordpress.com/2018/04/10/creating-isolated-python-environments-with-virtualenv/>`__, but yours might be found wherever you have Python installed.

::

   C:\Users\your_username\Desktop\36env\Scripts\python.exe

5. Under "Add arguments (optional)", add the path to your .py script, within quotes:

::

   "C:\Users\your_username\Desktop\36env\clean_desktop_excels.py"

.. image:: http://pythonmarketer.files.wordpress.com/2018/11/bd0a9-actions-e1543177551739.png
   :alt: actions
   :class: alignnone size-full wp-image-1578
   :width: 448px
   :height: 236px

6. Select additional conditions and settings as desired, such as "Wake the computer to run this task" and "Run with highest privileges".

I am enjoying this simple, easy and convenient scheduling manager for Windows. I figured most of this out thanks to `this blog <https://www.esri.com/arcgis-blog/products/product/analytics/scheduling-a-python-script-or-model-to-run-at-a-prescribed-time/?rmedium=redirect&rsource=/esri/arcgis/2013/07/30/scheduling-a-scrip>`__. Below is my script to clean my desktop each morning by moving my Excel files into a folder, using Python's stock `shutil <https://docs.python.org/3/library/shutil.html>`__ and os libraries. Set it and forget it, ya know what i mean? :D

::

   from shutil import move
   import getpass
   import os

   """
   Desktop Spreadsheet File Cleaner - Python Marketer
   https://atomic-temporary-107329037.wpcomstaging.com/2018/11/25/automated-python-with-windows-task-scheduler/
   """
   # Get all Desktop files and folders
   src_directory = f'C:\\Users\\{getpass.getuser()}\\Desktop'
   dir_items = os.listdir(src_directory)
   excel_files = [item for item in dir_items \
                   if '.csv' in item or '.xls' in item]

   dst = f'C:\\Users\\{getpass.getuser()}\\Desktop\\Current_Month_Excels'
   os.makedirs(dst, exist_ok=True)
   for xl in excel_files: 
       path_to_file = src_directory + xl
       move(path_to_file, dst)

**Additional Reading**

`Troubleshooting Windows Task Scheduler <https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc721846(v=ws.11)?redirectedfrom=MSDN>`__ - Windows Documentation
