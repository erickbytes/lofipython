SQLite3: Pythonic First Impressions & Lay of the Land
#####################################################
:date: 2020-09-20 00:09
:author: pythonmarketer
:category: data, Databases, python, SQL
:tags: open data, SQLite, SQLite commands, sqlite3
:slug: getting-the-lay-of-the-land-in-sqlite-and-connecting-to-a-db-with-pythons-sqlite3-library
:status: published

**introduction**

SQLite is one of the heavy hitters in the database space, up there with other popular choices like MySQL, Postgres, Microsoft SQLServer, Cassandra and MariaDB. There is no shortage of `database technologies <https://dbdb.io/>`__ but SQLite is certainly one that is commonly used. It also has a positive reputation. Its terminal interface reminds me of `MySQL <https://pythonmarketer.wordpress.com/2020/05/25/essential-mysql-terminal-commands-and-connecting-to-mysql-with-flask-pandas-and-pythonanywhere/>`__. The syntax of both seem similarly "SQL-like" and easy to pick up.

I finally got around to test-driving a `SQLite <https://en.wikipedia.org/wiki/SQLite>`__ database this week. In this post, I've listed my impressions of some practical SQLite commands. The "dot" syntax is helpful to do a lot things as you'll see below. I'll conclude by briefly exploring the sqlite3 python library in the python interpreter.

**getting started**

I `installed SQLite from the terminal <https://linuxhint.com/install_sqlite_browser_ubuntu_1804/>`__ with apt on Ubuntu Linux.

There are also downloads for Windows. A popular GUI is `SQLite Studio <https://sqlitestudio.pl/>`__.

**create a new database**

``sqlite3 PythonMarketer.db``

**create a new db + new table and import a csv file to the table, "Readers"**

::

   sqlite3 PythonMarketer.db
   .mode csv Readers
   .import PythonMarketerReaders2015-2020.csv Readers

[`source <https://tableplus.com/blog/2018/07/sqlite-how-to-import-csv-file-into-sqlite-table.html>`__]

**create a table**

``CREATE TABLE``\ Readers\ ``(Country TEXT,Visits INTEGER);``

**add new column with a default value**

``ALTER TABLE Readers ADD  TEXT DEFAULT '0';``

**show all help (and . syntax) options**

``.help``

**show all tables**

``.tables``

**show table creation statement (table schema)**

``.schema Readers``

**exit sqlite terminal**

``.exit``

**show databases**

``.databases``

**show all indexes**

``.indexes``

**"show" various DB settings**

``.show``

.. container:: wp-block-image

   .. figure:: https://pythonmarketer.files.wordpress.com/2020/09/show-explain-sqlite3.jpg?w=904
      :alt: 
      :figclass: wp-image-4412

*Pictured: "showing" DB settings and "*\ `EXPLAIN-ing <https://sqlite.org/lang_explain.html>`__\ *" a query*

**Exploring sqlite operators:** the `GLOB operator <https://www.sqlitetutorial.net/sqlite-glob/>`__

Exploring my new table with the `Python sqlite3 library <https://docs.python.org/3/library/sqlite3.html>`__ in the Python interpreter
-------------------------------------------------------------------------------------------------------------------------------------

`sqlite3 <https://docs.python.org/3/library/sqlite3.html>`__ is in the python standard library, always a nice convenience to simply import it! Here we are connecting to an existing .db with ``sqlite3.connect()``

.. container:: wp-block-image

   .. figure:: https://pythonmarketer.files.wordpress.com/2020/09/python-interpreter-python-sqlite.jpeg?w=717
      :alt: 
      :figclass: wp-image-4416

Below, getting a cursor object that holds our S\ ``ELECT`` query results. Then iterating through each row of the cursor object with a for loop, as demonstrated in the documentation.

.. container:: wp-block-image

   .. figure:: https://pythonmarketer.files.wordpress.com/2020/09/pythonsqlitedbreaders.jpeg?w=820
      :alt: **Shown above:** printing the rows within the cursor object returned from executing a SELECT SQL statement.
      :figclass: wp-image-4417

      **Shown above:** printing the rows within the cursor object returned from executing a SELECT SQL statement.

**Comparable Cursors and PEP 249**

The cursor object has a variety of methods you can call on it for database operations and to execute SQL. You can read more about them in the `sqlite3 module documentation <https://docs.python.org/3/library/sqlite3.html>`__. This library also follows `PEP 249 - Python Database API Specification <https://www.python.org/dev/peps/pep-0249/>`__ for recommended Database API interfaces. I've noticed that in `pyodbc <https://pythonmarketer.wordpress.com/2019/11/30/inserting-new-records-into-a-microsoft-access-database-with-python/>`__, for example, the cursor object looks and feels the same as the cursor object in sqlite3. This is because they are both likely following PEP 249. Very cool!

Before You Go, Check Out Python Marketer's `Open Data Github Repository <https://github.com/erickbytes/Python-Marketer-Reader-Analytics>`__
-------------------------------------------------------------------------------------------------------------------------------------------

The data shown in this post is published on `Github <https://github.com/erickbytes/Python-Marketer-Reader-Analytics>`__. There you'll find you this blog's reader by country data, with analysis in a Jupyter Notebook. `This post I wrote <https://pythonmarketer.wordpress.com/2019/04/12/datasets-plotting-using-jupyter-pandas-and-matplotlib/>`__ shows more info about using Jupyter and matplotlib for data analysis if you're curious about it.

In 2020, **105 countries or 53%** of the world's countries have read about Python on this blog. 🤯👏👏👏 Amazing.

I think this data offers a hint of perspective into the question, "Where in the world are people learning about Python?" The short answer is all around the world! That's pretty rad. Thanks for reading and stay curious.
