Cleaning Data with Python and Excel: A Brief Example
####################################################
:date: 2018-03-30 02:24
:author: pythonmarketer
:category: coding, data, excel
:tags: code, programming, python
:slug: cleaning-data-with-python
:status: published

I want to show a simple, real world problem and solution I made today with Python.

**Problem:** My data has been corrupted (over 8,000 rows in Excel). Somewhere in my haste, I have scrambled first names and last names in the 'first name' and 'last name' field.

.. image:: https://pythonmarketer.files.wordpress.com/2018/03/office_scrambled.png
   :alt: office_scrambled
   :class: size-full wp-image-1351 alignnone
   :width: 314px
   :height: 133px

**Solution:** Find unique words from both fields, which leads to unique first and last names.

Copy the columns from Excel into a Notepad text file. Then run the below `code <https://www.dropbox.com/s/kxmg3ndnx8d70hv/remove_dupe_words.py?dl=0>`__ on the text file in command prompt.

.. image:: https://pythonmarketer.files.wordpress.com/2018/03/run_command.png
   :alt: run_command
   :class: alignnone size-full wp-image-1352
   :width: 464px
   :height: 25px

.. container:: line number1 index0 alt2

   ::

      with open('file_name.txt',"r") as f:
          lines = f.readlines()
          lines = [line.split() for line in lines]
          new_line = list()
          edited_lines = list()
          for line in lines:
              # keep only the first appearance of a word on each line
              new_line = [word for word in words if word.strip() not in new_line]
              edited_lines.append(new_line)

      with open("edited_lines.txt",'w) as f:
          for line in edited_lines:
              line = ' '.join(line) +'\n'
              f.write(line)

.. container::

   .. container::

      **Output**

   .. container::

      |unique_words|

   As you can see to the right, this has done a good job of repairing the damage, but we still need to get separation of first and last names. Luckily, I had already written some very ugly code tthat I probably shoudn't share (oh well!) that tries to match first and last names to columns appropriately and insert a semi-colon as a delimiter. `Here is the code. <https://www.dropbox.com/home/Sieve?preview=name_columnizer.py>`__

.. container::

.. container::

   |form_Text|\ **Note:** You may need to use Excel's "From Text" feature if pasting in data from text files does not work.

.. container::

.. container::

   Once we paste the data from our program in, we can use Excel's Text to Columns feature and split on the semi-colon delimiter.

.. container::

.. container::

   After running our new file through the code linked above, we arrive at an output closer to what is desired: split name columns. A bug in my name_columnizer.py program accidentally inserted an extra '&' into some records. (I'm not perfect :)) Thankfully it could be fixed by a simple find and replace in Excel.

.. container::

.. container::

   |find_replace_2|

.. container::

.. container::

   This takes us to the below data, which is not ideal but suited my purposes for the job at hand.

.. container::

   |finish|

.. container::

.. container::

   I enjoyed this, because it was a custom solution to a problem created by my own carelessness in Excel. But I fixed it using relatively few lines of code. I want to start sharing more actual code on this blog so here is a start. I strive to be 'Pythonic', but my code is not always the best way. Often, it's far from it. Sometimes I just write code until I find a solution. I try to solve problems and learn to the best of my ability.

.. container::

   Hope you enjoyed :D

.. container::

.. container::

.. container::

   This solution was used before I discovered the `Pandas <https://pythonmarketer.wordpress.com/2018/05/12/pandas-pythons-excel-powerhouse/>`__ library, which I highly recommend looking into for doing Excel tasks with Python.

 

.. |unique_words| image:: https://pythonmarketer.files.wordpress.com/2018/03/unique_words.png
   :class: size-full wp-image-1353 alignright
   :width: 224px
   :height: 137px
.. |form_Text| image:: https://pythonmarketer.files.wordpress.com/2018/03/form_text.png
   :class: size-full wp-image-1354 alignright
   :width: 220px
   :height: 142px
.. |find_replace_2| image:: https://pythonmarketer.files.wordpress.com/2018/03/find_replace_2.png
   :class: alignnone size-full wp-image-1356
   :width: 604px
   :height: 248px
.. |finish| image:: https://pythonmarketer.files.wordpress.com/2018/03/finish.png
   :class: alignnone size-full wp-image-1357
   :width: 224px
   :height: 122px
