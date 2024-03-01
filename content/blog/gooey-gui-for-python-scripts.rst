Gooey GUI for Python Scripts
############################
:date: 2018-08-25 16:32
:author: pythonmarketer
:category: coding, data, product development, programming, software
:tags: gooey, gui, python, software development
:slug: gooey-gui-for-python-scripts
:status: published

GUI stands for "Graphical User Interface", aka the part of a program designed for human interaction. Adding a GUI to a Python 
script allows anyone to run it without having to code or use the command line.

There are several GUI libraries in Python. A few I have heard of are Tkinter (comes in the standard library), wxPython, PyQT, 
easygui, `DearPyGui <https://github.com/hoffstadt/DearPyGui>`__ and PySimpleGUI. I `explored Tkinter <https://lofipython.com/tkinter-and-python-libraries/>`__ 
back when I first got into Python. It was more intricate and offered more control over the look of your app, and took longer to pick up. Gooey is more of a pre-packaged GUI library.

The `Gooey Github page <https://github.com/chriskiehl/Gooey>`__ was most useful to me and helped me to do what I needed. 
The script posted `in this blog <http://pbpython.com/pandas-gui.html>`__ helped as well. I needed to enable a human to 
supply three files and enter a number. Gooey was a good match for this. The library has two branches:

#. some basic widgets piggyback off the `argparse <https://blog.pythonlibrary.org/2015/10/08/a-intro-to-argparse/>`__ library
#. another part of the library uses a function called the GooeyParser. The GooeyParser offers more advanced widgets, like a file chooser. This was exactly what I was looking to use to pull in files for my script.

**Installing Gooey**

Argparse comes stock with Python. You can install Gooey via the `pip installer <https://lofipython.com/how-to-python-pip-install-new-libraries/>`__. Open command prompt or terminal and enter:

::

    python -m pip install Gooey

Below is a basic argparse/Gooey combination script. The argparse version offers a handful of widgets such as checkboxes and dropdown, but I had trouble getting them to work with the GooeyParser (used in 2nd script).

.. code-block:: python

   from argparse import ArgumentParser
   from gooey import Gooey

   @Gooey(program_name='Report Generator', default_size=(575, 600))
   def get_args():
       """Demonstrating python's vars built-in to store arguments in a python dict."""
       parser = ArgumentParser(description='A simple argument parser', epilog='This is where you might put example usage')
       parser.add_argument('Name', action='store', required=True, help='Help text for option X')
       parser.add_argument('Email', help='Help text for option Y', default=False)
       parser.add_argument('Campaign Number', help='Help text for option Z', type=int)
       parser.add_argument('Campaign Segment', choices=['A', 'B','All'], default='a', nargs='?')
       user_inputs = vars(parser.parse_args())
       print(user_inputs) 
       name = user_inputs['Name']
       campaign_number = user_inputs['Campaign Number']
       return parser.parse_args()

   if __name__ == '__main__':
       get_args()

..

   Side note: Check out Python's `vars() built-in <https://docs.python.org/3/library/functions.html#vars>`__ function above. 
   It returns the input data as a dictionary called user_inputs. Then we can get the values via the dictionary's keys. Pretty nifty!

The @Gooey() part of the code is an advanced function known as a `decorator in Python <https://www.python.org/dev/peps/pep-0318/>`__. 
Put simply, decorators are functions that modify the function to which they are attached.

Below is my script that uses the more advanced GooeyParser for its "FileChooser" widget. Gooey allows you to group widgets together 
and set how many widgets per line with the gooey_options={} parameter.

.. code-block:: python

   from gooey import Gooey, GooeyParser
    
   @Gooey(program_name='Email Campaign Reporting Generator', default_size=(575, 600))
   def get_args():
       """Adding two argument groups, each accepting two arguments. Using gooey_options to set layout."""
       parser = GooeyParser(description='Export campaign report spreadsheets and upload below.')
       top_group = parser.add_argument_group(gooey_options={'show_border': False,'columns': 1})
       top_group.add_argument('Contact List', help='Upload Send List (.xlsx)', widget='FileChooser') 
       top_group.add_argument('Opens List', help='Upload Opens List (.xlsx)', widget='FileChooser')
       top_group.add_argument('Unsubscribe List', help='Upload Unsubscribe List (.xlsx)', widget='FileChooser')
       bottom_group = parser.add_argument_group(gooey_options={'show_border': False,'columns': 1, 'required':False})
       bottom_group.add_argument('Campaign ID', action='store', help="Number found in the Campaign 'Reports' tab")
       bottom_group.add_argument('Campaign Segment', action='store', help='Enter A, B, or All. All lists supplied must match segment.')
       user_inputs = vars(parser.parse_args())
       name = user_inputs['Name']
       return parser.parse_args()

   if __name__ == '__main__':
       get_args()

Overall, Gooey knows what it wants to be, an easy to use GUI framework for Python. It does it well. Here's a screenshot of my program's shiny GUI:

.. image:: https://pythonmarketer.files.wordpress.com/2018/08/gooey_gui_shot_2.png
   :alt: gooey_gui_shot_2
   :class: alignnone size-full wp-image-1431
   :width: 578px
   :height: 603px

Now that I have a GUI on top of my program and it delivers the expected output file, I'm hoping to take it one step further by packaging it up as a Windows .exe file. 
This would allow it to run as a desktop app on any Windows computer without the need to install Python or library dependencies. 
I've only begun exploring options to do this but a few libraries I've heard of are pyinstaller, cx_Freeze and Py2Exe. Updates coming if I figure it out. Cheers :D

**Update:** I did figure out how to compile my Gooey app to a Windows application with Pyinstaller. You can `read more on how I did it here <https://lofipython.com/packaging-python-as-a-windows-app/>`__.
