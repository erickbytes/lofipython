Title: The Joy of Logging With Python
Date: 2019-02-02 20:23
Author: pythonmarketer
Category: automation, coding, Colors, programming, software
Tags: Bob Ross, python
Slug: the-joy-of-logging-with-python
Status: published

**In painting and coding, there are no mistakes, only happy accidents. **

Fortunately when errors happen, Python affords us its stock '[logging](https://docs.python.org/3/howto/logging.html)' module, which sometimes catches flak in the community for its syntax and documentation. After poking around this module, I've found it quite suitable to my needs. Thanks to the logging module, I'm catching my happy coding accidents and fixing them like a pro.

**Below is my simple logging setup, which I am using to monitor [automated Python scripts](https://pythonmarketer.wordpress.com/2018/11/25/automated-python-with-windows-task-scheduler/).** **This script is a "painting" program created to demonstrate logging. **Passing the below to the basicConfig() format argument logs a timestamp, effective for tracking the time of errors. This example logs the error and the traceback to a .log file.

    import logging
    logging.basicConfig(filename='your_log.log',level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.info('Running painter...')

    def paint(painter):
        if painter == 'Bob Ross':
            print('Choose colors, Pfthalo Blue.')
            print('Apply liquid white to canvas.')
            print('Clean brush in odorless paint thinner, and juuust beat the devil out of it.')
            print('Paint happy little trees. There’s nothing wrong with having a tree as a friend.')
            painting = 'https://www.youtube.com/watch?v=5U3G61r35Mc'
            painting_complete = True
            wisdom = 'Remember this is your world. You get to decide what's in it.'
            return painting, wisdom, painting_complete

    try:
        painter = 'Bob Ross' # comment this line out to produce error for log
        painting, wisdom, painting_complete = paint(painter)
        print(painting)
    except:
        logging.exception('Got exception on main handler')

**Below is an example of logging only the error, without a traceback. **I am still learning when each is appropriate, but I've found this exception handling variation useful when logging lots of errors that are acceptable and expected in my try/except loops. Note also that in this variation, I have changed the level argument to logging.DEBUG. This mode offers more program execution details to help debug an error when needed.

    import logging
    logging.basicConfig(filename='your_log.log',level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.info("Running painter...")
    try:
        painter = "Bob Ross"
        painting = paint(painter)
        print(painting)
    except Exception as e:
        logging.info(e)

**Result: writing errors to a .log file.**  
You should see that Python has created a fresh .log file with your happy little errors. Below is an example log from a tabular data cleaning program I wrote. The single line errors were produced using the second "Exception as e" method. At the bottom, we can see the full traceback, produced by the first, "logging.exception" method. This .log file resulted from passing the level=logging.INFO argument.

**Example .log output file:**

![logex.png](http://pythonmarketer.files.wordpress.com/2019/02/006e2-logex-e1549135549973.png){.alignnone .size-full .wp-image-1637 width="960" height="648"}

**What's the difference between a .log file and a .txt file?**

> The difference between the two file types is that [.LOG](https://pc.net/extensions/file/log) files are typically generated automatically, while [.TXT](https://pc.net/extensions/file/txt) files are created by the user.  **- pc.net**

**Final Thoughts**

I will continue to explore logging methods but this seems to sufficiently log my program activity and errors. Now, my favorite part of work is peeking in on the logs to see how my happy little Python programs are running.

[![The_Joy_of_Painting_title_screen](https://pythonmarketer.files.wordpress.com/2019/02/the_joy_of_painting_title_screen.jpg){.wp-image-1638 .alignright width="312" height="229" hspace="100"}](https://www.youtube.com/watch?v=5U3G61r35Mc)

It's worth mentioning there are alternative, external logging libraries to Python's default logging library. *Do whatever makes you happy*, just make sure you are logging somehow, especially if you have [automated your Python programs](https://pythonmarketer.wordpress.com/2018/11/25/automated-python-with-windows-task-scheduler/) and want to monitor them. This method has worked for me as someone who previously had no experience whatsoever at logging program error activity. Thank you for reading and enjoying the joy of logging. :)

> *Do whatever makes you happy, because ~~painting~~ coding is individual and you should ~~paint~~ code what you want. *- adapted from Bob Ross

 
