How I Sped Up My Python CLI By 25%
##################################
:date: 2023-10-13 17:25
:author: lofipython
:category: coding, programming, python, python performance, CLI
:tags: python CLI, python script optimization, speeding up python code
:slug: how-i-sped-up-a-python-get-request-by-25%
:status: published

I recently noticed that the `Yahoo Finance stock summary command line interface (CLI) <https://github.com/erickbytes/finsou.py>`__ I made seemed to be slowing down. Seeking to understand what was happening in my code, I remembered Python has multiple profilers available like Scalene, line_profiler, cProfile and pyinstrument. In this case, I was running my code on Python version 3.11. 

First, I tried `cProfile <https://docs.python.org/3/library/profile.html#module-cProfile>`__ from the Python standard library. It is nice to have without any install required! However, I found its output to be tough to interpret. I also remembered I liked a `I saw about Scalene <https://www.youtube.com/watch?v=5iEf-_7mM1k>`__, which gave a thorough overview of several Python profilers and how they're different. So next, I tried Scalene. Finally, I found pyinstrument and can safely say it is now my favorite Python profiler. This post will focus on how I used `pyinstrument <https://pyinstrument.readthedocs.io/en/latest/guide.html>`__ to make my command line tool faster.

**Install pyinstrument with pip**

.. code:: console

   pip install pyinstrument

I preferred the format in which pyinstrument presented the modules, functions and time they consumed in a tree structure. Scalene's percentage based diagnosis was useful also. Scalene showed the specific lines where code was bottlenecked, whereas pyinstrument showed the time spent in each module and function. I liked that I could see time of specific  functions from the external modules I was using with pyinstrument. For example, the beautiful soup and rich both consumed shockingly little time. However, the pandas module took a whole second.

I saw that just importing the pandas module and doing nothing else was taking up to and sometimes over a second each time my CLI ran. On a script that takes about four seconds to execute, one second is 25% of the total run time! Once I realized this, I decided that I could only import the pandas module if my CLI's --csv argument was given. I was only using pandas to sort stocks and write a CSV. It wasn't critical functionality for my CLI.

My CLI script accepts a stock ticker as an argument. The below command fetches a stock report from Yahoo Finance and prints to the terminal. Swapping out "python" for pyinstrument runs the script and prints a pyinstrument report to your console.

**Fetch a stock report from Yahoo.**

.. code:: console

    pyinstrument finsou.py -s GOOG
    

**pyinstrument Results With Normal Pandas Import**

**GOOG, Google**

.. image:: {static}/blog/images/goog-pandas-import.png
  :alt: profiling a Python script with pyinstrument, before with GOOG

**MSFT, Microsoft**

.. image:: {static}/blog/images/msft-pandas-import.png
  :alt: profiling a Python script with pyinstrument, before with MSFT

The line for the pandas module looks like this:

    0.946 <module>  pandas/__init__.py:1

**pyinstrument Results With Pandas Import Only If Necessary**

After changing the pandas module to only import if needed, it is no longer eating almost a second of time. As a result, the script runs about second faster each time! Below are the pyinstrument reports for two different stocks after changing my pandas import to only be called if it was actually used:

**GOOG, Google**

.. image:: {static}/blog/images/goog-no-pandas-import-fast.png
  :alt: profiling a Python script with pyinstrument, after with GOOG

**NVDA, Nvidia**
 
.. image:: {static}/blog/images/nvda-no-pandas-import.png
  :alt: profiling a Python script with pyinstrument, after with NVDA
  
**Sidebar: HTTP Request Volatility**
    
    The time that the script runs fluctuates about half a second to a few seconds based on the HTTP get request. It lags even more if my internet connection is weaker or Yahoo throttles my request because I've made too many in a short period of time. My time savings weren't gained from tinkering with the HTTP request, even though that was a time-eater. I noticed my get request tends to fluctate quite a bit and sometimes causes an extra delay. 
 
**Simplified Python Example to Achieve Speed Gains**

Below shows the method I used to achieve a faster CLI. Heads up, this code will not work if you run it. It's only meant to explain how I my code faster. You can find the actual script where I made this improvement `here on Github <https://github.com/erickbytes/finsou.py/blob/main/finsou.py>`__. 

.. code-block:: python

    import argparse
    from bs4 import BeautifulSoup
    from rich import print as rprint
    # Original import --> lazy import only if csv argument given: import pandas as pd

    parser = argparse.ArgumentParser(
        prog="finsou.py",
        description="Beautiful Financial Soup",
        epilog="fin soup... yum yum yum yum",
        )
    parser.add_argument("-s", "--stocks", help="comma sep. stocks or portfolio.txt")
    parser.add_argument("-c", "--csv", help='set csv export with "your_csv.csv"')
    args = parser.parse_args()
    prices = list()
    for stock in args.stocks:
        summary, ah_pct_change = yahoo_finance_prices(url, stock)
        rprint(f"[steel_blue]{summary}[/steel_blue]\n")
        prices.append([stock, summary, url, ah_pct_change])
    if args.csv:
        # Importing here shaves 1 second off the CLI when CSV is not required.
        import pandas as pd
        cols = ["Stock", "Price_Summary", "URL", "AH_%_Change"]
        stock_prices = pd.DataFrame(prices, columns=cols)
        stock_prices["Percent_Change"] = (
            stock_prices["AH_%_Change"]
            .str.replace("-", "")
            .str.replace("%", "")
            .str.replace("+", "")
            .apply(lambda num: Decimal(num))
        )
        moving_up = stock_prices[
            stock_prices["AH_%_Change"].str.contains("+", regex=False)
        ].sort_values(by="Percent_Change", ascending=False)
        flat = stock_prices[stock_prices["AH_%_Change"].str.contains("0.00", regex=False)]
        moving_down = stock_prices[
            stock_prices["AH_%_Change"].str.contains("-", regex=False)
        ].sort_values(by="Percent_Change", ascending=True)
        stock_prices = pd.concat([moving_up, flat, moving_down]).drop(
            "Percent_Change", axis=1
        )
        stock_prices.to_csv(args.csv, index=False)


**Make It Fast**

    "Make it work, make it better, make it fast."
    \- `Kent Beck <https://tidyfirst.substack.com/>`__

That's how I sped up my Python CLI by 25%. This method bucks the convention of keeping your import statements at the top of your script. In my case, it's a hobby project so I feel ok with making the trade-off of less readable code for a snappier CLI experience. You could also consider using the standard library csv module instead of pandas. 

**For Comparison, An import csv pyinstrument Report**

.. image:: {static}/blog/images/csv-module-import.png
  :alt: profiling an import of the Python csv module

I clocked the csv module import at 0.003 or three thousandths of a second with pyinstrument. That's insanely fast compared to pandas. I chose to make a quick fix by shifting the import but using the csv module could be a better long-term solution for speeding up your scripts.

**Supplementary Reading**

`Making a Yahoo Stock Price CLI With Python <https://lofipython.com/making-a-yahoo-stock-price-summary-cli-with-python>`__

`The Python Profilers, Python Documentation <https://docs.python.org/3/library/profile.html>`__

`Stack Overflow Thread About Slow HTTP Requests <https://stackoverflow.com/questions/62599036/python-requests-is-slow-and-takes-very-long-to-complete-http-or-https-request>`__

`An Overview of Python Profiling and Diagnostic Tools <https://lofipython.com/tools-tips-to-beat-memoryerror-in-your-python-scripts>`__