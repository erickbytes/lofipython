A Guide To Making HTTP Requests To APIs With JSON & Python
##########################################################
:date: 2020-05-18 05:41
:author: pythonmarketer
:category: Chicago, coding, HTTP, json, pandas, programming
:tags: api, data, python, requests, sandwiches, web
:slug: how-to-make-json-requests-with-python
:status: published

This contains all of my best API-related knowledge picked up since learning how to use them. All APIs have their own style, quirks and unique requirements. This post explains general terminology, tips and examples if you're looking to tackle your first API.

**Here's what is covered:**

#. API & HTTP Lingo You Should Know
#. Testing and Exporting Python Request Code from Postman (Optional)
#. Formatting Your Request
#. Example GET and POST Requests
#. "Gotchyas" To Avoid
#. Sidebar: requests.Session()
#. Dig deeper into requests by raising your HTTPConnection.debuglevel

..

   **Terminology Clarification**: I will refer to "items" or "data" throughout this post. This could be substituted for contacts or whatever data you are looking for. For example, you might be fetching a page of contacts from your CRM. Or fetching your tweets from Twitter's API. Or searching the Google location API, you might look up an address and return geo-location coordinates.

API & HTTP Lingo You Should Know
--------------------------------

**Hypertext Transfer Protocol (HTTP)**

Per `Mozilla <https://developer.mozilla.org/en-US/docs/Web/HTTP>`__, "Hypertext Transfer Protocol (HTTP) is an application-layer protocol for transmitting hypermedia documents, such as HTML. It was designed for communication between web browsers and web servers, but it can also be used for other purposes. HTTP follows a classical `client-server model <https://en.wikipedia.org/wiki/Client%E2%80%93server_model>`__, with a client opening a connection to make a request, then waiting until it receives a response."

   HTTP: you = client. API = way to communicate with server

**Application Programming Interface (API)**

`Per Wikipedia <https://en.wikipedia.org/wiki/Application_programming_interface>`__, the purpose of an API is to simplify "programming by `abstracting <https://en.wikipedia.org/wiki/Abstraction_(software_engineering)>`__ the underlying implementation and only exposing objects or actions the developer needs."

**Representational State Transfer (REST)**

`REST <https://en.wikipedia.org/wiki/Representational_state_transfer>`__ is an architectural style of web APIs. It is the dominant architecture that many APIs use. Simple Object Access Protocol (`SOAP <https://smartbear.com/blog/test-and-monitor/soap-vs-rest-whats-the-difference/>`__) is another style I've heard of, but it seems less common nowadays.

A REST API is built for interoperability and has properties like: "simplicity of a uniform interface" and "visibility of communication between components by service agents." [`Wikipedia <https://en.wikipedia.org/wiki/Representational_state_transfer>`__] If an API follows REST, it has many good principles baked in.

**GET, POST and PATCH**

These are three common types of request methods.

-  `GET`: Read data returned, such as all of your tweets in `the Twitter API <https://developer.twitter.com/en/docs>`__.
-  `POST`: Create a new item, like writing a new tweet. Can also update existing data. Tweets aren't editable though!
-  `PATCH`: Similar to `POST`, this is typically used for updating data.

**URL or "Endpoint"**

This is the website target to send your request. Some APIs have multiple endpoints for different functionality.

**URL Parameters**

Values you pass to tell the API what you want. They are defined by the API specifications, which are usually well documented. In Python's requests library, they may be passed as `keyword arguments <https://treyhunner.com/2018/04/keyword-arguments-in-python/>`__. Sometimes they are passable directly within the endpoint url string.

**Body or "Payload"**

To make a request, you send a payload to the url. Often this is a JSON string with the API's URL parameters and values, AKA the request body. If the `API is written specifically for Python <https://jira.readthedocs.io/>`__, it might accept an actual Python dictionary.

**Javascript Object Notation (JSON)**

`JSON <https://www.youtube.com/watch?v=KnAyziNnuI0>`__ is the data interchange standard for all languages. Usually it is the default way to pass data into and receive data from an API. If making a POST, you can check your json object is formatted correctly by using a `json linter <https://jslint.com/>`__. Or try Python's `json.tool <https://docs.python.org/3/library/json.html#module-json.tool>`__! You can also pretty print your JSON or python dictionary with the `pprint <https://docs.python.org/3/library/pprint.html>`__ module. If you're using json.dumps remember it has `pretty printing accessible by keyword arguments <https://docs.python.org/3/library/json.html>`__! These features are accessible in the standard library. Isn't Python great? See also: `Python 101 - An Intro to Working with JSON <https://www.blog.pythonlibrary.org/2020/09/15/python-101-an-intro-to-working-with-json/>`__


**Pages**

API data is commonly returned in multiple pages when there is a lot of data returned. Each page can be accessed one request at a time. Sometimes you can specify how many items you want on a page. But there is usually a maximum items per page limit like 100.

**Status Code**

Each request usually gives you a `numeric code corresponding to happened <https://en.wikipedia.org/wiki/List_of_HTTP_status_codes>`__ when the server tried to handle your request. There is also usually a message returned.


**Headers**

These usually contain website cookies and authorization info. They also may tell the API what kind of data you want back. JSON and XML are the two most common types of data to return. You can specify the return format in the **content-type** headers.

   If you need to parse an XML response, check out Python's stock `ElementTree API <https://docs.python.org/3.8/library/xml.etree.elementtree.html>`__. I've only seen a few APIs using XML responses, such as the `USPS Address Validation API <https://www.usps.com/business/web-tools-apis/>`__.

**Authorization**

Authorization varies widely. This is the level of identification you need to pass to the API to make a request. Public APIs might require none. Some just need a username and password. Others use the `Oauth standard <https://en.wikipedia.org/wiki/OAuth>`__, which is a system involving credentials and tokens for extra security.

   **Authorization Scheme Example [**\ `Mozilla <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization>`__\ **]**

   Authorization: <auth-scheme> <authorisation-parameters>

.. code-block:: python

   # headers python dict example
   headers = {"Authorization": f"basic {token}"}


Creating the Request JSON
-------------------------

I recommend using `Postman <https://www.postman.com/>`__ in most cases, depending on the complexity of the API. If the JSON syntax is straightforward, you can format your data as a python dictionary, then convert it to a JSON object with **json.dumps** from the standard library's `json module <https://docs.python.org/3/library/json.html#json.dumps>`__. But JSON can be tricky sometimes. You may also need to pass a dictionary of HTTP headers.

Some APIs have "Postman Collections", a set of Python (or any language) script templates for the API. In those cases, it might make sense to use those resources.

   **Path One: Make HTTP request with json & requests libraries**

   Format Python dict with **json.dumps** from the standard library's `json module <https://docs.python.org/3/library/json.html#json.dumps>`__. Infer API requirements from documentation. Use requests for HTTP.

   **Path Two: Make HTTP request with Postman & requests library**

   Use Postman to generate the JSON payload. Plug headers and payload into requests. Use requests library for HTTP.

Postman has a friendly interface for plugging in all your pieces and tinkering with your request body until it works. Make it easier on yourself and use Postman, especially if there are collections. An alternative is to troubleshoot in Python if you are confident in your grasp of the API. I use both options depending on my familiarity with the API at hand.

Formatting Your Request
-----------------------

#. Once you have the request working, you may `export your Postman request to almost any language <https://learning.postman.com/docs/postman/sending-api-requests/generate-code-snippets/>`__. For Python, you can sometimes export to the requests, http.client or urllib libraries. Hit the "code" button in Postman and then copy your code.
#. Paste your Postman headers, payload and url into your existing code.
#. You may want to use a dict or `string formatting <https://www.blog.pythonlibrary.org/2020/04/07/python-101-working-with-strings/>`__ to pass values to your request parameters or url.
#. If the API uses a token or other form of authorization that needs to be refreshed intermittently, I usually have a function that returns a token. **token = fetch_token()** Then put the token in the headers dict. **{"Authorization": f"basic {token}"}** Finally pass your headers and payload to your **requests.get**, **requests.post**, or **requests.request** function along with the endpoint url. You're now ready to test the request.

If you choose not to use Postman, you can use the json library. See the use of **json.dumps()** to convert a dictionary to a JSON object in example #2 below.

Python Installation
-------------------

You can install **requests** with `pip <https://lofipython.com/how-to-python-pip-install-new-libraries/>`__. Alternatively, **http.client** is included within the Python standard library. If you want to convert HTTP response data to a dataframe or csv, install **pandas**.

::

    python -m pip install requests
    python -m pip install pandas

Example #1: **GET** the geolocation details of any public location with the Google API
--------------------------------------------------------------------------------------

This was modified from another example of `Google's Geolocation API <https://www.geeksforgeeks.org/get-post-requests-using-python/>`__. To use this, you need to 
`create a developer account with Google <https://developers.google.com/maps/documentation/geolocation/intro>`__ and paste your API keys below.

.. code-block:: python

   import requests


   # Find the best double-cheeseburger + fries $7 can buy.
   payload = {"key": "Add_Google_API_Key_Here", "address": "Redhot Ranch"}
   url = "https://maps.googleapis.com/maps/api/geocode/json"
   # Optional: set a 5 second timeout for the http request.
   r = requests.get(url=url, params=payload, timeout=5)
   print(r.text)
   print(r.status_code)
   data = r.json()

   # Extract the latitude, longitude and formatted address of the first matching location.
   latitude = data["results"][0]["geometry"]["location"]["lat"]
   longitude = data["results"][0]["geometry"]["location"]["lng"]
   formatted_address = data["results"][0]["formatted_address"]
   print(longitude)
   print(latitude)
   print(formatted_address)

   # Optional: convert response into a dataframe with pandas.
   # import pandas as pd
   # location_df = pd.json_normalize(data['results'])
   # location_df.to_csv('Locations.csv')

**Above you can see:**

-  requests makes it easy to see the server's text response also with **response.text**
-  requests also makes JSON encoding easy with **response.json()**
-  **pd.json_normalize()** is convenient to convert the response dictionary to a dataframe.

Example #2: Encode a Python dictionary to json string and **POST** to a hypothetical API
----------------------------------------------------------------------------------------

#. Create a dictionary with request body data and pretty inspect it with pprint.
#. Encode the json string with **json.dumps** from the standard library's `json module <https://docs.python.org/3/library/json.html#json.dumps>`__.
#. **POST** the encoded JSON to the endpoint url with requests.

.. code-block:: python

   import pprint
   import json
   import requests


   def dict_to_json_data():
       """Create request body with fictional contact details."""
       payload = {
           "first_name": "P",
           "last_name": "Sherman",
           "address": "42 Wallaby Way",
           "address_2": "",
           "city": "Sydney",
           "state": "NSW",
           "country": "AU",
           "zip": "2000",
       }
       pprint.pprint(payload)
       json_str = json.dumps(payload, ensure_ascii=True)
       # Optional: encode json str to utf-8.
       return json_str.encode("utf-8")


   def post_data(json_str):
       """This is a fictional API request that passes a json object to requests.
       It decodes the server response with response.json() and 
       Returns dictionary value by calling the data's keys.
       """
       headers = {
           "Authorization": f"Bearer {token}",
           "Content-Type": "application/json",
           "cache-control": "no-cache",
       }
       r = requests.request(
           method="POST",
           url="https://SomeSoftwareAPI.com/people/",
           data=json_str,
           headers=headers,
       )
       data = r.json()
       print(data.keys())
       # Call dict keys to get their values.
       contact_id = data["contact_id"]
       return contact_id


   json_str = dict_to_json_data()
   contact_id = post_data(json_str)


..

   **requests.request keyword argument alternatives for passing data**

   **params** – (optional) Dictionary, list of tuples or bytes to send in the query string for the Request.

   **data** – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request

   **json** – (optional) A JSON serializable Python object to send in the body of the Request

   **[**\ `requests API documentation <https://requests.readthedocs.io/en/latest/api/>`__\ **]**

**"Gotchyas" To Avoid**

-  `Status codes <https://en.wikipedia.org/wiki/List_of_HTTP_status_codes>`__ are your friend. They offer a hint at why your request is not working. If you see 200 or 201, that's a good sign. They're usually helpful, but sometimes they can be misleading.
-  Ensure you are defining the correct content-type. I had an experience where Postman defined two conflicting **content-type** headers and it `caused my request to fail <https://github.com/postmanlabs/postman-code-generators/issues/215>`__. The server's error message indicated the problem was in my JSON, so it took me a while to figure out the headers were the problem.
-  Sometimes it makes a difference if your url has **http://** vs. **https://** in it. Usually **https://** is preferred.

**Sidebar:** `requests.Session() <https://requests.readthedocs.io/en/master/user/advanced/>`__

You might be able to improve performance by using a requests `"session" object <https://requests.readthedocs.io/en/master/user/advanced/>`__.

.. code-block:: python

   import requests


   # A session adds a "keep-alive" header to your HTTP connection + stores cookies across requests.
   s = requests.Session()
   for page in range(0, 2):
       url = f"https://exampleapi.com/widgets/{str(page)}"
       r = s.get(url)
       print(r.text)

**Dig deeper into requests by raising your HTTPConnection.debuglevel**

   **HTTPResponse.debuglevel:** A debugging hook. If `debuglevel <https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.debuglevel>`__ is greater than zero, messages will be printed to stdout as the response is read and parsed.
   Source: `http.client Python Docs <https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.debuglevel>`__

.. code-block:: python

   from http.client import HTTPConnection
   import requests


   HTTPConnection.debuglevel = 1
   payload = {"key":"Add_Google_API_Key_Here", "address":"90 Miles"}
   url = "https://maps.googleapis.com/maps/api/geocode/json"
   r = requests.get(url=url, params=payload, timeout=5)
   print(r.text)

|
|
   **Web Server Gateway Interface (WSGI, pronounced "Wis-Ghee")**

   "As described in `PEP3333 <https://www.python.org/dev/peps/pep-3333/>`__, the Python Web Server Gateway Interface (WSGI) is a way to make sure 
   that web servers and python web applications can talk to each other."  `Gunicorn <https://docs.gunicorn.org/en/latest/install.html>`__ is one 
   of `a few Python WSGI clients <https://flask.palletsprojects.com/en/1.1.x/deploying/wsgi-standalone/#uwsgi>`__. 
   `web2py <https://lofipython.com/2016/04/30/useful-links-for-web2py-beginners/>`__ is another WSGI client and web framework I have used.


**Conclusion**

I remember APIs seemed mysterious and daunting before I had used them. But like all things, they can be conquered with knowledge, understanding and tenacity to keep trying until you figure it out. Good luck!

**Requests Documentation**

`requests.request() API documentation <https://requests.readthedocs.io/en/master/api/>`__

`requests.get() API documentation <https://requests.readthedocs.io/en/latest/api/#requests.get>`__

`requests.post() API documentation <https://requests.readthedocs.io/en/latest/api/#requests.post>`__

**Supplementary Reading**

`Google's HTTP Timing Explanation <https://developers.google.com/web/tools/chrome-devtools/network/reference#timing-explanation>`__

`List of Interesting "Unofficial" APIs <https://github.com/Rolstenhouse/unofficial-apis>`__

`Proxy servers <https://en.wikipedia.org/wiki/Proxy_server>`__

`Making 1 million requests with python-aiohttp <https://pawelmhm.github.io/asyncio/python/aiohttp/2016/04/22/asyncio-aiohttp.html>`__

`Nginx <https://en.wikipedia.org/wiki/Nginx>`__

`Create, read, update and delete (CRUD) <https://en.wikipedia.org/wiki/Create,_read,_update_and_delete>`__