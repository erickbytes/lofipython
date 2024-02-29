Reflections on 5 Years of Solving Problems with Python
######################################################
:date: 2020-04-11 17:15
:author: pythonmarketer
:category: coding, education, Marketing, programming, python, wisdom
:tags: advice, learning, problem solving, writing
:slug: reflections-on-5-years-of-solving-problems-with-python
:status: published

Prior to learning Python, I had no programming experience. I worked in marketing for a book publisher and did not perform well at my job. It was not a good fit. They eventually fired me. As my previous job unraveled, I discovered Python and the Coursera course, `Programming for Everybody (Getting Started with Python) <https://www.coursera.org/learn/python?utm_medium=email&utm_source=other&utm_campaign=opencourse.course_complete.python.%7Eopencourse.course_complete.7A1yFTaREeWWBQrVFXqd1w.>`__. Fortunately, that course jump-started me onto a path of learning and reading each day. My aim was to make my own website, a `goal that I accomplished <https://pythonmarketer.wordpress.com/2016/05/25/askkevinparker-com-my-first-web-app-other-notes/>`__. I needed to know how the sausage was made.

Looking back from 2020, I can safely say Python changed my life. Because of it, I now have a fulfilling marketing\data-oriented career. I'm also grateful for the financial stability that came with it. I love to learn about the language and continue to improve my abilities to solve problems with new tools, not only Python.

Below are pieces of wisdom picked up from my experiences. They are the result of many hours of study, reading, mistakes, luck, toil and eventual glory.

**These are thought-provoking adages and guidelines, not absolute truths in all cases.**

#. Developing a habit of learning pays off over time, no matter what the subject is. It is an investment in yourself that compounds.
#. Follow your own curiosity. It's less important to compare what you know to others. Compare what you know today to what you knew yesterday. Don't worry about `how long it takes to learn <https://nedbatchelder.com/blog/202003/how_long_did_it_take_you_to_learn_python.html>`__.
#. Watch educational or technical conference talks on sites like `YouTube <https://www.youtube.com/channel/UCMjMBMGt0WJQLeluw6qNJuA/videos>`__ or InfoQ. `Rich Hickey, <https://www.infoq.com/presentations/Simple-Made-Easy/>`__ `Brandon Rhodes <https://rhodesmill.org/brandon/talks/#selenium-at-scale>`__ and `David Beazley <https://www.youtube.com/watch?v=lyDLAutA88s>`__ are some of my favorite speakers. Watch talks from all languages, not just Python. Often the concepts apply to any programming language.
#. Use an RSS reader. Anytime you find a good blog, subscribe by RSS or email to get new posts. I use the `Feeder Chrome extension <https://chrome.google.com/webstore/detail/rss-feed-reader/pnjaodmkngahhkoihejjehlcdlnohgmp?hl=en>`__\\Android app.
#. The `Zen of Python <https://www.python.org/dev/peps/pep-0020/>`__ contains a lot of wisdom. I like the concept of ``Explicit is better than implicit.`` This implies declaring your actions in written or oral fashion, providing additional context. Consider favoring easier to read solutions over clever one-liners. For example:

   -  `List comprehensions <https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions>`__ are useful and "pythonic", use them! But sometimes it's easier to use a for loop to hash out an idea. (Contrarily, avoiding the `Initialize Then Modify <https://www.youtube.com/watch?v=W-lZttZhsUY>`__ pattern benefits those comfortable with comprehensions.)
   -  Explicitly using `keyword arguments <https://treyhunner.com/2018/04/keyword-arguments-in-python/>`__ versus positional arguments is another way to make your code easier to understand.

#. Can you explain the solution simply? If not, try to clarify your understanding or maybe there's a simpler way. In Python, there are often several ways to accomplish the same goal. But keep in mind the Zen of Python: ``There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch.`` Look for the obvious way. An example of this is `string formatting. <https://www.blog.pythonlibrary.org/2020/04/07/python-101-working-with-strings/>`__ I've heard f-strings are the hot new way to do this now.
#. Don't be afraid to change course if things don't feel right. Ask yourself while coding, "Does this feel efficient?" Recently I was trying to format a json string so I approached it like I had in the past, by `exporting the request from Postman and formatting the json string <https://lofipython.com/how-to-make-json-requests-with-python/>`__ with python's `format() built-in <https://docs.python.org/3/library/functions.html?highlight=format#format>`__. But this time, the curly braces were confusing me, I was struggling and it wasn't working. I googled and around and saw python's `json module <https://docs.python.org/3/library/json.html?highlight=json#module-json>`__ and `df.to_json() <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html>`__ in pandas. They were a much easier and better-looking solution. But it still wasn't working. Finally, i used the Postman approach and f-strings to format a successful payload. The third try worked! F-strings are super nice and clean.
#. If you're stuck, there's probably a free online course or blog post that explains whatever is confusing you. Use the Googles. When in doubt, Google the error message.
#. Begin your project by writing a list of requirements. This often leads to good questions and cases that may need to be addressed. The book `Code Complete 2 <https://www.amazon.com/gp/product/0735619670/>`__ covers establishing project requirements in great detail, along with the other stages in the life-cycle of a software project. I'm really enjoying this book and highly recommend it.
#. Names are really important. Take time to think about a good name for your variables and functions. Also, name your scripts well. I name my scripts using `action verbs <https://examples.yourdictionary.com/action-verb-examples.html>`__. For example, my script that organizes accumulated files on my desktop into folders is named ``clean_desktop_files.py``. When I see this script months later, its name reminds me the action the script is performing. I believe it's better to err on the side of longer, more descriptive names for variables and functions. It makes code easier to understand. But there is a trade-off with length to keep in check.
#. Moving a block of code into a function can abstract away repetitive code and increase its readability.
#. Each function should do one thing only. Follow the `single-responsibility principle <https://en.wikipedia.org/wiki/Single-responsibility_principle>`__.
#. Train yourself to think in `data structure <https://docs.python.org/3/tutorial/datastructures.html>`__ conversions. The Python dictionary is very useful and can be converted to and from lists, tuples, sets, etc. I often find it more efficient to convert to a different structure to efficiently organize it. Usually I am googling things like "convert class object to python dictionary" because dictionaries are easy to work with or convert to other structures. The ``vars()`` built-in is great for converting objects to a dictionary. For example, once you have a dictionary, you might be able to solve your problem by `converting it to a dataframe <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.from_dict.html>`__.
#. Use only the data you need. Reading in just the essential data helps avoid memory issues and hanging programs. In `pandas <https://pythonmarketer.wordpress.com/2018/04/10/creating-isolated-python-environments-with-virtualenv/>`__, the ``usecols`` argument in `pd.read_csv() <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html>`__ is great for this. This creates a dataframe with 2 columns:

.. code-block:: python

    df = pd.read_csv('emails.csv', usecols=['name','email'])

15. Assume that if something is broken, it's because of something you've done. Start from the assumption that your code contains the bug and work outward by eliminating possibilities. Avoid jumping to quick conclusions. Instead, carefully consider possible reasons for why something is happening. Many times, I find my 2nd or 3rd hypothesis is actually true.

16. There will be times when you'll look at someone else's choices and wonder why they did things a certain way. Consider the possibility that they know more than you in this domain.

17. Beware of sequencing errors. Are your tasks, scripts or functions executing in an efficient order to reach your end goal? Look to unblock bottlenecks and correct chronological mistakes in your processes.

18. Before you send that email asking for help, go back and take another look. There's also no shame in asking for help. Be sure you proofread your email before sending.

19. `Status code 200 <https://en.wikipedia.org/wiki/List_of_HTTP_status_codes>`__ does not guarantee your API request was successful. You may want to write a test to confirm success that doesn't rely on response status codes.

20. Unfortunately, `testing <https://lofipython.com/a-collection-of-software-testing-opinions-for-python-and-beyond/>`__ gets shunned sometimes. Make it a priority. I enjoy writing `pytest tests <https://lofipython.com/automating-pytest-on-windows-with-a-bat-file-python-task-scheduler-and-box/>`__ more than most other code. Why? Because tests confirm my scripts are working to some degree, detect bugs and provide a refactoring safety net.

21. Refactoring your code is a crucial step in making it better. Coming back to my code after a few weeks, months or years brings clarity, experience and a new perspective. It feels good to improve the quality of my old work.

22. Consolidate your tasks. Bundling things can save you a bundle of time! Identify redundant patterns and remove if possible. Observe yourself while working. Any repetitive manual process can probably be automated away. Recently, I figured out how to use a `Windows batch file <https://www.windowscentral.com/how-create-and-run-batch-file-windows-10>`__ to instantly activate my Python `virtual environment <https://pythonmarketer.wordpress.com/2018/04/10/creating-isolated-python-environments-with-virtualenv/>`__. It took me a few years of tediously pasting the ``cd`` and ``activate`` commands into command prompt every day to realize. Now it's a snap.

23. Stack Overflow is a useful resource. But the top answers may be outdated. Check the other less popular answers sometimes. Or...

24. Read the documentation! An updated or more elegant solution might be there. I recently found ``os.makedirs(path, exist_ok=True)`` in the `os docs <https://docs.python.org/3/library/os.html#os.makedirs>`__. I didn't know about the ``exist_ok`` argument. I was creating folders with a more complicated alternative from `Stack Overflow <https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory>`__ for years. I use this way all the time now. In the same vein, if you need the local system username, the Python docs state `getpass.getuser() <https://docs.python.org/3.8/library/getpass.html>`__ is preferred over os.getlogin().

25. Write documentation explaining how to use your projects. Even if you can only muster a quick `README <https://en.wikipedia.org/wiki/README>`__ text file, that's better than nothing. Within your code, `docstrings <https://www.python.org/dev/peps/pep-0257/>`__ are a nice addition. I have yet to use `Sphinx <https://www.sphinx-doc.org/en/master/>`__, but it is a popular choice for generating documentation.

26. Teaching others feels good and solidifies your knowledge. Writing and pair programming are great ways to improve your understanding and pass your skills along to other people. While we're on the subject of writing...

27. Write everything down! Your head is not good at storing information in memory. Computers are. This frees your mind to come up with new ideas rather than expending energy to remember what you've already done. It also helps you plan. I use a Notepad text file to keep a running to-do list. You could also use services like Trello or Microsoft Planner. While writing code, use comments and docstrings conservatively for quick notes, clarifications or reminders. The important thing is to write it down somewhere.

28. When editing your writing, continually ask yourself, "Do I need this word or phrase?" for every word you write.

..

   "Brevity is the soul of wit." - William Shakespeare (Hamlet)

29. Draw inspiration from culture, nature and professional disciplines outside of your own. `Insights can be mined from anything <https://lofipython.com/lessons-learned-from-lost-in-space-on-netflix/>`__. Don't dismiss a situation as mundane without first scanning for knowledge nuggets and gems.
30. Better solutions often come to me after gaining time and experience with a problem. Building software is an iterative cycle of adjustment towards consistently fulfilling the needs of those it serves in 100% of cases. In a perfect world, you'd never have bugs. But edge cases tend to pop up in ways you didn't think of when you first wrote a solution. There will also be projects where requirements or business rules change. Consider that possibility when you are designing your solution.
31. It's possible to find a job that you're excited about and genuinely enjoy the work.
32. Respect your craft, whether it's coding or another profession. A skilled carpenter needs precision, practice and focus to make something beautiful. Approach your craft with the same mindset and pride in making your best art.
33. We all have holes in our knowledge. Be receptive to other ways of thinking. The best way to learn is from other humans. Everyone has different backgrounds and experiences. I have never used object oriented programming, classes or certain command line tools like `ssh <https://www.howtogeek.com/336775/how-to-enable-and-use-windows-10s-built-in-ssh-commands/>`__. I have a loose understanding of these things but have not yet applied them to my projects. Working with paths (os and pathlib) still gives me fits sometimes. These are knowledge gaps that I want to fill in. Additionally, we don't know what we don't know. Try to illuminate the fog of your unknown.
34. Choosing to dedicate to learning Python is among the best decisions I've made.
35. Attitude is more important than intelligence. Anyone can learn to program, play guitar or fly an airplane. You can become an adept problem solver. Acquire an attitude to support your determination and persistence.

[caption id="attachment_2981" align="alignnone" width="959"]\ |brandonrhodes| Brandon Rhodes: Stopping to Sharpen Your Tools - PyWaw Summit 2015[/caption]

**I'll leave you with the 4 P's and 4 C's from my** `Programming for Everybody Coursera course graduation ceremony <https://www.youtube.com/watch?v=SfQYA0JQWkA>`__\ **. Cultivating these principles will guide you to growing your education and finding a positive course in life:**

   **4 P's:** Passion, Purpose, Persistence, Playfulness

   **4 C's:** Choice, Commitment, Connection, Completion

Thank you for reading and I hope this post helps you on your own educational journey.

.. |pytest_test_results| image:: https://pythonmarketer.files.wordpress.com/2020/04/pytest_test_results.png
   :class: alignnone size-full wp-image-3108
   :width: 941px
   :height: 540px
.. |brandonrhodes| image:: https://pythonmarketer.files.wordpress.com/2020/04/brandonrhodes.png
   :class: alignnone size-full wp-image-2981
   :width: 959px
   :height: 541px
   :target: https://www.youtube.com/watch?v=I56oFTm9UlE
