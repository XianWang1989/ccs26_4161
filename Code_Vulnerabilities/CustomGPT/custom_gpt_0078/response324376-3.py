
import socket
import requests

# Force the usage of IPv4
socket.setdefaultfamily(socket.AF_INET)

def send_post_request(url, data):
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Process the JSON response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Usage
data = {'key': 'value'}
response = send_post_request('http://your_external_server.com/api/', data)
print(response)
