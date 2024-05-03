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

      Base URL: https://calendar.google.com/calendar/u/0/r/eventedit
      
      URL Arguments

      action: defines action to perform for person who clicks link, "TEMPLATE"
      text: Event Title
      dates: 20240503T123000Z/20240503T133000Z (start_datetime / end_datetime)
      details: include info about the event
      location: url to webcast, call or physical location name
      ctz: set the time zone by its name, ex: "America/New_York" (See all time zones: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
      recur: set recurring invite ex: RRULE:FREQ%3DWEEKLY;INTERVAL%3D3 (See recurrence rule syntax: https://icalendar.org/iCalendar-RFC-5545/3-8-5-3-recurrence-rule.html)
      crm: if Free, Busy, or Out of Office. AVAILABLE, BUSY or BLOCKING
      add: add a list of guests by email, ex: elf1@example.com,elf2@example.com

      Google Documentation: https://github.com/InteractionDesignFoundation/add-event-to-calendar-docs/blob/main/services/google.md
      """
      payload = {
         "action": "TEMPLATE",
         "text": "Title of Event",
         "dates": "20240504T123000Z/20240504T133000Z",
         "details": "Event Details: https://lofipython.com",
         "location": "Link to Webcast, call or physical location",
         "ctz": "America/Chicago",
         "crm": "AVAILABLE"
      }
      # Returns str of URL encoded parameters.
      url_parameters = urlencode(payload)
      url = f"https://calendar.google.com/calendar/u/0/r/eventedit?{url_parameters}"
      print(url)
      return url

   url = new_google_calendar_event()
   webbrowser.open_new(url)


.. image:: {static}/images/google-calendar-event-example.png
  :alt: share a google calendar event via a url


Read the full documentation of url arguments in Google's `add-event-to-calendar-docs Github repo
<https://github.com/InteractionDesignFoundation/add-event-to-calendar-docs/blob/main/services/google.md>`__.