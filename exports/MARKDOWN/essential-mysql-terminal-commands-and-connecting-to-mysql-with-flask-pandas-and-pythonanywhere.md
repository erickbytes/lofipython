Title: Integrating MySQL with Flask, pandas and pythonanywhere
Date: 2020-05-25 21:48
Author: pythonmarketer
Category: data, Databases, ODBC, pandas, programming, SQL, web development, web2py
Tags: flask, mysql, py4web, pyDAL, python
Slug: essential-mysql-terminal-commands-and-connecting-to-mysql-with-flask-pandas-and-pythonanywhere
Status: published

`<!-- wp:paragraph -->`{=html}

Sometimes a spark comes from seemingly nowhere. That's when you reach for your tools and create. After a series of successful experiments, I decided this stack might be my quickest, best shot to get a functional website up and running in Python. I was pleasantly surprised to make rapid progress over the span of a quarantine weekend. Here are the steps to create a [MySQL backed website](https://weedfiend.pythonanywhere.com) with Flask.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Hosting With pythonanywhere**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[pythonanywhere](https://www.pythonanywhere.com/user/weedfiend/) is a web hosting service like GoDaddy. If you host your app with them, MySQL is the default database. Postgres integration is available at higher price tiers.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**To get your Flask app's database up and running you need to:**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:list {"ordered":true} -->`{=html}

1.  Create your database (see the "Databases" tab in pythonanywhere)
2.  Use the mysql terminal to create your tables
3.  Use the mysql.connector API to connect to your table and execute SQL from your Flask app.

`<!-- /wp:list -->`{=html}

`<!-- wp:heading -->`{=html}

## Essential MySQL Terminal Commands

`<!-- /wp:heading -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Show MySQL Version**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
SELECT VERSION();
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:paragraph -->`{=html}

**List tables in a database**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
SHOW TABLES;
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Show All MySQL Variable Values**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
SHOW VARIABLES;
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Creating a Table**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
CREATE TABLE Marijuana (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(350), date VARCHAR(350));
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:paragraph -->`{=html}

**[Create a Table with a JSON column](https://www.sitepoint.com/use-json-data-fields-mysql-databases/)**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
CREATE TABLE ​Marijuana (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `store` varchar(200) NOT NULL,
  `details` json DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Add New Column and specify column to insert AFTER**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
ALTER TABLE Marijuana
ADD COLUMN date VARCHAR(100) AFTER other_column;
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Alter Datatype of a Column**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
ALTER TABLE Marijuana MODIFY id INT AUTO_INCREMENT PRIMARY KEY;
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Describe a Table**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
DESCRIBE Marijuana;
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:paragraph -->`{=html}

**View All Records in a Table**

`<!-- /wp:paragraph -->`{=html}

``` wp-block-preformatted
SELECT * from Marijuana;
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:paragraph -->`{=html}

[**Using LIKE in MySQL**](https://www.mysqltutorial.org/mysql-like/)

**Select 10 Newest Records**

``` {.prettyprint .notranslate .prettyprinted}
SELECT * from Marijuana ORDER BY id DESC LIMIT 10;
```

**"Explaining" A Query**

``` wp-block-preformatted
EXPLAIN SELECT * from Marijuana;
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Using "ANALYZE TABLE" to [optimize them](https://dev.mysql.com/doc/refman/8.0/en/statement-optimization.html) is periodically recommended by MySQL:**

    ANALYZE TABLE Marijuana;

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:image {"id":3418} -->`{=html}

```{=html}
<figure>
```
```{=html}
</figure>
```
![](https://pythonmarketer.files.wordpress.com/2020/05/mysql_commands-1.png){.wp-image-3418}

`<!-- /wp:image -->`{=html}

`<!-- wp:heading -->`{=html}

## Installing Libraries in PythonAnywhere

You can use [pip](http://pythonmarketer.wordpress.com/2018/01/20/how-to-python-pip-install-new-libraries/) to install python libraries within the PythonAnywhere bash terminal. Go to the consoles tab and start a new bash terminal. Then to install a library, such as pandas:

    python -m pip3.8 install --user pandas

## Flask app with [mysql.connector API](https://dev.mysql.com/doc/connector-python/en/), SQL and pandas

`<!-- /wp:heading -->`{=html}

`<!-- wp:paragraph -->`{=html}

**A Flask app making a mysql database connection with pandas:**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:list {"ordered":true} -->`{=html}

1.  Creating an error log with logging.
2.  Connecting to a mysql database hosted through [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/) and [pythonanywhere](http://pythonanywhere.com)
3.  Then reading a table to a pandas [dataframe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)

`<!-- /wp:list -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
import mysql.connector
from flask import Flask
import pandas as pd
from datetime import date
import logging
import sys

"""
Flask + MySQL + pandas app from Python Marketer:
https://atomic-temporary-107329037.wpcomstaging.com/2020/05/25/essential-mysql-terminal-commands-and-connecting-to-mysql-with-flask-pandas-and-pythonanywhere/ 
"""

app = Flask(__name__)
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

@app.route('/') 
def hello_world(): 
    """Call database and return data from df. Then display homepage."""
    try: 
        email_df = get_database_table_as_dataframe()
        print(email_df.shape) 
        html_page = render_homepage()
        return html_page 
    except: 
        logging.exception('Failed to connect to database.')

def render_homepage():
    """
    Note: you should use Flask's render_template to render HTML files. 
    But here's a quick f-string HTML page that works:
    """
    html_page = f"""<html><head><link rel='stylesheet' href="/static/styles/some_file.css"><link rel="shortcut icon" type="image/x-icon" href="static/favicon.ico">
                    <Title>Support BLM</Title></head>
                    <body><h2>Black Lives Matter</h2>
                    <p>No to Systemic Racism!</p><br>
                    <h6><b>Support BLM:</b></h6><br>
                    <div class="form">
                    <form action="/add_signup_to_db" method="post" style="width:420px;text-align:center;display:block;" >
                    <input type="text" name="Signup Form">
                    <input type="submit" value="Submit">
                    </form></div><br><br>
                    <p><b>Current Time:</b>
                    {str(date.today())} </p></body></html>"""
    return html_page
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:paragraph -->`{=html}

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:preformatted -->`{=html}

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:paragraph -->`{=html}

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

    def get_database_table_as_dataframe():
        """Connect to a table named 'Emails'. Returns pandas dataframe."""
        try:
            connection = mysql.connector.connect(
                                host='username.mysql.pythonanywhere-services.com', 
                                db='username$DatabaseName', 
                                user='username', 
                                password='password'
                                ) 
                                
            email_df = pd.read_sql(sql="""SELECT * FROM Emails""",
                                   con=connection)
            logging.info(email_df.head()) 
            return email_df
        except:
            logging.exception('Failed to fetch dataframe from DB.')
            return "Oops!" 

    @app.route("/add_signup_to_db", methods=["GET","POST"])
    def add_signup_to_db(email, date):
        """Pass data as SQL parameters with mysql."""
        try:
            connection = mysql.connector.connect(
                                host='username.mysql.pythonanywhere-services.com', 
                                db='username$DatabaseName', 
                                user='username', 
                                password='password'
                                ) 
            cursor = connection.cursor()
            sql = """INSERT INTO Emails (message, date) VALUES (%s, %s) """
            record_tuple = (email, date)
            cursor.execute(sql,record_tuple)
            connection.commit()
        except mysql.connector.Error as error:
            logging.info("Failed to insert into MySQL table {}".format(error))
        except:
            logging.exception('Error inserting records to DB.')
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
            return("MySQL connection is closed")

**Iterative Development**

> Below: making [my website](https://weedfiend.pythonanywhere.com/) look less like a "my first HTML" website, experimenting with my app's message\\name and adding a sign-up form connected to the database.

![Screenshot_20200606-132252 (1)](https://pythonmarketer.files.wordpress.com/2020/05/screenshot_20200606-132252-1-1.png){.alignnone .size-full .wp-image-3524 width="344" height="566"}

**Note: if you see this error when making a request in pythonanywhere:**

`<!-- wp:paragraph -->`{=html}

`OSError: Tunnel connection failed: 403 Forbidden `

It's likely because you are "whitelisted" on the free plan. Upgrading to the \$5/month plan will fix it!

**Scoping The Full Stack**

I'm really enjoying this web development stack. Here are all of the tools and library choices for this website:

-   [HTML](https://en.wikipedia.org/wiki/HTML)
-   [CSS](https://www.taniarascia.com/overview-of-css-concepts/)
-   [web framework](https://en.wikipedia.org/wiki/Web_framework): Flask library
-   email: [Flask-Mail](https://pythonhosted.org/Flask-Mail/) library ([SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol))
-   API calls to external websites: [requests](https://requests.readthedocs.io/en/master/) and json libraries
-   data handling: MySQL database, mysql.connector API, [pandas](https://pythonmarketer.wordpress.com/2018/05/12/pandas-pythons-excel-powerhouse/) library
-   file system: [logging](https://docs.python.org/3/library/logging.html), os and sys libraries
-   (may add) payment processing: [Braintree Library](https://github.com/braintree/braintree_python)
-   web hosting: pythonanywhere

**Finding Your Flask Groove**

Flask is a little scary at first, but reasonable once you get a grasp of the basic syntax. Using the logging module to establish access, error and server log feeds was a big step to finding my Python traceback fixing groove. It's a work in progress.

`<!-- /wp:paragraph -->`{=html}

**Recapping My Python Web Development and Database Experiences**

I previously created a [website](http://tameimpala.pythonanywhere.com/) with [web2py](https://pythonmarketer.wordpress.com/2016/03/29/getting-started-with-web2py/), another Python web framework like Flask and Django. I think it was a decent choice for me at that point in my Python journey. Back then, I connected a MongoDB back-end to web2py. I randomly picked Mongo out of the DB hat and it worked well enough.

> **My Python Web Development and Database Tools**
>
> **App #1**                    web2py + MongoDB
>
> **App #2                     **Flask + MySQL 
>
> **Future App?**      py4web + pyDAL + PostgreSQL
>
> **Future App?**     tornado + streamlit (or) Flask + Dash (+ SQLite)

Of these two diverse Python stacks, I favor MySQL and Flask. But I learned a lot from watching web2py's tutorial videos and it's less intimidating for beginners. And I barely scratched the surface of web2py's "pure Python" [pyDAL (Database Abstraction Layer)](https://github.com/web2py/pydal), which seems pretty dope.

web2py's [creator](https://www.youtube.com/watch?v=hcYUgNWvPtw) has a new framework in progress called [py4web](https://github.com/web2py/py4web). It has the same [DAL](http://www.web2py.com/books/default/chapter/29/06/the-database-abstraction-layer) and inherits many other web2py qualities. Definitely looking forward to exploring the DAL on my first py4web website. I'll likely use it to connect to PostgreSQL or SQLite. Maybe I'll [install pyDAL with pip](https://github.com/web2py/pydal) in the meantime.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**[Final Thoughts]{style="color:var(--color-text);"}**

[Both of my websites are hosted with pythonanywhere, which gives you a text editor and ]{style="color:var(--color-text);"}[bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell))[ terminal to run your scripts in a shell environment. I'm so pleased with all of these tools. They fit together smoothly and made creating my website a fun experience. 👍👍]{style="color:var(--color-text);"}

`<!-- /wp:paragraph -->`{=html}
