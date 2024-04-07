Ask Tame Impala - My First Web App
##################################
:date: 2016-05-25 02:03
:author: pythonmarketer
:category: tame impala
:slug: askkevinparker-com-my-first-web-app-other-notes
:status: published

**My app is alive.** It is a simple program - ask it a question, and it queries a database of Tame Impala lyrics and pulls a response line from the lyrics 
based on which words match up. Kevin Parker is the frontman of the band. 

**View the app here:** `tameimpala.pythonanywhere.com <http://tameimpala.pythonanywhere.com/tameimpala>`__.

I published it a few weeks ago and according to Google Analytics it has had 50 sessions from Google and over 200 page views in 10 different countries - not bad!

**SSL Certificates / Start SSL / PythonAnywhere"** 
An SSL certificate is required for the domain by PythonAnywhere to control the Admin page and set up your app. You don't need this if your domain is "username.pythonanywhere.com".

It was kind of tricky was figuring out how to set up the certificate for the first time. `These instructions from PythonAnywhere <https://help.pythonanywhere.com/pages/SSLOwnDomains>`__ helped a lot.

I used a free certificate from Start SSL and it worked fine. If you're new to SSL like me, here's a simple explanation: you get certificates aka 
two text files containing a long code from your SSL provider and submit them to the domain host. The last step is to notify your domain host and have them verify with the SSL provider. If all goes well, you'll be live in a few hours.

**"Masking" domains**
This means if you type "google.com", it will redirect to "www.Google.com" `GoDaddy makes this super easy <https://www.godaddy.com/help/manually-forwarding-or-masking-your-domain-name-422>`__. I set it up for my site as well. `Here's a post from PythonAnywhere <https://help.pythonanywhere.com/pages/NakedDomains>`__ on this also.

**Collaborating with other programmers**
Currently trying to install and run GitHub on my Desktop (trickier to do on an outdated operating system). Another programmer explained to me how 
it is the base means of collaboration and managing work flow for programmers working together on a project. Probably will know more about this soon 
and `write a post on it <https://lofipython.com/git-the-basics-a-git-version-control-cheat-sheet/>`__. Git seems awesome and I had not been exposed to this tool until recently.
