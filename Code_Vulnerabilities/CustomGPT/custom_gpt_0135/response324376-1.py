
import requests
import socket

def send_post_request(url, data):
    try:
        # Create a new socket using the specified address family
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Use AF_INET for IPv4
        sock.connect(('your_server_address', your_port))  # Replace with server details

        # Sending POST request
        response = requests.post(url, json=data)

        if response.status_code == 200:
            print('Success:', response.json())
        else:
            print('Error:', response.status_code, response.text)

    except requests.ConnectionError as e:
        print('Connection Error:', e)

# Example usage
send_post_request('http://example.com/api', {'key': 'value'})
