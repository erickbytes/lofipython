Title: Pick Stocks Intelligently with ffn
Date: 2021-01-16 23:21
Author: pythonmarketer
Category: investing
Tags: money, personal finance, python, stock formulas, stocks
Slug: pick-stocks-like-a-pro-with-ffn
Status: published

`<!-- wp:paragraph -->`{=html}

**How do you calculate stock valuation metrics like [Sharpe ratio](https://www.investopedia.com/terms/s/sharperatio.asp)?**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

Recently I've been reading about common [stock valuation metrics](https://www.suredividend.com/ratios-metrics/) and wondered how I can apply them to my stock portfolio. I started reading about different metrics, sketching formulas and entertained writing a script to calculate these metrics. But Python has no shortage of finance-related libraries. After some furious googling I found [ffn](https://github.com/pmorissette/ffn), a way better option than rolling my own formulas. It's a "financial function" library, installable with pip.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

It will be interesting to observe how these metrics vary in my portfolio and learn more of [ffn's API](http://pmorissette.github.io/ffn/ffn.html). I like that they use [pandas dataframes](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) within their library because I'm already familiar with them. At minimum, it's good to understand what stock formulas purport to measure and what it means if the measure is low or high. It makes sense to compare stocks in similar industries or competitors like [NKE](https://finance.yahoo.com/quote/NKE/) and [ADDYY](https://finance.yahoo.com/quote/ADDYY?p=ADDYY&.tsrc=fin-srch). This is a neat tool for stock nerds who want to level up their stock analysis, make smart decisions and ideally pad the portfolio!

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

The funny thing is... my lowest university grade was a "C" in my only Finance class. It wasn't easy for me to grasp. But with Python it's a little more interesting and easier to apply. Anyone can level up their finance skills thanks to a cornucopia of finance calculation libraries in the Python ecosystem.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

Recommended Reading: [A Brief Introduction - ffn documentation](https://pmorissette.github.io/ffn/index.html#a-brief-introduction)

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Install ffn with pip:**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

`python -m pip install ffn`

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

Here's the code to get stock data with [ffn](https://pmorissette.github.io/ffn/quick.html):

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:code -->`{=html}

``` wp-block-code
import ffn

# ffn.get returns a pandas dataframe of market data.
data = ffn.get(
    'tsla,spot,nflx,nke,addyy', 
    start='2019-01-01', 
    end='2020-12-31'
)
print(data.head()) 
stats = data.calc_stats()
print(stats.display())
```

`<!-- /wp:code -->`{=html}

`<!-- wp:image {"id":5165,"sizeSlug":"large","linkDestination":"none"} -->`{=html}

![](https://pythonmarketer.files.wordpress.com/2021/01/2019-2020-top-stock.jpg?w=794){.wp-image-5165}

`<!-- /wp:image -->`{=html}

`<!-- wp:paragraph -->`{=html}

**side note on the pyfolio library**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

I first considered using pyfolio to pull stock data. It is not "out of the box" ready per se to deliver the results pictured in their ["single stock" example](https://pythonmarketer.wordpress.com/2021/01/16/pick-stocks-like-a-pro-with-pyfolio/) documentation. You'd need to find another way to fetch your market data or somehow patch the Yahoo Finance API within pyfolio. I preferred [ffn](http://pmorissette.github.io/ffn/quick.html), mostly because it worked right away after pip installing it and running the above code.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**2023 Update:** ffn and pyfolio depend on the Yahoo Finance API, which changes sometimes break these libraries. Troubleshooting traceback errors may be required.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Try these other Python financial analysis libraries:**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[Best Python Libraries/Packages for Finance and Financial Data Scientists](https://financetrain.com/best-python-librariespackages-finance-financial-data-scientists/)

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[python's built-in statistics module](https://docs.python.org/3/library/statistics.html) - [Backtrader](https://github.com/mementum/backtrader)

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[tia: Toolkit for integration and analysis](https://github.com/bpsmith/tia) - [FinTA (Financial Technical Analysis)](https://github.com/peerchemist/finta)

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[pandas-datareader](https://pydata.github.io/pandas-datareader/index.html) - [mplfinance](https://github.com/matplotlib/mplfinance#usage) - [PyPortfolioOpt](https://github.com/robertmartin8/PyPortfolioOpt) - [TA-Lib Python Port](https://github.com/mrjbq7/ta-lib)

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[finsou.py](https://github.com/erickbytes/finsou.py) (CLI written by me)

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

see more: [awesome-quant](https://github.com/wilsonfreitas/awesome-quant)[](https://github.com/bpsmith/tia#overview)

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:image {"id":5037,"sizeSlug":"large","linkDestination":"none"} -->`{=html}

![Image credit, ActiveState: https://www.activestate.com/blog/top-10-python-packages-for-finance-and-financial-modeling/](https://pythonmarketer.files.wordpress.com/2021/01/top10financepackages-1200x675-1.png?w=1024){.wp-image-5037}

`<!-- /wp:image -->`{=html}
