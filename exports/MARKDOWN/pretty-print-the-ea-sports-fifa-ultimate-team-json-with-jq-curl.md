Title: Analyzing Messi vs. Ronaldo with the FIFA API + jq + curl
Date: 2022-01-10 23:15
Author: pythonmarketer
Category: command prompt, productivity
Tags: command line, data, fifa, football, jq, json
Slug: pretty-print-the-ea-sports-fifa-ultimate-team-json-with-jq-curl
Status: published

`<!-- wp:paragraph -->`{=html}

Who is the world's greatest footballer, Messi or Ronaldo? EA Sports surely has calculated the answer to this question in their player ratings. They rate peak Crisitiano Ronaldo, Lionel Messi and Luka Modrić at 99 overall, with Neymar and Lewandowski at 98. Anecdotally, Messi has won 7 [Ballon d'Or](https://www.topendsports.com/sport/soccer/list-player-of-the-year-ballondor.htm), the highest individual football honor one can achieve each year. Ronaldo has won 5 B'allon d'Or. Modrić has won 1 Ballon d'Or. Lewandowski was runner up this year, but has never won the honor. Neymar has never won a Ballon d'Or.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

In [FIFA](https://www.ea.com/games/fifa/fifa-22), a player's video game representation is modeled intricately in a series of traits and specialties characterizing each player. The ["Ultimate Team" EA Sports API](https://www.easports.com/fifa/ultimate-team/api/fut/item) is viewable as a plain json page or more cheekily with one line of [curl](https://curl.se/) and [jq, a "command line json processor"](https://github.com/stedolan/jq):

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
curl 'https://www.easports.com/fifa/ultimate-team/api/fut/item' | jq '.'
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:paragraph -->`{=html}

Enter this in a [shell](https://missing.csail.mit.edu/2020/shell-tools/) or [command line](https://github.com/jlevy/the-art-of-command-line). The result is beautiful, readable, pretty printed json!

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:heading {"level":3} -->`{=html}

### Messi (Left) Vs. Ronaldo (Right) FIFA Player Ratings {#messi-left-vs-ronaldo-right-fifa-player-ratings}

`<!-- /wp:heading -->`{=html}

`<!-- wp:jetpack/tiled-gallery {"columnWidths":[["53.33045","46.66955"]],"ids":[6511,6514]} -->`{=html}

::: {.wp-block-jetpack-tiled-gallery .aligncenter .is-style-rectangular}
::: tiled-gallery__gallery
::: tiled-gallery__row
::: {.tiled-gallery__col style="flex-basis:53.33045%;"}
![](https://pythonmarketer.files.wordpress.com/2022/01/messi-fifa-attributes-cropped.png){data-height="923" data-id="6511" data-link="https://pythonmarketer.com/messi-fifa-attributes-cropped/" url="https://pythonmarketer.files.wordpress.com/2022/01/messi-fifa-attributes-cropped.png?w=433" data-width="433" amp-layout="responsive"}
:::

::: {.tiled-gallery__col style="flex-basis:46.66955%;"}
![](https://pythonmarketer.files.wordpress.com/2022/01/ronaldo-attributes-fifa.png){data-height="955" data-id="6514" data-link="https://pythonmarketer.com/ronaldo-attributes-fifa/" url="https://pythonmarketer.files.wordpress.com/2022/01/ronaldo-attributes-fifa.png?w=392" data-width="392" amp-layout="responsive"}
:::
:::
:::
:::

`<!-- /wp:jetpack/tiled-gallery -->`{=html}

`<!-- wp:paragraph -->`{=html}

These ratings represent the players at their peak of their careers. Messi is a better dribbler, while Ronaldo has more power and strength. Messi has the edge in free kicks, curve in his shot and "longshots" 99 to 98 over Cristiano. They are tied at "finishing", each with 99. Ronaldo has the "Power Free-Kick" trait, whereas Messi has "Chip Shot", "Finesse Shot" and "Playmaker" traits giving him an edge.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

EA's ratings suggest that both are prominent goal scorers, with a slight edge to Messi in finesse and shooting from distance. However, there's something to be said for kicking the ball really damn hard. Ronaldo has superior raw shot power and a lethal combo of more powerful jump and stronger headers. All this combined with an "Aerial Threat" specialty enables Ronaldo to vault above and around defenders to smash in golazos off the volley. Ronaldo sizes up to 6' 2" (187 cm) vs. Messi's 5' 7" (170 cm) frame. This Portugese man definitely has an advantage in getting higher in the air. But the Argentinian is quite darty.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:embed {"url":"https://www.instagram.com/p/Cc59jtvjk_0/","type":"rich","providerNameSlug":"instagram","responsive":true} -->`{=html}

```{=html}
<figure class="wp-block-embed is-type-rich is-provider-instagram wp-block-embed-instagram">
```
::: wp-block-embed__wrapper
https://www.instagram.com/p/Cc59jtvjk_0/
:::

```{=html}
<figcaption>
```
Messi has incredible accuracy from distance.

```{=html}
</figcaption>
```
```{=html}
</figure>
```
`<!-- /wp:embed -->`{=html}

`<!-- wp:paragraph -->`{=html}

Messi is a better passer all around and has perfect "vision", great qualities for winning football games. Only in crossing does he have a lower passing rating. Ronaldo is also 10 points better at "penalties" or penalty kicks. The closer he gets to the goal, the more dangerous he is. Messi is more dangerous with the ball while dribbling, passing or shooting except when taking a PK.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

Advantages can be gained in many different aspects of soccer. EA has developed a fun dataset to model these all time greats across several football skill dimensions. In [2022's version of the game](https://www.ea.com/en-gb/games/fifa/fifa-22/ratings/ratings-database), Messi is rated a 93, with Cristiano 91. Clearly these two are worthy of top honors. Don't forget Robert Lewandowski, with a 92 rating, who consistently lights up the Champions League and Bundesliga.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**jq ftw**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

I had never used jq before this. Really enjoyed the quick, stylish and practical view of some json. This cool terminal display and syntax highlighting was on my Chromebook shell. It's neat how easily you can pretty print json with jq. I rate it a 99 for json pretty printing on the FIFA scale. Read more in the [jq documentation](https://stedolan.github.io/jq/tutorial/)!

`<!-- /wp:paragraph -->`{=html}
