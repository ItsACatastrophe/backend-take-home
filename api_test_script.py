import json
import requests

url = "http://127.0.0.1:5000"
endpoint = "/users/"
querystring = ""

post_body = {
    "": "",
}

response = requests.get(url=f"{url}{endpoint}{querystring}") #GET request
# response = requests.post(url=f"{url}{endpoint}{querystring}", json=json.dumps(post_body)) #POST request
# response = requests.delete(url=f"{url}{endpoint}{querystring}", json=json.dumps(post_body)) #DELETE request
print(response.json())