"Git" The Basics: A Version Control Cheat Sheet
###############################################
:date: 2020-01-25 05:06
:author: pythonmarketer
:category: coding, command prompt, data analysis, git, programming, software
:tags: github, terminal, version control
:slug: git-the-basics-a-git-version-control-cheat-sheet
:status: published

I am finally starting to understand `git version control <https://en.wikipedia.org/wiki/Git>`__! It makes developing a project on different computers easy. Some of these notes were picked up from the super informative `Reproducible Data Analysis in Jupyter video series <https://www.youtube.com/watch?v=_ZEWDGpM-vM>`__ by Jake VanderPlas, author of the `Python Data Science Handbook <https://jakevdp.github.io/PythonDataScienceHandbook/>`__.

First, `go here <https://git-scm.com/downloads>`__ to download and install git if you haven't yet. Alright, here are my go-to steps and commands for git:

**Beginning a New Project With Git**

#. Create new repository on GitHub
#. Add a README
#. Add a Python gitignore
#. Add a license. Jake V. used an MIT license.

**Clone Any Repository from GitHub**

#. Visit your new project, or any GitHub project, click the green "Clone or download" button and copy the link.
#. In your terminal or command prompt, navigate to the directory where you want to clone your project.
#. In terminal, enter: git clone REPO_URL
#. Now cd into your project folder.

**Push Your Local Computer Changes to the Remote Repository**

Let's say you did some work on your computer and want to push the changes to GitHub. Enter these commands in terminal:

.. code-block:: console

    git add .
    git commit -m "Add your commit note here"
    git push origin main

Above: "git add ." stages all files in project directory for main. Add your commit message, then push your changes to the remote repo.

**Fetch Changes From Main Branch to Your Local Computer**

You might want to update your local computer with any main branch changes before beginning work on it. Enter these commands in terminal:

.. code-block:: console

    git fetch
    git pull origin main

**Review Merge Conflicts**

Sometimes, your code may conflict with changes in the main branch. You'll find out if you try to push or pull changes and the auto-merge fails. Use "git status" to locate the files with the conflicts. Enter in your terminal:

.. code-block:: console

    git status

Then `follow these instructions <https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-using-the-command-line>`__ to review the merge conflicts.

**Or maybe you want to discard any local changes, then merge:**

.. code-block:: console

    git fetch
    git checkout
    git pull origin main

**Recovering from a Corrupted Repository**

.. code-block:: console

    git fsck --full --no-dangling

`Additional Reading <https://mirrors.edge.kernel.org/pub/software/scm/git/docs/user-manual.html#recovering-from-repository-corruption>`__


**Revert local repo to a previous commit, then push your repo to the remote.**

.. code-block:: console
    
    git reset --hard rollback_commit_id
    git push origin main


**Supplementary Reading**

`CS Visualized: Useful Git Commands <https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1>`__

`8 Git Commands I Use Every Day <https://lanraccoon.com/2018/8-git-commands-i-use-everyday/>`__

`On Commit Messages <http://who-t.blogspot.com/2009/12/on-commit-messages.html>`__

`Pandas Library Git Workflows <https://github.com/pandas-dev/pandas/wiki/Git-Workflows>`__
