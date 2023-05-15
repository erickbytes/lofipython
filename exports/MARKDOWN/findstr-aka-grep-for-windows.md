Title: Findstr, RegEx File Searches for Windows
Date: 2018-07-15 19:52
Author: pythonmarketer
Category: command prompt, data, python, Windows
Tags: programming, regex
Slug: findstr-aka-grep-for-windows
Status: published

Findstr is the Windows alternative to GREP, which runs on the [Unix operating system](https://www.howtogeek.com/182649/htg-explains-what-is-unix/). Findstr searches files with [regular expressions](https://en.wikipedia.org/wiki/Regular_expression) and seems useful for string matching within files and directories.  It is one of over [280 command prompt commands](https://www.lifewire.com/list-of-command-prompt-commands-4092302). Here's the official [Windows Documentation](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/findstr) and some [Linux vs. Windows Examples.](https://www.mkyong.com/linux/grep-for-windows-findstr-example/)

**Update:** Windows announced that [Grep and several other Unix command line tools will be added to Windows 10](https://hackaday.com/2019/06/10/windows-10-goes-to-shell/). This is a new alternative to findstr.

**This findstr command returns all lines containing an '@' in a text file.**

    findstr @ test.txt

![findstr Emails](https://pythonmarketer.files.wordpress.com/2018/07/findstr-emails.png){.alignnone .size-full .wp-image-1406 width="602" height="48"}

**I was happy to see Findstr's convenient help menu:**

    findstr -?

![findstr_help](https://pythonmarketer.files.wordpress.com/2018/07/findstr_help.png){.alignnone .size-full .wp-image-1408 width="657" height="603"}

Regular expressions are so powerful. It's nice to have this utility within the command prompt. I am hoping to get to know some of the other 280 command prompt commands.

**I've previously explored regex with Python. This Python regex example finds all words in a text file containing '@' symbols:**

    import re


    # read the file to string + regex email search
    with open('test.txt', 'r') as fhand:
        string = fhand.read()
        # this regex returns a python list of emails:
        emails = re.findall('(\S*@\S+)', string) 
        print(emails)

![findall_python](https://pythonmarketer.files.wordpress.com/2018/07/findall_python.png){.alignnone .size-full .wp-image-1405 width="633" height="173"}

For more command prompt nuggets, check out my more recent post: [Exploring Windows Command Line Tools, Batch Files and Remote Desktop Connection](https://pythonmarketer.wordpress.com/2020/05/06/exploring-windows-command-line-tools-batch-file-automation-and-remote-desktop-connection/).
