
import requests

url = "http://<IPv4_address_of_external_server>/api/endpoint"  # Replace with the actual URL
data = {"key": "value"}  # Your request payload

try:
    response = requests.post(url, json=data)
    print("Success:", response.json())
except requests.exceptions.ConnectionError as e:
    print("Connection Error:", e)
