
import requests
import socket

def send_post_request(url, data):
    # Force the use of IPv4
    original_socket = socket.socket
    socket.socket = lambda *args, **kwargs: original_socket(socket.AF_INET, *args[1:])

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raises an exception for HTTP errors
        return response.json()
    except requests.ConnectionError as e:
        print(f"ConnectionError: {e}")
    finally:
        socket.socket = original_socket  # Restore the original socket

# Example usage
url = "http://external-server.com/api"
data = {"key": "value"}
result = send_post_request(url, data)
print(result)
