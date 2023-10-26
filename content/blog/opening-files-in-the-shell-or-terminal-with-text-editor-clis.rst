Opening Files From The Terminal With Text Editor CLIs
######################################################
:date: 2023-08-07 13:56
:author: lofipython
:category: coding, programming, text editors
:tags: sublime command line, vscode command prompt, text editor CLI, emacs open text file, vs code open script, open in notepad++ file
:slug: opening-files-in-the-shell-or-terminal-with-text-editor-clis
:status: published


Most text editors can open files from a computer's command line shell. Here are 8 different text editor commands for opening a file:


**IDLE (Python's Built-in Editor)**

.. code:: console

   idle file.py


.. image:: {static}/images/idlecli.png
  :alt: CLI help options for Python's IDLE text editor

image source: `IDLE documentation <https://docs.python.org/3/library/idle.html#startup-and-code-execution>`__


**Sublime**

.. code:: console

   subl template.rst


.. image:: {static}/images/sublimeeditorexample.png
  :alt: using subl CLI to open files in Sublime


**VS Code**


.. code:: console

   code file.py


**Atom**

.. code:: console

   atom file.py


**Emacs**


.. code:: console

   emacs -nw file.txt

source: `Stack Overflow user Anthon <https://unix.stackexchange.com/questions/165724/open-an-emacs-file-from-terminal>`__


**Notepad++**

.. code:: console

   start notepad++ file.py


source: `W3 Schools <https://www.w3schools.io/editor/notepad++-open/>`__


**TextEdit**

.. code:: console

   open -a TextEdit file.txt


source: `Stack Overflow user robmathers <https://www.w3schools.io/editor/notepad++-open/>`__


**Vim**

.. code:: console

   :e file.txt


source: `confirm blog <https://blog.confirm.ch/mastering-vim-opening-files/>`__


The ability to quickly pop open and view a file is essential. Ubuntu has the cat command to print a file's contents to the terminal screen also if you don't need to edit it. Tools like `sed <https://www.gnu.org/software/sed/manual/sed.html>`__ and `awk <https://www.geeksforgeeks.org/awk-command-unixlinux-examples/>`__ are useful for command line file editing if you prefer to keep it in the terminal.

Want to read more about text editors? Check out my text editor file size comparison `here <https://lofipython.com/comparing-text-editors-on-ubuntu-atom-emacs-sublime-vim-vs-code>`__.
