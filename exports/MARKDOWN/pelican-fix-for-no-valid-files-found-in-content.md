Title: Pelican Fix for "No valid files found in content"...
Date: 2022-10-08 13:43
Author: pythonmarketer
Category: coding, python, writing
Tags: markdown library, pelican blog, python fix
Slug: pelican-fix-for-no-valid-files-found-in-content
Status: published

`<!-- wp:paragraph -->`{=html}

Pelican is a popular [static site generator library](https://pythonmarketer.com/2021/07/28/a-brief-summary-of-promising-python-static-site-generators/) in Python. I didn't know why my pelican blog was not working. I've used the "pelican content" command many times for my blog. This time, when attempting to write a new post on a new computer, I was getting this error where none of my posts were visible to Pelican:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:syntaxhighlighter/code -->`{=html}

``` wp-block-syntaxhighlighter-code
WARNING  No valid files found in content for the active         log.py:91
         readers:                                                        
           | BaseReader (static)                                         
           | HTMLReader (htm, html)                                      
           | RstReader (rst)     
```

`<!-- /wp:syntaxhighlighter/code -->`{=html}

`<!-- wp:image {"id":7221,"sizeSlug":"large","linkDestination":"none"} -->`{=html}

![](https://pythonmarketer.files.wordpress.com/2022/10/image.png?w=665){.wp-image-7221}

`<!-- /wp:image -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Solution**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

Install the markdown library, which is stated in the [pelican docs](https://docs.getpelican.com/en/3.6.3/install.html#optional-packages). This [Github issue](https://github.com/getpelican/pelican/issues/1868) also provides some background on this warning.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:code -->`{=html}

``` wp-block-code
pip install markdown
```

`<!-- /wp:code -->`{=html}

`<!-- wp:image {"id":7224,"sizeSlug":"large","linkDestination":"none"} -->`{=html}

![](https://pythonmarketer.files.wordpress.com/2022/10/image-1.png?w=672){.wp-image-7224}

`<!-- /wp:image -->`{=html}

`<!-- wp:paragraph -->`{=html}

Now my "pelican content" command works!

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:code -->`{=html}

``` wp-block-code
pelican content
```

`<!-- /wp:code -->`{=html}

`<!-- wp:image {"id":7226,"sizeSlug":"large","linkDestination":"none"} -->`{=html}

![](https://pythonmarketer.files.wordpress.com/2022/10/image-2.png?w=679){.wp-image-7226}

`<!-- /wp:image -->`{=html}
