An Example Pelican + Git Blog Post Workflow
###########################################
:date: 2022-12-04 12:17
:author: pythonmarketer
:category: automation, git, pelican, programming, python, writing
:tags: pelican blog, pelican workflow, pelican writing example
:slug: an-example-pelican-git-blog-post-workflow
:status: published

In my Ubuntu Linux environment, I'm now publishing new blog posts following this `Pelican <https://docs.getpelican.com/en/latest/quickstart.html>`__ + Python + git workflow.


1. Activate the Python environment: 

::
   
   # Create with a virtual env with venv: python -m venv env_name
   source env_name/bin/activate


2. Clone your repo and go to the project folder: 

::

   git clone https://github.com/erickbytes/lofipython.git && cd lofipython

3. Run Python script to create new markdown or `.rst <https://github.com/erickbytes/lofipython/blob/main/new_rst_post.py>`__ file from a template:

::

   python new_post.py

4. After writing the new post, update the Pelican content:

::

   pelican content


5. Preview the new post with Pelican in development mode at local host 8000 in Firefox:

::

   pelican -l ; firefox -new-tab http://127.0.0.1:8000


6. Use git to stage, commit and push the files to a Github repo:

::

   git add .
   git commit -m "new post edits and fixes"
   git push -u origin main


The new blog post is now live! This is my own workflow for my Pelican blog, this blog which is hosted for free with `Cloudflare Pages <https://pages.cloudflare.com/>`__. You can read more about connecting Pelican and Cloudflare in `this past post I wrote <https://lofipython.com/launching-a-live-static-blog-via-pelican-github-and-cloudflare-pages/>`__.

|

**An Ubuntu Shell One-Liner for Pelican Blog Preview**
   - compile my Pelican static site
   - serve development blog preview to port 8000
   - wait to open the local host 8000 page in a Firefox browser

When I'm editing an old post or write a new post and want to preview it, the workflow can be wrapped up in a single chain of commands if desired. For the sake of Linux one-liners, it had to be done:

::

   pelican content ; pelican -l ; firefox -new-tab http://127.0.0.1:8000

|

**Github SSH Required**

You will need to `create a SSH key and connect it to your Github account <https://docs.github.com/en/authentication/connecting-to-github-with-ssh>`__ to get this working, as it's required by Github now. Make sure you write down your passphrase. I was able to create an ssh key with this command:

::

   ssh-keygen -t ed25519 -C "yourname@example.com"


**Scripting New Post Creation**

Below is the short Python script I wrote for generating the markdown file for a new post.


.. code-block:: python

   from datetime import date


   def post_name():
       """Ask for the new post's name."""
       name = input("Enter the new post's title:\n")
       return name


   def post_template(title):
       """Return str, post draft"""
       post = f"Title: {title} \nDate: {date.today()} 4:20 \nCategory: Essay"
       return post


   def save_draft(name, post):
       """Save new post draft to content folder."""
       content = "~/projects/lofipython/content"
       name = name.replace(" ", "-")
       md = f"{content}/{name}.md"
       with open(md, "w") as fhand:
           fhand.write(post)
       return None


   name = post_name()
   post = post_template(name)
   save_draft(name, post)


I've enjoyed working this out on my new blog. I can easily edit, improve and fire off blog posts rapidly with this command line workflow.