
import requests
import socket

def send_post_request():
    url = "http://example.com/api/endpoint"
    data = {"key": "value"}

    # Ensure we force the use of IPv4
    old_socket = socket.socket
    socket.socket = lambda *args, **kwargs: old_socket(socket.AF_INET, *args, **kwargs)

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    finally:
        socket.socket = old_socket  # Restore original socket

# Call the function within your view
send_post_request()
