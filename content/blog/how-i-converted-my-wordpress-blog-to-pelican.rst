How I Converted My Wordpress Blog to Pelican, A Checklist
#########################################################
:date: 2024-10-17 16:42
:author: lofipython
:category: coding, programming, python, wordpress, blog
:tags: moving from Wordpress to Pelican, Wordpress migration checklist
:slug: how-i-converted-my-wordpress-blog-to-pelican
:status: published

Recently there has been a lot of noise online about the Wordpress website platform. 
This blog is formerly a Wordpress blog, so I am in the unique position to share how 
I moved this blog for anyone looking to get off Wordpress. I wrote an announcement post about 
`migrating my wordpress blog in 2023 <https://lofipython.com/wordpress-to-pelican-blog-migration-complete>`__.
This blog began as on the Wordpress free plan, then had few years as a paying customer of Automattic, 
the corporate entity associated with Wordpress.org. The notes below are from my experience moving to a Python Pelican blog.

Here is the checklist I wrote down when I made than transition:

1. Export posts to XML.

2. Export all media.

3. Convert posts to new blog format: Markdown or Restructured Text Edits.

4. Set DNS redirect from old blog to new blog.

5. Turn off search engine indexing for old blog.

6. Update old blog with notice of new blog. 

7. Update urls from old domain to new domain.

---------------------

**1. Export posts to XML.**

Go into the Wordpress settings and export posts. I selected XML format.

.. image:: {static}/images/wordpress-export-tools.png
  :alt: export blog from wordpress settings

**2. Export all media.**

Wordpress allowed me to choose to export posts or media, so I exported all the images on my blog also.

.. image:: {static}/images/wordpress-export-tool-options.png
  :alt: export blog from content and media from  wordpress settings


.. image:: {static}/images/wordpress-export-tool-options-details.png
  :alt: export blog from content and media from  wordpress settings

**3. Convert posts to new blog format: Markdown or Restructured Text Edits.**

Pelican's import tool for wordpress converts your XML file to either .md or .rst files 
based on which CLI argument you pass.

**4. Set DNS redirect from old blog to new blog.**

I previously hosted my blog on a custom .com domain. When I stopped paying for the domain,
my domain reverted back to example.wordpress.com. However, you can pay a domain register a small 
fee to forward traffic to your new domain. You can transfer old domain to services like Namecheap 
or Cloudflare to set up a redirect. It's recommended to keep a redirect for at least 1 or 2 years 
after moving to a new domain to catch any legacy backlinked traffic.

**5. Turn off search engine indexing for old blog.**

One benefit of Wordpress from an SEO perspective is that they have search engine indexing control in the settings panel.
In the settings, you have the ability to tell search engines whether or not you should index your blog.
Once I got the hang of Pelican, I reviewed each converted post to fix links, grammar or 
formatting errors from the conversion. 

I slowly moved them over in batches of 2 or 3 posts at a time. As I moved the posts to the new blog, 
I set the old posts to private within the Wordpress CMS. I also changed their search engine indexing 
settings to "Discourage search engines from indexing this site" and  "Prevent third-party sharing for example.wordpress.com". 
This allows people who might be searching for my old blog or following legacy links to have a chance 
to track down the few posts available and hopefully find my new home on the web.

**6. Update old blog with notice of new blog.**

*Keep A Few Posts Exclusively on the Old Blog*

The benefit of Worpdress's free plan is that you can still keep some posts 
and the original sub-domain live on their free plan. You can write your final post 
on the old blog to let subscribers know you've moved.

*Update the Site Tagline on Your Old Blog*

I also set the old blog tagline, pointing readers to new blog:

In Settings / General, you can edit the site tagline:

.. image:: {static}/images/update-wordpress-site-tagline.png
  :alt: change blog headline in wordpress


.. image:: {static}/images/blog-headline-announcement.png
  :alt: blog moved announcement

**7. Update urls from old domain to new domain.**

It's common practice to add a "CTA" or call to action at the end of a blog post. For me, that tends to be the related posts I've
written in the past. Any links that contain the old domain need to be swapped to the new one.

For validating urls in my 100+ past posts, I also wrote a python script to help find broken links and .rst tags here: 
`rst-url-validator Github Repo <https://github.com/erickbytes/rst-url-validator>`__

**Install the Pelican, lxml, beautiful soup and feedparser Python libraries.**

.. code:: console

   pip install pelican
   pip install BeautifulSoup4
   pip install lxml
   pip install feedparser


**Use the pelican-importer CLI to convert the XML to Markdown or reStructuredText.**

I chose to use the default detting of the CLI to export to .rst. If you want to specify a folder to drop the contents, 
use the -o argument. Use the -m argument to specify which output format.

.. code-block:: console

   # Convert CML to reStructuredText Format files.
   pelican-import --wpfile pymarketer.wordpress.2023-05-14.000.xml
   # Convert XML to Markdown files.
   pelican-import --wpfile pymarketer.wordpress.2023-05-14.000.xml -o ~/projects/example.com/content/blog -m MARKDOWN

`pelican-importer documentation <https://docs.getpelican.com/en/stable/importer.html>`__

**Moving From Wordpress Was Easy With Pelican**

I did thorough `research into Python static site generators <https://lofipython.com/a-brief-summary-of-promising-python-static-site-generators>`__
before choosing Pelican. The benefits of Pelican include a 
wordpress import CLI that makes it easy to quickly compile an an alternative MVP to move your blog from Wordpress.
Pelican is an obvious choice for static site generation in the Python ecosystem. After 17 months of using it, 
I can safely say I'm happy with the decision!

**Supplementary Reading**

`Deploy a Hugo website to Cloudflare <https://tanis.codes/posts/deploy-hugo-website-to-cloudflare/?utm_source=pocket_shared>`__

`How to Convert a Wordpress blog to an Astro Static Site <https://blog.okturtles.org/2024/10/convert-wordpress-to-static-site/>`__

`Pelican Documentation <https://docs.getpelican.com/en/latest/>`__

`Launching a Live Static Site Blog via Pelican, Github and Cloudflare Pages <hhttps://lofipython.com/launching-a-live-static-blog-via-pelican-github-and-cloudflare-pages>`__

