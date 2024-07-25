Importing and Analyzing Data With Google Sheets Functions
##########################################################
:date: 2024-07-25 16:00
:author: lofipython
:category: spreadsheets, data analysis, google sheets
:tags: google sheets, data wrangling, speadsheet data import
:slug: import-analyze-data-with-google-sheets-functions
:status: published

This post focuses on Google Sheets formulas, rather than Python. If you're interested in accessing Google Sheets with Python,
check out this `post I wrote about the pygsheets library <https:/lofipython.com/copying-a-csv-file-to-google-sheets-with-pygsheets>`__. I haven't personally tried it, but 
`xlwings <https://www.xlwings.org/blog/python-for-google-sheets>`__ also looks like a decent option if you're looking for Google Sheets Python libraries.

Here are some functions I recently discovered to analyze data in Sheets. There a few different strategies you can use to import data into Google Sheets with the functions available. 
Below, you'll see some different approaches you use to get data into Google Sheets and then analyze it. The Google Sheets formulas rabbit hole is deep.
Lots of power can be harnessed by getting familiar with the formulas it has built-in.

**Year To Date SPARKLINE of a Stock**
::

   =SPARKLINE(GOOGLEFINANCE("Nasdaq:NVDA", "price", DATE(YEAR(TODAY()), 1, 1), TODAY(), "daily"), {"charttype", "line"; "linewidth", 2; "color", "green"})


**Year to Date SPARKLINE of USD to MXN Currency Value with GOOGLEFINANCE + SPARKLINE USING IF to Dynamically Color the SPARKLINE**
::

   =SPARKLINE(GOOGLEFINANCE("CURRENCY:USDMXN", "price", TODAY()-365, TODAY(), "DAILY"), {"charttype", "line"; "linewidth", 2; "color", if(P22>0,"green","red")})


Note the use of an if condition to check another cell and set the color to green if > 0 or red if < 0.

.. image:: {static}/images/sparkline-example.png
  :alt: Applying Google Sheets Sparklines


**Market Cap with GOOOGLEFINANCE**
::

   =GOOGLEFINANCE("Nasdaq:NVDA", "marketcap")


**Price/Earnings Ratio**
::

   =GOOGLEFINANCE("Nasdaq:MSFT", "pe")


**Daily % Change of a Stock**
::
   
   =GOOGLEFINANCE("Nasdaq:TSLA","changepct") &"%"


**Import the Price of a Cryptocurrency with IMPORTDATA**
::
   
   =IMPORTDATA("https://cryptoprices.cc/ADA")

This function imports the price of Cardano cryptocurrency from cryptoprices.cc.

**Import the Market Cap of a Cryptocurrency with IMPORTDATA**
::

   =IMPORTDATA("https://cryptoprices.cc/ADA/MCAP")

This function imports the current market cap of Cardano cryptocurrency.


**Import the Daily % Change of Ethereum Cryptocurrency with IMPORTXML and INDEX**
::

   =IF(
   INDEX(IMPORTXML("https://coinmarketcap.com/currencies/ethereum/", "//p[contains(@class, 'sc-71024e3e-0 sc-58c82cf9-1 ihXFUo iPawMI')]/@data-change"), 1) = "down",
   "-" & VALUE(SUBSTITUTE(IMPORTXML("https://coinmarketcap.com/currencies/ethereum/", "//div[contains(@class, 'sc-65e7f566-0 gCtSWR')]"), "(1d)", ""))*100&"%",
   VALUE(SUBSTITUTE(IMPORTXML("https://coinmarketcap.com/currencies/ethereum/", "//div[contains(@class, 'sc-65e7f566-0 gCtSWR')]"), "(1d)", ""))*100&"%"
   )

This method uses IMPORTXML to import data to google sheets by passing an "xpath query". The first line checks if the direction of the % change is "down". If it is down,
then we know the % change is negative, otherwise the % change is positive. In this case I inspected the source code of coinmarketcap to reference the class names of the HTML I was targeting.


**Conditionally sum a range with SUMIFS, SUMIF and COUNTIF**

::

   =SUMIFS('sheet_name'!G:G, 'sheet_name'!N:N, ">0")


In the following examples, "sheet_name" = Your Google sheet's name. This function sums the corresponding cells in column N if column G contains a number greater than 0.

::

   =SUMIF('sheet_name'!N:N, "Some Value",'sheet_name'!G:G)


This function sums all values in column G if the values in column N are equal to "Some Value".

::

   =COUNTIF('sheet_name'!A:A, "Some Value")

Count all the cells in column A that equal "Some Value".

**Select Columns from a Dataset**
::

   { 'sheet_name'!A:D, 'sheet_name'!T:X, 'sheet_name'!Z:AA}

Google sheets recognizes this format of bracket enclosed ranges of columns to select into your dataset. In the next example, you can see this applied.


**Conditionally Select a Range of Cells from a Dataset with SORTN, FILTER, and REGEXMATCH**

::

   =SORTN(FILTER({'sheet_name'!A:A, 'sheet_name'!E:E, 'sheet_name'!P:P/1,'sheet_name'!F:F}, REGEXMATCH('sheet_name'!P:P, "-")), 5, 0, 3, TRUE)


This formula constructs a dataset, then filters it on a condition using REGEXMATCH to check if the cell contains a hyphen (-). 
5 specifies how many rows to return, and 3 specifies which column to sort on, in this case the 3rd column.

**Conditionally Select a Range of Cells from a Dataset with SORTN and QUERY with SQL-Like Language**
::

   =SORTN(QUERY({'sheet_name'!A:A, 'sheet_name'!E:E, 'sheet_name'!P:P,'sheet_name'!F:F}, "SELECT * WHERE Col3 IS NOT NULL"), 6, 0, 3, FALSE)

This queries rows that are not null, containing data.


**Official Function Documentation**

`Google Sheets Function List <https://support.google.com/docs/table/25273?hl=en&ref_topic=9054531&sjid=14386119101264594616-NC#>`__

`GOOGLEFINANCE <https://support.google.com/docs/answer/3093281?sjid=14386119101264594616-NCl>`__

`IMPORTDATA <https://support.google.com/docs/answer/3093335?hl=en>`__

`IMPORTXML <https://support.google.com/docs/answer/3093342?hl=en&ref_topic=9199554&sjid=14386119101264594616-NC>`__

`SPARKLINE <https://support.google.com/docs/answer/3093289?sjid=14386119101264594616-NC>`__

`FILTER <https://support.google.com/docs/answer/3093197?sjid=14386119101264594616-NC>`__

`SUMIFS <https://support.google.com/docs/answer/3238496?sjid=14386119101264594616-NC>`__

`QUERY <https://support.google.com/docs/answer/3093343?hl=en>`__

`SORTN <https://support.google.com/docs/answer/7354624?sjid=14386119101264594616-NC>`__

`INDEX <https://support.google.com/docs/answer/3098242?sjid=14386119101264594616-NC>`__

`REGEXMATCH <https://support.google.com/docs/answer/3098292?sjid=14386119101264594616-NC>`__
