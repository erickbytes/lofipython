Opening Files From The Terminal With Text Editor CLIs
######################################################
:date: 2023-08-07 13:56
:author: lofipython
:category: coding, programming, text editors
:tags: sublime command line, vscode command prompt, text editor CLI, emacs open text file, vs code open script, open in notepad++ file
:slug: opening-files-in-the-shell-or-terminal-with-text-editor-clis
:status: published


Many text editors have the ability to open files from a computer's shell. Here are a few text editor commands that I've learned for opening a file automatically from the command line:


**Sublime**

.. code:: console

   subl file.txt


**VS Code**


.. code:: console

   code file.py


**Emacs**


.. code:: console

   emacs -nw file.txt

source: `Stack Overflow user Anthon <https://unix.stackexchange.com/questions/165724/open-an-emacs-file-from-terminal>`__


**Notepad++**

.. code:: console

   start notepad++ file.rst


source: `W3 Schools <https://www.w3schools.io/editor/notepad++-open/>`__


.. image:: {static}/blog/images/sublimeeditorexample.png
  :alt: using subl CLI to open files in Sublime


The ability to quickly pop open and view a file is essential. Ubuntu has the cat command to print a file's contents to the terminal screen also if you don't need to edit it. Tools like `sed <https://www.gnu.org/software/sed/manual/sed.html>`__ and `awk <https://www.geeksforgeeks.org/awk-command-unixlinux-examples/>`__ are useful for command line file editing if you prefer to keep it in the terminal.

Can't get enough text editors? Read more about text editors in my comparison of their file sizes `here <https://lofipython.com/comparing-text-editors-on-ubuntu-atom-emacs-sublime-vim-vs-code>`__.
