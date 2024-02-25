A Collection of Software Testing Opinions for Python and Beyond
###############################################################
:date: 2019-12-05 03:06
:author: pythonmarketer
:category: coding, productivity, programming, python, software testing
:tags: pytest, software development, test driven development
:slug: a-collection-of-software-testing-opinions-for-python-and-beyond
:status: published

I am a beginner to testing my code. I wanted to write about testing to better understand it. While shaping this link fest masquerading as an essay, I collected great ideas from people who are way more experienced than me. You'll find a few of my thoughts, a Pytest example I use to monitor files, ideas for unit testing, property testing, test driven development and many other commonly used software tests.

**An Introductory Rant on Testing**

Over several years as a programmer, I've slowly grasped the landscape of testing in software development. After moving beyond my first few tutorials and projects, it seemed very noisy to sort out. Examples provided are usually simple assertions that seem tough to relate to a real use case. It might be easy test the wrong things. Plus, some don't do it at all! The quality of the tests is more important than the quantity. But what makes a quality test? Where's the balance between testing every minute detail of a program and not at all?

   Yeah. And the worst thing that happens is that you get people that just stop *thinking* about what they’re doing. “This is the principle, to always write unit tests, so I’m always going to write unit tests,” and then they’re just not thinking about how they’re spending their time, and they wind up wasting a lot of it.

   Joel Spolsky, `Stack Overflow Podcast #38 <https://www.joelonsoftware.com/2009/01/>`__

Implementing software tests is a best practice for maintaining code, but seems ambiguous to someone who has not tested any code before. I guess the best way is 
to `read open source projects with test suites <https://github.com/pyodide/pyodide/tree/main>`__, but those can be tough to find. How do you know `a good test suite <https://docs.python-guide.org/writing/reading/>`__ when you see it? Maybe the maintainers went rogue and off the deep end with tests. 
Online, everybody says you should test your code, `is the emperor wearing any clothes? <https://en.wikipedia.org/wiki/The_Emperor%27s_New_Clothes>`__

As a beginner stumbling across articles on testing, these questions were tough to answer. As with most things in programming, figuring out the right question to ask is a challenge in itself. `Codeacademy <https://www.codecademy.com/learn/learn-python-3>`__ and `Coursera <https://www.coursera.org/specializations/python>`__ never mentioned anything about writing tests. On the other hand, `Django <https://docs.djangoproject.com/en/2.2/intro/tutorial05/>`__ includes testing in its tutorial and documentation. Also, most languages come with built-in testing tools. Python has the `unittest <https://docs.python.org/3/library/unittest.html>`__ library.

**Why test at all? First, some solid benefits of software testing:**

-  With tests on your code in place, you can implement changes and have confidence the code still works if the tests pass. This gives developers more confidence to iterate and improve an application.
-  Detect problems faster. Passing tests are a good indicator that your programs are actually doing what they're supposed to do. If they don't pass, you likely found a bug you might have missed otherwise.
-  When you find a bug, you either need to amend your code, or your tests. write a test for that bug and then fix it. Either that, or you need to be amend your tests. You've just improved the quality of your test suite.
-  `Automation <https://daedtech.com/dont-learn-to-code-learn-to-automate/>`__. If you are writing tests, those tests can be automated. If you are manually checking the results of your program, you're missing a chance to automate those checks away. I haven't applied it yet, but have heard the `Tox library <https://tox.readthedocs.io/en/latest/>`__ may be useful to automate tests related to Python packaging. For more on automating tests, see this PyCon talk, `Three Excellent Python Tools to Automate Repetitive Tasks <https://www.youtube.com/watch?v=-BHverY7IwU>`__.
-  Test Driven Development can decrease the time spent debugging code. This claim sometimes lacks empirical evidence, supporting evidence tends to be anecdotal.

..

   A good unit test, therefore, is one that helps enforce the contract to which the function is committed.

   If a good unit test breaks, the contract is violated and should be either explicitly amended (by changing the documentation and tests), or fixed (by fixing the code and leaving the tests as is).

   A good unit test is also *strict*. It does its best to ensure the output is valid. This helps it catch more bugs.

   - Moshe Zadka, `Precise Unit Tests With pyhamcrest <https://orbifold.xyz/pyhamcrest.html>`__

**Pytest and Unit Testing in Python**

This is where the Python hits the pavement. Unit tests are generally liked, although some prefer property tests or integration tests because they think the scope of unit tests is too narrow. The `unittest <https://docs.python.org/3/library/unittest.html>`__ library is Python's default testing framework. However nowadays, `pytest <https://docs.pytest.org/en/latest/contents.html>`__ seems to be the preferred unit testing framework for Python. `Hypothesis <https://hypothesis.readthedocs.io/en/latest/>`__ is another popular framework I've read about.

**Pytest Testing**

-  `Interview with the author of Pytest <https://realpython.com/interview-brian-okken/>`__

-  `Pytest Documentation <https://docs.pytest.org/en/latest/>`__

-  `Pytest Features That You Need In Your Life <https://martinheinz.dev/blog/7>`__

-  `Table Driven Unit Testing With pytest <http://love-python.blogspot.com/2017/10/table-driven-unit-test-in-python.html>`__

-  `Reproducible Data Analysis in Jupyter, Part 6/10: Unit Testing with PyTest <https://www.youtube.com/watch?v=Pf1ADyUKOrE>`__ [YouTube]

..

   Tests start to lose signal when `Mock <https://docs.python.org/3/library/unittest.mock.html>`__ becomes routine instead of a reluctant workaround. - Brandon Rhodes, `When Python Practices Go Wrong <https://www.youtube.com/watch?v=S0No2zSJmks>`__

**Testing in Python \\ General Unit Testing Ideas**

-  `Testing Conventions for the Pandas Library <https://github.com/pandas-dev/pandas/wiki/Testing>`__
-  `How to Create a Dataframe for Testing <https://kanoki.org/2019/11/18/how-to-create-dataframe-for-testing/>`__
-  `Improve Your Python: Understanding Unit Testing <https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing//>`__
-  `Write Unit Tests <http://kbroman.org/blog/2015/12/07/write-unit-tests/>`__
-  `Writing Unit Tests for Time <https://henrikwarne.com/2013/12/08/tdd-unit-tests-and-the-passage-of-time/>`__
-  `5 Unit Testing Mistakes <https://henrikwarne.com/2014/02/19/5-unit-testing-mistakes/>`__
-  `Unit Tests Are Not Tests <https://hillelwayne.com/post/unit-tests-are-not-tests/>`__
-  `The Best New Feature in unittest You Didn't Know You Need <https://hakibenita.com/the-best-new-feature-in-unittest-you-didnt-know-you-need>`__
-  `Precise Unit Tests With pyhamcrest <https://orbifold.xyz/pyhamcrest.html>`__
-  `The Flawed Theory Behind Unit Testing <https://michaelfeathers.typepad.com/michael_feathers_blog/2008/06/the-flawed-theo.html>`__
-  `Django Introduction to Automated Testing <https://docs.djangoproject.com/en/2.2/intro/tutorial05/>`__
-  `Python Doc Tests <https://hillelwayne.com/post/python-doctests/>`__ Turn docstrings into tests, unique to Python.

..

   I think `hypothesis <https://hypothesis.readthedocs.io/en/latest/>`__ is probably underrated—some libraries are hesitant to incorporate it into their testing frameworks, but I think the property-based testing has real potential to catch scenarios humans would have a hard time anticipating, or at least that would take a long time to properly plan for. I find that hypothesis almost always adds a few useful test cases I hadn’t thought of that will require special error handling, for example.

   `Tyler Reddy <http://www.blog.pythonlibrary.org/2020/01/13/pydev-of-the-week-tyler-reddy/>`__, SciPy Release Manager

**Integration \\ Property Tests**

-  `Unit Tests Are Good, Integration Tests Are Gooder <https://blog.juliobiason.me/books/things-i-learnt/integration-tests/>`__
-  `PROPERTY TESTS + CONTRACTS = INTEGRATION TESTS <https://hillelwayne.com/post/pbt-contracts/>`__
-  `Finding Property Tests <https://hillelwayne.com/post/contract-examples/>`__
-  `In Praise of Property-Based Testing <https://increment.com/testing/in-praise-of-property-based-testing/>`__
-  `Contracts <https://hillelwayne.com/post/contracts/>`__

..

   Traditional, or example-based, testing specifies the behavior of your software by writing examples of it—each test sets up a single concrete scenario and asserts how the software should behave in that scenario. Property-based tests take these concrete scenarios and generalize them by focusing on which features of the scenario are essential and which are allowed to vary. This results in cleaner tests that better specify the software’s behavior—and that better uncover bugs missed by traditional testing.

   - David Maciver, `In Praise of Property-based Testing <https://increment.com/testing/in-praise-of-property-based-testing/>`__

**Assertions**

Assertions are generally accepted as welcome additions to your code.

-  `Use of Assertions <https://blog.regehr.org/archives/1091>`__
-  `Fuzzers Love Assertions <http://www.squarefree.com/2014/02/03/fuzzers-love-assertions/>`__
-  `pytest Assertions <https://docs.pytest.org/en/latest/assert.html#assert>`__

..

   In reality, the safety and restraints that these code carabiners provide actually give you **more freedom** to take risks in your coding. If you want to try out some risky feature, refactoring, or external library, you know something is wrong as soon as one of your assertions or tests fail and can undo back to an earlier working state.

   Phillip J. Guo, Code Carabiners, (Link Broken)

**Test Driven Development**

Eventually, you'll discover the evangelists preaching Test Driven Development. There are certain discussions which polarize us in the software development world, such as the appropriate scenarios to deploy this system of development.

Opinions vary widely on the merits and appropriate application of TDD. I'm admittedly skeptical but do see the merits of TDD. But which flavor? Where do unit tests and integration tests fit in? How many tests should I write? What exactly should I be testing? `This essay <https://georgestocker.com/2019/12/10/is-pair-programming-tdd-worth-it/?utm_source=rss&utm_medium=rss&utm_campaign=is-pair-programming-tdd-worth-it>`__ claims anyone pair programming software with an expected life of 3 or more years should use Test Driven Development.

-  `When TDD is Not a Good Fit <https://henrikwarne.com/2019/09/29/when-tdd-is-not-a-good-fit/>`__
-  `Test Driven Development vs. Test Last Development <http://neverworkintheory.org/2016/10/05/test-driven-development.html>`__ [Study]
-  `Why TDD Is Crap <https://www.youtube.com/watch?v=DQBf6li1hww>`__ [YouTube]
-  `Why TDD Isn't Crap <https://hillelwayne.com/post/why-tdd-isnt-crap/>`__ [Response Blog to Video]
-  `Testing Isn't Everything <https://www.arp242.net/testing.html>`__
-  `Is Pair Programming + TDD worth it? <https://georgestocker.com/2019/12/10/is-pair-programming-tdd-worth-it/?utm_source=rss&utm_medium=rss&utm_campaign=is-pair-programming-tdd-worth-it>`__

..

   "Test Driven Development is a tool for continuously evaluating hypotheses."

   - `James Shore, Assert(JS) Con 2019 <https://www.youtube.com/watch?time_continue=170&v=UOOuW5tqT8M&feature=emb_logo>`__

**General Testing Ideas and Principles**

-  `Testing Your Code <https://docs.python-guide.org/writing/tests/>`__, The Hitchhiker's Guide to Python
-  `The Point of Software Testing <https://blog.liw.fi/posts/2019/06/29/dijkstra_was_only_partially_correct_about_testing/>`__
-  `Connecting Bug Fixing to Automated Testing <https://rachelbythebay.com/w/2013/01/30/test/>`__
-  `Thinking in Tests <https://www.jamesshore.com/In-the-News/Thinking-In-Tests.html>`__ [YouTube]
-  `Some empirically derived testing principles <https://www.drmaciver.com/2015/04/some-empirically-derived-testing-principles/>`__
-  `Testing Vs. Informal Reasoning <https://danluu.com/tests-v-reason/>`__
-  `How I Write Tests <https://blog.nelhage.com/2016/12/how-i-test/>`__
-  `Stop Mocking, Start Testing <https://www.youtube.com/watch?v=Xu5EhKVZdV8>`__ [YouTube]
-  "`Each one of these projects is a paragon of Python coding. <https://python-guide-es.readthedocs.io/es/latest/writing/reading.html>`__"
-  `What it's Like to Be a Developer at... <https://increment.com/development/what-its-like-to-be-a-developer-at/>`__ [Testing Practices Described]
-  `Hammock Driven Development <https://www.youtube.com/watch?v=f84n5oFoZBc>`__ [YouTube] Not so much testing focused, but including because I really enjoyed this talk.

**Other common tests types:**

   Unit test: when it fails, it tells you what piece of your code needs to be fixed.

   Integration test: when it fails, it tells you that the pieces of your application are not working together as expected.

   Acceptance test: when it fails, it tells you that the application is not doing what the customer expects it to do.

   Regression test: when it fails, it tells you that the application no longer behaves the way it used to.

   - `Mathias, Stack Overflow Answer <https://stackoverflow.com/questions/7672511/unit-test-integration-test-regression-test-acceptance-test>`__

**Testing maturity level progression:**

#. No tests
#. Occasional, slow, unreliable tests
#. Semi-comprehensive integration tests
#. Fast, comprehensive unit tests comprise the bulk of testing

   -  Dependency injection
   -  Composable subsystem design

#. Real-time test feedback (ideally integrated into the editor)
#. Tests are extremely reliable or `guaranteed reliable by the type system <http://andyfriesen.com/2015/06/17/testable-io-in-haskell.html>`__

   -  With tooling that tracks the reliability of tests and provides that feedback to authors.

#. Fuzzing, statistically automated microbenchmarking, rich testing frameworks for every language and every platform, and a company culture of writing the appropriate number of unit tests and high-value integration tests.

- `ChadAustin.me <https://chadaustin.me/2019/11/two-years-at-dropbox/>`__

**I recently wrote my first unit tests with pytest. Below is a script named test_file_date.py. It tests if the day of month of the most recently changed file in a directory matches today's day. To install pytest, enter into command prompt or terminal:**

``python -m pip install pytest``

**test_file_date.py**

.. code-block:: python

   import glob
   import os
   from datetime import datetime, date

   # The dir_query format is for a Windows path with Unix style pattern matching.
   def test_csv_date_equals_today():
       dir_query = 'C:\\Users\\your_username\\Desktop\\*.csv' # specify csv extension and folder
       file_path = sorted(glob.iglob(dir_query), key=os.path.getmtime)[-1] # get most recent file
       file_timestamp = os.path.getmtime(file_path)
       file_date = datetime.fromtimestamp(file_timestamp)
       print(file_date.day)
       print(date.today().day)
       assert file_date.day == date.today().day

| **Run the test with pytest by entering:**
| ``pytest test_file_date.py``

| **Conclusion**
| I write programs for personal productivity and to `automate processes <https://lofipython.com/automated-python-with-windows-task-scheduler/>`__. The scope of problems my code solves has grown with my programming ability. I'm now reaching the point where I can apply tests to my advantage. However, sometimes I'll write a quick-hitter script for which I can't justify writing tests. Beyond those cases, testing can help if you pick the right style for your project. More so for recurring, automated processes.

It feels pretty cool when your tests run and you know with more certainty whether a part of your program is getting the job done or not. After setting up my first test with pytest, I have leveled up to novice tester, instead of blissfully not knowing what I don't know about testing. That's a step in the right direction.
