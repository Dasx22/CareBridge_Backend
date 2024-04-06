import requests
import json


    # post request using query parameters
# url = 'http://127.0.0.1:8000/orders'
# headers = {
#     'accept': 'application/json',
# }
# params = {
#     'product': 'laptop',
#     'units': '1'
# }

# response = requests.post(url, headers = headers, params = params)
# print(response.json())


    # post request using body of request
url = 'http://127.0.0.1:8000/orders_pydantic'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}
params = {
    'product': 'laptop',
    'units': '1'
}

response = requests.post(url, headers = headers, data = json.dumps(params))     # when passing anything in the body of the request pass it as a json object
print(response.json())