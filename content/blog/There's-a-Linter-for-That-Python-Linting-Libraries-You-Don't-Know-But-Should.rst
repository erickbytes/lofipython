There's a Linter for That! Python Linter and Formatter Libraries You Gotta Know
################################################################################
:date: 2023-07-23 21:10
:author: lofipython
:category: coding, programming, python, linting, tools
:tags: python linters, linting tools, python RST linting, SQL linting, code linting, HTML linter, Markdown linter
:slug: There's-a-Linter-for-That-Python-Linting-Libraries-You-Should-Know
:status: published

Linters exist for almost every kind of structured document. Python code, SQL, reStructuredText and many data formats can be improved with a linting library. Python's ecosystem has no shortage of formatters and linters. 

In this post, I'll highlight the typical players and some niche linters you might not have heard of! The best quality of linters is their ability to find potential problems in your code by enforcing domain-specific rules. In return, you receive a list of hints for fixing anti-patterns, inconsistencies or unused code to remove. Many linters also offer document reformatting capabilities like the ubiquitous black library for Python code.

**Python Linters and Formatters You Gotta Know**

* `ruff <https://github.com/astral-sh/ruff>`__: the lean and fast linter library that's gotten a lot of people's attention. For good reason, it's the easiest and fastest Python code linter, running rust under the hood. In my experience, using ruff has made me a more efficient Python programmer. The ruff CLI's **--fix**  argument is a nice touch for automatically fixing up your code.



**Run ruff on your Python script for quick and easy linting.**

.. code:: 

    pip install ruff
    ruff do_stuff.py
    # Find Python code errors and fix them with ruff.
    ruff do_stuff.py --fix



.. image:: {static}/blog/images/sqlfluffexample.png
  :alt: sqlfluff SQL linting CLI tool


* `sqlfluff <https://docs.sqlfluff.com/en/stable/index.html>`__: "The SQL linter for humans", sqlfluff is a linter and code reformatting tool to tidy up your database queries. sqlfluff does the little things like uppercase your keywords, add whitespace where appropriate, check syntax and in general clean up your scripts. The CLI is configurable for nearly all dialects from DuckDB, T-SQL, Redshift, MySQL, to SQLlite and more. Check the `sqlfluff Github repo <https://github.com/sqlfluff/sqlfluff>`__ for all their supported SQL dialects or use the **sqlfluff dialects** command to list them in your shell. This is the library I want to tell every Python programmer about right now, along with ruff. SQL is everywhere, we all use it. SQL linters are not something most people even know exist. Next time you need to fix a broken SQL script or clean up some legacy code, enter this into your shell:

.. code:: 

    pip install sqlfluff
    # Lint your SQL code.
    sqlfluff lint stuff.sql


.. code:: 

    # Fix your SQL file in the PostgreSQL dialect.
    sqlfluff fix stuff.sql --dialect postgres


.. code:: 

    # Check available SQL dialects.
    sqlfluff dialects



* `json.tool <https://docs.python.org/3/library/json.html#module-json.tool>`__: a Python standard library CLI tool with JSON validation abilities. If you're working with json, remember this stock Python tool.


**Validate JSON with a built-in python CLI tool.**


.. code:: 

    echo '{1.2:3.4}' | python -m json.tool



* `pylint <https://pypi.org/project/pylint/>`__: commonly used static code analyser that enforces PEP-8 and other rules in your code.



**Use pylint to improve to improve your Python scripts.**

.. code:: 

    pip install pylint
    pylint do_stuff.py



* `black <https://pypi.org/project/black/>`__: a must-mention, this Python code formatter with some linting-like qualities if your code has syntax errors. I now run it on every script I write.

**Reformat your code with black.**


.. code:: 

    pip install black
    python -m black do_stuff.py


* `yamllint <https://pypi.org/project/yamllint/>`__: YAML is unavoidable as a configration staple in tons of modern software. It gets heaps of praise for its readability. I appreciated yamllint's instrospective linter when trying to figure out why my YAML config was broken. 



**Lint your YAML files.**


.. code:: 

    pip install --user yamllint
    yamllint config.yaml



.. image:: {static}/blog/images/yamllintexample.png
  :alt: yamllint YAML linting CLI tool



* rstfmt and restructuredtext-lint (`read more <https://pypi.org/project/restructuredtext-lint/>`__): Both of these reStructuredText format linter libaries offer code reformatting and linting abilities for reStructuredText files (.rst). I favored restructuredtext-lint, due to its rst-lint CLI tool. I used it to fix and tested it on old posts from this blog. Beware that using a reformatter might surface buried errors found by linting the RST, which you'll need to resolve by reading somewhat cryptic RST error messages given by your linter like "hyperlink mismatch, 1 reference but 0 targets". At least the line number is provided so you have a relative scope of where the error is coming from. rstfmt is another `Python CLI tool <https://pypi.org/project/rstfmt/>`__ in this space. One note of using these tools is to watch out for unwanted changes. One effect I saw was having code blocks auto-converted from Python formatting to regular code formatting.



**Lint and reformat your .rst documents.**

.. code:: 

    pip install restructuredtext-lint
    rst-lint post.rst


**Pelican + .rst or .md**


    RST is one of two `pelican\-import command line tool <https://docs.getpelican.com/en/latest/importer.html>`__ conversion options by the `Pelican <https://docs.getpelican.com/en/3.6.3/quickstart.html>`__ static site generator library, along with Markdown (.md). RST is the format this blog is composed in. Pelican has linting-like functionality when you run its **pelican content** command to compile your static site.



Although I haven't used them personally, it's worth mentioning popular libraries like `pyflakes <https://pypi.org/project/pyflakes/>`__ and `flake8 <https://pypi.org/project/flake8/>`__ for linting Python code. ruff supports some of these libraries also. Check out `pymarkdownlint <https://pypi.org/project/pymarkdownlnt/>`__ for linting Markdown documents. While researching for this post, I even stumbled upon an HTML linting command line tool that exists. `html-linter <https://pypi.org/project/html-linter/>`__ applies linting to your HTML code. Starting to think that behind every seasoned Python programmer is a thick stack of linters! When it comes to fixing and refactoring old documents and code, linters and auto-formatters go hand in hand as invaluable tools.


**Lint your Markdown documents.**


.. code:: 
    
    pip install pymarkdownlnt
    pymarkdown scan example.md


**Lint your HTML documents.**


.. code:: 
    
    pip install html-linter
    html_lint.py filename.html


**Supplementary Reading + Documentation**

`7 Python libraries for more maintainable code <https://opensource.com/article/18/7/7-python-libraries-more-maintainable-code>`__

`reStructuredText documentation <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__

`sqlfluff CLI documentation reference <https://docs.sqlfluff.com/en/stable/cli.html>`__
