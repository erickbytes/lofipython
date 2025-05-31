Installing Debian 9 Stretch Linux OS on a Dell Inspiron Laptop and Configuring the Wifi Network
###############################################################################################
:date: 2019-04-25 14:14
:author: pythonmarketer
:category: Linux, software
:tags: computers, debian, operating system, os upgrade, Windows
:slug: installing-debian-9-stretch-linux-os-on-a-dell-inspiron-laptop-and-troubleshooting-wifi
:status: published

Yesterday, I converted an 11-year old Dell Inspiron E1505 from Windows XP to Debian 9 Stretch. 
I may have overwrote my Windows XP OS. I do not care if I lost it since it's a vulnerable 
and outdated OS, which is no longer supported by Microsoft. I encountered difficulty with 
getting the wifi to work on Debian, but was able to find a solution 
using `Wicd <https://help.ubuntu.com/community/WICD>`__. Here are the steps I followed to do it all.

Using The Debian Installer-Loader
---------------------------------

#. First, back up your Windows computer files. Then download the `Debian-Installer Loader <https://wiki.debian.org/DebianInstaller/Loader>`__ Windows executable from the Debian wiki.
#. Click the downloaded executable and |IMG_20190423_184816999|\ follow instructions. I followed the default settings all the way through.
#. You may need to choose your own partitioning settings to ensure Windows is preserved if desired.
#. During installation, choose your Linux collection. I chose Xfce because it `seems to be highest ranked <https://www.slant.co/versus/1122/1124/~xfce_vs_gnome-3>`__ among Linux users and "not just helpful for older computers where few system resources are available, but also simply for those who want to get the most out of their systems." Gnome and KDE are other popular options.

.. image:: http://pythonmarketer.files.wordpress.com/2019/04/46248-img_20190423_184023738-e1556211291659.jpg
   :alt: IMG_20190423_184023738
   :class: wp-image-1784 aligncenter
   :width: 564px
   :height: 375px

**After completing installation, restart your computer and select your new OS on boot-up. The following error codes displayed for me while starting up, signaling missing wifi firmware.**

::

   ERROR Failed to load firmware!
   b43ssb0:0: firmware: failed to load b43/ucode5.fw (-2)
   b43ssb0:0: firmware: failed to load b43-open/ucode5.fw (-2)
   b43-phy0 ERROR: You must go to https://wireless.wiki.kernel.org/en/users/drivers/b43#devicefirmware and download the correct firmware for this driver version.

*It took me a few boot-ups before I realized what this error message meant. In the rest of this post I am trying to figure out and fix what is wrong before I saw the error message. I enjoyed learning how to introspect Linux networks, but if I were trying to fix this problem again, I'd go to directly to *\ `this page <http://linuxwireless.sipsolutions.net/en/users/Drivers/b43/>`__\ *, which is linked to from the link in the error message, and try the solution there first.*

Post Installation Setup
-----------------------

**Open up the terminal once you're into your new Desktop OS** and enter the below commands.

::

   su - 
   apt-get install sudo -y usermod -aG sudo yourusername

**1) Enable yourself as root user.**

**2) Install sudo.**

**3) Give yourself sudo user permission.**

Optional: Replacing Network-Manager With Wicd
---------------------------------------------

This Debian 9 package ships with Network-Manager. After logging in, I wasn't sure why wifi was not working, so I decided to remove Network-Manager and install Wicd. (This was before I realized what the error code displayed on boot-up meant.) Wicd is a Linux network managing alternative and it's built with Python, by the way. I followed `these instructions <https://help.ubuntu.com/community/WICD>`__ to execute the below commands.

::

   uninstall nm
   sudo apt-get install -d --reinstall network-manager network-manager-gnome
   install wicd
   sudo apt-get install wicd-gtk

**After installing Wicd, my Ethernet connection was not working. This fixed it for me:**

::

   sudo ifconfig eth0 up

Troubleshooting Linux Wifi & Inspecting Your System
---------------------------------------------------

Now, let's check for enabled network interfaces. "wlan0" is usually the name of the wireless interface. Does wlan0 show when you enter this command? If not, then you may need to update your wifi firmware. This was the case for me. Below is an output where wlan0 is correctly configured.

::

   sudo ifconfig


::

    eth0: flags=4099<UP,BROADCAST,MULTICAST> mtu 1500
    ether 00:25:a5:cf:38:7d txqueuelen 1000 (Ethernet)
    RX packets 0 bytes 0 (0.0 B)
    RX errors 0 dropped 0 overruns 0 frame 0
    TX packets 0 bytes 0 (0.0 B)
    TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0
    device interrupt 17 
    lo: flags=73<UP,LOOPBACK,RUNNING> mtu 65536
    inet 127.0.0.1 netmask 255.0.0.0
    inet6 ::1 prefixlen 128 scopeid 0x10
    loop txqueuelen 1 (Local Loopback)
    RX packets 4 bytes 240 (240.0 B)
    RX errors 0 dropped 0 overruns 0 frame 0
    TX packets 4 bytes 240 (240.0 B)
    TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0
    wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500
    inet 191.142.1.297 netmask 255.255.255.0 broadcast 182.138.5.255
    inet6 2601:241:8c00:50ea:21a:92ff:fe0d:7531 prefixlen 64 scopeid 0x0
    inet6 fe80::22a:42tf:fe0d:7531 prefixlen 64 scopeid 0x20 ether 00:2a:92:2d:45:51 txqueuelen 1000 (Ethernet)
    RX packets 8509 bytes 4639778 (4.4 MiB)
    RX errors 0 dropped 0 overruns 0 frame 0
    TX packets 6206 bytes 923792 (902.1 KiB)
    TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0

**Check wlan0 is not blocked on kill list.**

::

   sudo rfkill list all

Some computers have a "kill switch" for wifi. This command lists any blocked interfaces. If it is blocked, `this thread <https://ubuntuforums.org/showthread.php?t=2298330>`__ might be useful. If nothing shows when you run this command, or if you see wlan0 is not blocked, carry on.

**Check which wifi controller you have.** `This thread <https://askubuntu.com/questions/55868/installing-broadcom-wireless-drivers>`__ **provides more info on what this means.**

::

   lspci -nn | grep -e 0200 -e 0280

::

   03:00.0 Ethernet controller [0200]: Broadcom Limited BCM4401-B0 100Base-TX [14e4:170c] (rev 02)
   0b:00.0 Network controller [0280]: Broadcom Limited BCM4311 802.11b/g WLAN [14e4:4311] (rev 01)

**Find your system architecture. This determines which firmware you should download in the next step.**

::

   sudo dpkg --print-architecture

**First,** `read here <https://wireless.wiki.kernel.org/en/users/drivers/b43/firmware>`__ **to determine the right packages for your Linux system. Then download the appropriate missing wifi firmware. For Debian, I downloaded the two packages below.**

1) `b43-fwcutter <https://packages.debian.org/stretch/b43-fwcutter>`__ 2) `b43-installer <https://packages.debian.org/stretch/firmware-b43-installer>`__

**"cd" into the directory with .deb files. Run the below commands to install the new firmware, then reboot your computer. The last two commands are adapted from** `this thread <https://ubuntuforums.org/showthread.php?t=2203312&page=4>`__.

::

   sudo dpkg -i firmware-b43-installer_019-3_all.deb
   sudo dpkg -i firmware-b43-fwcutter_019-3_i386.deb
   sudo modprobe -r b43
   sudo modprobe b43

**Edit Wicd preferences to set wlan0 as the wireless interface if needed.**

.. image:: https://pythonmarketer.files.wordpress.com/2019/04/change_wicd_settings.png
   :alt: change_wicd_settings
   :class: alignnone wp-image-1779
   :width: 380px
   :height: 357px

**Success! Wireless networks are now showing.**

.. image:: https://pythonmarketer.files.wordpress.com/2019/04/wicd_success.png
   :alt: wicd_success
   :class: alignnone wp-image-1780
   :width: 375px
   :height: 351px

**Wrapping Up**

I'd like to thank the awesome people who contributed to the Debian Installer-loader and all the help 
in Linux forums that enabled me figure this out. I'm new to the world of Linux but already enjoying 
diving into this operating system. Its ability to do just about anything from the command line are a 
lot of fun. I am now running two Linux systems, one on my Dell and another running Ubuntu that I 
installed on a Chromebook with `Crouton <https://www.howtogeek.com/162120/how-to-install-ubuntu-linux-on-your-chromebook-with-crouton/>`__. 
Both have been relatively painless to set up. It this case, it turned a sluggish laptop into a 
very capable machine. They should call it Lit-nux :)

**Full Disclosure**

This worked on my computer for a few days before the keyboard stopped working correctly on my computer. 
Typing became impossible because the keys didn't work or entered the wrong letters when pressed. 
I'm not sure what the cause of it was, but consider that before attempting this on a machine. 
Be prepared to lose it. If you really need the machine to be functional, it may not be a great idea to try this. 
This was attempted on an old beat up computer. I would try this method of porting a Windows machine to Linux 
again as a salvage project or on a low-risk Windows machine if I had one lying around.

.. |IMG_20190423_184816999| image:: http://pythonmarketer.files.wordpress.com/2019/04/97878-img_20190423_184816999-e1556211269262.jpg
   :class: wp-image-1785 alignright
   :width: 311px
   :height: 196px
