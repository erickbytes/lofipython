How to Check Github Repo Star Counts With Python
################################################
:date: 2022-10-10 00:08
:author: pythonmarketer
:category: APIs, coding, programming, python
:tags: github api, github stars python, repo star counts
:slug: how-to-check-github-repo-star-counts-with-python
:status: published

Snooping through my package list, I noticed the `PyGithub library <https://github.com/PyGithub/PyGithub>`__ was installed. Its repo boasts "Typed interactions with the GitHub API v3". I googled the package, wanting to check in on the repos I profiled in an `earlier post about static site generators <https://lofipython.com/a-brief-summary-of-promising-python-static-site-generators/>`__.

I drafted the code below after noticing the `repo.stargazer_count <https://pygithub.readthedocs.io/en/latest/examples/Repository.html#get-count-of-stars>`__ function in its documentation. This is neat to have if you want to keep tabs on a batch of repos, instead of tediously checking the Github web interface! If you're new to Github, the `trending page <https://github.com/trending>`__ is an easy way to find new, interesting repos.

**Getting Started**

#. You'll need to create a personal access token for your Github account. See the Github docs, `"Creating a personal access token". <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token>`__
#. `Install PyGithub <https://pypi.org/project/PyGithub/>`__ and `pandas <https://pandas.pydata.org/docs/getting_started/index.html>`__:

.. code-block:: python

   pip install PyGithub
   pip install pandas

3. Run the below code as a Python script.

.. code-block:: python

   python github_stars.py

.. code-block:: python

   import pandas as pd
   from github import Github


   def stars(repo, g):
       """Retrieve github repo star count.
       Accepts: str, repo "username/repo name",ex: "getpelican/pelican"
       Returns: int, github repo stargazers number"""
       repo = g.get_repo(repo)
       return repo.stargazers_count


   # static site repos: http://lofipython.com/a-brief-summary-of-promising-python-static-site-generators/
   urls = [
       "https://github.com/getpelican/pelican",
       "https://github.com/lektor/lektor",
       "https://github.com/eudicots/Cactus",
       "https://github.com/getnikola/nikola",
       "https://github.com/sunainapai/makesite",
       "https://github.com/hyde/hyde",
       "https://github.com/Anomareh/mynt",
       "https://github.com/staticjinja/staticjinja",
   ]
   repos = [url.replace("https://github.com/", "") for url in urls]
   g = Github("access_token")
   counts = [(repo, stars(repo, g)) for repo in repos]
   stars_df = pd.DataFrame(counts, columns=["repo","stars"])
   stars_df.to_csv("Stars.csv", index=False)

On Linux, I was able to check the results of the CSV with the cat command:

.. figure:: https://pythonmarketer.files.wordpress.com/2022/10/check-pelican.png?w=409
   :alt: 
   :figclass: wp-image-7254

I confirmed the API was accurate against the web interface in `pelican's repo <https://github.com/getpelican/pelican>`__!

.. figure:: https://pythonmarketer.files.wordpress.com/2022/10/pelican-stars.png?w=1024
   :alt: 
   :figclass: wp-image-7251

`Github Repo Stargazer API Reference <https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository.stargazers_count>`__
