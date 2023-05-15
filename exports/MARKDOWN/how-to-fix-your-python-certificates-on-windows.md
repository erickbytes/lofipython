Title: Python Requests SSLCertVerificationError Solution for Windows
Date: 2021-06-10 11:59
Author: pythonmarketer
Category: coding, HTTP, python, Windows
Tags: .PEM solution, problem solving, Windows 10
Slug: how-to-fix-your-python-certificates-on-windows
Status: published

`<!-- wp:paragraph -->`{=html}

I initially installed my Python version from the [Windows Store](https://www.microsoft.com/en-us/p/python-39/9p7qfqmjrfp7) and it worked fine for almost a year on my Windows 10 computer. Then I started getting this error message when trying to use the [requests library](https://docs.python-requests.org/en/master/user/advanced/#ssl-cert-verification) on all HTTP requests:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:preformatted -->`{=html}

``` wp-block-preformatted
requests.exceptions.SSLError: HTTPSConnectionPool(host='api.example.com', port=443): Max retries exceeded with url: /oauth/token?grant_type=client_credentials (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1131)')))
```

`<!-- /wp:preformatted -->`{=html}

`<!-- wp:paragraph -->`{=html}

Apparently my Python certificates were not valid or up to date on my computer. These are ".PEM" or ".cert" files that certify your connection for the [SSL protocol](https://www.ssl.com/faqs/faq-what-is-ssl/). I googled this error until I found the [python-certifi-win32](https://pypi.org/project/python-certifi-win32/) library. I only needed to [pip install](https://pythonmarketer.wordpress.com/2018/01/20/how-to-python-pip-install-new-libraries/) this library and it fixed the problem:

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

`pip install python-certifi-win32`

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

Huge thank you to [the maintainer](https://pypi.org/user/andrewleech/) of this package. It solved my issues and now I can make HTTP requests again!

`<!-- /wp:paragraph -->`{=html}
