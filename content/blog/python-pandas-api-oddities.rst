Python Pandas API Oddities
##########################
:date: 2024-01-15 17:41
:author: lofipython
:category: coding, programming, python, pandas
:tags: pandas api, using pandas in Python, working with data, how to use pandas, reading HTML with pandas, reading pandas memory usage
:slug: python-pandas-api-oddities
:status: published

Below I've highlighted some niche functions in Python's pandas library. I've plucked
a few examples from the pandas documentation and the
`Delta Airlines Airports Wikipedia HTML table <https://en.wikipedia.org/wiki/List_of_Delta_Air_Lines_destinations>`__
for sample data. This post is aimed at the more advanced stuff on the fringes of the pandas docs.
Here are some oddities of the less traveled parts of the pandas documentation.
You never know what you'll find there, it's always evolving.

**Install pandas + lxml**

Install Python dependencies with pip: pandas and lxml, required for read_html()

::

   python3.12 -m pip install pandas
   python3.12 -m pip install lxml

**What's Not Mentioned Here**

I skipped the standard must know functions like `pd.read_csv() <https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html>`__,
pd.read_excel(), pd.DataFrame.to_csv(), `pd.DataFrame.to_json() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html>`__
and so on. The documentation on these functions is extensive. I recommend checking
out all the ways you can customize behavior of your data with their arguments.


**pd.DataFrame.__dataframe__() + pd.api.interchange.from_dataframe()**

Import a DataFrame from another library via the DataFrame interchange protocol.
The .__dataframe__() dunder method returns an interchange object which can be used to
convert another dialect of dataframe to pandas. If the protocol is supported,
a dataframe interchange object has the methods "column_names" and "select_columns_by_name".
If you're dealing with a flavor of dataframe other than pandas, keep in mind it may support
the DataFrame interchange protocol. `Pandas Interchange Object Documentation <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.api.interchange.from_dataframe.html#pandas.api.interchange.from_dataframe>`__

.. code-block:: python

  import pandas as pd

  df_not_necessarily_pandas = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
  interchange_object = df_not_necessarily_pandas.__dataframe__()
  df_pandas = (pd.api.interchange.from_dataframe
             (interchange_object.select_columns_by_name(['A'])))


::

  >>> df_pandas

       A
  0    1
  1    2

  >>> interchange_object.column_names()

  Index(['A', 'B'], dtype='object')


.. image:: {static}/images/pandasdataframeinterchangeprotocol.png
 :alt: interchange dataframes between libraries


**pd.read_html(url)**

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


**pd.DataFrame.to_html()**

This function returns your tabular data as an HTML string.
df.head() accepts a number and returns a df with that many records, in this case 2.
`to_html() Documentation <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_html.html>`__

.. code-block:: python

   html = airports.head(2).to_html(index=False)
   print(html)

::

  <table border="1" class="dataframe">
    <thead>
      <tr style="text-align: right;">
        <th>Country / Territory</th>
        <th>City</th>
        <th>Airport</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Antigua and Barbuda</td>
        <td>Osbourn</td>
        <td>V. C. Bird International Airport</td>
        <td>Seasonal</td>
      </tr>
      <tr>
        <td>Argentina</td>
        <td>Buenos Aires</td>
        <td>Ministro Pistarini International Airport</td>
        <td></td>
      </tr>
    </tbody>
  </table>


.. image:: {static}/images/htmltable.png
 :alt: example pandas HTML table


**pd.DataFrame.memory_usage()**

Returns the memory usage of each column in bytes. Per the docs, "this value is displayed in DataFrame.info by default."
`.memory_usage() Documentation <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.memory_usage.html>`__

.. code-block:: python

  # To include memory footprint of object dtypes, pass deep=True.
  print(airports.memory_usage(deep=True))

::

  Index                    132
  Country / Territory    24125
  City                   21164
  Airport                30660
  Notes                  19237
  dtype: int64


.. code-block:: python


  def readable_format(size: int) -> str:
      """Converts a bytes integer to a human-readable format.

      Args:
          size (int): The bytes integer to convert.

      Returns:
          str: The human-readable format of the bytes integer.
      """
      for unit in ["B", "KB", "MB", "GB", "TB"]:
          if size < 1024:
              return f"{size:.2f} {unit}"
          size /= 1024
      return f"{size:.2f} PB"

  # Use pd.Series.apply() to convert bytes to "human readable" data format.
  memory_usage = airports.memory_usage(deep=True).apply(readable_format)
  print(memory_usage)

::

  Index                  132.00 B
  Country / Territory    23.56 KB
  City                   20.67 KB
  Airport                29.94 KB
  Notes                  18.79 KB
  dtype: object

**pd.DataFrame.empty**

Every pandas DataFrame has a ".empty" attribute. If Series/DataFrame is empty,
returns True, if not returns False. `.empty Documentation <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.empty.html>`__

.. code-block:: python

  print(airports.empty)
  # False
  if airports.empty:
      print("DataFrame has no data.")
  else:
      print("DataFrame contains data.")
  # DataFrame contains data.

**pd.DataFrame.T**

Every pandas DataFrame has a ".T" attribute. It returns the transposed version
of the DataFrame. `.T Documentation <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.T.html#pandas.DataFrame.T>`__

::

  >>> airports.head(3).T

::

    0                                         1                                    2
  Country / Territory               Antigua and Barbuda                                 Argentina                                Aruba
  City                                          Osbourn                              Buenos Aires                           Oranjestad
  Airport              V. C. Bird International Airport  Ministro Pistarini International Airport  Queen Beatrix International Airport
  Notes                                        Seasonal

**pd.DataFrame.convert_dtypes() + .infer_objects()**

These are 2 functions for swiftly handling data types in your tabular data.
Note: these are alternatives to the `"astype()" function <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.astype.html>`__, which is used more commonly.
Use astype() to set a column or dataframe to a specific dtype. Use infer_objects() to
infer more suitable types for object columns. Use convert_dtypes to let pandas choose the best possible dtype.


.. code-block:: python

   print(airports.head())
   print(airports.dtypes)

   # Convert columns to the best possible dtypes using dtypes supporting pd.NA.
   typed_df = airports.convert_dtypes()
   print(typed_df.dtypes)

   # Attempt to infer better dtypes for object columns.
   inferred_df = airports.infer_objects()
   print(inferred_df.dtypes)

::

  >>> airports.head()
    Country / Territory          City                                   Airport       Notes
  0  Antigua and Barbuda       Osbourn          V. C. Bird International Airport    Seasonal
  1            Argentina  Buenos Aires  Ministro Pistarini International Airport
  2                Aruba    Oranjestad       Queen Beatrix International Airport
  3            Australia        Sydney                            Sydney Airport
  4              Austria        Vienna              Vienna International Airport  Terminated

  >>> airports.dtypes
  Country / Territory    object
  City                   object
  Airport                object
  Notes                  object
  dtype: object

  >>> typed_df.dtypes
  Country / Territory    string[python]
  City                   string[python]
  Airport                string[python]
  Notes                  string[python]
  dtype: object

  >>> inferred_df.dtypes
  Country / Territory    object
  City                   object
  Airport                object
  Notes                  object
  dtype: object


`convert_dtypes Documentation <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.convert_dtypes.html>`__
+ `infer_objects() Documentation <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.convert_dtypes.html>`__

**pd.Series.str.get(index)**

str.get() is available via the pandas Series string accessor.
This function is useful when your dataset contains a column holding a list in each cell.
It also works on strings by returning the character at the index of a string.
You can pass an index and that value will be returned for each cell in a column.
`str.get() Documentation <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.get.html#pandas-series-str-get>`__


.. code-block:: python

  import pandas as pd

  s = pd.Series(
      ["String", (1, 2, 3), ["a", "b", "c"], 123, -456, {1: "Hello", "2": "World"}]
  )
  new_column = s.str.get(1)
  print(new_column)

::

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



**Pique Your Curiosity With Pandas**

Now you know a few of my favorite pandas API oddities. It's always time
well spent reading the `Pandas API documentation <https://pandas.pydata.org/>`__.
Check out `this other post I wrote about pandas <https://lofipython.com/pandas-pythons-excel-powerhouse>`__
for a deeper dive into this powerful Python module.
