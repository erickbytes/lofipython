Title: Google Vision OCR, Image Text and a Markov Chain: a recipe for positivipy
Date: 2020-10-11 15:37
Author: pythonmarketer
Category: coding, data analysis, Google, pandas, programming, python
Tags: Google Vision, natural language, positive thinking, positivity
Slug: generating-positive-thoughts-with-google-vision-ocr-and-markov-chains
Status: published

`<!-- wp:paragraph -->`{=html}

**Introduction**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

Recently an old idea came back to life. I've posted to a [Facebook Page](https://www.facebook.com/positivedailythought) for several years as part of project I started on a whim. The goal of the page is to share anything positive and inspirational by famous thinkers, artists and creators I read, or simply something positive to meditate on. It was partially inspired by the discipline of "[Positive Psychology](https://en.wikipedia.org/wiki/Positive_psychology)". Basically, William James was a cool dude. [Martin Seligman](https://www.ted.com/talks/martin_seligman_the_new_era_of_positive_psychology/transcript?language=en) is too. I believe that positive feelings create positive outcomes and we can "game" ourselves into this feedback loop with literature and other habits that support well-being like sleep and exercise.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

After building up years of posts, I pondered for years how to capture the dataset of quote images to generate new positive-minded prose. This post details one implementation and alternatives I considered to accomplish this goal. All of the data and code in this post is [published on Github](https://github.com/erickbytes/positivipy). Possibly will post my entire [flask website](http://positivipy.com) there eventually! Here's how I made my latest project, [positivipy](https://positivethoughts.pythonanywhere.com/).

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Project Overview**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:list {"ordered":true} -->`{=html}

1.  Export all Facebook post images from my page
2.  Convert images to quote text with **Optical character recognition** (OCR)
3.  Data cleaning (via pandas and manual correction)
4.  Train on past quotes and generate new quotes with a Markov chain

`<!-- /wp:list -->`{=html}

`<!-- wp:heading {"level":3} -->`{=html}

### 1. Export all Facebook post images from my page {#1-export-all-facebook-post-images-from-my-page}

`<!-- /wp:heading -->`{=html}

`<!-- wp:paragraph -->`{=html}

Facebook made this easy. I exported all of my timeline photos by [following these instructions](https://www.facebook.com/help/466076673571942).

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:heading {"level":3} -->`{=html}

### 2. Converting images to quote text with OCR {#2-converting-images-to-quote-text-with-ocr}

`<!-- /wp:heading -->`{=html}

`<!-- wp:quote -->`{=html}

> `<!-- wp:paragraph -->`{=html}
>
> **Optical character recognition** or **optical character reader** (**OCR**) is the [electronic](https://en.wikipedia.org/wiki/Electronics) or [mechanical](https://en.wikipedia.org/wiki/Machine) conversion of [images](https://en.wikipedia.org/wiki/Image) of typed, handwritten or printed text into machine-encoded text, whether from a scanned document, a photo of a document, a scene-photo
>
> `<!-- /wp:paragraph -->`{=html}`<cite>`{=html}Wikipedia - https://en.wikipedia.org/wiki/Optical_character_recognition`</cite>`{=html}

`<!-- /wp:quote -->`{=html}

`<!-- wp:paragraph -->`{=html}

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

Once I had a folder of .jpg images, I used the [Google Vision API](https://github.com/googleapis/python-vision)'s OCR to detect the text in the images. I also considered using the open source [Calamari OCR library](https://github.com/Calamari-OCR/calamari), but my research found that Google's Vision API may be more effective at detecting text.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

Since I had only 771 images, I was able to extract text on all of them and stay within Google's free plan (1,000 requests / month). I [followed these installation instructions](https://cloud.google.com/vision/docs/quickstart) on my Ubuntu Linux computer. It worked well on most of the images. Here's the code I used to detect text in all my images and save it in a .csv file:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:syntaxhighlighter/code {"language":"python"} -->`{=html}

``` wp-block-syntaxhighlighter-code
import io
import os
from google.cloud import vision
import pandas as pd


"""
Setup Instructions
1) Save this as detect_image_text.py
2) Create a folder named 'photos' and put your photos in them.
3) in your terminal, run: python detect_image_text.py
"""

def detect_text(path):
    """Detects text in the file."""
    
    client = vision.ImageAnnotatorClient()

    with io.open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print("Texts:")

    for text in texts:
        return text.description

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(
                response.error.message))

images = os.listdir("/images")
img_text = list()
for i, img in enumerate(images):
    try:
        img_path = f"photos/{img}"
        text = detect_text(img_path)
        img_text.append(text)
        print(f"{i}: {text}")
    except:
        print(f"Failed: {img}")

quotes_df = pd.DataFrame(img_text, columns=["Text"])
csv = "Extracted Image Text.csv"
quotes_df.to_csv(csv, index=False)
```

`<!-- /wp:syntaxhighlighter/code -->`{=html}

`<!-- wp:heading {"level":3} -->`{=html}

### 3. Data cleaning (via [pandas](https://pythonmarketer.wordpress.com/2018/05/12/pandas-pythons-excel-powerhouse/) and manual correction) {#3-data-cleaning-via-pandas-and-manual-correction}

`<!-- /wp:heading -->`{=html}

`<!-- wp:paragraph -->`{=html}

The data did not come back perfect, but I was pleased with the Google Vision API's results. It saved me a lot of time compared to manually transcribing the images! Next I used pandas to clean the data. You can see more in a Jupyter notebook with [all of the code on github](https://github.com/erickbytes/positivipy). Then I manually removed the author or source names, keeping only the quote text.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:heading {"level":3} -->`{=html}

### 4. Train on past quotes and generate new quotes {#4-train-on-past-quotes-and-generate-new-quotes}

`<!-- /wp:heading -->`{=html}

`<!-- wp:paragraph -->`{=html}

**GPT-3, The State of the Art Option**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

Initially, I considered machine learning options for generating new text. The GPT-3 library, released in early 2020 by Open AI, is the current state of the art model for text generation. However, its API is only accessible on an invite basis. If I get access, I think I'll try using it with the [GPT-Sandbox](https://github.com/shreyashankar/gpt3-sandbox) python library. 🤞 You can join the [GPT-3 waitlist here](https://share.hsforms.com/1Lfc7WtPLRk2ppXhPjcYY-A4sk30).

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

I searched around for other text generation python libraries on Github and found a promising one named [GPT-2_simple](https://github.com/minimaxir/gpt-2-simple), which utilizes GPT-3's predecessor. However, it requires using an old version of TensorFlow. I feel less inclined to learn older versions of machine learning libraries. Currently, I'm holding out for GPT-3 access. I may try the GPT-2 route if I don't get a chance at GPT-3.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**A "[Simple is Better Than Complex](https://zen-of-python.info/simple-is-better-than-complex.html)" Approach: Markov Chain**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

I wondered, are there any simpler options for text generation in python? Enter the Markov chain, which I stumbled across while Googling.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:quote -->`{=html}

> `<!-- wp:paragraph -->`{=html}
>
> A **Markov chain** is a stochastic model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event.
>
> `<!-- /wp:paragraph -->`{=html}`<cite>`{=html}Wikipedia - https://en.wikipedia.org/wiki/Markov_chain`</cite>`{=html}

`<!-- /wp:quote -->`{=html}

`<!-- wp:paragraph -->`{=html}

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Using the markovify library**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

Google pointed me to [this post from Analytics India Magazine](https://analyticsindiamag.com/hands-on-guide-to-markov-chain-for-text-generation/) showing the ["Markovify" library](https://github.com/jsvine/markovify). Markovify makes generating your own Markov chain very easy! Install with pip:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

`pip install markovify`

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

Here's the code to create Markov chain on the quote text:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:syntaxhighlighter/code -->`{=html}

``` wp-block-syntaxhighlighter-code
import markovify
# Build a markov chain model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())
```

`<!-- /wp:syntaxhighlighter/code -->`{=html}

`<!-- wp:paragraph -->`{=html}

Markov chains are below the level of sophistication of machine learning technologies like GPT-3 or GPT-2. But Markov chains demonstrate how we can apply mathematics to mimic results or at least achieve an mvp with a simpler approach. Another intriguing tool worth mentioning is the [nltk library](https://www.nltk.org/), which offers natural language capabilities.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

Eventually I will try the more sophisticated way using machine learning, but at least I am enjoying a quick taste of success with a Markov chain. Here's what some cherry-picked results look like! 😆 Ok, they're not great, but not too shabby either for my first time generating text from examples:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:image {"id":4695,"sizeSlug":"large","linkDestination":"none"} -->`{=html}

![](https://pythonmarketer.files.wordpress.com/2020/10/generating_positive_thoughts.jpg?w=1024){.wp-image-4695}

`<!-- /wp:image -->`{=html}

`<!-- wp:paragraph -->`{=html}

Maybe in the future I will use this for posts on my Facebook page, but it's not quite ready yet! I really enjoyed the process of researching this challenge and hope this post helps you evaluate your own text generation possibilities. This was fun to learn about. And best of all, I achieved satisfying, albeit primitive results within one weekend. Thanks for reading and stay positive.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:heading {"level":3} -->`{=html}

### Check out Markov chain in the wild [here](https://positivethoughts.pythonanywhere.com/). {#see-the-markov-chain-in-the-wild-at-positivipy-com}

`<!-- /wp:heading -->`{=html}
