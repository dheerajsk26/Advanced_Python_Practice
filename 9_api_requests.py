
#* API Requests in Python

# API stands for Application Programming Interface and allows different software applications to communicate with each other.
# A Python program sends an HTTP request to another system/API and receives a response, usually as JSON.
# Making API requests in Python is commonly done using the 'requests' library.
# You can send GET, POST, PUT, PATCH, DELETE requests to interact with web APIs.
# API requests typically involve sending HTTP requests to a server and handling the responses.
# Use cases
    # - Fetching data from web services
    # - Sending data to web services
    # - Interacting with RESTful APIs
    # - Automating tasks that involve web APIs

# Install (if not already installed): pip install requests


import requests

#* HTTP methods - what they're for
    # GET    - retrieve data, should not change anything on the server
    # POST   - create a new re source / submit data
    # PUT    - replace an existing resource entirely
    # PATCH  - partially update an existing resource
    # DELETE - remove a resource

#* Status codes - quick reference
    # 200 OK              - request succeeded
    # 201 Created         - resource was created (common after POST)
    # 204 No Content      - succeeded, nothing to return (common after DELETE)
    # 400 Bad Request     - client sent invalid data
    # 401 Unauthorized    - missing/invalid authentication
    # 403 Forbidden       - authenticated but not allowed
    # 404 Not Found       - resource doesn't exist
    # 429 Too Many Requests - rate limited
    # 500 Internal Server Error - something broke on the server

# We're using jsonplaceholder.typicode.com below - a free fake REST API meant for testing/learning. 
    # Requests to it are real network calls but nothing is actually persisted on their servers.

BASE_URL = "https://jsonplaceholder.typicode.com"


#* GET request - fetching data

# Always set a timeout so your script can't hang forever waiting on a
# server that never responds. Value is in seconds.
# Always wrap network calls in try/except - DNS failures, timeouts, and
# connection errors raise exceptions *before* you get a response object,
# so checking status_code alone isn't enough.
try:
    response = requests.get(f"{BASE_URL}/todos/1", timeout=5)
    response.raise_for_status()  # raises an exception for 4xx/5xx status codes
    data = response.json()       # parse the JSON response body into a dict/list
    print("GET result:", data)
except requests.exceptions.RequestException as e:
    print(f"GET request failed: {e}")


#* Query parameters
# Pass a dict via `params` instead of hand-building the URL string;
# requests handles the URL-encoding for you.
try:
    response = requests.get(
        f"{BASE_URL}/comments",
        params={"postId": 1},
        timeout=5,
    )
    response.raise_for_status()
    print(f"GET with params returned {len(response.json())} comments")
except requests.exceptions.RequestException as e:
    print(f"GET with params failed: {e}")


#* POST request - creating data
# Use `json=` (not `data=`) to send a JSON body - requests will
# automatically serialize the dict and set the Content-Type header.
try:
    new_post = {"title": "hello", "body": "world", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=new_post, timeout=5)
    response.raise_for_status()
    print("POST created:", response.json())
except requests.exceptions.RequestException as e:
    print(f"POST request failed: {e}")


#* PUT request - replacing a resource entirely
try:
    updated_post = {"id": 1, "title": "updated", "body": "new body", "userId": 1}
    response = requests.put(f"{BASE_URL}/posts/1", json=updated_post, timeout=5)
    response.raise_for_status()
    print("PUT result:", response.json())
except requests.exceptions.RequestException as e:
    print(f"PUT request failed: {e}")


#* PATCH request - partially updating a resource
try:
    response = requests.patch(f"{BASE_URL}/posts/1", json={"title": "patched title"}, timeout=5)
    response.raise_for_status()
    print("PATCH result:", response.json())
except requests.exceptions.RequestException as e:
    print(f"PATCH request failed: {e}")


#* DELETE request - removing a resource
try:
    response = requests.delete(f"{BASE_URL}/posts/1", timeout=5)
    response.raise_for_status()
    print(f"DELETE status: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"DELETE request failed: {e}")


#* Headers
# Many APIs require headers, e.g. for auth tokens or content negotiation.
headers = {
    "Content-Type": "application/json",
    # "Authorization": "Bearer <your_token_here>",
}
try:
    response = requests.get(f"{BASE_URL}/todos/2", headers=headers, timeout=5)
    response.raise_for_status()
    print("GET with headers:", response.json())
except requests.exceptions.RequestException as e:
    print(f"GET with headers failed: {e}")


#* Authentication
# Common patterns:
    # - API key in header:   headers={"Authorization": "Bearer <token>"}
    # - API key in query:    params={"api_key": "<key>"}
    # - Basic auth:          requests.get(url, auth=("username", "password"))


# Basic Authentication Example
from requests.auth import HTTPBasicAuth

response = requests.get(f"{BASE_URL}/todos/2", auth=HTTPBasicAuth("username", "password"), timeout=5)
response.raise_for_status()


#* Inspecting the response object
    # response.status_code  - int, e.g. 200
    # response.ok            - True if status_code < 400
    # response.headers       - dict of response headers
    # response.text          - raw response body as a string
    # response.json()        - parsed JSON body (raises if body isn't valid JSON)
    # response.raise_for_status() - raises requests.HTTPError if status is 4xx/5xx


#* Good practices
    # - Always set a timeout, otherwise a hung server can freeze your script.
    # - Always handle exceptions (requests.exceptions.RequestException and
    #   its subclasses: ConnectionError, Timeout, HTTPError, etc).
    # - Use response.raise_for_status() to fail fast on bad status codes
    #   instead of manually checking response.status_code == 200 everywhere.
    # - Use `json=` for sending JSON bodies, not `data=` (data= sends
    #   form-encoded content instead).
    # - Don't hardcode secrets/tokens in code - use environment variables.
    # - For repeated calls to the same host, use a requests.Session() to
    #   reuse the underlying TCP connection (better performance).
