
import requests
import socket

# Ensure you are using IPv4
socket.setdefaulttimeout(10)  # Setting a default timeout

def send_post_request(url, data):
    try:
        response = requests.post(url, json=data, timeout=5)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
url = 'http://example.com/api/endpoint'
data = {'key': 'value'}

result = send_post_request(url, data)
print(result)
