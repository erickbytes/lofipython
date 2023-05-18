Automating pytest on Windows with a .bat file, Python, Task Scheduler and Box
#############################################################################
:date: 2020-03-21 01:47
:author: pythonmarketer
:category: automation, programming, software testing, Windows
:tags: coding, pytest, python, software development
:slug: automating-pytest-on-windows-with-a-bat-file-python-task-scheduler-and-box
:status: published

**Automatic pytest Testing and Failure Alert Monitoring**

This is my solution to replace manually running pytest each day in command prompt. I want to automate running pytest every day, test if my automated python scripts ran smoothly and get notified if any tests fail.

**Installing **\ `pytest <https://docs.pytest.org/en/latest/getting-started.html>`__\ **, a python testing library:**

``python -m pip install pytest``

**A Few Words on pytest**

It is a unit test framework in python. pytest expects you to write each test as a self-contained function. One python file can contain many different test functions.

**Writing a Test**

Let's use **test_file_date.py** as our test, which uses the `glob <https://docs.python.org/3/library/glob.html>`__ module and `os.getmtime <https://docs.python.org/2/library/os.path.html#os.path.getmtime>`__\  to get the csv with the most recent modification dateon my desktop. Then it tests if that date is today, in my case, for an expected daily file drop.

.. code-block:: python

    from datetime import datetime, date
    import glob
    import os
    import getpass

    def test_csv_date_equals_today():
        """The dir_query format is for a Windows path with Unix style pattern matching."""
         # specify csv extension and folder
        match = f'C:Users/{getpass.getuser()}/Desktop/*.csv'
        # get most recent file
        csv = sorted(glob.iglob(dir_query), key=os.path.getmtime)[-1]
        csv_timestamp = os.path.getmtime(csv)
        csv_date = datetime.fromtimestamp(csv_timestamp)
        print(csv_date.day)
        print(date.today().day)
        assert csv_date.day == date.today().day
        

**Here's the pytest text output when the test is passing:**

::

   ============================= test session starts =============================
   platform win32 -- Python 3.8.1, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
   rootdir: C:\
   collected 1 item

   ..\..\Users\martech\Desktop\test_file_date.py . [ 14%]
                                                                      [100%]

   ============================== 1 passed in 0.28s ==============================

**Creating a Task with Windows Task Scheduler**

If you haven't used python with Windows Task Scheduler before, `my previous post <https://pythonmarketer.wordpress.com/2018/11/25/automated-python-with-windows-task-scheduler/>`__ on creating a task may help you. We'll create two of them for our testing system.

**Adding Your Task Scheduler Program: a Windows .bat file**

Add your username to the text below and adjust the paths to your system. Then save a `Windows .bat file <https://en.wikipedia.org/wiki/Batch_file>`__ with this text, which points to your pytest.exe file:

::

   cmd /c "C:\Users\your_username\Desktop\VM_Jobs\Scripts\pytest.exe --capture=sys" ^
   C:\Users\your_username\Desktop\test_file_date.py > C:\Users\your_username\Desktop\VM_Jobs\Test_Results\Test_Results.txt

This example is referencing an .exe within a hypothetical "VM_Jobs" `virtual environment <https://pythonmarketer.wordpress.com/2018/04/10/creating-isolated-python-environments-with-virtualenv/>`__, located on my Desktop. If you have a virtualenv or venv, check the Scripts folder. (Bin on Linux.)

**Breaking this out, there are five .bat files parts:**

   cmd /c "C:\Users\your_username\Desktop\VM_Jobs\Scripts\pytest.exe --capture=sys"

Windows' `cmd command <https://ss64.com/nt/cmd.html>`__ takes a program, so we're passing pytest. `The --capture=sys argument <https://docs.pytest.org/en/latest/capture.html>`__ tells pytest to capture the test results. **Note:** switching cmd /c to cmd /k forces the terminal to stay open when you are testing your bat file. You can double-click your .bat file to test run it.

   ^

circumflex represents a line continuation in Windows batch files for better readability

   C:\Users\your_username\Desktop\test_file_date.py

Next we're passing our python file as an argument to pytest, testing our file's modified date matches today's date.

   **>**

This is a Windows redirect. It redirects the pytest output from sys to a text file, which is the last argument in our .bat file:

    C:\Users\your_username\Desktop\VM_Jobs\Test_Results\Test_Results.txt

**Browse to select your .bat file for your Windows Task Scheduler task:**

.. image:: https://pythonmarketer.files.wordpress.com/2020/03/bat_task.jpg
   :alt: bat_task
   :class: alignnone size-full wp-image-2669
   :width: 1032px
   :height: 590px

**Reading the Tests and Triggering Alerts**

Passing tests signal your scripts are running successfully. When things don't work, email alerts of the failure help us respond quickly.

Let's set another task scheduler job to run **read_test_results.py,** to run a few minutes after the first job each day. See this `example of running Python with Task Scheduler <https://pythonmarketer.wordpress.com/2018/11/25/automated-python-with-windows-task-scheduler/>`__ if you haven't triggered a python script from Task Scheduler before.

.. code-block:: python

    from datetime import date
    import getpass
    import logging
    import os

    """Automate pytest with Windows Task Scheduler
    Use Task Scheduler run a batch file. The batch file runs pytest and captures our pytest function results to sys.
    If a text file contains a failure or error, write the test contents into a folder.
    """
    logging.basicConfig(
        filename="Automated_Testing_Alerts.log",
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
    )
    logging.info("Checking for failed tests...")
    directory = f"C:/Users/{getpass.getuser()}/Desktop/test_results/"
    test_results = [fname for fname in os.listdir(directory) if ".txt" in fname]
    for txt_file in test_results:
        file_path = directory + txt_file
        with open(file_path) as f:
            text = f.read()
        if "FAILURES" in text:
            directory = f"C:/Users/{user_name}/Desktop/send_failure_alert/"
            today = str(date.today())
            name = f"{directory}{txt_file}_Failed_Results_{today}.txt"
            with open(name, "w+") as f:
                f.write(name)
                f.write(text)
        else:
            print("No failed tests found in file:")
            print(txt_file)

**Setting up Email Alert Notifications on a Box Folder**

The above script checks the test results and creates a file with any failed tests in a different folder. I `edited the folder's settings <https://support.box.com/hc/en-us/articles/360044194073-Manage-Notifications-for-Enterprise-Users>`__ to email me when a new file is added, thanks to Box notifications. We use `Box <http://www.box.com>`__ for secure file sharing at my day current day job.

Alternatively for those without Box, you could use 'ole trusty `smtplib <https://docs.python.org/3/library/smtplib.html>`__ to send the failure alerts with python. I chose the easier, ready to go option. Remember, "`Simple is better than complex <https://zen-of-python.info/simple-is-better-than-complex.html>`__."

Or the `pywin32 module <https://github.com/mhammond/pywin32>`__ has an interface to Outlook that is very handy. For an example of sending a Windows Outlook email, check the very end of `this post I wrote on "Scripting Windows Like a Pro" <http://pythonmarketer.wordpress.com/2020/05/06/exploring-windows-command-line-tools-batch-file-automation-and-remote-desktop-connection/>`__.

**We now have an automated testing system with email monitoring alerts if our csv file date test fails, thanks to:**

-  Windows Task Scheduler (two tasks running each day in succession)
-  python/pytest
-  a Windows .bat file
-  Box (or smtplib or pywin32) email alerts

**In Summation**

#. The first task runs a .bat file to run pytest and create a text file with daily automation test results.
#. The second task runs a python file. Setting in motion:
#. Checking the test result text files, looking for failed tests
#. Creating a text file with any failing tests in a Box folder, if found
#. Then Box emails me if any test fails.

**Final Thoughts on the .bat**

This was the first time I successfully deployed a Windows batch file. It took me many tries and googling to properly format of the .bat file. They are worth understanding and seem to open up many possibilities on Windows. In this case it was a "glue" piece that allowed me to accomplish my goal, automated testing and alerts for my python scripts.

**Life is in the journey.**

What we learn along the way shapes us. Learning to use these resources together has been a giant step towards writing more reliable python programs. It has improved my knowledge of Windows OS scripting, which can sometimes be a handy substitute or complement to python. Now, time to write more tests. Thanks for reading!

**See also:**

`pytest plugins <_wp_link_placeholder>`__

`pytest-csv <https://pypi.org/project/pytest-csv/>`__: write test results to a csv with this plugin

I wrote another post compiling peoples' thoughts on testing `here <https://pythonmarketer.wordpress.com/2019/12/05/a-collection-of-software-testing-opinions-for-python-and-beyond/>`__.


