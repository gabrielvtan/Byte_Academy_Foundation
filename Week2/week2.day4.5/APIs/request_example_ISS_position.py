import requests
import json
from pprint import pprint


# Make the same request we did earlier, but with the coordinates of San Francisco instead.
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a python object.  Verify that it's a dictionary.
data = response.json()
print(type(data))
pprint(data)

# Headers is a dictionary
print(response.headers)

# Get the content-type from the dictionary.
print(response.headers["content-type"])

# Get the response from the API endpoint.
response1 = requests.get("http://api.open-notify.org/astros.json")
data1 = response1.json()

# 9 people are currently in space.
print(data1["number"])
pprint(data1)
 