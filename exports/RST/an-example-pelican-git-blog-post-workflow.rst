An Example Pelican + Git Blog Post Workflow
###########################################
:date: 2022-12-04 12:17
:author: pythonmarketer
:category: automation, git, pelican, programming, python, writing
:tags: pelican blog, pelican workflow, pelican writing example
:slug: an-example-pelican-git-blog-post-workflow
:status: published

On my Windows subsystem for Linux environment, I am now publishing new blog posts following this `Pelican <https://docs.getpelican.com/en/latest/quickstart.html>`__-based workflow:

.. code:: wp-block-code

   1. Activate the Python environment: cd Your_Env/bin & source activate

.. code:: wp-block-code

   2. Go to the project folder: cd /home/username/my_project

.. code:: wp-block-code

   3. Run Python script to create new markdown file from a template:
   python new_post.py

.. code:: wp-block-code

   4. After writing the new post, update the Pelican content:
   pelican content

   (Optional) preview the new post at local host http://127.0.0.1:8000/
   pelican -l 

.. code:: wp-block-code

   5. Use git to stage, commit and push the files to a Github repo:
   git add .
   git commit -m "new post edits and fixes"
   git push -u origin main

The new blog post is now live! This is my own workflow for my Pelican blog, `divbull.com <http://divbull.com>`__, which is hosted for free with `Cloudflare Pages <https://pages.cloudflare.com/>`__. You can read more about connecting Pelican and Cloudflare in `this past post I wrote <https://pythonmarketer.com/2022/07/08/launching-a-live-static-blog-via-pelican-github-and-cloudflare-pages/>`__.

You will need to `create a SSH key and connect it to your Github account <https://docs.github.com/en/authentication/connecting-to-github-with-ssh>`__ to get this completely working, as it's required by Github now. Make sure you write down your passphrase! I was able to create an ssh key with this command:

.. code:: wp-block-code

   ssh-keygen -t ed25519 -C "youname@example.com"

Below is the short Python script I wrote for generating the markdown file for a new post. I've enjoyed working this out on my new blog and now can fire off posts rapidly with this command line based workflow.

.. code:: wp-block-syntaxhighlighter-code

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
       content = "/home/erickbytes/divbull/divbull.com/content"
       name = name.replace(" ", "-")
       md = f"{content}/{name}.md"
       with open(md, "w") as fhand:
           fhand.write(post)
       return None


   name = post_name()
   post = post_template(name)
   save_draft(name, post)
