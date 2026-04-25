
import requests
import socket

def make_request():
    try:
        # Force IPv4 connection
        sock = socket.create_connection(('external-server.com', 80))
        response = requests.post('http://external-server.com/api/', data={'key': 'value'}, socket=sock)
        print("Response:", response.content)
    except requests.ConnectionError as e:
        print("Connection failed:", e)

make_request()
