
import requests
import socket

# Ensure we're using IPv4
socket.setdefaulttimeout(10)

def send_post_request(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Process the JSON response if needed
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# Example usage
url = "http://external-server.com/api"
data = {"key": "value"}

# Send the POST request
send_post_request(url, data)
