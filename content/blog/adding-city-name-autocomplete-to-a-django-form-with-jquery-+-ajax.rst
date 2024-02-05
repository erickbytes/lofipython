Adding City Name Autocomplete to a Django Form With jQuery + AJAX
#################################################################
:date: 2024-02-05 14:33
:author: lofipython
:category: coding, programming, python, AJAX, Javascript, web development
:tags: making a city autocomplete form, how to make django autocomplete, integrating Django and jQuery
:slug: adding-city-name-autocomplete-to-a-django-form-with-jquery-ajax
:status: published

Below is a slightly modified adaptation of the `Espere.in Step By Step Guide <https://espere.in/Enhance-Your-Django-App:-Step-by-Step-Guide-to-Implementing-Autocomplete-Search-with-jQuery/>`__
by Abdulla Fajal. I needed to make a few changes to the code to get things to work.
I also expanded the example to show how I created the Django model and imported cities data.
In this post, I'll show how you can use AJAX and `jQuery Autocomplete <https://jqueryui.com/autocomplete/>`__
with a Django model to create a form with city auto-completion.


**Add a Model to models.py**

.. code-block:: python

    class City(models.Model):
        city = models.CharField(max_length=200)
        country = models.CharField(max_length=200)


**Migrate the Django Model**

.. code:: console

   python manage.py makemigrations City
   python manage.py migrate


**Add Auto-complete TextInput() to forms.py**

The key item here is the "id" attribute holding the value "search-input". This id
will tell jQuery for which form element to render the autocomplete view.

.. code-block:: python

       from django import forms
       from bookings.models import Booking

       class BookingForm(forms.ModelForm):
           class Meta:
               model = Booking
               fields = "__all__"
               widgets = {
                   "city": forms.TextInput(
                       attrs={
                           "class": "form-control",
                           "id": "search-input",
                           "name": "city_name",
                           "placeholder": "Type to search",
                       }
                   )
               }


**Download the World Cities Database from Simplemaps**

The `World Cities Database <https://simplemaps.com/data/world-cities>`__ basic version
is free and allowed for commercial use. In this example, this provides the cities data.

**Import the Cities Database to Django Model**

Now we need to import the cities to our Django model. I achieved this by running
this code in the Django shell and entering each line individually. This code was
modified from a `Stack Overflow post <https://stackoverflow.com/questions/2459979/how-to-import-csv-data-into-django-models>`__.
The World Cities data stores the city in the first column (index 0) and the country
in the 5th column (index 4).

.. code:: console

   python manage.py shell


.. code-block:: python

  import csv
  from django.apps import apps

  City = apps.get_model(app_label="bookings", model_name="City")
  with open("worldcities.csv") as f:
      reader = csv.reader(f)
      for row in reader:
          _, created = City.objects.get_or_create(city=row[0], country=row[4],)


.. image:: {static}/images/djangoshell.png
  :alt: running Python in the Django shell


**View Your City Model in the Admin Panel**

Enter the below command to start your local Django development server. Then you
can go to http://127.0.0.1:8000/admin in a web browser to see your model on the back-end.

.. code:: console

   python manage.py runserver


**Add jQuery Scripts to HTML File**

Add the jquery import scripts to your HTML <head> tag.

.. code-block:: javascript

  <link rel="stylesheet" href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css" type="text/css" media="all" />

  <!-- Add jQuery and jQuery UI JavaScript -->
  <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>


Add the jQuery autocomplete script to the bottom of your HTML. This is where we
reference the "search-input" id in our form and specify the url route "/ajax_calls/search/".

.. code-block:: javascript

  <script>
  $(document).ready(function(){
      $("#search-input").autocomplete({
          source: "/ajax_calls/search/",
          minLength: 2,
          open: function(){
              setTimeout(function () {
                  $('.ui-autocomplete').css('z-index', 99);
              }, 0);
          }
      });
  });
  </script>


**Add the Autocomplete View to Views.py**

Note this script is using an `XMLHttpRequest API <https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest>`__,
which is used in combination with `AJAX <https://en.wikipedia.org/wiki/Ajax_(programming)>`__

.. code-block:: python

    import json
    from django.apps import apps
    from django.forms.models import model_to_dict

    def autocomplete(request):
        """Show the City model records via AJAX + jQuery."""
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            City = apps.get_model(app_label="bookings", model_name="City")
            term = request.GET["term"]
            search_results = City.objects.filter(city_name__startswith=term)
            cities = [f"{result.city_name}, {result.country}" for result in search_results]
            data = json.dumps(cities)
       else:
            data = "fail"
       return HttpResponse(data, "application/json")


**Understanding Ajax + XMLHttpRequest**

  Ajax is a technique that uses XMLHttpRequest  to exchange data with a web server
  without reloading the whole page. XMLHttpRequest is an object that allows web apps
  to make HTTP requests and receive the responses programmatically using JavaScript.
  Ajax stands for Asynchronous JavaScript and XML,  which means that the data exchange
  can happen in the background, while the user interacts with the web page.
  - Bing AI

**Add the URL Route to urls.py**

.. code-block:: python

    from django.urls import path
    from . import views

    app_name = "your_app_name"
    urlpatterns = [
        path('ajax_calls/search/', views.autocomplete, name='city_autocomplete'),
    ]


**Voila! The City Autocomplete View**

.. image:: {static}/images/jQueryautocomplete.png
  :alt: adding autocomplete to a Django form with jQuery


This felt very rewarding to see once it was working. I stretched my abilities
outside of coding only in Python to achieve this functionality in my website.
Someday I would like to be an experienced Javascript developer also. `jQuery <https://api.jquery.com/>`__ has
been a staple in web development for many years. Auto-complete is just one of the features
that this core Javascript library enables. I am definitely intrigued to explore jQuery further.

Want to read more about Django? Check out my
`notes on Django here <https://lofipython.com/first-impressions-and-key-concepts-of-the-django-python-web-framework>`__.
