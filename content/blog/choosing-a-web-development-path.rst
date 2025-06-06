#################################
 Choosing a Web Development Path
#################################

:date:
   2016-03-22 03:45

:author:
   pythonmarketer

:category:
   coding, programming, python, web development, web2py

:slug:
   choosing-a-web-development-path

:status:
   published

I have recently finished this `HTML course <https://www.coursera.org/learn/html>`__, 
which recommends using cPanel to configure websites. So I bought a domain and registered with cPanel.

**What I thought would happen in trying to create a website:**

Buy a domain and use cPanel and Python in perfect sync to create a website.

**Reality:**

cPanel is configured mostly for PHP. You can run Python scripts with it, but it doesn't seem to be 
the most effective route from what I've read.

So I went back to the drawing board and I've simplified this down to two basic paths:

.. csv-table:: 
   :header: "Tools", "Hosting", "Framework / IDE"
   :widths: 30, 30, 30

   "1) Python + Web Framework", "PythonAnywhere or Cloudflare Pages", "FastAPI, Flask, Django or web2py"
   "2) Javascript + Python", "cPanel or Cloudflare Pages", "React, Angular, Express.js"
   
I'm going with Path 1 because the only language I know is Python. I hope to learn other languages 
like Javascript and CSS but would like to get building as fast as possible. I found a free web 
hosting service called PythonAnywhere. There are other `free <https://wiki.python.org/moin/FreeHosts>`__ 
and paid Python-friendly hosts. 

   I also added in Cloudflare Pages retroactively to this post, since I discovered it many years after writing this post.

A note on PythonAnywhere: 5 stars for the tutorial pictured below. It is very nice to see in the whirlwind 
of confusion of learning to deal with code and a new environment.

.. image:: https://pythonmarketer.files.wordpress.com/2016/03/pythonanywhere-tutorial.jpg
   :alt: PythonAnywhere Tutorial
   :class: alignnone size-full wp-image-286
   :width: 600px
   :height: 150px

Love this opening quote from `web2py Documentation <http://web2py.com/book>`__: 

   "I believe that the ability to easily build high quality web applications is of 
   critical importance for the growth of a free and open society. This prevents the 
   biggest players from monopolizing the flow of information."


Instead of the `previously mentioned web frameworks <https://lofipython.com/starting-to-almost-kinda-think-about-creating-a-web-app/>`__,
I've chosen web2py as a starter because of its compatibility with PythonAnywhere, its simplicity, 
easy to read documentation and relative ease of use for beginners. A note on web2py so far: 
`the videos from the creator <http://www.web2py.com/init/default/documentation>`__, Massimo Di Pierro, are super useful!

   **Update:** consider using `py4web <https://github.com/web2py/py4web>`__, web2py's successor
