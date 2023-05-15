Title: How to Track Python Script Completion
Date: 2022-01-05 11:49
Author: pythonmarketer
Category: coding, programming, python, Scripts
Tags: logging, python scripts, reliability, tracking
Slug: how-to-track-python-script-completion
Status: published

`<!-- wp:paragraph -->`{=html}

Did your script run to completion? Sure, you might log some tracebacks along the way or terminate the program early with [sys.exit()](https://docs.python.org/3/library/sys.html#sys.exit). But did your script actually run completely to the end? I have yet to use the [Trace module](https://docs.python.org/3/library/trace.html) but it seems worth checking out also. Visualization tools like [heartrate](https://github.com/alexmojaki/heartrate) are worth mentioning too depending on how you are running your scripts. Task runners typically have run status tracking as well. I like having a visual confirmation by logging some sort of information when a script finishes as intended. It's nice to know when your scripts finished or not. Use logging and Trace to up your reliability of your scripts.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Another anecdotal way to track this is with the logging module:**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
import logging

def improvise():
    """Improv Tutorial: https://www.youtube.com/watch?v=C6wY9OwqJ2A"""
    try:
        print("Boom! Detective Michael Scarn, I'm with the FBI!")
        return None
    except:
        logging.exception("Error occurred during improv.")
        return None

FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(filename="improvise.log", format=FORMAT)
improvise()
logging.info("Improvisation finished!")
```

`<!-- /wp:preformatted -->`{=html}
