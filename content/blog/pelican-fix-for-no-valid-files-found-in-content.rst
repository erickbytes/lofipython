Pelican Fix for "No valid files found in content"...
####################################################
:date: 2022-10-08 13:43
:author: pythonmarketer
:category: coding, python, writing
:tags: markdown library, pelican blog, python fix
:slug: pelican-fix-for-no-valid-files-found-in-content
:status: published

Pelican is a popular `static site generator library <https://pythonmarketer.com/2021/07/28/a-brief-summary-of-promising-python-static-site-generators/>`__ in Python. I didn't know why my pelican blog was not working. I've used the "pelican content" command many times for my blog. This time, when attempting to write a new post on a new computer, I was getting this error where none of my posts were visible to Pelican:

.. code-block:: python

   WARNING  No valid files found in content for the active         log.py:91
            readers:                                                        
              | BaseReader (static)                                         
              | HTMLReader (htm, html)                                      
              | RstReader (rst)     

.. figure:: https://pythonmarketer.files.wordpress.com/2022/10/image.png?w=665
   :alt: 
   :figclass: wp-image-7221

**Solution**

Install the markdown library, which is stated in the `pelican docs <https://docs.getpelican.com/en/3.6.3/install.html#optional-packages>`__. This `Github issue <https://github.com/getpelican/pelican/issues/1868>`__ also provides some background on this warning.

::

   pip install markdown

.. figure:: https://pythonmarketer.files.wordpress.com/2022/10/image-1.png?w=672
   :alt: 
   :figclass: wp-image-7224

Now my "pelican content" command works!

.. code-block:: python

   pelican content

.. figure:: https://pythonmarketer.files.wordpress.com/2022/10/image-2.png?w=679
   :alt: 
   :figclass: wp-image-7226
