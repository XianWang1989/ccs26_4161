
import requests
import socket

# Force the usage of IPv4
socket.setdefaultfamily(socket.AF_INET)

def post_data(url, payload):
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print(f"Response: {response.status_code}, Data: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# Sending a sample POST request
url = 'http://example.com/api/endpoint'
data = {'key': 'value'}
post_data(url, data)
