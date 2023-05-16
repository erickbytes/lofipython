How to Check if a Python Variable is a Tuple
############################################
:date: 2021-05-14 00:00
:author: pythonmarketer
:category: coding, life, programming, python
:tags: coursera, Google, humility
:slug: stay-hungry-stay-humble
:status: published

Tonight I Googled "how to check if a variable is a tuple", expecting to find a Stack Overflow `isinstance() <https://docs.python.org/3/library/functions.html#isinstance>`__ snippet. Instead, I found that i could use Python's type built-in to check if my variable is a tuple:

.. code:: wp-block-syntaxhighlighter-code

   # Wrong
   A = (3,3)
   if type(A) is tuple:
       print('Found a tuple.')
   # >>> Found a tuple.

I thought that looked like a good solution until I found a section in `PEP 8, Python's official style guide <https://www.python.org/dev/peps/pep-0008/>`__, that said that is not the best way to do this.

.. code:: wp-block-syntaxhighlighter-code

   # Correct
   A = (3,3)
   B = 'hello world'
   if isinstance(A, tuple):
       print('Found a tuple.')
   if isinstance(B, tuple):
       print('Found a tuple.')
   else:
       print('Not a tuple.')
   # >>> Found a tuple.
   # >>> Not a tuple.

Never let yourself believe that you know all you need to know already. There's always something new to rediscover. And (sometimes) only one best way.

.. code:: wp-block-preformatted

   There should be one-- and preferably only one --obvious way to do it.
   - Zen of Python
