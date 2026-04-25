
import requests
import socket

def send_post_request(url, data):
    # Force IPv4
    with requests.Session() as session:
        session.mount('http://', requests.adapters.HTTPAdapter(
            max_retries=3,
            pool_connections=10,
            pool_maxsize=10
        ))
        # Force using IPv4
        socket.setdefaultfamily(socket.AF_INET)
        response = session.post(url, data=data)
        return response

# Example usage:
url = 'http://external-server.com/api'
data = {'key': 'value'}
try:
    response = send_post_request(url, data)
    print(response.status_code, response.text)
except requests.exceptions.RequestException as e:
    print(e)
