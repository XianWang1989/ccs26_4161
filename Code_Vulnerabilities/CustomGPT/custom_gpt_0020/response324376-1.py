
import requests
import socket

# Force the usage of IPv4
def make_post_request(url, data):
    try:
        # Set socket options to force IPv4
        socket.setdefaulttimeout(5)
        requests.get(url)  # Test if we can reach the URL

        response = requests.post(url, json=data, timeout=5)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except Exception as ex:
        print(f"General error: {ex}")

# Example usage:
url = "http://externalserver.com/api/resource"
data = {"key": "value"}

make_post_request(url, data)
