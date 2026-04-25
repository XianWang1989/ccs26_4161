
import requests
import socket

# Force IPv4
socket.setdefaulttimeout(10)  # Set a default timeout

# Example POST request
def send_post_request(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")

# Usage
url = "http://example.com/api"
data = {"key": "value"}
send_post_request(url, data)
