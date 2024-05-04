How to Share a Google Calendar Event URL
########################################
:date: 2024-05-01 16:14
:author: lofipython
:category: coding, programming, python, urls, automation
:tags: Google Calendar URL API example, sharing a Google Calendar event, create google calendar event with python
:slug: how-to-share-a-google-calendar-event-url
:status: published


You can easily share a Google Calendar event if you know the url syntax Google uses.
When the url is opened in a browser, it prompts the person you want to share an event 
with to save it to their calendar.


**Demonstrating Google Calendar URL Arguments in Python**

By simply knowing the proper url arguments, you can enable people to quickly save a Google Calendar event.
This example uses the Python standard library: urllib to format the Google calendar url parameters and webbrowser 
to open the url in a browser. This is a handy little trick to keep in your back pocket!


.. code-block:: python

   from urllib.parse import urlencode
   import webbrowser

   def new_google_calendar_event():
      """
      Pass an event to Google Calendar with url arguments.

      Base URL: https://calendar.google.com/calendar/render

      URL Arguments:

      action: TEMPLATE
      text: Event Title
      dates: start_datetime/end_datetime
      details: event description or link to more info
      location: url to webcast, call or physical location name
      ctz: set the time zone by name, ex: America/New_York 
      recur: set a recurring event, ex: RRULE:FREQ%3DWEEKLY;INTERVAL%3D3
      crm: if Free, Busy, or Out of Office, ex: AVAILABLE, BUSY or BLOCKING
      add: add a list of guests by email, ex: elf1@example.com,elf2@example.com
      """
      parameters = {
         "action": "TEMPLATE",
         "text": "Title of Event",
         "dates": "20240504T123000Z/20240504T133000Z",
         "details": "Event Details: https://lofipython.com",
         "location": "link to webcast, call or physical location",
         "ctz": "America/Chicago",
         "crm": "BUSY"
      }
      # Returns str of URL encoded parameters.
      url_parameters = urlencode(parameters)
      url = f"https://calendar.google.com/calendar/render?{url_parameters}"
      print(url)
      return url

   url = new_google_calendar_event()
   webbrowser.open_new(url)

.. image:: {static}/images/google-calendar-event-example.png
  :alt: share a google calendar event via a url


I was struggling to find any official documentation, so I figured Google's `Gemini AI model <https://gemini.google.com/>`__ might know where this is documented.

.. image:: {static}/images/gemini-google-calendar-convo.png
  :alt: share a google calendar event via a url

Using the app on my phone, Gemini informed me of a `useful Google Calendar Help thread response from Neil@GCalTools <https://support.google.com/calendar/thread/128416249?authuser=0&hl=en&msgid=129231290>`__.

   The official documentation says to use "https://calendar.google.com/calendar/render" instead of "https://calendar.google.com/calendar/event", but they both work, at least for now.
      \- Neil\@GCalTools, Google Calendar Help

**Relevant Links**

Read more documentation of possible url arguments in the `add-event-to-calendar-docs Github repo
<https://github.com/InteractionDesignFoundation/add-event-to-calendar-docs/blob/main/services/google.md>`__.

`Wikipedia Time Zone List <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`__

`Recurrence Rule Syntax <https://icalendar.org/iCalendar-RFC-5545/3-8-5-3-recurrence-rule.html>`__

`Kalinka Google Calendar Link Generator <https://kalinka.tardate.com/>`__