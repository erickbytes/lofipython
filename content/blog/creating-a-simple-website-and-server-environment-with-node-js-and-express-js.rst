##############################################################################
 Creating A Simple Website and Server Environment with Node.js and Express.js
##############################################################################

:date:
   2017-08-09 21:16

:author:
   pythonmarketer

:category:
   coding, javascript, programming, web development

:tags:
   command line, creating websites, express.js, mongodb, Node.js, web
   dev, website

:slug:
   creating-a-simple-website-and-server-environment-with-node-js-and-express-js

:status:
   published

Here is what I have deduced is the fastest way to get an app up and
running with Node.js. This requires some familiarity with using the
command line. I completed the Codeacademy course "`Learn The Command
Line <https://www.codecademy.com/learn/learn-the-command-line>`__"
before beginning with Node.js. I think it helped me better understand
what the commands are and what they do.

Download and install `Node.JS <https://nodejs.org/en/>`__ Open the node
command prompt. This was done on a windows machine.

.. code::

   mkdir node_apps

creates a folder for your app(s)

.. code::

   cd \app_name

changes command prompt directory to your app's folder

.. code::

   npm init

|  Creates json file for your app
|  fill out applicable info or just hit enter until the file is created

.. code::

   npm install express

installs express.js module in node.js

.. code::

   npm install express-generator -g

|  installs express-generator module in node.js
|  this module creates the web app's structure once the command in the
   next step is entered

.. code::

   express app_name

creates the structure for your app and all necessary folders. (views,
css, Javascript, routing, etc.)

.. code::

   npm install

ensures all app module dependencies are installed

.. code::

   npm start

starts your server and web app

Go to http://localhost:3000 in a browser. Port 3000 is the default port
of Express. Your app is live in dev environment.

**Notes**

-  I learned most of this from `this great blog post
   <https://codeforgeek.com/2014/10/express-complete-tutorial-part-1/>`__.

-  The above does not include a database integration. I integrated with
   a MongoDB database by `following the instructions in this post
   <https://closebrace.com/tutorials/2017-03-02/the-dead-simple-step-by-step-guide-for-front-end-developers-to-getting-up-and-running-with-nodejs-express-and-mongodb>`__.

-  This `YouTube video <https://www.youtube.com/watch?v=1uFY60CESlM>`__
   was also very helpful to me for figuring out MongoDB and Node.js
   integration.

-  An HTML shorthand language called jade (aka pug) comes stock within
   Express.js. `Here's further reading <https://webapplog.com/jade/>`__
   on the pros and cons.

-  All of the above has been from my own studies. I do not claim
   anything listed as the most efficient or best way to use Node.js.
   This is what has worked for me over the past two days.

-  It feels good to whip up a nimble app environment that is capable of
   producing and supporting world changing software; Node.js is used by
   Netflix, PayPal, Microsoft and Uber.
