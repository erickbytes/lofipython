#########################################
 15 Cloudflare Pages Free Plan Features
#########################################

:date:
   2023-07-09 21:16

:author:
   lofipython

:category:
   coding, programming, blogging, web hosting

:tags:
   Cloudflare Pages blog, best Cloudflare website features, Cloudflare blog hosting features

:slug:
    15-Cloudflare-Pages-Free-Plan-Features

:status:
   published

Recently, this blog switched to `Cloudflare Pages <https://pages.cloudflare.com/>`__ after years of hosting on WordPress. I'm now using the free plan and enjoying the various settings that allow you control aspects of security at a level not found in WordPress. 

For example, you can activate the "bot fight mode", "browser integrity check" and "user agent blocking" settings to help you fend off bad actors.

.. image:: {static}/images/botfightmode.png
  :alt: enable bot fight mode

Enable bot fight mode.

.. image:: {static}/images/speedtest.png
  :alt: run a speed test on your blog

Run a speed test on your blog.

.. image:: {static}/images/crawlerhints.png
  :alt: enable crawler hints

Turn on search engine hints.

.. image:: {static}/images/topcrawlers.png
  :alt: see crawler traffic

See which search engines are crawling your blog.

**Here are my top Cloudflare Pages features:**

1. Zone analytics: the primary analytics to view unique visitors count, requests, bandwidth and network error logging
2. `crawler hints <https://developers.cloudflare.com/cache/advanced-configuration/crawler-hints/>`__: turn on hints to search engine crawlers and avoid wasteful compute
3. `bot fight mode <https://developers.cloudflare.com/support/firewall/learn-more/understanding-cloudflare-tor-support-and-onion-routing/#onion-routing>`__: enabling this mode will stop malicious bots
4. security center scan: validates your DNS configuration and tells you if anything needs fixed
5. run a speed test: test your site's speed 
6. enable IP geolocation: includes the country code for each blog visitor
7. GraphQL API: extensible analytics HTTP API
8. AMP real url: ask Google to show your site's actual url in AMP
9. notifications: set email alerts to monitor your website
10. security events log: monitor managed challenges and bots
11. `browser integrity check <https://developers.cloudflare.com/fundamentals/security/browser-integrity-check/>`__: looks for common http headers abused by spammers 
12. user agent blocking: blocks users with malicious user agent
13. `0-RTT Connection Resumption <https://blog.cloudflare.com/introducing-0-rtt>`__: enable "0-Round Trip Time", optimized DNS for your blog
14. DNS Analytics: see DNS traffic visualizations
15. `Onion Routing <https://developers.cloudflare.com/support/firewall/learn-more/understanding-cloudflare-tor-support-and-onion-routing/#onion-routing>`__: serve your website's content in a tor-friendly way

These are all included in the free plan. Some are enabled out of the box and others need to be toggled on to activate. I'm really digging my two Cloudflare Pages blogs. It's taken some time to get used to writing in `reStructuredText format <https://docutils.sourceforge.io/rst.html>`__. Using pelican for static site generation is working well. 

One quirk of Cloudflare is that only the past 30 days of data is stored. It's not as convenient as Wordpress, which stores the entire analytics history of a blog's traffic. However, Cloudflare's GraphQL API is also an option for your data querying needs. Regardless, I'm very impressed at the level of configuration Cloudflare exposes out of the box!