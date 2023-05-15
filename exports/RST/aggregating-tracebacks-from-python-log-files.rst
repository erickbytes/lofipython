Aggregating A Python Error Summary from Log Files
#################################################
:date: 2021-04-06 01:09
:author: pythonmarketer
:category: automation, coding, education, programming, Scripts
:tags: productivity, python
:slug: aggregating-tracebacks-from-python-log-files
:status: published

Follow these steps to maintain more reliable scripts and catch more of your traceback errors:

#. automate your scripts to run daily, weekly, monthly, etc.
#. `Log all your traceback errors <https://pythonmarketer.wordpress.com/2019/02/02/the-joy-of-logging-with-python/>`__ with the `logging module <https://docs.python.org/3/library/logging.html>`__. I like dumping all of my logs into a single folder.
#. automate aggregating the logs and parsing tracebacks
#. start a feedback loop of fixing the tracebacks until 0 tracebacks remain
#. re-run the script and confirm tracebacks disappeared

.. code:: wp-block-syntaxhighlighter-code

   import itertools
   import os

   def parse_errors(log):
       """look in each log file, line by line for Python error keywords"""
       errors = list()
       with open(log,'r') as f:
           for line in f:
               if 'Traceback' in line or 'Error' in line:
                   # replace commas for csv
                   line = line.strip().replace(',','')
                   errors.append([log,line])
           return errors

   """
   parse traceback errors from log files in current working directory 
   and write to them to a csv file
   """
   logs = [f for f in os.listdir(os.getcwd()) if '.log' in f.lower()]
   tracebacks = [parse_errors(log) for log in logs]
   # dedupe list of lists with itertools module + list comprehension
   tracebacks = [t for t,_ in itertools.groupby(tracebacks)]
   with open('Log Traceback Errors.csv', 'w') as fhand:
       fhand.write('Log,Traceback') # csv header row
       for t in tracebacks:
           for error in t:
               fhand.write(f"\n{','.join(error)}")

This pure python script allows me to hone in on potential automation problem areas with my scheduled Python scripts. It doesn't catch the entire traceback. Rather, it shows the error type and the name of the log file that contains that error in a csv. I use this log aggregation script to monitor my daily or weekly scheduled python scripts, along with `pytest tests <https://pythonmarketer.wordpress.com/2020/03/21/automating-pytest-on-windows-with-a-bat-file-python-task-scheduler-and-box/>`__.

**Noteworthy gains from aggregating my logs:**

-  less fear of missing mistakes
-  more freedom to improve the code
-  catch the mistakes faster

See also: `Python Documentation - Basic Logging Tutorial <https://docs.python.org/3/howto/logging.html>`__
