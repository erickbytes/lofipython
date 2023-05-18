So You Want to Learn Python?
############################
:date: 2021-02-14 14:05
:author: pythonmarketer
:category: programming
:tags: learning, python, skills, technology
:slug: so-you-want-to-learn-python
:status: published

Here are a few Python concepts for beginners to explore if you are starting out with the language. In this post, I'll highlight my favorite "must-learn" tools to master that come with your Python installation. Understanding them will make you a more capable Python programmer and problem solver.

1. `Built-in Functions <https://docs.python.org/3/library/functions.html#built-in-funcs>`__. They are awesome! You can do so much with these. Learn to apply them. You won't regret it! See also: `An Intro to Python's Built-in Functions <https://www.blog.pythonlibrary.org/2021/02/17/an-intro-to-pythons-built-in-functions/>`__

2. `String methods <https://docs.python.org/3/library/stdtypes.html#string-methods>`__. Want to capitalize, lowercase or replace characters in text? How about checking if a `str.isdigit() <https://docs.python.org/3/library/stdtypes.html#str.isdigit>`__? Get to know Python's string methods. I use these frequently. Also, the `pandas string method implementations <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.isdigit.html>`__ are great for applying them to tabular data.

3. `Docstrings <https://docs.python.org/3/tutorial/controlflow.html#documentation-strings>`__. I truly enjoy adding docstrings at the beginning of my functions. They add clarity and ease of understanding.

4. `The Mighty Dictionary <https://www.youtube.com/watch?v=C4Kc8xzcA68&ab_channel=EugeneYarmash>`__. Lists and tuples are useful too, but `dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`__ are so handy with the ability to store and access key-value pairs.

5. `List Comprehensions <https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions>`__. These allow you to perform transformations on lists in one line of code! I love the feeling when I apply a list comprehension that is concise, yet readable.

6. `Lambda Expressions <https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions>`__. These can be used to apply a function "on the fly". I love their succinctness. It took me a few years to become comfortable with them. Sometimes it makes sense to use a lambda expression instead of a regular function to transform data.

7. `Date Objects <https://docs.python.org/3/library/datetime.html#date-objects>`__. Wielding date objects and formatting them to your needs is a pivotal Python skill. Once you have it down, it unlocks a lot of automation and scripting abilities when combined with libraries like `pathlib <https://docs.python.org/3/library/pathlib.html>`__, `os <https://docs.python.org/3/library/os.html?highlight=os#module-os>`__ or `glob <https://docs.python.org/3/library/glob.html?highlight=glob#module-glob>`__ for reading file metadata and then executing an action based on the date of the file, for example. I use `date.today() <https://docs.python.org/3/library/datetime.html#datetime.date.today>`__ a lot when I want to fetch today's date and `timedelta <https://docs.python.org/3/library/datetime.html#available-types>`__ to compare two dates. The datetime module is your friend, dive in. Must know for custom date formatting: strftime() and strptime(). See also: `Time Format Codes <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes>`__

For tabular data, I often use ``pd.to_datetime()`` to convert a series of strings to datetime objects:

.. code-block:: python

    # install pandas with this command: python -m pip install pandas
    import pandas as pd
    events = [
        ["USA Born", "1776-07-04"],
        ["WTC Bombings", "2001-09-11"],
        ["Biden Inauguration", "2021-01-20"],
    ]
    df = pd.DataFrame(events, columns=["events", "dates"])
    # convert a pandas series of strings to datetime objects
    df.dates = pd.to_datetime(df.dates)
    print(df.dtypes)
    print(df.head())


`Go here <#%20convert%20a%20list%20of%20strings%20to%20a%20pandas%20series%20of%20datetime%20objects>`__ if you're having pip installation problems.

**Just the tip of the iceberg...**

The amazing part of Python is that its community has developed an astonishing plethora of external libraries which can be `installed by pip <https://pythonmarketer.wordpress.com/2018/01/20/how-to-python-pip-install-new-libraries/>`__. Usually I'll learn how to use new libraries after googling to find a well-written README on Github or helpful documentation. The language comes with an impressive line-up of baked-in `tools and libraries <https://docs.python.org/3/library/>`__ way beyond what I've mentioned here. But I think this is a great start. Get to know these common Python language features and you'll be surprised how much you can do!

**Additional Comprehensive Python Learning Resources**

`How long did it take you to learn Python? <https://nedbatchelder.com/blog/202003/how_long_did_it_take_you_to_learn_python.html>`__

`Practical Python Programming <https://github.com/dabeaz-course/practical-python>`__ (free course)

`Google Python Style Guide <https://google.github.io/styleguide/pyguide.html>`__

`What the f*ck Python! <https://github.com/satwikkansal/wtfpython>`__

`PySanity <https://pysanity.netlify.app/#testing>`__
