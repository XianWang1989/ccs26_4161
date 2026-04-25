
import requests
import socket

def send_post_request(url, data):
    socket.setdefaultfamily(socket.AF_INET)  # Ensure IPv4 is used
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # or response.text based on your needs
    except requests.ConnectionError as e:
        print(f"Connection error: {e}")
    except requests.HTTPError as e:
        print(f"HTTP error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
url = 'http://external-api.com/endpoint'
data = {'key': 'value'}
result = send_post_request(url, data)
if result:
    print(result)
