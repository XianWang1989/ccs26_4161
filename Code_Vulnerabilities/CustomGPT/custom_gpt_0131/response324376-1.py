
import requests

url = 'http://example.com/api/endpoint'  # replace with your actual URL
data = {'key': 'value'}  # replace with your actual data
try:
    response = requests.post(url, json=data)
    print(response.status_code)
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error occurred: {e}")
