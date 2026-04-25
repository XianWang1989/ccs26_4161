
import requests
import socket

def send_post_request(url, data):
    # Force IPv4
    socket.setdefaultfamily(socket.AF_INET)

    response = requests.post(url, data=data)
    return response

# Example usage
url = 'http://external-server.com/api'
data = {'key': 'value'}
try:
    response = send_post_request(url, data)
    print(response.content)
except requests.ConnectionError as e:
    print("Error:", e)
