import os
from datetime import datetime
from shutil import copy


def post_title():
    """Ask for the new post's title and create slug."""
    title = input("Enter the new post's title:\n")
    slug = title.replace(" ", "-").lower()
    return title, slug


def copy_template(slug):
    """Copy a reStructuredText template file for a new post."""
    content = f"{os.getcwd()}/content"
    rst = f"{content}/blog/drafts/template.rst"
    dst = f"{content}/blog/{slug}.rst"
    copy(rst, dst)
    return dst


def read_rst(rst):
    """Returns string, text of .rst file."""
    with open(rst, "r") as file_handle:
        text = file_handle.read()
    return text


def edit_text(text, title, slug):
    """Set date to current time, add new slug and title."""
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    old_slug = "delete-all-your-tweets-with-tweepy-and-the-twitter-api"
    old_title = "Delete All Your Tweets with Tweepy and the Twitter API"
    text = (
        text.replace("2020-09-13 21:07", today)
        .replace(old_slug, slug)
        .replace(old_title, title)
    )
    return text


def save_rst(rst, text):
    """Save new .rst file with updated text."""
    with open(rst, "w") as file_handle:
        file_handle.write(text)
    return None


title, slug = post_title()
rst = copy_template(slug)
text = read_rst(rst)
text = edit_text(text, title, slug)
save_rst(rst, text)
