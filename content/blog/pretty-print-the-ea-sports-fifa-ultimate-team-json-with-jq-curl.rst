Analyzing Messi vs. Ronaldo with the FIFA API + jq + curl
#########################################################
:date: 2022-01-10 23:15
:author: pythonmarketer
:category: command prompt, productivity
:tags: command line, data, fifa, football, jq, json
:slug: pretty-print-the-ea-sports-fifa-ultimate-team-json-with-jq-curl
:status: published

Who is the world's greatest footballer, Messi or Ronaldo? EA Sports surely has calculated the answer to this question in their player ratings. They rate peak Crisitiano Ronaldo, Lionel Messi and Luka Modrić at 99 overall, with Neymar and Lewandowski at 98. Anecdotally, Messi has won 7 `Ballon d'Or <https://www.topendsports.com/sport/soccer/list-player-of-the-year-ballondor.htm>`__, the highest individual football honor one can achieve each year. Ronaldo has won 5 B'allon d'Or. Modrić has won 1 Ballon d'Or. Lewandowski was runner up this year, but has never won the honor. Neymar has never won a Ballon d'Or.

In `FIFA <https://www.ea.com/games/fifa/fifa-22>`__, a player's video game representation is modeled intricately in a series of traits and specialties characterizing each player. The `"Ultimate Team" EA Sports API <https://www.easports.com/fifa/ultimate-team/api/fut/item>`__ is viewable as a plain json page or more cheekily with one line of `curl <https://curl.se/>`__ and `jq, a "command line json processor" <https://github.com/jqlang/jq>`__:

::

   curl 'https://www.easports.com/fifa/ultimate-team/api/fut/item' | jq '.'

Enter this in a `shell <https://missing.csail.mit.edu/2020/shell-tools/>`__ or `command line <https://github.com/jlevy/the-art-of-command-line>`__. The result is beautiful, readable, pretty printed json!

.. _messi-left-vs-ronaldo-right-fifa-player-ratings:

Messi (Top) Vs. Ronaldo (Bottom) FIFA Player Ratings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. container:: tiled-gallery__gallery

      .. container:: tiled-gallery__row

         .. container:: tiled-gallery__col

            .. figure:: https://pythonmarketer.files.wordpress.com/2022/01/messi-fifa-attributes-cropped.png
               :alt: Messi FIFA skill attributes

         .. container:: tiled-gallery__col

            .. figure:: https://pythonmarketer.files.wordpress.com/2022/01/ronaldo-attributes-fifa.png
               :alt: Ronaldo FIFA skill attributes

These ratings represent the players at their peak of their careers. Messi is a better dribbler, while Ronaldo has more power and strength. Messi has the edge in free kicks, curve in his shot and "longshots" 99 to 98 over Cristiano. They are tied at "finishing", each with 99. Ronaldo has the "Power Free-Kick" trait, whereas Messi has "Chip Shot", "Finesse Shot" and "Playmaker" traits giving him an edge.

EA's ratings suggest that both are prominent goal scorers, with a slight edge to Messi in finesse and shooting from distance. However, there's something to be said for kicking the ball really damn hard. Ronaldo has superior raw shot power and a lethal combo of more powerful jump and stronger headers. All this combined with an "Aerial Threat" specialty enables Ronaldo to vault above and around defenders to smash in golazos off the volley. Ronaldo sizes up to 6' 2" (187 cm) vs. Messi's 5' 7" (170 cm) frame. This Portugese man definitely has an advantage in getting higher in the air. But the Argentinian is `quite darty <https://www.instagram.com/p/Cc59jtvjk_0/>`__.

Messi has incredible accuracy from distance. He's also a better passer all around and has perfect "vision", great qualities for winning football games. Only in crossing does he have a lower passing rating. Ronaldo is also 10 points better at "penalties" or penalty kicks. The closer he gets to the goal, the more dangerous he is. Messi is more dangerous with the ball while dribbling, passing or shooting except when taking a PK.

Advantages can be gained in many different aspects of soccer. EA has developed a fun dataset to model these all time greats across several football skill dimensions. In `2022's version of the game <https://www.ea.com/en-gb/games/fifa/fifa-22/ratings/ratings-database>`__, Messi is rated a 93, with Cristiano 91. Clearly these two are worthy of top honors. Don't forget Robert Lewandowski, with a 92 rating, who consistently lights up the Champions League and Bundesliga.

**jq ftw**

I had never used jq before this. Really enjoyed the quick, stylish and practical view of some json. This cool terminal display and syntax highlighting was on my Chromebook shell. It's neat how easily you can pretty print json with jq. I rate it a 99 for json pretty processing and pretty printing on the FIFA scale. Read more in the `jq documentation <https://stedolan.github.io/jq/tutorial/>`__!
