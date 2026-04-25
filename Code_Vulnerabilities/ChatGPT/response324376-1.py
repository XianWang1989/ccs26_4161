
import socket
import requests

def post_request_to_external_server(url, data):
    # Create a socket with IPv4
    socket.setdefaultfamily(socket.AF_INET)

    try:
        # Making a POST request
        response = requests.post(url, json=data)
        return response
    except requests.exceptions.ConnectionError as e:
        print(f'ConnectionError: {e}')

# Example usage
url = 'https://external-server.com/api/endpoint'
data = {'key': 'value'}
response = post_request_to_external_server(url, data)

if response:
    print('Response:', response.json())
