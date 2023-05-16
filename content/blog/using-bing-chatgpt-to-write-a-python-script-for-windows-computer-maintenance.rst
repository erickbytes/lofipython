Using Bing + GPT-4 to Write a Python Script for Windows Computer Maintenance
############################################################################
:date: 2023-02-26 22:05
:author: pythonmarketer
:category: automation, coding, command prompt, performance, productivity, programming, python, Scripts, software
:tags: AI chat, Bing ChatGPT Review, Python code Bing and ChatGPT, Windows 10 Command Line, Windows Maintenance
:slug: using-bing-chatgpt-to-write-a-python-script-for-windows-computer-maintenance
:status: published

Today, I was granted access to Bing's large language model, the next generation GPT-4. Bing's chat is the "more powerful" successor to `OpenAI <https://openai.com/>`__'s groundbreaking chat service that's generating heaps of hype in addition to its AI text generation abilities. I gained the new chat functionality a few weeks after joining the Bing waitlist.

.. figure:: https://pythonmarketer.files.wordpress.com/2023/02/screenshot_20230301-225703-397.png?w=704
   :alt: 
   :figclass: wp-image-7521

A guilty pleasure of mine is fixing up old Windows machines by installing updates and running command prompt tools like SFC and chkdsk. There's also GUI based tools like disk cleanup and the disk defragmenter.

My HP computer on Windows 10 is running slow and steady. It's an old model, so I want to improve performance wherever possible and hopefully speed it up. Enter Bing. It did what I wanted and more, but I needed to rephrase my first question to get better results.

First, I asked how to improve performance on a Windows computer. Bing offered generic windows maintenance tips, then followed up to ask my operating system version, which is Windows 10. When I informed Bing it offered more targeted advice after I rephrased my question to focus on command line commands.

.. figure:: https://pythonmarketer.files.wordpress.com/2023/02/image_editor_output_image-214678727-1677463333126.png?w=618
   :alt: 
   :figclass: wp-image-7473

.. figure:: https://pythonmarketer.files.wordpress.com/2023/02/image_editor_output_image845498026-1677473969816.png?w=884
   :alt: 
   :figclass: wp-image-7500

I then asked a new question in a fresh chat session. This time I included my OS and asked more specifically for Windows command prompt commands for improving performance. Bing listed a few options and gave a little context of what they do. Then I was presented options to show how to use powercfg or msconfig.

.. figure:: https://pythonmarketer.files.wordpress.com/2023/02/image_editor_output_image1028440375-1677466609760.png?w=588
   :alt: 
   :figclass: wp-image-7480

.. raw:: html

   </figure>

**How to use powercfg according to Bing:**

.. figure:: https://pythonmarketer.files.wordpress.com/2023/02/image_editor_output_image885862200-1677466557121.png?w=584
   :alt: 
   :figclass: wp-image-7479

.. raw:: html

   </figure>

Bing chat helped me find and remember the **SFC /scannow** command. It caches copies of files, fixes corrupted files and may speed up your machine.

You can even prompt Bing for detailed examples of how to use specific windows commands. To get this kind of result from a search engine is incredible. It's like Bing is your own personal tutor. As someone who is constantly googling how to do computer and programming related things, this feels impressive. This was my first time using this service and it has raised the bar for searching the web. I then prompted Bing for a Python script capable of running the SFC command and had my first "wow" moment.

.. figure:: https://pythonmarketer.files.wordpress.com/2023/02/image_editor_output_image885068823-1677461283407.png?w=559
   :alt: 
   :figclass: wp-image-7467

.. figure:: https://pythonmarketer.files.wordpress.com/2023/02/image_editor_output_image774027644-1677461889456.png?w=849
   :alt: 
   :figclass: wp-image-7468

Then it asks if I want the Python code explained. I'm so chuffed at this point. It tapped the `subprocess module <https://docs.python.org/3/library/subprocess.html>`__ to write the script and capture its output. Simply stunning.

SFC requires an administrator command prompt. You can start an admin command prompt from the start menu. I ran "python run_sfc.py" containing the below script on version Python 3.11. The command finished running approximately 20 minutes later. Additionally, if you get the error 'utf-8' bytes can't be decoded, you'll need to pass an encoding argument to decode(). Ok, here's **the Python script**:

.. code-block:: python

   # Import the subprocess module
   import subprocess

   # Define the SFC command as a list of arguments
   sfc_command = ["sfc", "/scannow"]

   # Run the SFC command using subprocess.run and capture the output
   sfc_output = subprocess.run(sfc_command, capture_output=True)

   # Print the output of the SFC command
   print(sfc_output.stdout.decode())

.. figure:: https://pythonmarketer.files.wordpress.com/2023/02/image_editor_output_image63547969-1677469517174.png?w=911
   :alt: 
   :figclass: wp-image-7493

.. figure:: https://pythonmarketer.files.wordpress.com/2023/02/image_editor_output_image-324660109-1677469443109.png?w=527
   :alt: 
   :figclass: wp-image-7491

.. figure:: https://pythonmarketer.files.wordpress.com/2023/02/wp-1677631583420.png
   :alt: an 
   :figclass: wp-image-7517

If your text is using a non-English character encoding, I found you may need to pass a different encoding besides the default utf-8. For example, I found this to work if your command prompt characters are in Spanish:

.. code-block:: python

   # en español
   print(sfc_output.stdout.decode(encoding="latin-1"))

.. figure:: https://pythonmarketer.files.wordpress.com/2023/02/image_editor_output_image1620635696-1677463544366.png?w=632
   :alt: 
   :figclass: wp-image-7475

You could also use a Windows batch file of course:

.. figure:: https://pythonmarketer.files.wordpress.com/2023/02/screenshot_20230301-231228-130.png?w=494
   :alt: 
   :figclass: wp-image-7524
