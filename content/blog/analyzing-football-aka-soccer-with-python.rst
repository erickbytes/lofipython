Analyzing Football AKA Soccer With Python
#########################################
:date: 2023-07-27 22:23
:author: lofipython
:category: football, coding, programming, python, sports
:tags: python football analytics Python football heat map, football data analytics, Python soccer analytics
:slug: analyzing-football-aka-soccer-with-python
:status: published


The world's game is fun to watch. It's obvious when a team is dominant against a weaker opponent. What gives one team an edge over another? Is it short, crisp and reliable passing resulting in a high conversion percentage? Or shots on goal? Clinicality in the final third is what separates the Champions from the rest. Making the most of your chances.

We all have our theories to what makes a great player or team. But how do we assess football performance from an analytics perspective? It is difficult to predict how teams with varying styles will match up. Fortunately, data is integrating with the football world. Extensive analytics resources and tactics now available for free online. 

If you're interested in football analytics, there seems to be a few areas you can go. Do you need to collect data? If you can record a game correctly, it can be converted into data from which winning insights are extracted. If you are lucky enough to already have data, what does it say about player and team performance? Can you study open data from professional teams to explore your hypotheses? 

Searching the internet, FC Python was the first thing I saw. They have some `free tools <https://fcpython.com/free-football-data-analysis-tools>`__ available for collecting data from live games. I was impressed at the Python code for `pitch heat maps <https://fcpython.com/visualisation/football-heatmaps-seaborn>`__ to track Abby Wombach's passing. Their example uses `seaborn <https://seaborn.pydata.org/>`__ and `matplotlib <https://matplotlib.org/>`__:


.. code-block:: python


    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.patches import Arc
    import seaborn as sns

    %matplotlib inline

    data = pd.read_csv("Data/passes.csv")
    data.head()

    fig, ax = plt.subplots()
    fig.set_size_inches(14, 4)

    # Plot One - distinct areas with few lines
    plt.subplot(121)
    sns.kdeplot(data["Xstart"], data["Ystart"], shade="True", n_levels=5)

    # Plot Two - fade lines with more of them
    plt.subplot(122)
    sns.kdeplot(data["Xstart"], data["Ystart"], shade="True", n_levels=40)

    plt.show()

    # Create figure
    fig = plt.figure()
    fig.set_size_inches(7, 5)
    ax = fig.add_subplot(1, 1, 1)

    # Pitch Outline & Centre Line
    plt.plot([0, 0], [0, 90], color="black")
    plt.plot([0, 130], [90, 90], color="black")
    plt.plot([130, 130], [90, 0], color="black")
    plt.plot([130, 0], [0, 0], color="black")
    plt.plot([65, 65], [0, 90], color="black")

    # Left Penalty Area
    plt.plot([16.5, 16.5], [65, 25], color="black")
    plt.plot([0, 16.5], [65, 65], color="black")
    plt.plot([16.5, 0], [25, 25], color="black")

    # Right Penalty Area
    plt.plot([130, 113.5], [65, 65], color="black")
    plt.plot([113.5, 113.5], [65, 25], color="black")
    plt.plot([113.5, 130], [25, 25], color="black")

    # Left 6-yard Box
    plt.plot([0, 5.5], [54, 54], color="black")
    plt.plot([5.5, 5.5], [54, 36], color="black")
    plt.plot([5.5, 0.5], [36, 36], color="black")

    # Right 6-yard Box
    plt.plot([130, 124.5], [54, 54], color="black")
    plt.plot([124.5, 124.5], [54, 36], color="black")
    plt.plot([124.5, 130], [36, 36], color="black")

    # Prepare Circles
    centreCircle = plt.Circle((65, 45), 9.15, color="black", fill=False)
    centreSpot = plt.Circle((65, 45), 0.8, color="black")
    leftPenSpot = plt.Circle((11, 45), 0.8, color="black")
    rightPenSpot = plt.Circle((119, 45), 0.8, color="black")

    # Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)

    # Prepare Arcs
    leftArc = Arc(
        (11, 45), height=18.3, width=18.3, angle=0, theta1=310, theta2=50, color="black"
    )
    rightArc = Arc(
        (119, 45), height=18.3, width=18.3, angle=0, theta1=130, theta2=230, color="black"
    )

    # Draw Arcs
    ax.add_patch(leftArc)
    ax.add_patch(rightArc)

    # Tidy Axes
    plt.axis("off")

    sns.kdeplot(data["Xstart"], data["Ystart"], shade=True, n_levels=50)
    plt.ylim(0, 90)
    plt.xlim(0, 130)

    # Display Pitch
    plt.show()


.. image:: {static}/blog/images/pitchheatmap.png
  :alt: Analyzing football with Python

This code is meant for a `Jupyter notebook <https://jupyter.org/install>`__. However, I can't find the "passes.csv" data referenced online to test it out. Still, impressive use of matplotlib and seaborn!

Of course, in analytics data is king. Without it, you're the jester. If you need some data to chew on, check out statsbomb. Its a free footy dataset that's on display in this `Towards Data Science blog post <https://towardsdatascience.com/how-to-easily-get-football-data-with-a-python-package-without-web-scraping-c922e7ebfb41>`__. In another practical example of wrangling data, Tactics FC shows how to `calculate goal conversion rate with pandas <https://medium.com/@TacticsFC/analyzing-football-data-with-python-7b4e89c7abd8>`__. I'm guessing basic statskeeping and video is collected in great quantities by analytics teams during games for professional teams. At half time, typically on TV they will show both teams' shots, passes and time of possession. 

Another intriguing tactic is extensive tracking of individual player position and simulation on the pitch. Google hosted a `Kaggle competition with Manchester City <https://www.kaggle.com/competitions/google-football/code>`__ 3 years ago, where the goal was to train AI agents to play football. Formal courses are available like the `Mathematical Modeling of Football course at Uppsala University <https://www.uu.se/en/study/course?query=1RT001>`__. There's also the `football analytics topic <https://github.com/topics/football-analytics>`__ on Github that shows 100+ repos for those who want to dive into analytics tools. 

From that topic, I found `Awesome Football Analytics <https://github.com/diegopastor/awesome-football-analytics>`__, which is a long list of resources to browse through. It seems wise to stop through Jan Van Haren's `soccer analytics resources <https://github.com/JanVanHaaren/soccer-analytics-resources>`__. I'm really looking forward to checking out `Soccermatics for Python <https://github.com/Friends-of-Tracking-Data-FoTD/SoccermaticsForPython/>`__ also. There is a ton of stuff online about football analytics that is happening.

I sense there is a passionate community pushing football analytics forward and innovating. There are many facets to consider from video optimization, data collection, drawing insights from established datasets, tracking game stats and codifying player movements. 

Watching football is so satisfying. Why not study it with Python? My prediction is that the beautiful game will progress and improve as teams develop a more sophisticated data strategy.