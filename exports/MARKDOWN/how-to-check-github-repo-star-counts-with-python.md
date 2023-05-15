Title: How to Check Github Repo Star Counts With Python
Date: 2022-10-10 00:08
Author: pythonmarketer
Category: APIs, coding, programming, python
Tags: github api, github stars python, repo star counts
Slug: how-to-check-github-repo-star-counts-with-python
Status: published

`<!-- wp:paragraph -->`{=html}

Snooping through my package list, I noticed the [PyGithub library](https://github.com/PyGithub/PyGithub) was installed. Its repo boasts "Typed interactions with the GitHub API v3". I googled the package, wanting to check in on the repos I profiled in an [earlier post about static site generators](https://pythonmarketer.com/2021/07/28/a-brief-summary-of-promising-python-static-site-generators/).

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

I drafted the code below after noticing the [repo.stargazer_count](https://pygithub.readthedocs.io/en/latest/examples/Repository.html#get-count-of-stars) function in its documentation. This is neat to have if you want to keep tabs on a batch of repos, instead of tediously checking the Github web interface! If you're new to Github, the [trending page](https://github.com/trending) is an easy way to find new, interesting repos.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Getting Started**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:list {"ordered":true} -->`{=html}

1.  You'll need to create a personal access token for your Github account. See the Github docs, ["Creating a personal access token".](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
2.  [Install PyGithub](https://pypi.org/project/PyGithub/) and [pandas](https://pandas.pydata.org/docs/getting_started/index.html):

`<!-- /wp:list -->`{=html}

`<!-- wp:code -->`{=html}

``` wp-block-code
pip install PyGithub
pip install pandas
```

`<!-- /wp:code -->`{=html}

`<!-- wp:paragraph -->`{=html}

3\. Run the below code as a Python script.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:code -->`{=html}

``` wp-block-code
python github_stars.py
```

`<!-- /wp:code -->`{=html}

`<!-- wp:syntaxhighlighter/code -->`{=html}

``` wp-block-syntaxhighlighter-code
import pandas as pd
from github import Github


def stars(repo, g):
    """Retrieve github repo star count.
    Accepts: str, repo "username/repo name",ex: "getpelican/pelican"
    Returns: int, github repo stargazers number"""
    repo = g.get_repo(repo)
    return repo.stargazers_count


# static site repos: http://pythonmarketer.com/2021/07/lc28/a-brief-summary-of-promising-python-static-site-generators/
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
```

`<!-- /wp:syntaxhighlighter/code -->`{=html}

`<!-- wp:paragraph -->`{=html}

On Linux, I was able to check the results of the CSV with the cat command:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:image {"id":7254,"sizeSlug":"large","linkDestination":"none"} -->`{=html}

![](https://pythonmarketer.files.wordpress.com/2022/10/check-pelican.png?w=409){.wp-image-7254}

`<!-- /wp:image -->`{=html}

`<!-- wp:paragraph -->`{=html}

I confirmed the API was accurate against the web interface in [pelican's repo](https://github.com/getpelican/pelican)!

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:image {"id":7251,"sizeSlug":"large","linkDestination":"none"} -->`{=html}

![](https://pythonmarketer.files.wordpress.com/2022/10/pelican-stars.png?w=1024){.wp-image-7251}

`<!-- /wp:image -->`{=html}

`<!-- wp:paragraph -->`{=html}

[Github Repo Stargazer API Reference](https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository.stargazers_count)

`<!-- /wp:paragraph -->`{=html}
