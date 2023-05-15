Title: Launch the Browser with a Windows Batch File
Date: 2021-12-06 21:15
Author: pythonmarketer
Category: coding, productivity, programming, Scripts
Tags: automation, command line, scripting, Windows
Slug: can-you-script-it
Status: published

`<!-- wp:paragraph -->`{=html}

Can it be scripted? Ask yourself this question about everything you do. Every application opened, website viewed and task you knock out in the course of a day might be worth writing a script to automate. As an example, here is a [Windows batch file](https://en.wikipedia.org/wiki/Batch_file) that opens 3 websites I visit frequently:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Open Websites.bat**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

*Save below 3 lines as a ".bat" file and double click it to launch the websites in a browser.*

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:code -->`{=html}

``` wp-block-code
(start "Netflix" "https://www.netflix.com/browse"
start "Twitter" "https://twitter.com/home"
start "Gmail" "https://mail.google.com/")
```

`<!-- /wp:code -->`{=html}

`<!-- wp:paragraph -->`{=html}

Anything and everything is subject to automation. You can use [Windows Scripting](https://pythonmarketer.com/2020/05/06/exploring-windows-command-line-tools-batch-file-automation-and-remote-desktop-connection/), Python, R, other programming languages or [RPA](https://pythonmarketer.com/2021/08/15/how-to-open-firefox-with-webbrowser-on-ubuntu-linux/). Keep your eyes peeled for time you could be saving. One script like this might save (a few seconds everyday) **x** (every day for the rest of your life). Or more. Sometimes, I find myself piddling away at something I don't really need to be struggling to remember. Consider writing a script for it!

`<!-- /wp:paragraph -->`{=html}
