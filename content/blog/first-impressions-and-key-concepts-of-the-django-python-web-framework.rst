First Impressions and Key Concepts of the Django Python Web Framework
#####################################################################
:date: 2024-02-02 12:33
:author: lofipython
:category: coding, programming, python, django, web development
:tags: django web framework, building websites with django python, getting started with a django app
:slug: first-impressions-and-key-concepts-of-the-django-python-web-framework
:status: published

**First Impressions of Django**

Picking up `Django <https://pypi.org/project/Django/>`__ felt right. In the past I used
other Python web frameworks like `web2py <http://www.web2py.com/>`__ and `flask <http://www.web2py.com/>`__.
I mostly avoided Django before now because it felt a bit overkill for the smaller
toy apps I made in my beginning years as a Python developer. For example, this blog
is made with the `Pelican <https://getpelican.com/>`__ static site generator, a
choice which has served me well.

Recently, a project came my way that seemed a good fit to apply Django. The task
required building a travel booking website. For this use case, Django shined. It
fits like a glove on a seasoned Python programmer. I am impressed how quickly I
adapted to it and thrived as I made my minimum viable product website.

Kudos to the Django developers that I, a typical Python programmer
aided with artificial intelligence could rapidly develop using their tools to
achieve my goals. If I could learn to write some decent CSS, I'd be unstoppable!

I highly recommend all Python programmers pick Django for their web apps with more
robust requirements. I say this with no slight to fellow heavyweight Flask or other
popular Python web frameworks like `Tornado <https://www.tornadoweb.org/en/stable/>`__,
`Bottle <https://bottlepy.org/docs/dev/>`__, `CherryPy <https://docs.cherrypy.dev/en/latest/>`__
or `py4web <https://py4web.com/>`__ . All of these can all be justified in the
right situation due to their unique capabilities. Django stands out because it's
pretty easy to reach for things that already exist in the library to get what you
need done. Other frameworks may require a more nuanced skillset to achieve the same results.
Ok, enough pontification. Here are my notes of key Django concepts.

**Start with the Django official tutorial.**

The tutorial is lengthy and starts from the ground up. I commend its thoroughness.
Start there and work your way out. `Django Documentation Tutorial <https://docs.djangoproject.com/en/5.0/intro/tutorial01/>`__

**Django Models, Forms & Fields, models.py and forms.py**

Your forms.py and models.py files are crucial pieces to render a form, collect data
and store it in the database.

**views.py**

The views.py file contains the Python functions that execute the flow of your app.
Each function in the views.py can be a view.

**urls.py**

The urls.py defines your url schema so that when you go to "example.com/any_page",
you can tell django which view to show there.

**settings.py**

After you create your app with django cli commands, a settings.py is automatically generated.
You will need to make edits here occasionally, such as changing the value of debug
to true or false. You may need to add newly installed apps or make other changes
in your settings.py to get things to work.

**HTML + CSS Required**

Your HTML and CSS skills will come in handy when working with Django or any web framework.
This is not a big surprise. You almost always need to know HTML and CSS to mold
your website to your requirements.

**Javascript + jQuery Friendly**

Django seems fully capable of integrating with Javascript libraries. I was able
to get jQuery + AJAX request autocomplete functionality working in my form with
help from Bing's AI Chat. I followed along with this `helpful blog post <https://espere.in/Enhance-Your-Django-App:-Step-by-Step-Guide-to-Implementing-Autocomplete-Search-with-jQuery/>`__
to get my jQuery script working!

.. image:: {static}/images/jQueryautocomplete.png
  :alt: adding autocomplete to a django form with jQuery

**External Django Python Libraries**

Another plus of Django due to its popularity is the amount of external modules that
Python developers have written to add features and functionality. For example,
`django-autocomplete-light <https://django-autocomplete-light.readthedocs.io/en/master/tutorial.html>`__
and the `django-bootstrap-v5 <https://pypi.org/project/django-bootstrap-v5/>`__
CSS library are installed with pip. I successfully used django-bootstrap-v5 to add
bootstrap CSS styling to my website. Note this library requires a slightly older
version of Django.

Often there are several ways to get something done in Django, with external Python libraries
or Javascript libraries each a possibility to succeed. After several hours of
failing to get django-autocomplete-light working, I achieved the same result with
jQuery. It's always good to have options.

**The Admin Panel + admin.py**

One of the best out of the box features of Django is its admin panel and user model.
If you intend to build a website with for your users, this makes Django a great choice.
Don't forget to register your models in your admin.py.

**apps.get_model()**

You can import your models at the top of your code or use this handy convenience function to
retrieve it directly.

**model_to_dict()**

This is another function Django provides for converting a model object class to a Python dictionary.
Once a model is in dictionary format, you can pass it to a django form's "initial" argument
to easily auto-populate a form.

**request.GET()**

Django has its own request objects. You can pass a raw query string to HttpResponseRedirect.
Then, in the view of the target page, you can use this function to get the querystring
value by passing its key.

**render() and contexts**

The render function renders an HTML document. This function has a context argument
that allows you to pass variables into the HTML view.


**How to Install Django**

.. code:: console

   pip install Django


**Django Views.py Code Example**

.. code-block:: python

  from django.shortcuts import render
  from django.apps import apps
  from django.forms.models import model_to_dict
  from forms import BookingForm

  def index(request):
      """Displays an HTML page with a form. If the request is a post, save the data
      to the DB. If booking_id is passed in the url querystring, populate the form
      with data from that id."""
      if request.method == "POST":
            # Create a form instance and populate it with data from the request.
            form = BookingForm(request.POST)
            if form.is_valid():
                new_booking = form.save()
                return HttpResponseRedirect(f"/hotels?booking_id={new_booking.id}")
      try:
          booking_id = request.GET["booking_id"]
      except:
          booking_id = ""
      if booking_id.isdigit():
          Booking = apps.get_model(app_label="your_app_name", model_name="Booking")
          booking = Booking.objects.get(id=booking_id)
          booking_dict = model_to_dict(booking)
      context = {}
      if booking_dict:
          context["form"] = BookingForm(initial=booking_dict)
      else:
          context["form"] = BookingForm()
      return render(request, "simple_django_form.html", context)


      def hotels(request):
          """Render a list of hotels to for clients to view from the Hotel model."""
          booking_id = request.GET["booking_id"]
          Booking = apps.get_model(app_label="your_app_name", model_name="Booking")
          booking = Booking.objects.get(id=booking_id)
          Hotel = apps.get_model(app_label="bookings", model_name="Hotel")
          hotels = Hotel.objects.filter(city__contains=booking.to_city)
          # Pass context to access variables directly in hotels.html: {{ return_date }}
          context = {
              "hotels": hotels,
              "booking_id": booking_id,
              "departure_date": booking.departure_date.date(),
              "return_date": booking.return_date.date(),
              "to_city": booking.to_city,
          }
          return render(request, "hotels.html", context)


**Basic Model Example**

.. code-block:: python

    from django.db import models

    class Booking(models.Model):
        departure_date = models.DateTimeField("departure date")
        return_date = models.DateTimeField("return date")
        from_city = models.CharField("Origen", max_length=200)
        to_city = models.CharField("Destino", max_length=200)


Hopefully this helped you get started with Django. In my own experience, once you
get some momentum going with this web framework, you'll progress rapidly!


**Supplementary Django Links**

`Django Form Fields Reference <https://docs.djangoproject.com/en/5.0/ref/forms/fields/>`__

`Django Model Fields Reference <https://docs.djangoproject.com/en/5.0/ref/models/fields/>`__

`Django Settings Reference <https://docs.djangoproject.com/en/5.0/ref/settings/>`__

`Django How-to Guides <https://docs.djangoproject.com/en/5.0/howto/>`__
