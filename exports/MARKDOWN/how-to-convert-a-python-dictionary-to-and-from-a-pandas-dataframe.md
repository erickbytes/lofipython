Title: How to Convert a Python Dictionary to and from a pandas DataFrame
Date: 2022-02-09 23:16
Author: pythonmarketer
Category: coding, pandas, programming, python
Tags: pandas df to Python dict, Python data structure conversion, Python dict to pandas df
Slug: how-to-convert-a-python-dictionary-to-and-from-a-pandas-dataframe
Status: published

`<!-- wp:paragraph -->`{=html}

This is an example of how to cast a Python dict into a dataframe and vice versa. I picked up the df to dict part from this [Python and R tips post](https://cmdlinetips.com/2021/04/convert-two-column-values-from-pandas-dataframe-to-a-dictionary/#:~:text=Another%20approach%20to%20convert%20two,all%20columns%20in%20the%20dataframe.) and the dict to df part from a [Stack Overflow post](https://stackoverflow.com/questions/18837262/convert-python-dict-into-a-dataframe). The below adaptation begins by converting an "NFL quarterbacks" Python dictionary into a dataframe and then back into a dict.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

Sometimes a dictionary is adequate to solve a problem with handy methods like get() and [items()](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques). You can also do a ton with a [dict comprehension](https://www.python.org/dev/peps/pep-0274/). When more complex tabular data operations are needed, the pandas pd.DataFrame class is well equipped for the job. Dictionaries and dataframes are delightfully interoperable, like Tom Brady and any football team on the planet.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:syntaxhighlighter/code {"language":"python"} -->`{=html}

``` wp-block-syntaxhighlighter-code
import pprint
import pandas as pd

qbs_dict = {
    "Matthew Stafford":"Los Angeles Rams",
    "Joe Burrow":"Cincinnati Bengals",
    "Tom Brady":"Tampa Bay Buccaneers",
    "Pat Mahomes":"Kansas City Chiefs",
    "Tony Romo":"Dallas Cowboys"
}
qbs_df = pd.DataFrame(qbs_dict.items(), columns=["name", "team"])
print(qbs_df.info())
qbs_dict = pd.Series(qbs_df.team.values, index=qbs_df.name.values).to_dict()
pprint.pprint(qbs_dict, sort_dicts=True)
print(qbs_dict.get("Tom Brady", "Name not found."))
```

`<!-- /wp:syntaxhighlighter/code -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Terminal Output**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:syntaxhighlighter/code -->`{=html}

``` wp-block-syntaxhighlighter-code
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   name    5 non-null      object
 1   team    5 non-null      object
dtypes: object(2)
memory usage: 208.0+ bytes
None

{'Joe Burrow': 'Cincinnati Bengals',
 'Matthew Stafford': 'Los Angeles Rams',
 'Pat Mahomes': 'Kansas City Chiefs',
 'Tom Brady': 'Tampa Bay Buccaneers',
 'Tony Romo': 'Dallas Cowboys'}

Tampa Bay Buccaneers
```

`<!-- /wp:syntaxhighlighter/code -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Did you notice that pprint sorts dicts by default?**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

Here the printed dict is reordered alphabetically on the QB's names. Per the pprint docs, you can alter this behavior if desired via a keyword argument new in Python version 3.8:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:syntaxhighlighter/code {"language":"python"} -->`{=html}

``` wp-block-syntaxhighlighter-code
pprint.pprint(qbs_dict, sort_dicts=False)
```

`<!-- /wp:syntaxhighlighter/code -->`{=html}

`<!-- wp:paragraph -->`{=html}

**pandas** **Documentation**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[pandas installation documentation](https://pandas.pydata.org/docs/getting_started/install.html)

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[pandas.DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[pandas.Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[pandas.DataFrame.to_dict](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html)

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[pandas.DataFrame.info](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html)

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Python Standard Library Documentation**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[pprint.pprint](https://docs.python.org/3/library/pprint.html#pprint.pprint)

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[dict](https://docs.python.org/3/library/stdtypes.html?highlight=dict#mapping-types-dict)

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[dict.get](https://docs.python.org/3/library/stdtypes.html#dict.get)

`<!-- /wp:paragraph -->`{=html}
