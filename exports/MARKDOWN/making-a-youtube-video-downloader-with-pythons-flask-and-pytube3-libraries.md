Title: Making A YouTube Video Downloader With Python's Flask and pytube3 Libraries
Date: 2020-10-07 23:49
Author: pythonmarketer
Category: coding, flask, programming, python, web development
Tags: curiosity, hacking, prototyping, videos
Slug: making-a-youtube-video-downloader-with-pythons-flask-and-pytube3-libraries
Status: published

`<!-- wp:paragraph -->`{=html}

How do you download YouTube videos? The easiest answer is to google sites like [y2mate](https://y2mate.guru/en8/) that work for downloading videos. But then I thought, I wonder if I can make something?

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

Boredom, my curiosity and some googling turned up the [pytube3 library](https://github.com/get-pytube/pytube3), "A lightweight, dependency-free Python 3 library (and command-line utility) for downloading YouTube Videos." Lo and behold, 3 hours of experimentation later, I made a video downloader with Python. 😃

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

I used pytube3 with [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [pythonanywhere](https://www.pythonanywhere.com/) to accomplish the task. I was pleasantly surprised at how it came together and simply worked! I'm really not that familiar with Flask either. Here's how to make a primitive YouTube video downloader.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Install the pytube library in the pythonanywhere bash console with [pip](https://pythonmarketer.wordpress.com/2018/01/20/how-to-python-pip-install-new-libraries/)**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

`pip3.8 install --user pytube3 --upgrade`

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**If you're not using pythonanywhere, install Flask (it's already included in pythonanywhere)**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

`python -m pip install flask`

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:syntaxhighlighter/code -->`{=html}

``` wp-block-syntaxhighlighter-code
import logging
import sys
from pytube import YouTube
from flask import Flask, request, send_file

"""
Flask YouTube Video Downloader - Python Marketer
https://pythonmarketer.com/2020/10/07/making-a-youtube-video-downloader-with-pythons-flask-and-pytube3-libraries/
"""
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
app = Flask(__name__)

@app.route("/")
def youtube_downloader():
    """Render HTML form to accept YouTube URL."""
    html_page = f"""<html><head>
                    <Title>YouTube Downloader</Title></head>
                    <body><h2>Enter URL to download YouTube Vids!</h2>
                    <div class="form">
                    <form action="/download_video" method="post">
                    <input type="text" name="URL">
                    <input type="submit" value="Submit">
                    </form></div><br><br>
                    </body></html>"""
    return html_page

@app.route("/download_video", methods=["GET","POST"])
def download_video():
    """
    First pytube downloads the file locally in pythonanywhere:
    /home/your_username/video_name.mp4

    Then use Flask's send_file() to download the video 
    to the user's Downloads folder. 
    """
    try:
        youtube_url = request.form["URL"]
        download_path = YouTube(youtube_url).streams[0].download()
        fname = download_path.split("//")[-1]
        return send_file(fname, as_attachment=True)
    except:
        logging.exception("Failed download")
        return "Video download failed!"
```

`<!-- /wp:syntaxhighlighter/code -->`{=html}

`<!-- wp:image {"id":7185,"sizeSlug":"large","linkDestination":"none"} -->`{=html}

![](https://pythonmarketer.files.wordpress.com/2022/09/download.png?w=952){.wp-image-7185}

`<!-- /wp:image -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Minimum Viable Prototype Achieved**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

This is more of a proof of concept than workable solution. It works for many videos I tried. It occasionally had trouble downloading certain videos. I tested it successfully on videos of up to 10 minutes. Maybe it works more consistently if the file size is smaller? Or there is a bug on certain types of videos? For me, some videos of only a few minutes failed, so your results may vary. The videos that failed returned errors like `KeyError: 'cipher'` and `KeyError: 'url'`.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Honorable Mentions**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[youtube-dl](https://github.com/ytdl-org/youtube-dl/blob/master/README.md#installation): Command-line program to download videos from YouTube.com and other video sites

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[YoutubeDownload](https://github.com/YouTubeDownload/YouTubeDownload): GUI and CLI for downloading YouTube video/audio

`<!-- /wp:paragraph -->`{=html}
