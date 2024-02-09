Ways to Free Up Disk Space on Your Computer for Python Developers
#################################################################
:date: 2024-02-09 14:30
:author: lofipython
:category: computer maintenance, Python, Ubuntu, disk space
:tags: how to free up disk space, creating extra linux ubuntu disk space, cleaning up disk space on hard drive, managing linux files, clearing python cache and libraries
:slug: ways-to-free-up-disk-space-on-your-computer
:status: published

Below are some ways to free up disk space on your computer. This will be most helpful
for Ubuntu users and Python developers. The pip examples show what I used on my Python
version 3.11, so if you're running a different version use that number, like
pip3.12, pip3.10, pip3.9, etc.

**Benchmark your current disk space.**

Before you start freeing up space, you might want to see the current state of your
hard drive. You can print human readable disk space stats on Ubuntu with the df command.

.. code:: console

  df -h


.. image:: {static}/images/readdiskspacedfh.png
  :alt: read disk space stats on Ubuntu

**Clear your browser cache.**

.. image:: {static}/images/clearchromecache.png
  :alt: clear web browser cache


**Purge your pip cache.**

Before purging the Python pip package manager's cache, you can use the pip cache info command to see how much
storage is consumed by the cache.

.. code:: console

   pip3.11 cache info

Next, use the `pip cache purge command <https://pip.pypa.io/en/stable/cli/pip_cache/>`__
to clear up space on your system. Pip will print how many files it removed to the terminal.

.. code:: console

   pip3.11 cache purge


.. image:: {static}/images/pipcachepurge.png
  :alt: clear the pip package manager cache

**Uninstall unnecessary Python libraries.**

I tend to build up modules that I installed to see how it works or to quickly test something out,
then never use again. It makes sense to cull your pip installed libraries occasionally.
Be aware that sometimes an unknown module may be required dependency of a module
you want to use. First, use the pip list command to see your installed libraries:

.. code:: console

   pip3.11 list

.. image:: {static}/images/piplist.png
  :alt: view pip installed libraries

The pip uninstall command makes removing Python libraries easy.
For example, let's say you're already using both the ruff Python linter and black.
The ruff module recently introduced a new formatter that is more or less identical
to Black. Therefore, I can uninstall black and use ruff format command instead
to format my code.

.. code:: console

   pip3.11 uninstall black


**Run the autoremove Linux commands.**

  autoremove is used to remove packages that were automatically installed to satisfy
  dependencies for other packages and are now no longer needed as dependencies changed
  or the package(s) needing them were removed in the meantime.
  - `Linux apt Man Pages <https://manpages.ubuntu.com/manpages/xenial/man8/apt.8.html>`__

.. code:: console

  sudo apt-get autoremove


**Run the clean and autoclean Linux command.**

.. code:: console

    sudo apt-get clean
    sudo apt-get autoclean

Read more on Ask Ubuntu: `What is the difference between the options "autoclean" "autoremove" and "clean"? <https://askubuntu.com/questions/3167/what-is-difference-between-the-options-autoclean-autoremove-and-clean>`__

**Purge unnecessary Linux packages.**

If you are certain a Linux package can be deleted, the apt-get purge command remove a
package and all configuration files from your computer. Be careful not to remove
any critical Linux packages.

.. code:: console

    sudo apt-get purge <package-name>


**Find and delete your largest Linux files.**

This command prints the largest files on your root Linux file system. Then you can
use the rm command to remove the file. Hint: sometimes PDF files can be deceptively
large and can be good targets to free up space.

.. code:: console

    sudo find / -xdev -type f -size +25M -exec du -sh {} ';' | sort -rh | head -n 20
    rm ~/large_file.pdf

That summarizes a few ways Ubuntu users and Python developers can add some extra available
disk space. It can definitely be frustrating to watch an install fail because there's
no more space on your computer. These are a few strategies you can deploy to make room
to operate on a disk space constrained system.
