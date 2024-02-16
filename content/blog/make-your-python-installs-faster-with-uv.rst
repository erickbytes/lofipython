Make Your Python Installs Faster With uv
##########################################
:date: 2024-02-16 12:33
:author: lofipython
:category: coding, programming, python
:tags: optimizing python installs, uv python installation, installing python packages with uv
:slug: make-your-python-installs-faster-with-uv
:status: published

For a several years, pip and `pip-tools documentation <https://pypi.org/project/pip-tools/>`__ have become distinguished in Python packaging 
for their usability and ubiquity. Recently there has been some interesting new developments 
in the realm of Python packaging tools. In a trend that started around 2022, there has been an 
ongoing "Rustification" of Python tooling.

First, rye was released in pursuit of a "cargo for Python". Cargo is Rust's package manager. It seems to 
have inspired Python developers to keep trying to improve on what we have with pip.

While this was happening, in secret the creator of ruff was also working on yet another hybrid 
Rust + Python package manager named uv. There's seemingly no end to this man's projects! 
ruff quickly supplanted the incumbent Python linters to become a favorite among Python developers. 
Could lightning strike twice for the creator of ruff? Seems he won't be a one-hit wonder when it 
comes to developing hit Python packages.

    uv is 8-10x faster than pip and pip-tools without caching, and 80-115x faster 
    when running with a warm cache 
    - Charlie Marsh, Astral Blog, https://astral.sh/blog/uv

Improving Python packaging is an audacious and challenging task. Part of the problem 
is that out of the box Python installs can be tough to reason about for new Python developers. 
Not to mention the labor of explaining the purpose of virtual environments in Python coding via venv. 
One perk of uv is that it includes virtual environments in its workflow.

For more experienced developers, uv is a way you can make your code run much faster if you 
need to install a Python package everytime it runs. For example, if you're running a Python script 
on a Docker image, Python needs to install your packages everytime the image is run. In this case, 
a modest 8x speedup might shave off a shocking amount of time it takes your code to execute. Now, 
imagine an 80-115x speedup with caching. That's an incredible improvement we can now make with uv!

   uv is designed as a drop-in replacement for pip and pip-tools, and is 
   ready for production use today in projects built around those workflows.
   - Charlie Marsh, Astral Blog, https://astral.sh/blog/uv

This seems like an instance where two developers identified the same core problem 
and are now combining their efforts. Sounds like a win for all Python developers. Armin Ronacher, the
creator of the Flask web framework and Charlie Marsch with the proven success of ruff are converging 
to tackle one of Python's biggest pain points. It sounds like they could be merged into a python packaging 
super tool at some point:

   **Will Rye retired for uv?**
   Not today, but the desire is that these tools eventually converge into one.
   - Rye Grows with uv, Armin Ronacher, https://lucumr.pocoo.org/2024/2/15/rye-grows-with-uv/

Per Armin's recent blog post, Rye is probably not the final solution. He thinks rye will get absorbed 
into a more fleshed out project like uv. It sounds like Python packaging will continue evolving and improving,
a welcome sight for Pythonistas!


.. image:: {static}/images/uv-install-benchmarks.png
  :alt: optimize python installs with uv

*Image Source: `uv: Python Packaging in Rust <https://astral.sh/blog/uv>`__*


**Install uv and rye**

.. code:: console

   pip install uv
   pip install rye

   # Alternative install for uv with curl
   curl -LsSf https://astral.sh/uv/install.sh | sh
   # Alternative Install for rye on Linux and Mac
   curl -sSf https://rye-up.com/get | bash 


**Create a Virtual Environment With uv**

.. code:: console

   uv venv  # Create a virtual environment at .venv.


**Installing a New Module With uv**

.. code:: console

   uv pip install requests


**pip sync a requirements.txt file with uv**

.. code:: console

   uv pip sync requirements.txt  # Install from a requirements.txt file.


**Optional: Configure rye on Top of uv**

.. code:: console
   
   rye config --set-bool behavior.use-uv=true


**Create new Python project With Rye**

.. code:: console

   rye init my-project
   rye pin 3.10
   rye add black
   rye sync
   rye run black


**uv and rye Documentation Links**

`uv: Python Packaging in Rust <https://astral.sh/blog/uv>`__

`uv Github Repo <https://github.com/astral-sh/uv>`__

`Rye Grows with uv <https://lucumr.pocoo.org/2024/2/15/rye-grows-with-uv/>`__

`Rye User Guide <https://rye-up.com/guide/basics/#working-with-the-project>`__


.. image:: {static}/images/uv-tweet.png
  :alt: optimizing code with uv tweet
