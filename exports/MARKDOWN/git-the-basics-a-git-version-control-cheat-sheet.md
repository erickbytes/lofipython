Title: "Git" The Basics: A Version Control Cheat Sheet
Date: 2020-01-25 05:06
Author: pythonmarketer
Category: coding, command prompt, data analysis, git, programming, software
Tags: github, terminal, version control
Slug: git-the-basics-a-git-version-control-cheat-sheet
Status: published

*I am finally starting to understand [git version control](https://en.wikipedia.org/wiki/Git)! It makes developing a project on different computers easy. Some of these notes were picked up from the super informative [Reproducible Data Analysis in Jupyter video series](https://www.youtube.com/watch?v=_ZEWDGpM-vM) by Jake VanderPlas, author of the [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/).*

*First, [go here](https://git-scm.com/downloads), download and install git if you haven't yet. Alright, here are my go-to steps and commands for git:*

**Beginning a New Project With Git**

1.  Create new repository on GitHub
2.  Add a README
3.  Add a Python gitignore
4.  Add a license (Jake V. used an MIT license)

**Clone Any Repository from GitHub**

1.  Visit your new project, or any GitHub project, click the green "Clone or download" button and copy the link.
2.  In your terminal or command prompt, navigate to the directory where you want to clone your project.
3.  In terminal, enter: `git clone PASTE_URL_HERE`
4.  Now cd into your project folder.

**Push Your Local Computer Changes to the Master Repository**

Let's say you did some work on your computer and want to push the changes to GitHub. Enter these commands in terminal:

1.  `git add .`
2.  `git commit -m "Add your commit note here"`
3.  `git push origin master`

\*Above: `git add .` = stage all files in project directory for master

\*\*Substitute `git add path\to\file\here` to stage only a single file to add to your master repository.

**Fetch Changes From Master Branch to Your Local Computer**

I like to update my local computer with any master branch changes before beginning work on it. Enter these commands in terminal:

1.  `git fetch`
2.  `git pull origin master`

**Review Merge Conflicts**

Sometimes, your code may conflict with changes in the master branch. You'll find out if you try to push or pull changes and the auto-merge fails. Use "git status" to locate the files with the conflicts. Enter in your terminal:

1.  `git status`
2.  Then [follow these instructions](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-using-the-command-line) to review the merge conflicts.

See also: [Resolving Conflicts - Virtualenv Documentation](https://dont-be-afraid-to-commit.readthedocs.io/en/latest/git/conflicts.html)

**Or maybe you want to discard any local changes, then merge:**

1.  `git fetch`
2.  `git checkout .`
3.  `git pull origin master`

**Recovering from a Corrupted Repository**

`git fsck --full --no-dangling`

[Additional Reading](https://mirrors.edge.kernel.org/pub/software/scm/git/docs/user-manual.html#recovering-from-repository-corruption)

**Supplementary Reading**

[CS Visualized: Useful Git Commands](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1)

[8 Git Commands I Use Every Day](https://lanraccoon.com/2018/8-git-commands-i-use-everyday/)

[On Commit Messages](http://who-t.blogspot.com/2009/12/on-commit-messages.html)

[Pandas Library Git Workflows](https://github.com/pandas-dev/pandas/wiki/Git-Workflows)
