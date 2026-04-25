
import socket
import requests

# Force IPv4
socket.setdefaulttimeout(10)  # Set a timeout if needed

def post_request(url, data):
    # Make sure to use 'http' or 'https' as needed
    response = requests.post(url, json=data)
    return response.json()

# Example usage
url = "http://external-server.com/api"
data = {"key": "value"}

try:
    result = post_request(url, data)
    print("Response:", result)
except requests.ConnectionError as e:
    print("Error:", e)
