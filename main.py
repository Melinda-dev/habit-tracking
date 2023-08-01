import datetime
import requests
from api_key import *
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "melindasun"
GRAPHID = "graph1"
TODAY = datetime.datetime.today().strftime("%Y%m%d")

headers = {
    "X-USER-TOKEN":TOKEN,
}

# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
# print(type(response.text))


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPHID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)


value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
value_config = {
    "date": TODAY,
    "quantity": input("How many kilometers did you cycle today?"),
}
response = requests.post(url=value_endpoint, json=value_config, headers=headers)
print(response.text)


# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{TODAY}"
# update_config = {
#     "quantity" : "12",
#
# }
# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

#
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{TODAY}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)