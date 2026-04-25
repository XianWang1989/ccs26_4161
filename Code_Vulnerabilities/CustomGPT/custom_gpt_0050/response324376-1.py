
import requests
import socket

def send_post_request(url, data):
    # Optionally, set the address family
    socket.setdefaulttimeout(10)

    try:
        response = requests.post(url, json=data)
        return response.json()  # or response.text based on your needs
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error occurred: {e}")
        return None

# Example usage
data = {"key": "value"}
send_post_request("http://example.com/api", data)
