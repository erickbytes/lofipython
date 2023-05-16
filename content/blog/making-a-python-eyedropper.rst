Making A Desktop Color Eyedropper in Python to Grab Color Values
################################################################
:date: 2018-09-14 05:45
:author: pythonmarketer
:category: coding, Colors, pandas, programming
:tags: atom, color, eyedropper, gui, python
:slug: making-a-python-eyedropper
:status: published

| **Goal:** recreate my resume in the dark Atom text editor theme (background and fonts).
| **Sub-goal:** find a color eyedropper to grab the actual color values of the Atom layout.

**Approach #1: find an Atom eyedropper package to grab the colors.**

My first thought was to find the easiest solution, within the packages of my Atom text editor. After searching Atom's packages, the two best potential solutions were `an-color-eyedropper <https://atom.io/packages/an-color-picker>`__ and `color picker <https://atom.io/packages/color-picker>`__. The an-color-eyedropper description sounds perfect: *"A simple "real" color picker. By "real" I mean it's able to pick colors anywhere on any screen." *\ Unfortunately it failed to install and displayed the error, "Unable to download 400 Bad Request Repository inaccessible". It seems to rely on the "python" Atom package which is now deprecated (`script <https://atom.io/packages/script>`__ 
is its successor). I was unable to find a repo anywhere by googling.

`Color picker <https://atom.io/packages/color-picker>`__ has easy-to-follow instructions and installed with no problem. It allows you to quickly select any color visually with sliders. Then the RGB or Hexadecimal values of your color are added as text in the editor in proper format. However, we are looking for a color grabber to pull colors from a screen object. This is more of a productivity enhancing and color exploration tool for programmers. On to Python options.

**Approach #2: Use the python tkcolorpicker package to grab the colors.**

| The first thing I found on Google was `tkcolorpicker <https://pypi.org/project/tkcolorpicker/>`__, a package that uses the `tkinter <https://pythonmarketer.wordpress.com/2016/02/29/tkinter-and-python-libraries/>`__ library. I couldn't tell exactly what it was, so let's find out. First, install via `pip <https://pythonmarketer.wordpress.com/2018/01/20/how-to-python-pip-install-new-libraries/>`__:

``python -m pip install tkcolorpicker``

| Then run the below script. Cool gadget for sure, but also not quite what I was looking to use. It allows selection of a color with sliders or input values, similar to Atom's color picker, but for user input rather than color picking. Nice little tool. :D
| |color_picker_gui|

.. code-block:: python

   import tkinter as tk
   import tkinter.ttk as ttk
   from tkcolorpicker import askcolor

   root = tk.Tk()
   style = ttk.Style(root)
   style.theme_use('clam')
   hex_code, RGB_code = askcolor((255, 255, 0), root) 
   print(hex_code, RGB_code)
   root.mainloop()

``askcolor()`` returns a tuple with both the RGB and hex codes selected by the user. Above, we are unpacking that tuple into the ``hex_code`` and ``RGB_code`` variables.

**Approach #3: Use the Python eyedropper package to grab the colors.**

I then found `eyedropper <https://github.com/umluizlima/eyedropper>`__ for Windows, which has a minimalist repository and offers a simple approach to desktop eyedropper functionality. Install eyedropper via `pip <https://pythonmarketer.wordpress.com/2018/01/20/how-to-python-pip-install-new-libraries/>`__: ``python -m pip install eyedropper``

.. image:: https://pythonmarketer.files.wordpress.com/2018/09/pyeyedropper_start.png
   :alt: pyeyedropper_start
   :class: size-full wp-image-1458 alignright
   :width: 239px
   :height: 140px

Hover your mouse over the object you want to grab the color from (in my case, the Atom text editor background). Then `following these instructions <https://github.com/umluizlima/eyedropper>`__:

Alternatively, I was able to run eyedropper from the command line by entering: ``py -m eyedropper``

.. image:: https://pythonmarketer.files.wordpress.com/2018/09/pasted_hex2.png
   :alt: pasted_hex2
   :class: alignnone size-full wp-image-1461
   :width: 766px
   :height: 74px

.. image:: https://pythonmarketer.files.wordpress.com/2018/09/ccvoyfiugaa4djd.jpg
   :alt: CCvOYFiUgAA4DJd
   :class: alignright
   :width: 151px
   :height: 116px

**Mission possible.** Then I hit ctrl+v in a text file and there was the hex code for my Atom background. Some of the colors that eyedropper grabbed were nearly identical to those in the Atom text editor dark theme. Others were not quite the same. I made slight eyeball adjustments to the colors for some of the fonts.

Here's the end result:\ `See My Resume via Dropbox <https://www.dropbox.com/s/g5uiaqaa5nb3fgn/Developer_Resume_Invert_v2.docx?dl=0>`__\ :D

Why not `use Python to convert hex to RGB? <https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python>`__
----------------------------------------------------------------------------------------------------------------------------------

Microsoft Word uses RGB codes but eyedropper gave us hex. To convert, I found `this website <https://www.webpagefx.com/web-design/hex-to-rgb/>`__ practical and quick.

**Alternatively, you could** `convert a hex code to RGB with python: <https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python>`__

.. code-block:: python

   hex_code = input('Enter hex: ').lstrip('#')
   RGB_code = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
   print('RGB =', RGB_code)

.. image:: http://pythonmarketer.files.wordpress.com/2018/09/e084c-rgb_to_hex-e1581286493172.jpg
   :alt: rgb_to_hex
   :class: alignnone size-full wp-image-2308
   :width: 805px
   :height: 83px

What the hay, let's use `pd.read_clipboard() <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_clipboard.html>`__ to get the hex codes.
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Once eyedropper sends the color values to your system's clipboard, there are multiple ways to access them. This alternative uses pandas.

**Installing pandas and**\ `pyperclip <https://github.com/asweigart/pyperclip>`__\ **with pip:**

::

   python -m pip install pandas
   python -m pip install pyperclip

**On Linux, install**\ `xclip <https://github.com/astrand/xclip>`__\ **or**\ `xsel: <https://askubuntu.com/questions/705620/xclip-vs-xsel>`__\  ``sudo apt-get install xclip``\ **

**To get the clipboard contents with pandas:**

.. code-block:: python

   import pandas as pd
   hex_code_df = pd.read_clipboard() 
   print(hex_code_df.head())

**Supplementary Notes and Links**

-  Here's a Python `eyedropper script <https://github.com/gigawhitlocks/eyedropper/blob/master/x-color-get.py>`__ featuring the `pillow <https://pillow.readthedocs.io/en/5.2.x/index.html>`__ and `xlib <https://github.com/python-xlib/python-xlib>`__ libraries that I was unable to get working.
-  I didn't try `ColorCop for Windows <http://colorcop.net/>`__, but it may be a non-Python alternative.
-  **Did you know?** Python 2 had a `ColorPicker <https://docs.python.org/2/library/colorpicker.html>`__ module that is not in Python 3.
-  `How pandas read_clipboard method works <https://dev.to/espoir/how-pandas-readclipboard-method-works-ake>`__
-  `pandas to_clipboard and read_clipboard source code <https://github.com/pandas-dev/pandas/blob/v1.0.1/pandas/io/clipboards.py#L10-L76>`__
-  This `desktop tool <https://github.com/Toinane/colorpicker>`__ has great U/X and an eyedropper feature. It runs on Electron, a Javascript based framework. Coincidentally, Electron was used to build Atom.

 

.. |color_picker_gui| image:: https://pythonmarketer.files.wordpress.com/2018/09/color_picker_gui.png
   :class: wp-image-1462 alignright
   :width: 301px
   :height: 315px
