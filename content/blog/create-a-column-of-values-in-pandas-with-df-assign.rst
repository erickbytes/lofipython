Create a Column of Values in Pandas with df.assign()
####################################################
:date: 2022-01-07 13:12
:author: pythonmarketer
:category: pandas, programming, python
:tags: cats, data
:slug: create-a-column-of-values-in-pandas-with-df-assign
:status: published

`Pandas <https://pandas.pydata.org/docs/>`__ is amazing, what else is there to say? Learning the nuances of its API have yielded tons of times where it helped me get stuff done.

I recently picked up the `pandas dataframe's "assign" function <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html>`__ for creating a new column of values. This is an elegant way to set a column of values in tabular data with the pandas library. Below you'll see two ways to set a column of values in pandas. In the first way, I am chaining two assign functions together to create 2 new columns, "sound" and "type". I prefer using assign because it looks better and it does not result in any warnings from pandas. Highly recommend getting familiar with pandas functions like assign and API nuances like `Series accessors <https://pandas.pydata.org/docs/reference/series.html?highlight=str%20accessors#accessors>`__ to up your tabular data game.

.. code-block:: python

   import pandas as pd
   cats = ["Garfield","Meowth","Tom"]
   df = pd.DataFrame([cats], columns=["cats"])
   # best way
   df = df.assign(sound="Meow").assign(type="Cartoon")
   print(df.head())

   # alternative way that also works, but with warnings from pandas
   # df["sound"] = "Meow"


DataFrame.assign : Can evaluate an expression or function to create new values for a column.
pandas source code: https://github.com/pandas-dev/pandas/blob/v1.3.5/pandas/core/frame.py#L4421-L4487
