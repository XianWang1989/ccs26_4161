
import requests

url = "http://example.com/api/endpoint"
data = {
    "key": "value"
}

# Use a session to enforce IPv4
session = requests.Session()
session.adapters.clear()  # Clear existing adapters

# Add a new adapter for IPv4
session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))

try:
    response = session.post(url, json=data)
    response.raise_for_status()  # Raise an error for bad responses
except requests.ConnectionError as e:
    print(f"Connection failed: {e}")
