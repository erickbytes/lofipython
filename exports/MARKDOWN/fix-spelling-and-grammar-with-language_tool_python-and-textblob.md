Title: Fix Spelling and Grammar with language_tool_python and textblob
Date: 2022-01-30 16:28
Author: pythonmarketer
Category: APIs, data, programming, writing
Tags: language, language tool, python, text, textblob
Slug: fix-spelling-and-grammar-with-language_tool_python-and-textblob
Status: published

`<!-- wp:paragraph -->`{=html}

Below are two practical Python libraries for text processing. This function uses [textblob's spelling correction](https://textblob.readthedocs.io/en/dev/api_reference.html?highlight=correct#textblob.blob.TextBlob.correct) along with [language_tool_python](https://pypi.org/project/language-tool-python/), which applies grammatical corrections via the [Language Tool API](https://languagetool.org/http-api/swagger-ui/#!/default/post_check). I added these text processing transformations into my [concept text generation app](https://www.positivipy.com/). These are free, public APIs up to around 20 requests per second. You can send both text and receive back an improved version of your text, ideally altering and improving your writing.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

I found 2 errors when I piped the text of this post into the below code: the proper noun "textblob" corrected to "text blow's" and the word "app" corrected to "pp". Be sure to proof your results. Regardless, I like having these two Python tools in my bag!

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**[Install textblob](https://textblob.readthedocs.io/en/dev/install.html) and [language_tool_python](https://pypi.org/project/language-tool-python/) with these [pip](https://pythonmarketer.com/2018/01/20/how-to-python-pip-install-new-libraries/) commands:**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
pip install language-tool-python
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
pip install -U textblob
python -m textblob.download_corpora
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:syntaxhighlighter/code -->`{=html}

``` wp-block-syntaxhighlighter-code
import language_tool_python
from textblob import TextBlob

def fix_spelling_and_grammar(text):
    """ returns str: text transformed by language tool and text blob
    1) Apply language tool API correction
    Language Tool Public API: https://dev.languagetool.org/public-http-api
    https://languagetool.org/http-api/swagger-ui/#!/default/post_check
    python library: https://pypi.org/project/language-tool-python/
   
    2) Apply textblob's spell check to the text"""
    try:
        # use the public API, language English
        tool = language_tool_python.LanguageToolPublicAPI('en-US')
        text =  tool.correct(text)
        b = TextBlob(text)
        return str(b.correct())
    except:
        return text

text = "Language is incredble. Fascinatng how hoomans have so many."
transformed_text = fix_spelling_and_grammar(text)
print(transformed_text)
# >>> Language is incredible. Fascinating how humans have so many.
```

`<!-- /wp:syntaxhighlighter/code -->`{=html}
