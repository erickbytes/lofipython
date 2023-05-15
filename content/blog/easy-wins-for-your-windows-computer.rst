Easy Tune-ups For Your Windows Computer
#######################################
:date: 2020-03-22 22:59
:author: pythonmarketer
:category: performance, Windows
:tags: maintenance, operating system, windows update
:slug: easy-wins-for-your-windows-computer
:status: published

This post covers 6 handy Windows tools:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Windows Experience Index
#. Disk Cleanup
#. Windows Update Troubleshooter
#. Windows Update
#. Microsoft Support and Recovery Assistant
#. Disk Defragmenter

**First, get your baseline Windows Experience Index score.**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These metrics are a way to monitor your system's performance over time.

#. Go to "Control Panel\System and Security\System"
#. Select "Your Windows Experience Index needs to be refreshed."
#. Note the metrics you see and the last updated date. If you've never refreshed them, these are likely your computer's factory scores.
#. Then click "Refresh Now" and note the results. These are your computer's current scores.

.. image:: http://pythonmarketer.files.wordpress.com/2020/03/f6e0a-check_windows_experience_index-e1584936945758.jpg
   :alt: check_Windows_Experience_Index
   :class: alignnone size-full wp-image-2780
   :width: 729px
   :height: 501px

--------------

**Run Disk Cleanup**
~~~~~~~~~~~~~~~~~~~~

The name says it all. Go to the Start menu and search 'Disk Cleanup'. Running this freed up 40 GB of C: drive space for me.

disk_cleanup

--------------

**Install OS patches and software updates withWindows Update.**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**First, troubleshoot Windows Update to fix any errors.**

.. image:: http://pythonmarketer.files.wordpress.com/2020/03/83836-tdhotingtrpot2-e1584941263675.jpg
   :alt: tdhotingtrpot2
   :class: wp-image-2790 alignright
   :width: 357px
   :height: 274px

The `Windows Update Troubleshooter <https://support.microsoft.com/en-us/help/4027322/windows-update-troubleshooter>`__\ is supported by Windows and may help with updates that fail. I downloaded the troubleshooter forWindows Update and BITS, Windows'\ `Background Intelligence Transfer System. <https://docs.microsoft.com/en-us/windows/win32/bits/background-intelligent-transfer-service-portal>`__

The troubleshooter analyzes Windows Update and tries to fix the errors it finds. After running, it provides a status update on the issues it finds.

**Run Windows Update to upgrade your software.**

Windows Update usually updates your software reliably. However, some updates may fail or are not triggered automatically. Installing updates, especially security patches for your operating system is typically a good idea.In my case, several Windows 7 OS security patches had not auto-updated, some from 6 months ago.

check_updates

-  Go to your start menu and search for 'Windows Update'.
-  I clicked 'Check online for updates from Windows Update' also.
-  When you restart your computer, use a power cord for your laptop.
-  I found more new updates twice after installing new updates and restarting my system.  Some updates are required before another update may be installed.

windowsuptodate

 

 

--------------

Microsoft Support and Recovery Assistant
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Got Microsoft Errors?** Check out the `Microsoft Support and Recovery Assistant <https://support.office.com/en-us/article/about-the-microsoft-support-and-recovery-assistant-e90bb691-c2a7-4697-a94f-88836856c72f>`__. It may help you if you're having trouble with Microsoft Office, Skype or any other Windows tools.

.. image:: http://pythonmarketer.files.wordpress.com/2020/03/1ea73-options_recovery-e1587747001750.jpg
   :alt: options_recovery
   :class: wp-image-3225 alignnone
   :width: 465px
   :height: 350px

--------------

**Finally, defragment your C: drive.**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Defragmentation is like spring cleaning for your computer's hard disk. It optimizes your drive's data for more efficient computing and frees up space for other activities.

#. Go to your start menu and search for 'Disk Defragmenter'.
#. Click 'Analyze disk' to check your C: Drive's fragmented rate.
#. If the fragmented rate is above 10%, `Windows recommends <https://support.microsoft.com/en-us/help/17126/windows-7-improve-performance-defragmenting-hard-disk>`__ to defragment your C: Drive. As you can see below, mine had a whopping 48% fragmentation rate. 😨 My poor computer had never been defragged in 2.5 years of use.

.. image:: http://pythonmarketer.files.wordpress.com/2020/03/699fd-defragment_results-e1585007505765.jpg
   :alt: defragment_results
   :class: alignnone size-full wp-image-2740
   :width: 658px
   :height: 529px

**46% Less Fragmented Disk Space After Two Defrags**

Running the defragmenter once reduced my drive's fragmentation from 48% to 32%. Re-running the defragmenter dropped my C: drive to a 2% fragmented rate. That's more like it. 🤓

   .. container:: ng-scope

      Fragmentation makes your hard disk do extra work that can slow down your computer. Removable storage devices such as USB flash drives can also become fragmented. Disk Defragmenter in Windows rearranges fragmented data so your disks and drives can work more efficiently.

   .. container::

      Source: `Ways to Improve Your Computer's Performance <https://support.microsoft.com/en-us/help/17126/windows-7-improve-performance-defragmenting-hard-disk>`__

--------------

**My Windows 7 System Improvement Results**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Raised Windows Experience Index base sub-score from 4.9 to 5.0/7.9.
-  Added 40 GB of hard drive space thanks to Disk Cleanup.
-  Patched operating system security vulnerabilities and all software is up to date.
-  Fixed any misbehaving Windows products.
-  Decreased fragmented drive space from 48% to 2%. Windows recommends keeping it under 10%.

On paper, that looks great. Hopefully it means less spinning lag wheels and programs not responding when you really shoulda saved that document...  `We'll see <https://www.youtube.com/watch?v=e2cjVhUrmII>`__.
