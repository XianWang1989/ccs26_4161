
import requests
import socket

# Force the use of IPv4
def send_post_request(url, data):
    with requests.Session() as session:
        # Create a custom socket
        session.mount('http://', requests.adapters.HTTPAdapter())
        session.mount('https://', requests.adapters.HTTPAdapter())

        # Use `socket.AF_INET` for IPv4
        socket.setdefaultfamily(socket.AF_INET)

        response = session.post(url, data=data)
        return response

# Example usage
url = "http://external.server/api"
data = {"key": "value"}
response = send_post_request(url, data)
print(response.status_code, response.text)
