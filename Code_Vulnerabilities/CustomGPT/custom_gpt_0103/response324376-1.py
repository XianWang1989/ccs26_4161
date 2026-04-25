
import requests

url = 'https://example.com/api'
data = {'key': 'value'}

try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # Raise an error for bad responses
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
