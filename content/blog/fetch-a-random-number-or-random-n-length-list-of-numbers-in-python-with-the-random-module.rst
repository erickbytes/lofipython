#######################################################################
 Retrieve Random Numbers Via Python's random Module + range() Built-in
#######################################################################

:date:
   2022-09-15 23:09

:author:
   pythonmarketer

:category:
   coding, programming, python

:tags:
   python random numbers list, random module, random numbers python

:slug:
   fetch-a-random-number-or-random-n-length-list-of-numbers-in-python-with-the-random-module

:status:
   published

There are usually many ways to do most things in Python. I've retrieved
random numbers a few different ways at various times within the random
module, often after reading a Stack Overflow post. This time in my most
recent search for random digits, I discovered in the Python docs the
`random.sample()
<https://docs.python.org/3/library/random.html#random.sample>`__
function with its k parameter:

   Return a *k* length list of unique elements chosen from the
   population sequence or set. Used for random sampling without
   replacement.

   https://docs.python.org/3/library/random.html#random.sample

When combined with the `range() built-in
<https://docs.python.org/3.3/library/stdtypes.html?highlight=range#range>`__,
it makes doing this easy. Being able to specify a length and return a
list of random numbers is mighty convenient. This function seems a
Pythonic way to randomize to me. Have a look!

.. code-block:: python

   import random
   # Returns a list of 5 random numbers.
   numbers = random.sample(range(10000000), k=5)
   print(numbers)
   # Returns a single random number.
   number = random.sample(10000000), k=1)[0]
   print(number)

.. figure:: https://pythonmarketer.files.wordpress.com/2022/09/image-2.png?w=552
   :alt: Python Random Number Code
   :figclass: wp-image-7196

To choose a sample from a range of integers, use a `range()
<https://docs.python.org/3/library/stdtypes.html#range>`__ object as an
argument.

"This is especially fast and space efficient for sampling from a large
population":

.. code-block:: python

   sample(range(10000000), k=60)

\- Python Docs, https://docs.python.org/3/library/random.html#random.sample
