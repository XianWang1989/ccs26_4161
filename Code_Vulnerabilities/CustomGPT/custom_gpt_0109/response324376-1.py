
import requests
import socket

# Force the use of IPv4
socket.setdefaultfamily(socket.AF_INET)

def send_post_request(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raises an error for bad status
        return response.json()
    except requests.ConnectionError as e:
        print(f"Connection failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url = 'http://example.com/api/endpoint'
data = {'key': 'value'}
response = send_post_request(url, data)
print(response)
