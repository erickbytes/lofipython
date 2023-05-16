Plotting Datasets Using Jupyter, Pandas and Matplotlib
######################################################
:date: 2019-04-12 05:59
:author: pythonmarketer
:category: automation, Chicago, coding, data, pandas, plots, programming
:tags: data analysis, datasets, jupyter, matplotlib, python
:slug: datasets-plotting-using-jupyter-pandas-and-matplotlib
:status: published

I'm new to exploring datasets, but I've already found some great public data online. First, can I say that `Google Dataset Search <https://toolbox.google.com/datasetsearch>`__ is great? I have been enjoying many of the datasets I've found there. Additionally, organizations with public data like the `Chicago Data Portal <https://data.cityofchicago.org/>`__ are interesting to check out. I'm happy to live in a city that provides a lot of its data online for free. Do you know if your city has public data available? I discovered some of this data via sites like `data.world <http://data.world>`__ as well. With playful curiosity and the tools in this article, you will be well equipped to mine insights from any data.\ |screencapture-toolbox-google-datasetsearch-2019-04-11-07_47_50|

**Below, I will highlight three datasets that I recently stumbled into.**

#. Chicago Red Light Camera Violation Data
#. USDA Nutritional Data (2015)
#. Job Computerisation Forecast Data

Installation and Startup
------------------------

**New to Jupyter, pandas or pip? **

Welcome to the club. If you need a run-down on using pip, I wrote `this post <https://pythonmarketer.wordpress.com/2018/01/20/how-to-python-pip-install-new-libraries/>`__ to help sort it out. If you want a superb, gentle and funny introduction to pandas, Jupyter, and data analysis, `this PyCon session <https://www.youtube.com/watch?v=5JnMutdy6Fw>`__ is the best tutorial I have found, by far.

**To run the scripts shown in this post, you must:** (1) install the three libraries below to run in a Jupyter notebook (recommended) **OR** (2) run these plots from the command line and view them as a saved image. To do that, just install pandas and matplotlib.

**First,**\ `install libraries with pip <https://docs.python.org/3/installing/index.html>`__\ **. Enter in command prompt or terminal:**

#. ::

      python -m pip install pandas

#. ::

      python -m pip install matplotlib

#. ::

      python3 -m pip install jupyter

**Then, run Jupyter Notebook**

.. code:: highlight

   jupyter notebook

1. `Chicago Red Light Camera Violations (2014 - 2019) <https://data.cityofchicago.org/Transportation/Red-Light-Camera-Violations/spqx-js37>`__
----------------------------------------------------------------------------------------------------------------------------------------------

*Note the spikes in tickets per day in 2016 and 2017, and the amount of tickets issued in 2016.  Less tickets were issued in 2017 and 2018, after more allegations surfaced about this troublesome red light camera program. Jupyter Notebook with code for both these charts can be found*\ `here <https://github.com/erickbytes/Dataset-Analysis-Notebooks/blob/master/Chicago%20Red%20Light%20Camera%20Tickets%20(2014-2019)/Chicago%20Red%20Light%20Violations.ipynb>`__\ *.*

.. image:: https://pythonmarketer.files.wordpress.com/2019/04/chicago-traffic-violations-per-day-1.png
   :alt: Chicago Traffic Violations Per Day
   :class: wp-image-1751 alignleft
   :width: 322px
   :height: 306px

.. image:: https://pythonmarketer.files.wordpress.com/2019/04/chicago-red-light-violations-by-year.png
   :alt: Chicago Red Light Violations By Year
   :class: wp-image-1745 alignright
   :width: 323px
   :height: 207px

**Chicago's Shady Red Light Camera Program**

2,573,339 violations occurred from July 2014 - March 2019. Personally, I was issued 3 red light camera tickets over the last 5 years. I charted out the tickets by year, month and day.  The below code was used for the left image above, in which I plotted each day of red light camera violations in Chicago over the past 5 years.

::

   import pandas as pd
   import matplotlib.pyplot as plt
   import matplotlib.dates as mdates
   import matplotlib.patches as mpatches
   """
   plotting red light tickets with matplotlib - Python Marketer
   https://atomic-temporary-107329037.wpcomstaging.com/2019/04/12/datasets-plotting-using-jupyter-pandas-and-matplotlib/
   matplotlib.plot_date docs: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot_date.html 
   """
   df = pd.read_csv('Red_Light_Camera_Violations.csv')
   df['VIOLATION DATE'] = pd.to_datetime(df['VIOLATION DATE'])

   """Applying Plot Formatting"""
   plt.style.use('fivethirtyeight')
   years = mdates.YearLocator()
   fig, ax = plt.subplots(1,1)
   fig.set_figheight(5)
   fig.set_figwidth(5)
   ax.xaxis.set_major_locator(years)
   red_patch = mpatches.Patch(color='DarkRed', label='Each Dot is 1 Day')
   plt.legend(handles=[red_patch], fontsize='xx-small')
   plt.rcParams.update({'font.size': 12})

   """Pass pandas columns to plt.plot_date to create and save plot."""
   values = df['VIOLATIONS'] 
   dates = list(df['VIOLATION DATE'])
   plt.plot_date(x=dates, y=values, 
                 color='DarkRed', markersize=3)
   plt.xticks(rotation=0)
   plt.title('Chicago Red Light Ticket Violations - Past 5 Years', 
             fontsize=14)
   plt.savefig('Chicago traffic Violations By Year.png', bbox_inches='tight')

**Analysis:** We can see 2016 is the leader for the past 5 years in amount of violations that occurred. The city of Chicago has drawn criticism for unethical practices in its camera program to reap more revenue. In 2017, the city approved a settlement of "nearly $40 million after a previous class-action lawsuit alleged that the program had violated 1.2 million motorists’ due process rights." (`Source <https://www.illinoispolicy.org/lawsuit-claims-chicago-red-light-cameras-violate-state-law/>`__)

   "A Tribune analysis of more than 4 million tickets issued since 2007 and a deeper probe of individual cases reveal clear evidence that a series of sudden, unexplainable spikes in Chicago's network of 380 cameras were caused by faulty equipment, human tinkering or both. Chicago transportation officials say they had no knowledge of the wild swings in ticketing until they were told by the Tribune — even though City Hall legally required the camera vendor to watch for the slightest anomaly in ticketing patterns every day. Many of the spikes lasted weeks." (`Source <http://graphics.chicagotribune.com/news/local/red-light-timeline/>`__)

`See Full Jupyter Notebook <https://github.com/erickbytes/Dataset-Analysis-Notebooks/blob/master/Chicago%20Red%20Light%20Camera%20Tickets%20(2014-2019)/Chicago%20Red%20Light%20Violations.ipynb>`__

`2. USDA Nutritional Data (2015) <https://www.ars.usda.gov/northeast-area/beltsville-md-bhnrc/beltsville-human-nutrition-research-center/nutrient-data-laboratory/docs/sr28-download-files/>`__
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This USDA data was updated in 2015. It provides many common foods and their nutrient levels, such as carbohydrates and iron, for breads, fruits, vegetables, beverages and most foods you can find in a grocery store. I decided to see which foods contained the most: Sugar, Catbohydrates and Iron. The pandas `nlargest <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.nlargest.html>`__ method made this a breeze.

::

   import pandas as pd
   import matplotlib.pyplot as plt

   df = pd.read_excel('ABBREV.xlsx')
   df = df.sort_values(by=['Sugar_Tot_(g)'], ascending=False)
   df = df[df.Shrt_Desc.str.contains(pat='CEREALS,', 
                                     na=False,
                                     case=False)]
   df = df.nlargest(n=15, columns='Sugar_Tot_(g)')
   df.plot.barh(x='Shrt_Desc', y='Sugar_Tot_(g)',
                color='DarkBlue', legend=False)
   plt.xlabel(xlabel='Grams of Sugar')
   plt.ylabel(ylabel='Foods')
   plt.title('Most Sugar, Cereals - USDA', fontsize=14)
   plt.gca().invert_yaxis()

::

..

   **"Research suggests that as many as 80 percent of people in the world don't have enough iron in their bodies." -World Health Organization **

|Foods with The Most Iron - USDA|\ **Analysis:** Instant oatmeal and cereals are the highest in sugar content. Stay away from them if possible.  If you need to boost your iron levels, beef and pork are good options. If you don't eat meat, certain spices and wheat bran/flakes contain high levels of iron. Seaweed is also a good, iron rich snack. Ultimately, there are lots of ways to get iron in your diet besides meat.

`See Full Jupyter Notebook <https://github.com/erickbytes/Dataset-Analysis-Notebooks/blob/master/USDA%20Nutritional%20Data%20(2015)/USDA%20Food%20Nutrition.ipynb>`__

3. `Job Computerisation Forecast Data <https://data.world/quanticdata/occupation-and-salary-by-state-and-likelihood-of-automation/workspace/query?queryid=51754b08-7414-4f76-8a31-8b5c75166146>`__
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This data orignates from a 2013 University of Oxford study and the United States Bureau of Labor Statistics. It provides two key values: probability (%) that a job will be computerised within 1-2 decades, and the number of jobs that currently exist for that profession in each state.

::

   import pandas as pd
   import matplotlib.pyplot as plt
   import matplotlib.patches as mpatches

   """
   plotting occupational automation risk - Python Marketer
   https://atomic-temporary-107329037.wpcomstaging.com/2019/04/12/datasets-plotting-using-jupyter-pandas-and-matplotlib/

   Find most common Illinois jobs affected and at highest risk of automation.
   Source Data: https://data.world/quanticdata/occupation-and-salary-by-state-and-likelihood-of-automation/workspace/query?queryid=51754b08-7414-4f76-8a31-8b5c75166146

   plt.text matplotlib docs: https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.text.html 
   """

   file_name = 'high-risk-in-your-st-occupation-and-salary-by-state-and-likelihood-of-automation-QueryResult.csv'
   df = pd.read_csv(file_name)
   df = df.sort_values(by=['probability'], ascending=False)
   df = df.nlargest(30, 'Illinois')
   df = df[df['probability'] >= 0.95] # gets  "highest risk" subset

   df.plot.barh(x='occupation', y='Illinois', 
                color='DarkBlue', legend=False, figsize=(15,10))

   # add corresponding percent over each bar
   probs = list(df['probability']) 
   for i, v in enumerate(probs):
       percent = str(v).replace('0.','') + '%'
       plt.text(x=v+3, 
                y=i+.25, 
                s=percent, 
                color='white', 
                fontweight='bold', 
                fontsize=26)

   white_patch = mpatches.Patch(color='white', 
                                label='Est. % Probability of Computerisation')
   plt.legend(handles=[white_patch], fontsize='xx-large')
   plt.xticks(fontsize=18, rotation=0) 
   plt.yticks(fontsize=18) 
   plt.gca().invert_yaxis()
   plt.xlabel('Est. Number of Jobs At Risk in Illinois', fontsize=18) 
   plt.ylabel('Occupation', fontsize=18)
   plt.title('Most Common Illinois Jobs at "Highest Risk" of Being Computerised Within 15 Years', fontsize=20)
   plt.annotate('Source: Carl Benedikt Frey and Michael A. Osborne (2013 University of Oxford Study)', (0,0), (0, -60), xycoords='axes fraction', textcoords='offset points', va='top')
   plt.annotate('Source: data.world/quanticdata & Bureau of Labor Statistics', (0,0), (0, -80), xycoords='axes fraction', textcoords='offset points', va='top')
   plt.savefig('Most Common Jobs at "High Risk" of Being Computerised.png', bbox_inches='tight')

.. image:: https://pythonmarketer.files.wordpress.com/2019/04/job_computerisation.png
   :alt: job_computerisation
   :class: alignnone size-full wp-image-1734
   :width: 1614px
   :height: 672px

**Analysis:** It's strange to think that these common jobs, which currently make up a large portion of our economy, will likely be computerised some day. They all seem to be entry-level manual tasks. The promise of automation is that it frees humans up to focus on more meaningful or complex problems. How will the 125,000 cashiers in Illinois adapt when that is no longer a way to earn money?

`See Full Jupyter Notebook <https://github.com/erickbytes/Dataset-Analysis-Notebooks/blob/master/Illinois%20Job%20Computerisation%20Forecast/Job%20Automation%20Forecast%20-%20Illinois.ipynb>`__

**The Plot Thickens...**

I've barely scratched the surface in my experience with datasets, but already found some very interesting data to inspect and play with. These data visualization skills are adaptable to many situations. All you need is good data to bring to life. Stay curious, my friends.

**Additional reading**

`Matplotlib: Beyond the Default <https://uppsala.instructure.com/courses/28112/files?preview=1042670>`__

.. |screencapture-toolbox-google-datasetsearch-2019-04-11-07_47_50| image:: http://pythonmarketer.files.wordpress.com/2019/04/de1c3-screencapture-toolbox-google-datasetsearch-2019-04-11-07_47_50-e1555047601227.png
   :class: alignleft size-full wp-image-1736
   :width: 917px
   :height: 295px
   :target: https://toolbox.google.com/datasetsearch
.. |Foods with The Most Iron - USDA| image:: https://pythonmarketer.files.wordpress.com/2019/04/foods-with-the-most-iron-usda.png
   :class: alignnone size-full wp-image-1754
   :width: 718px
   :height: 279px
