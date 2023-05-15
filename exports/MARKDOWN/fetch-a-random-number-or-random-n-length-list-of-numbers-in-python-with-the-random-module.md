Title: Retrieve Random Numbers Via Python's random Module + range() Built-in
Date: 2022-09-15 23:09
Author: pythonmarketer
Category: coding, programming, python
Tags: python random numbers list, random module, random numbers python
Slug: fetch-a-random-number-or-random-n-length-list-of-numbers-in-python-with-the-random-module
Status: published

`<!-- wp:paragraph -->`{=html}

There are usually many ways to do most things in Python. I've retrieved random numbers a few different ways at various times within the random module, often after reading a Stack Overflow post. This time in my most recent search for random digits, I discovered in the Python docs the [random.sample()](https://docs.python.org/3/library/random.html#random.sample) function with its k parameter:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:quote -->`{=html}

> `<!-- wp:paragraph -->`{=html}
>
> Return a *k* length list of unique elements chosen from the population sequence or set. Used for random sampling without replacement.
>
> `<!-- /wp:paragraph -->`{=html}`<cite>`{=html}https://docs.python.org/3/library/random.html#random.sample`</cite>`{=html}

`<!-- /wp:quote -->`{=html}

`<!-- wp:paragraph -->`{=html}

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

When combined with the [range() built-in](https://docs.python.org/3.3/library/stdtypes.html?highlight=range#range), it makes doing this easy. Being able to specify a length and return a list of random numbers is mighty convenient. This function seems a Pythonic way to randomize to me. Have a look!

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:syntaxhighlighter/code -->`{=html}

``` wp-block-syntaxhighlighter-code
import random
# Returns a list of 5 random numbers.
numbers = random.sample(range(10000000), k=5)
print(numbers)
# Returns a single random number.
number = random.sample(10000000), k=1)[0]
print(number)
```

`<!-- /wp:syntaxhighlighter/code -->`{=html}

`<!-- wp:image {"id":7196,"sizeSlug":"large","linkDestination":"none"} -->`{=html}

![](https://pythonmarketer.files.wordpress.com/2022/09/image-2.png?w=552){.wp-image-7196}

`<!-- /wp:image -->`{=html}

`<!-- wp:quote -->`{=html}

> `<!-- wp:paragraph -->`{=html}
>
> To choose a sample from a range of integers, use a [`range()`](https://docs.python.org/3/library/stdtypes.html#range) object as an argument. This is especially fast and space efficient for sampling from a large population: `sample(range(10000000), k=60)`.
>
> `<!-- /wp:paragraph -->`{=html}`<cite>`{=html}https://docs.python.org/3/library/random.html#random.sample`</cite>`{=html}

`<!-- /wp:quote -->`{=html}
