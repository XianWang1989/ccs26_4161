
import requests
import socket

# Force IPv4 for socket connections
socket.setdefaulttimeout(10)
socket.setdefaultfamily(socket.AF_INET)

# Your POST request function
def send_post_request(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Usage
url = "http://external.api/endpoint"
data = {'key': 'value'}
result = send_post_request(url, data)
print(result)
