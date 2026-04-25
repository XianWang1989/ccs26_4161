
import requests
import socket

# Force the socket to use IPv4
def send_post_request(url, data):
    # Create a socket connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Use the default connection by specifying the IP address format
    with requests.Session() as session:
        session.mount(url, requests.adapters.HTTPAdapter(sock=sock))
        response = session.post(url, json=data)

    return response

url = "http://external.server/endpoint"
data = {"key": "value"}

try:
    response = send_post_request(url, data)
    print("Response:", response.json())
except requests.exceptions.ConnectionError as e:
    print("Connection error:", e)
