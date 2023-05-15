Title: Inserting New Rows Into A Microsoft Access Database With Python and pyodbc
Date: 2019-11-30 00:28
Author: pythonmarketer
Category: automation, data, Databases, excel, ODBC, pandas, python, Windows
Tags: Access, Microsoft, productivity, programming
Slug: inserting-new-records-into-a-microsoft-access-database-with-python
Status: published

I recently automated the loading of data into a Microsoft Access database with [pyodbc](https://github.com/mkleehammer/pyodbc/wiki), a Python library for connecting to databases. ODBC stands for [Open Database Connectivity](https://en.wikipedia.org/wiki/Open_Database_Connectivity). It can be used for a variety of Database Management Systems outside of Access also.

**First,** **[install libraries with pip](https://docs.python.org/3/installing/index.html). Enter in terminal or command prompt:**

1.  1.  `python -m pip install pyodbc`
    2.  `python -m pip install pandas`

**Next, check available Microsoft Access drivers on your computer. Enter the below statements into the Python interpreter:**

    python
    >>> import pyodbc
    >>> [x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')]

**Drivers for** **Access & Many Other Data Sources**

The driver is the engine that allows you to connect to a specific type of database. The drivers available vary depending on your machine.

The two most common drivers for Access are Microsoft Access Driver (\*.mdb) and Microsoft Access Driver (\*.mdb, \*.accdb). My computer only had \*.mdb, which has been deprecated. My Access database was a .mdb file, so I was able to use this driver as shown below. Read more on Access drivers [here](https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-Microsoft-Access).

> "Drivers exist for all major DBMSs, many other data sources like address book systems and Microsoft Excel, and even for text or comma-separated values (CSV) files."  - [Wikipedia](https://en.wikipedia.org/wiki/Open_Database_Connectivity)

**Database Data Types**

I set all of the field data types to "Short Text" because I'm passing strings as SQL parameters below. Uploading as other data types may require additional formatting. To edit the data types of your table, open the table and select "Design View" under the "Home" tab. It got the job done for me!

**Inserting new rows into a Microsoft Access Database:**

    import pandas as pd
    import pyodbc


    def df_to_row_tuples(df):
        """
        use list comprehension to format df rows as a list of tuples: 
        rows = [('Garfield','Orange','Eat'),('Meowth','White','Scratch')] 
        """
        df = df.fillna('')
        rows = [tuple(cell) for cell in df.values]
        return rows

    """
    Rows are not added to DB until they are committed. 
    Pass each row tuple as a SQL parameter (?,?,?). 
    cursor.execute docs: https://www.mcobject.com/docs/Content/Programming/Python/Classes/Cursor/execute.htm
    """ 
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=C:\Add_Path\To_DB\Here\Your_DB.mdb;')
    cursor = conn.cursor()
    sql = ''' INSERT INTO Cats (Name, Color, Move) 
              VALUES(?,?,?) '''
    df = pd.read_csv('Cat Data.csv')
    rows = df_to_row_tuples(df) 
    for row in rows:
        cursor.execute(sql, row) 
    conn.commit()

**Conclusion**

Running the above in command prompt uses pyodbc and SQL to add dataframe rows to a Microsoft Access DB table named "Cats". Passing each row as a [SQL parameter](https://www.python.org/dev/peps/pep-0249/#paramstyle) has two benefits:

1.  It handles strings with single quotes (') and loads them to the DB.
2.  It protects against [SQL injection](https://www.acunetix.com/websitesecurity/sql-injection/) attacks.

**Access Limitation Disclaimer**

Access topped out just shy of 10 million rows in my use case, when records stopped getting added to my database. So keep that in mind if you're thinking about using Access to store your data.

**Supplementary Resources**

[Insert Values into MS Access Table using Python](https://datatofish.com/insert-ms-access-python/)

[pyodbc documentation](https://github.com/mkleehammer/pyodbc/wiki)

[Microsoft Documentation pyodbc example](https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver15)

[The Python Cursor Class](https://www.mcobject.com/docs/Content/Programming/Python/Classes/Cursor.htm)

`<!-- wp:paragraph -->`{=html}

[Psycopg Cursor Class Documentation](https://www.psycopg.org/docs/cursor.html)

`<!-- /wp:paragraph -->`{=html}
