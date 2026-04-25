
import requests
import socket

def send_post_request(url, data):
    # Force the use of IPv4
    socket.setdefaultfamily(socket.AF_INET)

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Or response.text depending on your needs
    except requests.ConnectionError as e:
        print("Connection Error:", e)
    except Exception as e:
        print("An error occurred:", e)

# Example Usage
url = "http://example.com/api"
data = {"key": "value"}
result = send_post_request(url, data)
