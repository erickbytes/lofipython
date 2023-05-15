Title: Create a Column of Values in Pandas with df.assign()
Date: 2022-01-07 13:12
Author: pythonmarketer
Category: pandas, programming, python
Tags: cats, data
Slug: create-a-column-of-values-in-pandas-with-df-assign
Status: published

`<!-- wp:paragraph -->`{=html}

[Pandas](https://pandas.pydata.org/docs/) is amazing, what else is there to say? Learning the nuances of its API have yielded tons of times where it helped me get stuff done.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

I recently picked up the [pandas dataframe's "assign" function](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html) for creating a new column of values. This is an elegant way to set a column of values in tabular data with the pandas library. Below you'll see two ways to set a column of values in pandas. In the first way, I am chaining two assign functions together to create 2 new columns, "sound" and "type". I prefer using assign because it looks better and it does not result in any warnings from pandas. Highly recommend getting familiar with pandas functions like assign and API nuances like [Series accessors](https://pandas.pydata.org/docs/reference/series.html?highlight=str%20accessors#accessors) to up your tabular data game.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
import pandas as pd
cats = ["Garfield","Meowth","Tom"]
df = pd.DataFrame([cats], columns=["cats"])
# best way
df = df.assign(sound="Meow").assign(type="Cartoon")
print(df.head())

# alternative way that also works, but with warnings from pandas
# df["sound"] = "Meow"
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:quote -->`{=html}

> `<!-- wp:paragraph -->`{=html}
>
> DataFrame.assign : Can evaluate an expression or function to create new  
> values for a column.
>
> `<!-- /wp:paragraph -->`{=html}`<cite>`{=html}- [pandas source code](https://github.com/pandas-dev/pandas/blob/v1.3.5/pandas/core/frame.py#L4421-L4487)`</cite>`{=html}

`<!-- /wp:quote -->`{=html}

`<!-- wp:paragraph -->`{=html}

`<!-- /wp:paragraph -->`{=html}
