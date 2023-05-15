What I Learned from Black, Python's "Uncompromising" Code Formatter
###################################################################
:date: 2021-09-23 10:12
:author: pythonmarketer
:category: coding, programming, python
:tags: Black Python, PEP-8, writing code
:slug: a-learning-use-case-for-black-python-code-formatter
:status: published

Black is a code formatting tool that I have been testing out recently to see what the hype is about. It is the defacto "uncompromising code formatter in Python". I normally do not use any code formatters since I'm not required to use them. This short post aims to convince you that Black is an insightful way to see the parts of your code that are dangerously unreadable.

I have found it interesting to see what black does with my gnarliest code. It has taught me what is considered "good formatting" by some Pythonistas. The areas where I see the most improvement is how it enforces `PEP-8 <https://www.python.org/dev/peps/pep-0008/>`__'s characters per line limit. Often before, I didn't know how to break my code into several lines. My scripts tended to have one-liners trailing off the edge of my text editor. Black teaches you new ways to organize your code and makes it easier to understand. Now I write my code like Black the first time instead of letting it trail off the screen.

Initially I was hesitant to try Black because I didn't want to sabotage my own code style. But since running Black on a few of my scripts, it has taught me new ways to write code. Give Black a chance and you will learn how to write more readable Python.

Here's the project on GitHub: https://github.com/psf/black
