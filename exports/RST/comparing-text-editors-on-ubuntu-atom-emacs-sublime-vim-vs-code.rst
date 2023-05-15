Comparing Text Editors on Ubuntu: Atom, Emacs, Sublime, Vim & VS Code
#####################################################################
:date: 2019-12-26 01:25
:author: pythonmarketer
:category: coding, Linux, Scripts, software, Ubuntu
:tags: atom, emacs, sublime, text editors, vim, vs code
:slug: comparing-text-editors-on-ubuntu-atom-emacs-sublime-vim-vs-code
:status: published

The text editor is a core tool for writing software. I've always used Atom. Lately, I've noticed my Atom text editor was bogging down on my Chromebook running Ubuntu 16.04. Keystrokes and mouse movements were lagging and slowing my coding down. I'm also getting low on disk space, which may be a related issue.

You'll want to choose a text editor based on how it suits your own needs. In this case, I want a light-weight, responsive editor with no lag. Bells and whistles are less important. I'm also looking to minimize disk space required.

I decided to compare the `apt installed <https://codeburst.io/a-beginners-guide-to-using-apt-get-commands-in-linux-ubuntu-d5f102a56fc4>`__ package size of some popular editors. First, I installed Atom, Emacs, Sublime, VS Code and Vim using the Ubuntu 16.04 terminal. You could also consider using `IDLE, python's built-in text editor <https://docs.python.org/3/library/idle.html>`__ as an alternative that requires no additional software.

**Then I** `found the below command <https://unix.stackexchange.com/questions/40442/which-installed-software-packages-use-the-most-disk-space-on-debian>`__ **to list all installed apt packages by package size on Ubuntu:**

::

    dpkg-query -Wf '${Installed-Size}\t${Package}\n' | sort -n

**Here's the terminal output with relevant packages in Megabytes (including Firefox for comparative size):**

::

   136    emacsen-common
   366 vim-common
   1071    vim-tiny
   2400    vim
   21648   emacs26
   26870   vim-runtime
   34033   sublime-text
   70307   emacs26-common
   193694  firefox
   236965  code
   607932  atom

Atom is by far the largest package I downloaded. It is nearly three times the size of VS Code, my second largest package. The next largest was my web browser, Firefox. Most of the other packages I downloaded were considerably smaller.

   Side note: I also found out Ubuntu 16.04 ships with a stripped down version of Vim called `vim-tiny <https://askubuntu.com/questions/104138/what-features-does-vim-tiny-have>`__.

**Total Installed Package Sizes in Megabytes (Smallest to Largest)**

Some of these editors have multiple packages they are dependent on.

+-------------+-------------------------------+-----------------------------------------+
| Text Editor | Total Installed Packages Size | **Packages Installed**                  |
+-------------+-------------------------------+-----------------------------------------+
| Vim         | 29,636 MB                     | vim, vim-common, vim-runtime            |
+-------------+-------------------------------+-----------------------------------------+
| Sublime     | 34,033 MB                     | sublime-text                            |
+-------------+-------------------------------+-----------------------------------------+
| Emacs       | 91,955 MB                     | emacs26-common, emacs26, emacsen-common |
+-------------+-------------------------------+-----------------------------------------+
| VS Code     | 236,965 MB                    | code                                    |
+-------------+-------------------------------+-----------------------------------------+
| Atom        | 607,932 MB                    | atom                                    |
+-------------+-------------------------------+-----------------------------------------+

**Results: Vim and Sublime win for smallest installed package size.**

-  Vim is the lightest-weight package of these 5 popular text editors, with Sublime not far behind. Emacs is comparable to them for usability and relatively small.
-  Atom is nearly 3x the size of VS Code and 20x the size of Vim. Atom and VS Code are larger than the Firefox browser package, the third largest of any downloaded package on my system.
-  I tested out all of the editors by opening the same Python file and making some edits. I found Vim, Emacs and Sublime were much more responsive than Atom and VS Code.

**Conclusion: All Editors Are Not Created Equal**

These are fine editors when paired with the right machine and developer needs. In my case, a Chromebook running Linux installed with `Crouton <https://github.com/dnschneid/crouton>`__, a few editors are performing faster and taking up less space. I've chosen Sublime or Emacs as my editor for this computer. One slightly annoying feature of Sublime is being prompted to buy the paid version from the trial version. Atom, Emacs, Vim and VS Code are free. Vim might be a good option if I ever decide to conquer its `notoriously high learning curve <https://stackoverflow.com/questions/11828270/how-do-i-exit-the-vim-editor>`__.

**[Bonus] Find the size of all packages matching with "vim" in their name:**

::

    dpkg-query -Wf '${Installed-Size}\t${Package}\n' | sort -n | grep vim

**Terminal output from above command:**

::

   366 vim-common
   1071 vim-tiny
   2400 vim
   26870 vim-runtime

**Additional Reading**

`What is the best lightweight text editor? <https://www.quora.com/What-is-the-best-lightweight-text-editor>`__

`Atom as an Editor is Too Big <https://github.com/atom/atom/issues/9755>`__
