from shutil import copy


def post_name():
    """Ask for the new post's name."""
    name = input("Enter the new post's title:\n").replace(" ", "-").lower()
    return name


def copy_template(name):
    """Copy a reStructuredText template file for a new post."""
    # content = "/home/erickbytes/lofipython/content/"
    content = "/home/erick/Desktop/Projects/lofipython/content"
    rst = f"{content}/blog/drafts/template.rst"
    dst = f"{content}/blog/{name}.rst"
    copy(rst, dst)
    return None


name = post_name()
copy_template(name)
