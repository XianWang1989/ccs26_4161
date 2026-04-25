
import requests

# Replace with the actual IPv4 address of the external service
url = 'http://192.0.2.0/api/endpoint'  # Example IPv4 address
data = {'key': 'value'}

try:
    response = requests.post(url, data=data)
    response.raise_for_status()  # Raise an error for 4xx/5xx responses
except requests.exceptions.ConnectionError as e:
    print(f"Connection failed: {e}")
