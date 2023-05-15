Title: SQLite3: Pythonic First Impressions & Lay of the Land
Date: 2020-09-20 00:09
Author: pythonmarketer
Category: data, Databases, python, SQL
Tags: open data, SQLite, SQLite commands, sqlite3
Slug: getting-the-lay-of-the-land-in-sqlite-and-connecting-to-a-db-with-pythons-sqlite3-library
Status: published

`<!-- wp:paragraph -->`{=html}

**introduction**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

SQLite is one of the heavy hitters in the database space, up there with other popular choices like MySQL, Postgres, Microsoft SQLServer, Cassandra and MariaDB. There is no shortage of [database technologies](https://dbdb.io/) but SQLite is certainly one that is commonly used. It also has a positive reputation. Its terminal interface reminds me of [MySQL](https://pythonmarketer.wordpress.com/2020/05/25/essential-mysql-terminal-commands-and-connecting-to-mysql-with-flask-pandas-and-pythonanywhere/). The syntax of both seem similarly "SQL-like" and easy to pick up.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

I finally got around to test-driving a [SQLite](https://en.wikipedia.org/wiki/SQLite) database this week. In this post, I've listed my impressions of some practical SQLite commands. The "dot" syntax is helpful to do a lot things as you'll see below. I'll conclude by briefly exploring the sqlite3 python library in the python interpreter.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**getting started**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

I [installed SQLite from the terminal](https://linuxhint.com/install_sqlite_browser_ubuntu_1804/) with apt on Ubuntu Linux.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

There are also downloads for Windows. A popular GUI is [SQLite Studio](https://sqlitestudio.pl/).

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**create a new database**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

`sqlite3 PythonMarketer.db`

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**create a new db + new table and import a csv file to the table, "Readers"**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
sqlite3 PythonMarketer.db
.mode csv Readers
.import PythonMarketerReaders2015-2020.csv Readers
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:paragraph -->`{=html}

\[[source](https://tableplus.com/blog/2018/07/sqlite-how-to-import-csv-file-into-sqlite-table.html)\]

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**create a table**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

`CREATE TABLE `Readers` (Country TEXT,Visits INTEGER);`

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**add new column with a default value**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

`ALTER TABLE Readers ADD  TEXT DEFAULT '0';`

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**show all help (and . syntax) options**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

`.help`

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**show all tables**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

`.tables`

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**show table creation statement (table schema)**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

`.schema Readers`

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**exit sqlite terminal**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

`.exit `

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**show databases**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

`.databases `

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**show all indexes**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

`.indexes`

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**"show" various DB settings**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

`.show`

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:image {"align":"left","id":4412,"sizeSlug":"large"} -->`{=html}

::: wp-block-image
![](https://pythonmarketer.files.wordpress.com/2020/09/show-explain-sqlite3.jpg?w=904){.wp-image-4412}
:::

`<!-- /wp:image -->`{=html}

`<!-- wp:paragraph -->`{=html}

*Pictured: "showing" DB settings and "[EXPLAIN-ing](https://sqlite.org/lang_explain.html)" a query*

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Exploring sqlite operators:** the **[GLOB operator](https://www.sqlitetutorial.net/sqlite-glob/)**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:heading -->`{=html}

## Exploring my new table with the [Python sqlite3 library](https://docs.python.org/3/library/sqlite3.html) in the Python interpreter

`<!-- /wp:heading -->`{=html}

`<!-- wp:paragraph -->`{=html}

[sqlite3](https://docs.python.org/3/library/sqlite3.html) is in the python standard library, always a nice convenience to simply import it! Here we are connecting to an existing .db with `sqlite3.connect()`

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:image {"align":"left","id":4416,"sizeSlug":"large"} -->`{=html}

::: wp-block-image
![](https://pythonmarketer.files.wordpress.com/2020/09/python-interpreter-python-sqlite.jpeg?w=717){.wp-image-4416}
:::

`<!-- /wp:image -->`{=html}

`<!-- wp:paragraph -->`{=html}

Below, getting a cursor object that holds our S`ELECT` query results. Then iterating through each row of the cursor object with a for loop, as demonstrated in the documentation.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:image {"align":"left","id":4417,"sizeSlug":"large"} -->`{=html}

::: wp-block-image
![**Shown above:** printing the rows within the cursor object returned from executing a SELECT SQL statement.  
](https://pythonmarketer.files.wordpress.com/2020/09/pythonsqlitedbreaders.jpeg?w=820){.wp-image-4417}
:::

`<!-- /wp:image -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Comparable Cursors and PEP 249**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

The cursor object has a variety of methods you can call on it for database operations and to execute SQL. You can read more about them in the [sqlite3 module documentation](https://docs.python.org/3/library/sqlite3.html). This library also follows [PEP 249 - Python Database API Specification](https://www.python.org/dev/peps/pep-0249/) for recommended Database API interfaces. I've noticed that in [pyodbc](https://pythonmarketer.wordpress.com/2019/11/30/inserting-new-records-into-a-microsoft-access-database-with-python/), for example, the cursor object looks and feels the same as the cursor object in sqlite3. This is because they are both likely following PEP 249. Very cool!

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:heading -->`{=html}

## Before You Go, Check Out Python Marketer's [Open Data Github Repository](https://github.com/erickbytes/Python-Marketer-Reader-Analytics)

`<!-- /wp:heading -->`{=html}

`<!-- wp:paragraph -->`{=html}

The data shown in this post is published on [Github](https://github.com/erickbytes/Python-Marketer-Reader-Analytics). There you'll find you this blog's reader by country data, with analysis in a Jupyter Notebook. [This post I wrote](https://pythonmarketer.wordpress.com/2019/04/12/datasets-plotting-using-jupyter-pandas-and-matplotlib/) shows more info about using Jupyter and matplotlib for data analysis if you're curious about it.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

In 2020, **105 countries or 53%** of the world's countries have read about Python on this blog. 🤯👏👏👏 Amazing.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

I think this data offers a hint of perspective into the question, "Where in the world are people learning about Python?" The short answer is all around the world! That's pretty rad. Thanks for reading and stay curious.

`<!-- /wp:paragraph -->`{=html}
