Copying a pandas Dataframe to Google Sheets with pygsheets
##########################################################
:date: 2019-12-21 18:58
:author: pythonmarketer
:category: automation, coding, excel, Google, pandas
:tags: api, google api, google sheets, json, python, spreadsheets
:slug: copying-a-csv-file-to-google-sheets-with-pygsheets
:status: published

**Disclaimer**: This endeavor was before I discovered `AppScript <https://developers.google.com/apps-script>`__, which may be an alternative solution to using pygsheets or other python libraries. pygsheets is interesting, but it could be a stretch to justify using it for something that could be done with AppScript. Both are ways to solve a problem by automating Google Sheet operations.

**This was done on the Windows 7 OS.** **First,**\ `install libraries with pip <https://docs.python.org/3/installing/index.html>`__\ **. Enter in command prompt or terminal:**

#. ``python -m pip install pandas``
#. ``python -m pip install numpy``
#. ``python -m pip install pygsheets``

**Then, following the** `steps documented by pygsheets: <https://pygsheets.readthedocs.io/en/stable/authorization.html>`__

#. Create a Google Developer Account at `console.developers.google.com <http://console.developers.google.com>`__
#. `Enable Sheets API <https://pygsheets.readthedocs.io/en/stable/authorization.html>`__ to account
#. Enable Drive API to account. Same as last step, but search for Drive.
#. Create a Client Secret json file. Select "Credentials" tab, and "Create Credentials". Select Client Secret from options. Export from console and place in same directory as your .py file.
#. Create a Service Account json file by selecting it instead of "Client Secret".
#. Authorize pygsheets with your json files. (See below.)
#. Copy spreadsheet to Google Sheet with pandas and pygsheets. (See below.)

**After completing the first 5 steps, import pygsheets and authorize your account with the client secret json file:**

.. code-block:: python

   import pygsheets
   gc = pygsheets.authorize(client_secret='path/to/client_secret[...].json') 

You will be prompted by the terminal to go to a hyperlink in a browser, get your authorization code, and enter that authorization code into the terminal.

**Now, import both libraries needed and switch to authorize with your service json file. Then, load the csv to a dataframe with pandas. Finally, copy it to an existing Google Sheet with pygsheets:**

.. code-block:: python

   import pygsheets
   import pandas as pd

   """Select worksheets by id, index, or title."""
   gc = pygsheets.authorize(service_file='path/to/service_account_credentials.json') 
   sh = gc.open('add_google_sheet_name_here')
   wks = sh.worksheet_by_title('add_sheet_tab_name_here') 

   """Set a pandas dataframe to google sheet, starting at 1st row, 1st column"""
   df = pd.read_csv('Example_Data.csv') 
   wks.set_dataframe(df,(1,1))

**[Example] Split and upload a sheet with 40 columns**

Google Sheets limits importing to 26 columns and 1,000 rows at a time. So you'll have to load the sheets in chunks if you have more than that. This approach uses numpy's `array_split <https://docs.scipy.org/doc/numpy/reference/generated/numpy.array_split.html>`__:

.. code-block:: python

   import pygsheets 
   import pandas as pd
   import numpy as np

   gc = pygsheets.authorize(client_secret='path/to/client_secret[...].json')
   sh = gc.open('add_google_sheet_name_here') 
   wks = sh.worksheet_by_title('add_sheet_tab_name_here') 
   df = pd.read_csv('Data_to_GSheets.csv') 

   # split columns into two dataframes with numpy and pandas
   first_half_cols, second_half_cols = np.array_split(df.columns, 2)
   first_half = df[first_half_cols]
   second_half = df[second_half_cols]
    
   # set both dataframes side-by-side in Google sheet
   wks.set_dataframe(first_half,(1,1))
   start_column = first_half.shape[1]
   wks.set_dataframe(second_half,(1, start_column)) 

**Conclusion**

I found the terminal error messages from pygsheets to be very helpful while debugging the above. This module offers many other nifty spreadsheet operations. Solid library. You can now create and edit Google Sheets with Python.

AppsScript should probably be the default tool when working with Google Sheets because it is built in, but Python does have tools available to work with Google Sheets.

**Resources**

`pygsheets Github <https://github.com/nithinmurali/pygsheets>`__

`pygsheets Documentation <https://pygsheets.readthedocs.io/en/stable/authorization.html>`__

`Google Sheets Documentation <https://developers.google.com/sheets/api/guides/concepts>`__

`pandas Documentation <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html>`__
