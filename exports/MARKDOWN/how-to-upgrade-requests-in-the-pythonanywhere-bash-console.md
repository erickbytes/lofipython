Title: How to Upgrade Requests in the Bash Console
Date: 2022-01-23 14:41
Author: pythonmarketer
Category: coding, python
Tags: bash, pip, python install, pythonanywhere
Slug: how-to-upgrade-requests-in-the-pythonanywhere-bash-console
Status: published

`<!-- wp:paragraph -->`{=html}

This command can be used to upgrade your Python [requests library](https://docs.python-requests.org/en/latest/) with [pip](https://pythonmarketer.com/2018/01/20/how-to-python-pip-install-new-libraries/), Python's package manager. It is tailored for a PythonAnywhere environment. I suppose this command works on any [Bash console](https://www.gnu.org/software/bash/), but if you're running your app with pythonanywhere, you can find the bash console here:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
https://www.pythonanywhere.com/user/your_username/consoles/
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:image {"id":6771,"sizeSlug":"large","linkDestination":"none"} -->`{=html}

![](https://pythonmarketer.files.wordpress.com/2022/01/python-anywhere-bash-highlight-2.png?w=1024){.wp-image-6771}

`<!-- /wp:image -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Install requests with this command:**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:syntaxhighlighter/code -->`{=html}

``` wp-block-syntaxhighlighter-code
python3.8 -m pip install requests --upgrade --user
```

`<!-- /wp:syntaxhighlighter/code -->`{=html}

`<!-- wp:paragraph -->`{=html}

Substitute in whatever your Python version is. This command upgrades the requests library on a PythonAnywhere app. If any libraries depend on a specific version of requests, a warning appears like this one I saw for the [python-unsplash](https://github.com/yakupadakli/python-unsplash) library.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:quote -->`{=html}

> ERROR: python-unsplash 1.1.0 has requirement requests==2.20.0, but you'll have requests 2.27.1 which is incompatible.

`<!-- /wp:quote -->`{=html}

`<!-- wp:image {"id":6777,"sizeSlug":"large","linkDestination":"none"} -->`{=html}

![](https://pythonmarketer.files.wordpress.com/2022/01/requests-upgrade-full-install.png?w=1024){.wp-image-6777}

`<!-- /wp:image -->`{=html}
