The test script located at `/api_test_script.py` is meant to act as an alternative to `curl`ing requests in your terminal. It's not required but it can make the process a bit simpler! It does depend on the `requests` library but that's one of the dependencies of the project so it be installed with the rest. Make sure to run the script from your virtual environment!

To use it there are 3 variables you will need to edit: `endpoint`, `querystring`, and `post_body`. The contents of these variables should be relatively self explanatory so I'll mainly be providing examples to demonstrate it's usage.

There are also 3 request methods at the bottom of the script, 2 of which are commented out. Simply uncomment whichever of these you'd like to utilize.

### Examples
I'm only going to include the parts of the script that should be edited in the examples. If it's not included it probably doesn't need to be touched.

#### I'd like to create a user named Annette 
```python
endpoint = "/users/"
querystring = ""

post_body = {
    "username": "Annette",
}

# response = requests.get(url=f"{url}{endpoint}{querystring}") #GET request
response = requests.post(url=f"{url}{endpoint}{querystring}", json=json.dumps(post_body)) #POST request
# response = requests.delete(url=f"{url}{endpoint}{querystring}", json=json.dumps(post_body)) #DELETE request
```

#### I'd like to start a chat with a user named Leon
```python
endpoint = "/"
querystring = "?username=Annette"

post_body = {
    "username": "Leon",
}

# response = requests.get(url=f"{url}{endpoint}{querystring}") #GET request
response = requests.post(url=f"{url}{endpoint}{querystring}", json=json.dumps(post_body)) #POST request
# response = requests.delete(url=f"{url}{endpoint}{querystring}", json=json.dumps(post_body)) #DELETE request
```

#### I'd like to see all of my messages within the past 30 days wiith Leon
If a time given is >30 days ago, 30 days is used instead.
```python
endpoint = "/1/"
querystring = "?username=Annette&after=08-01-2021"

post_body = {
    "": "",
}

response = requests.get(url=f"{url}{endpoint}{querystring}") #GET request
# response = requests.post(url=f"{url}{endpoint}{querystring}", json=json.dumps(post_body)) #POST request
# response = requests.delete(url=f"{url}{endpoint}{querystring}", json=json.dumps(post_body)) #DELETE request
```

#### I'd like to see a list of users
```python
endpoint = "/users/"
querystring = ""

post_body = {
    "": "",
}

response = requests.get(url=f"{url}{endpoint}{querystring}") #GET request
# response = requests.post(url=f"{url}{endpoint}{querystring}", json=json.dumps(post_body)) #POST request
# response = requests.delete(url=f"{url}{endpoint}{querystring}", json=json.dumps(post_body)) #DELETE request
```

### I'd like to delete my chat with Leon
```python
endpoint = "/"
querystring = ""

post_body = {
    "id": "1",
}

# response = requests.get(url=f"{url}{endpoint}{querystring}") #GET request
# response = requests.post(url=f"{url}{endpoint}{querystring}", json=json.dumps(post_body)) #POST request
response = requests.delete(url=f"{url}{endpoint}{querystring}", json=json.dumps(post_body)) #DELETE request
```