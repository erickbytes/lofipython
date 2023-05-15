Title: Opening Firefox Via the webbrowser Module + RPA Tools
Date: 2021-08-15 23:13
Author: pythonmarketer
Category: automation, coding, gui, programming, python
Tags: Firefox, RPA
Slug: how-to-open-firefox-with-webbrowser-on-ubuntu-linux
Status: published

`<!-- wp:paragraph -->`{=html}

webbrowser is a convenient Python standard library module. It opened my Firefox browser on my Ubuntu Linux operating system running on a Chromebook. This code is adapted from a [Python Examples blog post](https://pythonexamples.org/python-open-url-in-firefox-browser/). Below is a list of other browsers you can open with webbrowser. At the bottom of this post, you'll find more tools to interact with browsers and GUIs programmatically.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:syntaxhighlighter/code -->`{=html}

``` wp-block-syntaxhighlighter-code
import webbrowser
firefox_sh = '/usr/lib/firefox/firefox.sh'
webbrowser.register('firefox',
    None,
    webbrowser.BackgroundBrowser(firefox_sh))
url = 'https://atomic-temporary-107329037.wpcomstaging.com'
webbrowser.get('firefox').open_new_tab(url)
print(webbrowser._browsers)
```

`<!-- /wp:syntaxhighlighter/code -->`{=html}

`<!-- wp:table {"className":"is-style-regular"} -->`{=html}

```{=html}
<figure class="wp-block-table is-style-regular">
```
  Type Name              Class Name
  ---------------------- ----------------------------------
  `'mozilla'`            `Mozilla('mozilla')`
  `'firefox'`            `Mozilla('mozilla')`
  `'netscape'`           `Mozilla('netscape')`
  `'galeon'`             `Galeon('galeon')`
  `'epiphany'`           `Galeon('epiphany')`
  `'skipstone'`          `BackgroundBrowser('skipstone')`
  `'kfmclient'`          `Konqueror()`
  `'konqueror'`          `Konqueror()`
  `'kfm'`                `Konqueror()`
  `'mosaic'`             `BackgroundBrowser('mosaic')`
  `'opera'`              `Opera()`
  `'grail'`              `Grail()`
  `'links'`              `GenericBrowser('links')`
  `'elinks'`             `Elinks('elinks')`
  `'lynx'`               `GenericBrowser('lynx')`
  `'w3m'`                `GenericBrowser('w3m')`
  `'windows-default'`    `WindowsDefault`
  `'macosx'`             `MacOSX('default')`
  `'safari'`             `MacOSX('safari')`
  `'google-chrome'`      `Chrome('google-chrome')`
  `'chrome'`             `Chrome('chrome')`
  `'chromium'`           `Chromium('chromium')`
  `'chromium-browser'`   `Chromium('chromium-browser')`

```{=html}
<figcaption>
```
[webbrowser docs](https://docs.python.org/3/library/webbrowser.html#webbrowser.get)

```{=html}
</figcaption>
```
```{=html}
</figure>
```
`<!-- /wp:table -->`{=html}

`<!-- wp:paragraph -->`{=html}

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Check out these other browser\\gui automation tools:**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:list -->`{=html}

-   [pyautogui](https://pyautogui.readthedocs.io/en/latest/)
-   [Selenium](https://www.selenium.dev/selenium/docs/api/py/)
-   [RPA for Python](https://github.com/tebelorg/RPA-Python)
-   [robotframework](https://github.com/robotframework/robotframework)
-   [TagUI](https://github.com/kelaberetiv/TagUI)
-   [Sikuli](https://github.com/RaiMan/SikuliX1)
-   [Open RPA](https://github.com/open-rpa/openrpa)
-   [Power Automate](https://flow.microsoft.com/en-us/blog/automate-tasks-with-power-automate-desktop-for-windows-10-no-additional-cost/)
-   [CasperJS](https://www.casperjs.org/)
-   [PhantomJS](https://github.com/ariya/phantomjs)
-   [SlimerJS](https://slimerjs.org/)

`<!-- /wp:list -->`{=html}

`<!-- wp:paragraph -->`{=html}

*see* *also:* [Robot Process Automation](https://en.wikipedia.org/wiki/Robotic_process_automation), [Things You Can Do With a Browser in 2020](https://github.com/luruke/browser-2020)

`<!-- /wp:paragraph -->`{=html}
