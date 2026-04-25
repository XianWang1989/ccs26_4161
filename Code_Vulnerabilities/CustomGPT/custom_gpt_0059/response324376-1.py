
import requests
import socket

# Force the use of IPv4
socket.setdefaulttimeout(10)

def send_post_request(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

# Example usage
url = "https://api.example.com/data"
data = {"key": "value"}
result = send_post_request(url, data)
print(result)
