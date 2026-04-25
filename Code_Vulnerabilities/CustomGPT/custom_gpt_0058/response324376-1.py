
import socket
import requests

# Force the socket to use IPv4
socket.setdefaultfamily(socket.AF_INET)

def send_post_request():
    try:
        response = requests.post('http://external-server-url.com/api', data={'key': 'value'})
        return response.json()
    except requests.exceptions.ConnectionError as e:
        print(f'Connection error: {e}')
