Solving My Broken Google Authenticator App
##########################################
:date: 2025-02-20 13:45
:author: lofipython
:category: problem solving, authentication
:tags: two factor authorization, troubleshooting login
:slug: solving-my-broken-google-authenticator-app
:status: published

Being a programmer is not just about learning new libraries and skills. 
Some would say that identifying oneself as a "programmer" is foolish.
What we really are is problem solvers. We apply technology or logic to achieve a desired result.
This post details an interesting problem I encountered and how I reasoned to fix it.

I use Google Authenticator as my two factor authorization app. For many websites I use, 
this is a layer of security to verify it is actually me signing in.

I started using the app and went years with no problems. Recently, I encountered an issue signing 
into my 401K provider's website to check on my 401k. I logged in with my username and password,
then went to the authenticator app when prompted for a code.

But this time, after trying multiple times, I received the error "code invalid".
After so many failed attempts, most websites will lock you out of your account. 
This ended up happening to me. 

Frustrated, I called the provider's customer support. Eventually, I regained access to my account. 
"There's something bonked with my Authenticator app! The codes aren't working.", I told them.
They had no solutions, since the app is from Google and they are a financial services company.

I moved on from the debacle. A month or so later on a different website, this time 
a cryptocurrency exchange, I attempted to log in. Once again, the codes were invalid. 
I tried multiple times, but seeing it wouldn't work I stopped before a lock was placed on my account.

Since I was dealing with a Google product, I consulted Google Gemini AI model to seek guidance.

.. image:: {static}/images/asking-google-gemini-authenticator-issue.png
  :alt: asking Google Gemini for help with Google Authenticator

The solution to my problem was just as Gemini suggested: "Google Authenticator relies on precise time precision."
Although the specific solution Gemini offered was not correct, it sent me searching in the right direction.
Gemini told me there was a "time sync setting" in the Authenticator app that didn't exist. Gemini did mention that my phone 
should be on "network time".

Bingo. I opened up the time settings on my cellular phone. I had manually been setting my time zone due to traveling.
I opened up my phone and enabled my automatic time settings:

.. image:: {static}/images/android-time-settings.jpg
  :alt: enabling Android's automatic time settings

Success! My phone's time settings caused Google Authenticator to display the wrong codes. I logged into my account, 
making a mental note that my cell phone clock's settings can indeed cause my two factor authentication app to stop working.