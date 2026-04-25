
import requests

url = 'http://127.0.0.1:8000/api/v1/images/'
data = {
    "name": "My family",
    "title": "Wassup",
    "gallery": "/api/v1/gallery/1/"
}

response = requests.post(url, json=data)

# Print the response from the server
print(response.json())
