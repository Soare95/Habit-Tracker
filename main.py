import requests
from datetime import datetime

USERNAME = "testpython195"
TOKEN = "sfa85s4f9a4s65c41a59wad"
GRAPH_ID = "graph1"
DATE_PIXEL = "20200616"

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create username
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_endpoint, json=user_params)

# Create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Minutes",
    "type": "int",
    "color": "shibafu"
}

# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Add a pixel to the graph
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

graph_pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you code today? ")
}

# response = requests.post(pixel_endpoint, json=graph_pixel, headers=headers)
# print(response.text)

# Update an existing pixel
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE_PIXEL}"

new_pixel_data = {
    "quantity": "100"
}

# response = requests.put(pixel_update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# Delete a pixel
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE_PIXEL}"

# response = requests.delete(pixel_delete_endpoint, headers=headers)
# print(response.text)
