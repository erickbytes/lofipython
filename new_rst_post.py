from datetime import datetime
from shutil import copy


def post_title():
    """Ask for the new post's name."""
    title = input("Enter the new post's title:\n")
    slug = title.replace(" ", "-").lower()
    return title, slug


def copy_template(slug):
    """Copy a reStructuredText template file for a new post."""
    content = "/home/erick/Desktop/Projects/lofipython/content"
    rst = f"{content}/blog/drafts/template.rst"
    dst = f"{content}/blog/{slug}.rst"
    try:
        copy(rst, dst)
    except FileNotFoundError:
        content = "/home/erickbytes/lofipython/content/"
        rst = f"{content}/blog/drafts/template.rst"
        dst = f"{content}/blog/{slug}.rst"
        copy(rst, dst)
    return dst


def read_rst(rst):
    with open(rst, "r") as file_handle:
        text = file_handle.read()
    return text


def edit_text(text, title):
    today = datetime.now().strftime("%Y-%d-%m %H:%M")
    old_slug = "delete-all-your-tweets-with-tweepy-and-the-twitter-api"
    old_title = "Delete All Your Tweets with Tweepy and the Twitter API"
    text = (
        text.replace("2020-09-13 21:07", today)
        .replace(old_slug, slug)
        .replace(old_title, title)
    )
    return text


def save_rst(rst, text):
    with open(rst, "w") as file_handle:
        file_handle.write(text)
    return None


title, slug = post_title()
rst = copy_template(slug)
text = read_rst(rst)
text = edit_text(text,title)
save_rst(rst, text)
