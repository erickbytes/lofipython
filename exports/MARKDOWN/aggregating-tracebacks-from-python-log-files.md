Title: Aggregating A Python Error Summary from Log Files
Date: 2021-04-06 01:09
Author: pythonmarketer
Category: automation, coding, education, programming, Scripts
Tags: productivity, python
Slug: aggregating-tracebacks-from-python-log-files
Status: published

`<!-- wp:paragraph -->`{=html}

Follow these steps to maintain more reliable scripts and catch more of your traceback errors:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:list {"ordered":true} -->`{=html}

1.  automate your scripts to run daily, weekly, monthly, etc.
2.  [Log all your traceback errors](https://pythonmarketer.wordpress.com/2019/02/02/the-joy-of-logging-with-python/) with the [logging module](https://docs.python.org/3/library/logging.html). I like dumping all of my logs into a single folder.
3.  automate aggregating the logs and parsing tracebacks
4.  start a feedback loop of fixing the tracebacks until 0 tracebacks remain
5.  re-run the script and confirm tracebacks disappeared

`<!-- /wp:list -->`{=html}

`<!-- wp:syntaxhighlighter/code -->`{=html}

``` wp-block-syntaxhighlighter-code
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
```

`<!-- /wp:syntaxhighlighter/code -->`{=html}

`<!-- wp:paragraph -->`{=html}

This pure python script allows me to hone in on potential automation problem areas with my scheduled Python scripts. It doesn't catch the entire traceback. Rather, it shows the error type and the name of the log file that contains that error in a csv. I use this log aggregation script to monitor my daily or weekly scheduled python scripts, along with [pytest tests](https://pythonmarketer.wordpress.com/2020/03/21/automating-pytest-on-windows-with-a-bat-file-python-task-scheduler-and-box/).

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Noteworthy gains from aggregating my logs:**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:list -->`{=html}

-   less fear of missing mistakes
-   more freedom to improve the code
-   catch the mistakes faster

`<!-- /wp:list -->`{=html}

`<!-- wp:paragraph -->`{=html}

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

See also: [Python Documentation - Basic Logging Tutorial](https://docs.python.org/3/howto/logging.html)

`<!-- /wp:paragraph -->`{=html}
