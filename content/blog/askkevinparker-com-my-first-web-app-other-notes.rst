Ask Tame Impala - My First Web App
##################################
:date: 2016-05-25 02:03
:author: pythonmarketer
:category: tame impala
:slug: askkevinparker-com-my-first-web-app-other-notes
:status: published

**My app is alive.** Ask it a question, and it queries a database of Tame Impala lyrics and pulls a response line from the lyrics 
based on which words match up. Kevin Parker is the frontman of the band. 

**Try out my web2py app at** `tameimpala.pythonanywhere.com <http://tameimpala.pythonanywhere.com>`__

When I first published the app in 2016, per Google Analytics it had 50 sessions from Google 
and over 200 page views in 10 different countries after a few weeks.
In April 2025, the app received 6,749 visits in traffic according to pythonanywhere.

**SSL Certificates / Start SSL / PythonAnywhere"** 
An SSL certificate is required for the domain by PythonAnywhere to control the Admin page 
and set up your app. You don't need this if your domain is "username.pythonanywhere.com".

It was kind of tricky was figuring out how to set up the certificate for the first time. 
`These instructions from PythonAnywhere <https://help.pythonanywhere.com/pages/SSLOwnDomains>`__ helped a lot.

I used a free certificate from Start SSL and it worked fine. If you're new to SSL like me, 
here's a simple explanation: you get certificates aka two text files containing a long code 
from your SSL provider and submit them to the domain host. The last step is to notify your 
domain host and have them verify with the SSL provider. If all goes well, you'll be live in a few hours.

**"Masking" domains**
This means if you type "google.com", it will redirect to "www.Google.com" `GoDaddy makes this super easy <https://www.godaddy.com/help/manually-forwarding-or-masking-your-domain-name-422>`__. 
I set it up for my site as well. `Here's a post from PythonAnywhere <https://help.pythonanywhere.com/pages/NakedDomains>`__ on this also.

**Collaborating with other programmers**
Currently trying to install and run GitHub on my Desktop. It's trickier to do on an outdated operating system. 
Another programmer explained to me how it is the base means of collaboration and managing work flow for programmers 
working together on a project. Probably will know more about this soon and `write a post on it <https://lofipython.com/git-the-basics-a-git-version-control-cheat-sheet/>`__. 
Git seems awesome and I had not been exposed to this tool until recently.
