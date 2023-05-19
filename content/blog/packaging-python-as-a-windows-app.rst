Packaging Python as a Windows App via Pyinstaller
#################################################
:date: 2018-11-20 02:59
:author: pythonmarketer
:category: coding, pandas, python, software
:tags: app development, computers, programming, Windows
:slug: packaging-python-as-a-windows-app
:status: published

My research found that for creating a single-file Windows executable from a .py file, the front-running Python library is Pyinstaller. It worked on my Windows 7 PC. My program used a `Gooey GUI <https://pythonmarketer.wordpress.com/2018/08/25/gooey-gui-for-python-scripts/>`__, but many of the popular Python GUI libraries work as well.

**Installation:**

| To install, enter this into command your command prompt or terminal:

::

    python -m pip install pyinstaller

| At the time of this article, this installed Pyinstaller version 3.3.1 using Python version 3.6.5. `Go here <https://lofipython.com/how-to-python-pip-install-new-libraries/>`__ for a refresher on setting up pip if you need it.

**Using the build.spec file and starting Pyinstaller:**

Most examples I found used a build.spec file. Think of this as the blueprint by which your app will be constructed. It provides the compiling settings, images and any other data necessary for assembling your app. The format for passing the .spec file to Pyinstaller in pseudo-code:

   pyinstaller (run mode options) (.spec file)

| **Basic start compiler command to build.spec:**

::

    pyinstaller build.spec

**Establishing a debugging loop with Pyinstaller**

Debug mode can be set from the command line:

::
    
    pyinstaller -debug build.spec

**OR** 
by passing debug=True to the EXE() function of the build.spec. I used the second option. See my full build.spec file at the bottom of this post. Pyinstaller displayed a lot of error messages while compiling my app, but it still compiled into a working .exe.

*To see your app's error message, run the resulting your_app.exe from the command line.* 
You can find it in the 'dist' folder that pyinstaller creates when you pass it the build.spec file. Set the dist folder as your working directory, type your_app.exe and hit enter. Once you are reading and fixing error messages, you're well on the way to creating your own desktop app.

**Flushing sys.stdout/Python printing for Windows:**

Python's design requires some code to play nice with Windows when it prints a statement. Simply add this to your .py file. I used write mode 'w'. What worked for me: don't pass 0 to fdopen(). This was contrary to `Gooey's instructions <http://chriskiehl.com/article/packaging-gooey-with-pyinstaller/>`__.

.. code-block:: python

   import os
   import sys
   nonbuffered_stdout = os.fdopen(sys.stdout.fileno(), 'w')
   sys.stdout = nonbuffered_stdout

**Fetching the local user's system information:**

In order to run on any user's system, we need to grab their local file paths. I accomplished this by referencing the sys._MEIPASS via the below code I found from a Stack Overflow post.

.. code-block:: python

   def resource_path(relative_path):
       """ Get absolute path to resource, works for dev and for PyInstaller"""
       base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
       return os.path.join(base_path, relative_path)

   temp_folder_path = getattr(sys, '_MEIPASS', os.getcwd())
   relative_path = resource_path(temp_folder_path)

**Adding library-specific patches:**

1. Below is the `fix <https://github.com/pyinstaller/pyinstaller/issues/3422>`__ I found for the Pandas library, which I added to my build.spec:

.. code-block:: python

   hiddenimports=['pandas._libs.tslibs.timedeltas','pandas._libs.tslibs.nattype',
   'pandas._libs.tslibs.np_datetime','pandas._libs.skiplist']

2. The Gooey library needs some special code added to the build.spec for its images and languages data. More details are found in this `blog post <http://chriskiehl.com/article/packaging-gooey-with-pyinstaller/>`__, written by the author of the Gooey library.

.. image:: https://pythonmarketer.files.wordpress.com/2018/11/will_ferrell_composure.jpg
   :alt: Will Ferrell Old School
   :class: wp-image-1535 alignright
   :width: 293px
   :height: 216px

**Last, but not least: don't panic.**

Compiling Python to Windows binary code sounds like a dauntingtask, but it wasn't nearly as complex as I feared. The folks behind Pyinstaller have done a great job of making it possible and, dare I say, simple. Stay calm, drink some coffee, dig in and welcome the challenge with a trial and error mentality. I was able to figure it out over the span of one Saturday. Good luck.

**Useful Resources:**

#. Pyinstaller Github - `If Things Go Wrong <https://github.com/pyinstaller/pyinstaller/wiki/If-Things-Go-Wrong>`__
#. Pyinstaller Documentation:`Using Pyinstaller Arguments <https://pyinstaller.readthedocs.io/en/stable/usage.html>`__
#. `Gooey Pyinstaller Instructions <http://chriskiehl.com/article/packaging-gooey-with-pyinstaller/>`__
#. `Pandas hiddenimports Discussion <https://github.com/pyinstaller/pyinstaller/issues/3422>`__

**Caveats:**

#. You should compile the program on the operating system it will be run on. There are options for creating a multi-os compatible package, but I did not attempt them.
#. Windows 7 is proven to work with Pyinstaller, per the documentation. It's also what I am running on. Other Windows systems older than Windows 10 may be less reliable.
#. I experienced trouble when passing arguments from the command line to pyinstaller and have so far been unable to get the console window to hide. Neither the -w, --windowed, --noconsole arguments seemed to work. I will update if I am able to find a solution.
#. Now that I am testing my compiled app, I am seeing 10x performance slowdowns when running as the final .exe vs. the original .py file. But at least the program runs correctly and still does so relatively quickly.
#. I also received the error: "Fatal error: Pyinstaller does not include a pre-compiled bootloader for your platform." I fixed this by upgrading to the latest version of Pyinstaller: 

::

    pip3 install --upgrade pyinstaller

My full build.spec file, modified from `here <http://chriskiehl.com/article/packaging-gooey-with-pyinstaller/>`__ :

.. code-block:: python

   # -*- mode: python -*-
   import gooey
   gooey_root = os.path.dirname(gooey.__file__)
   gooey_languages = Tree(os.path.join(gooey_root, 'languages'), prefix = 'gooey/languages')
   gooey_images = Tree(os.path.join(gooey_root, 'images'), prefix = 'gooey/images')

   a = Analysis(['your_program.py'],
                pathex=['C:\\Python36\\Lib\\site-packages\\your_appdir'],
                hiddenimports=['pandas._libs.tslibs.timedeltas', 'pandas._libs.tslibs.np_datetime', 'pandas._libs.tslibs.nattype', 'pandas._libs.skiplist'],
                hookspath=None,
                runtime_hooks=None,
                )
   options = [('u', None, 'OPTION')]
   a.datas += [('program_icon.ico', 'C:\\Python36\\Lib\\site-packages\\your_appdir\\program_icon.ico',  'DATA'),
               ('config_icon.png', 'C:\\Python36\\Lib\\site-packages\\your_appdir\\config_icon.png','DATA')]

   pyz = PYZ(a.pure) 
   exe = EXE(pyz,
             a.scripts,
             a.binaries,
             a.zipfiles,
             a.datas,
             options,
             gooey_languages,
             gooey_images,
             name='ADD YOUR APP NAME HERE',
             debug=True,
             strip=False,
             upx=True,
             console=True,
             icon=os.path.join('program_icon.ico'))
