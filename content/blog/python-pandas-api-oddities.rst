Python Pandas API Oddities
##########################
:date: 2024-01-15 17:41
:author: lofipython
:category: coding, programming, python, pandas
:tags: pandas api, using pandas in Python, working with data, how to use pandas, reading HTML with pandas, reading pandas memory usage
:slug: python-pandas-api-oddities
:status: published

This post uses the `Delta Airlines Airports Wikipedia HTML table <https://en.wikipedia.org/wiki/List_of_Delta_Air_Lines_destinations>`__
as an example to highlight some niche functions in Python's pandas library.
I skipped the standard must know functions like pd.read_csv() and pd.read_excel().
I use those all the time. This is aimed at the more advanced stuff on the fringes of the docs.
Here are some oddities of the less traveled parts of the pandas documentation.
You never know what you'll find there, it's always evolving.

**Install Python dependencies: pandas and lxml, required for read_html()**

.. code:: console

   python3.12 -m pip install pandas
   python3.12 -m pip install lxml


**Import a DataFrame From Another Library Using the DataFrame Interchange Standard.**

Keep in mind that a DataFrame standard exists and is supported across the Python ecosystem.

.. code-block:: python

  import pandas as pd
  df_not_necessarily_pandas = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
  interchange_object = df_not_necessarily_pandas.__dataframe__()


.. image:: {static}/images/pandasdataframeinterchangeprotocol.png
 :alt: interchange dataframes between libraries


`Pandas Interchange Object Documentation <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.api.interchange.from_dataframe.html#pandas.api.interchange.from_dataframe>`__

**pandas.read_html(url)**

pd.read_html() accepts a website url. It returns a list of all HTML tables
as DataFrames. After getting the table as a dataframe, use ".drop()" to drop a column and ".fillna()"
to fill NA values as blanks. `read_html() Documentation <https://pandas.pydata.org/docs/reference/api/pandas.read_html.html>`__


.. code-block:: python

  import pandas as pd

  url = "https://en.wikipedia.org/wiki/List_of_Delta_Air_Lines_destinations"
  airports = pd.read_html(url)[0]
  # Drop the irrelevant "Refs" column and fill nans blank.
  airports = airports.drop("Refs", axis=1).fillna("")
  print(airports.head())


**pandas.DataFrame.to_html()**

This function returns your tabular data as an HTML string.
df.head() accepts a number and returns a df with that many records, in this case 2.
`to_html() Documentation <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_html.html>`__

.. code-block:: python

   html = airports.head(2).to_html()
   print(html)


::

  <table border="1" class="dataframe">
   <thead>
     <tr style="text-align: right;">
       <th></th>
       <th>Country / Territory</th>
       <th>City</th>
       <th>Airport</th>
       <th>Notes</th>
     </tr>
   </thead>
   <tbody>
     <tr>
       <th>0</th>
       <td>Antigua and Barbuda</td>
       <td>Osbourn</td>
       <td>V. C. Bird International Airport</td>
       <td>Seasonal</td>
     </tr>
     <tr>
       <th>1</th>
       <td>Argentina</td>
       <td>Buenos Aires</td>
       <td>Ministro Pistarini International Airport</td>
       <td></td>
     </tr>
   </tbody>
  </table>


**pandas.DataFrame.memory_usage()**

Returns the memory usage of each column in bytes. `.memory_usage() Documentation <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.memory_usage.html>`__

.. code-block:: python

  print(airports.memory_usage())

.. code-block:: console

  >>> airports.memory_usage()

  Index                   132
  Country / Territory    2904
  City                   2904
  Airport                2904
  Notes                  2904
  dtype: int64


**pandas.DataFrame.empty**

Every pandas DataFrame has a ".empty" attribute. If Series/DataFrame is empty,
returns True, if not returns False. `.empty Documentation <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.empty.html>`__

.. code-block:: python

  print(airports.empty)
  # False

**pandas.DataFrame.T**

Every pandas DataFrame has a ".T" attribute. It returns the transposed version
of the DataFrame. `.T Documentation <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.T.html#pandas.DataFrame.T>`__

.. code-block:: python

  >>> airports.head(2).T

.. code-block:: console

    0                                         1                                    2
  Country / Territory               Antigua and Barbuda                                 Argentina                                Aruba
  City                                          Osbourn                              Buenos Aires                           Oranjestad
  Airport              V. C. Bird International Airport  Ministro Pistarini International Airport  Queen Beatrix International Airport
  Notes                                        Seasonal


**pandas.Series.str.get(index)**

str.get() is available via the pandas Series string accessor.
This function is useful when your dataset contains a column holding a list in each cell.
You can pass an index and that value will be returned for each cell in a column.
`str.get() Documentation <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.get.html#pandas-series-str-get>`__


.. code-block:: python

  import pandas as pd

  s = pd.Series(
      ["String", (1, 2, 3), ["a", "b", "c"], 123, -456, {1: "Hello", "2": "World"}]
  )
  new_column = s.str.get(1)
  print(new_column)

.. code-block:: console

  >>> s
  0                        String
  1                     (1, 2, 3)
  2                     [a, b, c]
  3                           123
  4                          -456
  5    {1: 'Hello', '2': 'World'}
  dtype: object

  >>> s.str.get(1)
  0        t
  1        2
  2        b
  3      NaN
  4      NaN
  5    Hello
  dtype: object


**pandas.DataFrame.convert_dtypes() and .infer_objects()**

These are 2 functions for swiftly handling data types in your tabular data.
Note: these are alternatives to the `"astype()" function <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.astype.html>`__, which is used more commonly.

.. code-block:: python

   import pandas as pd

   df = pd.DataFrame([["1234", "5678", ""]])
   print(df.head())
   print(df.dtypes)
   # Use pandas to coerce data to default types.
   typed_df = df.convert_dtypes()
   # Coerce data back to object types.
   objects_df = typed_df.infer_objects()
   print(converted_df.dtypes)
   print(objects_df.dtypes)

.. code-block:: console

  >>> df.head()
    0     1    2
  0  1234  5678  abc

  >>> df.dtypes
  0    object
  1    object
  2    object

  >>> converted_df.dtypes
  0    string[python]
  1    string[python]
  2    string[python]
  dtype: object

  >>> objects_df.dtypes
  0    object
  1    object
  2    object
  dtype: object


`convert_dtypes Documentation <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.convert_dtypes.html>`__
+ `infer_objects() Documentation <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.convert_dtypes.html>`__


**Pique Your Curiosity With Pandas**

Now you know a few of my favorite pandas API oddities. It's always time
well spent reading the `Pandas API documentation <https://pandas.pydata.org/>`__.
Check out `this other post I wrote about pandas <https://lofipython.com/pandas-pythons-excel-powerhouse>`__
for a deeper dive into this powerful Python module.
