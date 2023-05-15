Title: "Shutdown" a Windows Computer by Double-clicking a Batch File
Date: 2023-02-21 18:28
Author: pythonmarketer
Category: automation, coding, Windows
Tags: windows automation, windows batch files
Slug: shutdown-windows-in-a-batch-file
Status: published

`<!-- wp:paragraph -->`{=html}

Here is a quick and easy way to automate turning off your computer. This saves me about 15 seconds to manually click the start menu and restart buttons. It worked for me on an old, laggy HP computer running the Windows 10 operating system. Now, I can double-click a batch file on my Desktop and walk away while it struggles.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

Batch files are executable via:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:list -->`{=html}

-   double-clicking them
-   right-clicking and selecting "Run"
-   entering the batch file name in command prompt, ex: "shut down CPU.bat" if the current working directory is in the same folder as the batch file

`<!-- /wp:list -->`{=html}

`<!-- wp:paragraph -->`{=html}

Open a blank Notepad document and save as **shut down CPU.bat** with this text:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
cmd /c shutdown -s
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:image {"id":7432,"sizeSlug":"large"} -->`{=html}

![Source: [Microsoft shutdown documentation](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown)](https://pythonmarketer.files.wordpress.com/2023/02/screenshot_20230221-225405-494.png?w=681){.wp-image-7432}

`<!-- /wp:image -->`{=html}

`<!-- wp:paragraph -->`{=html}

When this batch file runs, it will trigger a pop-up window warning that your computer is about to shut down. For my slow, slogging computer it shut off about 20 seconds later. This may also trigger queued automatic updates to install, which happened when I used the above command.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:image {"id":7423,"sizeSlug":"large"} -->`{=html}

![[Source: Stack Overflow](https://stackoverflow.com/questions/162304/how-do-i-shutdown-restart-or-log-off-windows-via-a-bat-file)](https://pythonmarketer.files.wordpress.com/2023/02/image_editor_output_image1037058739-1677025419090.png?w=687){.wp-image-7423}

`<!-- /wp:image -->`{=html}
