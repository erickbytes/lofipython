A Stroll Through Pandas 1.0, Python’s Tabular Data Powerhouse
#############################################################
:date: 2018-05-12 03:39
:author: pythonmarketer
:category: coding, data, excel, pandas, python
:tags: data analysis, programming, software
:slug: pandas-pythons-excel-powerhouse
:status: published

**Introduction**

|pandas|\ Thanks to pandas, I have automated some data cleaning and file reading processes at my job. Here are some terms and code that have been useful or interesting to me after 2 years of exploration. I also checked out "\ `Python for Data Analysis <https://github.com/wesm/pydata-book>`__\ " from the\ `Chicago Public Library <https://www.chipublib.org/>`__\ .

If I could suggest anything to be successful with pandas, it is repetition. I use it nearly every day at work. Dive into its `API documentation. <https://pandas.pydata.org/pandas-docs/stable/reference/index.html>`__ There are tons of useful tools there, laid out with meticulous detail and examples. I began learning pandas with this PyCon 2015 `tutorial from Brandon Rhodes <https://www.youtube.com/watch?v=5JnMutdy6Fw>`__, it's informative and entertaining! (It's a little dated now but I still recommend it.) The `Reproducible Data Analysis in Jupyter video series <https://www.youtube.com/watch?v=_ZEWDGpM-vM>`__ by Jake VanderPlas is also a great example of pandas-related workflows.

**Table of Contents**

#. Python\pandas Installation and Version Compatibility
#. ACHIEVEMENT UNLOCKED: Welcome to pandas 1.0
#. Data Wrangling, Exploration and Broadcasting

   -  ``Series.str`` & ``Series.dt`` accessors
   -  ``apply``, ``applymap``, ``lambda`` and ``map``
   -  featuring ``pandas.to_markdown()``
   -  SQL operations with ``df.merge()`` and ``pandas.read_sql()``
   -  ``pandas.read_clipboard()``
   -  converting between Series and DataFrame

#. Turning json API responses into a dataframe with ``pandas.json_normalize()``
#. Plotting Visualizations with matplotlib
#. Supplementary Resources and Links

(1) Python\pandas Installation and Version Compatibility
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python 3.6 and higher can `install pandas 1.0 <https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html>`__.

**Installing Python 3.8 on Windows**

For Windows installation, see the python docs for an installer, "`Using Python on Windows" <https://docs.python.org/3/using/windows.html>`__.

**Installing Python 3.8 on Ubuntu**

`Follow these steps to download and install Python 3.8 in the Ubuntu terminal. <https://linuxize.com/post/how-to-install-python-3-8-on-ubuntu-18-04/>`__ To upgrade to pandas 1.0, I installed Python 3.8, the `latest stable release <https://www.google.com/search?client=ubuntu&channel=fs&q=python+latest+stable+release&ie=utf-8&oe=utf-8>`__, "`from source <https://linuxize.com/post/how-to-install-python-3-8-on-ubuntu-18-04/>`__" on Ubuntu 16.04.

**If you intend to use**\ `pandas.to_markdown() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_markdown.html>`__\ **on Ubuntu, it might save you trouble to pre-emptively install the '_bz2' library before you build your Python from source.**

On Ubuntu, I ran into ModuleNotFoundError: No module named '_bz2' and fixed by entering in the terminal: ``sudo apt-get install libbz2-dev``

I also saw this message when completing install:

   The necessary bits to build these optional modules were not found. To find the necessary bits, look in setup.py in detect-modules() for the module's name.

**If you need to re-build Python on Ubuntu, enter:**

::

   cd /home/erick/Python-3.8.0/
   ./configure --enable-loadable-sqlite-extensions && make && sudo make install

I installed missing  \_bz2 and \_sqllite3 modules then re-built with these commands.

**Installing Older pandas Versions on Ubuntu**

The version downloaded with this command is about 6 months behind the current version. For me, this installed pandas 0.17 on Ubuntu:

``sudo apt-get install python3-pandas``

As of February 2020, this command `installs pandas version 0.24 with pip <https://docs.python.org/3/installing/index.html>`__ when used with Python 3.5 on Linux Ubuntu 16.04:

``python3.5 -m pip install pandas``

.. image:: https://pythonmarketer.files.wordpress.com/2018/05/successful_python_install.jpg
   :alt: successful_python_install
   :class: alignnone wp-image-2420
   :width: 676px
   :height: 186px

**If pandas is already installed, you can upgrade with**\ `pip <https://pythonmarketer.wordpress.com/2018/01/20/how-to-python-pip-install-new-libraries/>`__\ **:**

[caption id="attachment_2572" align="alignright" width="179"]\ |pip_list| Enter pip list to see installed libraries.[/caption]

``python -m pip install --upgrade pandas``

To check if pip is installed: ``python -m pip list``

**Consider following best practice and create a**\ `virtual environment <https://pythonmarketer.wordpress.com/2018/04/10/creating-isolated-python-environments-with-virtualenv/>`__\ **with your new Python version.**\ `venv <https://docs.python.org/3/library/venv.html>`__\ **wasn't included in my Python 3.8 installation on Ubuntu 16.04, so I installed virtualenv:**

``python -m pip --user install virtualenv``

**Let's create a new virtual environment. Enter in terminal or command prompt:**

``virtualenv -p python3.8 add_env_name_here``

**Now, activate your new virtual environment on Linux:**

``cd add_env_name_here/bin && source activate``

**Or activate environment on Windows:**

``cd add_env_name_here\scripts & activate``

**"ImportError: Missing optional dependency 'tabulate'. Use pip or conda to install tabulate:" To use pd.to_markdown(), install Tabulate:**

``python -m pip install tabulate``

**To use pd.read_clipboard() on Linux, install**\ `xclip <https://github.com/astrand/xclip>`__\ **or**\ `xsel: <https://askubuntu.com/questions/705620/xclip-vs-xsel>`__\  

``sudo apt-get install xclip``\ **
**

**I also saw a prompt to install pyperclip:**

``python -m pip install pyperclip``

**Now install pandas 1.0 and**\ `matplotlib <https://matplotlib.org/users/installing.html>`__\ **in your virtual environment.**

::

   python3.8 -m pip install pandas
   python -m pip install -U matplotlib

(2) Welcome to pandas 1.0
~~~~~~~~~~~~~~~~~~~~~~~~~

You did it! Welcome to the good life. The basis of pandas is the "`dataframe <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html>`__", commonly abbreviated as df, which is similar to a spreadsheet. Another core pandas object is the `pandas.Series <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html>`__ object, which is similar to a Python list or `numpy <http://cs231n.github.io/python-numpy-tutorial/>`__ array. When imported, pandas is aliased as "pd". The pd object allows you to access many useful pandas functions. I'll use it interchangeably with pandas in this post.

   The library’s name derives from **pan**\ el **da**\ ta, a common term for multidimensional data sets encountered in statistics and econometrics.

   `pandas: a Foundational Python Library for Data Analysis and Statistics <https://www.dlr.de/sc/Portaldata/15/Resources/dokumente/pyhpc2011/submissions/pyhpc2011_submission_9.pdf>`__

   - Wes McKinney

(3) `Data Wrangling <https://en.wikipedia.org/wiki/Data_wrangling>`__, Exploration and Broadcasting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Data is commonly read in from file with**\ `pd.read_csv() <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html>`__\ **

::

   import pandas as pd
   file_name = 'my_bank_statement.csv'
   # you may sometimes need to specify an alternate encoding: encoding = "ISO-8859-1"
   df = pd.read_csv(file_name, encoding='utf-8')
   print(df.head())
   print(df.shape) # returns a tuple: (# of rows, # of columns)
   print(df.dtypes)
   print(df.info())

**Create a dataframe from a list of Python lists, named movies below, with**\ `pd.DataFrame <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html>`__\ **:**

::

   import pandas as pd

   column_names = ["Title", "Release Date", "Character", "Actor", "Movie Budget", "Worldwide Gross"]
   movies = [["Ocean's 11", "12/7/2001", "Danny Ocean", "George Clooney","$85,000,000"," $450,728,529"],
   ["Ocean's 11", "12/7/2001", "Tess Ocean", "Julia Roberts","$85,000,000"," $450,728,529"],
   ["Runaway Bride", "6/30/1999", "Ike Graham", "Richard Gere","$70,000,000","$309,457,509"],
   ["Runaway Bride", "6/30/1999", "Maggy Carpenter", "Julia Roberts","$70,000,000","$309,457,509"],
   ["Bonnie and Clyde", "9/1/1967", "Clyde Barrow", "Warren Beaty","$2,500,000", "$70,000,000"],
   ["Bonnie and Clyde", "9/1/1967", "Bonnie Parker", "Faye Dunaway","$2,500,000", "$70,000,000"]]

   df = pd.DataFrame(movies, columns=column_names)
   df = df[["Title","Character", "Actor", "Movie Budget", "Worldwide Gross"]]
   print(df.to_markdown(showindex=False, tablefmt="simple"))

**Let's print the table to our terminal with**\ `pd.to_markdown() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_markdown.html>`__\ **, which is\ `new in pandas version 1.0.0 <https://pandas.pydata.org/pandas-docs/version/1.0.0/whatsnew/v1.0.0.html>`__:**

.. image:: https://pythonmarketer.files.wordpress.com/2018/05/simple_layout_markdown.jpg
   :alt: simple_layout_markdown
   :class: alignnone size-full wp-image-2538
   :width: 847px
   :height: 189px

**Slicing and sorting a dataframe, removing duplicates, and working with datetime objects**

#. Let's create a new dataframe slice with only two columns
#. Drop duplicate movies
#. Convert the dates to datetime objects
#. Get the year from an array of datetime objects
#. Set the year as the dataframe index

::

   df = pd.DataFrame(movies, columns=column_names)
   date_df = df[['Title', 'Release Date']].drop_duplicates(subset=['Title'])
   date_df['Release Date'] = pd.to_datetime(date_df['Release Date'])
   # create year column using the pd.Series.dt datetime accessor:
   date_df['Release Year'] = df['Release Date'].dt.year
   date_df = date_df.sort_values(by=['Release Date'])
   date_df = date_df.set_index('Release Year')
   print(date_df.to_markdown(showindex=False, tablefmt='simple'))

|dates_of_movies|
-----------------

**Applying Broadcasting in pandas**

Broadcasting means to map a function or an arithmetic calculation over an over an array (using apply or map) or dataframe (applymap).

   "Summing up, apply works on a row/column basis of a DataFrame, applymap works element-wise on a DataFrame, and map works element-wise on a Series."

   - Stack Overflow [`Source <https://stackoverflow.com/questions/19798153/difference-between-map-applymap-and-apply-methods-in-pandas>`__]

**Applying a function to a pandas column**

-  Convert columns to int and calculate the difference between two columns.
-  Let's format those integers back to dollars with python's lambda and pandas' applymap for extra jazz.

::

   def format_dollars_as_int(dollars):
       """Accepts a dollar formatted string, returns an int."""
       number = dollars.replace('$','').replace(',','')
       return int(number)

   df = pd.DataFrame(movies, columns=column_names)
   df = df.drop_duplicates(subset=['Title'])
   df[['Movie Budget','Worldwide Gross']] = df[['Movie Budget','Worldwide Gross']].astype(str).applymap(format_dollars_as_int)
   df['Movie Net Income'] = df['Worldwide Gross'] - df['Movie Budget']
   money_columns = ['Movie Budget', 'Worldwide Gross','Movie Net Income']
   df[money_columns] = df[money_columns].applymap(lambda x:'${:,}'.format(x))

**Creating a new column and writing to a .csv file**

-  Then add the IMDB ratings of our three films in a new column.
-  Finally, write the result to markdown and a csv file.

::

   # create a new column with the three movies' IMDB ratings 
   df['IMDB Rating'] = list([7.8,5.5,7.8]) 
   print(df.to_markdown(showindex=False, tablefmt='simple'))
   df.to_csv('Movies.csv', index=False)

.. image:: https://pythonmarketer.files.wordpress.com/2018/05/imdb_movies.jpeg
   :alt: IMDB_movies
   :class: alignnone size-full wp-image-2540
   :width: 870px
   :height: 117px

``print(df.Actor.value_counts().to_markdown(tablefmt="github"))``

[caption id="attachment_2539" align="alignright" width="189"]\ |actor| Count the Actors with df.Actor.value_counts()[/caption]

--------------

   **I also must mention**\ `pandas.Series.value_counts() <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html>`__\ **, because it's so darn handy :D**

--------------

**Notice for column names without spaces, you can use dot notation instead of brackets:**

``df.Actor`` *vs.* ``df['Actor']``

**Lowercase column names Python's map function:**

``df.columns = map(str.lower, df.columns)``

| **Strip whitespace from a column of strings with the**\ `pandas.Series.str <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.html>`__\ **accessor:**
| ``df['Character'] = df['Character'].astype(str).str.strip()``

**Fix pesky leading zero zip codes with**\ `str.zfill() <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.zfill.htmlhttps://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.zfill.html>`__\ **:**

``log_df['zip'] = log_df['zip'].astype(str).str.zfill(5)``

**Get a row by index number us**\ `pandas.DataFrame.loc[] <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html>`__\ **:**

::

   first_row = df.loc[0, df.columns]
   third_row = df.loc[2, df.columns]

**Filter the df to get rows where the actor is 'Julia Roberts'.**

::

   julia_roberts_movies = df[df.Actor=='Julia Roberts'].reset_index(drop=True) 
   print(julia_roberts_movies.head())

**"Get" an item from a column of lists with**\ `str.get() <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.get.html>`__\ **.**

::

   # returns first item in each cell's list into new column
   df['first_item'] = df['items'].str.get(0)

**Execute SQL-like operations between dataframes with**\ `df.merge() <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html>`__\ **.**

First, use `df.copy() <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.copy.html>`__ to create a new dataframe copy of our actors table above.  By default, df.merge() uses an inner join to merge two dfs on a common column. Let's add each film's release year from our date_df to our original actors table, with an inner join based on 'Title':

::

   actors = df.copy(deep=True)
   # slice only the columns we want to merge:
   date_df = date_df[['Title','Release Year']] 
   joined_df = actors.merge(date_df, on='Title', how='inner')
   # You can pass the number of rows to see to head. It defaults to 5.
   print(joined_df.head(10))

**Execute database queries with**\ `pd.read_sql() <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html>`__\ **.**

When the chunksize argument is passed, pd.read_sql() returns an iterator. We can use this to iterate through a database with lots of rows. When combined with DB connection libraries like `pyodbc <https://pythonmarketer.wordpress.com/2019/11/30/inserting-new-records-into-a-microsoft-access-database-with-python/>`__ or SQLAlchemy, you can process a database in chunks. In this example, it's an Access DB connection via pyodbc to process 500,000 rows per chunk. Pyodbc works on a wide range of other databases also.

   uses `pd.Series.isin() <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.isin.html>`__ to check if each email is in the DB.

::

   import pandas as pd
   import pyodbc

   emails = ['email@email.com', 'notanemail@example.com', 'gmail@gmail.com']
   connection_string = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\path_to_db\Email_DB.accb;'
   print(connection_string)
   conn = pyodbc.connect(connection_string)
   query = """
       SELECT *
       FROM   ADD_TABLE_NAME
       """
   dfs = list()
   for i, db_chunk in enumerate(pd.read_sql(query, conn, chunksize=500000)):
       emails_in_db = db_chunk[db_chunk['EmailAddress'].isin(emails)]
       dfs.append(emails_in_db)
       print(i)
   emails_in_db = pd.concat(dfs)
   emails_in_db.to_csv('DB_Email_Query_Results.csv', index=False)

..

   In case you are wondering, enumerate is a `python built-in <https://docs.python.org/3/library/functions.html>`__ for enumerating, or counting an iterable, e.g. list or generator, as you iterate through it.

**Using**\ `pd.read_clipboard(): <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_clipboard.html>`__\ **
**

::

   import pandas as pd
   clipboard_contents = pd.read_clipboard() 
   print(clipboard_contents)

**Use**\ `pd.to_clipboard() <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_clipboard.html>`__\ **to store a dataframe as clipboard text:**

::

   import pandas as pd
   truths = ['pandas is great','I love pandas','pandas changed my life']
   df = pd.DataFrame([truths], columns=['Truths'])
   df = df.to_clipboard(index=False, sep='|')
   clipboard_contents = input('Press ctrl-v ')
   print(clipboard_contents)

**Convert the clipboard contents to df with**\ `pd.DataFrame() <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html>`__\ **:**

::

   import pandas as pd 
   clipboard_contents = list(input('Press ctrl-v '))
   df = pd.DataFrame([clipboard_contents])
   print(df.head())

**If the clipboard dataframe has one column, you could**\ `squeeze <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.squeeze.html#pandas.DataFrame.squeeze>`__\ **the clipboard contents into a**\ `pd.Series <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html>`__\ **object:**

::

   import pandas as pd 
   clipboard_text = pd.read_clipboard() 
   clipboard_contents = list(clipboard_text) 
   df = pd.DataFrame([clipboard_contents], columns=['Clipboard Data'])
   clipboard_series = df.squeeze(axis='columns')
   print(type(clipboard_series))

**Inversely, consider using**\ `pandas.Series.to_frame() <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_frame.html#pandas.Series.to_frame>`__\ **to convert a Series to a dataframe:**

::

   import pandas as pd 
   clipboard_contents = pd.Series(input('Press ctrl-v '))
   df = clipboard_contents.to_frame()
   print(df.head())

(4) Turning json API responses into a dataframe with pd.json_normalize()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**For**\ `older pandas versions <https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.io.json.json_normalize.html>`__\ **:**

::

   from pandas.io.json import json_normalize
   import requests
   url = 'pseudo_API.com/endpoint/'
   parameters = {'page_size'=100, format='json', api_type='contact_sync' }
   response = requests.get(url=url, params=parameters)
   data = response.json() # decode response into json
   # turn subset of json into df
   df = json_normalize(data['any_key']) 

**Update: beginning in pandas 1.0,**\ `json_normalize <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.json_normalize.html>`__\ **became a top-level pandas namespace.**

::

   import pandas as pd
   import requests 
   url = 'pseudo_API.com/endpoint/' 
   parameters = {'page_size'=100, format='json', api_type='contact_sync' }
   response = requests.get(url=url, params=parameters)
   data = response.json() # decode response into json 
   df = pd.json_normalize(data['any_key'])

..

   pandas.json_normalize() is now exposed in the top-level namespace. Usage of json_normalize as pandas.io.json.json_normalize is now deprecated and it is recommended to use json_normalize as pandas.json_normalize() instead (GH27586).

   `What's new in pandas 1.0.0 <https://pandas.pydata.org/pandas-docs/stable/whatsnew/v1.0.0.html>`__

(5) Plotting Visualizations with matplotlib
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Make a bar plot of the movie release year counts using pandas and matplotlib formatting.**

::

   import pandas as pd
   import matplotlib.pyplot as plt
   from matplotlib.ticker import MaxNLocator
   import matplotlib.ticker as ticker

   column_names = ["Title", "Release Date", "Character", "Actor"]
   rows = [["Ocean's 11", "12/7/2001", "Danny Ocean", "George Clooney"],
   ["Ocean's 11", "12/7/2001", "Tess Ocean", "Julia Roberts"],
   ["Runaway Bride", "6/30/1999", "Ike Graham", "Richard Gere"],
   ["Runaway Bride", "6/30/1999", "Maggy Carpenter", "Julia Roberts"],
   ["Bonnie and Clyde", "9/1/1967", "Clyde Barrow", "Richard Gere"],
   ["Bonnie and Clyde", "9/1/1967", "Bonnie Parker", "Julia Roberts"]]
   df = pd.DataFrame(rows, columns=column_names)
   ax = df.Year.value_counts().plot(x='title', ylim=0, kind='bar', title='Release Year of Movies', rot=0)
   ax.yaxis.set_major_locator(MaxNLocator(integer=True))
   fig = ax.get_figure() 
   fig.tight_layout()
   fig.savefig('images/Movie_Plot.png')

Use Jupyter Notebook to show plot, and/or download plot from command line. Read more about `plotting with Jupyter/pandas/Python here <https://pythonmarketer.wordpress.com/2019/04/12/datasets-plotting-using-jupyter-pandas-and-matplotlib/>`__.

**Plot George Clooney's movies over time in a line graph. [\ `Source <https://www.youtube.com/watch?v=5JnMutdy6Fw>`__\ ]**

::

   import matplotlib.pyplot as plt
   df = df[df.Actor=='George Clooney']
   df.groupby(['Year']).size().plot(ylim=0)
   fig = ax.get_figure()
   fig.savefig('/path/to/figure.pdf')

(7) Supplementary Resources and Guides
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Popular Supporting Libraries and Tools**

-  `NumPy (Arrays and math) <https://www.numpy.org/>`__
-  `Matplotlib (Visualization) <https://matplotlib.org/#>`__
-  `Seaborn (Visualization) <https://seaborn.pydata.org/>`__
-  `Bokeh (Visualization) <https://bokeh.pydata.org/en/latest/docs/installation.html>`__
-  `Jupyter Notebook (Reproducible Sharing and Viz) <https://jupyter.org/>`__

**Supplementary Resources:**

-  `pandas from the Ground Up (Video) <https://www.youtube.com/watch?v=5JnMutdy6Fw>`__
-  `Google's Intro to pandas Jupyter Notebook <https://colab.research.google.com/drive/1a4sbKG7jOJGn4oeonQPA8XjJm7OYgcdX>`__ (Tutorial)
-  `10 Minutes to pandas (Documentation) <https://pandas.pydata.org/pandas-docs/stable/10min.html>`__
-  `Numpy's <https://docs.scipy.org/doc/numpy/reference/generated/numpy.r_.html>`__ `r and c\_ stacking helpers to concatenate arrays <https://docs.scipy.org/doc/numpy/reference/generated/numpy.r_.html>`__
-  `Calculating Taxes with pandas <http://rhodesmill.org/brandon/2014/pandas-payroll/>`__ (Blog)

.. |pandas| image:: https://pythonmarketer.files.wordpress.com/2018/05/pandas.png
   :class: wp-image-2594 alignright
   :width: 301px
   :height: 122px
   :target: https://pandas.pydata.org/
.. |pip_list| image:: http://pythonmarketer.files.wordpress.com/2018/05/d1733-pip_list-e1581434945203.jpg
   :class: alignnone wp-image-2572
   :width: 179px
   :height: 230px
.. |dates_of_movies| image:: https://pythonmarketer.files.wordpress.com/2018/05/dates_of_movies.jpg
   :class: alignnone wp-image-2537
   :width: 662px
   :height: 148px
.. |actor| image:: https://pythonmarketer.files.wordpress.com/2018/05/actor.jpg
   :class: alignnone wp-image-2539
   :width: 189px
   :height: 111px
