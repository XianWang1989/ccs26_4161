
import requests
import socket

# Force IPv4
socket.setdefaulttimeout(10)
socket_family = socket.AF_INET

def send_post_request(url, data):
    # Use the requests library to send a POST request
    try:
        response = requests.post(url, json=data, timeout=5)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.ConnectionError as e:
        print("Connection Error:", e)
    except requests.exceptions.Timeout as e:
        print("Request timed out:", e)
    except Exception as e:
        print("An error occurred:", e)

# Example usage
url = "http://external-server/api/"
data = {"key": "value"}
result = send_post_request(url, data)
print(result)
