
import requests
import socket

def send_post_request(url, data):
    # Create a new socket and bind it to an IPv4 address
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Setting the custom socket to use the default timeout
    sock.settimeout(5)

    # Where to send the request
    response = requests.post(url, json=data, socket=sock)
    return response
