Title: A Guide To Making HTTP Requests To APIs With JSON & Python
Date: 2020-05-18 05:41
Author: pythonmarketer
Category: Chicago, coding, HTTP, json, pandas, programming
Tags: api, data, python, requests, sandwiches, web
Slug: how-to-make-json-requests-with-python
Status: published

This contains all of my best API-related knowledge picked up since learning how to use them. All APIs have their own style, quirks and unique requirements. This post explains general terminology, tips and examples if you're looking to tackle your first API.

**Here's what is covered:**

1.  API & HTTP Lingo You Should Know
2.  Testing and Exporting Python Request Code from Postman (Optional)
3.  Formatting Your Request
4.  Example GET and POST Requests
5.  "Gotchyas" To Avoid
6.  Sidebar: requests.Session()
7.  Dig deeper into requests by raising your HTTPConnection.debuglevel

> **Terminology Clarification**: I will refer to "items" or "data" throughout this post. This could be substituted for contacts or whatever data you are looking for. For example, you might be fetching a page of contacts from your CRM. Or fetching your tweets from Twitter's API. Or searching the Google location API, you might look up an address and return geo-location coordinates.

## API & HTTP Lingo You Should Know

**Hypertext Transfer Protocol (HTTP)**

Per [Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP),"Hypertext Transfer Protocol (HTTP) is an application-layer protocol for transmitting hypermedia documents, such as HTML. It was designed for communication between web browsers and web servers, but it can also be used for other purposes. HTTP follows a classical [client-server model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model){.external}, with a client opening a connection to make a request, then waiting until it receives a response."

> HTTP: you = client. API = way to communicate with server

**Application Programming Interface (API)**

[Per Wikipedia](https://en.wikipedia.org/wiki/Application_programming_interface), the purpose of an API is to simplify "programming by [abstracting](https://en.wikipedia.org/wiki/Abstraction_(software_engineering) "Abstraction (software engineering)"){.mw-redirect} the underlying implementation and only exposing objects or actions the developer needs."

**Representational State Transfer (REST)**

[REST](https://en.wikipedia.org/wiki/Representational_state_transfer) is an architectural style of web APIs. It is the dominant architecture that many APIs use. Simple Object Access Protocol ([SOAP](https://smartbear.com/blog/test-and-monitor/soap-vs-rest-whats-the-difference/)) is another style I've heard of, but it seems less common nowadays.

A REST API is built for interoperability and has properties like: "simplicity of a uniform interface" and "visibility of communication between components by service agents." \[[Wikipedia](https://en.wikipedia.org/wiki/Representational_state_transfer)\] If an API follows REST, it has many good principles baked in.

**`GET`, `POST` and `PATCH`**

These are three common types of request methods.

-   `GET`:  Read data returned, such as all of your tweets in [the Twitter API](https://developer.twitter.com/en/docs).
-   `POST`: Create a new item, like writing a new tweet. Can also update existing data. Tweets aren't editable though!
-   `PATCH`: Similar to `POST`, this is typically used for updating data.

**URL or "endpoint"**

The website location to send your request

**URL Parameters**

Values you pass to tell the API what you want. They are defined by the API specifications, which are usually [well documented](https://developers.activecampaign.com/reference). In python's `requests` library, they may be passed as [keyword arguments](https://treyhunner.com/2018/04/keyword-arguments-in-python/). Sometimes they are passable directly within the endpoint url string.

**Body or "payload"**

To make a request, you send a payload to the url. Often this is a JSON string with the API's URL parameters and values, AKA the request body. If the [API is written specifically for Python](https://jira.readthedocs.io/), it might accept an actual Python dictionary.

**Javascript Object Notation (JSON)**

[JSON](https://www.youtube.com/watch?v=KnAyziNnuI0) is the data interchange standard for all languages. Usually it is the default way to pass data into and receive data from an API. If making a  `POST`, you can check your json object is formatted correctly by using a [json linter](https://jslint.com/). Or try Python's [json.tool](https://docs.python.org/3/library/json.html#module-json.tool)! You can also pretty print your JSON or python dictionary with the [pprint](https://docs.python.org/3/library/pprint.html) module. If you're using json.dumps remember it has [pretty printing accessible by keyword arguments](https://docs.python.org/3/library/json.html)! These features are accessible in the standard library. Isn't Python great? See also: [Python 101 - An Intro to Working with JSON](https://www.blog.pythonlibrary.org/2020/09/15/python-101-an-intro-to-working-with-json/)

**Headers**

These usually contain website cookies and authorization info. They also may tell the API what kind of data you want back. JSON and XML are the two most common types of data to return. You can specify the return format in the `content-type` headers.

> If you need to parse an XML response, check out Python's stock [ElementTree API](https://docs.python.org/3.8/library/xml.etree.elementtree.html). I've only seen a few APIs using XML responses, such as the [USPS Address Validation API](https://www.usps.com/business/web-tools-apis/).

**Authorization**

Authorization varies widely. This is the level of identification you need to pass to the API to make a request. Public APIs might require none. Some just need a username and password. Others use the [Oauth standard](https://en.wikipedia.org/wiki/OAuth), which is a system involving credentials and tokens for extra security. 

> **Authorization Scheme Example \[[Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)\]**
>
> Authorization: \<auth-scheme> \<authorisation-parameters>

    # headers python dict example
    headers = {"Authorization": f"basic {token}"}

**Pages**

API data is commonly returned in multiple pages when there is a lot of data returned. Each page can be accessed one request at a time. Sometimes you can specify how many items you want on a page. But there is usually a maximum items per page limit like 100.

**Status code**

Each request usually gives you a [numeric code corresponding to happened](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) when the server tried to handle your request. There is also usually a message returned.

**See also: Web Server Gateway Interface (WSGI, pronounced "Wis-Ghee")**

"As described in [PEP3333](https://www.python.org/dev/peps/pep-3333/), the Python Web Server Gateway Interface (WSGI) is a way to make sure that web servers and python web applications can talk to each other."  [Gunicorn](https://docs.gunicorn.org/en/latest/install.html) is one of [a few Python WSGI clients](https://flask.palletsprojects.com/en/1.1.x/deploying/wsgi-standalone/#uwsgi). [web2py](https://pythonmarketer.wordpress.com/2016/04/30/useful-links-for-web2py-beginners/) is another WSGI client and web framework I have used.

**See also:** [Nginx](https://en.wikipedia.org/wiki/Nginx)

**See also: [Create, read, update and delete (CRUD)](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)**

## Creating the Request JSON

I recommend using [Postman](https://www.postman.com/) in most cases, depending on the complexity of the API. If the JSON syntax is straightforward, you can format your data as a python dictionary, then convert it to a JSON object with `json.dumps` from the standard library's [json module](https://docs.python.org/3/library/json.html#json.dumps). But JSON can be tricky sometimes. You may also need to pass a dictionary of HTTP headers.

Some APIs have "Postman Collections", a set of Python (or any language) script templates for the API. In those cases, it might make sense to use those resources.

> **Path One: Make HTTP request with json & requests libraries**
>
> Format Python dict with `json.dumps` from the standard library's [json module](https://docs.python.org/3/library/json.html#json.loads).  Infer API requirements from documentation. Use requests for HTTP.
>
> **Path Two: Make HTTP request with Postman & requests library**
>
> Use Postman to generate the JSON payload. Plug headers and payload into requests. Use requests library for HTTP.

Postman has a friendly interface for plugging in all your pieces and tinkering with your request body until it works. Make it easier on yourself and use Postman, especially if there are collections. An alternative is to troubleshoot in Python if you are confident in your grasp of the API. I use both options depending on my familiarity with the API at hand.

Once you have the request working, you may [export your Postman request to almost any language](https://learning.postman.com/docs/postman/sending-api-requests/generate-code-snippets/). For Python, you can sometimes export to the `requests`,  `http.client` or `urllib` libraries. Hit the "code" button in Postman and then copy your code.

> If you choose not to use Postman, you can use the json library. See the use of `json.dumps()`to convert a dictionary to a JSON object in Example #2 below

## Formatting Your Request

1.  Paste your Postman headers, payload and url into your existing code.
2.  You may want to use a dict or [string formatting](https://www.blog.pythonlibrary.org/2020/04/07/python-101-working-with-strings/) to pass values to your request parameters or url.
3.  If the API uses a token or other form of authorization that needs to be refreshed intermittently, I usually have a function that returns a token. `token = fetch_token()` Then put the token in the headers dict.  `{"Authorization": f"basic {token}"}`{style="white-space:pre-wrap;"} Finally pass your headers and payload to your  `requests.get` or `requests.request` function along with the endpoint url. You're now ready to test the request.

## Python Installation

You can install `requests` with [pip](https://pythonmarketer.wordpress.com/2018/01/20/how-to-python-pip-install-new-libraries/). Alternatively, `http.client` is included within the Python standard library. If you want to convert HTTP response data to a dataframe or csv, install `pandas.`

`python -m pip install requests`

`python -m pip install pandas`

## Example #1: `GET` the geolocation details of any public location with the Google API

This was modified from another example of [Google's Geolocation API](https://www.geeksforgeeks.org/get-post-requests-using-python/). To use this, you need to [create a developer account with Google](https://developers.google.com/maps/documentation/geolocation/intro) and paste your API keys below.

    import requests
    # import pandas as pd

    """Find the best double-cheeseburger + fries $7 can buy."""
    payload = {"key":"Add_Google_API_Key_Here", "address":"Redhot Ranch"}
    # optional: set a 5 second timeout for the http request
    r = requests.get(url="https://maps.googleapis.com/maps/api/geocode/json", 
                     params=payload,
                     timeout=5)
    print(r.text)
    print(r.status_code)
    data = r.json()

    # extracting latitude, longitude and formatted address of the first matching location
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    formatted_address = data['results'][0]['formatted_address']
    print(longitude)
    print(latitude)
    print(formatted_address)

    # optional: convert response into a dataframe with pandas 
    # location_df = pd.json_normalize(data['results'])
    # location_df.to_csv('Locations.csv')

**Above you can see:**

-   `requests` makes it easy to see the server's text response also with `response.text`
-   `requests` also makes JSON encoding easy with `response.json()`
-   I like to use `pd.json_normalize()` to convert the response object to a dataframe.

## Example #2: Encode a Python dictionary to json string and `POST` to a hypothetical API

1.  Create a simple dictionary with request body data and pretty inspect it with pprint.
2.  Convert it to encoded json string with `json.dumps` from the standard library's [json module](https://docs.python.org/3/library/json.html#json.loads).
3.  `POST` the encoded JSON to the endpoint url with requests.

```{=html}
<!-- -->
```
    import pprint
    import json
    import requests

    def convert_dict_to_json_object():
        """Create request body with fictional contact details."""
        payload = {
            "first_name":"P",
            "last_name":"Sherman",
            "address":"42 Wallaby Way",
            "address_2":"",
            "city":"Sydney",
            "state":"NSW",
            "country":"AU",
            "zip":"2000"
            }
        pprint.pprint(payload)
        json_str = json.dumps(payload, ensure_ascii=True)
        # encode json str to utf-8
        return json_str.encode("utf-8")

    def create_new_contact(json_str):
        """
        This is a fictional API request. 
        Passing a json object to requests.
        Decoding server response with response.json(), 
        Returning a contact id by calling the data's keys.
        """
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "cache-control": "no-cache",
            "Postman-Token": f"{postman_token}"
            }
        r = requests.request(method="POST", 
                             url="https://SomeSoftwareAPI.com/contacts/", 
                             data=json_str, 
                             headers=headers)
        data = r.json()
        print(data.keys())
        contact_id = data['contact_id'] # call dict keys to get their values
        return contact_id

    json_str = convert_dict_to_json_object()
    contact_id = create_new_contact(json_str)

> **requests.request keyword argument alternatives for passing data**
>
> **params** – (optional) Dictionary, list of tuples or bytes to send in the query string for the [`Request`{.xref .py .py-class .docutils .literal .notranslate}](https://2.python-requests.org/en/master/api/#requests.Request "requests.Request"){.reference .internal}.
>
> **data** – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the [`Request`{.xref .py .py-class .docutils .literal .notranslate}](https://2.python-requests.org/en/master/api/#requests.Request "requests.Request"){.reference .internal}.
>
> **json** – (optional) A JSON serializable Python object to send in the body of the [`Request`{.xref .py .py-class .docutils .literal .notranslate}](https://2.python-requests.org/en/master/api/#requests.Request "requests.Request"){.reference .internal}.
>
> **\[[requests API documentation](https://2.python-requests.org/en/master/api/)\]**

**"Gotchyas" To Avoid**

-   [Status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) are your friend. They offer a hint at why your request is not working. If you see 200 or 201, that's a good sign. They're usually helpful, but sometimes they can be misleading.
-   Ensure you are defining the correct content-type. I had an experience where Postman defined two conflicting `content-type` headers and it [caused my request to fail](https://github.com/postmanlabs/postman-code-generators/issues/215). The server's error message indicated the problem was in my JSON, so it took me a while to figure out the headers were the problem.
-   Sometimes it makes a difference if your url has `http://` vs. `https://` in it. Usually `https://` is preferred.** **

**Sidebar: [requests.Session()](https://requests.readthedocs.io/en/master/user/advanced/)**

You might be able to improve performance by using a requests ["session" object](https://requests.readthedocs.io/en/master/user/advanced/).

    """
    a session adds a "keep-alive" header to your HTTP connection.
    It can be used to store cookies across requests.
    """
    import requests
    s = requests.Session()
    for page in range(0, 2):
        url = f"https://SomeSoftwareAPI.com/contacts/{str(page)}"
        r = s.get(url)
        print(r.text)

**Dig deeper into requests by raising your HTTPConnection.debuglevel**

**HTTPResponse.debuglevel:** A debugging hook. If [`debuglevel`{.xref .py .py-attr .docutils .literal .notranslate}](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.debuglevel "http.client.HTTPResponse.debuglevel"){.reference .internal} is greater than zero, messages will be printed to stdout as the response is read and parsed. **- [http.client Python Docs](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.debuglevel)**

    from http.client import HTTPConnection
    import requests
    HTTPConnection.debuglevel = 1
    payload = {"key":"Add_Google_API_Key_Here", "address":"90 Miles"}
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    r = requests.get(url=url, params=payload, timeout=5)
    print(r.text)

**Conclusion**

I remember APIs seemed mysterious and daunting before I had used them. But like all things, they can be conquered with knowledge, understanding and tenacity to keep trying until you figure it out. Good luck!

**Requests Documentation**

[requests.request() API documentation](https://requests.readthedocs.io/en/master/api/)

[requests.get() API documentation](https://2.python-requests.org/en/master/api/#requests.get)

[requests.post() API documentation](https://2.python-requests.org/en/master/api/#requests.post)

**Supplementary Reading**

[Google's HTTP Timing Explanation](https://developers.google.com/web/tools/chrome-devtools/network/reference#timing-explanation)

[List of Interesting "Unofficial" APIs](https://github.com/Rolstenhouse/unofficial-apis)

[Proxy servers](https://en.wikipedia.org/wiki/Proxy_server)

`<!-- wp:paragraph -->`{=html}

[Making 1 million requests with python-aiohttp](https://pawelmhm.github.io/asyncio/python/aiohttp/2016/04/22/asyncio-aiohttp.html)

`<!-- /wp:paragraph -->`{=html}
