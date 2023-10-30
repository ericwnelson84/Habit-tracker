import requests
from datetime import datetime

USERNAME = 'your_username'
TOKEN = 'your_token'

pixela_endpoint = 'https://pixe.la/v1/users'

# token below is user defined for this API
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
# created user account below. Only need to call it at set up of course
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph created below
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
# graph_config = {
#     'id': 'graph1',
#     'name': 'Elliptical',
#     'unit': 'min',
#     'type': 'float',
#     'color': 'shibafu'
# }
# headers = {
#     'X-USER-TOKEN': TOKEN
# }
# # This method requires that we pass our token as a header ang not in the query string
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

headers = {
    'X-USER-TOKEN': TOKEN
}

today = datetime.now()


# .strftime() is used to format date for what API requests
pixel_data = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '30'
}

# graph_post_endpoint = f'{graph_endpoint}/graph1'
# response = requests.post(url=graph_post_endpoint, json=pixel_data, headers=headers)

new_pixel_data = {
    'quantity': '25'
}
# update with put request
# update_endpoint = f'{graph_endpoint}/graph1/{today.strftime("%Y%m%d")}'
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)

# delete method below

delete_endpoint = f'{graph_endpoint}/graph1/{today.strftime("%Y%m%d")}'
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)

