Run Python in Your HTML Via a Custom Django HTML Filter
#######################################################
:date: 2024-03-31 16:18
:author: lofipython
:category: coding, programming, python, Django
:tags: django custom filter, dynamic HTML python django, running Python in Django HTML
:slug: how-to-write-a-custom-django-html-filter
:status: published

These are steps I followed to set up a custom Django filter 
to divide a number by another number. Today's post comes with a side of mathematics!
Here's how to set up a custom Django filter that returns the quotient of two numbers.
I mostly followed along with the `Django custom template tags documentation <https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/>`__.

**Install Django Python Library**

.. code:: console

   pip install Django


**Create templatetags.py**

I dropped this Python file into my top-level folder of my project that held different app folders, 
static folder and templates folder. The @register.filter decorator registers the function so Django 
knows the divide function exists.

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


In the HTML, call the divide function by passing two numeric arguments:

.. code-block:: html
   
   {{ hotel.price|divide:16 }}

1. A number to be divided the hotel price from a "Hotels" DB model
2. The function name to call and a number to divide by. Here we use "divide:16" to approximately convert Mexican pesos to US dollars.



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

