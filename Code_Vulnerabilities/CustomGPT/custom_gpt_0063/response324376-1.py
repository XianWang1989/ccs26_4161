
import requests
import socket

def send_post_request():
    url = 'http://external-server/api/'
    data = {'key': 'value'}

    # Set the socket family to avoid the address family error
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad status
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
