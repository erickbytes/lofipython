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
This example uses the Python standard: urllib to format the Google calendar url parameters and webbrowser \
to open the url in a browser. This is a handy little trick to keep in your back pocket!


.. code-block:: python

   import webbrowser
   from urllib.parse import urlencode

   def new_google_calendar_event():
      """
      Pass an event to Google Calendar with url arguments.

      domain: https://calendar.google.com/calendar/u/0/r/eventedit
      args:
         text=Your Event Title
         &dates=YYYYMMDDT123000Z/YYYYMMDDT133000Z (start_datetime / end_datetime)
         &details=View+more+information:+https://ir.fubo.tv/events-and-presentations/event-details/2024/Fubo-Q1-2024-Earnings-Conference-Call/default.aspx&location
      """

      payload = {
         "text": "Title of Event",
         "dates": "20240504T123000Z/20240504T133000Z",
         "details": "Event Details: https://lofipython.com",
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

