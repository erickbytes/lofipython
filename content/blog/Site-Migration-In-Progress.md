Title: Wordpress to Pelican Blog Migration In Progress 
Date: 2023-05-15 17:45
Category: Meta

This blog is formerly known as "Python Marketer" from 2016 to 2023. In May 2023, I've begun the migration from Wordpress's "Personal" plan to a free Pelican static site. Currently, about half of the posts are now hosted exclusively on lofipython.com. 

I will be posting here in the future and moving the rest of the posts over one at a time because the Wordpress syntax highlighter html could not be read by Pelican's importer for code samples. I saw the error "invalid Pygments lexer class" for some parts of Wordpress's HTML when converting to RST. The posts that did convert with the importer were the ones that didn't have any code or used the "preformatted" HTML tag to show the code.

**The Next Chapter: Lo-Fi Python**

A Python static site blog generated with the Pelican Python library and hosted with Cloudflare Pages.

> Lo-fi (also typeset as lofi or low-fi; short for low fidelity) is a music or production quality in which elements usually regarded as imperfections in the context of a recording or performance are present, sometimes as a deliberate choice. *Wikipedia*

The content folder contains all of the posts in reStructured Text format. The "exports" folder also contains the Wordpress importer script I used to convert the posts from my Wordpress blog, PythonMarketer.com. That blog is currently being migrated to LofiPython.com. I will be posting new stuff there in the future.

**The Spirit of Low Fidelity**

Lo-Fi Python aims to find the "lo-fi" spirit of Python.
Doing more with less. Favoring the standard library. Lowest possible time to MVP (minimum viable product).
Learning new libraries. Exploring the ecosystem with playful curiosity.
Embrace helping others by helping yourself. This is the way.