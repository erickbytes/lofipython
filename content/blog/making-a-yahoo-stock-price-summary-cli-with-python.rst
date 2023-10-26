Making a Yahoo Stock Price Summary CLI with Python
##################################################
:date: 2023-10-10 18:56
:author: lofipython
:category: coding, programming, python, stocks, CLI
:tags: stock prices command line, python CLI, python investing research
:slug: making-a-yahoo-stock-price-summary-cli-with-python
:status: published

Over the past few years, I found a few different external Python libraries that relied on a broken `Yahoo Finance <https://finance.yahoo.com/>`__ API. Apparently, the API changes frequently, leaving us developers in a tough spot troubleshooting tracebacks in order to get stock data. I wanted to check my stocks' prices from the terminal. 6 months ago, dealing with these frustrations inspired me to begin making a Python command line interface (CLI) to fetch stock info directly from the Yahoo Finance website. 

With an idea and curiosity to see if I could make it work, I reached for the beautifulsoup4 library, the de facto HTML parser in Python. It turned out way better than I envisioned when I started. The CLI is working great, barring any changes to Yahoo's stock page HTML or CSS code. It accepts a stock ticker and grabs stock price data from the Yahoo website in your terminal. It is designed to monitor daily moves of stocks, including after hours prices.

Here is `the Github repo with the code <https://github.com/erickbytes/finsou.py>`__. I've named the CLI finsou.py, which I've been pronouncing to myself as "finsoupy", a word play on fin soup, short for financial soup. The standard library `argparse module <https://docs.python.org/3/library/argparse.html>`__ provided the CLI argument ingesting functionality. The CLI uses `the requests module <https://pypi.org/project/requests/>`__, `beautifulsoup4 <https://pypi.org/project/beautifulsoup4/>`__ and `re <https://docs.python.org/3/library/re.html>`__ modules. With these 3 modules, it retrieves stock info and organizes it into a tidy, color coded report that is printed to your console. After getting the essential functionality working, I added improvements like the `rich module <https://github.com/Textualize/rich>`__ to add in terminal color formatting and `tqdm <https://github.com/tqdm/tqdm>`__ for a progress bar.

The CLI currently works after the US stock market has closed normal market hours. Additionally, after hours prices for "over the counter" (OTC) traded stocks are not listed on Yahoo so an error is returned for those stocks.

**Getting Started with finsou.py**

1. First, install the necessary Python library dependencies:

.. code:: console

    pip install beautifulsoup4
    pip install pandas
    pip install requests
    pip install rich
    pip install tqdm


2. Next, clone the Github repo:

.. code:: console

    git clone https://github.com/erickbytes/finsou.py.git

3. Change directory into the finsou.py folder that contains the Python script:

.. code:: console

    cd finsou.py

4. Query a stock's daily price summary:

.. code:: console
    
    # Print a daily stock summary for Virgin Galactic (SPCE).
    python finsou.py -s SPCE


.. image:: {static}/images/finsoupy-stock-summary.png
  :alt: example stock summary report

**Fetch a stock summary for multiple companies.**

.. code:: console

    # Summarize a list of stocks.
    python finsou.py -s BABA,SPOT,KO


**Read a list of stocks from a .txt file.**

.. code:: console

    # Read a list of stocks from a text file with one ticker on each line.
    python finsou.py -s portfolio.txt -c "Portfolio Prices.csv"


**Research + download media from investor relations websites.**

Note: currently the code needs to be modified depending on the HTML structure of the page.

.. code:: console

    # Note: this is experimental and results will vary. URLs are typically buried in nested span and div tags.
    python finsou.py -s GRAB -r https://investors.grab.com/events-and-presentations


**How It Works**

Check out the `finsou.py Python script <https://github.com/erickbytes/finsou.py/blob/main/finsou.py>`__ to see the complete code for how this stock report is created. Here is a brief simplified example of the logic behind the code. 


.. code-block:: python
    
    import re
    import requests
    from bs4 import BeautifulSoup
    
    stock = "SNOW"
    url = f"https://finance.yahoo.com/quote/{stock}/"
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/43.0.845.0 Safari/534.1"
    headers = {
        "Cache-Control": "no-cache",
        "User-Agent": user_agent,
    }
    page = requests.get(url, headers=headers).text
    soup = BeautifulSoup(page, "html.parser")
    price_tags = soup.find_all(
        class_=re.compile("Fw\(b\) Fz\(36px\) Mb\(\-4px\) D\(ib\)")
    )
    mkt_close_price = price_tags[0].string.replace(",", "")
    print(mkt_close_price)


First, an HTTP request is made and parsed by beautiful soup using Python's html.parser. We can then use bs4 and regex's `re.compile function <https://docs.python.org/3/library/re.html#re.compile>`__ to return the HTML tags with a specific CSS class. Then once we have the tags, beautiful soup gives us a ".string" attribute for each tag to return their contents as a string. This pattern was applied to return all of the data in the stock report. To find the css classes I wanted, I right-clicked the price or data on Yahoo's website in a Chrome browser and selected "Inspect". Doing this opens Chrome's developer tools and drops you into that spot in the HTML code, where you can find the class you want to target.


**No Official API, No Problem**

It felt good to prove the concept that you don't need an official API to print stock data in your terminal! If you want to check in on your portfolio's daily moves, give this CLI a try. 

`finsou.py Github Repo <https://github.com/erickbytes/finsou.py>`__

