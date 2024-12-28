Comparing NFL Football Python Packages
######################################
:date: 2024-12-28 11:49
:author: lofipython
:category: coding, python, NFL, sports
:tags: NFL stats, NFL Python libraries, Python football stats, NFL data
:slug: comparing-nfl-football-python-packages
:status: published

In the spirit of the NFL regular season concluding and playoffs beginning soon, I wondered what packages 
Python had in the NFL stats space. Below, I have compiled my notes below on each of the libraries I found 
for the NFL in Python. 

After a first pass through, there is no runaway favorite. In Python, we say "there should be one obvious way to do it". This doesn't seem 
the case for NFL stats. In a somewhat rare occurrence, the Python community offers a graveyard of abandoned 
or incompatible projects with modern Python. Ultimately, this probably stems from the NFL's inability to provide a consistent stats 
API or feed over time. This may be one of the few times where the R community has better resources available, 
like the `nfldata <https://github.com/nflverse/nfldatay>`__ package in their ecosystem. 


Listed in Order of Most Recently Updated Project
================================================

**nfl_data_py** (`Github <https://github.com/bendominguez0111/nflfastpy>`__)
   - nfl_data_py is a Python library for interacting with NFL data sourced from nflfastR, nfldata, dynastyprocess, and Draft Scout.
   - github repo status: active
   - Github last updated: 3 months ago
   - notable dependencies: requires pandas<2.0,>=1.0
   - This package seems to be most recently updated, but it requires an outdated version of pandas. I suppose it is the best option since it is updated within the past 3 months, but I was unable to install it on Python 3.12.

**sportsipy** (`Github <https://github.com/roclark/sportsipy>`__)
   - A free sports API written for Python
   - Github repo status: "This project is no longer undergoing active development. Please consider opening a pull request for any new features or bug fixes to be reviewed and merged."
   - Github repo last updated: 2022
   - I was able to get the sportsipy package installed via pip, but upon attempting to use it I saw this message: "The requested page returned a valid response, but no data could be found. Has the season begun, and is the data available on www.sports-reference.com?"

**nflfastpy** (`Github <https://github.com/bendominguez0111/nflfastpy>`__)
   - a port of nflfastR, from the R programming language
   - Github repo status: "This repository has been archived by the owner on Nov 18, 2022. It is now read-only."
   - Github repo last updated: 2021
   - notable dependencies: matplotlib
   - This package installed on Python 3.12, but when I tried to import the package, I saw a ValueError from matplotlib. Troubleshooting required.

**nfldb** (`Github <https://github.com/bendominguez0111/nflfastpy>`__)
   - nfldb is a relational database bundled with a Python module to quickly and conveniently query and update the database with data from active games. Data is imported from nflgame, which in turn gets its data from a JSON feed on NFL.com's live GameCenter pages.
   - Github repo status: "THIS PROJECT IS UNMAINTAINED."
   - Github repo last updated: 2018
   - notable dependencies: nflgame package (requires Python 2)

**nflgame** (`pypi <https://pypi.org/project/nflgame/>`__)
   - nflgame is an API to retrieve and read NFL Game Center JSON data. 
   - pypi last updated: 2016
   - notable dependencies: nflgame requires Python 2.6+ and does not yet work with Python 3

**Conclusion**

This is one of the few times where I've been unable to find a Python package that does what I want: extend an API to view NFL stats. 
I could try some of these packages with an earlier version of Python 3, but I'd prefer to use something that works with a more current version of Python.
My suggestion to anyone looking for NFL stats via Python is: you may need to roll your own package, 
or find something like the `SportsRadar API <https://developer.sportradar.com/football/reference/nfl-overview>`__
or `SportsData.io API <https://sportsdata.io/nfl-api>`__. Another option might be to find an existing dataset like the `Dynasty Process data on Github <https://github.com/dynastyprocess/data>`__.