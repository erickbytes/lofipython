Lightning Scripts ⚡
####################
:date: 2019-02-12 06:27
:author: pythonmarketer
:category: automation, coding, pandas, productivity, programming, Scripts
:tags: alicia keys, code, computers, hamilton, lightning scripts, python
:slug: lightning-scripts-%e2%9a%a1
:status: published

You may or may not be familiar with `PyCon <https://www.youtube.com/channel/UCsX05-2sVSH7Nx3zuk3NYuQ>`__'s `Lightning Talks <https://pyvideo.org/pycon-us-2010/pycon-2010--plenary--saturday-evening-lightning-t.html>`__, a session of quick hitter talks given each year on a variety of topics. These "Lightning Scripts" are ten of my favorite Python scripts that have served me well as of late to perform a variety of tasks.

Highlights include the glob, os, calendar, webbrowser and pandas modules. Plus, how to convert a dataframe into a pdf and how to take a snapshot of a website with pdfkit. The webpage pdf was not the greatest snapshot in some cases, but did capture text and many of a live website's visual elements.

If you have Python installed, paste the script into a text editor and run your .py file from the command line or however you like to run your scripts. You may have to change file paths to work on your operating system.

The first 5 scripts use modules that ship with Python.
------------------------------------------------------

**(1) Uppercase all of the file names in the current working directory.**

.. code-block:: python

   import os
   filenames = os.listdir(os.getcwd())
   for filename in filenames:
       os.rename(filename, filename.upper())

os module `documentation <https://docs.python.org/3/library/os.html#os.rename>`__

**(2) Get all filenames in the current directory and write to a text file.**

.. code-block:: python

   import os
   folder_contents = os.listdir(os.getcwd())
   with open("list_of_dir_files.txt","w") as fhand:
       for item in folder_contents:
           fhand.write('f{item}\n')

**(3) Check what day of the week is today.**

.. code-block:: python

   import calendar
   from datetime import date
   today = date.today() 
   if calendar.day_name[today.weekday()] == 'Friday': 
       print("Today is Friday.") 
   else: 
       print("Today is not Friday.")

`calendar documentation <https://docs.python.org/3/library/calendar.html>`__

**(4) Get the two most recent file names from a directory. This is a Windows file path example. I have escaped the backslashes below to make it work in my Atom text editor.**

.. code-block:: python

   import glob
   import getpass
   import os
   # getctime == by created date, getmtime == by date modified
   # get all files, regardless of extension
   folder = f'C:/Users/{getpass.getuser()}/Desktop/'
   list_of_files = glob.glob(folder)
   newest_file = sorted(glob.iglob('C:/Users/your_username/Desktop/*.csv'), key=os.path.getmtime)[-1]
   second_newest_file = sorted(glob.iglob('C:/Users/your_username/Desktop/*.csv'), key=os.path.getmtime)[-2] 
   print(newest_file, second_newest_file)

glob module documentation: https://docs.python.org/3/library/glob.html#glob.iglob

**(5)  Auto-Hamilton Ticket Lottery**

.. code-block:: python

      import webbrowser
      webbrowser.open('https://www.luckyseat.com/hamilton-chi/', new=0)

webbrowser PMOTW: https://pymotw.com/3/webbrowser

To Run The Next 3 Scripts, install pandas:
------------------------------------------
::

   python -m pip install pandas

**(6) Split a csv file into smaller excel files.**

.. code-block:: python

   import pandas as pd
   file_name = 'big_file.csv'
   # slice off extension
   src_file_minus_ext = file_name.split('.')[:-1]
   for i, df in enumerate(pd.read_csv(file_name, chunksize=250000)):
       csv = f'{src_file_minus_ext}{str(i)}.csv'
       df.to_csv(csv, index=False, header=df.columns)

pandas beginner tutorial: https://www.youtube.com/watch?v=5JnMutdy6Fw

**(7) Convert a .xlsx to .csv**

.. code-block:: python

   import pandas as pd
   df = pd.read_excel("input.xlsx")
   df.to_csv("output.csv", index=False)

**(8) Convert a .xlsx to .html**

.. code-block:: python

   import pandas as pd
   file_name = "data.xlsx"
   df = pd.read_excel(file_name)
   df.to_html("data.html")

To Run The Last Two Scripts, install pdfkit:
--------------------------------------------

pdfkit relies on another library, wkhtmltopdf, which adds an extra wrinkle to setting it up for Windows users. I've laid out the differences between using pdfkit for Windows vs. Ubuntu below.

::

   python -m pip install pdfkit

**installing wkhtmltopdf on Windows**

To use pdfkit on Windows, go to the link, choose your version to download. This installs a Windows executable that pdfkit needs to find to work.

::

   https://wkhtmltopdf.org/downloads.html

**installing wkhtmltopdf on Ubuntu**

::

   sudo apt-get install wkhtmltopdf


   **For Windows, **\ `download wkhtmltopdf <https://wkhtmltopdf.org/downloads.html>`__\ ** and add this config patch for pdfkit:**

.. code-block:: python

   import pdfkit
   url = 'https://www.hollywoodreporter.com/news/grammys-alicia-keys-best-moments-as-host-1185013'
   config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
   pdfkit.from_url(url, 'webpage.pdf', configuration=config)

**4 Convert a .html file to .pdf. (Add config patch above for Windows.)**

.. code-block:: python

   import pdfkit
   pdfkit.from_file('data.html', 'report.pdf')

**5 Create a pdf snapshot of a webpage on Ubuntu below. (Add config patch above for Windows.)**

.. code-block:: python

   import pdfkit
   url = 'https://www.hollywoodreporter.com/news/grammys-alicia-keys-best-moments-as-host-1185013'
   pdfkit.from_url(url, 'alicia_keys.pdf')

pdfkit documentation: https://pypi.org/project/pdfkit/


**Final Thoughts**

I am very pleased with pdfkit. I am also toying around with Python's PyFPDF: https://pyfpdf.readthedocs.io/en/latest/index.html and PyPDF2: https://pythonhosted.org/PyPDF2 libraries. Together, these three offer some unique abilities for creating and manipulating pdf files. And the pandas library is amazing for reading and writing tabular data sheets, can't say enough great things about pandas. Worth the time. Hope you enjoyed these Lightning Scripts :)

