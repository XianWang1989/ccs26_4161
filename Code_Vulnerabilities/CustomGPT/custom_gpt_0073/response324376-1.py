
import requests
import socket

# Force IPv4
socket.setdefaultfamily(socket.AF_INET)

def send_post_request():
    url = 'http://example.com/api'  # Replace with your target URL
    data = {
        'key': 'value'
    }
    try:
        response = requests.post(url, data=data)
        print(response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

send_post_request()
