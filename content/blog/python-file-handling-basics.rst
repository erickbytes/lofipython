Python File Handling Basics
###########################
:date: 2018-01-14 18:53
:author: pythonmarketer
:category: coding, programming
:tags: data, python, software
:slug: python-file-handling-basics
:status: published

The basis of many great programs revolve around a simple set of operations:

#. Open a file.
#. Do something with the file contents.
#. Save the new file for the user.

Python is nice and simple for this. Paste the below lines into a `text editor <https://www.google.com/search?q=text+editor&oq=text+edit&aqs=chrome.0.0j69i57j0l4.2054j0j7&sourceid=chrome&ie=UTF-8>`__ and save as a .py file. `You need to have Python 3 installed <https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation>`__. In the same folder as your .py file, save a .txt file with some words in it. Alright, let's write some code:

::

   file_name = input("Enter your file name. e.g. words.txt")
   file_handle = open(file_name, "r")
   lines = file_handle.readlines()
   print (lines)
   file_handle.close()

In line 1, we ask the user to enter their file name with Python's raw_input function. When the program runs, the user enters their text file name with extension. This line stores the name in a variable called file_name.

**In line 2,** we open your text file and store it in a variable I have named file_handle. Think of the file handle as a bridge between your code and the text file. Quick point about the 'r' above: that tells the program to open the file in "Read" mode. There are several different file modes in programming. Some modes are just for reading an existing file, some are just for writing a new file, and some are capable of both. `This Stack Overflow post <https://stackoverflow.com/questions/16208206/confused-by-python-file-mode-w/16208298>`__ is well written and details the differences between file modes. Once established, the file handle allows you to read the file's contents or write new contents to the file.

**In line 3,** we are calling the .readlines() method on our file handle. This method takes the file contents and stores them, line by line, into a list named "lines". An alternative method is .read(), which opens the file and stores its contents as one string. Try switching this out in place of  .readlines() to check out the difference.

**In line 4,** we are printing the stored lines to show them to the user. We now have the file contents, ready to be used however we please.

**In line 5**, we are closing the file.

Below, we are going to write a new file. Let's pretend we've done something worth saving with our lines and now want to save them to a new file. We will represent this as the variable "output" in the first line below.

::

   file_name = input("Enter any file name.")
   save_file = open(file_name, "w")
   save_file.write("Here is some text to save in a file.")
   save_file.close()

In line 1, we are using Python's input function to ask the user what to name the file and storing it in a variable named file_name.

In line 2,  we are calling the open function again that we used in the first example, but this time, notice the "w". This indicates that we are opening the file in "write" mode.

In line 3, we are calling the .write() method on our file handle, named save_file, and passing it our text to be saved in our new file.

**In line 4**, we are closing the file, completing the creation of our new file in the same folder as our .py program file.

Your program is now ready to be run. Double-click your .py file to execute it.

Before learning Python, file operations were a mystery to me. It took me a while to understand this clearly, and I wanted to share. Once you master these basic file operations, programming gets to be a lot more fun. Do try it out for yourself :D
