Launching A Web Browser from Ubuntu Shell
#########################################
:date: 2024-08-29 12:45
:author: lofipython
:category: coding, programming, ubuntu, web browser
:tags: alias web browser from ubuntu, xdg-open browser in shell, ubuntu alias
:slug: launching-a-web-browser-from-ubuntu-shell
:status: published

Ubuntu allows aliasing commands to run a shell function. Below, I used 
`xdg-open <https://linux.die.net/man/1/xdg-open>`__ to open my Cloudflare Pages 
dashboard with an alias.

**Add Ubuntu Function to .bashrc**

I used VS Code to add this to my .bashrc file. Now, when I type **cloudflare** 
into my shell it launches the dashboard in Chrome. Remember to close and reopen 
a new shell before testing out the command.

.. code-block:: console

   open_cloudflare() {
       xdg-open "https://dash.cloudflare.com"
   }
   alias cloudflare=open_cloudflare

The pattern of being able to open a page in a web browser with a quick command could 
be applied to lots of my frequently visited websites. 

**Bonus Alternate Version: Python webbrowser Module CLI**

Sometimes the right tool is Python. Other times, the Linux shell CLI tools are sufficient. 
Since this is a Python blog... here is a version that leverages the 
Python `webbrowser <https://docs.python.org/3/library/webbrowser.html>`__ module CLI that 
also works, assuming you're already in your Python environment.

.. code-block:: console

   open_cloudflare() {
       python -m webbrowser https://dash.cloudflare.com
   }
   alias cloudflare=open_cloudflare