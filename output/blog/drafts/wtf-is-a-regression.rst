WTF is a Regression
###################
:date: 2018-10-19 03:15
:author: pythonmarketer
:category: data analysis, math, python, statistics
:tags: data science, mathematics, regressions, sci-kit learn
:slug: wtf-is-a-regression
:status: published

**re·gres·sion**

[caption id="attachment_1500" align="alignright" width="467"]\ |mitnewslol.png| wtf is a regression? - MIT News and I[/caption]

| /rəˈɡreSH(ə)n
| *noun*
| 1. a return to a former or less developed state.
| 2. *STATISTICS* a measure of the relation between the mean value of one variable (e.g., output) and corresponding values of other variables (e.g., time and cost).

Regression analysis is commonly cited in the data science community (and science in general), a building block of statistics, and routinely referenced within the rapidly growing `machine learning <https://en.wikipedia.org/wiki/Machine_learning>`__ movement. So what is this mysterious math sorcery? Did Isaac Newton use regression analysis? These magical regressions seem important. We shall dig deeper. Here's what I've found, thanks to `MIT News <http://news.mit.edu/2010/explained-reg-analysis-0316>`__, circa 2010:

   To grasp the basic concept, take the simplest form of a regression: a linear, bivariate regression, which describes an unchanging relationship between two (and not more) phenomena. Now suppose you are wondering if there is a connection between the time high school students spend doing French homework, and the grades they receive. These types of data can be plotted as points on a graph, where the x-axis is the average number of hours per week a student studies, and the y-axis represents exam scores out of 100. Together, the data points will typically scatter a bit on the graph. The regression analysis creates the single line that best summarizes the distribution of points.

Ok, so it's correlationary tool. Sounds useful. Additionally, consider the mathematical  equation representation of regressions:

   Mathematically, the line representing a simple linear regression is expressed through a basic equation: Y = a\ :sub:`0` + a\ :sub:`1` X. Here X is hours spent studying per week, the “independent variable.” Y is the exam scores, the “dependent variable,” since — we believe — those scores depend on time spent studying. Additionally, a\ :sub:`0` is the y-intercept (the value of Y when X is zero) and a\ :sub:`1` is the slope of the line, characterizing the relationship between the two variables. (**source:\ **\ `MIT News) <http://news.mit.edu/2010/explained-reg-analysis-0316>`__

Geesh, that's kinda dense. But can we do it with Python? Ah, yes we can. Below is the amassed code from `Towards Data Science <http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html>`__ to run a basic regression that generates predictions from a Boston house values dataset within `sci-kit learn. <http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html>`__

`pip install sklearn <https://scikit-learn.org/stable/install.html>`__\ **and pandas first, by entering in the terminal:**

#. ::

      pip install -U scikit-learn

#. ::

      python -m  pip install pandas

**Now run copy this code, save as a .py file  and run from your terminal or command prompt:**

::

   from sklearn import linear_model
   from sklearn import datasets ## imports datasets from scikit-learn
   import pandas as pd
   data = datasets.load_boston() ## loads Boston dataset from datasets library

   # define the data/predictors as the pre-set feature names
   df = pd.DataFrame(data.data, columns=data.feature_names)

   # Put the target (housing value -- MEDV) in another DataFrame
   target = pd.DataFrame(data.target, columns=["MEDV"])

   X = df
   y = target["MEDV"]

   lm = linear_model.LinearRegression()
   model = lm.fit(X,y)
   predictions = lm.predict(X)
   print(predictions[0:5]) # print the first 5 predictions for y

   lm.score(X,y) # This is the R² score of our model. As you probably remember, this the percentage of explained variance of the predictions.
   lm.coef_ # check coefficients
   lm.intercept_
   # More info: https://towardsdatascience.com/simple-and-multiple-linear-regression-in-python-c928425168f9

*source:*\ `Towards Data Science <https://towardsdatascience.com/simple-and-multiple-linear-regression-in-python-c928425168f9>`__

The above example is one of many predictive models. `Logistic regressions <https://towardsdatascience.com/building-a-logistic-regression-in-python-step-by-step-becd4d56c9c8>`__ and random forests are examples of other models. `This book <https://books.google.com/books/about/Learning_Predictive_Analytics_with_Pytho.html?id=Ia5KDAAAQBAJ&printsec=frontcover&source=kp_read_button#v=onepage&q&f=false>`__ dives deeper into them.

So there you have it: regressions... part correlation measurement tool between two variables, part fancy mathematical formula, part prediction generator that sci-kit learn graciously affords us to make predictions of future data. Alright regressions, you can stay. :)

.. |mitnewslol.png| image:: http://pythonmarketer.files.wordpress.com/2018/10/9ed88-mitnewslol-e1539920605255.png
   :class: alignnone wp-image-1500
   :width: 467px
   :height: 273px
