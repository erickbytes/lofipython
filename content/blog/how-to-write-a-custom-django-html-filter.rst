Run Python in Your HTML Via a Custom Django Template Tags Filter
################################################################
:date: 2024-03-31 16:18
:author: lofipython
:category: coding, programming, python, Django
:tags: django custom filter, dynamic HTML python django, running Python in Django HTML
:slug: how-to-write-a-custom-django-html-filter
:status: published

This post shows how to set up a custom Django template tag filter. With help from Django's load built-in, 
you can execute a Python function from your app's HTML. In this example, the function returns the quotient,
or result of dividing two numbers. Mathematics and Python for the win!

I worked some of this out with help from Bing and
following along with the `Django custom template tags documentation <https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/>`__.

**Install Django Python Library**

.. code:: console

   pip install Django


**Create templatetags.py**

I created a "templatetags" folder in the app folder and placed templatetags.py within it. 
The Django docs recommend your app's folder. Below, the @register.filter decorator registers the divide function so Django knows it exists.

.. code-block:: python

   from django import template

   register = template.Library()

   @register.filter
   def divide(value, divisor):
      """A Django filter that accepts 2 arguments:
      1. value, number to be divided
      2. divisor, number to divide by

      Returns the quotient in hundredths decimal format.
      """
      # Check if the argument is zero to avoid division by zero error.
      if divisor == 0:
         return None
      quotient = value / divisor
      return f"{quotient:.2f}"


**Edit Your HTML Code to Call the Divide Function**

.. code-block:: html
   
   {% extends 'base.html' %}
   {% block content %}
   {% load templatetags %}
   <div class="container" style="display: inline-block; inline-size: 90%; block-size: auto; writing-mode: horizontal-tb;">
   {% for hotel in hotels %}
   <div class="row row-cols-3" style="display: flex; justify-content: flex-end; padding: 10px; margin: 10px; background-color: #f0ffff; box-shadow: 5px 5px 10px gray; border-radius: 10px;">
      <div class="col">
      <h5 style="color: green;">Peso: ${{ hotel.price }}</h5>
      <h5 style="color: gray;">USD: ${{ hotel.price|divide:16.5 }}</h5>
      </div></div>
   {% endfor %}
   </div>
   {% endblock %}


In the HTML, call the divide function by loading the templatetags module and then passing two numeric arguments:

.. code:: console
   
   {{ hotel.price|divide:16.5 }}

1. A number to be divided, here the hotel price from a "Hotel" DB model
2. The function name to call and a number to divide by. Here we use "divide:16.5" to approximately convert Mexican pesos to US dollars. Currently, the exchange rate fluctuates between 16-17 pesos per dollar.



**Basic Hotel Model Example**

.. code-block:: python
      
   from django.db import models

   class Hotel(models.Model):
      name = models.CharField(max_length=200)
      price = models.DecimalField(max_digits=10, decimal_places=2)
      address = models.CharField(max_length=200)
      city = models.CharField(max_length=200)
      all_inclusive = models.BooleanField()
      photo = models.ImageField(upload_to="media")



**Register Model in admin.py**

.. code-block:: python

   from django.contrib import admin
   from .models import Hotel

   admin.site.register(Hotel)


I was pleased to be able to make some on the fly mathematic calculations in my HTML 
with a custom Django filter!


.. image:: {static}/images/django-filter-successful.png
  :alt: django filter in action example HTML page

