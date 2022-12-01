import requests

# api-endpoint
URL = "http://127.0.0.1:5000/predict"

# defining a params dict for the parameters to be sent to the API
JSON = "{\"X\":[[0.341549,1710000,2320,347648425,326.0]]}"

# sending get request and saving the response as response object
r = requests.post(url = URL, json=JSON)

if not r.ok:
    print("Error", r.status_code)

# extracting data in json format
data = r.json()

print(data)
