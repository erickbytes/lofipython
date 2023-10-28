Streamline Sharing Your Wi-Fi Network Details With Python
#########################################################
:date: 2023-10-27 19:33
:author: lofipython
:category: coding, programming, python, QR code, Wi-Fi
:tags: making a wi-fi QR code, how to create a QR code for internet password
:slug: how-to-make-a-wi-fi-qr-code-with-python
:status: published

If you host a public space or office with shared Wi-Fi, a QR code skips the tedious process of
exchanging your network's details. This is nice to have as an alternative to asking
people to manually enter an auto-generated, cryptic, error-prone 16 character string password.
Especially when you frequently have customers or new people asking for the information.
You could post a sign with the network name and password like most coffee shops do,
or you could try a QR code. Here's how to create a QR code for your Wi-Fi network.

To accomplish this task, I found the `wifi-qr-code-generator library on pypi <https://pypi.org/project/wifi-qrcode-generator/>`__.
It makes creating a Wi-Fi QR code very simple with help from the `pillow <https://pypi.org/project/Pillow/>`__ and `qrcode <https://pypi.org/project/qrcode/>`__ modules.
It is a great example of a library that has a very specific purpose and does it well.
The connection will only be automatic is your password is correct, so make sure you type it carefully.

The library has two ways to create a QR code:

#. Run a Python script to with the network details.

#. Use wifi-qr-code-generator's CLI.


**Install wifi-qrcode-generator**

.. code:: console

   pip install wifi-qrcode-generator


**Generating a QR Code Python Script**

This code snippet prints the qr code to the terminal screen, then saves it as a png image.

.. code-block:: python

  #!/usr/bin/env python3
  import wifi_qrcode_generator.generator

  qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
      ssid="add_wi-fi_network_name",
      hidden=False,
      authentication_type="WPA",
      password="add_wi-fi_password",
  )
  qr_code.print_ascii()
  qr_code.make_image().save("wifi-qr-code.png")


**QR Code Example Image**

.. image:: {static}/images/wifi-qr.png
  :alt: QR code image result

**Wi-Fi Auto-Connected Confirmation**

.. image:: {static}/images/connected-qr-notice.png
  :alt: confirmation of wi-fi connection

**Generating a QR Code With CLI Command**

The 2nd way to use this module is via a built-in command line interface to make your QR code.
It can be invoked with this command:

.. code:: console

  wifi-qrcode-generator


**Small Projects for the Win**

I like little projects like this. Some of my favorite coding happens when I
start with a simple goal, research the libraries available, apply Python skills
and get a tangible result in a short period of time. If you want to streamline
sharing your Wi-Fi network, remember this practical Python library!
