How to Track Python Script Completion
#####################################
:date: 2022-01-05 11:49
:author: pythonmarketer
:category: coding, programming, python, Scripts
:tags: logging, python scripts, reliability, tracking
:slug: how-to-track-python-script-completion
:status: published

Did your script run to completion? Sure, you might log some tracebacks along the way or terminate the program early with `sys.exit() <https://docs.python.org/3/library/sys.html#sys.exit>`__. But did your script actually run completely to the end? I have yet to use the `Trace module <https://docs.python.org/3/library/trace.html>`__ but it seems worth checking out also. Visualization tools like `heartrate <https://github.com/alexmojaki/heartrate>`__ are worth mentioning too depending on how you are running your scripts. Task runners typically have run status tracking as well. I like having a visual confirmation by logging some sort of information when a script finishes as intended. It's nice to know when your scripts finished or not. Use logging and Trace to up your reliability of your scripts.

**Another anecdotal way to track this is with the logging module:**

.. code-block:: python

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
